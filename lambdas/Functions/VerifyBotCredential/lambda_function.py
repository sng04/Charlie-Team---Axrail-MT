"""
VerifyBotCredential Lambda Function

Returns the current verification status of a bot credential.
Frontend can poll this endpoint to check if async SMTP validation is complete.
"""

import os

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


def _get_credential(credential_id: str) -> dict:
    response = table.get_item(Key={"credential_id": credential_id})
    if "Item" not in response:
        raise NotFoundError(f"Bot credential {credential_id} not found")
    return response["Item"]


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    Get verification status of a bot credential.
    
    Returns:
    - verification_status: "validating" | "verified" | "invalid"
    - verification_error: error message if status is "invalid"
    """
    try:
        credential_id = _get_credential_id(event)
        credential = _get_credential(credential_id)

        response_data = {
            "credential_id": credential_id,
            "email": credential["email"],
            "verification_status": credential.get("verification_status", "unknown"),
        }
        
        # Include error message if validation failed
        if credential.get("verification_error"):
            response_data["verification_error"] = credential["verification_error"]

        status = credential.get("verification_status")
        if status == "verified":
            message = "Email credentials verified successfully"
        elif status == "validating":
            message = "Validation in progress..."
        elif status == "invalid":
            message = "Email credentials validation failed"
        else:
            message = "Unknown verification status"

        return createResponse(200, message, response_data)
        
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
