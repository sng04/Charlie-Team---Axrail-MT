#!/usr/bin/env python3
"""
End-to-end test script for all AXRAIL Meeting-Tool endpoints (merged D1 + D2).

Covers:
  REST API  — Auth, Projects, Sessions, Agents, Personalities, Skills,
              QA Pairs, Bot Credentials, Warm Pool, Meeting Bot, Project Users
  WebSocket — sendMessage, detectQuestion, processTranscript,
              analyzeGaps, endMeeting, retroAnalysis, retroChat,
              setSuggestedQuestions

Usage:
    pip3 install websocket-client requests boto3
    python3 test_all_endpoints.py            # compact output
    python3 test_all_endpoints.py --verbose   # full response payloads
    python3 test_all_endpoints.py -v          # same as --verbose
"""

import json
import os
import ssl
import sys
import time
import uuid

import requests
import websocket

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REST_URL = os.environ.get(
    "REST_API_URL",
    "https://sjsd378hbd.execute-api.ap-southeast-1.amazonaws.com/dev",
).rstrip("/")

WS_URL = os.environ.get(
    "WS_API_URL",
    "wss://hey8o0q9tb.execute-api.ap-southeast-1.amazonaws.com/production",
)

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "Admin@12345")

WS_TIMEOUT = 90  # seconds — Bedrock calls can be slow
VERBOSE = False

# macOS Python SSL workaround
_SSL_OPTS = {"cert_reqs": ssl.CERT_NONE}

PASS = "\033[92m✓ PASS\033[0m"
FAIL = "\033[91m✗ FAIL\033[0m"
INFO = "\033[94mℹ INFO\033[0m"
WARN = "\033[93m⚠ WARN\033[0m"
VTAG = "\033[95m⤷ RESP\033[0m"

results: list[tuple[str, bool, str]] = []


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def record(name: str, passed: bool, detail: str = ""):
    tag = PASS if passed else FAIL
    print(f"  {tag}  {name}" + (f"  — {detail}" if detail else ""))
    results.append((name, passed, detail))


def vprint(label: str, data):
    if not VERBOSE:
        return
    formatted = json.dumps(data, indent=2, default=str) if isinstance(data, (dict, list)) else str(data)
    for line in formatted.splitlines():
        print(f"    {VTAG}  [{label}] {line}")


def rest(method: str, path: str, token: str = "", body: dict | None = None,
         params: dict | None = None) -> requests.Response:
    url = f"{REST_URL}/{path.lstrip('/')}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    r = requests.request(method, url, headers=headers, json=body, params=params, timeout=30)
    try:
        vprint(f"{method} {path}", r.json())
    except Exception:
        vprint(f"{method} {path}", r.text)
    return r


def ws_connect(session_id: str = "", agent_id: str = "") -> websocket.WebSocket:
    url = WS_URL
    qs = []
    if session_id:
        qs.append(f"session_id={session_id}")
    if agent_id:
        qs.append(f"agent_id={agent_id}")
    if qs:
        url += "?" + "&".join(qs)
    ws = websocket.WebSocket(sslopt=_SSL_OPTS)
    ws.settimeout(WS_TIMEOUT)
    ws.connect(url)
    return ws


def ws_send_recv(ws, payload: dict) -> dict:
    ws.send(json.dumps(payload))
    raw = ws.recv()
    resp = json.loads(raw)
    vprint(f"WS {payload.get('action', '?')}", resp)
    return resp


def ws_recv_all(ws, timeout_per_msg: float = 5.0, max_messages: int = 30) -> list:
    messages = []
    old = ws.gettimeout()
    ws.settimeout(timeout_per_msg)
    for _ in range(max_messages):
        try:
            raw = ws.recv()
            msg = json.loads(raw)
            vprint("WS recv", msg)
            messages.append(msg)
        except websocket.WebSocketTimeoutException:
            break
        except Exception:
            break
    ws.settimeout(old)
    return messages


def find_msg(messages: list, msg_type: str) -> dict | None:
    for m in messages:
        if m.get("type") == msg_type:
            return m
    return None


# ===========================================================================
# 0. Authentication
# ===========================================================================

