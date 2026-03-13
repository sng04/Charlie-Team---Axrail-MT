---
inclusion: auto
name: api-standards
description: REST API conventions including URL structure, HTTP method semantics, request/response formats, error envelopes, authentication flows, CORS, pagination, idempotency, and versioning.
---

# API Standards

REST API conventions for all API Gateway endpoints and Lambda handlers.

## URL Structure

### Resource Naming
- Use plural nouns for collections: `/items`, `/orders`, `/users`
- Use `{camelCase}` path parameters for resource IDs: `/items/{itemId}`
- Nest sub-resources under parents only when there's a true ownership relationship
- Dedicated `/search/{entity}` routes for search-powered queries

### Route Template
Standard CRUD resources follow this pattern:
```
GET    /{resources}                → List resources (paginated)
POST   /{resources}                → Create resource
GET    /{resources}/{resourceId}   → Get single resource
PUT    /{resources}/{resourceId}   → Update resource
DELETE /{resources}/{resourceId}   → Delete resource

GET    /search/{resources}?q=      → Full-text search
```

### HTTP Method Semantics
| Method | Purpose | Idempotent | Response Code |
|--------|---------|------------|---------------|
| GET | Read resource(s) | Yes | 200 |
| POST | Create resource | No | 200 or 202 (async) |
| PUT | Full update | Yes | 200 |
| DELETE | Remove resource | Yes | 200 |

## Request Conventions

### Path Parameters
- Extract from `event['pathParameters']` — always default to `{}` or `None`:
```python
path_params = event.get('pathParameters') or {}
resource_id = path_params.get('resourceId')
```

### Query Parameters
- Extract from `event['queryStringParameters']` — always default to `{}` or `None`:
```python
query_params = event.get('queryStringParameters') or {}
page = int(query_params.get('page', 1))
limit = min(int(query_params.get('limit', 20)), 100)
```
- Enforce sensible defaults and upper bounds on pagination params.
- Use `q` for free-text search queries.

### Request Body
- Parse defensively — body may arrive as string or dict:
```python
body = event.get('body', '{}')
data = json.loads(body) if isinstance(body, str) else body
```
- Validate required fields immediately after parsing (see coding-standards.md).

## Response Format

Every API response uses the shared `createResponse()` utility. The shape is:

```json
{
  "statusCode": 200,
  "status": true,
  "message": "Resource retrieved successfully",
  "data": { ... }
}
```

- `statusCode`: HTTP status code (mirrored in the response envelope for client convenience)
- `status`: `true` for 2xx/3xx, `false` for 4xx/5xx
- `message`: Human-readable summary
- `data`: Optional payload — omit when there's nothing to return

### Pagination Envelope
For list endpoints, wrap results in a pagination object:
```json
{
  "data": {
    "items": [ ... ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 142,
      "total_pages": 8
    }
  }
}
```

## HTTP Status Codes

| Code | Meaning | When to Use |
|------|---------|-------------|
| 200 | OK | Successful read, create, update, or delete |
| 202 | Accepted | Async operations queued for processing |
| 400 | Bad Request | Missing/invalid fields, malformed JSON |
| 401 | Unauthorized | Missing or invalid Authorization header |
| 403 | Forbidden | Valid auth but insufficient permissions |
| 404 | Not Found | Resource ID doesn't exist |
| 409 | Conflict | Duplicate creation or concurrent modification |
| 500 | Internal Server Error | Unhandled exceptions — never expose details |

## Error Responses

Error responses follow the same envelope. The `message` field contains a client-safe description:

```json
{
  "statusCode": 400,
  "status": false,
  "message": "Missing required fields: name, price"
}
```

- 4xx errors: include a descriptive message explaining what the client did wrong.
- 5xx errors: always return `"Internal server error"` — log the real error server-side.

## Authentication

### Cognito JWT Flow
1. Client authenticates via Cognito and receives a JWT access token.
2. Client sends the token in the `Authorization` header on every request.
3. Lambda extracts and validates the token:
```python
headers = event.get('headers', {})
auth = headers.get('Authorization') or headers.get('authorization')
if not auth:
    raise UnauthorizedError("Authorization header missing")
```
4. API Gateway can also enforce Cognito authorizers at the method level for pre-handler validation.

### Header Handling
- Always check both `Authorization` and `authorization` (API Gateway may lowercase headers).
- Never log the token value — log only the presence/absence and decoded claims if needed.

## CORS

CORS is configured at two levels:
1. API Gateway: preflight `OPTIONS` on the root resource with `allow_origins=["*"]`
2. Lambda responses: `createResponse()` includes CORS headers on every response:
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Headers: Content-Type,Authorization
Access-Control-Allow-Methods: GET,POST,PUT,DELETE,OPTIONS
```

## Idempotency

Write endpoints (POST) should accept an optional `idempotencyToken` in the request body:
- Query a GSI for existing records with the same token before creating.
- If found, return the existing resource with 202 instead of creating a duplicate.
- If not provided, generate a UUID server-side (best-effort, not guaranteed idempotent).

## Versioning

- Default: no version prefix (routes at root, e.g., `/items`).
- When breaking changes are needed: path-based versioning (`/v1/items`, `/v2/items`).
- When introducing a new version, keep the previous version active until all clients migrate.

## Search Endpoints

Search routes live under `/search/{entity}`:
- Required query param: `q` (free-text search string)
- Optional: `limit` (default 10, max 100)
- Response includes `results` array and `count`
- Multi-match across relevant fields with boosted weights (e.g., `name^2`)
