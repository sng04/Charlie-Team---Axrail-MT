"""
ListProjects Lambda Function

Lists projects with pagination.
- Admin: sees all projects
- User: sees only assigned projects
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

from response_utils import createResponse

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE"))
project_users_table = dynamodb.Table(os.environ.get("PROJECT_USERS_TABLE"))


def _get_pagination_params(event: dict) -> tuple:
    query_params = event.get("queryStringParameters") or {}
    limit = min(int(query_params.get("limit", 20)), 100)
    last_key = query_params.get("lastKey")
    return limit, last_key


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


def _get_projects_by_ids(project_ids: list) -> list:
    """Batch get projects by IDs."""
    if not project_ids:
        return []
    
    keys = [{"project_id": pid} for pid in project_ids]
    response = dynamodb.batch_get_item(
        RequestItems={os.environ.get("PROJECTS_TABLE"): {"Keys": keys}}
    )
    return response.get("Responses", {}).get(os.environ.get("PROJECTS_TABLE"), [])


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        user_id, is_admin = _get_user_context(event)
        limit, last_key = _get_pagination_params(event)
        
        if is_admin:
            scan_kwargs = {"Limit": limit}
            if last_key:
                scan_kwargs["ExclusiveStartKey"] = {"project_id": last_key}
            
            response = projects_table.scan(**scan_kwargs)
            
            result = {
                "items": response.get("Items", []),
                "count": response.get("Count", 0),
            }
            
            if "LastEvaluatedKey" in response:
                result["lastKey"] = response["LastEvaluatedKey"]["project_id"]
        else:
            project_ids = _get_user_assigned_projects(user_id)
            items = _get_projects_by_ids(project_ids)
            
            result = {
                "items": items,
                "count": len(items),
            }
        
        return createResponse(200, "Projects retrieved successfully", result)
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
