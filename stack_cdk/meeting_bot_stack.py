"""
Meeting Bot Stack

CDK Stack for Meeting Bot infrastructure (VPC, ECS, SQS for warm pool, etc).
Separated from other stacks because the resources are quite large.
"""

from aws_cdk import (
    Stack,
    RemovalPolicy,
    CfnOutput,
    Duration,
    CustomResource,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_iam as iam,
    aws_lambda as _lambda,
    aws_logs as logs,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_sqs as sqs,
    aws_ssm as ssm,
)
from aws_cdk.custom_resources import Provider
from constructs import Construct


class MeetingBotStack(Stack):
    """Stack for Meeting Bot ECS Fargate infrastructure with warm pool support."""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        *,
        environment: str,
        transcripts_table_arn: str,
        sessions_table_arn: str,
        projects_table_arn: str,
        bot_credentials_table_arn: str,
        bot_pool_table_arn: str,
        bot_pool_table_name: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self._environment = environment
        self._transcripts_table_arn = transcripts_table_arn
        self._sessions_table_arn = sessions_table_arn
        self._projects_table_arn = projects_table_arn
        self._bot_credentials_table_arn = bot_credentials_table_arn
        self._bot_pool_table_arn = bot_pool_table_arn
        self._bot_pool_table_name = bot_pool_table_name

        self._create_sqs_queue()
        self._create_vpc()
        self._create_security_group()
        self._create_ecs_cluster()
        self._create_transcribe_vocabulary()
        self._create_task_definition()
        self._create_outputs()

    def _create_sqs_queue(self) -> None:
        """Create SQS Queue for meeting requests."""
        self._meeting_queue = sqs.Queue(
            self,
            "MeetingRequestQueue",
            queue_name=f"{self._environment}-meeting-requests",
            visibility_timeout=Duration.minutes(15),
            retention_period=Duration.hours(1),
            receive_message_wait_time=Duration.seconds(20),
        )

    def _create_vpc(self) -> None:
        """Create VPC for ECS Fargate."""
        self._vpc = ec2.Vpc(
            self,
            "MeetingBotVpc",
            max_azs=2,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24,
                ),
                ec2.SubnetConfiguration(
                    name="Private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24,
                ),
            ],
        )

        self._vpc.add_interface_endpoint(
            "SecretsManagerEndpoint",
            service=ec2.InterfaceVpcEndpointAwsService.SECRETS_MANAGER,
        )
        self._vpc.add_interface_endpoint(
            "EcrEndpoint",
            service=ec2.InterfaceVpcEndpointAwsService.ECR,
        )
        self._vpc.add_interface_endpoint(
            "EcrDockerEndpoint",
            service=ec2.InterfaceVpcEndpointAwsService.ECR_DOCKER,
        )
        self._vpc.add_interface_endpoint(
            "LogsEndpoint",
            service=ec2.InterfaceVpcEndpointAwsService.CLOUDWATCH_LOGS,
        )
        self._vpc.add_gateway_endpoint(
            "DynamoDBEndpoint",
            service=ec2.GatewayVpcEndpointAwsService.DYNAMODB,
        )
        self._vpc.add_gateway_endpoint(
            "S3Endpoint",
            service=ec2.GatewayVpcEndpointAwsService.S3,
        )

    def _create_security_group(self) -> None:
        """Create Security Group for ECS tasks."""
        self._task_sg = ec2.SecurityGroup(
            self,
            "MeetingBotSecurityGroup",
            vpc=self._vpc,
            description="Security group for Meeting Bot ECS tasks",
            allow_all_outbound=True,
        )

    def _create_ecs_cluster(self) -> None:
        """Create ECS Cluster."""
        self._cluster = ecs.Cluster(
            self,
            "MeetingBotCluster",
            cluster_name=f"{self._environment}-meeting-bot",
            vpc=self._vpc,
            container_insights_v2=ecs.ContainerInsights.ENABLED,
        )

    def _create_transcribe_vocabulary(self) -> None:
        """Upload vocab file to S3 and create/update Transcribe custom vocabulary."""
        self._vocab_name = f"{self._environment}-tech-vocabulary"

        # S3 bucket for vocabulary file
        self._vocab_bucket = s3.Bucket(
            self,
            "VocabularyBucket",
            bucket_name=f"axrail-{self._environment}-transcribe-vocab-{self.account}",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        # Upload the vocab table file
        vocab_deployment = s3deploy.BucketDeployment(
            self,
            "VocabularyDeployment",
            sources=[s3deploy.Source.asset("resources", exclude=["*", "!tech-vocab-table.txt"])],
            destination_bucket=self._vocab_bucket,
            destination_key_prefix="vocabulary",
        )

        vocab_s3_uri = f"s3://{self._vocab_bucket.bucket_name}/vocabulary/tech-vocab-table.txt"

        # Lambda for custom resource to manage Transcribe vocabulary
        vocab_handler = _lambda.Function(
            self,
            "VocabularyHandler",
            function_name=f"AXRAIL-{self._environment}-TranscribeVocabulary",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="lambda_function.handler",
            code=_lambda.Code.from_asset("lambdas/Functions/ManageTranscribeVocabulary"),
            timeout=Duration.minutes(5),
            memory_size=128,
        )

        vocab_handler.add_to_role_policy(
            iam.PolicyStatement(
                actions=[
                    "transcribe:CreateVocabulary",
                    "transcribe:UpdateVocabulary",
                    "transcribe:DeleteVocabulary",
                    "transcribe:GetVocabulary",
                ],
                resources=["*"],
            )
        )

        vocab_handler.add_to_role_policy(
            iam.PolicyStatement(
                actions=["s3:GetObject"],
                resources=[f"{self._vocab_bucket.bucket_arn}/*"],
            )
        )

        provider = Provider(
            self,
            "VocabularyProvider",
            on_event_handler=vocab_handler,
        )

        self._vocab_resource = CustomResource(
            self,
            "TranscribeVocabulary",
            service_token=provider.service_token,
            properties={
                "VocabularyName": self._vocab_name,
                "LanguageCode": "en-US",
                "VocabularyFileUri": vocab_s3_uri,
            },
        )
        self._vocab_resource.node.add_dependency(vocab_deployment)

    def _create_task_definition(self) -> None:
        """Create Fargate Task Definition."""
        self._log_group = logs.LogGroup(
            self,
            "MeetingBotLogs",
            log_group_name=f"/ecs/{self._environment}/meeting-bot",
            retention=logs.RetentionDays.ONE_WEEK,
            removal_policy=RemovalPolicy.DESTROY,
        )

        execution_role = iam.Role(
            self,
            "MeetingBotExecutionRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name(
                    "service-role/AmazonECSTaskExecutionRolePolicy"
                )
            ],
        )

        execution_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["secretsmanager:GetSecretValue"],
                resources=[
                    f"arn:aws:secretsmanager:{self.region}:{self.account}:secret:{self._environment}/bot-credentials/*"
                ],
            )
        )

        task_role = iam.Role(
            self,
            "MeetingBotTaskRole",
            assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
        )

        task_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "transcribe:StartStreamTranscription",
                    "transcribe:StartStreamTranscriptionWebSocket",
                ],
                resources=["*"],
            )
        )

        task_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "dynamodb:PutItem",
                    "dynamodb:UpdateItem",
                    "dynamodb:GetItem",
                    "dynamodb:DeleteItem",
                    "dynamodb:Query",
                ],
                resources=[
                    self._transcripts_table_arn,
                    self._sessions_table_arn,
                    self._projects_table_arn,
                    self._bot_credentials_table_arn,
                    self._bot_pool_table_arn,
                    f"{self._bot_pool_table_arn}/index/*",
                ],
            )
        )

        task_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "sqs:ReceiveMessage",
                    "sqs:DeleteMessage",
                    "sqs:GetQueueAttributes",
                    "sqs:ChangeMessageVisibility",
                ],
                resources=[self._meeting_queue.queue_arn],
            )
        )

        task_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["secretsmanager:GetSecretValue"],
                resources=[
                    f"arn:aws:secretsmanager:{self.region}:{self.account}:secret:{self._environment}/bot-credentials/*"
                ],
            )
        )

        # Permission to post to WebSocket API for real-time transcript broadcast
        task_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=["execute-api:ManageConnections"],
                resources=[f"arn:aws:execute-api:{self.region}:{self.account}:*/*/*/*"],
            )
        )

        self._task_definition = ecs.FargateTaskDefinition(
            self,
            "MeetingBotTask",
            family=f"{self._environment}-meeting-bot",
            cpu=512,
            memory_limit_mib=1024,
            execution_role=execution_role,
            task_role=task_role,
        )

        self._task_definition.add_container(
            "MeetingBotContainer",
            container_name="MeetingBotContainer",
            image=ecs.ContainerImage.from_asset("./meeting_bot"),
            logging=ecs.LogDrivers.aws_logs(
                stream_prefix="meeting-bot",
                log_group=self._log_group,
            ),
            environment={
                "BROWSER_HEADLESS": "true",
                "BROWSER_TYPE": "firefox",
                "KEEP_ALIVE_INTERVAL": "30",
                "LOG_LEVEL": "INFO",
                "ENABLE_TRANSCRIPTION": "true",
                "TRANSCRIBE_LANGUAGE": "en-US",
                "TRANSCRIBE_VOCABULARY_NAME": self._vocab_name,
                "AWS_REGION": self.region,
                "ENVIRONMENT": self._environment,
                "SQS_QUEUE_URL": self._meeting_queue.queue_url,
                "BOT_POOL_TABLE": self._bot_pool_table_name,
                "WARM_POOL_MODE": "true",
            },
        )

    def _create_outputs(self) -> None:
        """Create CloudFormation outputs."""
        CfnOutput(self, "ClusterName", value=self._cluster.cluster_name)
        CfnOutput(self, "ClusterArn", value=self._cluster.cluster_arn)
        CfnOutput(
            self, "TaskDefinitionArn", value=self._task_definition.task_definition_arn
        )
        CfnOutput(self, "LogGroupName", value=self._log_group.log_group_name)
        CfnOutput(self, "SecurityGroupId", value=self._task_sg.security_group_id)
        CfnOutput(self, "VpcId", value=self._vpc.vpc_id)
        CfnOutput(
            self, "PrivateSubnetIds",
            value=",".join([s.subnet_id for s in self._vpc.private_subnets]),
        )
        CfnOutput(self, "MeetingQueueUrl", value=self._meeting_queue.queue_url)
        CfnOutput(self, "MeetingQueueArn", value=self._meeting_queue.queue_arn)

        # Store volatile values in SSM to avoid cross-stack export issues
        ssm.StringParameter(
            self, "TaskDefinitionArnParam",
            parameter_name=f"/axrail/{self._environment}/task-definition-arn",
            string_value=self._task_definition.task_definition_arn,
            description="ECS task definition ARN for meeting bot",
        )
        ssm.StringParameter(
            self, "ClusterArnParam",
            parameter_name=f"/axrail/{self._environment}/cluster-arn",
            string_value=self._cluster.cluster_arn,
            description="ECS cluster ARN for meeting bot",
        )
        ssm.StringParameter(
            self, "ClusterNameParam",
            parameter_name=f"/axrail/{self._environment}/cluster-name",
            string_value=self._cluster.cluster_name,
            description="ECS cluster name for meeting bot",
        )
        ssm.StringParameter(
            self, "SecurityGroupIdParam",
            parameter_name=f"/axrail/{self._environment}/security-group-id",
            string_value=self._task_sg.security_group_id,
            description="Security group ID for meeting bot tasks",
        )
        ssm.StringParameter(
            self, "PrivateSubnetIdsParam",
            parameter_name=f"/axrail/{self._environment}/private-subnet-ids",
            string_value=",".join([s.subnet_id for s in self._vpc.private_subnets]),
            description="Private subnet IDs for meeting bot tasks",
        )
        ssm.StringParameter(
            self, "MeetingQueueUrlParam",
            parameter_name=f"/axrail/{self._environment}/meeting-queue-url",
            string_value=self._meeting_queue.queue_url,
            description="SQS queue URL for meeting requests",
        )
        ssm.StringParameter(
            self, "MeetingQueueArnParam",
            parameter_name=f"/axrail/{self._environment}/meeting-queue-arn",
            string_value=self._meeting_queue.queue_arn,
            description="SQS queue ARN for meeting requests",
        )

    @property
    def cluster(self) -> ecs.Cluster:
        return self._cluster

    @property
    def cluster_arn(self) -> str:
        return self._cluster.cluster_arn

    @property
    def task_definition_arn(self) -> str:
        return self._task_definition.task_definition_arn

    @property
    def security_group_id(self) -> str:
        return self._task_sg.security_group_id

    @property
    def private_subnet_ids(self) -> list:
        return [s.subnet_id for s in self._vpc.private_subnets]

    @property
    def log_group_name(self) -> str:
        return self._log_group.log_group_name

    @property
    def meeting_queue_url(self) -> str:
        return self._meeting_queue.queue_url

    @property
    def meeting_queue_arn(self) -> str:
        return self._meeting_queue.queue_arn
