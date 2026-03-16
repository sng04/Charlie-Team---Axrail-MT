"""
GetUserProjects Lambda Function

Gets all projects assigned to a specific user. Admin only (enforced by Lambda Authorizer).
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


def _get_user_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    user_id = path_params.get("userId")
    if not user_id:
        raise BadRequestError("User ID is required")
    return user_id


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        user_id = _get_user_id(event)
        
        response = table.query(
            IndexName="user-index",
            KeyConditionExpression=Key("user_id").eq(user_id),
        )
        
        result = {
            "items": response.get("Items", []),
            "count": response.get("Count", 0),
        }
        
        return createResponse(200, "User projects retrieved successfully", result)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
