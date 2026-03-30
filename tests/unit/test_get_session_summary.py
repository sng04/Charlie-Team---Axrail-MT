"""Unit tests for GetSessionSummary Lambda handler."""

import json
from unittest.mock import MagicMock, patch

import pytest


def _parse_body(response):
    return json.loads(response["body"])


class TestGetSessionSummary:
    """GetSessionSummary: success, not-found, and validation."""

    @patch("lambdas.Functions.GetSessionSummary.lambda_function.s3_client")
    @patch("lambdas.Functions.GetSessionSummary.lambda_function.sessions_table")
    def test_success(self, mock_table, mock_s3):
        from lambdas.Functions.GetSessionSummary.lambda_function import lambda_handler

        mock_table.get_item.return_value = {
            "Item": {"session_id": "s1", "project_id": "p1"}
        }
        mock_body = MagicMock()
        mock_body.read.return_value = b"# Meeting Summary\nKey decisions made."
        mock_s3.get_object.return_value = {"Body": mock_body}

        event = {"pathParameters": {"sessionId": "s1"}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        assert body["data"]["summary_markdown"] == "# Meeting Summary\nKey decisions made."
        assert body["data"]["status"] == "available"

    @patch("lambdas.Functions.GetSessionSummary.lambda_function.s3_client")
    @patch("lambdas.Functions.GetSessionSummary.lambda_function.sessions_table")
    def test_not_found(self, mock_table, mock_s3):
        from lambdas.Functions.GetSessionSummary.lambda_function import lambda_handler

        mock_table.get_item.return_value = {}

        event = {"pathParameters": {"sessionId": "s-missing"}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 404
        assert body["status"] is False

    def test_missing_session_id(self):
        from lambdas.Functions.GetSessionSummary.lambda_function import lambda_handler

        event = {"pathParameters": {}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 400
        assert body["status"] is False
