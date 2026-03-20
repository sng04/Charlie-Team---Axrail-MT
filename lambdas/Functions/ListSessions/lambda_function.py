"""
ListSessions Lambda Function

Lists sessions with pagination support.
- Admin: sees all sessions
- User: sees only sessions from assigned projects
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

from response_utils import createResponse

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
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


def _get_user_assigned_projects(user_id: str) -> list:
    """Get list of project_ids assigned to user."""
    response = project_users_table.query(
        IndexName="user-index",
        KeyConditionExpression=Key("user_id").eq(user_id),
    )
    return [item["project_id"] for item in response.get("Items", [])]


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        user_id, is_admin = _get_user_context(event)
        query_params = event.get("queryStringParameters") or {}
        limit = min(int(query_params.get("limit", 20)), 100)
        
        if is_admin:
            scan_kwargs = {"Limit": limit}
            
            last_key = query_params.get("lastKey")
            if last_key:
                scan_kwargs["ExclusiveStartKey"] = {"session_id": last_key}
            
            response = sessions_table.scan(**scan_kwargs)
            
            result = {
                "items": response.get("Items", []),
                "count": len(response.get("Items", [])),
            }
            
            if "LastEvaluatedKey" in response:
                result["lastKey"] = response["LastEvaluatedKey"]["session_id"]
        else:
            project_ids = _get_user_assigned_projects(user_id)
            
            if not project_ids:
                return createResponse(200, "Sessions retrieved successfully", {
                    "items": [],
                    "count": 0,
                })
            
            all_sessions = []
            for project_id in project_ids:
                response = sessions_table.query(
                    IndexName="project-index",
                    KeyConditionExpression=Key("project_id").eq(project_id),
                )
                all_sessions.extend(response.get("Items", []))
            
            all_sessions.sort(key=lambda x: x.get("created_at", ""), reverse=True)
            
            result = {
                "items": all_sessions[:limit],
                "count": len(all_sessions[:limit]),
            }
        
        return createResponse(200, "Sessions retrieved successfully", result)
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
