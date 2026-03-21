# Agent Function Test Plan

## Overview

This document defines tests for every AI agent function using two test cases. Each test maps to a specific agent action, describes the input, and defines the expected behavior. Use these to evaluate quality, tune prompts, and benchmark performance.

### Test Data Summary

| | Test Case 1: NovaPay Sales Demo | Test Case 2: GreenBuild Consulting Kickoff |
|---|---|---|
| **Domain** | Fintech / payment processing | Sustainability consulting |
| **User role** | Sales rep (Alex Chen) | Consultant (Priya Sharma) |
| **Client role** | Retail chain CTO (Marcus Webb) | Manufacturing VP Ops (David Park) |
| **KB files** | product-overview, pricing-guide, api-reference, security-compliance | carbon-reporting-methodology, regulatory-landscape, service-tiers-pricing |
| **Skill files** | competitor-comparison, retail-industry-talking-points | manufacturing-emissions-guide, meridian-client-context |
| **Transcript** | 33 lines, ~13 min sales demo | 32 lines, ~14 min project kickoff |
| **KB gap** | Multi-currency / international (not supported) | Carbon offsets / credits (not covered) |

---

## Test Setup (Both Cases)

### Pre-requisites

1. Upload all KB files for the test case to the KB S3 bucket → verify Ingestion Lambda fires and indexes them in OpenSearch
2. Create an agent via `POST /agents` with appropriate role/task prompts
3. Create a personality via `POST /personalities`
4. Upload skill files via `POST /skills` → verify SkillIngestion fires
5. Create a session via `POST /sessions` linked to the project
6. Load the transcript into the Transcripts table (batch write with `session_id` + `timestamp`)
7. Connect to the WebSocket with `?session_id={id}&agent_id={id}`

---

## Test 1: Knowledge Base Ingestion

**Action:** Upload KB files to S3 bucket
**Trigger:** S3 OBJECT_CREATED → Ingestion Lambda

### Test Case 1

| Upload | Expected Result |
|---|---|
| `product-overview.md` | CloudWatch shows Ingestion Lambda invoked. OpenSearch `knowledge-vectors` index contains chunks with text about "unified payment gateway", "ShieldAI", "tokenization". |
| `pricing-guide.md` | Chunks indexed with text about "interchange-plus", "$149/month", "volume discounts". |
| `api-reference.md` | Chunks indexed with "POST /payments", "webhooks", "SDKs". |
| `security-compliance.md` | Chunks indexed with "PCI DSS Level 1", "SOC 2 Type II", "AES-256". |

### Test Case 2

| Upload | Expected Result |
|---|---|
| `carbon-reporting-methodology.md` | Chunks about "GHG Protocol", "Scope 1/2/3", "10-13 weeks". |
| `regulatory-landscape.md` | Chunks about "SEC Climate Disclosure", "CBAM", "SB 253". |
| `service-tiers-pricing.md` | Chunks about "$45,000-$75,000", "Enterprise Engagement", "add-on services". |

### Verification

```bash
# Check OpenSearch index has documents
curl -XGET "https://{opensearch-endpoint}/knowledge-vectors/_count"
```

---

## Test 2: Skill Ingestion

**Action:** Upload skill files via `POST /skills` then S3 upload
**Trigger:** S3 OBJECT_CREATED on Skills bucket → SkillIngestion Lambda

### Test Case 1

| Upload | Expected Result |
|---|---|
| `competitor-comparison.md` (attached to sales agent) | OpenSearch contains chunks with `agent_id` metadata and `doc_type: skill`. Text includes "Stripe", "Square", "interchange-plus transparency". |
| `retail-industry-talking-points.md` | Chunks include "BrightMart", "pain points", "discovery questions". |

### Test Case 2

| Upload | Expected Result |
|---|---|
| `manufacturing-emissions-guide.md` (attached to consulting agent) | Chunks with agent_id, text about "natural gas 53.06 kg CO2 per MMBtu", "refrigerants", "R-404A GWP 3,922". |
| `meridian-client-context.md` | Chunks with agent_id, text about "340M revenue", "brake assemblies", "70,000-97,000 tCO2e". |

### Verification

Skills table record should show `status: "indexed"` after ingestion completes.

---

## Test 3: processTranscript — Speaker Classification

