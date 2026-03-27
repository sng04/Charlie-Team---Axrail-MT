"""
GetProjectUsers Lambda Function

Gets all users assigned to a specific project with user details. Admin only (enforced by Lambda Authorizer).
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

from response_utils import createResponse
from custom_exceptions import BadRequestError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
project_users_table = dynamodb.Table(os.environ.get("PROJECT_USERS_TABLE"))
users_table = dynamodb.Table(os.environ.get("USERS_TABLE"))


def _get_project_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    project_id = path_params.get("projectId")
    if not project_id:
        raise BadRequestError("Project ID is required")
    return project_id


def _get_user_details(user_id: str) -> dict | None:
    response = users_table.get_item(Key={"user_id": user_id})
    item = response.get("Item")
    if item:
        item.pop("password_hash", None)
    return item


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        project_id = _get_project_id(event)
        
        response = project_users_table.query(
            IndexName="project-index",
            KeyConditionExpression=Key("project_id").eq(project_id),
        )
        
        project_user_items = response.get("Items", [])
        
        users = []
        for item in project_user_items:
            user_details = _get_user_details(item["user_id"])
            if user_details:
                user_details["project_user_id"] = item["project_user_id"]
                user_details["assigned_at"] = item.get("created_at")
                users.append(user_details)
        
        result = {
            "users": users,
            "total": len(users),
        }
        
        return createResponse(200, "Project users retrieved successfully", result)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
