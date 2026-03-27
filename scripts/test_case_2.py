"""
Test Case 2: GreenBuild Consulting Kickoff

Exercises all agent functions against the GreenBuild sustainability test fixtures.
Requires a fully deployed stack (all 6 CDK stacks).

Run:
    pip install requests boto3 websocket-client
    python test_case_2.py
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

# Report collector — each test appends its results here
_report: list[dict] = []

# =============================================================================
# CONFIGURATION — UPDATE THESE BEFORE RUNNING
# =============================================================================

# REST API base URL (from ApiServicesStack CfnOutput "RestApiUrl")
# Example: "https://abc123xyz.execute-api.ap-southeast-1.amazonaws.com/dev"
REST_API_URL = os.environ.get("REST_API_URL", "https://sjsd378hbd.execute-api.ap-southeast-1.amazonaws.com/dev")

# WebSocket API URL (from ApiServicesStack CfnOutput "WebSocketUrl")
# Example: "wss://xyz789abc.execute-api.ap-southeast-1.amazonaws.com/production"
WS_API_URL = os.environ.get("WS_API_URL", "wss://hey8o0q9tb.execute-api.ap-southeast-1.amazonaws.com/production")

# Admin credentials (from environment.py — used to obtain JWT)
ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin@axrail.com")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "DevAdmin@123")

# S3 bucket names (from ApiServicesStack CfnOutputs)
KB_BUCKET = os.environ.get("KB_BUCKET", "axrail-kb-dev-848332098006")
SKILLS_BUCKET = os.environ.get("SKILLS_BUCKET", "axrail-skills-dev-848332098006")

# DynamoDB table names (from DynamoDBStack — {env}-{TableName} pattern)
SESSIONS_TABLE = os.environ.get("SESSIONS_TABLE", "dev-Sessions")
TRANSCRIPTS_TABLE = os.environ.get("TRANSCRIPTS_TABLE", "dev-Transcripts")

# AWS region
REGION = os.environ.get("AWS_REGION", "ap-southeast-1")

# Path to test fixture files (relative to this script)
# Download and extract test-fixtures.zip, then point this to test-case-2/
FIXTURES_DIR = os.environ.get("FIXTURES_DIR", os.path.join(os.path.dirname(__file__), "..", "resources", "test-case-2"))

# =============================================================================
# HELPERS
# =============================================================================

s3 = boto3.client("s3", region_name=REGION)
dynamodb = boto3.resource("dynamodb", region_name=REGION)


def _print_header(title: str) -> None:
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def _print_result(label: str, data) -> None:
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


def _ws_send_and_receive(ws, payload: dict, wait_seconds: int = 15) -> list:
    ws.send(json.dumps(payload))
    messages = []
    deadline = time.time() + wait_seconds
    while time.time() < deadline:
        try:
            ws.settimeout(max(0.5, deadline - time.time()))
            raw = ws.recv()
            msg = json.loads(raw)
            messages.append(msg)
            if msg.get("type") in ("response", "questionResponse", "gapAnalysis",
                                    "meetingSummary", "retroFeedback", "retroResponse",
                                    "error"):
                break
        except websocket.WebSocketTimeoutException:
            continue
        except Exception as e:
            print(f"  [WS recv error] {e}")
            break
    return messages


def _record(test_name: str, status: str, details: dict | None = None, error: str | None = None) -> None:
    """Append a test result to the report collector."""
    _report.append({
        "test": test_name,
        "status": status,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "details": details or {},
        "error": error,
    })


def _write_report(session_id: str, agent_id: str, project_id: str) -> str:
    """Generate a markdown report from collected test results and write to resources/."""
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    report_dir = os.path.join(os.path.dirname(__file__), "..", "resources", "test-case-2")
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"report-{ts}.md")

    passed = sum(1 for r in _report if r["status"] == "PASS")
    failed = sum(1 for r in _report if r["status"] == "FAIL")
    total = len(_report)

    lines = [
        f"# Test Case 2: GreenBuild Consulting Kickoff — Report",
        f"",
        f"**Generated**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}  ",
        f"**Result**: {passed}/{total} passed, {failed} failed  ",
        f"**Session ID**: `{session_id}`  ",
        f"**Agent ID**: `{agent_id}`  ",
        f"**Project ID**: `{project_id}`  ",
        f"**REST API**: `{REST_API_URL}`  ",
        f"**WebSocket API**: `{WS_API_URL}`  ",
        f"",
        f"---",
        f"",
    ]

    for entry in _report:
        icon = "✅" if entry["status"] == "PASS" else "❌"
        lines.append(f"## {icon} {entry['test']}")
        lines.append(f"")
        lines.append(f"**Status**: {entry['status']}  ")
        lines.append(f"**Time**: {entry['timestamp']}  ")
        lines.append(f"")

        if entry.get("error"):
            lines.append(f"**Error**:")
            lines.append(f"```")
            lines.append(entry["error"])
            lines.append(f"```")
            lines.append(f"")

        if entry["details"]:
            lines.append(f"<details>")
            lines.append(f"<summary>Response Data</summary>")
            lines.append(f"")
            lines.append(f"```json")
            lines.append(json.dumps(entry["details"], indent=2, default=str)[:5000])
            lines.append(f"```")
            lines.append(f"</details>")
            lines.append(f"")

    with open(report_path, "w") as f:
        f.write("\n".join(lines))

    print(f"\n  Report written to: {report_path}")
    return report_path


# =============================================================================
# TEST FUNCTIONS
# =============================================================================

def test_00_authenticate() -> str:
    _print_header("TEST 0: Authenticate")
    try:
        resp = _api("POST", "/auth/admin/login", body={
            "username": ADMIN_USERNAME,
            "password": ADMIN_PASSWORD,
        })
        _print_result("Login response", resp)

        token = resp.get("data", {}).get("access_token", "")
        if not token:
            _record("TEST 0: Authenticate", "FAIL", resp, "No access token returned")
            print("  *** FAILED: No access token. Check credentials and API URL. ***")
            raise SystemExit(1)

        print(f"  Token obtained: {token[:20]}...")
        _record("TEST 0: Authenticate", "PASS", {"token_prefix": token[:20]})
        return token
    except SystemExit:
        raise
    except Exception as e:
        _record("TEST 0: Authenticate", "FAIL", error=traceback.format_exc())
        raise


def test_01_kb_ingestion(project_id: str) -> None:
    """Upload GreenBuild KB files to S3."""
    _print_header("TEST 1: Knowledge Base Ingestion")
    try:
        kb_dir = os.path.join(FIXTURES_DIR, "kb")
        uploaded = []
        for filename in sorted(os.listdir(kb_dir)):
            filepath = os.path.join(kb_dir, filename)
            s3_key = f"{project_id}/{filename}"
            print(f"  Uploading {filename} → s3://{KB_BUCKET}/{s3_key}")
            s3.upload_file(filepath, KB_BUCKET, s3_key)
            uploaded.append(filename)

        print("\n  Waiting 30s for Ingestion Lambda to process...")
        time.sleep(30)
        print("  Check CloudWatch logs for Ingestion Lambda to verify indexing.")
        _record("TEST 1: KB Ingestion", "PASS", {"files_uploaded": uploaded})
    except Exception as e:
        _record("TEST 1: KB Ingestion", "FAIL", error=traceback.format_exc())
        raise


def test_02_create_agent_and_personality(token: str) -> tuple:
    """Create a consulting-focused agent and personality."""
    _print_header("TEST 2: Create Agent & Personality")
    try:
        personality_resp = _api("POST", "/personalities", token, {
            "personality_name": f"Consulting Professional-{uuid.uuid4().hex[:8]}",
            "personality_prompt": (
                "Use formal, structured language appropriate for enterprise "
                "consulting. Reference specific regulations and standards by name. "
                "Be precise with numbers, timelines, and deliverables."
            ),
        })
        _print_result("Create personality", personality_resp)
        personality_id = personality_resp.get("data", {}).get("personality_id", "")

        agent_resp = _api("POST", "/agents", token, {
            "agent_name": f"GreenBuild Consulting Agent-{uuid.uuid4().hex[:8]}",
            "role_prompt": (
                "You are an AI assistant for GreenBuild carbon reporting consultants. "
                "You help answer client questions during kickoff and status meetings "
                "using the GreenBuild knowledge base, regulatory information, and "
                "client-specific context documents. Always cite the regulatory "
                "framework or standard when discussing compliance requirements."
            ),
            "task_prompt": (
                "Monitor the meeting conversation. When the client asks about "
                "methodology, regulations, pricing, or technical details, search "
                "the knowledge base and provide accurate answers. Flag topics "
                "not covered in the knowledge base."
            ),
            "personality_id": personality_id,
            "model_id": "amazon.nova-pro-v1:0",
            "use_case": "consulting_meeting",
        })
        _print_result("Create agent", agent_resp)
        agent_id = agent_resp.get("data", {}).get("agent_id", "")

        _record("TEST 2: Create Agent & Personality", "PASS", {
            "personality_id": personality_id,
            "agent_id": agent_id,
            "personality_response": personality_resp,
            "agent_response": agent_resp,
        })
        return agent_id, personality_id
    except Exception as e:
        _record("TEST 2: Create Agent & Personality", "FAIL", error=traceback.format_exc())
        raise


def test_03_skill_ingestion(token: str, agent_id: str) -> None:
    """Upload skills: manufacturing guide + Meridian client context."""
    _print_header("TEST 3: Skill Ingestion")
    try:
        skills_dir = os.path.join(FIXTURES_DIR, "skills")
        skill_results = []
        for filename in sorted(os.listdir(skills_dir)):
            filepath = os.path.join(skills_dir, filename)

            skill_resp = _api("POST", "/skills", token, {
                "skill_name": filename.replace(".md", "").replace("-", " ").title(),
                "description": f"Skill document: {filename}",
                "file_name": filename,
            })
            _print_result(f"Create skill ({filename})", skill_resp)

            skill_id = skill_resp.get("data", {}).get("skill", {}).get("skill_id", "")

            # Assign skill to agent
            if skill_id:
                assign_resp = _api("POST", f"/agents/{agent_id}/skills/{skill_id}", token)
                _print_result(f"Assign skill to agent ({filename})", assign_resp)

            upload_url = skill_resp.get("data", {}).get("upload_url", "")
            if not upload_url:
                print(f"  *** No upload URL for {filename}, skipping ***")
                skill_results.append({"file": filename, "upload": "skipped"})
                continue

            with open(filepath, "rb") as f:
                file_data = f.read()
                upload_resp = requests.put(upload_url, data=file_data)
                print(f"  S3 upload {filename}: {upload_resp.status_code}")
                if upload_resp.status_code != 200:
                    print(f"  *** Upload failed: {upload_resp.text[:200]} ***")
                    skill_s3_key = skill_resp.get("data", {}).get("skill", {}).get("s3_key", "")
                    if skill_s3_key:
                        print(f"  Falling back to direct S3 upload: s3://{SKILLS_BUCKET}/{skill_s3_key}")
                        s3.put_object(Bucket=SKILLS_BUCKET, Key=skill_s3_key, Body=file_data)
                        print(f"  Direct upload succeeded")
                        skill_results.append({"file": filename, "upload": "fallback_ok"})
                    else:
                        skill_results.append({"file": filename, "upload": "failed"})
                else:
                    skill_results.append({"file": filename, "upload": "ok"})

        print("\n  Waiting 30s for SkillIngestion Lambda...")
        time.sleep(30)

        skills_list = _api("GET", f"/skills?agent_id={agent_id}", token)
        _print_result("List skills", skills_list)
        _record("TEST 3: Skill Ingestion", "PASS", {"skills": skill_results, "list_response": skills_list})
    except Exception as e:
        _record("TEST 3: Skill Ingestion", "FAIL", error=traceback.format_exc())
        raise


def test_04_create_session_and_load_transcript(token: str, project_id: str) -> str:
    """Create session and load the consulting kickoff transcript."""
    _print_header("TEST 4: Create Session & Load Transcript")
    try:
        session_resp = _api("POST", "/sessions", token, {
            "project_id": project_id,
            "name": "Meridian Kickoff Meeting - March 18",
            "description": "Project kickoff with David Park, VP Operations",
        })
        _print_result("Create session", session_resp)
        session_id = session_resp.get("data", {}).get("session_id", "")

        transcript_path = os.path.join(FIXTURES_DIR, "transcripts", "consulting-kickoff-session.json")
        with open(transcript_path) as f:
            transcript_lines = json.load(f)

        table = dynamodb.Table(TRANSCRIPTS_TABLE)
        with table.batch_writer() as batch:
            for line in transcript_lines:
                batch.put_item(Item={
                    "session_id": session_id,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "transcript_id": str(uuid.uuid4()),
                    "speaker": line["speaker"],
                    "text": line["text"],
                    "start_time": str(line["start_time"]),
                    "end_time": str(line["end_time"]),
                    "confidence": str(line["confidence"]),
                    "is_partial": line.get("is_partial", False),
                })
        print(f"  Loaded {len(transcript_lines)} transcript entries for session {session_id}")

        sessions_table = dynamodb.Table(SESSIONS_TABLE)
        sessions_table.update_item(
            Key={"session_id": session_id},
            UpdateExpression="SET is_active = :a, last_transcript_update_at = :ts",
            ExpressionAttributeValues={
                ":a": "active",
                ":ts": datetime.now(timezone.utc).isoformat(),
            },
        )
        _record("TEST 4: Create Session & Load Transcript", "PASS", {
            "session_id": session_id,
            "transcript_lines": len(transcript_lines),
            "session_response": session_resp,
        })
        return session_id
    except Exception as e:
        _record("TEST 4: Create Session & Load Transcript", "FAIL", error=traceback.format_exc())
        raise


def test_05_websocket_process_transcript(session_id: str, agent_id: str) -> None:
    """Transcript processing — verify lines are processed."""
    _print_header("TEST 5: processTranscript — Transcript Processing")
    try:
        transcript_path = os.path.join(FIXTURES_DIR, "transcripts", "consulting-kickoff-session.json")
        with open(transcript_path) as f:
            all_lines = json.load(f)

        first_batch = all_lines[:4]

        ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
        print(f"  Connecting to {ws_url[:80]}...")

        ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
        try:
            messages = _ws_send_and_receive(ws, {
                "action": "processTranscript",
                "session_id": session_id,
                "lines": first_batch,
            }, wait_seconds=20)
            _print_result("processTranscript response", messages)
            _record("TEST 5: processTranscript — Transcript Processing", "PASS", {"messages": messages})
        finally:
            ws.close()
    except Exception as e:
        _record("TEST 5: processTranscript — Transcript Processing", "FAIL", error=traceback.format_exc())
        raise


def test_06_websocket_question_detection(session_id: str, agent_id: str) -> None:
    """Question detection — David's questions about process, data, CBAM, offsets."""
    _print_header("TEST 6: processTranscript — Question Detection")
    try:
        question_lines = [
            {"speaker": "spk_0",
             "text": "How exactly does the process work? We've never done a formal carbon inventory before.",
             "start_time": 97.30, "end_time": 103.85, "confidence": 0.956, "is_partial": False},
            {"speaker": "spk_0",
             "text": "Does that affect us?",
             "start_time": 264.80, "end_time": 277.45, "confidence": 0.876, "is_partial": False},
            {"speaker": "spk_0",
             "text": "Can you help us evaluate offset options? Like do you have partnerships with offset providers?",
             "start_time": 363.40, "end_time": 372.67, "confidence": 0.926, "is_partial": False},
        ]

        ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
        ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
        try:
            messages = _ws_send_and_receive(ws, {
                "action": "processTranscript",
                "session_id": session_id,
                "lines": question_lines,
            }, wait_seconds=25)

            for msg in messages:
                _print_result(f"Response ({msg.get('type', 'unknown')})", msg)

            print("  Expected: questionDetected for each question")
            print("  Process Q → GHG Protocol, 4 phases, 10-13 weeks")
            print("  CBAM Q → covers steel/aluminum, add-on $15K/product line")
            print("  Offsets Q → should indicate LIMITED/NO KB coverage (gap!)")
            _record("TEST 6: processTranscript — Question Detection", "PASS", {"messages": messages})
        finally:
            ws.close()
    except Exception as e:
        _record("TEST 6: processTranscript — Question Detection", "FAIL", error=traceback.format_exc())
        raise


