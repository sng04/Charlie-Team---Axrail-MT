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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_rtbfabric.IInboundExternalLinkRef"
)
class IInboundExternalLinkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InboundExternalLink.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="inboundExternalLinkRef")
    def inbound_external_link_ref(self) -> "InboundExternalLinkReference":
        '''(experimental) A reference to a InboundExternalLink resource.

        :stability: experimental
        '''
        ...


class _IInboundExternalLinkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InboundExternalLink.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rtbfabric.IInboundExternalLinkRef"

    @builtins.property
    @jsii.member(jsii_name="inboundExternalLinkRef")
    def inbound_external_link_ref(self) -> "InboundExternalLinkReference":
        '''(experimental) A reference to a InboundExternalLink resource.

        :stability: experimental
        '''
        return typing.cast("InboundExternalLinkReference", jsii.get(self, "inboundExternalLinkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInboundExternalLinkRef).__jsii_proxy_class__ = lambda : _IInboundExternalLinkRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rtbfabric.ILinkRef")
class ILinkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Link.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="linkRef")
    def link_ref(self) -> "LinkReference":
        '''(experimental) A reference to a Link resource.

        :stability: experimental
        '''
        ...


class _ILinkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Link.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rtbfabric.ILinkRef"

    @builtins.property
    @jsii.member(jsii_name="linkRef")
    def link_ref(self) -> "LinkReference":
        '''(experimental) A reference to a Link resource.

        :stability: experimental
        '''
        return typing.cast("LinkReference", jsii.get(self, "linkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILinkRef).__jsii_proxy_class__ = lambda : _ILinkRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_rtbfabric.IOutboundExternalLinkRef"
)
class IOutboundExternalLinkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OutboundExternalLink.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="outboundExternalLinkRef")
    def outbound_external_link_ref(self) -> "OutboundExternalLinkReference":
        '''(experimental) A reference to a OutboundExternalLink resource.

        :stability: experimental
        '''
        ...


class _IOutboundExternalLinkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OutboundExternalLink.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rtbfabric.IOutboundExternalLinkRef"

    @builtins.property
    @jsii.member(jsii_name="outboundExternalLinkRef")
    def outbound_external_link_ref(self) -> "OutboundExternalLinkReference":
        '''(experimental) A reference to a OutboundExternalLink resource.

        :stability: experimental
        '''
        return typing.cast("OutboundExternalLinkReference", jsii.get(self, "outboundExternalLinkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOutboundExternalLinkRef).__jsii_proxy_class__ = lambda : _IOutboundExternalLinkRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rtbfabric.IRequesterGatewayRef")
class IRequesterGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RequesterGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="requesterGatewayRef")
    def requester_gateway_ref(self) -> "RequesterGatewayReference":
        '''(experimental) A reference to a RequesterGateway resource.

        :stability: experimental
        '''
        ...


class _IRequesterGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RequesterGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rtbfabric.IRequesterGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="requesterGatewayRef")
    def requester_gateway_ref(self) -> "RequesterGatewayReference":
        '''(experimental) A reference to a RequesterGateway resource.

        :stability: experimental
        '''
        return typing.cast("RequesterGatewayReference", jsii.get(self, "requesterGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRequesterGatewayRef).__jsii_proxy_class__ = lambda : _IRequesterGatewayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rtbfabric.IResponderGatewayRef")
class IResponderGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResponderGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="responderGatewayRef")
    def responder_gateway_ref(self) -> "ResponderGatewayReference":
        '''(experimental) A reference to a ResponderGateway resource.

        :stability: experimental
        '''
        ...


