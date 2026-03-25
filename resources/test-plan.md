# Agent Function Test Plan

## Overview

This document defines tests for every AI agent function using two test cases. Each test maps to a specific agent action, describes the input, and defines the expected behavior.

### Single-Channel Transcript Constraint

The meeting bot captures audio as a single mixed channel. The transcript output has:
- **`speaker`**: Always `spk_0` — no speaker differentiation
- **`start_time` / `end_time`**: Float seconds elapsed from meeting start
- **`confidence`**: STT confidence score (0.0–1.0)
- **`is_partial`**: Whether this is a partial or final result
- **`text`**: Raw transcription with typical STT artifacts (missing punctuation, compound words split, occasional mishearings like "very phone" for "Verifone")

**Implications:**
- Speaker classification is not possible from the transcript alone
- Question detection is speaker-agnostic — the agent detects that a question was asked, but cannot determine who asked it
- Meeting summaries infer participant names from conversational context (introductions) rather than speaker labels
- Coaching feedback references time markers (e.g., "around 3:20") rather than attributing quotes to specific speakers

### Test Data Summary

| | Test Case 1: NovaPay Sales Demo | Test Case 2: GreenBuild Consulting Kickoff |
|---|---|---|
| **Domain** | Fintech / payment processing | Sustainability consulting |
| **Meeting type** | Sales rep demo to retail prospect | Consulting engagement kickoff |
| **KB files** | product-overview, pricing-guide, api-reference, security-compliance | carbon-reporting-methodology, regulatory-landscape, service-tiers-pricing |
| **Skill files** | competitor-comparison, retail-industry-talking-points | manufacturing-emissions-guide, meridian-client-context |
| **Transcript** | 36 lines, ~8 min, single channel (`spk_0`) | 38 lines, ~9 min, single channel (`spk_0`) |
| **KB gap** | Multi-currency / international (not supported) | Carbon offsets / credits (not covered) |

---

## Test Setup (Both Cases)

### Pre-requisites

1. Upload all KB files to the KB S3 bucket → verify Ingestion Lambda fires and indexes them in OpenSearch
2. Create an agent via `POST /agents` with appropriate role/task prompts
3. Create a personality via `POST /personalities`
4. Upload skill files via `POST /skills` → verify SkillIngestion fires
5. Create a project and session via REST API
6. Load the transcript into the Transcripts table (batch write with `session_id` + `timestamp`)
7. Connect to the WebSocket with `?session_id={id}&agent_id={id}`

### Transcript DynamoDB Schema

Each transcript entry written to `{env}-Transcripts`:

| Field | Type | Example |
|---|---|---|
| `session_id` (PK) | String | `"abc-123"` |
| `timestamp` (SK) | String | `"2026-03-15T10:00:12.050000+00:00"` (derived from meeting start + `start_time`) |
| `transcript_id` | String | UUID |
| `speaker` | String | `"spk_0"` (always) |
| `text` | String | Raw STT output |
| `start_time` | Number | `12.05` (seconds from meeting start) |
| `end_time` | Number | `19.82` |
| `confidence` | Number | `0.934` |
| `is_partial` | Boolean | `false` |

---

## Test 1: Knowledge Base Ingestion

**Action:** Upload KB files to S3 bucket
**Trigger:** S3 OBJECT_CREATED → Ingestion Lambda

### Test Case 1

| Upload | Expected Index Content |
|---|---|
| `product-overview.md` | Chunks with "unified payment gateway", "ShieldAI", "tokenization" |
| `pricing-guide.md` | Chunks with "interchange-plus", "$149/month", "volume discounts" |
| `api-reference.md` | Chunks with "POST /payments", "webhooks", "SDKs" |
| `security-compliance.md` | Chunks with "PCI DSS Level 1", "SOC 2 Type II", "AES-256" |

### Test Case 2

| Upload | Expected Index Content |
|---|---|
| `carbon-reporting-methodology.md` | Chunks with "GHG Protocol", "Scope 1/2/3", "10-13 weeks" |
| `regulatory-landscape.md` | Chunks with "SEC Climate Disclosure", "CBAM", "SB 253" |
| `service-tiers-pricing.md` | Chunks with "$45,000-$75,000", "Enterprise Engagement" |

---

## Test 2: Skill Ingestion

**Action:** Upload skill files via `POST /skills` then S3 upload
**Trigger:** S3 OBJECT_CREATED on Skills bucket → SkillIngestion Lambda

### Test Case 1

| Upload | Expected |
|---|---|
| `competitor-comparison.md` | OpenSearch chunks with `agent_id` metadata, text includes "Stripe", "Square" |
| `retail-industry-talking-points.md` | Chunks include "BrightMart", "pain points" |

### Test Case 2

| Upload | Expected |
|---|---|
| `manufacturing-emissions-guide.md` | Chunks with agent_id, text about "53.06 kg CO2 per MMBtu" |
| `meridian-client-context.md` | Chunks with "340M revenue", "brake assemblies" |

---

## Test 3: processTranscript — Ingestion and Question Detection

