"""
StartWarmPool Lambda Function

Starts warm pool ECS tasks for specified bot credentials.
Can be triggered manually or by EventBridge schedule.
"""

import json
import os

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse
from custom_exceptions import BadRequestError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
ecs_client = boto3.client("ecs")

bot_credentials_table = dynamodb.Table(os.environ.get("BOT_CREDENTIALS_TABLE"))
bot_pool_table = dynamodb.Table(os.environ.get("BOT_POOL_TABLE", ""))

ECS_CLUSTER = os.environ.get("ECS_CLUSTER")
ECS_TASK_DEFINITION = os.environ.get("ECS_TASK_DEFINITION")
ECS_SUBNETS = os.environ.get("ECS_SUBNETS", "").split(",")
ECS_SECURITY_GROUP = os.environ.get("ECS_SECURITY_GROUP")
ENVIRONMENT = os.environ.get("ENVIRONMENT", "dev")


def _parse_body(event: dict) -> dict:
    body = event.get("body")
    if not body:
        return {}
    return json.loads(body) if isinstance(body, str) else body


def _get_active_credentials() -> list:
    """Get all active and verified bot credentials."""
    try:
        response = bot_credentials_table.scan(
            FilterExpression="verification_status = :vs AND available_status = :as",
            ExpressionAttributeValues={
                ":vs": "verified",
                ":as": "active",
            },
        )
        return response.get("Items", [])
    except Exception as e:
        logger.error(f"Failed to get credentials: {e}")
        return []


def _get_idle_containers_for_credential(credential_id: str) -> int:
    """Count idle containers for a credential."""
    if not bot_pool_table.table_name:
        return 0

    try:
        response = bot_pool_table.query(
            IndexName="credential-status-index",
            KeyConditionExpression="credential_id = :cid AND #status = :status",
            ExpressionAttributeNames={"#status": "status"},
            ExpressionAttributeValues={
                ":cid": credential_id,
                ":status": "idle",
            },
        )
        return len(response.get("Items", []))
    except Exception as e:
        logger.warning(f"Error counting idle containers: {e}")
        return 0


def _start_warm_container(credential_id: str) -> str:
    """Start a warm pool ECS task for a credential."""
    if not all([ECS_CLUSTER, ECS_TASK_DEFINITION, ECS_SUBNETS, ECS_SECURITY_GROUP]):
        logger.warning("ECS configuration not complete")
        return None

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
                            {"name": "CREDENTIAL_ID", "value": credential_id},
                            {"name": "ENVIRONMENT", "value": ENVIRONMENT},
                            {"name": "WARM_POOL_MODE", "value": "true"},
                        ],
                    }
                ]
            },
        )

        if response.get("tasks"):
            task_arn = response["tasks"][0]["taskArn"]
            logger.info(f"Started warm container for {credential_id}: {task_arn}")
            return task_arn
        else:
            failures = response.get("failures", [])
            logger.error(f"Failed to start warm container: {failures}")
            return None

    except Exception as e:
        logger.error(f"Error starting warm container: {e}")
        return None


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    Start warm pool containers.
    
    Request body (optional):
    - credential_ids: List of specific credential IDs to warm up
    - containers_per_credential: Override warm_pool_size for all credentials (optional)
    
    If no body provided, warms up all active credentials using their warm_pool_size setting.
    Each credential can have different warm_pool_size stored in BotCredentials table.
    """
    try:
        data = _parse_body(event)
        
        credential_ids = data.get("credential_ids")
        override_containers = data.get("containers_per_credential")
        
        if credential_ids:
            # Warm specific credentials
            credentials = []
            for cid in credential_ids:
                response = bot_credentials_table.get_item(Key={"credential_id": cid})
                if "Item" in response:
                    credentials.append(response["Item"])
        else:
            # Warm all active credentials
            credentials = _get_active_credentials()
        
        if not credentials:
            return createResponse(200, "No active credentials to warm up", {"started": 0})
        
        started_tasks = []
        
        for credential in credentials:
            credential_id = credential["credential_id"]
            
            # Use override if provided, otherwise use credential's warm_pool_size (default: 1)
            target_containers = int(override_containers if override_containers else credential.get("warm_pool_size", 1))
            
            # Check how many idle containers already exist
            existing_idle = _get_idle_containers_for_credential(credential_id)
            needed = max(0, target_containers - existing_idle)
            
            if needed == 0:
                logger.info(f"Credential {credential_id} already has {existing_idle} idle containers (target: {target_containers})")
                continue
            
            logger.info(f"Starting {needed} containers for {credential_id} (target: {target_containers}, existing: {existing_idle})")
            
            for _ in range(needed):
                task_arn = _start_warm_container(credential_id)
                if task_arn:
                    started_tasks.append({
                        "credential_id": credential_id,
                        "task_arn": task_arn,
                    })
        
        return createResponse(200, f"Started {len(started_tasks)} warm containers", {
            "started": len(started_tasks),
            "tasks": started_tasks,
        })
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