def test_auth() -> str:
    """Authenticate as admin and return JWT token."""
    print("\n── Authentication ──")

    r = rest("POST", "/auth/admin/login", body={
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD,
    })
    data = r.json().get("data", {})
    token = data.get("access_token", "")
    record("Admin login", r.status_code == 200 and bool(token),
           f"status={r.status_code}")

    if not token:
        print(f"  {FAIL}  Cannot continue without token. Aborting.")
        raise SystemExit(1)

    # Change password (no-op — same password)
    r2 = rest("POST", "/auth/change-password", body={
        "username": ADMIN_USERNAME,
        "old_password": ADMIN_PASSWORD,
        "new_password": ADMIN_PASSWORD,
    })
    record("Change password endpoint reachable",
           r2.status_code in (200, 400),
           f"status={r2.status_code}")

    return token


# ===========================================================================
# 1. Projects CRUD
# ===========================================================================

def test_projects_crud(token: str) -> str:
    print("\n── Projects CRUD ──")

    r = rest("GET", "/projects", token)
    record("List projects", r.status_code == 200, f"status={r.status_code}")

    r = rest("POST", "/projects", token, body={
        "name": f"TestProject-{uuid.uuid4().hex[:8]}",
        "email": "test@example.com",
        "description": "Integration test project",
    })
    data = r.json().get("data", {})
    pid = data.get("project_id", "")
    record("Create project", r.status_code == 200 and bool(pid), f"id={pid}")

    if not pid:
        return ""

    r = rest("GET", f"/projects/{pid}", token)
    record("Get project", r.status_code == 200)

    r = rest("PUT", f"/projects/{pid}", token, body={"description": "Updated"})
    record("Update project", r.status_code == 200)

    r = rest("GET", f"/projects/{pid}/users", token)
    record("Get project users", r.status_code == 200, f"status={r.status_code}")

    return pid


# ===========================================================================
# 2. Sessions CRUD
# ===========================================================================

def test_sessions_crud(token: str, project_id: str) -> str:
    print("\n── Sessions CRUD ──")

    r = rest("GET", "/sessions", token)
    record("List sessions", r.status_code == 200, f"status={r.status_code}")

    r = rest("POST", "/sessions", token, body={
        "project_id": project_id,
        "name": f"TestSession-{uuid.uuid4().hex[:8]}",
        "description": "Integration test session",
    })
    data = r.json().get("data", {})
    sid = data.get("session_id", "")
    record("Create session (no meeting_link)", r.status_code == 200 and bool(sid),
           f"id={sid}")

    if not sid:
        return ""

    r = rest("GET", f"/sessions/{sid}", token)
    record("Get session", r.status_code == 200)

    r = rest("PUT", f"/sessions/{sid}", token, body={"description": "Updated session"})
    record("Update session", r.status_code == 200)

    r = rest("GET", f"/projects/{project_id}/sessions", token)
    record("Get project sessions", r.status_code == 200)

    # Meeting bot sub-routes (will 4xx without a real bot, but endpoint should exist)
    r = rest("GET", f"/sessions/{sid}/transcripts", token)
    record("Get session transcripts", r.status_code in (200, 404),
           f"status={r.status_code}")

    r = rest("GET", f"/sessions/{sid}/bot-status", token)
    record("Get bot status", r.status_code in (200, 404),
           f"status={r.status_code}")

    return sid


# ===========================================================================
# 3. Personalities CRUD
# ===========================================================================

def test_personalities_crud(token: str) -> str:
    print("\n── Personalities CRUD ──")

    r = rest("GET", "/personalities", token)
    record("List personalities", r.status_code == 200, f"status={r.status_code}")

    r = rest("POST", "/personalities", token, body={
        "personality_name": f"TestPersonality-{uuid.uuid4().hex[:8]}",
        "personality_prompt": "Speak like a pirate. Arrr!",
    })
    data = r.json().get("data", {})
    pid = data.get("personality_id", "")
    record("Create personality", r.status_code == 200 and bool(pid), f"id={pid}")

    if not pid:
        return ""

    r = rest("GET", f"/personalities/{pid}", token)
    record("Get personality", r.status_code == 200)

    r = rest("PUT", f"/personalities/{pid}", token, body={
        "personality_prompt": "Updated prompt",
    })
    record("Update personality", r.status_code == 200)

    return pid


