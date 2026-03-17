# End-to-End Test Suite Runbook

## Trigger

Manual execution. Run after any deployment to verify no regressions.

## Prerequisites

```bash
pip3 install websocket-client requests certifi
```

AWS credentials must be available (the script uses them for WebSocket SSL).

## Running

```bash
AWS_SHARED_CREDENTIALS_FILE=.aws/credentials .venv/bin/python3 scripts/test_all_endpoints.py
```

## Expected Outcome

```
Results: 66/66 passed  — all green!
```

The test suite covers:

| Section | Tests | What It Validates |
|---|---|---|
| Personalities CRUD | 4 | List, create, get, update |
| Agents CRUD | 4 | List, create, get, update (with personality FK) |
| WebSocket Actions | 5 | sendMessage, detectQuestion, extractQAPair, analyzeGaps, endMeeting |
| QA Pairs CRUD | 2 | List by session, get by ID |
| Retro Mode | 2 | retroAnalysis (requires completed session), retroChat |
| Speaker Hints | 2 | processTranscript with explicit role mapping |
| Model Classification | 2 | processTranscript with Nova Pro speaker inference |
| Suggested Questions | 2 | setSuggestedQuestions, empty list rejection |
| Question Matching | 6 | Semantic matching, answer window capture, QA auto-save |
| Client Question Detection | 6 | Heuristic detection, suggested response, short text filter, non-question filter |
| User Response Window | 6 | Client question → user response capture → QA auto-save |
| Full Live Flow | 9 | End-to-end: questions → matching → detection → windows → QA save |
| Edge Cases | 3 | Empty lines, single speaker, large batch |
| Cleanup | 3 | Delete test agent, personality, QA pair |

## Failure Scenarios

### Question matching tests fail (no `questionMatched` message)

Root cause is usually one of:
1. **Embeddings not persisted** — The `setSuggestedQuestions` call stores embeddings asynchronously. If the matching test runs before DynamoDB write completes, no questions are found. The test includes a 5-second wait, but under heavy load this may not be enough.
2. **DynamoDB Decimal serialization** — Embeddings must be stored as `Decimal` values. If raw `float` values are passed to `put_item`, the write silently fails and no questions are stored.
3. **Missing `speaker_hint`** — Question matching only runs for `speaker_role == "user"`. If `speaker_hint` is not provided, the speaker may not be classified as "user".

### WebSocket timeout

The test uses a 90-second timeout per WebSocket message. Bedrock model calls (especially `analyzeGaps` and `endMeeting`) can take 30-60 seconds. If tests time out, check CloudWatch for Lambda duration metrics.

### `retroAnalysis` returns error

Expected behavior if the session was not ended first. The test suite calls `endMeeting` before retro tests, but if `endMeeting` fails, retro tests will also fail.

## Resolution Steps

1. Check CloudWatch logs for the StrandsAgent Lambda — look for `Failed to store suggested question` or other exceptions
2. Verify the CDK deployment completed successfully: `npx cdk diff GMeetAgentStack`
3. Re-run the test suite — some failures are transient (model latency, eventual consistency)
4. If persistent, check that `MATCH_THRESHOLD` in `constants.py` is 0.80 and that `_store_suggested_questions` converts embeddings to `Decimal`
