# WebSocket API Reference

Endpoint: `wss://{api-id}.execute-api.{region}.amazonaws.com/production`

## Connection

Connect with optional query parameters:

```
wss://.../production?session_id=abc123&agent_id=optional-agent-uuid
```

- `session_id` — Associates the connection with a meeting session. Used to scope transcripts, QA pairs, and gap analysis.
- `agent_id` — Loads a specific agent configuration (role prompt, task prompt, personality). Falls back to the default agent if omitted or not found.

On connect, the server:
1. Looks up the `project_id` from the session record
2. Builds the agent's system prompt from the agent and personality records
3. Loads any active skill documents for the agent from the SkillsTable
4. If skills exist, appends a skill section to the system prompt instructing the agent to search skill documents first before the general knowledge base
5. Caches all connection data (system prompt, project_id, session_id, agent_id, skills) for the duration of the connection

## Message Format

All messages are JSON with an `action` field that determines routing:

```json
{
  "action": "sendMessage",
  "session_id": "abc123",
  "message": "Hello, what can you do?"
}
```

Responses are pushed back over the same WebSocket connection as JSON objects with a `type` field.

---

## Actions

### sendMessage

General-purpose chat with the AI agent. The agent has access to the knowledge base, session transcripts, and agent-specific skill documents (if any are attached to the agent).

Request:

```json
{
  "action": "sendMessage",
  "session_id": "abc123",
  "message": "What were the key topics discussed?"
}
```

Response:

```json
{
  "type": "response",
  "message": "Based on the transcript, the key topics were...",
  "agent_name": "Sales Meeting Assistant"
}
```

---

### detectQuestion

Answer a specific question using the knowledge base. Designed for questions detected in live transcripts.

Request:

```json
{
  "action": "detectQuestion",
  "session_id": "abc123",
  "question": "What is the project timeline?"
}
```

Response:

```json
{
  "type": "questionResponse",
  "message": "According to the knowledge base, the timeline is...",
  "agent_name": "Sales Meeting Assistant"
}
```

---

### extractQAPair

Extract and persist a question-answer pair. The agent uses the `save_qa_pair` tool to store it in DynamoDB.

Request:

```json
{
  "action": "extractQAPair",
  "session_id": "abc123",
  "question": "What is the deadline?",
  "answer": "The deadline is next Friday."
}
```

Response:

```json
{
  "type": "qaPairSaved",
  "message": "QA pair saved successfully.",
  "agent_name": "Sales Meeting Assistant"
}
```

---

### analyzeGaps

Perform a knowledge gap analysis for the session. The agent retrieves the transcript, identifies topics, searches the knowledge base for each, and reports gaps.

Request:

```json
{
  "action": "analyzeGaps",
  "session_id": "abc123"
}
```

Response:

```json
{
  "type": "gapAnalysis",
  "session_id": "abc123",
  "gaps": [
    {
      "topic": "Compliance certifications",
      "description": "No KB documents cover SOC 2 or ISO 27001 status",
      "confidence": "high"
    }
  ],
  "suggested_questions": [
    "What compliance certifications does the platform hold?"
  ]
}
```

Suggested questions from the analysis are automatically stored with embeddings for later question matching during live transcripts.

---

### endMeeting

Generate a structured 4-chapter meeting summary, save it to S3, and mark the session as inactive.

The agent retrieves the session transcript, QA pairs, and gap analysis results, then produces a markdown summary with exactly four chapters:

1. **Meeting Summary** — Participants, date (ISO 8601), key topics, and decisions
2. **Missed Agenda Items** — Gaps identified by gap analysis that were never addressed in the meeting. If no gap analysis was run, notes that no gap analysis was performed.
3. **Action Items / Next Steps** — Concrete items with owners, deadlines, and follow-up commitments
4. **Session Insights** — Patterns, communication effectiveness, notable moments, and recommendations

Request:

```json
{
  "action": "endMeeting",
  "session_id": "abc123"
}
```

Responses (two messages):

```json
{ "type": "status", "message": "Generating meeting summary..." }
```

```json
{
  "type": "meetingSummary",
  "session_id": "abc123",
  "summary_markdown": "## Meeting Summary\n\n**Participants:** ...\n**Date:** 2025-01-15\n...\n\n## Missed Agenda Items\n\n...\n\n## Action Items / Next Steps\n\n...\n\n## Session Insights\n\n..."
}
```

The summary uses `##` level headings for each chapter. It is saved to S3 at `{project_id}/summaries/{session_id}.md` and automatically ingested into the knowledge base via the Ingestion Lambda.

---

### retroAnalysis

Generate retrospective feedback for a completed meeting. Only available after `endMeeting` has been called.

Request:

```json
{
  "action": "retroAnalysis",
  "session_id": "abc123"
}
```

Response:

```json
{
  "type": "retroFeedback",
  "session_id": "abc123",
  "feedback": "## Retrospective Analysis\n\n### Communication Effectiveness: 7/10..."
}
```

Returns `error` if the session is still active (not yet ended).

---

### retroChat

Follow-up conversation about the retrospective analysis. Requires `retroAnalysis` to have been run first on the same connection.

Request:

```json
{
  "action": "retroChat",
  "message": "What were the main action items?"
}
```

Response:

```json
{
  "type": "retroResponse",
  "message": "The main action items identified were..."
}
```

---

### setSuggestedQuestions

Store a list of suggested questions with vector embeddings for semantic matching during live transcripts.

Request:

