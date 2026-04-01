"""
QAPairBroadcast Lambda — DynamoDB Streams trigger on QAPairs table.

Broadcasts QA events to all WebSocket connections for the session:
  INSERT                          → questionDetected
  MODIFY (suggested_answer added) → suggestedResponse
  MODIFY (answer added)           → qaPairAutoSaved
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


def _get_str(image, key):
    """Extract a string value from a DynamoDB stream image."""
    return image.get(key, {}).get("S", "")


def _get_bool(image, key):
    """Extract a boolean value from a DynamoDB stream image."""
    return image.get(key, {}).get("BOOL", False)


def _get_connection_ids(session_id):
    if not SESSIONS_TABLE_NAME or not session_id:
        return []
    try:
        table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
        resp = table.get_item(
            Key={"session_id": session_id},
            ProjectionExpression="connection_ids",
        )
        ids = resp.get("Item", {}).get("connection_ids", set())
        return list(ids) if ids else []
    except Exception:
        logger.exception("Failed to get connection_ids for %s", session_id)
        return []


def _broadcast(session_id, message):
    """Send message to all connections for a session."""
    client = _get_apigw()
    if not client:
        return
    data = json.dumps(message).encode("utf-8")
    for cid in _get_connection_ids(session_id):
        try:
            client.post_to_connection(ConnectionId=cid, Data=data)
        except client.exceptions.GoneException:
            # Stale connection — remove it
            try:
                table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
                table.update_item(
                    Key={"session_id": session_id},
                    UpdateExpression="DELETE connection_ids :cid_set",
                    ExpressionAttributeValues={":cid_set": {cid}},
                )
            except Exception:
                pass
        except Exception:
            logger.warning("Failed to post to %s", cid[:8])


def lambda_handler(event, context):
    if not WEBSOCKET_ENDPOINT:
        return {"processed": 0}

    processed = 0
    for record in event.get("Records", []):
        event_name = record.get("eventName", "")
        new_image = record.get("dynamodb", {}).get("NewImage", {})
        old_image = record.get("dynamodb", {}).get("OldImage", {})

        if not new_image:
            continue

        session_id = _get_str(new_image, "session_id")
        if not session_id:
            continue

        question = _get_str(new_image, "question")
        if not question:
            continue

        if event_name == "INSERT":
            # New QA pair created — broadcast questionDetected
            _broadcast(session_id, {
                "type": "questionDetected",
                "question": question,
                "speaker_role": _get_str(new_image, "speaker_role") or "unknown",
                "detection_method": _get_str(new_image, "detection_method") or "auto",
                "qa_pair_id": _get_str(new_image, "qa_pair_id"),
            })
            processed += 1

            # If the insert already has a suggested_answer, broadcast that too
            suggested = _get_str(new_image, "suggested_answer")
            if suggested:
                _broadcast(session_id, {
                    "type": "suggestedResponse",
                    "question": question,
                    "suggested_answer": suggested,
                    "qa_pair_id": _get_str(new_image, "qa_pair_id"),
                })
                processed += 1

            # If the insert already has an answer, broadcast qaPairAutoSaved
            answer = _get_str(new_image, "answer")
            if answer:
                _broadcast(session_id, {
                    "type": "qaPairAutoSaved",
                    "question": question,
                    "answer": answer,
                    "suggested_answer": suggested,
                    "source": _get_str(new_image, "source"),
                    "qa_pair_id": _get_str(new_image, "qa_pair_id"),
                })
                processed += 1

        elif event_name == "MODIFY":
            old_suggested = _get_str(old_image, "suggested_answer") if old_image else ""
            new_suggested = _get_str(new_image, "suggested_answer")
            old_answer = _get_str(old_image, "answer") if old_image else ""
            new_answer = _get_str(new_image, "answer")

            # suggested_answer was added or changed
            if new_suggested and new_suggested != old_suggested:
                _broadcast(session_id, {
                    "type": "suggestedResponse",
                    "question": question,
                    "suggested_answer": new_suggested,
                    "qa_pair_id": _get_str(new_image, "qa_pair_id"),
                })
                processed += 1

            # answer was added or changed
            if new_answer and new_answer != old_answer:
                _broadcast(session_id, {
                    "type": "qaPairAutoSaved",
                    "question": question,
                    "answer": new_answer,
                    "suggested_answer": new_suggested,
                    "source": _get_str(new_image, "source"),
                    "qa_pair_id": _get_str(new_image, "qa_pair_id"),
                })
                processed += 1

            # Check for unanswered status
            new_status = _get_str(new_image, "status")
            if new_status == "unanswered":
                _broadcast(session_id, {
                    "type": "questionUnanswered",
                    "question": question,
                    "speaker_role": _get_str(new_image, "speaker_role") or "unknown",
                    "qa_pair_id": _get_str(new_image, "qa_pair_id"),
                })
                processed += 1

    return {"processed": processed}
