"""
AdminChangelog Lambda Function

Retrieves admin changelog entries with optional filters.
Route: GET /admin/changelog
"""

import os

import boto3
from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Key, Attr

from response_utils import createResponse
from custom_exceptions import BadRequestError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ.get("ADMIN_CHANGELOG_TABLE_NAME", ""))


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        params = event.get("queryStringParameters") or {}
        entity_type = params.get("entity_type")
        entity_id = params.get("entity_id")
        admin_user_id = params.get("admin_user_id")
        limit = min(100, int(params.get("limit", 20)))
        last_key = params.get("lastKey")

        if entity_type:
            # Use GSI for entity_type queries (newest first)
            query_kwargs = {
                "IndexName": "entity-type-index",
                "KeyConditionExpression": Key("entity_type").eq(entity_type),
                "ScanIndexForward": False,
                "Limit": limit,
            }
            # Add filter expressions for entity_id and admin_user_id
            filters = []
            if entity_id:
                filters.append(Attr("entity_id").eq(entity_id))
            if admin_user_id:
                filters.append(Attr("admin_user_id").eq(admin_user_id))
            if filters:
                combined = filters[0]
                for f in filters[1:]:
                    combined = combined & f
                query_kwargs["FilterExpression"] = combined

            if last_key:
                query_kwargs["ExclusiveStartKey"] = {
                    "changelog_id": last_key,
                    "entity_type": entity_type,
                    "timestamp": params.get("lastTimestamp", ""),
                }

            resp = table.query(**query_kwargs)
        else:
            # Full scan (no entity_type filter)
            scan_kwargs = {"Limit": limit}
            filters = []
            if entity_id:
                filters.append(Attr("entity_id").eq(entity_id))
            if admin_user_id:
                filters.append(Attr("admin_user_id").eq(admin_user_id))
            if filters:
                combined = filters[0]
                for f in filters[1:]:
                    combined = combined & f
                scan_kwargs["FilterExpression"] = combined

            if last_key:
                scan_kwargs["ExclusiveStartKey"] = {"changelog_id": last_key}

            resp = table.scan(**scan_kwargs)

        items = resp.get("Items", [])
        result = {"entries": items, "count": len(items)}

        if "LastEvaluatedKey" in resp:
            lek = resp["LastEvaluatedKey"]
            result["lastKey"] = lek.get("changelog_id", "")
            if "timestamp" in lek:
                result["lastTimestamp"] = lek["timestamp"]

        return createResponse(200, "Changelog retrieved", result)
    except BadRequestError as e:
        return createResponse(400, str(e))
    except Exception:
        logger.exception("Unexpected error")
        return createResponse(500, "Internal server error")
