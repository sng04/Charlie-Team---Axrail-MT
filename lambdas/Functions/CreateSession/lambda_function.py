"""
CreateSession Lambda Function

Creates a new session linked to a project in DynamoDB.
- Admin: can create session for any project
- User: can only create session for assigned projects

Supports two modes:
1. Warm Pool Mode (default): Sends meeting request to SQS for pre-warmed containers
2. Cold Start Mode: Starts new ECS task directly (fallback)

Validates that project has a verified and active bot credential before starting bot.
"""

import json
import os
import uuid
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
sqs_client = boto3.client("sqs")

sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE"))
projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE"))
project_users_table = dynamodb.Table(os.environ.get("PROJECT_USERS_TABLE"))
bot_credentials_table = dynamodb.Table(os.environ.get("BOT_CREDENTIALS_TABLE"))
bot_pool_table = dynamodb.Table(os.environ.get("BOT_POOL_TABLE", ""))

ECS_CLUSTER = os.environ.get("ECS_CLUSTER")
ECS_TASK_DEFINITION = os.environ.get("ECS_TASK_DEFINITION")
ECS_SUBNETS = os.environ.get("ECS_SUBNETS", "").split(",")
ECS_SECURITY_GROUP = os.environ.get("ECS_SECURITY_GROUP")
SQS_QUEUE_URL = os.environ.get("SQS_QUEUE_URL", "")
WARM_POOL_ENABLED = os.environ.get("WARM_POOL_ENABLED", "true").lower() == "true"
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")


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


def _get_bot_credential(project: dict) -> dict:
    credential_id = project.get("bot_credential_id")
    if not credential_id:
        raise BadRequestError(
            "Project does not have a bot credential assigned. "
            "Please assign a verified bot credential to the project first."
        )

    response = bot_credentials_table.get_item(Key={"credential_id": credential_id})
    if "Item" not in response:
        raise BadRequestError(
            f"Bot credential {credential_id} not found. "
            "Please assign a valid bot credential to the project."
        )

    credential = response["Item"]

    if credential.get("verification_status") != "verified":
        raise BadRequestError(
            f"Bot credential {credential_id} is not verified. "
            "Please verify the email before creating a session."
        )

    if credential.get("available_status") != "active":
        raise BadRequestError(
            f"Bot credential {credential_id} is not active. "
            "Please activate the credential before creating a session."
        )

    return credential


def _check_warm_pool_available(credential_id: str) -> bool:
    """Check if there's an idle warm container for this credential."""
    if not bot_pool_table.table_name:
        return False

    try:
        response = bot_pool_table.query(
            IndexName="credential-status-index",
            KeyConditionExpression="credential_id = :cid AND #status = :status",
            ExpressionAttributeNames={"#status": "status"},
            ExpressionAttributeValues={
                ":cid": credential_id,
                ":status": "idle",
            },
            Limit=1,
        )
        return len(response.get("Items", [])) > 0
    except Exception as e:
        logger.warning(f"Error checking warm pool: {e}")
        return False


def _send_to_warm_pool(
    session_id: str, project_id: str, credential_id: str, meeting_link: str
) -> bool:
    if not SQS_QUEUE_URL:
        logger.warning("SQS_QUEUE_URL not configured")
        return False

    try:
        message = {
            "session_id": session_id,
            "project_id": project_id,
            "credential_id": credential_id,
            "meeting_url": meeting_link,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }

        send_params = {
            "QueueUrl": SQS_QUEUE_URL,
            "MessageBody": json.dumps(message),
        }

        if ".fifo" in SQS_QUEUE_URL:
            send_params["MessageGroupId"] = credential_id

        sqs_client.send_message(**send_params)

        logger.info(f"Sent meeting request to warm pool for session: {session_id}")
        return True

    except Exception as e:
        logger.error(f"Failed to send to warm pool: {e}")
        return False


def _start_meeting_bot(
    session_id: str, project_id: str, credential_id: str, meeting_link: str
) -> str:
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
                            {"name": "CREDENTIAL_ID", "value": credential_id},
                            {"name": "MEETING_URL", "value": meeting_link},
                            {"name": "ENVIRONMENT", "value": ENVIRONMENT},
                            {"name": "WARM_POOL_MODE", "value": "false"},
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

        user_id, is_admin = _get_user_context(event)
        
        if not is_admin and not _is_user_assigned_to_project(user_id, data["project_id"]):
            raise UnauthorizedError("You don't have access to this project")

        project = _verify_project_exists(data["project_id"])
        credential = _get_bot_credential(project)

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

        use_warm_pool = WARM_POOL_ENABLED and _check_warm_pool_available(credential["credential_id"])

        if use_warm_pool:
            sent = _send_to_warm_pool(
                session_id,
                data["project_id"],
                credential["credential_id"],
                data["meeting_link"],
            )
            if sent:
                item["bot_status"] = "queued"
                item["dispatch_mode"] = "warm_pool"
                logger.info(f"Session {session_id} queued for warm pool")
            else:
                use_warm_pool = False

        if not use_warm_pool:
            task_arn = _start_meeting_bot(
                session_id,
                data["project_id"],
                credential["credential_id"],
                data["meeting_link"],
            )
            if task_arn:
                item["task_arn"] = task_arn
                item["bot_status"] = "starting"
                item["dispatch_mode"] = "cold_start"

        sessions_table.put_item(Item=item)

        return createResponse(200, "Session created successfully", item)
    except UnauthorizedError as e:
        logger.warning(f"Unauthorized: {e}")
        return createResponse(403, str(e))
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
