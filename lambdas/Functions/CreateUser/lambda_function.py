import json

from aws_lambda_powertools import Logger, Tracer

from response_utils import createResponse
from custom_exceptions import BadRequestError, UnauthorizedError, NotFoundError, ConflictError
from auth_utils import create_user_by_admin, verify_admin_role

logger = Logger()
tracer = Tracer()


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _get_authorization_token(event: dict) -> str:
    headers = event.get("headers", {})
    auth = headers.get("Authorization") or headers.get("authorization")
    if not auth:
        raise UnauthorizedError("Authorization header missing")
    return auth.replace("Bearer ", "")


def _validate_create_user_input(data: dict) -> None:
    required_fields = ["email"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        access_token = _get_authorization_token(event)
        admin_info = verify_admin_role(access_token)
        
        data = _parse_body(event)
        _validate_create_user_input(data)
        
        result = create_user_by_admin(data["email"], admin_info["email"])
        
        return createResponse(200, "User created successfully", result)
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except UnauthorizedError as e:
        logger.warning(f"Unauthorized: {e}")
        return createResponse(401, str(e))
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
