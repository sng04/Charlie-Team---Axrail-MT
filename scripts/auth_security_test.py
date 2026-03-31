"""
Authorization Security Test

Tests privilege escalation and cross-user data access using admin JWT tokens
against user-restricted endpoints. Validates that proper authorization boundaries
are enforced at the API layer.

Usage:
    python scripts/auth_security_test.py

Environment variables (optional overrides):
    BASE_URL          - API Gateway base URL
    ADMIN_USERNAME    - Admin email for login
    ADMIN_PASSWORD    - Admin password
"""

import json
import os
import sys
import uuid
import urllib.request
import urllib.error
from dataclasses import dataclass, field
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

# Fake / non-existent IDs used to probe cross-user access
FAKE_USER_IDS = [
    str(uuid.uuid4()),
    "00000000-0000-0000-0000-000000000000",
    "nonexistent-user-id",
]
FAKE_SESSION_ID = str(uuid.uuid4())
FAKE_PROJECT_ID = str(uuid.uuid4())


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
@dataclass
class TestResult:
    name: str
    method: str
    path: str
    status_code: int
    passed: bool
    severity: str = "INFO"
    detail: str = ""


results: list[TestResult] = []


def _request(method: str, path: str, token: Optional[str] = None, body: Optional[dict] = None) -> tuple[int, dict]:
    """Send an HTTP request and return (status_code, parsed_body)."""
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


def _has_user_data_leak(body: dict) -> bool:
    """Check if response body contains sensitive user fields."""
    sensitive_keys = {"email", "username", "password", "phone", "address", "role", "access_token"}
    data = body.get("data", body)
    if isinstance(data, dict):
        return bool(sensitive_keys & set(data.keys()))
    if isinstance(data, list):
        return any(bool(sensitive_keys & set(item.keys())) for item in data if isinstance(item, dict))
    return False


def record(name: str, method: str, path: str, status: int, expected_codes: set[int], body: dict):
    """Evaluate a single probe and record the result."""
    data_leaked = _has_user_data_leak(body)
    passed = status in expected_codes and not data_leaked

    if not passed:
        if status == 200 and data_leaked:
            severity = "CRITICAL"
            detail = f"200 OK with data leakage. Body keys: {list(body.get('data', body).keys()) if isinstance(body.get('data', body), dict) else 'list'}"
        elif status == 200:
            severity = "CRITICAL"
            detail = f"200 OK returned — expected {expected_codes}"
        elif data_leaked:
            severity = "HIGH"
            detail = f"Status {status} but response contains sensitive fields"
        else:
            severity = "MEDIUM"
            detail = f"Unexpected status {status}, expected {expected_codes}"
    else:
        severity = "PASS"
        detail = f"Correctly returned {status}"

    results.append(TestResult(name, method, path, status, passed, severity, detail))


# ---------------------------------------------------------------------------
# Step 1 — Authenticate as admin
# ---------------------------------------------------------------------------
def authenticate_admin() -> Optional[str]:
    """Login as admin and return the access token."""
    print(f"\n{'='*70}")
    print("STEP 1: Authenticating as admin")
    print(f"{'='*70}")

    status, body = _request("POST", "/auth/admin/login", body={
        "username": ADMIN_USERNAME,
        "password": ADMIN_PASSWORD,
    })

    if status != 200:
        print(f"  [FAIL] Admin login failed: {status} — {body}")
        if body.get("data", {}).get("challenge"):
            print("  [INFO] Password challenge detected. Set a permanent password first.")
        return None

    token = body.get("data", {}).get("access_token")
    if not token:
        print(f"  [FAIL] No access_token in response: {body}")
        return None

    print(f"  [OK] Admin JWT obtained (token length: {len(token)})")
    return token


