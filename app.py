#!/usr/bin/env python3
import os

import aws_cdk as cdk

from bedrock_agent.bedrock_agent_stack import BedrockAgentStack
from gmeet_agent.gmeet_agent_stack import GMeetAgentStack

app = cdk.App()

GMeetAgentStack(
    app,
    "GMeetAgentStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region="ap-southeast-1",
    ),
)

BedrockAgentStack(
    app,
    "BedrockAgentStack",
    env=cdk.Environment(
        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
        region="us-east-1",
    ),
)

app.synth()
