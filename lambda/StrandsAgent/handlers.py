"""Action handlers for WebSocket message routing."""

import json

from aws_lambda_powertools import Logger, Tracer
from strands import Agent
from strands.models.bedrock import BedrockModel

from constants import BEDROCK_REGION, TASK_PROMPTS
from helpers import (
    _connection_prompts,
    _get_conn_data,
    _is_session_completed,
    _load_agent_skills,
    _lookup_project_id,
    _mark_session_active,
    _mark_session_inactive,
    _post_to_connection,
    build_system_prompt,
)
from tools import (
    get_meeting_summary,
    get_session_qa_pairs,
    get_session_transcript,
    save_qa_pair,
    save_summary_to_s3,
    search_agent_skills,
    search_knowledge_base,
)
from windows import _store_suggested_questions

logger = Logger(child=True)
tracer = Tracer()


# ---------------------------------------------------------------------------
# WebSocket route handlers
# ---------------------------------------------------------------------------


def _handle_connect(event) -> dict:
    """Handle $connect: build and cache the system prompt + project scope."""
    connection_id = event["requestContext"]["connectionId"]
    qs = event.get("queryStringParameters") or {}
    agent_id = qs.get("agent_id")
    session_id = qs.get("session_id", "")

    project_id = _lookup_project_id(session_id)
    system_prompt, agent_name = build_system_prompt(agent_id)

    # Load active skills for this agent
    skills = []
    if agent_id:
        skills = _load_agent_skills(agent_id)

    # Enrich system prompt with skill information
    if skills:
        skill_section = "\n\n## Available Skill Documents\n"
        skill_section += (
            "You have access to agent-specific skill documents. "
            "When answering questions, search these skill documents FIRST "
            "using the search_agent_skills tool before falling back to the "
            "general knowledge base.\n\n"
        )
        for s in skills:
            name = s.get("skill_name", "Unknown")
            desc = s.get("description", "")
            skill_section += f"- {name}"
            if desc:
                skill_section += f": {desc}"
            skill_section += "\n"
        system_prompt += skill_section

    _connection_prompts[connection_id] = {
        "system_prompt": system_prompt,
        "agent_name": agent_name,
        "project_id": project_id,
        "session_id": session_id,
        "agent_id": agent_id or "",
        "skills": skills,
    }

    _mark_session_active(session_id, connection_id)

    logger.info(
        "Connected %s (agent_id=%s, session_id=%s, project_id=%s, agent_name=%s, skills=%d)",
        connection_id, agent_id, session_id, project_id, agent_name, len(skills),
    )
    return {"statusCode": 200, "body": "Connected"}


def _handle_disconnect(event) -> dict:
    """Handle $disconnect: mark session inactive and clean up cache."""
    connection_id = event["requestContext"]["connectionId"]
    conn_data = _connection_prompts.pop(connection_id, None)

    if conn_data:
        _mark_session_inactive(conn_data.get("session_id", ""))

    logger.info("Disconnected %s", connection_id)
    return {"statusCode": 200, "body": "Disconnected"}


# ---------------------------------------------------------------------------
# Action handlers
# ---------------------------------------------------------------------------


def _handle_send_message(body: dict, connection_id: str) -> dict:
    """Handle sendMessage action — existing chat behavior."""
    message = body.get("message", "").strip()
    if not message:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Missing 'message' field",
        })
        return {"statusCode": 400, "body": "Missing message"}

    session_id = body.get("session_id", "default-session")
    conn_data = _get_conn_data(connection_id)
    project_id = conn_data["project_id"]
    agent_id = conn_data.get("agent_id", "")

    try:
        model = BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            region_name=BEDROCK_REGION,
        )
        agent = Agent(
            model=model,
            system_prompt=conn_data["system_prompt"],
            tools=[search_knowledge_base, get_session_transcript, search_agent_skills],
        )
        enriched_message = (
            f"[Context: session_id={session_id}, project_id={project_id}, "
            f"agent_id={agent_id}]\n"
            f"IMPORTANT: When searching the knowledge base, always use "
            f"project_id='{project_id}' to ensure results are scoped to "
            f"this project only. When searching agent skills, use "
            f"agent_id='{agent_id}'.\n\n"
            f"{message}"
        )
        result = agent(enriched_message)

        _post_to_connection(connection_id, {
            "type": "response",
            "message": str(result),
            "agent_name": conn_data["agent_name"],
        })
    except Exception as exc:
        logger.exception("Agent invocation failed")
        _post_to_connection(connection_id, {
            "type": "error",
            "message": f"Failed to process request: {exc}",
        })

    return {"statusCode": 200, "body": "OK"}


