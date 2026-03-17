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

    Supports .pdf (via PyPDF2) and .md (raw UTF-8 text).
    """
    response = s3_client.get_object(Bucket=bucket, Key=key)
    file_bytes = response["Body"].read()

    if key.lower().endswith(".md"):
        return file_bytes.decode("utf-8")

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

        except Exception:
            logger.exception("Failed to process S3 object", extra={"bucket": bucket, "key": key})
            raise

    return {"statusCode": 200, "body": "Ingestion complete"}