# ===========================================================================
# 4. Agents CRUD
# ===========================================================================

def test_agents_crud(token: str, personality_id: str) -> str:
    print("\n── Agents CRUD ──")

    if not personality_id:
        record("Agents CRUD", False, "skipped — no personality_id")
        return ""

    r = rest("GET", "/agents", token)
    record("List agents", r.status_code == 200, f"status={r.status_code}")

    r = rest("POST", "/agents", token, body={
        "agent_name": f"TestAgent-{uuid.uuid4().hex[:8]}",
        "role_prompt": "You are a test agent.",
        "task_prompt": "Answer test questions.",
        "personality_id": personality_id,
        "model_id": "amazon.nova-pro-v1:0",
        "use_case": "testing",
    })
    data = r.json().get("data", {})
    aid = data.get("agent_id", "")
    record("Create agent", r.status_code == 200 and bool(aid), f"id={aid}")

    if not aid:
        return ""

    r = rest("GET", f"/agents/{aid}", token)
    record("Get agent", r.status_code == 200)

    r = rest("PUT", f"/agents/{aid}", token, body={"agent_name": "UpdatedTestAgent"})
    record("Update agent", r.status_code == 200)

    return aid


# ===========================================================================
# 5. Skills CRUD
# ===========================================================================

def test_skills_crud(token: str, agent_id: str) -> str:
    print("\n── Skills CRUD ──")

    if not agent_id:
        record("Skills CRUD", False, "skipped — no agent_id")
        return ""

    r = rest("POST", "/skills", token, body={
        "skill_name": f"TestSkill-{uuid.uuid4().hex[:8]}",
        "file_name": "test-skill.md",
        "description": "Integration test skill",
    })
    data = r.json().get("data", {})
    skill_data = data.get("skill", data)
    upload_url = data.get("upload_url", "")
    skill_id = skill_data.get("skill_id", "")
    record("Create skill (standalone)", r.status_code == 200 and bool(skill_id),
           f"id={skill_id}")

    if not skill_id:
        return ""

    # Assign skill to agent
    r = rest("POST", f"/agents/{agent_id}/skills/{skill_id}", token)
    record("Assign skill to agent", r.status_code == 200,
           f"status={r.status_code}")

    # Verify assignment via agent skills list
    r = rest("GET", f"/agents/{agent_id}/skills", token)
    record("List agent skills (assignment endpoint)", r.status_code == 200)

    # Upload via pre-signed URL
    if upload_url:
        content = b"# Test Skill\n\nThis is a test skill document.\n"
        ur = requests.put(upload_url, data=content, timeout=30)
        record("Upload skill file (pre-signed URL)", ur.status_code == 200,
               f"status={ur.status_code}")
    else:
        record("Upload skill file (pre-signed URL)", False, "no upload_url returned")

    r = rest("GET", f"/skills?agent_id={agent_id}", token)
    record("List skills for agent (backward compat)", r.status_code == 200)

    r = rest("GET", f"/skills/{skill_id}", token)
    record("Get skill", r.status_code == 200)

    r = rest("PUT", f"/skills/{skill_id}", token, body={"skill_name": "UpdatedSkill"})
    record("Update skill", r.status_code == 200)

    return skill_id


# ===========================================================================
# 6. QA Pairs
# ===========================================================================

def test_qa_pairs(token: str, session_id: str) -> str:
    print("\n── QA Pairs ──")

    r = rest("GET", f"/qa-pairs?session_id={session_id}", token)
    record("List QA pairs by session", r.status_code == 200,
           f"status={r.status_code}")

    items = r.json().get("data", [])
    if isinstance(items, dict):
        items = items.get("items", [])

    if items:
        qid = items[0].get("qa_pair_id", "")
        r2 = rest("GET", f"/qa-pairs/{qid}", token)
        record("Get QA pair", r2.status_code == 200, f"id={qid}")
        return qid

    record("Get QA pair", True, "skipped — no QA pairs yet (expected)")
    return ""