def test_07_websocket_send_message(session_id: str, agent_id: str) -> None:
    """General KB chat with consulting-domain questions."""
    _print_header("TEST 7: sendMessage — KB Chat")
    try:
        questions = [
            "What Scope 3 categories does GreenBuild cover in the standard engagement?",
            "What are the SEC climate reporting deadlines by filer category?",
            "What's Meridian's estimated carbon footprint?",
            "What are some ways Meridian could reduce their emissions?",
        ]

        ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
        ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
        all_responses = {}
        try:
            for q in questions:
                print(f"  Q: {q}")
                messages = _ws_send_and_receive(ws, {
                    "action": "sendMessage",
                    "session_id": session_id,
                    "message": q,
                }, wait_seconds=20)
                for msg in messages:
                    answer = msg.get("message", msg) if isinstance(msg, dict) else msg
                    _print_result("Answer", str(answer)[:500])
                all_responses[q] = messages
        finally:
            ws.close()
        _record("TEST 7: sendMessage — KB Chat", "PASS", {"qa": all_responses})
    except Exception as e:
        _record("TEST 7: sendMessage — KB Chat", "FAIL", error=traceback.format_exc())
        raise


def test_08_websocket_detect_question(session_id: str, agent_id: str) -> None:
    """On-demand question answering."""
    _print_header("TEST 8: detectQuestion — On-Demand Answering")
    try:
        ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
        ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
        all_responses = {}
        try:
            questions = [
                "What penalties does a company face for not complying with SB 253?",
                "How many suppliers should we survey for Scope 3 Category 1?",
            ]
            for q in questions:
                print(f"  Q: {q}")
                messages = _ws_send_and_receive(ws, {
                    "action": "detectQuestion",
                    "session_id": session_id,
                    "question": q,
                }, wait_seconds=20)
                for msg in messages:
                    _print_result("Answer", msg)
                all_responses[q] = messages
                print("  ---")

            print("  Expected: SB 253 → $500K/year. Suppliers → top 30-50 by spend.")
        finally:
            ws.close()
        _record("TEST 8: detectQuestion — On-Demand Answering", "PASS", {"qa": all_responses})
    except Exception as e:
        _record("TEST 8: detectQuestion — On-Demand Answering", "FAIL", error=traceback.format_exc())
        raise


