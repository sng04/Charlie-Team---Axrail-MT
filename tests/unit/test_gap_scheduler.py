"""Unit tests for GapScheduler Lambda handler.

Per testing-standards: 2-3 tests per async/ETL handler covering
success and partial failure paths.
"""

import json
import os
import sys
from unittest.mock import MagicMock, patch

import pytest

GAP_SCHEDULER_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Functions", "GapScheduler")
)


def _import_handler():
    """Import the GapScheduler handler with mocked boto3 clients."""
    sys.path.insert(0, GAP_SCHEDULER_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]

    import lambda_function as mod
    return mod


def _cleanup():
    if GAP_SCHEDULER_DIR in sys.path:
        sys.path.remove(GAP_SCHEDULER_DIR)
    for mod_name in list(sys.modules.keys()):
        if mod_name == "lambda_function":
            del sys.modules[mod_name]


@pytest.fixture(autouse=True)
def _env_and_reset():
    with patch.dict(os.environ, {
        "SESSIONS_TABLE_NAME": "test-sessions",
        "AGENT_FUNCTION_NAME": "test-agent-fn",
    }):
        yield
    _cleanup()


class TestGapScheduler:
    """GapScheduler: triggers gap analysis for active sessions with new transcripts."""

    def test_triggers_eligible_sessions(self):
        """Sessions with new transcript data get gap analysis invoked."""
        mock_table = MagicMock()
        mock_table.query.return_value = {
            "Items": [
                {
                    "session_id": "sess-1",
                    "connection_id": "conn-1",
                    "last_transcript_update_at": "2026-03-21T10:00:00Z",
                    "last_gap_analysis_at": "2026-03-21T09:00:00Z",
                },
            ]
        }
        mock_lambda = MagicMock()

        handler_mod = _import_handler()
        try:
            handler_mod._dynamodb = None
            handler_mod._lambda_client = None
            with patch.object(handler_mod, "_get_dynamodb") as mock_get_ddb, \
                 patch.object(handler_mod, "_get_lambda_client") as mock_get_lc:
                mock_ddb = MagicMock()
                mock_ddb.Table.return_value = mock_table
                mock_get_ddb.return_value = mock_ddb
                mock_get_lc.return_value = mock_lambda

                result = handler_mod.lambda_handler({}, None)

            assert result["statusCode"] == 200
            assert "1/1" in result["body"]
            mock_lambda.invoke.assert_called_once()
        finally:
            _cleanup()

    def test_skips_sessions_without_new_transcripts(self):
        """Sessions where last_gap_analysis_at >= last_transcript_update_at are skipped."""
        mock_table = MagicMock()
        mock_table.query.return_value = {
            "Items": [
                {
                    "session_id": "sess-1",
                    "connection_id": "conn-1",
                    "last_transcript_update_at": "2026-03-21T09:00:00Z",
                    "last_gap_analysis_at": "2026-03-21T10:00:00Z",
                },
            ]
        }
        mock_lambda = MagicMock()

        handler_mod = _import_handler()
        try:
            handler_mod._dynamodb = None
            handler_mod._lambda_client = None
            with patch.object(handler_mod, "_get_dynamodb") as mock_get_ddb, \
                 patch.object(handler_mod, "_get_lambda_client") as mock_get_lc:
                mock_ddb = MagicMock()
                mock_ddb.Table.return_value = mock_table
                mock_get_ddb.return_value = mock_ddb
                mock_get_lc.return_value = mock_lambda

                result = handler_mod.lambda_handler({}, None)

            assert result["statusCode"] == 200
            assert "0/1" in result["body"]
            mock_lambda.invoke.assert_not_called()
        finally:
            _cleanup()

    def test_no_active_sessions(self):
        """Returns early when no active sessions exist."""
        mock_table = MagicMock()
        mock_table.query.return_value = {"Items": []}

        handler_mod = _import_handler()
        try:
            handler_mod._dynamodb = None
            handler_mod._lambda_client = None
            with patch.object(handler_mod, "_get_dynamodb") as mock_get_ddb:
                mock_ddb = MagicMock()
                mock_ddb.Table.return_value = mock_table
                mock_get_ddb.return_value = mock_ddb

                result = handler_mod.lambda_handler({}, None)

            assert result["statusCode"] == 200
            assert "No active sessions" in result["body"]
        finally:
            _cleanup()
