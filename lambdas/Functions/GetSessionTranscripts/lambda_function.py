"""
GetSessionTranscripts Lambda Function

Retrieves all transcripts for a specific session.
- Admin: can access any session's transcripts
- User: can only access transcripts from sessions in assigned projects
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError, UnauthorizedError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
transcripts_table = dynamodb.Table(os.environ.get("TRANSCRIPTS_TABLE"))
sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE"))
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


def _get_session_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    session_id = path_params.get("sessionId")
    if not session_id:
        raise BadRequestError("Session ID is required")
    return session_id


def _get_session(session_id: str) -> dict:
    response = sessions_table.get_item(Key={"session_id": session_id})
    if "Item" not in response:
        raise NotFoundError(f"Session {session_id} not found")
    return response["Item"]


def _get_pagination_params(event: dict) -> tuple:
    query_params = event.get("queryStringParameters") or {}
    limit = min(int(query_params.get("limit", 50)), 100)
    last_key = query_params.get("lastKey")
    return limit, last_key


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        session_id = _get_session_id(event)
        session = _get_session(session_id)
        
        user_id, is_admin = _get_user_context(event)
        
        if not is_admin:
            project_id = session.get("project_id")
            if not _is_user_assigned_to_project(user_id, project_id):
                raise UnauthorizedError("You don't have access to this session")

        limit, last_key = _get_pagination_params(event)

        query_kwargs = {
            "KeyConditionExpression": Key("session_id").eq(session_id),
            "Limit": limit,
            "ScanIndexForward": True, 
        }

        if last_key:
            query_kwargs["ExclusiveStartKey"] = {
                "session_id": session_id,
                "timestamp": last_key,
            }

        response = transcripts_table.query(**query_kwargs)

        result = {
            "session_id": session_id,
            "items": response.get("Items", []),
            "count": len(response.get("Items", [])),
        }

        if "LastEvaluatedKey" in response:
            result["lastKey"] = response["LastEvaluatedKey"]["timestamp"]

        return createResponse(200, "Transcripts retrieved successfully", result)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
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
