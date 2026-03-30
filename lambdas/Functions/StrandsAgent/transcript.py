"""Transcript processing: speaker classification, batch write, question matching."""

import json
import uuid
from datetime import datetime, timezone

from aws_lambda_powertools import Logger
from strands import Agent
from strands.models.bedrock import BedrockModel

from constants import BEDROCK_REGION, MATCH_THRESHOLD, SESSIONS_TABLE_NAME, TRANSCRIPTS_TABLE_NAME
from helpers import _get_conn_data, _get_dynamodb, _post_to_connection, _broadcast_to_session
from question_detection import _detect_question, _generate_suggested_response
from speaker_classification import classify_line_role, init_role_classifier
from tools import _generate_embedding
from windows import (
    _check_answer_windows,
    _check_user_response_windows,
    _cosine_similarity,
    _get_unmatched_questions,
    _mark_question_matched,
    _open_answer_window,
    _open_user_response_window,
)

logger = Logger(child=True)


# ---------------------------------------------------------------------------
# Speaker classification
# ---------------------------------------------------------------------------


def _classify_speakers(lines: list, conn_data: dict) -> tuple[dict, str]:
    """Classify each transcript line's speaker role from text content.

    When single-channel audio produces a single speaker label for all lines,
    we use Nova Pro to infer per-line roles (user vs client) from context.

    Returns (role_map, confidence) where role_map maps speaker labels to roles.
    For single-speaker transcripts, returns an empty map — per-line classification
    is handled by _classify_line_role instead.
    """
    speakers = list(
        {line.get("speaker", "") for line in lines if line.get("speaker")}
    )
    if not speakers:
        return {}, "high"
    if len(speakers) == 1:
        # Single speaker label (single-channel audio) — can't map labels to roles.
        # Per-line classification will be done by _classify_line_role.
        return {}, "low"

    transcript_sample = "\n".join(
        f"{l['speaker']}: {l['text']}" for l in lines[:10]
    )

    try:
        model = BedrockModel(
            model_id="amazon.nova-pro-v1:0",
            region_name=BEDROCK_REGION,
        )
        agent = Agent(
            model=model,
            system_prompt=(
                "You are a speaker role classifier. Given a transcript excerpt "
                "from a business meeting, determine which speaker is the 'user' "
                "(the meeting host / sales rep / presenter) and which is the "
                "'client' (the external participant / customer / prospect). "
                "Respond ONLY with valid JSON: "
                '{"role_map": {"Speaker A": "user", "Speaker B": "client"}, '
                '"confidence": "high"}'
            ),
            tools=[],
        )
        result = agent(f"Classify speakers:\n{transcript_sample}")
        parsed = json.loads(str(result))
        return parsed.get("role_map", {}), parsed.get("confidence", "low")
    except Exception:
        logger.exception("Speaker classification failed, using fallback")
        role_map = {}
        for i, s in enumerate(speakers):
            role_map[s] = "user" if i == 0 else "client"
        return role_map, "low"


def _batch_write_transcripts(entries: list) -> None:
    """Batch write transcript entries to TranscriptsTable."""
    if not entries or not TRANSCRIPTS_TABLE_NAME:
        return
    try:
        table = _get_dynamodb().Table(TRANSCRIPTS_TABLE_NAME)
        with table.batch_writer() as batch:
            for entry in entries:
                batch.put_item(Item=entry)
    except Exception:
        logger.exception("Failed to batch write transcripts")


def _update_session_transcript_ts(session_id: str) -> None:
    """Update last_transcript_update_at on SessionsTable."""
    if not session_id or not SESSIONS_TABLE_NAME:
        return
    try:
        table = _get_dynamodb().Table(SESSIONS_TABLE_NAME)
        table.update_item(
            Key={"session_id": session_id},
            UpdateExpression="SET last_transcript_update_at = :ts",
            ExpressionAttributeValues={
                ":ts": datetime.now(timezone.utc).isoformat(),
            },
        )
    except Exception:
        logger.exception(
            "Failed to update transcript timestamp for %s", session_id
        )


# ---------------------------------------------------------------------------
# Main processTranscript handler
# ---------------------------------------------------------------------------


