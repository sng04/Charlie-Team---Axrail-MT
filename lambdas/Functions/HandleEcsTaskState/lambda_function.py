"""
HandleEcsTaskState Lambda Function

Handles ECS task state change events from EventBridge.
Updates or deletes BotPool records when tasks stop or fail.
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
bot_pool_table = dynamodb.Table(os.environ.get("BOT_POOL_TABLE", ""))

ECS_CLUSTER_NAME = os.environ.get("ECS_CLUSTER_NAME", "")


def _extract_task_id(task_arn: str) -> str:
    """Extract task ID from task ARN."""
    return task_arn.split("/")[-1]


def _get_stop_reason(detail: dict) -> str:
    """Get human-readable stop reason."""
    stopped_reason = detail.get("stoppedReason", "Unknown")
    stop_code = detail.get("stopCode", "")
    
    if "Essential container" in stopped_reason:
        return "Container crashed"
    elif "Task failed" in stopped_reason:
        return "Task failed to start"
    elif stop_code == "UserInitiated":
        return "Stopped by user"
    elif stop_code == "ServiceSchedulerInitiated":
        return "Stopped by scheduler"
    
    return stopped_reason


def _is_warm_pool_task(detail: dict) -> bool:
    """Check if task is a warm pool task."""
    overrides = detail.get("overrides", {})
    container_overrides = overrides.get("containerOverrides", [])
    
    for container in container_overrides:
        for env in container.get("environment", []):
            if env.get("name") == "WARM_POOL_MODE" and env.get("value") == "true":
                return True
    
    return False


def _delete_bot_pool_entry(task_id: str) -> bool:
    """Delete bot pool entry by task_id (container_id)."""
    if not bot_pool_table.table_name:
        return False

    try:
        bot_pool_table.delete_item(Key={"container_id": task_id})
        logger.info(f"Deleted bot pool entry: {task_id}")
        return True
    except Exception as e:
        logger.error(f"Error deleting bot pool entry: {e}")
        return False


def _update_bot_pool_status(task_id: str, status: str, error_reason: str = None) -> bool:
    """Update bot pool entry status."""
    if not bot_pool_table.table_name:
        return False

    try:
        import time
        from datetime import datetime, timezone
        
        update_expr = "SET #status = :status, last_heartbeat = :hb"
        expr_values = {
            ":status": status,
            ":hb": datetime.now(timezone.utc).isoformat(),
        }
        
        if error_reason:
            update_expr += ", error_reason = :err"
            expr_values[":err"] = error_reason
        
        if status == "error":
            update_expr += ", #ttl = :ttl"
            expr_values[":ttl"] = int(time.time()) + 3600
        
        bot_pool_table.update_item(
            Key={"container_id": task_id},
            UpdateExpression=update_expr,
            ExpressionAttributeNames={"#status": "status", "#ttl": "ttl"} if status == "error" else {"#status": "status"},
            ExpressionAttributeValues=expr_values,
        )
        logger.info(f"Updated bot pool entry {task_id} status to: {status}")
        return True
    except Exception as e:
        logger.error(f"Error updating bot pool status: {e}")
        return False


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """
    Handle ECS task state change events.
    
    Triggered by EventBridge when ECS task state changes to STOPPED.
    Deletes the corresponding BotPool record.
    """
    try:
        detail = event.get("detail", {})
        
        task_arn = detail.get("taskArn", "")
        last_status = detail.get("lastStatus", "")
        cluster_arn = detail.get("clusterArn", "")
        
        logger.info(f"ECS task state change: {task_arn} -> {last_status}")
        
        if last_status != "STOPPED":
            logger.debug(f"Ignoring non-STOPPED event: {last_status}")
            return {"processed": False, "reason": "Not a STOPPED event"}
        
        if ECS_CLUSTER_NAME and ECS_CLUSTER_NAME not in cluster_arn:
            logger.debug(f"Ignoring event from different cluster: {cluster_arn}")
            return {"processed": False, "reason": "Different cluster"}
        
        if not _is_warm_pool_task(detail):
            logger.debug("Ignoring non-warm-pool task")
            return {"processed": False, "reason": "Not a warm pool task"}
        
        task_id = _extract_task_id(task_arn)
        stop_reason = _get_stop_reason(detail)
        
        logger.info(f"Warm pool task stopped: {task_id}, reason: {stop_reason}")
        
        stop_code = detail.get("stopCode", "")
        if stop_code == "UserInitiated":
            deleted = _delete_bot_pool_entry(task_id)
            return {
                "processed": True,
                "task_id": task_id,
                "stop_reason": stop_reason,
                "action": "deleted",
                "deleted": deleted,
            }
        else:
            updated = _update_bot_pool_status(task_id, "error", stop_reason)
            return {
                "processed": True,
                "task_id": task_id,
                "stop_reason": stop_reason,
                "action": "marked_error",
                "updated": updated,
            }
        
    except Exception as e:
        logger.exception("Error handling ECS task state change")
        tracer.put_annotation("error", str(e))
        return {"processed": False, "error": str(e)}
