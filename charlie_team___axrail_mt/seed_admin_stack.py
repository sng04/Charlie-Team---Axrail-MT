from aws_cdk import (
    Stack,
    Duration,
    CustomResource,
    aws_lambda as _lambda,
    aws_iam as iam,
    custom_resources as cr,
    CfnOutput,
)
from constructs import Construct

from charlie_team___axrail_mt.dynamodb_stack import DynamoDBStack
from charlie_team___axrail_mt.cognito_stack import CognitoStack


class SeedAdminStack(Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        env_name: str,
        dynamodb_stack: DynamoDBStack,
        cognito_stack: CognitoStack,
        admin_email: str = "admin@axrail.com",
        admin_temp_password: str = "TempAdmin@123",
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.env_name = env_name
        self.dynamodb_stack = dynamodb_stack
        self.cognito_stack = cognito_stack
        self.admin_email = admin_email
        self.admin_temp_password = admin_temp_password
        
        self._create_seed_admin_function()
        self._create_custom_resource()
        self._create_exports()

    def _create_seed_admin_function(self) -> None:
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
                actions=[
                    "dynamodb:PutItem",
                ],
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

    def _create_custom_resource(self) -> None:
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