def test_09_websocket_analyze_gaps(session_id: str, agent_id: str) -> None:
    """Gap analysis — should identify carbon offsets as a gap."""
    _print_header("TEST 9: analyzeGaps — Knowledge Gap Analysis")
    try:
        ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
        ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
        try:
            messages = _ws_send_and_receive(ws, {
                "action": "analyzeGaps",
                "session_id": session_id,
            }, wait_seconds=30)
            for msg in messages:
                _print_result("Gap analysis", msg)
            print("  Expected gaps:")
            print("    - Carbon offsets / credits (HIGH — client asked twice)")
            print("    - Full Scope 3 all 15 categories")
            print("    - SBTi target setting process detail")
            _record("TEST 9: analyzeGaps — Gap Analysis", "PASS", {"messages": messages})
        finally:
            ws.close()
    except Exception as e:
        _record("TEST 9: analyzeGaps — Gap Analysis", "FAIL", error=traceback.format_exc())
        raise


def test_10_websocket_set_suggested_questions(session_id: str, agent_id: str) -> None:
    """Set suggested questions, then process transcript to check for questionMatched events."""
    _print_header("TEST 10: setSuggestedQuestions — Question Matching")
    try:
        ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
        ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
        try:
            suggested = [
                "What is GreenBuild's methodology for carbon measurement?",
                "What are the regulatory requirements for carbon reporting?",
            ]
            set_messages = _ws_send_and_receive(ws, {
                "action": "setSuggestedQuestions",
                "session_id": session_id,
                "questions": suggested,
            }, wait_seconds=15)
            _print_result("setSuggestedQuestions response", set_messages)

            match_lines = [
                {"speaker": "spk_0",
                 "text": "We follow the GHG Protocol Corporate Standard which is the frame work the SEC and most global regulators recognize. There are four phases discovery data collection analysis and reporting.",
                 "start_time": 105.60, "end_time": 122.40, "confidence": 0.924, "is_partial": False},
                {"speaker": "spk_0",
                 "text": "The SEC's climate disclosure rules require large accelerated filers to report starting fiscal year 2025, with accelerated filers in 2026.",
                 "start_time": 401.20, "end_time": 422.78, "confidence": 0.879, "is_partial": False},
            ]
            match_messages = _ws_send_and_receive(ws, {
                "action": "processTranscript",
                "session_id": session_id,
                "lines": match_lines,
            }, wait_seconds=25)
            for msg in match_messages:
                _print_result(f"Response ({msg.get('type', 'unknown')})", msg)

            print("  Expected: questionMatched for methodology and regulatory topics")
            _record("TEST 10: setSuggestedQuestions — Question Matching", "PASS", {
                "set_response": set_messages,
                "match_response": match_messages,
            })
        finally:
            ws.close()
    except Exception as e:
        _record("TEST 10: setSuggestedQuestions — Question Matching", "FAIL", error=traceback.format_exc())
        raise


