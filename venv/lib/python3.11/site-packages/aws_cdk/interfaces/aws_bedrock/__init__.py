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
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.AgentAliasReference",
    jsii_struct_bases=[],
    name_mapping={
        "agent_alias_arn": "agentAliasArn",
        "agent_alias_id": "agentAliasId",
        "agent_id": "agentId",
    },
)
class AgentAliasReference:
    def __init__(
        self,
        *,
        agent_alias_arn: builtins.str,
        agent_alias_id: builtins.str,
        agent_id: builtins.str,
    ) -> None:
        '''A reference to a AgentAlias resource.

        :param agent_alias_arn: The ARN of the AgentAlias resource.
        :param agent_alias_id: The AgentAliasId of the AgentAlias resource.
        :param agent_id: The AgentId of the AgentAlias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            agent_alias_reference = interfaces_bedrock.AgentAliasReference(
                agent_alias_arn="agentAliasArn",
                agent_alias_id="agentAliasId",
                agent_id="agentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7863ca07ea79b188f977c72e03ff9119313dd3281bfea1fdc780c42e1e66684)
            check_type(argname="argument agent_alias_arn", value=agent_alias_arn, expected_type=type_hints["agent_alias_arn"])
            check_type(argname="argument agent_alias_id", value=agent_alias_id, expected_type=type_hints["agent_alias_id"])
            check_type(argname="argument agent_id", value=agent_id, expected_type=type_hints["agent_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_alias_arn": agent_alias_arn,
            "agent_alias_id": agent_alias_id,
            "agent_id": agent_id,
        }

    @builtins.property
    def agent_alias_arn(self) -> builtins.str:
        '''The ARN of the AgentAlias resource.'''
        result = self._values.get("agent_alias_arn")
        assert result is not None, "Required property 'agent_alias_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_alias_id(self) -> builtins.str:
        '''The AgentAliasId of the AgentAlias resource.'''
        result = self._values.get("agent_alias_id")
        assert result is not None, "Required property 'agent_alias_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_id(self) -> builtins.str:
        '''The AgentId of the AgentAlias resource.'''
        result = self._values.get("agent_id")
        assert result is not None, "Required property 'agent_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentAliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.AgentReference",
    jsii_struct_bases=[],
    name_mapping={"agent_arn": "agentArn", "agent_id": "agentId"},
)
class AgentReference:
    def __init__(self, *, agent_arn: builtins.str, agent_id: builtins.str) -> None:
        '''A reference to a Agent resource.

        :param agent_arn: The ARN of the Agent resource.
        :param agent_id: The AgentId of the Agent resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            agent_reference = interfaces_bedrock.AgentReference(
                agent_arn="agentArn",
                agent_id="agentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aea3cfbcffff2ed7540a46c8063a2135275d1028bbdec6bdbd46f8d6317f5907)
            check_type(argname="argument agent_arn", value=agent_arn, expected_type=type_hints["agent_arn"])
            check_type(argname="argument agent_id", value=agent_id, expected_type=type_hints["agent_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_arn": agent_arn,
            "agent_id": agent_id,
        }

    @builtins.property
    def agent_arn(self) -> builtins.str:
        '''The ARN of the Agent resource.'''
        result = self._values.get("agent_arn")
        assert result is not None, "Required property 'agent_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_id(self) -> builtins.str:
        '''The AgentId of the Agent resource.'''
        result = self._values.get("agent_id")
        assert result is not None, "Required property 'agent_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.ApplicationInferenceProfileReference",
    jsii_struct_bases=[],
    name_mapping={"inference_profile_identifier": "inferenceProfileIdentifier"},
)
class ApplicationInferenceProfileReference:
    def __init__(self, *, inference_profile_identifier: builtins.str) -> None:
        '''A reference to a ApplicationInferenceProfile resource.

        :param inference_profile_identifier: The InferenceProfileIdentifier of the ApplicationInferenceProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            application_inference_profile_reference = interfaces_bedrock.ApplicationInferenceProfileReference(
                inference_profile_identifier="inferenceProfileIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9312f77d90c2991e17437afdee91a2a8e231ad7ed8db9d5b592a11c0bafb31)
            check_type(argname="argument inference_profile_identifier", value=inference_profile_identifier, expected_type=type_hints["inference_profile_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "inference_profile_identifier": inference_profile_identifier,
        }

    @builtins.property
    def inference_profile_identifier(self) -> builtins.str:
        '''The InferenceProfileIdentifier of the ApplicationInferenceProfile resource.'''
        result = self._values.get("inference_profile_identifier")
        assert result is not None, "Required property 'inference_profile_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationInferenceProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.AutomatedReasoningPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_arn": "policyArn"},
)
class AutomatedReasoningPolicyReference:
    def __init__(self, *, policy_arn: builtins.str) -> None:
        '''A reference to a AutomatedReasoningPolicy resource.

        :param policy_arn: The PolicyArn of the AutomatedReasoningPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            automated_reasoning_policy_reference = interfaces_bedrock.AutomatedReasoningPolicyReference(
                policy_arn="policyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ddf668bf79c1411180f49e3b2f2491ea0caf68d4e73da779e6e8289bb0a346b)
            check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_arn": policy_arn,
        }

    @builtins.property
    def policy_arn(self) -> builtins.str:
        '''The PolicyArn of the AutomatedReasoningPolicy resource.'''
        result = self._values.get("policy_arn")
        assert result is not None, "Required property 'policy_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutomatedReasoningPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.AutomatedReasoningPolicyVersionReference",
    jsii_struct_bases=[],
    name_mapping={"policy_arn": "policyArn", "version": "version"},
)
class AutomatedReasoningPolicyVersionReference:
    def __init__(self, *, policy_arn: builtins.str, version: builtins.str) -> None:
        '''A reference to a AutomatedReasoningPolicyVersion resource.

        :param policy_arn: The PolicyArn of the AutomatedReasoningPolicyVersion resource.
        :param version: The Version of the AutomatedReasoningPolicyVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            automated_reasoning_policy_version_reference = interfaces_bedrock.AutomatedReasoningPolicyVersionReference(
                policy_arn="policyArn",
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__178718377c8c6e20e87dd12c80145195f71cc3a95b298c70f47ca3e4f10989a6)
            check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_arn": policy_arn,
            "version": version,
        }

    @builtins.property
    def policy_arn(self) -> builtins.str:
        '''The PolicyArn of the AutomatedReasoningPolicyVersion resource.'''
        result = self._values.get("policy_arn")
        assert result is not None, "Required property 'policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The Version of the AutomatedReasoningPolicyVersion resource.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutomatedReasoningPolicyVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.BlueprintReference",
    jsii_struct_bases=[],
    name_mapping={"blueprint_arn": "blueprintArn"},
)
class BlueprintReference:
    def __init__(self, *, blueprint_arn: builtins.str) -> None:
        '''A reference to a Blueprint resource.

        :param blueprint_arn: The BlueprintArn of the Blueprint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            blueprint_reference = interfaces_bedrock.BlueprintReference(
                blueprint_arn="blueprintArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c467920c18d9ab11612b085e024f0c8d31837c54bb58d9a67f667e297a91090)
            check_type(argname="argument blueprint_arn", value=blueprint_arn, expected_type=type_hints["blueprint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "blueprint_arn": blueprint_arn,
        }

    @builtins.property
    def blueprint_arn(self) -> builtins.str:
        '''The BlueprintArn of the Blueprint resource.'''
        result = self._values.get("blueprint_arn")
        assert result is not None, "Required property 'blueprint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BlueprintReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.DataAutomationProjectReference",
    jsii_struct_bases=[],
    name_mapping={"project_arn": "projectArn"},
)
class DataAutomationProjectReference:
    def __init__(self, *, project_arn: builtins.str) -> None:
        '''A reference to a DataAutomationProject resource.

        :param project_arn: The ProjectArn of the DataAutomationProject resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            data_automation_project_reference = interfaces_bedrock.DataAutomationProjectReference(
                project_arn="projectArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__203506f3f388f0173acfcb73d107f5a4214bb61fda1a5934e4815e50677e3398)
            check_type(argname="argument project_arn", value=project_arn, expected_type=type_hints["project_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_arn": project_arn,
        }

    @builtins.property
    def project_arn(self) -> builtins.str:
        '''The ProjectArn of the DataAutomationProject resource.'''
        result = self._values.get("project_arn")
        assert result is not None, "Required property 'project_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAutomationProjectReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.DataSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_id": "dataSourceId",
        "knowledge_base_id": "knowledgeBaseId",
    },
)
class DataSourceReference:
    def __init__(
        self,
        *,
        data_source_id: builtins.str,
        knowledge_base_id: builtins.str,
    ) -> None:
        '''A reference to a DataSource resource.

        :param data_source_id: The DataSourceId of the DataSource resource.
        :param knowledge_base_id: The KnowledgeBaseId of the DataSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            data_source_reference = interfaces_bedrock.DataSourceReference(
                data_source_id="dataSourceId",
                knowledge_base_id="knowledgeBaseId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0bf2d83e4541e1c43cb719782e1cec816e4258b1bd773390292a218ebdb85e3)
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument knowledge_base_id", value=knowledge_base_id, expected_type=type_hints["knowledge_base_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source_id": data_source_id,
            "knowledge_base_id": knowledge_base_id,
        }

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The DataSourceId of the DataSource resource.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def knowledge_base_id(self) -> builtins.str:
        '''The KnowledgeBaseId of the DataSource resource.'''
        result = self._values.get("knowledge_base_id")
        assert result is not None, "Required property 'knowledge_base_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.FlowAliasReference",
    jsii_struct_bases=[],
    name_mapping={"flow_alias_arn": "flowAliasArn", "flow_arn": "flowArn"},
)
class FlowAliasReference:
    def __init__(self, *, flow_alias_arn: builtins.str, flow_arn: builtins.str) -> None:
        '''A reference to a FlowAlias resource.

        :param flow_alias_arn: The Arn of the FlowAlias resource.
        :param flow_arn: The FlowArn of the FlowAlias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            flow_alias_reference = interfaces_bedrock.FlowAliasReference(
                flow_alias_arn="flowAliasArn",
                flow_arn="flowArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd4ba560709dca470a071df17cea02681b0a31fe31bb8cb4f206c48e66d1c751)
            check_type(argname="argument flow_alias_arn", value=flow_alias_arn, expected_type=type_hints["flow_alias_arn"])
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_alias_arn": flow_alias_arn,
            "flow_arn": flow_arn,
        }

    @builtins.property
    def flow_alias_arn(self) -> builtins.str:
        '''The Arn of the FlowAlias resource.'''
        result = self._values.get("flow_alias_arn")
        assert result is not None, "Required property 'flow_alias_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The FlowArn of the FlowAlias resource.'''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowAliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.FlowReference",
    jsii_struct_bases=[],
    name_mapping={"flow_arn": "flowArn"},
)
class FlowReference:
    def __init__(self, *, flow_arn: builtins.str) -> None:
        '''A reference to a Flow resource.

        :param flow_arn: The Arn of the Flow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            flow_reference = interfaces_bedrock.FlowReference(
                flow_arn="flowArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ca1977b41f714c0366a9f6787636edbc6785719f675f1716baea9155bd130bb)
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_arn": flow_arn,
        }

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The Arn of the Flow resource.'''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.FlowVersionReference",
    jsii_struct_bases=[],
    name_mapping={"flow_arn": "flowArn", "version": "version"},
)
class FlowVersionReference:
    def __init__(self, *, flow_arn: builtins.str, version: builtins.str) -> None:
        '''A reference to a FlowVersion resource.

        :param flow_arn: The FlowArn of the FlowVersion resource.
        :param version: The Version of the FlowVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            flow_version_reference = interfaces_bedrock.FlowVersionReference(
                flow_arn="flowArn",
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2874419298b6a77a2646ece3a5825bb09b6b15912b8586919219403a05350598)
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_arn": flow_arn,
            "version": version,
        }

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The FlowArn of the FlowVersion resource.'''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The Version of the FlowVersion resource.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.GuardrailReference",
    jsii_struct_bases=[],
    name_mapping={"guardrail_arn": "guardrailArn"},
)
class GuardrailReference:
    def __init__(self, *, guardrail_arn: builtins.str) -> None:
        '''A reference to a Guardrail resource.

        :param guardrail_arn: The GuardrailArn of the Guardrail resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            guardrail_reference = interfaces_bedrock.GuardrailReference(
                guardrail_arn="guardrailArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2665c2aac3057a56a72b5390eb1e2eb341665446d4bf813819b0eee3accc12b)
            check_type(argname="argument guardrail_arn", value=guardrail_arn, expected_type=type_hints["guardrail_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "guardrail_arn": guardrail_arn,
        }

    @builtins.property
    def guardrail_arn(self) -> builtins.str:
        '''The GuardrailArn of the Guardrail resource.'''
        result = self._values.get("guardrail_arn")
        assert result is not None, "Required property 'guardrail_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuardrailReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.GuardrailVersionReference",
    jsii_struct_bases=[],
    name_mapping={"guardrail_id": "guardrailId", "version": "version"},
)
class GuardrailVersionReference:
    def __init__(self, *, guardrail_id: builtins.str, version: builtins.str) -> None:
        '''A reference to a GuardrailVersion resource.

        :param guardrail_id: The GuardrailId of the GuardrailVersion resource.
        :param version: The Version of the GuardrailVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            guardrail_version_reference = interfaces_bedrock.GuardrailVersionReference(
                guardrail_id="guardrailId",
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6a893f9decc690a69a3826bfbca36059edb95fc2a7868258aaef41e61af6d40)
            check_type(argname="argument guardrail_id", value=guardrail_id, expected_type=type_hints["guardrail_id"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "guardrail_id": guardrail_id,
            "version": version,
        }

    @builtins.property
    def guardrail_id(self) -> builtins.str:
        '''The GuardrailId of the GuardrailVersion resource.'''
        result = self._values.get("guardrail_id")
        assert result is not None, "Required property 'guardrail_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The Version of the GuardrailVersion resource.'''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuardrailVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IAgentAliasRef")
class IAgentAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AgentAlias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentAliasRef")
    def agent_alias_ref(self) -> "AgentAliasReference":
        '''(experimental) A reference to a AgentAlias resource.

        :stability: experimental
        '''
        ...


class _IAgentAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AgentAlias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IAgentAliasRef"

    @builtins.property
    @jsii.member(jsii_name="agentAliasRef")
    def agent_alias_ref(self) -> "AgentAliasReference":
        '''(experimental) A reference to a AgentAlias resource.

        :stability: experimental
        '''
        return typing.cast("AgentAliasReference", jsii.get(self, "agentAliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentAliasRef).__jsii_proxy_class__ = lambda : _IAgentAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IAgentRef")
class IAgentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Agent.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentRef")
    def agent_ref(self) -> "AgentReference":
        '''(experimental) A reference to a Agent resource.

        :stability: experimental
        '''
        ...


class _IAgentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Agent.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IAgentRef"

    @builtins.property
    @jsii.member(jsii_name="agentRef")
    def agent_ref(self) -> "AgentReference":
        '''(experimental) A reference to a Agent resource.

        :stability: experimental
        '''
        return typing.cast("AgentReference", jsii.get(self, "agentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentRef).__jsii_proxy_class__ = lambda : _IAgentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IApplicationInferenceProfileRef"
)
class IApplicationInferenceProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationInferenceProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationInferenceProfileRef")
    def application_inference_profile_ref(
        self,
    ) -> "ApplicationInferenceProfileReference":
        '''(experimental) A reference to a ApplicationInferenceProfile resource.

        :stability: experimental
        '''
        ...


class _IApplicationInferenceProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationInferenceProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IApplicationInferenceProfileRef"

    @builtins.property
    @jsii.member(jsii_name="applicationInferenceProfileRef")
    def application_inference_profile_ref(
        self,
    ) -> "ApplicationInferenceProfileReference":
        '''(experimental) A reference to a ApplicationInferenceProfile resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationInferenceProfileReference", jsii.get(self, "applicationInferenceProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationInferenceProfileRef).__jsii_proxy_class__ = lambda : _IApplicationInferenceProfileRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IAutomatedReasoningPolicyRef"
)
class IAutomatedReasoningPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AutomatedReasoningPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="automatedReasoningPolicyRef")
    def automated_reasoning_policy_ref(self) -> "AutomatedReasoningPolicyReference":
        '''(experimental) A reference to a AutomatedReasoningPolicy resource.

        :stability: experimental
        '''
        ...


class _IAutomatedReasoningPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AutomatedReasoningPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IAutomatedReasoningPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="automatedReasoningPolicyRef")
    def automated_reasoning_policy_ref(self) -> "AutomatedReasoningPolicyReference":
        '''(experimental) A reference to a AutomatedReasoningPolicy resource.

        :stability: experimental
        '''
        return typing.cast("AutomatedReasoningPolicyReference", jsii.get(self, "automatedReasoningPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAutomatedReasoningPolicyRef).__jsii_proxy_class__ = lambda : _IAutomatedReasoningPolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IAutomatedReasoningPolicyVersionRef"
)
class IAutomatedReasoningPolicyVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AutomatedReasoningPolicyVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="automatedReasoningPolicyVersionRef")
    def automated_reasoning_policy_version_ref(
        self,
    ) -> "AutomatedReasoningPolicyVersionReference":
        '''(experimental) A reference to a AutomatedReasoningPolicyVersion resource.

        :stability: experimental
        '''
        ...


class _IAutomatedReasoningPolicyVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AutomatedReasoningPolicyVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IAutomatedReasoningPolicyVersionRef"

    @builtins.property
    @jsii.member(jsii_name="automatedReasoningPolicyVersionRef")
    def automated_reasoning_policy_version_ref(
        self,
    ) -> "AutomatedReasoningPolicyVersionReference":
        '''(experimental) A reference to a AutomatedReasoningPolicyVersion resource.

        :stability: experimental
        '''
        return typing.cast("AutomatedReasoningPolicyVersionReference", jsii.get(self, "automatedReasoningPolicyVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAutomatedReasoningPolicyVersionRef).__jsii_proxy_class__ = lambda : _IAutomatedReasoningPolicyVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IBlueprintRef")
class IBlueprintRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Blueprint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="blueprintRef")
    def blueprint_ref(self) -> "BlueprintReference":
        '''(experimental) A reference to a Blueprint resource.

        :stability: experimental
        '''
        ...


class _IBlueprintRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Blueprint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IBlueprintRef"

    @builtins.property
    @jsii.member(jsii_name="blueprintRef")
    def blueprint_ref(self) -> "BlueprintReference":
        '''(experimental) A reference to a Blueprint resource.

        :stability: experimental
        '''
        return typing.cast("BlueprintReference", jsii.get(self, "blueprintRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBlueprintRef).__jsii_proxy_class__ = lambda : _IBlueprintRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IDataAutomationProjectRef"
)
class IDataAutomationProjectRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataAutomationProject.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataAutomationProjectRef")
    def data_automation_project_ref(self) -> "DataAutomationProjectReference":
        '''(experimental) A reference to a DataAutomationProject resource.

        :stability: experimental
        '''
        ...


class _IDataAutomationProjectRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataAutomationProject.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IDataAutomationProjectRef"

    @builtins.property
    @jsii.member(jsii_name="dataAutomationProjectRef")
    def data_automation_project_ref(self) -> "DataAutomationProjectReference":
        '''(experimental) A reference to a DataAutomationProject resource.

        :stability: experimental
        '''
        return typing.cast("DataAutomationProjectReference", jsii.get(self, "dataAutomationProjectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataAutomationProjectRef).__jsii_proxy_class__ = lambda : _IDataAutomationProjectRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IDataSourceRef")
class IDataSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        ...


class _IDataSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IDataSourceRef"

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        return typing.cast("DataSourceReference", jsii.get(self, "dataSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSourceRef).__jsii_proxy_class__ = lambda : _IDataSourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IFlowAliasRef")
class IFlowAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FlowAlias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flowAliasRef")
    def flow_alias_ref(self) -> "FlowAliasReference":
        '''(experimental) A reference to a FlowAlias resource.

        :stability: experimental
        '''
        ...


class _IFlowAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FlowAlias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IFlowAliasRef"

    @builtins.property
    @jsii.member(jsii_name="flowAliasRef")
    def flow_alias_ref(self) -> "FlowAliasReference":
        '''(experimental) A reference to a FlowAlias resource.

        :stability: experimental
        '''
        return typing.cast("FlowAliasReference", jsii.get(self, "flowAliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowAliasRef).__jsii_proxy_class__ = lambda : _IFlowAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IFlowRef")
class IFlowRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Flow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flowRef")
    def flow_ref(self) -> "FlowReference":
        '''(experimental) A reference to a Flow resource.

        :stability: experimental
        '''
        ...


class _IFlowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Flow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IFlowRef"

    @builtins.property
    @jsii.member(jsii_name="flowRef")
    def flow_ref(self) -> "FlowReference":
        '''(experimental) A reference to a Flow resource.

        :stability: experimental
        '''
        return typing.cast("FlowReference", jsii.get(self, "flowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowRef).__jsii_proxy_class__ = lambda : _IFlowRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IFlowVersionRef")
class IFlowVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FlowVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flowVersionRef")
    def flow_version_ref(self) -> "FlowVersionReference":
        '''(experimental) A reference to a FlowVersion resource.

        :stability: experimental
        '''
        ...


class _IFlowVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FlowVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IFlowVersionRef"

    @builtins.property
    @jsii.member(jsii_name="flowVersionRef")
    def flow_version_ref(self) -> "FlowVersionReference":
        '''(experimental) A reference to a FlowVersion resource.

        :stability: experimental
        '''
        return typing.cast("FlowVersionReference", jsii.get(self, "flowVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowVersionRef).__jsii_proxy_class__ = lambda : _IFlowVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IGuardrailRef")
class IGuardrailRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Guardrail.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="guardrailRef")
    def guardrail_ref(self) -> "GuardrailReference":
        '''(experimental) A reference to a Guardrail resource.

        :stability: experimental
        '''
        ...


class _IGuardrailRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Guardrail.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IGuardrailRef"

    @builtins.property
    @jsii.member(jsii_name="guardrailRef")
    def guardrail_ref(self) -> "GuardrailReference":
        '''(experimental) A reference to a Guardrail resource.

        :stability: experimental
        '''
        return typing.cast("GuardrailReference", jsii.get(self, "guardrailRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGuardrailRef).__jsii_proxy_class__ = lambda : _IGuardrailRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IGuardrailVersionRef")
class IGuardrailVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GuardrailVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="guardrailVersionRef")
    def guardrail_version_ref(self) -> "GuardrailVersionReference":
        '''(experimental) A reference to a GuardrailVersion resource.

        :stability: experimental
        '''
        ...


class _IGuardrailVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GuardrailVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IGuardrailVersionRef"

    @builtins.property
    @jsii.member(jsii_name="guardrailVersionRef")
    def guardrail_version_ref(self) -> "GuardrailVersionReference":
        '''(experimental) A reference to a GuardrailVersion resource.

        :stability: experimental
        '''
        return typing.cast("GuardrailVersionReference", jsii.get(self, "guardrailVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGuardrailVersionRef).__jsii_proxy_class__ = lambda : _IGuardrailVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IIntelligentPromptRouterRef"
)
class IIntelligentPromptRouterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IntelligentPromptRouter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="intelligentPromptRouterRef")
    def intelligent_prompt_router_ref(self) -> "IntelligentPromptRouterReference":
        '''(experimental) A reference to a IntelligentPromptRouter resource.

        :stability: experimental
        '''
        ...


class _IIntelligentPromptRouterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IntelligentPromptRouter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IIntelligentPromptRouterRef"

    @builtins.property
    @jsii.member(jsii_name="intelligentPromptRouterRef")
    def intelligent_prompt_router_ref(self) -> "IntelligentPromptRouterReference":
        '''(experimental) A reference to a IntelligentPromptRouter resource.

        :stability: experimental
        '''
        return typing.cast("IntelligentPromptRouterReference", jsii.get(self, "intelligentPromptRouterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntelligentPromptRouterRef).__jsii_proxy_class__ = lambda : _IIntelligentPromptRouterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IKnowledgeBaseRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IKnowledgeBaseRef"

    @builtins.property
    @jsii.member(jsii_name="knowledgeBaseRef")
    def knowledge_base_ref(self) -> "KnowledgeBaseReference":
        '''(experimental) A reference to a KnowledgeBase resource.

        :stability: experimental
        '''
        return typing.cast("KnowledgeBaseReference", jsii.get(self, "knowledgeBaseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKnowledgeBaseRef).__jsii_proxy_class__ = lambda : _IKnowledgeBaseRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IPromptRef")
class IPromptRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Prompt.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="promptRef")
    def prompt_ref(self) -> "PromptReference":
        '''(experimental) A reference to a Prompt resource.

        :stability: experimental
        '''
        ...


class _IPromptRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Prompt.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IPromptRef"

    @builtins.property
    @jsii.member(jsii_name="promptRef")
    def prompt_ref(self) -> "PromptReference":
        '''(experimental) A reference to a Prompt resource.

        :stability: experimental
        '''
        return typing.cast("PromptReference", jsii.get(self, "promptRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPromptRef).__jsii_proxy_class__ = lambda : _IPromptRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IPromptVersionRef")
class IPromptVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PromptVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="promptVersionRef")
    def prompt_version_ref(self) -> "PromptVersionReference":
        '''(experimental) A reference to a PromptVersion resource.

        :stability: experimental
        '''
        ...


class _IPromptVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PromptVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_bedrock.IPromptVersionRef"

    @builtins.property
    @jsii.member(jsii_name="promptVersionRef")
    def prompt_version_ref(self) -> "PromptVersionReference":
        '''(experimental) A reference to a PromptVersion resource.

        :stability: experimental
        '''
        return typing.cast("PromptVersionReference", jsii.get(self, "promptVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPromptVersionRef).__jsii_proxy_class__ = lambda : _IPromptVersionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.IntelligentPromptRouterReference",
    jsii_struct_bases=[],
    name_mapping={"prompt_router_arn": "promptRouterArn"},
)
class IntelligentPromptRouterReference:
    def __init__(self, *, prompt_router_arn: builtins.str) -> None:
        '''A reference to a IntelligentPromptRouter resource.

        :param prompt_router_arn: The PromptRouterArn of the IntelligentPromptRouter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            intelligent_prompt_router_reference = interfaces_bedrock.IntelligentPromptRouterReference(
                prompt_router_arn="promptRouterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38a40ff6e0abe9dc6f7aade274b0120c2e6f40eee77f6758ec3f0558d176e782)
            check_type(argname="argument prompt_router_arn", value=prompt_router_arn, expected_type=type_hints["prompt_router_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prompt_router_arn": prompt_router_arn,
        }

    @builtins.property
    def prompt_router_arn(self) -> builtins.str:
        '''The PromptRouterArn of the IntelligentPromptRouter resource.'''
        result = self._values.get("prompt_router_arn")
        assert result is not None, "Required property 'prompt_router_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntelligentPromptRouterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.KnowledgeBaseReference",
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
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            knowledge_base_reference = interfaces_bedrock.KnowledgeBaseReference(
                knowledge_base_arn="knowledgeBaseArn",
                knowledge_base_id="knowledgeBaseId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b94f3e512cb504adcdb57798a5a24eb1317d023c697a912239afbe89bab2685a)
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
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.PromptReference",
    jsii_struct_bases=[],
    name_mapping={"prompt_arn": "promptArn"},
)
class PromptReference:
    def __init__(self, *, prompt_arn: builtins.str) -> None:
        '''A reference to a Prompt resource.

        :param prompt_arn: The Arn of the Prompt resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            prompt_reference = interfaces_bedrock.PromptReference(
                prompt_arn="promptArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__824c4b5df0dd7a9ba3a74d15b7e6c36f15575e13a951b91dfe44fa9357bdf1a7)
            check_type(argname="argument prompt_arn", value=prompt_arn, expected_type=type_hints["prompt_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prompt_arn": prompt_arn,
        }

    @builtins.property
    def prompt_arn(self) -> builtins.str:
        '''The Arn of the Prompt resource.'''
        result = self._values.get("prompt_arn")
        assert result is not None, "Required property 'prompt_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PromptReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_bedrock.PromptVersionReference",
    jsii_struct_bases=[],
    name_mapping={"prompt_version_arn": "promptVersionArn"},
)
class PromptVersionReference:
    def __init__(self, *, prompt_version_arn: builtins.str) -> None:
        '''A reference to a PromptVersion resource.

        :param prompt_version_arn: The Arn of the PromptVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_bedrock as interfaces_bedrock
            
            prompt_version_reference = interfaces_bedrock.PromptVersionReference(
                prompt_version_arn="promptVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac6e1c09d9b0c0069246f971a0e480a42b0dbc077e6ec81b3c8390956134b6be)
            check_type(argname="argument prompt_version_arn", value=prompt_version_arn, expected_type=type_hints["prompt_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "prompt_version_arn": prompt_version_arn,
        }

    @builtins.property
    def prompt_version_arn(self) -> builtins.str:
        '''The Arn of the PromptVersion resource.'''
        result = self._values.get("prompt_version_arn")
        assert result is not None, "Required property 'prompt_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PromptVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AgentAliasReference",
    "AgentReference",
    "ApplicationInferenceProfileReference",
    "AutomatedReasoningPolicyReference",
    "AutomatedReasoningPolicyVersionReference",
    "BlueprintReference",
    "DataAutomationProjectReference",
    "DataSourceReference",
    "FlowAliasReference",
    "FlowReference",
    "FlowVersionReference",
    "GuardrailReference",
    "GuardrailVersionReference",
    "IAgentAliasRef",
    "IAgentRef",
    "IApplicationInferenceProfileRef",
    "IAutomatedReasoningPolicyRef",
    "IAutomatedReasoningPolicyVersionRef",
    "IBlueprintRef",
    "IDataAutomationProjectRef",
    "IDataSourceRef",
    "IFlowAliasRef",
    "IFlowRef",
    "IFlowVersionRef",
    "IGuardrailRef",
    "IGuardrailVersionRef",
    "IIntelligentPromptRouterRef",
    "IKnowledgeBaseRef",
    "IPromptRef",
    "IPromptVersionRef",
    "IntelligentPromptRouterReference",
    "KnowledgeBaseReference",
    "PromptReference",
    "PromptVersionReference",
]

publication.publish()

def _typecheckingstub__b7863ca07ea79b188f977c72e03ff9119313dd3281bfea1fdc780c42e1e66684(
    *,
    agent_alias_arn: builtins.str,
    agent_alias_id: builtins.str,
    agent_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea3cfbcffff2ed7540a46c8063a2135275d1028bbdec6bdbd46f8d6317f5907(
    *,
    agent_arn: builtins.str,
    agent_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9312f77d90c2991e17437afdee91a2a8e231ad7ed8db9d5b592a11c0bafb31(
    *,
    inference_profile_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ddf668bf79c1411180f49e3b2f2491ea0caf68d4e73da779e6e8289bb0a346b(
    *,
    policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__178718377c8c6e20e87dd12c80145195f71cc3a95b298c70f47ca3e4f10989a6(
    *,
    policy_arn: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c467920c18d9ab11612b085e024f0c8d31837c54bb58d9a67f667e297a91090(
    *,
    blueprint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__203506f3f388f0173acfcb73d107f5a4214bb61fda1a5934e4815e50677e3398(
    *,
    project_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0bf2d83e4541e1c43cb719782e1cec816e4258b1bd773390292a218ebdb85e3(
    *,
    data_source_id: builtins.str,
    knowledge_base_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd4ba560709dca470a071df17cea02681b0a31fe31bb8cb4f206c48e66d1c751(
    *,
    flow_alias_arn: builtins.str,
    flow_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ca1977b41f714c0366a9f6787636edbc6785719f675f1716baea9155bd130bb(
    *,
    flow_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2874419298b6a77a2646ece3a5825bb09b6b15912b8586919219403a05350598(
    *,
    flow_arn: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2665c2aac3057a56a72b5390eb1e2eb341665446d4bf813819b0eee3accc12b(
    *,
    guardrail_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6a893f9decc690a69a3826bfbca36059edb95fc2a7868258aaef41e61af6d40(
    *,
    guardrail_id: builtins.str,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38a40ff6e0abe9dc6f7aade274b0120c2e6f40eee77f6758ec3f0558d176e782(
    *,
    prompt_router_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b94f3e512cb504adcdb57798a5a24eb1317d023c697a912239afbe89bab2685a(
    *,
    knowledge_base_arn: builtins.str,
    knowledge_base_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824c4b5df0dd7a9ba3a74d15b7e6c36f15575e13a951b91dfe44fa9357bdf1a7(
    *,
    prompt_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6e1c09d9b0c0069246f971a0e480a42b0dbc077e6ec81b3c8390956134b6be(
    *,
    prompt_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAgentAliasRef, IAgentRef, IApplicationInferenceProfileRef, IAutomatedReasoningPolicyRef, IAutomatedReasoningPolicyVersionRef, IBlueprintRef, IDataAutomationProjectRef, IDataSourceRef, IFlowAliasRef, IFlowRef, IFlowVersionRef, IGuardrailRef, IGuardrailVersionRef, IIntelligentPromptRouterRef, IKnowledgeBaseRef, IPromptRef, IPromptVersionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
