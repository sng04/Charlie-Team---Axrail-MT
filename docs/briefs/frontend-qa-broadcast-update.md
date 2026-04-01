# Frontend Brief: QA Events Now Broadcast via DDB Streams

## What Changed

QA detection events (`questionDetected`, `suggestedResponse`, `qaPairAutoSaved`, `questionUnanswered`) are now broadcast to ALL WebSocket connections on a session via DynamoDB Streams — the same pattern as `transcriptLine`.

Previously these events were only sent to the single connection that called `processTranscript`. Now they're triggered by DDB writes, so every connected client receives them regardless of who triggered the detection.

## Architecture

```
processTranscript detects question → writes QA pair to DDB
    → DynamoDB Stream fires (~50-100ms)
    → QAPairBroadcast Lambda
    → Reads connection_ids from Sessions table
    → Broadcasts event to all connections
```

## Events You'll Receive

All events now include a `qa_pair_id` field for deduplication.

### On new QA pair insert:

```json
{
  "type": "questionDetected",
  "question": "Can NovaPay handle MYR?",
  "speaker_role": "client",
  "detection_method": "heuristic",
  "qa_pair_id": "uuid"
}
```

### When AI suggested answer is added:

```json
{
  "type": "suggestedResponse",
  "question": "Can NovaPay handle MYR?",
  "suggested_answer": "NovaPay settles in USD only. Transactions process in MYR at the terminal but settle in USD with FX conversion.",
  "qa_pair_id": "uuid"
}
```

### When actual spoken answer is captured:

```json
{
  "type": "qaPairAutoSaved",
  "question": "Can NovaPay handle MYR?",
  "answer": "Right now NovaPay settles in USD only. Multi-currency settlement is on the roadmap.",
  "suggested_answer": "NovaPay settles in USD only. Transactions process in MYR...",
  "source": "participant",
  "qa_pair_id": "uuid"
}
```

### When a question goes unanswered:

```json
{
  "type": "questionUnanswered",
  "question": "What about carbon offsets?",
  "speaker_role": "client",
  "qa_pair_id": "uuid"
}
```

## Deduplication

You may receive the same event twice during the transition period — once from the `processTranscript` Lambda's direct post, and once from the DDB Stream broadcast. Deduplicate using `qa_pair_id` (preferred) or `question` text.

```javascript
const seenQAEvents = new Set();

ws.onmessage = (event) => {
  const msg = JSON.parse(event.data);
  
  if (['questionDetected', 'suggestedResponse', 'qaPairAutoSaved', 'questionUnanswered'].includes(msg.type)) {
    const dedupeKey = `${msg.type}:${msg.qa_pair_id || msg.question}`;
    if (seenQAEvents.has(dedupeKey)) return; // Skip duplicate
    seenQAEvents.add(dedupeKey);
  }
  
  // Handle normally
  handleMessage(msg);
};
```

## Event Timeline for a Detected Question

```
[+0ms]     transcriptLine arrives (from Transcripts DDB Stream)
[+0ms]     Frontend sends processTranscript
[+500ms]   questionDetected arrives (from QAPairs DDB Stream — INSERT)
[+2-4s]    suggestedResponse arrives (from QAPairs DDB Stream — MODIFY)
[+5-30s]   qaPairAutoSaved arrives (from QAPairs DDB Stream — MODIFY with answer)
```

## What Stays the Same

- WebSocket connection URL and query params — no change
- `transcriptLine` events — still from Transcripts DDB Stream
- `processTranscript` action — still required to trigger AI detection
- REST endpoints (`GET /qa-pairs`) — still available for initial page load
- `sendMessage`, `endMeeting`, `retroAnalysis`, etc. — no change

## Multi-Client Support

All events now reach every connected client on the session. Multiple browser tabs, multiple users watching the same session — everyone sees the same QA events simultaneously. No more missed events from connection drops.
