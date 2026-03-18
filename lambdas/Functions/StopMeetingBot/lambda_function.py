"""
StopMeetingBot Lambda Function

Stops the Meeting Bot ECS task for a specific session.
"""

import os
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
ecs_client = boto3.client("ecs")

sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE"))
ECS_CLUSTER = os.environ.get("ECS_CLUSTER")


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


def _stop_ecs_task(task_arn: str) -> bool:
    """Stop ECS task."""
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
    sessions_table.update_item(
        Key={"session_id": session_id},
        UpdateExpression="SET bot_status = :status, updated_at = :updated_at",
        ExpressionAttributeValues={
            ":status": status,
            ":updated_at": datetime.now(timezone.utc).isoformat(),
        },
    )


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        session_id = _get_session_id(event)
        session = _get_session(session_id)

        task_arn = session.get("task_arn")
        current_status = session.get("bot_status")

        if current_status in ["completed", "failed", "stopped"]:
            return createResponse(400, f"Bot is already {current_status}")

        if not task_arn:
            return createResponse(400, "No active bot task for this session")

        stopped = _stop_ecs_task(task_arn)

        if stopped:
            _update_session_status(session_id, "stopped")
            return createResponse(200, "Meeting bot stopped successfully")
        else:
            return createResponse(500, "Failed to stop meeting bot")

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
