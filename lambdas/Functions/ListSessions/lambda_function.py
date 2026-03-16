"""
ListSessions Lambda Function

Lists all sessions with pagination support.
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("SESSIONS_TABLE")
table = dynamodb.Table(table_name)


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        query_params = event.get("queryStringParameters") or {}
        limit = min(int(query_params.get("limit", 20)), 100)
        
        scan_kwargs = {"Limit": limit}
        
        last_key = query_params.get("lastKey")
        if last_key:
            scan_kwargs["ExclusiveStartKey"] = {"session_id": last_key}
        
        response = table.scan(**scan_kwargs)
        
        result = {
            "items": response.get("Items", []),
            "count": len(response.get("Items", [])),
        }
        
        if "LastEvaluatedKey" in response:
            result["lastKey"] = response["LastEvaluatedKey"]["session_id"]
        
        return createResponse(200, "Sessions retrieved successfully", result)
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
