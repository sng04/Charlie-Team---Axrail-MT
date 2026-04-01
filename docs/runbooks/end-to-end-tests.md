# End-to-End Test Suite Runbook

## Trigger

Manual execution. Run after any deployment to verify no regressions.

## Prerequisites

```bash
pip3 install websocket-client requests boto3 certifi
```

AWS credentials must be available at `.aws/credentials` (the scripts use them for DynamoDB writes and S3 uploads).

## Test Cases

Three test scripts exercise the stack:

| Script | Domain | Fixture Dir |
|---|---|---|
| `scripts/test_case_novapay.py` | NovaPay fintech sales demo (full ~15 min) | `resources/test-case-novapay/` |
| `scripts/test_case_short.py` | Quick check-in test (~5 min) | `resources/test-case-short/` |
| `scripts/backfill_changelog_names.py` | Backfill entity_name on changelog entries | N/A |

`test_case_short.py` uses single-speaker transcript data (all `spk_0`) to test the Cohere Embed v3 speaker role classifier. See [Speaker Role Classification](../features/speaker-role-classification.md).

The full test case script follows a 17-step flow:

1. Authenticate (JWT via `/auth/admin/login`)
2. Upload KB documents to S3
3. Create agent and personality via REST
4. Upload skill documents via pre-signed URL flow
5. Create project and session, load transcript into DynamoDB
6. WebSocket: `processTranscript` — transcript processing
7. WebSocket: `processTranscript` — question detection
8. WebSocket: `sendMessage` — KB chat
9. WebSocket: `detectQuestion` — on-demand answering
10. WebSocket: `analyzeGaps` — knowledge gap analysis
11. WebSocket: `setSuggestedQuestions` + question matching
12. WebSocket: `endMeeting` — meeting summary generation
13. Cleanup — remove test resources
14. Verify summary ingested into KB
15. WebSocket: `retroAnalysis` — post-meeting coaching
16. WebSocket: `retroChat` — follow-up questions
17. Post-completion retro analysis
18. Post-completion QA verification
19. REST: CRUD smoke test across all endpoints

## Running

### NovaPay Sales Demo (Full)

```bash
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials .venv/bin/python3 scripts/test_case_novapay.py
```

### Test Case Short: Quick Check-In (~5 min)

```bash
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials .venv/bin/python3 scripts/test_case_short.py
```

### Configuration

Both scripts read configuration from environment variables with sensible defaults. Override as needed:

| Variable | Default | Description |
|---|---|---|
| `REST_API_URL` | `https://sjsd378hbd.execute-api.ap-southeast-1.amazonaws.com/dev` | REST API base URL |
| `WS_API_URL` | `wss://hey8o0q9tb.execute-api.ap-southeast-1.amazonaws.com/production` | WebSocket API URL |
| `ADMIN_USERNAME` | `admin` | Admin login username |
| `ADMIN_PASSWORD` | `Admin@12345` | Admin login password |
| `KB_BUCKET` | `axrail-kb-dev-848332098006` | Knowledge base S3 bucket |
| `SKILLS_BUCKET` | `axrail-skills-dev-848332098006` | Skills S3 bucket |
| `SESSIONS_TABLE` | `dev-Sessions` | DynamoDB Sessions table |
| `TRANSCRIPTS_TABLE` | `dev-Transcripts` | DynamoDB Transcripts table |
| `AWS_REGION` | `ap-southeast-1` | AWS region |
| `FIXTURES_DIR` | `resources/test-case-{1,2}/` | Path to test fixture files |

## Expected Outcome

Each script prints results for all tests. Review output against the expected results documented in `docs/testing/test-plan.md`.

Key things to verify:
- Authentication returns a valid JWT token
- Transcript processing correctly handles single-channel input (all lines processed uniformly)
- Question detection fires `questionDetected` events with KB-sourced suggested responses
- Question matching produces `questionMatched` events for pre-set topics
- `endMeeting` generates a Markdown summary with attendees, topics, decisions, and action items
- `retroAnalysis` provides coaching feedback citing specific transcript moments
- QA pairs are extracted and accessible via REST

## Failure Scenarios

### Authentication fails (no access token)

Check that the admin user exists in Cognito and the REST API URL is correct. Verify the API Gateway deployment completed.

### KB/Skill ingestion — no vectors indexed

The Ingestion and SkillIngestion Lambdas are triggered by S3 events. Check CloudWatch logs for those Lambdas. Common issues:
- OpenSearch domain not reachable (VPC/security group)
- Bedrock Titan Embed model not available in the region
- S3 event notification not configured (redeploy LambdaStack)

### Question matching tests fail (no `questionMatched` message)

1. `setSuggestedQuestions` stores embeddings asynchronously. If the matching test runs before DynamoDB write completes, no questions are found. The test includes a wait, but under heavy load this may not be enough.
2. Embeddings must be stored as `Decimal` values. If raw `float` values are passed to `put_item`, the write silently fails.
3. Question matching runs on all non-partial lines. If lines are marked as `is_partial: true`, they are skipped. Ensure test fixture lines have `is_partial: false`.

### WebSocket timeout

The tests use 15-45 second timeouts per WebSocket action. Bedrock model calls (especially `analyzeGaps` and `endMeeting`) can take 30-60 seconds. If tests time out, check CloudWatch for Lambda duration metrics.

### `retroAnalysis` returns error

Expected if the session was not ended first. The test suite calls `endMeeting` before retro tests, but if `endMeeting` fails, retro tests will also fail.

## Resolution Steps

1. Check CloudWatch logs for the relevant Lambda — look for exceptions or timeout errors
2. Verify the CDK deployment completed successfully: `npx cdk diff`
3. Re-run the test suite — some failures are transient (model latency, eventual consistency)
4. If persistent, check that `MATCH_THRESHOLD` in `constants.py` is 0.80 and that `_store_suggested_questions` converts embeddings to `Decimal`
5. For S3 event issues, verify event notifications exist: check the LambdaStack S3 bucket configurations
