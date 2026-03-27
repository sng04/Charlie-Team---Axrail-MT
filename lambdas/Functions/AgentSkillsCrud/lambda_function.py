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

from custom_exceptions import BadRequestError, NotFoundError
from response_utils import createResponse

logger = Logger()
tracer = Tracer()

AGENTS_TABLE_NAME = os.environ.get("AGENTS_TABLE_NAME", "")
SKILLS_TABLE_NAME = os.environ.get("SKILLS_TABLE_NAME", "")
AGENT_SKILLS_TABLE_NAME = os.environ.get("AGENT_SKILLS_TABLE_NAME", "")

dynamodb = boto3.resource("dynamodb")
agents_table = dynamodb.Table(AGENTS_TABLE_NAME)
skills_table = dynamodb.Table(SKILLS_TABLE_NAME)
agent_skills_table = dynamodb.Table(AGENT_SKILLS_TABLE_NAME)


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
