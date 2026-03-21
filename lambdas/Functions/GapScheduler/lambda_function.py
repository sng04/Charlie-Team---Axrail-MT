"""Gap analysis scheduler — triggered by EventBridge.

Queries SessionsTable for active sessions, skips sessions with no new
transcript data, and invokes the Strands agent Lambda asynchronously
for each eligible session.
"""

import json
import os
from datetime import datetime, timezone

import boto3
from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Key

logger = Logger()
tracer = Tracer()

SESSIONS_TABLE_NAME = os.environ.get("SESSIONS_TABLE_NAME", "")
AGENT_FUNCTION_NAME = os.environ.get("AGENT_FUNCTION_NAME", "")
ACTIVE_SESSIONS_INDEX = os.environ.get(
    "ACTIVE_SESSIONS_INDEX_NAME", "active-sessions-index"
)

_dynamodb = None
_lambda_client = None


def _get_dynamodb():
    """Return a cached DynamoDB resource."""
    global _dynamodb
    if _dynamodb is None:
        _dynamodb = boto3.resource("dynamodb")
    return _dynamodb


def _get_lambda_client():
    """Return a cached Lambda client."""
    global _lambda_client
    if _lambda_client is None:
        _lambda_client = boto3.client("lambda")
    return _lambda_client


@tracer.capture_method
def _has_new_transcript(session: dict) -> bool:
    """Check if a session has new transcript data since last gap analysis."""
    last_transcript = session.get("last_transcript_update_at", "")
    last_analysis = session.get("last_gap_analysis_at", "")
    if not last_transcript:
        return False
    if not last_analysis:
        return True
    return last_transcript > last_analysis


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """Query active sessions and trigger gap analysis for eligible ones."""
    table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
    lambda_client = _get_lambda_client()

    response = table.query(
        IndexName=ACTIVE_SESSIONS_INDEX,
        KeyConditionExpression=Key("is_active").eq("active"),
    )
    sessions = response.get("Items", [])

    if not sessions:
        logger.info("No active sessions found")
        return {"statusCode": 200, "body": "No active sessions"}

    triggered = 0
    for session in sessions:
        session_id = session.get("session_id", "")
        connection_id = session.get("connection_id", "")

        if not _has_new_transcript(session):
            logger.info(
                "Skipping session — no new transcript data",
                extra={"session_id": session_id},
            )
            continue

        payload = {
            "requestContext": {
                "routeKey": "analyzeGaps",
                "connectionId": connection_id,
            },
            "body": json.dumps({
                "action": "analyzeGaps",
                "session_id": session_id,
            }),
        }

        try:
            lambda_client.invoke(
                FunctionName=AGENT_FUNCTION_NAME,
                InvocationType="Event",
                Payload=json.dumps(payload),
            )
            table.update_item(
                Key={"session_id": session_id},
                UpdateExpression="SET last_gap_analysis_at = :ts",
                ExpressionAttributeValues={
                    ":ts": datetime.now(timezone.utc).isoformat(),
                },
            )
            triggered += 1
            logger.info(
                "Triggered gap analysis",
                extra={"session_id": session_id},
            )
        except Exception:
            logger.exception(
                "Failed to invoke gap analysis",
                extra={"session_id": session_id},
            )

    return {
        "statusCode": 200,
        "body": f"Triggered {triggered}/{len(sessions)} sessions",
    }
