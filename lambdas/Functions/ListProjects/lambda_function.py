"""
ListProjects Lambda Function

Lists all projects with pagination. Admin only (enforced by Lambda Authorizer).
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("PROJECTS_TABLE")
table = dynamodb.Table(table_name)


def _get_pagination_params(event: dict) -> tuple:
    query_params = event.get("queryStringParameters") or {}
    limit = min(int(query_params.get("limit", 20)), 100)
    last_key = query_params.get("lastKey")
    return limit, last_key


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        limit, last_key = _get_pagination_params(event)
        
        scan_kwargs = {"Limit": limit}
        if last_key:
            scan_kwargs["ExclusiveStartKey"] = {"project_id": last_key}
        
        response = table.scan(**scan_kwargs)
        
        result = {
            "items": response.get("Items", []),
            "count": response.get("Count", 0),
        }
        
        if "LastEvaluatedKey" in response:
            result["lastKey"] = response["LastEvaluatedKey"]["project_id"]
        
        return createResponse(200, "Projects retrieved successfully", result)
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
