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
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.FarmReference",
    jsii_struct_bases=[],
    name_mapping={"farm_arn": "farmArn"},
)
class FarmReference:
    def __init__(self, *, farm_arn: builtins.str) -> None:
        '''A reference to a Farm resource.

        :param farm_arn: The Arn of the Farm resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            farm_reference = interfaces_deadline.FarmReference(
                farm_arn="farmArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df99153da6eb3ca62b0608e3067ea62d99f63d137a1238499434c5a9cfe18c3a)
            check_type(argname="argument farm_arn", value=farm_arn, expected_type=type_hints["farm_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "farm_arn": farm_arn,
        }

    @builtins.property
    def farm_arn(self) -> builtins.str:
        '''The Arn of the Farm resource.'''
        result = self._values.get("farm_arn")
        assert result is not None, "Required property 'farm_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FarmReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.FleetReference",
    jsii_struct_bases=[],
    name_mapping={"fleet_arn": "fleetArn"},
)
class FleetReference:
    def __init__(self, *, fleet_arn: builtins.str) -> None:
        '''A reference to a Fleet resource.

        :param fleet_arn: The Arn of the Fleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            fleet_reference = interfaces_deadline.FleetReference(
                fleet_arn="fleetArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11423614ebfe79bc624144d41e52f87151a790b2bc31e14259b38a5ab3d11b7a)
            check_type(argname="argument fleet_arn", value=fleet_arn, expected_type=type_hints["fleet_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fleet_arn": fleet_arn,
        }

    @builtins.property
    def fleet_arn(self) -> builtins.str:
        '''The Arn of the Fleet resource.'''
        result = self._values.get("fleet_arn")
        assert result is not None, "Required property 'fleet_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_deadline.IFarmRef")
class IFarmRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Farm.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="farmRef")
    def farm_ref(self) -> "FarmReference":
        '''(experimental) A reference to a Farm resource.

        :stability: experimental
        '''
        ...


