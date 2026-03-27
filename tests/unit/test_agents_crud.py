"""Unit tests for Agents CRUD Lambda handler.

Per testing-standards: 3-4 tests per CRUD handler covering
success, validation, not-found, and error paths.
"""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

# Path to the AgentsCrud Lambda directory
AGENTS_CRUD_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "AgentsCrud")
)

SAMPLE_AGENT = {
    "agent_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "agent_name": "Test Agent",
    "role_prompt": "You are a helpful assistant",
    "behavior_guidelines": "Answer questions",
    "personality_id": "pppppppp-1111-2222-3333-444444444444",
    "model_id": "anthropic.claude-v2",
    "use_case": "customer_support",
}

VALID_CREATE_BODY = {
    "agent_name": "New Agent",
    "role_prompt": "You are a sales bot",
    "behavior_guidelines": "Sell products",
    "personality_id": "pppppppp-1111-2222-3333-444444444444",
    "model_id": "anthropic.claude-v2",
    "use_case": "sales",
}


def _import_handler(mock_agents_table, mock_personalities_table, mock_agent_skills_table=None):
    """Import the agents handler with mocked DynamoDB tables."""
    sys.path.insert(0, AGENTS_CRUD_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource") as mock_boto:
        mock_dynamo = MagicMock()
        mock_boto.return_value = mock_dynamo

        def table_side_effect(name):
            if "agent-skills" in name.lower() or "agentskills" in name.lower():
                return mock_agent_skills_table or MagicMock()
            if "agents" in name.lower():
                return mock_agents_table
            return mock_personalities_table

        mock_dynamo.Table.side_effect = table_side_effect
        import lambda_function as agents_mod

    return agents_mod


def _cleanup():
    """Remove handler modules from sys.modules and sys.path."""
    if AGENTS_CRUD_DIR in sys.path:
        sys.path.remove(AGENTS_CRUD_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    """Set required environment variables for every test."""
    with patch.dict(
        os.environ,
        {
            "AGENTS_TABLE_NAME": "test-agents",
            "PERSONALITIES_TABLE_NAME": "test-personalities",
            "AGENT_SKILLS_TABLE_NAME": "test-agent-skills",
        },
    ):
        yield
    _cleanup()


class TestAgentsHandler:
    """Agents CRUD handler: success, validation, not-found, error."""

    def test_create_agent_success(self):
        """POST /agents with valid payload returns 200 with generated agent_id."""
        mock_agents = MagicMock()
        mock_personalities = MagicMock()
        mock_agents.query.return_value = {"Items": []}
        mock_personalities.get_item.return_value = {
            "Item": {
                "personality_id": VALID_CREATE_BODY["personality_id"],
                "personality_name": "Friendly",
                "personality_prompt": "Be friendly",
            }
        }

        handler_mod = _import_handler(mock_agents, mock_personalities)
        try:
            event = {
                "httpMethod": "POST",
                "resource": "/agents",
                "body": json.dumps(VALID_CREATE_BODY),
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            assert "agent_id" in body["data"]
            assert len(body["data"]["agent_id"]) == 36
            mock_agents.put_item.assert_called_once()
        finally:
            _cleanup()

    def test_create_agent_missing_fields_returns_400(self):
        """POST /agents with missing fields returns 400 listing missing fields."""
        mock_agents = MagicMock()
        mock_personalities = MagicMock()

        handler_mod = _import_handler(mock_agents, mock_personalities)
        try:
            event = {
                "httpMethod": "POST",
                "resource": "/agents",
                "body": json.dumps({"agent_name": "Incomplete Agent"}),
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert body["status"] is False
            for field in ["role_prompt", "behavior_guidelines", "personality_id", "model_id", "use_case"]:
                assert field in body["message"]
        finally:
            _cleanup()

    def test_get_agent_not_found_returns_404(self):
        """GET /agents/{agentId} returns 404 for non-existent agent."""
        mock_agents = MagicMock()
        mock_personalities = MagicMock()
        mock_agents.get_item.return_value = {}

        handler_mod = _import_handler(mock_agents, mock_personalities)
        try:
            event = {
                "httpMethod": "GET",
                "resource": "/agents/{agentId}",
                "pathParameters": {"agentId": "nonexistent-id"},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 404
            body = json.loads(response["body"])
            assert body["status"] is False
            assert body["message"] == "Agent not found"
        finally:
            _cleanup()

    def test_delete_agent_success(self):
        """DELETE /agents/{agentId} returns 200 for existing agent."""
        mock_agents = MagicMock()
        mock_personalities = MagicMock()
        mock_agents.get_item.return_value = {"Item": SAMPLE_AGENT}

        handler_mod = _import_handler(mock_agents, mock_personalities)
        try:
            event = {
                "httpMethod": "DELETE",
                "resource": "/agents/{agentId}",
                "pathParameters": {"agentId": SAMPLE_AGENT["agent_id"]},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            mock_agents.delete_item.assert_called_once()
        finally:
            _cleanup()
