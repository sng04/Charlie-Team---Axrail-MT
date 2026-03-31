#!/usr/bin/env python3
"""Post-deployment domain verification checker with stability testing.

Usage:
    python scripts/verify_domain_verification.py [--url URL] [--stability-rounds N]

Validates that the AWS Security Agent domain verification file is accessible
and returns the correct Content-Type and token payload.  When --stability-rounds
is given (default 10), sends N sequential requests and fails if ANY return HTML.

Exit codes:
    0 = PASS
    1 = FAIL
"""

import argparse
import json
import sys
import time
import urllib.request
import urllib.error

DEFAULT_URL = (
    "https://d2bed2yjnef4ve.cloudfront.net"
    "/.well-known/aws/securityagent-domain-verification.json"
)
EXPECTED_TOKEN = "jP2oeFgO9BqJJGZmVvkSXA"


def single_check(url: str, token: str) -> dict:
    """Run all verification checks and return a result dict."""
    result = {
        "url": url,
        "http_status": None,
        "content_type": None,
        "valid_json": False,
        "token_present": False,
        "x_cache": None,
        "x_verification_source": None,
        "status": "FAIL",
        "reason": "",
    }

    try:
        req = urllib.request.Request(url, method="GET")
        req.add_header("Cache-Control", "no-cache")
        req.add_header("Pragma", "no-cache")
        with urllib.request.urlopen(req, timeout=15) as resp:
            result["http_status"] = resp.status
            result["content_type"] = resp.headers.get("Content-Type", "")
            result["x_cache"] = resp.headers.get("X-Cache", "")
            result["x_verification_source"] = resp.headers.get(
                "X-Verification-Source", ""
            )
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        result["http_status"] = exc.code
        result["reason"] = f"HTTP {exc.code}"
        return result
    except Exception as exc:
        result["reason"] = str(exc)
        return result

    if result["http_status"] != 200:
        result["reason"] = f"Expected HTTP 200, got {result['http_status']}"
        return result

    if "application/json" not in result["content_type"]:
        result["reason"] = (
            f"Content-Type is '{result['content_type']}', "
            "expected application/json"
        )
        return result

    try:
        payload = json.loads(body)
        result["valid_json"] = True
    except json.JSONDecodeError:
        result["reason"] = "Response body is not valid JSON"
        return result

    tokens = payload.get("tokens", [])
    if token in tokens:
        result["token_present"] = True
        result["status"] = "PASS"
        result["reason"] = "All checks passed"
    else:
        result["reason"] = f"Token '{token}' not found in response tokens"

    return result


def stability_test(url: str, token: str, rounds: int) -> dict:
    """Send N sequential requests and report pass/fail per round."""
    results = []
    pass_count = 0
    fail_count = 0

    print(f"\n{'='*60}")
    print(f"STABILITY TEST: {rounds} sequential requests")
    print(f"{'='*60}")

    for i in range(1, rounds + 1):
        r = single_check(url, token)
        results.append(r)
        marker = "PASS" if r["status"] == "PASS" else "FAIL"
        if r["status"] == "PASS":
            pass_count += 1
        else:
            fail_count += 1

        src = r.get("x_verification_source") or "s3/cache"
        print(
            f"  [{i:>2}/{rounds}] {marker}  "
            f"status={r['http_status']}  "
            f"ct={r['content_type']:<20}  "
            f"source={src}"
        )
        if i < rounds:
            time.sleep(0.5)

    overall = "PASS" if fail_count == 0 else "FAIL"
    print(f"\nStability: {pass_count}/{rounds} passed  → {overall}")
    return {
        "rounds": rounds,
        "passed": pass_count,
        "failed": fail_count,
        "status": overall,
        "details": results,
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Verify domain verification file"
    )
    parser.add_argument("--url", default=DEFAULT_URL, help="Verification URL")
    parser.add_argument(
        "--stability-rounds",
        type=int,
        default=10,
        help="Number of sequential requests for stability test (0 to skip)",
    )
    args = parser.parse_args()

    # Single check
    result = single_check(args.url, EXPECTED_TOKEN)
    print(json.dumps(result, indent=2))
    print(f"\nVerification: {result['status']}")

    # Stability test
    if args.stability_rounds > 0:
        stability = stability_test(args.url, EXPECTED_TOKEN, args.stability_rounds)
        if stability["status"] != "PASS":
            print("\nSTABILITY TEST FAILED — responses are inconsistent")
            sys.exit(1)

    sys.exit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
