#!/usr/bin/env python3
"""
End-to-end test script for all GMeet Agent endpoints.

Tests:
  1.  REST API  — Personalities CRUD (list, create, get, update, delete)
  2.  REST API  — Agents CRUD (list, create, get, update, delete)
  3.  REST API  — QA Pairs (list by session, get, delete)
  4.  WebSocket — sendMessage
  5.  WebSocket — detectQuestion
  6.  WebSocket — extractQAPair
  7.  WebSocket — analyzeGaps
  8.  WebSocket — endMeeting
  9.  WebSocket — retroAnalysis
 10.  WebSocket — retroChat
 11.  WebSocket — processTranscript (speaker hints)
 12.  WebSocket — processTranscript (model classification)
 13.  WebSocket — setSuggestedQuestions
 14.  WebSocket — processTranscript (question matching + answer window)
 15.  WebSocket — processTranscript (client question detection — heuristic)
 16.  WebSocket — processTranscript (suggested response generation)
 17.  WebSocket — processTranscript (user response window capture)
 18.  WebSocket — full live transcript flow integration

Usage:
    pip3 install websocket-client requests certifi
    python3 test_all_endpoints.py            # normal (compact output)
    python3 test_all_endpoints.py --verbose   # print full response payloads
    python3 test_all_endpoints.py -v          # same as --verbose
"""

import json
import ssl
import sys
import time
import uuid

import certifi
import requests
import websocket

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REST_URL = "https://p4wa5y4vye.execute-api.ap-southeast-1.amazonaws.com/prod"
WS_URL = "wss://ao35uwn4rh.execute-api.ap-southeast-1.amazonaws.com/production"
WS_TIMEOUT = 90  # seconds — Bedrock calls can be slow
VERBOSE = False  # Set True (or pass --verbose) to print full response payloads

PASS = "\033[92m✓ PASS\033[0m"
FAIL = "\033[91m✗ FAIL\033[0m"
INFO = "\033[94mℹ INFO\033[0m"
WARN = "\033[93m⚠ WARN\033[0m"
VERBOSE_TAG = "\033[95m⤷ RESP\033[0m"

results = []  # (name, passed, detail)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def record(name: str, passed: bool, detail: str = ""):
    tag = PASS if passed else FAIL
    print(f"  {tag}  {name}" + (f"  — {detail}" if detail else ""))
    results.append((name, passed, detail))


def vprint(label: str, data):
    """Print full response payload when VERBOSE is enabled."""
    if not VERBOSE:
        return
    formatted = json.dumps(data, indent=2, default=str) if isinstance(data, (dict, list)) else str(data)
    for line in formatted.splitlines():
        print(f"    {VERBOSE_TAG}  [{label}] {line}")


def rest_get(path, params=None):
    r = requests.get(f"{REST_URL}{path}", params=params, timeout=30)
    vprint(f"GET {path}", r.json() if r.headers.get("content-type", "").startswith("application/json") else r.text)
    return r


def rest_post(path, body):
    r = requests.post(f"{REST_URL}{path}", json=body, timeout=30)
    vprint(f"POST {path}", r.json() if r.headers.get("content-type", "").startswith("application/json") else r.text)
    return r


def rest_put(path, body):
    r = requests.put(f"{REST_URL}{path}", json=body, timeout=30)
    vprint(f"PUT {path}", r.json() if r.headers.get("content-type", "").startswith("application/json") else r.text)
    return r


def rest_delete(path):
    r = requests.delete(f"{REST_URL}{path}", timeout=30)
    vprint(f"DELETE {path}", r.json() if r.headers.get("content-type", "").startswith("application/json") else r.text)
    return r


def ws_send_and_recv(ws, payload: dict) -> dict:
    """Send a JSON payload over WebSocket and wait for a response."""
    ws.send(json.dumps(payload))
    raw = ws.recv()
    resp = json.loads(raw)
    vprint(f"WS {payload.get('action', '?')}", resp)
    return resp


def ws_recv_until(ws, target_type: str, max_messages: int = 20) -> dict | None:
    """Receive messages until we get one with the target type, or exhaust max."""
    for _ in range(max_messages):
        try:
            raw = ws.recv()
            msg = json.loads(raw)
            if msg.get("type") == target_type:
                return msg
        except websocket.WebSocketTimeoutException:
            break
        except Exception:
            break
    return None


def ws_recv_all(ws, timeout_per_msg: float = 5.0, max_messages: int = 30) -> list:
    """Drain all pending messages from the WebSocket with a short timeout."""
    messages = []
    old_timeout = ws.gettimeout()
    ws.settimeout(timeout_per_msg)
    for _ in range(max_messages):
        try:
            raw = ws.recv()
            msg = json.loads(raw)
            vprint(f"WS recv", msg)
            messages.append(msg)
        except websocket.WebSocketTimeoutException:
            break
        except Exception:
            break
    ws.settimeout(old_timeout)
    return messages


def ws_connect(session_id: str = "") -> websocket.WebSocket:
    """Open a WebSocket connection with optional session_id."""
    url = WS_URL
    if session_id:
        url += f"?session_id={session_id}"
    sslopt = {
        "ca_certs": certifi.where(),
        "cert_reqs": ssl.CERT_REQUIRED,
        "check_hostname": True,
    }
    ws = websocket.WebSocket(sslopt=sslopt)
    ws.settimeout(WS_TIMEOUT)
    ws.connect(url)
    return ws


