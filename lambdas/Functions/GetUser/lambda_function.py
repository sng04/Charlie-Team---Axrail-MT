"""
GetUser Lambda Function

Gets a single user by ID from DynamoDB. Admin only (enforced by Lambda Authorizer).
"""

import os
from typing import Any

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE")


@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: Any) -> dict:
    """
    Handle get user request.

    Args:
        event: API Gateway event containing userId in path parameters.
        context: Lambda context object.

    Returns:
        API response with user data.
    """
    try:
        path_params = event.get("pathParameters") or {}
        user_id = path_params.get("userId")
        
        if not user_id:
            raise BadRequestError("User ID is required")
        
        table = dynamodb.Table(DYNAMODB_TABLE)
        response = table.get_item(Key={"user_id": user_id})
        
        if "Item" not in response:
            raise NotFoundError(f"User {user_id} not found")
        
        logger.info(f"Retrieved user {user_id}")
        return createResponse(200, "User retrieved successfully", response["Item"])
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
