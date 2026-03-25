---
inclusion: manual
name: frontend-bot-credential-integration
description: Frontend integration guide for Bot Credential and Bot Pool management API. Covers endpoints, request/response formats, and flows for managing meeting bot credentials and warm pool containers.
---

# Frontend Bot Credential & Bot Pool Integration Guide

## Overview

This document provides a complete guide for integrating frontend with Bot Credential and Bot Pool management API. Bot credentials are used to authenticate meeting bots that join video conferences. The warm pool system pre-starts containers for faster meeting joins.

Key concepts:
- **Bot Credential**: Email/password pair used by meeting bots to join meetings
- **Warm Pool**: Pre-started ECS containers ready to join meetings instantly
- **Verification**: Email verification required before credential can be used

## Base URL

```
{API_GATEWAY_URL}/{stage}
```

Example: `https://abc123.execute-api.ap-southeast-1.amazonaws.com/dev`

---

## Bot Credential Lifecycle

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Create    │────▶│   Email     │────▶│   Verify    │────▶│   Active    │
│  Credential │     │   Sent      │     │   Email     │     │   Ready     │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                                                           │
       │                                                           ▼
       │                                                    ┌─────────────┐
       │                                                    │  Assign to  │
       │                                                    │   Project   │
       │                                                    └─────────────┘
       │                                                           │
       ▼                                                           ▼
┌─────────────┐                                             ┌─────────────┐
│  not_verified │                                           │  Start Warm │
│  (inactive)   │                                           │    Pool     │
└─────────────┘                                             └─────────────┘
```

### Status Fields

| Field | Values | Description |
|-------|--------|-------------|
| `verification_status` | `not_verified`, `verified` | Email verification state |
| `available_status` | `inactive`, `active` | Whether credential can be used |

---

## API Endpoints

### Bot Credential Endpoints

#### 1. Create Bot Credential
**POST** `/bot-credentials`

Creates a new bot credential and sends verification email.

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Request Body:**
```json
{
  "email": "bot@example.com",
  "password": "xxxx-xxxx-xxxx-xxxx",
  "warm_pool_size": 2
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `email` | string | Yes | Bot account email |
| `password` | string | Yes | Bot account password (hyphens auto-removed) |
| `warm_pool_size` | integer | No | Number of warm containers (default: 1) |

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Bot credential created successfully. Verification email sent.",
  "data": {
    "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "email": "bot@example.com",
    "verification_status": "not_verified",
    "available_status": "inactive",
    "warm_pool_size": 2,
    "created_at": "2024-01-15T10:30:00.000000+00:00",
    "updated_at": "2024-01-15T10:30:00.000000+00:00"
  }
}
```

**Error Responses:**
- `400`: Missing required fields (email, password)
- `401`: Unauthorized (not admin)
- `409`: Bot credential with email already exists
- `500`: Internal server error

---

#### 2. List Bot Credentials
**GET** `/bot-credentials`

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `limit` | integer | Max items to return (default: 50, max: 100) |
| `lastKey` | string | Pagination key from previous response |

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Bot credentials retrieved successfully",
  "data": {
    "items": [
      {
        "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "email": "bot@example.com",
        "verification_status": "verified",
        "available_status": "active",
        "warm_pool_size": 2,
        "created_at": "2024-01-15T10:30:00.000000+00:00",
        "updated_at": "2024-01-15T10:30:00.000000+00:00"
      }
    ],
    "count": 1,
    "lastKey": "next-credential-id"
  }
}
```

**Error Responses:**
- `401`: Unauthorized (not admin)
- `500`: Internal server error

---

#### 3. Get Bot Credential
**GET** `/bot-credentials/{credentialId}`

Returns credential details including warm pool status.

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Bot credential retrieved successfully",
  "data": {
    "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "email": "bot@example.com",
    "verification_status": "verified",
    "available_status": "active",
    "warm_pool_size": 2,
    "created_at": "2024-01-15T10:30:00.000000+00:00",
    "updated_at": "2024-01-15T10:30:00.000000+00:00",
    "warm_pool_status": {
      "idle": 2,
      "busy": 0,
      "total": 2
    }
  }
}
```

**Error Responses:**
- `400`: Credential ID is required
- `401`: Unauthorized (not admin)
- `404`: Bot credential not found
- `500`: Internal server error

---

#### 4. Update Bot Credential
**PUT** `/bot-credentials/{credentialId}`

Updates credential. If email changes, resets verification and sends new email.

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Request Body:**
```json
{
  "email": "newbot@example.com",
  "password": "yyyy-yyyy-yyyy-yyyy",
  "available_status": "active",
  "warm_pool_size": 3
}
```

| Field | Type | Description |
|-------|------|-------------|
| `email` | string | New email (triggers re-verification) |
| `password` | string | New password |
| `available_status` | string | `active` or `inactive` |
| `warm_pool_size` | integer | Number of warm containers |

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Bot credential updated successfully. Verification email sent to new address.",
  "data": {
    "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "email": "newbot@example.com",
    "verification_status": "not_verified",
    "available_status": "active",
    "warm_pool_size": 3,
    "created_at": "2024-01-15T10:30:00.000000+00:00",
    "updated_at": "2024-01-16T14:00:00.000000+00:00"
  }
}
```

