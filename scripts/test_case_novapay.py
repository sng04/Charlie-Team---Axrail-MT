"""
NovaPay E2E Test — Project Setup + 2 Historical Sessions + Live Check-In

1. Ensures project, KB, agent, and skills exist (creates if missing, skips if present)
2. Creates 2 historical sessions with mock transcript + QA data (skips if present)
3. Starts a fresh live check-in session with mock transcript data, then waits
   for the user to end it via the frontend. Verifies post-meeting processes.

Run:
    AWS_SHARED_CREDENTIALS_FILE=.aws/credentials python scripts/test_case_novapay.py
"""

import json
import os
import ssl
import time
import traceback
import uuid
from datetime import datetime, timezone, timedelta

import boto3
import requests
import websocket

_SSL_OPTS = {"cert_reqs": ssl.CERT_NONE}

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
REGION = os.environ.get("AWS_REGION", "ap-southeast-1")
FIXTURES_DIR = os.path.join(os.path.dirname(__file__), "..", "resources", "test-case-novapay")

BOT_EMAIL = "savioenoson.dev@gmail.com"
MEETING_LINK = "https://meet.google.com/xae-vdjm-tje"
USER_EMAIL = "mt-savioenoson@axrail.com"

PROJECT_NAME = "NovaPay SEA Expansion"
AGENT_NAME = "NovaPay Sales Closer"
PERSONALITY_NAME = "Executive Advisor"

SESSION_1_NAME = "NovaPay × MegaMart MY — Kickoff & Requirements"
SESSION_2_NAME = "NovaPay × MegaMart MY — Proposal & Technical Review"
SESSION_3_NAME = "NovaPay × MegaMart MY — Pilot Check-In"

s3 = boto3.client("s3", region_name=REGION)
dynamodb = boto3.resource("dynamodb", region_name=REGION)

sessions_table = dynamodb.Table(os.environ.get("SESSIONS_TABLE", "dev-Sessions"))
transcripts_table = dynamodb.Table(os.environ.get("TRANSCRIPTS_TABLE", "dev-Transcripts"))
qa_pairs_table = dynamodb.Table(os.environ.get("QA_PAIRS_TABLE_NAME", "dev-QAPairs"))
gap_table = dynamodb.Table(os.environ.get("GAP_ANALYSIS_TABLE_NAME", "dev-GapAnalysisResults"))


def _h(title):
    print(f"\n{'='*65}\n  {title}\n{'='*65}\n")


def _api(method, path, token=None, body=None):
    url = f"{REST_API_URL.rstrip('/')}/{path.lstrip('/')}"
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    timeout = 60 if "sessions" in path and method.upper() == "POST" else 30
    resp = requests.request(method, url, headers=headers, json=body, timeout=timeout)
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
                                   "meetingSummary", "retroFeedback", "retroResponse",
                                   "error"):
                break
        except websocket.WebSocketTimeoutException:
            continue
        except Exception:
            break
    return msgs


# ─── Mock Data ───────────────────────────────────────────────────────────────
# Narrative: We are an integration consultancy helping NovaPay (US payment
# processor) expand into Southeast Asia. The client is MegaMart Malaysia,
# a 60-store retail chain looking to modernize their payment stack.
# Alex = our consultant (user), Rizal = MegaMart Head of Payments (client).

def _load_transcript(filename):
    """Load transcript from JSON file in the fixtures directory."""
    path = os.path.join(FIXTURES_DIR, "transcripts", filename)
    with open(path) as f:
        return json.load(f)

