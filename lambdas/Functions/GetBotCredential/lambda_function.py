"""
GetBotCredential Lambda Function

Retrieves a single bot credential by ID from DynamoDB.
Admin only (enforced by Lambda Authorizer).
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3

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


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        credential_id = _get_credential_id(event)

        response = table.get_item(Key={"credential_id": credential_id})

        if "Item" not in response:
            raise NotFoundError(f"Bot credential {credential_id} not found")

        item = response["Item"]
        item.pop("verification_token", None)

        return createResponse(200, "Bot credential retrieved successfully", item)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
