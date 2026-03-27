---
inclusion: manual
name: frontend-cognito-integration
description: Frontend integration guide for Cognito authentication API. Covers endpoints, request/response formats, and flows for admin and user authentication.
---

# Frontend Cognito Integration Guide

## Overview

This document provides a complete guide for integrating frontend with AWS Cognito-based authentication API. The system has two user types:
- **Admin**: Can manage users, projects, and all resources
- **User**: Can access assigned projects and manage sessions

## Base URL

```
{API_GATEWAY_URL}/{stage}
```

Example: `https://abc123.execute-api.ap-southeast-1.amazonaws.com/dev`

---

## Authentication Flow

### 1. Login Flow (Admin & User)

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Login     │────▶│  Response   │────▶│  Dashboard  │
│   Page      │     │  Check      │     │  or Change  │
└─────────────┘     └─────────────┘     │  Password   │
                           │            └─────────────┘
                           │
                    Has Challenge?
                           │
                    ┌──────┴──────┐
                    │             │
                   Yes           No
                    │             │
                    ▼             ▼
            ┌─────────────┐  ┌─────────────┐
            │   Change    │  │   Store     │
            │   Password  │  │   Tokens    │
            │   Page      │  │   & Redirect│
            └─────────────┘  └─────────────┘
```

### 2. Token Storage

Store tokens in localStorage or secure cookie:
```javascript
// After successful login
localStorage.setItem('access_token', data.access_token);
localStorage.setItem('id_token', data.id_token);
localStorage.setItem('refresh_token', data.refresh_token);
```

### 3. Authorization Header

All requests to protected endpoints must include:
```
Authorization: Bearer {access_token}
```

---

## API Endpoints

### Authentication Endpoints

#### 1. Admin Login
**POST** `/auth/admin/login`

**Request Body:**
```json
{
  "username": "admin@example.com",
  "password": "password123"
}
```

**Success Response (200) - Normal Login:**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Admin login successful",
  "data": {
    "access_token": "eyJraWQiOiJ...",
    "id_token": "eyJraWQiOiJ...",
    "refresh_token": "eyJjdHkiOiJ...",
    "token_type": "Bearer",
    "expires_in": 3600
  }
}
```

**Success Response (200) - Password Change Required:**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Password change required",
  "data": {
    "challenge": "NEW_PASSWORD_REQUIRED",
    "session": "AYABeC1u8...",
    "username": "admin@example.com"
  }
}
```

**Error Responses:**
- `400`: Missing required fields
- `401`: Invalid username or password
- `404`: User not found
- `500`: Internal server error

---

#### 2. User Login
**POST** `/auth/user/login`

**Request Body:**
```json
{
  "username": "user_abc123",
  "password": "password123"
}
```

**Success Response (200) - Normal Login:**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "User login successful",
  "data": {
    "access_token": "eyJraWQiOiJ...",
    "id_token": "eyJraWQiOiJ...",
    "refresh_token": "eyJjdHkiOiJ...",
    "token_type": "Bearer",
    "expires_in": 3600
  }
}
```

**Success Response (200) - Password Change Required:**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Password change required",
  "data": {
    "challenge": "NEW_PASSWORD_REQUIRED",
    "session": "AYABeC1u8...",
    "username": "user_abc123"
  }
}
```

**Error Responses:**
- `400`: Missing required fields
- `401`: Invalid username or password
- `404`: User not found
- `500`: Internal server error

---

#### 3. Change Password (First Login)
**POST** `/auth/change-password`

Used when user logs in for the first time and receives `NEW_PASSWORD_REQUIRED` challenge.

**Request Body:**
```json
{
  "session": "AYABeC1u8...",
  "username": "user_abc123",
  "new_password": "NewSecurePassword123!"
}
```

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Password changed successfully",
  "data": {
    "access_token": "eyJraWQiOiJ...",
    "id_token": "eyJraWQiOiJ...",
    "refresh_token": "eyJjdHkiOiJ...",
    "token_type": "Bearer",
    "expires_in": 3600
  }
}
```

**Error Responses:**
- `400`: Missing required fields / Invalid password / Session expired
- `401`: Unauthorized
- `500`: Internal server error

**Password Requirements:**
- Minimum 8 characters
- At least 1 uppercase letter
- At least 1 lowercase letter
- At least 1 number
- At least 1 special character

---

#### 4. Logout
**POST** `/auth/logout`

**Headers:**
```
Authorization: Bearer {access_token}
```

**Request Body:** None

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Logged out successfully"
}
```

**Error Responses:**
- `400`: Access token is required
- `401`: Invalid or expired token
- `500`: Internal server error

---

### User Management Endpoints (Admin Only)

#### 5. Create User
**POST** `/users`

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Request Body:**
```json
{
  "email": "newuser@example.com"
}
```

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "User created successfully",
  "data": {
    "user_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "username": "newuser_abc12345",
    "email": "newuser@example.com",
    "role": "user",
    "created_by": "admin@example.com",
    "created_at": "2024-01-15T10:30:00.000000"
  }
}
```

