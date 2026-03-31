"""
CreateUser Lambda Function

Creates a new user in Cognito and DynamoDB. Admin only (enforced by Lambda Authorizer).
"""

import json

from aws_lambda_powertools import Logger, Tracer

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError, ConflictError
from auth_utils import create_user_by_admin
from changelog_utils import log_admin_change

logger = Logger()
tracer = Tracer()


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _get_admin_email_from_context(event: dict) -> str:
    """Get admin email from authorizer context."""
    request_context = event.get("requestContext", {})
    authorizer = request_context.get("authorizer", {})
    return authorizer.get("username", "admin")


def _validate_create_user_input(data: dict) -> None:
    required_fields = ["email"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        data = _parse_body(event)
        _validate_create_user_input(data)
        
        admin_email = _get_admin_email_from_context(event)
        result = create_user_by_admin(data["email"], admin_email)
        
        log_admin_change(event, "user", result.get("user_id", ""), "create", data=result, entity_name=result.get("email", ""))
        
        return createResponse(200, "User created successfully", result)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except ConflictError as e:
        logger.warning(f"Conflict: {e}")
        return createResponse(409, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
