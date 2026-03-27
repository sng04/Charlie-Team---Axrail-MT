"""Personalities CRUD Lambda Function.

Routes HTTP methods for the /personalities resource, providing list, get,
create, update, and delete operations against the PersonalitiesTable
DynamoDB table. Enforces referential integrity on delete by checking
AgentsTable for references.
"""

import json
import os
import uuid
from datetime import datetime, timezone
from math import ceil

import boto3
from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Attr, Key

from custom_exceptions import BadRequestError, ConflictError, NotFoundError
from response_utils import createResponse

logger = Logger()
tracer = Tracer()

PERSONALITIES_TABLE_NAME = os.environ.get("PERSONALITIES_TABLE_NAME", "")
AGENTS_TABLE_NAME = os.environ.get("AGENTS_TABLE_NAME", "")

dynamodb = boto3.resource("dynamodb")
personalities_table = dynamodb.Table(PERSONALITIES_TABLE_NAME)
agents_table = dynamodb.Table(AGENTS_TABLE_NAME)

REQUIRED_PERSONALITY_FIELDS = ["personality_name", "personality_prompt"]


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


def list_personalities(event: dict) -> dict:
    """Scan PersonalitiesTable and return a paginated list."""
    params = event.get("queryStringParameters") or {}
    try:
        page = max(1, int(params.get("page", 1)))
    except (ValueError, TypeError):
        page = 1
    try:
        limit = min(100, max(1, int(params.get("limit", 20))))
    except (ValueError, TypeError):
        limit = 20

    resp = personalities_table.scan()
    items = resp.get("Items", [])
    total = len(items)
    total_pages = ceil(total / limit) if total > 0 else 1

    start = (page - 1) * limit
    page_items = items[start : start + limit]

    return createResponse(
        200,
        "Personalities retrieved successfully",
        {
            "items": page_items,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "total_pages": total_pages,
            },
        },
    )


def get_personality(event: dict) -> dict:
    """Get a single personality by personalityId."""
    personality_id = event.get("pathParameters", {}).get("personalityId", "")
    resp = personalities_table.get_item(Key={"personality_id": personality_id})
    item = resp.get("Item")
    if not item:
        raise NotFoundError("Personality not found")
    return createResponse(200, "Personality retrieved successfully", item)


def create_personality(event: dict) -> dict:
    """Create a new personality record after validating required fields."""
    data = _parse_body(event)
    _validate_required(data, REQUIRED_PERSONALITY_FIELDS)

    # Check for duplicate name via GSI query
    existing = personalities_table.query(
        IndexName="name-index",
        KeyConditionExpression=Key("personality_name").eq(data["personality_name"]),
    )
    if existing.get("Items"):
        return createResponse(409, "A personality with this name already exists")

    # Idempotency check
    idempotency_token = data.get("idempotencyToken")
    if idempotency_token:
        resp = personalities_table.scan(
            FilterExpression=Attr("idempotencyToken").eq(idempotency_token),
            Limit=1,
        )
        if resp.get("Items"):
            return createResponse(
                200, "Personality already exists", resp["Items"][0]
            )

    now = datetime.now(timezone.utc).isoformat()
    personality_id = str(uuid.uuid4())
    item = {
        "personality_id": personality_id,
        "idempotencyToken": idempotency_token,
        "created_at": now,
        "updated_at": now,
    }
    for field in REQUIRED_PERSONALITY_FIELDS:
        item[field] = data[field]

    personalities_table.put_item(Item=item)
    return createResponse(200, "Personality created successfully", item)


def update_personality(event: dict) -> dict:
    """Update an existing personality with the provided fields."""
    personality_id = event.get("pathParameters", {}).get("personalityId", "")
    data = _parse_body(event)

    if not data:
        raise BadRequestError("No update fields provided")

    resp = personalities_table.get_item(Key={"personality_id": personality_id})
    if "Item" not in resp:
        raise NotFoundError("Personality not found")

    # Build dynamic update expression
    parts, names, values = [], {}, {}
    for key, val in data.items():
        if key == "personality_id":
            continue
        parts.append(f"#{key} = :{key}")
        names[f"#{key}"] = key
        values[f":{key}"] = val

    # Always update timestamp
    parts.append("#updated_at = :updated_at")
    names["#updated_at"] = "updated_at"
    values[":updated_at"] = datetime.now(timezone.utc).isoformat()

    if not parts:
        raise BadRequestError("No update fields provided")

    result = personalities_table.update_item(
        Key={"personality_id": personality_id},
        UpdateExpression="SET " + ", ".join(parts),
        ExpressionAttributeNames=names,
        ExpressionAttributeValues=values,
        ReturnValues="ALL_NEW",
    )
    return createResponse(
        200, "Personality updated successfully", result["Attributes"]
    )


def delete_personality(event: dict) -> dict:
    """Delete a personality, checking for agent references first."""
    personality_id = event.get("pathParameters", {}).get("personalityId", "")

    resp = personalities_table.get_item(Key={"personality_id": personality_id})
    if "Item" not in resp:
        raise NotFoundError("Personality not found")

    scan_resp = agents_table.scan(
        FilterExpression=Attr("personality_id").eq(personality_id)
    )
    if scan_resp.get("Items"):
        raise ConflictError(
            "Cannot delete personality: referenced by existing agents"
        )

    personalities_table.delete_item(Key={"personality_id": personality_id})
    return createResponse(200, "Personality deleted successfully")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """Main Lambda entry point — routes based on httpMethod and resource."""
    try:
        http_method = event.get("httpMethod", "")
        resource = event.get("resource", "")

        if resource == "/personalities" and http_method == "GET":
            return list_personalities(event)
        elif resource == "/personalities/{personalityId}" and http_method == "GET":
            return get_personality(event)
        elif resource == "/personalities" and http_method == "POST":
            return create_personality(event)
        elif resource == "/personalities/{personalityId}" and http_method == "PUT":
            return update_personality(event)
        elif resource == "/personalities/{personalityId}" and http_method == "DELETE":
            return delete_personality(event)
        else:
            raise BadRequestError(
                f"Unsupported route: {http_method} {resource}"
            )
    except BadRequestError as e:
        logger.warning("Bad request", extra={"error": str(e)})
        tracer.put_annotation("error", str(e))
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning("Not found", extra={"error": str(e)})
        tracer.put_annotation("error", str(e))
        return createResponse(404, str(e))
    except ConflictError as e:
        logger.warning("Conflict", extra={"error": str(e)})
        tracer.put_annotation("error", str(e))
        return createResponse(409, str(e))
    except Exception:
        logger.exception("Internal server error")
        tracer.put_annotation("error", "internal_server_error")
        return createResponse(500, "Internal server error")
