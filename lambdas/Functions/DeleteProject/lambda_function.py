"""
DeleteProject Lambda Function

Deletes a project and all related data (sessions, transcripts, project-user
assignments). Rejects deletion if any session is currently in_meeting.
Admin only (enforced by Lambda Authorizer).
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

from response_utils import createResponse
from custom_exceptions import BadRequestError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE"))
sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE"))
transcripts_table = dynamodb.Table(os.environ.get("TRANSCRIPTS_TABLE"))
project_users_table = dynamodb.Table(os.environ.get("PROJECT_USERS_TABLE"))


def _get_project_id(event: dict) -> str:
    path_params = event.get("pathParameters") or {}
    project_id = path_params.get("projectId")
    if not project_id:
        raise BadRequestError("Project ID is required")
    return project_id


def _get_project_sessions(project_id: str) -> list:
    """Fetch all sessions for a project via GSI."""
    items = []
    query_kwargs = {
        "IndexName": "project-index",
        "KeyConditionExpression": Key("project_id").eq(project_id),
    }
    while True:
        response = sessions_table.query(**query_kwargs)
        items.extend(response.get("Items", []))
        if "LastEvaluatedKey" not in response:
            break
        query_kwargs["ExclusiveStartKey"] = response["LastEvaluatedKey"]
    return items


DELETABLE_BOT_STATUSES = {"none", "stopped", "completed", "failed"}


def _has_active_meeting(sessions: list) -> bool:
    """Check if any session has a bot_status that blocks deletion."""
    return any(
        s.get("bot_status", "none") not in DELETABLE_BOT_STATUSES
        for s in sessions
    )


def _delete_transcripts_for_session(session_id: str) -> int:
    """Delete all transcripts for a session. Returns count deleted."""
    count = 0
    query_kwargs = {
        "KeyConditionExpression": Key("session_id").eq(session_id),
        "ProjectionExpression": "session_id, #ts",
        "ExpressionAttributeNames": {"#ts": "timestamp"},
    }
    while True:
        response = transcripts_table.query(**query_kwargs)
        items = response.get("Items", [])
        with transcripts_table.batch_writer() as batch:
            for item in items:
                batch.delete_item(
                    Key={
                        "session_id": item["session_id"],
                        "timestamp": item["timestamp"],
                    }
                )
                count += 1
        if "LastEvaluatedKey" not in response:
            break
        query_kwargs["ExclusiveStartKey"] = response["LastEvaluatedKey"]
    return count


def _delete_sessions(sessions: list) -> int:
    """Delete all session records. Returns count deleted."""
    count = 0
    with sessions_table.batch_writer() as batch:
        for session in sessions:
            batch.delete_item(Key={"session_id": session["session_id"]})
            count += 1
    return count


def _delete_project_users(project_id: str) -> int:
    """Delete all project-user assignments for a project. Returns count deleted."""
    count = 0
    query_kwargs = {
        "IndexName": "project-index",
        "KeyConditionExpression": Key("project_id").eq(project_id),
        "ProjectionExpression": "project_user_id",
    }
    while True:
        response = project_users_table.query(**query_kwargs)
        items = response.get("Items", [])
        with project_users_table.batch_writer() as batch:
            for item in items:
                batch.delete_item(
                    Key={"project_user_id": item["project_user_id"]}
                )
                count += 1
        if "LastEvaluatedKey" not in response:
            break
        query_kwargs["ExclusiveStartKey"] = response["LastEvaluatedKey"]
    return count


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        project_id = _get_project_id(event)

        # Verify project exists
        response = projects_table.get_item(Key={"project_id": project_id})
        if "Item" not in response:
            return createResponse(404, f"Project {project_id} not found")

        # Check for active meetings
        sessions = _get_project_sessions(project_id)
        if _has_active_meeting(sessions):
            return createResponse(
                409,
                "Cannot delete project while a meeting is in progress. "
                "Please end all active meetings first.",
            )

        # Cascade delete: transcripts → sessions → project_users → project
        transcript_count = 0
        for session in sessions:
            transcript_count += _delete_transcripts_for_session(
                session["session_id"]
            )

        session_count = _delete_sessions(sessions)
        user_count = _delete_project_users(project_id)

        projects_table.delete_item(Key={"project_id": project_id})

        logger.info(
            "Project deleted with cascade",
            extra={
                "project_id": project_id,
                "sessions_deleted": session_count,
                "transcripts_deleted": transcript_count,
                "project_users_deleted": user_count,
            },
        )

        return createResponse(200, "Project and all related data deleted successfully")
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
