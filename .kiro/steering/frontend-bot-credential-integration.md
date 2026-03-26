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
│   Create    │────▶│  Validating │────▶│  Verified   │────▶│   Active    │
│  Credential │     │   (SMTP)    │     │   Ready     │     │   Ready     │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                   │                                       │
       │                   │ (invalid)                             ▼
       │                   ▼                                ┌─────────────┐
       │            ┌──────────────────┐                    │  Assign to  │
       │            │ verification_    │                    │   Project   │
       │            │ failed           │                    └─────────────┘
       │            │ (can retry)      │                           │
       │            └──────────────────┘                           ▼
       │                   │                                ┌─────────────┐
       │                   │ (update email/password)        │  Start Warm │
       │                   └───────────────────────────────▶│    Pool     │
       │                                                    └─────────────┘
```

### Verification Flow (Async SMTP Validation)

1. Admin creates credential via `POST /bot-credentials`
2. Backend validates input (email format, password not empty, warm_pool_size >= 0)
3. Backend saves credential with `verification_status: "validating"`
4. EventBridge triggers async SMTP validation worker
5. Worker attempts SMTP login with email/password
6. If valid: status updated to `"verified"`, `available_status` set to `"active"`
7. If invalid: status updated to `"verification_failed"` with `verification_error` message
8. Frontend polls `GET /bot-credentials/{id}/verify` to check status
9. If failed, admin can update email/password via `PUT /bot-credentials/{id}` to retry

### Status Fields

| Field | Values | Description |
|-------|--------|-------------|
| `verification_status` | `validating`, `verified`, `verification_failed` | SMTP validation state |
| `verification_error` | string | Error message when verification_failed |
| `available_status` | `inactive`, `active` | Whether credential can be used |

---

## API Endpoints

### Bot Credential Endpoints

#### 1. Create Bot Credential
**POST** `/bot-credentials`

Creates a new bot credential and triggers async SMTP validation.

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
| `email` | string | Yes | Bot account email (valid email format) |
| `password` | string | Yes | Bot account password (cannot be empty, hyphens auto-removed) |
| `warm_pool_size` | integer | No | Number of warm containers (default: 1, min: 0) |

**Input Validation:**
- Email: Must be valid email format (regex validated)
- Password: Cannot be empty or whitespace only
- warm_pool_size: Must be non-negative integer (>= 0)

**Supported Email Providers:**
- Gmail (`@gmail.com`, `@googlemail.com`) - requires App Password if 2FA enabled
- Google Workspace (custom domains with Google MX records)
- Outlook (`@outlook.com`, `@hotmail.com`, `@live.com`) - requires App Password if 2FA enabled
- Microsoft 365 (custom domains with Microsoft MX records)
- Yahoo (`@yahoo.com`)
- iCloud (`@icloud.com`, `@me.com`)
- Zoho (`@zoho.com`)

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Bot credential created. Validating email credentials...",
  "data": {
    "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "email": "bot@example.com",
    "verification_status": "validating",
    "available_status": "inactive",
    "warm_pool_size": 2,
    "created_at": "2024-01-15T10:30:00.000000+00:00",
    "updated_at": "2024-01-15T10:30:00.000000+00:00"
  }
}
```

**Error Responses:**
- `400`: Missing required fields / Invalid email format / Password cannot be empty / Invalid warm_pool_size
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
| `email` | string | New email (valid format, triggers re-verification) |
| `password` | string | New password (cannot be empty, triggers re-verification) |
| `available_status` | string | `active` or `inactive` |
| `warm_pool_size` | integer | Number of warm containers (>= 0) |

**Input Validation:**
- Email: Must be valid email format (regex validated)
- Password: Cannot be empty or whitespace only
- warm_pool_size: Must be non-negative integer (>= 0)
- available_status: Must be "active" or "inactive"

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
- `400`: No update data provided / Invalid email format / Password cannot be empty / Invalid available_status / Invalid warm_pool_size
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

#### 6. Check Verification Status
**GET** `/bot-credentials/{credentialId}/verify`

Returns current verification status. Frontend should poll this endpoint after creating a credential.

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Success Response (200) - Validating:**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Validation in progress...",
  "data": {
    "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "email": "bot@example.com",
    "verification_status": "validating"
  }
}
```

**Success Response (200) - Verified:**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Email credentials verified successfully",
  "data": {
    "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "email": "bot@example.com",
    "verification_status": "verified"
  }
}
```

