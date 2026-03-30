"""Unit tests for FileDownload Lambda handler."""

import json
from unittest.mock import MagicMock, patch

import pytest


def _parse_body(response):
    return json.loads(response["body"])


class TestFileDownload:
    """FileDownload: presigned URL generation for KB and Skills buckets."""

    @patch("lambdas.Functions.FileDownload.lambda_function.s3_client")
    def test_success_kb_bucket(self, mock_s3):
        from lambdas.Functions.FileDownload.lambda_function import lambda_handler

        mock_s3.head_object.return_value = {}
        mock_s3.generate_presigned_url.return_value = "https://s3.example.com/presigned"
        mock_s3.exceptions.NoSuchKey = type("NoSuchKey", (Exception,), {})

        event = {"queryStringParameters": {"key": "proj-1/doc.pdf"}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        assert "download_url" in body["data"]

    @patch("lambdas.Functions.FileDownload.lambda_function.ALLOWED_BUCKETS", {"test-kb", "test-skills"})
    @patch("lambdas.Functions.FileDownload.lambda_function.s3_client")
    def test_success_skills_bucket(self, mock_s3):
        from lambdas.Functions.FileDownload.lambda_function import lambda_handler

        mock_s3.head_object.return_value = {}
        mock_s3.generate_presigned_url.return_value = "https://s3.example.com/presigned"
        mock_s3.exceptions.NoSuchKey = type("NoSuchKey", (Exception,), {})

        event = {"queryStringParameters": {"key": "skill-1/doc.pdf", "bucket": "test-skills"}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 200
        assert "download_url" in body["data"]

    def test_missing_key(self):
        from lambdas.Functions.FileDownload.lambda_function import lambda_handler

        event = {"queryStringParameters": {}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 400
        assert body["status"] is False

    @patch("lambdas.Functions.FileDownload.lambda_function.ALLOWED_BUCKETS", {"test-kb"})
    def test_bucket_not_allowed(self):
        from lambdas.Functions.FileDownload.lambda_function import lambda_handler

        event = {"queryStringParameters": {"key": "doc.pdf", "bucket": "unknown-bucket"}}
        response = lambda_handler(event, None)
        body = _parse_body(response)

        assert response["statusCode"] == 400
        assert body["status"] is False