**Action:** `processTranscript` with first 5-10 transcript lines, no `speaker_hint`
**Expected:** Agent classifies speakers into `user` and `client` roles

### Test Case 1

**Input lines:** First 6 lines (Alex introduces himself as NovaPay rep, Marcus describes his retail chain)

**Expected result:**
- `speaker_role_map`: `{"Alex Chen": "user", "Marcus Webb": "client"}`
- `classification_confidence`: `"high"` (clear role signals — "I'm Alex from NovaPay")
- Response type: `transcriptProcessed` with `lines_processed: 6`

### Test Case 2

**Input lines:** First 4 lines (Priya identifies as consultant, David describes his company)

**Expected result:**
- `speaker_role_map`: `{"Priya Sharma": "user", "David Park": "client"}`
- `classification_confidence`: `"high"`

---

## Test 4: processTranscript — Client Question Detection

**Action:** `processTranscript` with lines containing client questions
**Expected:** Agent detects questions and generates suggested responses from KB

### Test Case 1

| Transcript Line | Detection Method | Expected suggestedResponse Topic |
|---|---|---|
| `"What does the pricing look like for our volume?"` (Marcus, 10:03:08) | heuristic (ends with `?`) | Should reference interchange-plus pricing, Enterprise tier, volume discounts from `pricing-guide.md` |
| `"Is that included in the enterprise plan or is it extra?"` (Marcus, 10:05:25) | heuristic | Should reference ShieldAI included on Enterprise, Stripe charges $0.05 extra (from skill: competitor-comparison) |
| `"Can NovaPay handle multi-currency transactions?"` (Marcus, 10:06:15) | heuristic | Should state multi-currency NOT currently supported, Canada/UK Q3 2026 from `product-overview.md` |
| `"What kind of uptime guarantees do you offer?"` (Marcus, 10:11:02) | heuristic | Should reference 99.99% SLA, active-active AWS from `security-compliance.md` |

### Test Case 2

| Transcript Line | Detection Method | Expected suggestedResponse Topic |
|---|---|---|
| `"How exactly does the process work?"` (David, 09:02:35) | heuristic | Should reference GHG Protocol, 4 phases, 10-13 weeks from `carbon-reporting-methodology.md` |
| `"What kind of data will you need from us?"` (David, 09:04:05) | heuristic | Should reference utility bills, fleet fuel, production logs from methodology + skill (manufacturing-emissions-guide) |
| `"Does that affect us?"` (David, about CBAM, 09:07:18) | model (no `?` but interrogative context) | Should reference CBAM covers steel/aluminum, add-on assessment from `regulatory-landscape.md` |
| `"Can you help us evaluate offset options?"` (David, 09:09:48) | heuristic | Should indicate limited/no KB coverage — this is the gap topic |

---

## Test 5: sendMessage — General KB Chat

**Action:** `sendMessage` with direct questions
**Expected:** Agent searches KB and/or skills, returns accurate answers

### Test Case 1

| Message | Expected Answer Source | Key Content to Verify |
|---|---|---|
| `"What payment methods does NovaPay support?"` | `product-overview.md` | Lists Visa, MC, Amex, Discover, Apple Pay, Google Pay, ACH, Affirm, Klarna |
| `"How does NovaPay compare to Stripe on pricing?"` | Skill: `competitor-comparison.md` | Mentions interchange-plus vs flat-rate, 15-30% savings for high-volume |
| `"What's the onboarding timeline for a Drop-In SDK integration?"` | `api-reference.md` | States 1-2 weeks |
| `"Does NovaPay support payments in Euros?"` | `product-overview.md` | Correctly states NO — USD only, international expansion planned |

### Test Case 2

| Message | Expected Answer Source | Key Content to Verify |
|---|---|---|
| `"What Scope 3 categories does GreenBuild cover?"` | `carbon-reporting-methodology.md` | Lists Categories 1, 4, 5, 6, 7 for standard; all 15 for enterprise |
| `"What are the SEC climate reporting deadlines?"` | `regulatory-landscape.md` | Large accelerated filers 2025, accelerated 2026, SRC 2027 |
| `"What's Meridian's estimated carbon footprint?"` | Skill: `meridian-client-context.md` | References 70,000-97,000 tCO2e/year estimate |
| `"What are some ways Meridian could reduce emissions?"` | Skill: `meridian-client-context.md` | Mentions EAF steel switch, renewable energy PPA, LED/VFD upgrades |