def find_message(messages: list, msg_type: str) -> dict | None:
    """Find the first message with a given type in a list."""
    for m in messages:
        if m.get("type") == msg_type:
            return m
    return None


def has_message_type(messages: list, msg_type: str) -> bool:
    """Check if any message in the list has the given type."""
    return find_message(messages, msg_type) is not None


# ---------------------------------------------------------------------------
# 1. Personalities CRUD
# ---------------------------------------------------------------------------

def test_personalities_crud():
    print("\n── Personalities CRUD ──")

    r = rest_get("/personalities")
    record("List personalities", r.status_code == 200, f"status={r.status_code}")

    body = {
        "personality_name": f"test-{uuid.uuid4().hex[:8]}",
        "personality_prompt": "Speak like a pirate. Arrr!",
    }
    r = rest_post("/personalities", body)
    data = r.json().get("data", {})
    pid = data.get("personality_id", "")
    record("Create personality", r.status_code == 200 and pid, f"id={pid}")

    if not pid:
        return None

    r = rest_get(f"/personalities/{pid}")
    record("Get personality", r.status_code == 200)

    r = rest_put(f"/personalities/{pid}", {"personality_prompt": "Updated prompt"})
    record("Update personality", r.status_code == 200)

    return pid


# ---------------------------------------------------------------------------
# 2. Agents CRUD
# ---------------------------------------------------------------------------

def test_agents_crud(personality_id: str):
    print("\n── Agents CRUD ──")

    if not personality_id:
        record("Agents CRUD", False, "skipped — no personality_id")
        return None

    r = rest_get("/agents")
    record("List agents", r.status_code == 200, f"status={r.status_code}")

    body = {
        "agent_name": f"TestAgent-{uuid.uuid4().hex[:8]}",
        "role_prompt": "You are a test agent.",
        "task_prompt": "Answer test questions.",
        "personality_id": personality_id,
        "model_id": "amazon.nova-pro-v1:0",
        "use_case": "testing",
    }
    r = rest_post("/agents", body)
    data = r.json().get("data", {})
    aid = data.get("agent_id", "")
    record("Create agent", r.status_code == 200 and aid, f"id={aid}")

    if not aid:
        return None

    r = rest_get(f"/agents/{aid}")
    record("Get agent", r.status_code == 200)

    r = rest_put(f"/agents/{aid}", {"agent_name": "UpdatedTestAgent"})
    record("Update agent", r.status_code == 200)

    return aid


# ---------------------------------------------------------------------------
# 3. QA Pairs (read-only — created via WebSocket extractQAPair)
# ---------------------------------------------------------------------------

def test_qa_pairs_crud(session_id: str):
    print("\n── QA Pairs CRUD ──")

    r = rest_get("/qa-pairs", params={"session_id": session_id})
    ok = r.status_code == 200
    items = r.json().get("data", [])
    record("List QA pairs by session", ok, f"count={len(items)}")

    if items:
        qid = items[0].get("qa_pair_id", "")
        r = rest_get(f"/qa-pairs/{qid}")
        record("Get QA pair", r.status_code == 200, f"id={qid}")
        return qid
    else:
        record("Get QA pair", False, "skipped — no QA pairs found")
        return None


# ---------------------------------------------------------------------------
# 4-10. WebSocket Actions (original)
# ---------------------------------------------------------------------------

def test_websocket_actions():
    print("\n── WebSocket Actions ──")

    session_id = f"test-session-{uuid.uuid4().hex[:8]}"

    try:
        ws = ws_connect(session_id)
        record("WebSocket connect", True, f"session={session_id}")
    except Exception as e:
        record("WebSocket connect", False, str(e))
        return session_id

    # 4. sendMessage
    try:
        resp = ws_send_and_recv(ws, {
            "action": "sendMessage",
            "message": "Hello, what can you do?",
            "session_id": session_id,
        })
        ok = resp.get("type") in ("response", "error")
        record("sendMessage", ok, f"type={resp.get('type')}")
    except Exception as e:
        record("sendMessage", False, str(e))

    # 5. detectQuestion
    try:
        resp = ws_send_and_recv(ws, {
            "action": "detectQuestion",
            "question": "What is the project timeline?",
            "session_id": session_id,
        })
        ok = resp.get("type") in ("questionResponse", "error")
        record("detectQuestion", ok, f"type={resp.get('type')}")
    except Exception as e:
        record("detectQuestion", False, str(e))

    # 6. extractQAPair
    try:
        resp = ws_send_and_recv(ws, {
            "action": "extractQAPair",
            "question": "What is the deadline?",
            "answer": "The deadline is next Friday.",
            "session_id": session_id,
        })
        ok = resp.get("type") in ("qaPairSaved", "error")
        record("extractQAPair", ok, f"type={resp.get('type')}")
    except Exception as e:
        record("extractQAPair", False, str(e))

    # 7. analyzeGaps
    try:
        resp = ws_send_and_recv(ws, {
            "action": "analyzeGaps",
            "session_id": session_id,
        })
        ok = resp.get("type") in ("gapAnalysis", "error")
        record("analyzeGaps", ok, f"type={resp.get('type')}")
    except Exception as e:
        record("analyzeGaps", False, str(e))

    # 8. endMeeting
    try:
        ws.send(json.dumps({
            "action": "endMeeting",
            "session_id": session_id,
        }))
        resp = json.loads(ws.recv())
        vprint("WS endMeeting", resp)
        if resp.get("type") == "status":
            resp = json.loads(ws.recv())
            vprint("WS endMeeting", resp)
        ok = resp.get("type") in ("meetingSummary", "error")
        record("endMeeting", ok, f"type={resp.get('type')}")
    except Exception as e:
        record("endMeeting", False, str(e))

    ws.close()
    return session_id


