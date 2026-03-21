"""CDK stack assertion tests for BedrockAgentStack.

Per testing-standards: 3-5 tests per resource covering creation,
env variance, and permissions.
"""

import aws_cdk as cdk
import aws_cdk.assertions as assertions
import pytest

from stack_cdk.bedrock_agent_stack import BedrockAgentStack


class TestBedrockAgentStack:
    """BedrockAgentStack: resource creation, model config, IAM permissions."""

    @pytest.fixture(autouse=True)
    def _setup(self):
        app = cdk.App()
        stack = BedrockAgentStack(app, "TestBedrockAgentStack")
        self.template = assertions.Template.from_stack(stack)

    def test_stack_synthesizes(self):
        assert self.template is not None

    def test_foundation_model_is_nova_pro(self):
        resources = self.template.find_resources("AWS::Bedrock::Agent")
        assert len(resources) > 0
        agent = list(resources.values())[0]
        joined_parts = agent["Properties"]["FoundationModel"]["Fn::Join"][1]
        assert joined_parts[-1] == "::foundation-model/amazon.nova-pro-v1:0"

    def test_agent_instruction_mentions_meeting_assistant(self):
        resources = self.template.find_resources("AWS::Bedrock::Agent")
        agent = list(resources.values())[0]
        assert "meeting assistant" in agent["Properties"]["Instruction"].lower()

    def test_agent_alias_created(self):
        self.template.resource_count_is("AWS::Bedrock::AgentAlias", 1)

    def test_lambda_runtime_and_timeout(self):
        self.template.has_resource_properties(
            "AWS::Lambda::Function",
            {"Runtime": "python3.11", "Timeout": 60},
        )

    def test_iam_policy_includes_invoke_agent(self):
        self.template.has_resource_properties(
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

    def test_iam_policy_includes_invoke_model(self):
        self.template.has_resource_properties(
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
