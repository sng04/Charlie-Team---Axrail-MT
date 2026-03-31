"""QA Pairs CRUD Lambda Function.

Routes HTTP methods for the /qa-pairs resource, providing list, get,
and delete operations against the QAPairsTable DynamoDB table.
"""

import json
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

MAX_LIMIT = 100
DEFAULT_LIMIT = 20


def _parse_last_key(raw: str) -> dict:
    """Decode a JSON-encoded ExclusiveStartKey from the client."""
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        raise BadRequestError("Invalid lastKey format")


def list_qa_pairs(event: dict) -> dict:
    """Query QA pairs with optional session_id / project_id filters.

    When neither filter is provided, returns all QA pairs sorted by
    created_at descending via the created-at-index GSI.
    """
    params = event.get("queryStringParameters") or {}
    session_id = params.get("session_id")
    project_id = params.get("project_id")
    limit = min(int(params.get("limit", DEFAULT_LIMIT)), MAX_LIMIT)
    last_key_raw = params.get("lastKey")

    query_kwargs = {"Limit": limit}

    if last_key_raw:
        query_kwargs["ExclusiveStartKey"] = _parse_last_key(last_key_raw)

    if session_id:
        query_kwargs["IndexName"] = "session-index"
        query_kwargs["KeyConditionExpression"] = Key("session_id").eq(session_id)
        query_kwargs["ScanIndexForward"] = False
    elif project_id:
        query_kwargs["IndexName"] = "project-index"
        query_kwargs["KeyConditionExpression"] = Key("project_id").eq(project_id)
        query_kwargs["ScanIndexForward"] = False
    else:
        query_kwargs["IndexName"] = "created-at-index"
        query_kwargs["KeyConditionExpression"] = Key("gsi_pk").eq("ALL")
        query_kwargs["ScanIndexForward"] = False

    resp = qa_pairs_table.query(**query_kwargs)

    result = {
        "items": resp.get("Items", []),
        "lastKey": None,
    }

    if "LastEvaluatedKey" in resp:
        result["lastKey"] = json.dumps(resp["LastEvaluatedKey"])

    return createResponse(200, "QA pairs retrieved successfully", result)


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
