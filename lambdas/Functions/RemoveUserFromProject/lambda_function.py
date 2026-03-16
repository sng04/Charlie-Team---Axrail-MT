"""
RemoveUserFromProject Lambda Function

Removes a user from a project (deletes project_user record). Admin only (enforced by Lambda Authorizer).
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
table_name = os.environ.get("PROJECT_USERS_TABLE")
table = dynamodb.Table(table_name)


def _get_project_user_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    project_user_id = path_params.get("projectUserId")
    if not project_user_id:
        raise BadRequestError("Project User ID is required")
    return project_user_id


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        project_user_id = _get_project_user_id(event)
        
        response = table.delete_item(
            Key={"project_user_id": project_user_id},
            ConditionExpression="attribute_exists(project_user_id)",
            ReturnValues="ALL_OLD",
        )
        
        if "Attributes" not in response:
            return createResponse(404, f"Assignment {project_user_id} not found")
        
        return createResponse(200, "User removed from project successfully")
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return createResponse(404, f"Assignment {project_user_id} not found")
        logger.exception("DynamoDB error")
        return createResponse(500, "Internal server error")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