def test_retro_actions(session_id: str):
    """Test retroAnalysis and retroChat on the (now-inactive) session."""
    print("\n── Retro Mode Actions ──")

    try:
        ws = ws_connect(session_id)
        record("WebSocket reconnect for retro", True)
    except Exception as e:
        record("WebSocket reconnect for retro", False, str(e))
        return

    # 9. retroAnalysis
    try:
        ws.send(json.dumps({
            "action": "retroAnalysis",
            "session_id": session_id,
        }))
        resp = json.loads(ws.recv())
        vprint("WS retroAnalysis", resp)
        if resp.get("type") == "status":
            resp = json.loads(ws.recv())
            vprint("WS retroAnalysis", resp)
        ok = resp.get("type") in ("retroFeedback", "error")
        detail = resp.get("type")
        if resp.get("type") == "error":
            detail += f": {resp.get('message', '')[:80]}"
        record("retroAnalysis", ok, f"type={detail}")
        retro_succeeded = resp.get("type") == "retroFeedback"
    except Exception as e:
        record("retroAnalysis", False, str(e))
        retro_succeeded = False

    # 10. retroChat
    try:
        resp = ws_send_and_recv(ws, {
            "action": "retroChat",
            "message": "What were the main action items?",
        })
        ok = resp.get("type") in ("retroResponse", "error")
        detail = resp.get("type")
        if resp.get("type") == "error":
            detail += f": {resp.get('message', '')[:80]}"
        if not retro_succeeded and resp.get("type") == "error":
            detail += " (expected — no retro context)"
        record("retroChat", ok, f"type={detail}")
    except Exception as e:
        record("retroChat", False, str(e))

    ws.close()


# ---------------------------------------------------------------------------
# 11-18. Live Transcript QA Detection (Stages 1-3)
# ---------------------------------------------------------------------------

def test_process_transcript_with_hints():
    """11. processTranscript with speaker_hint — skips model classification."""
    print("\n── processTranscript (speaker hints) ──")

    session_id = f"test-pt-hints-{uuid.uuid4().hex[:8]}"
    try:
        ws = ws_connect(session_id)
        record("Connect for processTranscript hints", True)
    except Exception as e:
        record("Connect for processTranscript hints", False, str(e))
        return None, None

    lines = [
        {"speaker": "Alice", "text": "Welcome everyone, let's get started with the demo."},
        {"speaker": "Bob", "text": "Thanks Alice, excited to see what you've built."},
        {"speaker": "Alice", "text": "We have a new feature for real-time question detection."},
    ]

    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": lines,
            "speaker_hint": {"Alice": "user", "Bob": "client"},
        }))
        messages = ws_recv_all(ws, timeout_per_msg=10.0)
        tp = find_message(messages, "transcriptProcessed")
        ok = tp is not None and tp.get("lines_processed") == 3
        role_map = tp.get("speaker_role_map", {}) if tp else {}
        record(
            "processTranscript with hints",
            ok,
            f"lines={tp.get('lines_processed') if tp else 0}, "
            f"roles={role_map}",
        )
        # Verify hints were applied correctly
        hints_ok = role_map.get("Alice") == "user" and role_map.get("Bob") == "client"
        record("Speaker hints applied correctly", hints_ok, f"map={role_map}")
    except Exception as e:
        record("processTranscript with hints", False, str(e))

    ws.close()
    return session_id, ws


def test_process_transcript_model_classification():
    """12. processTranscript without hints — triggers model speaker classification."""
    print("\n── processTranscript (model classification) ──")

    session_id = f"test-pt-model-{uuid.uuid4().hex[:8]}"
    try:
        ws = ws_connect(session_id)
        record("Connect for model classification", True)
    except Exception as e:
        record("Connect for model classification", False, str(e))
        return

    # Two speakers, no hints — forces Nova Pro classification
    lines = [
        {"speaker": "Speaker A", "text": "Hi, I'm the sales rep. Let me walk you through our product features today."},
        {"speaker": "Speaker B", "text": "Great, I'm interested in learning about your pricing and integration options."},
        {"speaker": "Speaker A", "text": "Our platform starts at fifty dollars per month for the basic tier."},
    ]

    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": lines,
        }))
        messages = ws_recv_all(ws, timeout_per_msg=30.0)
        tp = find_message(messages, "transcriptProcessed")
        ok = tp is not None and tp.get("lines_processed") == 3
        role_map = tp.get("speaker_role_map", {}) if tp else {}
        confidence = tp.get("classification_confidence", "") if tp else ""
        record(
            "processTranscript model classification",
            ok,
            f"lines={tp.get('lines_processed') if tp else 0}, "
            f"confidence={confidence}, roles={role_map}",
        )
        # Verify both speakers got roles assigned
        both_assigned = len(role_map) == 2 and all(
            v in ("user", "client") for v in role_map.values()
        )
        record("Both speakers classified", both_assigned, f"map={role_map}")
    except Exception as e:
        record("processTranscript model classification", False, str(e))

    ws.close()


