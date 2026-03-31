"""Unit tests for CreateSession Lambda handler."""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

CREATE_SESSION_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "CreateSession")
)


def _import_handler(
    mock_sessions, mock_projects, mock_project_users, mock_bot_creds, mock_bot_pool=None,
):
    sys.path.insert(0, CREATE_SESSION_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource") as mock_boto, \
         patch("boto3.client") as mock_client_factory:
        mock_dynamo = MagicMock()
        mock_boto.return_value = mock_dynamo

        table_map = {
            "test-sessions": mock_sessions,
            "test-projects": mock_projects,
            "test-project-users": mock_project_users,
            "test-bot-creds": mock_bot_creds,
            "test-bot-pool": mock_bot_pool or MagicMock(),
        }
        mock_dynamo.Table.side_effect = lambda name: table_map.get(name, MagicMock())

        mock_ecs = MagicMock()
        mock_sqs = MagicMock()
        mock_client_factory.side_effect = lambda svc, **kw: mock_ecs if svc == "ecs" else mock_sqs

        import lambda_function as mod

    return mod, mock_ecs


def _cleanup():
    if CREATE_SESSION_DIR in sys.path:
        sys.path.remove(CREATE_SESSION_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(os.environ, {
        "SESSIONS_TABLE": "test-sessions",
        "PROJECTS_TABLE": "test-projects",
        "PROJECT_USERS_TABLE": "test-project-users",
        "BOT_CREDENTIALS_TABLE": "test-bot-creds",
        "BOT_POOL_TABLE": "test-bot-pool",
        "ECS_CLUSTER": "test-cluster",
        "ECS_TASK_DEFINITION": "test-task-def",
        "ECS_SUBNETS": "subnet-1,subnet-2",
        "ECS_SECURITY_GROUP": "sg-123",
        "WARM_POOL_ENABLED": "false",
    }):
        yield
    _cleanup()


class TestCreateSession:
    def test_create_session_success(self):
        mock_sessions = MagicMock()
        mock_projects = MagicMock()
        mock_projects.get_item.return_value = {
            "Item": {
                "project_id": "proj-1",
                "bot_credential_id": "cred-1",
            }
        }
        mock_project_users = MagicMock()
        mock_bot_creds = MagicMock()
        mock_bot_creds.get_item.return_value = {
            "Item": {
                "credential_id": "cred-1",
                "verification_status": "verified",
                "available_status": "active",
            }
        }

        handler_mod, mock_ecs = _import_handler(
            mock_sessions, mock_projects, mock_project_users, mock_bot_creds,
        )
        mock_ecs.run_task.return_value = {
            "tasks": [{"taskArn": "arn:aws:ecs:us-east-1:123:task/abc"}]
        }
        try:
            event = {
                "body": json.dumps({
                    "project_id": "proj-1",
                    "name": "Test Session",
                    "meeting_link": "https://meet.google.com/abc-defg-hij",
                }),
                "requestContext": {
                    "authorizer": {"user_id": "admin-1", "groups": "admin"},
                },
            }
            response = handler_mod.lambda_handler(event, None)
            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            assert "session_id" in body["data"]
            assert body["data"]["is_active"] == "inactive"
            mock_sessions.put_item.assert_called_once()
        finally:
            _cleanup()

    def test_create_session_missing_fields_returns_400(self):
        mock_sessions = MagicMock()
        mock_projects = MagicMock()
        mock_project_users = MagicMock()
        mock_bot_creds = MagicMock()

        handler_mod, _ = _import_handler(
            mock_sessions, mock_projects, mock_project_users, mock_bot_creds,
        )
        try:
            event = {
                "body": json.dumps({"name": "No project or link"}),
                "requestContext": {
                    "authorizer": {"user_id": "admin-1", "groups": "admin"},
                },
            }
            response = handler_mod.lambda_handler(event, None)
            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert body["status"] is False
            assert "project_id" in body["message"]
        finally:
            _cleanup()

    def test_create_session_bot_dispatch_error_returns_500(self):
        mock_sessions = MagicMock()
        mock_sessions.put_item.side_effect = Exception("DynamoDB error")
        mock_projects = MagicMock()
        mock_projects.get_item.return_value = {
            "Item": {"project_id": "proj-1", "bot_credential_id": "cred-1"}
        }
        mock_project_users = MagicMock()
        mock_bot_creds = MagicMock()
        mock_bot_creds.get_item.return_value = {
            "Item": {
                "credential_id": "cred-1",
                "verification_status": "verified",
                "available_status": "active",
            }
        }

        handler_mod, mock_ecs = _import_handler(
            mock_sessions, mock_projects, mock_project_users, mock_bot_creds,
        )
        mock_ecs.run_task.return_value = {"tasks": [{"taskArn": "arn:task/abc"}]}
        try:
            event = {
                "body": json.dumps({
                    "project_id": "proj-1",
                    "name": "Test",
                    "meeting_link": "https://meet.google.com/abc-defg-hij",
                }),
                "requestContext": {
                    "authorizer": {"user_id": "admin-1", "groups": "admin"},
                },
            }
            response = handler_mod.lambda_handler(event, None)
            assert response["statusCode"] == 500
        finally:
            _cleanup()
