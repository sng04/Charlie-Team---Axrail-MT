"""
ListUsers Lambda Function

Lists all users from DynamoDB. Admin only (enforced by Lambda Authorizer).
"""

import os
from typing import Any

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE")


@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: Any) -> dict:
    """
    Handle list users request.

    Args:
        event: API Gateway event.
        context: Lambda context object.

    Returns:
        API response with list of users.
    """
    try:
        table = dynamodb.Table(DYNAMODB_TABLE)
        response = table.scan()
        
        users = response.get("Items", [])
        
        # Handle pagination if there are more items
        while "LastEvaluatedKey" in response:
            response = table.scan(ExclusiveStartKey=response["LastEvaluatedKey"])
            users.extend(response.get("Items", []))
        
        logger.info(f"Retrieved {len(users)} users")
        return createResponse(200, "Users retrieved successfully", {"users": users})
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