class _IFarmRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Farm.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.IFarmRef"

    @builtins.property
    @jsii.member(jsii_name="farmRef")
    def farm_ref(self) -> "FarmReference":
        '''(experimental) A reference to a Farm resource.

        :stability: experimental
        '''
        return typing.cast("FarmReference", jsii.get(self, "farmRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFarmRef).__jsii_proxy_class__ = lambda : _IFarmRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_deadline.IFleetRef")
class IFleetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Fleet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        ...


class _IFleetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Fleet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.IFleetRef"

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        return typing.cast("FleetReference", jsii.get(self, "fleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFleetRef).__jsii_proxy_class__ = lambda : _IFleetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_deadline.ILicenseEndpointRef")
class ILicenseEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LicenseEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="licenseEndpointRef")
    def license_endpoint_ref(self) -> "LicenseEndpointReference":
        '''(experimental) A reference to a LicenseEndpoint resource.

        :stability: experimental
        '''
        ...


class _ILicenseEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LicenseEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.ILicenseEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="licenseEndpointRef")
    def license_endpoint_ref(self) -> "LicenseEndpointReference":
        '''(experimental) A reference to a LicenseEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("LicenseEndpointReference", jsii.get(self, "licenseEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILicenseEndpointRef).__jsii_proxy_class__ = lambda : _ILicenseEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_deadline.ILimitRef")
class ILimitRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Limit.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="limitRef")
    def limit_ref(self) -> "LimitReference":
        '''(experimental) A reference to a Limit resource.

        :stability: experimental
        '''
        ...


class _ILimitRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Limit.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.ILimitRef"

    @builtins.property
    @jsii.member(jsii_name="limitRef")
    def limit_ref(self) -> "LimitReference":
        '''(experimental) A reference to a Limit resource.

        :stability: experimental
        '''
        return typing.cast("LimitReference", jsii.get(self, "limitRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILimitRef).__jsii_proxy_class__ = lambda : _ILimitRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_deadline.IMeteredProductRef")
class IMeteredProductRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MeteredProduct.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="meteredProductRef")
    def metered_product_ref(self) -> "MeteredProductReference":
        '''(experimental) A reference to a MeteredProduct resource.

        :stability: experimental
        '''
        ...


class _IMeteredProductRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MeteredProduct.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.IMeteredProductRef"

    @builtins.property
    @jsii.member(jsii_name="meteredProductRef")
    def metered_product_ref(self) -> "MeteredProductReference":
        '''(experimental) A reference to a MeteredProduct resource.

        :stability: experimental
        '''
        return typing.cast("MeteredProductReference", jsii.get(self, "meteredProductRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMeteredProductRef).__jsii_proxy_class__ = lambda : _IMeteredProductRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_deadline.IMonitorRef")
class IMonitorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Monitor.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="monitorRef")
    def monitor_ref(self) -> "MonitorReference":
        '''(experimental) A reference to a Monitor resource.

        :stability: experimental
        '''
        ...


class _IMonitorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Monitor.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.IMonitorRef"

    @builtins.property
    @jsii.member(jsii_name="monitorRef")
    def monitor_ref(self) -> "MonitorReference":
        '''(experimental) A reference to a Monitor resource.

        :stability: experimental
        '''
        return typing.cast("MonitorReference", jsii.get(self, "monitorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMonitorRef).__jsii_proxy_class__ = lambda : _IMonitorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_deadline.IQueueEnvironmentRef")
class IQueueEnvironmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a QueueEnvironment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queueEnvironmentRef")
    def queue_environment_ref(self) -> "QueueEnvironmentReference":
        '''(experimental) A reference to a QueueEnvironment resource.

        :stability: experimental
        '''
        ...


class _IQueueEnvironmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a QueueEnvironment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.IQueueEnvironmentRef"

    @builtins.property
    @jsii.member(jsii_name="queueEnvironmentRef")
    def queue_environment_ref(self) -> "QueueEnvironmentReference":
        '''(experimental) A reference to a QueueEnvironment resource.

        :stability: experimental
        '''
        return typing.cast("QueueEnvironmentReference", jsii.get(self, "queueEnvironmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueueEnvironmentRef).__jsii_proxy_class__ = lambda : _IQueueEnvironmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.IQueueFleetAssociationRef"
)
class IQueueFleetAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a QueueFleetAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queueFleetAssociationRef")
    def queue_fleet_association_ref(self) -> "QueueFleetAssociationReference":
        '''(experimental) A reference to a QueueFleetAssociation resource.

        :stability: experimental
        '''
        ...


class _IQueueFleetAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a QueueFleetAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.IQueueFleetAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="queueFleetAssociationRef")
    def queue_fleet_association_ref(self) -> "QueueFleetAssociationReference":
        '''(experimental) A reference to a QueueFleetAssociation resource.

        :stability: experimental
        '''
        return typing.cast("QueueFleetAssociationReference", jsii.get(self, "queueFleetAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueueFleetAssociationRef).__jsii_proxy_class__ = lambda : _IQueueFleetAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.IQueueLimitAssociationRef"
)
class IQueueLimitAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a QueueLimitAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queueLimitAssociationRef")
    def queue_limit_association_ref(self) -> "QueueLimitAssociationReference":
        '''(experimental) A reference to a QueueLimitAssociation resource.

        :stability: experimental
        '''
        ...


class _IQueueLimitAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a QueueLimitAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.IQueueLimitAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="queueLimitAssociationRef")
    def queue_limit_association_ref(self) -> "QueueLimitAssociationReference":
        '''(experimental) A reference to a QueueLimitAssociation resource.

        :stability: experimental
        '''
        return typing.cast("QueueLimitAssociationReference", jsii.get(self, "queueLimitAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueueLimitAssociationRef).__jsii_proxy_class__ = lambda : _IQueueLimitAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_deadline.IQueueRef")
class IQueueRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Queue.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queueRef")
    def queue_ref(self) -> "QueueReference":
        '''(experimental) A reference to a Queue resource.

        :stability: experimental
        '''
        ...


class _IQueueRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Queue.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.IQueueRef"

    @builtins.property
    @jsii.member(jsii_name="queueRef")
    def queue_ref(self) -> "QueueReference":
        '''(experimental) A reference to a Queue resource.

        :stability: experimental
        '''
        return typing.cast("QueueReference", jsii.get(self, "queueRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueueRef).__jsii_proxy_class__ = lambda : _IQueueRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_deadline.IStorageProfileRef")
class IStorageProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StorageProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="storageProfileRef")
    def storage_profile_ref(self) -> "StorageProfileReference":
        '''(experimental) A reference to a StorageProfile resource.

        :stability: experimental
        '''
        ...


class _IStorageProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StorageProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_deadline.IStorageProfileRef"

    @builtins.property
    @jsii.member(jsii_name="storageProfileRef")
    def storage_profile_ref(self) -> "StorageProfileReference":
        '''(experimental) A reference to a StorageProfile resource.

        :stability: experimental
        '''
        return typing.cast("StorageProfileReference", jsii.get(self, "storageProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStorageProfileRef).__jsii_proxy_class__ = lambda : _IStorageProfileRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.LicenseEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"license_endpoint_arn": "licenseEndpointArn"},
)
class LicenseEndpointReference:
    def __init__(self, *, license_endpoint_arn: builtins.str) -> None:
        '''A reference to a LicenseEndpoint resource.

        :param license_endpoint_arn: The Arn of the LicenseEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            license_endpoint_reference = interfaces_deadline.LicenseEndpointReference(
                license_endpoint_arn="licenseEndpointArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a65d81a345ecd21e0a8920fe1134f641700b5d1b805a876ebf3d9119eec56203)
            check_type(argname="argument license_endpoint_arn", value=license_endpoint_arn, expected_type=type_hints["license_endpoint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "license_endpoint_arn": license_endpoint_arn,
        }

    @builtins.property
    def license_endpoint_arn(self) -> builtins.str:
        '''The Arn of the LicenseEndpoint resource.'''
        result = self._values.get("license_endpoint_arn")
        assert result is not None, "Required property 'license_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LicenseEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.LimitReference",
    jsii_struct_bases=[],
    name_mapping={"farm_id": "farmId", "limit_id": "limitId"},
)
class LimitReference:
    def __init__(self, *, farm_id: builtins.str, limit_id: builtins.str) -> None:
        '''A reference to a Limit resource.

        :param farm_id: The FarmId of the Limit resource.
        :param limit_id: The LimitId of the Limit resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            limit_reference = interfaces_deadline.LimitReference(
                farm_id="farmId",
                limit_id="limitId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15fd5d3ace1136b8e519ab8902fd31c72a2fcf2f331b52c78b33f50e099678e9)
            check_type(argname="argument farm_id", value=farm_id, expected_type=type_hints["farm_id"])
            check_type(argname="argument limit_id", value=limit_id, expected_type=type_hints["limit_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "farm_id": farm_id,
            "limit_id": limit_id,
        }

    @builtins.property
    def farm_id(self) -> builtins.str:
        '''The FarmId of the Limit resource.'''
        result = self._values.get("farm_id")
        assert result is not None, "Required property 'farm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def limit_id(self) -> builtins.str:
        '''The LimitId of the Limit resource.'''
        result = self._values.get("limit_id")
        assert result is not None, "Required property 'limit_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LimitReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.MeteredProductReference",
    jsii_struct_bases=[],
    name_mapping={"metered_product_arn": "meteredProductArn"},
)
class MeteredProductReference:
    def __init__(self, *, metered_product_arn: builtins.str) -> None:
        '''A reference to a MeteredProduct resource.

        :param metered_product_arn: The Arn of the MeteredProduct resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            metered_product_reference = interfaces_deadline.MeteredProductReference(
                metered_product_arn="meteredProductArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a4ab99457156e6e3be3dc3ff89dd0d3f75d121ab0dabcab8a29d817ac0e750d)
            check_type(argname="argument metered_product_arn", value=metered_product_arn, expected_type=type_hints["metered_product_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "metered_product_arn": metered_product_arn,
        }

    @builtins.property
    def metered_product_arn(self) -> builtins.str:
        '''The Arn of the MeteredProduct resource.'''
        result = self._values.get("metered_product_arn")
        assert result is not None, "Required property 'metered_product_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MeteredProductReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.MonitorReference",
    jsii_struct_bases=[],
    name_mapping={"monitor_arn": "monitorArn"},
)
class MonitorReference:
    def __init__(self, *, monitor_arn: builtins.str) -> None:
        '''A reference to a Monitor resource.

        :param monitor_arn: The Arn of the Monitor resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            monitor_reference = interfaces_deadline.MonitorReference(
                monitor_arn="monitorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd1e2f3342f18dcc723759973d0d283ccd7c291e36462cf22f025595059bc1af)
            check_type(argname="argument monitor_arn", value=monitor_arn, expected_type=type_hints["monitor_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitor_arn": monitor_arn,
        }

    @builtins.property
    def monitor_arn(self) -> builtins.str:
        '''The Arn of the Monitor resource.'''
        result = self._values.get("monitor_arn")
        assert result is not None, "Required property 'monitor_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MonitorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.QueueEnvironmentReference",
    jsii_struct_bases=[],
    name_mapping={
        "farm_id": "farmId",
        "queue_environment_id": "queueEnvironmentId",
        "queue_id": "queueId",
    },
)
class QueueEnvironmentReference:
    def __init__(
        self,
        *,
        farm_id: builtins.str,
        queue_environment_id: builtins.str,
        queue_id: builtins.str,
    ) -> None:
        '''A reference to a QueueEnvironment resource.

        :param farm_id: The FarmId of the QueueEnvironment resource.
        :param queue_environment_id: The QueueEnvironmentId of the QueueEnvironment resource.
        :param queue_id: The QueueId of the QueueEnvironment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            queue_environment_reference = interfaces_deadline.QueueEnvironmentReference(
                farm_id="farmId",
                queue_environment_id="queueEnvironmentId",
                queue_id="queueId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e08d0d1a8679a61e7a4646b9d545773c128ff748ae2e4766c4c560318341869)
            check_type(argname="argument farm_id", value=farm_id, expected_type=type_hints["farm_id"])
            check_type(argname="argument queue_environment_id", value=queue_environment_id, expected_type=type_hints["queue_environment_id"])
            check_type(argname="argument queue_id", value=queue_id, expected_type=type_hints["queue_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "farm_id": farm_id,
            "queue_environment_id": queue_environment_id,
            "queue_id": queue_id,
        }

    @builtins.property
    def farm_id(self) -> builtins.str:
        '''The FarmId of the QueueEnvironment resource.'''
        result = self._values.get("farm_id")
        assert result is not None, "Required property 'farm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_environment_id(self) -> builtins.str:
        '''The QueueEnvironmentId of the QueueEnvironment resource.'''
        result = self._values.get("queue_environment_id")
        assert result is not None, "Required property 'queue_environment_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_id(self) -> builtins.str:
        '''The QueueId of the QueueEnvironment resource.'''
        result = self._values.get("queue_id")
        assert result is not None, "Required property 'queue_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueEnvironmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.QueueFleetAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"farm_id": "farmId", "fleet_id": "fleetId", "queue_id": "queueId"},
)
class QueueFleetAssociationReference:
    def __init__(
        self,
        *,
        farm_id: builtins.str,
        fleet_id: builtins.str,
        queue_id: builtins.str,
    ) -> None:
        '''A reference to a QueueFleetAssociation resource.

        :param farm_id: The FarmId of the QueueFleetAssociation resource.
        :param fleet_id: The FleetId of the QueueFleetAssociation resource.
        :param queue_id: The QueueId of the QueueFleetAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            queue_fleet_association_reference = interfaces_deadline.QueueFleetAssociationReference(
                farm_id="farmId",
                fleet_id="fleetId",
                queue_id="queueId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f29a4c3f81d41e6f30228663837bfb0dfd1ba070a0c12c6683e9c59ee2a786eb)
            check_type(argname="argument farm_id", value=farm_id, expected_type=type_hints["farm_id"])
            check_type(argname="argument fleet_id", value=fleet_id, expected_type=type_hints["fleet_id"])
            check_type(argname="argument queue_id", value=queue_id, expected_type=type_hints["queue_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "queue_id": queue_id,
        }

    @builtins.property
    def farm_id(self) -> builtins.str:
        '''The FarmId of the QueueFleetAssociation resource.'''
        result = self._values.get("farm_id")
        assert result is not None, "Required property 'farm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fleet_id(self) -> builtins.str:
        '''The FleetId of the QueueFleetAssociation resource.'''
        result = self._values.get("fleet_id")
        assert result is not None, "Required property 'fleet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_id(self) -> builtins.str:
        '''The QueueId of the QueueFleetAssociation resource.'''
        result = self._values.get("queue_id")
        assert result is not None, "Required property 'queue_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueFleetAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.QueueLimitAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"farm_id": "farmId", "limit_id": "limitId", "queue_id": "queueId"},
)
class QueueLimitAssociationReference:
    def __init__(
        self,
        *,
        farm_id: builtins.str,
        limit_id: builtins.str,
        queue_id: builtins.str,
    ) -> None:
        '''A reference to a QueueLimitAssociation resource.

        :param farm_id: The FarmId of the QueueLimitAssociation resource.
        :param limit_id: The LimitId of the QueueLimitAssociation resource.
        :param queue_id: The QueueId of the QueueLimitAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            queue_limit_association_reference = interfaces_deadline.QueueLimitAssociationReference(
                farm_id="farmId",
                limit_id="limitId",
                queue_id="queueId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3856621b5c5a42b0e69163693d3b2eff2b022f54c69e9819b7ee7ac83f596de5)
            check_type(argname="argument farm_id", value=farm_id, expected_type=type_hints["farm_id"])
            check_type(argname="argument limit_id", value=limit_id, expected_type=type_hints["limit_id"])
            check_type(argname="argument queue_id", value=queue_id, expected_type=type_hints["queue_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "farm_id": farm_id,
            "limit_id": limit_id,
            "queue_id": queue_id,
        }

    @builtins.property
    def farm_id(self) -> builtins.str:
        '''The FarmId of the QueueLimitAssociation resource.'''
        result = self._values.get("farm_id")
        assert result is not None, "Required property 'farm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def limit_id(self) -> builtins.str:
        '''The LimitId of the QueueLimitAssociation resource.'''
        result = self._values.get("limit_id")
        assert result is not None, "Required property 'limit_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_id(self) -> builtins.str:
        '''The QueueId of the QueueLimitAssociation resource.'''
        result = self._values.get("queue_id")
        assert result is not None, "Required property 'queue_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueLimitAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.QueueReference",
    jsii_struct_bases=[],
    name_mapping={"queue_arn": "queueArn"},
)
class QueueReference:
    def __init__(self, *, queue_arn: builtins.str) -> None:
        '''A reference to a Queue resource.

        :param queue_arn: The Arn of the Queue resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            queue_reference = interfaces_deadline.QueueReference(
                queue_arn="queueArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d94dff445ee31e3bcdcb3f94a6b60b1559b385f92eb3fff2a2b01b1d1406fe5)
            check_type(argname="argument queue_arn", value=queue_arn, expected_type=type_hints["queue_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "queue_arn": queue_arn,
        }

    @builtins.property
    def queue_arn(self) -> builtins.str:
        '''The Arn of the Queue resource.'''
        result = self._values.get("queue_arn")
        assert result is not None, "Required property 'queue_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_deadline.StorageProfileReference",
    jsii_struct_bases=[],
    name_mapping={"farm_id": "farmId", "storage_profile_id": "storageProfileId"},
)
class StorageProfileReference:
    def __init__(
        self,
        *,
        farm_id: builtins.str,
        storage_profile_id: builtins.str,
    ) -> None:
        '''A reference to a StorageProfile resource.

        :param farm_id: The FarmId of the StorageProfile resource.
        :param storage_profile_id: The StorageProfileId of the StorageProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_deadline as interfaces_deadline
            
            storage_profile_reference = interfaces_deadline.StorageProfileReference(
                farm_id="farmId",
                storage_profile_id="storageProfileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f92720515e6a968365e391848e2b0c280919eebf82cb53130c21a2b13e041586)
            check_type(argname="argument farm_id", value=farm_id, expected_type=type_hints["farm_id"])
            check_type(argname="argument storage_profile_id", value=storage_profile_id, expected_type=type_hints["storage_profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "farm_id": farm_id,
            "storage_profile_id": storage_profile_id,
        }

    @builtins.property
    def farm_id(self) -> builtins.str:
        '''The FarmId of the StorageProfile resource.'''
        result = self._values.get("farm_id")
        assert result is not None, "Required property 'farm_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_profile_id(self) -> builtins.str:
        '''The StorageProfileId of the StorageProfile resource.'''
        result = self._values.get("storage_profile_id")
        assert result is not None, "Required property 'storage_profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "FarmReference",
    "FleetReference",
    "IFarmRef",
    "IFleetRef",
    "ILicenseEndpointRef",
    "ILimitRef",
    "IMeteredProductRef",
    "IMonitorRef",
    "IQueueEnvironmentRef",
    "IQueueFleetAssociationRef",
    "IQueueLimitAssociationRef",
    "IQueueRef",
    "IStorageProfileRef",
    "LicenseEndpointReference",
    "LimitReference",
    "MeteredProductReference",
    "MonitorReference",
    "QueueEnvironmentReference",
    "QueueFleetAssociationReference",
    "QueueLimitAssociationReference",
    "QueueReference",
    "StorageProfileReference",
]

publication.publish()

def _typecheckingstub__df99153da6eb3ca62b0608e3067ea62d99f63d137a1238499434c5a9cfe18c3a(
    *,
    farm_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11423614ebfe79bc624144d41e52f87151a790b2bc31e14259b38a5ab3d11b7a(
    *,
    fleet_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a65d81a345ecd21e0a8920fe1134f641700b5d1b805a876ebf3d9119eec56203(
    *,
    license_endpoint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15fd5d3ace1136b8e519ab8902fd31c72a2fcf2f331b52c78b33f50e099678e9(
    *,
    farm_id: builtins.str,
    limit_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a4ab99457156e6e3be3dc3ff89dd0d3f75d121ab0dabcab8a29d817ac0e750d(
    *,
    metered_product_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd1e2f3342f18dcc723759973d0d283ccd7c291e36462cf22f025595059bc1af(
    *,
    monitor_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e08d0d1a8679a61e7a4646b9d545773c128ff748ae2e4766c4c560318341869(
    *,
    farm_id: builtins.str,
    queue_environment_id: builtins.str,
    queue_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f29a4c3f81d41e6f30228663837bfb0dfd1ba070a0c12c6683e9c59ee2a786eb(
    *,
    farm_id: builtins.str,
    fleet_id: builtins.str,
    queue_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3856621b5c5a42b0e69163693d3b2eff2b022f54c69e9819b7ee7ac83f596de5(
    *,
    farm_id: builtins.str,
    limit_id: builtins.str,
    queue_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d94dff445ee31e3bcdcb3f94a6b60b1559b385f92eb3fff2a2b01b1d1406fe5(
    *,
    queue_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f92720515e6a968365e391848e2b0c280919eebf82cb53130c21a2b13e041586(
    *,
    farm_id: builtins.str,
    storage_profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IFarmRef, IFleetRef, ILicenseEndpointRef, ILimitRef, IMeteredProductRef, IMonitorRef, IQueueEnvironmentRef, IQueueFleetAssociationRef, IQueueLimitAssociationRef, IQueueRef, IStorageProfileRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
