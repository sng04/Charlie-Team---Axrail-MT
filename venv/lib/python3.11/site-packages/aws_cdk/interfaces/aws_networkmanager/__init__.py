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
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ConnectAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"attachment_id": "attachmentId"},
)
class ConnectAttachmentReference:
    def __init__(self, *, attachment_id: builtins.str) -> None:
        '''A reference to a ConnectAttachment resource.

        :param attachment_id: The AttachmentId of the ConnectAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            connect_attachment_reference = interfaces_networkmanager.ConnectAttachmentReference(
                attachment_id="attachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f015d9931081e9ffd7676e999aae6fc39f581562fb6e8347743350a120d4066)
            check_type(argname="argument attachment_id", value=attachment_id, expected_type=type_hints["attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attachment_id": attachment_id,
        }

    @builtins.property
    def attachment_id(self) -> builtins.str:
        '''The AttachmentId of the ConnectAttachment resource.'''
        result = self._values.get("attachment_id")
        assert result is not None, "Required property 'attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ConnectPeerReference",
    jsii_struct_bases=[],
    name_mapping={"connect_peer_id": "connectPeerId"},
)
class ConnectPeerReference:
    def __init__(self, *, connect_peer_id: builtins.str) -> None:
        '''A reference to a ConnectPeer resource.

        :param connect_peer_id: The ConnectPeerId of the ConnectPeer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            connect_peer_reference = interfaces_networkmanager.ConnectPeerReference(
                connect_peer_id="connectPeerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66c18e1d85bf0c649a8ea0d151647ff638d4397ed0718be580410310894d2d7a)
            check_type(argname="argument connect_peer_id", value=connect_peer_id, expected_type=type_hints["connect_peer_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connect_peer_id": connect_peer_id,
        }

    @builtins.property
    def connect_peer_id(self) -> builtins.str:
        '''The ConnectPeerId of the ConnectPeer resource.'''
        result = self._values.get("connect_peer_id")
        assert result is not None, "Required property 'connect_peer_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectPeerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.CoreNetworkPrefixListAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "core_network_id": "coreNetworkId",
        "prefix_list_arn": "prefixListArn",
    },
)
class CoreNetworkPrefixListAssociationReference:
    def __init__(
        self,
        *,
        core_network_id: builtins.str,
        prefix_list_arn: builtins.str,
    ) -> None:
        '''A reference to a CoreNetworkPrefixListAssociation resource.

        :param core_network_id: The CoreNetworkId of the CoreNetworkPrefixListAssociation resource.
        :param prefix_list_arn: The PrefixListArn of the CoreNetworkPrefixListAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            core_network_prefix_list_association_reference = interfaces_networkmanager.CoreNetworkPrefixListAssociationReference(
                core_network_id="coreNetworkId",
                prefix_list_arn="prefixListArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c8d4f555ff411e787c4b2f46cde88abc78ed7ee372570671fa5c40432bdc805)
            check_type(argname="argument core_network_id", value=core_network_id, expected_type=type_hints["core_network_id"])
            check_type(argname="argument prefix_list_arn", value=prefix_list_arn, expected_type=type_hints["prefix_list_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "core_network_id": core_network_id,
            "prefix_list_arn": prefix_list_arn,
        }

    @builtins.property
    def core_network_id(self) -> builtins.str:
        '''The CoreNetworkId of the CoreNetworkPrefixListAssociation resource.'''
        result = self._values.get("core_network_id")
        assert result is not None, "Required property 'core_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def prefix_list_arn(self) -> builtins.str:
        '''The PrefixListArn of the CoreNetworkPrefixListAssociation resource.'''
        result = self._values.get("prefix_list_arn")
        assert result is not None, "Required property 'prefix_list_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CoreNetworkPrefixListAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.CoreNetworkReference",
    jsii_struct_bases=[],
    name_mapping={
        "core_network_arn": "coreNetworkArn",
        "core_network_id": "coreNetworkId",
    },
)
class CoreNetworkReference:
    def __init__(
        self,
        *,
        core_network_arn: builtins.str,
        core_network_id: builtins.str,
    ) -> None:
        '''A reference to a CoreNetwork resource.

        :param core_network_arn: The ARN of the CoreNetwork resource.
        :param core_network_id: The CoreNetworkId of the CoreNetwork resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            core_network_reference = interfaces_networkmanager.CoreNetworkReference(
                core_network_arn="coreNetworkArn",
                core_network_id="coreNetworkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f49c1c1e6910e95d47508abb869f1875c7676b6e07e13830ee881f85fdfe9918)
            check_type(argname="argument core_network_arn", value=core_network_arn, expected_type=type_hints["core_network_arn"])
            check_type(argname="argument core_network_id", value=core_network_id, expected_type=type_hints["core_network_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "core_network_arn": core_network_arn,
            "core_network_id": core_network_id,
        }

    @builtins.property
    def core_network_arn(self) -> builtins.str:
        '''The ARN of the CoreNetwork resource.'''
        result = self._values.get("core_network_arn")
        assert result is not None, "Required property 'core_network_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def core_network_id(self) -> builtins.str:
        '''The CoreNetworkId of the CoreNetwork resource.'''
        result = self._values.get("core_network_id")
        assert result is not None, "Required property 'core_network_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CoreNetworkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.CustomerGatewayAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "customer_gateway_arn": "customerGatewayArn",
        "global_network_id": "globalNetworkId",
    },
)
class CustomerGatewayAssociationReference:
    def __init__(
        self,
        *,
        customer_gateway_arn: builtins.str,
        global_network_id: builtins.str,
    ) -> None:
        '''A reference to a CustomerGatewayAssociation resource.

        :param customer_gateway_arn: The CustomerGatewayArn of the CustomerGatewayAssociation resource.
        :param global_network_id: The GlobalNetworkId of the CustomerGatewayAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            customer_gateway_association_reference = interfaces_networkmanager.CustomerGatewayAssociationReference(
                customer_gateway_arn="customerGatewayArn",
                global_network_id="globalNetworkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__911ffbd15ccc1a7d86ead56007d8eb9c2528825b5af2ef0809fd40d4ec1ce74a)
            check_type(argname="argument customer_gateway_arn", value=customer_gateway_arn, expected_type=type_hints["customer_gateway_arn"])
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "customer_gateway_arn": customer_gateway_arn,
            "global_network_id": global_network_id,
        }

    @builtins.property
    def customer_gateway_arn(self) -> builtins.str:
        '''The CustomerGatewayArn of the CustomerGatewayAssociation resource.'''
        result = self._values.get("customer_gateway_arn")
        assert result is not None, "Required property 'customer_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The GlobalNetworkId of the CustomerGatewayAssociation resource.'''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomerGatewayAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.DeviceReference",
    jsii_struct_bases=[],
    name_mapping={
        "device_arn": "deviceArn",
        "device_id": "deviceId",
        "global_network_id": "globalNetworkId",
    },
)
class DeviceReference:
    def __init__(
        self,
        *,
        device_arn: builtins.str,
        device_id: builtins.str,
        global_network_id: builtins.str,
    ) -> None:
        '''A reference to a Device resource.

        :param device_arn: The ARN of the Device resource.
        :param device_id: The DeviceId of the Device resource.
        :param global_network_id: The GlobalNetworkId of the Device resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            device_reference = interfaces_networkmanager.DeviceReference(
                device_arn="deviceArn",
                device_id="deviceId",
                global_network_id="globalNetworkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4f1b21f8b59b3382965e6dbbc349341509e709e290d9e27e109f15555d74c0d)
            check_type(argname="argument device_arn", value=device_arn, expected_type=type_hints["device_arn"])
            check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_arn": device_arn,
            "device_id": device_id,
            "global_network_id": global_network_id,
        }

    @builtins.property
    def device_arn(self) -> builtins.str:
        '''The ARN of the Device resource.'''
        result = self._values.get("device_arn")
        assert result is not None, "Required property 'device_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def device_id(self) -> builtins.str:
        '''The DeviceId of the Device resource.'''
        result = self._values.get("device_id")
        assert result is not None, "Required property 'device_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The GlobalNetworkId of the Device resource.'''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeviceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.DirectConnectGatewayAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"attachment_id": "attachmentId"},
)
class DirectConnectGatewayAttachmentReference:
    def __init__(self, *, attachment_id: builtins.str) -> None:
        '''A reference to a DirectConnectGatewayAttachment resource.

        :param attachment_id: The AttachmentId of the DirectConnectGatewayAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            direct_connect_gateway_attachment_reference = interfaces_networkmanager.DirectConnectGatewayAttachmentReference(
                attachment_id="attachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__422b500ab1fc288c3781046eaef3774ee79854d533a125b94b7c7dc4dac4be14)
            check_type(argname="argument attachment_id", value=attachment_id, expected_type=type_hints["attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attachment_id": attachment_id,
        }

    @builtins.property
    def attachment_id(self) -> builtins.str:
        '''The AttachmentId of the DirectConnectGatewayAttachment resource.'''
        result = self._values.get("attachment_id")
        assert result is not None, "Required property 'attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DirectConnectGatewayAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.GlobalNetworkReference",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_arn": "globalNetworkArn",
        "global_network_id": "globalNetworkId",
    },
)
class GlobalNetworkReference:
    def __init__(
        self,
        *,
        global_network_arn: builtins.str,
        global_network_id: builtins.str,
    ) -> None:
        '''A reference to a GlobalNetwork resource.

        :param global_network_arn: The ARN of the GlobalNetwork resource.
        :param global_network_id: The Id of the GlobalNetwork resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            global_network_reference = interfaces_networkmanager.GlobalNetworkReference(
                global_network_arn="globalNetworkArn",
                global_network_id="globalNetworkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4980d7494d3e20076cef7d01476600b6690bde6ad66a0f9ccc3a278dc3ddefb)
            check_type(argname="argument global_network_arn", value=global_network_arn, expected_type=type_hints["global_network_arn"])
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_network_arn": global_network_arn,
            "global_network_id": global_network_id,
        }

    @builtins.property
    def global_network_arn(self) -> builtins.str:
        '''The ARN of the GlobalNetwork resource.'''
        result = self._values.get("global_network_arn")
        assert result is not None, "Required property 'global_network_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The Id of the GlobalNetwork resource.'''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlobalNetworkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.IConnectAttachmentRef"
)
class IConnectAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectAttachmentRef")
    def connect_attachment_ref(self) -> "ConnectAttachmentReference":
        '''(experimental) A reference to a ConnectAttachment resource.

        :stability: experimental
        '''
        ...


