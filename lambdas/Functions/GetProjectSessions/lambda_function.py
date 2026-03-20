"""
GetProjectSessions Lambda Function

Retrieves all sessions for a specific project using GSI.
- Admin: can access any project's sessions
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


def _verify_project_exists(project_id: str) -> None:
    response = projects_table.get_item(Key={"project_id": project_id})
    if "Item" not in response:
        raise NotFoundError(f"Project {project_id} not found")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        path_params = event.get("pathParameters") or {}
        project_id = path_params.get("projectId")
        
        if not project_id:
            return createResponse(400, "Missing projectId path parameter")
        
        _verify_project_exists(project_id)
        
        user_id, is_admin = _get_user_context(event)
        
        if not is_admin and not _is_user_assigned_to_project(user_id, project_id):
            raise UnauthorizedError("You don't have access to this project")
        
        query_params = event.get("queryStringParameters") or {}
        limit = min(int(query_params.get("limit", 20)), 100)
        
        query_kwargs = {
            "IndexName": "project-index",
            "KeyConditionExpression": Key("project_id").eq(project_id),
            "Limit": limit,
        }
        
        last_key = query_params.get("lastKey")
        if last_key:
            query_kwargs["ExclusiveStartKey"] = {
                "session_id": last_key,
                "project_id": project_id,
            }
        
        response = sessions_table.query(**query_kwargs)
        
        result = {
            "project_id": project_id,
            "items": response.get("Items", []),
            "count": len(response.get("Items", [])),
        }
        
        if "LastEvaluatedKey" in response:
            result["lastKey"] = response["LastEvaluatedKey"]["session_id"]
        
        return createResponse(200, "Project sessions retrieved successfully", result)
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
