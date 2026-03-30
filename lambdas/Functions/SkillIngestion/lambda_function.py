"""
Skill Ingestion Lambda handler.

Triggered by S3 OBJECT_CREATED events on the Skills Bucket. Extracts text
from skill documents (.pdf, .md), chunks, embeds via Bedrock Titan, and
indexes vectors into the knowledge-vectors OpenSearch index with
doc_type="agent_skill" and the associated agent_id.
"""

import json
import os
import time
from datetime import datetime, timezone
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
BEDROCK_REGION = os.environ.get("BEDROCK_REGION", "us-east-1")
SKILLS_TABLE_NAME = os.environ.get("SKILLS_TABLE_NAME", "")

MAX_RETRIES = 3
INITIAL_BACKOFF = 1  # seconds


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------


def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list:
    """Split *text* into overlapping chunks."""
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


def _parse_skill_key(key: str) -> tuple:
    """Parse skill_id and filename from S3 key.

    Expected format: {skill_id}/{filename}
    """
    parts = key.split("/", 1)
    if len(parts) < 2:
        raise ValueError(f"Invalid skill S3 key format: {key}")
    return parts[0], parts[1]


def _update_skill_status(skill_id: str, status: str) -> None:
    """Update the skill record status in SkillsTable."""
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(SKILLS_TABLE_NAME)
    now = datetime.now(timezone.utc).isoformat()
    table.update_item(
        Key={"skill_id": skill_id},
        UpdateExpression="SET #status = :status, updated_at = :ts",
        ExpressionAttributeNames={"#status": "status"},
        ExpressionAttributeValues={":status": status, ":ts": now},
    )
    logger.info("Updated skill status", extra={"skill_id": skill_id, "status": status})


# ------------------------------------------------------------------
# Handler
# ------------------------------------------------------------------


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """Process S3 event: extract skill text, embed, and index."""
    s3_client = boto3.client("s3")
    bedrock_client = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)
    os_client = _get_opensearch_client()

    for record in event.get("Records", []):
        bucket = record["s3"]["bucket"]["name"]
        key = record["s3"]["object"]["key"]
        logger.info("Processing skill upload", extra={"bucket": bucket, "key": key})

        try:
            skill_id, filename = _parse_skill_key(key)
        except ValueError:
            logger.error("Invalid S3 key format", extra={"key": key})
            continue

        try:
            text = _extract_text_from_file(s3_client, bucket, key)

            if not text.strip():
                logger.warning("No text extracted", extra={"key": key})
                _update_skill_status(skill_id, "failed")
                continue

            chunks = chunk_text(text)

            for idx, chunk in enumerate(chunks):
                embedding = _generate_embedding(bedrock_client, chunk)
                document = {
                    "embedding": embedding,
                    "text": chunk,
                    "skill_id": skill_id,
                    "doc_type": "agent_skill",
                    "source_file": filename,
                    "chunk_index": idx,
                }
                _index_document(os_client, document)

            _update_skill_status(skill_id, "active")
            logger.info(
                "Skill ingestion complete",
                extra={"skill_id": skill_id, "chunks": len(chunks)},
            )

        except Exception:
            logger.exception("Skill ingestion failed", extra={"key": key})
            tracer.put_annotation("error", "skill_ingestion_failed")
            try:
                _update_skill_status(skill_id, "failed")
            except Exception:
                logger.exception("Failed to update skill status to failed")
            raise

    return {"statusCode": 200, "body": "Skill ingestion complete"}
