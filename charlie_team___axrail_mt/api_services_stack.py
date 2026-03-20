from aws_cdk import (
    Stack,
    Duration,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_iam as iam,
    CfnOutput,
)
from constructs import Construct

from charlie_team___axrail_mt.lambda_stack import LambdaStack
from charlie_team___axrail_mt.shared_resources_stack import SharedResourcesStack


class ApiServicesStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        env_name: str,
        lambda_stack: LambdaStack,
        shared_resources: SharedResourcesStack,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.env_name = env_name
        self.lambda_stack = lambda_stack
        self.shared_resources = shared_resources
        
        self._create_api_gateway()
        self._create_admin_authorizer_lambda()
        self._create_auth_authorizer_lambda()
        self._create_authorizers()
        self._create_auth_routes()
        self._create_project_routes()
        self._create_project_user_routes()
        self._create_session_routes()
        self._create_meeting_bot_routes()
        self._create_bot_credential_routes()
        self._create_warm_pool_routes()
        self._create_exports()

    def _create_api_gateway(self) -> None:
        self.api = apigw.RestApi(
            self,
            "AuthApi",
            rest_api_name=f"AXRAIL-AuthApi-{self.env_name}",
            description="Authentication API for AXRAIL",
            deploy_options=apigw.StageOptions(
                stage_name=self.env_name,
                logging_level=apigw.MethodLoggingLevel.INFO,
                data_trace_enabled=True,
                tracing_enabled=True,
            ),
            default_cors_preflight_options=apigw.CorsOptions(
                allow_origins=apigw.Cors.ALL_ORIGINS,
                allow_methods=apigw.Cors.ALL_METHODS,
                allow_headers=["Content-Type", "Authorization"],
            ),
        )

    def _create_admin_authorizer_lambda(self) -> None:
        self.admin_authorizer_fn = _lambda.Function(
            self,
            "AdminAuthorizerFn",
            function_name=f"AXRAIL-AdminAuthorizer-{self.env_name}",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambdas/Functions/AdminAuthorizer"),
            role=self.shared_resources.lambda_role,
            layers=[
                self.shared_resources.shared_layer,
                self.shared_resources.powertools_layer,
            ],
            environment={
                "POWERTOOLS_SERVICE_NAME": "axrail-authorizer",
                "LOG_LEVEL": "INFO",
            },
            timeout=Duration.seconds(10),
            memory_size=128,
            tracing=_lambda.Tracing.ACTIVE,
        )

    def _create_auth_authorizer_lambda(self) -> None:
        self.auth_authorizer_fn = _lambda.Function(
            self,
            "AuthAuthorizerFn",
            function_name=f"AXRAIL-AuthAuthorizer-{self.env_name}",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambdas/Functions/AuthAuthorizer"),
            role=self.shared_resources.lambda_role,
            layers=[
                self.shared_resources.shared_layer,
                self.shared_resources.powertools_layer,
            ],
            environment={
                "POWERTOOLS_SERVICE_NAME": "axrail-authorizer",
                "LOG_LEVEL": "INFO",
            },
            timeout=Duration.seconds(10),
            memory_size=128,
            tracing=_lambda.Tracing.ACTIVE,
        )

    def _create_authorizers(self) -> None:
        # Admin-only authorizer
        self.admin_authorizer = apigw.TokenAuthorizer(
            self,
            "AdminAuthorizer",
            authorizer_name=f"AXRAIL-AdminAuthorizer-{self.env_name}",
            handler=self.admin_authorizer_fn,
            results_cache_ttl=Duration.minutes(5),
        )
        
        # Auth authorizer (admin or user)
        self.auth_authorizer = apigw.TokenAuthorizer(
            self,
            "AuthAuthorizer",
            authorizer_name=f"AXRAIL-AuthAuthorizer-{self.env_name}",
            handler=self.auth_authorizer_fn,
            results_cache_ttl=Duration.minutes(5),
        )

    def _create_auth_routes(self) -> None:
        auth_resource = self.api.root.add_resource("auth")
        
        admin_resource = auth_resource.add_resource("admin")
        admin_login_resource = admin_resource.add_resource("login")
        admin_login_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.admin_login_fn),
        )
        
        user_resource = auth_resource.add_resource("user")
        user_login_resource = user_resource.add_resource("login")
        user_login_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.user_login_fn),
        )
        
        users_resource = self.api.root.add_resource("users")
        users_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.create_user_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        change_password_resource = auth_resource.add_resource("change-password")
        change_password_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.change_password_fn),
        )

    def _create_project_routes(self) -> None:
        projects_resource = self.api.root.add_resource("projects")
        
        # GET /projects - List all projects (admin only)
        projects_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.list_projects_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        # POST /projects - Create project (admin only)
        projects_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.create_project_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        project_resource = projects_resource.add_resource("{projectId}")
        
        # GET /projects/{projectId} - Get single project (admin only)
        project_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_project_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        # PUT /projects/{projectId} - Update project (admin only)
        project_resource.add_method(
            "PUT",
            apigw.LambdaIntegration(self.lambda_stack.update_project_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        # DELETE /projects/{projectId} - Delete project (admin only)
        project_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.delete_project_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        # GET /projects/{projectId}/users - Get users in project (admin only)
        project_users_resource = project_resource.add_resource("users")
        project_users_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_project_users_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_project_user_routes(self) -> None:
        project_users_resource = self.api.root.add_resource("project-users")
        
        # POST /project-users - Assign user to project (admin only)
        project_users_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.assign_user_to_project_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        project_user_resource = project_users_resource.add_resource("{projectUserId}")
        
        # DELETE /project-users/{projectUserId} - Remove user from project (admin only)
        project_user_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.remove_user_from_project_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        # GET /users/{userId}/projects - Get projects for user (admin only)
        users_resource = self.api.root.get_resource("users")
        if not users_resource:
            users_resource = self.api.root.add_resource("users")
        user_resource = users_resource.add_resource("{userId}")
        user_projects_resource = user_resource.add_resource("projects")
        user_projects_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_user_projects_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_session_routes(self) -> None:
        sessions_resource = self.api.root.add_resource("sessions")
        
        # GET /sessions - List all sessions (authenticated users)
        sessions_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.list_sessions_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        # POST /sessions - Create session (authenticated users)
        sessions_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.create_session_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        session_resource = sessions_resource.add_resource("{sessionId}")
        
        # GET /sessions/{sessionId} - Get single session (authenticated users)
        session_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_session_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        # PUT /sessions/{sessionId} - Update session (authenticated users)
        session_resource.add_method(
            "PUT",
            apigw.LambdaIntegration(self.lambda_stack.update_session_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        # DELETE /sessions/{sessionId} - Delete session (authenticated users)
        session_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.delete_session_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        # GET /projects/{projectId}/sessions - Get sessions for project (authenticated users)
        projects_resource = self.api.root.get_resource("projects")
        project_resource = projects_resource.get_resource("{projectId}")
        project_sessions_resource = project_resource.add_resource("sessions")
        project_sessions_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_project_sessions_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_meeting_bot_routes(self) -> None:
        """Create Meeting Bot related API routes."""
        # GET /sessions/{sessionId}/transcripts - Get session transcripts (authenticated users)
        sessions_resource = self.api.root.get_resource("sessions")
        session_resource = sessions_resource.get_resource("{sessionId}")
        transcripts_resource = session_resource.add_resource("transcripts")
        transcripts_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_session_transcripts_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # POST /sessions/{sessionId}/stop-bot - Stop meeting bot (authenticated users)
        stop_bot_resource = session_resource.add_resource("stop-bot")
        stop_bot_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.stop_meeting_bot_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # GET /sessions/{sessionId}/bot-status - Get bot status (authenticated users)
        bot_status_resource = session_resource.add_resource("bot-status")
        bot_status_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_bot_status_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_bot_credential_routes(self) -> None:
        """Create Bot Credential CRUD API routes."""
        bot_credentials_resource = self.api.root.add_resource("bot-credentials")

        # GET /bot-credentials - List all bot credentials (admin only)
        bot_credentials_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.list_bot_credentials_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # POST /bot-credentials - Create bot credential (admin only)
        bot_credentials_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.create_bot_credential_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        bot_credential_resource = bot_credentials_resource.add_resource("{credentialId}")

        # GET /bot-credentials/{credentialId} - Get single bot credential (admin only)
        bot_credential_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_bot_credential_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # PUT /bot-credentials/{credentialId} - Update bot credential (admin only)
        bot_credential_resource.add_method(
            "PUT",
            apigw.LambdaIntegration(self.lambda_stack.update_bot_credential_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # DELETE /bot-credentials/{credentialId} - Delete bot credential (admin only)
        bot_credential_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.delete_bot_credential_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # GET /bot-credentials/{credentialId}/verify - Verify email (public)
        verify_resource = bot_credential_resource.add_resource("verify")
        verify_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.verify_bot_credential_fn),
        )

    def _create_warm_pool_routes(self) -> None:
        """Create Warm Pool management API routes."""
        warm_pool_resource = self.api.root.add_resource("warm-pool")

        # POST /warm-pool/start - Start warm pool containers (admin only)
        start_resource = warm_pool_resource.add_resource("start")
        start_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.start_warm_pool_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )


    def _create_exports(self) -> None:
        CfnOutput(
            self,
            "ApiEndpoint",
            value=self.api.url,
            export_name=f"AXRAIL-ApiEndpoint-{self.env_name}",
        )
