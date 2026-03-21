"""Property-based and edge-case tests for the inline Lambda handler."""

import os
import sys
import types
from unittest.mock import MagicMock, patch

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st

from stack_cdk.bedrock_agent_stack import LAMBDA_HANDLER_CODE


def _build_handler(mock_client: MagicMock):
    """Compile and exec the inline handler code with a mocked boto3 client."""
    fake_boto3 = types.ModuleType("boto3")
    fake_boto3.client = MagicMock(return_value=mock_client)

    env_vars = {"AGENT_ID": "test-agent-id", "AGENT_ALIAS_ID": "test-alias-id"}
    namespace: dict = {}

    with patch.dict(os.environ, env_vars), patch.dict(sys.modules, {"boto3": fake_boto3}):
        code = compile(LAMBDA_HANDLER_CODE, "<lambda_handler>", "exec")
        exec(code, namespace)  # noqa: S102

    return namespace["handler"]


@pytest.fixture
def handler_module():
    mock_client = MagicMock()
    handler = _build_handler(mock_client)
    return types.SimpleNamespace(handler=handler, mock_client=mock_client)


class TestPromptRoundTrip:
    """Handler passes prompt to invoke_agent and returns 200."""

    @given(prompt=st.text(min_size=1).filter(lambda s: s.strip()))
    @settings(max_examples=100)
    def test_handler_passes_prompt_and_returns_200(self, prompt: str) -> None:
        mock_client = MagicMock()
        mock_client.invoke_agent.return_value = {
            "completion": [{"chunk": {"bytes": b"agent reply"}}],
        }

        handler = _build_handler(mock_client)
        result = handler({"prompt": prompt}, None)

        call_kwargs = mock_client.invoke_agent.call_args[1]
        assert call_kwargs["inputText"] == prompt
        assert result["statusCode"] == 200
        assert result["body"]["response"] == "agent reply"


class TestErrorPropagation:
    """Handler returns 500 with error message on exception."""

    @given(error_msg=st.text(min_size=1))
    @settings(max_examples=100)
    def test_handler_returns_500_with_error_message(self, error_msg: str) -> None:
        mock_client = MagicMock()
        mock_client.invoke_agent.side_effect = Exception(error_msg)

        handler = _build_handler(mock_client)
        result = handler({"prompt": "any prompt"}, None)

        assert result["statusCode"] == 500
        assert result["body"]["error"] == error_msg


class TestEdgeCases:
    """Edge-case tests for input validation."""

    def test_missing_prompt_returns_400(self, handler_module) -> None:
        result = handler_module.handler({}, None)
        assert result["statusCode"] == 400
        assert "error" in result["body"]

    def test_empty_prompt_returns_400(self, handler_module) -> None:
        result = handler_module.handler({"prompt": ""}, None)
        assert result["statusCode"] == 400
        assert "error" in result["body"]

    def test_whitespace_prompt_returns_400(self, handler_module) -> None:
        result = handler_module.handler({"prompt": "   \t\n  "}, None)
        assert result["statusCode"] == 400
        assert "error" in result["body"]
