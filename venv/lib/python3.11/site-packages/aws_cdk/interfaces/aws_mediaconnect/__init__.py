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
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.BridgeOutputReference",
    jsii_struct_bases=[],
    name_mapping={"bridge_arn": "bridgeArn", "bridge_output_name": "bridgeOutputName"},
)
class BridgeOutputReference:
    def __init__(
        self,
        *,
        bridge_arn: builtins.str,
        bridge_output_name: builtins.str,
    ) -> None:
        '''A reference to a BridgeOutput resource.

        :param bridge_arn: The BridgeArn of the BridgeOutput resource.
        :param bridge_output_name: The Name of the BridgeOutput resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            bridge_output_reference = interfaces_mediaconnect.BridgeOutputReference(
                bridge_arn="bridgeArn",
                bridge_output_name="bridgeOutputName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73182f10d25757e57316dcdbde383b2563dd187db8a77ce9d9b64f432f3132b2)
            check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
            check_type(argname="argument bridge_output_name", value=bridge_output_name, expected_type=type_hints["bridge_output_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bridge_arn": bridge_arn,
            "bridge_output_name": bridge_output_name,
        }

    @builtins.property
    def bridge_arn(self) -> builtins.str:
        '''The BridgeArn of the BridgeOutput resource.'''
        result = self._values.get("bridge_arn")
        assert result is not None, "Required property 'bridge_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bridge_output_name(self) -> builtins.str:
        '''The Name of the BridgeOutput resource.'''
        result = self._values.get("bridge_output_name")
        assert result is not None, "Required property 'bridge_output_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BridgeOutputReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.BridgeReference",
    jsii_struct_bases=[],
    name_mapping={"bridge_arn": "bridgeArn"},
)
class BridgeReference:
    def __init__(self, *, bridge_arn: builtins.str) -> None:
        '''A reference to a Bridge resource.

        :param bridge_arn: The BridgeArn of the Bridge resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            bridge_reference = interfaces_mediaconnect.BridgeReference(
                bridge_arn="bridgeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7440fa6612c678dd575ec05ad66dc7948fc8c70e784c74785f80ab5356faec4)
            check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bridge_arn": bridge_arn,
        }

    @builtins.property
    def bridge_arn(self) -> builtins.str:
        '''The BridgeArn of the Bridge resource.'''
        result = self._values.get("bridge_arn")
        assert result is not None, "Required property 'bridge_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BridgeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.BridgeSourceReference",
    jsii_struct_bases=[],
    name_mapping={"bridge_arn": "bridgeArn", "bridge_source_name": "bridgeSourceName"},
)
class BridgeSourceReference:
    def __init__(
        self,
        *,
        bridge_arn: builtins.str,
        bridge_source_name: builtins.str,
    ) -> None:
        '''A reference to a BridgeSource resource.

        :param bridge_arn: The BridgeArn of the BridgeSource resource.
        :param bridge_source_name: The Name of the BridgeSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            bridge_source_reference = interfaces_mediaconnect.BridgeSourceReference(
                bridge_arn="bridgeArn",
                bridge_source_name="bridgeSourceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a57ab8b2799544f17aecf266ba0a305c9946b460679a831f68a8cc2667ab5ce)
            check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
            check_type(argname="argument bridge_source_name", value=bridge_source_name, expected_type=type_hints["bridge_source_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bridge_arn": bridge_arn,
            "bridge_source_name": bridge_source_name,
        }

    @builtins.property
    def bridge_arn(self) -> builtins.str:
        '''The BridgeArn of the BridgeSource resource.'''
        result = self._values.get("bridge_arn")
        assert result is not None, "Required property 'bridge_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bridge_source_name(self) -> builtins.str:
        '''The Name of the BridgeSource resource.'''
        result = self._values.get("bridge_source_name")
        assert result is not None, "Required property 'bridge_source_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BridgeSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.FlowEntitlementReference",
    jsii_struct_bases=[],
    name_mapping={"entitlement_arn": "entitlementArn"},
)
class FlowEntitlementReference:
    def __init__(self, *, entitlement_arn: builtins.str) -> None:
        '''A reference to a FlowEntitlement resource.

        :param entitlement_arn: The EntitlementArn of the FlowEntitlement resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            flow_entitlement_reference = interfaces_mediaconnect.FlowEntitlementReference(
                entitlement_arn="entitlementArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0edc53b6b6e960dbdc6bd64c4eb6c4541ecc0a17bdd262b31812971a606f44ad)
            check_type(argname="argument entitlement_arn", value=entitlement_arn, expected_type=type_hints["entitlement_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entitlement_arn": entitlement_arn,
        }

    @builtins.property
    def entitlement_arn(self) -> builtins.str:
        '''The EntitlementArn of the FlowEntitlement resource.'''
        result = self._values.get("entitlement_arn")
        assert result is not None, "Required property 'entitlement_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowEntitlementReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.FlowOutputReference",
    jsii_struct_bases=[],
    name_mapping={"output_arn": "outputArn"},
)
class FlowOutputReference:
    def __init__(self, *, output_arn: builtins.str) -> None:
        '''A reference to a FlowOutput resource.

        :param output_arn: The OutputArn of the FlowOutput resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            flow_output_reference = interfaces_mediaconnect.FlowOutputReference(
                output_arn="outputArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d86e4aa7f442e2ea027387f7ae0fa891b3494c4e892279cf982fa261e9fe71de)
            check_type(argname="argument output_arn", value=output_arn, expected_type=type_hints["output_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "output_arn": output_arn,
        }

    @builtins.property
    def output_arn(self) -> builtins.str:
        '''The OutputArn of the FlowOutput resource.'''
        result = self._values.get("output_arn")
        assert result is not None, "Required property 'output_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowOutputReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.FlowReference",
    jsii_struct_bases=[],
    name_mapping={"flow_arn": "flowArn"},
)
class FlowReference:
    def __init__(self, *, flow_arn: builtins.str) -> None:
        '''A reference to a Flow resource.

        :param flow_arn: The FlowArn of the Flow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            flow_reference = interfaces_mediaconnect.FlowReference(
                flow_arn="flowArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b8601eaf471f9bacfb5f3d93788a33c0fcea9ec28ec13b3ec3b0a0e901ce8c3)
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_arn": flow_arn,
        }

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The FlowArn of the Flow resource.'''
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
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.FlowSourceReference",
    jsii_struct_bases=[],
    name_mapping={"source_arn": "sourceArn"},
)
class FlowSourceReference:
    def __init__(self, *, source_arn: builtins.str) -> None:
        '''A reference to a FlowSource resource.

        :param source_arn: The SourceArn of the FlowSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            flow_source_reference = interfaces_mediaconnect.FlowSourceReference(
                source_arn="sourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__324aca350b47900f430f689f94e3804fb4163b2fedf800ae93532fba0c81ff41)
            check_type(argname="argument source_arn", value=source_arn, expected_type=type_hints["source_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_arn": source_arn,
        }

    @builtins.property
    def source_arn(self) -> builtins.str:
        '''The SourceArn of the FlowSource resource.'''
        result = self._values.get("source_arn")
        assert result is not None, "Required property 'source_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.FlowVpcInterfaceReference",
    jsii_struct_bases=[],
    name_mapping={
        "flow_arn": "flowArn",
        "flow_vpc_interface_name": "flowVpcInterfaceName",
    },
)
class FlowVpcInterfaceReference:
    def __init__(
        self,
        *,
        flow_arn: builtins.str,
        flow_vpc_interface_name: builtins.str,
    ) -> None:
        '''A reference to a FlowVpcInterface resource.

        :param flow_arn: The FlowArn of the FlowVpcInterface resource.
        :param flow_vpc_interface_name: The Name of the FlowVpcInterface resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            flow_vpc_interface_reference = interfaces_mediaconnect.FlowVpcInterfaceReference(
                flow_arn="flowArn",
                flow_vpc_interface_name="flowVpcInterfaceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e0ee518d99cf6243e684c2f001fd1a4fe609ddc62da39d24153e3a1fd10a7b2)
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument flow_vpc_interface_name", value=flow_vpc_interface_name, expected_type=type_hints["flow_vpc_interface_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_arn": flow_arn,
            "flow_vpc_interface_name": flow_vpc_interface_name,
        }

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The FlowArn of the FlowVpcInterface resource.'''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flow_vpc_interface_name(self) -> builtins.str:
        '''The Name of the FlowVpcInterface resource.'''
        result = self._values.get("flow_vpc_interface_name")
        assert result is not None, "Required property 'flow_vpc_interface_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowVpcInterfaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.GatewayReference",
    jsii_struct_bases=[],
    name_mapping={"gateway_arn": "gatewayArn"},
)
class GatewayReference:
    def __init__(self, *, gateway_arn: builtins.str) -> None:
        '''A reference to a Gateway resource.

        :param gateway_arn: The GatewayArn of the Gateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            gateway_reference = interfaces_mediaconnect.GatewayReference(
                gateway_arn="gatewayArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44fc01aa24c69700318ae11a14f4daf44e0bf09d9678be7c8ad85380d73c70a1)
            check_type(argname="argument gateway_arn", value=gateway_arn, expected_type=type_hints["gateway_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_arn": gateway_arn,
        }

    @builtins.property
    def gateway_arn(self) -> builtins.str:
        '''The GatewayArn of the Gateway resource.'''
        result = self._values.get("gateway_arn")
        assert result is not None, "Required property 'gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IBridgeOutputRef")
class IBridgeOutputRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BridgeOutput.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="bridgeOutputRef")
    def bridge_output_ref(self) -> "BridgeOutputReference":
        '''(experimental) A reference to a BridgeOutput resource.

        :stability: experimental
        '''
        ...


class _IBridgeOutputRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BridgeOutput.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IBridgeOutputRef"

    @builtins.property
    @jsii.member(jsii_name="bridgeOutputRef")
    def bridge_output_ref(self) -> "BridgeOutputReference":
        '''(experimental) A reference to a BridgeOutput resource.

        :stability: experimental
        '''
        return typing.cast("BridgeOutputReference", jsii.get(self, "bridgeOutputRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBridgeOutputRef).__jsii_proxy_class__ = lambda : _IBridgeOutputRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IBridgeRef")
class IBridgeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Bridge.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="bridgeRef")
    def bridge_ref(self) -> "BridgeReference":
        '''(experimental) A reference to a Bridge resource.

        :stability: experimental
        '''
        ...


class _IBridgeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Bridge.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IBridgeRef"

    @builtins.property
    @jsii.member(jsii_name="bridgeRef")
    def bridge_ref(self) -> "BridgeReference":
        '''(experimental) A reference to a Bridge resource.

        :stability: experimental
        '''
        return typing.cast("BridgeReference", jsii.get(self, "bridgeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBridgeRef).__jsii_proxy_class__ = lambda : _IBridgeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IBridgeSourceRef")
class IBridgeSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BridgeSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="bridgeSourceRef")
    def bridge_source_ref(self) -> "BridgeSourceReference":
        '''(experimental) A reference to a BridgeSource resource.

        :stability: experimental
        '''
        ...


class _IBridgeSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BridgeSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IBridgeSourceRef"

    @builtins.property
    @jsii.member(jsii_name="bridgeSourceRef")
    def bridge_source_ref(self) -> "BridgeSourceReference":
        '''(experimental) A reference to a BridgeSource resource.

        :stability: experimental
        '''
        return typing.cast("BridgeSourceReference", jsii.get(self, "bridgeSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBridgeSourceRef).__jsii_proxy_class__ = lambda : _IBridgeSourceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IFlowEntitlementRef"
)
class IFlowEntitlementRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FlowEntitlement.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flowEntitlementRef")
    def flow_entitlement_ref(self) -> "FlowEntitlementReference":
        '''(experimental) A reference to a FlowEntitlement resource.

        :stability: experimental
        '''
        ...


class _IFlowEntitlementRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FlowEntitlement.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IFlowEntitlementRef"

    @builtins.property
    @jsii.member(jsii_name="flowEntitlementRef")
    def flow_entitlement_ref(self) -> "FlowEntitlementReference":
        '''(experimental) A reference to a FlowEntitlement resource.

        :stability: experimental
        '''
        return typing.cast("FlowEntitlementReference", jsii.get(self, "flowEntitlementRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowEntitlementRef).__jsii_proxy_class__ = lambda : _IFlowEntitlementRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IFlowOutputRef")
class IFlowOutputRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FlowOutput.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flowOutputRef")
    def flow_output_ref(self) -> "FlowOutputReference":
        '''(experimental) A reference to a FlowOutput resource.

        :stability: experimental
        '''
        ...


class _IFlowOutputRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FlowOutput.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IFlowOutputRef"

    @builtins.property
    @jsii.member(jsii_name="flowOutputRef")
    def flow_output_ref(self) -> "FlowOutputReference":
        '''(experimental) A reference to a FlowOutput resource.

        :stability: experimental
        '''
        return typing.cast("FlowOutputReference", jsii.get(self, "flowOutputRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowOutputRef).__jsii_proxy_class__ = lambda : _IFlowOutputRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IFlowRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IFlowRef"

    @builtins.property
    @jsii.member(jsii_name="flowRef")
    def flow_ref(self) -> "FlowReference":
        '''(experimental) A reference to a Flow resource.

        :stability: experimental
        '''
        return typing.cast("FlowReference", jsii.get(self, "flowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowRef).__jsii_proxy_class__ = lambda : _IFlowRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IFlowSourceRef")
class IFlowSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FlowSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flowSourceRef")
    def flow_source_ref(self) -> "FlowSourceReference":
        '''(experimental) A reference to a FlowSource resource.

        :stability: experimental
        '''
        ...


class _IFlowSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FlowSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IFlowSourceRef"

    @builtins.property
    @jsii.member(jsii_name="flowSourceRef")
    def flow_source_ref(self) -> "FlowSourceReference":
        '''(experimental) A reference to a FlowSource resource.

        :stability: experimental
        '''
        return typing.cast("FlowSourceReference", jsii.get(self, "flowSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowSourceRef).__jsii_proxy_class__ = lambda : _IFlowSourceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IFlowVpcInterfaceRef"
)
class IFlowVpcInterfaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FlowVpcInterface.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flowVpcInterfaceRef")
    def flow_vpc_interface_ref(self) -> "FlowVpcInterfaceReference":
        '''(experimental) A reference to a FlowVpcInterface resource.

        :stability: experimental
        '''
        ...


class _IFlowVpcInterfaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FlowVpcInterface.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IFlowVpcInterfaceRef"

    @builtins.property
    @jsii.member(jsii_name="flowVpcInterfaceRef")
    def flow_vpc_interface_ref(self) -> "FlowVpcInterfaceReference":
        '''(experimental) A reference to a FlowVpcInterface resource.

        :stability: experimental
        '''
        return typing.cast("FlowVpcInterfaceReference", jsii.get(self, "flowVpcInterfaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowVpcInterfaceRef).__jsii_proxy_class__ = lambda : _IFlowVpcInterfaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IGatewayRef")
class IGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Gateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gatewayRef")
    def gateway_ref(self) -> "GatewayReference":
        '''(experimental) A reference to a Gateway resource.

        :stability: experimental
        '''
        ...


class _IGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Gateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="gatewayRef")
    def gateway_ref(self) -> "GatewayReference":
        '''(experimental) A reference to a Gateway resource.

        :stability: experimental
        '''
        return typing.cast("GatewayReference", jsii.get(self, "gatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGatewayRef).__jsii_proxy_class__ = lambda : _IGatewayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IRouterInputRef")
class IRouterInputRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouterInput.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routerInputRef")
    def router_input_ref(self) -> "RouterInputReference":
        '''(experimental) A reference to a RouterInput resource.

        :stability: experimental
        '''
        ...


class _IRouterInputRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouterInput.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IRouterInputRef"

    @builtins.property
    @jsii.member(jsii_name="routerInputRef")
    def router_input_ref(self) -> "RouterInputReference":
        '''(experimental) A reference to a RouterInput resource.

        :stability: experimental
        '''
        return typing.cast("RouterInputReference", jsii.get(self, "routerInputRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouterInputRef).__jsii_proxy_class__ = lambda : _IRouterInputRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IRouterNetworkInterfaceRef"
)
class IRouterNetworkInterfaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouterNetworkInterface.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routerNetworkInterfaceRef")
    def router_network_interface_ref(self) -> "RouterNetworkInterfaceReference":
        '''(experimental) A reference to a RouterNetworkInterface resource.

        :stability: experimental
        '''
        ...


class _IRouterNetworkInterfaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouterNetworkInterface.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IRouterNetworkInterfaceRef"

    @builtins.property
    @jsii.member(jsii_name="routerNetworkInterfaceRef")
    def router_network_interface_ref(self) -> "RouterNetworkInterfaceReference":
        '''(experimental) A reference to a RouterNetworkInterface resource.

        :stability: experimental
        '''
        return typing.cast("RouterNetworkInterfaceReference", jsii.get(self, "routerNetworkInterfaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouterNetworkInterfaceRef).__jsii_proxy_class__ = lambda : _IRouterNetworkInterfaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.IRouterOutputRef")
class IRouterOutputRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RouterOutput.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routerOutputRef")
    def router_output_ref(self) -> "RouterOutputReference":
        '''(experimental) A reference to a RouterOutput resource.

        :stability: experimental
        '''
        ...


class _IRouterOutputRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RouterOutput.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediaconnect.IRouterOutputRef"

    @builtins.property
    @jsii.member(jsii_name="routerOutputRef")
    def router_output_ref(self) -> "RouterOutputReference":
        '''(experimental) A reference to a RouterOutput resource.

        :stability: experimental
        '''
        return typing.cast("RouterOutputReference", jsii.get(self, "routerOutputRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouterOutputRef).__jsii_proxy_class__ = lambda : _IRouterOutputRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.RouterInputReference",
    jsii_struct_bases=[],
    name_mapping={"router_input_arn": "routerInputArn"},
)
class RouterInputReference:
    def __init__(self, *, router_input_arn: builtins.str) -> None:
        '''A reference to a RouterInput resource.

        :param router_input_arn: The Arn of the RouterInput resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            router_input_reference = interfaces_mediaconnect.RouterInputReference(
                router_input_arn="routerInputArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ed9ce4be85dfab764f028608ee5a4495bcc6912e55aac3d482ac0f847879dd8)
            check_type(argname="argument router_input_arn", value=router_input_arn, expected_type=type_hints["router_input_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "router_input_arn": router_input_arn,
        }

    @builtins.property
    def router_input_arn(self) -> builtins.str:
        '''The Arn of the RouterInput resource.'''
        result = self._values.get("router_input_arn")
        assert result is not None, "Required property 'router_input_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouterInputReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.RouterNetworkInterfaceReference",
    jsii_struct_bases=[],
    name_mapping={"router_network_interface_arn": "routerNetworkInterfaceArn"},
)
class RouterNetworkInterfaceReference:
    def __init__(self, *, router_network_interface_arn: builtins.str) -> None:
        '''A reference to a RouterNetworkInterface resource.

        :param router_network_interface_arn: The Arn of the RouterNetworkInterface resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            router_network_interface_reference = interfaces_mediaconnect.RouterNetworkInterfaceReference(
                router_network_interface_arn="routerNetworkInterfaceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6402a2957d68c201351255b35b741d64087684d0195556ad2b446d5aea60393b)
            check_type(argname="argument router_network_interface_arn", value=router_network_interface_arn, expected_type=type_hints["router_network_interface_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "router_network_interface_arn": router_network_interface_arn,
        }

    @builtins.property
    def router_network_interface_arn(self) -> builtins.str:
        '''The Arn of the RouterNetworkInterface resource.'''
        result = self._values.get("router_network_interface_arn")
        assert result is not None, "Required property 'router_network_interface_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouterNetworkInterfaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediaconnect.RouterOutputReference",
    jsii_struct_bases=[],
    name_mapping={"router_output_arn": "routerOutputArn"},
)
class RouterOutputReference:
    def __init__(self, *, router_output_arn: builtins.str) -> None:
        '''A reference to a RouterOutput resource.

        :param router_output_arn: The Arn of the RouterOutput resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediaconnect as interfaces_mediaconnect
            
            router_output_reference = interfaces_mediaconnect.RouterOutputReference(
                router_output_arn="routerOutputArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb1ab08a2a2f206b84e407515955ae1d24f39785cfe1e4e1df154f9ce21e292b)
            check_type(argname="argument router_output_arn", value=router_output_arn, expected_type=type_hints["router_output_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "router_output_arn": router_output_arn,
        }

    @builtins.property
    def router_output_arn(self) -> builtins.str:
        '''The Arn of the RouterOutput resource.'''
        result = self._values.get("router_output_arn")
        assert result is not None, "Required property 'router_output_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouterOutputReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BridgeOutputReference",
    "BridgeReference",
    "BridgeSourceReference",
    "FlowEntitlementReference",
    "FlowOutputReference",
    "FlowReference",
    "FlowSourceReference",
    "FlowVpcInterfaceReference",
    "GatewayReference",
    "IBridgeOutputRef",
    "IBridgeRef",
    "IBridgeSourceRef",
    "IFlowEntitlementRef",
    "IFlowOutputRef",
    "IFlowRef",
    "IFlowSourceRef",
    "IFlowVpcInterfaceRef",
    "IGatewayRef",
    "IRouterInputRef",
    "IRouterNetworkInterfaceRef",
    "IRouterOutputRef",
    "RouterInputReference",
    "RouterNetworkInterfaceReference",
    "RouterOutputReference",
]

publication.publish()

def _typecheckingstub__73182f10d25757e57316dcdbde383b2563dd187db8a77ce9d9b64f432f3132b2(
    *,
    bridge_arn: builtins.str,
    bridge_output_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7440fa6612c678dd575ec05ad66dc7948fc8c70e784c74785f80ab5356faec4(
    *,
    bridge_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a57ab8b2799544f17aecf266ba0a305c9946b460679a831f68a8cc2667ab5ce(
    *,
    bridge_arn: builtins.str,
    bridge_source_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0edc53b6b6e960dbdc6bd64c4eb6c4541ecc0a17bdd262b31812971a606f44ad(
    *,
    entitlement_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d86e4aa7f442e2ea027387f7ae0fa891b3494c4e892279cf982fa261e9fe71de(
    *,
    output_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b8601eaf471f9bacfb5f3d93788a33c0fcea9ec28ec13b3ec3b0a0e901ce8c3(
    *,
    flow_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__324aca350b47900f430f689f94e3804fb4163b2fedf800ae93532fba0c81ff41(
    *,
    source_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e0ee518d99cf6243e684c2f001fd1a4fe609ddc62da39d24153e3a1fd10a7b2(
    *,
    flow_arn: builtins.str,
    flow_vpc_interface_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44fc01aa24c69700318ae11a14f4daf44e0bf09d9678be7c8ad85380d73c70a1(
    *,
    gateway_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ed9ce4be85dfab764f028608ee5a4495bcc6912e55aac3d482ac0f847879dd8(
    *,
    router_input_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6402a2957d68c201351255b35b741d64087684d0195556ad2b446d5aea60393b(
    *,
    router_network_interface_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb1ab08a2a2f206b84e407515955ae1d24f39785cfe1e4e1df154f9ce21e292b(
    *,
    router_output_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBridgeOutputRef, IBridgeRef, IBridgeSourceRef, IFlowEntitlementRef, IFlowOutputRef, IFlowRef, IFlowSourceRef, IFlowVpcInterfaceRef, IGatewayRef, IRouterInputRef, IRouterNetworkInterfaceRef, IRouterOutputRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