def _handle_detect_question(body: dict, connection_id: str) -> dict:
    """Handle detectQuestion action — answer a question from the transcript."""
    question = body.get("question", "").strip()
    if not question:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Missing 'question' field",
        })
        return {"statusCode": 400, "body": "Missing question"}

    session_id = body.get("session_id", "default-session")
    conn_data = _get_conn_data(connection_id)
    project_id = conn_data["project_id"]
    agent_id = conn_data.get("agent_id", "")

    try:
        model = BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            region_name=BEDROCK_REGION,
        )
        system_prompt = (
            f"{TASK_PROMPTS['detectQuestion']}\n\n{conn_data['system_prompt']}"
        )
        agent = Agent(
            model=model,
            system_prompt=system_prompt,
            tools=[search_knowledge_base, get_session_transcript, search_agent_skills],
        )
        enriched = (
            f"[Context: session_id={session_id}, project_id={project_id}, "
            f"agent_id={agent_id}]\n"
            f"IMPORTANT: When searching the knowledge base, always use "
            f"project_id='{project_id}' to scope results. "
            f"When searching agent skills, use agent_id='{agent_id}'.\n\n"
            f"Question: {question}"
        )
        result = agent(enriched)

        _post_to_connection(connection_id, {
            "type": "questionResponse",
            "message": str(result),
            "agent_name": conn_data["agent_name"],
        })
    except Exception as exc:
        logger.exception("detectQuestion failed")
        _post_to_connection(connection_id, {
            "type": "error",
            "message": f"Failed to process request: {exc}",
        })

    return {"statusCode": 200, "body": "OK"}


def _handle_extract_qa_pair(body: dict, connection_id: str) -> dict:
    """Handle extractQAPair action — save a QA pair via the agent."""
    question = body.get("question", "").strip()
    answer = body.get("answer", "").strip()
    if not question or not answer:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Missing required fields: 'question' and 'answer'",
        })
        return {"statusCode": 400, "body": "Missing required fields"}

    session_id = body.get("session_id", "default-session")
    conn_data = _get_conn_data(connection_id)
    project_id = conn_data["project_id"]

    try:
        model = BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            region_name=BEDROCK_REGION,
        )
        system_prompt = (
            f"{TASK_PROMPTS['extractQAPair']}\n\n{conn_data['system_prompt']}"
        )
        agent = Agent(
            model=model,
            system_prompt=system_prompt,
            tools=[save_qa_pair],
        )
        enriched = (
            f"[Context: session_id={session_id}, project_id={project_id}]\n"
            f"Question: {question}\n"
            f"Answer: {answer}"
        )
        result = agent(enriched)

        _post_to_connection(connection_id, {
            "type": "qaPairSaved",
            "message": str(result),
            "agent_name": conn_data["agent_name"],
        })
    except Exception as exc:
        logger.exception("extractQAPair failed")
        _post_to_connection(connection_id, {
            "type": "error",
            "message": f"Failed to process request: {exc}",
        })

    return {"statusCode": 200, "body": "OK"}


def _handle_analyze_gaps(body: dict, connection_id: str) -> dict:
    """Handle analyzeGaps action — identify knowledge gaps in the session."""
    session_id = body.get("session_id", "").strip()
    if not session_id:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Missing 'session_id' field",
        })
        return {"statusCode": 400, "body": "Missing session_id"}

    conn_data = _get_conn_data(connection_id)
    project_id = conn_data["project_id"]
    agent_id = conn_data.get("agent_id", "")

    try:
        model = BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            region_name=BEDROCK_REGION,
        )
        system_prompt = (
            f"{TASK_PROMPTS['analyzeGaps']}\n\n{conn_data['system_prompt']}"
        )
        agent = Agent(
            model=model,
            system_prompt=system_prompt,
            tools=[search_knowledge_base, get_session_transcript, search_agent_skills],
        )
        enriched = (
            f"[Context: session_id={session_id}, project_id={project_id}, "
            f"agent_id={agent_id}]\n"
            f"IMPORTANT: When searching the knowledge base, always use "
            f"project_id='{project_id}' to scope results. "
            f"When searching agent skills, use agent_id='{agent_id}'.\n\n"
            f"Analyze knowledge gaps for session {session_id}."
        )
        result = agent(enriched)

        try:
            analysis = json.loads(str(result))
        except (ValueError, TypeError):
            analysis = {"gaps": [], "suggested_questions": [], "raw": str(result)}

        # Store suggested questions with embeddings for matching
        suggested = analysis.get("suggested_questions", [])
        if suggested:
            _store_suggested_questions(session_id, suggested)

        _post_to_connection(connection_id, {
            "type": "gapAnalysis",
            "session_id": session_id,
            **analysis,
        })
    except Exception as exc:
        logger.exception("Gap analysis failed")
        _post_to_connection(connection_id, {
            "type": "error",
            "message": f"Failed to process gap analysis: {exc}",
        })

    return {"statusCode": 200, "body": "OK"}


