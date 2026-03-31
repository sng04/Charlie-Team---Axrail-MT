"""
FileDownload Lambda Function

Generates pre-signed S3 download URLs for KB documents, skills, and summaries.

Routes:
  GET /files/download?bucket={bucket}&key={s3_key}
"""

import os

import boto3
from aws_lambda_powertools import Logger, Tracer

from response_utils import createResponse
from custom_exceptions import BadRequestError

logger = Logger()
tracer = Tracer()

s3_client = boto3.client("s3")

KB_BUCKET = os.environ.get("KB_BUCKET_NAME", "")
SKILLS_BUCKET = os.environ.get("SKILLS_BUCKET_NAME", "")
PRESIGNED_URL_EXPIRY = 900  # 15 minutes


def _get_allowed_buckets() -> set:
    """Build allowed buckets set from env vars at call time (not module load)."""
    buckets = set()
    kb = os.environ.get("KB_BUCKET_NAME", "")
    skills = os.environ.get("SKILLS_BUCKET_NAME", "")
    if kb:
        buckets.add(kb)
    if skills:
        buckets.add(skills)
    return buckets


def _get_content_type(key: str) -> str:
    ext = key.rsplit(".", 1)[-1].lower() if "." in key else ""
    return {
        "pdf": "application/pdf",
        "md": "text/markdown",
        "txt": "text/plain",
        "json": "application/json",
        "csv": "text/csv",
        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    }.get(ext, "application/octet-stream")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        qs = event.get("queryStringParameters") or {}
        s3_key = qs.get("key", "").strip()
        bucket = qs.get("bucket", KB_BUCKET).strip()

        if not s3_key:
            raise BadRequestError("Missing required query parameter: key")

        if bucket not in _get_allowed_buckets():
            raise BadRequestError(f"Bucket not allowed: {bucket}")

        # Verify the object exists
        try:
            s3_client.head_object(Bucket=bucket, Key=s3_key)
        except s3_client.exceptions.NoSuchKey:
            return createResponse(404, "File not found")
        except Exception:
            return createResponse(404, "File not found")

        # Generate presigned download URL
        filename = s3_key.split("/")[-1]
        url = s3_client.generate_presigned_url(
            "get_object",
            Params={
                "Bucket": bucket,
                "Key": s3_key,
                "ResponseContentType": _get_content_type(s3_key),
                "ResponseContentDisposition": f'inline; filename="{filename}"',
            },
            ExpiresIn=PRESIGNED_URL_EXPIRY,
        )

        return createResponse(200, "Download URL generated", {
            "download_url": url,
            "file_name": filename,
            "expires_in": PRESIGNED_URL_EXPIRY,
        })
    except BadRequestError as e:
        return createResponse(400, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        return createResponse(500, "Internal server error")
