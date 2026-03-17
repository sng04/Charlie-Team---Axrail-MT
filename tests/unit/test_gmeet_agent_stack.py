"""Unit tests for GMeetAgentStack CDK template assertions.

Tests are organized by resource group matching the stack's logical sections:
1. Shared Resources (layers)
2. Data Stores (DynamoDB, OpenSearch, S3)
3. API Services (REST API, CRUD Lambdas, WebSocket, Strands agent)
4. Seed Data (seed Lambda + custom resource)
"""

import aws_cdk as cdk
import aws_cdk.assertions as assertions
from aws_cdk.assertions import Match
import pytest

from gmeet_agent.gmeet_agent_stack import GMeetAgentStack


@pytest.fixture
def template():
    """Synthesize the GMeetAgentStack and return the template."""
    app = cdk.App()
    stack = GMeetAgentStack(app, "TestStack")
    return assertions.Template.from_stack(stack)


# ------------------------------------------------------------------
# 1. Shared Resources — Lambda layers
# ------------------------------------------------------------------


class TestLambdaLayers:
    """Lambda layers with Python 3.11 compatibility."""

    def test_layers_exist_with_python311(self, template):
        """At least two Lambda layers with Python 3.11 compatible runtime."""
        resources = template.find_resources(
            "AWS::Lambda::LayerVersion",
            {"Properties": {"CompatibleRuntimes": ["python3.11"]}},
        )
        assert len(resources) >= 2


# ------------------------------------------------------------------
# 2. Data Stores — DynamoDB, OpenSearch, S3
# ------------------------------------------------------------------

_EXPECTED_TABLES = {
    "agent_id": "AgentsTable",
    "project_id": "ProjectsTable",
    "session_id": "SessionsTable",
    "transcript_id": "TranscriptsTable",
    "personality_id": "PersonalitiesTable",
}


class TestDynamoDBTables:
    """DynamoDB table creation, key schemas, billing, and removal policy."""

    def test_five_tables_exist(self, template):
        """Exactly five DynamoDB tables are defined."""
        template.resource_count_is("AWS::DynamoDB::Table", 5)

    @pytest.mark.parametrize("partition_key", _EXPECTED_TABLES.keys())
    def test_table_key_schema_and_billing(self, template, partition_key):
        """Each table has the correct partition key and PAY_PER_REQUEST billing."""
        template.has_resource_properties(
            "AWS::DynamoDB::Table",
            Match.object_like({
                "KeySchema": [{"AttributeName": partition_key, "KeyType": "HASH"}],
                "BillingMode": "PAY_PER_REQUEST",
            }),
        )

    def test_all_tables_have_deletion_policy_delete(self, template):
        """Every DynamoDB table has DeletionPolicy Delete."""
        resources = template.find_resources("AWS::DynamoDB::Table")
        for logical_id, resource in resources.items():
            assert resource.get("DeletionPolicy") == "Delete", (
                f"{logical_id} DeletionPolicy is {resource.get('DeletionPolicy')!r}"
            )

    def test_sessions_table_project_index_gsi(self, template):
        """Sessions table has GSI 'project-index' on project_id."""
        template.has_resource_properties(
            "AWS::DynamoDB::Table",
            Match.object_like({
                "KeySchema": [{"AttributeName": "session_id", "KeyType": "HASH"}],
                "GlobalSecondaryIndexes": Match.array_with([
                    Match.object_like({
                        "IndexName": "project-index",
                        "KeySchema": [{"AttributeName": "project_id", "KeyType": "HASH"}],
                    }),
                ]),
            }),
        )

    def test_transcripts_table_session_index_gsi(self, template):
        """Transcripts table has GSI 'session-index' on session_id."""
        template.has_resource_properties(
            "AWS::DynamoDB::Table",
            Match.object_like({
                "KeySchema": [{"AttributeName": "transcript_id", "KeyType": "HASH"}],
                "GlobalSecondaryIndexes": Match.array_with([
                    Match.object_like({
                        "IndexName": "session-index",
                        "KeySchema": [{"AttributeName": "session_id", "KeyType": "HASH"}],
                    }),
                ]),
            }),
        )


class TestOpenSearchDomain:
    """OpenSearch domain configuration and removal policy."""

    def test_domain_configuration(self, template):
        """OpenSearch domain has correct engine, instance type, and EBS."""
        template.has_resource_properties(
            "AWS::OpenSearchService::Domain",
            Match.object_like({
                "EngineVersion": "OpenSearch_2.11",
                "ClusterConfig": {"InstanceType": "t3.small.search", "InstanceCount": 1},
                "EBSOptions": {"EBSEnabled": True, "VolumeSize": 20, "VolumeType": "gp3"},
            }),
        )

    def test_domain_deletion_policy(self, template):
        """OpenSearch domain has DeletionPolicy Delete."""
        template.has_resource(
            "AWS::OpenSearchService::Domain",
            Match.object_like({"DeletionPolicy": "Delete"}),
        )