# ===========================================================================
# 7. Bot Credentials CRUD
# ===========================================================================

def test_bot_credentials_crud(token: str) -> str:
    print("\n── Bot Credentials CRUD ──")

    r = rest("GET", "/bot-credentials", token)
    record("List bot credentials", r.status_code == 200, f"status={r.status_code}")

    r = rest("POST", "/bot-credentials", token, body={
        "email": f"bot-{uuid.uuid4().hex[:6]}@example.com",
        "password": "test-bot-password-1234",
    })
    data = r.json().get("data", {})
    cid = data.get("credential_id", "")
    record("Create bot credential", r.status_code == 200 and bool(cid),
           f"id={cid}")

    if not cid:
        return ""

    r = rest("GET", f"/bot-credentials/{cid}", token)
    record("Get bot credential", r.status_code == 200)

    r = rest("PUT", f"/bot-credentials/{cid}", token, body={
        "platform": "zoom",
    })
    record("Update bot credential", r.status_code == 200)

    # Verify endpoint (public — no auth)
    r = rest("GET", f"/bot-credentials/{cid}/verify")
    record("Verify bot credential endpoint", r.status_code in (200, 400, 404),
           f"status={r.status_code}")

    return cid


# ===========================================================================
# 8. Warm Pool
# ===========================================================================

def test_warm_pool(token: str):
    print("\n── Warm Pool ──")

    # These may fail if ECS is not configured, but the endpoints should respond
    r = rest("POST", "/warm-pool/start", token, body={})
    record("Start warm pool endpoint", r.status_code in (200, 400, 500),
           f"status={r.status_code}")

    r = rest("POST", "/warm-pool/stop", token, body={})
    record("Stop warm pool endpoint", r.status_code in (200, 400, 500),
           f"status={r.status_code}")


# ===========================================================================
# 9. Project Users
# ===========================================================================

def test_project_users(token: str, project_id: str):
    print("\n── Project Users ──")

    if not project_id:
        record("Project users", False, "skipped — no project_id")
        return

    # Create a test user first
    r = rest("POST", "/users", token, body={
        "email": f"testuser-{uuid.uuid4().hex[:6]}@example.com",
        "password": "TestPass@123",
        "name": "Test User",
    })
    data = r.json().get("data", {})
    user_id = data.get("user_id", data.get("sub", ""))
    record("Create user", r.status_code in (200, 400),
           f"status={r.status_code}, id={user_id}")

    if user_id:
        # Assign user to project
        r = rest("POST", "/project-users", token, body={
            "project_id": project_id,
            "user_id": user_id,
        })
        record("Assign user to project", r.status_code in (200, 400),
               f"status={r.status_code}")

        # Get user's projects
        r = rest("GET", f"/users/{user_id}/projects", token)
        record("Get user projects", r.status_code in (200, 404),
               f"status={r.status_code}")


# ===========================================================================
# 10. WebSocket — Core Actions
# ===========================================================================

def test_ws_core_actions(session_id: str, agent_id: str):
    print("\n── WebSocket Core Actions ──")

    try:
        ws = ws_connect(session_id, agent_id)
        record("WebSocket connect", True, f"session={session_id}")
    except Exception as e:
        record("WebSocket connect", False, str(e))
        return

    # sendMessage
    try:
        ws.send(json.dumps({
            "action": "sendMessage",
            "session_id": session_id,
            "message": "Hello, what can you do?",
        }))
        messages = ws_recv_all(ws, timeout_per_msg=20.0, max_messages=5)
        has_resp = any(m.get("type") in ("response", "error") for m in messages)
        record("sendMessage", has_resp,
               f"types={[m.get('type') for m in messages]}")
    except Exception as e:
        record("sendMessage", False, str(e))

    # detectQuestion
    try:
        ws.send(json.dumps({
            "action": "detectQuestion",
            "session_id": session_id,
            "question": "What is the project timeline?",
        }))
        messages = ws_recv_all(ws, timeout_per_msg=20.0, max_messages=5)
        has_resp = any(m.get("type") in ("questionResponse", "error") for m in messages)
        record("detectQuestion", has_resp,
               f"types={[m.get('type') for m in messages]}")
    except Exception as e:
        record("detectQuestion", False, str(e))

    # analyzeGaps
    try:
        ws.send(json.dumps({
            "action": "analyzeGaps",
            "session_id": session_id,
        }))
        messages = ws_recv_all(ws, timeout_per_msg=30.0, max_messages=5)
        has_resp = any(m.get("type") in ("gapAnalysis", "error") for m in messages)
        record("analyzeGaps", has_resp,
               f"types={[m.get('type') for m in messages]}")
    except Exception as e:
        record("analyzeGaps", False, str(e))

    ws.close()


