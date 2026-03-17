# ADR-001: Strands Agent Lambda Decomposition

## Context

The StrandsAgent Lambda started as a single 1348-line `lambda_function.py` monolith handling WebSocket routing, AI agent invocation, transcript processing, question detection, window management, and all tool definitions. This made the code difficult to navigate, test, and extend.

## Decision

Decompose the monolith into 7 focused modules within the same Lambda package:

| Module | Responsibility |
|---|---|
| `lambda_function.py` | WebSocket route dispatch only (~80 lines) |
| `handlers.py` | Action handlers (sendMessage, detectQuestion, etc.) |
| `transcript.py` | processTranscript logic, speaker classification, question matching |
| `question_detection.py` | Client question heuristics and model classification |
| `windows.py` | Answer windows, user response windows, suggested question storage |
| `tools.py` | Strands agent tools (KB search, transcript retrieval, QA save, S3) |
| `helpers.py` | DynamoDB access, connection cache, WebSocket posting |
| `constants.py` | Environment variables, thresholds, default configs, task prompts |

## Consequences

- Each module has a single responsibility and can be understood in isolation
- Import graph is acyclic: `lambda_function` → `handlers`/`transcript` → `tools`/`windows`/`question_detection` → `helpers`/`constants`
- No circular dependencies
- Adding new WebSocket actions requires touching only `lambda_function.py` (dispatch) and a handler module
- Trade-off: more files to navigate, but each is small and focused