SESSION_1_QA_PAIRS = [
    {"question": "Can NovaPay handle MYR?", "answer": "NovaPay settles in USD only currently. Transactions are processed in MYR at the terminal but settled in USD with FX conversion. Multi-currency settlement is on the roadmap.", "source": "participant"},
    {"question": "What's the FX markup on the conversion?", "answer": "Standard FX markup is 1.5%. At MegaMart's volume (~RM 8M/month), negotiable down to ~1%. Competitive for the USD/MYR corridor.", "source": "participant"},
    {"question": "Is ShieldAI included or is it an add-on?", "answer": "Included on the Enterprise plan at no extra per-transaction charge. Reduces fraud losses by ~68% using ML trained on 2B+ transactions.", "source": "participant"},
    {"question": "What about PCI compliance?", "answer": "NovaPay is PCI DSS Level 1 certified, SOC 2 Type II. Using the drop-in SDK keeps merchants at SAQ-A (20-question self-assessment vs full audit).", "source": "participant"},
    {"question": "Would the same integration work for Singapore?", "answer": "Yes, same platform. Singapore has no currency restrictions — accept SGD, settle in USD. Brunei dollar is pegged to SGD.", "source": "participant"},
]

SESSION_2_QA_PAIRS = [
    {"question": "Does the drop-in SDK support React Native?", "answer": "Yes, NovaPay has a React Native wrapper supporting iOS and Android from a single codebase.", "source": "participant"},
    {"question": "What's the webhook retry policy?", "answer": "Exponential backoff: 1 min, 5 min, 30 min, 2 hours, then every 6 hours for up to 72 hours. Webhooks can be replayed from the dashboard.", "source": "participant"},
    {"question": "What's the contract term?", "answer": "Two-year enterprise agreement with annual pricing reviews. Interchange-plus markup locked for the full term. Volume discounts apply automatically.", "source": "participant"},
    {"question": "What about the SST implications?", "answer": "Platform fee is subject to imported services SST (8%). Finance team self-accounts for it on the monthly fee. Per-transaction fees are built into interchange-plus pricing.", "source": "participant"},
    {"question": "Is the FX rate locked daily or per-transaction?", "answer": "Per-settlement batch (T+1). Batch rates are tighter than per-transaction rates, which works in the merchant's favor.", "source": "participant"},
]

SESSION_3_QA_PAIRS = [
    {"question": "Is there a way to customize the card input styling to match our brand colors?", "answer": "Yes, the drop-in SDK supports a theme configuration object for primary color, font family, border radius, and error colors.", "source": "participant"},
    {"question": "Has ShieldAI flagged anything unusual on the NovaPay transactions so far?", "answer": "18 transactions flagged as high risk out of ~11,000 online orders. Two confirmed card testing attempts auto-declined. False positive rate at 0.1%.", "source": "participant"},
    {"question": "What's the process for adding the remaining 50 stores?", "answer": "Same terminal provisioning flow. Batch-provision remotely, 15-20 stores per batch, three batches over two weeks. Store managers power cycle Verifone units after config push.", "source": "agent"},
    {"question": "Has your legal team finished reviewing the contract?", "answer": "Legal returned with two minor redlines: clarify data retention under PDPA and add breach notification timeline clause. Should be resolved in a day or two.", "source": "agent"},
]


# ─── Step Functions ──────────────────────────────────────────────────────────

