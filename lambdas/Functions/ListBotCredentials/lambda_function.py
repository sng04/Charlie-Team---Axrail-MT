"""
ListBotCredentials Lambda Function

Lists all bot credentials from DynamoDB. Admin only (enforced by Lambda Authorizer).
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("BOT_CREDENTIALS_TABLE")
table = dynamodb.Table(table_name)


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        query_params = event.get("queryStringParameters") or {}
        limit = min(int(query_params.get("limit", 50)), 100)

        scan_kwargs = {"Limit": limit}

        if "lastKey" in query_params:
            scan_kwargs["ExclusiveStartKey"] = {
                "credential_id": query_params["lastKey"]
            }

        response = table.scan(**scan_kwargs)

        items = response.get("Items", [])
        for item in items:
            item.pop("verification_token", None)

        result = {
            "items": items,
            "count": len(items),
        }

        if "LastEvaluatedKey" in response:
            result["lastKey"] = response["LastEvaluatedKey"]["credential_id"]

        return createResponse(200, "Bot credentials retrieved successfully", result)
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
