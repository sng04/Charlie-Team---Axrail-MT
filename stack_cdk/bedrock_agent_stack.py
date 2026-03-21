"""
Bedrock Agent Stack.

Defines all Amazon Bedrock-related resources deployed to us-east-1,
including a Nova Pro-backed agent and a test Lambda for verification.
"""

from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_iam as iam,
)
from constructs import Construct
from cdklabs.generative_ai_cdk_constructs import bedrock


AGENT_INSTRUCTION = (
    "You are an AI Meeting Assistant. Your role is to answer questions "
    "about meetings, including topics discussed, action items, decisions "
    "made, and participant information. Provide clear, concise, and "
    "accurate responses based on the meeting context provided."
)

LAMBDA_HANDLER_CODE = """\
import json
import os
import uuid

import boto3

AGENT_ID = os.environ["AGENT_ID"]
AGENT_ALIAS_ID = os.environ["AGENT_ALIAS_ID"]

client = boto3.client("bedrock-agent-runtime")


def handler(event, context):
    prompt = event.get("prompt", "")
    session_id = event.get("session_id", str(uuid.uuid4()))

    if not prompt or not prompt.strip():
        return {
            "statusCode": 400,
            "body": {"error": "prompt is required and must be non-empty"},
        }

    try:
        response = client.invoke_agent(
            agentId=AGENT_ID,
            agentAliasId=AGENT_ALIAS_ID,
            sessionId=session_id,
            inputText=prompt,
        )

        completion = ""
        for event_chunk in response.get("completion", []):
            chunk = event_chunk.get("chunk", {})
            if "bytes" in chunk:
                completion += chunk["bytes"].decode("utf-8")

        return {
            "statusCode": 200,
            "body": {"response": completion, "session_id": session_id},
        }
    except Exception as exc:
        return {"statusCode": 500, "body": {"error": str(exc)}}
"""


class BedrockAgentStack(Stack):
    """CDK stack for Bedrock Agent resources in us-east-1."""

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self._create_agent()
        self._create_test_lambda()

    def _create_agent(self) -> None:
        """Create the Bedrock Agent with Nova Pro model and an alias."""
        foundation_model = bedrock.BedrockFoundationModel(
            "amazon.nova-pro-v1:0",
            supports_agents=True,
        )

        self.agent = bedrock.Agent(
            self,
            "MeetingAssistantAgent",
            foundation_model=foundation_model,
            instruction=AGENT_INSTRUCTION,
            should_prepare_agent=True,
        )

        self.agent_alias = bedrock.AgentAlias(
            self,
            "MeetingAssistantAgentAlias",
            agent=self.agent,
            alias_name="live",
        )

    def _create_test_lambda(self) -> None:
        """Create a test Lambda that invokes the Bedrock Agent."""
        test_fn = _lambda.Function(
            self,
            "TestInvokeAgentFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="index.handler",
            code=_lambda.Code.from_inline(LAMBDA_HANDLER_CODE),
            timeout=Duration.seconds(60),
            environment={
                "AGENT_ID": self.agent.agent_id,
                "AGENT_ALIAS_ID": self.agent_alias.alias_id,
            },
        )

        test_fn.add_to_role_policy(
            iam.PolicyStatement(
                actions=["bedrock:InvokeAgent"],
                resources=["*"],
            )
        )
