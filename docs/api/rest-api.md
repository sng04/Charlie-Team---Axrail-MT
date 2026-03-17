# REST API Reference

Base URL: `https://{api-id}.execute-api.{region}.amazonaws.com/prod`

All endpoints return the standard response envelope:

```json
{
  "statusCode": 200,
  "status": true,
  "message": "...",
  "data": { ... }
}
```

---

## Personalities

Personality records define communication style prompts that agents use when generating responses.

### List Personalities

```
GET /personalities?page=1&limit=20
```

Query parameters (optional):
- `page` — Page number (default: 1)
- `limit` — Items per page (default: 20, max: 100)

Response `data`:

```json
{
  "items": [
    {
      "personality_id": "uuid",
      "personality_name": "Friendly Coach",
      "personality_prompt": "Use warm, encouraging language...",
      "createdAt": "2025-01-15T10:00:00Z",
      "updatedAt": "2025-01-15T10:00:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 5,
    "total_pages": 1
  }
}
```

### Get Personality

```
GET /personalities/{personalityId}
```

Returns a single personality object in `data`.

### Create Personality

```
POST /personalities
```

Request body:

```json
{
  "personality_name": "Friendly Coach",
  "personality_prompt": "Use warm, encouraging language...",
  "idempotencyToken": "optional-unique-token"
}
```

Required fields: `personality_name`, `personality_prompt`

The `idempotencyToken` field is optional. If provided and a personality with the same token already exists, the existing record is returned instead of creating a duplicate.

### Update Personality

```
PUT /personalities/{personalityId}
```

Request body — any subset of fields to update:

```json
{
  "personality_prompt": "Updated prompt text..."
}
```

The `updatedAt` timestamp is set automatically.

### Delete Personality

```
DELETE /personalities/{personalityId}
```

Returns `409 Conflict` if any agents reference this personality. Unlink agents first before deleting.

---

## Agents

Agent records define the AI assistant's role, task instructions, model, and linked personality.

### List Agents

```
GET /agents?page=1&limit=20
```

Query parameters (optional):
- `page` — Page number (default: 1)
- `limit` — Items per page (default: 20, max: 100)

Response `data`:

```json
{
  "items": [
    {
      "agent_id": "uuid",
      "agent_name": "Sales Meeting Assistant",
      "role_prompt": "You are an AI Meeting Assistant...",
      "task_prompt": "1. Answer questions...",
      "personality_id": "uuid",
      "model_id": "amazon.nova-pro-v1:0",
      "use_case": "sales",
      "createdAt": "2025-01-15T10:00:00Z",
      "updatedAt": "2025-01-15T10:00:00Z"
    }
  ],
  "pagination": { ... }
}
```

### Get Agent

```
GET /agents/{agentId}
```

### Create Agent

```
POST /agents
```

Request body:

```json
{
  "agent_name": "Sales Meeting Assistant",
  "role_prompt": "You are an AI Meeting Assistant...",
  "task_prompt": "1. Answer questions from participants...",
  "personality_id": "existing-personality-uuid",
  "model_id": "amazon.nova-pro-v1:0",
  "use_case": "sales",
  "idempotencyToken": "optional-unique-token"
}
```

Required fields: `agent_name`, `role_prompt`, `task_prompt`, `personality_id`, `model_id`, `use_case`

Returns `400` if the referenced `personality_id` does not exist.

### Update Agent

```
PUT /agents/{agentId}
```

Request body — any subset of fields to update:

```json
{
  "agent_name": "Updated Name",
  "personality_id": "new-personality-uuid"
}
```

Returns `400` if a new `personality_id` is provided but does not exist.

### Delete Agent

```
DELETE /agents/{agentId}
```

---

## QA Pairs

QA pairs are created via WebSocket actions (`extractQAPair`, answer windows, user response windows). The REST API provides read and delete access.

### List QA Pairs

```
GET /qa-pairs?session_id=abc123
GET /qa-pairs?project_id=proj-456
```

One of `session_id` or `project_id` is required. Returns `400` if neither is provided.

Response `data`:

```json
[
  {
    "qa_pair_id": "uuid",
    "session_id": "abc123",
    "project_id": "proj-456",
    "question": "What is the pricing model?",
    "answer": "Our enterprise tier starts at...",
    "source": "participant",
    "created_at": "2025-01-15T10:05:00Z"
  }
]
```

The `source` field indicates how the QA pair was captured:
- `"participant"` — A meeting participant asked a suggested question and the client answered (answer window)
- `"client"` — A client asked a question and the user/host answered (user response window)
- `"agent"` — The AI agent extracted the QA pair via `extractQAPair`

### Get QA Pair

```
GET /qa-pairs/{qaPairId}
```

### Delete QA Pair

```
DELETE /qa-pairs/{qaPairId}
```

---

## Error Codes

| Code | Meaning |
|---|---|
| 200 | Success |
| 400 | Bad request — missing or invalid fields |
| 404 | Resource not found |
| 409 | Conflict — referential integrity violation (e.g., deleting a personality used by agents) |
| 500 | Internal server error |
