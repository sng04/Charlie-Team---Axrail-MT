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
import uuid
from datetime import datetime, timezone

import boto3
import requests
import websocket

_SSL_OPTS = {"cert_reqs": ssl.CERT_NONE}

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


# =============================================================================
# TEST FUNCTIONS
# =============================================================================

def test_00_authenticate() -> str:
    _print_header("TEST 0: Authenticate")
    resp = _api("POST", "/auth/admin/login", body={
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD,
    })
    _print_result("Login response", resp)

    token = resp.get("data", {}).get("access_token", "")
    if not token:
        print("  *** FAILED: No access token. Check credentials and API URL. ***")
        raise SystemExit(1)

    print(f"  Token obtained: {token[:20]}...")
    return token


def test_01_kb_ingestion(project_id: str) -> None:
    """Upload GreenBuild KB files to S3.

    Uses the real project_id as the S3 key prefix so the Ingestion Lambda
    indexes documents with the correct project_id.
    """
    _print_header("TEST 1: Knowledge Base Ingestion")

    kb_dir = os.path.join(FIXTURES_DIR, "kb")
    for filename in sorted(os.listdir(kb_dir)):
        filepath = os.path.join(kb_dir, filename)
        s3_key = f"{project_id}/{filename}"
        print(f"  Uploading {filename} → s3://{KB_BUCKET}/{s3_key}")
        s3.upload_file(filepath, KB_BUCKET, s3_key)

    print("\n  Waiting 30s for Ingestion Lambda to process...")
    time.sleep(30)
    print("  Check CloudWatch logs for Ingestion Lambda to verify indexing.")


