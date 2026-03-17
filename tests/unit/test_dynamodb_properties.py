"""Property-based tests for DynamoDB agent sessions.

Removed trivial dict-construction properties (agent/personality record
schema, referential consistency) that only validate data structures,
not actual logic. Kept seed error propagation and transcript structure.
"""

import json
import os
import sys
import types
from unittest.mock import MagicMock, patch

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from gmeet_agent.gmeet_agent_stack import SEED_HANDLER_CODE


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
# Helpers
# ---------------------------------------------------------------------------

def _build_seed_handler(mock_agents_table: MagicMock, mock_personalities_table: MagicMock):
    """Compile and exec SEED_HANDLER_CODE with mocked boto3.resource."""
    def _mock_table(name):
        if name == "test-agents-table":
            return mock_agents_table
        return mock_personalities_table

    mock_resource = MagicMock()
    mock_resource.Table.side_effect = _mock_table

    fake_boto3 = types.ModuleType("boto3")
    fake_boto3.resource = MagicMock(return_value=mock_resource)

    env_vars = {
        "TABLE_NAME": "test-agents-table",
        "PERSONALITIES_TABLE_NAME": "test-personalities-table",
    }
    namespace: dict = {}

    with patch.dict(os.environ, env_vars), patch.dict(
        sys.modules, {"boto3": fake_boto3}
    ):
        code = compile(SEED_HANDLER_CODE, "<seed_handler>", "exec")
        exec(code, namespace)  # noqa: S102

    return namespace["handler"]


# ---------------------------------------------------------------------------
# Property 1 – Transcript record structure validity
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
# Property 2 – Seed function error propagation
# ---------------------------------------------------------------------------


class TestSeedErrorPropagation:
    """Seed handler propagates put_item exceptions from both tables."""

    @given(error_msg=st.text(min_size=1))
    @settings(max_examples=50)
    def test_agents_put_item_exception_propagates(self, error_msg: str) -> None:
        mock_agents = MagicMock()
        mock_agents.put_item.side_effect = Exception(error_msg)
        mock_personalities = MagicMock()

        handler = _build_seed_handler(mock_agents, mock_personalities)
        with pytest.raises(Exception):
            handler({"RequestType": "Create"}, None)

    @given(error_msg=st.text(min_size=1))
    @settings(max_examples=50)
    def test_personalities_put_item_exception_propagates(self, error_msg: str) -> None:
        mock_agents = MagicMock()
        mock_personalities = MagicMock()
        mock_personalities.put_item.side_effect = Exception(error_msg)

        handler = _build_seed_handler(mock_agents, mock_personalities)
        with pytest.raises(Exception):
            handler({"RequestType": "Create"}, None)
