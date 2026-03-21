"""
StopWarmPool Lambda Function

Stops warm pool ECS tasks to scale down.
Can stop all warm containers or scale down to target warm_pool_size.
Only stops idle containers (not actively in a meeting).
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


def _parse_body(event: dict) -> dict:
    body = event.get("body")
    if not body:
        return {}
    return json.loads(body) if isinstance(body, str) else body


def _get_warm_pool_tasks() -> list:
    """Get all running warm pool ECS tasks with their credential IDs and container IDs."""
    if not ECS_CLUSTER:
        return []

    try:
        task_arns = []
        paginator = ecs_client.get_paginator("list_tasks")
        for page in paginator.paginate(cluster=ECS_CLUSTER, desiredStatus="RUNNING"):
            task_arns.extend(page.get("taskArns", []))

        if not task_arns:
            return []

        warm_tasks = []
        for i in range(0, len(task_arns), 100):
            batch = task_arns[i:i + 100]
            response = ecs_client.describe_tasks(cluster=ECS_CLUSTER, tasks=batch)

            for task in response.get("tasks", []):
                task_arn = task.get("taskArn")
                credential_id = None
                is_warm_pool = False

                for container in task.get("overrides", {}).get("containerOverrides", []):
                    for env in container.get("environment", []):
                        if env.get("name") == "CREDENTIAL_ID":
                            credential_id = env.get("value")
                        if env.get("name") == "WARM_POOL_MODE" and env.get("value") == "true":
                            is_warm_pool = True

                if is_warm_pool and credential_id:
                    warm_tasks.append({
                        "task_arn": task_arn,
                        "credential_id": credential_id,
                    })

        return warm_tasks

    except Exception as e:
        logger.error(f"Error getting warm pool tasks: {e}")
        return []


def _get_idle_task_arns(credential_id: str, task_arns: list) -> list:
    """Get task ARNs that are idle (not in meeting) for a credential."""
    if not bot_pool_table.table_name:
        return task_arns

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
        
        # container_id is now task_id (last part of task_arn)
        idle_task_ids = set()
        for item in response.get("Items", []):
            idle_task_ids.add(item.get("container_id"))
        
        # Filter task_arns where task_id is in idle set
        idle_task_arns = []
        for task_arn in task_arns:
            task_id = task_arn.split("/")[-1]
            if task_id in idle_task_ids:
                idle_task_arns.append(task_arn)
        
        return idle_task_arns
    except Exception as e:
        logger.warning(f"Error getting idle containers: {e}")
        return task_arns


def _get_busy_count(credential_id: str) -> int:
    """Get count of busy containers for a credential."""
    if not bot_pool_table.table_name:
        return 0

    try:
        response = bot_pool_table.query(
            IndexName="credential-status-index",
            KeyConditionExpression="credential_id = :cid AND #status = :status",
            ExpressionAttributeNames={"#status": "status"},
            ExpressionAttributeValues={
                ":cid": credential_id,
                ":status": "busy",
            },
        )
        return len(response.get("Items", []))
    except Exception as e:
        logger.warning(f"Error getting busy count: {e}")
        return 0


def _stop_task(task_arn: str) -> bool:
    """Stop an ECS task."""
    try:
        ecs_client.stop_task(
            cluster=ECS_CLUSTER,
            task=task_arn,
            reason="Warm pool scale down",
        )
        logger.info(f"Stopped task: {task_arn}")
        return True
    except Exception as e:
        logger.error(f"Error stopping task {task_arn}: {e}")
        return False


def _cleanup_bot_pool_entry(credential_id: str, task_arn: str) -> None:
    """Remove bot pool entry for stopped task."""
    if not bot_pool_table.table_name:
        return

    try:
        task_id = task_arn.split("/")[-1]
        
        bot_pool_table.delete_item(Key={"container_id": task_id})
        logger.info(f"Cleaned up bot pool entry: {task_id}")
    except Exception as e:
        logger.warning(f"Error cleaning up bot pool entry: {e}")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    Stop warm pool containers.
    
    Request body (optional):
    - credential_id: Stop containers for specific credential only
    - stop_all: If true, stop ALL idle warm containers (default: false)
    - target_count: Scale down to this number (uses warm_pool_size if not provided)
    
    If no body provided, scales down all credentials to their warm_pool_size.
    Only stops idle containers, not ones actively in meetings.
    """
    try:
        data = _parse_body(event)
        
        credential_id_filter = data.get("credential_id")
        stop_all = data.get("stop_all", False)
        target_count = data.get("target_count")
        
        warm_tasks = _get_warm_pool_tasks()
        
        if not warm_tasks:
            return createResponse(200, "No warm pool containers running", {"stopped": 0})
        
        tasks_by_credential = {}
        for task in warm_tasks:
            cid = task["credential_id"]
            if cid not in tasks_by_credential:
                tasks_by_credential[cid] = []
            tasks_by_credential[cid].append(task["task_arn"])
        
        if credential_id_filter:
            tasks_by_credential = {
                k: v for k, v in tasks_by_credential.items() 
                if k == credential_id_filter
            }
        
        stopped_tasks = []
        skipped_busy = 0
        
        for credential_id, task_arns in tasks_by_credential.items():
            current_count = len(task_arns)
            
            idle_task_arns = _get_idle_task_arns(credential_id, task_arns)
            idle_count = len(idle_task_arns)
            busy_count = current_count - idle_count
            
            if stop_all:
                to_stop = idle_count
            else:
                if target_count is not None:
                    target = int(target_count)
                else:
                    response = bot_credentials_table.get_item(Key={"credential_id": credential_id})
                    credential = response.get("Item", {})
                    target = int(credential.get("warm_pool_size", 1))
                
                needed_to_stop = max(0, current_count - target)
                to_stop = min(needed_to_stop, idle_count)
                
                if needed_to_stop > idle_count:
                    skipped_busy += (needed_to_stop - idle_count)
            
            if to_stop == 0:
                logger.info(f"Credential {credential_id}: no idle containers to stop (current: {current_count}, idle: {idle_count}, busy: {busy_count})")
                continue
            
            logger.info(f"Credential {credential_id}: stopping {to_stop} idle containers (current: {current_count}, idle: {idle_count}, busy: {busy_count})")
            
            for task_arn in idle_task_arns[:to_stop]:
                if _stop_task(task_arn):
                    stopped_tasks.append({
                        "credential_id": credential_id,
                        "task_arn": task_arn,
                    })
                    _cleanup_bot_pool_entry(credential_id, task_arn)
        
        message = f"Stopped {len(stopped_tasks)} idle containers"
        if skipped_busy > 0:
            message += f", {skipped_busy} containers skipped (in meeting)"
        
        return createResponse(200, message, {
            "stopped": len(stopped_tasks),
            "skipped_busy": skipped_busy,
            "tasks": stopped_tasks,
        })
    except BadRequestError as e:
        logger.warning(f"Bad request: {e}")
        return createResponse(400, str(e))
    except Exception as e:
        logger.exception("Unexpected error")
        tracer.put_annotation("error", str(e))
        return createResponse(500, "Internal server error")
