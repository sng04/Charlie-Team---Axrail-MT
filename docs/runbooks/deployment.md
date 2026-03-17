# Deployment Runbook

## Trigger

Manual. Run when code changes need to be deployed to the AWS environment.

## Prerequisites

- AWS credentials configured in `.aws/credentials`
- Node.js and CDK CLI installed
- Python 3.11 virtual environment at `.venv/`

## Deploy Command

```bash
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials \
  JSII_SILENCE_WARNING_UNTESTED_NODE_VERSION=1 \
  npx cdk deploy GMeetAgentStack --require-approval never \
  -a ".venv/bin/python3 app.py"
```

## Expected Outcome

```
✅  GMeetAgentStack
✨  Deployment time: ~45s
```

Outputs:
- `RestApiUrl` — REST API endpoint
- `WebSocketUrl` — WebSocket endpoint

## Failure Scenarios

### Credentials expired

```
ExpiredTokenException: The security token included in the request is expired
```

Resolution: Get fresh credentials and write them to `.aws/credentials`:

```ini
[default]
aws_access_key_id = ...
aws_secret_access_key = ...
aws_session_token = ...
```

### CloudFormation rollback

Check the CloudFormation console for the `GMeetAgentStack` stack. Common causes:
- Lambda code has syntax errors (test locally first)
- Layer size exceeds 250 MB limit
- IAM permission changes that conflict with existing resources

Resolution:
1. Fix the root cause
2. Re-run the deploy command
3. If stuck in `ROLLBACK_COMPLETE`, delete the stack and redeploy (destructive — all data lost)

### Layer build issues

Lambda layers with native dependencies need to be built for the `linux/amd64` target. Each layer directory has a `build.sh` script:

```bash
cd layers/opensearch && bash build.sh
cd layers/strands && bash build.sh
```

These scripts use `pip install --target` to install packages into the `python/` directory that CDK packages as the layer.

## Post-Deployment Verification

Run the end-to-end test suite:

```bash
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials \
  .venv/bin/python3 scripts/test_all_endpoints.py
```

Expected: 66/66 tests passing.
