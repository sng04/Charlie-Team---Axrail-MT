"""DynamoDB access, connection cache, WebSocket posting, and session helpers."""

import json
from datetime import datetime, timezone

import boto3
from aws_lambda_powertools import Logger, Tracer

from constants import (
    AGENT_SKILLS_TABLE_NAME,
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
    """Load active skills for an agent via the AgentSkills junction table.

    Queries AgentSkills_Table by agent_id to get skill_ids, then batch-gets
    skill records from Skills_Table filtered by status="active".
    Returns an empty list on failure or if no skills exist.
    """
    if not agent_id or not AGENT_SKILLS_TABLE_NAME or not SKILLS_TABLE_NAME:
        return []
    try:
        from boto3.dynamodb.conditions import Key

        # Step 1: Query junction table for assigned skill_ids
        junction_table = _get_dynamodb().Table(AGENT_SKILLS_TABLE_NAME)
        resp = junction_table.query(
            KeyConditionExpression=Key("agent_id").eq(agent_id),
        )
        skill_ids = [item["skill_id"] for item in resp.get("Items", [])]
        if not skill_ids:
            return []

        # Step 2: Batch-get skill records and filter by active status
        skills_table = _get_dynamodb().Table(SKILLS_TABLE_NAME)
        active_skills = []
        for sid in skill_ids:
            r = skills_table.get_item(Key={"skill_id": sid})
            item = r.get("Item")
            if item and item.get("status") == "active":
                active_skills.append(item)
        return active_skills
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

    behavior = agent.get("behavior_guidelines") or agent.get("task_prompt")
    if agent.get("role_prompt") and behavior:
        system_prompt = (
            f"## Role\n{agent['role_prompt']}\n\n"
            f"## Behavior Guidelines\n{behavior}\n\n"
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
        # Strip protocol prefix if already present to avoid double-https
        clean_endpoint = endpoint.replace("https://", "").replace("http://", "")
        apigw = boto3.client(
            "apigatewaymanagementapi", endpoint_url=f"https://{clean_endpoint}"
        )
        apigw.post_to_connection(
            ConnectionId=connection_id,
            Data=json.dumps(data).encode("utf-8"),
        )
    except Exception:
        logger.exception("Failed to post to connection %s", connection_id)


def _broadcast_to_session(
    session_id: str, data: dict, exclude_connection_id: str = ""
) -> None:
    """Broadcast a message to all active WebSocket connections for a session.

    Iterates the in-memory connection cache to find all connections with
    the matching session_id and posts the message to each one.

    Args:
        session_id: The session to broadcast to.
        data: The message payload to send.
        exclude_connection_id: Optional connection to skip (the caller).
    """
    if not session_id:
        return
    for conn_id, conn_data in _connection_prompts.items():
        if conn_data.get("session_id") == session_id and conn_id != exclude_connection_id:
            _post_to_connection(conn_id, data)


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
                ":ts": datetime.now(timezone.utc).isoformat(),
                ":cid": connection_id,
            },
        )
    except Exception:
        logger.exception("Failed to mark session %s as active", session_id)


def _mark_session_inactive(session_id: str) -> None:
    """Update SessionsTable to mark a session as completed (meeting ended)."""
    if not session_id or not SESSIONS_TABLE_NAME:
        return
    try:
        table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
        table.update_item(
            Key={"session_id": session_id},
            UpdateExpression="SET is_active = :completed",
            ExpressionAttributeValues={":completed": "completed"},
        )
    except Exception:
        logger.exception("Failed to mark session %s as completed", session_id)


def _is_session_completed(session_id: str) -> bool | None:
    """Check if a session is completed (is_active = 'completed').

    Returns True if completed, False if still active/inactive, None if lookup fails.
    """
    if not session_id or not SESSIONS_TABLE_NAME:
        return None
    try:
        table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
        resp = table.get_item(Key={"session_id": session_id})
        item = resp.get("Item")
        if not item:
            return None
        return item.get("is_active") == "completed"
    except Exception:
        logger.exception("Failed to check session status for %s", session_id)
        return None
