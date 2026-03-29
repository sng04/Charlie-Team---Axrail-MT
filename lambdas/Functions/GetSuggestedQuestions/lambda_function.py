"""
GetSuggestedQuestions Lambda Function

Returns suggested questions for a session.
GET /sessions/{sessionId}/suggested-questions
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3
from boto3.dynamodb.conditions import Key

from response_utils import createResponse
from custom_exceptions import BadRequestError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ.get("SUGGESTED_QUESTIONS_TABLE_NAME", ""))


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        path_params = event.get("pathParameters") or {}
        session_id = path_params.get("sessionId")
        if not session_id:
            raise BadRequestError("Session ID is required")

        response = table.query(
            IndexName="session-index",
            KeyConditionExpression=Key("session_id").eq(session_id),
        )
        items = response.get("Items", [])

        # Sort by created_at
        items.sort(key=lambda x: x.get("created_at", ""))

        questions = [
            {
                "question_id": item["question_id"],
                "question_text": item.get("question_text", ""),
                "matched": item.get("matched", False),
                "created_at": item.get("created_at", ""),
            }
            for item in items
        ]

        return createResponse(200, "Suggested questions retrieved", {
            "session_id": session_id,
            "questions": questions,
            "count": len(questions),
        })
    except BadRequestError as e:
        return createResponse(400, str(e))
    except Exception:
        logger.exception("Unexpected error")
        return createResponse(500, "Internal server error")
