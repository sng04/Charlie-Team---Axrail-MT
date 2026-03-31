"""Token usage tracking utility for Bedrock model invocations.

Provides fire-and-forget functions to log token consumption per action.
"""

import os
import uuid
from datetime import datetime, timezone

import boto3

TOKEN_USAGE_TABLE_NAME = os.environ.get("TOKEN_USAGE_TABLE_NAME", "")

_dynamodb = None
_table = None


def _get_table():
    global _dynamodb, _table
    if _table is None and TOKEN_USAGE_TABLE_NAME:
        _dynamodb = _dynamodb or boto3.resource("dynamodb")
        _table = _dynamodb.Table(TOKEN_USAGE_TABLE_NAME)
    return _table


def _extract_token_usage(result) -> tuple:
    """Extract input/output token counts from a Strands agent result."""
    try:
        # Strands SDK stores accumulated usage on result.metrics.accumulated_usage
        if hasattr(result, "metrics") and hasattr(result.metrics, "accumulated_usage"):
            usage = result.metrics.accumulated_usage
            return int(usage.get("inputTokens", 0)), int(usage.get("outputTokens", 0))
        # Fallback: check metrics as dict
        if hasattr(result, "metrics"):
            metrics = result.metrics if isinstance(result.metrics, dict) else {}
            usage = metrics.get("usage", {}) or metrics.get("accumulated_usage", {})
            if usage:
                return int(usage.get("inputTokens", 0)), int(usage.get("outputTokens", 0))
        if hasattr(result, "usage"):
            usage = result.usage if isinstance(result.usage, dict) else {}
            return int(usage.get("inputTokens", 0)), int(usage.get("outputTokens", 0))
        # Try Strands agent's internal state
        if hasattr(result, "_model_response"):
            resp = result._model_response or {}
            usage = resp.get("usage", {})
            if usage:
                return int(usage.get("inputTokens", 0)), int(usage.get("outputTokens", 0))
    except Exception:
        pass
    return 0, 0


def track_token_usage(
    session_id: str,
    action: str,
    model_id: str,
    input_tokens: int,
    output_tokens: int,
    project_id: str = "",
    estimated: bool = False,
) -> None:
    """Write a token usage record. Fire-and-forget."""
    table = _get_table()
    if not table:
        return
    try:
        now = datetime.now(timezone.utc).isoformat()
        table.put_item(Item={
            "usage_id": str(uuid.uuid4()),
            "session_id": session_id,
            "project_id": project_id,
            "action": action,
            "model_id": model_id,
            "input_tokens": max(0, input_tokens),
            "output_tokens": max(0, output_tokens),
            "total_tokens": max(0, input_tokens + output_tokens),
            "estimated": estimated,
            "timestamp": now,
        })
    except Exception:
        pass
