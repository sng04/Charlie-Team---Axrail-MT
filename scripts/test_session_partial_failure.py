"""
End-to-End Session End Processing — Partial Failure & Data Preservation

AGT-E007: Transcription failure — session incomplete, partial data preserved.
AGT-E008: Summary failure — transcript fully accessible, summary unavailable.
AGT-E009: Insights failure — transcript + summary accessible, insights unavailable.

Architecture:
  - endMeeting is a WebSocket action (not REST). These tests validate the
    REST-observable state that each failure scenario should produce.
  - Transcript: DynamoDB Transcripts table, GET /sessions/{id}/transcripts
  - Summary: S3 at {project_id}/summaries/{session_id}.md, GET /sessions/{id}/summary
  - Insights: QA pairs (GET /qa-pairs?session_id=), suggested questions
    (GET /sessions/{id}/suggested-questions)
  - Session state: is_active field (inactive → active → completed)

Usage:
    ADMIN_PASSWORD="YourPassword" python scripts/test_session_partial_failure.py
    ADMIN_PASSWORD="YourPassword" python scripts/test_session_partial_failure.py --test E007

Environment variables:
    BASE_URL, ADMIN_USERNAME, ADMIN_PASSWORD, PROJECT_ID
"""

import json
import os
import sys
import time
import uuid
import urllib.request
import urllib.error
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
    method: str, path: str,
    token: Optional[str] = None, body: Optional[dict] = None,
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
            rb = json.loads(e.read().decode())
        except Exception:
            rb = {}
        return e.code, rb


def _record(test_id: str, name: str, passed: bool, detail: str):
    tag = "✓ PASS" if passed else "✗ FAIL"
    results.append(TestResult(test_id, name, passed, detail))
    print(f"  [{tag}] {test_id}: {name}")
    if not passed:
        print(f"         → {detail}")


def authenticate() -> Optional[str]:
    status, body = _api("POST", "/auth/admin/login", body={
        "username": ADMIN_USERNAME, "password": ADMIN_PASSWORD,
    })
    if status != 200:
        print(f"  [FAIL] Login: {status} — {body}")
        return None
    token = body.get("data", {}).get("access_token")
    if token:
        print(f"  [OK] Authenticated")
    return token


def _resolve_project_id(token: str) -> Optional[str]:
    if PROJECT_ID:
        return PROJECT_ID
    s, b = _api("GET", "/projects", token=token)
    if s != 200:
        return None
    projects = b.get("data", {}).get("items", [])
    if isinstance(b.get("data"), list):
        projects = b["data"]
    if not projects:
        print("  [FAIL] No projects. Create one or set PROJECT_ID.")
        return None
    pid = projects[0].get("project_id")
    print(f"  [INFO] Auto-selected project: {pid}")
    return pid


# Shorthand API calls
def _create_session(tk, pid, name):
    return _api("POST", "/sessions", tk, {"name": name, "project_id": pid})

def _get_session(tk, sid):
    return _api("GET", f"/sessions/{sid}", tk)

def _get_transcripts(tk, sid):
    return _api("GET", f"/sessions/{sid}/transcripts", tk)

def _get_summary(tk, sid):
    return _api("GET", f"/sessions/{sid}/summary", tk)

def _get_qa_pairs(tk, sid):
    return _api("GET", f"/qa-pairs?session_id={sid}", tk)

def _get_suggested_questions(tk, sid):
    return _api("GET", f"/sessions/{sid}/suggested-questions", tk)

def _delete_session(tk, sid):
    return _api("DELETE", f"/sessions/{sid}", tk)


