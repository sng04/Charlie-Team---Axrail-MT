# Domain Verification Report

**Date:** 2026-03-31
**Target URL:** `https://d2bed2yjnef4ve.cloudfront.net/.well-known/aws/securityagent-domain-verification.json`
**Expected Token:** `jP2oeFgO9BqJJGZmVvkSXA`

---

## Summary

The AWS Security Agent domain verification file is currently **NOT accessible**. The file was deleted from S3 by a frontend deployment that used `aws s3 sync --delete` without excluding `.well-known/*`. CloudFront's SPA fallback (custom error response 403 → 200 + index.html) is masking the missing file by returning HTML instead of a 403.

## Root Cause

Two compounding issues:

1. **File deleted from S3:** A frontend deployment ran `aws s3 sync --delete` against the S3 bucket without `--exclude ".well-known/*"`, which removed the verification JSON file.

2. **CloudFront SPA fallback masking the error:** The CloudFront distribution has a custom error response that converts S3 403 (object not found with OAI) into HTTP 200 + `index.html`. Without the dedicated `.well-known/*` cache behavior (which bypasses this fallback), the verification URL returns the SPA's HTML page instead of a proper 403 or the JSON file.

**Evidence from HTTP response:**
```
HTTP 200
Content-Type: text/html
X-Cache: Error from cloudfront
Body: <!DOCTYPE html>...<title>MeetAgent</title>...
```

## Current Verification Result

| Check              | Result | Detail                                          |
|--------------------|--------|-------------------------------------------------|
| HTTP Status        | ✓ 200  | But misleading — it's the SPA fallback          |
| Content-Type       | ✗ FAIL | `text/html` instead of `application/json`       |
| Valid JSON         | ✗ FAIL | Response body is HTML                           |
| Token Present      | ✗ FAIL | Token not found (body is HTML)                  |
| Stability (3 rds)  | ✗ FAIL | 0/3 passed — consistently returning HTML        |
| **Overall**        | **FAIL** | Domain verification will not pass             |

## Fix Applied

### 1. Infrastructure — forced re-deploy on every `cdk deploy` (FIXED)

The `SecurityVerificationStack` CDK stack (`stack_cdk/security_verification_stack.py`) was correctly architected but had a critical gap: CDK's `BucketDeployment` custom resource only re-executes when its input properties change. If the S3 file was deleted out-of-band (by a frontend sync), `cdk deploy` would report "no changes" and skip re-uploading the file.

**Fix applied:** Added `_DEPLOY_EPOCH = str(int(time.time()))` and a `.deploy-marker` source file to both `BucketDeployment` constructs. Since the epoch changes on every synth, the asset hash always differs, forcing CloudFormation to re-execute the custom resource and re-upload the verification files on every deploy.

Stack features:
- Deploys `.well-known/aws/securityagent-domain-verification.json` to S3 with `prune=False` and `content_type="application/json"`
- Adds a dedicated `.well-known/*` CloudFront cache behavior (via custom resource Lambda) that bypasses the SPA fallback
- Uses `CachingDisabled` managed cache policy so verification requests always hit S3 origin
- Runs a post-deploy validation Lambda that confirms HTTP 200 + correct Content-Type + token
- **Now forces re-upload on every deploy** regardless of whether CloudFormation detects changes

### 2. Frontend deploy script (already in place)

`scripts/deploy_frontend.sh` correctly:
- Pre-flight checks that the verification file exists in S3 before syncing
- Uses `aws s3 sync --delete --exclude ".well-known/*"` to protect the verification directory
- Post-deploy verifies the file survived
- Runs the full HTTP verification + stability test

### 3. Regression check (NEW)

- Created `scripts/check_verification_persistence.sh` — standalone regression script that validates S3 object existence, HTTP status, Content-Type, and token presence
- Created agent hook `verify-domain-file` — automatically runs verification after any shell-based deployment command

### 4. Documentation (already in place)

`docs/runbooks/deployment.md` documents:
- The safe S3 sync command with `--exclude ".well-known/*"`
- Instructions to place the file in `public/.well-known/aws/` for frontend framework builds
- The belt-and-suspenders approach (CDK deploys it + frontend build includes it)

## Remediation Steps (Action Required)

To restore the verification file and CloudFront behavior, run:

```bash
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials \
  JSII_SILENCE_WARNING_UNTESTED_NODE_VERSION=1 \
  npx cdk deploy AXRAIL-SecurityVerification-dev --require-approval never \
  -a ".venv/bin/python3 app.py"
```

This will:
1. Re-upload the verification JSON to S3 with correct Content-Type
2. Re-create the `.well-known/*` CloudFront cache behavior
3. Invalidate the CloudFront cache for the verification path
4. Run the post-deploy validator Lambda to confirm everything works

After deployment, verify with:
```bash
python3 scripts/verify_domain_verification.py --stability-rounds 10
```

## Recommendations

1. **Immediate:** Redeploy `AXRAIL-SecurityVerification-dev` to restore the file and CloudFront behavior.

2. **Frontend CI/CD:** If there is a separate CI/CD pipeline for the frontend (outside this repo), update it to either:
   - Use `scripts/deploy_frontend.sh` instead of raw `aws s3 sync`
   - Add `--exclude ".well-known/*"` to any `aws s3 sync --delete` command

3. **Belt-and-suspenders:** Place the verification file in the frontend project's `public/` directory:
   ```
   public/.well-known/aws/securityagent-domain-verification.json
   ```
   Contents: `{"tokens":["jP2oeFgO9BqJJGZmVvkSXA"]}`
   This way even if the CDK-deployed copy is deleted, the frontend build will restore it.

4. **Staging/Prod:** Configure `frontend_bucket_name` and `cloudfront_distribution_id` in `stack_cdk/environment.py` for staging and prod environments (currently empty strings, so the SecurityVerificationStack is only deployed for dev).

5. **Monitoring:** Consider adding a CloudWatch synthetic canary or Route 53 health check that periodically hits the verification URL and alerts if it stops returning valid JSON.

## Verification Readiness Status

| Environment | Status     | Notes                                           |
|-------------|------------|-------------------------------------------------|
| dev         | **FAIL**   | File deleted, needs CDK redeploy                |
| staging     | N/A        | No frontend bucket configured                   |
| prod        | N/A        | No frontend bucket configured                   |