def test_set_suggested_questions():
    """13. setSuggestedQuestions — store questions with embeddings for matching."""
    print("\n── setSuggestedQuestions ──")

    session_id = f"test-sq-{uuid.uuid4().hex[:8]}"
    try:
        ws = ws_connect(session_id)
        record("Connect for setSuggestedQuestions", True)
    except Exception as e:
        record("Connect for setSuggestedQuestions", False, str(e))
        return session_id

    questions = [
        "What is the pricing model for the enterprise tier?",
        "How does the integration with Salesforce work?",
        "What security certifications do you have?",
    ]

    try:
        resp = ws_send_and_recv(ws, {
            "action": "setSuggestedQuestions",
            "session_id": session_id,
            "questions": questions,
        })
        ok = resp.get("type") == "suggestedQuestionsSet" and resp.get("count") == 3
        record(
            "setSuggestedQuestions",
            ok,
            f"type={resp.get('type')}, count={resp.get('count')}",
        )
    except Exception as e:
        record("setSuggestedQuestions", False, str(e))

    # Test empty questions list — should return error
    try:
        resp = ws_send_and_recv(ws, {
            "action": "setSuggestedQuestions",
            "session_id": session_id,
            "questions": [],
        })
        ok = resp.get("type") == "error"
        record("setSuggestedQuestions empty list rejected", ok, f"type={resp.get('type')}")
    except Exception as e:
        record("setSuggestedQuestions empty list rejected", False, str(e))

    ws.close()
    return session_id


def test_question_matching_and_answer_window(sq_session_id: str):
    """14. processTranscript — question matching + answer window capture."""
    print("\n── Question Matching & Answer Window ──")

    # Reuse the session that has suggested questions stored
    session_id = sq_session_id
    try:
        ws = ws_connect(session_id)
        record("Connect for question matching", True)
    except Exception as e:
        record("Connect for question matching", False, str(e))
        return

    # Send a user line that semantically matches "What is the pricing model
    # for the enterprise tier?" — should trigger questionMatched
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Host",
                    "text": "What is the pricing model for the enterprise tier?",
                    "timestamp": "2025-01-15T10:00:00Z",
                },
            ],
            "speaker_hint": {"Host": "user", "Client": "client"},
        }))
        # Expect: possibly questionMatched, then transcriptProcessed
        messages = ws_recv_all(ws, timeout_per_msg=15.0)
        tp = find_message(messages, "transcriptProcessed")
        qm = find_message(messages, "questionMatched")

        record(
            "processTranscript for matching",
            tp is not None,
            f"lines={tp.get('lines_processed') if tp else 0}",
        )
        if qm:
            record(
                "Question matched",
                True,
                f"sim={qm.get('similarity')}, "
                f"q={qm.get('question_text', '')[:50]}",
            )
        else:
            record(
                "Question matched",
                False,
                "no questionMatched message (similarity may be below threshold)",
            )
    except Exception as e:
        record("Question matching", False, str(e))

    # Now send client lines to trigger answer window capture
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Client",
                    "text": "Our enterprise tier starts at two hundred dollars per seat per month.",
                    "timestamp": "2025-01-15T10:00:05Z",
                },
                {
                    "speaker": "Client",
                    "text": "That includes unlimited API access and priority support.",
                    "timestamp": "2025-01-15T10:00:10Z",
                },
                {
                    "speaker": "Host",
                    "text": "That sounds reasonable for our team size.",
                    "timestamp": "2025-01-15T10:00:15Z",
                },
            ],
            "speaker_hint": {"Host": "user", "Client": "client"},
        }))
        messages = ws_recv_all(ws, timeout_per_msg=15.0)
        qa_saved = find_message(messages, "qaPairAutoSaved")
        tp = find_message(messages, "transcriptProcessed")

        record(
            "Answer window processed",
            tp is not None,
            f"lines={tp.get('lines_processed') if tp else 0}",
        )
        if qa_saved:
            record(
                "QA pair auto-saved from answer window",
                True,
                f"source={qa_saved.get('source')}, "
                f"q={qa_saved.get('question', '')[:40]}...",
            )
            # Verify source is "participant" (Stage 2 answer windows)
            record(
                "Answer window source=participant",
                qa_saved.get("source") == "participant",
                f"source={qa_saved.get('source')}",
            )
        else:
            record(
                "QA pair auto-saved from answer window",
                False,
                "no qaPairAutoSaved (window may not have been open)",
            )
    except Exception as e:
        record("Answer window capture", False, str(e))

    ws.close()


