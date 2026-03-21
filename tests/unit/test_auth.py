"""Unit tests for AdminLogin Lambda handler."""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

ADMIN_LOGIN_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "AdminLogin")
)


def _import_handler():
    sys.path.insert(0, ADMIN_LOGIN_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    import lambda_function as mod
    return mod


def _cleanup():
    if ADMIN_LOGIN_DIR in sys.path:
        sys.path.remove(ADMIN_LOGIN_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(os.environ, {
        "USER_POOL_ID": "test-pool",
        "CLIENT_ID": "test-client",
    }):
        yield
    _cleanup()


class TestAdminLogin:
    def test_login_success(self):
        handler_mod = _import_handler()
        try:
            with patch("auth_utils.cognito_client") as mock_cognito:
                mock_cognito.initiate_auth.return_value = {
                    "AuthenticationResult": {
                        "AccessToken": "access-token-123",
                        "IdToken": "id-token-123",
                        "RefreshToken": "refresh-token-123",
                        "TokenType": "Bearer",
                        "ExpiresIn": 3600,
                    }
                }
                event = {
                    "body": json.dumps({"username": "admin", "password": "secret123"}),
                }
                response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            assert "access_token" in body["data"]
        finally:
            _cleanup()

    def test_login_invalid_credentials_returns_401(self):
        from custom_exceptions import UnauthorizedError

        handler_mod = _import_handler()
        try:
            with patch.object(
                handler_mod, "admin_login",
                side_effect=UnauthorizedError("Invalid username or password"),
            ):
                event = {
                    "body": json.dumps({"username": "admin", "password": "wrong"}),
                }
                response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 401
            body = json.loads(response["body"])
            assert body["status"] is False
        finally:
            _cleanup()

    def test_login_missing_fields_returns_400(self):
        handler_mod = _import_handler()
        try:
            event = {"body": json.dumps({"username": "admin"})}
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert body["status"] is False
            assert "password" in body["message"]
        finally:
            _cleanup()
