"""
StopMeetingBot Lambda Function

Stops the Meeting Bot for a specific session.
- Admin: can stop any session's bot
- User: can only stop bot from sessions in assigned projects

For warm pool mode: signals the container to stop the current meeting (container stays alive)
For cold start mode: stops the ECS task entirely
"""

import os
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError, UnauthorizedError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
ecs_client = boto3.client("ecs")

sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE"))
project_users_table = dynamodb.Table(os.environ.get("PROJECT_USERS_TABLE"))
bot_pool_table_name = os.environ.get("BOT_POOL_TABLE", "")
bot_pool_table = dynamodb.Table(bot_pool_table_name) if bot_pool_table_name else None

ECS_CLUSTER = os.environ.get("ECS_CLUSTER")


def _get_user_context(event: dict) -> tuple:
    """Extract user_id and role from authorizer context."""
    request_context = event.get("requestContext", {})
    authorizer = request_context.get("authorizer", {})
    user_id = authorizer.get("user_id", "")
    groups = authorizer.get("groups", "")
    is_admin = "admin" in groups.split(",")
    return user_id, is_admin


def _is_user_assigned_to_project(user_id: str, project_id: str) -> bool:
    """Check if user is assigned to the project."""
    response = project_users_table.query(
        IndexName="user-index",
        KeyConditionExpression=Key("user_id").eq(user_id),
    )
    assigned_projects = [item["project_id"] for item in response.get("Items", [])]
    return project_id in assigned_projects


def _get_session_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    session_id = path_params.get("sessionId")
    if not session_id:
        raise BadRequestError("Session ID is required")
    return session_id


def _get_session(session_id: str) -> dict:
    response = sessions_table.get_item(Key={"session_id": session_id})
    if "Item" not in response:
        raise NotFoundError(f"Session {session_id} not found")
    return response["Item"]


def _is_warm_pool_session(session: dict) -> bool:
    """Check if session is using warm pool mode."""
    return session.get("dispatch_mode") == "warm_pool"


def _signal_warm_container_to_stop(session: dict) -> bool:
    session_id = session.get("session_id")
    container_id = session.get("container_id")

    try:
        sessions_table.update_item(
            Key={"session_id": session_id},
            UpdateExpression="SET bot_status = :status, updated_at = :updated_at, stop_requested = :stop",
            ConditionExpression="attribute_exists(session_id)",
            ExpressionAttributeValues={
                ":status": "stopping",
                ":updated_at": datetime.now(timezone.utc).isoformat(),
                ":stop": True,
            },
        )
        logger.info(f"Signaled warm container to stop session: {session_id}")

        if bot_pool_table and container_id:
            try:
                bot_pool_table.update_item(
                    Key={"container_id": container_id},
                    UpdateExpression="SET stop_current_session = :stop",
                    ConditionExpression="attribute_exists(container_id)",
                    ExpressionAttributeValues={":stop": True},
                )
            except dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
                logger.warning(f"Container {container_id} not found in BotPool")
            except Exception as e:
                logger.warning(f"Could not update BotPool: {e}")

        return True
    except Exception as e:
        logger.error(f"Error signaling warm container: {e}")
        return False


def _stop_ecs_task(task_arn: str) -> bool:
    """Stop ECS task (for cold start mode only)."""
    if not task_arn or not ECS_CLUSTER:
        return False

    try:
        ecs_client.stop_task(
            cluster=ECS_CLUSTER,
            task=task_arn,
            reason="Stopped by user request",
        )
        logger.info(f"Stopped ECS task: {task_arn}")
        return True
    except Exception as e:
        logger.error(f"Error stopping ECS task: {e}")
        return False


def _update_session_status(session_id: str, status: str) -> None:
    """Update session bot_status."""
    try:
        sessions_table.update_item(
            Key={"session_id": session_id},
            UpdateExpression="SET bot_status = :status, updated_at = :updated_at",
            ConditionExpression="attribute_exists(session_id)",
            ExpressionAttributeValues={
                ":status": status,
                ":updated_at": datetime.now(timezone.utc).isoformat(),
            },
        )
    except dynamodb.meta.client.exceptions.ConditionalCheckFailedException:
        logger.warning(f"Session {session_id} not found, skipping status update")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        session_id = _get_session_id(event)
        session = _get_session(session_id)
        
        user_id, is_admin = _get_user_context(event)
        
        if not is_admin:
            project_id = session.get("project_id")
            if not _is_user_assigned_to_project(user_id, project_id):
                raise UnauthorizedError("You don't have access to this session")

        current_status = session.get("bot_status")

        if current_status in ["completed", "failed", "stopped"]:
            return createResponse(400, f"Bot is already {current_status}")

        if _is_warm_pool_session(session):
            signaled = _signal_warm_container_to_stop(session)
            if signaled:
                return createResponse(200, "Stop signal sent to meeting bot", {
                    "session_id": session_id,
                    "mode": "warm_pool",
                    "message": "Container will stop current meeting and return to idle state"
                })
            else:
                return createResponse(500, "Failed to signal meeting bot to stop")

        task_arn = session.get("task_arn")
        if not task_arn:
            return createResponse(400, "No active bot task for this session")

        stopped = _stop_ecs_task(task_arn)

        if stopped:
            _update_session_status(session_id, "stopped")
            return createResponse(200, "Meeting bot stopped successfully", {
                "session_id": session_id,
                "mode": "cold_start"
            })
        else:
            return createResponse(500, "Failed to stop meeting bot")

    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except UnauthorizedError as e:
        logger.warning(f"Unauthorized: {e}")
        return createResponse(403, str(e))
    except NotFoundError as e:
        logger.warning(f"Not found: {e}")
        return createResponse(404, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
