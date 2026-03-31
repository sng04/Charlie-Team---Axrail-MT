"""Agents CRUD Lambda Function.

Routes HTTP methods for the /agents resource, providing list, get, create,
update, and delete operations against the AgentsTable DynamoDB table.
"""

import json
import os
import uuid
from datetime import datetime, timezone
from math import ceil

import boto3
from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Attr, Key

from changelog_utils import log_admin_change
from custom_exceptions import BadRequestError, ConflictError, NotFoundError
from response_utils import createResponse

logger = Logger()
tracer = Tracer()

AGENTS_TABLE_NAME = os.environ.get("AGENTS_TABLE_NAME", "")
PERSONALITIES_TABLE_NAME = os.environ.get("PERSONALITIES_TABLE_NAME", "")
AGENT_SKILLS_TABLE_NAME = os.environ.get("AGENT_SKILLS_TABLE_NAME", "")
AGENT_CONFIG_HISTORY_TABLE_NAME = os.environ.get("AGENT_CONFIG_HISTORY_TABLE_NAME", "")

dynamodb = boto3.resource("dynamodb")
agents_table = dynamodb.Table(AGENTS_TABLE_NAME)
personalities_table = dynamodb.Table(PERSONALITIES_TABLE_NAME)
agent_skills_table = dynamodb.Table(AGENT_SKILLS_TABLE_NAME)
history_table = dynamodb.Table(AGENT_CONFIG_HISTORY_TABLE_NAME) if AGENT_CONFIG_HISTORY_TABLE_NAME else None

REQUIRED_AGENT_FIELDS = [
    "agent_name",
    "role_prompt",
    "behavior_guidelines",
    "personality_id",
    "model_id",
    "use_case",
]


def _normalize_behavior_field(data: dict) -> dict:
    """Normalize task_prompt → behavior_guidelines for backward compatibility."""
    if "behavior_guidelines" not in data and "task_prompt" in data:
        data["behavior_guidelines"] = data.pop("task_prompt")
    elif "behavior_guidelines" in data and "task_prompt" in data:
        data.pop("task_prompt")
    return data


def _enrich_response(item: dict) -> dict:
    """Ensure both behavior_guidelines and task_prompt are in the response."""
    if "behavior_guidelines" in item and "task_prompt" not in item:
        item["task_prompt"] = item["behavior_guidelines"]
    elif "task_prompt" in item and "behavior_guidelines" not in item:
        item["behavior_guidelines"] = item["task_prompt"]
    return item


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


def _personality_exists(personality_id: str) -> bool:
    """Check whether a personality_id exists in PersonalitiesTable."""
    resp = personalities_table.get_item(Key={"personality_id": personality_id})
    return "Item" in resp


