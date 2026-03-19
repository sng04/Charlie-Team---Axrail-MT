"""
CreateBotCredential Lambda Function

Creates a new bot credential in DynamoDB and stores password in Secrets Manager.
Sends verification email via SES. Admin only (enforced by Lambda Authorizer).
"""

import json
import os
import uuid
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError, ConflictError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
secrets_client = boto3.client("secretsmanager")
ses_client = boto3.client("ses")
ssm_client = boto3.client("ssm")

table_name = os.environ.get("BOT_CREDENTIALS_TABLE")
table = dynamodb.Table(table_name)

ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")
API_ENDPOINT = os.environ.get("API_ENDPOINT", "")
SES_SENDER_EMAIL_PARAM = os.environ.get("SES_SENDER_EMAIL_PARAM", "")

_ses_sender_email_cache = None


def _get_ses_sender_email() -> str:
    """Get SES sender email from SSM Parameter Store with caching."""
    global _ses_sender_email_cache
    if _ses_sender_email_cache:
        return _ses_sender_email_cache

    if not SES_SENDER_EMAIL_PARAM:
        logger.warning("SES_SENDER_EMAIL_PARAM not configured")
        return ""

    try:
        response = ssm_client.get_parameter(Name=SES_SENDER_EMAIL_PARAM)
        _ses_sender_email_cache = response["Parameter"]["Value"]
        return _ses_sender_email_cache
    except Exception as e:
        logger.error(f"Failed to get SES sender email from SSM: {e}")
        return ""


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _validate_input(data: dict) -> None:
    required_fields = ["email", "password"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


def _normalize_password(password: str) -> str:
    """Remove hyphens from password (e.g., 'xxxx-xxxx-xxxx-xxxx' -> 'xxxxxxxxxxxxxxxx')."""
    return password.replace("-", "")


def _check_email_exists(email: str) -> None:
    """Check if email already exists in BotCredentials table."""
    response = table.query(
        IndexName="email-index",
        KeyConditionExpression="email = :email",
        ExpressionAttributeValues={":email": email},
        Limit=1,
    )
    if response.get("Items"):
        raise ConflictError(f"Bot credential with email {email} already exists")


def _store_password(credential_id: str, password: str) -> None:
    """Store password in Secrets Manager."""
    secret_name = f"{ENVIRONMENT}/bot-credentials/{credential_id}"
    secret_value = json.dumps({"password": password})

    try:
        secrets_client.create_secret(
            Name=secret_name,
            Description=f"Bot credential password for {credential_id}",
            SecretString=secret_value,
        )
        logger.info(f"Created secret: {secret_name}")
    except secrets_client.exceptions.ResourceExistsException:
        secrets_client.put_secret_value(
            SecretId=secret_name,
            SecretString=secret_value,
        )
        logger.info(f"Updated secret: {secret_name}")


def _generate_verification_token() -> str:
    """Generate a unique verification token."""
    return str(uuid.uuid4())


def _send_verification_email(email: str, credential_id: str, token: str) -> None:
    """Send verification email via SES."""
    if not API_ENDPOINT:
        logger.warning("API_ENDPOINT not configured, skipping verification email")
        return

    sender_email = _get_ses_sender_email()
    if not sender_email:
        logger.warning("SES sender email not configured, skipping verification email")
        return

    verification_link = f"{API_ENDPOINT}/bot-credentials/{credential_id}/verify?token={token}"

    subject = "Verify your Bot Credential Email - AXRAIL Meeting Assistant"
    body_html = f"""
    <html>
    <body>
        <h2>Email Verification Required</h2>
        <p>Please click the link below to verify your bot credential email:</p>
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

    Please visit the following link to verify your bot credential email:
    {verification_link}

    This link will expire in 24 hours.

    Best regards,
    AXRAIL Meeting Assistant Team
    """

    try:
        ses_client.send_email(
            Source=sender_email,
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
        data = _parse_body(event)
        _validate_input(data)

        _check_email_exists(data["email"])

        credential_id = str(uuid.uuid4())
        verification_token = _generate_verification_token()
        now = datetime.now(timezone.utc).isoformat()

        normalized_password = _normalize_password(data["password"])
        _store_password(credential_id, normalized_password)

        item = {
            "credential_id": credential_id,
            "email": data["email"],
            "verification_status": "not_verified",
            "verification_token": verification_token,
            "available_status": "inactive",
            "created_at": now,
            "updated_at": now,
        }

        table.put_item(Item=item)

        _send_verification_email(data["email"], credential_id, verification_token)

        response_item = {k: v for k, v in item.items() if k != "verification_token"}

        return createResponse(
            200,
            "Bot credential created successfully. Verification email sent.",
            response_item,
        )
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
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
