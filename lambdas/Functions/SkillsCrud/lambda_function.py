"""Skills CRUD Lambda Function.

Routes HTTP methods for the /skills resource, providing list, get, create,
update, and delete operations against the SkillsTable DynamoDB table.
"""

import json
import os
import uuid
from datetime import datetime, timezone
from math import ceil

import boto3
from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Attr, Key

from custom_exceptions import BadRequestError, NotFoundError
from response_utils import createResponse

logger = Logger()
tracer = Tracer()

SKILLS_TABLE_NAME = os.environ.get("SKILLS_TABLE_NAME", "")
AGENTS_TABLE_NAME = os.environ.get("AGENTS_TABLE_NAME", "")
SKILLS_BUCKET_NAME = os.environ.get("SKILLS_BUCKET_NAME", "")
AGENT_SKILLS_TABLE_NAME = os.environ.get("AGENT_SKILLS_TABLE_NAME", "")

dynamodb = boto3.resource("dynamodb")
skills_table = dynamodb.Table(SKILLS_TABLE_NAME)
agents_table = dynamodb.Table(AGENTS_TABLE_NAME)
agent_skills_table = dynamodb.Table(AGENT_SKILLS_TABLE_NAME)
s3_client = boto3.client("s3")

REQUIRED_CREATE_FIELDS = ["skill_name", "file_name"]
UPDATABLE_FIELDS = ["skill_name", "description"]
PRESIGNED_URL_EXPIRY = 900  # 15 minutes


def _parse_body(event: dict) -> dict:
    """Defensively parse the request body from the event."""
    body = event.get("body", "{}")
    if body is None:
        body = "{}"
    try:
        return json.loads(body) if isinstance(body, str) else body
    except (json.JSONDecodeError, TypeError):
        return {}


def _validate_required(data: dict, fields: list) -> None:
    """Raise BadRequestError if any required fields are missing."""
    missing = [f for f in fields if not data.get(f)]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


def _generate_presigned_url(s3_key: str) -> str:
    """Generate a pre-signed PUT URL for the given S3 key."""
    return s3_client.generate_presigned_url(
        "put_object",
        Params={"Bucket": SKILLS_BUCKET_NAME, "Key": s3_key},
        ExpiresIn=PRESIGNED_URL_EXPIRY,
    )


def list_skills(event: dict) -> dict:
    """List skills, optionally filtered by agent_id."""
    params = event.get("queryStringParameters") or {}
    agent_id = params.get("agent_id")

    try:
        page = max(1, int(params.get("page", 1)))
    except (ValueError, TypeError):
        page = 1
    try:
        limit = min(100, max(1, int(params.get("limit", 50))))
    except (ValueError, TypeError):
        limit = 50

    if agent_id:
        # Query junction table to get skill_ids for this agent
        junction_resp = agent_skills_table.query(
            KeyConditionExpression=Key("agent_id").eq(agent_id),
        )
        skill_ids = [item["skill_id"] for item in junction_resp.get("Items", [])]
        if not skill_ids:
            return createResponse(
                200,
                "Skills retrieved",
                {"skills": [], "count": 0, "page": page, "limit": limit},
            )
        # Batch-get full skill records
        items = []
        for sid in skill_ids:
            skill_resp = skills_table.get_item(Key={"skill_id": sid})
            skill_item = skill_resp.get("Item")
            if skill_item:
                items.append(skill_item)
    else:
        resp = skills_table.scan()
        items = resp.get("Items", [])
    total = len(items)
    total_pages = ceil(total / limit) if total > 0 else 1

    start = (page - 1) * limit
    page_items = items[start : start + limit]

    return createResponse(
        200,
        "Skills retrieved",
        {
            "skills": page_items,
            "count": len(page_items),
            "page": page,
            "limit": limit,
        },
    )


def get_skill(event: dict) -> dict:
    """Get a single skill by skillId."""
    skill_id = event.get("pathParameters", {}).get("skillId", "")
    resp = skills_table.get_item(Key={"skill_id": skill_id})
    item = resp.get("Item")
    if not item:
        raise NotFoundError("Skill not found")
    return createResponse(200, "Skill retrieved successfully", item)


def create_skill(event: dict) -> dict:
    """Create a skill record and return a pre-signed upload URL."""
    data = _parse_body(event)
    _validate_required(data, REQUIRED_CREATE_FIELDS)

    # Check for duplicate name via GSI query
    existing = skills_table.query(
        IndexName="name-index",
        KeyConditionExpression=Key("skill_name").eq(data["skill_name"]),
    )
    if existing.get("Items"):
        return createResponse(409, "A skill with this name already exists")

    # Idempotency check
    idempotency_token = data.get("idempotencyToken")
    if idempotency_token:
        resp = skills_table.scan(
            FilterExpression=Attr("idempotencyToken").eq(idempotency_token),
            Limit=1,
        )
        if resp.get("Items"):
            return createResponse(200, "Skill already exists", resp["Items"][0])

    now = datetime.now(timezone.utc).isoformat()
    skill_id = str(uuid.uuid4())
    file_name = data["file_name"]
    file_type = file_name.rsplit(".", 1)[-1].lower() if "." in file_name else ""
    s3_key = f"{skill_id}/{file_name}"

    item = {
        "skill_id": skill_id,
        "skill_name": data["skill_name"],
        "description": data.get("description", ""),
        "s3_key": s3_key,
        "file_type": file_type,
        "status": "pending",
        "created_at": now,
        "updated_at": now,
        "idempotencyToken": idempotency_token,
    }

    skills_table.put_item(Item=item)
    upload_url = _generate_presigned_url(s3_key)

    return createResponse(
        200,
        "Skill created successfully",
        {"skill": item, "upload_url": upload_url},
    )