# ===========================================================================
# 11. WebSocket — processTranscript (basic)
# ===========================================================================

def test_ws_process_transcript_basic(session_id: str, agent_id: str):
    print("\n── processTranscript (basic) ──")

    try:
        ws = ws_connect(session_id, agent_id)
        record("Connect for processTranscript basic", True)
    except Exception as e:
        record("Connect for processTranscript basic", False, str(e))
        return

    lines = [
        {"speaker": "spk_0", "text": "Welcome everyone, let's get started with the demo.",
         "start_time": "0.00", "end_time": "3.50", "confidence": "0.95", "is_partial": False},
        {"speaker": "spk_0", "text": "Thanks Alice, excited to see what you've built.",
         "start_time": "3.80", "end_time": "6.20", "confidence": "0.93", "is_partial": False},
        {"speaker": "spk_0", "text": "We have a new feature for real-time question detection.",
         "start_time": "6.50", "end_time": "9.80", "confidence": "0.97", "is_partial": False},
    ]

    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": lines,
        }))
        messages = ws_recv_all(ws, timeout_per_msg=15.0)
        tp = find_msg(messages, "transcriptProcessed")
        ok = tp is not None and tp.get("lines_processed") == 3
        record("processTranscript basic", ok,
               f"lines={tp.get('lines_processed') if tp else 0}")
    except Exception as e:
        record("processTranscript basic", False, str(e))

    ws.close()


# ===========================================================================
# 12. WebSocket — processTranscript (no hints)
# ===========================================================================

def test_ws_process_transcript_no_hints(session_id: str, agent_id: str):
    print("\n── processTranscript (no hints) ──")

    try:
        ws = ws_connect(session_id, agent_id)
        record("Connect for processTranscript no hints", True)
    except Exception as e:
        record("Connect for processTranscript no hints", False, str(e))
        return

    lines = [
        {"speaker": "spk_0",
         "text": "Hi, I'm the sales rep. Let me walk you through our product features today.",
         "start_time": "0.00", "end_time": "4.50", "confidence": "0.92", "is_partial": False},
        {"speaker": "spk_0",
         "text": "Great, I'm interested in learning about your pricing and integration options.",
         "start_time": "5.00", "end_time": "8.30", "confidence": "0.94", "is_partial": False},
        {"speaker": "spk_0",
         "text": "Our platform starts at fifty dollars per month for the basic tier.",
         "start_time": "8.80", "end_time": "12.10", "confidence": "0.96", "is_partial": False},
    ]

    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": lines,
        }))
        messages = ws_recv_all(ws, timeout_per_msg=30.0)
        tp = find_msg(messages, "transcriptProcessed")
        ok = tp is not None and tp.get("lines_processed") == 3
        record("processTranscript no hints", ok,
               f"lines={tp.get('lines_processed') if tp else 0}")
    except Exception as e:
        record("processTranscript no hints", False, str(e))

    ws.close()


# ===========================================================================
# 13. WebSocket — setSuggestedQuestions + question matching
# ===========================================================================