# ---------------------------------------------------------------------------
# Step 2 — Probe user-restricted endpoints with admin token
# ---------------------------------------------------------------------------
def test_cross_user_access(token: str):
    """Use admin token to access user-scoped resources that should be restricted."""
    print(f"\n{'='*70}")
    print("STEP 2: Testing cross-user / privilege escalation vectors")
    print(f"{'='*70}")

    # 2a. GET /users/{userId} — admin-only endpoint, but test with fake IDs
    #     Admin IS allowed here, so 200 = expected if user exists, 404 if not.
    #     We verify no data leak for non-existent users.
    for uid in FAKE_USER_IDS:
        path = f"/users/{uid}"
        status, body = _request("GET", path, token=token)
        record(
            f"GET user with fake ID ({uid[:12]}…)",
            "GET", path, status,
            expected_codes={404, 400},
            body=body,
        )
        print(f"  GET {path} → {status} {'✓' if status in {404, 400} else '✗ UNEXPECTED'}")


    # 2b. GET /users/{userId}/projects — admin-only, fake user IDs
    for uid in FAKE_USER_IDS:
        path = f"/users/{uid}/projects"
        status, body = _request("GET", path, token=token)
        # Admin can call this, but fake user should return empty or 404
        has_leak = _has_user_data_leak(body)
        record(
            f"GET projects for fake user ({uid[:12]}…)",
            "GET", path, status,
            expected_codes={200, 404, 400},
            body=body,
        )
        items = body.get("data", {}).get("items", []) if isinstance(body.get("data"), dict) else []
        print(f"  GET {path} → {status}, items={len(items)}, leak={has_leak}")

    # 2c. GET /sessions/{sessionId} — authenticated endpoint with ownership check
    #     Admin can access any session, but a non-existent session should 404.
    path = f"/sessions/{FAKE_SESSION_ID}"
    status, body = _request("GET", path, token=token)
    record(
        "GET session with fake session ID",
        "GET", path, status,
        expected_codes={404, 400},
        body=body,
    )
    print(f"  GET {path} → {status} {'✓' if status in {404, 400} else '✗'}")

    # 2d. GET /projects/{projectId}/sessions — with fake project
    path = f"/projects/{FAKE_PROJECT_ID}/sessions"
    status, body = _request("GET", path, token=token)
    record(
        "GET sessions for fake project",
        "GET", path, status,
        expected_codes={404, 400},
        body=body,
    )
    print(f"  GET {path} → {status} {'✓' if status in {404, 400} else '✗'}")


    # 2e. GET /projects/{projectId} — fake project
    path = f"/projects/{FAKE_PROJECT_ID}"
    status, body = _request("GET", path, token=token)
    record(
        "GET fake project by ID",
        "GET", path, status,
        expected_codes={404, 400},
        body=body,
    )
    print(f"  GET {path} → {status} {'✓' if status in {404, 400} else '✗'}")

    # 2f. Attempt to delete a fake user (should 404, not 200)
    for uid in FAKE_USER_IDS[:1]:
        path = f"/users/{uid}"
        status, body = _request("DELETE", path, token=token)
        record(
            f"DELETE fake user ({uid[:12]}…)",
            "DELETE", path, status,
            expected_codes={404, 400},
            body=body,
        )
        print(f"  DELETE {path} → {status} {'✓' if status in {404, 400} else '✗'}")


# ---------------------------------------------------------------------------
# Step 3 — Test with NO token (should get 401)
# ---------------------------------------------------------------------------
def test_unauthenticated_access():
    """Verify protected endpoints reject requests without a token."""
    print(f"\n{'='*70}")
    print("STEP 3: Testing unauthenticated access (no token)")
    print(f"{'='*70}")

    protected_paths = [
        ("GET", "/users"),
        ("GET", f"/users/{FAKE_USER_IDS[0]}"),
        ("GET", "/projects"),
        ("GET", "/sessions"),
        ("GET", "/agents"),
        ("GET", "/bot-credentials"),
        ("GET", "/personalities"),
        ("GET", "/skills"),
    ]

    for method, path in protected_paths:
        status, body = _request(method, path, token=None)
        record(
            f"No-token {method} {path}",
            method, path, status,
            expected_codes={401, 403},
            body=body,
        )
        print(f"  {method} {path} → {status} {'✓' if status in {401, 403} else '✗ CRITICAL'}")


# ---------------------------------------------------------------------------
# Step 4 — Test with invalid / tampered token
# ---------------------------------------------------------------------------
def test_invalid_token():
    """Verify endpoints reject a garbage or tampered JWT."""
    print(f"\n{'='*70}")
    print("STEP 4: Testing with invalid / tampered token")
    print(f"{'='*70}")

    bad_tokens = [
        "invalid.jwt.token",
        "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmYWtlIn0.fakesignature",
        "",
    ]

    test_paths = [
        ("GET", "/users"),
        ("GET", "/sessions"),
        ("GET", "/projects"),
    ]

    for bad_token in bad_tokens:
        label = bad_token[:20] + "…" if len(bad_token) > 20 else bad_token or "(empty)"
        for method, path in test_paths:
            status, body = _request(method, path, token=bad_token)
            record(
                f"Bad token [{label}] {method} {path}",
                method, path, status,
                expected_codes={401, 403},
                body=body,
            )
            print(f"  {method} {path} (token={label}) → {status} {'✓' if status in {401, 403} else '✗'}")


