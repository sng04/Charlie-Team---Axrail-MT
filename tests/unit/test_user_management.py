"""Unit tests for user management Lambdas (ListUsers, GetUser, DeleteUser, UpdateUser)."""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

FUNCTIONS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions")
)

SAMPLE_USER = {
    "user_id": "user-1",
    "email": "test@example.com",
    "username": "testuser",
    "role": "user",
}


def _import_handler(function_name, mock_table, mock_cognito=None):
    func_dir = os.path.join(FUNCTIONS_DIR, function_name)
    sys.path.insert(0, func_dir)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource") as mock_boto, \
         patch("boto3.client") as mock_client_factory:
        mock_dynamo = MagicMock()
        mock_boto.return_value = mock_dynamo
        mock_dynamo.Table.return_value = mock_table
        mock_client_factory.return_value = mock_cognito or MagicMock()
        import lambda_function as mod

    return mod


def _cleanup(function_name):
    func_dir = os.path.join(FUNCTIONS_DIR, function_name)
    if func_dir in sys.path:
        sys.path.remove(func_dir)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(os.environ, {
        "DYNAMODB_TABLE": "test-Users",
        "USER_POOL_ID": "test-pool",
    }):
        yield


class TestListUsers:
    def test_list_users_success(self):
        mock_table = MagicMock()
        mock_table.scan.return_value = {"Items": [SAMPLE_USER]}
        mod = _import_handler("ListUsers", mock_table)
        try:
            response = mod.lambda_handler({}, None)
            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert len(body["data"]["users"]) == 1
        finally:
            _cleanup("ListUsers")


class TestGetUser:
    def test_get_user_success(self):
        mock_table = MagicMock()
        mock_table.get_item.return_value = {"Item": SAMPLE_USER}
        mod = _import_handler("GetUser", mock_table)
        try:
            event = {"pathParameters": {"userId": "user-1"}}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["data"]["user_id"] == "user-1"
        finally:
            _cleanup("GetUser")

    def test_get_user_not_found(self):
        mock_table = MagicMock()
        mock_table.get_item.return_value = {}
        mod = _import_handler("GetUser", mock_table)
        try:
            event = {"pathParameters": {"userId": "nonexistent"}}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 404
        finally:
            _cleanup("GetUser")


class TestDeleteUser:
    def test_delete_user_success(self):
        mock_table = MagicMock()
        mock_table.get_item.return_value = {"Item": SAMPLE_USER}
        mock_cognito = MagicMock()
        mod = _import_handler("DeleteUser", mock_table, mock_cognito)
        try:
            event = {"pathParameters": {"userId": "user-1"}}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 200
            mock_table.delete_item.assert_called_once()
            mock_cognito.admin_delete_user.assert_called_once()
        finally:
            _cleanup("DeleteUser")

    def test_delete_user_not_found(self):
        mock_table = MagicMock()
        mock_table.get_item.return_value = {}
        mod = _import_handler("DeleteUser", mock_table)
        try:
            event = {"pathParameters": {"userId": "nonexistent"}}
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 404
        finally:
            _cleanup("DeleteUser")


class TestUpdateUser:
    def test_update_user_success(self):
        mock_table = MagicMock()
        mock_table.get_item.return_value = {"Item": SAMPLE_USER.copy()}
        mod = _import_handler("UpdateUser", mock_table)
        try:
            event = {
                "pathParameters": {"userId": "user-1"},
                "body": json.dumps({"email": "new@example.com"}),
            }
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 200
            mock_table.put_item.assert_called_once()
        finally:
            _cleanup("UpdateUser")

    def test_update_user_not_found(self):
        mock_table = MagicMock()
        mock_table.get_item.return_value = {}
        mod = _import_handler("UpdateUser", mock_table)
        try:
            event = {
                "pathParameters": {"userId": "nonexistent"},
                "body": json.dumps({"email": "new@example.com"}),
            }
            response = mod.lambda_handler(event, None)
            assert response["statusCode"] == 404
        finally:
            _cleanup("UpdateUser")
