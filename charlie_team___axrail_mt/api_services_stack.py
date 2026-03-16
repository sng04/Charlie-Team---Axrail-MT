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
        self._create_authorizer()
        self._create_auth_routes()
        self._create_project_routes()
        self._create_project_user_routes()
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

    def _create_authorizer(self) -> None:
        # Custom Lambda Authorizer untuk admin-only endpoints
        self.admin_authorizer = apigw.TokenAuthorizer(
            self,
            "AdminAuthorizer",
            authorizer_name=f"AXRAIL-AdminAuthorizer-{self.env_name}",
            handler=self.admin_authorizer_fn,
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

    def _create_exports(self) -> None:
        CfnOutput(
            self,
            "ApiEndpoint",
            value=self.api.url,
            export_name=f"AXRAIL-ApiEndpoint-{self.env_name}",
        )