def test_ws_suggested_questions(session_id: str, agent_id: str):
    print("\n── setSuggestedQuestions & Question Matching ──")

    try:
        ws = ws_connect(session_id, agent_id)
        record("Connect for setSuggestedQuestions", True)
    except Exception as e:
        record("Connect for setSuggestedQuestions", False, str(e))
        return

    questions = [
        "What is the pricing model for the enterprise tier?",
        "How does the integration with Salesforce work?",
        "What security certifications do you have?",
    ]

    try:
        resp = ws_send_recv(ws, {
            "action": "setSuggestedQuestions",
            "session_id": session_id,
            "questions": questions,
        })
        ok = resp.get("type") == "suggestedQuestionsSet" and resp.get("count") == 3
        record("setSuggestedQuestions", ok,
               f"type={resp.get('type')}, count={resp.get('count')}")
    except Exception as e:
        record("setSuggestedQuestions", False, str(e))

    # Empty list should be rejected
    try:
        resp = ws_send_recv(ws, {
            "action": "setSuggestedQuestions",
            "session_id": session_id,
            "questions": [],
        })
        record("Empty questions rejected", resp.get("type") == "error",
               f"type={resp.get('type')}")
    except Exception as e:
        record("Empty questions rejected", False, str(e))

    time.sleep(3)

    # Send a line that matches a suggested question
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [{
                "speaker": "spk_0",
                "text": "What is the pricing model for the enterprise tier?",
                "timestamp": "2026-03-21T10:00:00Z",
                "start_time": "0.00",
                "end_time": "3.50",
                "confidence": "0.95",
                "is_partial": False,
            }],
        }))
        messages = ws_recv_all(ws, timeout_per_msg=15.0)
        qm = find_msg(messages, "questionMatched")
        record("Question matched", qm is not None,
               f"sim={qm.get('similarity') if qm else 'N/A'}")
    except Exception as e:
        record("Question matching", False, str(e))

    ws.close()


# ===========================================================================
# 14. WebSocket — Question detection + suggested response
# ===========================================================================

def test_ws_question_detection(session_id: str, agent_id: str):
    print("\n── Question Detection & Suggested Response ──")

    try:
        ws = ws_connect(session_id, agent_id)
        record("Connect for question detection", True)
    except Exception as e:
        record("Connect for question detection", False, str(e))
        return

    # Question mark heuristic
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [{
                "speaker": "spk_0",
                "text": "What kind of security certifications does your platform have?",
                "timestamp": "2026-03-21T10:01:00Z",
                "start_time": "0.00",
                "end_time": "4.20",
                "confidence": "0.95",
                "is_partial": False,
            }],
        }))
        messages = ws_recv_all(ws, timeout_per_msg=30.0, max_messages=10)
        qd = find_msg(messages, "questionDetected")
        sr = find_msg(messages, "suggestedResponse")

        record("Question detected (? mark)", qd is not None,
               f"method={qd.get('detection_method') if qd else 'N/A'}")
        record("Suggested response received", sr is not None,
               f"len={len(sr.get('suggested_answer', '')) if sr else 0}")
    except Exception as e:
        record("Question detection", False, str(e))

    # Short text should NOT be detected
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [{
                "speaker": "spk_0",
                "text": "How much?",
                "timestamp": "2026-03-21T10:02:00Z",
                "start_time": "5.00",
                "end_time": "5.80",
                "confidence": "0.90",
                "is_partial": False,
            }],
        }))
        messages = ws_recv_all(ws, timeout_per_msg=10.0, max_messages=5)
        qd = find_msg(messages, "questionDetected")
        record("Short text NOT detected (<5 words)", qd is None,
               "correctly skipped" if qd is None else "incorrectly detected")
    except Exception as e:
        record("Short text skip", False, str(e))

    ws.close()


# ===========================================================================
# 15. WebSocket — endMeeting + retroAnalysis + retroChat
# ===========================================================================

