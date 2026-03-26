"""
ValidateBotCredentialWorker Lambda Function

Async worker triggered by EventBridge to validate bot credentials via SMTP.
Updates credential status to 'verified' or 'invalid' based on SMTP login result.
"""

import dns.resolver
import json
import os
import smtplib
import ssl
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
secrets_client = boto3.client("secretsmanager")

table_name = os.environ.get("BOT_CREDENTIALS_TABLE")
table = dynamodb.Table(table_name)
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")

# Known SMTP servers by email domain
KNOWN_SMTP_SERVERS = {
    "gmail.com": {"host": "smtp.gmail.com", "port": 587},
    "googlemail.com": {"host": "smtp.gmail.com", "port": 587},
    "outlook.com": {"host": "smtp.office365.com", "port": 587},
    "hotmail.com": {"host": "smtp.office365.com", "port": 587},
    "live.com": {"host": "smtp.office365.com", "port": 587},
    "yahoo.com": {"host": "smtp.mail.yahoo.com", "port": 587},
    "icloud.com": {"host": "smtp.mail.me.com", "port": 587},
    "me.com": {"host": "smtp.mail.me.com", "port": 587},
    "zoho.com": {"host": "smtp.zoho.com", "port": 587},
}

# MX record patterns to detect email provider
MX_PATTERNS = {
    "google": {"host": "smtp.gmail.com", "port": 587},  # Google Workspace
    "outlook": {"host": "smtp.office365.com", "port": 587},  # Microsoft 365
    "microsoft": {"host": "smtp.office365.com", "port": 587},  # Microsoft 365
}


def _detect_smtp_from_mx(domain: str) -> dict | None:
    """Detect SMTP server from MX records (for custom domains like Google Workspace)."""
    try:
        mx_records = dns.resolver.resolve(domain, "MX")
        for mx in mx_records:
            mx_host = str(mx.exchange).lower()
            logger.info(f"MX record for {domain}: {mx_host}")
            
            for pattern, config in MX_PATTERNS.items():
                if pattern in mx_host:
                    logger.info(f"Detected {pattern} for domain {domain}")
                    return config
        return None
    except Exception as e:
        logger.warning(f"Failed to lookup MX for {domain}: {e}")
        return None


def _get_smtp_server(email: str) -> dict | None:
    """Get SMTP server config based on email domain."""
    domain = email.split("@")[-1].lower()
    
    # Check known domains first
    if domain in KNOWN_SMTP_SERVERS:
        return KNOWN_SMTP_SERVERS[domain]
    
    # Try to detect from MX records (for custom domains)
    return _detect_smtp_from_mx(domain)


def _get_password(credential_id: str) -> str:
    """Retrieve password from Secrets Manager."""
    secret_name = f"{ENVIRONMENT}/bot-credentials/{credential_id}"
    response = secrets_client.get_secret_value(SecretId=secret_name)
    secret = json.loads(response["SecretString"])
    return secret["password"]


def _validate_smtp(email: str, password: str) -> tuple[bool, str]:
    """
    Validate email credentials via SMTP login.
    Returns (success: bool, error_message: str).
    """
    smtp_config = _get_smtp_server(email)
    if not smtp_config:
        domain = email.split("@")[-1]
        return False, f"Unsupported email domain: {domain}"

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_config["host"], smtp_config["port"], timeout=15) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(email, password)
            server.quit()
        return True, ""
    except smtplib.SMTPAuthenticationError as e:
        logger.warning(f"SMTP auth failed for {email}: {e}")
        return False, "Invalid email or password. For Gmail/Outlook, use App Password if 2FA is enabled."
    except smtplib.SMTPException as e:
        logger.error(f"SMTP error for {email}: {e}")
        return False, f"SMTP error: {str(e)}"
    except TimeoutError:
        logger.error(f"SMTP timeout for {email}")
        return False, "Connection timeout. Please try again."
    except Exception as e:
        logger.exception(f"Unexpected error validating {email}")
        return False, f"Validation error: {str(e)}"


def _update_credential_status(credential_id: str, status: str, error_message: str = None) -> None:
    """Update credential verification status in DynamoDB.
    
    If status is 'verified', also set available_status to 'active'.
    """
    now = datetime.now(timezone.utc).isoformat()
    
    update_expr = "SET verification_status = :status, updated_at = :updated_at"
    expr_values = {
        ":status": status,
        ":updated_at": now,
    }
    
    # Auto-activate when verified
    if status == "verified":
        update_expr += ", available_status = :available"
        expr_values[":available"] = "active"
    
    if error_message:
        update_expr += ", verification_error = :error"
        expr_values[":error"] = error_message
    else:
        update_expr += " REMOVE verification_error"
    
    table.update_item(
        Key={"credential_id": credential_id},
        UpdateExpression=update_expr,
        ExpressionAttributeValues=expr_values,
    )
    logger.info(f"Updated credential {credential_id} status to {status}")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    Handle EventBridge event for bot credential validation.
    
    Event detail structure:
    {
        "credential_id": "uuid",
        "email": "user@example.com"
    }
    """
    try:
        detail = event.get("detail", {})
        credential_id = detail.get("credential_id")
        email = detail.get("email")
        
        if not credential_id or not email:
            logger.error(f"Missing required fields in event: {event}")
            return {"statusCode": 400, "body": "Missing credential_id or email"}
        
        logger.info(f"Validating credential {credential_id} for email {email}")
        
        # Get password from Secrets Manager
        try:
            password = _get_password(credential_id)
        except ClientError as e:
            logger.error(f"Failed to get password for {credential_id}: {e}")
            _update_credential_status(credential_id, "invalid", "Failed to retrieve credentials")
            return {"statusCode": 500, "body": "Failed to retrieve credentials"}
        
        # Validate via SMTP
        is_valid, error_message = _validate_smtp(email, password)
        
        if is_valid:
            _update_credential_status(credential_id, "verified")
            logger.info(f"Credential {credential_id} verified successfully")
            return {"statusCode": 200, "body": "Credential verified"}
        else:
            # Mark as verification_failed but keep the credential
            _update_credential_status(credential_id, "verification_failed", error_message)
            logger.warning(f"Credential {credential_id} validation failed: {error_message}")
            return {"statusCode": 200, "body": f"Credential verification failed: {error_message}"}
            
    except Exception as e:
        logger.exception("Unexpected error in validation worker")
        return {"statusCode": 500, "body": str(e)}
