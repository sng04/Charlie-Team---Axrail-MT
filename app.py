#!/usr/bin/env python3
import os

import aws_cdk as cdk

from charlie_team___axrail_mt.shared_resources_stack import SharedResourcesStack
from charlie_team___axrail_mt.dynamodb_stack import DynamoDBStack
from charlie_team___axrail_mt.cognito_stack import CognitoStack
from charlie_team___axrail_mt.lambda_stack import LambdaStack
from charlie_team___axrail_mt.api_services_stack import ApiServicesStack
from charlie_team___axrail_mt.seed_admin_stack import SeedAdminStack
from charlie_team___axrail_mt.environment import get_environment


app = cdk.App()

environment = app.node.try_get_context("environment") or "dev"
env_config = get_environment(environment)

env = cdk.Environment(
    account=env_config["account"],
    region=env_config["region"],
)

shared_resources = SharedResourcesStack(
    app,
    f"AXRAIL-SharedResources-{environment}",
    env_name=environment,
    env=env,
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

lambda_stack = LambdaStack(
    app,
    f"AXRAIL-Lambda-{environment}",
    env_name=environment,
    shared_resources=shared_resources,
    dynamodb_stack=dynamodb_stack,
    cognito_stack=cognito_stack,
    env=env,
)

api_services_stack = ApiServicesStack(
    app,
    f"AXRAIL-ApiServices-{environment}",
    env_name=environment,
    lambda_stack=lambda_stack,
    env=env,
)

seed_admin_stack = SeedAdminStack(
    app,
    f"AXRAIL-SeedAdmin-{environment}",
    env_name=environment,
    dynamodb_stack=dynamodb_stack,
    cognito_stack=cognito_stack,
    admin_email="admin@axrail.com",
    admin_temp_password="TempAdmin@123",
    env=env,
)

lambda_stack.add_dependency(shared_resources)
lambda_stack.add_dependency(dynamodb_stack)
lambda_stack.add_dependency(cognito_stack)

api_services_stack.add_dependency(lambda_stack)

seed_admin_stack.add_dependency(cognito_stack)
seed_admin_stack.add_dependency(dynamodb_stack)

app.synth()
