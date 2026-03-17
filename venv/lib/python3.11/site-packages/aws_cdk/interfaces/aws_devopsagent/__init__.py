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
    jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.AgentSpaceReference",
    jsii_struct_bases=[],
    name_mapping={
        "agent_space_arn": "agentSpaceArn",
        "agent_space_id": "agentSpaceId",
    },
)
class AgentSpaceReference:
    def __init__(
        self,
        *,
        agent_space_arn: builtins.str,
        agent_space_id: builtins.str,
    ) -> None:
        '''A reference to a AgentSpace resource.

        :param agent_space_arn: The ARN of the AgentSpace resource.
        :param agent_space_id: The AgentSpaceId of the AgentSpace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsagent as interfaces_devopsagent
            
            agent_space_reference = interfaces_devopsagent.AgentSpaceReference(
                agent_space_arn="agentSpaceArn",
                agent_space_id="agentSpaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__243d248446cd635e4d580c7e821c36a9651420cfff39e507c6e56843c8dfb804)
            check_type(argname="argument agent_space_arn", value=agent_space_arn, expected_type=type_hints["agent_space_arn"])
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_arn": agent_space_arn,
            "agent_space_id": agent_space_id,
        }

    @builtins.property
    def agent_space_arn(self) -> builtins.str:
        '''The ARN of the AgentSpace resource.'''
        result = self._values.get("agent_space_arn")
        assert result is not None, "Required property 'agent_space_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The AgentSpaceId of the AgentSpace resource.'''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AgentSpaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.AssociationReference",
    jsii_struct_bases=[],
    name_mapping={"agent_space_id": "agentSpaceId", "association_id": "associationId"},
)
class AssociationReference:
    def __init__(
        self,
        *,
        agent_space_id: builtins.str,
        association_id: builtins.str,
    ) -> None:
        '''A reference to a Association resource.

        :param agent_space_id: The AgentSpaceId of the Association resource.
        :param association_id: The AssociationId of the Association resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsagent as interfaces_devopsagent
            
            association_reference = interfaces_devopsagent.AssociationReference(
                agent_space_id="agentSpaceId",
                association_id="associationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02318c63b2a10c35692903fce2e2a91bd6e6b83485fb019a8dd7f1e3e1a7d952)
            check_type(argname="argument agent_space_id", value=agent_space_id, expected_type=type_hints["agent_space_id"])
            check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_space_id": agent_space_id,
            "association_id": association_id,
        }

    @builtins.property
    def agent_space_id(self) -> builtins.str:
        '''The AgentSpaceId of the Association resource.'''
        result = self._values.get("agent_space_id")
        assert result is not None, "Required property 'agent_space_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def association_id(self) -> builtins.str:
        '''The AssociationId of the Association resource.'''
        result = self._values.get("association_id")
        assert result is not None, "Required property 'association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.IAgentSpaceRef")
class IAgentSpaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AgentSpace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="agentSpaceRef")
    def agent_space_ref(self) -> "AgentSpaceReference":
        '''(experimental) A reference to a AgentSpace resource.

        :stability: experimental
        '''
        ...


class _IAgentSpaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AgentSpace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsagent.IAgentSpaceRef"

    @builtins.property
    @jsii.member(jsii_name="agentSpaceRef")
    def agent_space_ref(self) -> "AgentSpaceReference":
        '''(experimental) A reference to a AgentSpace resource.

        :stability: experimental
        '''
        return typing.cast("AgentSpaceReference", jsii.get(self, "agentSpaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAgentSpaceRef).__jsii_proxy_class__ = lambda : _IAgentSpaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.IAssociationRef")
class IAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Association.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="associationRef")
    def association_ref(self) -> "AssociationReference":
        '''(experimental) A reference to a Association resource.

        :stability: experimental
        '''
        ...


class _IAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Association.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsagent.IAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="associationRef")
    def association_ref(self) -> "AssociationReference":
        '''(experimental) A reference to a Association resource.

        :stability: experimental
        '''
        return typing.cast("AssociationReference", jsii.get(self, "associationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssociationRef).__jsii_proxy_class__ = lambda : _IAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.IServiceRef")
class IServiceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        ...


class _IServiceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsagent.IServiceRef"

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        return typing.cast("ServiceReference", jsii.get(self, "serviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceRef).__jsii_proxy_class__ = lambda : _IServiceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsagent.ServiceReference",
    jsii_struct_bases=[],
    name_mapping={"service_id": "serviceId"},
)
class ServiceReference:
    def __init__(self, *, service_id: builtins.str) -> None:
        '''A reference to a Service resource.

        :param service_id: The ServiceId of the Service resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsagent as interfaces_devopsagent
            
            service_reference = interfaces_devopsagent.ServiceReference(
                service_id="serviceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07ccf3b3910b4e346e3aafaa8df25d00cb1ad66f67f835fb8c05b14d4cf5ce22)
            check_type(argname="argument service_id", value=service_id, expected_type=type_hints["service_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_id": service_id,
        }

    @builtins.property
    def service_id(self) -> builtins.str:
        '''The ServiceId of the Service resource.'''
        result = self._values.get("service_id")
        assert result is not None, "Required property 'service_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AgentSpaceReference",
    "AssociationReference",
    "IAgentSpaceRef",
    "IAssociationRef",
    "IServiceRef",
    "ServiceReference",
]

publication.publish()

def _typecheckingstub__243d248446cd635e4d580c7e821c36a9651420cfff39e507c6e56843c8dfb804(
    *,
    agent_space_arn: builtins.str,
    agent_space_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02318c63b2a10c35692903fce2e2a91bd6e6b83485fb019a8dd7f1e3e1a7d952(
    *,
    agent_space_id: builtins.str,
    association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07ccf3b3910b4e346e3aafaa8df25d00cb1ad66f67f835fb8c05b14d4cf5ce22(
    *,
    service_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAgentSpaceRef, IAssociationRef, IServiceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
