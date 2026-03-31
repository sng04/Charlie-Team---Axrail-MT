from aws_cdk import (
    Stack,
    Duration,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_ssm as ssm,
    CfnOutput,
)
from constructs import Construct

from stack_cdk.lambda_stack import LambdaStack


class ApiServicesStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        env_name: str,
        lambda_stack: LambdaStack,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.env_name = env_name
        self.lambda_stack = lambda_stack

        # Look up layer ARNs from SSM instead of using direct cross-stack
        # construct references (which create fragile CloudFormation exports).
        shared_layer_arn = ssm.StringParameter.value_for_string_parameter(
            self, f"/axrail/{env_name}/shared-layer-arn"
        )
        powertools_layer_arn = ssm.StringParameter.value_for_string_parameter(
            self, f"/axrail/{env_name}/powertools-layer-arn"
        )
        self._shared_layer = _lambda.LayerVersion.from_layer_version_arn(
            self, "ImportedSharedLayer", shared_layer_arn
        )
        self._powertools_layer = _lambda.LayerVersion.from_layer_version_arn(
            self, "ImportedPowertoolsLayer", powertools_layer_arn
        )

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
        # D2 additions
        self._create_agent_routes()
        self._create_agent_skill_routes()
        self._create_personality_routes()
        self._create_skill_routes()
        self._create_kb_document_routes()
        self._create_file_download_routes()
        self._create_qa_routes()
        self._create_admin_changelog_routes()
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
        
        # Add CORS headers to Gateway Responses for error cases
        self.api.add_gateway_response(
            "Unauthorized",
            type=apigw.ResponseType.UNAUTHORIZED,
            response_headers={
                "Access-Control-Allow-Origin": "'*'",
                "Access-Control-Allow-Headers": "'Content-Type,Authorization'",
            },
        )
        self.api.add_gateway_response(
            "AccessDenied",
            type=apigw.ResponseType.ACCESS_DENIED,
            response_headers={
                "Access-Control-Allow-Origin": "'*'",
                "Access-Control-Allow-Headers": "'Content-Type,Authorization'",
            },
        )
        self.api.add_gateway_response(
            "Default4xx",
            type=apigw.ResponseType.DEFAULT_4_XX,
            response_headers={
                "Access-Control-Allow-Origin": "'*'",
                "Access-Control-Allow-Headers": "'Content-Type,Authorization'",
            },
        )
        self.api.add_gateway_response(
            "Default5xx",
            type=apigw.ResponseType.DEFAULT_5_XX,
            response_headers={
                "Access-Control-Allow-Origin": "'*'",
                "Access-Control-Allow-Headers": "'Content-Type,Authorization'",
            },
        )

    def _create_admin_authorizer_lambda(self) -> None:
        self.admin_authorizer_fn = _lambda.Function(
            self,
            "AdminAuthorizerFn",
            function_name=f"AXRAIL-AdminAuthorizer-{self.env_name}",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambdas/Functions/AdminAuthorizer"),
            role=self.lambda_stack.lambda_role,
            layers=[
                self._shared_layer,
                self._powertools_layer,
            ],
            environment={
                "POWERTOOLS_SERVICE_NAME": "axrail-authorizer",
                "LOG_LEVEL": "INFO",
                "USER_POOL_ID": self.lambda_stack.cognito_stack.user_pool.user_pool_id,
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
            role=self.lambda_stack.lambda_role,
            layers=[
                self._shared_layer,
                self._powertools_layer,
            ],
            environment={
                "POWERTOOLS_SERVICE_NAME": "axrail-authorizer",
                "LOG_LEVEL": "INFO",
                "USER_POOL_ID": self.lambda_stack.cognito_stack.user_pool.user_pool_id,
            },
            timeout=Duration.seconds(10),
            memory_size=128,
            tracing=_lambda.Tracing.ACTIVE,
        )

    def _create_authorizers(self) -> None:
        # Admin-only authorizer (no cache to ensure logout works immediately)
        self.admin_authorizer = apigw.TokenAuthorizer(
            self,
            "AdminAuthorizer",
            authorizer_name=f"AXRAIL-AdminAuthorizer-{self.env_name}",
            handler=self.admin_authorizer_fn,
            results_cache_ttl=Duration.seconds(0),
        )
        
        # Auth authorizer (no cache to ensure logout works immediately)
        self.auth_authorizer = apigw.TokenAuthorizer(
            self,
            "AuthAuthorizer",
            authorizer_name=f"AXRAIL-AuthAuthorizer-{self.env_name}",
            handler=self.auth_authorizer_fn,
            results_cache_ttl=Duration.seconds(0),
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
        
        # GET /users - List all users (admin only)
        users_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.list_users_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        # POST /users - Create user (admin only)
        users_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.create_user_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        user_id_resource = users_resource.add_resource("{userId}")

        # GET /users/{userId} - Get single user (admin only)
        user_id_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_user_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # PUT /users/{userId} - Update user (admin only)
        user_id_resource.add_method(
            "PUT",
            apigw.LambdaIntegration(self.lambda_stack.update_user_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # DELETE /users/{userId} - Delete user (admin only)
        user_id_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.delete_user_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        
        change_password_resource = auth_resource.add_resource("change-password")
        change_password_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.change_password_fn),
        )
        
        # POST /auth/logout - Logout (authenticated users)
        logout_resource = auth_resource.add_resource("logout")
        logout_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.logout_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_project_routes(self) -> None:
        projects_resource = self.api.root.add_resource("projects")
        
        # GET /projects - List projects (admin: all, user: assigned only)
        projects_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.list_projects_fn),
            authorizer=self.auth_authorizer,
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
        
        # GET /projects/{projectId} - Get single project (admin: any, user: assigned only)
        project_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_project_fn),
            authorizer=self.auth_authorizer,
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
        user_resource = users_resource.get_resource("{userId}")
        if not user_resource:
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
        
        # GET /sessions/{sessionId}/suggested-questions
        suggested_questions_resource = session_resource.add_resource("suggested-questions")
        suggested_questions_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_suggested_questions_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # GET /sessions/{sessionId}/summary
        summary_resource = session_resource.add_resource("summary")
        summary_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.get_session_summary_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # GET /sessions/{sessionId}/token-usage
        token_usage_resource = session_resource.add_resource("token-usage")
        token_usage_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.token_usage_fn),
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

        # GET /bot-credentials/{credentialId}/pool - List bot pool containers (admin only)
        pool_resource = bot_credential_resource.add_resource("pool")
        pool_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.list_bot_pool_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
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

        # POST /warm-pool/stop - Stop/scale down warm pool containers (admin only)
        stop_resource = warm_pool_resource.add_resource("stop")
        stop_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.stop_warm_pool_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_agent_routes(self) -> None:
        """Create Agent CRUD REST routes."""
        agents_resource = self.api.root.add_resource("agents")

        agents_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.agents_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        agents_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.agents_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        agent_resource = agents_resource.add_resource("{agentId}")
        self.agent_resource = agent_resource
        agent_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.agents_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        agent_resource.add_method(
            "PUT",
            apigw.LambdaIntegration(self.lambda_stack.agents_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        agent_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.agents_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # Test Prompt — POST /agents/test-prompt
        test_prompt_resource = agents_resource.add_resource("test-prompt")
        test_prompt_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.test_prompt_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_agent_skill_routes(self) -> None:
        """Create agent-skill assignment REST routes under /agents/{agentId}/skills."""
        skills_resource = self.agent_resource.add_resource("skills")

        # GET /agents/{agentId}/skills - List skills for agent
        skills_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.agent_skills_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        skill_resource = skills_resource.add_resource("{skillId}")

        # POST /agents/{agentId}/skills/{skillId} - Assign skill to agent
        skill_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.agent_skills_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # DELETE /agents/{agentId}/skills/{skillId} - Unassign skill from agent
        skill_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.agent_skills_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # History routes under /agents/{agentId}/history
        history_resource = self.agent_resource.add_resource("history")

        # GET /agents/{agentId}/history - List config history
        history_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.agents_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        version_resource = history_resource.add_resource("{version}")

        # GET /agents/{agentId}/history/{version} - Get specific version
        version_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.agents_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_personality_routes(self) -> None:
        """Create Personality CRUD REST routes (top-level)."""
        personalities_resource = self.api.root.add_resource("personalities")

        personalities_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.personalities_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        personalities_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.personalities_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        personality_resource = personalities_resource.add_resource("{personalityId}")
        personality_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.personalities_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        personality_resource.add_method(
            "PUT",
            apigw.LambdaIntegration(self.lambda_stack.personalities_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        personality_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.personalities_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_skill_routes(self) -> None:
        """Create Skill CRUD REST routes (top-level)."""
        skills_resource = self.api.root.add_resource("skills")

        skills_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.skills_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        skills_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.skills_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        skill_resource = skills_resource.add_resource("{skillId}")
        skill_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.skills_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        skill_resource.add_method(
            "PUT",
            apigw.LambdaIntegration(self.lambda_stack.skills_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        skill_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.skills_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # Replace document — POST /skills/{skillId}/replace-document
        replace_doc_resource = skill_resource.add_resource("replace-document")
        replace_doc_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.skills_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # Alias: POST /skills/{skillId}/replace (for frontend compatibility)
        replace_alias_resource = skill_resource.add_resource("replace")
        replace_alias_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.skills_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_kb_document_routes(self) -> None:
        """Create KB Document CRUD API routes under /projects/{projectId}/kb-documents."""
        projects_resource = self.api.root.get_resource("projects")
        project_resource = projects_resource.get_resource("{projectId}")

        kb_docs_resource = project_resource.add_resource("kb-documents")

        # GET /projects/{projectId}/kb-documents - List KB documents
        kb_docs_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.kb_documents_crud_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # POST /projects/{projectId}/kb-documents - Create KB document
        kb_docs_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.kb_documents_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        kb_doc_resource = kb_docs_resource.add_resource("{documentId}")

        # GET /projects/{projectId}/kb-documents/{documentId} - Get single document
        kb_doc_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.kb_documents_crud_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # DELETE /projects/{projectId}/kb-documents/{documentId} - Delete document
        kb_doc_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.kb_documents_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # POST /projects/{projectId}/kb-documents/{documentId}/replace - Replace file
        replace_resource = kb_doc_resource.add_resource("replace")
        replace_resource.add_method(
            "POST",
            apigw.LambdaIntegration(self.lambda_stack.kb_documents_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_file_download_routes(self) -> None:
        """Create file download route: GET /files/download?bucket=...&key=..."""
        files_resource = self.api.root.add_resource("files")
        download_resource = files_resource.add_resource("download")

        download_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.file_download_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_qa_routes(self) -> None:
        """Create QA pairs and suggested questions routes (top-level)."""
        qa_pairs_resource = self.api.root.add_resource("qa-pairs")
        qa_pairs_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.qa_pairs_crud_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        qa_pair_resource = qa_pairs_resource.add_resource("{qaPairId}")
        qa_pair_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.qa_pairs_crud_fn),
            authorizer=self.auth_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )
        qa_pair_resource.add_method(
            "DELETE",
            apigw.LambdaIntegration(self.lambda_stack.qa_pairs_crud_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

    def _create_admin_changelog_routes(self) -> None:
        """Create admin changelog retrieval route: GET /admin/changelog."""
        admin_resource = self.api.root.add_resource("admin")
        changelog_resource = admin_resource.add_resource("changelog")

        changelog_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.admin_changelog_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        # Token usage routes under /admin/token-usage
        token_usage_resource = admin_resource.add_resource("token-usage")

        summary_resource = token_usage_resource.add_resource("summary")
        summary_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.token_usage_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        daily_resource = token_usage_resource.add_resource("daily")
        daily_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.token_usage_fn),
            authorizer=self.admin_authorizer,
            authorization_type=apigw.AuthorizationType.CUSTOM,
        )

        by_project_resource = token_usage_resource.add_resource("by-project")
        by_project_resource.add_method(
            "GET",
            apigw.LambdaIntegration(self.lambda_stack.token_usage_fn),
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
