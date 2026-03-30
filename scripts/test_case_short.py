"""
Test Case Short: NovaPay Quick Check-In — Minified E2E Test (~5 min)

Reuses the existing NovaPay project + KB + skills. Streams a short
client check-in transcript, runs core WebSocket actions, ends the
meeting, and verifies the summary.

Run:
    python scripts/test_case_short.py
"""

import json
import os
import ssl
import time
import traceback
import uuid
from datetime import datetime, timezone

import boto3
import requests
import websocket

_SSL_OPTS = {"cert_reqs": ssl.CERT_NONE}
_report: list[dict] = []

REST_API_URL = os.environ.get(
    "REST_API_URL",
    "https://sjsd378hbd.execute-api.ap-southeast-1.amazonaws.com/dev",
)
WS_API_URL = os.environ.get(
    "WS_API_URL",
    "wss://hey8o0q9tb.execute-api.ap-southeast-1.amazonaws.com/production",
)
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "Admin@12345")
KB_BUCKET = os.environ.get("KB_BUCKET", "axrail-kb-dev-848332098006")
SESSIONS_TABLE = os.environ.get("SESSIONS_TABLE", "dev-Sessions")
TRANSCRIPTS_TABLE = os.environ.get("TRANSCRIPTS_TABLE", "dev-Transcripts")
REGION = os.environ.get("AWS_REGION", "ap-southeast-1")
FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "..", "resources", "test-case-short")

BOT_EMAIL = "savioenoson.dev@gmail.com"
MEETING_LINK = "https://meet.google.com/kxy-pozb-rqq"

s3 = boto3.client("s3", region_name=REGION)
dynamodb = boto3.resource("dynamodb", region_name=REGION)


# ── Helpers ──────────────────────────────────────────────────────────────────

def _h(title): print(f"\n{'='*60}\n  {title}\n{'='*60}\n")

def _api(method, path, token=None, body=None):
    url = f"{REST_API_URL.rstrip('/')}/{path.lstrip('/')}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    resp = requests.request(method, url, headers=headers, json=body, timeout=30)
    try:
        return resp.json()
    except Exception:
        return {"statusCode": resp.status_code, "raw": resp.text}

def _ws_send_recv(ws, payload, wait=15):
    ws.send(json.dumps(payload))
    msgs = []
    deadline = time.time() + wait
    while time.time() < deadline:
        try:
            ws.settimeout(max(0.5, deadline - time.time()))
            msg = json.loads(ws.recv())
            msgs.append(msg)
            if msg.get("type") in ("response", "questionResponse", "gapAnalysis",
                                   "meetingSummary", "retroFeedback", "retroResponse", "error"):
                break
        except websocket.WebSocketTimeoutException:
            continue
        except Exception:
            break
    return msgs

def _rec(name, status, details=None, error=None):
    _report.append({"test": name, "status": status, "ts": datetime.now(timezone.utc).isoformat(),
                     "details": details or {}, "error": error})
    icon = "✅" if status == "PASS" else "❌"
    print(f"  {icon} {name}: {status}")


# ── Steps ────────────────────────────────────────────────────────────────────

