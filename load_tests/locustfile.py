"""
AXRAIL API Load Test Suite
===========================
Tests REST API and WebSocket endpoints under normal, peak, and stress loads.

Usage:
    locust -f locustfile.py --headless -u 50 -r 5 --run-time 5m --csv=results/normal
"""

import json
import time
import uuid
import logging

from locust import HttpUser, TaskSet, task, between, events
import websocket

from config import (
    BASE_URL, WS_URL,
    ADMIN_USERNAME, ADMIN_PASSWORD,
    USER_USERNAME, USER_PASSWORD,
    PROJECT_ID, SESSION_ID, AGENT_ID,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

class TokenCache:
    """Shared token cache so we don't re-auth on every request."""
    _admin_token: str | None = None
    _user_token: str | None = None

    @classmethod
    def get_admin_token(cls, client) -> str:
        if cls._admin_token:
            return cls._admin_token
        resp = client.post(
            "/auth/admin/login",
            json={"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD},
            name="/auth/admin/login [setup]",
        )
        data = resp.json()
        cls._admin_token = data.get("data", {}).get("access_token", "")
        return cls._admin_token

    @classmethod
    def get_user_token(cls, client) -> str:
        if cls._user_token:
            return cls._user_token
        resp = client.post(
            "/auth/user/login",
            json={"username": USER_USERNAME, "password": USER_PASSWORD},
            name="/auth/user/login [setup]",
        )
        data = resp.json()
        cls._user_token = data.get("data", {}).get("access_token", "")
        return cls._user_token


def admin_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def user_headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


# ---------------------------------------------------------------------------
# Task Sets
# ---------------------------------------------------------------------------

class AuthTasks(TaskSet):
    """Authentication endpoint tests."""

    @task(3)
    def admin_login(self):
        self.client.post(
            "/auth/admin/login",
            json={"username": ADMIN_USERNAME, "password": ADMIN_PASSWORD},
            name="POST /auth/admin/login",
        )

    @task(5)
    def user_login(self):
        self.client.post(
            "/auth/user/login",
            json={"username": USER_USERNAME, "password": USER_PASSWORD},
            name="POST /auth/user/login",
        )


class ProjectReadTasks(TaskSet):
    """Read-heavy project operations (most common user pattern)."""

    def on_start(self):
        self.token = TokenCache.get_admin_token(self.client)
        self.project_id = PROJECT_ID or self._create_project()

    def _create_project(self) -> str:
        resp = self.client.post(
            "/projects",
            json={
                "name": f"loadtest-{uuid.uuid4().hex[:8]}",
                "email": "loadtest@example.com",
                "description": "Load test project",
            },
            headers=admin_headers(self.token),
            name="POST /projects [setup]",
        )
        return resp.json().get("data", {}).get("project_id", "unknown")

    @task(5)
    def list_projects(self):
        self.client.get(
            "/projects",
            headers=admin_headers(self.token),
            name="GET /projects",
        )

    @task(3)
    def get_project(self):
        self.client.get(
            f"/projects/{self.project_id}",
            headers=admin_headers(self.token),
            name="GET /projects/{projectId}",
        )

    @task(2)
    def get_project_sessions(self):
        self.client.get(
            f"/projects/{self.project_id}/sessions",
            headers=admin_headers(self.token),
            name="GET /projects/{projectId}/sessions",
        )

    @task(1)
    def get_project_users(self):
        self.client.get(
            f"/projects/{self.project_id}/users",
            headers=admin_headers(self.token),
            name="GET /projects/{projectId}/users",
        )


class SessionTasks(TaskSet):
    """Session CRUD — the most frequently hit resource."""

    def on_start(self):
        self.token = TokenCache.get_admin_token(self.client)
        self.project_id = PROJECT_ID or self._ensure_project()
        self.session_ids: list[str] = []
        if SESSION_ID:
            self.session_ids.append(SESSION_ID)

    def _ensure_project(self) -> str:
        resp = self.client.post(
            "/projects",
            json={
                "name": f"loadtest-sess-{uuid.uuid4().hex[:8]}",
                "email": "loadtest@example.com",
            },
            headers=admin_headers(self.token),
            name="POST /projects [setup]",
        )
        return resp.json().get("data", {}).get("project_id", "unknown")

    @task(4)
    def list_sessions(self):
        self.client.get(
            "/sessions",
            headers=admin_headers(self.token),
            name="GET /sessions",
        )

    @task(3)
    def create_session(self):
        resp = self.client.post(
            "/sessions",
            json={
                "project_id": self.project_id,
                "name": f"loadtest-{uuid.uuid4().hex[:8]}",
            },
            headers=admin_headers(self.token),
            name="POST /sessions",
        )
        sid = resp.json().get("data", {}).get("session_id")
        if sid:
            self.session_ids.append(sid)

    @task(5)
    def get_session(self):
        if not self.session_ids:
            return
        sid = self.session_ids[-1]
        self.client.get(
            f"/sessions/{sid}",
            headers=admin_headers(self.token),
            name="GET /sessions/{sessionId}",
        )

    @task(2)
    def get_session_summary(self):
        if not self.session_ids:
            return
        sid = self.session_ids[-1]
        self.client.get(
            f"/sessions/{sid}/summary",
            headers=admin_headers(self.token),
            name="GET /sessions/{sessionId}/summary",
        )

    @task(2)
    def get_transcripts(self):
        if not self.session_ids:
            return
        sid = self.session_ids[-1]
        self.client.get(
            f"/sessions/{sid}/transcripts",
            headers=admin_headers(self.token),
            name="GET /sessions/{sessionId}/transcripts",
        )

    @task(1)
    def get_suggested_questions(self):
        if not self.session_ids:
            return
        sid = self.session_ids[-1]
        self.client.get(
            f"/sessions/{sid}/suggested-questions",
            headers=admin_headers(self.token),
            name="GET /sessions/{sessionId}/suggested-questions",
        )


class AgentConfigTasks(TaskSet):
    """Agent, personality, and skill management (admin-heavy)."""

    def on_start(self):
        self.token = TokenCache.get_admin_token(self.client)

    @task(4)
    def list_agents(self):
        self.client.get(
            "/agents",
            headers=admin_headers(self.token),
            name="GET /agents",
        )

    @task(3)
    def list_personalities(self):
        self.client.get(
            "/personalities",
            headers=admin_headers(self.token),
            name="GET /personalities",
        )

    @task(3)
    def list_skills(self):
        self.client.get(
            "/skills",
            headers=admin_headers(self.token),
            name="GET /skills",
        )

    @task(1)
    def list_bot_credentials(self):
        self.client.get(
            "/bot-credentials",
            headers=admin_headers(self.token),
            name="GET /bot-credentials",
        )


class WebSocketTasks(TaskSet):
    """WebSocket connection and message tests."""

    def on_start(self):
        self.token = TokenCache.get_admin_token(self.client)
        self.session_id = SESSION_ID or self._ensure_session()
        self.agent_id = AGENT_ID or ""

    def _ensure_session(self) -> str:
        # Create a project + session for WS testing
        resp = self.client.post(
            "/projects",
            json={"name": f"ws-test-{uuid.uuid4().hex[:8]}", "email": "ws@example.com"},
            headers=admin_headers(self.token),
            name="POST /projects [ws-setup]",
        )
        pid = resp.json().get("data", {}).get("project_id", "unknown")
        resp = self.client.post(
            "/sessions",
            json={"project_id": pid, "name": f"ws-sess-{uuid.uuid4().hex[:8]}"},
            headers=admin_headers(self.token),
            name="POST /sessions [ws-setup]",
        )
        return resp.json().get("data", {}).get("session_id", "unknown")

    def _ws_connect(self) -> websocket.WebSocket | None:
        url = f"{WS_URL}?session_id={self.session_id}"
        if self.agent_id:
            url += f"&agent_id={self.agent_id}"
        start = time.time()
        try:
            ws = websocket.create_connection(url, timeout=10)
            elapsed = (time.time() - start) * 1000
            events.request.fire(
                request_type="WSS",
                name="WS $connect",
                response_time=elapsed,
                response_length=0,
                exception=None,
            )
            return ws
        except Exception as e:
            elapsed = (time.time() - start) * 1000
            events.request.fire(
                request_type="WSS",
                name="WS $connect",
                response_time=elapsed,
                response_length=0,
                exception=e,
            )
            return None

    def _ws_send(self, ws, payload: dict, name: str) -> dict | None:
        start = time.time()
        try:
            ws.send(json.dumps(payload))
            result = ws.recv()
            elapsed = (time.time() - start) * 1000
            events.request.fire(
                request_type="WSS",
                name=name,
                response_time=elapsed,
                response_length=len(result),
                exception=None,
            )
            return json.loads(result)
        except Exception as e:
            elapsed = (time.time() - start) * 1000
            events.request.fire(
                request_type="WSS",
                name=name,
                response_time=elapsed,
                response_length=0,
                exception=e,
            )
            return None

    @task(3)
    def send_message(self):
        ws = self._ws_connect()
        if not ws:
            return
        try:
            self._ws_send(ws, {
                "action": "sendMessage",
                "session_id": self.session_id,
                "message": "What were the key topics discussed?",
            }, "WS sendMessage")
        finally:
            ws.close()

    @task(2)
    def detect_question(self):
        ws = self._ws_connect()
        if not ws:
            return
        try:
            self._ws_send(ws, {
                "action": "detectQuestion",
                "session_id": self.session_id,
                "question": "What is the project timeline?",
            }, "WS detectQuestion")
        finally:
            ws.close()

    @task(4)
    def process_transcript(self):
        ws = self._ws_connect()
        if not ws:
            return
        try:
            self._ws_send(ws, {
                "action": "processTranscript",
                "session_id": self.session_id,
                "lines": [{
                    "speaker": "spk_0",
                    "text": "Can you walk me through the pricing model?",
                    "start_time": 120.5,
                    "end_time": 124.3,
                    "confidence": 0.92,
                    "is_partial": False,
                }],
            }, "WS processTranscript")
        finally:
            ws.close()

    @task(1)
    def analyze_gaps(self):
        ws = self._ws_connect()
        if not ws:
            return
        try:
            self._ws_send(ws, {
                "action": "analyzeGaps",
                "session_id": self.session_id,
            }, "WS analyzeGaps")
        finally:
            ws.close()


# ---------------------------------------------------------------------------
# User Classes (weighted to simulate realistic traffic mix)
# ---------------------------------------------------------------------------

class RegularUser(HttpUser):
    """Simulates a regular user: mostly reads sessions, some WS activity."""
    host = BASE_URL
    wait_time = between(1, 3)
    weight = 5
    tasks = {
        SessionTasks: 4,
        ProjectReadTasks: 3,
        WebSocketTasks: 2,
    }


class AdminUser(HttpUser):
    """Simulates an admin: config management, auth, CRUD."""
    host = BASE_URL
    wait_time = between(1, 5)
    weight = 2
    tasks = {
        AuthTasks: 2,
        AgentConfigTasks: 3,
        ProjectReadTasks: 2,
        SessionTasks: 3,
    }


class WebSocketHeavyUser(HttpUser):
    """Simulates a live-mee