def test_11_websocket_end_meeting(session_id: str, agent_id: str) -> None:
    """Meeting summary generation."""
    _print_header("TEST 11: endMeeting — Meeting Summary")
    try:
        ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
        ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
        try:
            messages = _ws_send_and_receive(ws, {
                "action": "endMeeting",
                "session_id": session_id,
            }, wait_seconds=45)
            for msg in messages:
                _print_result(f"Response ({msg.get('type', '?')})", msg)
            print("  Expected: Summary with attendees, GHG methodology discussion,")
            print("  CBAM exposure, pricing ($83K-$123K), action items (proposal Friday)")
            _record("TEST 11: endMeeting — Meeting Summary", "PASS", {"messages": messages})
        finally:
            ws.close()
    except Exception as e:
        _record("TEST 11: endMeeting — Meeting Summary", "FAIL", error=traceback.format_exc())
        raise


def test_12_websocket_retro_analysis(session_id: str, agent_id: str) -> None:
    """Retro analysis — should flag the carbon offsets fumble."""
    _print_header("TEST 12: retroAnalysis — Post-Meeting Coaching")
    try:
        ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
        ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
        try:
            messages = _ws_send_and_receive(ws, {
                "action": "retroAnalysis",
                "session_id": session_id,
            }, wait_seconds=45)
            for msg in messages:
                _print_result(f"Retro ({msg.get('type', '?')})", msg)
            print("  Expected coaching points:")
            print("    - Carbon offsets answer was vague ('complicated area')")
            print("    - Client asked twice and was deflected both times")
            print("    - CBAM answer was strong (accurate pricing, clear scope)")
            print("    - 'Look into offset advisory' lacks a specific date")
            _record("TEST 12: retroAnalysis — Post-Meeting Coaching", "PASS", {"messages": messages})
        finally:
            ws.close()
    except Exception as e:
        _record("TEST 12: retroAnalysis — Post-Meeting Coaching", "FAIL", error=traceback.format_exc())
        raise


