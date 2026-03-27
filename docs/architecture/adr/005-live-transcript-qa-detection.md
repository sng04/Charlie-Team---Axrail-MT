# ADR-005: Live Transcript QA Detection (3-Stage Pipeline)

## Context

During live meetings, valuable question-answer exchanges happen organically but are lost if not captured. The platform needed a way to automatically detect questions, match them against pre-set topics, and capture answers.

The original implementation classified speakers into "user" and "client" roles and routed transcript lines to different pipeline stages based on role. This was replaced with a speaker-agnostic pipeline when the audio input was flattened to a single channel, making speaker differentiation unreliable.

## Decision

Implement a 3-stage pipeline within the `processTranscript` action. All non-partial transcript lines are processed uniformly regardless of speaker identity.

**Stage 1 — Suggested Question Matching:** Before a meeting, suggested questions are stored with Titan Embed V2 embeddings (1024 dimensions). During the transcript, every non-partial line is embedded and compared via cosine similarity. Matches above 0.80 threshold trigger answer windows.

**Stage 2 — Answer Window Capture:** When a suggested question is matched, an answer window opens to capture subsequent lines as the answer. Windows close on 5 collected lines, detection of a new question in an incoming line, or 60-second timeout. Captured answers are auto-saved as QA pairs with `source: "participant"`.

**Stage 3 — Question Detection:** All non-partial lines are checked for questions using a two-tier approach: fast heuristics first (question marks, interrogative words), then Nova Pro model classification for ambiguous cases. Detected questions trigger a suggested response from the KB and open a response window to capture the verbal answer that follows.

Embeddings are stored as `Decimal` values in DynamoDB (boto3 resource layer requirement) and converted back to `float` for cosine similarity computation.

## Consequences

- QA pairs are captured automatically without manual intervention
- The host receives real-time suggested responses for detected questions
- Heuristic-first detection avoids unnecessary model calls for obvious questions
- Short texts (< 5 words) are filtered to reduce false positives
- Partial lines (`is_partial: true`) are skipped entirely to avoid processing incomplete utterances
- Window close conditions use new-question-detected instead of speaker turn change, since speaker roles are not available
- Window state is ephemeral (in-memory on the Lambda) — if a Lambda cold-starts between transcript batches, open windows are lost. Clients should send related lines in the same batch when possible.
- Trade-off: the 0.80 similarity threshold balances precision vs. recall. Exact-match text always scores 1.0; paraphrased questions may fall below threshold.
- Trade-off: processing every line through question detection increases Bedrock model calls compared to the old role-filtered approach. Heuristics mitigate this for obvious non-questions.
