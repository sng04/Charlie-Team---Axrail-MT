"""Unit tests for GetSuggestedQuestions Lambda handler."""

import json
from unittest.mock import MagicMock, patch

import pytest


def _parse_body(response):
    return json.loads(response["body"])


class TestGetSuggestedQuestions:
    """GetSuggestedQuestions: success, empty, and validation."""

    @patch("lambdas.Functions.GetSuggestedQuestions.lambda_function.table")
    def test_success(self, mock_table):
        from lambdas.Functions.GetSuggestedQuestions.lambda_function import lambda_handler

        mock_table.query.return_value = {
            "Items": [
                {
                    "question_id": "q1",
                    "session_id": "s1",
                    "question_text": "What was decided?",
                    "matched": False,
                    "created_at": "2024-01-01T00:00:00Z",
                },
            ]
        }

        event = {"pathParameters": {"sessionId": "s1"}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        assert body["data"]["count"] == 1
        assert body["data"]["questions"][0]["question_text"] == "What was decided?"

    @patch("lambdas.Functions.GetSuggestedQuestions.lambda_function.table")
    def test_empty(self, mock_table):
        from lambdas.Functions.GetSuggestedQuestions.lambda_function import lambda_handler

        mock_table.query.return_value = {"Items": []}

        event = {"pathParameters": {"sessionId": "s1"}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        assert body["data"]["count"] == 0
        assert body["data"]["questions"] == []

    def test_missing_session_id(self):
        from lambdas.Functions.GetSuggestedQuestions.lambda_function import lambda_handler

        event = {"pathParameters": {}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 400
        assert body["status"] is False
