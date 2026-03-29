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
import re
import uuid
from datetime import datetime, timezone

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError, UnauthorizedError

QA_PAIRS_TABLE_NAME = os.environ.get("QA_PAIRS_TABLE_NAME", "")
SUGGESTED_QUESTIONS_TABLE_NAME = os.environ.get("SUGGESTED_QUESTIONS_TABLE_NAME", "")
GAP_ANALYSIS_TABLE_NAME = os.environ.get("GAP_ANALYSIS_TABLE_NAME", "")
BEDROCK_REGION = os.environ.get("BEDROCK_REGION", "us-east-1")

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
WEBSOCKET_API_URL = os.environ.get("WEBSOCKET_API_URL", "")


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
    required_fields = ["project_id", "name"]
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
            "websocket_api_url": WEBSOCKET_API_URL,
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
                            {"name": "WEBSOCKET_API_URL", "value": WEBSOCKET_API_URL},
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


def _generate_suggested_questions(session_id: str, project_id: str) -> list:
    """Generate suggested questions from previous session history."""
    try:
        qa_table = dynamodb.Table(QA_PAIRS_TABLE_NAME)
        gap_table = dynamodb.Table(GAP_ANALYSIS_TABLE_NAME)
        sq_table = dynamodb.Table(SUGGESTED_QUESTIONS_TABLE_NAME)

        # Get previous sessions for this project
        prev_sessions = sessions_table.query(
            IndexName="project-index",
            KeyConditionExpression=Key("project_id").eq(project_id),
        ).get("Items", [])

        # Exclude the current session
        prev_session_ids = [s["session_id"] for s in prev_sessions if s["session_id"] != session_id]
        if not prev_session_ids:
            return []

        # Collect QA pairs from previous sessions (max 10)
        qa_pairs = []
        for sid in prev_session_ids[:5]:
            resp = qa_table.query(
                IndexName="session-index",
                KeyConditionExpression=Key("session_id").eq(sid),
                Limit=5,
            )
            qa_pairs.extend(resp.get("Items", []))
        qa_pairs = qa_pairs[:10]

        # Collect gap analysis results
        gaps = []
        for sid in prev_session_ids[:3]:
            resp = gap_table.get_item(Key={"session_id": sid})
            if "Item" in resp:
                gaps.append(resp["Item"])

        if not qa_pairs and not gaps:
            return []

        # Build prompt
        history_text = "Previous meeting Q&A:\n"
        for qa in qa_pairs:
            history_text += f"- Q: {qa.get('question', '')}\n  A: {qa.get('answer', '')[:200]}\n"

        if gaps:
            history_text += "\nKnowledge gaps identified:\n"
            for g in gaps:
                for gap in g.get("gaps", [])[:3]:
                    history_text += f"- {gap.get('topic', '')}: {gap.get('description', '')[:150]}\n"

        prompt = (
            f"Based on this meeting history for a project, generate 3-5 suggested questions "
            f"that the meeting host should ask the client in the next meeting. "
            f"Focus on unresolved topics, knowledge gaps, and follow-up items.\n\n"
            f"{history_text}\n"
            f"Return ONLY a JSON array of question strings, no other text. Example:\n"
            f'["Question 1?", "Question 2?", "Question 3?"]'
        )

        bedrock = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)
        response = bedrock.converse(
            modelId="amazon.nova-pro-v1:0",
            messages=[{"role": "user", "content": [{"text": prompt}]}],
        )

        output_text = ""
        for block in response.get("output", {}).get("message", {}).get("content", []):
            if "text" in block:
                output_text += block["text"]

        # Parse JSON array from response
        match = re.search(r'\[.*\]', output_text, re.DOTALL)
        if not match:
            return []
        questions = json.loads(match.group())
        if not isinstance(questions, list):
            return []
        questions = [q for q in questions if isinstance(q, str) and q.strip()][:5]

        # Store in SuggestedQuestions table
        now = datetime.now(timezone.utc).isoformat()
        for q_text in questions:
            sq_table.put_item(Item={
                "question_id": str(uuid.uuid4()),
                "session_id": session_id,
                "question_text": q_text,
                "created_at": now,
                "matched": False,
            })

        logger.info(f"Generated {len(questions)} suggested questions for session {session_id}")
        return questions

    except Exception:
        logger.exception("Failed to generate suggested questions")
        return []


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        data = _parse_body(event)
        _validate_input(data)

        user_id, is_admin = _get_user_context(event)
        
        if not is_admin and not _is_user_assigned_to_project(user_id, data["project_id"]):
            raise UnauthorizedError("You don't have access to this project")

        project = _verify_project_exists(data["project_id"])

        session_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc).isoformat()

        meeting_link = data.get("meeting_link")

        item = {
            "session_id": session_id,
            "project_id": data["project_id"],
            "name": data["name"],
            "description": data.get("description", ""),
            "meeting_link": meeting_link or "",
            "bot_status": "pending" if meeting_link else "none",
            "is_active": "inactive",
            "task_arn": None,
            "start_time": None,
            "end_time": None,
            "created_at": now,
            "updated_at": now,
        }

        # Only dispatch bot if meeting_link is provided
        if meeting_link:
            credential = _get_bot_credential(project)
            use_warm_pool = WARM_POOL_ENABLED and _check_warm_pool_available(credential["credential_id"])

            if use_warm_pool:
                sent = _send_to_warm_pool(
                    session_id,
                    data["project_id"],
                    credential["credential_id"],
                    meeting_link,
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
                    meeting_link,
                )
                if task_arn:
                    item["task_arn"] = task_arn
                    item["bot_status"] = "starting"
                    item["dispatch_mode"] = "cold_start"

        sessions_table.put_item(Item=item)

        # Generate suggested questions from project history (non-blocking)
        suggested_questions = _generate_suggested_questions(session_id, data["project_id"])
        if suggested_questions:
            item["suggested_questions"] = suggested_questions

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
