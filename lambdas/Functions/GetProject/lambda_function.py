"""
GetProject Lambda Function

Retrieves a single project by ID. Admin only (enforced by Lambda Authorizer).
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError

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
        
        response = table.get_item(Key={"project_id": project_id})
        
        if "Item" not in response:
            raise NotFoundError(f"Project {project_id} not found")
        
        return createResponse(200, "Project retrieved successfully", response["Item"])
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
