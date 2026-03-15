from aws_cdk import (
    Stack,
    Duration,
    aws_lambda as _lambda,
    CfnOutput,
)
from constructs import Construct

from charlie_team___axrail_mt.shared_resources_stack import SharedResourcesStack
from charlie_team___axrail_mt.dynamodb_stack import DynamoDBStack
from charlie_team___axrail_mt.cognito_stack import CognitoStack


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
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.env_name = env_name
        self.shared_resources = shared_resources
        self.dynamodb_stack = dynamodb_stack
        self.cognito_stack = cognito_stack
        
        self._create_lambda_functions()
        self._create_exports()

    def _get_lambda_environment(self) -> dict:
        return {
            "USER_POOL_ID": self.cognito_stack.user_pool.user_pool_id,
            "CLIENT_ID": self.cognito_stack.user_pool_client.user_pool_client_id,
            "DYNAMODB_TABLE": self.dynamodb_stack.users_table.table_name,
            "POWERTOOLS_SERVICE_NAME": "axrail-auth",
            "LOG_LEVEL": "INFO",
        }

    def _create_lambda_function(self, function_name: str, handler_path: str) -> _lambda.Function:
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
            timeout=Duration.seconds(30),
            memory_size=256,
            tracing=_lambda.Tracing.ACTIVE,
        )

    def _create_lambda_functions(self) -> None:
        self.admin_login_fn = self._create_lambda_function(
            "AdminLogin",
            "lambdas/Functions/AdminLogin"
        )
        
        self.user_login_fn = self._create_lambda_function(
            "UserLogin",
            "lambdas/Functions/UserLogin"
        )
        
        self.create_user_fn = self._create_lambda_function(
            "CreateUser",
            "lambdas/Functions/CreateUser"
        )
        
        self.change_password_fn = self._create_lambda_function(
            "ChangePassword",
            "lambdas/Functions/ChangePassword"
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
