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
    jsii_type="aws-cdk-lib.interfaces.aws_appmesh.GatewayRouteReference",
    jsii_struct_bases=[],
    name_mapping={"gateway_route_arn": "gatewayRouteArn"},
)
class GatewayRouteReference:
    def __init__(self, *, gateway_route_arn: builtins.str) -> None:
        '''A reference to a GatewayRoute resource.

        :param gateway_route_arn: The Arn of the GatewayRoute resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appmesh as interfaces_appmesh
            
            gateway_route_reference = interfaces_appmesh.GatewayRouteReference(
                gateway_route_arn="gatewayRouteArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32f9dfc866e97093a7680c54e7baaba765d04e694a0898a329ffd7263580b8b3)
            check_type(argname="argument gateway_route_arn", value=gateway_route_arn, expected_type=type_hints["gateway_route_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_route_arn": gateway_route_arn,
        }

    @builtins.property
    def gateway_route_arn(self) -> builtins.str:
        '''The Arn of the GatewayRoute resource.'''
        result = self._values.get("gateway_route_arn")
        assert result is not None, "Required property 'gateway_route_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GatewayRouteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appmesh.IGatewayRouteRef")
class IGatewayRouteRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GatewayRoute.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gatewayRouteRef")
    def gateway_route_ref(self) -> "GatewayRouteReference":
        '''(experimental) A reference to a GatewayRoute resource.

        :stability: experimental
        '''
        ...


class _IGatewayRouteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GatewayRoute.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appmesh.IGatewayRouteRef"

    @builtins.property
    @jsii.member(jsii_name="gatewayRouteRef")
    def gateway_route_ref(self) -> "GatewayRouteReference":
        '''(experimental) A reference to a GatewayRoute resource.

        :stability: experimental
        '''
        return typing.cast("GatewayRouteReference", jsii.get(self, "gatewayRouteRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGatewayRouteRef).__jsii_proxy_class__ = lambda : _IGatewayRouteRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appmesh.IMeshRef")
class IMeshRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Mesh.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="meshRef")
    def mesh_ref(self) -> "MeshReference":
        '''(experimental) A reference to a Mesh resource.

        :stability: experimental
        '''
        ...


class _IMeshRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Mesh.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appmesh.IMeshRef"

    @builtins.property
    @jsii.member(jsii_name="meshRef")
    def mesh_ref(self) -> "MeshReference":
        '''(experimental) A reference to a Mesh resource.

        :stability: experimental
        '''
        return typing.cast("MeshReference", jsii.get(self, "meshRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMeshRef).__jsii_proxy_class__ = lambda : _IMeshRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appmesh.IRouteRef")
class IRouteRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Route.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeRef")
    def route_ref(self) -> "RouteReference":
        '''(experimental) A reference to a Route resource.

        :stability: experimental
        '''
        ...


class _IRouteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Route.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appmesh.IRouteRef"

    @builtins.property
    @jsii.member(jsii_name="routeRef")
    def route_ref(self) -> "RouteReference":
        '''(experimental) A reference to a Route resource.

        :stability: experimental
        '''
        return typing.cast("RouteReference", jsii.get(self, "routeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteRef).__jsii_proxy_class__ = lambda : _IRouteRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appmesh.IVirtualGatewayRef")
class IVirtualGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="virtualGatewayRef")
    def virtual_gateway_ref(self) -> "VirtualGatewayReference":
        '''(experimental) A reference to a VirtualGateway resource.

        :stability: experimental
        '''
        ...


class _IVirtualGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appmesh.IVirtualGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="virtualGatewayRef")
    def virtual_gateway_ref(self) -> "VirtualGatewayReference":
        '''(experimental) A reference to a VirtualGateway resource.

        :stability: experimental
        '''
        return typing.cast("VirtualGatewayReference", jsii.get(self, "virtualGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualGatewayRef).__jsii_proxy_class__ = lambda : _IVirtualGatewayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appmesh.IVirtualNodeRef")
class IVirtualNodeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualNode.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="virtualNodeRef")
    def virtual_node_ref(self) -> "VirtualNodeReference":
        '''(experimental) A reference to a VirtualNode resource.

        :stability: experimental
        '''
        ...


class _IVirtualNodeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualNode.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appmesh.IVirtualNodeRef"

    @builtins.property
    @jsii.member(jsii_name="virtualNodeRef")
    def virtual_node_ref(self) -> "VirtualNodeReference":
        '''(experimental) A reference to a VirtualNode resource.

        :stability: experimental
        '''
        return typing.cast("VirtualNodeReference", jsii.get(self, "virtualNodeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualNodeRef).__jsii_proxy_class__ = lambda : _IVirtualNodeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appmesh.IVirtualRouterRef")
class IVirtualRouterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualRouter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="virtualRouterRef")
    def virtual_router_ref(self) -> "VirtualRouterReference":
        '''(experimental) A reference to a VirtualRouter resource.

        :stability: experimental
        '''
        ...


class _IVirtualRouterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualRouter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appmesh.IVirtualRouterRef"

    @builtins.property
    @jsii.member(jsii_name="virtualRouterRef")
    def virtual_router_ref(self) -> "VirtualRouterReference":
        '''(experimental) A reference to a VirtualRouter resource.

        :stability: experimental
        '''
        return typing.cast("VirtualRouterReference", jsii.get(self, "virtualRouterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualRouterRef).__jsii_proxy_class__ = lambda : _IVirtualRouterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appmesh.IVirtualServiceRef")
class IVirtualServiceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualService.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="virtualServiceRef")
    def virtual_service_ref(self) -> "VirtualServiceReference":
        '''(experimental) A reference to a VirtualService resource.

        :stability: experimental
        '''
        ...


class _IVirtualServiceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualService.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appmesh.IVirtualServiceRef"

    @builtins.property
    @jsii.member(jsii_name="virtualServiceRef")
    def virtual_service_ref(self) -> "VirtualServiceReference":
        '''(experimental) A reference to a VirtualService resource.

        :stability: experimental
        '''
        return typing.cast("VirtualServiceReference", jsii.get(self, "virtualServiceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualServiceRef).__jsii_proxy_class__ = lambda : _IVirtualServiceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appmesh.MeshReference",
    jsii_struct_bases=[],
    name_mapping={"mesh_arn": "meshArn"},
)
class MeshReference:
    def __init__(self, *, mesh_arn: builtins.str) -> None:
        '''A reference to a Mesh resource.

        :param mesh_arn: The Arn of the Mesh resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appmesh as interfaces_appmesh
            
            mesh_reference = interfaces_appmesh.MeshReference(
                mesh_arn="meshArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b90d52e88f982a2eae93b3122a7a4c5eecc4ef9a4b13b5c948b3446f391e924)
            check_type(argname="argument mesh_arn", value=mesh_arn, expected_type=type_hints["mesh_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mesh_arn": mesh_arn,
        }

    @builtins.property
    def mesh_arn(self) -> builtins.str:
        '''The Arn of the Mesh resource.'''
        result = self._values.get("mesh_arn")
        assert result is not None, "Required property 'mesh_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MeshReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appmesh.RouteReference",
    jsii_struct_bases=[],
    name_mapping={"route_arn": "routeArn"},
)
class RouteReference:
    def __init__(self, *, route_arn: builtins.str) -> None:
        '''A reference to a Route resource.

        :param route_arn: The Arn of the Route resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appmesh as interfaces_appmesh
            
            route_reference = interfaces_appmesh.RouteReference(
                route_arn="routeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69bbf3d73f757ba9320fb88c0be633121bdabd4fc70b89f3cf930233e793be1b)
            check_type(argname="argument route_arn", value=route_arn, expected_type=type_hints["route_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "route_arn": route_arn,
        }

    @builtins.property
    def route_arn(self) -> builtins.str:
        '''The Arn of the Route resource.'''
        result = self._values.get("route_arn")
        assert result is not None, "Required property 'route_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appmesh.VirtualGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"virtual_gateway_arn": "virtualGatewayArn"},
)
class VirtualGatewayReference:
    def __init__(self, *, virtual_gateway_arn: builtins.str) -> None:
        '''A reference to a VirtualGateway resource.

        :param virtual_gateway_arn: The Arn of the VirtualGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appmesh as interfaces_appmesh
            
            virtual_gateway_reference = interfaces_appmesh.VirtualGatewayReference(
                virtual_gateway_arn="virtualGatewayArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a3f6112a2ac96415941139a80c912bcbd3cc4150f9d19ffb2ed8301bc438506)
            check_type(argname="argument virtual_gateway_arn", value=virtual_gateway_arn, expected_type=type_hints["virtual_gateway_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_gateway_arn": virtual_gateway_arn,
        }

    @builtins.property
    def virtual_gateway_arn(self) -> builtins.str:
        '''The Arn of the VirtualGateway resource.'''
        result = self._values.get("virtual_gateway_arn")
        assert result is not None, "Required property 'virtual_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appmesh.VirtualNodeReference",
    jsii_struct_bases=[],
    name_mapping={"virtual_node_arn": "virtualNodeArn"},
)
class VirtualNodeReference:
    def __init__(self, *, virtual_node_arn: builtins.str) -> None:
        '''A reference to a VirtualNode resource.

        :param virtual_node_arn: The Arn of the VirtualNode resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appmesh as interfaces_appmesh
            
            virtual_node_reference = interfaces_appmesh.VirtualNodeReference(
                virtual_node_arn="virtualNodeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5598969a1377de6ec924d41db272dd5dd531fc0efe16da92d5a1cbd9267d4ee8)
            check_type(argname="argument virtual_node_arn", value=virtual_node_arn, expected_type=type_hints["virtual_node_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_node_arn": virtual_node_arn,
        }

    @builtins.property
    def virtual_node_arn(self) -> builtins.str:
        '''The Arn of the VirtualNode resource.'''
        result = self._values.get("virtual_node_arn")
        assert result is not None, "Required property 'virtual_node_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualNodeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appmesh.VirtualRouterReference",
    jsii_struct_bases=[],
    name_mapping={"virtual_router_arn": "virtualRouterArn"},
)
class VirtualRouterReference:
    def __init__(self, *, virtual_router_arn: builtins.str) -> None:
        '''A reference to a VirtualRouter resource.

        :param virtual_router_arn: The Arn of the VirtualRouter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appmesh as interfaces_appmesh
            
            virtual_router_reference = interfaces_appmesh.VirtualRouterReference(
                virtual_router_arn="virtualRouterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30b6512320fa651664ac7d23cd15a484325a424f57eed28afda6ea95f36525f8)
            check_type(argname="argument virtual_router_arn", value=virtual_router_arn, expected_type=type_hints["virtual_router_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_router_arn": virtual_router_arn,
        }

    @builtins.property
    def virtual_router_arn(self) -> builtins.str:
        '''The Arn of the VirtualRouter resource.'''
        result = self._values.get("virtual_router_arn")
        assert result is not None, "Required property 'virtual_router_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualRouterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appmesh.VirtualServiceReference",
    jsii_struct_bases=[],
    name_mapping={"virtual_service_arn": "virtualServiceArn"},
)
class VirtualServiceReference:
    def __init__(self, *, virtual_service_arn: builtins.str) -> None:
        '''A reference to a VirtualService resource.

        :param virtual_service_arn: The Arn of the VirtualService resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appmesh as interfaces_appmesh
            
            virtual_service_reference = interfaces_appmesh.VirtualServiceReference(
                virtual_service_arn="virtualServiceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31a1da06971cf3191917cdf6392ad724b0f7117725e942fd00648526ac541a5c)
            check_type(argname="argument virtual_service_arn", value=virtual_service_arn, expected_type=type_hints["virtual_service_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_service_arn": virtual_service_arn,
        }

    @builtins.property
    def virtual_service_arn(self) -> builtins.str:
        '''The Arn of the VirtualService resource.'''
        result = self._values.get("virtual_service_arn")
        assert result is not None, "Required property 'virtual_service_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualServiceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GatewayRouteReference",
    "IGatewayRouteRef",
    "IMeshRef",
    "IRouteRef",
    "IVirtualGatewayRef",
    "IVirtualNodeRef",
    "IVirtualRouterRef",
    "IVirtualServiceRef",
    "MeshReference",
    "RouteReference",
    "VirtualGatewayReference",
    "VirtualNodeReference",
    "VirtualRouterReference",
    "VirtualServiceReference",
]

publication.publish()

def _typecheckingstub__32f9dfc866e97093a7680c54e7baaba765d04e694a0898a329ffd7263580b8b3(
    *,
    gateway_route_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b90d52e88f982a2eae93b3122a7a4c5eecc4ef9a4b13b5c948b3446f391e924(
    *,
    mesh_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69bbf3d73f757ba9320fb88c0be633121bdabd4fc70b89f3cf930233e793be1b(
    *,
    route_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a3f6112a2ac96415941139a80c912bcbd3cc4150f9d19ffb2ed8301bc438506(
    *,
    virtual_gateway_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5598969a1377de6ec924d41db272dd5dd531fc0efe16da92d5a1cbd9267d4ee8(
    *,
    virtual_node_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b6512320fa651664ac7d23cd15a484325a424f57eed28afda6ea95f36525f8(
    *,
    virtual_router_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31a1da06971cf3191917cdf6392ad724b0f7117725e942fd00648526ac541a5c(
    *,
    virtual_service_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IGatewayRouteRef, IMeshRef, IRouteRef, IVirtualGatewayRef, IVirtualNodeRef, IVirtualRouterRef, IVirtualServiceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