class _IConnectAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.IConnectAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="connectAttachmentRef")
    def connect_attachment_ref(self) -> "ConnectAttachmentReference":
        '''(experimental) A reference to a ConnectAttachment resource.

        :stability: experimental
        '''
        return typing.cast("ConnectAttachmentReference", jsii.get(self, "connectAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectAttachmentRef).__jsii_proxy_class__ = lambda : _IConnectAttachmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.IConnectPeerRef")
class IConnectPeerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectPeer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectPeerRef")
    def connect_peer_ref(self) -> "ConnectPeerReference":
        '''(experimental) A reference to a ConnectPeer resource.

        :stability: experimental
        '''
        ...


class _IConnectPeerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectPeer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.IConnectPeerRef"

    @builtins.property
    @jsii.member(jsii_name="connectPeerRef")
    def connect_peer_ref(self) -> "ConnectPeerReference":
        '''(experimental) A reference to a ConnectPeer resource.

        :stability: experimental
        '''
        return typing.cast("ConnectPeerReference", jsii.get(self, "connectPeerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectPeerRef).__jsii_proxy_class__ = lambda : _IConnectPeerRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ICoreNetworkPrefixListAssociationRef"
)
class ICoreNetworkPrefixListAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CoreNetworkPrefixListAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="coreNetworkPrefixListAssociationRef")
    def core_network_prefix_list_association_ref(
        self,
    ) -> "CoreNetworkPrefixListAssociationReference":
        '''(experimental) A reference to a CoreNetworkPrefixListAssociation resource.

        :stability: experimental
        '''
        ...


class _ICoreNetworkPrefixListAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CoreNetworkPrefixListAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.ICoreNetworkPrefixListAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="coreNetworkPrefixListAssociationRef")
    def core_network_prefix_list_association_ref(
        self,
    ) -> "CoreNetworkPrefixListAssociationReference":
        '''(experimental) A reference to a CoreNetworkPrefixListAssociation resource.

        :stability: experimental
        '''
        return typing.cast("CoreNetworkPrefixListAssociationReference", jsii.get(self, "coreNetworkPrefixListAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICoreNetworkPrefixListAssociationRef).__jsii_proxy_class__ = lambda : _ICoreNetworkPrefixListAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ICoreNetworkRef")
class ICoreNetworkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CoreNetwork.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="coreNetworkRef")
    def core_network_ref(self) -> "CoreNetworkReference":
        '''(experimental) A reference to a CoreNetwork resource.

        :stability: experimental
        '''
        ...


