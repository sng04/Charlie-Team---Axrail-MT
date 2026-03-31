#!/usr/bin/env bash
# Regression check: ensures the domain verification file survives deployments.
#
# Run this after ANY frontend deployment or CDK deploy to confirm the
# verification file is still accessible and returning valid JSON.
#
# Usage:
#   ./scripts/check_verification_persistence.sh
#
# Exit codes:
#   0 = PASS (file accessible, correct Content-Type, valid token)
#   1 = FAIL (file missing, wrong Content-Type, or token mismatch)

set -euo pipefail

VERIFICATION_URL="https://d2bed2yjnef4ve.cloudfront.net/.well-known/aws/securityagent-domain-verification.json"
EXPECTED_TOKEN="jP2oeFgO9BqJJGZmVvkSXA"
BUCKET="meetagentfrontend-sitebucket397a1860-faljsv4qc0to"
S3_KEY=".well-known/aws/securityagent-domain-verification.json"

echo "============================================"
echo "  Domain Verification Regression Check"
echo "============================================"
echo ""

PASS=true

# --- Check 1: S3 object exists ---
echo "[1/4] Checking S3 object existence..."
if aws s3api head-object --bucket "$BUCKET" --key "$S3_KEY" > /dev/null 2>&1; then
  echo "  ✓ S3 object exists"
else
  echo "  ✗ S3 object MISSING — run: npx cdk deploy AXRAIL-SecurityVerification-dev"
  PASS=false
fi

# --- Check 2: HTTP status ---
echo "[2/4] Checking HTTP accessibility..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -H "Cache-Control: no-cache" "$VERIFICATION_URL" 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "200" ]; then
  echo "  ✓ HTTP 200 OK"
else
  echo "  ✗ HTTP $HTTP_CODE (expected 200)"
  PASS=false
fi

# --- Check 3: Content-Type ---
echo "[3/4] Checking Content-Type..."
CONTENT_TYPE=$(curl -s -I -H "Cache-Control: no-cache" "$VERIFICATION_URL" 2>/dev/null | grep -i "^content-type:" | tr -d '\r' | awk '{print $2}')
if echo "$CONTENT_TYPE" | grep -q "application/json"; then
  echo "  ✓ Content-Type: application/json"
else
  echo "  ✗ Content-Type: $CONTENT_TYPE (expected application/json)"
  echo "    This usually means CloudFront's SPA fallback is intercepting the request."
  echo "    The .well-known/* cache behavior may be missing from the distribution."
  PASS=false
fi

# --- Check 4: Token present ---
echo "[4/4] Checking verification token..."
BODY=$(curl -s -H "Cache-Control: no-cache" "$VERIFICATION_URL" 2>/dev/null)
if echo "$BODY" | python3 -c "import sys,json; tokens=json.load(sys.stdin).get('tokens',[]); sys.exit(0 if '$EXPECTED_TOKEN' in tokens else 1)" 2>/dev/null; then
  echo "  ✓ Token '$EXPECTED_TOKEN' present"
else
  echo "  ✗ Token not found in response body"
  echo "    Body: ${BODY:0:200}"
  PASS=false
fi

echo ""
echo "============================================"
if [ "$PASS" = true ]; then
  echo "  RESULT: PASS ✓"
  echo "  Domain verification file is correctly served."
  echo "============================================"
  exit 0
else
  echo "  RESULT: FAIL ✗"
  echo ""
  echo "  REMEDIATION STEPS:"
  echo "  1. Redeploy the SecurityVerification CDK stack:"
  echo "     npx cdk deploy AXRAIL-SecurityVerification-dev"
  echo "  2. If the file keeps disappearing, ensure frontend"
  echo "     deploys use: aws s3 sync --delete --exclude '.well-known/*'"
  echo "  3. Use scripts/deploy_frontend.sh instead of raw s3 sync."
  echo "============================================"
  exit 1
fi
