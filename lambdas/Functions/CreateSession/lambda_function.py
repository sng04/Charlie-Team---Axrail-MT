"""
CreateSession Lambda Function

Creates a new session linked to a project in DynamoDB.
"""

import json
import os
import uuid
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE"))
projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE"))


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _validate_input(data: dict) -> None:
    required_fields = ["project_id", "name"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


def _verify_project_exists(project_id: str) -> None:
    response = projects_table.get_item(Key={"project_id": project_id})
    if "Item" not in response:
        raise NotFoundError(f"Project {project_id} not found")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        data = _parse_body(event)
        _validate_input(data)
        
        _verify_project_exists(data["project_id"])
        
        session_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc).isoformat()
        
        item = {
            "session_id": session_id,
            "project_id": data["project_id"],
            "name": data["name"],
            "description": data.get("description", ""),
            "meeting_link": data.get("meeting_link", ""),
            "status": data.get("status", False),
            "start_time": data.get("start_time"),
            "end_time": data.get("end_time"),
            "created_at": now,
            "updated_at": now,
        }
        
        sessions_table.put_item(Item=item)
        
        return createResponse(200, "Session created successfully", item)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
