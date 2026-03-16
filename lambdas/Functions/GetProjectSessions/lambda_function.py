"""
GetProjectSessions Lambda Function

Retrieves all sessions for a specific project using GSI.
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

from response_utils import createResponse
from custom_exceptions import NotFoundError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE"))
projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE"))


def _verify_project_exists(project_id: str) -> None:
    response = projects_table.get_item(Key={"project_id": project_id})
    if "Item" not in response:
        raise NotFoundError(f"Project {project_id} not found")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        path_params = event.get("pathParameters") or {}
        project_id = path_params.get("projectId")
        
        if not project_id:
            return createResponse(400, "Missing projectId path parameter")
        
        _verify_project_exists(project_id)
        
        query_params = event.get("queryStringParameters") or {}
        limit = min(int(query_params.get("limit", 20)), 100)
        
        query_kwargs = {
            "IndexName": "project-index",
            "KeyConditionExpression": Key("project_id").eq(project_id),
            "Limit": limit,
        }
        
        last_key = query_params.get("lastKey")
        if last_key:
            query_kwargs["ExclusiveStartKey"] = {
                "session_id": last_key,
                "project_id": project_id,
            }
        
        response = sessions_table.query(**query_kwargs)
        
        result = {
            "project_id": project_id,
            "items": response.get("Items", []),
            "count": len(response.get("Items", [])),
        }
        
        if "LastEvaluatedKey" in response:
            result["lastKey"] = response["LastEvaluatedKey"]["session_id"]
        
        return createResponse(200, "Project sessions retrieved successfully", result)
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