---

## Test 6: detectQuestion — On-Demand Question Answering

**Action:** `detectQuestion` with a specific question string
**Expected:** Agent searches KB and returns a concise, factual answer

### Test Case 1

**Input:** `"What is the chargeback fee and when is it waived?"`
**Expected:** References $15 per chargeback, waived if merchant wins dispute. Source: `pricing-guide.md`.

**Input:** `"What encryption does NovaPay use for card data at rest?"`
**Expected:** AES-256 with AWS KMS key management, annual rotation. Source: `security-compliance.md`.

### Test Case 2

**Input:** `"What penalties does a company face for not complying with SB 253?"`
**Expected:** Administrative penalties up to $500,000/year. Source: `regulatory-landscape.md`.

**Input:** `"How many suppliers should we survey for Scope 3 Category 1?"`
**Expected:** Top 30-50 by spend, representing 70-80% of procurement emissions. Source: `carbon-reporting-methodology.md` + skill: `manufacturing-emissions-guide.md`.

---

## Test 7: analyzeGaps — Knowledge Gap Analysis

**Action:** `analyzeGaps` after transcript is loaded
**Expected:** JSON with gaps (topics not well covered in KB) and suggested questions

### Test Case 1

**Expected gaps (high confidence):**
- **Multi-currency processing** — Client asked directly, KB explicitly states it's not supported but provides no migration playbook
- **International settlement / payouts** — KB says "international payouts not currently supported" but no detail on workarounds
- **Loyalty program integration** — Client asked about custom loyalty hooks; KB only mentions metadata fields, no loyalty-specific docs

**Expected gaps (medium confidence):**
- **POS hardware compatibility** — Client uses Verifone; KB doesn't detail specific terminal models or setup procedures

**Expected suggested_questions:** Should include questions like "What is the detailed timeline for Canada expansion?" and "How does NovaPay integrate with third-party loyalty systems?"

### Test Case 2

**Expected gaps (high confidence):**
- **Carbon offsets / credits** — Client asked directly, consultant deflected, no KB content exists on offset advisory
- **Full Scope 3 (all 15 categories)** — Client's OEM customers may need this; standard engagement only covers 5 categories

**Expected gaps (medium confidence):**
- **Science-based target setting process** — Mentioned as an add-on but no methodology detail in KB
- **Specific assurance provider recommendations** — KB mentions Deloitte/EY but no detail on the assurance process

**Expected suggested_questions:** Should include "What carbon offset programs does GreenBuild recommend?" and "What is the process for full Scope 3 reporting across all 15 categories?"

---

## Test 8: endMeeting — Meeting Summary

**Action:** `endMeeting` after transcript is loaded
**Expected:** Markdown summary with structured sections

### Test Case 1 — Expected Summary Sections

| Section | Key Content |
|---|---|
| **Attendees** | Alex Chen (NovaPay), Marcus Webb (FreshCart) |
| **Key Discussion Topics** | Unified payment gateway, interchange-plus pricing, ShieldAI fraud detection, multi-currency gap, PCI compliance simplification, integration timeline |
| **Decisions Made** | Marcus interested in Enterprise plan; will evaluate Canada gap; wants technical review |
| **Action Items** | Alex: send formal proposal with savings projection, API docs, sandbox credentials, Canada timeline from product team. Marcus: share API docs with CTO. Follow-up Thursday. |
| **Unresolved Questions** | Multi-currency / Canada timeline, loyalty program integration details |
| **QA Pairs** | Should capture 5-8 Q&A exchanges from the transcript |

### Test Case 2 — Expected Summary Sections

| Section | Key Content |
|---|---|
| **Attendees** | Priya Sharma (GreenBuild), David Park (Meridian Manufacturing) |
| **Key Discussion Topics** | GHG Protocol methodology, data collection requirements, Scope 3 supplier emissions, CBAM exposure, carbon offsets (unresolved), assurance readiness, pricing |
| **Decisions Made** | Include assurance readiness add-on ($18K); CBAM assessment pending CFO/EU team discussion; April start targeting August board meeting |
| **Action Items** | Priya: send formal proposal by Friday with breakdown + data request list, include team bios, follow up on offset advisory offering. David: confirm CBAM scope with EU sales team, begin gathering utility bills. |
| **Unresolved Questions** | Carbon offset advisory, CBAM scope decision |

