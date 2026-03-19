"""DynamoDB access, connection cache, WebSocket posting, and session helpers."""

import json
from datetime import datetime

import boto3
from aws_lambda_powertools import Logger, Tracer

from constants import (
    AGENTS_TABLE_NAME,
    DEFAULT_AGENT,
    DEFAULT_PERSONALITY_PROMPT,
    PERSONALITIES_TABLE_NAME,
    SESSIONS_TABLE_NAME,
    SKILLS_TABLE_NAME,
    WEBSOCKET_ENDPOINT,
)

logger = Logger(child=True)
tracer = Tracer()

# Module-level caches
_connection_prompts = {}
_dynamodb = None


# ---------------------------------------------------------------------------
# DynamoDB helpers
# ---------------------------------------------------------------------------


def _get_dynamodb():
    """Return a cached DynamoDB resource."""
    global _dynamodb
    if _dynamodb is None:
        _dynamodb = boto3.resource("dynamodb")
    return _dynamodb


def _lookup_project_id(session_id: str) -> str:
    """Look up project_id from SessionsTable via session_id."""
    if not session_id:
        return "default-project"
    if not SESSIONS_TABLE_NAME:
        logger.warning("SESSIONS_TABLE_NAME not configured — using default-project")
        return "default-project"
    try:
        table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
        resp = table.get_item(Key={"session_id": session_id})
        item = resp.get("Item")
        if item and item.get("project_id"):
            return item["project_id"]
    except Exception:
        logger.exception("Failed to look up session %s", session_id)
    return "default-project"


def _load_agent(agent_id: str) -> dict | None:
    """Load an agent record from DynamoDB. Returns None on failure."""
    if not agent_id:
        return None
    try:
        table = _get_dynamodb().Table(AGENTS_TABLE_NAME)
        resp = table.get_item(Key={"agent_id": agent_id})
        return resp.get("Item")
    except Exception:
        logger.exception("Failed to load agent %s", agent_id)
        return None


def _load_personality(personality_id: str) -> str | None:
    """Load a personality prompt from DynamoDB. Returns None on failure."""
    if not personality_id:
        return None
    try:
        table = _get_dynamodb().Table(PERSONALITIES_TABLE_NAME)
        resp = table.get_item(Key={"personality_id": personality_id})
        item = resp.get("Item")
        return item.get("personality_prompt") if item else None
    except Exception:
        logger.exception("Failed to load personality %s", personality_id)
        return None


def _load_agent_skills(agent_id: str) -> list:
    """Load active skills for an agent from SkillsTable.

    Queries the agent-index GSI filtered by status="active".
    Returns an empty list on failure or if no skills exist.
    """
    if not agent_id or not SKILLS_TABLE_NAME:
        return []
    try:
        from boto3.dynamodb.conditions import Attr, Key

        table = _get_dynamodb().Table(SKILLS_TABLE_NAME)
        resp = table.query(
            IndexName="agent-index",
            KeyConditionExpression=Key("agent_id").eq(agent_id),
            FilterExpression=Attr("status").eq("active"),
        )
        return resp.get("Items", [])
    except Exception:
        logger.exception("Failed to load skills for agent %s", agent_id)
        return []


def build_system_prompt(agent_id: str | None = None) -> tuple[str, str]:
    """Build the system prompt from agent and personality records.

    Returns (system_prompt, agent_name).
    """
    agent = _load_agent(agent_id) if agent_id else None
    if agent is None:
        agent = DEFAULT_AGENT
        logger.info("Using default agent (agent_id=%s)", agent_id)

    personality_prompt = _load_personality(agent.get("personality_id"))
    if personality_prompt is None:
        personality_prompt = DEFAULT_PERSONALITY_PROMPT
        logger.info("Using default personality")

    if "role_prompt" in agent and "task_prompt" in agent:
        system_prompt = (
            f"## Role\n{agent['role_prompt']}\n\n"
            f"## Tasks\n{agent['task_prompt']}\n\n"
            f"## Communication Style\n{personality_prompt}"
        )
    elif "system_prompt" in agent:
        system_prompt = (
            f"{agent['system_prompt']}\n\n"
            f"## Communication Style\n{personality_prompt}"
        )
    else:
        system_prompt = f"## Communication Style\n{personality_prompt}"

    return system_prompt, agent.get("agent_name", "Meeting Assistant")


# ---------------------------------------------------------------------------
# WebSocket helpers
# ---------------------------------------------------------------------------


def _post_to_connection(connection_id: str, data: dict) -> None:
    """Post a message back to the WebSocket client."""
    endpoint = WEBSOCKET_ENDPOINT
    if not endpoint:
        logger.error("WEBSOCKET_ENDPOINT not configured")
        return
    try:
        apigw = boto3.client(
            "apigatewaymanagementapi", endpoint_url=f"https://{endpoint}"
        )
        apigw.post_to_connection(
            ConnectionId=connection_id,
            Data=json.dumps(data).encode("utf-8"),
        )
    except Exception:
        logger.exception("Failed to post to connection %s", connection_id)


def _get_conn_data(connection_id: str) -> dict:
    """Retrieve or rebuild connection data from cache."""
    conn_data = _connection_prompts.get(connection_id)
    if conn_data is None:
        system_prompt, agent_name = build_system_prompt()
        conn_data = {
            "system_prompt": system_prompt,
            "agent_name": agent_name,
            "project_id": "default-project",
            "session_id": "",
        }
        _connection_prompts[connection_id] = conn_data
    return conn_data


# ---------------------------------------------------------------------------
# Session lifecycle helpers
# ---------------------------------------------------------------------------


def _mark_session_active(session_id: str, connection_id: str) -> None:
    """Update SessionsTable to mark a session as active."""
    if not session_id or not SESSIONS_TABLE_NAME:
        return
    try:
        table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
        table.update_item(
            Key={"session_id": session_id},
            UpdateExpression=(
                "SET is_active = :active, last_activity_at = :ts, "
                "connection_id = :cid"
            ),
            ExpressionAttributeValues={
                ":active": "active",
                ":ts": datetime.utcnow().isoformat() + "Z",
                ":cid": connection_id,
            },
        )
    except Exception:
        logger.exception("Failed to mark session %s as active", session_id)


def _mark_session_inactive(session_id: str) -> None:
    """Update SessionsTable to mark a session as inactive."""
    if not session_id or not SESSIONS_TABLE_NAME:
        return
    try:
        table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
        table.update_item(
            Key={"session_id": session_id},
            UpdateExpression="SET is_active = :inactive",
            ExpressionAttributeValues={":inactive": "inactive"},
        )
    except Exception:
        logger.exception("Failed to mark session %s as inactive", session_id)


def _is_session_completed(session_id: str) -> bool | None:
    """Check if a session is completed (is_active = 'inactive').

    Returns True if completed, False if still active, None if lookup fails.
    """
    if not session_id or not SESSIONS_TABLE_NAME:
        return None
    try:
        table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
        resp = table.get_item(Key={"session_id": session_id})
        item = resp.get("Item")
        if not item:
            return None
        return item.get("is_active") == "inactive"
    except Exception:
        logger.exception("Failed to check session status for %s", session_id)
        return None
