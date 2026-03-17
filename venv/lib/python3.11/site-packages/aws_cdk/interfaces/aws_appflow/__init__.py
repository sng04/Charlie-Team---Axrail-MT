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
    jsii_type="aws-cdk-lib.interfaces.aws_appflow.ConnectorProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "connector_profile_arn": "connectorProfileArn",
        "connector_profile_name": "connectorProfileName",
    },
)
class ConnectorProfileReference:
    def __init__(
        self,
        *,
        connector_profile_arn: builtins.str,
        connector_profile_name: builtins.str,
    ) -> None:
        '''A reference to a ConnectorProfile resource.

        :param connector_profile_arn: The ARN of the ConnectorProfile resource.
        :param connector_profile_name: The ConnectorProfileName of the ConnectorProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appflow as interfaces_appflow
            
            connector_profile_reference = interfaces_appflow.ConnectorProfileReference(
                connector_profile_arn="connectorProfileArn",
                connector_profile_name="connectorProfileName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0ab9c254228b4525d215ca08cd3b7955eabc767a7082b66099d996a9fd6d6cf)
            check_type(argname="argument connector_profile_arn", value=connector_profile_arn, expected_type=type_hints["connector_profile_arn"])
            check_type(argname="argument connector_profile_name", value=connector_profile_name, expected_type=type_hints["connector_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_profile_arn": connector_profile_arn,
            "connector_profile_name": connector_profile_name,
        }

    @builtins.property
    def connector_profile_arn(self) -> builtins.str:
        '''The ARN of the ConnectorProfile resource.'''
        result = self._values.get("connector_profile_arn")
        assert result is not None, "Required property 'connector_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_profile_name(self) -> builtins.str:
        '''The ConnectorProfileName of the ConnectorProfile resource.'''
        result = self._values.get("connector_profile_name")
        assert result is not None, "Required property 'connector_profile_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appflow.ConnectorReference",
    jsii_struct_bases=[],
    name_mapping={
        "connector_arn": "connectorArn",
        "connector_label": "connectorLabel",
    },
)
class ConnectorReference:
    def __init__(
        self,
        *,
        connector_arn: builtins.str,
        connector_label: builtins.str,
    ) -> None:
        '''A reference to a Connector resource.

        :param connector_arn: The ARN of the Connector resource.
        :param connector_label: The ConnectorLabel of the Connector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appflow as interfaces_appflow
            
            connector_reference = interfaces_appflow.ConnectorReference(
                connector_arn="connectorArn",
                connector_label="connectorLabel"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54f3a61a8727d0ce78a0d23574990b842d2ee5f562f125fb63fb2a692a6713c5)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
            check_type(argname="argument connector_label", value=connector_label, expected_type=type_hints["connector_label"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
            "connector_label": connector_label,
        }

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The ARN of the Connector resource.'''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_label(self) -> builtins.str:
        '''The ConnectorLabel of the Connector resource.'''
        result = self._values.get("connector_label")
        assert result is not None, "Required property 'connector_label' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appflow.FlowReference",
    jsii_struct_bases=[],
    name_mapping={"flow_arn": "flowArn", "flow_name": "flowName"},
)
class FlowReference:
    def __init__(self, *, flow_arn: builtins.str, flow_name: builtins.str) -> None:
        '''A reference to a Flow resource.

        :param flow_arn: The ARN of the Flow resource.
        :param flow_name: The FlowName of the Flow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appflow as interfaces_appflow
            
            flow_reference = interfaces_appflow.FlowReference(
                flow_arn="flowArn",
                flow_name="flowName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f8a38e4637786a3a5cb6bf2027809d64b766f0001f1f8ad9cd6ab0ebe28158e)
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument flow_name", value=flow_name, expected_type=type_hints["flow_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_arn": flow_arn,
            "flow_name": flow_name,
        }

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The ARN of the Flow resource.'''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flow_name(self) -> builtins.str:
        '''The FlowName of the Flow resource.'''
        result = self._values.get("flow_name")
        assert result is not None, "Required property 'flow_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appflow.IConnectorProfileRef")
class IConnectorProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectorProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectorProfileRef")
    def connector_profile_ref(self) -> "ConnectorProfileReference":
        '''(experimental) A reference to a ConnectorProfile resource.

        :stability: experimental
        '''
        ...


class _IConnectorProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectorProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appflow.IConnectorProfileRef"

    @builtins.property
    @jsii.member(jsii_name="connectorProfileRef")
    def connector_profile_ref(self) -> "ConnectorProfileReference":
        '''(experimental) A reference to a ConnectorProfile resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorProfileReference", jsii.get(self, "connectorProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorProfileRef).__jsii_proxy_class__ = lambda : _IConnectorProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appflow.IConnectorRef")
class IConnectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        ...


class _IConnectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appflow.IConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorReference", jsii.get(self, "connectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorRef).__jsii_proxy_class__ = lambda : _IConnectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appflow.IFlowRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appflow.IFlowRef"

    @builtins.property
    @jsii.member(jsii_name="flowRef")
    def flow_ref(self) -> "FlowReference":
        '''(experimental) A reference to a Flow resource.

        :stability: experimental
        '''
        return typing.cast("FlowReference", jsii.get(self, "flowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowRef).__jsii_proxy_class__ = lambda : _IFlowRefProxy


__all__ = [
    "ConnectorProfileReference",
    "ConnectorReference",
    "FlowReference",
    "IConnectorProfileRef",
    "IConnectorRef",
    "IFlowRef",
]

publication.publish()

def _typecheckingstub__b0ab9c254228b4525d215ca08cd3b7955eabc767a7082b66099d996a9fd6d6cf(
    *,
    connector_profile_arn: builtins.str,
    connector_profile_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f3a61a8727d0ce78a0d23574990b842d2ee5f562f125fb63fb2a692a6713c5(
    *,
    connector_arn: builtins.str,
    connector_label: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8a38e4637786a3a5cb6bf2027809d64b766f0001f1f8ad9cd6ab0ebe28158e(
    *,
    flow_arn: builtins.str,
    flow_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectorProfileRef, IConnectorRef, IFlowRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