def list_agents(event: dict) -> dict:
    """Scan AgentsTable and return a paginated list."""
    params = event.get("queryStringParameters") or {}
    try:
        page = max(1, int(params.get("page", 1)))
    except (ValueError, TypeError):
        page = 1
    try:
        limit = min(100, max(1, int(params.get("limit", 20))))
    except (ValueError, TypeError):
        limit = 20

    resp = agents_table.scan()
    items = resp.get("Items", [])
    total = len(items)
    total_pages = ceil(total / limit) if total > 0 else 1

    start = (page - 1) * limit
    page_items = items[start : start + limit]
    page_items = [_enrich_response(item) for item in page_items]

    return createResponse(
        200,
        "Agents retrieved successfully",
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


def get_agent(event: dict) -> dict:
    """Get a single agent by agentId."""
    agent_id = event.get("pathParameters", {}).get("agentId", "")
    resp = agents_table.get_item(Key={"agent_id": agent_id})
    item = resp.get("Item")
    if not item:
        raise NotFoundError("Agent not found")
    item = _enrich_response(item)
    return createResponse(200, "Agent retrieved successfully", item)


def create_agent(event: dict) -> dict:
    """Create a new agent record after validating required fields and FK."""
    data = _parse_body(event)
    data = _normalize_behavior_field(data)
    _validate_required(data, REQUIRED_AGENT_FIELDS)

    if not _personality_exists(data["personality_id"]):
        raise BadRequestError("Referenced personality_id does not exist")

    # Check for duplicate name via GSI query
    existing = agents_table.query(
        IndexName="name-index",
        KeyConditionExpression=Key("agent_name").eq(data["agent_name"]),
    )
    if existing.get("Items"):
        return createResponse(409, "An agent with this name already exists")

    # Idempotency check
    idempotency_token = data.get("idempotencyToken")
    if idempotency_token:
        resp = agents_table.scan(
            FilterExpression=Attr("idempotencyToken").eq(idempotency_token),
            Limit=1,
        )
        if resp.get("Items"):
            return createResponse(200, "Agent already exists", resp["Items"][0])

    now = datetime.now(timezone.utc).isoformat()
    agent_id = str(uuid.uuid4())
    item = {
        "agent_id": agent_id,
        "idempotencyToken": idempotency_token,
        "created_at": now,
        "updated_at": now,
    }
    for field in REQUIRED_AGENT_FIELDS:
        item[field] = data[field]

    agents_table.put_item(Item=item)
    log_admin_change(event, "agent", agent_id, "create", data=item, entity_name=item.get("agent_name", ""))
    return createResponse(200, "Agent created successfully", item)


def _get_personality_name(personality_id: str) -> str:
    """Look up personality name by ID."""
    if not personality_id:
        return ""
    try:
        resp = personalities_table.get_item(
            Key={"personality_id": personality_id},
            ProjectionExpression="personality_name",
        )
        return resp.get("Item", {}).get("personality_name", "")
    except Exception:
        return ""


def _get_skill_names(agent_id: str) -> list:
    """Look up active skill names for an agent."""
    try:
        jr = agent_skills_table.query(
            KeyConditionExpression=Key("agent_id").eq(agent_id),
        )
        skill_ids = [item["skill_id"] for item in jr.get("Items", [])]
        names = []
        skills_table = dynamodb.Table(os.environ.get("SKILLS_TABLE_NAME", ""))
        for sid in skill_ids:
            r = skills_table.get_item(Key={"skill_id": sid}, ProjectionExpression="skill_name")
            name = r.get("Item", {}).get("skill_name")
            if name:
                names.append(name)
        return names
    except Exception:
        return []


def _save_config_history(agent_id: str, pre_update_item: dict, changed_fields: list) -> None:
    """Save a versioned snapshot of the agent config before an update."""
    if not history_table:
        return
    try:
        # Get next version number
        resp = history_table.query(
            KeyConditionExpression=Key("agent_id").eq(agent_id),
            ScanIndexForward=False,
            Limit=1,
            ProjectionExpression="version",
        )
        items = resp.get("Items", [])
        next_version = int(items[0]["version"]) + 1 if items else 1

        now = datetime.now(timezone.utc).isoformat()

        # Build snapshot with resolved names
        snapshot = {
            "agent_id": agent_id,
            "version": next_version,
            "agent_name": pre_update_item.get("agent_name", ""),
            "role_prompt": pre_update_item.get("role_prompt", ""),
            "behavior_guidelines": pre_update_item.get("behavior_guidelines", ""),
            "personality_id": pre_update_item.get("personality_id", ""),
            "personality_name": _get_personality_name(pre_update_item.get("personality_id", "")),
            "model_id": pre_update_item.get("model_id", ""),
            "use_case": pre_update_item.get("use_case", ""),
            "skill_names": _get_skill_names(agent_id),
            "changed_fields": changed_fields,
            "created_at": pre_update_item.get("created_at", ""),
            "snapshot_at": now,
        }

        history_table.put_item(Item=snapshot)
        logger.info("Saved config history", extra={"agent_id": agent_id, "version": next_version})
    except Exception:
        logger.warning("Failed to save config history", extra={"agent_id": agent_id})


def update_agent(event: dict) -> dict:
    """Update an existing agent with the provided fields."""
    agent_id = event.get("pathParameters", {}).get("agentId", "")
    data = _parse_body(event)

    if not data:
        raise BadRequestError("No update fields provided")

    data = _normalize_behavior_field(data)

    resp = agents_table.get_item(Key={"agent_id": agent_id})
    if "Item" not in resp:
        raise NotFoundError("Agent not found")

    pre_update_item = resp["Item"]

    if "personality_id" in data and not _personality_exists(data["personality_id"]):
        raise BadRequestError("Referenced personality_id does not exist")

    # Determine which fields are changing
    changed_fields = [k for k in data if k != "agent_id" and data[k] != pre_update_item.get(k)]

    # Save pre-update snapshot to history (fire-and-forget)
    if changed_fields:
        _save_config_history(agent_id, pre_update_item, changed_fields)

    # Build dynamic update expression
    parts, names, values = [], {}, {}
    for key, val in data.items():
        if key == "agent_id":
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

    result = agents_table.update_item(
        Key={"agent_id": agent_id},
        UpdateExpression="SET " + ", ".join(parts),
        ExpressionAttributeNames=names,
        ExpressionAttributeValues=values,
        ReturnValues="ALL_NEW",
    )
    log_admin_change(event, "agent", agent_id, "update", data=data, previous_data=pre_update_item, changed_fields=changed_fields, entity_name=pre_update_item.get("agent_name", ""))
    return createResponse(200, "Agent updated successfully", result["Attributes"])


def delete_agent(event: dict) -> dict:
    """Delete an agent by agentId, cascading junction record deletions."""
    agent_id = event.get("pathParameters", {}).get("agentId", "")

    resp = agents_table.get_item(Key={"agent_id": agent_id})
    if "Item" not in resp:
        raise NotFoundError("Agent not found")

    # Cascade delete all junction records for this agent
    try:
        junction_resp = agent_skills_table.query(
            KeyConditionExpression=Key("agent_id").eq(agent_id),
        )
        for junction_item in junction_resp.get("Items", []):
            agent_skills_table.delete_item(
                Key={
                    "agent_id": junction_item["agent_id"],
                    "skill_id": junction_item["skill_id"],
                }
            )
    except Exception:
        logger.exception("Failed to delete junction records for agent %s", agent_id)

    agents_table.delete_item(Key={"agent_id": agent_id})
    log_admin_change(event, "agent", agent_id, "delete", previous_data=resp["Item"], entity_name=resp["Item"].get("agent_name", ""))
    return createResponse(200, "Agent deleted successfully")


def get_agent_history(event: dict) -> dict:
    """List version history for an agent, newest first."""
    agent_id = event.get("pathParameters", {}).get("agentId", "")
    if not agent_id:
        raise BadRequestError("Agent ID is required")
    if not history_table:
        return createResponse(200, "History not available", {"versions": [], "count": 0})

    params = event.get("queryStringParameters") or {}
    limit = min(50, int(params.get("limit", 20)))

    query_kwargs = {
        "KeyConditionExpression": Key("agent_id").eq(agent_id),
        "ScanIndexForward": False,
        "Limit": limit,
    }
    last_key = params.get("lastKey")
    if last_key:
        query_kwargs["ExclusiveStartKey"] = {"agent_id": agent_id, "version": int(last_key)}

    resp = history_table.query(**query_kwargs)
    items = resp.get("Items", [])

    result = {"versions": items, "count": len(items)}
    if "LastEvaluatedKey" in resp:
        result["lastKey"] = str(int(resp["LastEvaluatedKey"]["version"]))

    return createResponse(200, "Agent history retrieved", result)


def get_agent_version(event: dict) -> dict:
    """Get a specific version of an agent's config history."""
    agent_id = event.get("pathParameters", {}).get("agentId", "")
    version_str = event.get("pathParameters", {}).get("version", "")
    if not agent_id or not version_str:
        raise BadRequestError("Agent ID and version are required")
    if not history_table:
        raise NotFoundError("History not available")

    try:
        version = int(version_str)
    except ValueError:
        raise BadRequestError("Version must be a number")

    resp = history_table.get_item(Key={"agent_id": agent_id, "version": version})
    item = resp.get("Item")
    if not item:
        raise NotFoundError(f"Version {version} not found for agent {agent_id}")

    return createResponse(200, "Agent version retrieved", item)


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """Main Lambda entry point — routes based on httpMethod and resource."""
    try:
        http_method = event.get("httpMethod", "")
        resource = event.get("resource", "")

        if resource == "/agents" and http_method == "GET":
            return list_agents(event)
        elif resource == "/agents/{agentId}" and http_method == "GET":
            return get_agent(event)
        elif resource == "/agents" and http_method == "POST":
            return create_agent(event)
        elif resource == "/agents/{agentId}" and http_method == "PUT":
            return update_agent(event)
        elif resource == "/agents/{agentId}" and http_method == "DELETE":
            return delete_agent(event)
        elif resource == "/agents/{agentId}/history" and http_method == "GET":
            return get_agent_history(event)
        elif resource == "/agents/{agentId}/history/{version}" and http_method == "GET":
            return get_agent_version(event)
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
