from aws_cdk import (
    Stack,
    RemovalPolicy,
    aws_dynamodb as dynamodb,
    CfnOutput,
)
from constructs import Construct


class DynamoDBStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, *, env_name: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        self.env_name = env_name
        
        self._create_users_table()
        self._create_projects_table()
        self._create_project_users_table()
        self._create_exports()

    def _create_users_table(self) -> None:
        removal_policy = RemovalPolicy.DESTROY if self.env_name == "dev" else RemovalPolicy.RETAIN
        
        self.users_table = dynamodb.Table(
            self,
            "UsersTable",
            table_name=f"{self.env_name}-Users",
            partition_key=dynamodb.Attribute(
                name="user_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=removal_policy,
            point_in_time_recovery=self.env_name != "dev",
        )
        
        self.users_table.add_global_secondary_index(
            index_name="email-index",
            partition_key=dynamodb.Attribute(
                name="email",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_projects_table(self) -> None:
        removal_policy = RemovalPolicy.DESTROY if self.env_name == "dev" else RemovalPolicy.RETAIN
        
        self.projects_table = dynamodb.Table(
            self,
            "ProjectsTable",
            table_name=f"{self.env_name}-Projects",
            partition_key=dynamodb.Attribute(
                name="project_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=removal_policy,
            point_in_time_recovery=self.env_name != "dev",
        )

    def _create_project_users_table(self) -> None:
        removal_policy = RemovalPolicy.DESTROY if self.env_name == "dev" else RemovalPolicy.RETAIN
        
        self.project_users_table = dynamodb.Table(
            self,
            "ProjectUsersTable",
            table_name=f"{self.env_name}-ProjectUsers",
            partition_key=dynamodb.Attribute(
                name="project_user_id",
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=removal_policy,
            point_in_time_recovery=self.env_name != "dev",
        )
        
        self.project_users_table.add_global_secondary_index(
            index_name="project-index",
            partition_key=dynamodb.Attribute(
                name="project_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )
        
        self.project_users_table.add_global_secondary_index(
            index_name="user-index",
            partition_key=dynamodb.Attribute(
                name="user_id",
                type=dynamodb.AttributeType.STRING,
            ),
            projection_type=dynamodb.ProjectionType.ALL,
        )

    def _create_exports(self) -> None:
        CfnOutput(
            self,
            "UsersTableName",
            value=self.users_table.table_name,
            export_name=f"AXRAIL-UsersTableName-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "UsersTableArn",
            value=self.users_table.table_arn,
            export_name=f"AXRAIL-UsersTableArn-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "ProjectsTableName",
            value=self.projects_table.table_name,
            export_name=f"AXRAIL-ProjectsTableName-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "ProjectsTableArn",
            value=self.projects_table.table_arn,
            export_name=f"AXRAIL-ProjectsTableArn-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "ProjectUsersTableName",
            value=self.project_users_table.table_name,
            export_name=f"AXRAIL-ProjectUsersTableName-{self.env_name}",
        )
        
        CfnOutput(
            self,
            "ProjectUsersTableArn",
            value=self.project_users_table.table_arn,
            export_name=f"AXRAIL-ProjectUsersTableArn-{self.env_name}",
        )
