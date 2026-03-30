"""
Static Asset 403 Diagnostic
-----------------------------
Diagnoses why root URL returns 200 but static assets (e.g. main.js) return 403.
Tests Referer headers, response header differences, and WAF cookie priming.

Usage:
    pip install curl_cffi requests
    python scripts/static_asset_403_diagnostic.py
"""

from curl_cffi import requests as cffi_requests
import json

BASE = "https://d2bed2yjnef4ve.cloudfront.net"
ASSET = f"{BASE}/main.js"

CHROME_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

BROWSER_HEADERS = {
    "User-Agent": CHROME_UA,
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.9",
    "Sec-Fetch-Dest": "script",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "same-origin",
}

INTERESTING_HEADERS = [
    "x-amz-cf-id", "x-amz-cf-pop", "x-cache",
    "server", "content-type", "x-amz-waf-action",
    "set-cookie", "www-authenticate",
]


def dump_headers(resp, label=""):
    """Print the response headers we care about."""
    print(f"  --- Response Headers{f' ({label})' if label else ''} ---")
    for h in INTERESTING_HEADERS:
        val = resp.headers.get(h)
        if val:
            print(f"    {h}: {val}")
    # Also show any header with 'waf' or 'bot' in the name
    for k, v in resp.headers.items():
        if any(t in k.lower() for t in ("waf", "bot", "challenge", "captcha")):
            print(f"    {k}: {v}")
    print()


def dump_cookies(session):
    """Print all cookies in the session jar."""
    cookies = dict(session.cookies)
    if cookies:
        print(f"  Cookies in jar: {json.dumps(cookies, indent=4)}")
    else:
        print("  No cookies in jar.")
    print()


def test_a_direct_asset():
    """Test A: Request main.js directly, no Referer, no session."""
    print("=" * 60)
    print("TEST A: Direct request to main.js (no Referer, no cookies)")
    print("=" * 60)
    resp = cffi_requests.get(
        ASSET, headers=BROWSER_HEADERS, impersonate="chrome124", timeout=15
    )
    print(f"  Status: {resp.status_code}")
    dump_headers(resp)
    return resp.status_code


def test_b_with_referer():
    """Test B: Request main.js with Referer pointing to root."""
    print("=" * 60)
    print("TEST B: Request main.js WITH Referer header")
    print("=" * 60)
    headers = {**BROWSER_HEADERS, "Referer": f"{BASE}/"}
    resp = cffi_requests.get(
        ASSET, headers=headers, impersonate="chrome124", timeout=15
    )
    print(f"  Status: {resp.status_code}")
    dump_headers(resp)
    return resp.status_code


def test_c_primed_session():
    """Test C: Hit root first to collect WAF cookies, then request asset."""
    print("=" * 60)
    print("TEST C: Session priming (root first, then main.js)")
    print("=" * 60)

    session = cffi_requests.Session(impersonate="chrome124")

    # Step 1 — prime with root
    print("  Step 1: GET /")
    root_resp = session.get(BASE + "/", headers=BROWSER_HEADERS, timeout=15)
    print(f"  Root status: {root_resp.status_code}")
    dump_headers(root_resp, "root")
    dump_cookies(session)

    # Step 2 — request asset with Referer + primed cookies
    print("  Step 2: GET /main.js (with session cookies + Referer)")
    headers = {**BROWSER_HEADERS, "Referer": f"{BASE}/"}
    asset_resp = session.get(ASSET, headers=headers, timeout=15)
    print(f"  Asset status: {asset_resp.status_code}")
    dump_headers(asset_resp, "main.js")
    dump_cookies(session)

    return root_resp.status_code, asset_resp.status_code


def summarize(a: int, b: int, c_root: int, c_asset: int):
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"  Test A (direct, no Referer)     : {a}")
    print(f"  Test B (with Referer)           : {b}")
    print(f"  Test C root (session prime)     : {c_root}")
    print(f"  Test C asset (after priming)    : {c_asset}")
    print()

    if a == 403 and b != 403:
        print("  FINDING: Referer header is required for static assets.")
        print("  CloudFront or WAF has a Referer-based access rule.")
    elif a == 403 and b == 403 and c_asset != 403:
        print("  FINDING: WAF cookie priming is required.")
        print("  CloudFront sets an aws-waf-token (or similar) on the root")
        print("  response, and static assets are gated behind that cookie.")
        print("  Your Python client needs to hit / first, capture cookies,")
        print("  then request assets in the same session.")
    elif a == 403 and b == 403 and c_asset == 403:
        print("  FINDING: Neither Referer nor cookie priming helped.")
        print("  Likely causes:")
        print("    - JS-based WAF challenge (bot control with JS SDK)")
        print("    - Origin-level path restriction on *.js")
        print("    - CloudFront behavior/cache policy difference per path")
        print("  Next step: compare 'curl -v' headers for / vs /main.js")
    else:
        print("  FINDING: Asset returned 200 on direct request.")
        print("  The 403 may be intermittent or IP/rate-limit based.")


if __name__ == "__main__":
    status_a = test_a_direct_asset()
    status_b = test_b_with_referer()
    c_root, c_asset = test_c_primed_session()
    summarize(status_a, status_b, c_root, c_asset)