class _ICoreNetworkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CoreNetwork.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.ICoreNetworkRef"

    @builtins.property
    @jsii.member(jsii_name="coreNetworkRef")
    def core_network_ref(self) -> "CoreNetworkReference":
        '''(experimental) A reference to a CoreNetwork resource.

        :stability: experimental
        '''
        return typing.cast("CoreNetworkReference", jsii.get(self, "coreNetworkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICoreNetworkRef).__jsii_proxy_class__ = lambda : _ICoreNetworkRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ICustomerGatewayAssociationRef"
)
class ICustomerGatewayAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomerGatewayAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customerGatewayAssociationRef")
    def customer_gateway_association_ref(self) -> "CustomerGatewayAssociationReference":
        '''(experimental) A reference to a CustomerGatewayAssociation resource.

        :stability: experimental
        '''
        ...


class _ICustomerGatewayAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomerGatewayAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.ICustomerGatewayAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="customerGatewayAssociationRef")
    def customer_gateway_association_ref(self) -> "CustomerGatewayAssociationReference":
        '''(experimental) A reference to a CustomerGatewayAssociation resource.

        :stability: experimental
        '''
        return typing.cast("CustomerGatewayAssociationReference", jsii.get(self, "customerGatewayAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomerGatewayAssociationRef).__jsii_proxy_class__ = lambda : _ICustomerGatewayAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.IDeviceRef")
class IDeviceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Device.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deviceRef")
    def device_ref(self) -> "DeviceReference":
        '''(experimental) A reference to a Device resource.

        :stability: experimental
        '''
        ...


class _IDeviceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Device.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.IDeviceRef"

    @builtins.property
    @jsii.member(jsii_name="deviceRef")
    def device_ref(self) -> "DeviceReference":
        '''(experimental) A reference to a Device resource.

        :stability: experimental
        '''
        return typing.cast("DeviceReference", jsii.get(self, "deviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeviceRef).__jsii_proxy_class__ = lambda : _IDeviceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.IDirectConnectGatewayAttachmentRef"
)
class IDirectConnectGatewayAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DirectConnectGatewayAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayAttachmentRef")
    def direct_connect_gateway_attachment_ref(
        self,
    ) -> "DirectConnectGatewayAttachmentReference":
        '''(experimental) A reference to a DirectConnectGatewayAttachment resource.

        :stability: experimental
        '''
        ...


class _IDirectConnectGatewayAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DirectConnectGatewayAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.IDirectConnectGatewayAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayAttachmentRef")
    def direct_connect_gateway_attachment_ref(
        self,
    ) -> "DirectConnectGatewayAttachmentReference":
        '''(experimental) A reference to a DirectConnectGatewayAttachment resource.

        :stability: experimental
        '''
        return typing.cast("DirectConnectGatewayAttachmentReference", jsii.get(self, "directConnectGatewayAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDirectConnectGatewayAttachmentRef).__jsii_proxy_class__ = lambda : _IDirectConnectGatewayAttachmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.IGlobalNetworkRef"
)
class IGlobalNetworkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalNetwork.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="globalNetworkRef")
    def global_network_ref(self) -> "GlobalNetworkReference":
        '''(experimental) A reference to a GlobalNetwork resource.

        :stability: experimental
        '''
        ...


class _IGlobalNetworkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalNetwork.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.IGlobalNetworkRef"

    @builtins.property
    @jsii.member(jsii_name="globalNetworkRef")
    def global_network_ref(self) -> "GlobalNetworkReference":
        '''(experimental) A reference to a GlobalNetwork resource.

        :stability: experimental
        '''
        return typing.cast("GlobalNetworkReference", jsii.get(self, "globalNetworkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGlobalNetworkRef).__jsii_proxy_class__ = lambda : _IGlobalNetworkRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ILinkAssociationRef"
)
class ILinkAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LinkAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="linkAssociationRef")
    def link_association_ref(self) -> "LinkAssociationReference":
        '''(experimental) A reference to a LinkAssociation resource.

        :stability: experimental
        '''
        ...


class _ILinkAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LinkAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.ILinkAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="linkAssociationRef")
    def link_association_ref(self) -> "LinkAssociationReference":
        '''(experimental) A reference to a LinkAssociation resource.

        :stability: experimental
        '''
        return typing.cast("LinkAssociationReference", jsii.get(self, "linkAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILinkAssociationRef).__jsii_proxy_class__ = lambda : _ILinkAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ILinkRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.ILinkRef"

    @builtins.property
    @jsii.member(jsii_name="linkRef")
    def link_ref(self) -> "LinkReference":
        '''(experimental) A reference to a Link resource.

        :stability: experimental
        '''
        return typing.cast("LinkReference", jsii.get(self, "linkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILinkRef).__jsii_proxy_class__ = lambda : _ILinkRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ISiteRef")
class ISiteRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Site.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="siteRef")
    def site_ref(self) -> "SiteReference":
        '''(experimental) A reference to a Site resource.

        :stability: experimental
        '''
        ...


class _ISiteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Site.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.ISiteRef"

    @builtins.property
    @jsii.member(jsii_name="siteRef")
    def site_ref(self) -> "SiteReference":
        '''(experimental) A reference to a Site resource.

        :stability: experimental
        '''
        return typing.cast("SiteReference", jsii.get(self, "siteRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISiteRef).__jsii_proxy_class__ = lambda : _ISiteRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ISiteToSiteVpnAttachmentRef"
)
class ISiteToSiteVpnAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SiteToSiteVpnAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="siteToSiteVpnAttachmentRef")
    def site_to_site_vpn_attachment_ref(self) -> "SiteToSiteVpnAttachmentReference":
        '''(experimental) A reference to a SiteToSiteVpnAttachment resource.

        :stability: experimental
        '''
        ...


class _ISiteToSiteVpnAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SiteToSiteVpnAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.ISiteToSiteVpnAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="siteToSiteVpnAttachmentRef")
    def site_to_site_vpn_attachment_ref(self) -> "SiteToSiteVpnAttachmentReference":
        '''(experimental) A reference to a SiteToSiteVpnAttachment resource.

        :stability: experimental
        '''
        return typing.cast("SiteToSiteVpnAttachmentReference", jsii.get(self, "siteToSiteVpnAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISiteToSiteVpnAttachmentRef).__jsii_proxy_class__ = lambda : _ISiteToSiteVpnAttachmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ITransitGatewayPeeringRef"
)
class ITransitGatewayPeeringRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayPeering.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayPeeringRef")
    def transit_gateway_peering_ref(self) -> "TransitGatewayPeeringReference":
        '''(experimental) A reference to a TransitGatewayPeering resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayPeeringRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayPeering.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.ITransitGatewayPeeringRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayPeeringRef")
    def transit_gateway_peering_ref(self) -> "TransitGatewayPeeringReference":
        '''(experimental) A reference to a TransitGatewayPeering resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayPeeringReference", jsii.get(self, "transitGatewayPeeringRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayPeeringRef).__jsii_proxy_class__ = lambda : _ITransitGatewayPeeringRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ITransitGatewayRegistrationRef"
)
class ITransitGatewayRegistrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRegistration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRegistrationRef")
    def transit_gateway_registration_ref(self) -> "TransitGatewayRegistrationReference":
        '''(experimental) A reference to a TransitGatewayRegistration resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayRegistrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRegistration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.ITransitGatewayRegistrationRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRegistrationRef")
    def transit_gateway_registration_ref(self) -> "TransitGatewayRegistrationReference":
        '''(experimental) A reference to a TransitGatewayRegistration resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayRegistrationReference", jsii.get(self, "transitGatewayRegistrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayRegistrationRef).__jsii_proxy_class__ = lambda : _ITransitGatewayRegistrationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.ITransitGatewayRouteTableAttachmentRef"
)
class ITransitGatewayRouteTableAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRouteTableAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTableAttachmentRef")
    def transit_gateway_route_table_attachment_ref(
        self,
    ) -> "TransitGatewayRouteTableAttachmentReference":
        '''(experimental) A reference to a TransitGatewayRouteTableAttachment resource.

        :stability: experimental
        '''
        ...


class _ITransitGatewayRouteTableAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransitGatewayRouteTableAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.ITransitGatewayRouteTableAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="transitGatewayRouteTableAttachmentRef")
    def transit_gateway_route_table_attachment_ref(
        self,
    ) -> "TransitGatewayRouteTableAttachmentReference":
        '''(experimental) A reference to a TransitGatewayRouteTableAttachment resource.

        :stability: experimental
        '''
        return typing.cast("TransitGatewayRouteTableAttachmentReference", jsii.get(self, "transitGatewayRouteTableAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransitGatewayRouteTableAttachmentRef).__jsii_proxy_class__ = lambda : _ITransitGatewayRouteTableAttachmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.IVpcAttachmentRef"
)
class IVpcAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VpcAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcAttachmentRef")
    def vpc_attachment_ref(self) -> "VpcAttachmentReference":
        '''(experimental) A reference to a VpcAttachment resource.

        :stability: experimental
        '''
        ...


class _IVpcAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VpcAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_networkmanager.IVpcAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="vpcAttachmentRef")
    def vpc_attachment_ref(self) -> "VpcAttachmentReference":
        '''(experimental) A reference to a VpcAttachment resource.

        :stability: experimental
        '''
        return typing.cast("VpcAttachmentReference", jsii.get(self, "vpcAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVpcAttachmentRef).__jsii_proxy_class__ = lambda : _IVpcAttachmentRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.LinkAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "device_id": "deviceId",
        "global_network_id": "globalNetworkId",
        "link_id": "linkId",
    },
)
class LinkAssociationReference:
    def __init__(
        self,
        *,
        device_id: builtins.str,
        global_network_id: builtins.str,
        link_id: builtins.str,
    ) -> None:
        '''A reference to a LinkAssociation resource.

        :param device_id: The DeviceId of the LinkAssociation resource.
        :param global_network_id: The GlobalNetworkId of the LinkAssociation resource.
        :param link_id: The LinkId of the LinkAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            link_association_reference = interfaces_networkmanager.LinkAssociationReference(
                device_id="deviceId",
                global_network_id="globalNetworkId",
                link_id="linkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed0423a6841efd68247257479becb17914bd62a9b6e886a6bce03422d4d7e586)
            check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument link_id", value=link_id, expected_type=type_hints["link_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_id": device_id,
            "global_network_id": global_network_id,
            "link_id": link_id,
        }

    @builtins.property
    def device_id(self) -> builtins.str:
        '''The DeviceId of the LinkAssociation resource.'''
        result = self._values.get("device_id")
        assert result is not None, "Required property 'device_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The GlobalNetworkId of the LinkAssociation resource.'''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_id(self) -> builtins.str:
        '''The LinkId of the LinkAssociation resource.'''
        result = self._values.get("link_id")
        assert result is not None, "Required property 'link_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinkAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.LinkReference",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "link_arn": "linkArn",
        "link_id": "linkId",
    },
)
class LinkReference:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        link_arn: builtins.str,
        link_id: builtins.str,
    ) -> None:
        '''A reference to a Link resource.

        :param global_network_id: The GlobalNetworkId of the Link resource.
        :param link_arn: The ARN of the Link resource.
        :param link_id: The LinkId of the Link resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            link_reference = interfaces_networkmanager.LinkReference(
                global_network_id="globalNetworkId",
                link_arn="linkArn",
                link_id="linkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbda4dabf7d27ec945f106610f4f4eeae789320023da5dae3b919e0a0a41c39d)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument link_arn", value=link_arn, expected_type=type_hints["link_arn"])
            check_type(argname="argument link_id", value=link_id, expected_type=type_hints["link_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_network_id": global_network_id,
            "link_arn": link_arn,
            "link_id": link_id,
        }

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The GlobalNetworkId of the Link resource.'''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_arn(self) -> builtins.str:
        '''The ARN of the Link resource.'''
        result = self._values.get("link_arn")
        assert result is not None, "Required property 'link_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_id(self) -> builtins.str:
        '''The LinkId of the Link resource.'''
        result = self._values.get("link_id")
        assert result is not None, "Required property 'link_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.SiteReference",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "site_arn": "siteArn",
        "site_id": "siteId",
    },
)
class SiteReference:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        site_arn: builtins.str,
        site_id: builtins.str,
    ) -> None:
        '''A reference to a Site resource.

        :param global_network_id: The GlobalNetworkId of the Site resource.
        :param site_arn: The ARN of the Site resource.
        :param site_id: The SiteId of the Site resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            site_reference = interfaces_networkmanager.SiteReference(
                global_network_id="globalNetworkId",
                site_arn="siteArn",
                site_id="siteId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b3321f867c8bcf94d208eb33401f4531f16b75e80d3507e4bb854645c69e4c5)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument site_arn", value=site_arn, expected_type=type_hints["site_arn"])
            check_type(argname="argument site_id", value=site_id, expected_type=type_hints["site_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_network_id": global_network_id,
            "site_arn": site_arn,
            "site_id": site_id,
        }

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The GlobalNetworkId of the Site resource.'''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_arn(self) -> builtins.str:
        '''The ARN of the Site resource.'''
        result = self._values.get("site_arn")
        assert result is not None, "Required property 'site_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def site_id(self) -> builtins.str:
        '''The SiteId of the Site resource.'''
        result = self._values.get("site_id")
        assert result is not None, "Required property 'site_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.SiteToSiteVpnAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"attachment_id": "attachmentId"},
)
class SiteToSiteVpnAttachmentReference:
    def __init__(self, *, attachment_id: builtins.str) -> None:
        '''A reference to a SiteToSiteVpnAttachment resource.

        :param attachment_id: The AttachmentId of the SiteToSiteVpnAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            site_to_site_vpn_attachment_reference = interfaces_networkmanager.SiteToSiteVpnAttachmentReference(
                attachment_id="attachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e76be5f29a222b5891d4e06d0afd1fcd7f48acc2e6da1cdf3e87bd85deafbb44)
            check_type(argname="argument attachment_id", value=attachment_id, expected_type=type_hints["attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attachment_id": attachment_id,
        }

    @builtins.property
    def attachment_id(self) -> builtins.str:
        '''The AttachmentId of the SiteToSiteVpnAttachment resource.'''
        result = self._values.get("attachment_id")
        assert result is not None, "Required property 'attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SiteToSiteVpnAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.TransitGatewayPeeringReference",
    jsii_struct_bases=[],
    name_mapping={"peering_id": "peeringId"},
)
class TransitGatewayPeeringReference:
    def __init__(self, *, peering_id: builtins.str) -> None:
        '''A reference to a TransitGatewayPeering resource.

        :param peering_id: The PeeringId of the TransitGatewayPeering resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            transit_gateway_peering_reference = interfaces_networkmanager.TransitGatewayPeeringReference(
                peering_id="peeringId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2a5774a214ff0fd3d589935d7f77652018d176ecedffdd6131df23ea828c21a)
            check_type(argname="argument peering_id", value=peering_id, expected_type=type_hints["peering_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "peering_id": peering_id,
        }

    @builtins.property
    def peering_id(self) -> builtins.str:
        '''The PeeringId of the TransitGatewayPeering resource.'''
        result = self._values.get("peering_id")
        assert result is not None, "Required property 'peering_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayPeeringReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.TransitGatewayRegistrationReference",
    jsii_struct_bases=[],
    name_mapping={
        "global_network_id": "globalNetworkId",
        "transit_gateway_arn": "transitGatewayArn",
    },
)
class TransitGatewayRegistrationReference:
    def __init__(
        self,
        *,
        global_network_id: builtins.str,
        transit_gateway_arn: builtins.str,
    ) -> None:
        '''A reference to a TransitGatewayRegistration resource.

        :param global_network_id: The GlobalNetworkId of the TransitGatewayRegistration resource.
        :param transit_gateway_arn: The TransitGatewayArn of the TransitGatewayRegistration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            transit_gateway_registration_reference = interfaces_networkmanager.TransitGatewayRegistrationReference(
                global_network_id="globalNetworkId",
                transit_gateway_arn="transitGatewayArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c85647afdbc59544782dfb58818db0134f3e2592d7f70a0cb2cf4984f8bf875)
            check_type(argname="argument global_network_id", value=global_network_id, expected_type=type_hints["global_network_id"])
            check_type(argname="argument transit_gateway_arn", value=transit_gateway_arn, expected_type=type_hints["transit_gateway_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_network_id": global_network_id,
            "transit_gateway_arn": transit_gateway_arn,
        }

    @builtins.property
    def global_network_id(self) -> builtins.str:
        '''The GlobalNetworkId of the TransitGatewayRegistration resource.'''
        result = self._values.get("global_network_id")
        assert result is not None, "Required property 'global_network_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def transit_gateway_arn(self) -> builtins.str:
        '''The TransitGatewayArn of the TransitGatewayRegistration resource.'''
        result = self._values.get("transit_gateway_arn")
        assert result is not None, "Required property 'transit_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayRegistrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.TransitGatewayRouteTableAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"attachment_id": "attachmentId"},
)
class TransitGatewayRouteTableAttachmentReference:
    def __init__(self, *, attachment_id: builtins.str) -> None:
        '''A reference to a TransitGatewayRouteTableAttachment resource.

        :param attachment_id: The AttachmentId of the TransitGatewayRouteTableAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            transit_gateway_route_table_attachment_reference = interfaces_networkmanager.TransitGatewayRouteTableAttachmentReference(
                attachment_id="attachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aa06a6d891e2a06841f7f1cef9404483bf50dcd36d6888fa4c1cd663b8b2e12)
            check_type(argname="argument attachment_id", value=attachment_id, expected_type=type_hints["attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attachment_id": attachment_id,
        }

    @builtins.property
    def attachment_id(self) -> builtins.str:
        '''The AttachmentId of the TransitGatewayRouteTableAttachment resource.'''
        result = self._values.get("attachment_id")
        assert result is not None, "Required property 'attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransitGatewayRouteTableAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_networkmanager.VpcAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"attachment_id": "attachmentId"},
)
class VpcAttachmentReference:
    def __init__(self, *, attachment_id: builtins.str) -> None:
        '''A reference to a VpcAttachment resource.

        :param attachment_id: The AttachmentId of the VpcAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_networkmanager as interfaces_networkmanager
            
            vpc_attachment_reference = interfaces_networkmanager.VpcAttachmentReference(
                attachment_id="attachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e0ff976fac1bf48401e97de79ca9adb82683b277d96c4c2b04e540511aabc82)
            check_type(argname="argument attachment_id", value=attachment_id, expected_type=type_hints["attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "attachment_id": attachment_id,
        }

    @builtins.property
    def attachment_id(self) -> builtins.str:
        '''The AttachmentId of the VpcAttachment resource.'''
        result = self._values.get("attachment_id")
        assert result is not None, "Required property 'attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConnectAttachmentReference",
    "ConnectPeerReference",
    "CoreNetworkPrefixListAssociationReference",
    "CoreNetworkReference",
    "CustomerGatewayAssociationReference",
    "DeviceReference",
    "DirectConnectGatewayAttachmentReference",
    "GlobalNetworkReference",
    "IConnectAttachmentRef",
    "IConnectPeerRef",
    "ICoreNetworkPrefixListAssociationRef",
    "ICoreNetworkRef",
    "ICustomerGatewayAssociationRef",
    "IDeviceRef",
    "IDirectConnectGatewayAttachmentRef",
    "IGlobalNetworkRef",
    "ILinkAssociationRef",
    "ILinkRef",
    "ISiteRef",
    "ISiteToSiteVpnAttachmentRef",
    "ITransitGatewayPeeringRef",
    "ITransitGatewayRegistrationRef",
    "ITransitGatewayRouteTableAttachmentRef",
    "IVpcAttachmentRef",
    "LinkAssociationReference",
    "LinkReference",
    "SiteReference",
    "SiteToSiteVpnAttachmentReference",
    "TransitGatewayPeeringReference",
    "TransitGatewayRegistrationReference",
    "TransitGatewayRouteTableAttachmentReference",
    "VpcAttachmentReference",
]

publication.publish()

def _typecheckingstub__7f015d9931081e9ffd7676e999aae6fc39f581562fb6e8347743350a120d4066(
    *,
    attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66c18e1d85bf0c649a8ea0d151647ff638d4397ed0718be580410310894d2d7a(
    *,
    connect_peer_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c8d4f555ff411e787c4b2f46cde88abc78ed7ee372570671fa5c40432bdc805(
    *,
    core_network_id: builtins.str,
    prefix_list_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f49c1c1e6910e95d47508abb869f1875c7676b6e07e13830ee881f85fdfe9918(
    *,
    core_network_arn: builtins.str,
    core_network_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__911ffbd15ccc1a7d86ead56007d8eb9c2528825b5af2ef0809fd40d4ec1ce74a(
    *,
    customer_gateway_arn: builtins.str,
    global_network_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f1b21f8b59b3382965e6dbbc349341509e709e290d9e27e109f15555d74c0d(
    *,
    device_arn: builtins.str,
    device_id: builtins.str,
    global_network_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__422b500ab1fc288c3781046eaef3774ee79854d533a125b94b7c7dc4dac4be14(
    *,
    attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4980d7494d3e20076cef7d01476600b6690bde6ad66a0f9ccc3a278dc3ddefb(
    *,
    global_network_arn: builtins.str,
    global_network_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed0423a6841efd68247257479becb17914bd62a9b6e886a6bce03422d4d7e586(
    *,
    device_id: builtins.str,
    global_network_id: builtins.str,
    link_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbda4dabf7d27ec945f106610f4f4eeae789320023da5dae3b919e0a0a41c39d(
    *,
    global_network_id: builtins.str,
    link_arn: builtins.str,
    link_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b3321f867c8bcf94d208eb33401f4531f16b75e80d3507e4bb854645c69e4c5(
    *,
    global_network_id: builtins.str,
    site_arn: builtins.str,
    site_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e76be5f29a222b5891d4e06d0afd1fcd7f48acc2e6da1cdf3e87bd85deafbb44(
    *,
    attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2a5774a214ff0fd3d589935d7f77652018d176ecedffdd6131df23ea828c21a(
    *,
    peering_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c85647afdbc59544782dfb58818db0134f3e2592d7f70a0cb2cf4984f8bf875(
    *,
    global_network_id: builtins.str,
    transit_gateway_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aa06a6d891e2a06841f7f1cef9404483bf50dcd36d6888fa4c1cd663b8b2e12(
    *,
    attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e0ff976fac1bf48401e97de79ca9adb82683b277d96c4c2b04e540511aabc82(
    *,
    attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectAttachmentRef, IConnectPeerRef, ICoreNetworkPrefixListAssociationRef, ICoreNetworkRef, ICustomerGatewayAssociationRef, IDeviceRef, IDirectConnectGatewayAttachmentRef, IGlobalNetworkRef, ILinkAssociationRef, ILinkRef, ISiteRef, ISiteToSiteVpnAttachmentRef, ITransitGatewayPeeringRef, ITransitGatewayRegistrationRef, ITransitGatewayRouteTableAttachmentRef, IVpcAttachmentRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
