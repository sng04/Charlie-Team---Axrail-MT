"""Client question detection and suggested response generation."""

from aws_lambda_powertools import Logger
from strands import Agent
from strands.models.bedrock import BedrockModel

from constants import BEDROCK_REGION, TASK_PROMPTS
from helpers import _post_to_connection, _broadcast_to_session
from token_tracking import track_token_usage, _extract_token_usage
from tools import search_knowledge_base, search_agent_skills, get_session_transcript

logger = Logger(child=True)


# ---------------------------------------------------------------------------
# Heuristic patterns
# ---------------------------------------------------------------------------

# Interrogative words that START a question
_QUESTION_STARTERS = {
    "what is", "what are", "what does", "what do", "what would", "what about",
    "how do", "how does", "how is", "how are", "how long", "how much", "how many",
    "how would", "how can", "how about",
    "why is", "why are", "why do", "why does", "why would",
    "when is", "when do", "when does", "when will", "when can",
    "where is", "where are", "where do", "where does",
    "who is", "who are", "who does", "who will",
    "which is", "which are",
    "can you", "could you", "would you", "will you",
    "is there", "are there", "is it", "is that",
    "do you", "does it", "does that", "does the",
    "have you", "has it",
    "any update", "any news",
}

# Phrases that look like questions but are actually statements/offers
_FALSE_POSITIVE_PATTERNS = [
    "let me", "i'll", "i will", "we'll", "we will",
    "how about this", "how about i", "how about we",
    "what we", "what i", "what our",
    "that's what", "here's what", "here is what",
    "tell you what", "you know what",
    "thanks for", "thank you", "appreciate",
    "sounds good", "sounds great", "that works",
    "no i think", "no that", "yes that", "yes i",
    "absolutely", "exactly", "perfect",
]


# ---------------------------------------------------------------------------
# Question classification
# ---------------------------------------------------------------------------


def _is_question_heuristic(text: str):
    """Check if text is a question using improved heuristics.

    Returns True if definitely a question, False if definitely not, None if inconclusive.
    """
    text_lower = text.lower().strip()

    # Check false positive patterns first
    for pattern in _FALSE_POSITIVE_PATTERNS:
        if text_lower.startswith(pattern):
            return False

    # Ends with question mark — strong signal
    if text_lower.endswith("?"):
        return True

    # Check two-word question starters for better precision
    for starter in _QUESTION_STARTERS:
        if text_lower.startswith(starter):
            return True

    return None


def _is_question_model(text: str) -> bool:
    """Use Bedrock Converse API directly for fast yes/no classification.

    Bypasses the Strands Agent overhead — direct model call is ~2x faster.
    """
    try:
        import boto3
        import json
        client = boto3.client("bedrock-runtime", region_name=BEDROCK_REGION)
        response = client.converse(
            modelId="amazon.nova-lite-v1:0",
            messages=[{
                "role": "user",
                "content": [{"text": (
                    f'Is the following line from a meeting transcript a genuine question '
                    f'being asked to another person? Rhetorical questions, statements that '
                    f'start with question words (like "What we found is..."), and offers '
                    f'(like "How about I send you...") are NOT questions.\n\n'
                    f'Line: "{text}"\n\nAnswer ONLY "yes" or "no".'
                )}],
            }],
            inferenceConfig={"maxTokens": 3, "temperature": 0},
        )
        answer = response["output"]["message"]["content"][0]["text"].strip().lower()
        usage = response.get("usage", {})
        track_token_usage("", "questionClassify", "amazon.nova-lite-v1:0",
                          usage.get("inputTokens", 0), usage.get("outputTokens", 0))
        return answer.startswith("yes")
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
    if heuristic is False:
        return False, ""
    is_q = _is_question_model(text)
    return is_q, "model" if is_q else ""


# ---------------------------------------------------------------------------
# Suggested response generation
# ---------------------------------------------------------------------------


def _generate_suggested_response(
    question: str, connection_id: str, conn_data: dict, session_id: str = ""
) -> None:
    """Generate, broadcast, and cache a suggested response for a client question.

    The suggestion is cached in conn_data so the answer window can attach it
    to the QA pair when the actual spoken answer is captured.
    """
    project_id = conn_data["project_id"]
    skill_ids_str = ",".join(conn_data.get("skill_ids", []))
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
            tools=[search_knowledge_base, search_agent_skills, get_session_transcript],
        )
        enriched = (
            f"[Context: session_id={session_id}, project_id={project_id}]\n"
            f"IMPORTANT: Use project_id='{project_id}' when searching the knowledge base. "
            f"When searching agent skills, use skill_ids='{skill_ids_str}'. "
            f"Use session_id='{session_id}' to retrieve the transcript if needed.\n\n"
            f"Client question: {question}"
        )
        result = agent(enriched)
        inp, out = _extract_token_usage(result)
        track_token_usage(session_id, "suggestResponse", "amazon.nova-pro-v1:0", inp, out, project_id)
        suggested_answer = str(result)

        # Cache the suggestion so the answer window can attach it to the QA pair
        suggestions = conn_data.setdefault("_pending_suggestions", {})
        suggestions[question] = suggested_answer

        msg = {
            "type": "suggestedResponse",
            "question": question,
            "suggested_answer": suggested_answer,
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
