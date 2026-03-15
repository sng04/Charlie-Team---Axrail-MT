from aws_cdk import (
    Stack,
    aws_apigateway as apigw,
    CfnOutput,
)
from constructs import Construct

from charlie_team___axrail_mt.lambda_stack import LambdaStack


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
        
        self._create_api_gateway()
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

    def _create_exports(self) -> None:
        CfnOutput(
            self,
            "ApiEndpoint",
            value=self.api.url,
            export_name=f"AXRAIL-ApiEndpoint-{self.env_name}",
        )