```json
{
  "action": "setSuggestedQuestions",
  "session_id": "abc123",
  "questions": [
    "What is the pricing model for the enterprise tier?",
    "How does the integration with Salesforce work?",
    "What security certifications do you have?"
  ]
}
```

Response:

```json
{
  "type": "suggestedQuestionsSet",
  "count": 3
}
```

Each question is embedded using Titan Embed Text V2 (1024 dimensions) and stored in the SuggestedQuestionsTable. These embeddings are used by `processTranscript` for semantic matching.

---

### processTranscript

Process live transcript lines with question matching, question detection, and answer/response window management.

This is the most complex action — it orchestrates three stages of live QA detection. All non-partial lines are processed uniformly without speaker classification.

Request:

```json
{
  "action": "processTranscript",
  "session_id": "abc123",
  "lines": [
    {
      "speaker": "spk_0",
      "text": "What is the pricing model for the enterprise tier?",
      "start_time": "559.25",
      "end_time": "564.03",
      "confidence": "0.853",
      "is_partial": false
    },
    {
      "speaker": "spk_0",
      "text": "Our enterprise tier starts at two hundred dollars per seat.",
      "start_time": "565.10",
      "end_time": "570.44",
      "confidence": "0.912",
      "is_partial": false
    }
  ]
}
```

Fields:
- `lines` (required) — Array of transcript lines with `speaker`, `text`, `start_time`, `end_time`, `confidence`, and `is_partial`
- `speaker_hint` (deprecated) — Still accepted for backward compatibility but ignored. Speaker classification is no longer performed.

Response (always sent):

```json
{
  "type": "transcriptProcessed",
  "lines_processed": 2
}
```

Additional messages may be sent depending on what the transcript triggers:

#### Stage 1: Question Matching

When any non-partial line is semantically similar to a stored suggested question (cosine similarity >= 0.80), a match is reported and an answer window opens:

```json
{
  "type": "questionMatched",
  "question_text": "What is the pricing model for the enterprise tier?",
  "spoken_text": "What is the pricing model for the enterprise tier?",
  "similarity": 1.0
}
```

#### Stage 2: Answer Window Capture

After a question is matched, subsequent lines are captured in an answer window. The window closes when:
- 5 lines are collected, OR
- A new question is detected in an incoming line, OR
- 60 seconds elapse

On close, the QA pair is auto-saved:

```json
{
  "type": "qaPairAutoSaved",
  "question": "What is the pricing model for the enterprise tier?",
  "answer": "Our enterprise tier starts at two hundred dollars per seat.",
  "source": "participant"
}
```

If the window closes with no collected lines:

```json
{
  "type": "questionUnanswered",
  "question": "What is the pricing model for the enterprise tier?"
}
```

#### Stage 3: Question Detection

When any non-partial line contains a question (detected via heuristics or Nova Pro model classification), three things happen:

1. The question is reported:

```json
{
  "type": "questionDetected",
  "question": "What security certifications does your platform have?",
  "detection_method": "heuristic"
}
```

2. A suggested response is generated from the knowledge base:

```json
{
  "type": "suggestedResponse",
  "question": "What security certifications does your platform have?",
  "suggested_answer": "Based on the knowledge base, the platform holds SOC 2 Type II..."
}
```

3. A response window opens to capture the verbal answer that follows. It follows the same close rules as answer windows (5 lines / new question detected / 60s timeout) and auto-saves with `source: "participant"`.

Detection methods:
- `"heuristic"` — Text ends with `?` or starts with an interrogative word (what, how, why, etc.)
- `"model"` — Nova Pro classified the text as a question (used when heuristics are inconclusive)

Short texts (< 5 words) are skipped to avoid false positives.

---

## Agent Tools

The StrandsAgent has access to the following tools during WebSocket interactions:

| Tool | Available In | Description |
|---|---|---|
| `search_knowledge_base` | sendMessage, detectQuestion, analyzeGaps, retroChat | Vector search against the project knowledge base, filtered by project_id |
| `search_agent_skills` | sendMessage, detectQuestion, analyzeGaps, endMeeting, retroAnalysis, retroChat | Vector search against agent-specific skill documents, filtered by agent_id and doc_type |
| `get_session_transcript` | sendMessage, detectQuestion, analyzeGaps, endMeeting, retroAnalysis, retroChat | Retrieve transcript entries for a session |
| `save_qa_pair` | extractQAPair | Persist a question-answer pair to DynamoDB |
| `get_session_qa_pairs` | endMeeting, retroAnalysis | Retrieve QA pairs recorded during a session |
| `get_session_gaps` | endMeeting | Retrieve stored gap analysis results for a session |
| `save_summary_to_s3` | endMeeting | Save meeting summary markdown to S3 |
| `get_meeting_summary` | retroAnalysis | Retrieve a previously saved meeting summary |

When an agent has active skill documents, the system prompt instructs the agent to search skill documents first using `search_agent_skills` before falling back to the general knowledge base via `search_knowledge_base`.

---

## Error Messages

All errors follow this format:

```json
{
  "type": "error",
  "message": "Description of what went wrong"
}
```

Common errors:
- `"Missing 'message' field"` — Required field not provided
- `"Missing or empty 'lines' field"` — processTranscript called with no lines
- `"Retro mode is only available for completed sessions"` — retroAnalysis called on an active session
- `"No retro analysis found. Run retroAnalysis first."` — retroChat called without prior retroAnalysis
- `"Unsupported action: xyz"` — Unknown action name
