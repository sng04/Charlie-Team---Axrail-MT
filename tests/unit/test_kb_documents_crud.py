"""Unit tests for KbDocumentsCrud Lambda handler."""

import json
from unittest.mock import MagicMock, patch

import pytest


def _parse_body(response):
    return json.loads(response["body"])


class TestKbDocumentsCrud:
    """KbDocumentsCrud: list, create, delete, and validation."""

    @patch("lambdas.Functions.KbDocumentsCrud.lambda_function.documents_table")
    def test_list_documents(self, mock_table):
        from lambdas.Functions.KbDocumentsCrud.lambda_function import lambda_handler

        mock_table.query.return_value = {
            "Items": [
                {"document_id": "d1", "file_name": "a.pdf", "project_id": "p1", "created_at": "2024-01-01"},
            ]
        }

        event = {
            "httpMethod": "GET",
            "resource": "/projects/{projectId}/kb-documents",
            "pathParameters": {"projectId": "p1"},
            "queryStringParameters": None,
        }
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        assert body["data"]["count"] == 1

    @patch("lambdas.Functions.KbDocumentsCrud.lambda_function.s3_client")
    @patch("lambdas.Functions.KbDocumentsCrud.lambda_function.documents_table")
    def test_create_document(self, mock_table, mock_s3):
        from lambdas.Functions.KbDocumentsCrud.lambda_function import lambda_handler

        mock_s3.generate_presigned_url.return_value = "https://s3.example.com/upload"

        event = {
            "httpMethod": "POST",
            "resource": "/projects/{projectId}/kb-documents",
            "pathParameters": {"projectId": "p1"},
            "body": json.dumps({"file_name": "report.pdf"}),
        }
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        assert "upload_url" in body["data"]
        mock_table.put_item.assert_called_once()

    @patch("lambdas.Functions.KbDocumentsCrud.lambda_function.s3_client")
    @patch("lambdas.Functions.KbDocumentsCrud.lambda_function.documents_table")
    def test_delete_document(self, mock_table, mock_s3):
        from lambdas.Functions.KbDocumentsCrud.lambda_function import lambda_handler

        mock_table.get_item.return_value = {
            "Item": {"document_id": "d1", "s3_key": "p1/report.pdf"}
        }

        event = {
            "httpMethod": "DELETE",
            "resource": "/projects/{projectId}/kb-documents/{documentId}",
            "pathParameters": {"projectId": "p1", "documentId": "d1"},
        }
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        mock_table.delete_item.assert_called_once()

    def test_create_missing_filename(self):
        from lambdas.Functions.KbDocumentsCrud.lambda_function import lambda_handler

        event = {
            "httpMethod": "POST",
            "resource": "/projects/{projectId}/kb-documents",
            "pathParameters": {"projectId": "p1"},
            "body": json.dumps({}),
        }
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 400
        assert body["status"] is False
