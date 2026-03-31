"""Unit tests for CreateBotCredential Lambda handler."""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

CREATE_BOT_CRED_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "CreateBotCredential")
)


def _import_handler(mock_table):
    sys.path.insert(0, CREATE_BOT_CRED_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource") as mock_boto, \
         patch("boto3.client") as mock_client_factory:
        mock_dynamo = MagicMock()
        mock_boto.return_value = mock_dynamo
        mock_dynamo.Table.return_value = mock_table

        mock_secrets = MagicMock()
        mock_events = MagicMock()

        def client_side_effect(svc, **kw):
            if svc == "secretsmanager":
                return mock_secrets
            return mock_events

        mock_client_factory.side_effect = client_side_effect
        import lambda_function as mod

    return mod, mock_secrets, mock_events


def _cleanup():
    if CREATE_BOT_CRED_DIR in sys.path:
        sys.path.remove(CREATE_BOT_CRED_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(os.environ, {
        "BOT_CREDENTIALS_TABLE": "test-BotCredentials",
        "ENVIRONMENT": "test",
        "EVENT_BUS_NAME": "test-event-bus",
    }):
        yield
    _cleanup()


class TestCreateBotCredential:
    def test_create_success(self):
        """Successful creation sets status to verified (SMTP verification removed)."""
        mock_table = MagicMock()
        mock_table.query.return_value = {"Items": []}

        mod, mock_secrets, mock_events = _import_handler(mock_table)
        try:
            event = {
                "body": json.dumps({
                    "email": "bot@gmail.com",
                    "password": "app-password-123",
                }),
            }
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            assert body["data"]["verification_status"] == "verified"
            assert body["data"]["warm_pool_size"] == 1
            mock_table.put_item.assert_called_once()
            mock_secrets.create_secret.assert_called_once()
        finally:
            _cleanup()

    def test_invalid_email_returns_400(self):
        mock_table = MagicMock()
        mod, _, _ = _import_handler(mock_table)
        try:
            event = {"body": json.dumps({"email": "not-an-email", "password": "pass"})}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert "email" in body["message"].lower()
        finally:
            _cleanup()

    def test_duplicate_email_returns_409(self):
        mock_table = MagicMock()
        mock_table.query.return_value = {"Items": [{"credential_id": "existing"}]}

        mod, _, _ = _import_handler(mock_table)
        try:
            event = {"body": json.dumps({"email": "bot@gmail.com", "password": "pass"})}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 409
        finally:
            _cleanup()

    def test_empty_password_returns_400(self):
        mock_table = MagicMock()
        mod, _, _ = _import_handler(mock_table)
        try:
            event = {"body": json.dumps({"email": "bot@gmail.com", "password": "  "})}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert "password" in body["message"].lower()
        finally:
            _cleanup()

    def test_invalid_warm_pool_size_returns_400(self):
        mock_table = MagicMock()
        mod, _, _ = _import_handler(mock_table)
        try:
            event = {"body": json.dumps({"email": "bot@gmail.com", "password": "pass", "warm_pool_size": -1})}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert "warm_pool_size" in body["message"]
        finally:
            _cleanup()

    def test_missing_required_fields_returns_400(self):
        mock_table = MagicMock()
        mod, _, _ = _import_handler(mock_table)
        try:
            event = {"body": json.dumps({})}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert "missing" in body["message"].lower()
        finally:
            _cleanup()
