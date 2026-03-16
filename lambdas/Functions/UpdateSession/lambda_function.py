"""
UpdateSession Lambda Function

Updates an existing session in DynamoDB.
"""

import json
import os
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE"))
projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE"))


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _verify_project_exists(project_id: str) -> None:
    response = projects_table.get_item(Key={"project_id": project_id})
    if "Item" not in response:
        raise NotFoundError(f"Project {project_id} not found")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        path_params = event.get("pathParameters") or {}
        session_id = path_params.get("sessionId")
        
        if not session_id:
            return createResponse(400, "Missing sessionId path parameter")
        
        data = _parse_body(event)
        
        if not data:
            raise BadRequestError("No update data provided")
        
        if "project_id" in data:
            _verify_project_exists(data["project_id"])
        
        allowed_fields = ["name", "description", "meeting_link", "status", 
                         "start_time", "end_time", "project_id"]
        update_data = {k: v for k, v in data.items() if k in allowed_fields}
        
        if not update_data:
            raise BadRequestError("No valid fields to update")
        
        update_data["updated_at"] = datetime.now(timezone.utc).isoformat()
        
        parts, names, values = [], {}, {}
        for key, val in update_data.items():
            parts.append(f"#{key} = :{key}")
            names[f"#{key}"] = key
            values[f":{key}"] = val
        
        response = sessions_table.update_item(
            Key={"session_id": session_id},
            UpdateExpression="SET " + ", ".join(parts),
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values,
            ConditionExpression="attribute_exists(session_id)",
            ReturnValues="ALL_NEW",
        )
        
        return createResponse(200, "Session updated successfully", response["Attributes"])
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return createResponse(404, f"Session {session_id} not found")
        logger.exception("DynamoDB error")
        return createResponse(500, "Internal server error")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
