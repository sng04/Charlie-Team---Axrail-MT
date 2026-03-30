"""
CloudFront 403 Diagnostic Script
---------------------------------
Run all 3 tests against your CloudFront URL to identify which
bot-detection layer is causing the 403.

Usage:
    pip install requests curl_cffi
    python scripts/cloudfront_403_diagnostic.py <CLOUDFRONT_URL>
"""

import sys
import requests

CHROME_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

BROWSER_HEADERS = {
    "User-Agent": CHROME_UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
}


def test_1_default_requests(url: str) -> int:
    """Baseline: plain requests.get() with default headers."""
    print("\n=== Test 1: Default Requests (Baseline) ===")
    try:
        resp = requests.get(url, timeout=15)
        print(f"  Status : {resp.status_code}")
        print(f"  UA sent: {resp.request.headers.get('User-Agent', 'N/A')}")
        return resp.status_code
    except Exception as e:
        print(f"  Error  : {e}")
        return -1


def test_2_header_mirroring(url: str) -> int:
    """Mimic a real browser's headers (User-Agent + Sec-Fetch-*)."""
    print("\n=== Test 2: Header Mirroring (User-Agent & Sec-Fetch) ===")
    try:
        resp = requests.get(url, headers=BROWSER_HEADERS, timeout=15)
        print(f"  Status : {resp.status_code}")
        print(f"  UA sent: {resp.request.headers.get('User-Agent', 'N/A')}")
        return resp.status_code
    except Exception as e:
        print(f"  Error  : {e}")
        return -1


def test_3_tls_fingerprint(url: str) -> int:
    """Attempt a request with a Chrome-like TLS fingerprint using curl_cffi."""
    print("\n=== Test 3: TLS Fingerprint Check (JA3 Bypass) ===")

    # 3a: Try curl_cffi for Chrome-impersonated TLS
    try:
        from curl_cffi import requests as cffi_requests

        print("  curl_cffi available — impersonating Chrome TLS fingerprint")
        resp = cffi_requests.get(
            url,
            headers=BROWSER_HEADERS,
            impersonate="chrome124",
            timeout=15,
        )
        print(f"  Status : {resp.status_code}")
        return resp.status_code
    except ImportError:
        print("  curl_cffi not installed — falling back to JA3 hash check")
    except Exception as e:
        print(f"  curl_cffi error: {e}")

    # 3b: Fallback — fetch your JA3 hash so you can compare it
    print("  Fetching your JA3 hash from ja3er.com ...")
    try:
        resp = requests.get("https://ja3er.com/json", timeout=15)
        if resp.ok:
            data = resp.json()
            print(f"  Your JA3 hash : {data.get('ja3_hash', 'unknown')}")
            print(f"  Your JA3 text : {data.get('ja3', 'unknown')[:120]}...")
        else:
            print(f"  ja3er.com returned {resp.status_code}")
    except Exception as e:
        print(f"  JA3 check error: {e}")

    return -1


def summarize(t1: int, t2: int, t3: int):
    """Print a diagnosis based on the three test results."""
    print("\n" + "=" * 55)
    print("RESULTS SUMMARY")
    print("=" * 55)
    print(f"  Test 1 (Default Requests)   : {t1}")
    print(f"  Test 2 (Header Mirroring)   : {t2}")
    print(f"  Test 3 (TLS Fingerprint)    : {t3}")
    print()

    if t1 == 403 and t2 == 403 and t3 != 403:
        print("  DIAGNOSIS: TLS Fingerprinting")
        print("  The WAF/CloudFront is inspecting the TLS handshake (JA3).")
        print("  Headers alone aren't enough — you need curl_cffi or a")
        print("  browser-based session to get past this layer.")
    elif t1 == 403 and t2 != 403:
        print("  DIAGNOSIS: Simple User-Agent / Header Check")
        print("  Setting browser-like headers is sufficient. Move your auth")
        print("  logic into a requests.Session with BROWSER_HEADERS and")
        print("  inject the resulting cookies into the browser.")
    elif t1 != 403:
        print("  DIAGNOSIS: No bot detection on this URL (or it's IP-based).")
        print("  The default Python UA was not blocked.")
    else:
        print("  DIAGNOSIS: Unclear — all tests returned 403.")
        print("  Possible causes:")
        print("    - IP-based rate limiting or geo-blocking")
        print("    - JavaScript challenge (Cloudfront + WAF Bot Control)")
        print("    - Cookie/session requirement before the page loads")
        print("  Try running: curl -v <URL> from your terminal and compare.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <CLOUDFRONT_URL>")
        sys.exit(1)

    target = sys.argv[1]
    print(f"Target URL: {target}")

    r1 = test_1_default_requests(target)
    r2 = test_2_header_mirroring(target)
    r3 = test_3_tls_fingerprint(target)
    summarize(r1, r2, r3)
