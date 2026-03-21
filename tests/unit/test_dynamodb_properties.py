"""Property-based tests for DynamoDB agent seed data and transcript structure.

Rewritten to test the SeedAgentData Lambda directly instead of the
deleted gmeet_agent_stack inline code.
"""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

# ---------------------------------------------------------------------------
# Strategies
# ---------------------------------------------------------------------------

non_empty_text = st.text(min_size=1)

transcript_entry_st = st.fixed_dictionaries({"transcript": non_empty_text})
speaker_item_st = st.fixed_dictionaries({
    "start_time": non_empty_text,
    "end_time": non_empty_text,
    "speaker_label": non_empty_text,
})
segment_st = st.fixed_dictionaries({
    "start_time": non_empty_text,
    "end_time": non_empty_text,
    "speaker_label": non_empty_text,
    "items": st.lists(speaker_item_st, min_size=0, max_size=3),
})
alternative_st = st.fixed_dictionaries({
    "confidence": non_empty_text,
    "content": non_empty_text,
})
result_item_st = st.fixed_dictionaries({
    "start_time": non_empty_text,
    "end_time": non_empty_text,
    "alternatives": st.lists(alternative_st, min_size=0, max_size=3),
    "type": non_empty_text,
})
speaker_labels_st = st.fixed_dictionaries({
    "speakers": st.integers(min_value=1, max_value=10),
    "segments": st.lists(segment_st, min_size=0, max_size=3),
})
transcript_st = st.fixed_dictionaries({
    "jobName": non_empty_text,
    "accountId": non_empty_text,
    "status": non_empty_text,
    "results": st.fixed_dictionaries({
        "transcripts": st.lists(transcript_entry_st, min_size=0, max_size=3),
        "speaker_labels": speaker_labels_st,
        "items": st.lists(result_item_st, min_size=0, max_size=5),
    }),
})


# ---------------------------------------------------------------------------
# Helpers — import SeedAgentData Lambda
# ---------------------------------------------------------------------------

SEED_LAMBDA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "SeedAgentData")
)


def _import_seed_handler(mock_agents_table, mock_personalities_table):
    """Import the SeedAgentData handler with mocked DynamoDB tables."""
    sys.path.insert(0, SEED_LAMBDA_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    with patch.dict(os.environ, {
        "AGENTS_TABLE_NAME": "test-agents",
        "PERSONALITIES_TABLE_NAME": "test-personalities",
    }):
        with patch("boto3.resource") as mock_boto:
            mock_dynamo = MagicMock()
            mock_boto.return_value = mock_dynamo

            def table_side_effect(name):
                if "agents" in name.lower():
                    return mock_agents_table
                return mock_personalities_table

            mock_dynamo.Table.side_effect = table_side_effect
            import lambda_function as seed_mod

    return seed_mod


def _cleanup_seed():
    if SEED_LAMBDA_DIR in sys.path:
        sys.path.remove(SEED_LAMBDA_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


# ---------------------------------------------------------------------------
# Property 1 — Transcript record structure validity
# ---------------------------------------------------------------------------


class TestTranscriptStructure:
    """JSON round-trip preserves transcript structure and required keys exist."""

    @given(transcript=transcript_st)
    @settings(max_examples=50)
    def test_transcript_json_round_trip_and_structure(self, transcript: dict) -> None:
        serialized = json.dumps(transcript)
        deserialized = json.loads(serialized)
        assert deserialized == transcript

        assert {"jobName", "accountId", "status", "results"} <= set(deserialized)
        results = deserialized["results"]
        assert isinstance(results["transcripts"], list)
        assert isinstance(results["speaker_labels"], dict)
        assert isinstance(results["items"], list)


# ---------------------------------------------------------------------------
# Property 2 — Seed function error propagation
# ---------------------------------------------------------------------------


class TestSeedErrorPropagation:
    """Seed handler propagates put_item exceptions from both tables."""

    @given(error_msg=st.text(min_size=1))
    @settings(max_examples=50)
    def test_personalities_put_item_exception_propagates(self, error_msg: str) -> None:
        mock_agents = MagicMock()
        mock_personalities = MagicMock()
        mock_personalities.put_item.side_effect = Exception(error_msg)

        handler_mod = _import_seed_handler(mock_agents, mock_personalities)
        try:
            with pytest.raises(Exception):
                handler_mod.lambda_handler({"RequestType": "Create"}, None)
        finally:
            _cleanup_seed()

    @given(error_msg=st.text(min_size=1))
    @settings(max_examples=50)
    def test_agents_put_item_exception_propagates(self, error_msg: str) -> None:
        mock_agents = MagicMock()
        mock_agents.put_item.side_effect = Exception(error_msg)
        mock_personalities = MagicMock()

        handler_mod = _import_seed_handler(mock_agents, mock_personalities)
        try:
            with pytest.raises(Exception):
                handler_mod.lambda_handler({"RequestType": "Create"}, None)
        finally:
            _cleanup_seed()


# ---------------------------------------------------------------------------
# Property 3 — Seed handler idempotency (Delete is no-op)
# ---------------------------------------------------------------------------


class TestSeedIdempotency:
    """Seed handler returns SUCCESS on Delete without writing data."""

    def test_delete_event_returns_success_without_writes(self) -> None:
        mock_agents = MagicMock()
        mock_personalities = MagicMock()

        handler_mod = _import_seed_handler(mock_agents, mock_personalities)
        try:
            result = handler_mod.lambda_handler({"RequestType": "Delete"}, None)
            assert result["Status"] == "SUCCESS"
            mock_agents.put_item.assert_not_called()
            mock_personalities.put_item.assert_not_called()
        finally:
            _cleanup_seed()
