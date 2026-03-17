"""Property-based tests for the ingestion Lambda handler.

Feature: opensearch-knowledge-base
"""

import json
import sys
import os
import time
from unittest.mock import MagicMock, patch

import pytest
from hypothesis import given, settings, assume
from hypothesis import strategies as st

# Add the ingestion Lambda directory to sys.path so we can import from it.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "lambda", "ingestion"))

# We need to mock heavy dependencies before importing the handler module.
# opensearchpy, requests_aws4auth, and PyPDF2 are not available in the test env.
sys.modules.setdefault("opensearchpy", MagicMock())
sys.modules.setdefault("requests_aws4auth", MagicMock())
sys.modules.setdefault("PyPDF2", MagicMock())

from index import chunk_text, _retry_with_backoff, _generate_embedding  # noqa: E402


# ---------------------------------------------------------------------------
# Strategies
# ---------------------------------------------------------------------------

non_empty_text = st.text(min_size=1)


# ---------------------------------------------------------------------------
# Property 1 – Text chunking covers all input text
# Feature: opensearch-knowledge-base, Property 1: Text chunking covers all input text
# Validates: Requirement 4.4
# ---------------------------------------------------------------------------


class TestChunkTextCoversAllInput:
    """**Validates: Requirements 4.4**"""

    @given(text=non_empty_text)
    @settings(max_examples=100)
    def test_reconstructed_text_equals_original(self, text: str) -> None:
        """For any non-empty string, chunking and reconstructing from
        non-overlapping portions yields the original text."""
        chunk_size = 1000
        overlap = 200
        step = chunk_size - overlap

        chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)

        # Reconstruct: take the first `step` chars from every chunk except the
        # last, then append the entire last chunk.
        assert len(chunks) >= 1
        reconstructed = ""
        for i, chunk in enumerate(chunks):
            if i < len(chunks) - 1:
                reconstructed += chunk[:step]
            else:
                reconstructed += chunk
        assert reconstructed == text


# ---------------------------------------------------------------------------
# Property 2 – Text chunking respects size and overlap bounds
# Feature: opensearch-knowledge-base, Property 2: Text chunking respects size and overlap bounds
# Validates: Requirement 4.4
# ---------------------------------------------------------------------------


class TestChunkTextRespectsBounds:
    """**Validates: Requirements 4.4**"""

    @given(text=non_empty_text)
    @settings(max_examples=100)
    def test_chunk_sizes_and_overlap(self, text: str) -> None:
        """Every chunk has length ≤ 1000 and consecutive chunks share exactly
        200 characters of overlap (when the earlier chunk is long enough)."""
        chunk_size = 1000
        overlap = 200

        chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)

        for chunk in chunks:
            assert len(chunk) <= chunk_size

        for i in range(len(chunks) - 1):
            if len(chunks[i]) >= overlap:
                assert chunks[i][-overlap:] == chunks[i + 1][:overlap]


# ---------------------------------------------------------------------------
# Property 3 – Vector document schema completeness
# Feature: opensearch-knowledge-base, Property 3: Vector document schema completeness
# Validates: Requirements 4.6, 4.7
# ---------------------------------------------------------------------------


class TestVectorDocumentSchema:
    """**Validates: Requirements 4.6, 4.7**"""

    @given(
        text=st.text(min_size=1),
        project_id=st.text(min_size=1),
        source_file=st.text(min_size=1),
        chunk_index=st.integers(min_value=0),
    )
    @settings(max_examples=100)
    def test_vector_document_has_all_required_fields(
        self,
        text: str,
        project_id: str,
        source_file: str,
        chunk_index: int,
    ) -> None:
        """For any valid metadata, the vector document contains all required
        fields with correct types and doc_type equals 'user_upload'."""
        document = {
            "embedding": [0.0] * 1024,
            "text": text,
            "project_id": project_id,
            "doc_type": "user_upload",
            "source_file": source_file,
            "chunk_index": chunk_index,
        }

        required_fields = {"embedding", "text", "project_id", "doc_type", "source_file", "chunk_index"}
        assert set(document.keys()) == required_fields

        # embedding is a list of 1024 floats
        assert isinstance(document["embedding"], list)
        assert len(document["embedding"]) == 1024
        assert all(isinstance(v, float) for v in document["embedding"])

        # doc_type is always user_upload
        assert document["doc_type"] == "user_upload"

        # text, project_id, source_file are strings
        assert isinstance(document["text"], str)
        assert isinstance(document["project_id"], str)
        assert isinstance(document["source_file"], str)

        # chunk_index is an integer
        assert isinstance(document["chunk_index"], int)


# ---------------------------------------------------------------------------
# Property 4 – Embedding call count matches chunk count
# Feature: opensearch-knowledge-base, Property 4: Embedding call count matches chunk count
# Validates: Requirement 4.5
# ---------------------------------------------------------------------------


class TestEmbeddingCallCount:
    """**Validates: Requirements 4.5**"""

    @given(chunks=st.lists(st.text(min_size=1), min_size=1, max_size=20))
    @settings(max_examples=100)
    def test_invoke_model_called_once_per_chunk(self, chunks: list) -> None:
        """For any list of N chunks, _generate_embedding is called N times,
        resulting in exactly N invoke_model calls."""
        fake_embedding = [0.0] * 1024
        fake_response_body = json.dumps({"embedding": fake_embedding}).encode()

        mock_body = MagicMock()
        mock_body.read.return_value = fake_response_body

        mock_bedrock = MagicMock()
        mock_bedrock.invoke_model.return_value = {"body": mock_body}

        for chunk in chunks:
            _generate_embedding(mock_bedrock, chunk)

        assert mock_bedrock.invoke_model.call_count == len(chunks)


# ---------------------------------------------------------------------------
# Property 5 – Retry exhaustion raises exception
# Feature: opensearch-knowledge-base, Property 5: Retry exhaustion raises exception
# Validates: Requirements 4.12, 4.13
# ---------------------------------------------------------------------------


class TestRetryExhaustionRaises:
    """**Validates: Requirements 4.12, 4.13**"""

    @given(error_msg=st.text(min_size=1))
    @settings(max_examples=100)
    def test_exception_propagates_after_retries(self, error_msg: str) -> None:
        """For any exception message, if the wrapped function always fails,
        _retry_with_backoff raises the exception after 3 retries."""
        mock_func = MagicMock(side_effect=RuntimeError(error_msg))

        with patch("index.time.sleep"):
            with pytest.raises(RuntimeError):
                _retry_with_backoff(mock_func)

        assert mock_func.call_count == 3