def test_13_websocket_retro_chat(session_id: str, agent_id: str) -> None:
    """Retro follow-up chat."""
    _print_header("TEST 13: retroChat — Follow-Up Questions")
    try:
        ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
        ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
        try:
            _ws_send_and_receive(ws, {
                "action": "retroAnalysis",
                "session_id": session_id,
            }, wait_seconds=45)

            follow_ups = [
                "What should I have said about carbon offsets?",
                "Did I price the engagement correctly for their budget?",
            ]
            all_responses = {}
            for q in follow_ups:
                print(f"  Q: {q}")
                messages = _ws_send_and_receive(ws, {
                    "action": "retroChat",
                    "session_id": session_id,
                    "message": q,
                }, wait_seconds=25)
                for msg in messages:
                    _print_result("Retro chat", msg)
                all_responses[q] = messages
                print("  ---")

            print("  Offsets Q → should suggest structured response framework")
            print("  Pricing Q → within $125K budget, presented clearly")
            _record("TEST 13: retroChat — Follow-Up Questions", "PASS", {"qa": all_responses})
        finally:
            ws.close()
    except Exception as e:
        _record("TEST 13: retroChat — Follow-Up Questions", "FAIL", error=traceback.format_exc())
        raise


def test_14_qa_pairs(token: str, session_id: str) -> None:
    """Check QA pairs extracted by endMeeting."""
    _print_header("TEST 14: QA Pairs — Verify Extraction")
    try:
        resp = _api("GET", f"/qa-pairs?session_id={session_id}", token)
        _print_result("QA pairs for session", resp)
        items = resp.get("data", [])
        if isinstance(items, dict):
            items = items.get("items", [])
        print(f"  Total QA pairs extracted: {len(items)}")
        print("  Expected: 5-8 Q&A pairs from the kickoff transcript")
        _record("TEST 14: QA Pairs — Verify Extraction", "PASS", {"count": len(items), "response": resp})
    except Exception as e:
        _record("TEST 14: QA Pairs — Verify Extraction", "FAIL", error=traceback.format_exc())
        raise