**Error Responses:**
- `400`: No update data provided / Invalid available_status / Invalid warm_pool_size
- `401`: Unauthorized (not admin)
- `404`: Bot credential not found
- `409`: Bot credential with email already exists
- `500`: Internal server error

---

#### 5. Delete Bot Credential
**DELETE** `/bot-credentials/{credentialId}`

Deletes credential. Fails if assigned to any project.

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Bot credential deleted successfully"
}
```

**Error Responses:**
- `400`: Credential ID is required
- `401`: Unauthorized (not admin)
- `404`: Bot credential not found
- `409`: Bot credential is assigned to project(s)
- `500`: Internal server error

---

#### 6. Verify Bot Credential Email
**GET** `/bot-credentials/{credentialId}/verify?token={token}`

Public endpoint (no auth) - accessed via email link.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `token` | string | Yes | Verification token from email |

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Email verified successfully",
  "data": {
    "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "email": "bot@example.com",
    "verification_status": "verified"
  }
}
```

**Error Responses:**
- `400`: Verification token is required / Invalid or expired token
- `404`: Bot credential not found
- `500`: Internal server error

---

### Bot Pool Endpoints

#### 7. List Bot Pool Containers
**GET** `/bot-credentials/{credentialId}/pool`

Lists all warm pool containers for a credential.

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Query Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| `status` | string | Filter by status: `idle`, `busy`, `starting`, `error` |

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Bot pool containers retrieved successfully",
  "data": {
    "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "summary": {
      "idle": 2,
      "busy": 1,
      "starting": 0,
      "error": 0,
      "total": 3
    },
    "containers": [
      {
        "container_id": "abc123def456",
        "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "task_arn": "arn:aws:ecs:ap-southeast-1:123456789:task/cluster/abc123def456",
        "status": "idle",
        "current_session_id": null,
        "current_session_name": null,
        "registered_at": "2024-01-15T10:30:00.000000+00:00",
        "last_heartbeat": "2024-01-15T10:35:00.000000+00:00"
      },
      {
        "container_id": "xyz789ghi012",
        "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "task_arn": "arn:aws:ecs:ap-southeast-1:123456789:task/cluster/xyz789ghi012",
        "status": "busy",
        "current_session_id": "session-123",
        "current_session_name": "Weekly Team Standup",
        "registered_at": "2024-01-15T10:30:00.000000+00:00",
        "last_heartbeat": "2024-01-15T10:40:00.000000+00:00"
      }
    ]
  }
}
```

**Container Status Values:**
| Status | Description |
|--------|-------------|
| `starting` | Container is starting up |
| `idle` | Ready to join a meeting |
| `busy` | Currently in a meeting |
| `error` | Container encountered an error |

**Error Responses:**
- `400`: Credential ID is required
- `401`: Unauthorized (not admin)
- `404`: Bot credential not found
- `500`: Internal server error

---

#### 8. Start Warm Pool
**POST** `/warm-pool/start`

Starts warm pool containers for credentials.

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Request Body (optional):**
```json
{
  "credential_ids": ["cred-id-1", "cred-id-2"],
  "containers_per_credential": 3
}
```

| Field | Type | Description |
|-------|------|-------------|
| `credential_ids` | array | Specific credentials to warm (default: all active) |
| `containers_per_credential` | integer | Override warm_pool_size for all |

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Started 4 warm containers",
  "data": {
    "started": 4,
    "tasks": [
      {
        "credential_id": "cred-id-1",
        "task_arn": "arn:aws:ecs:ap-southeast-1:123456789:task/cluster/task-1"
      },
      {
        "credential_id": "cred-id-1",
        "task_arn": "arn:aws:ecs:ap-southeast-1:123456789:task/cluster/task-2"
      }
    ]
  }
}
```

**Error Responses:**
- `400`: Bad request
- `401`: Unauthorized (not admin)
- `500`: Internal server error

---

#### 9. Stop Warm Pool
**POST** `/warm-pool/stop`

Stops warm pool containers. Only stops idle containers.

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Request Body (optional):**
```json
{
  "credential_id": "specific-cred-id",
  "stop_all": false,
  "target_count": 1
}
```

