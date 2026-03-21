# ADR-004: Lambda Standards Alignment (5-Stage Refactoring)

## Context

An audit of the `lambda/` directory against project steering standards identified 11 deviations: inconsistent directory naming, missing Powertools instrumentation, duplicated utility code, no shared layers, and a monolithic agent Lambda. These issues made the codebase harder to maintain and debug in production.

## Decision

Execute a 5-stage refactoring plan:

1. **Shared Lambda Layers** — Extract common code (`response_utils`, `custom_exceptions`) into a shared layer. Create dedicated layers for PyPDF2, Powertools, OpenSearch, and Strands.
2. **File and Directory Renaming** — Rename all Lambda directories to PascalCase, entry files to `lambda_function.py`, and handlers to `lambda_handler`.
3. **CRUD Handler Refactoring** — Add Powertools Logger/Tracer, typed exceptions, standard try/except patterns, timestamps, and idempotency tokens to all CRUD Lambdas.
4. **Strands Agent Decomposition** — Split the 1348-line monolith into 7 focused modules (see ADR-003).
5. **Event-Driven Lambda Refactoring** — Add Powertools Logger/Tracer and structured logging to Ingestion, Deletion, and GapScheduler Lambdas.

## Consequences

- All Lambdas now follow the same structural conventions
- Structured JSON logging in CloudWatch across all functions
- X-Ray tracing with full call chains for debugging
- Shared layers reduce deployment package sizes and eliminate code duplication
- Idempotency tokens on create operations prevent duplicate records
- Trade-off: the refactoring touched every Lambda, requiring a full regression test pass (66/66 tests passing)