---

## Test 9: retroAnalysis — Post-Meeting Coaching

**Action:** `retroAnalysis` (session must be marked inactive via `endMeeting` first)
**Expected:** Structured feedback referencing specific transcript moments

### Test Case 1 — Expected Feedback Areas

| Area | What to Look For |
|---|---|
| **Communication Effectiveness** | Should note Alex handled pricing questions well with specific numbers, but was vague on the multi-currency interim solution |
| **Question Handling Quality** | Should praise immediate answers to pricing/security questions. Should flag that the loyalty program question got a "let me set up a technical call" deflection without providing any immediate value |
| **Knowledge Gap Assessment** | Should identify multi-currency as the biggest gap and note it almost derailed the deal |
| **Coaching Insights** | Should suggest: prepare a Canada expansion FAQ for future demos, have a loyalty integration one-pager ready, quantify the savings before the client asks |
| **Missed Agenda Items** | Could note that implementation support details (who handles migration, dedicated PM) weren't covered |

### Test Case 2 — Expected Feedback Areas

| Area | What to Look For |
|---|---|
| **Communication Effectiveness** | Should note Priya explained the methodology clearly. Should flag the carbon offsets response was notably vague — "it's a complicated area" with no concrete next step |
| **Question Handling Quality** | Should praise the CBAM answer (accurate, included pricing). Should flag the offset question was fumbled — client asked twice and got deflected both times |
| **Knowledge Gap Assessment** | Carbon offsets is the clear gap. Should note this is a board-level concern for the client |
| **Coaching Insights** | Should suggest: prepare an offset advisory FAQ or position statement, never say "let me look into it" without providing at least a high-level framework on the spot |
| **Action Item Completeness** | Proposal by Friday is clear, but "look into offset advisory" is vague — needs a specific date and deliverable |

---

## Test 10: retroChat — Follow-Up Questions

**Action:** `retroChat` after `retroAnalysis` has been completed
**Expected:** Specific, evidence-based answers referencing the transcript and retro feedback

### Test Case 1

| Message | Expected Response |
|---|---|
| `"What were the strongest moments in this meeting?"` | Should reference the pricing comparison moment (10:03-10:04) where Alex gave specific numbers, and the security/PCI simplification explanation (10:08-10:09) |
| `"How should I handle the Canada question better next time?"` | Should provide a concrete script or approach — e.g., acknowledge the gap, pivot to interim dual-processor strategy with specifics, offer a written timeline commitment |

### Test Case 2

| Message | Expected Response |
|---|---|
| `"What should I have said about carbon offsets?"` | Should suggest a structured response even with limited knowledge — e.g., explain the difference between avoidance and removal offsets, note SBTi's position, promise a detailed brief by a specific date |
| `"Did I price the engagement correctly?"` | Should reference the $65-75K base + $18K assurance = $83-123K range, note it's within the client's $125K approved budget, and that the pricing was presented clearly |

---

## Test 11: setSuggestedQuestions — Question Matching

**Action:** `setSuggestedQuestions` with prepared questions, then `processTranscript` with lines where the user speaks those topics
**Expected:** `questionMatched` events when user addresses a suggested topic

### Test Case 1

**Setup:** Set suggested questions:
1. `"What is NovaPay's pricing structure for enterprise retailers?"`
2. `"Does NovaPay support international payments?"`
3. `"What security certifications does NovaPay hold?"`

**Then process transcript.** Expected matches:
- Question 1 should match when Alex discusses interchange-plus pricing (~10:03:35)
- Question 2 should match when Alex discusses Canada/UK expansion (~10:06:42)
- Question 3 should match when Alex discusses PCI DSS and SOC 2 (~10:08:18)

### Test Case 2

**Setup:** Set suggested questions:
1. `"What is GreenBuild's methodology for carbon measurement?"`
2. `"What are the regulatory requirements for carbon reporting?"`

**Expected matches:**
- Question 1 matches when Priya explains GHG Protocol (~09:03:05)
- Question 2 matches when Priya discusses SEC filing requirements (~09:02:15)

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
