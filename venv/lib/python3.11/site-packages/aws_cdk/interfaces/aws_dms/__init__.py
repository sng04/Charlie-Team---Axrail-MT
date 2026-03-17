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
    jsii_type="aws-cdk-lib.interfaces.aws_dms.CertificateReference",
    jsii_struct_bases=[],
    name_mapping={"certificate_id": "certificateId"},
)
class CertificateReference:
    def __init__(self, *, certificate_id: builtins.str) -> None:
        '''A reference to a Certificate resource.

        :param certificate_id: The Id of the Certificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            certificate_reference = interfaces_dms.CertificateReference(
                certificate_id="certificateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dddbb2d150dcddbead74d31a5ed63e027a36c883e3adff1a6625fb7bf556ba97)
            check_type(argname="argument certificate_id", value=certificate_id, expected_type=type_hints["certificate_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_id": certificate_id,
        }

    @builtins.property
    def certificate_id(self) -> builtins.str:
        '''The Id of the Certificate resource.'''
        result = self._values.get("certificate_id")
        assert result is not None, "Required property 'certificate_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dms.DataMigrationReference",
    jsii_struct_bases=[],
    name_mapping={"data_migration_arn": "dataMigrationArn"},
)
class DataMigrationReference:
    def __init__(self, *, data_migration_arn: builtins.str) -> None:
        '''A reference to a DataMigration resource.

        :param data_migration_arn: The DataMigrationArn of the DataMigration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            data_migration_reference = interfaces_dms.DataMigrationReference(
                data_migration_arn="dataMigrationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7ce32da77e89591c1e645a63211fb840843830d36317162cdaeb7c245a833fc)
            check_type(argname="argument data_migration_arn", value=data_migration_arn, expected_type=type_hints["data_migration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_migration_arn": data_migration_arn,
        }

    @builtins.property
    def data_migration_arn(self) -> builtins.str:
        '''The DataMigrationArn of the DataMigration resource.'''
        result = self._values.get("data_migration_arn")
        assert result is not None, "Required property 'data_migration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataMigrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dms.DataProviderReference",
    jsii_struct_bases=[],
    name_mapping={"data_provider_arn": "dataProviderArn"},
)
class DataProviderReference:
    def __init__(self, *, data_provider_arn: builtins.str) -> None:
        '''A reference to a DataProvider resource.

        :param data_provider_arn: The DataProviderArn of the DataProvider resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            data_provider_reference = interfaces_dms.DataProviderReference(
                data_provider_arn="dataProviderArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__538ed4e8d5aaca3877a044998ac0a9f566f87cf7e0155ab9c32b465fb4eec685)
            check_type(argname="argument data_provider_arn", value=data_provider_arn, expected_type=type_hints["data_provider_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_provider_arn": data_provider_arn,
        }

    @builtins.property
    def data_provider_arn(self) -> builtins.str:
        '''The DataProviderArn of the DataProvider resource.'''
        result = self._values.get("data_provider_arn")
        assert result is not None, "Required property 'data_provider_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataProviderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dms.EndpointReference",
    jsii_struct_bases=[],
    name_mapping={"endpoint_id": "endpointId"},
)
class EndpointReference:
    def __init__(self, *, endpoint_id: builtins.str) -> None:
        '''A reference to a Endpoint resource.

        :param endpoint_id: The Id of the Endpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            endpoint_reference = interfaces_dms.EndpointReference(
                endpoint_id="endpointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bacd7fb4a98e49b4d9cba342b46e91b7d78d2478a75083429d89359bedf9c098)
            check_type(argname="argument endpoint_id", value=endpoint_id, expected_type=type_hints["endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_id": endpoint_id,
        }

    @builtins.property
    def endpoint_id(self) -> builtins.str:
        '''The Id of the Endpoint resource.'''
        result = self._values.get("endpoint_id")
        assert result is not None, "Required property 'endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dms.EventSubscriptionReference",
    jsii_struct_bases=[],
    name_mapping={"subscription_name": "subscriptionName"},
)
class EventSubscriptionReference:
    def __init__(self, *, subscription_name: builtins.str) -> None:
        '''A reference to a EventSubscription resource.

        :param subscription_name: The SubscriptionName of the EventSubscription resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            event_subscription_reference = interfaces_dms.EventSubscriptionReference(
                subscription_name="subscriptionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e10f1fa5fdaaffb8747b447030f241bdfa52238714c1ac890118f7dccdb0da41)
            check_type(argname="argument subscription_name", value=subscription_name, expected_type=type_hints["subscription_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscription_name": subscription_name,
        }

    @builtins.property
    def subscription_name(self) -> builtins.str:
        '''The SubscriptionName of the EventSubscription resource.'''
        result = self._values.get("subscription_name")
        assert result is not None, "Required property 'subscription_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventSubscriptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.ICertificateRef")
class ICertificateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Certificate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="certificateRef")
    def certificate_ref(self) -> "CertificateReference":
        '''(experimental) A reference to a Certificate resource.

        :stability: experimental
        '''
        ...


class _ICertificateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Certificate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.ICertificateRef"

    @builtins.property
    @jsii.member(jsii_name="certificateRef")
    def certificate_ref(self) -> "CertificateReference":
        '''(experimental) A reference to a Certificate resource.

        :stability: experimental
        '''
        return typing.cast("CertificateReference", jsii.get(self, "certificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificateRef).__jsii_proxy_class__ = lambda : _ICertificateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.IDataMigrationRef")
class IDataMigrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataMigration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataMigrationRef")
    def data_migration_ref(self) -> "DataMigrationReference":
        '''(experimental) A reference to a DataMigration resource.

        :stability: experimental
        '''
        ...


class _IDataMigrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataMigration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.IDataMigrationRef"

    @builtins.property
    @jsii.member(jsii_name="dataMigrationRef")
    def data_migration_ref(self) -> "DataMigrationReference":
        '''(experimental) A reference to a DataMigration resource.

        :stability: experimental
        '''
        return typing.cast("DataMigrationReference", jsii.get(self, "dataMigrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataMigrationRef).__jsii_proxy_class__ = lambda : _IDataMigrationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.IDataProviderRef")
class IDataProviderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataProvider.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataProviderRef")
    def data_provider_ref(self) -> "DataProviderReference":
        '''(experimental) A reference to a DataProvider resource.

        :stability: experimental
        '''
        ...


class _IDataProviderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataProvider.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.IDataProviderRef"

    @builtins.property
    @jsii.member(jsii_name="dataProviderRef")
    def data_provider_ref(self) -> "DataProviderReference":
        '''(experimental) A reference to a DataProvider resource.

        :stability: experimental
        '''
        return typing.cast("DataProviderReference", jsii.get(self, "dataProviderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataProviderRef).__jsii_proxy_class__ = lambda : _IDataProviderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.IEndpointRef")
class IEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Endpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "EndpointReference":
        '''(experimental) A reference to a Endpoint resource.

        :stability: experimental
        '''
        ...


class _IEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Endpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.IEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "EndpointReference":
        '''(experimental) A reference to a Endpoint resource.

        :stability: experimental
        '''
        return typing.cast("EndpointReference", jsii.get(self, "endpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointRef).__jsii_proxy_class__ = lambda : _IEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.IEventSubscriptionRef")
class IEventSubscriptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventSubscription.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventSubscriptionRef")
    def event_subscription_ref(self) -> "EventSubscriptionReference":
        '''(experimental) A reference to a EventSubscription resource.

        :stability: experimental
        '''
        ...


class _IEventSubscriptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventSubscription.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.IEventSubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="eventSubscriptionRef")
    def event_subscription_ref(self) -> "EventSubscriptionReference":
        '''(experimental) A reference to a EventSubscription resource.

        :stability: experimental
        '''
        return typing.cast("EventSubscriptionReference", jsii.get(self, "eventSubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventSubscriptionRef).__jsii_proxy_class__ = lambda : _IEventSubscriptionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.IInstanceProfileRef")
class IInstanceProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceProfileRef")
    def instance_profile_ref(self) -> "InstanceProfileReference":
        '''(experimental) A reference to a InstanceProfile resource.

        :stability: experimental
        '''
        ...


class _IInstanceProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.IInstanceProfileRef"

    @builtins.property
    @jsii.member(jsii_name="instanceProfileRef")
    def instance_profile_ref(self) -> "InstanceProfileReference":
        '''(experimental) A reference to a InstanceProfile resource.

        :stability: experimental
        '''
        return typing.cast("InstanceProfileReference", jsii.get(self, "instanceProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceProfileRef).__jsii_proxy_class__ = lambda : _IInstanceProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.IMigrationProjectRef")
class IMigrationProjectRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MigrationProject.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="migrationProjectRef")
    def migration_project_ref(self) -> "MigrationProjectReference":
        '''(experimental) A reference to a MigrationProject resource.

        :stability: experimental
        '''
        ...


class _IMigrationProjectRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MigrationProject.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.IMigrationProjectRef"

    @builtins.property
    @jsii.member(jsii_name="migrationProjectRef")
    def migration_project_ref(self) -> "MigrationProjectReference":
        '''(experimental) A reference to a MigrationProject resource.

        :stability: experimental
        '''
        return typing.cast("MigrationProjectReference", jsii.get(self, "migrationProjectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMigrationProjectRef).__jsii_proxy_class__ = lambda : _IMigrationProjectRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.IReplicationConfigRef")
class IReplicationConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="replicationConfigRef")
    def replication_config_ref(self) -> "ReplicationConfigReference":
        '''(experimental) A reference to a ReplicationConfig resource.

        :stability: experimental
        '''
        ...


class _IReplicationConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.IReplicationConfigRef"

    @builtins.property
    @jsii.member(jsii_name="replicationConfigRef")
    def replication_config_ref(self) -> "ReplicationConfigReference":
        '''(experimental) A reference to a ReplicationConfig resource.

        :stability: experimental
        '''
        return typing.cast("ReplicationConfigReference", jsii.get(self, "replicationConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReplicationConfigRef).__jsii_proxy_class__ = lambda : _IReplicationConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.IReplicationInstanceRef")
class IReplicationInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceRef")
    def replication_instance_ref(self) -> "ReplicationInstanceReference":
        '''(experimental) A reference to a ReplicationInstance resource.

        :stability: experimental
        '''
        ...


class _IReplicationInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.IReplicationInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceRef")
    def replication_instance_ref(self) -> "ReplicationInstanceReference":
        '''(experimental) A reference to a ReplicationInstance resource.

        :stability: experimental
        '''
        return typing.cast("ReplicationInstanceReference", jsii.get(self, "replicationInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReplicationInstanceRef).__jsii_proxy_class__ = lambda : _IReplicationInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.IReplicationSubnetGroupRef")
class IReplicationSubnetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationSubnetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupRef")
    def replication_subnet_group_ref(self) -> "ReplicationSubnetGroupReference":
        '''(experimental) A reference to a ReplicationSubnetGroup resource.

        :stability: experimental
        '''
        ...


class _IReplicationSubnetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationSubnetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.IReplicationSubnetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupRef")
    def replication_subnet_group_ref(self) -> "ReplicationSubnetGroupReference":
        '''(experimental) A reference to a ReplicationSubnetGroup resource.

        :stability: experimental
        '''
        return typing.cast("ReplicationSubnetGroupReference", jsii.get(self, "replicationSubnetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReplicationSubnetGroupRef).__jsii_proxy_class__ = lambda : _IReplicationSubnetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dms.IReplicationTaskRef")
class IReplicationTaskRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationTask.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="replicationTaskRef")
    def replication_task_ref(self) -> "ReplicationTaskReference":
        '''(experimental) A reference to a ReplicationTask resource.

        :stability: experimental
        '''
        ...


class _IReplicationTaskRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationTask.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dms.IReplicationTaskRef"

    @builtins.property
    @jsii.member(jsii_name="replicationTaskRef")
    def replication_task_ref(self) -> "ReplicationTaskReference":
        '''(experimental) A reference to a ReplicationTask resource.

        :stability: experimental
        '''
        return typing.cast("ReplicationTaskReference", jsii.get(self, "replicationTaskRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReplicationTaskRef).__jsii_proxy_class__ = lambda : _IReplicationTaskRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dms.InstanceProfileReference",
    jsii_struct_bases=[],
    name_mapping={"instance_profile_arn": "instanceProfileArn"},
)
class InstanceProfileReference:
    def __init__(self, *, instance_profile_arn: builtins.str) -> None:
        '''A reference to a InstanceProfile resource.

        :param instance_profile_arn: The InstanceProfileArn of the InstanceProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            instance_profile_reference = interfaces_dms.InstanceProfileReference(
                instance_profile_arn="instanceProfileArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ad79cce0bb086ac777e79c29e51e8cc96f70404e6f03a6e3d173a80e0999bad)
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_profile_arn": instance_profile_arn,
        }

    @builtins.property
    def instance_profile_arn(self) -> builtins.str:
        '''The InstanceProfileArn of the InstanceProfile resource.'''
        result = self._values.get("instance_profile_arn")
        assert result is not None, "Required property 'instance_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dms.MigrationProjectReference",
    jsii_struct_bases=[],
    name_mapping={"migration_project_arn": "migrationProjectArn"},
)
class MigrationProjectReference:
    def __init__(self, *, migration_project_arn: builtins.str) -> None:
        '''A reference to a MigrationProject resource.

        :param migration_project_arn: The MigrationProjectArn of the MigrationProject resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            migration_project_reference = interfaces_dms.MigrationProjectReference(
                migration_project_arn="migrationProjectArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc8a9913b1fcf4ed076942ac157867ddfe027285874dc18c58504cb4e088f278)
            check_type(argname="argument migration_project_arn", value=migration_project_arn, expected_type=type_hints["migration_project_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "migration_project_arn": migration_project_arn,
        }

    @builtins.property
    def migration_project_arn(self) -> builtins.str:
        '''The MigrationProjectArn of the MigrationProject resource.'''
        result = self._values.get("migration_project_arn")
        assert result is not None, "Required property 'migration_project_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MigrationProjectReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dms.ReplicationConfigReference",
    jsii_struct_bases=[],
    name_mapping={"replication_config_arn": "replicationConfigArn"},
)
class ReplicationConfigReference:
    def __init__(self, *, replication_config_arn: builtins.str) -> None:
        '''A reference to a ReplicationConfig resource.

        :param replication_config_arn: The ReplicationConfigArn of the ReplicationConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            replication_config_reference = interfaces_dms.ReplicationConfigReference(
                replication_config_arn="replicationConfigArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fb56c33f244da855425f02482766c202aa4645f2c315245851c9ead4284fb8a)
            check_type(argname="argument replication_config_arn", value=replication_config_arn, expected_type=type_hints["replication_config_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_config_arn": replication_config_arn,
        }

    @builtins.property
    def replication_config_arn(self) -> builtins.str:
        '''The ReplicationConfigArn of the ReplicationConfig resource.'''
        result = self._values.get("replication_config_arn")
        assert result is not None, "Required property 'replication_config_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicationConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dms.ReplicationInstanceReference",
    jsii_struct_bases=[],
    name_mapping={"replication_instance_id": "replicationInstanceId"},
)
class ReplicationInstanceReference:
    def __init__(self, *, replication_instance_id: builtins.str) -> None:
        '''A reference to a ReplicationInstance resource.

        :param replication_instance_id: The Id of the ReplicationInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            replication_instance_reference = interfaces_dms.ReplicationInstanceReference(
                replication_instance_id="replicationInstanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b41cdc31c0ea172c3879c0deb65a6a9b70b9f824f53d77389b4c9d272a2f37ce)
            check_type(argname="argument replication_instance_id", value=replication_instance_id, expected_type=type_hints["replication_instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_instance_id": replication_instance_id,
        }

    @builtins.property
    def replication_instance_id(self) -> builtins.str:
        '''The Id of the ReplicationInstance resource.'''
        result = self._values.get("replication_instance_id")
        assert result is not None, "Required property 'replication_instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicationInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dms.ReplicationSubnetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"replication_subnet_group_id": "replicationSubnetGroupId"},
)
class ReplicationSubnetGroupReference:
    def __init__(self, *, replication_subnet_group_id: builtins.str) -> None:
        '''A reference to a ReplicationSubnetGroup resource.

        :param replication_subnet_group_id: The Id of the ReplicationSubnetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            replication_subnet_group_reference = interfaces_dms.ReplicationSubnetGroupReference(
                replication_subnet_group_id="replicationSubnetGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc5d133dd09a422b7b86d14f260b9aff35300fe810630d9349a741a5ec07733d)
            check_type(argname="argument replication_subnet_group_id", value=replication_subnet_group_id, expected_type=type_hints["replication_subnet_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_subnet_group_id": replication_subnet_group_id,
        }

    @builtins.property
    def replication_subnet_group_id(self) -> builtins.str:
        '''The Id of the ReplicationSubnetGroup resource.'''
        result = self._values.get("replication_subnet_group_id")
        assert result is not None, "Required property 'replication_subnet_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicationSubnetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dms.ReplicationTaskReference",
    jsii_struct_bases=[],
    name_mapping={"replication_task_id": "replicationTaskId"},
)
class ReplicationTaskReference:
    def __init__(self, *, replication_task_id: builtins.str) -> None:
        '''A reference to a ReplicationTask resource.

        :param replication_task_id: The Id of the ReplicationTask resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dms as interfaces_dms
            
            replication_task_reference = interfaces_dms.ReplicationTaskReference(
                replication_task_id="replicationTaskId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__058318f539698ef8b693c781ecb998f9619364d8e8b86a247f3ed3aa44bd537b)
            check_type(argname="argument replication_task_id", value=replication_task_id, expected_type=type_hints["replication_task_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_task_id": replication_task_id,
        }

    @builtins.property
    def replication_task_id(self) -> builtins.str:
        '''The Id of the ReplicationTask resource.'''
        result = self._values.get("replication_task_id")
        assert result is not None, "Required property 'replication_task_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicationTaskReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CertificateReference",
    "DataMigrationReference",
    "DataProviderReference",
    "EndpointReference",
    "EventSubscriptionReference",
    "ICertificateRef",
    "IDataMigrationRef",
    "IDataProviderRef",
    "IEndpointRef",
    "IEventSubscriptionRef",
    "IInstanceProfileRef",
    "IMigrationProjectRef",
    "IReplicationConfigRef",
    "IReplicationInstanceRef",
    "IReplicationSubnetGroupRef",
    "IReplicationTaskRef",
    "InstanceProfileReference",
    "MigrationProjectReference",
    "ReplicationConfigReference",
    "ReplicationInstanceReference",
    "ReplicationSubnetGroupReference",
    "ReplicationTaskReference",
]

publication.publish()

def _typecheckingstub__dddbb2d150dcddbead74d31a5ed63e027a36c883e3adff1a6625fb7bf556ba97(
    *,
    certificate_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7ce32da77e89591c1e645a63211fb840843830d36317162cdaeb7c245a833fc(
    *,
    data_migration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__538ed4e8d5aaca3877a044998ac0a9f566f87cf7e0155ab9c32b465fb4eec685(
    *,
    data_provider_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bacd7fb4a98e49b4d9cba342b46e91b7d78d2478a75083429d89359bedf9c098(
    *,
    endpoint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e10f1fa5fdaaffb8747b447030f241bdfa52238714c1ac890118f7dccdb0da41(
    *,
    subscription_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ad79cce0bb086ac777e79c29e51e8cc96f70404e6f03a6e3d173a80e0999bad(
    *,
    instance_profile_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc8a9913b1fcf4ed076942ac157867ddfe027285874dc18c58504cb4e088f278(
    *,
    migration_project_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fb56c33f244da855425f02482766c202aa4645f2c315245851c9ead4284fb8a(
    *,
    replication_config_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b41cdc31c0ea172c3879c0deb65a6a9b70b9f824f53d77389b4c9d272a2f37ce(
    *,
    replication_instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc5d133dd09a422b7b86d14f260b9aff35300fe810630d9349a741a5ec07733d(
    *,
    replication_subnet_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__058318f539698ef8b693c781ecb998f9619364d8e8b86a247f3ed3aa44bd537b(
    *,
    replication_task_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICertificateRef, IDataMigrationRef, IDataProviderRef, IEndpointRef, IEventSubscriptionRef, IInstanceProfileRef, IMigrationProjectRef, IReplicationConfigRef, IReplicationInstanceRef, IReplicationSubnetGroupRef, IReplicationTaskRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
