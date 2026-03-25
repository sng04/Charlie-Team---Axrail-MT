"""
UpdateBotCredential Lambda Function

Updates an existing bot credential. Admin only (enforced by Lambda Authorizer).
Supports updating email, password, and available_status.
If email or password is changed, triggers async SMTP re-validation.
"""

import json
import os
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError, ConflictError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
secrets_client = boto3.client("secretsmanager")
events_client = boto3.client("events")

table_name = os.environ.get("BOT_CREDENTIALS_TABLE")
table = dynamodb.Table(table_name)

ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
EVENT_BUS_NAME = os.environ.get("EVENT_BUS_NAME", "default")


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _get_credential_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    credential_id = path_params.get("credentialId")
    if not credential_id:
        raise BadRequestError("Credential ID is required")
    return credential_id


def _get_existing_credential(credential_id: str) -> dict:
    response = table.get_item(Key={"credential_id": credential_id})
    if "Item" not in response:
        raise NotFoundError(f"Bot credential {credential_id} not found")
    return response["Item"]


def _check_email_exists(email: str, exclude_credential_id: str) -> None:
    """Check if email already exists for another credential."""
    response = table.query(
        IndexName="email-index",
        KeyConditionExpression="email = :email",
        ExpressionAttributeValues={":email": email},
        Limit=1,
    )
    items = response.get("Items", [])
    for item in items:
        if item["credential_id"] != exclude_credential_id:
            raise ConflictError(f"Bot credential with email {email} already exists")


def _normalize_password(password: str) -> str:
    """Remove hyphens from password."""
    return password.replace("-", "")


def _update_password(credential_id: str, password: str) -> None:
    """Update password in Secrets Manager."""
    secret_name = f"{ENVIRONMENT}/bot-credentials/{credential_id}"
    secret_value = json.dumps({"password": password})

    try:
        secrets_client.put_secret_value(
            SecretId=secret_name,
            SecretString=secret_value,
        )
        logger.info(f"Updated secret: {secret_name}")
    except secrets_client.exceptions.ResourceNotFoundException:
        secrets_client.create_secret(
            Name=secret_name,
            Description=f"Bot credential password for {credential_id}",
            SecretString=secret_value,
        )
        logger.info(f"Created secret: {secret_name}")


def _publish_validation_event(credential_id: str, email: str, is_update: bool = False) -> None:
    """Publish event to EventBridge for async SMTP validation."""
    events_client.put_events(
        Entries=[
            {
                "Source": "axrail.bot-credentials",
                "DetailType": "BotCredentialValidation",
                "Detail": json.dumps({
                    "credential_id": credential_id,
                    "email": email,
                    "is_update": is_update,
                }),
                "EventBusName": EVENT_BUS_NAME,
            }
        ]
    )
    logger.info(f"Published validation event for credential {credential_id}")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        credential_id = _get_credential_id(event)
        data = _parse_body(event)

        if not data:
            raise BadRequestError("No update data provided")

        existing = _get_existing_credential(credential_id)

        allowed_fields = ["email", "password", "available_status", "warm_pool_size"]
        update_data = {}
        needs_revalidation = False
        new_email = existing.get("email")

        for key in allowed_fields:
            if key in data:
                if key == "email" and data[key] != existing.get("email"):
                    _check_email_exists(data[key], credential_id)
                    update_data["email"] = data[key]
                    update_data["verification_status"] = "validating"
                    new_email = data[key]
                    needs_revalidation = True
                elif key == "password":
                    normalized_password = _normalize_password(data[key])
                    _update_password(credential_id, normalized_password)
                    # Re-validate if password changed
                    if not needs_revalidation:
                        update_data["verification_status"] = "validating"
                        needs_revalidation = True
                elif key == "available_status":
                    if data[key] not in ["active", "inactive"]:
                        raise BadRequestError("available_status must be 'active' or 'inactive'")
                    update_data["available_status"] = data[key]
                elif key == "warm_pool_size":
                    if not isinstance(data[key], int) or data[key] < 1:
                        raise BadRequestError("warm_pool_size must be a positive integer")
                    update_data["warm_pool_size"] = data[key]

        if not update_data and "password" not in data:
            raise BadRequestError("No valid fields to update")

        if update_data:
            update_data["updated_at"] = datetime.now(timezone.utc).isoformat()
            
            # Remove verification_error if re-validating
            if needs_revalidation:
                update_data["verification_error"] = None

            parts, names, values = [], {}, {}
            remove_parts = []
            for key, val in update_data.items():
                if val is None:
                    remove_parts.append(f"#{key}")
                    names[f"#{key}"] = key
                else:
                    parts.append(f"#{key} = :{key}")
                    names[f"#{key}"] = key
                    values[f":{key}"] = val

            update_expr = "SET " + ", ".join(parts)
            if remove_parts:
                update_expr += " REMOVE " + ", ".join(remove_parts)

            response = table.update_item(
                Key={"credential_id": credential_id},
                UpdateExpression=update_expr,
                ExpressionAttributeNames=names,
                ExpressionAttributeValues=values if values else None,
                ReturnValues="ALL_NEW",
            )

            result = response["Attributes"]
        else:
            result = existing
            result["updated_at"] = datetime.now(timezone.utc).isoformat()
            table.update_item(
                Key={"credential_id": credential_id},
                UpdateExpression="SET updated_at = :updated_at",
                ExpressionAttributeValues={":updated_at": result["updated_at"]},
            )

        # Trigger async SMTP validation if email or password changed
        if needs_revalidation:
            _publish_validation_event(credential_id, new_email, is_update=True)

        # Remove internal fields from response
        result.pop("verification_token", None)
        result.pop("verification_error", None)

        message = "Bot credential updated successfully"
        if needs_revalidation:
            message += ". Re-validating email credentials..."

        return createResponse(200, message, result)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except ConflictError as e:
        logger.warning(f"Conflict: {e}")
        return createResponse(409, str(e))
    except ClientError as e:
        logger.exception(f"AWS error: {e}")
        return createResponse(500, "Internal server error")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
