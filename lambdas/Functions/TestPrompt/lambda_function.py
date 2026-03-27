"""Test Prompt Lambda Function.

POST /agents/test-prompt — accepts ad-hoc prompts and a message, runs them
through Bedrock Nova Pro, and returns the response. Nothing is persisted.
"""

import json
import os

import boto3
from aws_lambda_powertools import Logger, Tracer

from custom_exceptions import BadRequestError
from response_utils import createResponse

logger = Logger()
tracer = Tracer()

PERSONALITIES_TABLE_NAME = os.environ.get("PERSONALITIES_TABLE_NAME", "")
SKILLS_TABLE_NAME = os.environ.get("SKILLS_TABLE_NAME", "")
BEDROCK_REGION = os.environ.get("BEDROCK_REGION", "us-east-1")
MODEL_ID = "amazon.nova-pro-v1:0"

dynamodb = boto3.resource("dynamodb")
personalities_table = dynamodb.Table(PERSONALITIES_TABLE_NAME)
skills_table = dynamodb.Table(SKILLS_TABLE_NAME) if SKILLS_TABLE_NAME else None

_bedrock_client = None


def _get_bedrock_client():
    global _bedrock_client
    if _bedrock_client is None:
        _bedrock_client = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)
    return _bedrock_client


def _parse_body(event: dict) -> dict:
    body = event.get("body", "{}")
    if body is None:
        body = "{}"
    try:
        return json.loads(body) if isinstance(body, str) else body
    except (json.JSONDecodeError, TypeError):
        return {}


def _load_personality_prompt(personality_id: str) -> str:
    if not personality_id or not PERSONALITIES_TABLE_NAME:
        raise BadRequestError("personality_id is required")
    resp = personalities_table.get_item(Key={"personality_id": personality_id})
    item = resp.get("Item")
    if not item:
        raise BadRequestError(f"Personality {personality_id} not found")
    return item.get("personality_prompt", "")


def _load_skills(skill_ids: list) -> list:
    """Look up skill records by ID from SkillsTable."""
    if not skill_ids or not skills_table:
        return []
    skills = []
    for sid in skill_ids:
        try:
            resp = skills_table.get_item(Key={"skill_id": sid})
            item = resp.get("Item")
            if item:
                skills.append(item)
        except Exception:
            logger.warning("Failed to load skill %s", sid)
    return skills


def _build_skill_section(skills: list) -> str:
    """Build the skill documents section for the system prompt."""
    if not skills:
        return ""
    section = "\n\n## Available Skill Documents\n"
    section += (
        "You have access to agent-specific skill documents. "
        "When answering questions, search these skill documents FIRST "
        "using the search_agent_skills tool before falling back to the "
        "general knowledge base.\n\n"
    )
    for s in skills:
        name = s.get("skill_name", "Unknown")
        desc = s.get("description", "")
        section += f"- {name}"
        if desc:
            section += f": {desc}"
        section += "\n"
    return section


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        data = _parse_body(event)

        role_prompt = (data.get("role_prompt") or "").strip()
        behavior_guidelines = (data.get("behavior_guidelines") or "").strip()
        personality_id = (data.get("personality_id") or "").strip()
        message = (data.get("message") or "").strip()
        conversation_history = data.get("conversation_history") or []
        skill_ids = data.get("skill_ids") or []

        if not role_prompt:
            raise BadRequestError("Missing required field: role_prompt")
        if not behavior_guidelines:
            raise BadRequestError("Missing required field: behavior_guidelines")
        if not personality_id:
            raise BadRequestError("Missing required field: personality_id")
        if not message:
            raise BadRequestError("Missing required field: message")

        personality_prompt = _load_personality_prompt(personality_id)

        system_prompt = (
            f"## Role\n{role_prompt}\n\n"
            f"## Behavior Guidelines\n{behavior_guidelines}\n\n"
            f"## Communication Style\n{personality_prompt}"
        )

        # Append skill context if skill_ids provided
        if skill_ids:
            skills = _load_skills(skill_ids)
            system_prompt += _build_skill_section(skills)

        messages = []
        for turn in conversation_history:
            role = turn.get("role", "user")
            content = turn.get("content", "")
            if role in ("user", "assistant") and content:
                messages.append({"role": role, "content": [{"text": content}]})

        messages.append({"role": "user", "content": [{"text": message}]})

        bedrock = _get_bedrock_client()
        response = bedrock.converse(
            modelId=MODEL_ID,
            system=[{"text": system_prompt}],
            messages=messages,
        )

        output = response.get("output", {})
        response_message = output.get("message", {})
        content_blocks = response_message.get("content", [])
        response_text = ""
        for block in content_blocks:
            if "text" in block:
                response_text += block["text"]

        return createResponse(200, "Test prompt executed", {
            "response": response_text,
            "model_id": MODEL_ID,
        })

    except BadRequestError as e:
        logger.warning("Bad request", extra={"error": str(e)})
        return createResponse(400, str(e))
    except Exception:
        logger.exception("Test prompt failed")
        return createResponse(500, "Internal server error")
