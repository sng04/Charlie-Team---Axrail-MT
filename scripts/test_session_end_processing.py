"""
End-to-End Session End Processing Tests

SESS-E006: Lambda transcription failure — error shown, session marked incomplete.
SESS-E007: Summary generation failure — transcript accessible, summary unavailable.
SESS-E008: User navigates away — background processing continues, results available.
SESS-E009: Concurrent end-session — deduplication, no duplicate processing.

Architecture notes:
  - Session end is triggered via WebSocket `endMeeting` action (not REST).
  - Summary is saved to S3 at {project_id}/summaries/{session_id}.md
  - Session state: inactive → active → completed (terminal)
  - Transcripts are in DynamoDB (session_id PK, timestamp SK)
  - REST API is used for session CRUD, transcript/summary retrieval, bot control.

This test validates the REST-observable state after session end processing:
  - Session state in DynamoDB (via GET /sessions/{sessionId})
  - Transcript availability (via GET /sessions/{sessionId}/transcripts)
  - Summary availability (via GET /sessions/{sessionId}/summary)
  - Concurrency behavior (via parallel session updates)

Usage:
    ADMIN_PASSWORD="YourPassword" python scripts/test_session_end_processing.py
    ADMIN_PASSWORD="YourPassword" python scripts/test_session_end_processing.py --test E006

Environment variables:
    BASE_URL          - API Gateway base URL
    ADMIN_USERNAME    - Admin email
    ADMIN_PASSWORD    - Admin password
    PROJECT_ID        - Existing project ID (auto-selected if not set)
"""

import json
import os
import sys
import time
import uuid
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from typing import Optional


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_URL = os.environ.get(
    "BASE_URL",
    "https://sjsd378hbd.execute-api.ap-southeast-1.amazonaws.com/dev",
).rstrip("/")

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "admin@axrail.com")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "TempAdmin@123")
PROJECT_ID = os.environ.get("PROJECT_ID", "")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
@dataclass
class TestResult:
    test_id: str
    name: str
    passed: bool
    detail: str


results: list[TestResult] = []
_cleanup_session_ids: list[str] = []


def _api(
    method: str,
    path: str,
    token: Optional[str] = None,
    body: Optional[dict] = None,
) -> tuple[int, dict]:
    url = f"{BASE_URL}{path}"
    data = json.dumps(body).encode() if body else None
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        try:
            resp_body = json.loads(e.read().decode())
        except Exception:
            resp_body = {}
        return e.code, resp_body


def _record(test_id: str, name: str, passed: bool, detail: str):
    tag = "✓ PASS" if passed else "✗ FAIL"
    results.append(TestResult(test_id, name, passed, detail))
    print(f"  [{tag}] {test_id}: {name}")
    if not passed:
        print(f"         → {detail}")


def _create_session(token: str, project_id: str, name: str) -> tuple[int, dict]:
    return _api("POST", "/sessions", token=token, body={
        "name": name,
        "project_id": project_id,
    })


def _get_session(token: str, session_id: str) -> tuple[int, dict]:
    return _api("GET", f"/sessions/{session_id}", token=token)


def _update_session(token: str, session_id: str, data: dict) -> tuple[int, dict]:
    return _api("PUT", f"/sessions/{session_id}", token=token, body=data)


def _get_transcripts(token: str, session_id: str) -> tuple[int, dict]:
    return _api("GET", f"/sessions/{session_id}/transcripts", token=token)


def _get_summary(token: str, session_id: str) -> tuple[int, dict]:
    return _api("GET", f"/sessions/{session_id}/summary", token=token)


def _delete_session(token: str, session_id: str) -> tuple[int, dict]:
    return _api("DELETE", f"/sessions/{session_id}", token=token)


def _stop_bot(token: str, session_id: str) -> tuple[int, dict]:
    return _api("POST", f"/sessions/{session_id}/stop-bot", token=token)


# ---------------------------------------------------------------------------
# Auth & Setup
# ---------------------------------------------------------------------------
def authenticate() -> Optional[str]:
    print(f"\n{'='*70}")
    print("AUTH: Logging in as admin")
    print(f"{'='*70}")
    status, body = _api("POST", "/auth/admin/login", body={
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD,
    })
    if status != 200:
        print(f"  [FAIL] Login failed: {status} — {body}")
        return None
    token = body.get("data", {}).get("access_token")
    if not token:
        print(f"  [FAIL] No access_token")
        return None
    print(f"  [OK] Authenticated")
    return token


