"""
GetSessionSummary Lambda Function

Returns the meeting summary markdown for a completed session.
GET /sessions/{sessionId}/summary

The summary is stored in S3 at: {project_id}/summaries/{session_id}.md
Written by the endMeeting WebSocket action.
"""

import os

from aws_lambda_powertools import Logger, Tracer
import boto3

from response_utils import createResponse
from custom_exceptions import BadRequestError, NotFoundError

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
s3_client = boto3.client("s3")

sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE", ""))
KB_BUCKET = os.environ.get("KB_BUCKET_NAME", "")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        path_params = event.get("pathParameters") or {}
        session_id = path_params.get("sessionId")
        if not session_id:
            raise BadRequestError("Session ID is required")

        # Look up the session to get project_id
        session_resp = sessions_table.get_item(Key={"session_id": session_id})
        if "Item" not in session_resp:
            raise NotFoundError(f"Session {session_id} not found")

        session = session_resp["Item"]
        project_id = session.get("project_id", "")

        if not project_id:
            raise NotFoundError("Session has no project_id")

        # Read summary from S3
        s3_key = f"{project_id}/summaries/{session_id}.md"
        try:
            response = s3_client.get_object(Bucket=KB_BUCKET, Key=s3_key)
            summary_markdown = response["Body"].read().decode("utf-8")
        except s3_client.exceptions.NoSuchKey:
            return createResponse(200, "No summary available", {
                "session_id": session_id,
                "summary_markdown": None,
                "status": "not_generated",
            })

        return createResponse(200, "Summary retrieved", {
            "session_id": session_id,
            "project_id": project_id,
            "summary_markdown": summary_markdown,
            "status": "available",
        })
    except BadRequestError as e:
        return createResponse(400, str(e))
    except NotFoundError as e:
        return createResponse(404, str(e))
    except Exception:
        logger.exception("Unexpected error")
        return createResponse(500, "Internal server error")
