#!/usr/bin/env bash
# Safe frontend deployment script.
# Syncs build output to S3 while preserving .well-known/* verification files.
#
# Usage:
#   ./scripts/deploy_frontend.sh [BUILD_DIR]
#
# BUILD_DIR defaults to ./dist (standard Vite output).

set -euo pipefail

BUCKET="meetagentfrontend-sitebucket397a1860-faljsv4qc0to"
CF_DISTRIBUTION_ID="E2RLR03PHFYGN1"
BUILD_DIR="${1:-./dist}"
VERIFICATION_KEY=".well-known/aws/securityagent-domain-verification.json"

if [ ! -d "$BUILD_DIR" ]; then
  echo "ERROR: Build directory '$BUILD_DIR' does not exist."
  echo "Run your frontend build first."
  exit 1
fi

# --- Pre-flight: confirm verification file exists in S3 ---
echo "Pre-flight: checking verification file in S3 ..."
if aws s3api head-object --bucket "$BUCKET" --key "$VERIFICATION_KEY" \
     > /dev/null 2>&1; then
  echo "  ✓ Verification file exists in S3."
else
  echo "  ✗ Verification file NOT found in S3."
  echo "  Deploy the SecurityVerification CDK stack first:"
  echo "    npx cdk deploy AXRAIL-SecurityVerification-dev"
  exit 1
fi

# --- Sync frontend assets, excluding .well-known/* ---
echo "Syncing $BUILD_DIR → s3://$BUCKET (excluding .well-known/*) ..."
aws s3 sync "$BUILD_DIR" "s3://$BUCKET" \
  --delete \
  --exclude ".well-known/*"

# --- Invalidate CloudFront cache ---
echo "Invalidating CloudFront cache ..."
aws cloudfront create-invalidation \
  --distribution-id "$CF_DISTRIBUTION_ID" \
  --paths "/*" \
  --no-cli-pager

# --- Post-deploy: verify the file survived ---
echo "Post-deploy: verifying S3 object ..."
if aws s3api head-object --bucket "$BUCKET" --key "$VERIFICATION_KEY" \
     > /dev/null 2>&1; then
  echo "  ✓ Verification file still present after deploy."
else
  echo "  ✗ CRITICAL: Verification file was deleted during deploy!"
  exit 1
fi

# --- HTTP-level validation with stability test ---
echo "Running HTTP verification + stability test ..."
python3 scripts/verify_domain_verification.py --stability-rounds 10

echo "Frontend deployment complete."