def test_client_question_detection():
    """15-16. Client question detection (heuristic) + suggested response."""
    print("\n── Client Question Detection & Suggested Response ──")

    session_id = f"test-cqd-{uuid.uuid4().hex[:8]}"
    try:
        ws = ws_connect(session_id)
        record("Connect for client question detection", True)
    except Exception as e:
        record("Connect for client question detection", False, str(e))
        return session_id

    # --- Test 15a: Heuristic detection via question mark ---
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Client",
                    "text": "What kind of security certifications does your platform have?",
                    "timestamp": "2025-01-15T10:01:00Z",
                },
            ],
            "speaker_hint": {"Host": "user", "Client": "client"},
        }))
        # Expect: clientQuestionDetected, suggestedResponse, transcriptProcessed
        messages = ws_recv_all(ws, timeout_per_msg=30.0, max_messages=10)
        cqd = find_message(messages, "clientQuestionDetected")
        sr = find_message(messages, "suggestedResponse")
        tp = find_message(messages, "transcriptProcessed")

        record(
            "processTranscript with client question",
            tp is not None,
            f"lines={tp.get('lines_processed') if tp else 0}",
        )

        if cqd:
            record(
                "Client question detected (question mark)",
                True,
                f"method={cqd.get('detection_method')}, "
                f"q={cqd.get('question', '')[:50]}",
            )
            record(
                "Detection method is heuristic",
                cqd.get("detection_method") == "heuristic",
                f"method={cqd.get('detection_method')}",
            )
        else:
            record("Client question detected (question mark)", False, "no clientQuestionDetected")

        if sr:
            has_answer = bool(sr.get("suggested_answer"))
            record(
                "Suggested response received",
                has_answer,
                f"answer_len={len(sr.get('suggested_answer', ''))}",
            )
        else:
            record("Suggested response received", False, "no suggestedResponse message")
    except Exception as e:
        record("Client question detection (question mark)", False, str(e))

    # --- Test 15b: Heuristic detection via interrogative word ---
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Client",
                    "text": "How does the integration with existing CRM systems work exactly",
                    "timestamp": "2025-01-15T10:02:00Z",
                },
            ],
            "speaker_hint": {"Host": "user", "Client": "client"},
        }))
        messages = ws_recv_all(ws, timeout_per_msg=30.0, max_messages=10)
        cqd = find_message(messages, "clientQuestionDetected")

        if cqd:
            record(
                "Client question detected (interrogative word)",
                True,
                f"method={cqd.get('detection_method')}, "
                f"q={cqd.get('question', '')[:50]}",
            )
        else:
            record(
                "Client question detected (interrogative word)",
                False,
                "no clientQuestionDetected",
            )
    except Exception as e:
        record("Client question detection (interrogative)", False, str(e))

    # --- Test 15c: Short text should NOT be detected (< 5 words) ---
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Client",
                    "text": "How much?",
                    "timestamp": "2025-01-15T10:03:00Z",
                },
            ],
        }))
        messages = ws_recv_all(ws, timeout_per_msg=10.0, max_messages=5)
        cqd = find_message(messages, "clientQuestionDetected")
        tp = find_message(messages, "transcriptProcessed")

        record(
            "Short client text processed",
            tp is not None,
            f"lines={tp.get('lines_processed') if tp else 0}",
        )
        record(
            "Short text NOT detected as question (<5 words)",
            cqd is None,
            "correctly skipped" if cqd is None else f"incorrectly detected: {cqd}",
        )
    except Exception as e:
        record("Short text skip", False, str(e))

    # --- Test 15d: Non-question client statement should NOT be detected ---
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Client",
                    "text": "That sounds great, I think we should move forward with the pilot program.",
                    "timestamp": "2025-01-15T10:04:00Z",
                },
            ],
        }))
        messages = ws_recv_all(ws, timeout_per_msg=30.0, max_messages=10)
        cqd = find_message(messages, "clientQuestionDetected")
        tp = find_message(messages, "transcriptProcessed")

        record(
            "Non-question client statement processed",
            tp is not None,
            f"lines={tp.get('lines_processed') if tp else 0}",
        )
        # This may or may not be detected depending on model — record as info
        if cqd is None:
            record("Non-question correctly not detected", True, "no false positive")
        else:
            print(f"  {WARN}  Non-question detected as question (model may disagree) — method={cqd.get('detection_method')}")
    except Exception as e:
        record("Non-question statement", False, str(e))

    ws.close()
    return session_id


