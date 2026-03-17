"""Unit tests for BedrockAgentStack CDK template."""

import aws_cdk as cdk
import aws_cdk.assertions as assertions
import pytest

from bedrock_agent.bedrock_agent_stack import BedrockAgentStack


@pytest.fixture
def template():
    """Synthesize the BedrockAgentStack and return the template."""
    app = cdk.App()
    stack = BedrockAgentStack(app, "TestBedrockAgentStack")
    return assertions.Template.from_stack(stack)


def test_stack_synthesizes_without_errors():
    """Stack synthesizes without errors."""
    app = cdk.App()
    stack = BedrockAgentStack(app, "SynthTestStack")
    template = assertions.Template.from_stack(stack)
    assert template is not None


def test_bedrock_agent_has_correct_foundation_model(template):
    """Template contains AWS::Bedrock::Agent with Nova Pro model."""
    resources = template.find_resources("AWS::Bedrock::Agent")
    assert len(resources) > 0

    agent_resource = list(resources.values())[0]
    foundation_model = agent_resource["Properties"]["FoundationModel"]

    # The model ARN is constructed via Fn::Join; verify it ends with the model ID.
    assert foundation_model["Fn::Join"][0] == ""
    joined_parts = foundation_model["Fn::Join"][1]
    assert joined_parts[-1] == "::foundation-model/amazon.nova-pro-v1:0"


def test_agent_instruction_mentions_meeting_assistant(template):
    """Agent instruction references meeting assistant (case-insensitive)."""
    resources = template.find_resources("AWS::Bedrock::Agent")
    agent_resource = list(resources.values())[0]
    instruction = agent_resource["Properties"]["Instruction"]
    assert "meeting assistant" in instruction.lower()


def test_template_contains_agent_alias(template):
    """Template contains AWS::Bedrock::AgentAlias."""
    template.resource_count_is("AWS::Bedrock::AgentAlias", 1)


def test_lambda_has_python311_runtime(template):
    """Lambda function uses Python 3.11 runtime."""
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {"Runtime": "python3.11"},
    )


def test_lambda_has_60_second_timeout(template):
    """Lambda function has a 60-second timeout."""
    template.has_resource_properties(
        "AWS::Lambda::Function",
        {"Timeout": 60},
    )


def test_lambda_iam_policy_includes_invoke_agent(template):
    """Lambda IAM policy includes bedrock-agent-runtime:InvokeAgent."""
    template.has_resource_properties(
        "AWS::IAM::Policy",
        assertions.Match.object_like({
            "PolicyDocument": {
                "Statement": assertions.Match.array_with([
                    assertions.Match.object_like({
                        "Action": "bedrock:InvokeAgent",
                        "Effect": "Allow",
                    }),
                ]),
            },
        }),
    )


def test_agent_iam_role_includes_invoke_model(template):
    """Agent IAM role policy includes bedrock:InvokeModel."""
    template.has_resource_properties(
        "AWS::IAM::Policy",
        assertions.Match.object_like({
            "PolicyDocument": {
                "Statement": assertions.Match.array_with([
                    assertions.Match.object_like({
                        "Action": assertions.Match.array_with(
                            ["bedrock:InvokeModel*"]
                        ),
                        "Effect": "Allow",
                    }),
                ]),
            },
        }),
    )