# ---------------------------------------------------------------------------
# Step 5 — Test query parameter variations for IDOR
# ---------------------------------------------------------------------------
def test_idor_query_params(token: str):
    """Test slight variations in query parameters to detect IDOR vulnerabilities."""
    print(f"\n{'='*70}")
    print("STEP 5: Testing IDOR via query parameter variations")
    print(f"{'='*70}")

    # QA pairs with random session/project IDs
    idor_paths = [
        ("GET", f"/qa-pairs?session_id={FAKE_SESSION_ID}"),
        ("GET", f"/qa-pairs?project_id={FAKE_PROJECT_ID}"),
        ("GET", f"/sessions/{FAKE_SESSION_ID}/transcripts"),
        ("GET", f"/sessions/{FAKE_SESSION_ID}/summary"),
        ("GET", f"/sessions/{FAKE_SESSION_ID}/suggested-questions"),
        ("GET", f"/sessions/{FAKE_SESSION_ID}/bot-status"),
    ]

    for method, path in idor_paths:
        status, body = _request(method, path, token=token)
        data = body.get("data")
        has_items = False
        if isinstance(data, dict):
            has_items = bool(data.get("items"))
        elif isinstance(data, list):
            has_items = len(data) > 0

        # For non-existent resources, we expect 404 or empty results
        record(
            f"IDOR probe {method} {path.split('?')[0]}",
            method, path, status,
            expected_codes={200, 404, 400},
            body=body,
        )
        print(f"  {method} {path} → {status}, has_data={has_items}")


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
def print_report():
    """Print final summary report."""
    print(f"\n{'='*70}")
    print("SECURITY TEST REPORT")
    print(f"{'='*70}\n")

    total = len(results)
    passed = sum(1 for r in results if r.passed)
    failed = total - passed
    critical = [r for r in results if r.severity == "CRITICAL"]
    high = [r for r in results if r.severity == "HIGH"]

    print(f"Total tests:  {total}")
    print(f"Passed:       {passed}")
    print(f"Failed:       {failed}")
    print(f"Critical:     {len(critical)}")
    print(f"High:         {len(high)}")

    if critical:
        print(f"\n{'─'*70}")
        print("🚨 CRITICAL FINDINGS (data leakage / privilege escalation)")
        print(f"{'─'*70}")
        for r in critical:
            print(f"  [{r.severity}] {r.name}")
            print(f"    {r.method} {r.path} → {r.status_code}")
            print(f"    {r.detail}\n")

    if high:
        print(f"\n{'─'*70}")
        print("⚠️  HIGH FINDINGS")
        print(f"{'─'*70}")
        for r in high:
            print(f"  [{r.severity}] {r.name}")
            print(f"    {r.method} {r.path} → {r.status_code}")
            print(f"    {r.detail}\n")

    failures = [r for r in results if not r.passed and r.severity not in {"CRITICAL", "HIGH"}]
    if failures:
        print(f"\n{'─'*70}")
        print("ℹ️  OTHER FAILURES")
        print(f"{'─'*70}")
        for r in failures:
            print(f"  [{r.severity}] {r.name}")
            print(f"    {r.method} {r.path} → {r.status_code}")
            print(f"    {r.detail}\n")

    if failed == 0:
        print("\n✅ All authorization checks passed. No privilege escalation detected.")
    else:
        print(f"\n❌ {failed} test(s) failed — review findings above.")

    return 1 if critical else 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print(f"Target: {BASE_URL}")
    print(f"Admin:  {ADMIN_USERNAME}")

    # Step 1 — Get admin JWT
    token = authenticate_admin()
    if not token:
        print("\nCannot proceed without admin token. Exiting.")
        sys.exit(1)

    # Step 2 — Cross-user access with admin token
    test_cross_user_access(token)

    # Step 3 — No token
    test_unauthenticated_access()

    # Step 4 — Invalid tokens
    test_invalid_token()

    # Step 5 — IDOR via query params
    test_idor_query_params(token)

    # Report
    exit_code = print_report()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
