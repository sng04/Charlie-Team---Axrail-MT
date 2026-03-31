"""
CreateProject Lambda Function

Creates a new project in DynamoDB. Admin only (enforced by Lambda Authorizer).
"""

import json
import os
import uuid
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Attr, Key

from response_utils import createResponse
from custom_exceptions import BadRequestError
from changelog_utils import log_admin_change

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("PROJECTS_TABLE")
table = dynamodb.Table(table_name)


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _validate_input(data: dict) -> None:
    required_fields = ["name", "email"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        data = _parse_body(event)
        _validate_input(data)

        # Check for duplicate name via GSI query
        existing = table.query(
            IndexName="name-index",
            KeyConditionExpression=Key("name").eq(data["name"]),
        )
        if existing.get("Items"):
            return createResponse(409, "A project with this name already exists")
        
        project_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc).isoformat()
        
        item = {
            "project_id": project_id,
            "name": data["name"],
            "description": data.get("description", ""),
            "email": data["email"],
            "s3_arn": data.get("s3_arn", ""),
            "created_at": now,
            "updated_at": now,
        }
        
        table.put_item(Item=item)
        
        log_admin_change(event, "project", project_id, "create", data=item, entity_name=item.get("name", ""))
        
        return createResponse(200, "Project created successfully", item)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
