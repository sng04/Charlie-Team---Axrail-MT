#!/usr/bin/env python3
import os

import aws_cdk as cdk

from charlie_team___axrail_mt.dynamodb_stack import DynamoDBStack
from charlie_team___axrail_mt.cognito_stack import CognitoStack
from charlie_team___axrail_mt.meeting_bot_stack import MeetingBotStack
from charlie_team___axrail_mt.lambda_stack import LambdaStack
from charlie_team___axrail_mt.api_services_stack import ApiServicesStack
from charlie_team___axrail_mt.environment import get_environment


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

app.synth()