# ---------------------------------------------------------------------------
# AGT-E007: Transcription failure — partial data preserved
# ---------------------------------------------------------------------------
def test_agt_e007(token: str, project_id: str):
    """Simulate transcription failure: session created but no bot/transcripts.

    Validates:
    - Session is NOT marked 'completed' (no processing ran)
    - Transcript endpoint returns 200 with empty list (no crash)
    - Summary is 'not_generated'
    - Session record is fully intact (no silent data loss)
    - QA pairs and suggested questions return empty (no orphaned data)
    """
    print(f"\n{'='*70}")
    print("AGT-E007: Transcription Failure — Partial Data Preserved")
    print(f"{'='*70}")

    name = f"E007-TranscriptFail-{uuid.uuid4().hex[:8]}"
    s, b = _create_session(token, project_id, name)
    _record("E007-1", "Create session returns 200", s == 200,
            f"Got {s}: {b.get('message', '')}")
    if s != 200:
        return

    sid = b.get("data", {}).get("session_id")
    _cleanup_session_ids.append(sid)

    # Session state should NOT be 'completed'
    gs, gb = _get_session(token, sid)
    gd = gb.get("data", {})
    _record("E007-2", "Session not marked 'completed'",
            gs == 200 and gd.get("is_active") != "completed",
            f"is_active={gd.get('is_active')}")

    # Transcript endpoint returns 200 with empty items
    ts, tb = _get_transcripts(token, sid)
    td = tb.get("data", {})
    items = td.get("items", []) if isinstance(td, dict) else []
    _record("E007-3", "Transcript endpoint returns 200 (empty, no crash)",
            ts == 200 and len(items) == 0,
            f"status={ts}, items={len(items)}")

    # Summary is not_generated
    ss, sb = _get_summary(token, sid)
    sd = sb.get("data", {})
    _record("E007-4", "Summary marked 'not_generated'",
            ss == 200 and (sd.get("status") == "not_generated" or sd.get("summary_markdown") is None),
            f"status={ss}, summary_status={sd.get('status')}")

    # Session record intact
    _record("E007-5", "Session record intact (name, project_id preserved)",
            gd.get("name") == name and gd.get("project_id") == project_id,
            f"name={gd.get('name')}, project_id={gd.get('project_id')}")

    # QA pairs empty
    qs, qb = _get_qa_pairs(token, sid)
    qa_data = qb.get("data", [])
    qa_count = len(qa_data) if isinstance(qa_data, list) else 0
    _record("E007-6", "No orphaned QA pairs",
            qs == 200 and qa_count == 0,
            f"status={qs}, qa_count={qa_count}")

    # Suggested questions empty
    sqs, sqb = _get_suggested_questions(token, sid)
    sq_data = sqb.get("data", {})
    sq_count = sq_data.get("count", 0) if isinstance(sq_data, dict) else 0
    _record("E007-7", "No orphaned suggested questions",
            sqs == 200 and sq_count == 0,
            f"status={sqs}, sq_count={sq_count}")


# ---------------------------------------------------------------------------
# AGT-E008: Summary failure — transcript accessible, summary unavailable
# ---------------------------------------------------------------------------
def test_agt_e008(token: str, project_id: str):
    """Verify transcript and summary endpoints are independent.

    When summary generation fails, the transcript must remain fully accessible.
    Summary endpoint must clearly indicate 'not_generated' — no partial/corrupt data.
    """
    print(f"\n{'='*70}")
    print("AGT-E008: Summary Failure — Transcript Still Accessible")
    print(f"{'='*70}")

    name = f"E008-SummaryFail-{uuid.uuid4().hex[:8]}"
    s, b = _create_session(token, project_id, name)
    _record("E008-1", "Create session returns 200", s == 200,
            f"Got {s}: {b.get('message', '')}")
    if s != 200:
        return

    sid = b.get("data", {}).get("session_id")
    _cleanup_session_ids.append(sid)

    # Transcript endpoint works independently of summary
    ts, tb = _get_transcripts(token, sid)
    _record("E008-2", "Transcript endpoint returns 200 (independent of summary)",
            ts == 200,
            f"status={ts}")

    # Transcript response structure is valid
    td = tb.get("data", {})
    _record("E008-3", "Transcript response has valid structure",
            isinstance(td, dict) and "items" in td,
            f"data keys={list(td.keys()) if isinstance(td, dict) else type(td)}")

    # Summary clearly marked unavailable
    ss, sb = _get_summary(token, sid)
    sd = sb.get("data", {})
    _record("E008-4", "Summary returns 200 with 'not_generated'",
            ss == 200 and sd.get("status") == "not_generated",
            f"status={ss}, summary_status={sd.get('status')}")

    _record("E008-5", "Summary markdown is null (no partial data)",
            sd.get("summary_markdown") is None,
            f"summary_markdown type={type(sd.get('summary_markdown'))}")

    # Session record accessible for Retro Mode
    gs, gb = _get_session(token, sid)
    gd = gb.get("data", {})
    _record("E008-6", "Session accessible for Retro Mode",
            gs == 200 and gd.get("session_id") == sid,
            f"GET status={gs}")

    # No cascade: QA pairs endpoint still works
    qs, _ = _get_qa_pairs(token, sid)
    _record("E008-7", "QA pairs endpoint not affected by summary failure",
            qs == 200,
            f"status={qs}")