**Notes:**
- Password is automatically sent to user's email
- Username is auto-generated from email + UUID
- User will be prompted to change password on first login

**Error Responses:**
- `400`: Missing required fields
- `401`: Unauthorized (not admin)
- `404`: Not found
- `409`: User with email already exists
- `500`: Internal server error

---

#### 6. List Users
**GET** `/users`

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "Users retrieved successfully",
  "data": {
    "users": [
      {
        "user_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
        "username": "user_abc12345",
        "email": "user@example.com",
        "role": "user",
        "created_by": "admin@example.com",
        "created_at": "2024-01-15T10:30:00.000000"
      }
    ]
  }
}
```

**Error Responses:**
- `401`: Unauthorized (not admin)
- `500`: Internal server error

---

#### 7. Get User
**GET** `/users/{userId}`

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "User retrieved successfully",
  "data": {
    "user_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "username": "user_abc12345",
    "email": "user@example.com",
    "role": "user",
    "created_by": "admin@example.com",
    "created_at": "2024-01-15T10:30:00.000000"
  }
}
```

**Error Responses:**
- `400`: User ID is required
- `401`: Unauthorized (not admin)
- `404`: User not found
- `500`: Internal server error

---

#### 8. Update User
**PUT** `/users/{userId}`

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Request Body:**
```json
{
  "email": "updated@example.com"
}
```

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "User updated successfully",
  "data": {
    "user_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "username": "user_abc12345",
    "email": "updated@example.com",
    "role": "user",
    "created_by": "admin@example.com",
    "created_at": "2024-01-15T10:30:00.000000",
    "updated_at": "2024-01-16T14:00:00.000000"
  }
}
```

**Error Responses:**
- `400`: User ID is required / Request body is required
- `401`: Unauthorized (not admin)
- `404`: User not found
- `500`: Internal server error

---

#### 9. Delete User
**DELETE** `/users/{userId}`

**Headers:**
```
Authorization: Bearer {admin_access_token}
```

**Success Response (200):**
```json
{
  "statusCode": 200,
  "status": true,
  "message": "User deleted successfully"
}
```

**Error Responses:**
- `400`: User ID is required
- `401`: Unauthorized (not admin)
- `404`: User not found
- `500`: Internal server error

---

## Frontend Pages

### 1. Admin Login Page (`/admin/login`)

**Components:**
- Form with fields: username/email, password
- Submit button
- Error message display

**Flow:**
1. User submits form
2. Call `POST /auth/admin/login`
3. If response has `challenge: "NEW_PASSWORD_REQUIRED"`:
   - Store `session` and `username` in state
   - Redirect to `/admin/change-password`
4. If successful without challenge:
   - Store tokens in localStorage
   - Redirect to `/admin/dashboard`

---

### 2. Admin Change Password Page (`/admin/change-password`)

**Components:**
- Form with fields: new password, confirm password
- Password strength indicator
- Submit button
- Error message display

**Flow:**
1. Get `session` and `username` from state/query params
2. User submits form
3. Call `POST /auth/change-password`
4. If successful:
   - Store tokens in localStorage
   - Redirect to `/admin/dashboard`

---

### 3. Admin Dashboard (`/admin/dashboard`)

**Components:**
- Sidebar navigation
- Header with user info and logout button
- Main content area

**Navigation Items:**
- Dashboard (overview)
- Users
- Projects
- Sessions
- Settings

---

### 4. Admin Users Page (`/admin/users`)

**Components:**
- Header with "Create User" button
- Search/filter bar
- Users table with columns:
  - Name (username)
  - Email
  - Created By
  - Created At
  - Actions (Edit, Delete)
- Pagination

**Table Structure:**
```html
<table>
  <thead>
    <tr>
      <th>Name</th>
      <th>Email</th>
      <th>Created By</th>
      <th>Created At</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>user_abc12345</td>
      <td>user@example.com</td>
      <td>admin@example.com</td>
      <td>Jan 15, 2024 10:30 AM</td>
      <td>
        <button>Edit</button>
        <button>Delete</button>
      </td>
    </tr>
  </tbody>
