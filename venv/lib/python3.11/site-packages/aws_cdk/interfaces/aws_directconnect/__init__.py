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
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.ConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"connection_arn": "connectionArn"},
)
class ConnectionReference:
    def __init__(self, *, connection_arn: builtins.str) -> None:
        '''A reference to a Connection resource.

        :param connection_arn: The ConnectionArn of the Connection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_directconnect as interfaces_directconnect
            
            connection_reference = interfaces_directconnect.ConnectionReference(
                connection_arn="connectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecc1baa45366df795416273ab50a10d994aba4b4bd3eaea1aad1724372ad7c0d)
            check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_arn": connection_arn,
        }

    @builtins.property
    def connection_arn(self) -> builtins.str:
        '''The ConnectionArn of the Connection resource.'''
        result = self._values.get("connection_arn")
        assert result is not None, "Required property 'connection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.DirectConnectGatewayAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"association_id": "associationId"},
)
class DirectConnectGatewayAssociationReference:
    def __init__(self, *, association_id: builtins.str) -> None:
        '''A reference to a DirectConnectGatewayAssociation resource.

        :param association_id: The AssociationId of the DirectConnectGatewayAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_directconnect as interfaces_directconnect
            
            direct_connect_gateway_association_reference = interfaces_directconnect.DirectConnectGatewayAssociationReference(
                association_id="associationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f3e59a2b0118d3f066d12696601397ea35c407bdf689d829eaad636f9e6defc)
            check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_id": association_id,
        }

    @builtins.property
    def association_id(self) -> builtins.str:
        '''The AssociationId of the DirectConnectGatewayAssociation resource.'''
        result = self._values.get("association_id")
        assert result is not None, "Required property 'association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectConnectGatewayAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.DirectConnectGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"direct_connect_gateway_arn": "directConnectGatewayArn"},
)
class DirectConnectGatewayReference:
    def __init__(self, *, direct_connect_gateway_arn: builtins.str) -> None:
        '''A reference to a DirectConnectGateway resource.

        :param direct_connect_gateway_arn: The DirectConnectGatewayArn of the DirectConnectGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_directconnect as interfaces_directconnect
            
            direct_connect_gateway_reference = interfaces_directconnect.DirectConnectGatewayReference(
                direct_connect_gateway_arn="directConnectGatewayArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c20f5c45ba60148433cd3c2e5af50999fe635c2e2e52eb9663f1741bd2a2b423)
            check_type(argname="argument direct_connect_gateway_arn", value=direct_connect_gateway_arn, expected_type=type_hints["direct_connect_gateway_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "direct_connect_gateway_arn": direct_connect_gateway_arn,
        }

    @builtins.property
    def direct_connect_gateway_arn(self) -> builtins.str:
        '''The DirectConnectGatewayArn of the DirectConnectGateway resource.'''
        result = self._values.get("direct_connect_gateway_arn")
        assert result is not None, "Required property 'direct_connect_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectConnectGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_directconnect.IConnectionRef")
class IConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        ...


class _IConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_directconnect.IConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionReference", jsii.get(self, "connectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionRef).__jsii_proxy_class__ = lambda : _IConnectionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.IDirectConnectGatewayAssociationRef"
)
class IDirectConnectGatewayAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DirectConnectGatewayAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayAssociationRef")
    def direct_connect_gateway_association_ref(
        self,
    ) -> "DirectConnectGatewayAssociationReference":
        '''(experimental) A reference to a DirectConnectGatewayAssociation resource.

        :stability: experimental
        '''
        ...


class _IDirectConnectGatewayAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DirectConnectGatewayAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_directconnect.IDirectConnectGatewayAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayAssociationRef")
    def direct_connect_gateway_association_ref(
        self,
    ) -> "DirectConnectGatewayAssociationReference":
        '''(experimental) A reference to a DirectConnectGatewayAssociation resource.

        :stability: experimental
        '''
        return typing.cast("DirectConnectGatewayAssociationReference", jsii.get(self, "directConnectGatewayAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDirectConnectGatewayAssociationRef).__jsii_proxy_class__ = lambda : _IDirectConnectGatewayAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.IDirectConnectGatewayRef"
)
class IDirectConnectGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DirectConnectGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayRef")
    def direct_connect_gateway_ref(self) -> "DirectConnectGatewayReference":
        '''(experimental) A reference to a DirectConnectGateway resource.

        :stability: experimental
        '''
        ...


class _IDirectConnectGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DirectConnectGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_directconnect.IDirectConnectGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayRef")
    def direct_connect_gateway_ref(self) -> "DirectConnectGatewayReference":
        '''(experimental) A reference to a DirectConnectGateway resource.

        :stability: experimental
        '''
        return typing.cast("DirectConnectGatewayReference", jsii.get(self, "directConnectGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDirectConnectGatewayRef).__jsii_proxy_class__ = lambda : _IDirectConnectGatewayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_directconnect.ILagRef")
class ILagRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Lag.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="lagRef")
    def lag_ref(self) -> "LagReference":
        '''(experimental) A reference to a Lag resource.

        :stability: experimental
        '''
        ...


class _ILagRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Lag.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_directconnect.ILagRef"

    @builtins.property
    @jsii.member(jsii_name="lagRef")
    def lag_ref(self) -> "LagReference":
        '''(experimental) A reference to a Lag resource.

        :stability: experimental
        '''
        return typing.cast("LagReference", jsii.get(self, "lagRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILagRef).__jsii_proxy_class__ = lambda : _ILagRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.IPrivateVirtualInterfaceRef"
)
class IPrivateVirtualInterfaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PrivateVirtualInterface.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="privateVirtualInterfaceRef")
    def private_virtual_interface_ref(self) -> "PrivateVirtualInterfaceReference":
        '''(experimental) A reference to a PrivateVirtualInterface resource.

        :stability: experimental
        '''
        ...


class _IPrivateVirtualInterfaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PrivateVirtualInterface.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_directconnect.IPrivateVirtualInterfaceRef"

    @builtins.property
    @jsii.member(jsii_name="privateVirtualInterfaceRef")
    def private_virtual_interface_ref(self) -> "PrivateVirtualInterfaceReference":
        '''(experimental) A reference to a PrivateVirtualInterface resource.

        :stability: experimental
        '''
        return typing.cast("PrivateVirtualInterfaceReference", jsii.get(self, "privateVirtualInterfaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrivateVirtualInterfaceRef).__jsii_proxy_class__ = lambda : _IPrivateVirtualInterfaceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.IPublicVirtualInterfaceRef"
)
class IPublicVirtualInterfaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PublicVirtualInterface.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="publicVirtualInterfaceRef")
    def public_virtual_interface_ref(self) -> "PublicVirtualInterfaceReference":
        '''(experimental) A reference to a PublicVirtualInterface resource.

        :stability: experimental
        '''
        ...


class _IPublicVirtualInterfaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PublicVirtualInterface.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_directconnect.IPublicVirtualInterfaceRef"

    @builtins.property
    @jsii.member(jsii_name="publicVirtualInterfaceRef")
    def public_virtual_interface_ref(self) -> "PublicVirtualInterfaceReference":
        '''(experimental) A reference to a PublicVirtualInterface resource.

        :stability: experimental
        '''
        return typing.cast("PublicVirtualInterfaceReference", jsii.get(self, "publicVirtualInterfaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublicVirtualInterfaceRef).__jsii_proxy_class__ = lambda : _IPublicVirtualInterfaceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.ITransitVirtualInterfaceRef"
)
class ITransitVirtualInterfaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitVirtualInterface.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitVirtualInterfaceRef")
    def transit_virtual_interface_ref(self) -> "TransitVirtualInterfaceReference":
        '''(experimental) A reference to a TransitVirtualInterface resource.

        :stability: experimental
        '''
        ...


class _ITransitVirtualInterfaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitVirtualInterface.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_directconnect.ITransitVirtualInterfaceRef"

    @builtins.property
    @jsii.member(jsii_name="transitVirtualInterfaceRef")
    def transit_virtual_interface_ref(self) -> "TransitVirtualInterfaceReference":
        '''(experimental) A reference to a TransitVirtualInterface resource.

        :stability: experimental
        '''
        return typing.cast("TransitVirtualInterfaceReference", jsii.get(self, "transitVirtualInterfaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitVirtualInterfaceRef).__jsii_proxy_class__ = lambda : _ITransitVirtualInterfaceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.LagReference",
    jsii_struct_bases=[],
    name_mapping={"lag_arn": "lagArn"},
)
class LagReference:
    def __init__(self, *, lag_arn: builtins.str) -> None:
        '''A reference to a Lag resource.

        :param lag_arn: The LagArn of the Lag resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_directconnect as interfaces_directconnect
            
            lag_reference = interfaces_directconnect.LagReference(
                lag_arn="lagArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3bd2fbb85a32e0d60c41201599e82cea45179c54b82c95d72bfb2343ee49e91)
            check_type(argname="argument lag_arn", value=lag_arn, expected_type=type_hints["lag_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lag_arn": lag_arn,
        }

    @builtins.property
    def lag_arn(self) -> builtins.str:
        '''The LagArn of the Lag resource.'''
        result = self._values.get("lag_arn")
        assert result is not None, "Required property 'lag_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LagReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.PrivateVirtualInterfaceReference",
    jsii_struct_bases=[],
    name_mapping={"virtual_interface_arn": "virtualInterfaceArn"},
)
class PrivateVirtualInterfaceReference:
    def __init__(self, *, virtual_interface_arn: builtins.str) -> None:
        '''A reference to a PrivateVirtualInterface resource.

        :param virtual_interface_arn: The VirtualInterfaceArn of the PrivateVirtualInterface resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_directconnect as interfaces_directconnect
            
            private_virtual_interface_reference = interfaces_directconnect.PrivateVirtualInterfaceReference(
                virtual_interface_arn="virtualInterfaceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be51fcf63a03cda0880ab055396fd4350c986ed29b67b2fe9ccbe13bd7eef635)
            check_type(argname="argument virtual_interface_arn", value=virtual_interface_arn, expected_type=type_hints["virtual_interface_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_interface_arn": virtual_interface_arn,
        }

    @builtins.property
    def virtual_interface_arn(self) -> builtins.str:
        '''The VirtualInterfaceArn of the PrivateVirtualInterface resource.'''
        result = self._values.get("virtual_interface_arn")
        assert result is not None, "Required property 'virtual_interface_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateVirtualInterfaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.PublicVirtualInterfaceReference",
    jsii_struct_bases=[],
    name_mapping={"virtual_interface_arn": "virtualInterfaceArn"},
)
class PublicVirtualInterfaceReference:
    def __init__(self, *, virtual_interface_arn: builtins.str) -> None:
        '''A reference to a PublicVirtualInterface resource.

        :param virtual_interface_arn: The VirtualInterfaceArn of the PublicVirtualInterface resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_directconnect as interfaces_directconnect
            
            public_virtual_interface_reference = interfaces_directconnect.PublicVirtualInterfaceReference(
                virtual_interface_arn="virtualInterfaceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__931652cc8f8bd991d36eef258ac37b8e6d4b98d35ddec1b4412f379d31da0806)
            check_type(argname="argument virtual_interface_arn", value=virtual_interface_arn, expected_type=type_hints["virtual_interface_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_interface_arn": virtual_interface_arn,
        }

    @builtins.property
    def virtual_interface_arn(self) -> builtins.str:
        '''The VirtualInterfaceArn of the PublicVirtualInterface resource.'''
        result = self._values.get("virtual_interface_arn")
        assert result is not None, "Required property 'virtual_interface_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicVirtualInterfaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_directconnect.TransitVirtualInterfaceReference",
    jsii_struct_bases=[],
    name_mapping={"virtual_interface_arn": "virtualInterfaceArn"},
)
class TransitVirtualInterfaceReference:
    def __init__(self, *, virtual_interface_arn: builtins.str) -> None:
        '''A reference to a TransitVirtualInterface resource.

        :param virtual_interface_arn: The VirtualInterfaceArn of the TransitVirtualInterface resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_directconnect as interfaces_directconnect
            
            transit_virtual_interface_reference = interfaces_directconnect.TransitVirtualInterfaceReference(
                virtual_interface_arn="virtualInterfaceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0705d8064ea639011f2ee10d0baa0493bf0fc5c5bc6553bf778c002e716eaaa9)
            check_type(argname="argument virtual_interface_arn", value=virtual_interface_arn, expected_type=type_hints["virtual_interface_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "virtual_interface_arn": virtual_interface_arn,
        }

    @builtins.property
    def virtual_interface_arn(self) -> builtins.str:
        '''The VirtualInterfaceArn of the TransitVirtualInterface resource.'''
        result = self._values.get("virtual_interface_arn")
        assert result is not None, "Required property 'virtual_interface_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitVirtualInterfaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConnectionReference",
    "DirectConnectGatewayAssociationReference",
    "DirectConnectGatewayReference",
    "IConnectionRef",
    "IDirectConnectGatewayAssociationRef",
    "IDirectConnectGatewayRef",
    "ILagRef",
    "IPrivateVirtualInterfaceRef",
    "IPublicVirtualInterfaceRef",
    "ITransitVirtualInterfaceRef",
    "LagReference",
    "PrivateVirtualInterfaceReference",
    "PublicVirtualInterfaceReference",
    "TransitVirtualInterfaceReference",
]

publication.publish()

def _typecheckingstub__ecc1baa45366df795416273ab50a10d994aba4b4bd3eaea1aad1724372ad7c0d(
    *,
    connection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f3e59a2b0118d3f066d12696601397ea35c407bdf689d829eaad636f9e6defc(
    *,
    association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c20f5c45ba60148433cd3c2e5af50999fe635c2e2e52eb9663f1741bd2a2b423(
    *,
    direct_connect_gateway_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3bd2fbb85a32e0d60c41201599e82cea45179c54b82c95d72bfb2343ee49e91(
    *,
    lag_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be51fcf63a03cda0880ab055396fd4350c986ed29b67b2fe9ccbe13bd7eef635(
    *,
    virtual_interface_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__931652cc8f8bd991d36eef258ac37b8e6d4b98d35ddec1b4412f379d31da0806(
    *,
    virtual_interface_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0705d8064ea639011f2ee10d0baa0493bf0fc5c5bc6553bf778c002e716eaaa9(
    *,
    virtual_interface_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectionRef, IDirectConnectGatewayAssociationRef, IDirectConnectGatewayRef, ILagRef, IPrivateVirtualInterfaceRef, IPublicVirtualInterfaceRef, ITransitVirtualInterfaceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
