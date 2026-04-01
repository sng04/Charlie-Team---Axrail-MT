# Agent Function Test Plan

## Overview

This document defines tests for every AI agent function using the NovaPay Sales Demo test case. Each test maps to a specific agent action, describes the input, and defines the expected behavior. Use these to evaluate quality, tune prompts, and benchmark performance.

### Test Data Summary

| | NovaPay Sales Demo |
|---|---|
| **Domain** | Fintech / payment processing |
| **KB files** | product-overview, pricing-guide, api-reference, security-compliance |
| **Skill files** | competitor-comparison, retail-industry-talking-points |
| **Transcript** | 36 lines, single-channel (`spk_0`) |
| **KB gap** | Multi-currency / international (not supported) |

---

## Test Setup

### Pre-requisites

1. Upload all KB files for the test case to the KB S3 bucket → verify Ingestion Lambda fires and indexes them in OpenSearch
2. Create an agent via `POST /agents` with appropriate role/task prompts
3. Create a personality via `POST /personalities`
4. Upload skill files via `POST /skills` → verify SkillIngestion fires
5. Create a session via `POST /sessions` linked to the project
6. Load the transcript into the Transcripts table (batch write with `session_id`, `speaker`, `text`, `start_time`, `end_time`, `confidence`)
7. Connect to the WebSocket with `?session_id={id}&agent_id={id}`

---

## Test 1: Knowledge Base Ingestion

**Action:** Upload KB files to S3 bucket
**Trigger:** S3 OBJECT_CREATED → Ingestion Lambda

### NovaPay

| Upload | Expected Result |
|---|---|
| `product-overview.md` | CloudWatch shows Ingestion Lambda invoked. OpenSearch `knowledge-vectors` index contains chunks with text about "unified payment gateway", "ShieldAI", "tokenization". |
| `pricing-guide.md` | Chunks indexed with text about "interchange-plus", "$149/month", "volume discounts". |
| `api-reference.md` | Chunks indexed with "POST /payments", "webhooks", "SDKs". |
| `security-compliance.md` | Chunks indexed with "PCI DSS Level 1", "SOC 2 Type II", "AES-256". |

### Verification

```bash
# Check OpenSearch index has documents
curl -XGET "https://{opensearch-endpoint}/knowledge-vectors/_count"
```

---

## Test 2: Skill Ingestion

**Action:** Upload skill files via `POST /skills` then S3 upload
**Trigger:** S3 OBJECT_CREATED on Skills bucket → SkillIngestion Lambda

### NovaPay

| Upload | Expected Result |
|---|---|
| `competitor-comparison.md` (attached to sales agent) | OpenSearch contains chunks with `agent_id` metadata and `doc_type: skill`. Text includes "Stripe", "Square", "interchange-plus transparency". |
| `retail-industry-talking-points.md` | Chunks include "BrightMart", "pain points", "discovery questions". |

### Verification

Skills table record should show `status: "indexed"` after ingestion completes.

---

## Test 3: processTranscript — Transcript Processing

**Action:** `processTranscript` with first 4-6 transcript lines
**Expected:** Lines are processed, `transcriptProcessed` response returned with correct line count

### NovaPay

**Input lines:** First 6 lines from the sales demo transcript (single-channel, `spk_0`)

**Expected result:**
- Response type: `transcriptProcessed` with `lines_processed: 6`
- No `speaker_role_map` or `classification_confidence` in response

---

## Test 4: processTranscript — Question Detection

**Action:** `processTranscript` with lines containing questions
**Expected:** Agent detects questions and generates suggested responses from KB

### NovaPay

| Transcript Line | Detection Method | Expected suggestedResponse Topic |
|---|---|---|
| `"What does the pricing look like for our volume?"` | heuristic (ends with `?`) | Should reference interchange-plus pricing, Enterprise tier, volume discounts from `pricing-guide.md` |
| `"Is that included in the enterprise plan or is it extra?"` | heuristic | Should reference ShieldAI included on Enterprise, Stripe charges $0.05 extra (from skill: competitor-comparison) |
| `"Can NovaPay handle multi-currency transactions?"` | heuristic | Should state multi-currency NOT currently supported, Canada/UK Q3 2026 from `product-overview.md` |
| `"What kind of uptime guarantees do you offer?"` | heuristic | Should reference 99.99% SLA, active-active AWS from `security-compliance.md` |