**Action:** `processTranscript` with transcript lines
**Expected:** Lines are stored, questions are detected (speaker-agnostic)

Since all lines are `spk_0`, the agent cannot determine who is asking. It can only detect that a question exists in the transcript and generate a suggested response from the KB.

### Test Case 1

| Transcript Line (start_time) | Detection | Expected suggestedResponse |
|---|---|---|
| `"What does the pricing look like for our volume?"` (99.80s) | heuristic (`?`) | Interchange-plus pricing, Enterprise tier, volume discounts |
| `"Is that included in the enterprise plan or is it extra?"` (180.50s) | heuristic (`?`) | ShieldAI included on Enterprise, no extra per-txn charge |
| `"Can nova pay handle multi currency transactions?"` (202.80s) | heuristic (`?`) | NOT supported today, Canada/UK Q3 2026 |
| `"What kind of up time guarantees do you offer?"` (383.80s) | heuristic (`?`) | 99.99% SLA, active-active AWS |

### Test Case 2

| Transcript Line (start_time) | Detection | Expected suggestedResponse |
|---|---|---|
| `"So how exactly does the process work?"` (97.30s) | heuristic (`?`) | GHG Protocol, 4 phases, 10-13 weeks |
| `"What kind of data will you need from us?"` (148.80s) | heuristic (`?`) | Utility bills, fleet fuel, production logs, refrigerant records |
| `"Does that affect us?"` (264.80s — re: CBAM) | heuristic (`?`) | CBAM covers steel/aluminum, add-on $15K/product line |
| `"Can we purchase off sets to bring them down?"` (329.70s) | heuristic (`?`) | Limited/no KB coverage — this is the gap |

---

## Test 4: sendMessage — General KB Chat

**Action:** `sendMessage` with direct questions
**Expected:** Agent searches KB and/or skills, returns accurate answers

### Test Case 1

| Message | Expected Source | Key Content |
|---|---|---|
| `"What payment methods does NovaPay support?"` | product-overview.md | Visa, MC, Amex, Apple Pay, Google Pay, ACH, Affirm, Klarna |
| `"How does NovaPay compare to Stripe on pricing?"` | Skill: competitor-comparison.md | Interchange-plus vs flat-rate, 15-30% savings |
| `"Does NovaPay support payments in Euros?"` | product-overview.md | NO — USD only, international expansion planned |

### Test Case 2

| Message | Expected Source | Key Content |
|---|---|---|
| `"What Scope 3 categories does GreenBuild cover?"` | carbon-reporting-methodology.md | Categories 1, 4, 5, 6, 7 standard; all 15 enterprise |
| `"What are the SEC climate reporting deadlines?"` | regulatory-landscape.md | Large accel 2025, accel 2026, SRC 2027 |
| `"What's Meridian's estimated carbon footprint?"` | Skill: meridian-client-context.md | 70,000-97,000 tCO2e/year |

---

## Test 5: detectQuestion — On-Demand Answering

**Action:** `detectQuestion` with a specific question string
**Expected:** Concise factual answer from KB

### Test Case 1

- `"What is the chargeback fee and when is it waived?"` → $15, waived if won
- `"What encryption does NovaPay use for card data at rest?"` → AES-256, AWS KMS

### Test Case 2

- `"What penalties does a company face for not complying with SB 253?"` → Up to $500,000/year
- `"How many suppliers should we survey for Scope 3?"` → Top 30-50 by spend

---

## Test 6: analyzeGaps — Knowledge Gap Analysis

**Action:** `analyzeGaps` after transcript is loaded
**Expected:** JSON with gaps (topics discussed but not covered in KB) and suggested questions

### Test Case 1 — Expected Gaps

| Gap | Confidence | Why |
|---|---|---|
| Multi-currency processing | High | Explicitly asked about, KB says "not supported" with no workaround detail |
| Loyalty program integration | High | Asked about custom loyalty hooks, KB only mentions metadata fields |
| POS hardware compatibility details | Medium | "very phone terminals" mentioned, no terminal setup docs in KB |

### Test Case 2 — Expected Gaps

| Gap | Confidence | Why |
|---|---|---|
| Carbon offsets / credits | High | Asked twice, no KB content on offset advisory |
| Full Scope 3 (all 15 categories) | Medium | OEM customers may need this, standard only covers 5 |
| Science-based target setting process | Medium | Mentioned as add-on, no methodology detail |

---

## Test 7: endMeeting — Meeting Summary

**Action:** `endMeeting` after transcript is loaded
**Expected:** Markdown summary — participant names inferred from conversational context (introductions), not from speaker labels

### Test Case 1 — Expected

| Section | Key Content |
|---|---|
| **Participants** | Alex (NovaPay) and Marcus (inferred from "Thanks for joining today Marcus", "I'm Alex from nova pay") |
| **Topics Discussed** | Unified gateway, interchange-plus pricing, ShieldAI fraud, multi-currency gap, PCI simplification, integration timeline |
| **Decisions** | Interest in Enterprise plan, Canada is a concern |
| **Action Items** | Formal proposal with savings, API docs + sandbox, Canada timeline, follow-up Thursday, technical call for loyalty integration |
| **Unresolved** | Multi-currency, loyalty integration |

