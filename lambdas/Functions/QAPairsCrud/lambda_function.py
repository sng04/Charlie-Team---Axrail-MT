"""QA Pairs CRUD Lambda Function.

Routes HTTP methods for the /qa-pairs resource, providing list, get,
and delete operations against the QAPairsTable DynamoDB table.
"""

import os

import boto3
from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Key

from custom_exceptions import BadRequestError, NotFoundError
from response_utils import createResponse

logger = Logger()
tracer = Tracer()

QA_PAIRS_TABLE_NAME = os.environ.get("QA_PAIRS_TABLE_NAME", "")

dynamodb = boto3.resource("dynamodb")
qa_pairs_table = dynamodb.Table(QA_PAIRS_TABLE_NAME)


def list_qa_pairs(event: dict) -> dict:
    """Query QA pairs by session_id or project_id via the appropriate GSI."""
    params = event.get("queryStringParameters") or {}
    session_id = params.get("session_id")
    project_id = params.get("project_id")

    if not session_id and not project_id:
        raise BadRequestError(
            "session_id or project_id query parameter required"
        )

    if session_id:
        resp = qa_pairs_table.query(
            IndexName="session-index",
            KeyConditionExpression=Key("session_id").eq(session_id),
        )
    else:
        resp = qa_pairs_table.query(
            IndexName="project-index",
            KeyConditionExpression=Key("project_id").eq(project_id),
        )

    items = resp.get("Items", [])
    return createResponse(200, "QA pairs retrieved successfully", items)


def get_qa_pair(event: dict) -> dict:
    """Get a single QA pair by qaPairId."""
    qa_pair_id = event.get("pathParameters", {}).get("qaPairId", "")
    resp = qa_pairs_table.get_item(Key={"qa_pair_id": qa_pair_id})
    item = resp.get("Item")
    if not item:
        raise NotFoundError("QA pair not found")
    return createResponse(200, "QA pair retrieved successfully", item)


def delete_qa_pair(event: dict) -> dict:
    """Delete a QA pair by qaPairId."""
    qa_pair_id = event.get("pathParameters", {}).get("qaPairId", "")
    resp = qa_pairs_table.get_item(Key={"qa_pair_id": qa_pair_id})
    if "Item" not in resp:
        raise NotFoundError("QA pair not found")
    qa_pairs_table.delete_item(Key={"qa_pair_id": qa_pair_id})
    return createResponse(200, "QA pair deleted successfully")


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """Main Lambda entry point — routes based on httpMethod and resource."""
    try:
        http_method = event.get("httpMethod", "")
        resource = event.get("resource", "")

        if resource == "/qa-pairs" and http_method == "GET":
            return list_qa_pairs(event)
        elif resource == "/qa-pairs/{qaPairId}" and http_method == "GET":
            return get_qa_pair(event)
        elif resource == "/qa-pairs/{qaPairId}" and http_method == "DELETE":
            return delete_qa_pair(event)
        else:
            raise BadRequestError(
                f"Unsupported route: {http_method} {resource}"
            )
    except BadRequestError as e:
        logger.warning("Bad request", extra={"error": str(e)})
        tracer.put_annotation("error", str(e))
        return createResponse(400, str(e))
    except NotFoundError as e:
        logger.warning("Not found", extra={"error": str(e)})
        tracer.put_annotation("error", str(e))
        return createResponse(404, str(e))
    except Exception:
        logger.exception("Internal server error")
        tracer.put_annotation("error", "internal_server_error")
        return createResponse(500, "Internal server error")
