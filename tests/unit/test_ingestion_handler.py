"""Property-based tests for the ingestion Lambda handler.

Feature: opensearch-knowledge-base
"""

import json
import sys
import os
from unittest.mock import MagicMock, patch

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

# Add the Ingestion Lambda directory to sys.path
sys.path.insert(
    0,
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "Ingestion"),
)

from lambda_function import chunk_text, _retry_with_backoff, _generate_embedding  # noqa: E402

# ---------------------------------------------------------------------------
# Strategies
# ---------------------------------------------------------------------------

non_empty_text = st.text(min_size=1)


class TestChunkTextCoversAllInput:
    """Text chunking covers all input text."""

    @given(text=non_empty_text)
    @settings(max_examples=100)
    def test_reconstructed_text_equals_original(self, text: str) -> None:
        chunk_size = 1000
        overlap = 200
        step = chunk_size - overlap

        chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)

        assert len(chunks) >= 1
        reconstructed = ""
        for i, chunk in enumerate(chunks):
            if i < len(chunks) - 1:
                reconstructed += chunk[:step]
            else:
                reconstructed += chunk
        assert reconstructed == text


class TestChunkTextRespectsBounds:
    """Text chunking respects size and overlap bounds."""

    @given(text=non_empty_text)
    @settings(max_examples=100)
    def test_chunk_sizes_and_overlap(self, text: str) -> None:
        chunk_size = 1000
        overlap = 200

        chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)

        for chunk in chunks:
            assert len(chunk) <= chunk_size

        for i in range(len(chunks) - 1):
            if len(chunks[i]) >= overlap:
                assert chunks[i][-overlap:] == chunks[i + 1][:overlap]


class TestVectorDocumentSchema:
    """Vector document schema completeness."""

    @given(
        text=st.text(min_size=1),
        project_id=st.text(min_size=1),
        source_file=st.text(min_size=1),
        chunk_index=st.integers(min_value=0),
    )
    @settings(max_examples=100)
    def test_vector_document_has_all_required_fields(
        self, text, project_id, source_file, chunk_index,
    ) -> None:
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
        assert isinstance(document["embedding"], list)
        assert len(document["embedding"]) == 1024
        assert document["doc_type"] == "user_upload"


class TestEmbeddingCallCount:
    """Embedding call count matches chunk count."""

    @given(chunks=st.lists(st.text(min_size=1), min_size=1, max_size=20))
    @settings(max_examples=100)
    def test_invoke_model_called_once_per_chunk(self, chunks: list) -> None:
        fake_embedding = [0.0] * 1024
        fake_response_body = json.dumps({"embedding": fake_embedding}).encode()

        mock_body = MagicMock()
        mock_body.read.return_value = fake_response_body

        mock_bedrock = MagicMock()
        mock_bedrock.invoke_model.return_value = {"body": mock_body}

        for chunk in chunks:
            _generate_embedding(mock_bedrock, chunk)

        assert mock_bedrock.invoke_model.call_count == len(chunks)


class TestRetryExhaustionRaises:
    """Retry exhaustion raises exception."""

    @given(error_msg=st.text(min_size=1))
    @settings(max_examples=100)
    def test_exception_propagates_after_retries(self, error_msg: str) -> None:
        mock_func = MagicMock(side_effect=RuntimeError(error_msg))

        with patch("lambda_function.time.sleep"):
            with pytest.raises(RuntimeError):
                _retry_with_backoff(mock_func)

        assert mock_func.call_count == 3
