"""Unit tests for AdminChangelog retrieval Lambda."""

import json
from unittest.mock import MagicMock, patch


def _parse_body(response):
    return json.loads(response["body"])


class TestAdminChangelog:

    @patch("lambdas.Functions.AdminChangelog.lambda_function.table")
    def test_list_by_entity_type(self, mock_table):
        from lambdas.Functions.AdminChangelog.lambda_function import lambda_handler

        mock_table.query.return_value = {
            "Items": [{"changelog_id": "c1", "entity_type": "project", "action": "create"}]
        }

        event = {"queryStringParameters": {"entity_type": "project"}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        assert body["data"]["count"] == 1

    @patch("lambdas.Functions.AdminChangelog.lambda_function.table")
    def test_empty_results(self, mock_table):
        from lambdas.Functions.AdminChangelog.lambda_function import lambda_handler

        mock_table.scan.return_value = {"Items": []}

        event = {"queryStringParameters": None}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        assert body["data"]["count"] == 0
        assert body["data"]["entries"] == []

    @patch("lambdas.Functions.AdminChangelog.lambda_function.table")
    def test_scan_without_filters(self, mock_table):
        from lambdas.Functions.AdminChangelog.lambda_function import lambda_handler

        mock_table.scan.return_value = {
            "Items": [
                {"changelog_id": "c1", "entity_type": "user", "action": "create"},
                {"changelog_id": "c2", "entity_type": "login_attempt", "action": "login_success"},
            ]
        }

        event = {"queryStringParameters": {}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        assert body["data"]["count"] == 2
