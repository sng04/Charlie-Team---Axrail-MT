"""
GMeetAgentStack.

Provisions all GMeet Agent resources in ap-southeast-1, organized into
four logical groups following the deployment-workflow stack dependency order:

1. Shared Resources  — Lambda layers (OpenSearch, Strands)
2. Data Stores       — DynamoDB tables, OpenSearch domain, S3 bucket
3. API Services      — REST API + CRUD Lambdas, WebSocket API + Strands agent
4. Seed Data         — Custom resource that populates initial agent/personality records

TODO(pending-other-developer): Per-project S3 bucket creation is not yet
implemented. Currently all files go to a single shared KB bucket. Once the
Projects table CRUD is complete, each project should have its own S3 bucket
(or key prefix) and the S3 event notifications should be configured
accordingly. The UI upload integration is also pending.
"""

import os

from aws_cdk import (
    CfnOutput,
    Duration,
    Fn,
    RemovalPolicy,
    Stack,
    aws_apigateway as apigw,
    aws_apigatewayv2 as apigwv2,
    aws_dynamodb as dynamodb,
    aws_ec2 as ec2,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_opensearchservice as opensearch,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    custom_resources as cr,
    CustomResource,
)
from constructs import Construct


SEED_HANDLER_CODE = """\
import json
import os
import uuid

import boto3

TABLE_NAME = os.environ["TABLE_NAME"]
PERSONALITIES_TABLE_NAME = os.environ["PERSONALITIES_TABLE_NAME"]

dynamodb = boto3.resource("dynamodb")
agents_table = dynamodb.Table(TABLE_NAME)
personalities_table = dynamodb.Table(PERSONALITIES_TABLE_NAME)

NAMESPACE = uuid.UUID("a1b2c3d4-e5f6-7890-abcd-ef1234567890")

PERSONALITIES = [
    {
        "personality_id": str(uuid.uuid5(NAMESPACE, "casual")),
        "personality_name": "casual",
        "personality_prompt": (
            "Use relaxed, conversational language. Use contractions, "
            "informal phrasing, and a friendly tone. Keep things "
            "approachable and easy to read."
        ),
    },
    {
        "personality_id": str(uuid.uuid5(NAMESPACE, "concise")),
        "personality_name": "concise",
        "personality_prompt": (
            "Use minimal words. Prefer short sentences and bullet points. "
            "Omit filler words. Get straight to the point."
        ),
    },
    {
        "personality_id": str(uuid.uuid5(NAMESPACE, "professional")),
        "personality_name": "professional",
        "personality_prompt": (
            "Use formal, structured language. Write in complete sentences "
            "with proper terminology. Maintain a polished, "
            "business-appropriate tone."
        ),
    },
]

PERSONALITY_MAP = {p["personality_name"]: p["personality_id"] for p in PERSONALITIES}

AGENTS = [
    {
        "agent_id": str(uuid.uuid5(NAMESPACE, "live_transcription")),
        "agent_name": "Live Transcription Agent",
        "role_prompt": (
            "You are an AI Meeting Agent designed for live meeting "
            "transcription. You monitor ongoing conversations in real time "
            "and maintain awareness of the discussion context."
        ),
        "task_prompt": (
            "1. Detect questions raised by meeting participants.\\n"
            "2. Query relevant knowledge bases for accurate answers.\\n"
            "3. Generate clear responses without disrupting the meeting.\\n"
            "4. Track action items, decisions, and key discussion points.\\n"
            "5. Provide summaries when requested."
        ),
        "personality_id": PERSONALITY_MAP["professional"],
        "model_id": "amazon.nova-pro-v1:0",
        "use_case": "live_meeting_transcription",
    },
    {
        "agent_id": str(uuid.uuid5(NAMESPACE, "meeting_qa")),
        "agent_name": "Q&A Assistant Agent",
        "role_prompt": (
            "You are an AI Meeting Q&A Assistant. You help meeting "
            "participants get quick, accurate answers to questions raised "
            "during discussions."
        ),
        "task_prompt": (
            "1. Listen for questions from participants.\\n"
            "2. Search the knowledge base for relevant information.\\n"
            "3. Provide accurate, referenced answers.\\n"
            "4. Flag low-confidence answers for verification."
        ),
        "personality_id": PERSONALITY_MAP["concise"],
        "model_id": "amazon.nova-pro-v1:0",
        "use_case": "meeting_qa",
    },
    {
        "agent_id": str(uuid.uuid5(NAMESPACE, "meeting_summary")),
        "agent_name": "Meeting Summary Agent",
        "role_prompt": (
            "You are an AI Meeting Summarizer. You create helpful "
            "summaries of meetings, capturing the key points so "
            "participants can review them later."
        ),
        "task_prompt": (
            "1. Generate meeting summaries after discussions.\\n"
            "2. Track action items and owners.\\n"
            "3. Highlight decisions made during the meeting.\\n"
            "4. Note unresolved questions and follow-ups."
        ),
        "personality_id": PERSONALITY_MAP["casual"],
        "model_id": "amazon.nova-pro-v1:0",
        "use_case": "meeting_summary",
    },
]


def lambda_handler(event, context):
    request_type = event.get("RequestType", "")
    physical_id = event.get("PhysicalResourceId", str(uuid.uuid4()))

    if request_type in ("Create", "Update"):
        for personality in PERSONALITIES:
            personalities_table.put_item(Item=personality)

        for agent in AGENTS:
            agents_table.put_item(Item=agent)

        physical_id = "seed-complete"

    return {"PhysicalResourceId": physical_id}
"""