class _IResponderGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResponderGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rtbfabric.IResponderGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="responderGatewayRef")
    def responder_gateway_ref(self) -> "ResponderGatewayReference":
        '''(experimental) A reference to a ResponderGateway resource.

        :stability: experimental
        '''
        return typing.cast("ResponderGatewayReference", jsii.get(self, "responderGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResponderGatewayRef).__jsii_proxy_class__ = lambda : _IResponderGatewayRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rtbfabric.InboundExternalLinkReference",
    jsii_struct_bases=[],
    name_mapping={"inbound_external_link_arn": "inboundExternalLinkArn"},
)
class InboundExternalLinkReference:
    def __init__(self, *, inbound_external_link_arn: builtins.str) -> None:
        '''A reference to a InboundExternalLink resource.

        :param inbound_external_link_arn: The Arn of the InboundExternalLink resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rtbfabric as interfaces_rtbfabric
            
            inbound_external_link_reference = interfaces_rtbfabric.InboundExternalLinkReference(
                inbound_external_link_arn="inboundExternalLinkArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdfa6fc10753fecc7651354ecdbd49e27d9714a8b6b2781df195ab63efd6bc3c)
            check_type(argname="argument inbound_external_link_arn", value=inbound_external_link_arn, expected_type=type_hints["inbound_external_link_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "inbound_external_link_arn": inbound_external_link_arn,
        }

    @builtins.property
    def inbound_external_link_arn(self) -> builtins.str:
        '''The Arn of the InboundExternalLink resource.'''
        result = self._values.get("inbound_external_link_arn")
        assert result is not None, "Required property 'inbound_external_link_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InboundExternalLinkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rtbfabric.LinkReference",
    jsii_struct_bases=[],
    name_mapping={"link_arn": "linkArn"},
)
class LinkReference:
    def __init__(self, *, link_arn: builtins.str) -> None:
        '''A reference to a Link resource.

        :param link_arn: The Arn of the Link resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rtbfabric as interfaces_rtbfabric
            
            link_reference = interfaces_rtbfabric.LinkReference(
                link_arn="linkArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ee5fdcf0604322dd959fcfe412ef348575c9fb082efe86a373a6d37ab6c070f)
            check_type(argname="argument link_arn", value=link_arn, expected_type=type_hints["link_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "link_arn": link_arn,
        }

    @builtins.property
    def link_arn(self) -> builtins.str:
        '''The Arn of the Link resource.'''
        result = self._values.get("link_arn")
        assert result is not None, "Required property 'link_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rtbfabric.OutboundExternalLinkReference",
    jsii_struct_bases=[],
    name_mapping={"outbound_external_link_arn": "outboundExternalLinkArn"},
)
class OutboundExternalLinkReference:
    def __init__(self, *, outbound_external_link_arn: builtins.str) -> None:
        '''A reference to a OutboundExternalLink resource.

        :param outbound_external_link_arn: The Arn of the OutboundExternalLink resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rtbfabric as interfaces_rtbfabric
            
            outbound_external_link_reference = interfaces_rtbfabric.OutboundExternalLinkReference(
                outbound_external_link_arn="outboundExternalLinkArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee3a7fe3807b978c616b6ff52440409d21008b6ac11275f68bfac4ed14dbb2e2)
            check_type(argname="argument outbound_external_link_arn", value=outbound_external_link_arn, expected_type=type_hints["outbound_external_link_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "outbound_external_link_arn": outbound_external_link_arn,
        }

    @builtins.property
    def outbound_external_link_arn(self) -> builtins.str:
        '''The Arn of the OutboundExternalLink resource.'''
        result = self._values.get("outbound_external_link_arn")
        assert result is not None, "Required property 'outbound_external_link_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OutboundExternalLinkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rtbfabric.RequesterGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"requester_gateway_arn": "requesterGatewayArn"},
)
class RequesterGatewayReference:
    def __init__(self, *, requester_gateway_arn: builtins.str) -> None:
        '''A reference to a RequesterGateway resource.

        :param requester_gateway_arn: The Arn of the RequesterGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rtbfabric as interfaces_rtbfabric
            
            requester_gateway_reference = interfaces_rtbfabric.RequesterGatewayReference(
                requester_gateway_arn="requesterGatewayArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cda403205169364e19a675d26bc881462955f89c5b85cf1af97223cf28bf1371)
            check_type(argname="argument requester_gateway_arn", value=requester_gateway_arn, expected_type=type_hints["requester_gateway_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "requester_gateway_arn": requester_gateway_arn,
        }

    @builtins.property
    def requester_gateway_arn(self) -> builtins.str:
        '''The Arn of the RequesterGateway resource.'''
        result = self._values.get("requester_gateway_arn")
        assert result is not None, "Required property 'requester_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RequesterGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rtbfabric.ResponderGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"responder_gateway_arn": "responderGatewayArn"},
)
class ResponderGatewayReference:
    def __init__(self, *, responder_gateway_arn: builtins.str) -> None:
        '''A reference to a ResponderGateway resource.

        :param responder_gateway_arn: The Arn of the ResponderGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rtbfabric as interfaces_rtbfabric
            
            responder_gateway_reference = interfaces_rtbfabric.ResponderGatewayReference(
                responder_gateway_arn="responderGatewayArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f992d87253eb02f346f69b0f2d9924f3e82c06510bf2db9b3bead8a840038c0)
            check_type(argname="argument responder_gateway_arn", value=responder_gateway_arn, expected_type=type_hints["responder_gateway_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "responder_gateway_arn": responder_gateway_arn,
        }

    @builtins.property
    def responder_gateway_arn(self) -> builtins.str:
        '''The Arn of the ResponderGateway resource.'''
        result = self._values.get("responder_gateway_arn")
        assert result is not None, "Required property 'responder_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResponderGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IInboundExternalLinkRef",
    "ILinkRef",
    "IOutboundExternalLinkRef",
    "IRequesterGatewayRef",
    "IResponderGatewayRef",
    "InboundExternalLinkReference",
    "LinkReference",
    "OutboundExternalLinkReference",
    "RequesterGatewayReference",
    "ResponderGatewayReference",
]

publication.publish()

def _typecheckingstub__bdfa6fc10753fecc7651354ecdbd49e27d9714a8b6b2781df195ab63efd6bc3c(
    *,
    inbound_external_link_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ee5fdcf0604322dd959fcfe412ef348575c9fb082efe86a373a6d37ab6c070f(
    *,
    link_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee3a7fe3807b978c616b6ff52440409d21008b6ac11275f68bfac4ed14dbb2e2(
    *,
    outbound_external_link_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cda403205169364e19a675d26bc881462955f89c5b85cf1af97223cf28bf1371(
    *,
    requester_gateway_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f992d87253eb02f346f69b0f2d9924f3e82c06510bf2db9b3bead8a840038c0(
    *,
    responder_gateway_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IInboundExternalLinkRef, ILinkRef, IOutboundExternalLinkRef, IRequesterGatewayRef, IResponderGatewayRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
