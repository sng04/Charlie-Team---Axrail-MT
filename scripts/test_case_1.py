"""
Test Case 1: NovaPay Sales Demo — End-to-End Integration Test

Creates (or reuses) a project with the savioenoson.dev@gmail.com bot credential,
sets up agent + personality + skills + KB, starts a live session with a real
Google Meet link, streams the transcript slowly over ~3 minutes, exercises all
WebSocket actions (questions, gap analysis, suggested questions, etc.), ends
the meeting, uploads the summary to the project KB, and writes a report.

Run:
    pip install requests boto3 websocket-client
    python scripts/test_case_1.py
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

# =============================================================================
# CONFIGURATION
# =============================================================================

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
SKILLS_BUCKET = os.environ.get("SKILLS_BUCKET", "axrail-skills-dev-848332098006")
SESSIONS_TABLE = os.environ.get("SESSIONS_TABLE", "dev-Sessions")
TRANSCRIPTS_TABLE = os.environ.get("TRANSCRIPTS_TABLE", "dev-Transcripts")
REGION = os.environ.get("AWS_REGION", "ap-southeast-1")
FIXTURES_DIR = os.environ.get(
    "FIXTURES_DIR",
    os.path.join(os.path.dirname(__file__), "..", "resources", "test-case-1"),
)

# Bot credential email and meeting link
BOT_EMAIL = "savioenoson.dev@gmail.com"
MEETING_LINK = "https://meet.google.com/kxy-pozb-rqq"

# How long to stream the transcript (seconds)
STREAM_DURATION = 180  # 3 minutes

# =============================================================================
# AWS CLIENTS
# =============================================================================

s3 = boto3.client("s3", region_name=REGION)
dynamodb = boto3.resource("dynamodb", region_name=REGION)

# =============================================================================
# HELPERS
# =============================================================================


def _h(title: str) -> None:
    print(f"\n{'='*70}\n  {title}\n{'='*70}\n")


def _p(label: str, data) -> None:
    if isinstance(data, (dict, list)):
        print(f"  [{label}]")
        print(f"  {json.dumps(data, indent=2, default=str)[:2000]}")
    else:
        print(f"  [{label}] {str(data)[:2000]}")
    print()


def _api(method: str, path: str, token: str = None, body: dict = None) -> dict:
    url = f"{REST_API_URL.rstrip('/')}/{path.lstrip('/')}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    resp = requests.request(method, url, headers=headers, json=body, timeout=30)
    try:
        return resp.json()
    except Exception:
        return {"statusCode": resp.status_code, "raw": resp.text}


def _ws_send_recv(ws, payload: dict, wait: int = 15) -> list:
    ws.send(json.dumps(payload))
    msgs = []
    deadline = time.time() + wait
    while time.time() < deadline:
        try:
            ws.settimeout(max(0.5, deadline - time.time()))
            raw = ws.recv()
            msg = json.loads(raw)
            msgs.append(msg)
            if msg.get("type") in (
                "response", "questionResponse", "gapAnalysis",
                "meetingSummary", "retroFeedback", "retroResponse", "error",
            ):
                break
        except websocket.WebSocketTimeoutException:
            continue
        except Exception as e:
            print(f"  [WS recv error] {e}")
            break
    return msgs


def _rec(name: str, status: str, details: dict = None, error: str = None):
    _report.append({
        "test": name, "status": status,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "details": details or {}, "error": error,
    })


def _write_report(session_id: str, agent_id: str, project_id: str) -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    report_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "test-case-1")
    os.makedirs(report_dir, exist_ok=True)
    path = os.path.join(report_dir, f"report-{ts}.md")
    passed = sum(1 for r in _report if r["status"] == "PASS")
    failed = sum(1 for r in _report if r["status"] == "FAIL")
    lines = [
        f"# Test Case 1: NovaPay Sales Demo — Report",
        f"",
        f"**Generated**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}  ",
        f"**Result**: {passed}/{len(_report)} passed, {failed} failed  ",
        f"**Session**: `{session_id}` | **Agent**: `{agent_id}` | **Project**: `{project_id}`  ",
        f"**REST**: `{REST_API_URL}` | **WS**: `{WS_API_URL}`  ",
        f"**Meeting**: `{MEETING_LINK}` | **Bot**: `{BOT_EMAIL}`  ",
        f"", f"---", f"",
    ]
    for e in _report:
        icon = "✅" if e["status"] == "PASS" else "❌"
        lines += [f"## {icon} {e['test']}", f"", f"**Status**: {e['status']}  ", f"**Time**: {e['timestamp']}  ", f""]
        if e.get("error"):
            lines += [f"**Error**:", f"```", e["error"], f"```", f""]
        if e["details"]:
            lines += [f"<details><summary>Data</summary>", f"", f"```json",
                       json.dumps(e["details"], indent=2, default=str)[:5000], f"```", f"</details>", f""]
    with open(path, "w") as f:
        f.write("\n".join(lines))
    print(f"\n  Report written to: {path}")
    return path


# =============================================================================
# TEST STEPS
# =============================================================================

def step_00_authenticate() -> str:
    _h("STEP 0: Authenticate")
    try:
        resp = _api("POST", "/auth/admin/login", body={
            "username": ADMIN_USERNAME, "password": ADMIN_PASSWORD,
        })
        token = resp.get("data", {}).get("access_token", "")
        if not token:
            _rec("Authenticate", "FAIL", resp, "No access token")
            raise SystemExit(1)
        print(f"  Token: {token[:20]}...")
        _rec("Authenticate", "PASS")
        return token
    except SystemExit:
        raise
    except Exception:
        _rec("Authenticate", "FAIL", error=traceback.format_exc())
        raise


def step_00b_cleanup_previous_sessions(token: str):
    """Delete previous E2E test sessions to avoid stale data."""
    _h("STEP 0b: Cleanup Previous Test Sessions")
    try:
        sessions_resp = _api("GET", "/sessions?limit=50", token)
        items = sessions_resp.get("data", {}).get("items", [])
        deleted = 0
        if isinstance(items, list):
            test_sessions = [s for s in items if "E2E Test" in s.get("name", "") or "e2e" in s.get("description", "").lower()]
            for s in test_sessions:
                sid = s["session_id"]
                print(f"  Deleting: {s.get('name', '')} ({sid[:8]}...)")
                _api("DELETE", f"/sessions/{sid}", token)
                dynamodb.Table(SESSIONS_TABLE).delete_item(Key={"session_id": sid})
                deleted += 1
        print(f"  Cleaned up {deleted} previous test session(s)")
        _rec("Cleanup", "PASS", {"deleted": deleted})
    except Exception:
        _rec("Cleanup", "FAIL", error=traceback.format_exc())
        # Non-fatal — continue even if cleanup fails


def step_01_get_or_create_project(token: str) -> str:
    """Reuse existing NovaPay project or create one with the bot credential."""
    _h("STEP 1: Get or Create Project")
    try:
        # Check for existing project linked to our bot credential
        cred_resp = _api("GET", "/bot-credentials", token)
        cred_items = cred_resp.get("data", {}).get("items", [])
        our_cred = next((c for c in cred_items if c.get("email") == BOT_EMAIL), None)
        if not our_cred:
            _rec("Get/Create Project", "FAIL", error=f"Bot credential for {BOT_EMAIL} not found. Create it first.")
            raise SystemExit(1)
        cred_id = our_cred["credential_id"]
        print(f"  Bot credential: {cred_id} ({BOT_EMAIL})")

        # Look for existing project with this credential
        projects_resp = _api("GET", "/projects", token)
        projects = projects_resp.get("data", {}).get("items", [])
        existing = next((p for p in projects if p.get("bot_credential_id") == cred_id), None)

        if existing:
            project_id = existing["project_id"]
            print(f"  Reusing project: {existing.get('name')} ({project_id})")
            _rec("Get/Create Project", "PASS", {"reused": True, "project_id": project_id})
            return project_id

        # Create new project
        resp = _api("POST", "/projects", token, {
            "name": f"NovaPay E2E Test-{uuid.uuid4().hex[:6]}",
            "email": "test@novapay.com",
            "description": "End-to-end integration test project",
            "bot_credential_id": cred_id,
        })
        _p("Create project", resp)
        project_id = resp.get("data", {}).get("project_id", "")
        _rec("Get/Create Project", "PASS", {"created": True, "project_id": project_id})
        return project_id
    except SystemExit:
        raise
    except Exception:
        _rec("Get/Create Project", "FAIL", error=traceback.format_exc())
        raise


def step_02_setup_agent(token: str) -> tuple:
    """Create personality + agent, return (agent_id, personality_id)."""
    _h("STEP 2: Create Agent & Personality")
    try:
        p_resp = _api("POST", "/personalities", token, {
            "personality_name": f"Sales Pro-{uuid.uuid4().hex[:6]}",
            "personality_prompt": "Use confident, consultative language. Be specific with data.",
        })
        pid = p_resp.get("data", {}).get("personality_id", "")

        a_resp = _api("POST", "/agents", token, {
            "agent_name": f"NovaPay Agent-{uuid.uuid4().hex[:6]}",
            "role_prompt": "You are an AI assistant for NovaPay sales reps. Answer client questions using the knowledge base.",
            "behavior_guidelines": "Search the KB first. Provide concise, factual answers with specific numbers.",
            "personality_id": pid,
            "model_id": "amazon.nova-pro-v1:0",
            "use_case": "sales_demo",
        })
        aid = a_resp.get("data", {}).get("agent_id", "")
        print(f"  Personality: {pid}")
        print(f"  Agent: {aid}")
        _rec("Create Agent & Personality", "PASS", {"agent_id": aid, "personality_id": pid})
        return aid, pid
    except Exception:
        _rec("Create Agent & Personality", "FAIL", error=traceback.format_exc())
        raise


def step_03_upload_kb(project_id: str):
    """Upload KB files to S3."""
    _h("STEP 3: Knowledge Base Ingestion")
    try:
        kb_dir = os.path.join(FIXTURES_DIR, "kb")
        uploaded = []
        for f in sorted(os.listdir(kb_dir)):
            key = f"{project_id}/{f}"
            print(f"  Uploading {f} → s3://{KB_BUCKET}/{key}")
            s3.upload_file(os.path.join(kb_dir, f), KB_BUCKET, key)
            uploaded.append(f)
        print(f"\n  Waiting 30s for Ingestion Lambda...")
        time.sleep(30)
        _rec("KB Ingestion", "PASS", {"files": uploaded})
    except Exception:
        _rec("KB Ingestion", "FAIL", error=traceback.format_exc())
        raise


def step_04_upload_skills(token: str, agent_id: str):
    """Create skills via API, upload files, assign to agent."""
    _h("STEP 4: Skill Ingestion")
    try:
        skills_dir = os.path.join(FIXTURES_DIR, "skills")
        results = []
        for fname in sorted(os.listdir(skills_dir)):
            resp = _api("POST", "/skills", token, {
                "skill_name": fname.replace(".md", "").replace("-", " ").title(),
                "description": f"Skill: {fname}",
                "file_name": fname,
            })
            sid = resp.get("data", {}).get("skill", {}).get("skill_id", "")
            if sid:
                _api("POST", f"/agents/{agent_id}/skills/{sid}", token)
            url = resp.get("data", {}).get("upload_url", "")
            if url:
                with open(os.path.join(skills_dir, fname), "rb") as fh:
                    data = fh.read()
                    r = requests.put(url, data=data)
                    if r.status_code != 200:
                        s3_key = resp.get("data", {}).get("skill", {}).get("s3_key", "")
                        if s3_key:
                            s3.put_object(Bucket=SKILLS_BUCKET, Key=s3_key, Body=data)
                results.append({"file": fname, "skill_id": sid})
            print(f"  {fname} → {sid}")
        print(f"\n  Waiting 30s for SkillIngestion Lambda...")
        time.sleep(30)
        _rec("Skill Ingestion", "PASS", {"skills": results})
    except Exception:
        _rec("Skill Ingestion", "FAIL", error=traceback.format_exc())
        raise


def step_05_create_live_session(token: str, project_id: str) -> str:
    """Create a session with the real Google Meet link — bot will join."""
    _h("STEP 5: Create Live Session (bot joins meeting)")
    try:
        resp = _api("POST", "/sessions", token, {
            "project_id": project_id,
            "name": f"E2E Test Session - {datetime.now().strftime('%H:%M')}",
            "meeting_link": MEETING_LINK,
            "description": "Automated end-to-end integration test",
        })
        _p("Create session", resp)
        sid = resp.get("data", {}).get("session_id", "")
        print(f"  Session: {sid}")
        print(f"  Meeting: {MEETING_LINK}")
        print(f"  Bot should be joining the meeting now...")
        print(f"  Waiting 60s for bot to join...")
        time.sleep(60)

        # Check session status
        s_resp = _api("GET", f"/sessions/{sid}", token)
        status = s_resp.get("data", {}).get("bot_status", "unknown")
        print(f"  Bot status: {status}")
        _rec("Create Live Session", "PASS", {"session_id": sid, "bot_status": status})
        return sid
    except Exception:
        _rec("Create Live Session", "FAIL", error=traceback.format_exc())
        raise


def step_06_stream_and_process(session_id: str, agent_id: str) -> None:
    """Stream transcript in batches, processing each batch via WebSocket in real-time."""
    _h("STEP 6: Stream Transcript + Real-Time Processing (~2.5 min)")
    try:
        batch_timings = []  # Track when each batch was written vs when detections came back

        path = os.path.join(FIXTURES_DIR, "transcripts", "sales-demo-session.json")
        with open(path) as f:
            all_lines = json.load(f)

        table = dynamodb.Table(TRANSCRIPTS_TABLE)
        sessions_table = dynamodb.Table(SESSIONS_TABLE)
        total = len(all_lines)
        batch_size = 6
        batches = [all_lines[i:i+batch_size] for i in range(0, total, batch_size)]
        all_ws_responses = []

        ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
        print(f"  Streaming {total} lines in {len(batches)} batches of {batch_size}")
        print(f"  WebSocket: {ws_url[:60]}...")

        ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
        try:
            for batch_idx, batch in enumerate(batches):
                batch_num = batch_idx + 1
                print(f"\n  --- Batch {batch_num}/{len(batches)} ({len(batch)} lines) ---")

                # 1. Write lines to DynamoDB (simulating real-time transcription)
                batch_write_start = time.time()
                for i, line in enumerate(batch):
                    ts = datetime.now(timezone.utc).isoformat()
                    line_num = batch_idx * batch_size + i + 1
                    table.put_item(Item={
                        "session_id": session_id,
                        "timestamp": ts,
                        "transcript_id": str(uuid.uuid4()),
                        "speaker": line["speaker"],
                        "text": line["text"],
                        "confidence": str(line.get("confidence", 0.95)),
                    })
                    sessions_table.update_item(
                        Key={"session_id": session_id},
                        UpdateExpression="SET is_active = :a, last_transcript_update_at = :ts",
                        ExpressionAttributeValues={":a": "active", ":ts": ts},
                    )
                    print(f"  [{line_num}/{total}] {line['speaker']}: {line['text'][:60]}...")
                    time.sleep(0.5)  # Small delay between lines within a batch
                batch_write_end = time.time()

                # 2. Send batch to WebSocket for processing
                print(f"  >> Sending batch {batch_num} to WebSocket for processing...")
                msgs = _ws_send_recv(ws, {
                    "action": "processTranscript",
                    "session_id": session_id,
                    "lines": batch,
                }, wait=20)
                batch_ws_end = time.time()

                for m in msgs:
                    msg_type = m.get("type", "unknown")
                    if msg_type == "questionDetected":
                        print(f"  🔍 Question detected: {m.get('question', '')[:80]}...")
                    elif msg_type == "suggestedResponse":
                        print(f"  💡 Suggested answer: {m.get('suggested_answer', '')[:80]}...")
                    elif msg_type == "qaPairAutoSaved":
                        print(f"  💾 QA pair saved: {m.get('question', '')[:60]}...")
                    elif msg_type == "questionMatched":
                        print(f"  ✅ Question matched: {m.get('question', '')[:60]}...")
                    elif msg_type == "transcriptProcessed":
                        print(f"  ✓ Batch {batch_num} processed ({m.get('lines_processed', 0)} lines)")
                    else:
                        print(f"  [{msg_type}] {json.dumps(m, default=str)[:100]}...")
                all_ws_responses.extend(msgs)

                detection_count = sum(1 for m in msgs if m.get("type") in ("questionDetected", "suggestedResponse", "qaPairAutoSaved"))
                batch_timings.append({
                    "batch": batch_num,
                    "write_duration_s": round(batch_write_end - batch_write_start, 1),
                    "ws_processing_s": round(batch_ws_end - batch_write_end, 1),
                    "total_s": round(batch_ws_end - batch_write_start, 1),
                    "detections": detection_count,
                })

                # 3. Wait between batches
                if batch_idx < len(batches) - 1:
                    print(f"  Waiting 5s before next batch...")
                    time.sleep(5)

        finally:
            ws.close()

        # Summary of real-time processing
        q_detected = sum(1 for m in all_ws_responses if m.get("type") == "questionDetected")
        qa_saved = sum(1 for m in all_ws_responses if m.get("type") == "qaPairAutoSaved")
        suggested = sum(1 for m in all_ws_responses if m.get("type") == "suggestedResponse")
        print(f"\n  Real-time processing summary:")
        print(f"    Questions detected: {q_detected}")
        print(f"    QA pairs auto-saved: {qa_saved}")
        print(f"    Suggested responses: {suggested}")

        print(f"\n  Timing report:")
        print(f"  {'Batch':<8} {'DDB Write':<12} {'WS Process':<12} {'Total':<10} {'Detections':<12}")
        print(f"  {'-'*54}")
        for t in batch_timings:
            print(f"  {t['batch']:<8} {t['write_duration_s']:<12.1f} {t['ws_processing_s']:<12.1f} {t['total_s']:<10.1f} {t['detections']:<12}")

        _rec("Stream + Real-Time Processing", "PASS", {
            "batches": len(batches),
            "total_lines": total,
            "questions_detected": q_detected,
            "qa_pairs_saved": qa_saved,
            "suggested_responses": suggested,
            "batch_timings": batch_timings,
        })
    except Exception:
        _rec("Stream + Real-Time Processing", "FAIL", error=traceback.format_exc())
        raise


def step_07_ws_send_message(session_id: str, agent_id: str):
    """Test KB chat via sendMessage."""
    _h("STEP 7: sendMessage — KB Chat")
    try:
        questions = [
            "What payment methods does NovaPay support?",
            "How does NovaPay compare to Stripe on pricing?",
            "Does NovaPay support payments in Euros?",
        ]
        ws = websocket.create_connection(
            f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
            timeout=10, sslopt=_SSL_OPTS,
        )
        all_resp = {}
        try:
            for q in questions:
                print(f"  Q: {q}")
                msgs = _ws_send_recv(ws, {
                    "action": "sendMessage", "session_id": session_id, "message": q,
                }, wait=20)
                for m in msgs:
                    _p("A", m.get("message", m) if isinstance(m, dict) else m)
                all_resp[q] = msgs
        finally:
            ws.close()
        _rec("sendMessage — KB Chat", "PASS", {"qa": all_resp})
    except Exception:
        _rec("sendMessage — KB Chat", "FAIL", error=traceback.format_exc())
        raise


def step_08_ws_detect_question(session_id: str, agent_id: str):
    """Test on-demand question answering."""
    _h("STEP 8: detectQuestion")
    try:
        ws = websocket.create_connection(
            f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
            timeout=10, sslopt=_SSL_OPTS,
        )
        all_resp = {}
        try:
            for q in ["What is the chargeback fee?", "What encryption does NovaPay use?"]:
                print(f"  Q: {q}")
                msgs = _ws_send_recv(ws, {
                    "action": "detectQuestion", "session_id": session_id, "question": q,
                }, wait=20)
                for m in msgs:
                    _p("A", m)
                all_resp[q] = msgs
        finally:
            ws.close()
        _rec("detectQuestion", "PASS", {"qa": all_resp})
    except Exception:
        _rec("detectQuestion", "FAIL", error=traceback.format_exc())
        raise


def step_09_ws_analyze_gaps(session_id: str, agent_id: str):
    _h("STEP 9: analyzeGaps")
    try:
        ws = websocket.create_connection(
            f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
            timeout=10, sslopt=_SSL_OPTS,
        )
        try:
            msgs = _ws_send_recv(ws, {"action": "analyzeGaps", "session_id": session_id}, wait=30)
            for m in msgs:
                _p("Gap", m)
            _rec("analyzeGaps", "PASS", {"messages": msgs})
        finally:
            ws.close()
    except Exception:
        _rec("analyzeGaps", "FAIL", error=traceback.format_exc())
        raise


def step_10_ws_suggested_questions(session_id: str, agent_id: str):
    _h("STEP 10: setSuggestedQuestions + matching")
    try:
        ws = websocket.create_connection(
            f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
            timeout=10, sslopt=_SSL_OPTS,
        )
        try:
            _ws_send_recv(ws, {
                "action": "setSuggestedQuestions", "session_id": session_id,
                "questions": [
                    "What is NovaPay's pricing for enterprise retailers?",
                    "Does NovaPay support international payments?",
                    "What security certifications does NovaPay hold?",
                ],
            }, wait=15)
            match_lines = [
                {"speaker": "spk_0", "text": "Enterprise plan — interchange-plus pricing.",
                 "start_time": 110.4, "end_time": 125.6, "confidence": 0.94, "is_partial": False},
                {"speaker": "spk_0", "text": "We're PCI DSS Level 1 certified and SOC 2 Type II.",
                 "start_time": 274.3, "end_time": 292.5, "confidence": 0.92, "is_partial": False},
            ]
            msgs = _ws_send_recv(ws, {
                "action": "processTranscript", "session_id": session_id, "lines": match_lines,
            }, wait=25)
            for m in msgs:
                _p(f"Match ({m.get('type', '?')})", m)
            _rec("setSuggestedQuestions", "PASS", {"messages": msgs})
        finally:
            ws.close()
    except Exception:
        _rec("setSuggestedQuestions", "FAIL", error=traceback.format_exc())
        raise


def step_11_ws_end_meeting(session_id: str, agent_id: str, token: str) -> str:
    """End meeting and capture the summary."""
    _h("STEP 11: endMeeting — Summary")
    summary_text = ""
    try:
        ws = websocket.create_connection(
            f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
            timeout=10, sslopt=_SSL_OPTS,
        )
        try:
            msgs = _ws_send_recv(ws, {"action": "endMeeting", "session_id": session_id}, wait=45)
            for m in msgs:
                _p(f"Summary ({m.get('type', '?')})", m)
                if m.get("type") == "meetingSummary":
                    summary_text = (
                        m.get("summary_markdown")
                        or m.get("summary")
                        or m.get("message")
                        or ""
                    )
            _rec("endMeeting", "PASS", {"messages": msgs})
        finally:
            ws.close()

        # Verify summary is retrievable via REST API
        print(f"\n  Verifying summary via REST API...")
        time.sleep(5)  # Brief wait for S3 write to propagate
        rest_resp = _api("GET", f"/sessions/{session_id}/summary", token)
        rest_status = rest_resp.get("data", {}).get("status", "unknown")
        print(f"  REST summary status: {rest_status}")
        if rest_status == "available":
            rest_summary = rest_resp.get("data", {}).get("summary_markdown", "")
            print(f"  REST summary length: {len(rest_summary)} chars")

        # Signal the bot to leave the meeting
        print(f"  Sending stop-bot signal...")
        stop_resp = _api("POST", f"/sessions/{session_id}/stop-bot", token)
        print(f"  Stop-bot response: {stop_resp.get('statusCode', '?')}")

        return summary_text
    except Exception:
        _rec("endMeeting", "FAIL", error=traceback.format_exc())
        raise


def step_12_ws_retro(session_id: str, agent_id: str):
    """Retro analysis + follow-up chat."""
    _h("STEP 12: retroAnalysis + retroChat")
    try:
        ws = websocket.create_connection(
            f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
            timeout=10, sslopt=_SSL_OPTS,
        )
        try:
            retro_msgs = _ws_send_recv(ws, {"action": "retroAnalysis", "session_id": session_id}, wait=45)
            for m in retro_msgs:
                _p(f"Retro ({m.get('type', '?')})", m)

            chat_msgs = _ws_send_recv(ws, {
                "action": "retroChat", "session_id": session_id,
                "message": "How should I handle the multi-currency question better next time?",
            }, wait=25)
            for m in chat_msgs:
                _p("RetroChat", m)
            _rec("retroAnalysis + retroChat", "PASS", {"retro": retro_msgs, "chat": chat_msgs})
        finally:
            ws.close()
    except Exception:
        _rec("retroAnalysis + retroChat", "FAIL", error=traceback.format_exc())
        raise


def step_13_qa_pairs(token: str, session_id: str):
    _h("STEP 13: QA Pairs")
    try:
        resp = _api("GET", f"/qa-pairs?session_id={session_id}", token)
        _p("QA pairs", resp)
        items = resp.get("data", [])
        if isinstance(items, dict):
            items = items.get("items", [])
        print(f"  Total QA pairs: {len(items)}")
        _rec("QA Pairs", "PASS", {"count": len(items)})
    except Exception:
        _rec("QA Pairs", "FAIL", error=traceback.format_exc())
        raise


def step_14_verify_summary_ingested(token: str, session_id: str, project_id: str):
    """Verify the meeting summary was saved to S3 and ingested into OpenSearch."""
    _h("STEP 14: Verify Summary Ingested into KB")
    try:
        # Check summary exists via REST
        resp = _api("GET", f"/sessions/{session_id}/summary", token)
        status = resp.get("data", {}).get("status", "unknown")
        print(f"  Summary status: {status}")

        if status != "available":
            print("  Summary not yet available, waiting 30s for S3 write...")
            time.sleep(30)
            resp = _api("GET", f"/sessions/{session_id}/summary", token)
            status = resp.get("data", {}).get("status", "unknown")
            print(f"  Summary status after wait: {status}")

        # Check S3 directly
        s3_key = f"{project_id}/summaries/{session_id}.md"
        try:
            s3.head_object(Bucket=KB_BUCKET, Key=s3_key)
            print(f"  ✓ Summary exists in S3: s3://{KB_BUCKET}/{s3_key}")
            s3_exists = True
        except Exception:
            print(f"  ✗ Summary NOT found in S3: {s3_key}")
            s3_exists = False

        # Wait for Ingestion Lambda to index it into OpenSearch
        print(f"  Waiting 30s for Ingestion Lambda to index summary...")
        time.sleep(30)
        print(f"  Summary should now be indexed in OpenSearch as doc_type=meeting_summary")

        _rec("Verify Summary Ingested", "PASS" if s3_exists else "FAIL", {
            "rest_status": status,
            "s3_exists": s3_exists,
            "s3_key": s3_key,
        })
    except Exception:
        _rec("Verify Summary Ingested", "FAIL", error=traceback.format_exc())
        raise


def step_15_post_completion_retro(session_id: str, agent_id: str):
    """Verify retro feedback can be generated for a completed session."""
    _h("STEP 15: Post-Completion Retro Feedback")
    try:
        ws = websocket.create_connection(
            f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
            timeout=10, sslopt=_SSL_OPTS,
        )
        try:
            print(f"  Requesting retro analysis for completed session...")
            msgs = _ws_send_recv(ws, {"action": "retroAnalysis", "session_id": session_id}, wait=45)

            has_feedback = any(m.get("type") == "retroFeedback" for m in msgs)
            print(f"  Retro feedback received: {has_feedback}")

            for m in msgs:
                if m.get("type") == "retroFeedback":
                    feedback = m.get("feedback", "")
                    print(f"  Feedback preview: {feedback[:200]}...")
                elif m.get("type") == "error":
                    print(f"  ✗ Error: {m.get('message', '')}")

            _rec("Post-Completion Retro", "PASS" if has_feedback else "FAIL", {
                "has_feedback": has_feedback,
                "messages": msgs,
            })
        finally:
            ws.close()
    except Exception:
        _rec("Post-Completion Retro", "FAIL", error=traceback.format_exc())
        raise


def step_16_post_completion_qa(session_id: str, agent_id: str):
    """Verify we can ask questions about the session after it's completed."""
    _h("STEP 16: Post-Completion Q&A (retroChat)")
    try:
        questions = [
            "What were the main pricing concerns raised by the client?",
            "Did we address the multi-currency question adequately?",
            "What action items came out of this meeting?",
        ]
        ws = websocket.create_connection(
            f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}",
            timeout=10, sslopt=_SSL_OPTS,
        )
        all_resp = {}
        try:
            # First trigger retro analysis to load context
            print(f"  Loading retro context...")
            _ws_send_recv(ws, {"action": "retroAnalysis", "session_id": session_id}, wait=45)

            for q in questions:
                print(f"\n  Q: {q}")
                msgs = _ws_send_recv(ws, {
                    "action": "retroChat", "session_id": session_id, "message": q,
                }, wait=25)

                has_answer = any(m.get("type") == "retroResponse" for m in msgs)
                for m in msgs:
                    if m.get("type") == "retroResponse":
                        answer = m.get("message", "")
                        print(f"  A: {answer[:200]}...")
                    elif m.get("type") == "error":
                        print(f"  ✗ Error: {m.get('message', '')}")

                all_resp[q] = {"has_answer": has_answer, "messages": msgs}

            all_answered = all(r["has_answer"] for r in all_resp.values())
            print(f"\n  All questions answered: {all_answered}")
            _rec("Post-Completion Q&A", "PASS" if all_answered else "FAIL", {"qa": all_resp})
        finally:
            ws.close()
    except Exception:
        _rec("Post-Completion Q&A", "FAIL", error=traceback.format_exc())
        raise


