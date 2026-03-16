from aws_cdk import (
    Stack,
    RemovalPolicy,
    Duration,
    aws_cognito as cognito,
    CfnOutput,
)
from constructs import Construct


class CognitoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, *, env_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.env_name = env_name
        
        self._create_user_pool()
        self._create_user_pool_client()
        self._create_groups()
        self._create_exports()

    def _create_user_pool(self) -> None:
        removal_policy = RemovalPolicy.DESTROY if self.env_name == "dev" else RemovalPolicy.RETAIN
        
        self.user_pool = cognito.UserPool(
            self,
            "UserPool",
            user_pool_name=f"AXRAIL-UserPool-{self.env_name}",
            self_sign_up_enabled=False,
            sign_in_aliases=cognito.SignInAliases(
                email=True,
                username=True,
            ),
            auto_verify=cognito.AutoVerifiedAttrs(
                email=True,
            ),
            standard_attributes=cognito.StandardAttributes(
                email=cognito.StandardAttribute(
                    required=True,
                    mutable=True,
                ),
            ),
            password_policy=cognito.PasswordPolicy(
                min_length=8,
                require_lowercase=True,
                require_uppercase=True,
                require_digits=True,
                require_symbols=True,
                temp_password_validity=Duration.days(7),
            ),
            account_recovery=cognito.AccountRecovery.EMAIL_ONLY,
            removal_policy=removal_policy,
        )

    def _create_user_pool_client(self) -> None:
        self.user_pool_client = self.user_pool.add_client(
            "UserPoolClient",
            user_pool_client_name=f"AXRAIL-Client-{self.env_name}",
            auth_flows=cognito.AuthFlow(
                user_password=True,
                user_srp=True,
            ),
            generate_secret=False,
            access_token_validity=Duration.hours(1),
            id_token_validity=Duration.hours(1),
            refresh_token_validity=Duration.days(30),
        )

    def _create_groups(self) -> None:
        cognito.CfnUserPoolGroup(
            self,
            "AdminGroup",
            user_pool_id=self.user_pool.user_pool_id,
            group_name="admin",
            description="Administrator group with full access",
            precedence=1,
        )
        
        cognito.CfnUserPoolGroup(
            self,
            "UserGroup",
            user_pool_id=self.user_pool.user_pool_id,
            group_name="user",
            description="Regular user group",
            precedence=10,
        )

    def _create_exports(self) -> None:
        CfnOutput(
            self,
            "UserPoolId",
            value=self.user_pool.user_pool_id,
            export_name=f"AXRAIL-UserPoolId-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "UserPoolArn",
            value=self.user_pool.user_pool_arn,
            export_name=f"AXRAIL-UserPoolArn-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "UserPoolClientId",
            value=self.user_pool_client.user_pool_client_id,
            export_name=f"AXRAIL-UserPoolClientId-{self.env_name}",
        )
