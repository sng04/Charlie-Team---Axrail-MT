# REST API Reference

Base URL: `https://{api-id}.execute-api.{region}.amazonaws.com/{stage}`

All endpoints return the standard response envelope:

```json
{
  "statusCode": 200,
  "status": true,
  "message": "...",
  "data": { ... }
}
```

Authentication is handled via Cognito JWT tokens passed in the `Authorization` header.

---

## Authentication

### Admin Login

```
POST /auth/admin/login
```

Request body:

```json
{
  "username": "admin@axrail.com",
  "password": "password123"
}
```

Returns JWT tokens (`access_token`, `id_token`, `refresh_token`) or a password challenge.

### User Login

```
POST /auth/user/login
```

Request body:

```json
{
  "username": "user@example.com",
  "password": "password123"
}
```

Returns JWT tokens for non-admin users.

### Change Password

```
POST /auth/change-password
```

Request body:

```json
{
  "username": "user@example.com",
  "previous_password": "old-password",
  "proposed_password": "new-password"
}
```

### Logout

```
POST /auth/logout
```

Requires `Authorization` header. Invalidates the current session.

---

## Projects

### Create Project (Admin only)

```
POST /projects
```

Request body:

```json
{
  "name": "Project Name",
  "email": "contact@example.com",
  "description": "Optional description",
  "s3_arn": "optional-s3-arn"
}
```

Required fields: `name`, `email`

### List Projects

```
GET /projects
```

### Get Project

```
GET /projects/{projectId}
```

### Update Project (Admin only)

```
PUT /projects/{projectId}
```

### Delete Project (Admin only)

```
DELETE /projects/{projectId}
```

---

## Sessions

### Create Session

```
POST /sessions
```

Request body:

```json
{
  "project_id": "uuid",
  "name": "Session Name",
  "meeting_link": "https://meet.example.com/abc",
  "description": "Optional",
  "start_time": "2025-01-15T10:00:00Z",
  "end_time": "2025-01-15T11:00:00Z"
}
```

Required fields: `project_id`, `name`

Optional fields: `meeting_link`, `description`, `start_time`, `end_time`

The session is created with `is_active: "inactive"` and `bot_status: "pending"`. The meeting bot is dispatched via warm pool (SQS) or cold start (ECS) depending on configuration.

### List Sessions

```
GET /sessions?project_id={projectId}
```

### Get Session

```
GET /sessions/{sessionId}
```

### Update Session

```
PUT /sessions/{sessionId}
```

### Delete Session

```
DELETE /sessions/{sessionId}
```

### Get Project Sessions

```
GET /projects/{projectId}/sessions
```

Returns all sessions belonging to a project.

---

## Users (Admin only)

### Create User

```
POST /users
```

### List Users

```
GET /users
```

### Get User Projects

```
GET /users/{userId}/projects
```

Returns all projects assigned to a specific user.

### Assign User to Project

```
POST /project-users
```

Request body:

```json
{
  "project_id": "uuid",
  "user_id": "uuid"
}
```

### Remove User from Project

```
DELETE /project-users/{projectUserId}
```

### Get Project Users

```
GET /projects/{projectId}/users
```

Returns all users assigned to a specific project.

---

## Meeting Bot

### Get Session Transcripts

```
GET /sessions/{sessionId}/transcripts
```

Returns all transcript entries for a session. Requires user authentication.

### Stop Meeting Bot

```
POST /sessions/{sessionId}/stop-bot
```

Stops the meeting bot for the given session. Requires user authentication.

### Get Bot Status

```
GET /sessions/{sessionId}/bot-status
```

Returns the current bot status for the session. Requires user authentication.

---

## Bot Credentials (Admin only)

Bot credentials store Google Meet service account credentials used by the meeting bot.

### List Bot Credentials

```
GET /bot-credentials
```

### Create Bot Credential

```
POST /bot-credentials
```

### Get Bot Credential

```
GET /bot-credentials/{credentialId}
```

### Update Bot Credential

```
PUT /bot-credentials/{credentialId}
```

### Delete Bot Credential

```
DELETE /bot-credentials/{credentialId}
```

### Verify Bot Credential Email

```
GET /bot-credentials/{credentialId}/verify
```

Public endpoint (no auth required). Used for email verification flow.

---

## Warm Pool (Admin only)

Manages the ECS warm pool for meeting bot containers.

### Start Warm Pool

```
POST /warm-pool/start
```

Starts or scales up warm pool containers.

### Stop Warm Pool

```
POST /warm-pool/stop
```

Stops or scales down warm pool containers.

---

## Agents (Admin only)

Agent records define the AI assistant's role, task instructions, model, and linked personality.

### List Agents

```
GET /agents?page=1&limit=20
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

### Delete Agent

```
DELETE /agents/{agentId}
```

---

## Personalities (Admin only)

Personality records define communication style prompts that agents use when generating responses.

### List Personalities

```
GET /personalities?page=1&limit=20
```

### Get Personality

```
GET /personalities/{personalityId}
```

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

### Update Personality

```
PUT /personalities/{personalityId}
```

### Delete Personality

```
DELETE /personalities/{personalityId}
```

Returns `409 Conflict` if any agents reference this personality.

---

## Skills (Admin only)

Skill documents are agent-specific knowledge files (PDF or Markdown) uploaded via pre-signed S3 URLs.

### List Skills

```
GET /skills?agent_id={agentId}&page=1&limit=20
```

### Get Skill

```
GET /skills/{skillId}
```

### Create Skill

```
POST /skills
```

Request body:

```json
{
  "agent_id": "existing-agent-uuid",
  "skill_name": "Product Pricing Guide",
  "file_name": "pricing-guide.pdf",
  "description": "Optional description"
}
```

Returns a `skill` object and a pre-signed `upload_url` for direct S3 upload.

### Update Skill

```
PUT /skills/{skillId}
```

### Delete Skill

```
DELETE /skills/{skillId}
```

---

## QA Pairs

QA pairs are captured via WebSocket actions and accessible via REST for read/delete.

### List QA Pairs

```
GET /qa-pairs?session_id=abc123
GET /qa-pairs?project_id=proj-456
```

One of `session_id` or `project_id` is required.

### Get QA Pair

```
GET /qa-pairs/{qaPairId}
```

### Delete QA Pair (Admin only)

```
DELETE /qa-pairs/{qaPairId}
```

---

## Error Codes

| Code | Meaning |
|---|---|
| 200 | Success |
| 400 | Bad request — missing or invalid fields |
| 401 | Unauthorized — invalid credentials |
| 403 | Forbidden — insufficient permissions |
| 404 | Resource not found |
| 409 | Conflict — referential integrity violation |
| 500 | Internal server error |