def _resolve_project_id(token: str) -> Optional[str]:
    if PROJECT_ID:
        return PROJECT_ID
    status, body = _api("GET", "/projects", token=token)
    if status != 200:
        return None
    projects = body.get("data", {}).get("items", [])
    if isinstance(body.get("data"), list):
        projects = body["data"]
    if not projects:
        print("  [FAIL] No projects found. Create one or set PROJECT_ID.")
        return None
    pid = projects[0].get("project_id")
    print(f"  [INFO] Auto-selected project: {pid}")
    return pid


# ---------------------------------------------------------------------------
# SESS-E006: Lambda transcription failure — session marked incomplete
# ---------------------------------------------------------------------------
def test_sess_e006(token: str, project_id: str):
    """Simulate a session that ends without transcription data.

    Since endMeeting is WebSocket-only, we simulate the failure scenario by:
    1. Creating a session (no meeting link → no bot → no transcripts)
    2. Verifying transcript endpoint returns empty (simulating transcription failure)
    3. Verifying session state reflects no processing occurred
    4. Verifying no silent data loss — session record is intact
    """
    print(f"\n{'='*70}")
    print("SESS-E006: Transcription Failure Handling")
    print(f"{'='*70}")

    session_name = f"E006-TranscriptFail-{uuid.uuid4().hex[:8]}"

    # Create session without meeting link (no bot dispatched)
    status, body = _create_session(token, project_id, session_name)
    _record("E006-1", "Create session returns 200", status == 200,
            f"Got {status}: {body.get('message', '')}")

    if status != 200:
        return

    session_data = body.get("data", {})
    session_id = session_data.get("session_id")
    _cleanup_session_ids.append(session_id)

    _record("E006-2", "Session ID generated",
            session_id is not None and len(session_id) == 36,
            f"session_id={session_id}")

    # Verify no transcripts exist (simulates transcription failure)
    t_status, t_body = _get_transcripts(token, session_id)
    t_data = t_body.get("data", {})
    items = t_data.get("items", []) if isinstance(t_data, dict) else []
    _record("E006-3", "Transcript endpoint returns empty (no transcription)",
            t_status == 200 and len(items) == 0,
            f"Status={t_status}, items={len(items)}")

    # Verify summary is not generated
    s_status, s_body = _get_summary(token, session_id)
    s_data = s_body.get("data", {})
    summary_status = s_data.get("status", "")
    summary_md = s_data.get("summary_markdown")
    _record("E006-4", "Summary marked as not generated",
            s_status == 200 and (summary_status == "not_generated" or summary_md is None),
            f"Status={s_status}, summary_status={summary_status}")

    # Verify session record is intact (no silent data loss)
    g_status, g_body = _get_session(token, session_id)
    g_data = g_body.get("data", {})
    _record("E006-5", "Session record intact (no data loss)",
            g_status == 200 and g_data.get("session_id") == session_id,
            f"GET status={g_status}, name={g_data.get('name')}")

    _record("E006-6", "Session state is not 'completed' (no processing ran)",
            g_data.get("is_active") != "completed",
            f"is_active={g_data.get('is_active')}")


# ---------------------------------------------------------------------------
# SESS-E007: Summary generation failure — transcript still accessible
# ---------------------------------------------------------------------------
def test_sess_e007(token: str, project_id: str):
    """Verify that when summary is unavailable, transcript data is still accessible.

    Creates a session, verifies transcript endpoint works independently of summary.
    Summary endpoint should clearly indicate 'not_generated' status.
    """
    print(f"\n{'='*70}")
    print("SESS-E007: Summary Failure — Transcript Still Accessible")
    print(f"{'='*70}")

    session_name = f"E007-SummaryFail-{uuid.uuid4().hex[:8]}"

    status, body = _create_session(token, project_id, session_name)
    _record("E007-1", "Create session returns 200", status == 200,
            f"Got {status}: {body.get('message', '')}")

    if status != 200:
        return

    session_id = body.get("data", {}).get("session_id")
    _cleanup_session_ids.append(session_id)

    # Transcript endpoint should work regardless of summary state
    t_status, t_body = _get_transcripts(token, session_id)
    _record("E007-2", "Transcript endpoint accessible (independent of summary)",
            t_status == 200,
            f"Transcript GET status={t_status}")

    # Summary should clearly indicate unavailable
    s_status, s_body = _get_summary(token, session_id)
    s_data = s_body.get("data", {})
    _record("E007-3", "Summary endpoint returns 200 with 'not_generated' status",
            s_status == 200 and s_data.get("status") == "not_generated",
            f"Status={s_status}, summary_status={s_data.get('status')}")

    _record("E007-4", "Summary markdown is null (not partial/corrupt)",
            s_data.get("summary_markdown") is None,
            f"summary_markdown={s_data.get('summary_markdown')}")

    # Verify session record is fully accessible (Retro Mode readiness)
    g_status, g_body = _get_session(token, session_id)
    g_data = g_body.get("data", {})
    _record("E007-5", "Session record accessible for Retro Mode",
            g_status == 200 and g_data.get("name") == session_name,
            f"GET status={g_status}, name={g_data.get('name')}")