# ---------------------------------------------------------------------------
# AGT-E009: Insights failure — transcript + summary accessible
# ---------------------------------------------------------------------------
def test_agt_e009(token: str, project_id: str):
    """Verify insights failure doesn't cascade to transcript or summary.

    'Insights' = QA pairs + suggested questions + gap analysis.
    When insights generation fails, transcript and summary must remain intact.
    Insights endpoints must return empty/unavailable — no crash, no cascade.
    """
    print(f"\n{'='*70}")
    print("AGT-E009: Insights Failure — No Cascade to Transcript/Summary")
    print(f"{'='*70}")

    name = f"E009-InsightsFail-{uuid.uuid4().hex[:8]}"
    s, b = _create_session(token, project_id, name)
    _record("E009-1", "Create session returns 200", s == 200,
            f"Got {s}: {b.get('message', '')}")
    if s != 200:
        return

    sid = b.get("data", {}).get("session_id")
    _cleanup_session_ids.append(sid)

    # Transcript endpoint works (not affected by insights failure)
    ts, tb = _get_transcripts(token, sid)
    _record("E009-2", "Transcript endpoint returns 200",
            ts == 200,
            f"status={ts}")

    # Summary endpoint works (not affected by insights failure)
    ss, sb = _get_summary(token, sid)
    _record("E009-3", "Summary endpoint returns 200",
            ss == 200,
            f"status={ss}")

    # QA pairs returns empty (no crash)
    qs, qb = _get_qa_pairs(token, sid)
    qa_data = qb.get("data", [])
    # data may be a list directly or a dict — either way, count should be 0
    if isinstance(qa_data, list):
        qa_empty = len(qa_data) == 0
    elif isinstance(qa_data, dict):
        qa_empty = len(qa_data.get("items", qa_data.get("qa_pairs", []))) == 0
    else:
        qa_empty = True
    _record("E009-4", "QA pairs returns 200 with empty result",
            qs == 200 and qa_empty,
            f"status={qs}, type={type(qa_data).__name__}, empty={qa_empty}")

    # Suggested questions returns empty (no crash)
    sqs, sqb = _get_suggested_questions(token, sid)
    sq_data = sqb.get("data", {})
    _record("E009-5", "Suggested questions returns 200 with empty list",
            sqs == 200,
            f"status={sqs}")

    sq_count = sq_data.get("count", 0) if isinstance(sq_data, dict) else -1
    _record("E009-6", "Suggested questions count is 0 (no orphaned data)",
            sq_count == 0,
            f"count={sq_count}")

    # Session record intact — no cascade failure
    gs, gb = _get_session(token, sid)
    gd = gb.get("data", {})
    _record("E009-7", "Session record intact (no cascade failure)",
            gs == 200 and gd.get("name") == name,
            f"GET status={gs}, name={gd.get('name')}")

    _record("E009-8", "Session state consistent",
            gd.get("is_active") != "completed",
            f"is_active={gd.get('is_active')} (should not be completed without processing)")

    # Verify all endpoints are independently accessible (no shared failure mode)
    endpoints_ok = all([ts == 200, ss == 200, qs == 200, sqs == 200, gs == 200])
    _record("E009-9", "All endpoints independently accessible (no shared failure)",
            endpoints_ok,
            f"transcript={ts}, summary={ss}, qa={qs}, suggested={sqs}, session={gs}")


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
        s, _ = _delete_session(token, sid)
        tag = "OK" if s == 200 else f"WARN ({s})"
        print(f"  [{tag}] Deleted {sid}")


def print_report() -> int:
    print(f"\n{'='*70}")
    print("TEST REPORT")
    print(f"{'='*70}\n")

    total = len(results)
    passed = sum(1 for r in results if r.passed)
    failed = total - passed

    for prefix, label in [
        ("E007", "AGT-E007 Transcription Failure"),
        ("E008", "AGT-E008 Summary Failure"),
        ("E009", "AGT-E009 Insights Failure"),
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
        print("\n✅ All partial failure tests passed.")
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
        "E007": ("AGT-E007", test_agt_e007),
        "E008": ("AGT-E008", test_agt_e008),
        "E009": ("AGT-E009", test_agt_e009),
    }

    if selected:
        if selected not in all_tests:
            print(f"\nUnknown: {selected}. Available: {', '.join(all_tests)}")
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
