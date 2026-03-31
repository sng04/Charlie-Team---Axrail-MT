# AXRAIL AI Meeting Assistant — Load Testing Strategy

## System Under Test

| Component | Details |
|---|---|
| Platform | AWS Serverless (Lambda, API Gateway, DynamoDB, ECS Fargate, OpenSearch) |
| Region | ap-southeast-1 (Bedrock in us-east-1) |
| Auth | Cognito JWT (admin + user groups) |
| REST API | 50+ endpoints via API Gateway |
| WebSocket API | 11 routes via StrandsAgent Lambda (512MB, 120s timeout) |
| Database | 14 DynamoDB tables (on-demand billing) + OpenSearch (t3.small, 1 node) |
| Meeting Bot | ECS Fargate (512 CPU, 1024MB) with SQS warm pool |
| AI Models | Amazon Nova Pro (LLM), Titan Embed Text V2 (embeddings), Cohere Embed v3 (classification) |

## Estimated User Profile

| Metric | Estimate |
|---|---|
| Total registered users | 50–200 |
| Concurrent admin users | 1–5 |
| Concurrent regular users | 10–30 |
| Concurrent active meetings | 5–15 |
| Peak WebSocket connections | 30–50 |

---

## Load Testing Strategies

### 1. Load Testing (Normal Traffic)
- **What:** Simulates expected daily traffic patterns across all API endpoints
- **Why:** Validates the system handles normal operations within SLA targets
- **When:** Before every production deployment, after infrastructure changes

### 2. Stress Testing (Beyond Limits)
- **What:** Pushes beyond expected capacity (3–5x normal) to find breaking points
- **Why:** Identifies the ceiling before degradation; critical for serverless cold-start behavior
- **When:** Quarterly, or after major architecture changes

### 3. Spike Testing (Sudden Bursts)
- **What:** Simulates sudden traffic surges (e.g., 10 meetings starting simultaneously)
- **Why:** Tests Lambda cold-start behavior, DynamoDB on-demand scaling lag, ECS task launch latency
- **When:** Before events where multiple meetings may start concurrently

### 4. Soak Testing (Long Duration)
- **What:** Sustained moderate load over 2–4 hours
- **Why:** Detects memory leaks in ECS containers, WebSocket connection drift, OpenSearch index degradation
- **When:** Monthly, or after changes to long-running components (ECS bot, WebSocket agent)

### 5. Concurrency Testing
- **What:** Multiple users hitting the same resources simultaneously (same session transcripts, same project)
- **Why:** Tests DynamoDB conditional writes, WebSocket broadcast fan-out, authorizer caching
- **When:** Before features that increase per-session user count

### 6. Volume Testing (Large Data)
- **What:** Tests with sessions containing 1000+ transcript lines, 50+ QA pairs, large KB documents
- **Why:** Validates pagination, OpenSearch query performance, Lambda memory limits
- **When:** Before onboarding large clients

### 7. WebSocket Sustained Connection Testing
- **What:** Maintains 50+ WebSocket connections with continuous processTranscript messages
- **Why:** Tests StrandsAgent Lambda concurrency, Bedrock API rate limits, DynamoDB write throughput
- **When:** Before scaling meeting capacity

### 8. Cold Start / Warm Pool Testing
- **What:** Measures ECS Fargate cold-start time vs warm pool dispatch latency
- **Why:** Directly impacts the "bot joins meeting within X seconds" SLA
- **When:** After changes to ECS task definition, VPC config, or warm pool logic

### 9. Cross-Region Latency Testing
- **What:** Measures round-trip latency for Bedrock calls from ap-southeast-1 to us-east-1
- **Why:** Bedrock models are in us-east-1; this adds 100–300ms per AI call
- **When:** Baseline measurement, then after model changes

### 10. Rate Limiting / Throttling Validation
- **What:** Tests API Gateway throttling, Lambda concurrency limits, Bedrock TPS limits
- **Why:** Ensures graceful degradation under throttling, not cascading failures
- **When:** After changing API Gateway throttle settings or Lambda reserved concurrency

---

## Test Plan

See `k6-scripts/` for executable test scripts.
See `reports/` for simulated execution results.
