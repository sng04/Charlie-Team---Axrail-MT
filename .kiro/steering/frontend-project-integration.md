---
inclusion: manual
name: frontend-project-integration
description: Frontend integration guide for Delete Project API. Covers cascade delete behavior, error handling for active meetings, and confirmation UX patterns.
---

# Frontend Project Delete Integration Guide

## Overview

Delete Project performs a cascade delete — removing the project along with all related data (sessions, transcripts, project-user assignments). Bot credentials are NOT deleted.

The cascade delete is fully handled by the backend. The frontend only needs to call a single `DELETE /projects/{projectId}` endpoint — no need to delete sessions, transcripts, or user assignments separately.

This endpoint is admin-only (enforced by Lambda Authorizer).

---

## API Endpoint

```
DELETE /projects/{projectId}
```

Authorization: Admin JWT token (via AdminAuthorizer)

---

## Response Scenarios

### Success (200)

```json
{
  "statusCode": 200,
  "status": true,
  "message": "Project and all related data deleted successfully"
}
```

### Blocked by Active Meeting (409)

If any session has `bot_status = "in_meeting"`, the delete is rejected:

```json
{
  "statusCode": 409,
  "status": false,
  "message": "Cannot delete project while a meeting is in progress. Please end all active meetings first."
}
```

### Project Not Found (404)

```json
{
  "statusCode": 404,
  "status": false,
  "message": "Project {projectId} not found"
}
```

---

## Cascade Delete Behavior

When a project is deleted, the following data is removed in order:

1. All **transcripts** from every session belonging to the project
2. All **sessions** belonging to the project
3. All **project-user assignments** (ProjectUsers table)
4. The **project** itself

Data that is NOT deleted:
- Bot credentials (BotCredentials table)
- User accounts (Users table)

---

## Frontend Implementation

### Confirmation Dialog

Since delete is destructive and irreversible, show a confirmation dialog:

```javascript
async function deleteProject(projectId, projectName) {
  const confirmed = await showConfirmDialog({
    title: 'Delete Project',
    message: `Are you sure you want to delete "${projectName}"? This will permanently delete all sessions, transcripts, and user assignments. This action cannot be undone.`,
    confirmText: 'Delete Project',
    confirmVariant: 'destructive',
  });

  if (!confirmed) return;

  try {
    const response = await apiClient.delete(`/projects/${projectId}`);
    showToast('Project deleted successfully');
    navigateTo('/projects');
  } catch (error) {
    if (error.status === 409) {
      showToast(error.message, 'warning');
    } else if (error.status === 404) {
      showToast('Project not found', 'error');
    } else {
      showToast('Failed to delete project', 'error');
    }
  }
}
```

### UX Recommendations

- Disable the delete button if any session has a bot_status outside of `none`, `stopped`, `completed`, `failed` (check via GetProjectSessions). Show a tooltip explaining why delete is disabled (e.g., "Cannot delete while sessions are active").
- Also disable the edit button if any session has a bot_status of `pending`, `queued`, `starting`, `joining`, `in_meeting`, or `stopping` — the project should not be modified while containers are running or starting.
- Show the number of sessions and transcripts that will be deleted in the confirmation dialog
- After a successful delete, redirect to the project list and refresh data
- Handle 409 with a clear message that the user must end the meeting first
