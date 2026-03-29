"""
UpdateProject Lambda Function

Updates an existing project. Admin only (enforced by Lambda Authorizer).
Supports assigning/unassigning bot_credential_id.
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
table_name = os.environ.get("PROJECTS_TABLE")
table = dynamodb.Table(table_name)

bot_credentials_table_name = os.environ.get("BOT_CREDENTIALS_TABLE")
bot_credentials_table = dynamodb.Table(bot_credentials_table_name)


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _get_project_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    project_id = path_params.get("projectId")
    if not project_id:
        raise BadRequestError("Project ID is required")
    return project_id


def _validate_bot_credential(credential_id: str) -> None:
    """Validate that bot credential exists, is verified, and is active."""
    if not credential_id:
        return

    response = bot_credentials_table.get_item(Key={"credential_id": credential_id})
    if "Item" not in response:
        raise NotFoundError(f"Bot credential {credential_id} not found")

    credential = response["Item"]

    if credential.get("verification_status") != "verified":
        raise BadRequestError(
            f"Bot credential {credential_id} is not verified. "
            "Please verify the email before assigning to a project."
        )

    if credential.get("available_status") != "active":
        raise BadRequestError(
            f"Bot credential {credential_id} is not active. "
            "Please activate the credential before assigning to a project."
        )


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        project_id = _get_project_id(event)
        data = _parse_body(event)

        if not data:
            raise BadRequestError("No update data provided")

        allowed_fields = ["name", "description", "email", "s3_arn", "bot_credential_id", "agent_id"]
        update_data = {}

        for key in allowed_fields:
            if key in data:
                if key == "bot_credential_id":
                    if data[key] is not None and data[key] != "":
                        _validate_bot_credential(data[key])
                    update_data[key] = data[key] if data[key] else None
                else:
                    update_data[key] = data[key]

        if not update_data:
            raise BadRequestError("No valid fields to update")

        update_data["updated_at"] = datetime.now(timezone.utc).isoformat()

        parts, names, values = [], {}, {}
        remove_parts = []

        for key, val in update_data.items():
            if val is None and key == "bot_credential_id":
                remove_parts.append(f"#{key}")
                names[f"#{key}"] = key
            else:
                parts.append(f"#{key} = :{key}")
                names[f"#{key}"] = key
                values[f":{key}"] = val

        update_expression = ""
        if parts:
            update_expression = "SET " + ", ".join(parts)
        if remove_parts:
            if update_expression:
                update_expression += " REMOVE " + ", ".join(remove_parts)
            else:
                update_expression = "REMOVE " + ", ".join(remove_parts)

        response = table.update_item(
            Key={"project_id": project_id},
            UpdateExpression=update_expression,
            ExpressionAttributeNames=names,
            ExpressionAttributeValues=values if values else None,
            ConditionExpression="attribute_exists(project_id)",
            ReturnValues="ALL_NEW",
        )

        return createResponse(200, "Project updated successfully", response["Attributes"])
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return createResponse(404, f"Project {project_id} not found")
        logger.exception("DynamoDB error")
        return createResponse(500, "Internal server error")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