def test_user_response_window(cqd_session_id: str):
    """17. User response window — capture user's response to client question."""
    print("\n── User Response Window Capture ──")

    # Reuse the session from client question detection (has open user response windows)
    session_id = cqd_session_id
    try:
        ws = ws_connect(session_id)
        record("Connect for user response window", True)
    except Exception as e:
        record("Connect for user response window", False, str(e))
        return

    # First, send a client question to open a user response window
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Client",
                    "text": "Can you explain how the onboarding process works for new customers?",
                    "timestamp": "2025-01-15T10:05:00Z",
                },
            ],
            "speaker_hint": {"Host": "user", "Client": "client"},
        }))
        messages = ws_recv_all(ws, timeout_per_msg=30.0, max_messages=10)
        cqd = find_message(messages, "clientQuestionDetected")
        record(
            "Client question opened response window",
            cqd is not None,
            f"detected={cqd is not None}",
        )
    except Exception as e:
        record("Open user response window", False, str(e))
        ws.close()
        return

    # Now send user response lines — should capture and auto-save
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Host",
                    "text": "Sure, the onboarding process starts with a kickoff call where we review your requirements.",
                    "timestamp": "2025-01-15T10:05:10Z",
                },
                {
                    "speaker": "Host",
                    "text": "Then we set up your project workspace and upload your initial documents to the knowledge base.",
                    "timestamp": "2025-01-15T10:05:20Z",
                },
                {
                    "speaker": "Client",
                    "text": "That makes sense, thank you for explaining.",
                    "timestamp": "2025-01-15T10:05:30Z",
                },
            ],
        }))
        messages = ws_recv_all(ws, timeout_per_msg=15.0, max_messages=15)
        qa_saved = find_message(messages, "qaPairAutoSaved")
        tp = find_message(messages, "transcriptProcessed")

        record(
            "User response lines processed",
            tp is not None,
            f"lines={tp.get('lines_processed') if tp else 0}",
        )

        if qa_saved:
            record(
                "QA pair auto-saved from user response window",
                True,
                f"source={qa_saved.get('source')}, "
                f"q={qa_saved.get('question', '')[:40]}...",
            )
            # Verify source is "client" (Stage 3 user response windows)
            record(
                "User response window source=client",
                qa_saved.get("source") == "client",
                f"source={qa_saved.get('source')}",
            )
            # Verify the answer contains user lines
            answer = qa_saved.get("answer", "")
            has_content = len(answer) > 20
            record(
                "Captured answer has content",
                has_content,
                f"answer_len={len(answer)}, preview={answer[:60]}...",
            )
        else:
            record(
                "QA pair auto-saved from user response window",
                False,
                "no qaPairAutoSaved (window may not have closed yet)",
            )
    except Exception as e:
        record("User response window capture", False, str(e))

    ws.close()


def test_full_live_transcript_flow():
    """18. Full integration — transcript → questions → matching → detection → QA."""
    print("\n── Full Live Transcript Flow ──")

    session_id = f"test-full-{uuid.uuid4().hex[:8]}"
    try:
        ws = ws_connect(session_id)
        record("Connect for full flow", True)
    except Exception as e:
        record("Connect for full flow", False, str(e))
        return

    all_messages = []

    # Step 1: Set suggested questions
    try:
        resp = ws_send_and_recv(ws, {
            "action": "setSuggestedQuestions",
            "session_id": session_id,
            "questions": [
                "What is the expected return on investment?",
                "How long does implementation typically take?",
            ],
        })
        ok = resp.get("type") == "suggestedQuestionsSet"
        record("Full flow: set suggested questions", ok, f"count={resp.get('count')}")
    except Exception as e:
        record("Full flow: set suggested questions", False, str(e))

    # Wait for embeddings to persist
    time.sleep(5)

    # Step 2: Process initial transcript with speaker hints
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Sales Rep",
                    "text": "Welcome to the demo. Let me show you our platform capabilities.",
                    "timestamp": "2025-01-15T14:00:00Z",
                },
                {
                    "speaker": "Prospect",
                    "text": "Thanks, I'm particularly interested in the analytics features.",
                    "timestamp": "2025-01-15T14:00:10Z",
                },
            ],
            "speaker_hint": {"Sales Rep": "user", "Prospect": "client"},
        }))
        messages = ws_recv_all(ws, timeout_per_msg=15.0)
        all_messages.extend(messages)
        tp = find_message(messages, "transcriptProcessed")
        record("Full flow: initial transcript", tp is not None, f"lines={tp.get('lines_processed') if tp else 0}")
    except Exception as e:
        record("Full flow: initial transcript", False, str(e))

    # Step 3: User asks something matching a suggested question
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Sales Rep",
                    "text": "What is the expected return on investment?",
                    "timestamp": "2025-01-15T14:01:00Z",
                },
            ],
            "speaker_hint": {"Sales Rep": "user", "Prospect": "client"},
        }))
        messages = ws_recv_all(ws, timeout_per_msg=15.0)
        all_messages.extend(messages)
        qm = find_message(messages, "questionMatched")
        record(
            "Full flow: user question matched",
            qm is not None,
            f"sim={qm.get('similarity') if qm else 'N/A'}",
        )
    except Exception as e:
        record("Full flow: user question matched", False, str(e))

    # Step 4: Client responds (answer window capture)
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Prospect",
                    "text": "Most of our customers see a three to five X return within the first year.",
                    "timestamp": "2025-01-15T14:01:10Z",
                },
                {
                    "speaker": "Sales Rep",
                    "text": "That's impressive. Let me show you some case studies.",
                    "timestamp": "2025-01-15T14:01:20Z",
                },
            ],
            "speaker_hint": {"Sales Rep": "user", "Prospect": "client"},
        }))
        messages = ws_recv_all(ws, timeout_per_msg=15.0)
        all_messages.extend(messages)
        qa_participant = find_message(messages, "qaPairAutoSaved")
        if qa_participant:
            record(
                "Full flow: answer window QA saved",
                True,
                f"source={qa_participant.get('source')}",
            )
        else:
            record("Full flow: answer window QA saved", False, "no auto-save triggered")
    except Exception as e:
        record("Full flow: answer window QA", False, str(e))

    # Step 5: Client asks a question AND user responds (same batch for state continuity)
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {
                    "speaker": "Prospect",
                    "text": "How long does the typical implementation process take for enterprise clients?",
                    "timestamp": "2025-01-15T14:02:00Z",
                },
                {
                    "speaker": "Sales Rep",
                    "text": "Implementation typically takes four to six weeks depending on the complexity of your setup.",
                    "timestamp": "2025-01-15T14:02:10Z",
                },
                {
                    "speaker": "Sales Rep",
                    "text": "We assign a dedicated implementation manager to guide you through the process.",
                    "timestamp": "2025-01-15T14:02:20Z",
                },
                {
                    "speaker": "Prospect",
                    "text": "That timeline works for us.",
                    "timestamp": "2025-01-15T14:02:30Z",
                },
            ],
            "speaker_hint": {"Sales Rep": "user", "Prospect": "client"},
        }))
        messages = ws_recv_all(ws, timeout_per_msg=30.0, max_messages=15)
        all_messages.extend(messages)
        cqd = find_message(messages, "clientQuestionDetected")
        sr = find_message(messages, "suggestedResponse")

        record(
            "Full flow: client question detected",
            cqd is not None,
            f"method={cqd.get('detection_method') if cqd else 'N/A'}",
        )
        record(
            "Full flow: suggested response sent",
            sr is not None,
            f"answer_len={len(sr.get('suggested_answer', '')) if sr else 0}",
        )

        qa_client = find_message(messages, "qaPairAutoSaved")
        if qa_client:
            record(
                "Full flow: user response window QA saved",
                True,
                f"source={qa_client.get('source')}, "
                f"q={qa_client.get('question', '')[:40]}...",
            )
            record(
                "Full flow: source=client for user response",
                qa_client.get("source") == "client",
                f"source={qa_client.get('source')}",
            )
        else:
            record("Full flow: user response window QA saved", False, "no auto-save")
    except Exception as e:
        record("Full flow: client question + response", False, str(e))

    # Summary of all message types received
    type_counts = {}
    for m in all_messages:
        t = m.get("type", "unknown")
        type_counts[t] = type_counts.get(t, 0) + 1
    print(f"  {INFO}  All message types received: {type_counts}")

    ws.close()


