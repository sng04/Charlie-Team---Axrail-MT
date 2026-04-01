"""
TranscriptBroadcast Lambda — DynamoDB Streams trigger.

Broadcasts new transcript lines to all WebSocket connections for the session.
Triggered by INSERT events on the Transcripts table stream.
"""

import json
import os

import boto3
from aws_lambda_powertools import Logger

logger = Logger()

SESSIONS_TABLE_NAME = os.environ.get("SESSIONS_TABLE_NAME", "")
WEBSOCKET_ENDPOINT = os.environ.get("WEBSOCKET_ENDPOINT", "")

_dynamodb = None
_apigw = None


def _get_dynamodb():
    global _dynamodb
    if _dynamodb is None:
        _dynamodb = boto3.resource("dynamodb")
    return _dynamodb


def _get_apigw():
    global _apigw
    if _apigw is None and WEBSOCKET_ENDPOINT:
        clean = WEBSOCKET_ENDPOINT.replace("wss://", "").replace("https://", "")
        _apigw = boto3.client(
            "apigatewaymanagementapi",
            endpoint_url=f"https://{clean}",
        )
    return _apigw


def _get_connection_ids(session_id):
    """Get all active connection_ids for a session."""
    if not SESSIONS_TABLE_NAME:
        return []
    try:
        table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
        resp = table.get_item(
            Key={"session_id": session_id},
            ProjectionExpression="connection_ids",
        )
        item = resp.get("Item", {})
        ids = item.get("connection_ids", set())
        return list(ids) if ids else []
    except Exception:
        logger.exception("Failed to get connection_ids for %s", session_id)
        return []


def _post_to_connection(connection_id, data):
    """Post message to a WebSocket connection. Returns False if gone."""
    client = _get_apigw()
    if not client:
        return False
    try:
        client.post_to_connection(
            ConnectionId=connection_id,
            Data=json.dumps(data).encode("utf-8"),
        )
        return True
    except client.exceptions.GoneException:
        return False
    except Exception:
        logger.warning("Failed to post to %s", connection_id[:8])
        return False


def _remove_stale_connection(session_id, connection_id):
    """Remove a stale connection_id from the session's set."""
    try:
        table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
        table.update_item(
            Key={"session_id": session_id},
            UpdateExpression="DELETE connection_ids :cid_set",
            ExpressionAttributeValues={":cid_set": {connection_id}},
        )
    except Exception:
        pass


def lambda_handler(event, context):
    """Process DynamoDB Stream events — broadcast new transcript lines."""
    if not WEBSOCKET_ENDPOINT:
        return {"processed": 0}

    processed = 0
    for record in event.get("Records", []):
        if record.get("eventName") != "INSERT":
            continue

        new_image = record.get("dynamodb", {}).get("NewImage", {})
        if not new_image:
            continue

        # Extract fields from DynamoDB stream format (typed attributes)
        session_id = new_image.get("session_id", {}).get("S", "")
        if not session_id:
            continue

        line = {
            "session_id": session_id,
            "transcript_id": new_image.get("transcript_id", {}).get("S", ""),
            "speaker": new_image.get("speaker", {}).get("S", ""),
            "speaker_role": new_image.get("speaker_role", {}).get("S", ""),
            "text": new_image.get("text", {}).get("S", ""),
            "timestamp": new_image.get("timestamp", {}).get("S", ""),
            "start_time": new_image.get("start_time", {}).get("S", ""),
            "end_time": new_image.get("end_time", {}).get("S", ""),
            "confidence": new_image.get("confidence", {}).get("S", ""),
            "is_partial": new_image.get("is_partial", {}).get("BOOL", False),
        }

        message = {"type": "transcriptLine", "line": line}

        connection_ids = _get_connection_ids(session_id)
        for cid in connection_ids:
            ok = _post_to_connection(cid, message)
            if not ok:
                _remove_stale_connection(session_id, cid)

        processed += 1

    return {"processed": processed}