def test_02_create_agent_and_personality(token: str) -> tuple:
    """Create a consulting-focused agent and personality."""
    _print_header("TEST 2: Create Agent & Personality")

    personality_resp = _api("POST", "/personalities", token, {
        "personality_name": "Consulting Professional",
        "personality_prompt": (
            "Use formal, structured language appropriate for enterprise "
            "consulting. Reference specific regulations and standards by name. "
            "Be precise with numbers, timelines, and deliverables."
        ),
    })
    _print_result("Create personality", personality_resp)
    personality_id = personality_resp.get("data", {}).get("personality_id", "")

    agent_resp = _api("POST", "/agents", token, {
        "agent_name": "GreenBuild Consulting Agent",
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

    return agent_id, personality_id


def test_03_skill_ingestion(token: str, agent_id: str) -> None:
    """Upload skills: manufacturing guide + Meridian client context."""
    _print_header("TEST 3: Skill Ingestion")

    skills_dir = os.path.join(FIXTURES_DIR, "skills")
    for filename in sorted(os.listdir(skills_dir)):
        filepath = os.path.join(skills_dir, filename)

        skill_resp = _api("POST", "/skills", token, {
            "agent_id": agent_id,
            "skill_name": filename.replace(".md", "").replace("-", " ").title(),
            "description": f"Skill document: {filename}",
            "file_name": filename,
        })
        _print_result(f"Create skill ({filename})", skill_resp)

        upload_url = skill_resp.get("data", {}).get("upload_url", "")
        if not upload_url:
            print(f"  *** No upload URL for {filename}, skipping ***")
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

    print("\n  Waiting 30s for SkillIngestion Lambda...")
    time.sleep(30)

    skills_list = _api("GET", f"/skills?agent_id={agent_id}", token)
    _print_result("List skills", skills_list)


def test_04_create_session_and_load_transcript(token: str, project_id: str) -> str:
    """Create session and load the consulting kickoff transcript."""
    _print_header("TEST 4: Create Session & Load Transcript")

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
                "timestamp": line["timestamp"],
                "transcript_id": str(uuid.uuid4()),
                "speaker": line["speaker"],
                "text": line["text"],
                "confidence": "0.95",
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

    return session_id


def test_05_websocket_process_transcript(session_id: str, agent_id: str) -> None:
    """Speaker classification — Priya (consultant/user) vs David (client)."""
    _print_header("TEST 5: processTranscript — Speaker Classification")

    transcript_path = os.path.join(FIXTURES_DIR, "transcripts", "consulting-kickoff-session.json")
    with open(transcript_path) as f:
        all_lines = json.load(f)

    first_batch = [{"speaker": l["speaker"], "text": l["text"],
                     "timestamp": l["timestamp"]} for l in all_lines[:4]]

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
        print("  Expected: Priya Sharma=user, David Park=client")
    finally:
        ws.close()


def test_06_websocket_question_detection(session_id: str, agent_id: str) -> None:
    """Client question detection — David's questions about process, data, CBAM, offsets."""
    _print_header("TEST 6: processTranscript — Client Question Detection")

    question_lines = [
        {"speaker": "David Park",
         "text": "How exactly does the process work? We've never done a formal carbon inventory before.",
         "timestamp": "2026-03-18T09:02:35Z"},
        {"speaker": "David Park",
         "text": "Does that affect us?",
         "timestamp": "2026-03-18T09:07:18Z"},
        {"speaker": "David Park",
         "text": "Can you help us evaluate offset options? Like, do you have partnerships with offset providers?",
         "timestamp": "2026-03-18T09:09:48Z"},
    ]

    ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
    ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
    try:
        messages = _ws_send_and_receive(ws, {
            "action": "processTranscript",
            "session_id": session_id,
            "lines": question_lines,
            "speaker_hint": {"Priya Sharma": "user", "David Park": "client"},
        }, wait_seconds=25)

        for msg in messages:
            _print_result(f"Response ({msg.get('type', 'unknown')})", msg)

        print("  Expected: clientQuestionDetected for each question")
        print("  Process Q → GHG Protocol, 4 phases, 10-13 weeks")
        print("  CBAM Q → covers steel/aluminum, add-on $15K/product line")
        print("  Offsets Q → should indicate LIMITED/NO KB coverage (gap!)")
    finally:
        ws.close()


def test_07_websocket_send_message(session_id: str, agent_id: str) -> None:
    """General KB chat with consulting-domain questions."""
    _print_header("TEST 7: sendMessage — KB Chat")

    questions = [
        "What Scope 3 categories does GreenBuild cover in the standard engagement?",
        "What are the SEC climate reporting deadlines by filer category?",
        "What's Meridian's estimated carbon footprint?",
        "What are some ways Meridian could reduce their emissions?",
    ]

    ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
    ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
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
    finally:
        ws.close()


def test_08_websocket_detect_question(session_id: str, agent_id: str) -> None:
    """On-demand question answering."""
    _print_header("TEST 8: detectQuestion — On-Demand Answering")

    ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
    ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
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
            print("  ---")

        print("  Expected: SB 253 → $500K/year. Suppliers → top 30-50 by spend.")
    finally:
        ws.close()


def test_09_websocket_analyze_gaps(session_id: str, agent_id: str) -> None:
    """Gap analysis — should identify carbon offsets as a gap."""
    _print_header("TEST 9: analyzeGaps — Knowledge Gap Analysis")

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
    finally:
        ws.close()


def test_10_websocket_set_suggested_questions(session_id: str, agent_id: str) -> None:
    """Set suggested questions, then process transcript to check for questionMatched events."""
    _print_header("TEST 10: setSuggestedQuestions — Question Matching")

    ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
    ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
    try:
        # Step 1: Set suggested questions
        suggested = [
            "What is GreenBuild's methodology for carbon measurement?",
            "What are the regulatory requirements for carbon reporting?",
        ]
        messages = _ws_send_and_receive(ws, {
            "action": "setSuggestedQuestions",
            "session_id": session_id,
            "questions": suggested,
        }, wait_seconds=15)
        _print_result("setSuggestedQuestions response", messages)

        # Step 2: Process transcript lines where Priya discusses those topics
        match_lines = [
            {"speaker": "Priya Sharma",
             "text": "We follow the GHG Protocol Corporate Standard — it's the gold standard for carbon accounting. The process has four phases over about 10 to 13 weeks.",
             "timestamp": "2026-03-18T09:03:05Z"},
            {"speaker": "Priya Sharma",
             "text": "The SEC's climate disclosure rules require large accelerated filers to report starting fiscal year 2025, with accelerated filers in 2026.",
             "timestamp": "2026-03-18T09:02:15Z"},
        ]
        messages = _ws_send_and_receive(ws, {
            "action": "processTranscript",
            "session_id": session_id,
            "lines": match_lines,
            "speaker_hint": {"Priya Sharma": "user", "David Park": "client"},
        }, wait_seconds=25)
        for msg in messages:
            _print_result(f"Response ({msg.get('type', 'unknown')})", msg)

        print("  Expected: questionMatched for methodology and regulatory topics")
    finally:
        ws.close()


def test_11_websocket_end_meeting(session_id: str, agent_id: str) -> None:
    """Meeting summary generation."""
    _print_header("TEST 11: endMeeting — Meeting Summary")

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
    finally:
        ws.close()


def test_12_websocket_retro_analysis(session_id: str, agent_id: str) -> None:
    """Retro analysis — should flag the carbon offsets fumble."""
    _print_header("TEST 12: retroAnalysis — Post-Meeting Coaching")

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
    finally:
        ws.close()


def test_13_websocket_retro_chat(session_id: str, agent_id: str) -> None:
    """Retro follow-up chat."""
    _print_header("TEST 13: retroChat — Follow-Up Questions")

    ws_url = f"{WS_API_URL}?session_id={session_id}&agent_id={agent_id}"
    ws = websocket.create_connection(ws_url, timeout=10, sslopt=_SSL_OPTS)
    try:
        # Run retroAnalysis first to populate context
        _ws_send_and_receive(ws, {
            "action": "retroAnalysis",
            "session_id": session_id,
        }, wait_seconds=45)

        follow_ups = [
            "What should I have said about carbon offsets?",
            "Did I price the engagement correctly for their budget?",
        ]
        for q in follow_ups:
            print(f"  Q: {q}")
            messages = _ws_send_and_receive(ws, {
                "action": "retroChat",
                "session_id": session_id,
                "message": q,
            }, wait_seconds=25)
            for msg in messages:
                _print_result("Retro chat", msg)
            print("  ---")

        print("  Offsets Q → should suggest structured response framework")
        print("  Pricing Q → within $125K budget, presented clearly")
    finally:
        ws.close()


def test_14_qa_pairs(token: str, session_id: str) -> None:
    """Check QA pairs extracted by endMeeting."""
    _print_header("TEST 14: QA Pairs — Verify Extraction")

    resp = _api("GET", f"/qa-pairs?session_id={session_id}", token)
    _print_result("QA pairs for session", resp)
    items = resp.get("data", [])
    if isinstance(items, dict):
        items = items.get("items", [])
    print(f"  Total QA pairs extracted: {len(items)}")
    print("  Expected: 5-8 Q&A pairs from the kickoff transcript")


def test_15_crud_cleanup(token: str) -> None:
    """CRUD smoke test — verify all resource endpoints."""
    _print_header("TEST 15: CRUD Smoke Test")

    for endpoint in ["/agents", "/personalities", "/skills", "/projects", "/sessions"]:
        resp = _api("GET", endpoint, token)
        count = 0
        data = resp.get("data", {})
        if isinstance(data, dict):
            count = len(data.get("items", []))
        elif isinstance(data, list):
            count = len(data)
        print(f"  GET {endpoint}: {resp.get('statusCode', '?')} — {count} items")


def _create_project(token: str) -> str:
    """Create the test project and return its project_id."""
    project_resp = _api("POST", "/projects", token, {
        "name": "GreenBuild - Meridian Manufacturing",
        "email": "priya@greenbuild.com",
        "description": "Carbon reporting engagement for Meridian Manufacturing",
    })
    _print_result("Create project", project_resp)
    return project_resp.get("data", {}).get("project_id", "")


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

    token = test_00_authenticate()
    agent_id, _ = test_02_create_agent_and_personality(token)

    # Create project early so its ID can be used as the KB S3 key prefix
    project_id = _create_project(token)

    test_01_kb_ingestion(project_id)
    test_03_skill_ingestion(token, agent_id)
    session_id = test_04_create_session_and_load_transcript(token, project_id)

    # WebSocket tests
    test_05_websocket_process_transcript(session_id, agent_id)
    test_06_websocket_question_detection(session_id, agent_id)
    test_07_websocket_send_message(session_id, agent_id)
    test_08_websocket_detect_question(session_id, agent_id)
    test_09_websocket_analyze_gaps(session_id, agent_id)
    test_10_websocket_set_suggested_questions(session_id, agent_id)
    test_11_websocket_end_meeting(session_id, agent_id)
    test_12_websocket_retro_analysis(session_id, agent_id)
    test_13_websocket_retro_chat(session_id, agent_id)

    # Post-meeting verification
    test_14_qa_pairs(token, session_id)
    test_15_crud_cleanup(token)

    _print_header("ALL TESTS COMPLETE")
    print(f"  Session ID: {session_id}")
    print(f"  Agent ID:   {agent_id}")
    print("  Review outputs above against test-plan.md expected results.")


if __name__ == "__main__":
    main()
