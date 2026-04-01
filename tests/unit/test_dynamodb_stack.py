"""CDK stack assertion tests for DynamoDBStack.

Per testing-standards: 3-5 tests per resource covering creation,
env variance, and GSI configuration.
"""

import aws_cdk as cdk
import aws_cdk.assertions as assertions
import pytest

from stack_cdk.dynamodb_stack import DynamoDBStack


class TestDynamoDBStack:
    """DynamoDBStack: table counts, OpenSearch, GSIs, env naming."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        app = cdk.App()
        stack = DynamoDBStack(app, "TestDynamoDBStack", env_name="dev")
        self.template = assertions.Template.from_stack(stack)

    def test_eighteen_tables_created(self):
        self.template.resource_count_is("AWS::DynamoDB::Table", 18)

    def test_opensearch_domain_created(self):
        self.template.resource_count_is("AWS::OpenSearchService::Domain", 1)

    def test_sessions_has_active_sessions_index(self):
        self.template.has_resource_properties(
            "AWS::DynamoDB::Table",
            assertions.Match.object_like({
                "TableName": "dev-Sessions",
                "GlobalSecondaryIndexes": assertions.Match.array_with([
                    assertions.Match.object_like({"IndexName": "active-sessions-index"})
                ]),
            }),
        )

    def test_agents_table_exists(self):
        self.template.has_resource_properties(
            "AWS::DynamoDB::Table",
            {"TableName": "dev-Agents"},
        )

    def test_skills_table_has_name_index(self):
        self.template.has_resource_properties(
            "AWS::DynamoDB::Table",
            assertions.Match.object_like({
                "TableName": "dev-Skills",
                "GlobalSecondaryIndexes": assertions.Match.array_with([
                    assertions.Match.object_like({"IndexName": "name-index"})
                ]),
            }),
        )

    def test_token_usage_table_has_session_index(self):
        self.template.has_resource_properties(
            "AWS::DynamoDB::Table",
            assertions.Match.object_like({
                "TableName": "dev-TokenUsage",
                "GlobalSecondaryIndexes": assertions.Match.array_with([
                    assertions.Match.object_like({"IndexName": "session-index"})
                ]),
            }),
        )

    def test_admin_changelog_table_has_entity_type_index(self):
        self.template.has_resource_properties(
            "AWS::DynamoDB::Table",
            assertions.Match.object_like({
                "TableName": "dev-AdminChangelog",
                "GlobalSecondaryIndexes": assertions.Match.array_with([
                    assertions.Match.object_like({"IndexName": "entity-type-index"})
                ]),
            }),
        )

    def test_agent_config_history_table_exists(self):
        self.template.has_resource_properties(
            "AWS::DynamoDB::Table",
            {"TableName": "dev-AgentConfigHistory"},
        )
