"""
CreateBotCredential Lambda Function

Creates a new bot credential in DynamoDB and stores password in Secrets Manager.
Credential is immediately set to verified and active (no SMTP validation).
Admin only (enforced by Lambda Authorizer).
"""

import json
import os
import re
import uuid
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError, ConflictError
from url_validation import validate_email_domain
from changelog_utils import log_admin_change

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

# Only Gmail accounts are supported for meeting bot
ALLOWED_EMAIL_DOMAINS = ["gmail.com", "axrail.com"]

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
secrets_client = boto3.client("secretsmanager")

table_name = os.environ.get("BOT_CREDENTIALS_TABLE")
table = dynamodb.Table(table_name)

ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _validate_input(data: dict) -> None:
    required_fields = ["email", "password"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")

    # Validate email format
    email = data.get("email", "").strip()
    if not email or not EMAIL_REGEX.match(email):
        raise BadRequestError("Invalid email format")

    # Validate email domain is not targeting internal resources
    domain_error = validate_email_domain(email)
    if domain_error:
        raise BadRequestError(domain_error)

    # Validate email domain — only Gmail supported
    domain = email.split("@")[-1].lower()
    if domain not in ALLOWED_EMAIL_DOMAINS:
        raise BadRequestError(
            f"Email domain '{domain}' is not supported. Only Gmail accounts (gmail.com) are allowed."
        )

    # Validate password not empty
    password = data.get("password", "")
    if not password or not password.strip():
        raise BadRequestError("Password cannot be empty")

    # Validate warm_pool_size if provided
    if "warm_pool_size" in data:
        warm_pool_size = data.get("warm_pool_size")
        if not isinstance(warm_pool_size, int) or warm_pool_size < 0:
            raise BadRequestError("warm_pool_size must be a non-negative integer")


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


def _publish_validation_event(credential_id: str, email: str) -> None:
    """Publish event to EventBridge for async SMTP validation."""
    events_client.put_events(
        Entries=[
            {
                "Source": "axrail.bot-credentials",
                "DetailType": "BotCredentialValidation",
                "Detail": json.dumps({
                    "credential_id": credential_id,
                    "email": email,
                }),
                "EventBusName": EVENT_BUS_NAME,
            }
        ]
    )
    logger.info(f"Published validation event for credential {credential_id}")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        data = _parse_body(event)
        _validate_input(data)

        _check_email_exists(data["email"])

        credential_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc).isoformat()

        normalized_password = _normalize_password(data["password"])
        _store_password(credential_id, normalized_password)

        warm_pool_size = data.get("warm_pool_size", 1)
        if not isinstance(warm_pool_size, int) or warm_pool_size < 0:
            warm_pool_size = 1

        item = {
            "credential_id": credential_id,
            "email": data["email"],
            "verification_status": "verified",
            "available_status": "active",
            "warm_pool_size": warm_pool_size,
            "created_at": now,
            "updated_at": now,
        }

        table.put_item(Item=item)

        log_admin_change(event, "bot_credential", credential_id, "create", data=item, entity_name=data["email"])

        return createResponse(
            200,
            "Bot credential created and activated.",
            item,
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
