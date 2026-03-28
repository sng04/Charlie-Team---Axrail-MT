"""
StartWarmPool Lambda Function

Starts warm pool ECS tasks for specified bot credentials.
Can be triggered manually or by EventBridge schedule.
Checks running ECS tasks to prevent duplicate containers.
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
WEBSOCKET_API_URL = os.environ.get("WEBSOCKET_API_URL", "")


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
    """Count idle containers for a credential from DynamoDB."""
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


def _count_running_tasks_for_credential(credential_id: str) -> int:
    """
    Count running ECS tasks for a specific credential.
    This is more reliable than checking DynamoDB because tasks may not have registered yet.
    """
    if not ECS_CLUSTER:
        return 0

    try:
        task_arns = []
        paginator = ecs_client.get_paginator("list_tasks")
        for page in paginator.paginate(cluster=ECS_CLUSTER, desiredStatus="RUNNING"):
            task_arns.extend(page.get("taskArns", []))

        if not task_arns:
            return 0

        count = 0
        for i in range(0, len(task_arns), 100):
            batch = task_arns[i:i + 100]
            response = ecs_client.describe_tasks(cluster=ECS_CLUSTER, tasks=batch)

            for task in response.get("tasks", []):
                for container in task.get("overrides", {}).get("containerOverrides", []):
                    for env in container.get("environment", []):
                        if env.get("name") == "CREDENTIAL_ID" and env.get("value") == credential_id:
                            is_warm_pool = any(
                                e.get("name") == "WARM_POOL_MODE" and e.get("value") == "true"
                                for e in container.get("environment", [])
                            )
                            if is_warm_pool:
                                count += 1
                            break

        logger.info(f"Found {count} running warm pool tasks for credential {credential_id}")
        return count

    except Exception as e:
        logger.error(f"Error counting running tasks: {e}")
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
                            {"name": "WEBSOCKET_API_URL", "value": WEBSOCKET_API_URL},
                        ],
                    }
                ]
            },
        )

        if response.get("tasks"):
            task_arn = response["tasks"][0]["taskArn"]
            logger.info(f"Started warm container for {credential_id}: {task_arn}")
            
            _create_bot_pool_entry(credential_id, task_arn)
            
            return task_arn
        else:
            failures = response.get("failures", [])
            logger.error(f"Failed to start warm container: {failures}")
            return None

    except Exception as e:
        logger.error(f"Error starting warm container: {e}")
        return None


def _create_bot_pool_entry(credential_id: str, task_arn: str) -> None:
    """Create bot pool entry with 'starting' status."""
    if not bot_pool_table.table_name:
        return

    try:
        import time
        from datetime import datetime, timezone
        
        task_id = task_arn.split("/")[-1]
        
        bot_pool_table.put_item(Item={
            "container_id": task_id,
            "credential_id": credential_id,
            "task_arn": task_arn,
            "status": "starting",
            "current_session_id": None,
            "registered_at": datetime.now(timezone.utc).isoformat(),
            "last_heartbeat": datetime.now(timezone.utc).isoformat(),
            "ttl": int(time.time()) + 86400,
        })
        logger.info(f"Created bot pool entry with status 'starting': {task_id}")
    except Exception as e:
        logger.warning(f"Error creating bot pool entry: {e}")


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
            credentials = []
            for cid in credential_ids:
                response = bot_credentials_table.get_item(Key={"credential_id": cid})
                if "Item" in response:
                    credentials.append(response["Item"])
        else:
            credentials = _get_active_credentials()
        
        if not credentials:
            return createResponse(200, "No active credentials to warm up", {"started": 0})
        
        started_tasks = []
        
        for credential in credentials:
            credential_id = credential["credential_id"]
            
            target_containers = int(override_containers if override_containers else credential.get("warm_pool_size", 1))
            
            existing_running = _count_running_tasks_for_credential(credential_id)
            needed = max(0, target_containers - existing_running)
            
            if needed == 0:
                logger.info(f"Credential {credential_id} already has {existing_running} running tasks (target: {target_containers})")
                continue
            
            logger.info(f"Starting {needed} containers for {credential_id} (target: {target_containers}, running: {existing_running})")
            
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
