"""
UpdateProject Lambda Function

Updates an existing project. Admin only (enforced by Lambda Authorizer).
"""

import json
import os
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("PROJECTS_TABLE")
table = dynamodb.Table(table_name)


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _get_project_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    project_id = path_params.get("projectId")
    if not project_id:
        raise BadRequestError("Project ID is required")
    return project_id


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        project_id = _get_project_id(event)
        data = _parse_body(event)
        
        if not data:
            raise BadRequestError("No update data provided")
        
        allowed_fields = ["name", "description", "email", "s3_arn"]
        update_data = {k: v for k, v in data.items() if k in allowed_fields}
        
        if not update_data:
            raise BadRequestError("No valid fields to update")
        
        update_data["updated_at"] = datetime.now(timezone.utc).isoformat()
        
        parts, names, values = [], {}, {}
        for key, val in update_data.items():
            parts.append(f"#{key} = :{key}")
            names[f"#{key}"] = key
            values[f":{key}"] = val
        
        response = table.update_item(
            Key={"project_id": project_id},
            UpdateExpression="SET " + ", ".join(parts),
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ConditionExpression="attribute_exists(project_id)",
            ReturnValues="ALL_NEW",
        )
        
        return createResponse(200, "Project updated successfully", response["Attributes"])
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return createResponse(404, f"Project {project_id} not found")
        logger.exception("DynamoDB error")
        return createResponse(500, "Internal server error")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