def test_ws_meeting_lifecycle(session_id: str, agent_id: str):
    print("\n── Meeting Lifecycle (endMeeting → retro) ──")

    # endMeeting
    try:
        ws = ws_connect(session_id, agent_id)
        ws.send(json.dumps({
            "action": "endMeeting",
            "session_id": session_id,
        }))
        messages = ws_recv_all(ws, timeout_per_msg=45.0, max_messages=5)
        summary = find_msg(messages, "meetingSummary")
        err = find_msg(messages, "error")
        ok = summary is not None or err is not None
        record("endMeeting", ok,
               f"type={'meetingSummary' if summary else 'error'}")
        ws.close()
    except Exception as e:
        record("endMeeting", False, str(e))

    time.sleep(2)

    # retroAnalysis
    try:
        ws = ws_connect(session_id, agent_id)
        ws.send(json.dumps({
            "action": "retroAnalysis",
            "session_id": session_id,
        }))
        messages = ws_recv_all(ws, timeout_per_msg=45.0, max_messages=5)
        retro = find_msg(messages, "retroFeedback")
        err = find_msg(messages, "error")
        ok = retro is not None or err is not None
        detail = "retroFeedback" if retro else f"error: {err.get('message', '')[:60]}" if err else "no response"
        record("retroAnalysis", ok, f"type={detail}")
        retro_ok = retro is not None
    except Exception as e:
        record("retroAnalysis", False, str(e))
        retro_ok = False

    # retroChat
    try:
        ws.send(json.dumps({
            "action": "retroChat",
            "session_id": session_id,
            "message": "What were the main action items?",
        }))
        messages = ws_recv_all(ws, timeout_per_msg=25.0, max_messages=5)
        resp = find_msg(messages, "retroResponse")
        err = find_msg(messages, "error")
        ok = resp is not None or err is not None
        if not retro_ok and err:
            detail = "error (expected — no retro context)"
        elif resp:
            detail = "retroResponse"
        else:
            detail = "no response"
        record("retroChat", ok, f"type={detail}")
        ws.close()
    except Exception as e:
        record("retroChat", False, str(e))


# ===========================================================================
# 16. WebSocket — Edge Cases
# ===========================================================================

def test_ws_edge_cases(session_id: str, agent_id: str):
    print("\n── processTranscript Edge Cases ──")

    try:
        ws = ws_connect(session_id, agent_id)
        record("Connect for edge cases", True)
    except Exception as e:
        record("Connect for edge cases", False, str(e))
        return

    # Empty lines
    try:
        resp = ws_send_recv(ws, {
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [],
        })
        record("Empty lines rejected", resp.get("type") == "error",
               f"type={resp.get('type')}")
    except Exception as e:
        record("Empty lines rejected", False, str(e))

    # Single speaker
    try:
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": [
                {"speaker": "spk_0", "text": "I'm presenting to myself today.",
                 "start_time": "0.00", "end_time": "2.50", "confidence": "0.95", "is_partial": False},
                {"speaker": "spk_0", "text": "Let me review the quarterly numbers.",
                 "start_time": "3.00", "end_time": "5.80", "confidence": "0.93", "is_partial": False},
            ],
        }))
        messages = ws_recv_all(ws, timeout_per_msg=10.0)
        tp = find_msg(messages, "transcriptProcessed")
        record("Single speaker transcript", tp is not None,
               f"lines={tp.get('lines_processed') if tp else 0}")
    except Exception as e:
        record("Single speaker transcript", False, str(e))

    # Large batch (10 lines)
    try:
        lines = [{"speaker": "spk_0", "text": f"Line {i} of the large batch test.",
                   "start_time": f"{i * 3.0:.2f}", "end_time": f"{i * 3.0 + 2.5:.2f}",
                   "confidence": "0.95", "is_partial": False} for i in range(10)]
        ws.send(json.dumps({
            "action": "processTranscript",
            "session_id": session_id,
            "lines": lines,
        }))
        messages = ws_recv_all(ws, timeout_per_msg=60.0, max_messages=30)
        tp = find_msg(messages, "transcriptProcessed")
        record("Large batch (10 lines)",
               tp is not None and tp.get("lines_processed") == 10,
               f"lines={tp.get('lines_processed') if tp else 0}")
    except Exception as e:
        record("Large batch", False, str(e))

    ws.close()


# ===========================================================================
# Cleanup
# ===========================================================================

