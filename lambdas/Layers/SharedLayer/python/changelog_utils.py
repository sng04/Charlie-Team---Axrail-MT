"""Admin changelog utility for audit trail of CRUD operations.

Provides a single fire-and-forget function that any Lambda can call
after a successful write to record who changed what and when.
"""

import os
import uuid
from datetime import datetime, timezone

import boto3

ADMIN_CHANGELOG_TABLE_NAME = os.environ.get("ADMIN_CHANGELOG_TABLE_NAME", "")
SENSITIVE_FIELDS = {"password", "secret", "token", "access_token", "secret_string"}

_dynamodb = None
_table = None


def _get_table():
    """Return a cached DynamoDB Table resource."""
    global _dynamodb, _table
    if _table is None and ADMIN_CHANGELOG_TABLE_NAME:
        _dynamodb = _dynamodb or boto3.resource("dynamodb")
        _table = _dynamodb.Table(ADMIN_CHANGELOG_TABLE_NAME)
    return _table


def _strip_sensitive(data: dict) -> dict:
    """Remove sensitive fields from a data dict."""
    if not data:
        return {}
    return {k: v for k, v in data.items() if k.lower() not in SENSITIVE_FIELDS}


def _extract_admin(event: dict) -> tuple:
    """Extract admin user_id and username from authorizer context."""
    ctx = event.get("requestContext", {}).get("authorizer", {})
    return ctx.get("user_id", "system"), ctx.get("username", "system")


def log_admin_change(
    event: dict,
    entity_type: str,
    entity_id: str,
    action: str,
    data: dict = None,
    previous_data: dict = None,
    changed_fields: list = None,
    entity_name: str = "",
) -> None:
    """Write a changelog entry. Fire-and-forget — never raises.

    Args:
        event: The API Gateway event (used to extract admin identity).
        entity_type: e.g. "user", "project", "agent", "bot_credential".
        entity_id: The primary key of the entity.
        action: "create", "update", or "delete".
        data: Entity snapshot after create, or changed fields for update.
        previous_data: Previous values for update, full snapshot for delete.
        changed_fields: List of field names that changed (update only).
        entity_name: Human-readable name of the entity at the time of the action.
    """
    table = _get_table()
    if not table:
        return
    try:
        admin_user_id, admin_username = _extract_admin(event)
        now = datetime.now(timezone.utc).isoformat()

        item = {
            "changelog_id": str(uuid.uuid4()),
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action": action,
            "admin_user_id": admin_user_id,
            "admin_username": admin_username,
            "timestamp": now,
        }

        if entity_name:
            item["entity_name"] = entity_name
        if data:
            item["data"] = _strip_sensitive(data)
        if previous_data:
            item["previous_data"] = _strip_sensitive(previous_data)
        if changed_fields:
            item["changed_fields"] = changed_fields

        table.put_item(Item=item)
    except Exception:
        pass  # Fire-and-forget — never block the CRUD operation


def log_audit_event(
    entity_type: str,
    entity_id: str,
    action: str,
    data: dict = None,
    username: str = "",
    ip_address: str = "",
    entity_name: str = "",
) -> None:
    """Write an audit event entry (e.g., login attempts). Fire-and-forget.

    Unlike log_admin_change, this doesn't require an API Gateway event
    with authorizer context — the caller provides identity directly.

    Args:
        entity_type: e.g. "login_attempt", "password_change".
        entity_id: The username or user_id involved.
        action: e.g. "login_success", "login_failed", "login_locked".
        data: Additional context (e.g., reason for failure).
        username: The username attempting the action.
        ip_address: Source IP if available.
        entity_name: Human-readable name of the entity.
    """
    table = _get_table()
    if not table:
        return
    try:
        now = datetime.now(timezone.utc).isoformat()
        item = {
            "changelog_id": str(uuid.uuid4()),
            "entity_type": entity_type,
            "entity_id": entity_id,
            "action": action,
            "admin_user_id": username,
            "admin_username": username,
            "timestamp": now,
        }
        if entity_name:
            item["entity_name"] = entity_name
        if data:
            item["data"] = _strip_sensitive(data)
        if ip_address:
            item["ip_address"] = ip_address
        table.put_item(Item=item)
    except Exception:
        pass
