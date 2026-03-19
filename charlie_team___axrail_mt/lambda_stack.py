from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_iam as iam,
    CfnOutput,
)
from constructs import Construct

from charlie_team___axrail_mt.shared_resources_stack import SharedResourcesStack
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
        shared_resources: SharedResourcesStack,
        dynamodb_stack: DynamoDBStack,
        cognito_stack: CognitoStack,
        meeting_bot_stack: MeetingBotStack,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.env_name = env_name
        self.shared_resources = shared_resources
        self.dynamodb_stack = dynamodb_stack
        self.cognito_stack = cognito_stack
        self.meeting_bot_stack = meeting_bot_stack

        self._grant_ecs_permissions()
        self._grant_secrets_permissions()
        self._create_lambda_functions()
        self._create_exports()

    def _grant_ecs_permissions(self) -> None:
        """Grant ECS permissions to Lambda role for starting/stopping tasks."""
        self.shared_resources.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "ecs:RunTask",
                    "ecs:StopTask",
                    "ecs:DescribeTasks",
                ],
                resources=["*"],
            )
        )
        self.shared_resources.lambda_role.add_to_policy(
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

    def _grant_secrets_permissions(self) -> None:
        """Grant Secrets Manager permissions to Lambda role."""
        self.shared_resources.lambda_role.add_to_policy(
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
            "ENVIRONMENT": self.env_name,
            "POWERTOOLS_SERVICE_NAME": "axrail-api",
            "LOG_LEVEL": "INFO",
            "SES_SENDER_EMAIL_PARAM": f"/axrail/{self.env_name}/ses/sender-email",
            "API_ENDPOINT": "https://tavz3lny8c.execute-api.ap-southeast-1.amazonaws.com/dev",
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
            role=self.shared_resources.lambda_role,
            layers=[
                self.shared_resources.shared_layer,
                self.shared_resources.powertools_layer,
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
