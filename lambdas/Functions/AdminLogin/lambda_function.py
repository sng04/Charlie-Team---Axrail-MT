"""
AdminLogin Lambda Function

Authenticates admin users via Cognito and returns JWT tokens.
"""

import json
from typing import Any

from aws_lambda_powertools import Logger, Tracer

from response_utils import createResponse
from custom_exceptions import BadRequestError, UnauthorizedError, NotFoundError
from auth_utils import admin_login

logger = Logger()
tracer = Tracer()


def _parse_body(event: dict) -> dict:
    """Parse request body from event, handling both string and dict formats."""
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _validate_login_input(data: dict) -> None:
    """Validate required fields for login."""
    required_fields = ["username", "password"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: Any) -> dict:
    """
    Handle admin login request.

    Args:
        event: API Gateway event containing login credentials.
        context: Lambda context object.

    Returns:
        API response with JWT tokens or password challenge.
    """
    try:
        data = _parse_body(event)
        _validate_login_input(data)
        
        result = admin_login(data["username"], data["password"])
        
        if "challenge" in result:
            return createResponse(200, "Password change required", result)
        
        return createResponse(200, "Admin login successful", result)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except UnauthorizedError as e:
        logger.warning(f"Unauthorized: {e}")
        return createResponse(401, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
