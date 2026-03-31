"""
AssignUserToProject Lambda Function

Assigns a user to a project (creates project_user record). Admin only (enforced by Lambda Authorizer).
"""

import json
import os
import uuid
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError, ConflictError
from changelog_utils import log_admin_change

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
project_users_table = dynamodb.Table(os.environ.get("PROJECT_USERS_TABLE"))
projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE"))
users_table = dynamodb.Table(os.environ.get("USERS_TABLE"))


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _validate_input(data: dict) -> None:
    required_fields = ["user_id", "project_id"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


def _verify_project_exists(project_id: str) -> None:
    response = projects_table.get_item(Key={"project_id": project_id})
    if "Item" not in response:
        raise NotFoundError(f"Project {project_id} not found")


def _verify_user_exists(user_id: str) -> None:
    response = users_table.get_item(Key={"user_id": user_id})
    if "Item" not in response:
        raise NotFoundError(f"User {user_id} not found")


def _check_assignment_exists(user_id: str, project_id: str) -> None:
    response = project_users_table.query(
        IndexName="user-index",
        KeyConditionExpression=Key("user_id").eq(user_id),
    )
    for item in response.get("Items", []):
        if item.get("project_id") == project_id:
            raise ConflictError("User is already assigned to this project")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        data = _parse_body(event)
        _validate_input(data)
        
        user_id = data["user_id"]
        project_id = data["project_id"]
        
        _verify_project_exists(project_id)
        _verify_user_exists(user_id)
        _check_assignment_exists(user_id, project_id)
        
        project_user_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc).isoformat()
        
        item = {
            "project_user_id": project_user_id,
            "user_id": user_id,
            "project_id": project_id,
            "created_at": now,
        }
        
        project_users_table.put_item(Item=item)
        
        log_admin_change(event, "project_user_assignment", project_user_id, "create", data=item, entity_name="")
        
        return createResponse(200, "User assigned to project successfully", item)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except ConflictError as e:
        logger.warning(f"Conflict: {e}")
        return createResponse(409, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