</table>
```

**Flow:**
1. On mount, call `GET /users`
2. Display users in table
3. Create User: Open modal, call `POST /users`
4. Edit User: Open modal, call `PUT /users/{userId}`
5. Delete User: Confirm dialog, call `DELETE /users/{userId}`

---

### 5. User Login Page (`/login`)

**Components:**
- Form with fields: username, password
- Submit button
- Error message display

**Flow:**
1. User submits form
2. Call `POST /auth/user/login`
3. If response has `challenge: "NEW_PASSWORD_REQUIRED"`:
   - Store `session` and `username` in state
   - Redirect to `/change-password`
4. If successful without challenge:
   - Store tokens in localStorage
   - Redirect to `/dashboard`

---

### 6. User Change Password Page (`/change-password`)

**Components:**
- Form with fields: new password, confirm password
- Password strength indicator
- Submit button
- Error message display

**Flow:**
1. Get `session` and `username` from state/query params
2. User submits form
3. Call `POST /auth/change-password`
4. If successful:
   - Store tokens in localStorage
   - Redirect to `/dashboard`

---

## Response Format Standard

All API responses follow this format:

```json
{
  "statusCode": number,    // HTTP status code
  "status": boolean,       // true if successful (statusCode < 400)
  "message": string,       // Human-readable message
  "data": object          // Optional, payload data
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
| 409 | Conflict | Show conflict message (e.g., email exists) |
| 500 | Server Error | Show generic error |

### Frontend Error Handling Example

```javascript
async function apiCall(url, options) {
  try {
    const response = await fetch(url, {
      ...options,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
        ...options.headers,
      },
    });
    
    const data = await response.json();
    
    if (response.status === 401) {
      // Token expired or invalid
      localStorage.clear();
      window.location.href = '/login';
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

## CDK Configuration Required

The following Lambda functions need to be added to `stack_cdk/lambda_stack.py`:

```python
# ListUsers Lambda
self.list_users_fn = self._create_lambda_function(
    "ListUsers", "lambdas/Functions/ListUsers"
)

# GetUser Lambda
self.get_user_fn = self._create_lambda_function(
    "GetUser", "lambdas/Functions/GetUser"
)

# UpdateUser Lambda
self.update_user_fn = self._create_lambda_function(
    "UpdateUser", "lambdas/Functions/UpdateUser"
)

# DeleteUser Lambda
self.delete_user_fn = self._create_lambda_function(
    "DeleteUser", "lambdas/Functions/DeleteUser"
)
```

Add these routes to `stack_cdk/api_services_stack.py` in `_create_auth_routes`:

```python
# GET /users - List all users (admin only)
users_resource.add_method(
    "GET",
    apigw.LambdaIntegration(self.lambda_stack.list_users_fn),
    authorizer=self.admin_authorizer,
    authorization_type=apigw.AuthorizationType.CUSTOM,
)

# GET /users/{userId} - Get single user (admin only)
user_resource.add_method(
    "GET",
    apigw.LambdaIntegration(self.lambda_stack.get_user_fn),
    authorizer=self.admin_authorizer,
    authorization_type=apigw.AuthorizationType.CUSTOM,
)

# PUT /users/{userId} - Update user (admin only)
user_resource.add_method(
    "PUT",
    apigw.LambdaIntegration(self.lambda_stack.update_user_fn),
    authorizer=self.admin_authorizer,
    authorization_type=apigw.AuthorizationType.CUSTOM,
)

# DELETE /users/{userId} - Delete user (admin only)
user_resource.add_method(
    "DELETE",
    apigw.LambdaIntegration(self.lambda_stack.delete_user_fn),
    authorizer=self.admin_authorizer,
    authorization_type=apigw.AuthorizationType.CUSTOM,
)
```

---

## Design Style Guidelines

Follow consistent design style with the application:

### Color Palette
- Primary: #3B82F6 (Blue)
- Success: #10B981 (Green)
- Warning: #F59E0B (Amber)
- Error: #EF4444 (Red)
- Background: #F9FAFB (Light Gray)
- Text: #111827 (Dark Gray)

### Component Styling
- Border radius: 8px for cards, 4px for buttons
- Shadow: `0 1px 3px rgba(0,0,0,0.1)`
- Padding: 16px for cards, 8px-12px for buttons
- Font: Inter or system font stack

### Table Styling
```css
.table {
  width: 100%;
  border-collapse: collapse;
}

.table th {
  background: #F3F4F6;
  padding: 12px 16px;
  text-align: left;
  font-weight: 600;
  color: #374151;
}

.table td {
  padding: 12px 16px;
  border-bottom: 1px solid #E5E7EB;
}

.table tr:hover {
  background: #F9FAFB;
}
```

### Button Styling
```css
.btn-primary {
  background: #3B82F6;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}

.btn-primary:hover {
  background: #2563EB;
}

.btn-danger {
  background: #EF4444;
  color: white;
}

.btn-danger:hover {
  background: #DC2626;
}
```

---

## Summary

### Available Endpoints:
1. ✅ `POST /auth/admin/login` - Admin login
2. ✅ `POST /auth/user/login` - User login
3. ✅ `POST /auth/change-password` - Change password (first login)
4. ✅ `POST /auth/logout` - Logout
5. ✅ `POST /users` - Create user (admin only)
6. ✅ `GET /users` - List all users (admin only)
7. ✅ `GET /users/{userId}` - Get single user (admin only)
8. ✅ `PUT /users/{userId}` - Update user (admin only)
9. ✅ `DELETE /users/{userId}` - Delete user (admin only)

### Pages to Build:
1. Admin Login Page (`/admin/login`)
2. Admin Change Password Page (`/admin/change-password`)
3. Admin Dashboard (`/admin/dashboard`)
4. Admin Users Page (`/admin/users`)
5. User Login Page (`/login`)
6. User Change Password Page (`/change-password`)
