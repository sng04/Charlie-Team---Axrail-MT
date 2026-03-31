"""AgentSkillsCrud Lambda – assign, unassign, and list agent-skill assignments.

Routes:
  POST   /agents/{agentId}/skills/{skillId}  → assign_skill
  DELETE /agents/{agentId}/skills/{skillId}  → unassign_skill
  GET    /agents/{agentId}/skills            → list_agent_skills
"""

import os
from datetime import datetime, timezone

import boto3
from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Key

from changelog_utils import log_admin_change
from custom_exceptions import BadRequestError, NotFoundError
from response_utils import createResponse

logger = Logger()
tracer = Tracer()

AGENTS_TABLE_NAME = os.environ.get("AGENTS_TABLE_NAME", "")
SKILLS_TABLE_NAME = os.environ.get("SKILLS_TABLE_NAME", "")
AGENT_SKILLS_TABLE_NAME = os.environ.get("AGENT_SKILLS_TABLE_NAME", "")
AGENT_CONFIG_HISTORY_TABLE_NAME = os.environ.get("AGENT_CONFIG_HISTORY_TABLE_NAME", "")
PERSONALITIES_TABLE_NAME = os.environ.get("PERSONALITIES_TABLE_NAME", "")

dynamodb = boto3.resource("dynamodb")
agents_table = dynamodb.Table(AGENTS_TABLE_NAME)
skills_table = dynamodb.Table(SKILLS_TABLE_NAME)
agent_skills_table = dynamodb.Table(AGENT_SKILLS_TABLE_NAME)
history_table = dynamodb.Table(AGENT_CONFIG_HISTORY_TABLE_NAME) if AGENT_CONFIG_HISTORY_TABLE_NAME else None


def _save_agent_snapshot(agent_id: str, changed_fields: list) -> None:
    """Save a config history snapshot when skills change.

    Includes a 5-second debounce: if a snapshot was written for this agent
    within the last 5 seconds, skip to avoid duplicates when the frontend
    fires multiple API calls for a single user action.
    """
    if not history_table:
        return
    try:
        # Get current agent config
        agent_resp = agents_table.get_item(Key={"agent_id": agent_id})
        agent = agent_resp.get("Item", {})
        if not agent:
            return

        # Get latest version + debounce check
        resp = history_table.query(
            KeyConditionExpression=Key("agent_id").eq(agent_id),
            ScanIndexForward=False,
            Limit=1,
        )
        items = resp.get("Items", [])
        next_version = int(items[0]["version"]) + 1 if items else 1

        # Debounce: skip if last snapshot was within 5 seconds
        if items:
            last_snapshot_at = items[0].get("snapshot_at", "")
            if last_snapshot_at:
                from datetime import datetime as dt
                try:
                    last_time = dt.fromisoformat(last_snapshot_at.replace("Z", "+00:00"))
                    now_time = dt.now(timezone.utc)
                    if (now_time - last_time).total_seconds() < 5:
                        return  # Skip — recent snapshot exists
                except (ValueError, TypeError):
                    pass

        # Get personality name
        personality_name = ""
        pid = agent.get("personality_id", "")
        if pid and PERSONALITIES_TABLE_NAME:
            try:
                pr = dynamodb.Table(PERSONALITIES_TABLE_NAME).get_item(
                    Key={"personality_id": pid}, ProjectionExpression="personality_name"
                )
                personality_name = pr.get("Item", {}).get("personality_name", "")
            except Exception:
                pass

        # Get current skill names
        skill_names = []
        try:
            jr = agent_skills_table.query(KeyConditionExpression=Key("agent_id").eq(agent_id))
            for j in jr.get("Items", []):
                sr = skills_table.get_item(Key={"skill_id": j["skill_id"]}, ProjectionExpression="skill_name")
                name = sr.get("Item", {}).get("skill_name")
                if name:
                    skill_names.append(name)
        except Exception:
            pass

        now = datetime.now(timezone.utc).isoformat()
        history_table.put_item(Item={
            "agent_id": agent_id,
            "version": next_version,
            "agent_name": agent.get("agent_name", ""),
            "role_prompt": agent.get("role_prompt", ""),
            "behavior_guidelines": agent.get("behavior_guidelines", ""),
            "personality_id": pid,
            "personality_name": personality_name,
            "model_id": agent.get("model_id", ""),
            "use_case": agent.get("use_case", ""),
            "skill_names": skill_names,
            "changed_fields": changed_fields,
            "created_at": agent.get("created_at", ""),
            "snapshot_at": now,
        })
    except Exception:
        logger.warning("Failed to save agent config snapshot", extra={"agent_id": agent_id})