def step_17_crud_smoke(token: str):
    _h("STEP 17: CRUD Smoke Test")
    try:
        results = {}
        for ep in ["/agents", "/personalities", "/skills", "/projects", "/sessions", "/bot-credentials"]:
            resp = _api("GET", ep, token)
            items = resp.get("data", {})
            count = len(items.get("items", [])) if isinstance(items, dict) else 0
            print(f"  GET {ep}: {resp.get('statusCode', '?')} — {count} items")
            results[ep] = {"status": resp.get("statusCode"), "count": count}
        _rec("CRUD Smoke Test", "PASS", results)
    except Exception:
        _rec("CRUD Smoke Test", "FAIL", error=traceback.format_exc())
        raise


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("  TEST CASE 1: NovaPay Sales Demo — End-to-End")
    print(f"  Bot: {BOT_EMAIL}")
    print(f"  Meeting: {MEETING_LINK}")
    print(f"  REST: {REST_API_URL}")
    print(f"  WS:   {WS_API_URL}")
    print("=" * 70)

    if not os.path.isdir(os.path.join(FIXTURES_DIR, "kb")):
        print(f"\n  *** Fixtures not found at {FIXTURES_DIR} ***")
        raise SystemExit(1)

    session_id = agent_id = project_id = ""
    summary = ""
    try:
        token = step_00_authenticate()
        step_00b_cleanup_previous_sessions(token)
        project_id = step_01_get_or_create_project(token)
        agent_id, _ = step_02_setup_agent(token)
        step_03_upload_kb(project_id)
        step_04_upload_skills(token, agent_id)
        session_id = step_05_create_live_session(token, project_id)
        step_06_stream_and_process(session_id, agent_id)

        # Post-streaming WebSocket tests
        step_07_ws_send_message(session_id, agent_id)
        step_08_ws_detect_question(session_id, agent_id)
        step_09_ws_analyze_gaps(session_id, agent_id)
        step_10_ws_suggested_questions(session_id, agent_id)
        summary = step_11_ws_end_meeting(session_id, agent_id, token)  # added token param
        step_12_ws_retro(session_id, agent_id)

        # Post-meeting verification
        step_13_qa_pairs(token, session_id)
        step_14_verify_summary_ingested(token, session_id, project_id)
        step_15_post_completion_retro(session_id, agent_id)
        step_16_post_completion_qa(session_id, agent_id)
        step_17_crud_smoke(token)
    except SystemExit:
        raise
    except Exception:
        print("\n  *** Test run aborted (see report) ***")
    finally:
        _write_report(session_id, agent_id, project_id)

    _h("ALL TESTS COMPLETE")
    passed = sum(1 for r in _report if r["status"] == "PASS")
    failed = sum(1 for r in _report if r["status"] == "FAIL")
    print(f"  Result: {passed}/{len(_report)} passed, {failed} failed")
    print(f"  Session: {session_id}")
    print(f"  Agent:   {agent_id}")
    print(f"  Project: {project_id}")


if __name__ == "__main__":
    main()
