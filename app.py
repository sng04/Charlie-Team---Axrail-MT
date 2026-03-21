#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stack_cdk.dynamodb_stack import DynamoDBStack
from stack_cdk.cognito_stack import CognitoStack
from stack_cdk.meeting_bot_stack import MeetingBotStack
from stack_cdk.lambda_stack import LambdaStack
from stack_cdk.api_services_stack import ApiServicesStack
from stack_cdk.bedrock_agent_stack import BedrockAgentStack
from stack_cdk.environment import get_environment


app = cdk.App()

environment = app.node.try_get_context("environment") or "dev"
env_config = get_environment(environment)

env = cdk.Environment(
    account=env_config["account"],
    region=env_config["region"],
)

dynamodb_stack = DynamoDBStack(
    app,
    f"AXRAIL-DynamoDB-{environment}",
    env_name=environment,
    env_config=env_config,
    env=env,
)

cognito_stack = CognitoStack(
    app,
    f"AXRAIL-Cognito-{environment}",
    env_name=environment,
    env=env,
)

meeting_bot_stack = MeetingBotStack(
    app,
    f"AXRAIL-MeetingBot-{environment}",
    environment=environment,
    transcripts_table_arn=dynamodb_stack.transcripts_table.table_arn,
    sessions_table_arn=dynamodb_stack.sessions_table.table_arn,
    projects_table_arn=dynamodb_stack.projects_table.table_arn,
    bot_credentials_table_arn=dynamodb_stack.bot_credentials_table.table_arn,
    bot_pool_table_arn=dynamodb_stack.bot_pool_table.table_arn,
    bot_pool_table_name=dynamodb_stack.bot_pool_table.table_name,
    env=env,
)

lambda_stack = LambdaStack(
    app,
    f"AXRAIL-Lambda-{environment}",
    env_name=environment,
    dynamodb_stack=dynamodb_stack,
    cognito_stack=cognito_stack,
    meeting_bot_stack=meeting_bot_stack,
    ses_sender_email=env_config["ses_sender_email"],
    admin_email=env_config["admin_email"],
    admin_temp_password=env_config["admin_temp_password"],
    env_config=env_config,
    env=env,
)

api_services_stack = ApiServicesStack(
    app,
    f"AXRAIL-ApiServices-{environment}",
    env_name=environment,
    lambda_stack=lambda_stack,
    env=env,
)

lambda_stack.add_dependency(dynamodb_stack)
lambda_stack.add_dependency(cognito_stack)
lambda_stack.add_dependency(meeting_bot_stack)

meeting_bot_stack.add_dependency(dynamodb_stack)

api_services_stack.add_dependency(lambda_stack)

# Bedrock Agent stack (deployed to us-east-1, cross-region)
env_us_east_1 = cdk.Environment(
    account=env_config["account"],
    region=env_config["bedrock_region"],
)

bedrock_stack = BedrockAgentStack(
    app,
    f"AXRAIL-BedrockAgent-{environment}",
    env=env_us_east_1,
)

app.synth()
