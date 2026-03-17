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
    jsii_type="aws-cdk-lib.interfaces.aws_neptune.DBClusterParameterGroupReference",
    jsii_struct_bases=[],
    name_mapping={"db_cluster_parameter_group_name": "dbClusterParameterGroupName"},
)
class DBClusterParameterGroupReference:
    def __init__(self, *, db_cluster_parameter_group_name: builtins.str) -> None:
        '''A reference to a DBClusterParameterGroup resource.

        :param db_cluster_parameter_group_name: The Name of the DBClusterParameterGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_neptune as interfaces_neptune
            
            d_bCluster_parameter_group_reference = interfaces_neptune.DBClusterParameterGroupReference(
                db_cluster_parameter_group_name="dbClusterParameterGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d247a16ac17259a27b6f94fe3380e6af442c02299cc0c72a99bfe924c468bc25)
            check_type(argname="argument db_cluster_parameter_group_name", value=db_cluster_parameter_group_name, expected_type=type_hints["db_cluster_parameter_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_cluster_parameter_group_name": db_cluster_parameter_group_name,
        }

    @builtins.property
    def db_cluster_parameter_group_name(self) -> builtins.str:
        '''The Name of the DBClusterParameterGroup resource.'''
        result = self._values.get("db_cluster_parameter_group_name")
        assert result is not None, "Required property 'db_cluster_parameter_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBClusterParameterGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_neptune.DBClusterReference",
    jsii_struct_bases=[],
    name_mapping={"db_cluster_identifier": "dbClusterIdentifier"},
)
class DBClusterReference:
    def __init__(self, *, db_cluster_identifier: builtins.str) -> None:
        '''A reference to a DBCluster resource.

        :param db_cluster_identifier: The DBClusterIdentifier of the DBCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_neptune as interfaces_neptune
            
            d_bCluster_reference = interfaces_neptune.DBClusterReference(
                db_cluster_identifier="dbClusterIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__710f24b62ecafdac142c5e51eaa009e94698414d5fc8dfc9c3e2e2762681a471)
            check_type(argname="argument db_cluster_identifier", value=db_cluster_identifier, expected_type=type_hints["db_cluster_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_cluster_identifier": db_cluster_identifier,
        }

    @builtins.property
    def db_cluster_identifier(self) -> builtins.str:
        '''The DBClusterIdentifier of the DBCluster resource.'''
        result = self._values.get("db_cluster_identifier")
        assert result is not None, "Required property 'db_cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_neptune.DBInstanceReference",
    jsii_struct_bases=[],
    name_mapping={"db_instance_identifier": "dbInstanceIdentifier"},
)
class DBInstanceReference:
    def __init__(self, *, db_instance_identifier: builtins.str) -> None:
        '''A reference to a DBInstance resource.

        :param db_instance_identifier: The DBInstanceIdentifier of the DBInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_neptune as interfaces_neptune
            
            d_bInstance_reference = interfaces_neptune.DBInstanceReference(
                db_instance_identifier="dbInstanceIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f4d8f92720f7e70de17539a7aeb47470136a22ef266d8994e4ff6fa5cf17d8a)
            check_type(argname="argument db_instance_identifier", value=db_instance_identifier, expected_type=type_hints["db_instance_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_instance_identifier": db_instance_identifier,
        }

    @builtins.property
    def db_instance_identifier(self) -> builtins.str:
        '''The DBInstanceIdentifier of the DBInstance resource.'''
        result = self._values.get("db_instance_identifier")
        assert result is not None, "Required property 'db_instance_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_neptune.DBParameterGroupReference",
    jsii_struct_bases=[],
    name_mapping={"db_parameter_group_name": "dbParameterGroupName"},
)
class DBParameterGroupReference:
    def __init__(self, *, db_parameter_group_name: builtins.str) -> None:
        '''A reference to a DBParameterGroup resource.

        :param db_parameter_group_name: The Name of the DBParameterGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_neptune as interfaces_neptune
            
            d_bParameter_group_reference = interfaces_neptune.DBParameterGroupReference(
                db_parameter_group_name="dbParameterGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1c8ddf236cd1a7709785a6ee0ba8b1cc255155518038144bfa013f5d5ad9878)
            check_type(argname="argument db_parameter_group_name", value=db_parameter_group_name, expected_type=type_hints["db_parameter_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_parameter_group_name": db_parameter_group_name,
        }

    @builtins.property
    def db_parameter_group_name(self) -> builtins.str:
        '''The Name of the DBParameterGroup resource.'''
        result = self._values.get("db_parameter_group_name")
        assert result is not None, "Required property 'db_parameter_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBParameterGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_neptune.DBSubnetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"db_subnet_group_name": "dbSubnetGroupName"},
)
class DBSubnetGroupReference:
    def __init__(self, *, db_subnet_group_name: builtins.str) -> None:
        '''A reference to a DBSubnetGroup resource.

        :param db_subnet_group_name: The DBSubnetGroupName of the DBSubnetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_neptune as interfaces_neptune
            
            d_bSubnet_group_reference = interfaces_neptune.DBSubnetGroupReference(
                db_subnet_group_name="dbSubnetGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afa7de6888cc0674082ebe6f459471f8b000a05772a528eb8da77594564a1d1e)
            check_type(argname="argument db_subnet_group_name", value=db_subnet_group_name, expected_type=type_hints["db_subnet_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_subnet_group_name": db_subnet_group_name,
        }

    @builtins.property
    def db_subnet_group_name(self) -> builtins.str:
        '''The DBSubnetGroupName of the DBSubnetGroup resource.'''
        result = self._values.get("db_subnet_group_name")
        assert result is not None, "Required property 'db_subnet_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DBSubnetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_neptune.EventSubscriptionReference",
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
            from aws_cdk.interfaces import aws_neptune as interfaces_neptune
            
            event_subscription_reference = interfaces_neptune.EventSubscriptionReference(
                subscription_name="subscriptionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa78d3296c26fc5ac60f282fd40f63ee64ea2004d5591ae85bc615aaf18c9e7c)
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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_neptune.IDBClusterParameterGroupRef"
)
class IDBClusterParameterGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBClusterParameterGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbClusterParameterGroupRef")
    def db_cluster_parameter_group_ref(self) -> "DBClusterParameterGroupReference":
        '''(experimental) A reference to a DBClusterParameterGroup resource.

        :stability: experimental
        '''
        ...


class _IDBClusterParameterGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBClusterParameterGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_neptune.IDBClusterParameterGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbClusterParameterGroupRef")
    def db_cluster_parameter_group_ref(self) -> "DBClusterParameterGroupReference":
        '''(experimental) A reference to a DBClusterParameterGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBClusterParameterGroupReference", jsii.get(self, "dbClusterParameterGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBClusterParameterGroupRef).__jsii_proxy_class__ = lambda : _IDBClusterParameterGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_neptune.IDBClusterRef")
class IDBClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbClusterRef")
    def db_cluster_ref(self) -> "DBClusterReference":
        '''(experimental) A reference to a DBCluster resource.

        :stability: experimental
        '''
        ...


class _IDBClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_neptune.IDBClusterRef"

    @builtins.property
    @jsii.member(jsii_name="dbClusterRef")
    def db_cluster_ref(self) -> "DBClusterReference":
        '''(experimental) A reference to a DBCluster resource.

        :stability: experimental
        '''
        return typing.cast("DBClusterReference", jsii.get(self, "dbClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBClusterRef).__jsii_proxy_class__ = lambda : _IDBClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_neptune.IDBInstanceRef")
class IDBInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbInstanceRef")
    def db_instance_ref(self) -> "DBInstanceReference":
        '''(experimental) A reference to a DBInstance resource.

        :stability: experimental
        '''
        ...


class _IDBInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_neptune.IDBInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="dbInstanceRef")
    def db_instance_ref(self) -> "DBInstanceReference":
        '''(experimental) A reference to a DBInstance resource.

        :stability: experimental
        '''
        return typing.cast("DBInstanceReference", jsii.get(self, "dbInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBInstanceRef).__jsii_proxy_class__ = lambda : _IDBInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_neptune.IDBParameterGroupRef")
class IDBParameterGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBParameterGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbParameterGroupRef")
    def db_parameter_group_ref(self) -> "DBParameterGroupReference":
        '''(experimental) A reference to a DBParameterGroup resource.

        :stability: experimental
        '''
        ...


class _IDBParameterGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBParameterGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_neptune.IDBParameterGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbParameterGroupRef")
    def db_parameter_group_ref(self) -> "DBParameterGroupReference":
        '''(experimental) A reference to a DBParameterGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBParameterGroupReference", jsii.get(self, "dbParameterGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBParameterGroupRef).__jsii_proxy_class__ = lambda : _IDBParameterGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_neptune.IDBSubnetGroupRef")
class IDBSubnetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DBSubnetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupRef")
    def db_subnet_group_ref(self) -> "DBSubnetGroupReference":
        '''(experimental) A reference to a DBSubnetGroup resource.

        :stability: experimental
        '''
        ...


class _IDBSubnetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DBSubnetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_neptune.IDBSubnetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupRef")
    def db_subnet_group_ref(self) -> "DBSubnetGroupReference":
        '''(experimental) A reference to a DBSubnetGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBSubnetGroupReference", jsii.get(self, "dbSubnetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBSubnetGroupRef).__jsii_proxy_class__ = lambda : _IDBSubnetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_neptune.IEventSubscriptionRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_neptune.IEventSubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="eventSubscriptionRef")
    def event_subscription_ref(self) -> "EventSubscriptionReference":
        '''(experimental) A reference to a EventSubscription resource.

        :stability: experimental
        '''
        return typing.cast("EventSubscriptionReference", jsii.get(self, "eventSubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventSubscriptionRef).__jsii_proxy_class__ = lambda : _IEventSubscriptionRefProxy


__all__ = [
    "DBClusterParameterGroupReference",
    "DBClusterReference",
    "DBInstanceReference",
    "DBParameterGroupReference",
    "DBSubnetGroupReference",
    "EventSubscriptionReference",
    "IDBClusterParameterGroupRef",
    "IDBClusterRef",
    "IDBInstanceRef",
    "IDBParameterGroupRef",
    "IDBSubnetGroupRef",
    "IEventSubscriptionRef",
]

publication.publish()

def _typecheckingstub__d247a16ac17259a27b6f94fe3380e6af442c02299cc0c72a99bfe924c468bc25(
    *,
    db_cluster_parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__710f24b62ecafdac142c5e51eaa009e94698414d5fc8dfc9c3e2e2762681a471(
    *,
    db_cluster_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f4d8f92720f7e70de17539a7aeb47470136a22ef266d8994e4ff6fa5cf17d8a(
    *,
    db_instance_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1c8ddf236cd1a7709785a6ee0ba8b1cc255155518038144bfa013f5d5ad9878(
    *,
    db_parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa7de6888cc0674082ebe6f459471f8b000a05772a528eb8da77594564a1d1e(
    *,
    db_subnet_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa78d3296c26fc5ac60f282fd40f63ee64ea2004d5591ae85bc615aaf18c9e7c(
    *,
    subscription_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDBClusterParameterGroupRef, IDBClusterRef, IDBInstanceRef, IDBParameterGroupRef, IDBSubnetGroupRef, IEventSubscriptionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
