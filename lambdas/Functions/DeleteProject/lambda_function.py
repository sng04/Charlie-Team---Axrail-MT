"""
DeleteProject Lambda Function

Deletes a project by ID. Admin only (enforced by Lambda Authorizer).
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
table_name = os.environ.get("PROJECTS_TABLE")
table = dynamodb.Table(table_name)


def _get_project_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    project_id = path_params.get("projectId")
    if not project_id:
        raise BadRequestError("Project ID is required")
    return project_id


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        project_id = _get_project_id(event)
        
        response = table.delete_item(
            Key={"project_id": project_id},
            ConditionExpression="attribute_exists(project_id)",
            ReturnValues="ALL_OLD",
        )
        
        if "Attributes" not in response:
            raise NotFoundError(f"Project {project_id} not found")
        
        return createResponse(200, "Project deleted successfully")
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except ClientError as e:
        if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
            return createResponse(404, f"Project {project_id} not found")
        logger.exception("DynamoDB error")
        return createResponse(500, "Internal server error")
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
