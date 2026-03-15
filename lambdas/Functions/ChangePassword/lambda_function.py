"""
ChangePassword Lambda Function

Handles NEW_PASSWORD_REQUIRED challenge from Cognito for first-time login.
"""

import json
from typing import Any

from aws_lambda_powertools import Logger, Tracer

from response_utils import createResponse
from custom_exceptions import BadRequestError, UnauthorizedError
from auth_utils import respond_to_new_password_challenge

logger = Logger()
tracer = Tracer()


def _parse_body(event: dict) -> dict:
    """Parse request body from event, handling both string and dict formats."""
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _validate_change_password_input(data: dict) -> None:
    """Validate required fields for password change."""
    required_fields = ["session", "username", "new_password"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: Any) -> dict:
    """
    Handle password change request for NEW_PASSWORD_REQUIRED challenge.

    Args:
        event: API Gateway event containing session, username, and new password.
        context: Lambda context object.

    Returns:
        API response with JWT tokens after successful password change.
    """
    try:
        data = _parse_body(event)
        _validate_change_password_input(data)
        
        result = respond_to_new_password_challenge(
            data["session"],
            data["username"],
            data["new_password"]
        )
        
        return createResponse(200, "Password changed successfully", result)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except UnauthorizedError as e:
        logger.warning(f"Unauthorized: {e}")
        return createResponse(401, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
