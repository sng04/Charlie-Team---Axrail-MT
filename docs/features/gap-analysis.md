# Knowledge Gap Analysis

## Overview

Gap analysis identifies topics discussed in a meeting that lack coverage in the knowledge base. It runs in two modes: on-demand via WebSocket and automatically via a scheduled Lambda.

## On-Demand Analysis

Send the `analyzeGaps` action over WebSocket:

```json
{
  "action": "analyzeGaps",
  "session_id": "abc123"
}
```

The agent retrieves the session transcript, identifies key topics, searches the knowledge base for each topic, and reports gaps with confidence levels.

Suggested questions from the analysis are automatically stored with embeddings for question matching during live transcripts.

## Scheduled Analysis

The GapScheduler Lambda runs every 2 minutes via EventBridge. It:

1. Queries the SessionsTable for active sessions (via the `active-sessions-index` GSI)
2. Skips sessions with no new transcript data since the last analysis (compares `last_transcript_update_at` vs `last_gap_analysis_at`)
3. Asynchronously invokes the StrandsAgent Lambda with an `analyzeGaps` payload for each eligible session
4. Updates `last_gap_analysis_at` on the session record

This ensures gap analysis results stay current as new transcript data flows in, without requiring the client to manually trigger it.

## Response Format

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


## Persistence

After each gap analysis run (whether triggered on-demand via WebSocket or automatically by the GapScheduler), results are written to the `GapAnalysisResults` DynamoDB table. The table is keyed by `session_id`, so each session holds exactly one gap analysis record. Subsequent analyses for the same session overwrite the previous record (latest-wins semantics).

The persisted record contains:

| Field | Description |
|---|---|
| `session_id` | Partition key — the session this analysis belongs to |
| `gaps` | Array of identified knowledge gaps (topic, description, confidence) |
| `suggested_questions` | Array of suggested follow-up questions |
| `analyzed_at` | ISO 8601 timestamp of when the analysis ran |

Persistence failures are logged but do not block the WebSocket response to the client.

## Retrieval Tool

The `get_session_gaps` Strands agent tool retrieves stored gap analysis results for a given session. It performs a direct `get_item` lookup by `session_id` and returns a formatted summary of the gaps found.

This tool is intended for use by the `endMeeting` agent (Phase 3) to include knowledge gap information in meeting summaries as missed agenda items.

```python
get_session_gaps(session_id="abc123")
```

Returns a formatted string listing each gap with its confidence level, topic, and description — or a descriptive message if no results exist for the session.
