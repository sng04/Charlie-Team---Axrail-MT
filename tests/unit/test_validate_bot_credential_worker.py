"""Unit tests for ValidateBotCredentialWorker Lambda handler."""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

WORKER_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "ValidateBotCredentialWorker")
)


def _import_handler(mock_table):
    sys.path.insert(0, WORKER_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource") as mock_boto, \
         patch("boto3.client") as mock_client_factory:
        mock_dynamo = MagicMock()
        mock_boto.return_value = mock_dynamo
        mock_dynamo.Table.return_value = mock_table

        mock_secrets = MagicMock()
        mock_client_factory.return_value = mock_secrets

        import lambda_function as mod

    return mod, mock_secrets


def _cleanup():
    if WORKER_DIR in sys.path:
        sys.path.remove(WORKER_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(os.environ, {
        "BOT_CREDENTIALS_TABLE": "test-BotCredentials",
        "ENVIRONMENT": "test",
    }):
        yield
    _cleanup()


class TestValidateBotCredentialWorker:
    def test_successful_smtp_validation(self):
        """Verified credential updates status to 'verified' and available_status to 'active'."""
        mock_table = MagicMock()
        mod, mock_secrets = _import_handler(mock_table)
        try:
            mock_secrets.get_secret_value.return_value = {
                "SecretString": json.dumps({"password": "app-pass"})
            }
            with patch.object(mod, "_validate_smtp", return_value=(True, "")):
                event = {
                    "detail": {
                        "credential_id": "cred-1",
                        "email": "bot@gmail.com",
                    }
                }
                response = mod.lambda_handler(event, None)
                assert response["statusCode"] == 200
                mock_table.update_item.assert_called_once()
                call_kwargs = mock_table.update_item.call_args[1]
                assert call_kwargs["ExpressionAttributeValues"][":status"] == "verified"
                assert call_kwargs["ExpressionAttributeValues"][":available"] == "active"
        finally:
            _cleanup()

    def test_failed_smtp_auth(self):
        """Failed SMTP auth sets status to 'verification_failed' with error message."""
        mock_table = MagicMock()
        mod, mock_secrets = _import_handler(mock_table)
        try:
            mock_secrets.get_secret_value.return_value = {
                "SecretString": json.dumps({"password": "bad-pass"})
            }
            error_msg = "Invalid email or password."
            with patch.object(mod, "_validate_smtp", return_value=(False, error_msg)):
                event = {
                    "detail": {
                        "credential_id": "cred-1",
                        "email": "bot@gmail.com",
                    }
                }
                response = mod.lambda_handler(event, None)
                assert response["statusCode"] == 200
                call_kwargs = mock_table.update_item.call_args[1]
                assert call_kwargs["ExpressionAttributeValues"][":status"] == "verification_failed"
                assert call_kwargs["ExpressionAttributeValues"][":error"] == error_msg
        finally:
            _cleanup()

    def test_unsupported_email_domain(self):
        """Unsupported domain returns failure with domain error message."""
        mock_table = MagicMock()
        mod, mock_secrets = _import_handler(mock_table)
        try:
            mock_secrets.get_secret_value.return_value = {
                "SecretString": json.dumps({"password": "pass"})
            }
            with patch.object(mod, "_validate_smtp", return_value=(False, "Unsupported email domain: custom.local")):
                event = {
                    "detail": {
                        "credential_id": "cred-1",
                        "email": "bot@custom.local",
                    }
                }
                response = mod.lambda_handler(event, None)
                assert response["statusCode"] == 200
                call_kwargs = mock_table.update_item.call_args[1]
                assert call_kwargs["ExpressionAttributeValues"][":status"] == "verification_failed"
        finally:
            _cleanup()

    def test_missing_event_fields(self):
        """Missing credential_id or email returns 400."""
        mock_table = MagicMock()
        mod, _ = _import_handler(mock_table)
        try:
            event = {"detail": {}}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 400
        finally:
            _cleanup()

    def test_get_smtp_server_known_domains(self):
        """Known domains (gmail, outlook, yahoo) return correct SMTP configs."""
        mock_table = MagicMock()
        mod, _ = _import_handler(mock_table)
        try:
            gmail = mod._get_smtp_server("user@gmail.com")
            assert gmail["host"] == "smtp.gmail.com"

            outlook = mod._get_smtp_server("user@outlook.com")
            assert outlook["host"] == "smtp.office365.com"

            yahoo = mod._get_smtp_server("user@yahoo.com")
            assert yahoo["host"] == "smtp.mail.yahoo.com"
        finally:
            _cleanup()
