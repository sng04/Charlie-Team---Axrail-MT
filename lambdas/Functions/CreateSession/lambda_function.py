"""
CreateSession Lambda Function

Creates a new session linked to a project in DynamoDB.
Automatically triggers Meeting Bot to join the meeting if meeting_link is provided.
"""

import json
import os
import uuid
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
projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE"))

# ECS Configuration
ECS_CLUSTER = os.environ.get("ECS_CLUSTER")
ECS_TASK_DEFINITION = os.environ.get("ECS_TASK_DEFINITION")
ECS_SUBNETS = os.environ.get("ECS_SUBNETS", "").split(",")
ECS_SECURITY_GROUP = os.environ.get("ECS_SECURITY_GROUP")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    return json.loads(body) if isinstance(body, str) else body


def _validate_input(data: dict) -> None:
    required_fields = ["project_id", "name", "meeting_link"]
    missing = [f for f in required_fields if f not in data or data[f] is None]
    if missing:
        raise BadRequestError(f"Missing required fields: {', '.join(missing)}")


def _verify_project_exists(project_id: str) -> dict:
    """Verify project exists and return project data."""
    response = projects_table.get_item(Key={"project_id": project_id})
    if "Item" not in response:
        raise NotFoundError(f"Project {project_id} not found")
    return response["Item"]


def _start_meeting_bot(session_id: str, project_id: str, meeting_link: str) -> str:
    """
    Start ECS Fargate task for Meeting Bot.
    
    Returns:
        str: Task ARN
    """
    if not all([ECS_CLUSTER, ECS_TASK_DEFINITION, ECS_SUBNETS, ECS_SECURITY_GROUP]):
        logger.warning("ECS configuration not complete, skipping bot start")
        return None

    logger.info(f"Starting Meeting Bot for session: {session_id}")

    try:
        response = ecs_client.run_task(
            cluster=ECS_CLUSTER,
            taskDefinition=ECS_TASK_DEFINITION,
            launchType="FARGATE",
            networkConfiguration={
                "awsvpcConfiguration": {
                    "subnets": [s.strip() for s in ECS_SUBNETS if s.strip()],
                    "securityGroups": [ECS_SECURITY_GROUP],
                    "assignPublicIp": "DISABLED",
                }
            },
            overrides={
                "containerOverrides": [
                    {
                        "name": "MeetingBotContainer",
                        "environment": [
                            {"name": "SESSION_ID", "value": session_id},
                            {"name": "PROJECT_ID", "value": project_id},
                            {"name": "MEETING_URL", "value": meeting_link},
                            {"name": "ENVIRONMENT", "value": ENVIRONMENT},
                        ],
                    }
                ]
            },
        )

        if response.get("tasks"):
            task_arn = response["tasks"][0]["taskArn"]
            logger.info(f"Meeting Bot started with task ARN: {task_arn}")
            return task_arn
        else:
            failures = response.get("failures", [])
            logger.error(f"Failed to start Meeting Bot: {failures}")
            return None

    except Exception as e:
        logger.error(f"Error starting Meeting Bot: {e}")
        return None


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        data = _parse_body(event)
        _validate_input(data)

        project = _verify_project_exists(data["project_id"])

        session_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc).isoformat()

        item = {
            "session_id": session_id,
            "project_id": data["project_id"],
            "name": data["name"],
            "description": data.get("description", ""),
            "meeting_link": data["meeting_link"],
            "bot_status": "pending",
            "task_arn": None,
            "start_time": data.get("start_time"),
            "end_time": data.get("end_time"),
            "created_at": now,
            "updated_at": now,
        }

        # Start Meeting Bot
        task_arn = _start_meeting_bot(
            session_id, data["project_id"], data["meeting_link"]
        )

        if task_arn:
            item["task_arn"] = task_arn
            item["bot_status"] = "starting"

        sessions_table.put_item(Item=item)

        return createResponse(200, "Session created successfully", item)
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
