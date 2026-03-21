"""Unit tests for Skills CRUD Lambda handler.

Per testing-standards: 3-4 tests per CRUD handler covering
success, validation, not-found, and error paths.
"""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

SKILLS_CRUD_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "SkillsCrud")
)

SAMPLE_SKILL = {
    "skill_id": "ssssssss-1111-2222-3333-444444444444",
    "agent_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "skill_name": "Test Skill",
    "description": "A test skill",
    "s3_key": "agent-id/skill-id/test.md",
    "file_type": "md",
    "status": "active",
}

VALID_CREATE_BODY = {
    "agent_id": "aaaaaaaa-1111-2222-3333-444444444444",
    "skill_name": "New Skill",
    "file_name": "guide.md",
    "description": "A new skill document",
}


def _import_handler(mock_skills_table, mock_agents_table, mock_s3_client=None):
    """Import the skills handler with mocked DynamoDB tables and S3."""
    sys.path.insert(0, SKILLS_CRUD_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource") as mock_boto, \
         patch("boto3.client") as mock_client_factory:
        mock_dynamo = MagicMock()
        mock_boto.return_value = mock_dynamo

        def table_side_effect(name):
            if "skills" in name.lower():
                return mock_skills_table
            return mock_agents_table

        mock_dynamo.Table.side_effect = table_side_effect

        s3 = mock_s3_client or MagicMock()
        s3.generate_presigned_url.return_value = "https://s3.example.com/presigned"
        mock_client_factory.return_value = s3

        import lambda_function as skills_mod

    return skills_mod


def _cleanup():
    if SKILLS_CRUD_DIR in sys.path:
        sys.path.remove(SKILLS_CRUD_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(os.environ, {
        "SKILLS_TABLE_NAME": "test-skills",
        "AGENTS_TABLE_NAME": "test-agents",
        "SKILLS_BUCKET_NAME": "test-skills-bucket",
    }):
        yield
    _cleanup()


class TestSkillsHandler:
    """Skills CRUD handler: success, validation, not-found, error."""

    def test_create_skill_success(self):
        """POST /skills with valid payload returns 200 with upload_url."""
        mock_skills = MagicMock()
        mock_agents = MagicMock()
        mock_agents.get_item.return_value = {
            "Item": {"agent_id": VALID_CREATE_BODY["agent_id"]}
        }

        handler_mod = _import_handler(mock_skills, mock_agents)
        try:
            event = {
                "httpMethod": "POST",
                "resource": "/skills",
                "body": json.dumps(VALID_CREATE_BODY),
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            assert "upload_url" in body["data"]
            mock_skills.put_item.assert_called_once()
        finally:
            _cleanup()

    def test_create_skill_missing_fields_returns_400(self):
        """POST /skills with missing fields returns 400."""
        mock_skills = MagicMock()
        mock_agents = MagicMock()

        handler_mod = _import_handler(mock_skills, mock_agents)
        try:
            event = {
                "httpMethod": "POST",
                "resource": "/skills",
                "body": json.dumps({"skill_name": "Incomplete"}),
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert body["status"] is False
            assert "agent_id" in body["message"]
            assert "file_name" in body["message"]
        finally:
            _cleanup()

    def test_get_skill_not_found_returns_404(self):
        """GET /skills/{skillId} returns 404 for non-existent skill."""
        mock_skills = MagicMock()
        mock_agents = MagicMock()
        mock_skills.get_item.return_value = {}

        handler_mod = _import_handler(mock_skills, mock_agents)
        try:
            event = {
                "httpMethod": "GET",
                "resource": "/skills/{skillId}",
                "pathParameters": {"skillId": "nonexistent-id"},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 404
            body = json.loads(response["body"])
            assert body["status"] is False
            assert body["message"] == "Skill not found"
        finally:
            _cleanup()

    def test_list_skills_missing_agent_id_returns_400(self):
        """GET /skills without agent_id query param returns 400."""
        mock_skills = MagicMock()
        mock_agents = MagicMock()

        handler_mod = _import_handler(mock_skills, mock_agents)
        try:
            event = {
                "httpMethod": "GET",
                "resource": "/skills",
                "queryStringParameters": {},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 400
            body = json.loads(response["body"])
            assert body["status"] is False
            assert "agent_id" in body["message"]
        finally:
            _cleanup()