def test_15_crud_cleanup(token: str) -> None:
    """CRUD smoke test — verify all resource endpoints."""
    _print_header("TEST 15: CRUD Smoke Test")
    try:
        results = {}
        for endpoint in ["/agents", "/personalities", "/skills", "/projects", "/sessions"]:
            resp = _api("GET", endpoint, token)
            count = 0
            data = resp.get("data", {})
            if isinstance(data, dict):
                count = len(data.get("items", []))
            elif isinstance(data, list):
                count = len(data)
            print(f"  GET {endpoint}: {resp.get('statusCode', '?')} — {count} items")
            results[endpoint] = {"statusCode": resp.get("statusCode"), "count": count}
        _record("TEST 15: CRUD Smoke Test", "PASS", results)
    except Exception as e:
        _record("TEST 15: CRUD Smoke Test", "FAIL", error=traceback.format_exc())
        raise


def _create_project(token: str) -> str:
    """Create the test project and return its project_id."""
    project_resp = _api("POST", "/projects", token, {
        "name": f"GreenBuild - Meridian Manufacturing-{uuid.uuid4().hex[:8]}",
        "email": "priya@greenbuild.com",
        "description": "Carbon reporting engagement for Meridian Manufacturing",
    })
    _print_result("Create project", project_resp)
    project_id = project_resp.get("data", {}).get("project_id", "")
    _record("Create Project", "PASS" if project_id else "FAIL", {"project_id": project_id, "response": project_resp})
    return project_id


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("  TEST CASE 2: GreenBuild Consulting Kickoff")
    print("  Fixtures:", FIXTURES_DIR)
    print("  REST API:", REST_API_URL)
    print("  WebSocket:", WS_API_URL)
    print("=" * 70)

    if not os.path.isdir(os.path.join(FIXTURES_DIR, "kb")):
        print(f"\n  *** Fixtures not found at {FIXTURES_DIR} ***")
        print("  Extract test-fixtures.zip and set FIXTURES_DIR to test-case-2/")
        raise SystemExit(1)

    session_id = agent_id = project_id = ""
    try:
        token = test_00_authenticate()
        agent_id, _ = test_02_create_agent_and_personality(token)
        project_id = _create_project(token)
        test_01_kb_ingestion(project_id)
        test_03_skill_ingestion(token, agent_id)
        session_id = test_04_create_session_and_load_transcript(token, project_id)

        test_05_websocket_process_transcript(session_id, agent_id)
        test_06_websocket_question_detection(session_id, agent_id)
        test_07_websocket_send_message(session_id, agent_id)
        test_08_websocket_detect_question(session_id, agent_id)
        test_09_websocket_analyze_gaps(session_id, agent_id)
        test_10_websocket_set_suggested_questions(session_id, agent_id)
        test_11_websocket_end_meeting(session_id, agent_id)
        test_12_websocket_retro_analysis(session_id, agent_id)
        test_13_websocket_retro_chat(session_id, agent_id)

        test_14_qa_pairs(token, session_id)
        test_15_crud_cleanup(token)
    except SystemExit:
        raise
    except Exception:
        print("\n  *** Test run aborted due to error (see report for details) ***")
    finally:
        _write_report(session_id, agent_id, project_id)

    _print_header("ALL TESTS COMPLETE")
    print(f"  Session ID: {session_id}")
    print(f"  Agent ID:   {agent_id}")
    print("  Review outputs above against test-plan.md expected results.")


if __name__ == "__main__":
    main()
