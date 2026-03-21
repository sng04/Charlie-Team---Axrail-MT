# ADR-006: Repository Integration (D1 + D2 Merge)

## Context

The project was developed by two teams in parallel:
- D1 built the meeting management platform (projects, sessions, users, bot dispatch, ECS meeting bot)
- D2 built the AI meeting agent engine (agents, personalities, skills, knowledge base, live transcript processing, gap analysis, retro mode)

Both teams used the same AWS account and CDK but maintained separate codebases. The D2 codebase needed to be integrated into D1's repository as the canonical codebase.

## Decision

Execute a 7-phase integration plan:

1. **Project Structure** — Rename D1's CDK package to `stack_cdk/`, copy D2 Lambda functions, layers, and ancillary files into D1's directory structure.
2. **Environment Config** — Extend D1's `environment.py` with D2's OpenSearch, Bedrock, and AI Lambda configuration.
3. **Data Stores** — Add D2's 5 new DynamoDB tables and OpenSearch domain to D1's `DynamoDBStack`.
4. **Stack Wiring** — Add D2's Lambda layers, functions, IAM grants, WebSocket API, S3 buckets, and EventBridge rule to D1's `LambdaStack`. Add D2 REST routes to `ApiServicesStack`.
5. **Lambda Code Standardization** — Align D2's Lambda code with D1's conventions (timestamp fields, datetime usage, tracer annotations).
6. **API Gateway Integration** — Fix D2 REST routes to top-level paths, apply correct Cognito authorizers, create `SeedAgentData` Custom Resource.
7. **Tests & Documentation** — Migrate D2 tests with rewritten imports, add D1 handler tests, merge documentation.

### Key Decisions

- **D1 conventions are canonical.** All conflicts (naming, patterns, structure) resolved in favor of D1.
- **WebSocket API and S3 buckets in LambdaStack.** Originally planned for `ApiServicesStack`, but moved to `LambdaStack` to avoid CDK cyclic dependencies (S3 event notifications need Lambda references).
- **D2 routes are top-level.** `/personalities`, `/skills`, `/qa-pairs` instead of nested under `/agents/{agentId}/` or `/sessions/{sessionId}/`, matching Lambda handler routing expectations.
- **SeedAgentData as Custom Resource.** Replaces D2's inline `SEED_HANDLER_CODE` with a standalone Lambda using deterministic UUIDs (`uuid5`) for idempotent seeding.
- **Shared Lambda Layers.** D2's `response_utils` and `custom_exceptions` were already compatible with D1's SharedLayer. No code changes needed.

## Consequences

- Single repository with unified CDK deployment
- 12 DynamoDB tables + 1 OpenSearch domain in one stack
- 46 Lambda functions across 4 layers
- Both REST and WebSocket APIs served from the same deployment
- D2's AI features (agents, skills, gap analysis, retro mode) are immediately available
- Test suite covers both D1 and D2 handlers (48 tests)
- Trade-off: larger deployment footprint, but simplified operations and single `cdk deploy` command