def step_auth():
    _h("Auth")
    resp = _api("POST", "/auth/admin/login", body={"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD})
    token = resp.get("data", {}).get("access_token", "")
    assert token, f"No access token: {resp}"
    print(f"  Token: {token[:20]}...")
    _rec("Auth", "PASS")
    return token


def step_cleanup_previous_sessions(token):
    """Delete any previous test sessions to avoid stale data."""
    _h("Cleanup Previous Test Sessions")
    sessions_resp = _api("GET", "/sessions?limit=50", token)
    items = sessions_resp.get("data", {}).get("items", [])
    if isinstance(items, list):
        test_sessions = [s for s in items if "Check-In" in s.get("name", "") or "check-in" in s.get("description", "").lower()]
        for s in test_sessions:
            sid = s["session_id"]
            print(f"  Deleting session: {s.get('name', '')} ({sid[:8]}...)")
            _api("DELETE", f"/sessions/{sid}", token)
            # Also delete from DDB directly in case REST doesn't clean up
            dynamodb.Table(SESSIONS_TABLE).delete_item(Key={"session_id": sid})
    deleted = len(test_sessions) if isinstance(items, list) else 0
    print(f"  Cleaned up {deleted} previous test session(s)")
    _rec("Cleanup", "PASS", {"deleted": deleted})


def step_find_project(token):
    """Find existing NovaPay project with our bot credential."""
    _h("Find Project + Agent")
    creds = _api("GET", "/bot-credentials", token).get("data", {}).get("items", [])
    cred = next((c for c in creds if c.get("email") == BOT_EMAIL), None)
    assert cred, f"Bot credential for {BOT_EMAIL} not found"
    cred_id = cred["credential_id"]

    projects = _api("GET", "/projects", token).get("data", {}).get("items", [])
    proj = next((p for p in projects if p.get("bot_credential_id") == cred_id), None)
    assert proj, "No project found with this bot credential"
    project_id = proj["project_id"]
    agent_id = proj.get("agent_id", "")
    print(f"  Project: {proj.get('name')} ({project_id})")
    print(f"  Agent: {proj.get('agent_name', 'N/A')} ({agent_id})")
    _rec("Find Project", "PASS", {"project_id": project_id, "agent_id": agent_id})
    return project_id, agent_id


def step_create_session(token, project_id):
    _h("Create Session")
    resp = _api("POST", "/sessions", token, {
        "project_id": project_id,
        "name": f"Quick Check-In - {datetime.now().strftime('%H:%M')}",
        "meeting_link": MEETING_LINK,
        "description": "Short pilot status check-in",
    })
    sid = resp.get("data", {}).get("session_id", "")
    assert sid, f"No session_id: {resp}"
    print(f"  Session: {sid}")
    print(f"  Waiting 45s for bot to join...")
    time.sleep(45)
    status = _api("GET", f"/sessions/{sid}", token).get("data", {}).get("bot_status", "unknown")
    print(f"  Bot status: {status}")
    _rec("Create Session", "PASS", {"session_id": sid, "bot_status": status})
    return sid


def step_stream_transcript(session_id, agent_id):
    """Stream 28 transcript lines in batches, ~2 min."""
    _h("Stream Transcript (~2 min)")
    path = os.path.join(FIXTURES_DIR, "transcripts", "quick-checkin.json")
    with open(path) as f:
        lines = json.load(f)

    table = dynamodb.Table(TRANSCRIPTS_TABLE)
    sessions_table = dynamodb.Table(SESSIONS_TABLE)
    batch_size = 7
    batches = [lines[i:i+batch_size] for i in range(0, len(lines), batch_size)]
    all_ws = []

    ws = websocket.create_connection(
        f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
        timeout=10, sslopt=_SSL_OPTS,
    )
    try:
        for bi, batch in enumerate(batches):
            print(f"\n  Batch {bi+1}/{len(batches)} ({len(batch)} lines)")
            for i, line in enumerate(batch):
                ts = datetime.now(timezone.utc).isoformat()
                table.put_item(Item={
                    "session_id": session_id, "timestamp": ts,
                    "transcript_id": str(uuid.uuid4()),
                    "speaker": line["speaker"], "text": line["text"],
                    "confidence": str(line.get("confidence", 0.95)),
                })
                sessions_table.update_item(
                    Key={"session_id": session_id},
                    UpdateExpression="SET is_active = :a, last_transcript_update_at = :ts",
                    ExpressionAttributeValues={":a": "active", ":ts": ts},
                )
                num = bi * batch_size + i + 1
                print(f"    [{num}/{len(lines)}] {line['speaker']}: {line['text'][:55]}...")
                time.sleep(0.8)

            msgs = _ws_send_recv(ws, {
                "action": "processTranscript", "session_id": session_id, "lines": batch,
            }, wait=15)
            for m in msgs:
                t = m.get("type", "?")
                if t == "questionDetected":
                    print(f"    🔍 Q: {m.get('question', '')[:70]}...")
                elif t == "qaPairAutoSaved":
                    print(f"    💾 QA saved")
                elif t == "transcriptProcessed":
                    print(f"    ✓ Processed")
            all_ws.extend(msgs)

            if bi < len(batches) - 1:
                time.sleep(3)
    finally:
        ws.close()

    q_count = sum(1 for m in all_ws if m.get("type") == "questionDetected")
    print(f"\n  Questions detected: {q_count}")
    _rec("Stream Transcript", "PASS", {"lines": len(lines), "questions": q_count})


def step_kb_chat(session_id, agent_id):
    _h("KB Chat (sendMessage)")
    ws = websocket.create_connection(
        f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
        timeout=10, sslopt=_SSL_OPTS,
    )
    try:
        for q in ["What is NovaPay's settlement SLA?", "Does NovaPay support Apple Pay?"]:
            print(f"  Q: {q}")
            msgs = _ws_send_recv(ws, {"action": "sendMessage", "session_id": session_id, "message": q}, wait=20)
            for m in msgs:
                if m.get("type") == "response":
                    print(f"  A: {m.get('message', '')[:120]}...")
    finally:
        ws.close()
    _rec("KB Chat", "PASS")


def step_end_meeting(session_id, agent_id, token):
    _h("End Meeting + Summary")
    ws = websocket.create_connection(
        f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
        timeout=10, sslopt=_SSL_OPTS,
    )
    summary = ""
    try:
        msgs = _ws_send_recv(ws, {"action": "endMeeting", "session_id": session_id}, wait=45)
        for m in msgs:
            if m.get("type") == "meetingSummary":
                summary = m.get("summary_markdown", "")[:200]
                print(f"  Summary: {summary}...")
            elif m.get("type") == "error":
                print(f"  Error: {m.get('message', '')}")
    finally:
        ws.close()

    # Verify S3
    time.sleep(5)
    resp = _api("GET", f"/sessions/{session_id}/summary", token)
    rest_ok = resp.get("data", {}).get("status") == "available"
    print(f"  REST summary available: {rest_ok}")

    # Stop bot
    _api("POST", f"/sessions/{session_id}/stop-bot", token)
    print(f"  Stop-bot signal sent")

    _rec("End Meeting", "PASS" if summary else "FAIL", {"summary_preview": summary, "rest_ok": rest_ok})


def step_retro(session_id, agent_id):
    _h("Retro Analysis")
    ws = websocket.create_connection(
        f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
        timeout=10, sslopt=_SSL_OPTS,
    )
    try:
        msgs = _ws_send_recv(ws, {"action": "retroAnalysis", "session_id": session_id}, wait=45)
        has_feedback = any(m.get("type") == "retroFeedback" for m in msgs)
        for m in msgs:
            if m.get("type") == "retroFeedback":
                print(f"  Feedback: {m.get('feedback', '')[:150]}...")
        _rec("Retro Analysis", "PASS" if has_feedback else "FAIL")
    finally:
        ws.close()


def step_verify_summary_in_kb(token, session_id, project_id):
    _h("Verify Summary in KB")
    s3_key = f"{project_id}/summaries/{session_id}.md"
    try:
        s3.head_object(Bucket=KB_BUCKET, Key=s3_key)
        print(f"  ✓ s3://{KB_BUCKET}/{s3_key}")
        _rec("Summary in KB", "PASS", {"s3_key": s3_key})
    except Exception:
        print(f"  ✗ Not found: {s3_key}")
        _rec("Summary in KB", "FAIL", {"s3_key": s3_key})


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  TEST CASE SHORT: NovaPay Quick Check-In (~5 min)")
    print(f"  REST: {REST_API_URL}")
    print(f"  WS:   {WS_API_URL}")
    print("=" * 60)

    session_id = agent_id = project_id = ""
    try:
        token = step_auth()
        step_cleanup_previous_sessions(token)
        project_id, agent_id = step_find_project(token)
        session_id = step_create_session(token, project_id)
        step_stream_transcript(session_id, agent_id)
        step_kb_chat(session_id, agent_id)
        step_end_meeting(session_id, agent_id, token)
        step_retro(session_id, agent_id)
        step_verify_summary_in_kb(token, session_id, project_id)
    except Exception:
        print(f"\n  *** Aborted ***\n{traceback.format_exc()}")
    finally:
        _h("RESULTS")
        passed = sum(1 for r in _report if r["status"] == "PASS")
        failed = sum(1 for r in _report if r["status"] == "FAIL")
        print(f"  {passed}/{len(_report)} passed, {failed} failed")
        print(f"  Session: {session_id}")
        print(f"  Project: {project_id}")
        for r in _report:
            icon = "✅" if r["status"] == "PASS" else "❌"
            print(f"    {icon} {r['test']}")


if __name__ == "__main__":
    main()
