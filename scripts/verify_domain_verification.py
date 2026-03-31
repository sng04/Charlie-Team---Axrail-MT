#!/usr/bin/env python3
"""Post-deployment domain verification checker.

Usage:
    python scripts/verify_domain_verification.py [--url URL]

Validates that the AWS Security Agent domain verification file is accessible
and returns the correct Content-Type and token payload.

Exit codes:
    0 = PASS
    1 = FAIL
"""

import argparse
import json
import sys
import urllib.request
import urllib.error

DEFAULT_URL = (
    "https://d2bed2yjnef4ve.cloudfront.net"
    "/.well-known/aws/securityagent-domain-verification.json"
)
EXPECTED_TOKEN = "jP2oeFgO9BqJJGZmVvkSXA"


def check(url: str, token: str) -> dict:
    """Run all verification checks and return a result dict."""
    result = {
        "url": url,
        "http_status": None,
        "content_type": None,
        "valid_json": False,
        "token_present": False,
        "status": "FAIL",
        "reason": "",
    }

    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=15) as resp:
            result["http_status"] = resp.status
            result["content_type"] = resp.headers.get("Content-Type", "")
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Verify domain verification file")
    parser.add_argument("--url", default=DEFAULT_URL, help="Verification URL")
    args = parser.parse_args()

    result = check(args.url, EXPECTED_TOKEN)

    print(json.dumps(result, indent=2))
    print(f"\nVerification: {result['status']}")

    sys.exit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
