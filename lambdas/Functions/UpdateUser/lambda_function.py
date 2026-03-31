"""
UpdateUser Lambda Function

Updates user information in Cognito and DynamoDB. Admin only (enforced by Lambda Authorizer).
"""

import json
import os
from datetime import datetime
from typing import Any

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError
from changelog_utils import log_admin_change

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
cognito_client = boto3.client("cognito-idp")
DYNAMODB_TABLE = os.environ.get("DYNAMODB_TABLE")
USER_POOL_ID = os.environ.get("USER_POOL_ID")


def _parse_body(event: dict) -> dict:
    """Parse request body from event, handling both string and dict formats."""
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: Any) -> dict:
    """
    Handle update user request.

    Args:
        event: API Gateway event containing userId in path parameters and update data in body.
        context: Lambda context object.

    Returns:
        API response with updated user data.
    """
    try:
        path_params = event.get("pathParameters") or {}
        user_id = path_params.get("userId")
        
        if not user_id:
            raise BadRequestError("User ID is required")
        
        data = _parse_body(event)
        
        if not data:
            raise BadRequestError("Request body is required")
        
        table = dynamodb.Table(DYNAMODB_TABLE)
        response = table.get_item(Key={"user_id": user_id})
        
        if "Item" not in response:
            raise NotFoundError(f"User {user_id} not found")
        
        user = response["Item"]
        
        # Update email in Cognito if provided
        if "email" in data and data["email"] != user.get("email"):
            try:
                cognito_client.admin_update_user_attributes(
                    UserPoolId=USER_POOL_ID,
                    Username=user["username"],
                    UserAttributes=[
                        {"Name": "email", "Value": data["email"]},
                        {"Name": "email_verified", "Value": "true"},
                    ],
                )
                user["email"] = data["email"]
            except cognito_client.exceptions.UserNotFoundException:
                raise NotFoundError(f"User {user_id} not found in Cognito")
            except ClientError as e:
                raise BadRequestError(f"Failed to update email: {e.response['Error']['Message']}")
        
        user["updated_at"] = datetime.utcnow().isoformat()
        
        table.put_item(Item=user)
        
        log_admin_change(event, "user", user_id, "update", data=data, previous_data=user, changed_fields=list(data.keys()), entity_name=user.get("email", ""))
        
        logger.info(f"Updated user {user_id}")
        return createResponse(200, "User updated successfully", user)
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
