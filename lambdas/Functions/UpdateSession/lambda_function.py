"""
UpdateSession Lambda Function

Updates an existing session in DynamoDB.
- Admin: can update any session
- User: can only update sessions from assigned projects
"""

import json
import os
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError, UnauthorizedError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE"))
projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE"))
project_users_table = dynamodb.Table(os.environ.get("PROJECT_USERS_TABLE"))


def _get_user_context(event: dict) -> tuple:
    """Extract user_id and role from authorizer context."""
    request_context = event.get("requestContext", {})
    authorizer = request_context.get("authorizer", {})
    user_id = authorizer.get("user_id", "")
    groups = authorizer.get("groups", "")
    is_admin = "admin" in groups.split(",")
    return user_id, is_admin


def _is_user_assigned_to_project(user_id: str, project_id: str) -> bool:
    """Check if user is assigned to the project."""
    response = project_users_table.query(
        IndexName="user-index",
        KeyConditionExpression=Key("user_id").eq(user_id),
    )
    assigned_projects = [item["project_id"] for item in response.get("Items", [])]
    return project_id in assigned_projects


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _verify_project_exists(project_id: str) -> None:
    response = projects_table.get_item(Key={"project_id": project_id})
    if "Item" not in response:
        raise NotFoundError(f"Project {project_id} not found")


def _get_session(session_id: str) -> dict:
    response = sessions_table.get_item(Key={"session_id": session_id})
    if "Item" not in response:
        raise NotFoundError(f"Session {session_id} not found")
    return response["Item"]


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        path_params = event.get("pathParameters") or {}
        session_id = path_params.get("sessionId")
        
        if not session_id:
            return createResponse(400, "Missing sessionId path parameter")
        
        session = _get_session(session_id)
        user_id, is_admin = _get_user_context(event)
        
        if not is_admin:
            project_id = session.get("project_id")
            if not _is_user_assigned_to_project(user_id, project_id):
                raise UnauthorizedError("You don't have access to this session")
        
        data = _parse_body(event)
        
        if not data:
            raise BadRequestError("No update data provided")
        
        if "project_id" in data:
            _verify_project_exists(data["project_id"])
            if not is_admin and not _is_user_assigned_to_project(user_id, data["project_id"]):
                raise UnauthorizedError("You don't have access to the target project")
        
        allowed_fields = ["name", "description", "meeting_link", "status", 
                         "start_time", "end_time", "project_id"]
        update_data = {k: v for k, v in data.items() if k in allowed_fields}
        
        if not update_data:
            raise BadRequestError("No valid fields to update")
        
        update_data["updated_at"] = datetime.now(timezone.utc).isoformat()
        
        parts, names, values = [], {}, {}
        for key, val in update_data.items():
            parts.append(f"#{key} = :{key}")
            names[f"#{key}"] = key
            values[f":{key}"] = val
        
        response = sessions_table.update_item(
            Key={"session_id": session_id},
            UpdateExpression="SET " + ", ".join(parts),
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ConditionExpression="attribute_exists(session_id)",
            ReturnValues="ALL_NEW",
        )
        
        return createResponse(200, "Session updated successfully", response["Attributes"])
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except UnauthorizedError as e:
        logger.warning(f"Unauthorized: {e}")
        return createResponse(403, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return createResponse(404, f"Session {session_id} not found")
        logger.exception("DynamoDB error")
        return createResponse(500, "Internal server error")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
