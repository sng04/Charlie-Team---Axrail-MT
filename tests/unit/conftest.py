"""Shared fixtures and module-level mocks for the unified test suite."""
import os
import sys
from unittest.mock import MagicMock

# ---------------------------------------------------------------------------
# Module-level mocks — must happen before any Lambda import
# ---------------------------------------------------------------------------

# Mock aws-lambda-powertools
mock_powertools = MagicMock()
mock_powertools.Logger.return_value = MagicMock()
_mock_tracer = MagicMock()
_mock_tracer.capture_lambda_handler = lambda f: f
_mock_tracer.capture_method = lambda f: f
mock_powertools.Tracer.return_value = _mock_tracer
sys.modules["aws_lambda_powertools"] = mock_powertools

# Mock Strands SDK
sys.modules["strands"] = MagicMock()
sys.modules["strands.models"] = MagicMock()
sys.modules["strands.models.bedrock"] = MagicMock()

# Mock OpenSearch + PyPDF2
sys.modules["opensearchpy"] = MagicMock()
sys.modules["requests_aws4auth"] = MagicMock()
sys.modules["PyPDF2"] = MagicMock()

# ---------------------------------------------------------------------------
# Layer path injection — add SharedLayer so response_utils / custom_exceptions
# are importable by Lambda code under test.
# ---------------------------------------------------------------------------
_layers_base = os.path.join(os.path.dirname(__file__), "..", "..", "lambdas", "Layers")
for layer_dir in ["SharedLayer", "PowertoolsLayer", "StrandsLayer"]:
    path = os.path.join(_layers_base, layer_dir, "python")
    if os.path.isdir(path):
        sys.path.insert(0, os.path.abspath(path))

# ---------------------------------------------------------------------------
# Environment variable defaults (D1 + D2 tables)
# ---------------------------------------------------------------------------
_defaults = {
    # D1 tables
    "USERS_TABLE": "test-Users",
    "PROJECTS_TABLE": "test-Projects",
    "PROJECT_USERS_TABLE": "test-ProjectUsers",
    "SESSIONS_TABLE": "test-Sessions",
    "TRANSCRIPTS_TABLE": "test-Transcripts",
    "BOT_CREDENTIALS_TABLE": "test-BotCredentials",
    "BOT_POOL_TABLE": "test-BotPool",
    # D2 tables
    "AGENTS_TABLE_NAME": "test-Agents",
    "PERSONALITIES_TABLE_NAME": "test-Personalities",
    "QA_PAIRS_TABLE_NAME": "test-QAPairs",
    "SUGGESTED_QUESTIONS_TABLE_NAME": "test-SuggestedQuestions",
    "SKILLS_TABLE_NAME": "test-Skills",
    "SESSIONS_TABLE_NAME": "test-Sessions",
    "TRANSCRIPTS_TABLE_NAME": "test-Transcripts",
    # Infrastructure
    "OPENSEARCH_ENDPOINT": "https://test-os.example.com",
    "INDEX_NAME": "knowledge-vectors",
    "BEDROCK_REGION": "us-east-1",
    "WEBSOCKET_ENDPOINT": "https://test-ws.example.com",
    "KB_BUCKET_NAME": "test-kb",
    "SKILLS_BUCKET_NAME": "test-skills",
    "USER_POOL_ID": "test-pool",
    "CLIENT_ID": "test-client",
    "ENVIRONMENT": "test",
    "POWERTOOLS_SERVICE_NAME": "test",
    "LOG_LEVEL": "DEBUG",
    "ECS_CLUSTER": "test-cluster",
    "EVENT_BUS_NAME": "default",
}
for k, v in _defaults.items():
    os.environ.setdefault(k, v)