| Field | Type | Description |
|-------|------|-------------|
| `credential_id` | string | Stop only for this credential |
| `stop_all` | boolean | Stop all idle containers (default: false) |
| `target_count` | integer | Scale down to this number |

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Stopped 2 idle containers, 1 containers skipped (in meeting)",
  "data": {
    "stopped": 2,
    "skipped_busy": 1,
    "tasks": [
      {
        "credential_id": "cred-id-1",
        "task_arn": "arn:aws:ecs:ap-southeast-1:123456789:task/cluster/task-1"
      }
    ]
  }
}
```

**Error Responses:**
- `400`: Bad request
- `401`: Unauthorized (not admin)
- `500`: Internal server error

---

## Frontend Pages

### 1. Bot Credentials List Page (`/admin/bot-credentials`)

**Components:**
- Header with "Add Credential" button
- Search/filter bar
- Credentials table with columns:
  - Email
  - Verification Status (badge)
  - Available Status (toggle)
  - Warm Pool Size
  - Pool Status (idle/busy/total)
  - Actions (View, Edit, Delete)
- Pagination

**Table Structure:**
```html
<table>
  <thead>
    <tr>
      <th>Email</th>
      <th>Verification</th>
      <th>Status</th>
      <th>Pool Size</th>
      <th>Pool Status</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>bot@example.com</td>
      <td><span class="badge badge-success">Verified</span></td>
      <td><toggle checked /></td>
      <td>2</td>
      <td>
        <span class="text-green">2 idle</span> / 
        <span class="text-orange">0 busy</span>
      </td>
      <td>
        <button>View Pool</button>
        <button>Edit</button>
        <button>Delete</button>
      </td>
    </tr>
  </tbody>
</table>
```

**Flow:**
1. On mount, call `GET /bot-credentials`
2. Display credentials in table
3. Add Credential: Open modal, call `POST /bot-credentials`
4. Edit Credential: Open modal, call `PUT /bot-credentials/{id}`
5. Delete Credential: Confirm dialog, call `DELETE /bot-credentials/{id}`
6. Toggle Status: Call `PUT /bot-credentials/{id}` with `available_status`

---

### 2. Create/Edit Bot Credential Modal

**Components:**
- Form fields:
  - Email (required)
  - Password (required for create, optional for edit)
  - Warm Pool Size (number input, min: 1)
  - Available Status (toggle, edit only)
- Submit button
- Cancel button
- Error message display

**Form Validation:**
- Email: Valid email format
- Password: Required for create
- Warm Pool Size: Positive integer

**Create Flow:**
```javascript
async function createCredential(data) {
  const response = await apiCall('POST', '/bot-credentials', {
    email: data.email,
    password: data.password,
    warm_pool_size: data.warmPoolSize || 1
  });
  
  if (response.status) {
    showSuccess('Credential created. Verification email sent.');
    refreshList();
    closeModal();
  }
}
```

**Edit Flow:**
```javascript
async function updateCredential(credentialId, data) {
  const payload = {};
  if (data.email) payload.email = data.email;
  if (data.password) payload.password = data.password;
  if (data.warmPoolSize) payload.warm_pool_size = data.warmPoolSize;
  if (data.availableStatus !== undefined) {
    payload.available_status = data.availableStatus ? 'active' : 'inactive';
  }
  
  const response = await apiCall('PUT', `/bot-credentials/${credentialId}`, payload);
  
  if (response.status) {
    const message = response.message.includes('Verification') 
      ? 'Credential updated. Please verify new email.'
      : 'Credential updated successfully.';
    showSuccess(message);
    refreshList();
    closeModal();
  }
}
```

---

### 3. Bot Pool Detail Page (`/admin/bot-credentials/{id}/pool`)

**Components:**
- Credential info header
- Pool summary cards (idle, busy, starting, error, total)
- Pool control buttons (Start Pool, Stop Pool)
- Containers table with columns:
  - Container ID
  - Status (badge with color)
  - Current Session
  - Registered At
  - Last Heartbeat
- Auto-refresh toggle (every 10 seconds)

**Summary Cards:**
```html
<div class="pool-summary">
  <div class="card card-success">
    <div class="card-value">2</div>
    <div class="card-label">Idle</div>
  </div>
  <div class="card card-warning">
    <div class="card-value">1</div>
    <div class="card-label">Busy</div>
  </div>
  <div class="card card-info">
    <div class="card-value">0</div>
    <div class="card-label">Starting</div>
  </div>
  <div class="card card-danger">
    <div class="card-value">0</div>
    <div class="card-label">Error</div>
  </div>
