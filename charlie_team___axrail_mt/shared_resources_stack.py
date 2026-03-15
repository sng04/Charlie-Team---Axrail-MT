from aws_cdk import (
    Stack,
    Duration,
    RemovalPolicy,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_ssm as ssm,
    CfnOutput,
)
from constructs import Construct


class SharedResourcesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, *, env_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.env_name = env_name
        
        self._create_lambda_layer()
        self._create_lambda_role()
        self._create_exports()

    def _create_lambda_layer(self) -> None:
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
        
        ssm.StringParameter(
            self,
            "SharedLayerArnParam",
            parameter_name=f"/axrail/{self.env_name}/layers/shared-layer-arn",
            string_value=self.shared_layer.layer_version_arn,
        )
        
        ssm.StringParameter(
            self,
            "PowertoolsLayerArnParam",
            parameter_name=f"/axrail/{self.env_name}/layers/powertools-layer-arn",
            string_value=self.powertools_layer.layer_version_arn,
        )

    def _create_lambda_role(self) -> None:
        self.lambda_role = iam.Role(
            self,
            "AuthLambdaRole",
            role_name=f"AXRAIL-AuthLambdaRole-{self.env_name}",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AWSXRayDaemonWriteAccess"),
            ],
        )
        
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
                ],
                resources=["*"],
            )
        )
        
        self.lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "dynamodb:PutItem",
                    "dynamodb:GetItem",
                    "dynamodb:UpdateItem",
                    "dynamodb:DeleteItem",
                    "dynamodb:Query",
                    "dynamodb:Scan",
                ],
                resources=["*"],
            )
        )

    def _create_exports(self) -> None:
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
        
        CfnOutput(
            self,
            "LambdaRoleArn",
            value=self.lambda_role.role_arn,
            export_name=f"AXRAIL-AuthLambdaRoleArn-{self.env_name}",
        )