def _handle_end_meeting(body: dict, connection_id: str) -> dict:
    """Handle endMeeting action — generate summary, save to S3, mark inactive."""
    session_id = body.get("session_id", "").strip()
    if not session_id:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Missing 'session_id' field",
        })
        return {"statusCode": 400, "body": "Missing session_id"}

    conn_data = _get_conn_data(connection_id)
    project_id = conn_data["project_id"]
    agent_id = conn_data.get("agent_id", "")

    _post_to_connection(connection_id, {
        "type": "status",
        "message": "Generating meeting summary...",
    })

    try:
        model = BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            region_name=BEDROCK_REGION,
        )
        system_prompt = (
            f"{TASK_PROMPTS['endMeeting']}\n\n{conn_data['system_prompt']}"
        )
        agent = Agent(
            model=model,
            system_prompt=system_prompt,
            tools=[get_session_transcript, get_session_qa_pairs, save_summary_to_s3, search_agent_skills],
        )
        enriched = (
            f"[Context: session_id={session_id}, project_id={project_id}, "
            f"agent_id={agent_id}]\n"
            f"Generate a meeting summary for session {session_id}."
        )
        result = agent(enriched)
        summary_markdown = str(result)

        _post_to_connection(connection_id, {
            "type": "meetingSummary",
            "session_id": session_id,
            "summary_markdown": summary_markdown,
        })

        _mark_session_inactive(session_id)
    except Exception as exc:
        logger.exception("End meeting summary generation failed")
        _post_to_connection(connection_id, {
            "type": "error",
            "message": f"Failed to generate meeting summary: {exc}",
        })

    return {"statusCode": 200, "body": "OK"}


def _handle_retro_analysis(body: dict, connection_id: str) -> dict:
    """Handle retroAnalysis action — generate retro feedback for a completed meeting."""
    session_id = body.get("session_id", "").strip()
    if not session_id:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Missing 'session_id' field",
        })
        return {"statusCode": 400, "body": "Missing session_id"}

    is_completed = _is_session_completed(session_id)
    if is_completed is False:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Retro mode is only available for completed sessions",
        })
        return {"statusCode": 400, "body": "Session not completed"}

    conn_data = _get_conn_data(connection_id)
    project_id = conn_data["project_id"]
    agent_id = conn_data.get("agent_id", "")

    _post_to_connection(connection_id, {
        "type": "status",
        "message": "Generating retro analysis...",
    })

    try:
        model = BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            region_name=BEDROCK_REGION,
        )
        system_prompt = (
            f"{TASK_PROMPTS['retroAnalysis']}\n\n{conn_data['system_prompt']}"
        )
        agent = Agent(
            model=model,
            system_prompt=system_prompt,
            tools=[get_session_transcript, get_meeting_summary, get_session_qa_pairs, search_agent_skills],
        )
        enriched = (
            f"[Context: session_id={session_id}, project_id={project_id}, "
            f"agent_id={agent_id}]\n"
            f"Perform a retrospective analysis for session {session_id}."
        )
        result = agent(enriched)
        feedback_text = str(result)

        conn_data["retro_context"] = {
            "session_id": session_id,
            "feedback": feedback_text,
        }

        _post_to_connection(connection_id, {
            "type": "retroFeedback",
            "session_id": session_id,
            "feedback": feedback_text,
        })
    except Exception as exc:
        logger.exception("Retro analysis failed")
        _post_to_connection(connection_id, {
            "type": "error",
            "message": f"Failed to generate retro analysis: {exc}",
        })

    return {"statusCode": 200, "body": "OK"}


def _handle_retro_chat(body: dict, connection_id: str) -> dict:
    """Handle retroChat action — follow-up conversation about retro feedback."""
    message = body.get("message", "").strip()
    if not message:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Missing 'message' field",
        })
        return {"statusCode": 400, "body": "Missing message"}

    conn_data = _connection_prompts.get(connection_id)
    if conn_data is None or "retro_context" not in conn_data:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "No retro analysis found. Run retroAnalysis first.",
        })
        return {"statusCode": 400, "body": "No retro context"}

    retro_ctx = conn_data["retro_context"]

    try:
        model = BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            region_name=BEDROCK_REGION,
        )
        retro_system_prompt = (
            f"{conn_data['system_prompt']}\n\n"
            f"## Retro Analysis Context\n"
            f"Session: {retro_ctx['session_id']}\n\n"
            f"### Previous Retro Feedback\n{retro_ctx['feedback']}\n"
        )
        agent = Agent(
            model=model,
            system_prompt=retro_system_prompt,
            tools=[search_knowledge_base, get_session_transcript, search_agent_skills],
        )
        enriched = (
            f"{TASK_PROMPTS['retroChat']}\n\n{message}"
        )
        result = agent(enriched)

        _post_to_connection(connection_id, {
            "type": "retroResponse",
            "message": str(result),
        })
    except Exception as exc:
        logger.exception("Retro chat failed")
        _post_to_connection(connection_id, {
            "type": "error",
            "message": f"Failed to process retro chat: {exc}",
        })

    return {"statusCode": 200, "body": "OK"}


def _handle_set_suggested_questions(body: dict, connection_id: str) -> dict:
    """Handle setSuggestedQuestions action — store questions with embeddings."""
    questions = body.get("questions", [])
    if not questions:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Missing or empty 'questions' field",
        })
        return {"statusCode": 400, "body": "Missing questions"}

    session_id = body.get("session_id", "default-session")
    _store_suggested_questions(session_id, questions)

    _post_to_connection(connection_id, {
        "type": "suggestedQuestionsSet",
        "count": len(questions),
    })
    return {"statusCode": 200, "body": "OK"}