def _handle_process_transcript(body: dict, connection_id: str) -> dict:
    """Handle processTranscript action — store, match, buffer with speaker classification."""
    lines = body.get("lines", [])
    if not lines:
        _post_to_connection(connection_id, {
            "type": "error",
            "message": "Missing or empty 'lines' field",
        })
        return {"statusCode": 400, "body": "Missing lines"}

    session_id = body.get("session_id", "default-session")
    conn_data = _get_conn_data(connection_id)
    project_id = conn_data["project_id"]

    # --- Speaker classification (cached per connection) ---
    role_map = conn_data.get("speaker_role_map")
    single_speaker_mode = False
    if role_map is None:
        speakers = list({l.get("speaker", "") for l in lines if l.get("speaker")})
        if len(speakers) >= 2:
            role_map, confidence = _classify_speakers(lines, conn_data)
            conn_data["speaker_role_map"] = role_map
            conn_data["single_speaker_mode"] = False
            logger.info("Speaker roles classified: %s (confidence: %s)", role_map, confidence)
            _post_to_connection(connection_id, {
                "type": "speakerRoles",
                "role_map": role_map,
                "confidence": confidence,
            })
        else:
            # Single-channel audio — all lines have the same speaker label.
            # Initialize Cohere Embed classifier for per-line role detection.
            role_map = {}
            conn_data["speaker_role_map"] = role_map
            conn_data["single_speaker_mode"] = True
            init_role_classifier(conn_data)
            logger.info("Single speaker detected — using Cohere Embed role classification")
    single_speaker_mode = conn_data.get("single_speaker_mode", False)

    # --- Build entries ---
    entries = []
    buffer = conn_data.get("transcript_buffer", [])
    for line in lines:
        speaker = line.get("speaker", "Unknown")
        if single_speaker_mode:
            # Classify each line using Cohere Embed cosine similarity
            speaker_role = classify_line_role(line.get("text", ""), conn_data)
        else:
            speaker_role = role_map.get(speaker, "unknown")
        timestamp = line.get("timestamp", "")
        if not timestamp:
            timestamp = datetime.now(timezone.utc).isoformat()
        entries.append({
            "transcript_id": str(uuid.uuid4()),
            "session_id": session_id,
            "speaker": speaker,
            "speaker_role": speaker_role,
            "text": line.get("text", ""),
            "timestamp": timestamp,
            "start_time": line.get("start_time", ""),
            "end_time": line.get("end_time", ""),
            "confidence": line.get("confidence", ""),
            "is_partial": line.get("is_partial", False),
        })

    # --- Batch write to TranscriptsTable ---
    _batch_write_transcripts(entries)

    # --- Update session timestamp ---
    _update_session_transcript_ts(session_id)

    # --- Question matching, answer windows & question detection per line ---
    for entry in entries:
        # Skip partial lines entirely
        if entry.get("is_partial", False):
            continue

        # Run question detection first (to get is_new_question flag)
        is_question_detected = False
        detection_method = ""
        try:
            is_question_detected, detection_method = _detect_question(entry["text"])
        except Exception:
            logger.exception("Question detection failed for line")

        # Run question matching (to get is_question_matched flag)
        is_question_matched = False
        matched_question = None
        try:
            user_embedding = _generate_embedding(entry["text"])
            unmatched = _get_unmatched_questions(session_id)
            for q in unmatched:
                q_embedding = q.get("embedding", [])
                if not q_embedding:
                    continue
                # DynamoDB stores numbers as Decimal — convert to float
                q_embedding = [float(v) for v in q_embedding]
                sim = _cosine_similarity(user_embedding, q_embedding)
                if sim >= MATCH_THRESHOLD:
                    is_question_matched = True
                    matched_question = (q, sim)
                    break  # One match per line
        except Exception:
            logger.exception("Question matching failed for line")

        # Determine is_new_question for window close decisions
        is_new_question = is_question_detected or is_question_matched

        # Check active answer windows (append line, check close conditions)
        _check_answer_windows(
            conn_data, entry, connection_id, session_id, project_id,
            is_new_question=is_new_question,
        )

        # Check user response windows (append line, check close conditions)
        _check_user_response_windows(
            conn_data, entry, connection_id, session_id, project_id,
            is_new_question=is_new_question,
        )

        # If question detected → send questionDetected, generate suggested response only for client questions
        if is_question_detected:
            try:
                speaker_role = entry.get("speaker_role", "unknown")
                q_detected_msg = {
                    "type": "questionDetected",
                    "question": entry["text"],
                    "speaker": entry.get("speaker", ""),
                    "speaker_role": speaker_role,
                    "detection_method": detection_method,
                }
                _post_to_connection(connection_id, q_detected_msg)
                _broadcast_to_session(session_id, q_detected_msg, exclude_connection_id=connection_id)
                # Only generate suggested response for client questions (or unknown as safe default)
                if speaker_role in ("client", "unknown"):
                    _generate_suggested_response(
                        entry["text"], connection_id, conn_data, session_id
                    )
                _open_user_response_window(
                    conn_data, entry["text"], entry
                )
            except Exception:
                logger.exception("Question detection handling failed for line")

        # If question matched → send questionMatched, open answer window
        if is_question_matched and matched_question:
            try:
                q, sim = matched_question
                _mark_question_matched(q["question_id"])
                q_matched_msg = {
                    "type": "questionMatched",
                    "question_text": q["question_text"],
                    "spoken_text": entry["text"],
                    "similarity": round(sim, 4),
                }
                _post_to_connection(connection_id, q_matched_msg)
                _broadcast_to_session(session_id, q_matched_msg, exclude_connection_id=connection_id)
                _open_answer_window(conn_data, q, entry)
            except Exception:
                logger.exception("Question matching handling failed for line")

    # --- Update transcript buffer (rolling 50) ---
    buffer = conn_data.get("transcript_buffer", [])
    buffer.extend(entries)
    conn_data["transcript_buffer"] = buffer[-50:]

    _post_to_connection(connection_id, {
        "type": "transcriptProcessed",
        "lines_processed": len(entries),
    })

    return {"statusCode": 200, "body": "OK"}
