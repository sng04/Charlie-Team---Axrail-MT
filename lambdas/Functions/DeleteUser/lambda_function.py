"""
DeleteUser Lambda Function

Deletes a user from Cognito and DynamoDB. Admin only (enforced by Lambda Authorizer).
"""

import os
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


@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: Any) -> dict:
    """
    Handle delete user request.

    Args:
        event: API Gateway event containing userId in path parameters.
        context: Lambda context object.

    Returns:
        API response confirming deletion.
    """
    try:
        path_params = event.get("pathParameters") or {}
        user_id = path_params.get("userId")
        
        if not user_id:
            raise BadRequestError("User ID is required")
        
        table = dynamodb.Table(DYNAMODB_TABLE)
        response = table.get_item(Key={"user_id": user_id})
        
        if "Item" not in response:
            raise NotFoundError(f"User {user_id} not found")
        
        user = response["Item"]
        username = user.get("username")
        
        # Delete from Cognito
        if username:
            try:
                cognito_client.admin_delete_user(
                    UserPoolId=USER_POOL_ID,
                    Username=username,
                )
                logger.info(f"Deleted user {username} from Cognito")
            except cognito_client.exceptions.UserNotFoundException:
                logger.warning(f"User {username} not found in Cognito, continuing with DynamoDB deletion")
            except ClientError as e:
                raise BadRequestError(f"Failed to delete from Cognito: {e.response['Error']['Message']}")
        
        # Delete from DynamoDB
        table.delete_item(Key={"user_id": user_id})
        
        log_admin_change(event, "user", user_id, "delete", previous_data=user, entity_name=user.get("email", ""))
        
        logger.info(f"Deleted user {user_id}")
        return createResponse(200, "User deleted successfully")
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
