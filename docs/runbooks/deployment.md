# Deployment Runbook

## Trigger

Manual. Run when code changes need to be deployed to the AWS environment.

## Prerequisites

- AWS credentials configured in `.aws/credentials`
- Node.js 18+ and CDK CLI installed (`npm install -g aws-cdk`)
- Python 3.11 virtual environment at `.venv/`
- Dependencies installed: `pip install -r requirements.txt`

## Deploy All Stacks

```bash
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials \
  JSII_SILENCE_WARNING_UNTESTED_NODE_VERSION=1 \
  npx cdk deploy --all --require-approval never \
  -a ".venv/bin/python3 app.py"
```

This deploys 7 stacks in dependency order:

1. `AXRAIL-DynamoDB-dev` — 12 DynamoDB tables + OpenSearch domain
2. `AXRAIL-Cognito-dev` — User Pool + groups
3. `AXRAIL-MeetingBot-dev` — ECS cluster + VPC + SQS
4. `AXRAIL-Lambda-dev` — 46 Lambdas + WebSocket API + S3 buckets + EventBridge
5. `AXRAIL-ApiServices-dev` — REST API Gateway + routes
6. `AXRAIL-BedrockAgent-dev` — Bedrock Agent in us-east-1
7. `AXRAIL-SecurityVerification-dev` — Domain verification file + CloudFront behavior

## EventBridge Rule: Bot Credential Validation

The Lambda stack deploys an EventBridge rule that triggers the `ValidateBotCredentialWorker` Lambda when a `BotCredentialValidation` event is published (source: `axrail.bot-credentials`). This enables async SMTP validation of bot credentials after creation.

The `ValidateBotCredentialWorker` Lambda requires the `dnspython` package (included in the SharedLayer) for MX record lookups when detecting SMTP servers for custom email domains.

## Deploy a Single Stack

```bash
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials \
  JSII_SILENCE_WARNING_UNTESTED_NODE_VERSION=1 \
  npx cdk deploy AXRAIL-Lambda-dev --require-approval never \
  -a ".venv/bin/python3 app.py"
```

## Deploy to a Different Environment

```bash
npx cdk deploy --all -c environment=staging
```

Available environments: `dev`, `staging`, `prod`. See `stack_cdk/environment.py` for config differences.

## Expected Outcome

```
✅  AXRAIL-DynamoDB-dev
✅  AXRAIL-Cognito-dev
✅  AXRAIL-MeetingBot-dev
✅  AXRAIL-Lambda-dev
✅  AXRAIL-ApiServices-dev
✅  AXRAIL-BedrockAgent-dev
✅  AXRAIL-SecurityVerification-dev

Outputs:
AXRAIL-ApiServices-dev.RestApiUrl = https://{id}.execute-api.ap-southeast-1.amazonaws.com/dev
AXRAIL-Lambda-dev.WebSocketUrl = wss://{id}.execute-api.ap-southeast-1.amazonaws.com/production
AXRAIL-SecurityVerification-dev.VerificationFileUrl = https://d2bed2yjnef4ve.cloudfront.net/.well-known/aws/securityagent-domain-verification.json
AXRAIL-SecurityVerification-dev.VerificationStatus = PASS
```

## Frontend Deployment — Protecting Verification Files

The frontend is deployed separately to the S3 bucket `meetagentfrontend-sitebucket397a1860-faljsv4qc0to`. When syncing frontend assets, you **must** exclude the `.well-known/` prefix to prevent overwriting the domain verification file.

### Safe S3 sync command

```bash
aws s3 sync ./dist s3://meetagentfrontend-sitebucket397a1860-faljsv4qc0to \
  --delete \
  --exclude ".well-known/*"
```

If your frontend CI/CD pipeline uses `aws s3 sync --delete` without `--exclude ".well-known/*"`, the verification file will be deleted on every deploy. Update the pipeline accordingly.

### If using a frontend framework (React, Vite, Next.js)

Place the verification file in the `public/` directory of the frontend project so it is included in every build output:

```
public/.well-known/aws/securityagent-domain-verification.json
```

Contents:
```json
{"tokens":["jP2oeFgO9BqJJGZmVvkSXA"]}
```

This provides a belt-and-suspenders approach: the CDK stack deploys the file, and the frontend build also includes it.

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

### MeetingBot stack synth error (ExpiredToken)

The MeetingBot stack performs VPC lookups during synthesis, which requires valid credentials. If you see `ExpiredToken` during `cdk synth`, refresh credentials. This is not a code issue.

### CloudFormation rollback

Check the CloudFormation console for the failing stack. Common causes:

- Lambda code syntax errors (run `pytest tests/unit/ -v` first)
- Layer size exceeds 250 MB limit
- IAM permission conflicts with existing resources
- Circular dependency between stacks

Resolution:

1. Fix the root cause
2. Re-run the deploy command
3. If stuck in `ROLLBACK_COMPLETE`, delete the stack and redeploy (destructive for data stacks)

### Cross-stack export conflict

```
Cannot update export AXRAIL-Lambda-dev:ExportsOutputRef...
```

This occurs when another stack imports a resource from the Lambda stack and CloudFormation cannot update the export. CDK deploy will fail even though the code changes are valid.

Workaround — deploy the Lambda code directly via AWS CLI:

```bash
# Package the Lambda
cd lambdas/Functions/<FunctionDir>
zip -r /tmp/<function-name>.zip . -x "__pycache__/*" "*.pyc"

# Deploy
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials \
  aws lambda update-function-code \
  --function-name AXRAIL-<FunctionName>-dev \
  --zip-file fileb:///tmp/<function-name>.zip \
  --region ap-southeast-1
```

This bypasses CloudFormation entirely and updates only the Lambda code. Use this when CDK deploy fails due to cross-stack export issues but the code change is isolated to a single Lambda.

### WebSocket deployment ordering

The WebSocket API requires a deployment resource that depends on all route integrations. If routes are added without updating the deployment, the WebSocket API returns `{"message":"Forbidden"}`. The CDK stack handles this automatically via `addDependency` on the deployment resource.

## Pre-Deployment Checks

```bash
# Synthesize templates (catches CDK errors)
npx cdk synth -a ".venv/bin/python3 app.py" --quiet

# Run unit tests
pytest tests/unit/ -v
```

## Post-Deployment Verification

```bash
# Run integration tests (requires test fixtures in resources/)
python scripts/test_case_1.py
python scripts/test_case_2.py
```

## Destroy Stacks

```bash
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials \
  npx cdk destroy --all --force \
  -a ".venv/bin/python3 app.py"
```

Stacks are destroyed in reverse dependency order. DynamoDB tables in `dev` have `RemovalPolicy.DESTROY`; in `staging`/`prod` they use `RETAIN`.