def assign_skill(event: dict) -> dict:
    """Assign a skill to an agent (idempotent)."""
    agent_id = event["pathParameters"]["agentId"]
    skill_id = event["pathParameters"]["skillId"]

    # Validate agent exists
    resp = agents_table.get_item(Key={"agent_id": agent_id})
    if "Item" not in resp:
        raise NotFoundError("Agent not found")

    # Validate skill exists
    resp = skills_table.get_item(Key={"skill_id": skill_id})
    if "Item" not in resp:
        raise NotFoundError("Skill not found")

    # Check if assignment already exists (idempotent)
    resp = agent_skills_table.get_item(
        Key={"agent_id": agent_id, "skill_id": skill_id}
    )
    if "Item" in resp:
        return createResponse(200, "Skill already assigned", resp["Item"])

    # Create junction record
    now = datetime.now(timezone.utc).isoformat()
    item = {
        "agent_id": agent_id,
        "skill_id": skill_id,
        "assigned_at": now,
    }
    agent_skills_table.put_item(Item=item)
    log_admin_change(event, "agent_skill_assignment", f"{agent_id}:{skill_id}", "create", data=item, entity_name="")

    _save_agent_snapshot(agent_id, ["skills_assigned"])

    return createResponse(200, "Skill assigned", item)


def unassign_skill(event: dict) -> dict:
    """Remove a skill assignment from an agent."""
    agent_id = event["pathParameters"]["agentId"]
    skill_id = event["pathParameters"]["skillId"]

    # Check junction record exists
    resp = agent_skills_table.get_item(
        Key={"agent_id": agent_id, "skill_id": skill_id}
    )
    if "Item" not in resp:
        raise NotFoundError("Assignment not found")

    agent_skills_table.delete_item(
        Key={"agent_id": agent_id, "skill_id": skill_id}
    )
    log_admin_change(event, "agent_skill_assignment", f"{agent_id}:{skill_id}", "delete", previous_data=resp["Item"], entity_name="")

    _save_agent_snapshot(agent_id, ["skills_unassigned"])

    return createResponse(200, "Skill unassigned")


def list_agent_skills(event: dict) -> dict:
    """List all skills assigned to an agent with full skill records."""
    agent_id = event["pathParameters"]["agentId"]

    # Query junction table by agent_id
    resp = agent_skills_table.query(
        KeyConditionExpression=Key("agent_id").eq(agent_id),
    )
    junction_items = resp.get("Items", [])

    if not junction_items:
        return createResponse(200, "Skills retrieved", {"skills": [], "count": 0})

    # Batch-get full skill records from Skills table
    skill_ids = [item["skill_id"] for item in junction_items]
    skills = []
    for skill_id in skill_ids:
        skill_resp = skills_table.get_item(Key={"skill_id": skill_id})
        item = skill_resp.get("Item")
        if item:
            skills.append(item)

    return createResponse(200, "Skills retrieved", {"skills": skills, "count": len(skills)})


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    """Main Lambda entry point — routes based on httpMethod and resource."""
    try:
        http_method = event.get("httpMethod", "")
        resource = event.get("resource", "")

        if resource == "/agents/{agentId}/skills/{skillId}" and http_method == "POST":
            return assign_skill(event)
        elif resource == "/agents/{agentId}/skills/{skillId}" and http_method == "DELETE":
            return unassign_skill(event)
        elif resource == "/agents/{agentId}/skills" and http_method == "GET":
            return list_agent_skills(event)
        else:
            raise BadRequestError(f"Unsupported route: {http_method} {resource}")
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