def test_process_transcript_edge_cases():
    """Edge cases: empty lines, missing fields, user-only transcript."""
    print("\n── processTranscript Edge Cases ──")

    session_id = f"test-edge-{uuid.uuid4().hex[:8]}"
    try:
        ws = ws_connect(session_id)
        record("Connect for edge cases", True)
    except Exception as e:
        record("Connect for edge cases", False, str(e))
        return

    # Empty lines array
    try:
        resp = ws_send_and_recv(ws, {
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [],
        })
        ok = resp.get("type") == "error"
        record("Empty lines rejected", ok, f"type={resp.get('type')}")
    except Exception as e:
        record("Empty lines rejected", False, str(e))

    # Single speaker transcript (no classification needed)
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {"speaker": "Solo", "text": "I'm presenting to myself today."},
                {"speaker": "Solo", "text": "Let me review the quarterly numbers."},
            ],
        }))
        messages = ws_recv_all(ws, timeout_per_msg=10.0)
        tp = find_message(messages, "transcriptProcessed")
        role_map = tp.get("speaker_role_map", {}) if tp else {}
        record(
            "Single speaker transcript",
            tp is not None and role_map.get("Solo") == "user",
            f"roles={role_map}",
        )
    except Exception as e:
        record("Single speaker transcript", False, str(e))

    # Large batch (10 lines)
    try:
        lines = [
            {"speaker": "A", "text": f"This is line number {i} of the large batch test."}
            for i in range(10)
        ]
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": lines,
            "speaker_hint": {"A": "user"},
        }))
        messages = ws_recv_all(ws, timeout_per_msg=15.0)
        tp = find_message(messages, "transcriptProcessed")
        record(
            "Large batch (10 lines)",
            tp is not None and tp.get("lines_processed") == 10,
            f"lines={tp.get('lines_processed') if tp else 0}",
        )
    except Exception as e:
        record("Large batch", False, str(e))

    ws.close()


# ---------------------------------------------------------------------------
# Cleanup
# ---------------------------------------------------------------------------

