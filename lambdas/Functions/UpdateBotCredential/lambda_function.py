"""
UpdateBotCredential Lambda Function

Updates an existing bot credential. Admin only (enforced by Lambda Authorizer).
Supports updating email, password, and available_status.
If email is changed, resets verification_status to not_verified and sends new verification email.
"""

import json
import os
import uuid
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
ses_client = boto3.client("ses")

table_name = os.environ.get("BOT_CREDENTIALS_TABLE")
table = dynamodb.Table(table_name)

ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
API_ENDPOINT = os.environ.get("API_ENDPOINT", "")
SES_SENDER_EMAIL = os.environ.get("SES_SENDER_EMAIL", "noreply@axrail.com")


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


def _send_verification_email(email: str, credential_id: str, token: str) -> None:
    """Send verification email via SES."""
    if not API_ENDPOINT:
        logger.warning("API_ENDPOINT not configured, skipping verification email")
        return

    verification_link = f"{API_ENDPOINT}/bot-credentials/{credential_id}/verify?token={token}"

    subject = "Verify your Bot Credential Email - AXRAIL Meeting Assistant"
    body_html = f"""
    <html>
    <body>
        <h2>Email Verification Required</h2>
        <p>Your bot credential email has been updated. Please verify the new email:</p>
        <p><a href="{verification_link}">Verify Email</a></p>
        <p>Or copy and paste this URL into your browser:</p>
        <p>{verification_link}</p>
        <p>This link will expire in 24 hours.</p>
        <br>
        <p>Best regards,<br>AXRAIL Meeting Assistant Team</p>
    </body>
    </html>
    """
    body_text = f"""
    Email Verification Required

    Your bot credential email has been updated. Please verify the new email:
    {verification_link}

    This link will expire in 24 hours.

    Best regards,
    AXRAIL Meeting Assistant Team
    """

    try:
        ses_client.send_email(
            Source=SES_SENDER_EMAIL,
            Destination={"ToAddresses": [email]},
            Message={
                "Subject": {"Data": subject, "Charset": "UTF-8"},
                "Body": {
                    "Text": {"Data": body_text, "Charset": "UTF-8"},
                    "Html": {"Data": body_html, "Charset": "UTF-8"},
                },
            },
        )
        logger.info(f"Verification email sent to: {email}")
    except ClientError as e:
        logger.error(f"Failed to send verification email: {e}")
        raise


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        credential_id = _get_credential_id(event)
        data = _parse_body(event)

        if not data:
            raise BadRequestError("No update data provided")

        existing = _get_existing_credential(credential_id)

        allowed_fields = ["email", "password", "available_status"]
        update_data = {}
        email_changed = False
        verification_token = None

        for key in allowed_fields:
            if key in data:
                if key == "email" and data[key] != existing.get("email"):
                    _check_email_exists(data[key], credential_id)
                    update_data["email"] = data[key]
                    update_data["verification_status"] = "not_verified"
                    verification_token = str(uuid.uuid4())
                    update_data["verification_token"] = verification_token
                    email_changed = True
                elif key == "password":
                    normalized_password = _normalize_password(data[key])
                    _update_password(credential_id, normalized_password)
                elif key == "available_status":
                    if data[key] not in ["active", "inactive"]:
                        raise BadRequestError("available_status must be 'active' or 'inactive'")
                    update_data["available_status"] = data[key]

        if not update_data and "password" not in data:
            raise BadRequestError("No valid fields to update")

        if update_data:
            update_data["updated_at"] = datetime.now(timezone.utc).isoformat()

            parts, names, values = [], {}, {}
            for key, val in update_data.items():
                parts.append(f"#{key} = :{key}")
                names[f"#{key}"] = key
                values[f":{key}"] = val

            response = table.update_item(
                Key={"credential_id": credential_id},
                UpdateExpression="SET " + ", ".join(parts),
                ExpressionAttributeNames=names,
                ExpressionAttributeValues=values,
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

        if email_changed and verification_token:
            _send_verification_email(data["email"], credential_id, verification_token)

        result.pop("verification_token", None)

        message = "Bot credential updated successfully"
        if email_changed:
            message += ". Verification email sent to new address."

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
