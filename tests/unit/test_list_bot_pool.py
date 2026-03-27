"""Unit tests for ListBotPool Lambda handler."""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

LIST_BOT_POOL_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "ListBotPool")
)


def _import_handler(mock_creds_table, mock_pool_table, mock_sessions_table=None):
    sys.path.insert(0, LIST_BOT_POOL_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource") as mock_boto:
        mock_dynamo = MagicMock()
        mock_boto.return_value = mock_dynamo

        table_map = {
            "test-BotCredentials": mock_creds_table,
            "test-BotPool": mock_pool_table,
            "test-Sessions": mock_sessions_table or MagicMock(),
        }
        mock_dynamo.Table.side_effect = lambda name: table_map.get(name, MagicMock())
        import lambda_function as mod

    return mod


def _cleanup():
    if LIST_BOT_POOL_DIR in sys.path:
        sys.path.remove(LIST_BOT_POOL_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(os.environ, {
        "BOT_CREDENTIALS_TABLE": "test-BotCredentials",
        "BOT_POOL_TABLE": "test-BotPool",
        "SESSIONS_TABLE": "test-Sessions",
    }):
        yield
    _cleanup()


class TestListBotPool:
    def test_list_with_containers(self):
        """Returns containers with summary counts."""
        mock_creds = MagicMock()
        mock_creds.get_item.return_value = {"Item": {"credential_id": "cred-1"}}
        mock_pool = MagicMock()
        mock_pool.query.return_value = {
            "Items": [
                {"container_id": "c1", "status": "idle", "credential_id": "cred-1", "registered_at": "2025-01-01"},
                {"container_id": "c2", "status": "busy", "credential_id": "cred-1", "registered_at": "2025-01-02"},
            ]
        }

        mod = _import_handler(mock_creds, mock_pool)
        try:
            event = {"pathParameters": {"credentialId": "cred-1"}, "queryStringParameters": None}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["data"]["summary"]["total"] == 2
            assert body["data"]["summary"]["idle"] == 1
            assert body["data"]["summary"]["busy"] == 1
            assert len(body["data"]["containers"]) == 2
        finally:
            _cleanup()

    def test_credential_not_found_returns_404(self):
        mock_creds = MagicMock()
        mock_creds.get_item.return_value = {}
        mock_pool = MagicMock()

        mod = _import_handler(mock_creds, mock_pool)
        try:
            event = {"pathParameters": {"credentialId": "nonexistent"}, "queryStringParameters": None}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 404
        finally:
            _cleanup()

    def test_status_filter(self):
        """Passing status query param filters containers."""
        mock_creds = MagicMock()
        mock_creds.get_item.return_value = {"Item": {"credential_id": "cred-1"}}
        mock_pool = MagicMock()
        mock_pool.query.return_value = {
            "Items": [{"container_id": "c1", "status": "idle", "credential_id": "cred-1", "registered_at": "2025-01-01"}]
        }

        mod = _import_handler(mock_creds, mock_pool)
        try:
            event = {"pathParameters": {"credentialId": "cred-1"}, "queryStringParameters": {"status": "idle"}}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["data"]["summary"]["total"] == 1
        finally:
            _cleanup()

    def test_empty_pool(self):
        mock_creds = MagicMock()
        mock_creds.get_item.return_value = {"Item": {"credential_id": "cred-1"}}
        mock_pool = MagicMock()
        mock_pool.query.return_value = {"Items": []}

        mod = _import_handler(mock_creds, mock_pool)
        try:
            event = {"pathParameters": {"credentialId": "cred-1"}, "queryStringParameters": None}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["data"]["summary"]["total"] == 0
            assert body["data"]["containers"] == []
        finally:
            _cleanup()

    def test_summary_counts(self):
        """Summary correctly counts each status category."""
        mock_creds = MagicMock()
        mock_creds.get_item.return_value = {"Item": {"credential_id": "cred-1"}}
        mock_pool = MagicMock()
        mock_pool.query.return_value = {
            "Items": [
                {"container_id": "c1", "status": "idle", "registered_at": "2025-01-01"},
                {"container_id": "c2", "status": "idle", "registered_at": "2025-01-02"},
                {"container_id": "c3", "status": "busy", "registered_at": "2025-01-03"},
                {"container_id": "c4", "status": "starting", "registered_at": "2025-01-04"},
                {"container_id": "c5", "status": "error", "registered_at": "2025-01-05"},
            ]
        }

        mod = _import_handler(mock_creds, mock_pool)
        try:
            event = {"pathParameters": {"credentialId": "cred-1"}, "queryStringParameters": None}
            response = mod.lambda_handler(event, None)
            body = json.loads(response["body"])
            summary = body["data"]["summary"]
            assert summary["idle"] == 2
            assert summary["busy"] == 1
            assert summary["starting"] == 1
            assert summary["error"] == 1
            assert summary["total"] == 5
        finally:
            _cleanup()
