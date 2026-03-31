"""Client question detection and suggested response generation."""

from aws_lambda_powertools import Logger
from strands import Agent
from strands.models.bedrock import BedrockModel

from constants import BEDROCK_REGION, TASK_PROMPTS, _QUESTION_INDICATORS
from helpers import _post_to_connection, _broadcast_to_session
from token_tracking import track_token_usage, _extract_token_usage
from tools import search_knowledge_base

logger = Logger(child=True)


# ---------------------------------------------------------------------------
# Question classification
# ---------------------------------------------------------------------------


def _is_question_heuristic(text: str):
    """Check if text is a question using heuristics.

    Returns True if definitely a question, None if inconclusive.
    """
    text_lower = text.lower().strip()
    if text_lower.endswith("?"):
        return True
    for indicator in _QUESTION_INDICATORS:
        if text_lower.startswith(indicator):
            return True
    return None


def _is_question_model(text: str) -> bool:
    """Use Nova Pro to classify if text is a question."""
    try:
        model = BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            region_name=BEDROCK_REGION,
        )
        agent = Agent(
            model=model,
            system_prompt=(
                "You are a question classifier. Given a line of meeting "
                "transcript, determine if the speaker is asking a question. "
                "Respond with ONLY 'yes' or 'no'."
            ),
            tools=[],
        )
        result = agent(f'Is this a question? "{text}"')
        inp, out = _extract_token_usage(result)
        track_token_usage("", "questionClassify", "amazon.nova-pro-v1:0", inp, out)
        return str(result).strip().lower().startswith("yes")
    except Exception:
        logger.exception("Question classification failed")
        return False


def _detect_question(text: str) -> tuple:
    """Detect if text is a question.

    Returns (is_question, detection_method).
    """
    words = text.split()
    if len(words) < 5:
        return False, ""
    heuristic = _is_question_heuristic(text)
    if heuristic is True:
        return True, "heuristic"
    is_q = _is_question_model(text)
    return is_q, "model" if is_q else ""


# ---------------------------------------------------------------------------
# Suggested response generation
# ---------------------------------------------------------------------------


def _generate_suggested_response(
    question: str, connection_id: str, conn_data: dict, session_id: str = ""
) -> None:
    """Generate and send a suggested response for a client question."""
    project_id = conn_data["project_id"]
    try:
        model = BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            region_name=BEDROCK_REGION,
        )
        system_prompt = (
            f"{TASK_PROMPTS['suggestResponse']}\n\n{conn_data['system_prompt']}"
        )
        agent = Agent(
            model=model,
            system_prompt=system_prompt,
            tools=[search_knowledge_base],
        )
        enriched = (
            f"[Context: project_id={project_id}]\n"
            f"IMPORTANT: Use project_id='{project_id}' when searching.\n\n"
            f"Client question: {question}"
        )
        result = agent(enriched)
        inp, out = _extract_token_usage(result)
        track_token_usage(session_id, "suggestResponse", "amazon.nova-pro-v1:0", inp, out, project_id)
        msg = {
            "type": "suggestedResponse",
            "question": question,
            "suggested_answer": str(result),
        }
        _post_to_connection(connection_id, msg)
        if session_id:
            _broadcast_to_session(session_id, msg, exclude_connection_id=connection_id)
    except Exception as exc:
        logger.exception("Suggested response generation failed")
        err_msg = {
            "type": "suggestedResponse",
            "question": question,
            "suggested_answer": f"Error generating suggestion: {exc}",
        }
        _post_to_connection(connection_id, err_msg)
        if session_id:
            _broadcast_to_session(session_id, err_msg, exclude_connection_id=connection_id)
