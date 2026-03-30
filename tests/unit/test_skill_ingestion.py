"""Unit tests for SkillIngestion Lambda handler."""

import os
import sys
from unittest.mock import MagicMock, patch

import pytest

SKILL_INGESTION_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "SkillIngestion")
)


def _import_handler():
    sys.path.insert(0, SKILL_INGESTION_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch("boto3.resource"), \
         patch("boto3.client"), \
         patch("boto3.Session"):
        import lambda_function as mod

    return mod


def _cleanup():
    if SKILL_INGESTION_DIR in sys.path:
        sys.path.remove(SKILL_INGESTION_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_vars():
    with patch.dict(os.environ, {
        "OPENSEARCH_ENDPOINT": "https://test-os.example.com",
        "INDEX_NAME": "knowledge-vectors",
        "BEDROCK_REGION": "us-east-1",
        "SKILLS_TABLE_NAME": "test-Skills",
    }):
        yield
    _cleanup()


class TestSkillIngestion:
    def test_parse_skill_key_valid(self):
        """Valid 2-part key returns (skill_id, filename)."""
        mod = _import_handler()
        try:
            skill_id, filename = mod._parse_skill_key("abc-123/document.pdf")
            assert skill_id == "abc-123"
            assert filename == "document.pdf"
        finally:
            _cleanup()

    def test_parse_skill_key_invalid(self):
        """Key without slash raises ValueError."""
        mod = _import_handler()
        try:
            with pytest.raises(ValueError):
                mod._parse_skill_key("no-slash-key")
        finally:
            _cleanup()

    def test_chunk_text(self):
        """chunk_text splits text into overlapping chunks."""
        mod = _import_handler()
        try:
            text = "a" * 2500
            chunks = mod.chunk_text(text, chunk_size=1000, overlap=200)
            assert len(chunks) >= 3
            # First chunk is 1000 chars
            assert len(chunks[0]) == 1000
        finally:
            _cleanup()

    def test_handler_processes_s3_records(self):
        """Handler processes S3 records and calls ingestion pipeline."""
        mod = _import_handler()
        try:
            with patch.object(mod, "_extract_text_from_file", return_value="Some skill text content"), \
                 patch.object(mod, "_generate_embedding", return_value=[0.1] * 1024), \
                 patch.object(mod, "_index_document"), \
                 patch.object(mod, "_update_skill_status"), \
                 patch.object(mod, "_get_opensearch_client"):
                event = {
                    "Records": [{
                        "s3": {
                            "bucket": {"name": "test-skills"},
                            "object": {"key": "skill-123/doc.pdf"},
                        }
                    }]
                }
                response = mod.lambda_handler(event, None)
                assert response["statusCode"] == 200
                mod._update_skill_status.assert_called_with("skill-123", "active")
        finally:
            _cleanup()


    def test_extract_text_from_txt_file(self):
        """Verify .txt files are decoded as UTF-8."""
        mod = _import_handler()
        try:
            content = "Plain text skill document."
            mock_body = MagicMock()
            mock_body.read.return_value = content.encode("utf-8")

            mock_s3 = MagicMock()
            mock_s3.get_object.return_value = {"Body": mock_body}

            result = mod._extract_text_from_file(mock_s3, "test-skills", "skill-1/doc.txt")
            assert result == content
        finally:
            _cleanup()

    def test_extract_text_from_docx_file(self):
        """Verify .docx files use python-docx Document class."""
        mod = _import_handler()
        try:
            mock_body = MagicMock()
            mock_body.read.return_value = b"fake-docx-bytes"

            mock_s3 = MagicMock()
            mock_s3.get_object.return_value = {"Body": mock_body}

            para1 = MagicMock()
            para1.text = "First paragraph"
            para2 = MagicMock()
            para2.text = "Second paragraph"
            para_empty = MagicMock()
            para_empty.text = "   "

            mock_doc = MagicMock()
            mock_doc.paragraphs = [para1, para2, para_empty]

            with patch.dict(sys.modules, {"docx": MagicMock()}):
                import docx as mock_docx_mod
                mock_docx_mod.Document.return_value = mock_doc

                result = mod._extract_text_from_file(mock_s3, "test-skills", "skill-1/doc.docx")
                assert result == "First paragraph\nSecond paragraph"
        finally:
            _cleanup()
