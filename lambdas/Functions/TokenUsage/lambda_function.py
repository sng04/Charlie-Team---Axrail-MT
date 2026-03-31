"""
TokenUsage Lambda Function

Retrieval endpoints for token usage data:
  GET /admin/token-usage/summary?period=YYYY-MM
  GET /admin/token-usage/daily?period=YYYY-MM
  GET /admin/token-usage/by-project?period=YYYY-MM
  GET /sessions/{sessionId}/token-usage
"""

import os
from collections import defaultdict
from datetime import datetime, timezone
from decimal import Decimal

import boto3
from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Attr

from response_utils import createResponse

logger = Logger()
tracer = Tracer()

dynamodb = boto3.resource("dynamodb")
token_table = dynamodb.Table(os.environ.get("TOKEN_USAGE_TABLE_NAME", ""))
sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE", ""))
projects_table = dynamodb.Table(os.environ.get("PROJECTS_TABLE", ""))
qa_pairs_table = dynamodb.Table(os.environ.get("QA_PAIRS_TABLE_NAME", ""))

# Nova Pro pricing (per 1K tokens)
COST_INPUT_PER_1K = 0.0008
COST_OUTPUT_PER_1K = 0.0032


def _get_period(event):
    params = event.get("queryStringParameters") or {}
    period = params.get("period", "")
    if not period:
        period = datetime.now(timezone.utc).strftime("%Y-%m")
    return period


def _scan_period(period):
    """Scan TokenUsage table for records matching a YYYY-MM period."""
    items = []
    scan_kwargs = {
        "FilterExpression": Attr("timestamp").begins_with(period),
    }
    while True:
        resp = token_table.scan(**scan_kwargs)
        items.extend(resp.get("Items", []))
        if "LastEvaluatedKey" not in resp:
            break
        scan_kwargs["ExclusiveStartKey"] = resp["LastEvaluatedKey"]
    return items


def _estimate_cost(input_tokens, output_tokens):
    return round(float(input_tokens) / 1000 * COST_INPUT_PER_1K + float(output_tokens) / 1000 * COST_OUTPUT_PER_1K, 4)


def handle_summary(event):
    period = _get_period(event)
    items = _scan_period(period)

    total_input = sum(int(i.get("input_tokens", 0)) for i in items)
    total_output = sum(int(i.get("output_tokens", 0)) for i in items)
    session_ids = set(i.get("session_id", "") for i in items if i.get("session_id"))

    # Count QA pairs for the period
    qa_count = 0
    try:
        for sid in session_ids:
            from boto3.dynamodb.conditions import Key
            resp = qa_pairs_table.query(
                IndexName="session-index",
                KeyConditionExpression=Key("session_id").eq(sid),
                Select="COUNT",
            )
            qa_count += resp.get("Count", 0)
    except Exception:
        pass

    return createResponse(200, "Usage summary", {
        "period": period,
        "total_tokens": total_input + total_output,
        "total_input_tokens": total_input,
        "total_output_tokens": total_output,
        "estimated_cost_usd": _estimate_cost(total_input, total_output),
        "total_sessions": len(session_ids),
        "total_qa_pairs": qa_count,
    })


def handle_daily(event):
    period = _get_period(event)
    items = _scan_period(period)

    daily = defaultdict(lambda: {"tokens": 0, "input_tokens": 0, "output_tokens": 0, "sessions": set()})
    for i in items:
        date = i.get("timestamp", "")[:10]
        inp = int(i.get("input_tokens", 0))
        out = int(i.get("output_tokens", 0))
        daily[date]["tokens"] += inp + out
        daily[date]["input_tokens"] += inp
        daily[date]["output_tokens"] += out
        if i.get("session_id"):
            daily[date]["sessions"].add(i["session_id"])

    days = sorted([
        {"date": d, "tokens": v["tokens"], "input_tokens": v["input_tokens"],
         "output_tokens": v["output_tokens"], "sessions": len(v["sessions"])}
        for d, v in daily.items()
    ], key=lambda x: x["date"])

    return createResponse(200, "Daily breakdown", {"period": period, "days": days})


def handle_by_project(event):
    period = _get_period(event)
    items = _scan_period(period)

    by_project = defaultdict(lambda: {"total_tokens": 0, "input_tokens": 0, "output_tokens": 0, "sessions": set()})
    for i in items:
        pid = i.get("project_id", "unknown")
        inp = int(i.get("input_tokens", 0))
        out = int(i.get("output_tokens", 0))
        by_project[pid]["total_tokens"] += inp + out
        by_project[pid]["input_tokens"] += inp
        by_project[pid]["output_tokens"] += out
        if i.get("session_id"):
            by_project[pid]["sessions"].add(i["session_id"])

    # Resolve project names
    projects = []
    for pid, v in by_project.items():
        name = pid
        try:
            resp = projects_table.get_item(Key={"project_id": pid}, ProjectionExpression="#n", ExpressionAttributeNames={"#n": "name"})
            name = resp.get("Item", {}).get("name", pid)
        except Exception:
            pass

        # Count QA pairs
        qa_count = 0
        try:
            from boto3.dynamodb.conditions import Key
            for sid in v["sessions"]:
                resp = qa_pairs_table.query(IndexName="session-index", KeyConditionExpression=Key("session_id").eq(sid), Select="COUNT")
                qa_count += resp.get("Count", 0)
        except Exception:
            pass

        projects.append({
            "project_id": pid,
            "project_name": name,
            "total_tokens": v["total_tokens"],
            "total_sessions": len(v["sessions"]),
            "total_qa_pairs": qa_count,
            "estimated_cost_usd": _estimate_cost(v["input_tokens"], v["output_tokens"]),
        })

    projects.sort(key=lambda x: x["total_tokens"], reverse=True)
    return createResponse(200, "Usage by project", {"period": period, "projects": projects})


def handle_session(event):
    session_id = event.get("pathParameters", {}).get("sessionId", "")
    if not session_id:
        return createResponse(400, "Session ID required")

    from boto3.dynamodb.conditions import Key
    resp = token_table.query(
        IndexName="session-index",
        KeyConditionExpression=Key("session_id").eq(session_id),
    )
    items = resp.get("Items", [])

    total_input = sum(int(i.get("input_tokens", 0)) for i in items)
    total_output = sum(int(i.get("output_tokens", 0)) for i in items)

    breakdown = defaultdict(lambda: {"input_tokens": 0, "output_tokens": 0, "count": 0, "estimated": False})
    for i in items:
        action = i.get("action", "unknown")
        breakdown[action]["input_tokens"] += int(i.get("input_tokens", 0))
        breakdown[action]["output_tokens"] += int(i.get("output_tokens", 0))
        breakdown[action]["count"] += 1
        if i.get("estimated"):
            breakdown[action]["estimated"] = True

    return createResponse(200, "Session token usage", {
        "session_id": session_id,
        "total_input_tokens": total_input,
        "total_output_tokens": total_output,
        "total_tokens": total_input + total_output,
        "estimated_cost_usd": _estimate_cost(total_input, total_output),
        "breakdown": [{"action": k, **v} for k, v in breakdown.items()],
    })


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        resource = event.get("resource", "")
        if resource == "/admin/token-usage/summary":
            return handle_summary(event)
        elif resource == "/admin/token-usage/daily":
            return handle_daily(event)
        elif resource == "/admin/token-usage/by-project":
            return handle_by_project(event)
        elif resource == "/sessions/{sessionId}/token-usage":
            return handle_session(event)
        else:
            return createResponse(400, f"Unknown route: {resource}")
    except Exception:
        logger.exception("Unexpected error")
        return createResponse(500, "Internal server error")