def update_skill(event: dict) -> dict:
    """Update a skill's name or description."""
    skill_id = event.get("pathParameters", {}).get("skillId", "")
    data = _parse_body(event)

    resp = skills_table.get_item(Key={"skill_id": skill_id})
    if "Item" not in resp:
        raise NotFoundError("Skill not found")

    updates = {k: v for k, v in data.items() if k in UPDATABLE_FIELDS}
    if not updates:
        raise BadRequestError("No valid update fields provided")

    parts, names, values = [], {}, {}
    for key, val in updates.items():
        parts.append(f"#{key} = :{key}")
        names[f"#{key}"] = key
        values[f":{key}"] = val

    parts.append("#updated_at = :updated_at")
    names["#updated_at"] = "updated_at"
    values[":updated_at"] = datetime.now(timezone.utc).isoformat()

    result = skills_table.update_item(
        Key={"skill_id": skill_id},
        UpdateExpression="SET " + ", ".join(parts),
        ExpressionAttributeNames=names,
        ExpressionAttributeValues=values,
        ReturnValues="ALL_NEW",
    )
    return createResponse(200, "Skill updated successfully", result["Attributes"])


def delete_skill(event: dict) -> dict:
    """Delete a skill record, its junction records, and its associated S3 object."""
    skill_id = event.get("pathParameters", {}).get("skillId", "")

    resp = skills_table.get_item(Key={"skill_id": skill_id})
    item = resp.get("Item")
    if not item:
        raise NotFoundError("Skill not found")

    s3_key = item.get("s3_key", "")

    # Cascade delete all junction records for this skill
    try:
        junction_resp = agent_skills_table.query(
            IndexName="skill-index",
            KeyConditionExpression=Key("skill_id").eq(skill_id),
        )
        for junction_item in junction_resp.get("Items", []):
            agent_skills_table.delete_item(
                Key={
                    "agent_id": junction_item["agent_id"],
                    "skill_id": junction_item["skill_id"],
                }
            )
    except Exception:
        logger.exception("Failed to delete junction records for skill %s", skill_id)

    skills_table.delete_item(Key={"skill_id": skill_id})

    if s3_key:
        try:
            s3_client.delete_object(Bucket=SKILLS_BUCKET_NAME, Key=s3_key)
        except Exception:
            logger.warning("Failed to delete S3 object", extra={"s3_key": s3_key})

    return createResponse(200, "Skill deleted successfully")


def replace_document(event: dict) -> dict:
    """Replace a skill's document: delete old S3 object, return new upload URL.

    Deleting the S3 object triggers SkillDeletion Lambda which removes old
    vectors from OpenSearch. Uploading the new file triggers SkillIngestion
    which re-indexes the content.
    """
    skill_id = event.get("pathParameters", {}).get("skillId", "")

    resp = skills_table.get_item(Key={"skill_id": skill_id})
    item = resp.get("Item")
    if not item:
        raise NotFoundError("Skill not found")

    s3_key = item.get("s3_key", "")
    if not s3_key:
        raise BadRequestError("Skill has no associated document")

    # Delete old S3 object → triggers SkillDeletion → cleans OpenSearch
    try:
        s3_client.delete_object(Bucket=SKILLS_BUCKET_NAME, Key=s3_key)
        logger.info("Deleted old document", extra={"s3_key": s3_key})
    except Exception:
        logger.exception("Failed to delete old S3 object", extra={"s3_key": s3_key})

    # Reset skill status to pending
    skills_table.update_item(
        Key={"skill_id": skill_id},
        UpdateExpression="SET #status = :s, #updated = :u",
        ExpressionAttributeNames={"#status": "status", "#updated": "updated_at"},
        ExpressionAttributeValues={
            ":s": "pending",
            ":u": datetime.now(timezone.utc).isoformat(),
        },
    )

    # Generate new upload URL for the same S3 key
    upload_url = _generate_presigned_url(s3_key)

    return createResponse(200, "Upload new document to replace the existing one", {
        "skill_id": skill_id,
        "s3_key": s3_key,
        "upload_url": upload_url,
    })


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """Main Lambda entry point — routes based on httpMethod and resource."""
    try:
        http_method = event.get("httpMethod", "")
        resource = event.get("resource", "")

        if resource == "/skills" and http_method == "GET":
            return list_skills(event)
        elif resource == "/skills/{skillId}" and http_method == "GET":
            return get_skill(event)
        elif resource == "/skills" and http_method == "POST":
            return create_skill(event)
        elif resource == "/skills/{skillId}" and http_method == "PUT":
            return update_skill(event)
        elif resource == "/skills/{skillId}" and http_method == "DELETE":
            return delete_skill(event)
        elif resource == "/skills/{skillId}/replace-document" and http_method == "POST":
            return replace_document(event)
        else:
            raise BadRequestError(f"Unsupported route: {http_method} {resource}")
    except BadRequestError as e:
        logger.warning("Bad request", extra={"error": str(e)})
        tracer.put_annotation("error", str(e))
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning("Not found", extra={"error": str(e)})
        tracer.put_annotation("error", str(e))
        return createResponse(404, str(e))
    except Exception:
        logger.exception("Internal server error")
        tracer.put_annotation("error", "internal_server_error")
        return createResponse(500, "Internal server error")
