"""
Ingestion Lambda handler.

Triggered by S3 events when a .pdf file is uploaded to the knowledge base
bucket. Downloads the PDF, extracts text with PyPDF2, chunks the text,
generates embeddings via Bedrock Titan in us-east-1, and indexes vectors
into the OpenSearch ``knowledge-vectors`` index.
"""

import json
import os
import time
from io import BytesIO

import boto3
from aws_lambda_powertools import Logger, Tracer
from opensearchpy import OpenSearch, RequestsHttpConnection
from PyPDF2 import PdfReader
from requests_aws4auth import AWS4Auth

logger = Logger()
tracer = Tracer()

OPENSEARCH_ENDPOINT = os.environ.get("OPENSEARCH_ENDPOINT", "")
INDEX_NAME = os.environ.get("INDEX_NAME", "knowledge-vectors")
PROJECT_ID = os.environ.get("PROJECT_ID", "default-project")
BEDROCK_REGION = os.environ.get("BEDROCK_REGION", "us-east-1")
KB_DOCUMENTS_TABLE_NAME = os.environ.get("KB_DOCUMENTS_TABLE_NAME", "")

MAX_RETRIES = 3
INITIAL_BACKOFF = 1  # seconds

# TODO(pending-other-developer): Per-project S3 bucket routing depends on
# the Projects table CRUD being completed. Once projects have their own S3
# buckets, the S3 event notifications should be configured per-bucket.
# Until then, files are expected in the shared KB bucket with the key
# format: {project_id}/{filename}.pdf


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------