class TestS3Bucket:
    """S3 knowledge base bucket and event notifications."""

    def test_bucket_deletion_policy(self, template):
        """S3 bucket has DeletionPolicy Delete."""
        template.has_resource(
            "AWS::S3::Bucket",
            Match.object_like({"DeletionPolicy": "Delete"}),
        )

    def test_pdf_notification_exists(self, template):
        """S3 bucket has .pdf notification targeting a Lambda."""
        template.has_resource_properties(
            "Custom::S3BucketNotifications",
            Match.object_like({
                "NotificationConfiguration": {
                    "LambdaFunctionConfigurations": Match.array_with([
                        Match.object_like({
                            "Events": ["s3:ObjectCreated:*"],
                            "Filter": {"Key": {"FilterRules": Match.array_with([
                                {"Name": "suffix", "Value": ".pdf"},
                            ])}},
                        }),
                    ]),
                },
            }),
        )


# ------------------------------------------------------------------
# 3. API Services — REST API, CRUD Lambdas, WebSocket, Strands agent
# ------------------------------------------------------------------


class TestRestApi:
    """REST API Gateway and CRUD Lambda configuration."""

    def test_rest_api_exists(self, template):
        """REST API Gateway named GMeetAgentCrudApi exists with prod stage."""
        template.has_resource_properties(
            "AWS::ApiGateway::RestApi",
            Match.object_like({"Name": "GMeetAgentCrudApi"}),
        )
        template.has_resource_properties(
            "AWS::ApiGateway::Stage",
            Match.object_like({"StageName": "prod"}),
        )

    def test_crud_lambdas_exist(self, template):
        """At least 2 Lambda functions with Python 3.11, 30s timeout, 256MB."""
        resources = template.find_resources(
            "AWS::Lambda::Function",
            {"Properties": {"Runtime": "python3.11", "Timeout": 30, "MemorySize": 256}},
        )
        assert len(resources) >= 2

    def test_dynamodb_crud_iam_policy(self, template):
        """IAM policy grants DynamoDB CRUD actions."""
        template.has_resource_properties(
            "AWS::IAM::Policy",
            Match.object_like({
                "PolicyDocument": {"Statement": Match.array_with([
                    Match.object_like({
                        "Action": [
                            "dynamodb:GetItem", "dynamodb:PutItem",
                            "dynamodb:UpdateItem", "dynamodb:DeleteItem", "dynamodb:Scan",
                        ],
                        "Effect": "Allow",
                    }),
                ])},
            }),
        )


class TestIngestionLambda:
    """Ingestion Lambda configuration and IAM permissions."""

    def test_configuration_and_env_vars(self, template):
        """Ingestion Lambda has Python 3.11, 300s timeout, 512MB, correct env vars."""
        template.has_resource_properties(
            "AWS::Lambda::Function",
            Match.object_like({
                "Runtime": "python3.11",
                "Timeout": 300,
                "MemorySize": 512,
                "Environment": {"Variables": {
                    "OPENSEARCH_ENDPOINT": Match.any_value(),
                    "INDEX_NAME": "knowledge-vectors",
                    "PROJECT_ID": "default-project",
                    "BEDROCK_REGION": "us-east-1",
                }},
            }),
        )

    def test_bedrock_iam_permission(self, template):
        """IAM policy includes bedrock:InvokeModel."""
        template.has_resource_properties(
            "AWS::IAM::Policy",
            Match.object_like({
                "PolicyDocument": {"Statement": Match.array_with([
                    Match.object_like({"Action": "bedrock:InvokeModel", "Effect": "Allow"}),
                ])},
            }),
        )


class TestWebSocketApi:
    """WebSocket API Gateway."""

    def test_websocket_api_exists(self, template):
        """WebSocket API with WEBSOCKET protocol exists."""
        template.has_resource_properties(
            "AWS::ApiGatewayV2::Api",
            Match.object_like({"ProtocolType": "WEBSOCKET"}),
        )


# ------------------------------------------------------------------
# 4. Seed Data
# ------------------------------------------------------------------


class TestSeedLambda:
    """Seed Lambda and custom resource."""

    def test_seed_lambda_runtime_and_env(self, template):
        """Seed Lambda uses python3.11 with TABLE_NAME and PERSONALITIES_TABLE_NAME."""
        template.has_resource_properties(
            "AWS::Lambda::Function",
            Match.object_like({
                "Runtime": "python3.11",
                "Environment": {"Variables": {
                    "TABLE_NAME": Match.any_value(),
                    "PERSONALITIES_TABLE_NAME": Match.any_value(),
                }},
            }),
        )

    def test_seed_lambda_iam_putitem(self, template):
        """Seed Lambda IAM policy grants dynamodb:PutItem."""
        template.has_resource_properties(
            "AWS::IAM::Policy",
            Match.object_like({
                "PolicyDocument": {"Statement": Match.array_with([
                    Match.object_like({"Action": "dynamodb:PutItem", "Effect": "Allow"}),
                ])},
            }),
        )
