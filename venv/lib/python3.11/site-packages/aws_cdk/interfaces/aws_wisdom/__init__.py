from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from ..._jsii import *

import constructs as _constructs_77d1e7e8
from .. import IEnvironmentAware as _IEnvironmentAware_f39049ee


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.AIAgentReference",
    jsii_struct_bases=[],
    name_mapping={
        "ai_agent_arn": "aiAgentArn",
        "ai_agent_id": "aiAgentId",
        "assistant_id": "assistantId",
    },
)
class AIAgentReference:
    def __init__(
        self,
        *,
        ai_agent_arn: builtins.str,
        ai_agent_id: builtins.str,
        assistant_id: builtins.str,
    ) -> None:
        '''A reference to a AIAgent resource.

        :param ai_agent_arn: The ARN of the AIAgent resource.
        :param ai_agent_id: The AIAgentId of the AIAgent resource.
        :param assistant_id: The AssistantId of the AIAgent resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            a_iAgent_reference = interfaces_wisdom.AIAgentReference(
                ai_agent_arn="aiAgentArn",
                ai_agent_id="aiAgentId",
                assistant_id="assistantId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5c9f980da07d34883a98368cc7d4439a05c9661c54ad4701636ca1bde6d899a)
            check_type(argname="argument ai_agent_arn", value=ai_agent_arn, expected_type=type_hints["ai_agent_arn"])
            check_type(argname="argument ai_agent_id", value=ai_agent_id, expected_type=type_hints["ai_agent_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_agent_arn": ai_agent_arn,
            "ai_agent_id": ai_agent_id,
            "assistant_id": assistant_id,
        }

    @builtins.property
    def ai_agent_arn(self) -> builtins.str:
        '''The ARN of the AIAgent resource.'''
        result = self._values.get("ai_agent_arn")
        assert result is not None, "Required property 'ai_agent_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ai_agent_id(self) -> builtins.str:
        '''The AIAgentId of the AIAgent resource.'''
        result = self._values.get("ai_agent_id")
        assert result is not None, "Required property 'ai_agent_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The AssistantId of the AIAgent resource.'''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AIAgentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.AIAgentVersionReference",
    jsii_struct_bases=[],
    name_mapping={
        "ai_agent_id": "aiAgentId",
        "assistant_id": "assistantId",
        "version_number": "versionNumber",
    },
)
class AIAgentVersionReference:
    def __init__(
        self,
        *,
        ai_agent_id: builtins.str,
        assistant_id: builtins.str,
        version_number: builtins.str,
    ) -> None:
        '''A reference to a AIAgentVersion resource.

        :param ai_agent_id: The AIAgentId of the AIAgentVersion resource.
        :param assistant_id: The AssistantId of the AIAgentVersion resource.
        :param version_number: The VersionNumber of the AIAgentVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            a_iAgent_version_reference = interfaces_wisdom.AIAgentVersionReference(
                ai_agent_id="aiAgentId",
                assistant_id="assistantId",
                version_number="versionNumber"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df7b590b7f1d754e26a03c29ec446c8d6d6e0ccd43e8549d13dda2b64a1f148f)
            check_type(argname="argument ai_agent_id", value=ai_agent_id, expected_type=type_hints["ai_agent_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument version_number", value=version_number, expected_type=type_hints["version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_agent_id": ai_agent_id,
            "assistant_id": assistant_id,
            "version_number": version_number,
        }

    @builtins.property
    def ai_agent_id(self) -> builtins.str:
        '''The AIAgentId of the AIAgentVersion resource.'''
        result = self._values.get("ai_agent_id")
        assert result is not None, "Required property 'ai_agent_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The AssistantId of the AIAgentVersion resource.'''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_number(self) -> builtins.str:
        '''The VersionNumber of the AIAgentVersion resource.'''
        result = self._values.get("version_number")
        assert result is not None, "Required property 'version_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AIAgentVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.AIGuardrailReference",
    jsii_struct_bases=[],
    name_mapping={
        "ai_guardrail_arn": "aiGuardrailArn",
        "ai_guardrail_id": "aiGuardrailId",
        "assistant_id": "assistantId",
    },
)
class AIGuardrailReference:
    def __init__(
        self,
        *,
        ai_guardrail_arn: builtins.str,
        ai_guardrail_id: builtins.str,
        assistant_id: builtins.str,
    ) -> None:
        '''A reference to a AIGuardrail resource.

        :param ai_guardrail_arn: The ARN of the AIGuardrail resource.
        :param ai_guardrail_id: The AIGuardrailId of the AIGuardrail resource.
        :param assistant_id: The AssistantId of the AIGuardrail resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            a_iGuardrail_reference = interfaces_wisdom.AIGuardrailReference(
                ai_guardrail_arn="aiGuardrailArn",
                ai_guardrail_id="aiGuardrailId",
                assistant_id="assistantId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fa4d7e3096b174861d8134fc19ca8a9424037e513dd67917f5753076fe65a5c)
            check_type(argname="argument ai_guardrail_arn", value=ai_guardrail_arn, expected_type=type_hints["ai_guardrail_arn"])
            check_type(argname="argument ai_guardrail_id", value=ai_guardrail_id, expected_type=type_hints["ai_guardrail_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_guardrail_arn": ai_guardrail_arn,
            "ai_guardrail_id": ai_guardrail_id,
            "assistant_id": assistant_id,
        }

    @builtins.property
    def ai_guardrail_arn(self) -> builtins.str:
        '''The ARN of the AIGuardrail resource.'''
        result = self._values.get("ai_guardrail_arn")
        assert result is not None, "Required property 'ai_guardrail_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ai_guardrail_id(self) -> builtins.str:
        '''The AIGuardrailId of the AIGuardrail resource.'''
        result = self._values.get("ai_guardrail_id")
        assert result is not None, "Required property 'ai_guardrail_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The AssistantId of the AIGuardrail resource.'''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AIGuardrailReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.AIGuardrailVersionReference",
    jsii_struct_bases=[],
    name_mapping={
        "ai_guardrail_id": "aiGuardrailId",
        "assistant_id": "assistantId",
        "version_number": "versionNumber",
    },
)
class AIGuardrailVersionReference:
    def __init__(
        self,
        *,
        ai_guardrail_id: builtins.str,
        assistant_id: builtins.str,
        version_number: builtins.str,
    ) -> None:
        '''A reference to a AIGuardrailVersion resource.

        :param ai_guardrail_id: The AIGuardrailId of the AIGuardrailVersion resource.
        :param assistant_id: The AssistantId of the AIGuardrailVersion resource.
        :param version_number: The VersionNumber of the AIGuardrailVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            a_iGuardrail_version_reference = interfaces_wisdom.AIGuardrailVersionReference(
                ai_guardrail_id="aiGuardrailId",
                assistant_id="assistantId",
                version_number="versionNumber"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1504a5277569873463fc7fb8164b4ed9a3247ea857816478ee85d9f991c1399a)
            check_type(argname="argument ai_guardrail_id", value=ai_guardrail_id, expected_type=type_hints["ai_guardrail_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument version_number", value=version_number, expected_type=type_hints["version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_guardrail_id": ai_guardrail_id,
            "assistant_id": assistant_id,
            "version_number": version_number,
        }

    @builtins.property
    def ai_guardrail_id(self) -> builtins.str:
        '''The AIGuardrailId of the AIGuardrailVersion resource.'''
        result = self._values.get("ai_guardrail_id")
        assert result is not None, "Required property 'ai_guardrail_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The AssistantId of the AIGuardrailVersion resource.'''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_number(self) -> builtins.str:
        '''The VersionNumber of the AIGuardrailVersion resource.'''
        result = self._values.get("version_number")
        assert result is not None, "Required property 'version_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AIGuardrailVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.AIPromptReference",
    jsii_struct_bases=[],
    name_mapping={
        "ai_prompt_arn": "aiPromptArn",
        "ai_prompt_id": "aiPromptId",
        "assistant_id": "assistantId",
    },
)
class AIPromptReference:
    def __init__(
        self,
        *,
        ai_prompt_arn: builtins.str,
        ai_prompt_id: builtins.str,
        assistant_id: builtins.str,
    ) -> None:
        '''A reference to a AIPrompt resource.

        :param ai_prompt_arn: The ARN of the AIPrompt resource.
        :param ai_prompt_id: The AIPromptId of the AIPrompt resource.
        :param assistant_id: The AssistantId of the AIPrompt resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            a_iPrompt_reference = interfaces_wisdom.AIPromptReference(
                ai_prompt_arn="aiPromptArn",
                ai_prompt_id="aiPromptId",
                assistant_id="assistantId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da00bbb51042c62200cf26b300da1f1cf8fdd019213e51de295f69c453de7f01)
            check_type(argname="argument ai_prompt_arn", value=ai_prompt_arn, expected_type=type_hints["ai_prompt_arn"])
            check_type(argname="argument ai_prompt_id", value=ai_prompt_id, expected_type=type_hints["ai_prompt_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_prompt_arn": ai_prompt_arn,
            "ai_prompt_id": ai_prompt_id,
            "assistant_id": assistant_id,
        }

    @builtins.property
    def ai_prompt_arn(self) -> builtins.str:
        '''The ARN of the AIPrompt resource.'''
        result = self._values.get("ai_prompt_arn")
        assert result is not None, "Required property 'ai_prompt_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ai_prompt_id(self) -> builtins.str:
        '''The AIPromptId of the AIPrompt resource.'''
        result = self._values.get("ai_prompt_id")
        assert result is not None, "Required property 'ai_prompt_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The AssistantId of the AIPrompt resource.'''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AIPromptReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.AIPromptVersionReference",
    jsii_struct_bases=[],
    name_mapping={
        "ai_prompt_id": "aiPromptId",
        "assistant_id": "assistantId",
        "version_number": "versionNumber",
    },
)
class AIPromptVersionReference:
    def __init__(
        self,
        *,
        ai_prompt_id: builtins.str,
        assistant_id: builtins.str,
        version_number: builtins.str,
    ) -> None:
        '''A reference to a AIPromptVersion resource.

        :param ai_prompt_id: The AIPromptId of the AIPromptVersion resource.
        :param assistant_id: The AssistantId of the AIPromptVersion resource.
        :param version_number: The VersionNumber of the AIPromptVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            a_iPrompt_version_reference = interfaces_wisdom.AIPromptVersionReference(
                ai_prompt_id="aiPromptId",
                assistant_id="assistantId",
                version_number="versionNumber"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__069cc2f0d138e268a2b17ac010b7fb4fa3bc49052926c62d0f383348f06c158e)
            check_type(argname="argument ai_prompt_id", value=ai_prompt_id, expected_type=type_hints["ai_prompt_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
            check_type(argname="argument version_number", value=version_number, expected_type=type_hints["version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ai_prompt_id": ai_prompt_id,
            "assistant_id": assistant_id,
            "version_number": version_number,
        }

    @builtins.property
    def ai_prompt_id(self) -> builtins.str:
        '''The AIPromptId of the AIPromptVersion resource.'''
        result = self._values.get("ai_prompt_id")
        assert result is not None, "Required property 'ai_prompt_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The AssistantId of the AIPromptVersion resource.'''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version_number(self) -> builtins.str:
        '''The VersionNumber of the AIPromptVersion resource.'''
        result = self._values.get("version_number")
        assert result is not None, "Required property 'version_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AIPromptVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.AssistantAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "assistant_association_arn": "assistantAssociationArn",
        "assistant_association_id": "assistantAssociationId",
        "assistant_id": "assistantId",
    },
)
class AssistantAssociationReference:
    def __init__(
        self,
        *,
        assistant_association_arn: builtins.str,
        assistant_association_id: builtins.str,
        assistant_id: builtins.str,
    ) -> None:
        '''A reference to a AssistantAssociation resource.

        :param assistant_association_arn: The ARN of the AssistantAssociation resource.
        :param assistant_association_id: The AssistantAssociationId of the AssistantAssociation resource.
        :param assistant_id: The AssistantId of the AssistantAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            assistant_association_reference = interfaces_wisdom.AssistantAssociationReference(
                assistant_association_arn="assistantAssociationArn",
                assistant_association_id="assistantAssociationId",
                assistant_id="assistantId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79de64bf9a32f58953346e98715c2172e750981e9f09141629b8000b2e0b8799)
            check_type(argname="argument assistant_association_arn", value=assistant_association_arn, expected_type=type_hints["assistant_association_arn"])
            check_type(argname="argument assistant_association_id", value=assistant_association_id, expected_type=type_hints["assistant_association_id"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assistant_association_arn": assistant_association_arn,
            "assistant_association_id": assistant_association_id,
            "assistant_id": assistant_id,
        }

    @builtins.property
    def assistant_association_arn(self) -> builtins.str:
        '''The ARN of the AssistantAssociation resource.'''
        result = self._values.get("assistant_association_arn")
        assert result is not None, "Required property 'assistant_association_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_association_id(self) -> builtins.str:
        '''The AssistantAssociationId of the AssistantAssociation resource.'''
        result = self._values.get("assistant_association_id")
        assert result is not None, "Required property 'assistant_association_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The AssistantId of the AssistantAssociation resource.'''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssistantAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.AssistantReference",
    jsii_struct_bases=[],
    name_mapping={"assistant_arn": "assistantArn", "assistant_id": "assistantId"},
)
class AssistantReference:
    def __init__(
        self,
        *,
        assistant_arn: builtins.str,
        assistant_id: builtins.str,
    ) -> None:
        '''A reference to a Assistant resource.

        :param assistant_arn: The ARN of the Assistant resource.
        :param assistant_id: The AssistantId of the Assistant resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            assistant_reference = interfaces_wisdom.AssistantReference(
                assistant_arn="assistantArn",
                assistant_id="assistantId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ce10c49e9f56a127e62a262a788ac22afd2d17753177a2250d015beb74071f2)
            check_type(argname="argument assistant_arn", value=assistant_arn, expected_type=type_hints["assistant_arn"])
            check_type(argname="argument assistant_id", value=assistant_id, expected_type=type_hints["assistant_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "assistant_arn": assistant_arn,
            "assistant_id": assistant_id,
        }

    @builtins.property
    def assistant_arn(self) -> builtins.str:
        '''The ARN of the Assistant resource.'''
        result = self._values.get("assistant_arn")
        assert result is not None, "Required property 'assistant_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def assistant_id(self) -> builtins.str:
        '''The AssistantId of the Assistant resource.'''
        result = self._values.get("assistant_id")
        assert result is not None, "Required property 'assistant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssistantReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IAIAgentRef")
class IAIAgentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AIAgent.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aiAgentRef")
    def ai_agent_ref(self) -> "AIAgentReference":
        '''(experimental) A reference to a AIAgent resource.

        :stability: experimental
        '''
        ...


class _IAIAgentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AIAgent.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IAIAgentRef"

    @builtins.property
    @jsii.member(jsii_name="aiAgentRef")
    def ai_agent_ref(self) -> "AIAgentReference":
        '''(experimental) A reference to a AIAgent resource.

        :stability: experimental
        '''
        return typing.cast("AIAgentReference", jsii.get(self, "aiAgentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAIAgentRef).__jsii_proxy_class__ = lambda : _IAIAgentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IAIAgentVersionRef")
class IAIAgentVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AIAgentVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aiAgentVersionRef")
    def ai_agent_version_ref(self) -> "AIAgentVersionReference":
        '''(experimental) A reference to a AIAgentVersion resource.

        :stability: experimental
        '''
        ...


class _IAIAgentVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AIAgentVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IAIAgentVersionRef"

    @builtins.property
    @jsii.member(jsii_name="aiAgentVersionRef")
    def ai_agent_version_ref(self) -> "AIAgentVersionReference":
        '''(experimental) A reference to a AIAgentVersion resource.

        :stability: experimental
        '''
        return typing.cast("AIAgentVersionReference", jsii.get(self, "aiAgentVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAIAgentVersionRef).__jsii_proxy_class__ = lambda : _IAIAgentVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IAIGuardrailRef")
class IAIGuardrailRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AIGuardrail.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aiGuardrailRef")
    def ai_guardrail_ref(self) -> "AIGuardrailReference":
        '''(experimental) A reference to a AIGuardrail resource.

        :stability: experimental
        '''
        ...


class _IAIGuardrailRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AIGuardrail.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IAIGuardrailRef"

    @builtins.property
    @jsii.member(jsii_name="aiGuardrailRef")
    def ai_guardrail_ref(self) -> "AIGuardrailReference":
        '''(experimental) A reference to a AIGuardrail resource.

        :stability: experimental
        '''
        return typing.cast("AIGuardrailReference", jsii.get(self, "aiGuardrailRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAIGuardrailRef).__jsii_proxy_class__ = lambda : _IAIGuardrailRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IAIGuardrailVersionRef")
class IAIGuardrailVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AIGuardrailVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aiGuardrailVersionRef")
    def ai_guardrail_version_ref(self) -> "AIGuardrailVersionReference":
        '''(experimental) A reference to a AIGuardrailVersion resource.

        :stability: experimental
        '''
        ...


class _IAIGuardrailVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AIGuardrailVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IAIGuardrailVersionRef"

    @builtins.property
    @jsii.member(jsii_name="aiGuardrailVersionRef")
    def ai_guardrail_version_ref(self) -> "AIGuardrailVersionReference":
        '''(experimental) A reference to a AIGuardrailVersion resource.

        :stability: experimental
        '''
        return typing.cast("AIGuardrailVersionReference", jsii.get(self, "aiGuardrailVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAIGuardrailVersionRef).__jsii_proxy_class__ = lambda : _IAIGuardrailVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IAIPromptRef")
class IAIPromptRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AIPrompt.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aiPromptRef")
    def ai_prompt_ref(self) -> "AIPromptReference":
        '''(experimental) A reference to a AIPrompt resource.

        :stability: experimental
        '''
        ...


class _IAIPromptRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AIPrompt.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IAIPromptRef"

    @builtins.property
    @jsii.member(jsii_name="aiPromptRef")
    def ai_prompt_ref(self) -> "AIPromptReference":
        '''(experimental) A reference to a AIPrompt resource.

        :stability: experimental
        '''
        return typing.cast("AIPromptReference", jsii.get(self, "aiPromptRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAIPromptRef).__jsii_proxy_class__ = lambda : _IAIPromptRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IAIPromptVersionRef")
class IAIPromptVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AIPromptVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aiPromptVersionRef")
    def ai_prompt_version_ref(self) -> "AIPromptVersionReference":
        '''(experimental) A reference to a AIPromptVersion resource.

        :stability: experimental
        '''
        ...


class _IAIPromptVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AIPromptVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IAIPromptVersionRef"

    @builtins.property
    @jsii.member(jsii_name="aiPromptVersionRef")
    def ai_prompt_version_ref(self) -> "AIPromptVersionReference":
        '''(experimental) A reference to a AIPromptVersion resource.

        :stability: experimental
        '''
        return typing.cast("AIPromptVersionReference", jsii.get(self, "aiPromptVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAIPromptVersionRef).__jsii_proxy_class__ = lambda : _IAIPromptVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IAssistantAssociationRef")
class IAssistantAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AssistantAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="assistantAssociationRef")
    def assistant_association_ref(self) -> "AssistantAssociationReference":
        '''(experimental) A reference to a AssistantAssociation resource.

        :stability: experimental
        '''
        ...


class _IAssistantAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AssistantAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IAssistantAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="assistantAssociationRef")
    def assistant_association_ref(self) -> "AssistantAssociationReference":
        '''(experimental) A reference to a AssistantAssociation resource.

        :stability: experimental
        '''
        return typing.cast("AssistantAssociationReference", jsii.get(self, "assistantAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssistantAssociationRef).__jsii_proxy_class__ = lambda : _IAssistantAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IAssistantRef")
class IAssistantRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Assistant.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="assistantRef")
    def assistant_ref(self) -> "AssistantReference":
        '''(experimental) A reference to a Assistant resource.

        :stability: experimental
        '''
        ...


class _IAssistantRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Assistant.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IAssistantRef"

    @builtins.property
    @jsii.member(jsii_name="assistantRef")
    def assistant_ref(self) -> "AssistantReference":
        '''(experimental) A reference to a Assistant resource.

        :stability: experimental
        '''
        return typing.cast("AssistantReference", jsii.get(self, "assistantRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssistantRef).__jsii_proxy_class__ = lambda : _IAssistantRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IKnowledgeBaseRef")
class IKnowledgeBaseRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a KnowledgeBase.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="knowledgeBaseRef")
    def knowledge_base_ref(self) -> "KnowledgeBaseReference":
        '''(experimental) A reference to a KnowledgeBase resource.

        :stability: experimental
        '''
        ...


class _IKnowledgeBaseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a KnowledgeBase.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IKnowledgeBaseRef"

    @builtins.property
    @jsii.member(jsii_name="knowledgeBaseRef")
    def knowledge_base_ref(self) -> "KnowledgeBaseReference":
        '''(experimental) A reference to a KnowledgeBase resource.

        :stability: experimental
        '''
        return typing.cast("KnowledgeBaseReference", jsii.get(self, "knowledgeBaseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKnowledgeBaseRef).__jsii_proxy_class__ = lambda : _IKnowledgeBaseRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IMessageTemplateRef")
class IMessageTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MessageTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="messageTemplateRef")
    def message_template_ref(self) -> "MessageTemplateReference":
        '''(experimental) A reference to a MessageTemplate resource.

        :stability: experimental
        '''
        ...


class _IMessageTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MessageTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IMessageTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="messageTemplateRef")
    def message_template_ref(self) -> "MessageTemplateReference":
        '''(experimental) A reference to a MessageTemplate resource.

        :stability: experimental
        '''
        return typing.cast("MessageTemplateReference", jsii.get(self, "messageTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMessageTemplateRef).__jsii_proxy_class__ = lambda : _IMessageTemplateRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IMessageTemplateVersionRef"
)
class IMessageTemplateVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MessageTemplateVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="messageTemplateVersionRef")
    def message_template_version_ref(self) -> "MessageTemplateVersionReference":
        '''(experimental) A reference to a MessageTemplateVersion resource.

        :stability: experimental
        '''
        ...


class _IMessageTemplateVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MessageTemplateVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IMessageTemplateVersionRef"

    @builtins.property
    @jsii.member(jsii_name="messageTemplateVersionRef")
    def message_template_version_ref(self) -> "MessageTemplateVersionReference":
        '''(experimental) A reference to a MessageTemplateVersion resource.

        :stability: experimental
        '''
        return typing.cast("MessageTemplateVersionReference", jsii.get(self, "messageTemplateVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMessageTemplateVersionRef).__jsii_proxy_class__ = lambda : _IMessageTemplateVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wisdom.IQuickResponseRef")
class IQuickResponseRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a QuickResponse.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="quickResponseRef")
    def quick_response_ref(self) -> "QuickResponseReference":
        '''(experimental) A reference to a QuickResponse resource.

        :stability: experimental
        '''
        ...


class _IQuickResponseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a QuickResponse.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wisdom.IQuickResponseRef"

    @builtins.property
    @jsii.member(jsii_name="quickResponseRef")
    def quick_response_ref(self) -> "QuickResponseReference":
        '''(experimental) A reference to a QuickResponse resource.

        :stability: experimental
        '''
        return typing.cast("QuickResponseReference", jsii.get(self, "quickResponseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQuickResponseRef).__jsii_proxy_class__ = lambda : _IQuickResponseRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.KnowledgeBaseReference",
    jsii_struct_bases=[],
    name_mapping={
        "knowledge_base_arn": "knowledgeBaseArn",
        "knowledge_base_id": "knowledgeBaseId",
    },
)
class KnowledgeBaseReference:
    def __init__(
        self,
        *,
        knowledge_base_arn: builtins.str,
        knowledge_base_id: builtins.str,
    ) -> None:
        '''A reference to a KnowledgeBase resource.

        :param knowledge_base_arn: The ARN of the KnowledgeBase resource.
        :param knowledge_base_id: The KnowledgeBaseId of the KnowledgeBase resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            knowledge_base_reference = interfaces_wisdom.KnowledgeBaseReference(
                knowledge_base_arn="knowledgeBaseArn",
                knowledge_base_id="knowledgeBaseId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__784538eeb1cb7c78a0c4f36b23fd67be497b7a8fc257bc7c7ba21e7e16f5af75)
            check_type(argname="argument knowledge_base_arn", value=knowledge_base_arn, expected_type=type_hints["knowledge_base_arn"])
            check_type(argname="argument knowledge_base_id", value=knowledge_base_id, expected_type=type_hints["knowledge_base_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "knowledge_base_arn": knowledge_base_arn,
            "knowledge_base_id": knowledge_base_id,
        }

    @builtins.property
    def knowledge_base_arn(self) -> builtins.str:
        '''The ARN of the KnowledgeBase resource.'''
        result = self._values.get("knowledge_base_arn")
        assert result is not None, "Required property 'knowledge_base_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def knowledge_base_id(self) -> builtins.str:
        '''The KnowledgeBaseId of the KnowledgeBase resource.'''
        result = self._values.get("knowledge_base_id")
        assert result is not None, "Required property 'knowledge_base_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KnowledgeBaseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.MessageTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"message_template_arn": "messageTemplateArn"},
)
class MessageTemplateReference:
    def __init__(self, *, message_template_arn: builtins.str) -> None:
        '''A reference to a MessageTemplate resource.

        :param message_template_arn: The MessageTemplateArn of the MessageTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            message_template_reference = interfaces_wisdom.MessageTemplateReference(
                message_template_arn="messageTemplateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff8270e935b282639e3df13edda0358b19da2ab3d253c7dc875c2ffd364577ce)
            check_type(argname="argument message_template_arn", value=message_template_arn, expected_type=type_hints["message_template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "message_template_arn": message_template_arn,
        }

    @builtins.property
    def message_template_arn(self) -> builtins.str:
        '''The MessageTemplateArn of the MessageTemplate resource.'''
        result = self._values.get("message_template_arn")
        assert result is not None, "Required property 'message_template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MessageTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.MessageTemplateVersionReference",
    jsii_struct_bases=[],
    name_mapping={"message_template_version_arn": "messageTemplateVersionArn"},
)
class MessageTemplateVersionReference:
    def __init__(self, *, message_template_version_arn: builtins.str) -> None:
        '''A reference to a MessageTemplateVersion resource.

        :param message_template_version_arn: The MessageTemplateVersionArn of the MessageTemplateVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            message_template_version_reference = interfaces_wisdom.MessageTemplateVersionReference(
                message_template_version_arn="messageTemplateVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4760036332f940237c7ae9724d3d2543a49b120e12abcde43679ed9a27eed01a)
            check_type(argname="argument message_template_version_arn", value=message_template_version_arn, expected_type=type_hints["message_template_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "message_template_version_arn": message_template_version_arn,
        }

    @builtins.property
    def message_template_version_arn(self) -> builtins.str:
        '''The MessageTemplateVersionArn of the MessageTemplateVersion resource.'''
        result = self._values.get("message_template_version_arn")
        assert result is not None, "Required property 'message_template_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MessageTemplateVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wisdom.QuickResponseReference",
    jsii_struct_bases=[],
    name_mapping={"quick_response_arn": "quickResponseArn"},
)
class QuickResponseReference:
    def __init__(self, *, quick_response_arn: builtins.str) -> None:
        '''A reference to a QuickResponse resource.

        :param quick_response_arn: The QuickResponseArn of the QuickResponse resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wisdom as interfaces_wisdom
            
            quick_response_reference = interfaces_wisdom.QuickResponseReference(
                quick_response_arn="quickResponseArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc0a215922c97e582e8d40f0fcefa16cb8f7f673f658c6c0a0f5d6cc2457dca6)
            check_type(argname="argument quick_response_arn", value=quick_response_arn, expected_type=type_hints["quick_response_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "quick_response_arn": quick_response_arn,
        }

    @builtins.property
    def quick_response_arn(self) -> builtins.str:
        '''The QuickResponseArn of the QuickResponse resource.'''
        result = self._values.get("quick_response_arn")
        assert result is not None, "Required property 'quick_response_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QuickResponseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AIAgentReference",
    "AIAgentVersionReference",
    "AIGuardrailReference",
    "AIGuardrailVersionReference",
    "AIPromptReference",
    "AIPromptVersionReference",
    "AssistantAssociationReference",
    "AssistantReference",
    "IAIAgentRef",
    "IAIAgentVersionRef",
    "IAIGuardrailRef",
    "IAIGuardrailVersionRef",
    "IAIPromptRef",
    "IAIPromptVersionRef",
    "IAssistantAssociationRef",
    "IAssistantRef",
    "IKnowledgeBaseRef",
    "IMessageTemplateRef",
    "IMessageTemplateVersionRef",
    "IQuickResponseRef",
    "KnowledgeBaseReference",
    "MessageTemplateReference",
    "MessageTemplateVersionReference",
    "QuickResponseReference",
]

publication.publish()

def _typecheckingstub__d5c9f980da07d34883a98368cc7d4439a05c9661c54ad4701636ca1bde6d899a(
    *,
    ai_agent_arn: builtins.str,
    ai_agent_id: builtins.str,
    assistant_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df7b590b7f1d754e26a03c29ec446c8d6d6e0ccd43e8549d13dda2b64a1f148f(
    *,
    ai_agent_id: builtins.str,
    assistant_id: builtins.str,
    version_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fa4d7e3096b174861d8134fc19ca8a9424037e513dd67917f5753076fe65a5c(
    *,
    ai_guardrail_arn: builtins.str,
    ai_guardrail_id: builtins.str,
    assistant_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1504a5277569873463fc7fb8164b4ed9a3247ea857816478ee85d9f991c1399a(
    *,
    ai_guardrail_id: builtins.str,
    assistant_id: builtins.str,
    version_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da00bbb51042c62200cf26b300da1f1cf8fdd019213e51de295f69c453de7f01(
    *,
    ai_prompt_arn: builtins.str,
    ai_prompt_id: builtins.str,
    assistant_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__069cc2f0d138e268a2b17ac010b7fb4fa3bc49052926c62d0f383348f06c158e(
    *,
    ai_prompt_id: builtins.str,
    assistant_id: builtins.str,
    version_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79de64bf9a32f58953346e98715c2172e750981e9f09141629b8000b2e0b8799(
    *,
    assistant_association_arn: builtins.str,
    assistant_association_id: builtins.str,
    assistant_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ce10c49e9f56a127e62a262a788ac22afd2d17753177a2250d015beb74071f2(
    *,
    assistant_arn: builtins.str,
    assistant_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__784538eeb1cb7c78a0c4f36b23fd67be497b7a8fc257bc7c7ba21e7e16f5af75(
    *,
    knowledge_base_arn: builtins.str,
    knowledge_base_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff8270e935b282639e3df13edda0358b19da2ab3d253c7dc875c2ffd364577ce(
    *,
    message_template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4760036332f940237c7ae9724d3d2543a49b120e12abcde43679ed9a27eed01a(
    *,
    message_template_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc0a215922c97e582e8d40f0fcefa16cb8f7f673f658c6c0a0f5d6cc2457dca6(
    *,
    quick_response_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAIAgentRef, IAIAgentVersionRef, IAIGuardrailRef, IAIGuardrailVersionRef, IAIPromptRef, IAIPromptVersionRef, IAssistantAssociationRef, IAssistantRef, IKnowledgeBaseRef, IMessageTemplateRef, IMessageTemplateVersionRef, IQuickResponseRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