**Success Response (200) - Verification Failed:**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Email credentials validation failed",
  "data": {
    "credential_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "email": "bot@example.com",
    "verification_status": "verification_failed",
    "verification_error": "Invalid email or password. For Gmail/Outlook, use App Password if 2FA is enabled."
  }
}
```

**Error Responses:**
- `400`: Credential ID is required
- `401`: Unauthorized (not admin)
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
    <!-- Failed verification row -->
    <tr>
      <td>
        invalid@example.com
        <span class="text-red text-sm">Invalid credentials</span>
      </td>
      <td>
        <span class="badge badge-danger">Failed</span>
        <button class="btn-sm">Retry</button>
      </td>
      <td><toggle disabled /></td>
      <td>1</td>
      <td>-</td>
      <td>
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
- Email: Valid email format (regex: `/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/`)
- Password: Required for create, cannot be empty
- Warm Pool Size: Non-negative integer (>= 0)

**Create Flow:**
```javascript
async function createCredential(data) {
  // Frontend validation
  if (!isValidEmail(data.email)) {
    showError('Invalid email format');
    return;
  }
  if (!data.password || !data.password.trim()) {
    showError('Password cannot be empty');
    return;
  }
  if (data.warmPoolSize !== undefined && (data.warmPoolSize < 0 || !Number.isInteger(data.warmPoolSize))) {
    showError('Warm pool size must be a non-negative integer');
    return;
  }

  const response = await apiCall('POST', '/bot-credentials', {
    email: data.email,
    password: data.password,
    warm_pool_size: data.warmPoolSize ?? 1
  });
  
  if (response.status) {
    showInfo('Credential created. Validating email credentials...');
    // Start polling for verification status
    pollVerificationStatus(response.data.credential_id);
  }
}

function isValidEmail(email) {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return emailRegex.test(email);
}

// Poll verification status every 2 seconds
async function pollVerificationStatus(credentialId, maxAttempts = 30) {
  let attempts = 0;
  
  const poll = async () => {
    attempts++;
    try {
      const response = await apiCall('GET', `/bot-credentials/${credentialId}/verify`);
      
      if (response.data.verification_status === 'verified') {
        showSuccess('Email credentials verified successfully!');
        refreshList();
        closeModal();
        return;
      }
      
      if (response.data.verification_status === 'verification_failed') {
        const errorMsg = response.data.verification_error || 'Verification failed';
        showError(`Verification failed: ${errorMsg}`);
        // Keep modal open so user can update credentials
        setFormError(errorMsg);
        return;
      }
      
      if (response.data.verification_status === 'validating' && attempts < maxAttempts) {
        setTimeout(poll, 2000);
        return;
      }
      
      // Timeout after max attempts
      showWarning('Verification is taking longer than expected. Please check back later.');
      refreshList();
      closeModal();
    } catch (error) {
      showError('Error checking verification status');
      throw error;
    }
  };
  
  poll();
}
```

**Edit Flow:**
```javascript
async function updateCredential(credentialId, data) {
  // Frontend validation
  if (data.email && !isValidEmail(data.email)) {
    showError('Invalid email format');
    return;
  }
  if (data.password !== undefined && (!data.password || !data.password.trim())) {
    showError('Password cannot be empty');
    return;
  }
  if (data.warmPoolSize !== undefined && (data.warmPoolSize < 0 || !Number.isInteger(data.warmPoolSize))) {
    showError('Warm pool size must be a non-negative integer');
    return;
  }

  const payload = {};
  if (data.email) payload.email = data.email;
  if (data.password) payload.password = data.password;
  if (data.warmPoolSize !== undefined) payload.warm_pool_size = data.warmPoolSize;
  if (data.availableStatus !== undefined) {
    payload.available_status = data.availableStatus ? 'active' : 'inactive';
  }
  
  const response = await apiCall('PUT', `/bot-credentials/${credentialId}`, payload);
  
  if (response.status) {
    if (response.message.includes('Re-validating')) {
      showInfo('Credential updated. Re-validating email credentials...');
      // Start polling for verification status
      pollVerificationStatus(credentialId);
    } else {
      showSuccess('Credential updated successfully.');
      refreshList();
      closeModal();
    }
  }
}
```

**Retry Failed Verification Flow:**
```javascript
// When verification_status is 'verification_failed', show retry option
async function retryVerification(credentialId, newPassword) {
  if (!newPassword || !newPassword.trim()) {
    showError('Password cannot be empty');
    return;
  }

  const response = await apiCall('PUT', `/bot-credentials/${credentialId}`, {
    password: newPassword
  });
  
  if (response.status) {
    showInfo('Re-validating email credentials...');
    pollVerificationStatus(credentialId);
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

.badge-validating {
  background: #DBEAFE;
  color: #1E40AF;
}

.badge-verification-failed {
  background: #FEE2E2;
  color: #991B1B;
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
1. ✅ `POST /bot-credentials` - Create bot credential (triggers async SMTP validation)
2. ✅ `GET /bot-credentials` - List all bot credentials
3. ✅ `GET /bot-credentials/{credentialId}` - Get single credential
4. ✅ `PUT /bot-credentials/{credentialId}` - Update credential
5. ✅ `DELETE /bot-credentials/{credentialId}` - Delete credential
6. ✅ `GET /bot-credentials/{credentialId}/verify` - Check verification status (poll this)
7. ✅ `GET /bot-credentials/{credentialId}/pool` - List pool containers
8. ✅ `POST /warm-pool/start` - Start warm pool
9. ✅ `POST /warm-pool/stop` - Stop warm pool

### Pages to Build:
1. Bot Credentials List Page (`/admin/bot-credentials`)
2. Create/Edit Bot Credential Modal
3. Bot Pool Detail Page (`/admin/bot-credentials/{id}/pool`)
4. Warm Pool Overview Page (`/admin/warm-pool`)
