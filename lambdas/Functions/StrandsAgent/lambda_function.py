"""Strands agent WebSocket Lambda handler.

Routes WebSocket events ($connect, $disconnect) and dispatches message
actions (sendMessage, detectQuestion, extractQAPair, processTranscript, etc.)
through a task router. Each action shares the same agent identity (system
prompt from DynamoDB) but gets a task-specific instruction overlay.
"""

import json

from aws_lambda_powertools import Logger, Tracer

from helpers import _post_to_connection
from handlers import (
    _handle_connect,
    _handle_disconnect,
    _handle_send_message,
    _handle_detect_question,
    _handle_extract_qa_pair,
    _handle_analyze_gaps,
    _handle_end_meeting,
    _handle_retro_analysis,
    _handle_retro_chat,
    _handle_set_suggested_questions,
)
from transcript import _handle_process_transcript

logger = Logger()
tracer = Tracer()


def _handle_action(event: dict) -> dict:
    """Dispatch message events to the appropriate action handler."""
    connection_id = event["requestContext"]["connectionId"]
    raw_body = event.get("body", "{}")
    try:
        body = json.loads(raw_body) if isinstance(raw_body, str) else raw_body
    except (json.JSONDecodeError, TypeError):
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Invalid JSON in request body",
        })
        return {"statusCode": 400, "body": "Invalid JSON"}

    action = body.get("action", "sendMessage")

    dispatch = {
        "sendMessage": lambda: _handle_send_message(body, connection_id),
        "detectQuestion": lambda: _handle_detect_question(body, connection_id),
        "extractQAPair": lambda: _handle_extract_qa_pair(body, connection_id),
        "analyzeGaps": lambda: _handle_analyze_gaps(body, connection_id),
        "endMeeting": lambda: _handle_end_meeting(body, connection_id),
        "retroAnalysis": lambda: _handle_retro_analysis(body, connection_id),
        "retroChat": lambda: _handle_retro_chat(body, connection_id),
        "processTranscript": lambda: _handle_process_transcript(body, connection_id),
        "setSuggestedQuestions": lambda: _handle_set_suggested_questions(body, connection_id),
    }

    handler = dispatch.get(action)
    if handler:
        return handler()

    _post_to_connection(connection_id, {
        "type": "error",
        "message": f"Unsupported action: {action}",
    })
    return {"statusCode": 400, "body": f"Unsupported action: {action}"}


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """Main Lambda entry point — routes WebSocket events."""
    route_key = event.get("requestContext", {}).get("routeKey", "")
    logger.info("Route: %s", route_key)

    if route_key == "$connect":
        return _handle_connect(event)
    elif route_key == "$disconnect":
        return _handle_disconnect(event)
    else:
        return _handle_action(event)
