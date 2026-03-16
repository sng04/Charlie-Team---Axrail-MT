"""
GetProjectUsers Lambda Function

Gets all users assigned to a specific project. Admin only (enforced by Lambda Authorizer).
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
table_name = os.environ.get("PROJECT_USERS_TABLE")
table = dynamodb.Table(table_name)


def _get_project_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    project_id = path_params.get("projectId")
    if not project_id:
        raise BadRequestError("Project ID is required")
    return project_id


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        project_id = _get_project_id(event)
        
        response = table.query(
            IndexName="project-index",
            KeyConditionExpression=Key("project_id").eq(project_id),
        )
        
        result = {
            "items": response.get("Items", []),
            "count": response.get("Count", 0),
        }
        
        return createResponse(200, "Project users retrieved successfully", result)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