def step_authenticate():
    _h("Authenticate")
    resp = _api("POST", "/auth/admin/login", body={"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD})
    token = resp.get("data", {}).get("access_token", "")
    assert token, f"Auth failed: {resp}"
    print(f"  Token: {token[:20]}...")
    return token


def step_cleanup_warm_pool(token):
    """Remove error containers, stop orphaned ECS tasks, ensure 10 idle containers."""
    _h("Cleanup & Start Warm Pool")

    creds = _api("GET", "/bot-credentials", token).get("data", {}).get("items", [])
    cred = next((c for c in creds if c.get("email") == BOT_EMAIL), None)
    if not cred:
        print(f"  ⚠ Bot credential for {BOT_EMAIL} not found, skipping")
        return
    cred_id = cred["credential_id"]
    ecs = boto3.client("ecs", region_name=REGION)

    # Stop orphaned ECS tasks not tracked in bot pool
    pool = dynamodb.Table("dev-BotPool")
    pool_resp = pool.scan()
    pool_task_ids = {i.get("container_id", "") for i in pool_resp.get("Items", [])}

    resp = ecs.list_tasks(cluster="dev-meeting-bot", desiredStatus="RUNNING")
    task_arns = resp.get("taskArns", [])
    orphaned = 0
    if task_arns:
        details = ecs.describe_tasks(cluster="dev-meeting-bot", tasks=task_arns)
        for task in details.get("tasks", []):
            task_id = task["taskArn"].split("/")[-1]
            # Check if this task belongs to our credential
            is_ours = False
            for container in task.get("overrides", {}).get("containerOverrides", []):
                for env in container.get("environment", []):
                    if env.get("name") == "CREDENTIAL_ID" and env.get("value") == cred_id:
                        is_ours = True
                        break
            if is_ours and task_id not in pool_task_ids:
                ecs.stop_task(cluster="dev-meeting-bot", task=task["taskArn"], reason="Orphaned task cleanup")
                orphaned += 1
    if orphaned:
        print(f"  Stopped {orphaned} orphaned ECS tasks")
        time.sleep(5)

    # Remove error/stopping containers from bot pool
    pool_resp = pool.scan()
    error_deleted = 0
    healthy = 0
    idle = 0
    for item in pool_resp.get("Items", []):
        if item.get("credential_id") != cred_id:
            continue
        status = item.get("status", "")
        if status in ("error", "stopping"):
            pool.delete_item(Key={"container_id": item["container_id"]})
            error_deleted += 1
        elif status in ("idle", "starting", "busy"):
            healthy += 1
            if status == "idle":
                idle += 1
    if error_deleted:
        print(f"  Removed {error_deleted} error containers")
    print(f"  Containers: {healthy} total, {idle} idle")

    # Start more if needed to reach 10
    needed = max(0, 10 - healthy)
    if needed > 0:
        print(f"  Starting {needed} containers...")
        resp = _api("POST", "/warm-pool/start", token, {
            "credential_ids": [cred_id],
            "containers_per_credential": 10,
        })
        started = len(resp.get("data", {}).get("started_tasks", []))
        print(f"  ✓ Requested {started} containers")

    # Wait until at least 1 container is idle
    if idle == 0:
        print(f"  Waiting for containers to become idle...")
        for attempt in range(18):
            time.sleep(10)
            pool_resp = pool.scan()
            idle = sum(1 for i in pool_resp.get("Items", [])
                       if i.get("credential_id") == cred_id and i.get("status") == "idle")
            total = sum(1 for i in pool_resp.get("Items", [])
                        if i.get("credential_id") == cred_id and i.get("status") in ("idle", "starting", "busy"))
            print(f"    [{(attempt+1)*10}s] {idle} idle / {total} total")
            if idle >= 1:
                break
        print(f"  ✓ {idle} containers ready")
    else:
        print(f"  ✓ {idle} containers already idle")


def step_ensure_project(token):
    """Find or create the NovaPay project with bot credential and user assigned."""
    _h("Ensure Project")

    # Find bot credential
    creds = _api("GET", "/bot-credentials", token).get("data", {}).get("items", [])
    cred = next((c for c in creds if c.get("email") == BOT_EMAIL), None)
    assert cred, f"Bot credential for {BOT_EMAIL} not found — create it first"
    cred_id = cred["credential_id"]

    # Find user
    users = _api("GET", "/users", token).get("data", {}).get("items", [])
    user = next((u for u in users if u.get("email") == USER_EMAIL), None)

    # Check for existing project
    projects = _api("GET", "/projects?limit=100", token).get("data", {}).get("items", [])
    existing = next((p for p in projects if p.get("name") == PROJECT_NAME), None)
    if existing:
        pid = existing["project_id"]
        print(f"  ✓ Project exists: {pid[:8]}...")
        # Ensure bot credential is assigned
        if existing.get("bot_credential_id") != cred_id:
            _api("PUT", f"/projects/{pid}", token, {"bot_credential_id": cred_id})
            print(f"  ↳ Assigned bot credential: {BOT_EMAIL}")
        # Ensure user is assigned
        if user:
            _ensure_user_assigned(token, pid, user["user_id"])
        return pid

    resp = _api("POST", "/projects", token, {
        "name": PROJECT_NAME,
        "email": "novapay-sea@axrail.com",
        "description": "NovaPay payment processing expansion into Southeast Asia — MegaMart Malaysia integration",
    })
    pid = resp.get("data", {}).get("project_id", "")
    print(f"  ✓ Created project: {pid[:8]}...")

    # Assign bot credential
    _api("PUT", f"/projects/{pid}", token, {"bot_credential_id": cred_id})
    print(f"  ↳ Assigned bot credential: {BOT_EMAIL}")

    # Assign user
    if user:
        _ensure_user_assigned(token, pid, user["user_id"])

    return pid


def _ensure_user_assigned(token, project_id, user_id):
    """Assign user to project if not already assigned."""
    proj_users = _api("GET", f"/projects/{project_id}/users", token).get("data", {}).get("items", [])
    already = any(pu.get("user_id") == user_id for pu in proj_users)
    if already:
        print(f"  ✓ User already assigned: {USER_EMAIL}")
        return
    _api("POST", "/project-users", token, {"project_id": project_id, "user_id": user_id})
    print(f"  ↳ Assigned user: {USER_EMAIL}")


def step_ensure_kb(token, project_id):
    """Upload KB files via the API. Delete any KB docs not in our fixture set."""
    _h("Ensure Knowledge Base")
    kb_dir = os.path.join(FIXTURES_DIR, "kb")
    if not os.path.isdir(kb_dir):
        print("  ⚠ No KB fixtures found, skipping")
        return

    # Our expected KB files
    our_files = {f for f in os.listdir(kb_dir) if not f.startswith(".")}

    # Check existing KB documents — delete any not in our set
    existing_docs = _api("GET", f"/projects/{project_id}/kb-documents", token).get("data", {}).get("documents", [])
    existing_names = set()
    for doc in existing_docs:
        fname = doc.get("file_name", "")
        doc_id = doc.get("document_id", "")
        if fname in our_files:
            existing_names.add(fname)
        elif doc_id:
            _api("DELETE", f"/projects/{project_id}/kb-documents/{doc_id}", token)
            print(f"  ✗ Removed stale KB doc: {fname}")

    uploaded = 0
    for fname in sorted(our_files):
        if fname in existing_names:
            print(f"  ✓ {fname} already in KB")
            continue

        # Create KB document via API to get pre-signed URL + DDB record
        resp = _api("POST", f"/projects/{project_id}/kb-documents", token, {"file_name": fname})
        doc_data = resp.get("data", {})
        upload_url = doc_data.get("upload_url", "")
        if not upload_url:
            print(f"  ✗ {fname} — no upload URL: {resp.get('message', '')}")
            continue

        # Determine content type
        ext = fname.rsplit(".", 1)[-1].lower() if "." in fname else ""
        content_type = {"pdf": "application/pdf", "md": "text/markdown", "txt": "text/plain",
                        "docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        }.get(ext, "application/octet-stream")

        with open(os.path.join(kb_dir, fname), "rb") as f:
            put_resp = requests.put(upload_url, data=f.read(), headers={"Content-Type": content_type}, timeout=30)

        if put_resp.status_code == 200:
            print(f"  ↑ {fname} — uploaded via API")
            uploaded += 1
        else:
            print(f"  ⚠ {fname} — upload failed ({put_resp.status_code})")

    if uploaded:
        print(f"  Waiting 20s for ingestion...")
        time.sleep(20)
    print(f"  KB ready ({uploaded} new uploads)")


def _ensure_skills_assigned(token, agent_id):
    """Ensure all skill files from fixtures are uploaded and assigned to the agent."""
    skills_dir = os.path.join(FIXTURES_DIR, "skills")
    if not os.path.isdir(skills_dir):
        return

    # Get currently assigned skills
    assigned = _api("GET", f"/agents/{agent_id}/skills", token).get("data", {}).get("skills", [])
    assigned_names = {s.get("skill_name", "") for s in assigned}

    # Get all existing skills
    all_skills = _api("GET", "/skills?limit=100", token).get("data", {}).get("skills", [])
    skill_by_name = {s.get("skill_name", ""): s for s in all_skills}

    for fname in sorted(os.listdir(skills_dir)):
        if fname.startswith("."):
            continue
        skill_name = fname.replace(".md", "").replace("-", " ").title()

        if skill_name in assigned_names:
            continue

        # Check if skill exists but isn't assigned
        if skill_name in skill_by_name:
            sid = skill_by_name[skill_name]["skill_id"]
            _api("POST", f"/agents/{agent_id}/skills/{sid}", token)
            print(f"  ↳ Assigned existing skill: {skill_name}")
            continue

        # Create and upload new skill
        resp = _api("POST", "/skills", token, {
            "skill_name": skill_name, "file_name": fname,
            "description": f"Skill: {fname}",
        })
        sd = resp.get("data", {})
        sid = sd.get("skill", {}).get("skill_id", "")
        url = sd.get("upload_url", "")
        ct = sd.get("content_type", "text/markdown")
        if sid and url:
            with open(os.path.join(skills_dir, fname), "rb") as f:
                requests.put(url, data=f.read(), headers={"Content-Type": ct}, timeout=30)
            _api("POST", f"/agents/{agent_id}/skills/{sid}", token)
            print(f"  ↳ Created & assigned skill: {skill_name}")


def step_ensure_agent(token, project_id):
    """Find or create the agent + personality, assign skills, link to project."""
    _h("Ensure Agent & Skills")

    # Check existing agents
    agents = _api("GET", "/agents", token).get("data", {}).get("items", [])
    existing = next((a for a in agents if a.get("agent_name") == AGENT_NAME), None)
    if existing:
        agent_id = existing["agent_id"]
        print(f"  ✓ Agent exists: {agent_id[:8]}...")
        # Ensure project is linked
        proj = _api("GET", f"/projects/{project_id}", token).get("data", {})
        if proj.get("agent_id") != agent_id:
            _api("PUT", f"/projects/{project_id}", token, {"agent_id": agent_id})
            print(f"  ↳ Linked agent to project")
        # Ensure skills are assigned
        _ensure_skills_assigned(token, agent_id)
        return agent_id

    # Find or create personality
    personalities = _api("GET", "/personalities", token).get("data", {}).get("items", [])
    personality = next((p for p in personalities if p.get("personality_name") == PERSONALITY_NAME), None)
    if personality:
        pid = personality["personality_id"]
        print(f"  ✓ Personality exists: {PERSONALITY_NAME}")
    else:
        resp = _api("POST", "/personalities", token, {
            "personality_name": PERSONALITY_NAME,
            "personality_prompt": "Communicate like a senior executive advisor. Lead with business impact. Use precise numbers.",
        })
        pid = resp.get("data", {}).get("personality_id", "")
        print(f"  ✓ Created personality: {PERSONALITY_NAME}")

    # Create agent
    resp = _api("POST", "/agents", token, {
        "agent_name": AGENT_NAME,
        "role_prompt": "You are an AI assistant for NovaPay sales reps. Help close deals by providing accurate product info, pricing, and competitive intelligence.",
        "behavior_guidelines": "1. Search KB first for factual answers\n2. Search skills for competitive positioning\n3. Be specific with numbers and timelines\n4. Honestly state when something is not available",
        "personality_id": pid,
        "model_id": "amazon.nova-pro-v1:0",
        "use_case": "sales_meeting",
    })
    agent_id = resp.get("data", {}).get("agent_id", "")
    print(f"  ✓ Created agent: {agent_id[:8]}...")

    # Assign all skills from fixtures
    _ensure_skills_assigned(token, agent_id)
    time.sleep(15)  # Wait for skill ingestion

    # Link agent to project
    _api("PUT", f"/projects/{project_id}", token, {"agent_id": agent_id})
    print(f"  ✓ Agent linked to project")
    return agent_id


def _write_mock_session(token, project_id, agent_id, session_name, transcript, qa_pairs, base_time):
    """Create a fully fabricated completed session. No bot, no ECS, pure DDB."""
    sessions = _api("GET", f"/projects/{project_id}/sessions", token).get("data", {}).get("items", [])
    existing = next((s for s in sessions if s.get("name") == session_name), None)
    if existing:
        print(f"  ✓ Session exists: {session_name}")
        return existing["session_id"]

    sid = str(uuid.uuid4())
    end_time = base_time + timedelta(seconds=len(transcript) * 12)
    sessions_table.put_item(Item={
        "session_id": sid, "project_id": project_id,
        "name": session_name, "meeting_link": MEETING_LINK,
        "description": f"Historical session: {session_name}",
        "bot_status": "stopped", "is_active": "active", "status": "",
        "created_at": base_time.isoformat(), "updated_at": end_time.isoformat(),
        "last_transcript_update_at": end_time.isoformat(),
    })
    print(f"  ✓ Created session: {session_name} ({sid[:8]}...)")

    for i, line in enumerate(transcript):
        ts = (base_time + timedelta(seconds=i * 12)).isoformat()
        transcripts_table.put_item(Item={
            "session_id": sid, "timestamp": ts,
            "transcript_id": str(uuid.uuid4()),
            "speaker": line["speaker"], "text": line["text"],
            "confidence": str(line.get("confidence", 0.95)),
            "speaker_role": "user" if i % 2 == 0 else "client",
        })
    print(f"    ↳ {len(transcript)} transcript lines")

    for qi, qa in enumerate(qa_pairs):
        qa_time = base_time + timedelta(seconds=qi * len(transcript) * 12 // max(len(qa_pairs), 1))
        qa_pairs_table.put_item(Item={
            "qa_pair_id": str(uuid.uuid4()),
            "session_id": sid, "project_id": project_id,
            "question": qa["question"], "answer": qa["answer"],
            "source": qa["source"], "detected_at": qa_time.isoformat(), "gsi_pk": "ALL",
        })
    print(f"    ↳ {len(qa_pairs)} QA pairs")

    print(f"    ↳ Generating summary...")
    try:
        ws = websocket.create_connection(
            f"{WS_API_URL}?session_id={sid}&agent_id={agent_id}",
            timeout=10, sslopt=_SSL_OPTS,
        )
        msgs = _ws_send_recv(ws, {"action": "endMeeting", "session_id": sid}, wait=60)
        ws.close()
        if any(m.get("type") == "meetingSummary" for m in msgs):
            print(f"    ↳ Summary ✓")
        else:
            print(f"    ↳ endMeeting: {[m.get('type') for m in msgs]}")
    except Exception as e:
        print(f"    ↳ Summary failed: {e}")

    sessions_table.update_item(
        Key={"session_id": sid},
        UpdateExpression="SET bot_status = :bs, is_active = :ia, #s = :s",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":bs": "stopped", ":ia": "completed", ":s": "completed"},
    )
    print(f"    ↳ Completed")
    return sid


def step_ensure_historical_sessions(token, project_id, agent_id):
    """Create 2 historical sessions with mock data if they don't exist."""
    _h("Ensure Historical Sessions")

    now = datetime.now(timezone.utc)
    _write_mock_session(token, project_id, agent_id, SESSION_1_NAME,
                        _load_transcript("session-1-kickoff.json"), SESSION_1_QA_PAIRS,
                        now - timedelta(days=7))
    _write_mock_session(token, project_id, agent_id, SESSION_2_NAME,
                        _load_transcript("session-2-proposal.json"), SESSION_2_QA_PAIRS,
                        now - timedelta(days=3))


def step_start_live_session(token, project_id, agent_id):
    """Delete any existing check-in session, create a fresh one with mock data."""
    _h("Start Live Check-In Session")

    # Delete existing check-in session if present
    sessions = _api("GET", f"/projects/{project_id}/sessions", token).get("data", {}).get("items", [])
    for s in sessions:
        if s.get("name") == SESSION_3_NAME:
            sid = s["session_id"]
            print(f"  Deleting previous check-in session: {sid[:8]}...")
            _api("DELETE", f"/sessions/{sid}", token)
            # Clean up related data
            _cleanup_session_data(sid)

    # Create fresh session
    resp = _api("POST", "/sessions", token, {
        "project_id": project_id,
        "name": SESSION_3_NAME,
        "meeting_link": MEETING_LINK,
        "description": "Quick pilot status check-in between Alex (NovaPay) and Marcus (FreshCart)",
    })
    sid = resp.get("data", {}).get("session_id", "")
    if not sid:
        print(f"  ✗ Failed to create session: {resp.get('message', resp)}")
        raise RuntimeError("Session creation failed")
    print(f"  ✓ Created session: {sid[:8]}...")

    # Wait for bot to actually join the meeting
    print(f"  Waiting for bot to join meeting...")
    if _wait_for_bot_join(token, sid):
        print(f"  ✓ Bot has joined the meeting")
    else:
        print(f"  ⚠ Bot may not have joined — proceeding anyway")

    # Stream transcript line-by-line to DDB, send to WebSocket individually
    session_3_lines = _load_transcript("session-3-checkin.json")
    print(f"  Streaming {len(session_3_lines)} transcript lines (~3 min)...")

    try:
        ws = websocket.create_connection(
            f"{WS_API_URL}?session_id={sid}&agent_id={agent_id}",
            timeout=10, sslopt=_SSL_OPTS,
        )
    except Exception as e:
        print(f"  ⚠ WebSocket connect failed: {e}")
        ws = None

    pending_lines = []
    for i, line in enumerate(session_3_lines):
        line_num = i + 1
        ts = datetime.now(timezone.utc).isoformat()

        # Write to DDB (like the real bot does per-line)
        transcripts_table.put_item(Item={
            "session_id": sid, "timestamp": ts,
            "transcript_id": str(uuid.uuid4()),
            "speaker": line["speaker"], "text": line["text"],
            "confidence": str(line.get("confidence", 0.95)),
            "speaker_role": "user" if line_num % 2 != 0 else "client",
        })
        sessions_table.update_item(
            Key={"session_id": sid},
            UpdateExpression="SET is_active = :a, last_transcript_update_at = :ts",
            ExpressionAttributeValues={":a": "active", ":ts": ts},
        )
        print(f"    [{line_num}/{len(session_3_lines)}] {line['speaker']}: {line['text'][:60]}...")

        # Send each line individually to processTranscript
        if ws:
            try:
                msgs = _ws_send_recv(ws, {
                    "action": "processTranscript", "session_id": sid, "lines": [line],
                }, wait=15)
                for m in msgs:
                    t = m.get("type", "?")
                    if t == "questionDetected":
                        print(f"    🔍 Q: {m.get('question', '')[:70]}...")
                    elif t == "suggestedResponse":
                        print(f"    💡 Suggested: {m.get('suggested_answer', '')[:70]}...")
                    elif t == "qaPairAutoSaved":
                        print(f"    💾 QA saved")
                    elif t == "transcriptProcessed":
                        pass  # Don't clutter output for every line
            except Exception as e:
                print(f"    ⚠ WS error: {e}")

        time.sleep(0.8)  # ~1 second per line, realistic speaking pace

    if ws:
        try:
            ws.close()
        except Exception:
            pass

    print(f"\n  ✓ Transcript streamed")

    return sid


def _wait_for_bot_join(token, session_id, max_wait=180):
    """Poll session until bot_status is in_meeting. Returns True if joined."""
    for attempt in range(max_wait // 10):
        time.sleep(10)
        resp = _api("GET", f"/sessions/{session_id}", token)
        bot_status = resp.get("data", {}).get("bot_status", "pending")
        is_active = resp.get("data", {}).get("is_active", "")
        if bot_status in ("in_meeting", "running", "active") or is_active == "active":
            return True
        if bot_status in ("stopped", "error", "failed"):
            return False
    return False


def _cleanup_session_data(session_id):
    """Remove transcript, QA pairs, and gap analysis for a session."""
    # Transcripts
    resp = transcripts_table.query(KeyConditionExpression=boto3.dynamodb.conditions.Key("session_id").eq(session_id))
    with transcripts_table.batch_writer() as batch:
        for item in resp.get("Items", []):
            batch.delete_item(Key={"session_id": item["session_id"], "timestamp": item["timestamp"]})

    # QA pairs
    from boto3.dynamodb.conditions import Key
    resp = qa_pairs_table.query(IndexName="session-index", KeyConditionExpression=Key("session_id").eq(session_id))
    with qa_pairs_table.batch_writer() as batch:
        for item in resp.get("Items", []):
            batch.delete_item(Key={"qa_pair_id": item["qa_pair_id"]})

    # Gap analysis
    try:
        gap_table.delete_item(Key={"session_id": session_id})
    except Exception:
        pass


def step_wait_for_end_meeting(token, session_id, agent_id, project_id):
    """Wait for the user to end the meeting, then verify post-meeting processes."""
    _h("Waiting for Meeting End")
    print(f"  Session: {session_id}")
    print(f"  The session is now live with transcript data.")
    print(f"  End the meeting from the frontend when ready.")
    print(f"  Polling session status every 15s...\n")

    while True:
        try:
            resp = _api("GET", f"/sessions/{session_id}", token)
            data = resp.get("data", {})
            status = data.get("status", "")
            is_active = data.get("is_active", "active")

            if status == "completed" or is_active in ("false", "completed"):
                print(f"\n  ✓ Meeting ended (status={status}, is_active={is_active})")
                break

            print(f"  ... still active (is_active={is_active})", end="\r")
            time.sleep(15)
        except KeyboardInterrupt:
            print(f"\n  Interrupted — skipping wait")
            return

    # Verify post-meeting processes
    print(f"\n  Verifying post-meeting processes...")
    time.sleep(10)

    # Check summary
    resp = _api("GET", f"/sessions/{session_id}/summary", token)
    summary_status = resp.get("data", {}).get("status", "not_found")
    if summary_status == "available":
        print(f"  ✓ Summary generated")
    else:
        print(f"  ⏳ Summary status: {summary_status} (may still be processing)")
        time.sleep(20)
        resp = _api("GET", f"/sessions/{session_id}/summary", token)
        summary_status = resp.get("data", {}).get("status", "not_found")
        print(f"  Summary status after wait: {summary_status}")

    # Check S3
    s3_key = f"{project_id}/summaries/{session_id}.md"
    try:
        s3.head_object(Bucket=KB_BUCKET, Key=s3_key)
        print(f"  ✓ Summary in S3: {s3_key}")
    except Exception:
        print(f"  ⚠ Summary not yet in S3: {s3_key}")

    # Check KB documents
    resp = _api("GET", f"/projects/{project_id}/kb-documents", token)
    docs = resp.get("data", {}).get("documents", [])
    summary_doc = next((d for d in docs if d.get("session_id") == session_id), None)
    if summary_doc:
        print(f"  ✓ Summary registered in KB documents: {summary_doc.get('file_name', '')}")
    else:
        print(f"  ⚠ Summary not yet in KB documents list")

    # Check token usage
    resp = _api("GET", f"/sessions/{session_id}/token-usage", token)
    total = resp.get("data", {}).get("total_tokens", 0)
    print(f"  ✓ Token usage: {total} tokens recorded")

    print(f"\n  Post-meeting verification complete.")


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("  NovaPay E2E Test — FreshCart Integration")
    print(f"  REST: {REST_API_URL}")
    print(f"  WS:   {WS_API_URL}")
    print("=" * 65)

    try:
        token = step_authenticate()
        step_cleanup_warm_pool(token)
        project_id = step_ensure_project(token)
        step_ensure_kb(token, project_id)
        agent_id = step_ensure_agent(token, project_id)
        step_ensure_historical_sessions(token, project_id, agent_id)
        session_id = step_start_live_session(token, project_id, agent_id)
        step_wait_for_end_meeting(token, session_id, agent_id, project_id)
    except KeyboardInterrupt:
        print("\n\n  Interrupted.")
    except Exception:
        print(f"\n  *** Error ***\n{traceback.format_exc()}")

    print("\n  Done.")


if __name__ == "__main__":
    main()
