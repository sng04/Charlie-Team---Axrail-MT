"""
SetProjectBotCredentials Lambda Function

Sets Gmail bot credentials for a project in Secrets Manager.
Admin only (enforced by Lambda Authorizer).
"""

import json
import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
secrets_client = boto3.client("secretsmanager")

projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE"))
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _get_project_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    project_id = path_params.get("projectId")
    if not project_id:
        raise BadRequestError("Project ID is required")
    return project_id


def _validate_input(data: dict) -> None:
    required_fields = ["bot_email", "bot_password"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


def _normalize_password(password: str) -> str:
    """Remove hyphens from password (e.g., 'xxxx-xxxx-xxxx-xxxx' -> 'xxxxxxxxxxxxxxxx')."""
    return password.replace("-", "")


def _verify_project_exists(project_id: str) -> None:
    response = projects_table.get_item(Key={"project_id": project_id})
    if "Item" not in response:
        raise NotFoundError(f"Project {project_id} not found")


def _store_credentials(project_id: str, email: str, password: str) -> None:
    """Store credentials in Secrets Manager."""
    secret_name = f"{ENVIRONMENT}/{project_id}/gmail-credentials"
    secret_value = json.dumps({"email": email, "password": password})

    try:
        secrets_client.put_secret_value(
            SecretId=secret_name,
            SecretString=secret_value,
        )
        logger.info(f"Updated secret: {secret_name}")
    except secrets_client.exceptions.ResourceNotFoundException:
        secrets_client.create_secret(
            Name=secret_name,
            Description=f"Gmail bot credentials for project {project_id}",
            SecretString=secret_value,
        )
        logger.info(f"Created secret: {secret_name}")


def _update_project_bot_email(project_id: str, bot_email: str) -> None:
    """Update project with bot_email field."""
    projects_table.update_item(
        Key={"project_id": project_id},
        UpdateExpression="SET bot_email = :email",
        ExpressionAttributeValues={":email": bot_email},
    )


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        project_id = _get_project_id(event)
        data = _parse_body(event)
        _validate_input(data)
        _verify_project_exists(project_id)

        normalized_password = _normalize_password(data["bot_password"])

        _store_credentials(project_id, data["bot_email"], normalized_password)

        _update_project_bot_email(project_id, data["bot_email"])

        return createResponse(
            200,
            "Bot credentials set successfully",
            {"project_id": project_id, "bot_email": data["bot_email"]},
        )
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except ClientError as e:
        logger.exception(f"AWS error: {e}")
        return createResponse(500, "Failed to store credentials")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
