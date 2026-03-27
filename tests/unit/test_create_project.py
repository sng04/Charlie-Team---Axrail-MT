"""Unit tests for CreateProject Lambda handler."""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

CREATE_PROJECT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "CreateProject")
)


def _import_handler(mock_table):
    sys.path.insert(0, CREATE_PROJECT_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource") as mock_boto:
        mock_dynamo = MagicMock()
        mock_boto.return_value = mock_dynamo
        mock_dynamo.Table.return_value = mock_table
        import lambda_function as mod

    return mod


def _cleanup():
    if CREATE_PROJECT_DIR in sys.path:
        sys.path.remove(CREATE_PROJECT_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(os.environ, {"PROJECTS_TABLE": "test-projects"}):
        yield
    _cleanup()


class TestCreateProject:
    def test_create_project_success(self):
        mock_table = MagicMock()
        mock_table.query.return_value = {"Items": []}
        handler_mod = _import_handler(mock_table)
        try:
            event = {
                "body": json.dumps({"name": "Test Project", "email": "test@example.com"}),
            }
            response = handler_mod.lambda_handler(event, None)
            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            assert "project_id" in body["data"]
            mock_table.put_item.assert_called_once()
        finally:
            _cleanup()

    def test_create_project_missing_fields_returns_400(self):
        mock_table = MagicMock()
        handler_mod = _import_handler(mock_table)
        try:
            event = {"body": json.dumps({"name": "No Email"})}
            response = handler_mod.lambda_handler(event, None)
            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert body["status"] is False
            assert "email" in body["message"]
        finally:
            _cleanup()

    def test_create_project_unexpected_error_returns_500(self):
        mock_table = MagicMock()
        mock_table.query.return_value = {"Items": []}
        mock_table.put_item.side_effect = Exception("DynamoDB error")
        handler_mod = _import_handler(mock_table)
        try:
            event = {
                "body": json.dumps({"name": "Test", "email": "test@example.com"}),
            }
            response = handler_mod.lambda_handler(event, None)
            assert response["statusCode"] == 500
            body = json.loads(response["body"])
            assert body["status"] is False
        finally:
            _cleanup()
