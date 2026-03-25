"""
ListBotPool Lambda Function

Lists bot pool containers for a specific credential.
Returns detailed information about each container including status, task_arn, session info.
Admin only (enforced by Lambda Authorizer).
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")

bot_credentials_table = dynamodb.Table(os.environ.get("BOT_CREDENTIALS_TABLE"))
bot_pool_table_name = os.environ.get("BOT_POOL_TABLE", "")
bot_pool_table = dynamodb.Table(bot_pool_table_name) if bot_pool_table_name else None
sessions_table_name = os.environ.get("SESSIONS_TABLE", "")
sessions_table = dynamodb.Table(sessions_table_name) if sessions_table_name else None


def _get_credential_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    credential_id = path_params.get("credentialId")
    if not credential_id:
        raise BadRequestError("Credential ID is required")
    return credential_id


def _get_query_params(event: dict) -> dict:
    params = event.get("queryStringParameters") or {}
    return {
        "status": params.get("status"),
    }


def _verify_credential_exists(credential_id: str) -> None:
    response = bot_credentials_table.get_item(Key={"credential_id": credential_id})
    if "Item" not in response:
        raise NotFoundError(f"Bot credential {credential_id} not found")


def _list_containers(credential_id: str, status_filter: str = None) -> list:
    """List all containers for a credential, optionally filtered by status."""
    if not bot_pool_table:
        return []

    try:
        if status_filter:
            response = bot_pool_table.query(
                IndexName="credential-status-index",
                KeyConditionExpression="credential_id = :cid AND #status = :status",
                ExpressionAttributeNames={"#status": "status"},
                ExpressionAttributeValues={
                    ":cid": credential_id,
                    ":status": status_filter,
                },
            )
        else:
            response = bot_pool_table.query(
                IndexName="credential-status-index",
                KeyConditionExpression="credential_id = :cid",
                ExpressionAttributeValues={":cid": credential_id},
            )

        items = response.get("Items", [])
        
        items.sort(key=lambda x: x.get("registered_at", ""), reverse=True)
        
        return items
    except Exception as e:
        logger.error(f"Error listing containers: {e}")
        return []


def _enrich_with_session_names(containers: list) -> list:
    """Add current_session_name to containers that have a current_session_id."""
    if not sessions_table:
        return containers

    session_ids = [
        c.get("current_session_id")
        for c in containers
        if c.get("current_session_id")
    ]

    if not session_ids:
        return containers

    session_names = {}
    for session_id in session_ids:
        try:
            response = sessions_table.get_item(
                Key={"session_id": session_id},
                ProjectionExpression="#name",
                ExpressionAttributeNames={"#name": "name"},
            )
            if "Item" in response:
                session_names[session_id] = response["Item"].get("name", "")
        except Exception as e:
            logger.warning(f"Error fetching session {session_id}: {e}")

    for container in containers:
        session_id = container.get("current_session_id")
        if session_id:
            container["current_session_name"] = session_names.get(session_id, "")
        else:
            container["current_session_name"] = None

    return containers


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    List bot pool containers for a credential.
    
    Path: GET /bot-credentials/{credentialId}/pool
    Query params:
    - status: Filter by status (idle, busy, starting, error)
    
    Returns list of containers with:
    - container_id
    - task_arn
    - status
    - current_session_id
    - current_session_name
    - registered_at
    - last_heartbeat
    """
    try:
        credential_id = _get_credential_id(event)
        query_params = _get_query_params(event)
        
        _verify_credential_exists(credential_id)
        
        containers = _list_containers(credential_id, query_params.get("status"))
        containers = _enrich_with_session_names(containers)
        
        summary = {
            "idle": sum(1 for c in containers if c.get("status") == "idle"),
            "busy": sum(1 for c in containers if c.get("status") == "busy"),
            "starting": sum(1 for c in containers if c.get("status") == "starting"),
            "error": sum(1 for c in containers if c.get("status") == "error"),
            "total": len(containers),
        }
        
        return createResponse(200, "Bot pool containers retrieved successfully", {
            "credential_id": credential_id,
            "summary": summary,
            "containers": containers,
        })
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
