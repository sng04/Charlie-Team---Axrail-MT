"""
GetSession Lambda Function

Retrieves a single session by ID from DynamoDB.
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse
from custom_exceptions import NotFoundError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("SESSIONS_TABLE")
table = dynamodb.Table(table_name)


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        path_params = event.get("pathParameters") or {}
        session_id = path_params.get("sessionId")
        
        if not session_id:
            return createResponse(400, "Missing sessionId path parameter")
        
        response = table.get_item(Key={"session_id": session_id})
        
        if "Item" not in response:
            raise NotFoundError(f"Session {session_id} not found")
        
        return createResponse(200, "Session retrieved successfully", response["Item"])
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