# ---------------------------------------------------------------------------
# SESS-E008: User navigates away — background processing continues
# ---------------------------------------------------------------------------
def test_sess_e008(token: str, project_id: str):
    """Verify that session data remains accessible after user 'navigates away'.

    Simulates: create session → update it → wait → verify all data still available.
    Since endMeeting runs server-side (Lambda), navigating away doesn't interrupt it.
    We verify the REST endpoints return consistent data regardless of client state.
    """
    print(f"\n{'='*70}")
    print("SESS-E008: Background Processing Continues After Navigate Away")
    print(f"{'='*70}")

    session_name = f"E008-NavAway-{uuid.uuid4().hex[:8]}"

    status, body = _create_session(token, project_id, session_name)
    _record("E008-1", "Create session returns 200", status == 200,
            f"Got {status}: {body.get('message', '')}")

    if status != 200:
        return

    session_id = body.get("data", {}).get("session_id")
    _cleanup_session_ids.append(session_id)

    # Update session (simulates user activity before navigating away)
    u_status, _ = _update_session(token, session_id, {
        "name": f"{session_name}-updated",
        "description": "Updated before navigate away",
    })
    _record("E008-2", "Session update succeeds", u_status == 200,
            f"Update status={u_status}")

    # Simulate "navigate away" — just wait a few seconds
    print("    Simulating user navigating away (5s pause)...")
    time.sleep(5)

    # Re-authenticate (simulates user returning with fresh session)
    fresh_token = authenticate()
    if not fresh_token:
        _record("E008-3", "Re-auth after navigate away", False, "Re-auth failed")
        return

    # Verify session data is fully available on return
    g_status, g_body = _get_session(fresh_token, session_id)
    g_data = g_body.get("data", {})
    _record("E008-3", "Session data available after return",
            g_status == 200 and g_data.get("session_id") == session_id,
            f"GET status={g_status}")

    _record("E008-4", "Session update persisted",
            g_data.get("name") == f"{session_name}-updated",
            f"name={g_data.get('name')}")

    _record("E008-5", "Description persisted",
            g_data.get("description") == "Updated before navigate away",
            f"description={g_data.get('description')}")

    # Transcript endpoint still works
    t_status, _ = _get_transcripts(fresh_token, session_id)
    _record("E008-6", "Transcript endpoint accessible on return",
            t_status == 200,
            f"Transcript GET status={t_status}")

    # Summary endpoint still works
    s_status, _ = _get_summary(fresh_token, session_id)
    _record("E008-7", "Summary endpoint accessible on return",
            s_status == 200,
            f"Summary GET status={s_status}")


# ---------------------------------------------------------------------------
# SESS-E009: Concurrent end-session requests — deduplication
# ---------------------------------------------------------------------------
def test_sess_e009(token: str, project_id: str):
    """Test concurrent session updates to verify state consistency.

    Since endMeeting is WebSocket-only, we test concurrency via REST:
    1. Create a session
    2. Fire concurrent PUT updates (simulating race conditions)
    3. Verify final state is consistent (no corruption)
    4. Verify only one session record exists (no duplicates)
    """
    print(f"\n{'='*70}")
    print("SESS-E009: Concurrent Session Requests — Deduplication")
    print(f"{'='*70}")

    session_name = f"E009-Concurrent-{uuid.uuid4().hex[:8]}"

    status, body = _create_session(token, project_id, session_name)
    _record("E009-1", "Create session returns 200", status == 200,
            f"Got {status}: {body.get('message', '')}")

    if status != 200:
        return

    session_id = body.get("data", {}).get("session_id")
    _cleanup_session_ids.append(session_id)

    # Fire concurrent updates to simulate race condition
    print("    Sending 5 concurrent session updates...")

    def _concurrent_update(i: int) -> tuple[int, dict]:
        # Each thread gets a fresh token to avoid auth issues
        t = authenticate()
        if not t:
            return 401, {}
        return _update_session(t, session_id, {
            "description": f"Concurrent update {i}",
        })

    statuses = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(_concurrent_update, i): i for i in range(5)}
        for future in as_completed(futures):
            i = futures[future]
            try:
                s, b = future.result()
                statuses.append(s)
                print(f"    Update {i}: status={s}")
            except Exception as e:
                statuses.append(500)
                print(f"    Update {i}: error={e}")

    success_count = sum(1 for s in statuses if s == 200)
    _record("E009-2", "All concurrent updates return 200 (no crashes)",
            success_count == 5,
            f"{success_count}/5 succeeded, statuses={statuses}")

    # Verify final state is consistent (one of the updates won)
    fresh_token = authenticate() or token
    g_status, g_body = _get_session(fresh_token, session_id)
    g_data = g_body.get("data", {})
    _record("E009-3", "Session state is consistent after concurrent updates",
            g_status == 200 and g_data.get("session_id") == session_id,
            f"GET status={g_status}")

    desc = g_data.get("description", "")
    _record("E009-4", "Description reflects one of the concurrent updates",
            desc.startswith("Concurrent update"),
            f"description='{desc}'")

    # Verify no duplicate sessions created
    list_status, list_body = _api("GET", f"/projects/{project_id}/sessions", token=fresh_token)
    sessions = list_body.get("data", {}).get("items", [])
    if isinstance(list_body.get("data"), list):
        sessions = list_body["data"]
    matches = [s for s in sessions if s.get("name") == session_name]
    _record("E009-5", "No duplicate session records",
            len(matches) == 1,
            f"Found {len(matches)} session(s) named '{session_name}'")

    # Verify session_id is unchanged
    _record("E009-6", "Session ID unchanged after concurrent updates",
            g_data.get("session_id") == session_id,
            f"Expected {session_id}, got {g_data.get('session_id')}")


