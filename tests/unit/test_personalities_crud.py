"""Unit tests for Personalities CRUD Lambda handler.

Per testing-standards: 3-4 tests per CRUD handler covering
success, validation, not-found, and error paths.
"""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

PERSONALITIES_CRUD_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "PersonalitiesCrud")
)

SAMPLE_PERSONALITY = {
    "personality_id": "pppppppp-1111-2222-3333-444444444444",
    "personality_name": "Friendly Bot",
    "personality_prompt": "You are a friendly assistant",
}

VALID_CREATE_BODY = {
    "personality_name": "Professional Bot",
    "personality_prompt": "You are a professional assistant",
}


def _import_handler(mock_personalities_table, mock_agents_table):
    """Import the personalities handler with mocked DynamoDB tables."""
    sys.path.insert(0, PERSONALITIES_CRUD_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource") as mock_boto:
        mock_dynamo = MagicMock()
        mock_boto.return_value = mock_dynamo

        def table_side_effect(name):
            if "personalities" in name.lower():
                return mock_personalities_table
            return mock_agents_table

        mock_dynamo.Table.side_effect = table_side_effect
        import lambda_function as personalities_mod

    return personalities_mod


def _cleanup():
    if PERSONALITIES_CRUD_DIR in sys.path:
        sys.path.remove(PERSONALITIES_CRUD_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(
        os.environ,
        {
            "PERSONALITIES_TABLE_NAME": "test-personalities",
            "AGENTS_TABLE_NAME": "test-agents",
        },
    ):
        yield
    _cleanup()


class TestPersonalitiesHandler:
    """Personalities CRUD handler: success, validation, not-found, conflict."""

    def test_create_personality_success(self):
        mock_personalities = MagicMock()
        mock_agents = MagicMock()

        handler_mod = _import_handler(mock_personalities, mock_agents)
        try:
            event = {
                "httpMethod": "POST",
                "resource": "/personalities",
                "body": json.dumps(VALID_CREATE_BODY),
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            assert "personality_id" in body["data"]
            assert len(body["data"]["personality_id"]) == 36
            mock_personalities.put_item.assert_called_once()
        finally:
            _cleanup()

    def test_create_personality_missing_fields_returns_400(self):
        mock_personalities = MagicMock()
        mock_agents = MagicMock()

        handler_mod = _import_handler(mock_personalities, mock_agents)
        try:
            event = {
                "httpMethod": "POST",
                "resource": "/personalities",
                "body": json.dumps({"personality_name": "Incomplete"}),
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert body["status"] is False
            assert "personality_prompt" in body["message"]
        finally:
            _cleanup()

    def test_get_personality_not_found_returns_404(self):
        mock_personalities = MagicMock()
        mock_agents = MagicMock()
        mock_personalities.get_item.return_value = {}

        handler_mod = _import_handler(mock_personalities, mock_agents)
        try:
            event = {
                "httpMethod": "GET",
                "resource": "/personalities/{personalityId}",
                "pathParameters": {"personalityId": "nonexistent-id"},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 404
            body = json.loads(response["body"])
            assert body["status"] is False
            assert body["message"] == "Personality not found"
        finally:
            _cleanup()

    def test_delete_personality_conflict_returns_409(self):
        mock_personalities = MagicMock()
        mock_agents = MagicMock()
        mock_personalities.get_item.return_value = {"Item": SAMPLE_PERSONALITY}
        mock_agents.scan.return_value = {
            "Items": [{"agent_id": "aaaa-1111", "personality_id": SAMPLE_PERSONALITY["personality_id"]}]
        }

        handler_mod = _import_handler(mock_personalities, mock_agents)
        try:
            event = {
                "httpMethod": "DELETE",
                "resource": "/personalities/{personalityId}",
                "pathParameters": {"personalityId": SAMPLE_PERSONALITY["personality_id"]},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 409
            body = json.loads(response["body"])
            assert body["status"] is False
            assert "referenced by existing agents" in body["message"]
            mock_personalities.delete_item.assert_not_called()
        finally:
            _cleanup()