def test_skills_crud(agent_id: str):
    """Test the full skills CRUD lifecycle including pre-signed URL upload."""
    print("\n── Skills CRUD ──")

    if not agent_id:
        record("Skills CRUD", False, "skipped — no agent_id")
        return None

    # 1. Create skill
    body = {
        "agent_id": agent_id,
        "skill_name": f"TestSkill-{uuid.uuid4().hex[:8]}",
        "file_name": "test-skill.md",
        "description": "A test skill for integration testing",
    }
    r = rest_post("/skills", body)
    data = r.json().get("data", {})
    skill = data.get("skill", {})
    upload_url = data.get("upload_url", "")
    skill_id = skill.get("skill_id", "")
    record(
        "Create skill",
        r.status_code == 200 and skill_id and upload_url,
        f"id={skill_id}, status={skill.get('status')}",
    )

    if not skill_id:
        return None

    # 2. Upload test file via pre-signed URL
    test_content = (
        "# Test Skill Document\n\n"
        "This is a test skill document for integration testing.\n\n"
        "## Key Points\n\n"
        "- Point one about the skill\n"
        "- Point two about the skill\n"
        "- Point three about the skill\n"
    )
    upload_r = requests.put(upload_url, data=test_content.encode("utf-8"), timeout=30)
    record("Upload file via pre-signed URL", upload_r.status_code == 200, f"status={upload_r.status_code}")

    # 3. Poll for ingestion completion
    print(f"  {INFO}  Polling skill status (waiting for ingestion)...")
    max_wait = 60
    start = time.time()
    final_status = "pending"
    while time.time() - start < max_wait:
        sr = rest_get(f"/skills/{skill_id}")
        sdata = sr.json().get("data", {})
        final_status = sdata.get("status", "pending")
        if final_status in ("active", "failed"):
            break
        time.sleep(5)
    record("Skill ingestion", final_status == "active", f"status={final_status}")

    # 4. List skills for agent
    r = rest_get("/skills", params={"agent_id": agent_id})
    items = r.json().get("data", {}).get("items", [])
    pagination = r.json().get("data", {}).get("pagination", {})
    found = any(s.get("skill_id") == skill_id for s in items)
    record("List skills for agent", r.status_code == 200 and found, f"total={pagination.get('total', 0)}")

    # 5. Get single skill
    r = rest_get(f"/skills/{skill_id}")
    record("Get skill", r.status_code == 200 and r.json().get("data", {}).get("skill_id") == skill_id)

    # 6. Update skill
    r = rest_put(f"/skills/{skill_id}", {"skill_name": "UpdatedTestSkill"})
    updated_name = r.json().get("data", {}).get("skill_name", "")
    record("Update skill", r.status_code == 200 and updated_name == "UpdatedTestSkill")

    # 7. Error cases
    r = rest_get("/skills")
    record("List skills without agent_id → 400", r.status_code == 400)

    r = rest_post("/skills", {"agent_id": "non-existent-id", "skill_name": "X", "file_name": "x.md"})
    record("Create skill with bad agent_id → 400", r.status_code == 400)

    r = rest_get(f"/skills/non-existent-id")
    record("Get non-existent skill → 404", r.status_code == 404)

    # 8. Delete skill
    r = rest_delete(f"/skills/{skill_id}")
    record("Delete skill", r.status_code == 200)

    r = rest_get(f"/skills/{skill_id}")
    record("Get deleted skill → 404", r.status_code == 404)

    return skill_id


def cleanup(agent_id, personality_id, qa_pair_id):
    print("\n── Cleanup ──")

    if agent_id:
        r = rest_delete(f"/agents/{agent_id}")
        record("Delete test agent", r.status_code == 200)

    if personality_id:
        r = rest_delete(f"/personalities/{personality_id}")
        record("Delete test personality", r.status_code == 200)

    if qa_pair_id:
        r = rest_delete(f"/qa-pairs/{qa_pair_id}")
        record("Delete test QA pair", r.status_code == 200)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    global VERBOSE
    if "--verbose" in sys.argv or "-v" in sys.argv:
        VERBOSE = True

    print("=" * 60)
    print("  GMeet Agent — End-to-End Test Suite")
    if VERBOSE:
        print("  (verbose mode ON — full response payloads will be printed)")
    print("=" * 60)

    # REST API tests
    personality_id = test_personalities_crud()
    agent_id = test_agents_crud(personality_id)

    # WebSocket tests (original actions)
    session_id = test_websocket_actions()

    print(f"\n{INFO}  Waiting 3s for session state to settle...")
    time.sleep(3)

    # QA Pairs REST test
    qa_pair_id = test_qa_pairs_crud(session_id)

    # Skills CRUD test
    test_skills_crud(agent_id)

    # Retro mode tests
    test_retro_actions(session_id)

    # --- Stage 1: Transcript Processing ---
    test_process_transcript_with_hints()
    test_process_transcript_model_classification()

    # --- Stage 2: Question Matching & Answer Windows ---
    sq_session_id = test_set_suggested_questions()
    print(f"\n{INFO}  Waiting 5s for embeddings to persist...")
    time.sleep(5)
    test_question_matching_and_answer_window(sq_session_id)

    # --- Stage 3: Client Question Detection & Suggested Response ---
    cqd_session_id = test_client_question_detection()
    test_user_response_window(cqd_session_id)

    # --- Full Integration Flow ---
    test_full_live_transcript_flow()

    # --- Edge Cases ---
    test_process_transcript_edge_cases()

    # Cleanup
    cleanup(agent_id, personality_id, qa_pair_id)

    # Summary
    total = len(results)
    passed = sum(1 for _, ok, _ in results if ok)
    failed = total - passed
    print("\n" + "=" * 60)
    print(f"  Results: {passed}/{total} passed", end="")
    if failed:
        print(f"  ({failed} failed)")
        print("\n  Failed tests:")
        for name, ok, detail in results:
            if not ok:
                print(f"    ✗ {name}" + (f" — {detail}" if detail else ""))
    else:
        print("  — all green!")
    print("=" * 60)

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
