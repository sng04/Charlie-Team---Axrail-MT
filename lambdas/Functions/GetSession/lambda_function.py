"""
GetSession Lambda Function

Retrieves a single session by ID from DynamoDB.
- Admin: can access any session
- User: can only access sessions from assigned projects
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

from response_utils import createResponse
from custom_exceptions import NotFoundError, UnauthorizedError

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


def _get_project_name(project_id: str) -> str | None:
    """Get project name by project_id."""
    response = projects_table.get_item(
        Key={"project_id": project_id},
        ProjectionExpression="#name",
        ExpressionAttributeNames={"#name": "name"},
    )
    item = response.get("Item")
    return item.get("name") if item else None


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        path_params = event.get("pathParameters") or {}
        session_id = path_params.get("sessionId")
        
        if not session_id:
            return createResponse(400, "Missing sessionId path parameter")
        
        response = sessions_table.get_item(Key={"session_id": session_id})
        
        if "Item" not in response:
            raise NotFoundError(f"Session {session_id} not found")
        
        session = response["Item"]
        user_id, is_admin = _get_user_context(event)
        
        if not is_admin:
            project_id = session.get("project_id")
            if not _is_user_assigned_to_project(user_id, project_id):
                raise UnauthorizedError("You don't have access to this session")
        
        # Add project_name to response
        project_name = _get_project_name(session.get("project_id"))
        if project_name:
            session["project_name"] = project_name
        
        return createResponse(200, "Session retrieved successfully", session)
    except UnauthorizedError as e:
        logger.warning(f"Unauthorized: {e}")
        return createResponse(403, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