</div>
```

**Containers Table:**
```html
<table>
  <thead>
    <tr>
      <th>Container ID</th>
      <th>Status</th>
      <th>Session</th>
      <th>Registered</th>
      <th>Last Heartbeat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>abc123def456</code></td>
      <td><span class="badge badge-success">Idle</span></td>
      <td>-</td>
      <td>Jan 15, 2024 10:30 AM</td>
      <td>2 minutes ago</td>
    </tr>
    <tr>
      <td><code>xyz789ghi012</code></td>
      <td><span class="badge badge-warning">Busy</span></td>
      <td><a href="/sessions/session-123">session-123</a></td>
      <td>Jan 15, 2024 10:30 AM</td>
      <td>30 seconds ago</td>
    </tr>
  </tbody>
</table>
```

**Pool Control Flow:**
```javascript
// Start warm pool for this credential
async function startPool(credentialId) {
  const response = await apiCall('POST', '/bot-pool/start', {
    credential_ids: [credentialId]
  });
  
  if (response.status) {
    showSuccess(`Started ${response.data.started} containers`);
    refreshPool();
  }
}

// Stop all idle containers for this credential
async function stopPool(credentialId, stopAll = false) {
  const response = await apiCall('POST', '/bot-pool/stop', {
    credential_id: credentialId,
    stop_all: stopAll
  });
  
  if (response.status) {
    let message = `Stopped ${response.data.stopped} containers`;
    if (response.data.skipped_busy > 0) {
      message += ` (${response.data.skipped_busy} busy, not stopped)`;
    }
    showSuccess(message);
    refreshPool();
  }
}
```

---

### 4. Warm Pool Overview Page (`/admin/warm-pool`)

**Components:**
- Global pool summary
- Start All / Stop All buttons
- Credentials with pool status table
- Quick actions per credential

**Flow:**
1. On mount, call `GET /bot-credentials` to get all credentials
2. For each credential, display warm_pool_status from response
3. Start All: Call `POST /bot-pool/start` without body
4. Stop All: Call `POST /bot-pool/stop` with `stop_all: true`

---

## Response Format Standard

All API responses follow this format:

```json
{
  "statusCode": number,
  "status": boolean,
  "message": string,
  "data": object
}
```

---

## Error Handling

### HTTP Status Codes

| Code | Meaning | Action |
|------|---------|--------|
| 200 | Success | Process response data |
| 400 | Bad Request | Show validation error |
| 401 | Unauthorized | Redirect to login |
| 403 | Forbidden | Show access denied |
| 404 | Not Found | Show not found message |
| 409 | Conflict | Show conflict message |
| 500 | Server Error | Show generic error |

### Frontend Error Handling Example

```javascript
async function apiCall(method, url, body = null) {
  try {
    const options = {
      method,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
      },
    };
    
    if (body) {
      options.body = JSON.stringify(body);
    }
    
    const response = await fetch(`${API_BASE_URL}${url}`, options);
    const data = await response.json();
    
    if (response.status === 401) {
      localStorage.clear();
      window.location.href = '/admin/login';
      return;
    }
    
    if (!data.status) {
      throw new Error(data.message);
    }
    
    return data;
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
}
```

---

## Status Badge Styling

```css
.badge {
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
}

/* Verification Status */
.badge-verified {
  background: #D1FAE5;
  color: #065F46;
}

.badge-not-verified {
  background: #FEF3C7;
  color: #92400E;
}

/* Container Status */
.badge-idle {
  background: #D1FAE5;
  color: #065F46;
}

.badge-busy {
  background: #FEF3C7;
  color: #92400E;
}

.badge-starting {
  background: #DBEAFE;
  color: #1E40AF;
}

.badge-error {
  background: #FEE2E2;
  color: #991B1B;
}
```

---

## Summary

### Available Endpoints:
1. ✅ `POST /bot-credentials` - Create bot credential
2. ✅ `GET /bot-credentials` - List all bot credentials
3. ✅ `GET /bot-credentials/{credentialId}` - Get single credential
4. ✅ `PUT /bot-credentials/{credentialId}` - Update credential
5. ✅ `DELETE /bot-credentials/{credentialId}` - Delete credential
6. ✅ `GET /bot-credentials/{credentialId}/verify` - Verify email (public)
7. ✅ `GET /bot-credentials/{credentialId}/pool` - List pool containers
8. ✅ `POST /warm-pool/start` - Start warm pool
9. ✅ `POST /warm-pool/stop` - Stop warm pool

### Pages to Build:
1. Bot Credentials List Page (`/admin/bot-credentials`)
2. Create/Edit Bot Credential Modal
3. Bot Pool Detail Page (`/admin/bot-credentials/{id}/pool`)
4. Warm Pool Overview Page (`/admin/warm-pool`)