Note: All lines are processed uniformly regardless of speaker. The `questionDetected` message type is used for all detected questions.

---

## Test 5: sendMessage — General KB Chat

**Action:** `sendMessage` with direct questions
**Expected:** Agent searches KB and/or skills, returns accurate answers

### NovaPay

| Message | Expected Answer Source | Key Content to Verify |
|---|---|---|
| `"What payment methods does NovaPay support?"` | `product-overview.md` | Lists Visa, MC, Amex, Discover, Apple Pay, Google Pay, ACH, Affirm, Klarna |
| `"How does NovaPay compare to Stripe on pricing?"` | Skill: `competitor-comparison.md` | Mentions interchange-plus vs flat-rate, 15-30% savings for high-volume |
| `"What's the onboarding timeline for a Drop-In SDK integration?"` | `api-reference.md` | States 1-2 weeks |
| `"Does NovaPay support payments in Euros?"` | `product-overview.md` | Correctly states NO — USD only, international expansion planned |

---

## Test 6: detectQuestion — On-Demand Question Answering

**Action:** `detectQuestion` with a specific question string
**Expected:** Agent searches KB and returns a concise, factual answer

### NovaPay

**Input:** `"What is the chargeback fee and when is it waived?"`
**Expected:** References $15 per chargeback, waived if merchant wins dispute. Source: `pricing-guide.md`.

**Input:** `"What encryption does NovaPay use for card data at rest?"`
**Expected:** AES-256 with AWS KMS key management, annual rotation. Source: `security-compliance.md`.

---

## Test 7: analyzeGaps — Knowledge Gap Analysis

**Action:** `analyzeGaps` after transcript is loaded
**Expected:** JSON with gaps (topics not well covered in KB) and suggested questions

### NovaPay

**Expected gaps (high confidence):**
- **Multi-currency processing** — Client asked directly, KB explicitly states it's not supported but provides no migration playbook
- **International settlement / payouts** — KB says "international payouts not currently supported" but no detail on workarounds
- **Loyalty program integration** — Client asked about custom loyalty hooks; KB only mentions metadata fields, no loyalty-specific docs

**Expected gaps (medium confidence):**
- **POS hardware compatibility** — Client uses Verifone; KB doesn't detail specific terminal models or setup procedures

**Expected suggested_questions:** Should include questions like "What is the detailed timeline for Canada expansion?" and "How does NovaPay integrate with third-party loyalty systems?"

---

## Test 8: endMeeting — Meeting Summary

**Action:** `endMeeting` after transcript is loaded
**Expected:** Markdown summary with structured sections

### NovaPay — Expected Summary Sections

| Section | Key Content |
|---|---|
| **Attendees** | Alex Chen (NovaPay), Marcus Webb (FreshCart) — identified from conversational context |
| **Key Discussion Topics** | Unified payment gateway, interchange-plus pricing, ShieldAI fraud detection, multi-currency gap, PCI compliance simplification, integration timeline |
| **Decisions Made** | Marcus interested in Enterprise plan; will evaluate Canada gap; wants technical review |
| **Action Items** | Alex: send formal proposal with savings projection, API docs, sandbox credentials, Canada timeline from product team. Marcus: share API docs with CTO. Follow-up Thursday. |
| **Unresolved Questions** | Multi-currency / Canada timeline, loyalty program integration details |
| **QA Pairs** | Should capture 5-8 Q&A exchanges from the transcript |

---

## Test 9: retroAnalysis — Post-Meeting Coaching

**Action:** `retroAnalysis` (session must be marked inactive via `endMeeting` first)
**Expected:** Structured feedback referencing specific transcript moments

