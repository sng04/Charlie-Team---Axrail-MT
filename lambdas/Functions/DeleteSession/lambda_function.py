"""
DeleteSession Lambda Function

Deletes a session from DynamoDB.
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse

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
        
        table.delete_item(
            Key={"session_id": session_id},
            ConditionExpression="attribute_exists(session_id)",
        )
        
        return createResponse(200, "Session deleted successfully")
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return createResponse(404, f"Session {session_id} not found")
        logger.exception("DynamoDB error")
        return createResponse(500, "Internal server error")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
