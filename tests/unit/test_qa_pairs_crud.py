"""Unit tests for QA Pairs CRUD Lambda handler.

Per testing-standards: 3-4 tests per CRUD handler covering
success, validation, not-found, and error paths.
"""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

QA_PAIRS_CRUD_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "QAPairsCrud")
)

SAMPLE_QA_PAIR = {
    "qa_pair_id": "qqqqqqqq-1111-2222-3333-444444444444",
    "session_id": "ssssssss-1111-2222-3333-444444444444",
    "project_id": "pppppppp-1111-2222-3333-444444444444",
    "question": "What is the pricing?",
    "answer": "Enterprise tier starts at 2.1%",
    "gsi_pk": "ALL",
    "detected_at": "2026-03-31T10:35:41+00:00",
}


def _import_handler(mock_qa_table):
    """Import the QA pairs handler with mocked DynamoDB table."""
    sys.path.insert(0, QA_PAIRS_CRUD_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource") as mock_boto:
        mock_dynamo = MagicMock()
        mock_boto.return_value = mock_dynamo
        mock_dynamo.Table.return_value = mock_qa_table
        import lambda_function as qa_mod

    return qa_mod


def _cleanup():
    if QA_PAIRS_CRUD_DIR in sys.path:
        sys.path.remove(QA_PAIRS_CRUD_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(os.environ, {"QA_PAIRS_TABLE_NAME": "test-qa-pairs"}):
        yield
    _cleanup()


class TestQAPairsHandler:
    """QA Pairs CRUD handler: success, validation, not-found."""

    def test_list_qa_pairs_by_session_success(self):
        """GET /qa-pairs?session_id=... returns 200 with items."""
        mock_table = MagicMock()
        mock_table.query.return_value = {"Items": [SAMPLE_QA_PAIR]}

        handler_mod = _import_handler(mock_table)
        try:
            event = {
                "httpMethod": "GET",
                "resource": "/qa-pairs",
                "queryStringParameters": {"session_id": "sess-1"},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            assert len(body["data"]["items"]) == 1
            assert body["data"]["lastKey"] is None
        finally:
            _cleanup()

    def test_list_all_qa_pairs_no_filters(self):
        """GET /qa-pairs without filters returns 200 via created-at-index."""
        mock_table = MagicMock()
        mock_table.query.return_value = {"Items": [SAMPLE_QA_PAIR]}

        handler_mod = _import_handler(mock_table)
        try:
            event = {
                "httpMethod": "GET",
                "resource": "/qa-pairs",
                "queryStringParameters": {},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            assert len(body["data"]["items"]) == 1

            # Verify the GSI query was used
            call_kwargs = mock_table.query.call_args[1]
            assert call_kwargs["IndexName"] == "created-at-index"
            assert call_kwargs["ScanIndexForward"] is False
        finally:
            _cleanup()

    def test_list_qa_pairs_pagination(self):
        """GET /qa-pairs returns lastKey when more pages exist."""
        last_key = {"qa_pair_id": "abc", "gsi_pk": "ALL", "detected_at": "2026-03-31T00:00:00"}
        mock_table = MagicMock()
        mock_table.query.return_value = {
            "Items": [SAMPLE_QA_PAIR],
            "LastEvaluatedKey": last_key,
        }

        handler_mod = _import_handler(mock_table)
        try:
            event = {
                "httpMethod": "GET",
                "resource": "/qa-pairs",
                "queryStringParameters": {"limit": "1"},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["data"]["lastKey"] is not None
            decoded_key = json.loads(body["data"]["lastKey"])
            assert decoded_key == last_key
        finally:
            _cleanup()

    def test_get_qa_pair_not_found_returns_404(self):
        """GET /qa-pairs/{qaPairId} returns 404 for non-existent pair."""
        mock_table = MagicMock()
        mock_table.get_item.return_value = {}

        handler_mod = _import_handler(mock_table)
        try:
            event = {
                "httpMethod": "GET",
                "resource": "/qa-pairs/{qaPairId}",
                "pathParameters": {"qaPairId": "nonexistent-id"},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 404
            body = json.loads(response["body"])
            assert body["status"] is False
            assert body["message"] == "QA pair not found"
        finally:
            _cleanup()

    def test_delete_qa_pair_success(self):
        """DELETE /qa-pairs/{qaPairId} returns 200 for existing pair."""
        mock_table = MagicMock()
        mock_table.get_item.return_value = {"Item": SAMPLE_QA_PAIR}

        handler_mod = _import_handler(mock_table)
        try:
            event = {
                "httpMethod": "DELETE",
                "resource": "/qa-pairs/{qaPairId}",
                "pathParameters": {"qaPairId": SAMPLE_QA_PAIR["qa_pair_id"]},
            }
            response = handler_mod.lambda_handler(event, None)

            assert response["statusCode"] == 200
            body = json.loads(response["body"])
            assert body["status"] is True
            mock_table.delete_item.assert_called_once()
        finally:
            _cleanup()
