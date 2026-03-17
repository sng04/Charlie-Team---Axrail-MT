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
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.DestinationReference",
    jsii_struct_bases=[],
    name_mapping={
        "destination_arn": "destinationArn",
        "destination_name": "destinationName",
    },
)
class DestinationReference:
    def __init__(
        self,
        *,
        destination_arn: builtins.str,
        destination_name: builtins.str,
    ) -> None:
        '''A reference to a Destination resource.

        :param destination_arn: The ARN of the Destination resource.
        :param destination_name: The Name of the Destination resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            destination_reference = interfaces_iotwireless.DestinationReference(
                destination_arn="destinationArn",
                destination_name="destinationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01b22cebb6223a17a7839beb314e23234baaee086c51efa6fb71a1476d74032f)
            check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            check_type(argname="argument destination_name", value=destination_name, expected_type=type_hints["destination_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_arn": destination_arn,
            "destination_name": destination_name,
        }

    @builtins.property
    def destination_arn(self) -> builtins.str:
        '''The ARN of the Destination resource.'''
        result = self._values.get("destination_arn")
        assert result is not None, "Required property 'destination_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def destination_name(self) -> builtins.str:
        '''The Name of the Destination resource.'''
        result = self._values.get("destination_name")
        assert result is not None, "Required property 'destination_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DestinationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.DeviceProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "device_profile_arn": "deviceProfileArn",
        "device_profile_id": "deviceProfileId",
    },
)
class DeviceProfileReference:
    def __init__(
        self,
        *,
        device_profile_arn: builtins.str,
        device_profile_id: builtins.str,
    ) -> None:
        '''A reference to a DeviceProfile resource.

        :param device_profile_arn: The ARN of the DeviceProfile resource.
        :param device_profile_id: The Id of the DeviceProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            device_profile_reference = interfaces_iotwireless.DeviceProfileReference(
                device_profile_arn="deviceProfileArn",
                device_profile_id="deviceProfileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__416166c6fcf10bef82f2351948ca45b4fad3dfa063b76d3a692d6b512f0a7b51)
            check_type(argname="argument device_profile_arn", value=device_profile_arn, expected_type=type_hints["device_profile_arn"])
            check_type(argname="argument device_profile_id", value=device_profile_id, expected_type=type_hints["device_profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_profile_arn": device_profile_arn,
            "device_profile_id": device_profile_id,
        }

    @builtins.property
    def device_profile_arn(self) -> builtins.str:
        '''The ARN of the DeviceProfile resource.'''
        result = self._values.get("device_profile_arn")
        assert result is not None, "Required property 'device_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def device_profile_id(self) -> builtins.str:
        '''The Id of the DeviceProfile resource.'''
        result = self._values.get("device_profile_id")
        assert result is not None, "Required property 'device_profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeviceProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.FuotaTaskReference",
    jsii_struct_bases=[],
    name_mapping={"fuota_task_arn": "fuotaTaskArn", "fuota_task_id": "fuotaTaskId"},
)
class FuotaTaskReference:
    def __init__(
        self,
        *,
        fuota_task_arn: builtins.str,
        fuota_task_id: builtins.str,
    ) -> None:
        '''A reference to a FuotaTask resource.

        :param fuota_task_arn: The ARN of the FuotaTask resource.
        :param fuota_task_id: The Id of the FuotaTask resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            fuota_task_reference = interfaces_iotwireless.FuotaTaskReference(
                fuota_task_arn="fuotaTaskArn",
                fuota_task_id="fuotaTaskId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b92f2d5a0a31b7ffdf6ba02963ee7578398c952802ece9c619e2b5bcab41093e)
            check_type(argname="argument fuota_task_arn", value=fuota_task_arn, expected_type=type_hints["fuota_task_arn"])
            check_type(argname="argument fuota_task_id", value=fuota_task_id, expected_type=type_hints["fuota_task_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fuota_task_arn": fuota_task_arn,
            "fuota_task_id": fuota_task_id,
        }

    @builtins.property
    def fuota_task_arn(self) -> builtins.str:
        '''The ARN of the FuotaTask resource.'''
        result = self._values.get("fuota_task_arn")
        assert result is not None, "Required property 'fuota_task_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fuota_task_id(self) -> builtins.str:
        '''The Id of the FuotaTask resource.'''
        result = self._values.get("fuota_task_id")
        assert result is not None, "Required property 'fuota_task_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FuotaTaskReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.IDestinationRef")
class IDestinationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Destination.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="destinationRef")
    def destination_ref(self) -> "DestinationReference":
        '''(experimental) A reference to a Destination resource.

        :stability: experimental
        '''
        ...


class _IDestinationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Destination.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.IDestinationRef"

    @builtins.property
    @jsii.member(jsii_name="destinationRef")
    def destination_ref(self) -> "DestinationReference":
        '''(experimental) A reference to a Destination resource.

        :stability: experimental
        '''
        return typing.cast("DestinationReference", jsii.get(self, "destinationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDestinationRef).__jsii_proxy_class__ = lambda : _IDestinationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.IDeviceProfileRef")
class IDeviceProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeviceProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deviceProfileRef")
    def device_profile_ref(self) -> "DeviceProfileReference":
        '''(experimental) A reference to a DeviceProfile resource.

        :stability: experimental
        '''
        ...


class _IDeviceProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeviceProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.IDeviceProfileRef"

    @builtins.property
    @jsii.member(jsii_name="deviceProfileRef")
    def device_profile_ref(self) -> "DeviceProfileReference":
        '''(experimental) A reference to a DeviceProfile resource.

        :stability: experimental
        '''
        return typing.cast("DeviceProfileReference", jsii.get(self, "deviceProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeviceProfileRef).__jsii_proxy_class__ = lambda : _IDeviceProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.IFuotaTaskRef")
class IFuotaTaskRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FuotaTask.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fuotaTaskRef")
    def fuota_task_ref(self) -> "FuotaTaskReference":
        '''(experimental) A reference to a FuotaTask resource.

        :stability: experimental
        '''
        ...


class _IFuotaTaskRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FuotaTask.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.IFuotaTaskRef"

    @builtins.property
    @jsii.member(jsii_name="fuotaTaskRef")
    def fuota_task_ref(self) -> "FuotaTaskReference":
        '''(experimental) A reference to a FuotaTask resource.

        :stability: experimental
        '''
        return typing.cast("FuotaTaskReference", jsii.get(self, "fuotaTaskRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFuotaTaskRef).__jsii_proxy_class__ = lambda : _IFuotaTaskRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.IMulticastGroupRef")
class IMulticastGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MulticastGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="multicastGroupRef")
    def multicast_group_ref(self) -> "MulticastGroupReference":
        '''(experimental) A reference to a MulticastGroup resource.

        :stability: experimental
        '''
        ...


class _IMulticastGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MulticastGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.IMulticastGroupRef"

    @builtins.property
    @jsii.member(jsii_name="multicastGroupRef")
    def multicast_group_ref(self) -> "MulticastGroupReference":
        '''(experimental) A reference to a MulticastGroup resource.

        :stability: experimental
        '''
        return typing.cast("MulticastGroupReference", jsii.get(self, "multicastGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMulticastGroupRef).__jsii_proxy_class__ = lambda : _IMulticastGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.INetworkAnalyzerConfigurationRef"
)
class INetworkAnalyzerConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkAnalyzerConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkAnalyzerConfigurationRef")
    def network_analyzer_configuration_ref(
        self,
    ) -> "NetworkAnalyzerConfigurationReference":
        '''(experimental) A reference to a NetworkAnalyzerConfiguration resource.

        :stability: experimental
        '''
        ...


class _INetworkAnalyzerConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkAnalyzerConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.INetworkAnalyzerConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="networkAnalyzerConfigurationRef")
    def network_analyzer_configuration_ref(
        self,
    ) -> "NetworkAnalyzerConfigurationReference":
        '''(experimental) A reference to a NetworkAnalyzerConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("NetworkAnalyzerConfigurationReference", jsii.get(self, "networkAnalyzerConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkAnalyzerConfigurationRef).__jsii_proxy_class__ = lambda : _INetworkAnalyzerConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.IPartnerAccountRef")
class IPartnerAccountRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PartnerAccount.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="partnerAccountRef")
    def partner_account_ref(self) -> "PartnerAccountReference":
        '''(experimental) A reference to a PartnerAccount resource.

        :stability: experimental
        '''
        ...


class _IPartnerAccountRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PartnerAccount.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.IPartnerAccountRef"

    @builtins.property
    @jsii.member(jsii_name="partnerAccountRef")
    def partner_account_ref(self) -> "PartnerAccountReference":
        '''(experimental) A reference to a PartnerAccount resource.

        :stability: experimental
        '''
        return typing.cast("PartnerAccountReference", jsii.get(self, "partnerAccountRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPartnerAccountRef).__jsii_proxy_class__ = lambda : _IPartnerAccountRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.IServiceProfileRef")
class IServiceProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceProfileRef")
    def service_profile_ref(self) -> "ServiceProfileReference":
        '''(experimental) A reference to a ServiceProfile resource.

        :stability: experimental
        '''
        ...


class _IServiceProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.IServiceProfileRef"

    @builtins.property
    @jsii.member(jsii_name="serviceProfileRef")
    def service_profile_ref(self) -> "ServiceProfileReference":
        '''(experimental) A reference to a ServiceProfile resource.

        :stability: experimental
        '''
        return typing.cast("ServiceProfileReference", jsii.get(self, "serviceProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceProfileRef).__jsii_proxy_class__ = lambda : _IServiceProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.ITaskDefinitionRef")
class ITaskDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TaskDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionRef")
    def task_definition_ref(self) -> "TaskDefinitionReference":
        '''(experimental) A reference to a TaskDefinition resource.

        :stability: experimental
        '''
        ...


class _ITaskDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TaskDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.ITaskDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionRef")
    def task_definition_ref(self) -> "TaskDefinitionReference":
        '''(experimental) A reference to a TaskDefinition resource.

        :stability: experimental
        '''
        return typing.cast("TaskDefinitionReference", jsii.get(self, "taskDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITaskDefinitionRef).__jsii_proxy_class__ = lambda : _ITaskDefinitionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.IWirelessDeviceImportTaskRef"
)
class IWirelessDeviceImportTaskRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WirelessDeviceImportTask.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="wirelessDeviceImportTaskRef")
    def wireless_device_import_task_ref(self) -> "WirelessDeviceImportTaskReference":
        '''(experimental) A reference to a WirelessDeviceImportTask resource.

        :stability: experimental
        '''
        ...


class _IWirelessDeviceImportTaskRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WirelessDeviceImportTask.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.IWirelessDeviceImportTaskRef"

    @builtins.property
    @jsii.member(jsii_name="wirelessDeviceImportTaskRef")
    def wireless_device_import_task_ref(self) -> "WirelessDeviceImportTaskReference":
        '''(experimental) A reference to a WirelessDeviceImportTask resource.

        :stability: experimental
        '''
        return typing.cast("WirelessDeviceImportTaskReference", jsii.get(self, "wirelessDeviceImportTaskRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWirelessDeviceImportTaskRef).__jsii_proxy_class__ = lambda : _IWirelessDeviceImportTaskRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.IWirelessDeviceRef")
class IWirelessDeviceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WirelessDevice.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="wirelessDeviceRef")
    def wireless_device_ref(self) -> "WirelessDeviceReference":
        '''(experimental) A reference to a WirelessDevice resource.

        :stability: experimental
        '''
        ...


class _IWirelessDeviceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WirelessDevice.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.IWirelessDeviceRef"

    @builtins.property
    @jsii.member(jsii_name="wirelessDeviceRef")
    def wireless_device_ref(self) -> "WirelessDeviceReference":
        '''(experimental) A reference to a WirelessDevice resource.

        :stability: experimental
        '''
        return typing.cast("WirelessDeviceReference", jsii.get(self, "wirelessDeviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWirelessDeviceRef).__jsii_proxy_class__ = lambda : _IWirelessDeviceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.IWirelessGatewayRef")
class IWirelessGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WirelessGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="wirelessGatewayRef")
    def wireless_gateway_ref(self) -> "WirelessGatewayReference":
        '''(experimental) A reference to a WirelessGateway resource.

        :stability: experimental
        '''
        ...


class _IWirelessGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WirelessGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotwireless.IWirelessGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="wirelessGatewayRef")
    def wireless_gateway_ref(self) -> "WirelessGatewayReference":
        '''(experimental) A reference to a WirelessGateway resource.

        :stability: experimental
        '''
        return typing.cast("WirelessGatewayReference", jsii.get(self, "wirelessGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWirelessGatewayRef).__jsii_proxy_class__ = lambda : _IWirelessGatewayRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.MulticastGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "multicast_group_arn": "multicastGroupArn",
        "multicast_group_id": "multicastGroupId",
    },
)
class MulticastGroupReference:
    def __init__(
        self,
        *,
        multicast_group_arn: builtins.str,
        multicast_group_id: builtins.str,
    ) -> None:
        '''A reference to a MulticastGroup resource.

        :param multicast_group_arn: The ARN of the MulticastGroup resource.
        :param multicast_group_id: The Id of the MulticastGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            multicast_group_reference = interfaces_iotwireless.MulticastGroupReference(
                multicast_group_arn="multicastGroupArn",
                multicast_group_id="multicastGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d95417504e8a03f12d5ea08a41f157281d72dac4ea96cc7f7179cd8c85228897)
            check_type(argname="argument multicast_group_arn", value=multicast_group_arn, expected_type=type_hints["multicast_group_arn"])
            check_type(argname="argument multicast_group_id", value=multicast_group_id, expected_type=type_hints["multicast_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "multicast_group_arn": multicast_group_arn,
            "multicast_group_id": multicast_group_id,
        }

    @builtins.property
    def multicast_group_arn(self) -> builtins.str:
        '''The ARN of the MulticastGroup resource.'''
        result = self._values.get("multicast_group_arn")
        assert result is not None, "Required property 'multicast_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def multicast_group_id(self) -> builtins.str:
        '''The Id of the MulticastGroup resource.'''
        result = self._values.get("multicast_group_id")
        assert result is not None, "Required property 'multicast_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MulticastGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.NetworkAnalyzerConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "network_analyzer_configuration_arn": "networkAnalyzerConfigurationArn",
        "network_analyzer_configuration_name": "networkAnalyzerConfigurationName",
    },
)
class NetworkAnalyzerConfigurationReference:
    def __init__(
        self,
        *,
        network_analyzer_configuration_arn: builtins.str,
        network_analyzer_configuration_name: builtins.str,
    ) -> None:
        '''A reference to a NetworkAnalyzerConfiguration resource.

        :param network_analyzer_configuration_arn: The ARN of the NetworkAnalyzerConfiguration resource.
        :param network_analyzer_configuration_name: The Name of the NetworkAnalyzerConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            network_analyzer_configuration_reference = interfaces_iotwireless.NetworkAnalyzerConfigurationReference(
                network_analyzer_configuration_arn="networkAnalyzerConfigurationArn",
                network_analyzer_configuration_name="networkAnalyzerConfigurationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e7e13771b47a12c5dacc1b7440d6477d8ca3e0df8eb03e86978fe5a35334c5)
            check_type(argname="argument network_analyzer_configuration_arn", value=network_analyzer_configuration_arn, expected_type=type_hints["network_analyzer_configuration_arn"])
            check_type(argname="argument network_analyzer_configuration_name", value=network_analyzer_configuration_name, expected_type=type_hints["network_analyzer_configuration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_analyzer_configuration_arn": network_analyzer_configuration_arn,
            "network_analyzer_configuration_name": network_analyzer_configuration_name,
        }

    @builtins.property
    def network_analyzer_configuration_arn(self) -> builtins.str:
        '''The ARN of the NetworkAnalyzerConfiguration resource.'''
        result = self._values.get("network_analyzer_configuration_arn")
        assert result is not None, "Required property 'network_analyzer_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_analyzer_configuration_name(self) -> builtins.str:
        '''The Name of the NetworkAnalyzerConfiguration resource.'''
        result = self._values.get("network_analyzer_configuration_name")
        assert result is not None, "Required property 'network_analyzer_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkAnalyzerConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.PartnerAccountReference",
    jsii_struct_bases=[],
    name_mapping={
        "partner_account_arn": "partnerAccountArn",
        "partner_account_id": "partnerAccountId",
    },
)
class PartnerAccountReference:
    def __init__(
        self,
        *,
        partner_account_arn: builtins.str,
        partner_account_id: builtins.str,
    ) -> None:
        '''A reference to a PartnerAccount resource.

        :param partner_account_arn: The ARN of the PartnerAccount resource.
        :param partner_account_id: The PartnerAccountId of the PartnerAccount resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            partner_account_reference = interfaces_iotwireless.PartnerAccountReference(
                partner_account_arn="partnerAccountArn",
                partner_account_id="partnerAccountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53ea1209b5c561fc95a2355ae6fcf2dd39bc1e082ec5bb66f413062a634a5eba)
            check_type(argname="argument partner_account_arn", value=partner_account_arn, expected_type=type_hints["partner_account_arn"])
            check_type(argname="argument partner_account_id", value=partner_account_id, expected_type=type_hints["partner_account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "partner_account_arn": partner_account_arn,
            "partner_account_id": partner_account_id,
        }

    @builtins.property
    def partner_account_arn(self) -> builtins.str:
        '''The ARN of the PartnerAccount resource.'''
        result = self._values.get("partner_account_arn")
        assert result is not None, "Required property 'partner_account_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partner_account_id(self) -> builtins.str:
        '''The PartnerAccountId of the PartnerAccount resource.'''
        result = self._values.get("partner_account_id")
        assert result is not None, "Required property 'partner_account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PartnerAccountReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.ServiceProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "service_profile_arn": "serviceProfileArn",
        "service_profile_id": "serviceProfileId",
    },
)
class ServiceProfileReference:
    def __init__(
        self,
        *,
        service_profile_arn: builtins.str,
        service_profile_id: builtins.str,
    ) -> None:
        '''A reference to a ServiceProfile resource.

        :param service_profile_arn: The ARN of the ServiceProfile resource.
        :param service_profile_id: The Id of the ServiceProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            service_profile_reference = interfaces_iotwireless.ServiceProfileReference(
                service_profile_arn="serviceProfileArn",
                service_profile_id="serviceProfileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00f2f4e7e00b305d12ba04cebc7d8570a89248a5a86461346058742a8e7a2bbe)
            check_type(argname="argument service_profile_arn", value=service_profile_arn, expected_type=type_hints["service_profile_arn"])
            check_type(argname="argument service_profile_id", value=service_profile_id, expected_type=type_hints["service_profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_profile_arn": service_profile_arn,
            "service_profile_id": service_profile_id,
        }

    @builtins.property
    def service_profile_arn(self) -> builtins.str:
        '''The ARN of the ServiceProfile resource.'''
        result = self._values.get("service_profile_arn")
        assert result is not None, "Required property 'service_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_profile_id(self) -> builtins.str:
        '''The Id of the ServiceProfile resource.'''
        result = self._values.get("service_profile_id")
        assert result is not None, "Required property 'service_profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.TaskDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "task_definition_arn": "taskDefinitionArn",
        "task_definition_id": "taskDefinitionId",
    },
)
class TaskDefinitionReference:
    def __init__(
        self,
        *,
        task_definition_arn: builtins.str,
        task_definition_id: builtins.str,
    ) -> None:
        '''A reference to a TaskDefinition resource.

        :param task_definition_arn: The ARN of the TaskDefinition resource.
        :param task_definition_id: The Id of the TaskDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            task_definition_reference = interfaces_iotwireless.TaskDefinitionReference(
                task_definition_arn="taskDefinitionArn",
                task_definition_id="taskDefinitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c25a17474e35c3ceaaa0cef1f48d046cb1dc5f401db62af77d8ca4b325a0df3)
            check_type(argname="argument task_definition_arn", value=task_definition_arn, expected_type=type_hints["task_definition_arn"])
            check_type(argname="argument task_definition_id", value=task_definition_id, expected_type=type_hints["task_definition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "task_definition_arn": task_definition_arn,
            "task_definition_id": task_definition_id,
        }

    @builtins.property
    def task_definition_arn(self) -> builtins.str:
        '''The ARN of the TaskDefinition resource.'''
        result = self._values.get("task_definition_arn")
        assert result is not None, "Required property 'task_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_definition_id(self) -> builtins.str:
        '''The Id of the TaskDefinition resource.'''
        result = self._values.get("task_definition_id")
        assert result is not None, "Required property 'task_definition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.WirelessDeviceImportTaskReference",
    jsii_struct_bases=[],
    name_mapping={
        "wireless_device_import_task_arn": "wirelessDeviceImportTaskArn",
        "wireless_device_import_task_id": "wirelessDeviceImportTaskId",
    },
)
class WirelessDeviceImportTaskReference:
    def __init__(
        self,
        *,
        wireless_device_import_task_arn: builtins.str,
        wireless_device_import_task_id: builtins.str,
    ) -> None:
        '''A reference to a WirelessDeviceImportTask resource.

        :param wireless_device_import_task_arn: The ARN of the WirelessDeviceImportTask resource.
        :param wireless_device_import_task_id: The Id of the WirelessDeviceImportTask resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            wireless_device_import_task_reference = interfaces_iotwireless.WirelessDeviceImportTaskReference(
                wireless_device_import_task_arn="wirelessDeviceImportTaskArn",
                wireless_device_import_task_id="wirelessDeviceImportTaskId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebb283cc09d3c3f1a6e1c30c5673f07346aeab3baf5caca7749b9ced237896fe)
            check_type(argname="argument wireless_device_import_task_arn", value=wireless_device_import_task_arn, expected_type=type_hints["wireless_device_import_task_arn"])
            check_type(argname="argument wireless_device_import_task_id", value=wireless_device_import_task_id, expected_type=type_hints["wireless_device_import_task_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "wireless_device_import_task_arn": wireless_device_import_task_arn,
            "wireless_device_import_task_id": wireless_device_import_task_id,
        }

    @builtins.property
    def wireless_device_import_task_arn(self) -> builtins.str:
        '''The ARN of the WirelessDeviceImportTask resource.'''
        result = self._values.get("wireless_device_import_task_arn")
        assert result is not None, "Required property 'wireless_device_import_task_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def wireless_device_import_task_id(self) -> builtins.str:
        '''The Id of the WirelessDeviceImportTask resource.'''
        result = self._values.get("wireless_device_import_task_id")
        assert result is not None, "Required property 'wireless_device_import_task_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WirelessDeviceImportTaskReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.WirelessDeviceReference",
    jsii_struct_bases=[],
    name_mapping={
        "wireless_device_arn": "wirelessDeviceArn",
        "wireless_device_id": "wirelessDeviceId",
    },
)
class WirelessDeviceReference:
    def __init__(
        self,
        *,
        wireless_device_arn: builtins.str,
        wireless_device_id: builtins.str,
    ) -> None:
        '''A reference to a WirelessDevice resource.

        :param wireless_device_arn: The ARN of the WirelessDevice resource.
        :param wireless_device_id: The Id of the WirelessDevice resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            wireless_device_reference = interfaces_iotwireless.WirelessDeviceReference(
                wireless_device_arn="wirelessDeviceArn",
                wireless_device_id="wirelessDeviceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17aca232b8799b171f0821cc808b515466fa8821bde82a64f5136ca4d95fece6)
            check_type(argname="argument wireless_device_arn", value=wireless_device_arn, expected_type=type_hints["wireless_device_arn"])
            check_type(argname="argument wireless_device_id", value=wireless_device_id, expected_type=type_hints["wireless_device_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "wireless_device_arn": wireless_device_arn,
            "wireless_device_id": wireless_device_id,
        }

    @builtins.property
    def wireless_device_arn(self) -> builtins.str:
        '''The ARN of the WirelessDevice resource.'''
        result = self._values.get("wireless_device_arn")
        assert result is not None, "Required property 'wireless_device_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def wireless_device_id(self) -> builtins.str:
        '''The Id of the WirelessDevice resource.'''
        result = self._values.get("wireless_device_id")
        assert result is not None, "Required property 'wireless_device_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WirelessDeviceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotwireless.WirelessGatewayReference",
    jsii_struct_bases=[],
    name_mapping={
        "wireless_gateway_arn": "wirelessGatewayArn",
        "wireless_gateway_id": "wirelessGatewayId",
    },
)
class WirelessGatewayReference:
    def __init__(
        self,
        *,
        wireless_gateway_arn: builtins.str,
        wireless_gateway_id: builtins.str,
    ) -> None:
        '''A reference to a WirelessGateway resource.

        :param wireless_gateway_arn: The ARN of the WirelessGateway resource.
        :param wireless_gateway_id: The Id of the WirelessGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotwireless as interfaces_iotwireless
            
            wireless_gateway_reference = interfaces_iotwireless.WirelessGatewayReference(
                wireless_gateway_arn="wirelessGatewayArn",
                wireless_gateway_id="wirelessGatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c455af05bd5f61d3649670ec07120475d0ecd6b1b30ce40ac5b4e24455958c0a)
            check_type(argname="argument wireless_gateway_arn", value=wireless_gateway_arn, expected_type=type_hints["wireless_gateway_arn"])
            check_type(argname="argument wireless_gateway_id", value=wireless_gateway_id, expected_type=type_hints["wireless_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "wireless_gateway_arn": wireless_gateway_arn,
            "wireless_gateway_id": wireless_gateway_id,
        }

    @builtins.property
    def wireless_gateway_arn(self) -> builtins.str:
        '''The ARN of the WirelessGateway resource.'''
        result = self._values.get("wireless_gateway_arn")
        assert result is not None, "Required property 'wireless_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def wireless_gateway_id(self) -> builtins.str:
        '''The Id of the WirelessGateway resource.'''
        result = self._values.get("wireless_gateway_id")
        assert result is not None, "Required property 'wireless_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WirelessGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DestinationReference",
    "DeviceProfileReference",
    "FuotaTaskReference",
    "IDestinationRef",
    "IDeviceProfileRef",
    "IFuotaTaskRef",
    "IMulticastGroupRef",
    "INetworkAnalyzerConfigurationRef",
    "IPartnerAccountRef",
    "IServiceProfileRef",
    "ITaskDefinitionRef",
    "IWirelessDeviceImportTaskRef",
    "IWirelessDeviceRef",
    "IWirelessGatewayRef",
    "MulticastGroupReference",
    "NetworkAnalyzerConfigurationReference",
    "PartnerAccountReference",
    "ServiceProfileReference",
    "TaskDefinitionReference",
    "WirelessDeviceImportTaskReference",
    "WirelessDeviceReference",
    "WirelessGatewayReference",
]

publication.publish()

def _typecheckingstub__01b22cebb6223a17a7839beb314e23234baaee086c51efa6fb71a1476d74032f(
    *,
    destination_arn: builtins.str,
    destination_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__416166c6fcf10bef82f2351948ca45b4fad3dfa063b76d3a692d6b512f0a7b51(
    *,
    device_profile_arn: builtins.str,
    device_profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92f2d5a0a31b7ffdf6ba02963ee7578398c952802ece9c619e2b5bcab41093e(
    *,
    fuota_task_arn: builtins.str,
    fuota_task_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d95417504e8a03f12d5ea08a41f157281d72dac4ea96cc7f7179cd8c85228897(
    *,
    multicast_group_arn: builtins.str,
    multicast_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e7e13771b47a12c5dacc1b7440d6477d8ca3e0df8eb03e86978fe5a35334c5(
    *,
    network_analyzer_configuration_arn: builtins.str,
    network_analyzer_configuration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53ea1209b5c561fc95a2355ae6fcf2dd39bc1e082ec5bb66f413062a634a5eba(
    *,
    partner_account_arn: builtins.str,
    partner_account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00f2f4e7e00b305d12ba04cebc7d8570a89248a5a86461346058742a8e7a2bbe(
    *,
    service_profile_arn: builtins.str,
    service_profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c25a17474e35c3ceaaa0cef1f48d046cb1dc5f401db62af77d8ca4b325a0df3(
    *,
    task_definition_arn: builtins.str,
    task_definition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebb283cc09d3c3f1a6e1c30c5673f07346aeab3baf5caca7749b9ced237896fe(
    *,
    wireless_device_import_task_arn: builtins.str,
    wireless_device_import_task_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17aca232b8799b171f0821cc808b515466fa8821bde82a64f5136ca4d95fece6(
    *,
    wireless_device_arn: builtins.str,
    wireless_device_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c455af05bd5f61d3649670ec07120475d0ecd6b1b30ce40ac5b4e24455958c0a(
    *,
    wireless_gateway_arn: builtins.str,
    wireless_gateway_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDestinationRef, IDeviceProfileRef, IFuotaTaskRef, IMulticastGroupRef, INetworkAnalyzerConfigurationRef, IPartnerAccountRef, IServiceProfileRef, ITaskDefinitionRef, IWirelessDeviceImportTaskRef, IWirelessDeviceRef, IWirelessGatewayRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
