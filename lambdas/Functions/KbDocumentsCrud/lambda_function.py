"""KbDocumentsCrud Lambda — list, create, get, delete KB documents for a project.

Routes:
  GET    /projects/{projectId}/kb-documents              → list_documents
  POST   /projects/{projectId}/kb-documents              → create_document
  GET    /projects/{projectId}/kb-documents/{documentId}  → get_document
  DELETE /projects/{projectId}/kb-documents/{documentId}  → delete_document
  POST   /projects/{projectId}/kb-documents/{documentId}/replace → replace_document
"""

import json
import os
import uuid
from datetime import datetime, timezone
from math import ceil

import boto3
from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Key

from custom_exceptions import BadRequestError, NotFoundError
from response_utils import createResponse

logger = Logger()
tracer = Tracer()

KB_DOCUMENTS_TABLE_NAME = os.environ.get("KB_DOCUMENTS_TABLE_NAME", "")
KB_BUCKET_NAME = os.environ.get("KB_BUCKET_NAME", "")

dynamodb = boto3.resource("dynamodb")
documents_table = dynamodb.Table(KB_DOCUMENTS_TABLE_NAME)
s3_client = boto3.client("s3")

REQUIRED_CREATE_FIELDS = ["file_name"]
PRESIGNED_URL_EXPIRY = 900  # 15 minutes


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    if body is None:
        body = "{}"
    try:
        return json.loads(body) if isinstance(body, str) else body
    except (json.JSONDecodeError, TypeError):
        return {}


def _validate_required(data: dict, fields: list) -> None:
    missing = [f for f in fields if not data.get(f)]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


def _generate_presigned_url(s3_key: str, method: str = "put_object") -> str:
    file_ext = s3_key.rsplit(".", 1)[-1].lower() if "." in s3_key else ""
    content_type = {
        "pdf": "application/pdf",
        "md": "text/markdown",
        "txt": "text/plain",
    }.get(file_ext, "application/octet-stream")
    params = {"Bucket": KB_BUCKET_NAME, "Key": s3_key, "ContentType": content_type}
    return s3_client.generate_presigned_url(
        method,
        Params=params,
        ExpiresIn=PRESIGNED_URL_EXPIRY,
    )


def list_documents(event: dict) -> dict:
    """List KB documents for a project."""
    project_id = event.get("pathParameters", {}).get("projectId", "")
    params = event.get("queryStringParameters") or {}

    try:
        page = max(1, int(params.get("page", 1)))
    except (ValueError, TypeError):
        page = 1
    try:
        limit = min(100, max(1, int(params.get("limit", 50))))
    except (ValueError, TypeError):
        limit = 50

    resp = documents_table.query(
        IndexName="project-index",
        KeyConditionExpression=Key("project_id").eq(project_id),
    )
    items = resp.get("Items", [])
    items.sort(key=lambda x: x.get("created_at", ""), reverse=True)
    total = len(items)
    total_pages = ceil(total / limit) if total > 0 else 1

    start = (page - 1) * limit
    page_items = items[start : start + limit]

    return createResponse(200, "KB documents retrieved", {
        "documents": page_items,
        "count": len(page_items),
        "total": total,
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
    })


def get_document(event: dict) -> dict:
    """Get a single KB document by ID."""
    document_id = event.get("pathParameters", {}).get("documentId", "")
    resp = documents_table.get_item(Key={"document_id": document_id})
    item = resp.get("Item")
    if not item:
        raise NotFoundError("Document not found")
    return createResponse(200, "Document retrieved", item)


def create_document(event: dict) -> dict:
    """Create a KB document record and return a pre-signed upload URL."""
    project_id = event.get("pathParameters", {}).get("projectId", "")
    data = _parse_body(event)
    _validate_required(data, REQUIRED_CREATE_FIELDS)

    now = datetime.now(timezone.utc).isoformat()
    document_id = str(uuid.uuid4())
    file_name = data["file_name"]
    file_type = file_name.rsplit(".", 1)[-1].lower() if "." in file_name else ""
    s3_key = f"{project_id}/{file_name}"

    item = {
        "document_id": document_id,
        "project_id": project_id,
        "file_name": file_name,
        "description": data.get("description", ""),
        "s3_key": s3_key,
        "file_type": file_type,
        "status": "pending",
        "created_at": now,
        "updated_at": now,
    }

    documents_table.put_item(Item=item)
    upload_url = _generate_presigned_url(s3_key)
    content_type = {
        "pdf": "application/pdf",
        "md": "text/markdown",
        "txt": "text/plain",
    }.get(file_type, "application/octet-stream")

    return createResponse(200, "Document created. Upload file using the pre-signed URL.", {
        "document": item,
        "upload_url": upload_url,
        "content_type": content_type,
    })


def delete_document(event: dict) -> dict:
    """Delete a KB document and its S3 object."""
    document_id = event.get("pathParameters", {}).get("documentId", "")

    resp = documents_table.get_item(Key={"document_id": document_id})
    item = resp.get("Item")
    if not item:
        raise NotFoundError("Document not found")

    s3_key = item.get("s3_key", "")
    documents_table.delete_item(Key={"document_id": document_id})

    if s3_key:
        try:
            s3_client.delete_object(Bucket=KB_BUCKET_NAME, Key=s3_key)
        except Exception:
            logger.warning("Failed to delete S3 object", extra={"s3_key": s3_key})

    return createResponse(200, "Document deleted")


def replace_document(event: dict) -> dict:
    """Replace the file for an existing KB document."""
    document_id = event.get("pathParameters", {}).get("documentId", "")

    resp = documents_table.get_item(Key={"document_id": document_id})
    item = resp.get("Item")
    if not item:
        raise NotFoundError("Document not found")

    s3_key = item.get("s3_key", "")
    now = datetime.now(timezone.utc).isoformat()

    documents_table.update_item(
        Key={"document_id": document_id},
        UpdateExpression="SET #status = :status, updated_at = :updated_at",
        ExpressionAttributeNames={"#status": "status"},
        ExpressionAttributeValues={":status": "pending", ":updated_at": now},
    )

    upload_url = _generate_presigned_url(s3_key)
    file_type = item.get("file_type", "")
    content_type = {
        "pdf": "application/pdf",
        "md": "text/markdown",
        "txt": "text/plain",
    }.get(file_type, "application/octet-stream")
    return createResponse(200, "Upload replacement file using the pre-signed URL.", {
        "document_id": document_id,
        "upload_url": upload_url,
        "content_type": content_type,
    })


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        method = event.get("httpMethod", "")
        resource = event.get("resource", "")

        if resource == "/projects/{projectId}/kb-documents" and method == "GET":
            return list_documents(event)
        elif resource == "/projects/{projectId}/kb-documents" and method == "POST":
            return create_document(event)
        elif resource == "/projects/{projectId}/kb-documents/{documentId}" and method == "GET":
            return get_document(event)
        elif resource == "/projects/{projectId}/kb-documents/{documentId}" and method == "DELETE":
            return delete_document(event)
        elif resource == "/projects/{projectId}/kb-documents/{documentId}/replace" and method == "POST":
            return replace_document(event)
        else:
            raise BadRequestError(f"Unsupported route: {method} {resource}")
    except BadRequestError as e:
        logger.warning("Bad request", extra={"error": str(e)})
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning("Not found", extra={"error": str(e)})
        return createResponse(404, str(e))
    except Exception:
        logger.exception("Internal server error")
        return createResponse(500, "Internal server error")