def _extract_project_id(key: str) -> str:
    """Extract project_id from S3 key prefix.

    Expected key format: ``{project_id}/{filename}.pdf``
    Falls back to the ``PROJECT_ID`` env var when no prefix exists.
    """
    parts = key.split("/")
    if len(parts) > 1 and parts[0]:
        return parts[0]
    return PROJECT_ID


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list:
    """Split *text* into overlapping chunks.

    Returns a list of strings where each chunk has at most *chunk_size*
    characters and consecutive chunks share *overlap* characters.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


def _get_opensearch_client() -> OpenSearch:
    """Build an OpenSearch client authenticated with IAM SigV4."""
    credentials = boto3.Session().get_credentials()
    region = os.environ.get("AWS_REGION", "ap-southeast-1")
    awsauth = AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        region,
        "es",
        session_token=credentials.token,
    )
    return OpenSearch(
        hosts=[{"host": OPENSEARCH_ENDPOINT, "port": 443}],
        http_auth=awsauth,
        use_ssl=True,
        verify_certs=True,
        connection_class=RequestsHttpConnection,
    )


def _retry_with_backoff(func, *args, **kwargs):
    """Call *func* with up to MAX_RETRIES retries and exponential backoff."""
    last_exc = None
    for attempt in range(MAX_RETRIES):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            last_exc = exc
            wait = INITIAL_BACKOFF * (2 ** attempt)
            logger.warning(
                "Retry attempt failed",
                extra={
                    "attempt": attempt + 1,
                    "max_retries": MAX_RETRIES,
                    "error": str(exc),
                    "backoff_seconds": wait,
                },
            )
            time.sleep(wait)
    raise last_exc


def ensure_index_exists(client: OpenSearch) -> None:
    """Create the knowledge-vectors index if it does not already exist."""
    if client.indices.exists(index=INDEX_NAME):
        return

    index_body = {
        "settings": {"index": {"knn": True}},
        "mappings": {
            "properties": {
                "embedding": {
                    "type": "knn_vector",
                    "dimension": 1024,
                    "method": {
                        "name": "hnsw",
                        "space_type": "cosinesimil",
                        "engine": "nmslib",
                    },
                },
                "text": {"type": "text"},
                "project_id": {"type": "keyword"},
                "doc_type": {"type": "keyword"},
                "agent_id": {"type": "keyword"},
                "source_file": {"type": "keyword"},
                "chunk_index": {"type": "integer"},
            }
        },
    }
    client.indices.create(index=INDEX_NAME, body=index_body)
    logger.info("Created index", extra={"index": INDEX_NAME})


@tracer.capture_method
def _generate_embedding(bedrock_client, text_chunk: str) -> list:
    """Call Titan Embeddings V2 to generate a 1024-dim embedding vector."""
    payload = json.dumps(
        {"inputText": text_chunk, "dimensions": 1024, "normalize": True}
    )

    def _invoke():
        response = bedrock_client.invoke_model(
            modelId="amazon.titan-embed-text-v2:0",
            contentType="application/json",
            accept="application/json",
            body=payload,
        )
        body = json.loads(response["body"].read())
        return body["embedding"]

    return _retry_with_backoff(_invoke)


@tracer.capture_method
def _index_document(client: OpenSearch, document: dict) -> None:
    """Index a single vector document into OpenSearch with retry."""

    def _do_index():
        client.index(index=INDEX_NAME, body=document)

    _retry_with_backoff(_do_index)


@tracer.capture_method
def _extract_text_from_file(s3_client, bucket: str, key: str) -> str:
    """Extract text from a file based on its extension.

    Supports .pdf (via PyPDF2), .md and .txt (raw UTF-8), and .docx (via python-docx).
    """
    response = s3_client.get_object(Bucket=bucket, Key=key)
    file_bytes = response["Body"].read()
    key_lower = key.lower()

    if key_lower.endswith(".md") or key_lower.endswith(".txt"):
        return file_bytes.decode("utf-8")

    if key_lower.endswith(".docx"):
        from docx import Document
        doc = Document(BytesIO(file_bytes))
        return "\n".join(p.text for p in doc.paragraphs if p.text.strip())

    # Default: treat as PDF
    reader = PdfReader(BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text


def _determine_doc_type(key: str) -> str:
    """Determine the doc_type based on the S3 key path.

    Files under a ``/summaries/`` path segment are ``meeting_summary``.
    All other files are ``user_upload``.
    """
    if "/summaries/" in key:
        return "meeting_summary"
    return "user_upload"


def _update_kb_document_status(s3_key: str, status: str) -> None:
    """Update the KbDocuments table status for a document matching this S3 key."""
    if not KB_DOCUMENTS_TABLE_NAME:
        return
    try:
        from datetime import datetime, timezone
        from boto3.dynamodb.conditions import Key as DDBKey, Attr

        project_id = _extract_project_id(s3_key)
        file_name = s3_key.split("/")[-1]

        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(KB_DOCUMENTS_TABLE_NAME)
        resp = table.query(
            IndexName="project-index",
            KeyConditionExpression=DDBKey("project_id").eq(project_id),
            FilterExpression=Attr("file_name").eq(file_name),
        )
        items = resp.get("Items", [])
        if items:
            doc_id = items[0]["document_id"]
            now = datetime.now(timezone.utc).isoformat()
            table.update_item(
                Key={"document_id": doc_id},
                UpdateExpression="SET #status = :s, updated_at = :u",
                ExpressionAttributeNames={"#status": "status"},
                ExpressionAttributeValues={":s": status, ":u": now},
            )
            logger.info("Updated KB document status", extra={"document_id": doc_id, "status": status})
    except Exception as exc:
        logger.warning("Failed to update KB document status", extra={"s3_key": s3_key, "error": str(exc)})


# ------------------------------------------------------------------
# Handler
# ------------------------------------------------------------------


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """Process S3 event: extract PDF text, embed, and index."""
    s3_client = boto3.client("s3")
    bedrock_client = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)
    os_client = _get_opensearch_client()

    ensure_index_exists(os_client)

    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        logger.info("Processing S3 object", extra={"bucket": bucket, "key": key})

        try:
            text = _extract_text_from_file(s3_client, bucket, key)

            if not text.strip():
                logger.warning("No text extracted", extra={"key": key})
                continue

            chunks = chunk_text(text)
            source_file = key.split("/")[-1]
            project_id = _extract_project_id(key)
            doc_type = _determine_doc_type(key)

            # For meeting summaries, look up the readable name from KbDocuments
            if "/summaries/" in key and KB_DOCUMENTS_TABLE_NAME:
                try:
                    from boto3.dynamodb.conditions import Attr
                    kb_table = boto3.resource("dynamodb").Table(KB_DOCUMENTS_TABLE_NAME)
                    s3_key = key
                    kb_resp = kb_table.scan(
                        FilterExpression=Attr("s3_key").eq(s3_key),
                        ProjectionExpression="file_name",
                        Limit=1,
                    )
                    kb_items = kb_resp.get("Items", [])
                    if kb_items and kb_items[0].get("file_name"):
                        raw_name = kb_items[0]["file_name"]
                        clean = raw_name.replace("Summary - ", "").replace(".md", "").strip()
                        slug = clean.lower().replace(" ", "-").replace("—", "-").replace("--", "-")
                        source_file = f"{slug}-summary.md"
                except Exception:
                    source_file = "meeting-summary.md"

            for idx, chunk in enumerate(chunks):
                embedding = _generate_embedding(bedrock_client, chunk)
                document = {
                    "embedding": embedding,
                    "text": chunk,
                    "project_id": project_id,
                    "doc_type": doc_type,
                    "source_file": source_file,
                    "chunk_index": idx,
                }
                _index_document(os_client, document)

            logger.info(
                "Indexed chunks",
                extra={"chunk_count": len(chunks), "key": key, "index": INDEX_NAME},
            )

            # Update KB document status to active if tracked in DynamoDB
            _update_kb_document_status(key, "active")

        except Exception:
            logger.exception("Failed to process S3 object", extra={"bucket": bucket, "key": key})
            tracer.put_annotation("error", "ingestion_failed")
            raise

    return {"statusCode": 200, "body": "Ingestion complete"}