### NovaPay — Expected Feedback Areas

| Area | What to Look For |
|---|---|
| **Communication Effectiveness** | Should note Alex handled pricing questions well with specific numbers, but was vague on the multi-currency interim solution |
| **Question Handling Quality** | Should praise immediate answers to pricing/security questions. Should flag that the loyalty program question got a "let me set up a technical call" deflection without providing any immediate value |
| **Knowledge Gap Assessment** | Should identify multi-currency as the biggest gap and note it almost derailed the deal |
| **Coaching Insights** | Should suggest: prepare a Canada expansion FAQ for future demos, have a loyalty integration one-pager ready, quantify the savings before the client asks |
| **Missed Agenda Items** | Could note that implementation support details (who handles migration, dedicated PM) weren't covered |

---

## Test 10: retroChat — Follow-Up Questions

**Action:** `retroChat` after `retroAnalysis` has been completed
**Expected:** Specific, evidence-based answers referencing the transcript and retro feedback

### NovaPay

| Message | Expected Response |
|---|---|
| `"What were the strongest moments in this meeting?"` | Should reference the pricing comparison moment (10:03-10:04) where Alex gave specific numbers, and the security/PCI simplification explanation (10:08-10:09) |
| `"How should I handle the Canada question better next time?"` | Should provide a concrete script or approach — e.g., acknowledge the gap, pivot to interim dual-processor strategy with specifics, offer a written timeline commitment |

---

## Test 11: setSuggestedQuestions — Question Matching

**Action:** `setSuggestedQuestions` with prepared questions, then `processTranscript` with lines where the user speaks those topics
**Expected:** `questionMatched` events when user addresses a suggested topic

### NovaPay

**Setup:** Set suggested questions:
1. `"What is NovaPay's pricing structure for enterprise retailers?"`
2. `"Does NovaPay support international payments?"`
3. `"What security certifications does NovaPay hold?"`

**Then process transcript.** Expected matches:
- Question 1 should match when the pricing discussion occurs (interchange-plus pricing explanation)
- Question 2 should match when the Canada/UK expansion is discussed
- Question 3 should match when PCI DSS and SOC 2 certifications are mentioned

---

## Test 12: CRUD Operations Smoke Test

Verify all CRUD endpoints work with auth:

| Endpoint | Test | Expected |
|---|---|---|
| `POST /agents` | Create agent with all required fields | 200, agent returned with `agent_id` |
| `GET /agents` | List all agents | 200, paginated list including seeded + created agents |
| `PUT /agents/{agentId}` | Update `role_prompt` | 200, updated agent returned |
| `DELETE /agents/{agentId}` | Delete created agent | 200 |
| `POST /personalities` | Create personality | 200 |
| `GET /personalities` | List | 200, includes seeded personalities |
| `POST /skills` | Create skill with file metadata | 200, returns pre-signed upload URL |
| `GET /qa-pairs?session_id={id}` | After `endMeeting` has saved QA pairs | 200, list of extracted Q&A pairs |
| `DELETE /qa-pairs/{id}` | Delete a QA pair | 200 |

---

## Test Evaluation Criteria

For each AI-generated output, evaluate on these dimensions:

| Dimension | Score 1 (Poor) | Score 3 (Acceptable) | Score 5 (Excellent) |
|---|---|---|---|
| **Factual Accuracy** | Hallucinated facts not in KB/skills | Mostly correct, minor inaccuracies | All claims traceable to source documents |
| **Source Attribution** | No indication of where info came from | Mentions general area | Cites specific documents or data points |
| **Completeness** | Misses major relevant information | Covers main points | Thorough coverage of all relevant KB content |
| **Conciseness** | Excessively verbose or rambling | Reasonable length | Tight, focused, no filler |
| **Gap Honesty** | Claims to know things not in KB | Partially acknowledges limits | Clearly states when info is not available |
| **Transcript Grounding** | Generic feedback not tied to meeting | Some references to transcript | Specific timestamps and quotes from transcript |
