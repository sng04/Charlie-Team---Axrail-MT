"""Property-based tests for Agent & Personality CRUD API.

Tests response envelope, field validation, and referential integrity.
"""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

# Import createResponse from the shared layer (path injected by conftest.py)
from response_utils import createResponse


class TestResponseEnvelope:
    """Response envelope always has required keys and correct status boolean."""

    @given(
        status_code=st.integers(min_value=100, max_value=599),
        message=st.text(min_size=1),
    )
    @settings(max_examples=50)
    def test_envelope_structure_and_status_flag(
        self, status_code: int, message: str
    ) -> None:
        response = createResponse(status_code, message)
        assert response["statusCode"] == status_code

        body = json.loads(response["body"])
        assert {"statusCode", "status", "message"} <= set(body)
        assert body["statusCode"] == status_code
        assert body["status"] is (status_code < 400)
        assert body["message"] == message


# ---------------------------------------------------------------------------
# Missing field validation — agents
# ---------------------------------------------------------------------------

REQUIRED_AGENT_FIELDS = [
    "agent_name", "role_prompt", "task_prompt",
    "personality_id", "model_id", "use_case",
]

AGENTS_CRUD_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "AgentsCrud")
)

agent_fields_to_omit_st = st.lists(
    st.sampled_from(REQUIRED_AGENT_FIELDS),
    min_size=1,
    max_size=len(REQUIRED_AGENT_FIELDS),
    unique=True,
)


class TestAgentFieldValidation:
    """Omitting any subset of required agent fields returns 400 listing them all."""

    @given(fields_to_omit=agent_fields_to_omit_st)
    @settings(max_examples=50)
    def test_missing_fields_listed_in_error(self, fields_to_omit: list) -> None:
        body = {f: "val" for f in REQUIRED_AGENT_FIELDS if f not in fields_to_omit}
        event = {"httpMethod": "POST", "resource": "/agents", "body": json.dumps(body)}

        with patch.dict(os.environ, {
            "AGENTS_TABLE_NAME": "t-agents",
            "PERSONALITIES_TABLE_NAME": "t-personalities",
        }):
            sys.path.insert(0, AGENTS_CRUD_DIR)
            try:
                for m in list(sys.modules):
                    if m == "lambda_function":
                        del sys.modules[m]
                with patch("boto3.resource") as mock_boto:
                    mock_dynamo = MagicMock()
                    mock_boto.return_value = mock_dynamo
                    mock_dynamo.Table.return_value = MagicMock()
                    import lambda_function as agents_mod
                    response = agents_mod.lambda_handler(event, None)
            finally:
                sys.path.pop(0)
                for m in list(sys.modules):
                    if m == "lambda_function":
                        del sys.modules[m]

        assert response["statusCode"] == 400
        msg = json.loads(response["body"])["message"]
        for field in fields_to_omit:
            assert field in msg


# ---------------------------------------------------------------------------
# Missing field validation — personalities
# ---------------------------------------------------------------------------

REQUIRED_PERSONALITY_FIELDS = ["personality_name", "personality_prompt"]

PERSONALITIES_CRUD_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "PersonalitiesCrud")
)

personality_fields_to_omit_st = st.lists(
    st.sampled_from(REQUIRED_PERSONALITY_FIELDS),
    min_size=1,
    max_size=len(REQUIRED_PERSONALITY_FIELDS),
    unique=True,
)


class TestPersonalityFieldValidation:
    """Omitting any subset of required personality fields returns 400."""

    @given(fields_to_omit=personality_fields_to_omit_st)
    @settings(max_examples=50)
    def test_missing_fields_listed_in_error(self, fields_to_omit: list) -> None:
        body = {f: "val" for f in REQUIRED_PERSONALITY_FIELDS if f not in fields_to_omit}
        event = {"httpMethod": "POST", "resource": "/personalities", "body": json.dumps(body)}

        with patch.dict(os.environ, {
            "PERSONALITIES_TABLE_NAME": "t-personalities",
            "AGENTS_TABLE_NAME": "t-agents",
        }):
            sys.path.insert(0, PERSONALITIES_CRUD_DIR)
            try:
                for m in list(sys.modules):
                    if m == "lambda_function":
                        del sys.modules[m]
                with patch("boto3.resource") as mock_boto:
                    mock_dynamo = MagicMock()
                    mock_boto.return_value = mock_dynamo
                    mock_dynamo.Table.return_value = MagicMock()
                    import lambda_function as personalities_mod
                    response = personalities_mod.lambda_handler(event, None)
            finally:
                sys.path.pop(0)
                for m in list(sys.modules):
                    if m == "lambda_function":
                        del sys.modules[m]

        assert response["statusCode"] == 400
        msg = json.loads(response["body"])["message"]
        for field in fields_to_omit:
            assert field in msg


# ---------------------------------------------------------------------------
# Referential integrity on personality delete
# ---------------------------------------------------------------------------


class TestReferentialIntegrity:
    """Deleting a personality referenced by agents returns 409."""

    @given(
        personality_id=st.uuids().map(str),
        num_agents=st.integers(min_value=1, max_value=5),
    )
    @settings(max_examples=50)
    def test_delete_returns_409_when_agents_reference(
        self, personality_id: str, num_agents: int
    ) -> None:
        agent_records = [
            {"agent_id": f"agent-{i}", "personality_id": personality_id}
            for i in range(num_agents)
        ]
        event = {
            "httpMethod": "DELETE",
            "resource": "/personalities/{personalityId}",
            "pathParameters": {"personalityId": personality_id},
        }

        mock_personalities = MagicMock()
        mock_agents = MagicMock()
        mock_personalities.get_item.return_value = {
            "Item": {"personality_id": personality_id, "personality_name": "T", "personality_prompt": "T"}
        }
        mock_agents.scan.return_value = {"Items": agent_records}

        with patch.dict(os.environ, {
            "PERSONALITIES_TABLE_NAME": "t-personalities",
            "AGENTS_TABLE_NAME": "t-agents",
        }):
            sys.path.insert(0, PERSONALITIES_CRUD_DIR)
            try:
                for m in list(sys.modules):
                    if m == "lambda_function":
                        del sys.modules[m]
                with patch("boto3.resource") as mock_boto:
                    mock_dynamo = MagicMock()
                    mock_boto.return_value = mock_dynamo

                    def table_side_effect(name):
                        if "personalities" in name.lower():
                            return mock_personalities
                        return mock_agents

                    mock_dynamo.Table.side_effect = table_side_effect
                    import lambda_function as personalities_mod
                    response = personalities_mod.lambda_handler(event, None)
            finally:
                sys.path.pop(0)
                for m in list(sys.modules):
                    if m == "lambda_function":
                        del sys.modules[m]

        assert response["statusCode"] == 409
        assert "referenced by existing agents" in json.loads(response["body"])["message"]