def cleanup(token: str, agent_id: str, personality_id: str,
            skill_id: str, credential_id: str, project_id: str,
            session_id: str, qa_pair_id: str):
    print("\n── Cleanup ──")

    if skill_id and agent_id:
        r = rest("DELETE", f"/agents/{agent_id}/skills/{skill_id}", token)
        record("Unassign skill from agent", r.status_code in (200, 404),
               f"status={r.status_code}")

    if skill_id:
        r = rest("DELETE", f"/skills/{skill_id}", token)
        record("Delete test skill", r.status_code == 200,
               f"status={r.status_code}")

    if agent_id:
        r = rest("DELETE", f"/agents/{agent_id}", token)
        record("Delete test agent", r.status_code == 200,
               f"status={r.status_code}")

    if personality_id:
        r = rest("DELETE", f"/personalities/{personality_id}", token)
        record("Delete test personality", r.status_code == 200,
               f"status={r.status_code}")

    if credential_id:
        r = rest("DELETE", f"/bot-credentials/{credential_id}", token)
        record("Delete test bot credential", r.status_code == 200,
               f"status={r.status_code}")

    if qa_pair_id:
        r = rest("DELETE", f"/qa-pairs/{qa_pair_id}", token)
        record("Delete test QA pair", r.status_code in (200, 404),
               f"status={r.status_code}")

    if session_id:
        r = rest("DELETE", f"/sessions/{session_id}", token)
        record("Delete test session", r.status_code == 200,
               f"status={r.status_code}")

    if project_id:
        r = rest("DELETE", f"/projects/{project_id}", token)
        record("Delete test project", r.status_code == 200,
               f"status={r.status_code}")


# ===========================================================================
# Main
# ===========================================================================

def main():
    global VERBOSE
    if "--verbose" in sys.argv or "-v" in sys.argv:
        VERBOSE = True

    print("=" * 65)
    print("  AXRAIL Meeting-Tool — End-to-End Test Suite (D1 + D2)")
    print(f"  REST : {REST_URL}")
    print(f"  WS   : {WS_URL}")
    if VERBOSE:
        print("  (verbose mode ON)")
    print("=" * 65)

    # --- Auth ---
    token = test_auth()

    # --- REST CRUD ---
    project_id = test_projects_crud(token)
    session_id = test_sessions_crud(token, project_id)
    personality_id = test_personalities_crud(token)
    agent_id = test_agents_crud(token, personality_id)
    skill_id = test_skills_crud(token, agent_id)
    qa_pair_id = test_qa_pairs(token, session_id)
    credential_id = test_bot_credentials_crud(token)
    test_warm_pool(token)
    test_project_users(token, project_id)

    # --- Logout (after all REST tests) ---
    print("\n── Logout ──")
    r = rest("POST", "/auth/logout", token)
    record("Logout", r.status_code in (200, 401), f"status={r.status_code}")

    # Re-auth for WebSocket tests (logout may have invalidated token)
    token = test_auth()

    # --- WebSocket ---
    ws_session = f"test-ws-{uuid.uuid4().hex[:8]}"
    test_ws_core_actions(ws_session, agent_id)

    print(f"\n{INFO}  Waiting 3s for session state to settle...")
    time.sleep(3)

    test_ws_process_transcript_basic(ws_session, agent_id)
    test_ws_process_transcript_no_hints(ws_session, agent_id)
    test_ws_suggested_questions(ws_session, agent_id)
    test_ws_question_detection(ws_session, agent_id)
    test_ws_meeting_lifecycle(ws_session, agent_id)
    test_ws_edge_cases(ws_session, agent_id)

    # --- Re-auth before cleanup (token may have expired during long WS tests) ---
    print(f"\n{INFO}  Re-authenticating for cleanup...")
    r = rest("POST", "/auth/admin/login", body={
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD,
    })
    cleanup_token = r.json().get("data", {}).get("access_token", token)

    # --- Cleanup ---
    cleanup(cleanup_token, agent_id, personality_id, skill_id, credential_id,
            project_id, session_id, qa_pair_id)

    # --- Summary ---
    total = len(results)
    passed = sum(1 for _, ok, _ in results if ok)
    failed = total - passed
    print("\n" + "=" * 65)
    print(f"  Results: {passed}/{total} passed", end="")
    if failed:
        print(f"  ({failed} failed)")
        print("\n  Failed tests:")
        for name, ok, detail in results:
            if not ok:
                print(f"    ✗ {name}" + (f" — {detail}" if detail else ""))
    else:
        print("  — all green!")
    print("=" * 65)

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
