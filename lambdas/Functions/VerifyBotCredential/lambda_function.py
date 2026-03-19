"""
VerifyBotCredential Lambda Function

Verifies a bot credential email using the verification token.
This endpoint is public (no auth required) as it's accessed via email link.
"""

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
table_name = os.environ.get("BOT_CREDENTIALS_TABLE")
table = dynamodb.Table(table_name)


def _get_credential_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    credential_id = path_params.get("credentialId")
    if not credential_id:
        raise BadRequestError("Credential ID is required")
    return credential_id


def _get_token(event: dict) -> str:
    query_params = event.get("queryStringParameters") or {}
    token = query_params.get("token")
    if not token:
        raise BadRequestError("Verification token is required")
    return token


def _get_credential(credential_id: str) -> dict:
    response = table.get_item(Key={"credential_id": credential_id})
    if "Item" not in response:
        raise NotFoundError(f"Bot credential {credential_id} not found")
    return response["Item"]


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        credential_id = _get_credential_id(event)
        token = _get_token(event)

        credential = _get_credential(credential_id)

        if credential.get("verification_status") == "verified":
            return createResponse(200, "Email already verified", {
                "credential_id": credential_id,
                "email": credential["email"],
                "verification_status": "verified",
            })

        stored_token = credential.get("verification_token")
        if not stored_token or stored_token != token:
            raise BadRequestError("Invalid or expired verification token")

        now = datetime.now(timezone.utc).isoformat()

        table.update_item(
            Key={"credential_id": credential_id},
            UpdateExpression="SET verification_status = :status, updated_at = :updated_at REMOVE verification_token",
            ExpressionAttributeValues={
                ":status": "verified",
                ":updated_at": now,
            },
        )

        logger.info(f"Bot credential {credential_id} verified successfully")

        return createResponse(200, "Email verified successfully", {
            "credential_id": credential_id,
            "email": credential["email"],
            "verification_status": "verified",
        })
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except ClientError as e:
        logger.exception(f"AWS error: {e}")
        return createResponse(500, "Internal server error")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