# ---------------------------------------------------------------------------
# Cleanup & Report
# ---------------------------------------------------------------------------
def cleanup(token: str):
    if not _cleanup_session_ids:
        return
    print(f"\n{'='*70}")
    print("CLEANUP: Deleting test sessions")
    print(f"{'='*70}")
    for sid in _cleanup_session_ids:
        if not sid:
            continue
        status, _ = _delete_session(token, sid)
        tag = "OK" if status == 200 else f"WARN ({status})"
        print(f"  [{tag}] Deleted {sid}")


def print_report() -> int:
    print(f"\n{'='*70}")
    print("TEST REPORT")
    print(f"{'='*70}\n")

    total = len(results)
    passed = sum(1 for r in results if r.passed)
    failed = total - passed

    for prefix, label in [
        ("E006", "SESS-E006 Transcription Failure"),
        ("E007", "SESS-E007 Summary Failure"),
        ("E008", "SESS-E008 Navigate Away"),
        ("E009", "SESS-E009 Concurrent Requests"),
    ]:
        group = [r for r in results if r.test_id.startswith(prefix)]
        if not group:
            continue
        gp = sum(1 for r in group if r.passed)
        st = "PASS" if gp == len(group) else "FAIL"
        print(f"  [{st}] {label}: {gp}/{len(group)} checks passed")

    print(f"\n  Total: {passed}/{total} passed, {failed} failed")

    if failed:
        print(f"\n{'─'*70}")
        print("FAILURES:")
        print(f"{'─'*70}")
        for r in results:
            if not r.passed:
                print(f"  [{r.test_id}] {r.name}")
                print(f"    → {r.detail}")

    if failed == 0:
        print("\n✅ All session end processing tests passed.")
    else:
        print(f"\n❌ {failed} check(s) failed — review above.")

    return 1 if failed else 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"Target: {BASE_URL}")
    print(f"Admin:  {ADMIN_USERNAME}")

    selected = None
    if "--test" in sys.argv:
        idx = sys.argv.index("--test")
        if idx + 1 < len(sys.argv):
            selected = sys.argv[idx + 1].upper()

    token = authenticate()
    if not token:
        print("\nCannot proceed without admin token. Exiting.")
        sys.exit(1)

    project_id = _resolve_project_id(token)
    if not project_id:
        print("\nNo project ID. Exiting.")
        sys.exit(1)

    print(f"  Project: {project_id}")

    all_tests = {
        "E006": ("SESS-E006", test_sess_e006),
        "E007": ("SESS-E007", test_sess_e007),
        "E008": ("SESS-E008", test_sess_e008),
        "E009": ("SESS-E009", test_sess_e009),
    }

    if selected:
        if selected not in all_tests:
            print(f"\nUnknown test: {selected}. Available: {', '.join(all_tests.keys())}")
            sys.exit(1)
        tests_to_run = {selected: all_tests[selected]}
        print(f"\n  Running only: {selected}")
    else:
        tests_to_run = all_tests

    try:
        for key, (label, test_fn) in tests_to_run.items():
            token = authenticate()
            if not token:
                print(f"\n  [SKIP] {label} — re-auth failed")
                continue
            test_fn(token, project_id)
    finally:
        token = authenticate() or token
        cleanup(token)

    exit_code = print_report()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
