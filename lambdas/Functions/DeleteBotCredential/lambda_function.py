"""
DeleteBotCredential Lambda Function

Deletes a bot credential from DynamoDB and its password from Secrets Manager.
Checks if credential is assigned to any project before deletion.
Admin only (enforced by Lambda Authorizer).
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError, ConflictError
from changelog_utils import log_admin_change

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
secrets_client = boto3.client("secretsmanager")

table_name = os.environ.get("BOT_CREDENTIALS_TABLE")
table = dynamodb.Table(table_name)

projects_table_name = os.environ.get("PROJECTS_TABLE")
projects_table = dynamodb.Table(projects_table_name)

ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")


def _get_credential_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    credential_id = path_params.get("credentialId")
    if not credential_id:
        raise BadRequestError("Credential ID is required")
    return credential_id


def _verify_credential_exists(credential_id: str) -> None:
    response = table.get_item(Key={"credential_id": credential_id})
    if "Item" not in response:
        raise NotFoundError(f"Bot credential {credential_id} not found")


def _check_credential_in_use(credential_id: str) -> None:
    """Check if credential is assigned to any project."""
    response = projects_table.scan(
        FilterExpression="bot_credential_id = :cred_id",
        ExpressionAttributeValues={":cred_id": credential_id},
    )
    projects = response.get("Items", [])
    if projects:
        project_names = [p.get("name", p["project_id"]) for p in projects]
        raise ConflictError(
            f"Bot credential is assigned to {len(projects)} project(s): {', '.join(project_names)}. "
            "Remove assignment before deleting."
        )


def _delete_secret(credential_id: str) -> None:
    """Delete password from Secrets Manager."""
    secret_name = f"{ENVIRONMENT}/bot-credentials/{credential_id}"
    try:
        secrets_client.delete_secret(
            SecretId=secret_name,
            ForceDeleteWithoutRecovery=True,
        )
        logger.info(f"Deleted secret: {secret_name}")
    except secrets_client.exceptions.ResourceNotFoundException:
        logger.warning(f"Secret not found: {secret_name}")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        credential_id = _get_credential_id(event)

        # Fetch before delete for changelog
        pre_delete = table.get_item(Key={"credential_id": credential_id})
        if "Item" not in pre_delete:
            raise NotFoundError(f"Bot credential {credential_id} not found")

        _check_credential_in_use(credential_id)

        _delete_secret(credential_id)

        table.delete_item(Key={"credential_id": credential_id})

        log_admin_change(event, "bot_credential", credential_id, "delete", previous_data=pre_delete["Item"], entity_name=pre_delete["Item"].get("email", ""))

        return createResponse(200, "Bot credential deleted successfully")
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
