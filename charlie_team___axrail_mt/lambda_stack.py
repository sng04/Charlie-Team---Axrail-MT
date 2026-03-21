from aws_cdk import (
    Stack,
    Duration,
    CustomResource,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_events as events,
    aws_events_targets as targets,
    custom_resources as cr,
    CfnOutput,
)
from constructs import Construct

from charlie_team___axrail_mt.dynamodb_stack import DynamoDBStack
from charlie_team___axrail_mt.cognito_stack import CognitoStack
from charlie_team___axrail_mt.meeting_bot_stack import MeetingBotStack


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
        ses_sender_email: str,
        admin_email: str,
        admin_temp_password: str,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.env_name = env_name
        self.dynamodb_stack = dynamodb_stack
        self.cognito_stack = cognito_stack
        self.meeting_bot_stack = meeting_bot_stack
        self.ses_sender_email = ses_sender_email
        self.admin_email = admin_email
        self.admin_temp_password = admin_temp_password

        self._create_lambda_layers()
        self._create_lambda_role()
        self._grant_dynamodb_permissions()
        self._grant_cognito_permissions()
        self._grant_ses_permissions()
        self._grant_ecs_permissions()
        self._grant_sqs_permissions()
        self._grant_secrets_permissions()
        self._grant_cloudformation_permissions()
        self._create_lambda_functions()
        self._create_ecs_task_state_handler()
        self._create_seed_admin()
        self._create_exports()

    def _create_lambda_layers(self) -> None:
        """Create Lambda layers for shared code."""
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
                ],
                resources=[self.cognito_stack.user_pool.user_pool_arn],
            )
        )

    def _grant_ses_permissions(self) -> None:
        """Grant SES permissions for sending verification emails."""
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "ses:SendEmail",
                    "ses:SendRawEmail",
                ],
                resources=[f"arn:aws:ses:{self.region}:{self.account}:identity/*"],
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
            "SES_SENDER_EMAIL": self.ses_sender_email,
        }

    def _create_lambda_function(
        self, function_name: str, handler_path: str, timeout: int = 30
    ) -> _lambda.Function:
        return _lambda.Function(
            self,
            function_name,
            function_name=f"AXRAIL-{function_name}-{self.env_name}",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset(handler_path),
            role=self.lambda_role,
            layers=[
                self.shared_layer,
                self.powertools_layer,
            ],
            environment=self._get_lambda_environment(),
            timeout=Duration.seconds(timeout),
            memory_size=256,
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

        self.list_bot_credentials_fn = self._create_lambda_function(
            "ListBotCredentials", "lambdas/Functions/ListBotCredentials"
        )

        self.get_bot_credential_fn = self._create_lambda_function(
            "GetBotCredential", "lambdas/Functions/GetBotCredential"
        )

        self.update_bot_credential_fn = self._create_lambda_function(
            "UpdateBotCredential", "lambdas/Functions/UpdateBotCredential"
        )

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