### Test Case 2 — Expected

| Section | Key Content |
|---|---|
| **Participants** | Priya (GreenBuild consultant) and David (Meridian VP Ops) — inferred from introductions |
| **Topics Discussed** | GHG methodology, data collection, CBAM exposure, carbon offsets (unresolved), assurance, pricing |
| **Decisions** | Include assurance readiness ($18K), CBAM pending, April start for August board meeting |
| **Action Items** | Proposal by Friday, confirm CBAM with EU team, start gathering utility bills |
| **Unresolved** | Carbon offset advisory, CBAM scope |

---

## Test 8: retroAnalysis — Post-Meeting Coaching

**Action:** `retroAnalysis` (session must be marked inactive first)
**Expected:** Coaching feedback referencing time markers since speakers can't be attributed

### Test Case 1 — Expected

| Area | What to Look For |
|---|---|
| **Question Handling** | Pricing questions answered well with specifics (~1:40-2:30). Multi-currency answer was transparent but the interim solution (dual processor) was vague (~3:55-4:20). Loyalty question deflected to "technical call" without immediate value (~5:50-6:20). |
| **Knowledge Gaps** | Multi-currency is the main gap — almost derailed the conversation |
| **Coaching** | Prepare a Canada expansion FAQ. Have a loyalty integration one-pager. Quantify savings proactively instead of waiting to be asked. |

### Test Case 2 — Expected

| Area | What to Look For |
|---|---|
| **Question Handling** | CBAM answer was strong with clear pricing (~4:39-5:28). Carbon offsets response was vague ("it's a complicated area") — asked twice with no concrete follow-up (~5:30-6:28). |
| **Knowledge Gaps** | Carbon offsets is the clear gap — board-level concern for the client |
| **Coaching** | Never say "let me look into it" without at least a high-level framework. The "look into offset advisory" action item needs a specific date. |

---

## Test 9: retroChat — Follow-Up Questions

**Action:** `retroChat` after `retroAnalysis` is complete

### Test Case 1

| Message | Expected |
|---|---|
| `"What were the strongest moments?"` | References pricing explanation (~1:50-2:30) and PCI simplification (~4:34-5:20) |
| `"How should I handle the Canada question better?"` | Concrete approach: acknowledge, pivot to interim strategy with specifics, commit to written timeline |

### Test Case 2

| Message | Expected |
|---|---|
| `"What should I have said about carbon offsets?"` | Structured framework even with limited knowledge — avoidance vs removal, SBTi position, promise specific brief by date |
| `"Did I price the engagement correctly?"` | Within $125K budget, presented clearly, range was appropriate |

---

## Test 10: setSuggestedQuestions — Question Matching

**Action:** `setSuggestedQuestions` then `processTranscript`
**Expected:** `questionMatched` when transcript text semantically matches a suggested question

### Test Case 1

**Setup questions:**
1. `"What is NovaPay's pricing structure?"`
2. `"Does NovaPay support international payments?"`
3. `"What security certifications does NovaPay hold?"`

**Expected matches when processing transcript:**
- Q1 matches around start_time 110.45 (interchange-plus pricing discussed)
- Q2 matches around start_time 217.50 (Canada/UK expansion)
- Q3 matches around start_time 274.30 (PCI DSS, SOC 2)

Note: since all speakers are `spk_0`, matching triggers regardless of who said it.

---

## Test 11: CRUD Operations Smoke Test

| Endpoint | Test | Expected |
|---|---|---|
| `POST /agents` | Create with all fields | 200 |
| `GET /agents` | List | 200, paginated |
| `PUT /agents/{id}` | Update `role_prompt` | 200 |
| `DELETE /agents/{id}` | Delete | 200 |
| `POST /personalities` | Create | 200 |
| `GET /personalities` | List | 200 |
| `POST /skills` | Create with file metadata | 200, includes `upload_url` |
| `GET /qa-pairs?session_id={id}` | After endMeeting | 200, list of QA pairs |
| `DELETE /qa-pairs/{id}` | Delete one | 200 |

---

## Test Evaluation Criteria

| Dimension | 1 (Poor) | 3 (Acceptable) | 5 (Excellent) |
|---|---|---|---|
| **Factual Accuracy** | Hallucinated facts | Mostly correct | All claims traceable to KB/skills |
| **Source Attribution** | No indication | Mentions general area | Cites specific documents |
| **Completeness** | Misses major info | Covers main points | Thorough coverage |
| **Conciseness** | Verbose/rambling | Reasonable length | Tight, no filler |
| **Gap Honesty** | Claims to know things not in KB | Partially acknowledges limits | Clearly states when info unavailable |
| **Transcript Grounding** | Generic feedback | Some time references | Specific time markers from transcript |
| **STT Tolerance** | Fails on STT artifacts | Handles most | Correctly interprets "nova pay", "very phone", etc. |