class GMeetAgentStack(Stack):
    """CDK stack for all GMeet Agent resources in ap-southeast-1."""

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. Shared resources (Lambda layers)
        self._create_shared_resources()

        # 2. Data stores (DynamoDB, OpenSearch, S3)
        self._create_data_stores()

        # 3. API services (REST API, WebSocket API, Lambdas)
        self._create_api_services()

        # 4. Seed data (custom resource for initial records)
        self._create_seed_data()

    # ==================================================================
    # 1. Shared Resources — Lambda layers
    # ==================================================================

    def _create_shared_resources(self) -> None:
        """Create reusable Lambda layers."""
        self._create_opensearch_layer()
        self._create_strands_layer()
        self._create_shared_layer()
        self._create_pypdf2_layer()
        self._create_powertools_layer()

    def _create_opensearch_layer(self) -> None:
        """Lambda layer with opensearch-py and requests-aws4auth."""
        layers_path = os.path.join(
            os.path.dirname(__file__), "..", "layers", "opensearch"
        )
        self.opensearch_layer = _lambda.LayerVersion(
            self,
            "OpenSearchLayer",
            code=_lambda.Code.from_asset(layers_path),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="opensearch-py and requests-aws4auth for OpenSearch access",
        )

    def _create_strands_layer(self) -> None:
        """Lambda layer with the Strands Agents SDK."""
        layers_path = os.path.join(
            os.path.dirname(__file__), "..", "layers", "strands"
        )
        self.strands_layer = _lambda.LayerVersion(
            self,
            "StrandsLayer",
            code=_lambda.Code.from_asset(layers_path),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="Strands Agents SDK and dependencies",
        )

    def _create_shared_layer(self) -> None:
        """Lambda layer with shared response_utils and custom_exceptions."""
        layers_path = os.path.join(
            os.path.dirname(__file__), "..", "layers", "shared"
        )
        self.shared_layer = _lambda.LayerVersion(
            self,
            "SharedUtilsLayer",
            code=_lambda.Code.from_asset(layers_path),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="Shared response utilities and custom exceptions",
        )

    def _create_pypdf2_layer(self) -> None:
        """Lambda layer with PyPDF2 for PDF text extraction."""
        layers_path = os.path.join(
            os.path.dirname(__file__), "..", "layers", "pypdf2"
        )
        self.pypdf2_layer = _lambda.LayerVersion(
            self,
            "PyPDF2Layer",
            code=_lambda.Code.from_asset(layers_path),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="PyPDF2 library for PDF text extraction",
        )

    def _create_powertools_layer(self) -> None:
        """Lambda layer with AWS Lambda Powertools for Python."""
        layers_path = os.path.join(
            os.path.dirname(__file__), "..", "layers", "powertools"
        )
        self.powertools_layer = _lambda.LayerVersion(
            self,
            "PowertoolsLayer",
            code=_lambda.Code.from_asset(layers_path),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="AWS Lambda Powertools for Python with tracer",
        )

    # ==================================================================
    # 2. Data Stores — DynamoDB tables, OpenSearch domain, S3 bucket
    # ==================================================================

    def _create_data_stores(self) -> None:
        """Create all persistent data stores."""
        self._create_dynamodb_tables()
        self._create_opensearch_domain()
        self._create_kb_bucket()

    def _create_dynamodb_tables(self) -> None:
        """Create the five DynamoDB tables with GSIs."""
        self.agents_table = dynamodb.Table(
            self,
            "AgentsTable",
            partition_key=dynamodb.Attribute(
                name="agent_id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )

        self.projects_table = dynamodb.Table(
            self,
            "ProjectsTable",
            partition_key=dynamodb.Attribute(
                name="project_id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )

        self.sessions_table = dynamodb.Table(
            self,
            "SessionsTable",
            partition_key=dynamodb.Attribute(
                name="session_id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )
        self.sessions_table.add_global_secondary_index(
            index_name="project-index",
            partition_key=dynamodb.Attribute(
                name="project_id", type=dynamodb.AttributeType.STRING
            ),
        )
        self.sessions_table.add_global_secondary_index(
            index_name="active-sessions-index",
            partition_key=dynamodb.Attribute(
                name="is_active", type=dynamodb.AttributeType.STRING
            ),
        )

        self.transcripts_table = dynamodb.Table(
            self,
            "TranscriptsTable",
            partition_key=dynamodb.Attribute(
                name="transcript_id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )
        self.transcripts_table.add_global_secondary_index(
            index_name="session-index",
            partition_key=dynamodb.Attribute(
                name="session_id", type=dynamodb.AttributeType.STRING
            ),
        )

        self.personalities_table = dynamodb.Table(
            self,
            "PersonalitiesTable",
            partition_key=dynamodb.Attribute(
                name="personality_id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )

        self.qa_pairs_table = dynamodb.Table(
            self,
            "QAPairsTable",
            partition_key=dynamodb.Attribute(
                name="qa_pair_id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )
        self.qa_pairs_table.add_global_secondary_index(
            index_name="session-index",
            partition_key=dynamodb.Attribute(
                name="session_id", type=dynamodb.AttributeType.STRING
            ),
        )
        self.qa_pairs_table.add_global_secondary_index(
            index_name="project-index",
            partition_key=dynamodb.Attribute(
                name="project_id", type=dynamodb.AttributeType.STRING
            ),
        )

        self.suggested_questions_table = dynamodb.Table(
            self,
            "SuggestedQuestionsTable",
            partition_key=dynamodb.Attribute(
                name="question_id", type=dynamodb.AttributeType.STRING
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )
        self.suggested_questions_table.add_global_secondary_index(
            index_name="session-index",
            partition_key=dynamodb.Attribute(
                name="session_id", type=dynamodb.AttributeType.STRING
            ),
        )

    def _create_opensearch_domain(self) -> None:
        """Create the OpenSearch Service domain for vector storage."""
        self.opensearch_domain = opensearch.Domain(
            self,
            "KbVectorsDomain",
            domain_name="gmeet-kb-vectors",
            version=opensearch.EngineVersion.OPENSEARCH_2_11,
            capacity=opensearch.CapacityConfig(
                data_node_instance_type="t3.small.search",
                data_nodes=1,
                multi_az_with_standby_enabled=False,
            ),
            ebs=opensearch.EbsOptions(
                enabled=True,
                volume_size=20,
                volume_type=ec2.EbsDeviceVolumeType.GP3,
            ),
            removal_policy=RemovalPolicy.DESTROY,
        )

    def _create_kb_bucket(self) -> None:
        """Create the S3 bucket for knowledge base documents."""
        self.kb_bucket = s3.Bucket(
            self,
            "KnowledgeBaseBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

    # ==================================================================
    # 3. API Services — REST API, CRUD Lambdas, KB pipeline,
    #                   Strands agent, WebSocket API
    # ==================================================================

    def _create_api_services(self) -> None:
        """Create all API-facing resources and their Lambdas."""
        self._create_rest_api()
        self._create_ingestion_lambda()
        self._create_deletion_lambda()
        self._create_strands_agent_lambda()
        self._create_gap_scheduler()
        self._create_websocket_api()

    def _create_rest_api(self) -> None:
        """Create the REST API Gateway with CRUD Lambda integrations."""
        self.rest_api = apigw.RestApi(
            self,
            "GMeetAgentCrudApi",
            rest_api_name="GMeetAgentCrudApi",
            deploy_options=apigw.StageOptions(stage_name="prod"),
            default_cors_preflight_options=apigw.CorsOptions(
                allow_origins=apigw.Cors.ALL_ORIGINS,
                allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                allow_headers=["Content-Type", "Authorization"],
            ),
        )

        # --- Agents Handler ---
        self.agents_handler = _lambda.Function(
            self,
            "AgentsHandler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda/AgentsCrud"),
            timeout=Duration.seconds(30),
            memory_size=256,
            layers=[self.shared_layer, self.powertools_layer],
            tracing=_lambda.Tracing.ACTIVE,
            environment={
                "AGENTS_TABLE_NAME": self.agents_table.table_name,
                "PERSONALITIES_TABLE_NAME": self.personalities_table.table_name,
            },
        )
        self.agents_handler.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:UpdateItem",
                    "dynamodb:DeleteItem",
                    "dynamodb:Scan",
                ],
                resources=[self.agents_table.table_arn],
            )
        )
        self.agents_handler.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:GetItem"],
                resources=[self.personalities_table.table_arn],
            )
        )

        # --- Personalities Handler ---
        self.personalities_handler = _lambda.Function(
            self,
            "PersonalitiesHandler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda/PersonalitiesCrud"),
            timeout=Duration.seconds(30),
            memory_size=256,
            layers=[self.shared_layer, self.powertools_layer],
            tracing=_lambda.Tracing.ACTIVE,
            environment={
                "PERSONALITIES_TABLE_NAME": self.personalities_table.table_name,
                "AGENTS_TABLE_NAME": self.agents_table.table_name,
            },
        )
        self.personalities_handler.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:UpdateItem",
                    "dynamodb:DeleteItem",
                    "dynamodb:Scan",
                ],
                resources=[self.personalities_table.table_arn],
            )
        )
        self.personalities_handler.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:Scan"],
                resources=[self.agents_table.table_arn],
            )
        )

        # --- QA Pairs Handler ---
        self.qa_pairs_handler = _lambda.Function(
            self,
            "QAPairsHandler",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda/QAPairsCrud"),
            timeout=Duration.seconds(30),
            memory_size=256,
            layers=[self.shared_layer, self.powertools_layer],
            tracing=_lambda.Tracing.ACTIVE,
            environment={
                "QA_PAIRS_TABLE_NAME": self.qa_pairs_table.table_name,
            },
        )
        self.qa_pairs_handler.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:GetItem", "dynamodb:DeleteItem"],
                resources=[self.qa_pairs_table.table_arn],
            )
        )
        self.qa_pairs_handler.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:Query"],
                resources=[
                    self.qa_pairs_table.table_arn + "/index/session-index",
                    self.qa_pairs_table.table_arn + "/index/project-index",
                ],
            )
        )

        # --- Route integrations ---
        agents_integration = apigw.LambdaIntegration(self.agents_handler)
        personalities_integration = apigw.LambdaIntegration(
            self.personalities_handler
        )
        qa_pairs_integration = apigw.LambdaIntegration(self.qa_pairs_handler)

        agents_resource = self.rest_api.root.add_resource("agents")
        agents_resource.add_method("GET", agents_integration)
        agents_resource.add_method("POST", agents_integration)

        agent_id_resource = agents_resource.add_resource("{agentId}")
        agent_id_resource.add_method("GET", agents_integration)
        agent_id_resource.add_method("PUT", agents_integration)
        agent_id_resource.add_method("DELETE", agents_integration)

        personalities_resource = self.rest_api.root.add_resource("personalities")
        personalities_resource.add_method("GET", personalities_integration)
        personalities_resource.add_method("POST", personalities_integration)

        personality_id_resource = personalities_resource.add_resource(
            "{personalityId}"
        )
        personality_id_resource.add_method("GET", personalities_integration)
        personality_id_resource.add_method("PUT", personalities_integration)
        personality_id_resource.add_method("DELETE", personalities_integration)

        qa_pairs_resource = self.rest_api.root.add_resource("qa-pairs")
        qa_pairs_resource.add_method("GET", qa_pairs_integration)

        qa_pair_id_resource = qa_pairs_resource.add_resource("{qaPairId}")
        qa_pair_id_resource.add_method("GET", qa_pairs_integration)
        qa_pair_id_resource.add_method("DELETE", qa_pairs_integration)

        CfnOutput(
            self,
            "RestApiUrl",
            value=self.rest_api.url,
            description="REST API Gateway endpoint URL",
        )

    def _create_ingestion_lambda(self) -> None:
        """Create the ingestion Lambda and wire S3 OBJECT_CREATED notification."""
        self.ingestion_function = _lambda.Function(
            self,
            "IngestionFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda/Ingestion"),
            timeout=Duration.seconds(300),
            memory_size=512,
            layers=[self.opensearch_layer, self.pypdf2_layer, self.powertools_layer],
            tracing=_lambda.Tracing.ACTIVE,
            environment={
                "OPENSEARCH_ENDPOINT": self.opensearch_domain.domain_endpoint,
                "INDEX_NAME": "knowledge-vectors",
                "PROJECT_ID": "default-project",
                "BEDROCK_REGION": "us-east-1",
            },
        )
        self.ingestion_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["bedrock:InvokeModel"],
                resources=[
                    "arn:aws:bedrock:us-east-1::foundation-model/"
                    "amazon.titan-embed-text-v2:0"
                ],
            )
        )
        self.ingestion_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "es:ESHttpPost",
                    "es:ESHttpPut",
                    "es:ESHttpGet",
                    "es:ESHttpHead",
                ],
                resources=[self.opensearch_domain.domain_arn + "/*"],
            )
        )
        self.kb_bucket.grant_read(self.ingestion_function)
        self.kb_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(self.ingestion_function),
            s3.NotificationKeyFilter(suffix=".pdf"),
        )
        self.kb_bucket.add_event_notification(
            s3.EventType.OBJECT_CREATED,
            s3n.LambdaDestination(self.ingestion_function),
            s3.NotificationKeyFilter(suffix=".md"),
        )

    def _create_deletion_lambda(self) -> None:
        """Create the deletion Lambda and wire S3 OBJECT_REMOVED notification."""
        self.deletion_function = _lambda.Function(
            self,
            "DeletionFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda/Deletion"),
            timeout=Duration.seconds(60),
            memory_size=256,
            layers=[self.opensearch_layer, self.powertools_layer],
            tracing=_lambda.Tracing.ACTIVE,
            environment={
                "OPENSEARCH_ENDPOINT": self.opensearch_domain.domain_endpoint,
                "INDEX_NAME": "knowledge-vectors",
            },
        )
        self.deletion_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["es:ESHttpGet", "es:ESHttpPost", "es:ESHttpDelete"],
                resources=[self.opensearch_domain.domain_arn + "/*"],
            )
        )
        self.kb_bucket.grant_read(self.deletion_function)
        self.kb_bucket.add_event_notification(
            s3.EventType.OBJECT_REMOVED,
            s3n.LambdaDestination(self.deletion_function),
            s3.NotificationKeyFilter(suffix=".pdf"),
        )
        self.kb_bucket.add_event_notification(
            s3.EventType.OBJECT_REMOVED,
            s3n.LambdaDestination(self.deletion_function),
            s3.NotificationKeyFilter(suffix=".md"),
        )

    def _create_strands_agent_lambda(self) -> None:
        """Create the Strands agent Lambda with tools and permissions."""
        self.agent_function = _lambda.Function(
            self,
            "StrandsAgentFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda/StrandsAgent"),
            timeout=Duration.seconds(120),
            memory_size=512,
            layers=[self.strands_layer, self.opensearch_layer, self.powertools_layer],
            tracing=_lambda.Tracing.ACTIVE,
            environment={
                "AGENTS_TABLE_NAME": self.agents_table.table_name,
                "PERSONALITIES_TABLE_NAME": self.personalities_table.table_name,
                "TRANSCRIPTS_TABLE_NAME": self.transcripts_table.table_name,
                "SESSIONS_TABLE_NAME": self.sessions_table.table_name,
                "QA_PAIRS_TABLE_NAME": self.qa_pairs_table.table_name,
                "KB_BUCKET_NAME": self.kb_bucket.bucket_name,
                "SUGGESTED_QUESTIONS_TABLE_NAME": self.suggested_questions_table.table_name,
                "OPENSEARCH_ENDPOINT": self.opensearch_domain.domain_endpoint,
                "INDEX_NAME": "knowledge-vectors",
                "BEDROCK_REGION": "us-east-1",
                "WEBSOCKET_ENDPOINT": "",  # Updated after WS API creation
            },
        )
        self.agent_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "bedrock:InvokeModelWithResponseStream",
                    "bedrock:InvokeModel",
                ],
                resources=[
                    "arn:aws:bedrock:us-east-1::foundation-model/"
                    "amazon.nova-pro-v1:0",
                    "arn:aws:bedrock:us-east-1::foundation-model/"
                    "amazon.titan-embed-text-v2:0",
                ],
            )
        )
        self.agent_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:GetItem"],
                resources=[
                    self.agents_table.table_arn,
                    self.personalities_table.table_arn,
                    self.sessions_table.table_arn,
                ],
            )
        )
        self.agent_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:UpdateItem"],
                resources=[self.sessions_table.table_arn],
            )
        )
        self.agent_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:Query"],
                resources=[
                    self.transcripts_table.table_arn,
                    self.transcripts_table.table_arn + "/index/session-index",
                ],
            )
        )
        self.agent_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:BatchWriteItem", "dynamodb:PutItem"],
                resources=[self.transcripts_table.table_arn],
            )
        )
        self.agent_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:GetItem", "dynamodb:PutItem"],
                resources=[self.qa_pairs_table.table_arn],
            )
        )
        self.agent_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["es:ESHttpGet", "es:ESHttpPost"],
                resources=[self.opensearch_domain.domain_arn + "/*"],
            )
        )
        self.kb_bucket.grant_put(self.agent_function)
        self.kb_bucket.grant_read(self.agent_function)
        self.agent_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:Query"],
                resources=[
                    self.qa_pairs_table.table_arn + "/index/session-index",
                ],
            )
        )
        self.agent_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:UpdateItem",
                    "dynamodb:Query",
                ],
                resources=[
                    self.suggested_questions_table.table_arn,
                    self.suggested_questions_table.table_arn + "/index/session-index",
                ],
            )
        )

    def _create_gap_scheduler(self) -> None:
        """Create the Gap Scheduler Lambda and EventBridge rule."""
        self.gap_scheduler_function = _lambda.Function(
            self,
            "GapSchedulerFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda/GapScheduler"),
            timeout=Duration.seconds(60),
            memory_size=256,
            layers=[self.powertools_layer],
            tracing=_lambda.Tracing.ACTIVE,
            environment={
                "SESSIONS_TABLE_NAME": self.sessions_table.table_name,
                "AGENT_FUNCTION_NAME": self.agent_function.function_name,
                "ACTIVE_SESSIONS_INDEX_NAME": "active-sessions-index",
            },
        )
        self.gap_scheduler_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:Query"],
                resources=[
                    self.sessions_table.table_arn,
                    self.sessions_table.table_arn + "/index/active-sessions-index",
                ],
            )
        )
        self.gap_scheduler_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:UpdateItem"],
                resources=[self.sessions_table.table_arn],
            )
        )
        self.gap_scheduler_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["lambda:InvokeFunction"],
                resources=[self.agent_function.function_arn],
            )
        )

        gap_analysis_rule = events.Rule(
            self,
            "GapAnalysisScheduleRule",
            schedule=events.Schedule.rate(Duration.minutes(2)),
            description="Triggers gap analysis for active meeting sessions",
        )
        gap_analysis_rule.add_target(
            targets.LambdaFunction(self.gap_scheduler_function)
        )

    def _create_websocket_api(self) -> None:
        """Create the WebSocket API with routes and Lambda integration."""
        self.ws_api = apigwv2.CfnApi(
            self,
            "AgentWebSocketApi",
            name="GMeetAgentWebSocket",
            protocol_type="WEBSOCKET",
            route_selection_expression="$request.body.action",
        )

        integration = apigwv2.CfnIntegration(
            self,
            "AgentLambdaIntegration",
            api_id=self.ws_api.ref,
            integration_type="AWS_PROXY",
            integration_uri=Fn.join(
                "",
                [
                    "arn:aws:apigateway:",
                    self.region,
                    ":lambda:path/2015-03-31/functions/",
                    self.agent_function.function_arn,
                    "/invocations",
                ],
            ),
        )

        for route_key in [
            "$connect", "$disconnect", "sendMessage",
            "detectQuestion", "extractQAPair", "analyzeGaps",
            "endMeeting", "retroAnalysis", "retroChat",
            "processTranscript", "setSuggestedQuestions", "$default",
        ]:
            route_id = route_key.replace("$", "").capitalize() or "Default"
            apigwv2.CfnRoute(
                self,
                f"Route{route_id}",
                api_id=self.ws_api.ref,
                route_key=route_key,
                target=Fn.join("/", ["integrations", integration.ref]),
            )

        apigwv2.CfnStage(
            self,
            "ProductionStage",
            api_id=self.ws_api.ref,
            stage_name="production",
            auto_deploy=True,
        )

        self.agent_function.add_permission(
            "WebSocketInvokePermission",
            principal=iam.ServicePrincipal("apigateway.amazonaws.com"),
            source_arn=Fn.join(
                "",
                [
                    "arn:aws:execute-api:",
                    self.region,
                    ":",
                    self.account,
                    ":",
                    self.ws_api.ref,
                    "/*",
                ],
            ),
        )

        self.agent_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["execute-api:ManageConnections"],
                resources=[
                    Fn.join(
                        "",
                        [
                            "arn:aws:execute-api:",
                            self.region,
                            ":",
                            self.account,
                            ":",
                            self.ws_api.ref,
                            "/production/*",
                        ],
                    ),
                ],
            )
        )

        ws_endpoint = Fn.join(
            "",
            [
                self.ws_api.ref,
                ".execute-api.",
                self.region,
                ".amazonaws.com/production",
            ],
        )
        cfn_function = self.agent_function.node.default_child
        cfn_function.add_property_override(
            "Environment.Variables.WEBSOCKET_ENDPOINT",
            ws_endpoint,
        )

        CfnOutput(
            self,
            "WebSocketUrl",
            value=Fn.join("", ["wss://", ws_endpoint]),
            description="WebSocket API endpoint URL",
        )

    # ==================================================================
    # 4. Seed Data — Custom resource for initial agent/personality records
    # ==================================================================

    def _create_seed_data(self) -> None:
        """Create the seed Lambda and custom resource."""
        self.seed_function = _lambda.Function(
            self,
            "SeedAgentsFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.lambda_handler",
            code=_lambda.Code.from_inline(SEED_HANDLER_CODE),
            environment={
                "TABLE_NAME": self.agents_table.table_name,
                "PERSONALITIES_TABLE_NAME": self.personalities_table.table_name,
            },
        )
        self.seed_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:PutItem"],
                resources=[
                    self.agents_table.table_arn,
                    self.personalities_table.table_arn,
                ],
            )
        )

        provider = cr.Provider(
            self,
            "SeedProvider",
            on_event_handler=self.seed_function,
        )
        CustomResource(
            self,
            "SeedAgentsResource",
            service_token=provider.service_token,
        )
