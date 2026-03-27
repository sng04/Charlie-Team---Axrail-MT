"""Answer windows, user response windows, and suggested question matching."""

import math
import uuid
from datetime import datetime, timezone
from decimal import Decimal

from aws_lambda_powertools import Logger

from constants import MATCH_THRESHOLD, SUGGESTED_QUESTIONS_TABLE_NAME
from helpers import _get_dynamodb, _post_to_connection
from tools import save_qa_pair, _generate_embedding

logger = Logger(child=True)


# ---------------------------------------------------------------------------
# Suggested questions storage & matching
# ---------------------------------------------------------------------------


def _store_suggested_questions(session_id: str, questions: list) -> None:
    """Store suggested questions with Titan Embed V2 embeddings."""
    if not SUGGESTED_QUESTIONS_TABLE_NAME or not questions:
        return
    table = _get_dynamodb().Table(SUGGESTED_QUESTIONS_TABLE_NAME)
    for q_text in questions:
        try:
            embedding = [Decimal(str(v)) for v in _generate_embedding(q_text)]
            table.put_item(Item={
                "question_id": str(uuid.uuid4()),
                "session_id": session_id,
                "question_text": q_text,
                "embedding": embedding,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "matched": False,
            })
        except Exception:
            logger.exception("Failed to store suggested question: %s", q_text)


def _cosine_similarity(vec_a: list, vec_b: list) -> float:
    """Compute cosine similarity between two vectors."""
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    norm_a = math.sqrt(sum(a * a for a in vec_a))
    norm_b = math.sqrt(sum(b * b for b in vec_b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def _get_unmatched_questions(session_id: str) -> list:
    """Query SuggestedQuestionsTable for unmatched questions in a session."""
    if not SUGGESTED_QUESTIONS_TABLE_NAME:
        return []
    try:
        from boto3.dynamodb.conditions import Key, Attr

        table = _get_dynamodb().Table(SUGGESTED_QUESTIONS_TABLE_NAME)
        resp = table.query(
            IndexName="session-index",
            KeyConditionExpression=Key("session_id").eq(session_id),
            FilterExpression=Attr("matched").eq(False),
        )
        return resp.get("Items", [])
    except Exception:
        logger.exception("Failed to get unmatched questions for %s", session_id)
        return []


def _mark_question_matched(question_id: str) -> None:
    """Mark a suggested question as matched."""
    if not SUGGESTED_QUESTIONS_TABLE_NAME:
        return
    try:
        table = _get_dynamodb().Table(SUGGESTED_QUESTIONS_TABLE_NAME)
        table.update_item(
            Key={"question_id": question_id},
            UpdateExpression="SET matched = :t",
            ExpressionAttributeValues={":t": True},
        )
    except Exception:
        logger.exception("Failed to mark question %s as matched", question_id)


# ---------------------------------------------------------------------------
# Answer windows (Stage 2 — user asks a suggested question, capture client answer)
# ---------------------------------------------------------------------------


def _open_answer_window(conn_data: dict, question: dict, trigger_line: dict) -> None:
    """Open an answer capture window for a matched question."""
    windows = conn_data.setdefault("answer_windows", {})
    windows[question["question_id"]] = {
        "question_text": question["question_text"],
        "spoken_text": trigger_line.get("text", ""),
        "collected_lines": [],
        "opened_at": trigger_line.get("timestamp", datetime.now(timezone.utc).isoformat()),
        "max_lines": 5,
        "timeout_seconds": 60,
    }


def _window_timed_out(window: dict, current_timestamp: str) -> bool:
    """Check if an answer window has timed out (60 seconds)."""
    try:
        opened = datetime.fromisoformat(window["opened_at"].rstrip("Z"))
        current = datetime.fromisoformat(current_timestamp.rstrip("Z"))
        return (current - opened).total_seconds() >= window["timeout_seconds"]
    except (ValueError, KeyError):
        return False


def _check_answer_windows(
    conn_data: dict,
    line: dict,
    connection_id: str,
    session_id: str,
    project_id: str,
    is_new_question: bool = False,
) -> None:
    """Process active answer windows — append all lines, check close conditions."""
    windows = conn_data.get("answer_windows", {})
    if not windows:
        return

    closed = []
    for qid, window in windows.items():
        window["collected_lines"].append(line.get("text", ""))

        should_close = (
            len(window["collected_lines"]) >= window["max_lines"]
            or (is_new_question and window["collected_lines"])
            or _window_timed_out(window, line.get("timestamp", ""))
        )

        if should_close:
            if window["collected_lines"]:
                answer = " ".join(window["collected_lines"])
                try:
                    save_qa_pair(
                        question=window["question_text"],
                        answer=answer,
                        session_id=session_id,
                        project_id=project_id,
                        source="participant",
                    )
                except Exception:
                    logger.exception("Failed to auto-save QA pair")
                _post_to_connection(connection_id, {
                    "type": "qaPairAutoSaved",
                    "question": window["question_text"],
                    "answer": answer,
                    "source": "participant",
                })
            else:
                _post_to_connection(connection_id, {
                    "type": "questionUnanswered",
                    "question": window["question_text"],
                })
            closed.append(qid)

    for qid in closed:
        del windows[qid]


# ---------------------------------------------------------------------------
# User response windows (Stage 3 — client asks question, capture user answer)
# ---------------------------------------------------------------------------


def _open_user_response_window(conn_data: dict, question_text: str, trigger_line: dict) -> str:
    """Open a user response capture window for a detected question."""
    windows = conn_data.setdefault("user_response_windows", {})
    window_id = str(uuid.uuid4())
    windows[window_id] = {
        "question_text": question_text,
        "collected_lines": [],
        "opened_at": trigger_line.get("timestamp", datetime.now(timezone.utc).isoformat()),
        "max_lines": 5,
        "timeout_seconds": 60,
    }
    return window_id


def _check_user_response_windows(
    conn_data: dict,
    line: dict,
    connection_id: str,
    session_id: str,
    project_id: str,
    is_new_question: bool = False,
) -> None:
    """Process active user response windows — append all lines, check close conditions."""
    windows = conn_data.get("user_response_windows", {})
    if not windows:
        return

    closed = []
    for wid, window in windows.items():
        window["collected_lines"].append(line.get("text", ""))

        should_close = (
            len(window["collected_lines"]) >= window["max_lines"]
            or (is_new_question and window["collected_lines"])
            or _window_timed_out(window, line.get("timestamp", ""))
        )

        if should_close:
            if window["collected_lines"]:
                answer = " ".join(window["collected_lines"])
                try:
                    save_qa_pair(
                        question=window["question_text"],
                        answer=answer,
                        session_id=session_id,
                        project_id=project_id,
                        source="client",
                    )
                except Exception:
                    logger.exception("Failed to auto-save client QA pair")
                _post_to_connection(connection_id, {
                    "type": "qaPairAutoSaved",
                    "question": window["question_text"],
                    "answer": answer,
                    "source": "client",
                })
            else:
                _post_to_connection(connection_id, {
                    "type": "questionUnanswered",
                    "question": window["question_text"],
                })
            closed.append(wid)

    for wid in closed:
        del windows[wid]
