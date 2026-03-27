from aws_cdk import (
    Stack,
    Duration,
    RemovalPolicy,
    CustomResource,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_events as events,
    aws_events_targets as targets,
    aws_s3 as s3,
    aws_apigatewayv2 as apigwv2,
    custom_resources as cr,
    CfnOutput,
)
from constructs import Construct

from stack_cdk.dynamodb_stack import DynamoDBStack
from stack_cdk.cognito_stack import CognitoStack
from stack_cdk.meeting_bot_stack import MeetingBotStack


class LambdaStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        env_name: str,
        dynamodb_stack: DynamoDBStack,
        cognito_stack: CognitoStack,
        meeting_bot_stack: MeetingBotStack,
        admin_email: str,
        admin_temp_password: str,
        env_config: dict = None,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.env_name = env_name
        self.env_config = env_config or {}
        self.dynamodb_stack = dynamodb_stack
        self.cognito_stack = cognito_stack
        self.meeting_bot_stack = meeting_bot_stack
        self.admin_email = admin_email
        self.admin_temp_password = admin_temp_password

        self._create_lambda_layers()
        self._create_lambda_role()
        self._grant_dynamodb_permissions()
        self._grant_cognito_permissions()
        self._grant_ecs_permissions()
        self._grant_sqs_permissions()
        self._grant_secrets_permissions()
        self._grant_cloudformation_permissions()
        self._grant_eventbridge_permissions()
        self._create_lambda_functions()
        self._create_d2_lambda_functions()
        self._grant_opensearch_permissions()
        self._grant_bedrock_permissions()
        self._grant_d2_dynamodb_permissions()
        self._grant_websocket_management_permissions()
        self._create_s3_buckets()
        self._create_websocket_api()
        self._create_ecs_task_state_handler()
        self._create_gap_scheduler_rule()
        self._create_bot_credential_validation_worker()
        self._create_seed_admin()
        self._create_seed_agent_data()
        self._create_exports()

    def _create_lambda_layers(self) -> None:
        """Create Lambda layers for shared code.

        Layer ARNs are stored in SSM Parameter Store so that other stacks
        (e.g. ApiServicesStack) can look them up without creating fragile
        CloudFormation cross-stack exports.  Direct construct references
        across stacks cause UPDATE_ROLLBACK when the layer content changes.
        """
        self.shared_layer = _lambda.LayerVersion(
            self,
            "SharedLayer",
            layer_version_name=f"AXRAIL-SharedLayer-{self.env_name}",
            code=_lambda.Code.from_asset("lambdas/Layers/SharedLayer"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="Shared utilities for Lambda functions",
        )

        self.powertools_layer = _lambda.LayerVersion(
            self,
            "PowertoolsLayer",
            layer_version_name=f"AXRAIL-PowertoolsLayer-{self.env_name}",
            code=_lambda.Code.from_asset("lambdas/Layers/PowertoolsLayer"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="AWS Lambda Powertools for logging and tracing",
        )

        # Publish layer ARNs to SSM so dependent stacks can import them
        # without CloudFormation cross-stack exports.
        from aws_cdk import aws_ssm as ssm

        ssm.StringParameter(
            self,
            "SharedLayerArnParam",
            parameter_name=f"/axrail/{self.env_name}/shared-layer-arn",
            string_value=self.shared_layer.layer_version_arn,
            description="SharedLayer ARN for cross-stack lookup",
        )
        ssm.StringParameter(
            self,
            "PowertoolsLayerArnParam",
            parameter_name=f"/axrail/{self.env_name}/powertools-layer-arn",
            string_value=self.powertools_layer.layer_version_arn,
            description="PowertoolsLayer ARN for cross-stack lookup",
        )

        self.opensearch_layer = _lambda.LayerVersion(
            self,
            "OpenSearchLayer",
            layer_version_name=f"AXRAIL-OpenSearchLayer-{self.env_name}",
            code=_lambda.Code.from_asset("lambdas/Layers/OpenSearchLayer"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="opensearch-py and requests-aws4auth",
        )

        self.strands_layer = _lambda.LayerVersion(
            self,
            "StrandsLayer",
            layer_version_name=f"AXRAIL-StrandsLayer-{self.env_name}",
            code=_lambda.Code.from_asset("lambdas/Layers/StrandsLayer"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="Strands Agents SDK",
        )

        self.pypdf2_layer = _lambda.LayerVersion(
            self,
            "PyPDF2Layer",
            layer_version_name=f"AXRAIL-PyPDF2Layer-{self.env_name}",
            code=_lambda.Code.from_asset("lambdas/Layers/PyPDF2Layer"),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_11],
            description="PyPDF2 for PDF text extraction",
        )

    def _create_lambda_role(self) -> None:
        """Create Lambda execution role with basic permissions."""
        self.lambda_role = iam.Role(
            self,
            "LambdaRole",
            role_name=f"AXRAIL-LambdaRole-{self.env_name}",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AWSXRayDaemonWriteAccess"),
            ],
        )

    def _grant_dynamodb_permissions(self) -> None:
        """Grant DynamoDB permissions using CDK grant methods for least privilege."""
        self.dynamodb_stack.users_table.grant_read_write_data(self.lambda_role)
        self.dynamodb_stack.projects_table.grant_read_write_data(self.lambda_role)
        self.dynamodb_stack.project_users_table.grant_read_write_data(self.lambda_role)
        self.dynamodb_stack.sessions_table.grant_read_write_data(self.lambda_role)
        self.dynamodb_stack.transcripts_table.grant_read_write_data(self.lambda_role)
        self.dynamodb_stack.bot_credentials_table.grant_read_write_data(self.lambda_role)
        self.dynamodb_stack.bot_pool_table.grant_read_write_data(self.lambda_role)

    def _grant_cognito_permissions(self) -> None:
        """Grant Cognito permissions with specific User Pool ARN."""
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "cognito-idp:InitiateAuth",
                    "cognito-idp:RespondToAuthChallenge",
                    "cognito-idp:GetUser",
                    "cognito-idp:AdminCreateUser",
                    "cognito-idp:AdminAddUserToGroup",
                    "cognito-idp:AdminListGroupsForUser",
                    "cognito-idp:GlobalSignOut",
                    "cognito-idp:AdminDeleteUser",
                    "cognito-idp:AdminUpdateUserAttributes",
                ],
                resources=[self.cognito_stack.user_pool.user_pool_arn],
            )
        )

    def _grant_ecs_permissions(self) -> None:
        """Grant ECS permissions for starting/stopping meeting bot tasks."""
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "ecs:RunTask",
                    "ecs:StopTask",
                    "ecs:DescribeTasks",
                ],
                resources=[
                    self.meeting_bot_stack.task_definition_arn,
                    f"arn:aws:ecs:{self.region}:{self.account}:task/{self.meeting_bot_stack.cluster.cluster_name}/*",
                ],
            )
        )

        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["ecs:ListTasks"],
                resources=["*"],
                conditions={
                    "ArnEquals": {
                        "ecs:cluster": self.meeting_bot_stack.cluster.cluster_arn
                    }
                },
            )
        )
        
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["iam:PassRole"],
                resources=["*"],
                conditions={
                    "StringLike": {
                        "iam:PassedToService": "ecs-tasks.amazonaws.com"
                    }
                },
            )
        )

    def _grant_sqs_permissions(self) -> None:
        """Grant SQS permissions for warm pool queue."""
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "sqs:SendMessage",
                    "sqs:GetQueueAttributes",
                ],
                resources=[self.meeting_bot_stack.meeting_queue_arn],
            )
        )

    def _grant_secrets_permissions(self) -> None:
        """Grant Secrets Manager permissions to Lambda role."""
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "secretsmanager:CreateSecret",
                    "secretsmanager:PutSecretValue",
                    "secretsmanager:GetSecretValue",
                    "secretsmanager:DeleteSecret",
                ],
                resources=[
                    f"arn:aws:secretsmanager:{self.region}:{self.account}:secret:{self.env_name}/bot-credentials/*"
                ],
            )
        )

    def _grant_cloudformation_permissions(self) -> None:
        """Grant CloudFormation permissions to read exports."""
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["cloudformation:ListExports"],
                resources=["*"],
            )
        )

    def _grant_eventbridge_permissions(self) -> None:
        """Grant EventBridge permissions to publish events."""
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["events:PutEvents"],
                resources=[f"arn:aws:events:{self.region}:{self.account}:event-bus/default"],
            )
        )

    def _get_lambda_environment(self) -> dict:
        return {
            "USER_POOL_ID": self.cognito_stack.user_pool.user_pool_id,
            "CLIENT_ID": self.cognito_stack.user_pool_client.user_pool_client_id,
            "DYNAMODB_TABLE": self.dynamodb_stack.users_table.table_name,
            "USERS_TABLE": self.dynamodb_stack.users_table.table_name,
            "PROJECTS_TABLE": self.dynamodb_stack.projects_table.table_name,
            "PROJECT_USERS_TABLE": self.dynamodb_stack.project_users_table.table_name,
            "SESSIONS_TABLE": self.dynamodb_stack.sessions_table.table_name,
            "TRANSCRIPTS_TABLE": self.dynamodb_stack.transcripts_table.table_name,
            "BOT_CREDENTIALS_TABLE": self.dynamodb_stack.bot_credentials_table.table_name,
            "ECS_CLUSTER": self.meeting_bot_stack.cluster_arn,
            "ECS_TASK_DEFINITION": self.meeting_bot_stack.task_definition_arn,
            "ECS_SUBNETS": ",".join(self.meeting_bot_stack.private_subnet_ids),
            "ECS_SECURITY_GROUP": self.meeting_bot_stack.security_group_id,
            "SQS_QUEUE_URL": self.meeting_bot_stack.meeting_queue_url,
            "BOT_POOL_TABLE": self.dynamodb_stack.bot_pool_table.table_name,
            "WARM_POOL_ENABLED": "true",
            "ENVIRONMENT": self.env_name,
            "POWERTOOLS_SERVICE_NAME": "axrail-api",
            "LOG_LEVEL": "INFO",
            # D2 table names
            "AGENTS_TABLE_NAME": self.dynamodb_stack.agents_table.table_name,
            "PERSONALITIES_TABLE_NAME": self.dynamodb_stack.personalities_table.table_name,
            "QA_PAIRS_TABLE_NAME": self.dynamodb_stack.qa_pairs_table.table_name,
            "SUGGESTED_QUESTIONS_TABLE_NAME": self.dynamodb_stack.suggested_questions_table.table_name,
            "SKILLS_TABLE_NAME": self.dynamodb_stack.skills_table.table_name,
            "SESSIONS_TABLE_NAME": self.dynamodb_stack.sessions_table.table_name,
            "TRANSCRIPTS_TABLE_NAME": self.dynamodb_stack.transcripts_table.table_name,
            "GAP_ANALYSIS_TABLE_NAME": self.dynamodb_stack.gap_analysis_results_table.table_name,
            "AGENT_SKILLS_TABLE_NAME": self.dynamodb_stack.agent_skills_table.table_name,
        }

    def _create_lambda_function(
        self, function_name: str, handler_path: str, timeout: int = 30,
        memory_size: int = 256, layers: list = None, environment: dict = None,
    ) -> _lambda.Function:
        return _lambda.Function(
            self,
            function_name,
            function_name=f"AXRAIL-{function_name}-{self.env_name}",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset(handler_path),
            role=self.lambda_role,
            layers=layers if layers is not None else [
                self.shared_layer,
                self.powertools_layer,
            ],
            environment=environment if environment is not None else self._get_lambda_environment(),
            timeout=Duration.seconds(timeout),
            memory_size=memory_size,
            tracing=_lambda.Tracing.ACTIVE,
        )

    def _create_lambda_functions(self) -> None:
        # Auth functions
        self.admin_login_fn = self._create_lambda_function(
            "AdminLogin", "lambdas/Functions/AdminLogin"
        )

        self.user_login_fn = self._create_lambda_function(
            "UserLogin", "lambdas/Functions/UserLogin"
        )

        self.create_user_fn = self._create_lambda_function(
            "CreateUser", "lambdas/Functions/CreateUser"
        )

        self.change_password_fn = self._create_lambda_function(
            "ChangePassword", "lambdas/Functions/ChangePassword"
        )

        self.logout_fn = self._create_lambda_function(
            "Logout", "lambdas/Functions/Logout"
        )

        # User CRUD (admin only)
        self.list_users_fn = self._create_lambda_function(
            "ListUsers", "lambdas/Functions/ListUsers"
        )

        self.get_user_fn = self._create_lambda_function(
            "GetUser", "lambdas/Functions/GetUser"
        )

        self.update_user_fn = self._create_lambda_function(
            "UpdateUser", "lambdas/Functions/UpdateUser"
        )

        self.delete_user_fn = self._create_lambda_function(
            "DeleteUser", "lambdas/Functions/DeleteUser"
        )

        # Project CRUD
        self.list_projects_fn = self._create_lambda_function(
            "ListProjects", "lambdas/Functions/ListProjects"
        )

        self.create_project_fn = self._create_lambda_function(
            "CreateProject", "lambdas/Functions/CreateProject"
        )

        self.get_project_fn = self._create_lambda_function(
            "GetProject", "lambdas/Functions/GetProject"
        )

        self.update_project_fn = self._create_lambda_function(
            "UpdateProject", "lambdas/Functions/UpdateProject"
        )

        self.delete_project_fn = self._create_lambda_function(
            "DeleteProject", "lambdas/Functions/DeleteProject"
        )

        # ProjectUser CRUD
        self.assign_user_to_project_fn = self._create_lambda_function(
            "AssignUserToProject", "lambdas/Functions/AssignUserToProject"
        )

        self.remove_user_from_project_fn = self._create_lambda_function(
            "RemoveUserFromProject", "lambdas/Functions/RemoveUserFromProject"
        )

        self.get_project_users_fn = self._create_lambda_function(
            "GetProjectUsers", "lambdas/Functions/GetProjectUsers"
        )

        self.get_user_projects_fn = self._create_lambda_function(
            "GetUserProjects", "lambdas/Functions/GetUserProjects"
        )

        # Session CRUD
        self.list_sessions_fn = self._create_lambda_function(
            "ListSessions", "lambdas/Functions/ListSessions"
        )

        self.create_session_fn = self._create_lambda_function(
            "CreateSession", "lambdas/Functions/CreateSession", timeout=60
        )

        self.get_session_fn = self._create_lambda_function(
            "GetSession", "lambdas/Functions/GetSession"
        )

        self.update_session_fn = self._create_lambda_function(
            "UpdateSession", "lambdas/Functions/UpdateSession"
        )

        self.delete_session_fn = self._create_lambda_function(
            "DeleteSession", "lambdas/Functions/DeleteSession"
        )

        self.get_project_sessions_fn = self._create_lambda_function(
            "GetProjectSessions", "lambdas/Functions/GetProjectSessions"
        )

        # Meeting Bot functions
        self.get_session_transcripts_fn = self._create_lambda_function(
            "GetSessionTranscripts", "lambdas/Functions/GetSessionTranscripts"
        )

        self.stop_meeting_bot_fn = self._create_lambda_function(
            "StopMeetingBot", "lambdas/Functions/StopMeetingBot"
        )

        self.get_bot_status_fn = self._create_lambda_function(
            "GetBotStatus", "lambdas/Functions/GetBotStatus"
        )

        # Bot Credentials CRUD
        self.create_bot_credential_fn = self._create_lambda_function(
            "CreateBotCredential", "lambdas/Functions/CreateBotCredential"
        )
        self.create_bot_credential_fn.add_environment("EVENT_BUS_NAME", "default")

        self.list_bot_credentials_fn = self._create_lambda_function(
            "ListBotCredentials", "lambdas/Functions/ListBotCredentials"
        )

        self.get_bot_credential_fn = self._create_lambda_function(
            "GetBotCredential", "lambdas/Functions/GetBotCredential"
        )

        self.update_bot_credential_fn = self._create_lambda_function(
            "UpdateBotCredential", "lambdas/Functions/UpdateBotCredential"
        )
        self.update_bot_credential_fn.add_environment("EVENT_BUS_NAME", "default")

        self.delete_bot_credential_fn = self._create_lambda_function(
            "DeleteBotCredential", "lambdas/Functions/DeleteBotCredential"
        )

        self.verify_bot_credential_fn = self._create_lambda_function(
            "VerifyBotCredential", "lambdas/Functions/VerifyBotCredential"
        )

        # Warm Pool Management
        self.start_warm_pool_fn = self._create_lambda_function(
            "StartWarmPool", "lambdas/Functions/StartWarmPool", timeout=120
        )

        self.stop_warm_pool_fn = self._create_lambda_function(
            "StopWarmPool", "lambdas/Functions/StopWarmPool", timeout=120
        )

        self.list_bot_pool_fn = self._create_lambda_function(
            "ListBotPool", "lambdas/Functions/ListBotPool"
        )

    def _create_d2_lambda_functions(self) -> None:
        """Create D2's 10 Lambda functions with appropriate layer/env combos."""
        # CRUD Lambdas (shared + powertools layers, base env)
        self.agents_crud_fn = self._create_lambda_function(
            "AgentsCrud", "lambdas/Functions/AgentsCrud"
        )
        self.personalities_crud_fn = self._create_lambda_function(
            "PersonalitiesCrud", "lambdas/Functions/PersonalitiesCrud"
        )
        self.qa_pairs_crud_fn = self._create_lambda_function(
            "QAPairsCrud", "lambdas/Functions/QAPairsCrud"
        )
        self.skills_crud_fn = self._create_lambda_function(
            "SkillsCrud", "lambdas/Functions/SkillsCrud"
        )

        self.agent_skills_crud_fn = self._create_lambda_function(
            "AgentSkillsCrud", "lambdas/Functions/AgentSkillsCrud"
        )

        # Test Prompt Lambda (admin only, no persistence)
        self.test_prompt_fn = self._create_lambda_function(
            "TestPrompt", "lambdas/Functions/TestPrompt",
            timeout=60,
            memory_size=256,
        )

        # AI base environment for event-driven Lambdas
        _ai_base_env = {
            **self._get_lambda_environment(),
            "OPENSEARCH_ENDPOINT": self.dynamodb_stack.opensearch_domain.domain_endpoint,
            "INDEX_NAME": "knowledge-vectors",
            "BEDROCK_REGION": self.env_config.get("bedrock_region", "us-east-1"),
        }

        # Ingestion/Deletion Lambdas (opensearch + pypdf2 layers)
        self.ingestion_fn = self._create_lambda_function(
            "Ingestion", "lambdas/Functions/Ingestion", timeout=300,
            memory_size=self.env_config.get("ingestion_memory", 512),
            layers=[self.shared_layer, self.powertools_layer, self.opensearch_layer, self.pypdf2_layer],
            environment=_ai_base_env,
        )

        self.deletion_fn = self._create_lambda_function(
            "Deletion", "lambdas/Functions/Deletion", timeout=60,
            layers=[self.shared_layer, self.powertools_layer, self.opensearch_layer, self.pypdf2_layer],
            environment=_ai_base_env,
        )

        self.skill_ingestion_fn = self._create_lambda_function(
            "SkillIngestion", "lambdas/Functions/SkillIngestion", timeout=300,
            memory_size=self.env_config.get("ingestion_memory", 512),
            layers=[self.shared_layer, self.powertools_layer, self.opensearch_layer, self.pypdf2_layer],
            environment=_ai_base_env,
        )

        self.skill_deletion_fn = self._create_lambda_function(
            "SkillDeletion", "lambdas/Functions/SkillDeletion", timeout=60,
            layers=[self.shared_layer, self.powertools_layer, self.opensearch_layer, self.pypdf2_layer],
            environment=_ai_base_env,
        )

        # GapScheduler Lambda
        self.gap_scheduler_fn = self._create_lambda_function(
            "GapScheduler", "lambdas/Functions/GapScheduler", timeout=60,
            environment={
                **self._get_lambda_environment(),
                "ACTIVE_SESSIONS_INDEX_NAME": "active-sessions-index",
            },
        )

        # StrandsAgent Lambda (strands + opensearch layers, merged env)
        self.strands_agent_fn = self._create_lambda_function(
            "StrandsAgent", "lambdas/Functions/StrandsAgent",
            timeout=self.env_config.get("strands_agent_timeout", 120),
            memory_size=self.env_config.get("strands_agent_memory", 512),
            layers=[self.shared_layer, self.powertools_layer, self.strands_layer, self.opensearch_layer],
            environment={
                **self._get_lambda_environment(),
                "OPENSEARCH_ENDPOINT": self.dynamodb_stack.opensearch_domain.domain_endpoint,
                "INDEX_NAME": "knowledge-vectors",
                "BEDROCK_REGION": self.env_config.get("bedrock_region", "us-east-1"),
                "WEBSOCKET_ENDPOINT": "",  # Set by ApiServicesStack after WS API creation
            },
        )

        # Wire GapScheduler → StrandsAgent invoke
        strands_fn_name = f"AXRAIL-StrandsAgent-{self.env_name}"
        self.gap_scheduler_fn.add_environment(
            "AGENT_FUNCTION_NAME", strands_fn_name
        )
        # Use explicit ARN string to avoid circular dependency
        # (grant_invoke would add a Ref to StrandsAgent in the shared role's default policy)
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                actions=["lambda:InvokeFunction"],
                resources=[
                    f"arn:aws:lambda:{self.region}:{self.account}:function:{strands_fn_name}",
                    f"arn:aws:lambda:{self.region}:{self.account}:function:{strands_fn_name}:*",
                ],
            )
        )

    def _grant_opensearch_permissions(self) -> None:
        """Grant OpenSearch permissions to Lambda role."""
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                actions=[
                    "es:ESHttpGet", "es:ESHttpPost", "es:ESHttpPut",
                    "es:ESHttpHead", "es:ESHttpDelete",
                ],
                resources=[
                    self.dynamodb_stack.opensearch_domain.domain_arn + "/*",
                ],
            )
        )

    def _grant_bedrock_permissions(self) -> None:
        """Grant Bedrock model invocation permissions."""
        bedrock_region = self.env_config.get("bedrock_region", "us-east-1")
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                actions=[
                    "bedrock:InvokeModel",
                    "bedrock:InvokeModelWithResponseStream",
                ],
                resources=[
                    f"arn:aws:bedrock:{bedrock_region}::foundation-model/amazon.nova-pro-v1:0",
                    f"arn:aws:bedrock:{bedrock_region}::foundation-model/amazon.titan-embed-text-v2:0",
                ],
            )
        )

    def _grant_d2_dynamodb_permissions(self) -> None:
        """Grant DynamoDB permissions for D2's 5 new tables."""
        for table in [
            self.dynamodb_stack.agents_table,
            self.dynamodb_stack.personalities_table,
            self.dynamodb_stack.qa_pairs_table,
            self.dynamodb_stack.suggested_questions_table,
            self.dynamodb_stack.skills_table,
            self.dynamodb_stack.gap_analysis_results_table,
            self.dynamodb_stack.agent_skills_table,
        ]:
            table.grant_read_write_data(self.lambda_role)

    def _grant_websocket_management_permissions(self) -> None:
        """Grant WebSocket connection management permissions."""
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                actions=["execute-api:ManageConnections"],
                resources=["*"],
            )
        )

    def _create_s3_buckets(self) -> None:
        """Create S3 buckets for KB and skill documents with event notifications.

        Uses low-level CfnBucket notification config to avoid circular
        dependencies caused by CDK's add_event_notification helper.
        """
        kb_bucket_name = f"axrail-kb-{self.env_name}-{self.account}"
        skills_bucket_name = f"axrail-skills-{self.env_name}-{self.account}"

        self.kb_bucket = s3.CfnBucket(
            self, "KbBucket",
            bucket_name=kb_bucket_name,
            notification_configuration=s3.CfnBucket.NotificationConfigurationProperty(
                lambda_configurations=[
                    s3.CfnBucket.LambdaConfigurationProperty(
                        event="s3:ObjectCreated:*",
                        function=self.ingestion_fn.function_arn,
                    ),
                    s3.CfnBucket.LambdaConfigurationProperty(
                        event="s3:ObjectRemoved:*",
                        function=self.deletion_fn.function_arn,
                    ),
                ],
            ),
        )
        self.kb_bucket.apply_removal_policy(RemovalPolicy.DESTROY)

        self.skills_bucket = s3.CfnBucket(
            self, "SkillsBucket",
            bucket_name=skills_bucket_name,
            cors_configuration=s3.CfnBucket.CorsConfigurationProperty(
                cors_rules=[
                    s3.CfnBucket.CorsRuleProperty(
                        allowed_headers=["*"],
                        allowed_methods=["PUT", "POST", "GET"],
                        allowed_origins=[
                            "http://localhost:3000",
                            "https://d2bed2yjnef4ve.cloudfront.net",
                        ],
                        exposed_headers=["ETag"],
                        max_age=3600,
                    ),
                ],
            ),
            notification_configuration=s3.CfnBucket.NotificationConfigurationProperty(
                lambda_configurations=[
                    s3.CfnBucket.LambdaConfigurationProperty(
                        event="s3:ObjectCreated:*",
                        function=self.skill_ingestion_fn.function_arn,
                    ),
                    s3.CfnBucket.LambdaConfigurationProperty(
                        event="s3:ObjectRemoved:*",
                        function=self.skill_deletion_fn.function_arn,
                    ),
                ],
            ),
        )
        self.skills_bucket.apply_removal_policy(RemovalPolicy.DESTROY)

        # Grant S3 invoke permission to each target Lambda
        for fn, bucket_ref, suffix in [
            (self.ingestion_fn, self.kb_bucket, "KbCreated"),
            (self.deletion_fn, self.kb_bucket, "KbRemoved"),
            (self.skill_ingestion_fn, self.skills_bucket, "SkillCreated"),
            (self.skill_deletion_fn, self.skills_bucket, "SkillRemoved"),
        ]:
            fn.add_permission(
                f"S3Invoke{suffix}",
                principal=iam.ServicePrincipal("s3.amazonaws.com"),
                source_arn=f"arn:aws:s3:::{bucket_ref.bucket_name}",
            )

        # S3 read/write via role policy (no grant_read_write to avoid implicit deps)
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                actions=["s3:GetObject*", "s3:PutObject*", "s3:DeleteObject*",
                         "s3:ListBucket", "s3:GetBucketLocation"],
                resources=[
                    f"arn:aws:s3:::{kb_bucket_name}",
                    f"arn:aws:s3:::{kb_bucket_name}/*",
                    f"arn:aws:s3:::{skills_bucket_name}",
                    f"arn:aws:s3:::{skills_bucket_name}/*",
                ],
            )
        )

        # Set bucket name env vars on relevant Lambdas
        self.skills_crud_fn.add_environment("SKILLS_BUCKET_NAME", skills_bucket_name)
        self.strands_agent_fn.add_environment("KB_BUCKET_NAME", kb_bucket_name)
        self.ingestion_fn.add_environment("KB_BUCKET_NAME", kb_bucket_name)
        self.skill_ingestion_fn.add_environment("SKILLS_BUCKET_NAME", skills_bucket_name)

    def _create_websocket_api(self) -> None:
        """Create WebSocket API Gateway for StrandsAgent real-time communication."""
        self.ws_api = apigwv2.CfnApi(
            self,
            "WebSocketApi",
            name=f"AXRAIL-WebSocket-{self.env_name}",
            protocol_type="WEBSOCKET",
            route_selection_expression="$request.body.action",
        )

        # Lambda integration for StrandsAgent
        integration = apigwv2.CfnIntegration(
            self,
            "WsStrandsIntegration",
            api_id=self.ws_api.ref,
            integration_type="AWS_PROXY",
            integration_uri=(
                f"arn:aws:apigateway:{self.region}:lambda:path"
                f"/2015-03-31/functions/{self.strands_agent_fn.function_arn}/invocations"
            ),
        )

        # Routes — all point to StrandsAgent
        routes = []
        for route_key in [
            "$connect", "$disconnect", "$default",
            "sendMessage", "processTranscript", "detectQuestion",
            "analyzeGaps", "endMeeting", "retroAnalysis", "retroChat",
            "setSuggestedQuestions",
        ]:
            safe_id = route_key.replace("$", "").capitalize() or "Default"
            route = apigwv2.CfnRoute(
                self, f"WsRoute{safe_id}",
                api_id=self.ws_api.ref,
                route_key=route_key,
                target=f"integrations/{integration.ref}",
            )
            routes.append(route)

        # Deployment and stage
        deployment = apigwv2.CfnDeployment(
            self, "WsDeployment",
            api_id=self.ws_api.ref,
        )
        deployment.add_dependency(integration)
        for route in routes:
            deployment.add_dependency(route)

        apigwv2.CfnStage(
            self, "WsStage",
            api_id=self.ws_api.ref,
            stage_name="production",
            deployment_id=deployment.ref,
        )

        # Grant API Gateway permission to invoke StrandsAgent
        self.strands_agent_fn.add_permission(
            "WsApiInvoke",
            principal=iam.ServicePrincipal("apigateway.amazonaws.com"),
            source_arn=f"arn:aws:execute-api:{self.region}:{self.account}:{self.ws_api.ref}/*",
        )

        # Set WEBSOCKET_ENDPOINT on StrandsAgent (no protocol — helpers.py prepends https://)
        ws_endpoint = f"{self.ws_api.ref}.execute-api.{self.region}.amazonaws.com/production"
        self.strands_agent_fn.add_environment("WEBSOCKET_ENDPOINT", ws_endpoint)

    def _create_ecs_task_state_handler(self) -> None:
        """Create Lambda and EventBridge rule to handle ECS task state changes."""
        self.handle_ecs_task_state_fn = _lambda.Function(
            self,
            "HandleEcsTaskState",
            function_name=f"AXRAIL-HandleEcsTaskState-{self.env_name}",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambdas/Functions/HandleEcsTaskState"),
            role=self.lambda_role,
            layers=[
                self.shared_layer,
                self.powertools_layer,
            ],
            environment={
                "BOT_POOL_TABLE": self.dynamodb_stack.bot_pool_table.table_name,
                "ECS_CLUSTER_NAME": self.meeting_bot_stack.cluster.cluster_name,
                "POWERTOOLS_SERVICE_NAME": "axrail-ecs-handler",
                "LOG_LEVEL": "INFO",
            },
            timeout=Duration.seconds(30),
            memory_size=128,
            tracing=_lambda.Tracing.ACTIVE,
        )

        self.ecs_task_state_rule = events.Rule(
            self,
            "EcsTaskStateRule",
            rule_name=f"AXRAIL-EcsTaskStateRule-{self.env_name}",
            description="Capture ECS task state changes for warm pool cleanup",
            event_pattern=events.EventPattern(
                source=["aws.ecs"],
                detail_type=["ECS Task State Change"],
                detail={
                    "clusterArn": [self.meeting_bot_stack.cluster.cluster_arn],
                    "lastStatus": ["STOPPED"],
                },
            ),
        )

        self.ecs_task_state_rule.add_target(
            targets.LambdaFunction(self.handle_ecs_task_state_fn)
        )

    def _create_gap_scheduler_rule(self) -> None:
        """Create EventBridge rule to trigger gap analysis on a schedule."""
        self.gap_scheduler_rule = events.Rule(
            self,
            "GapSchedulerRule",
            rule_name=f"AXRAIL-GapSchedulerRule-{self.env_name}",
            description="Trigger gap analysis for active sessions",
            schedule=events.Schedule.rate(Duration.minutes(2)),
        )
        self.gap_scheduler_rule.add_target(
            targets.LambdaFunction(self.gap_scheduler_fn)
        )

    def _create_bot_credential_validation_worker(self) -> None:
        """Create Lambda and EventBridge rule for async bot credential SMTP validation."""
        self.validate_bot_credential_worker_fn = _lambda.Function(
            self,
            "ValidateBotCredentialWorker",
            function_name=f"AXRAIL-ValidateBotCredentialWorker-{self.env_name}",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambdas/Functions/ValidateBotCredentialWorker"),
            role=self.lambda_role,
            layers=[
                self.shared_layer,
                self.powertools_layer,
            ],
            environment={
                "BOT_CREDENTIALS_TABLE": self.dynamodb_stack.bot_credentials_table.table_name,
                "ENVIRONMENT": self.env_name,
                "POWERTOOLS_SERVICE_NAME": "axrail-bot-credential-validator",
                "LOG_LEVEL": "INFO",
            },
            timeout=Duration.seconds(60),
            memory_size=256,
            tracing=_lambda.Tracing.ACTIVE,
        )

        # EventBridge rule to trigger validation worker
        self.bot_credential_validation_rule = events.Rule(
            self,
            "BotCredentialValidationRule",
            rule_name=f"AXRAIL-BotCredentialValidationRule-{self.env_name}",
            description="Trigger async SMTP validation for bot credentials",
            event_pattern=events.EventPattern(
                source=["axrail.bot-credentials"],
                detail_type=["BotCredentialValidation"],
            ),
        )

        self.bot_credential_validation_rule.add_target(
            targets.LambdaFunction(self.validate_bot_credential_worker_fn)
        )

    def _create_seed_admin(self) -> None:
        """Create SeedAdmin Lambda and Custom Resource for initial admin user."""
        self.seed_admin_role = iam.Role(
            self,
            "SeedAdminRole",
            role_name=f"AXRAIL-SeedAdminRole-{self.env_name}",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
            ],
        )

        self.seed_admin_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "cognito-idp:AdminCreateUser",
                    "cognito-idp:AdminAddUserToGroup",
                    "cognito-idp:AdminGetUser",
                ],
                resources=[self.cognito_stack.user_pool.user_pool_arn],
            )
        )

        self.seed_admin_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["dynamodb:PutItem"],
                resources=[self.dynamodb_stack.users_table.table_arn],
            )
        )

        self.seed_admin_fn = _lambda.Function(
            self,
            "SeedAdminFunction",
            function_name=f"AXRAIL-SeedAdmin-{self.env_name}",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambdas/Functions/SeedAdmin"),
            role=self.seed_admin_role,
            environment={
                "USER_POOL_ID": self.cognito_stack.user_pool.user_pool_id,
                "DYNAMODB_TABLE": self.dynamodb_stack.users_table.table_name,
                "ADMIN_EMAIL": self.admin_email,
                "ADMIN_TEMP_PASSWORD": self.admin_temp_password,
            },
            timeout=Duration.seconds(60),
            memory_size=256,
        )

        provider = cr.Provider(
            self,
            "SeedAdminProvider",
            on_event_handler=self.seed_admin_fn,
        )

        self.seed_admin_resource = CustomResource(
            self,
            "SeedAdminResource",
            service_token=provider.service_token,
            properties={
                "AdminEmail": self.admin_email,
                "Timestamp": "v4",
            },
        )

    def _create_seed_agent_data(self) -> None:
        """Create SeedAgentData Lambda and Custom Resource for initial agent/personality records."""
        self.seed_agent_data_fn = _lambda.Function(
            self,
            "SeedAgentDataFunction",
            function_name=f"AXRAIL-SeedAgentData-{self.env_name}",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambdas/Functions/SeedAgentData"),
            role=self.lambda_role,
            environment={
                "AGENTS_TABLE_NAME": self.dynamodb_stack.agents_table.table_name,
                "PERSONALITIES_TABLE_NAME": self.dynamodb_stack.personalities_table.table_name,
            },
            timeout=Duration.seconds(60),
            memory_size=256,
        )

        seed_agent_provider = cr.Provider(
            self,
            "SeedAgentDataProvider",
            on_event_handler=self.seed_agent_data_fn,
        )

        self.seed_agent_data_resource = CustomResource(
            self,
            "SeedAgentDataResource",
            service_token=seed_agent_provider.service_token,
            properties={
                "Timestamp": "v1",
            },
        )

    def _create_exports(self) -> None:
        CfnOutput(
            self,
            "AdminLoginFnArn",
            value=self.admin_login_fn.function_arn,
            export_name=f"AXRAIL-AdminLoginFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "UserLoginFnArn",
            value=self.user_login_fn.function_arn,
            export_name=f"AXRAIL-UserLoginFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "CreateUserFnArn",
            value=self.create_user_fn.function_arn,
            export_name=f"AXRAIL-CreateUserFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "ChangePasswordFnArn",
            value=self.change_password_fn.function_arn,
            export_name=f"AXRAIL-ChangePasswordFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "LogoutFnArn",
            value=self.logout_fn.function_arn,
            export_name=f"AXRAIL-LogoutFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "ListUsersFnArn",
            value=self.list_users_fn.function_arn,
            export_name=f"AXRAIL-ListUsersFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "GetUserFnArn",
            value=self.get_user_fn.function_arn,
            export_name=f"AXRAIL-GetUserFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "UpdateUserFnArn",
            value=self.update_user_fn.function_arn,
            export_name=f"AXRAIL-UpdateUserFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "DeleteUserFnArn",
            value=self.delete_user_fn.function_arn,
            export_name=f"AXRAIL-DeleteUserFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "ListProjectsFnArn",
            value=self.list_projects_fn.function_arn,
            export_name=f"AXRAIL-ListProjectsFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "CreateProjectFnArn",
            value=self.create_project_fn.function_arn,
            export_name=f"AXRAIL-CreateProjectFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "GetProjectFnArn",
            value=self.get_project_fn.function_arn,
            export_name=f"AXRAIL-GetProjectFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "UpdateProjectFnArn",
            value=self.update_project_fn.function_arn,
            export_name=f"AXRAIL-UpdateProjectFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "DeleteProjectFnArn",
            value=self.delete_project_fn.function_arn,
            export_name=f"AXRAIL-DeleteProjectFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "AssignUserToProjectFnArn",
            value=self.assign_user_to_project_fn.function_arn,
            export_name=f"AXRAIL-AssignUserToProjectFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "RemoveUserFromProjectFnArn",
            value=self.remove_user_from_project_fn.function_arn,
            export_name=f"AXRAIL-RemoveUserFromProjectFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "GetProjectUsersFnArn",
            value=self.get_project_users_fn.function_arn,
            export_name=f"AXRAIL-GetProjectUsersFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "GetUserProjectsFnArn",
            value=self.get_user_projects_fn.function_arn,
            export_name=f"AXRAIL-GetUserProjectsFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "ListSessionsFnArn",
            value=self.list_sessions_fn.function_arn,
            export_name=f"AXRAIL-ListSessionsFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "CreateSessionFnArn",
            value=self.create_session_fn.function_arn,
            export_name=f"AXRAIL-CreateSessionFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "GetSessionFnArn",
            value=self.get_session_fn.function_arn,
            export_name=f"AXRAIL-GetSessionFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "UpdateSessionFnArn",
            value=self.update_session_fn.function_arn,
            export_name=f"AXRAIL-UpdateSessionFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "DeleteSessionFnArn",
            value=self.delete_session_fn.function_arn,
            export_name=f"AXRAIL-DeleteSessionFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "GetProjectSessionsFnArn",
            value=self.get_project_sessions_fn.function_arn,
            export_name=f"AXRAIL-GetProjectSessionsFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "GetSessionTranscriptsFnArn",
            value=self.get_session_transcripts_fn.function_arn,
            export_name=f"AXRAIL-GetSessionTranscriptsFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "StopMeetingBotFnArn",
            value=self.stop_meeting_bot_fn.function_arn,
            export_name=f"AXRAIL-StopMeetingBotFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "GetBotStatusFnArn",
            value=self.get_bot_status_fn.function_arn,
            export_name=f"AXRAIL-GetBotStatusFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "CreateBotCredentialFnArn",
            value=self.create_bot_credential_fn.function_arn,
            export_name=f"AXRAIL-CreateBotCredentialFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "ListBotCredentialsFnArn",
            value=self.list_bot_credentials_fn.function_arn,
            export_name=f"AXRAIL-ListBotCredentialsFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "GetBotCredentialFnArn",
            value=self.get_bot_credential_fn.function_arn,
            export_name=f"AXRAIL-GetBotCredentialFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "UpdateBotCredentialFnArn",
            value=self.update_bot_credential_fn.function_arn,
            export_name=f"AXRAIL-UpdateBotCredentialFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "DeleteBotCredentialFnArn",
            value=self.delete_bot_credential_fn.function_arn,
            export_name=f"AXRAIL-DeleteBotCredentialFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "VerifyBotCredentialFnArn",
            value=self.verify_bot_credential_fn.function_arn,
            export_name=f"AXRAIL-VerifyBotCredentialFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "StartWarmPoolFnArn",
            value=self.start_warm_pool_fn.function_arn,
            export_name=f"AXRAIL-StartWarmPoolFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "StopWarmPoolFnArn",
            value=self.stop_warm_pool_fn.function_arn,
            export_name=f"AXRAIL-StopWarmPoolFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "ListBotPoolFnArn",
            value=self.list_bot_pool_fn.function_arn,
            export_name=f"AXRAIL-ListBotPoolFnArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "AdminEmail",
            value=self.admin_email,
            export_name=f"AXRAIL-AdminEmail-{self.env_name}",
        )

        CfnOutput(
            self,
            "AdminTempPassword",
            value=self.admin_temp_password,
            export_name=f"AXRAIL-AdminTempPassword-{self.env_name}",
            description="Temporary password for admin. Change immediately after first login.",
        )

        CfnOutput(
            self,
            "LambdaRoleArn",
            value=self.lambda_role.role_arn,
            export_name=f"AXRAIL-LambdaRoleArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "SharedLayerArn",
            value=self.shared_layer.layer_version_arn,
            export_name=f"AXRAIL-SharedLayerArn-{self.env_name}",
        )

        CfnOutput(
            self,
            "PowertoolsLayerArn",
            value=self.powertools_layer.layer_version_arn,
            export_name=f"AXRAIL-PowertoolsLayerArn-{self.env_name}",
        )

        # D2 exports
        CfnOutput(
            self,
            "WebSocketEndpoint",
            value=f"wss://{self.ws_api.ref}.execute-api.{self.region}.amazonaws.com/production",
            export_name=f"AXRAIL-WebSocketEndpoint-{self.env_name}",
        )

        CfnOutput(
            self,
            "KbBucketName",
            value=self.kb_bucket.bucket_name,
            export_name=f"AXRAIL-KbBucketName-{self.env_name}",
        )

        CfnOutput(
            self,
            "SkillsBucketName",
            value=self.skills_bucket.bucket_name,
            export_name=f"AXRAIL-SkillsBucketName-{self.env_name}",
        )
