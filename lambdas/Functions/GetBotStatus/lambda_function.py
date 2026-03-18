"""
GetBotStatus Lambda Function

Gets the Meeting Bot status for a specific session.
"""

import os

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


def _get_ecs_task_status(task_arn: str) -> dict:
    """Get ECS task status from AWS."""
    if not task_arn or not ECS_CLUSTER:
        return None

    try:
        response = ecs_client.describe_tasks(
            cluster=ECS_CLUSTER,
            tasks=[task_arn],
        )

        if response.get("tasks"):
            task = response["tasks"][0]
            return {
                "task_arn": task_arn,
                "last_status": task.get("lastStatus"),
                "desired_status": task.get("desiredStatus"),
                "started_at": task.get("startedAt").isoformat() if task.get("startedAt") else None,
                "stopped_at": task.get("stoppedAt").isoformat() if task.get("stoppedAt") else None,
                "stopped_reason": task.get("stoppedReason"),
                "cpu": task.get("cpu"),
                "memory": task.get("memory"),
            }
        return None
    except Exception as e:
        logger.error(f"Error getting ECS task status: {e}")
        return None


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        session_id = _get_session_id(event)
        session = _get_session(session_id)

        task_arn = session.get("task_arn")
        bot_status = session.get("bot_status", "unknown")

        result = {
            "session_id": session_id,
            "bot_status": bot_status,
            "task_arn": task_arn,
            "meeting_link": session.get("meeting_link"),
        }

        if task_arn:
            ecs_status = _get_ecs_task_status(task_arn)
            if ecs_status:
                result["ecs_task"] = ecs_status

        return createResponse(200, "Bot status retrieved successfully", result)
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
