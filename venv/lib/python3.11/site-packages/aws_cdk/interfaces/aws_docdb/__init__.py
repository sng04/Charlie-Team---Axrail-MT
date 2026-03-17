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
    jsii_type="aws-cdk-lib.interfaces.aws_docdb.DBClusterParameterGroupReference",
    jsii_struct_bases=[],
    name_mapping={"db_cluster_parameter_group_id": "dbClusterParameterGroupId"},
)
class DBClusterParameterGroupReference:
    def __init__(self, *, db_cluster_parameter_group_id: builtins.str) -> None:
        '''A reference to a DBClusterParameterGroup resource.

        :param db_cluster_parameter_group_id: The Id of the DBClusterParameterGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_docdb as interfaces_docdb
            
            d_bCluster_parameter_group_reference = interfaces_docdb.DBClusterParameterGroupReference(
                db_cluster_parameter_group_id="dbClusterParameterGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59ad0ed86fca2825742e2479fd25a959020db5a0431b40c09e95b63413733fd1)
            check_type(argname="argument db_cluster_parameter_group_id", value=db_cluster_parameter_group_id, expected_type=type_hints["db_cluster_parameter_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_cluster_parameter_group_id": db_cluster_parameter_group_id,
        }

    @builtins.property
    def db_cluster_parameter_group_id(self) -> builtins.str:
        '''The Id of the DBClusterParameterGroup resource.'''
        result = self._values.get("db_cluster_parameter_group_id")
        assert result is not None, "Required property 'db_cluster_parameter_group_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_docdb.DBClusterReference",
    jsii_struct_bases=[],
    name_mapping={"db_cluster_id": "dbClusterId"},
)
class DBClusterReference:
    def __init__(self, *, db_cluster_id: builtins.str) -> None:
        '''A reference to a DBCluster resource.

        :param db_cluster_id: The Id of the DBCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_docdb as interfaces_docdb
            
            d_bCluster_reference = interfaces_docdb.DBClusterReference(
                db_cluster_id="dbClusterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__682bd00486326ecd041d29352c5dcd0a2abf9cf2c96bf5a89e0fe205afefb73f)
            check_type(argname="argument db_cluster_id", value=db_cluster_id, expected_type=type_hints["db_cluster_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_cluster_id": db_cluster_id,
        }

    @builtins.property
    def db_cluster_id(self) -> builtins.str:
        '''The Id of the DBCluster resource.'''
        result = self._values.get("db_cluster_id")
        assert result is not None, "Required property 'db_cluster_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_docdb.DBInstanceReference",
    jsii_struct_bases=[],
    name_mapping={"db_instance_id": "dbInstanceId"},
)
class DBInstanceReference:
    def __init__(self, *, db_instance_id: builtins.str) -> None:
        '''A reference to a DBInstance resource.

        :param db_instance_id: The Id of the DBInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_docdb as interfaces_docdb
            
            d_bInstance_reference = interfaces_docdb.DBInstanceReference(
                db_instance_id="dbInstanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c13d32d14b52ba9e057053cdb7c67f20d9d269dab44a4960780f1c37ef94d63a)
            check_type(argname="argument db_instance_id", value=db_instance_id, expected_type=type_hints["db_instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_instance_id": db_instance_id,
        }

    @builtins.property
    def db_instance_id(self) -> builtins.str:
        '''The Id of the DBInstance resource.'''
        result = self._values.get("db_instance_id")
        assert result is not None, "Required property 'db_instance_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_docdb.DBSubnetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"db_subnet_group_id": "dbSubnetGroupId"},
)
class DBSubnetGroupReference:
    def __init__(self, *, db_subnet_group_id: builtins.str) -> None:
        '''A reference to a DBSubnetGroup resource.

        :param db_subnet_group_id: The Id of the DBSubnetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_docdb as interfaces_docdb
            
            d_bSubnet_group_reference = interfaces_docdb.DBSubnetGroupReference(
                db_subnet_group_id="dbSubnetGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed49d8d68c7ea117d936be5f042ed3494a607b7eef69ae511b442f6c345e85f8)
            check_type(argname="argument db_subnet_group_id", value=db_subnet_group_id, expected_type=type_hints["db_subnet_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "db_subnet_group_id": db_subnet_group_id,
        }

    @builtins.property
    def db_subnet_group_id(self) -> builtins.str:
        '''The Id of the DBSubnetGroup resource.'''
        result = self._values.get("db_subnet_group_id")
        assert result is not None, "Required property 'db_subnet_group_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_docdb.EventSubscriptionReference",
    jsii_struct_bases=[],
    name_mapping={"event_subscription_id": "eventSubscriptionId"},
)
class EventSubscriptionReference:
    def __init__(self, *, event_subscription_id: builtins.str) -> None:
        '''A reference to a EventSubscription resource.

        :param event_subscription_id: The Id of the EventSubscription resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_docdb as interfaces_docdb
            
            event_subscription_reference = interfaces_docdb.EventSubscriptionReference(
                event_subscription_id="eventSubscriptionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d1757a2d0c92dd54faf578c5eecb7a2d61d57c75b45c13f8d31e21cf8f37f3)
            check_type(argname="argument event_subscription_id", value=event_subscription_id, expected_type=type_hints["event_subscription_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_subscription_id": event_subscription_id,
        }

    @builtins.property
    def event_subscription_id(self) -> builtins.str:
        '''The Id of the EventSubscription resource.'''
        result = self._values.get("event_subscription_id")
        assert result is not None, "Required property 'event_subscription_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventSubscriptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_docdb.GlobalClusterReference",
    jsii_struct_bases=[],
    name_mapping={
        "global_cluster_arn": "globalClusterArn",
        "global_cluster_identifier": "globalClusterIdentifier",
    },
)
class GlobalClusterReference:
    def __init__(
        self,
        *,
        global_cluster_arn: builtins.str,
        global_cluster_identifier: builtins.str,
    ) -> None:
        '''A reference to a GlobalCluster resource.

        :param global_cluster_arn: The ARN of the GlobalCluster resource.
        :param global_cluster_identifier: The GlobalClusterIdentifier of the GlobalCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_docdb as interfaces_docdb
            
            global_cluster_reference = interfaces_docdb.GlobalClusterReference(
                global_cluster_arn="globalClusterArn",
                global_cluster_identifier="globalClusterIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f4b6750c1d1f170fb4cb1010269a7c82a1590cfb80511cdc32f1dc9f14423d9)
            check_type(argname="argument global_cluster_arn", value=global_cluster_arn, expected_type=type_hints["global_cluster_arn"])
            check_type(argname="argument global_cluster_identifier", value=global_cluster_identifier, expected_type=type_hints["global_cluster_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_cluster_arn": global_cluster_arn,
            "global_cluster_identifier": global_cluster_identifier,
        }

    @builtins.property
    def global_cluster_arn(self) -> builtins.str:
        '''The ARN of the GlobalCluster resource.'''
        result = self._values.get("global_cluster_arn")
        assert result is not None, "Required property 'global_cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def global_cluster_identifier(self) -> builtins.str:
        '''The GlobalClusterIdentifier of the GlobalCluster resource.'''
        result = self._values.get("global_cluster_identifier")
        assert result is not None, "Required property 'global_cluster_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlobalClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_docdb.IDBClusterParameterGroupRef"
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_docdb.IDBClusterParameterGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbClusterParameterGroupRef")
    def db_cluster_parameter_group_ref(self) -> "DBClusterParameterGroupReference":
        '''(experimental) A reference to a DBClusterParameterGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBClusterParameterGroupReference", jsii.get(self, "dbClusterParameterGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBClusterParameterGroupRef).__jsii_proxy_class__ = lambda : _IDBClusterParameterGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_docdb.IDBClusterRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_docdb.IDBClusterRef"

    @builtins.property
    @jsii.member(jsii_name="dbClusterRef")
    def db_cluster_ref(self) -> "DBClusterReference":
        '''(experimental) A reference to a DBCluster resource.

        :stability: experimental
        '''
        return typing.cast("DBClusterReference", jsii.get(self, "dbClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBClusterRef).__jsii_proxy_class__ = lambda : _IDBClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_docdb.IDBInstanceRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_docdb.IDBInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="dbInstanceRef")
    def db_instance_ref(self) -> "DBInstanceReference":
        '''(experimental) A reference to a DBInstance resource.

        :stability: experimental
        '''
        return typing.cast("DBInstanceReference", jsii.get(self, "dbInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBInstanceRef).__jsii_proxy_class__ = lambda : _IDBInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_docdb.IDBSubnetGroupRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_docdb.IDBSubnetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dbSubnetGroupRef")
    def db_subnet_group_ref(self) -> "DBSubnetGroupReference":
        '''(experimental) A reference to a DBSubnetGroup resource.

        :stability: experimental
        '''
        return typing.cast("DBSubnetGroupReference", jsii.get(self, "dbSubnetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDBSubnetGroupRef).__jsii_proxy_class__ = lambda : _IDBSubnetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_docdb.IEventSubscriptionRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_docdb.IEventSubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="eventSubscriptionRef")
    def event_subscription_ref(self) -> "EventSubscriptionReference":
        '''(experimental) A reference to a EventSubscription resource.

        :stability: experimental
        '''
        return typing.cast("EventSubscriptionReference", jsii.get(self, "eventSubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventSubscriptionRef).__jsii_proxy_class__ = lambda : _IEventSubscriptionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_docdb.IGlobalClusterRef")
class IGlobalClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="globalClusterRef")
    def global_cluster_ref(self) -> "GlobalClusterReference":
        '''(experimental) A reference to a GlobalCluster resource.

        :stability: experimental
        '''
        ...


class _IGlobalClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_docdb.IGlobalClusterRef"

    @builtins.property
    @jsii.member(jsii_name="globalClusterRef")
    def global_cluster_ref(self) -> "GlobalClusterReference":
        '''(experimental) A reference to a GlobalCluster resource.

        :stability: experimental
        '''
        return typing.cast("GlobalClusterReference", jsii.get(self, "globalClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGlobalClusterRef).__jsii_proxy_class__ = lambda : _IGlobalClusterRefProxy


__all__ = [
    "DBClusterParameterGroupReference",
    "DBClusterReference",
    "DBInstanceReference",
    "DBSubnetGroupReference",
    "EventSubscriptionReference",
    "GlobalClusterReference",
    "IDBClusterParameterGroupRef",
    "IDBClusterRef",
    "IDBInstanceRef",
    "IDBSubnetGroupRef",
    "IEventSubscriptionRef",
    "IGlobalClusterRef",
]

publication.publish()

def _typecheckingstub__59ad0ed86fca2825742e2479fd25a959020db5a0431b40c09e95b63413733fd1(
    *,
    db_cluster_parameter_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682bd00486326ecd041d29352c5dcd0a2abf9cf2c96bf5a89e0fe205afefb73f(
    *,
    db_cluster_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c13d32d14b52ba9e057053cdb7c67f20d9d269dab44a4960780f1c37ef94d63a(
    *,
    db_instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed49d8d68c7ea117d936be5f042ed3494a607b7eef69ae511b442f6c345e85f8(
    *,
    db_subnet_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d1757a2d0c92dd54faf578c5eecb7a2d61d57c75b45c13f8d31e21cf8f37f3(
    *,
    event_subscription_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f4b6750c1d1f170fb4cb1010269a7c82a1590cfb80511cdc32f1dc9f14423d9(
    *,
    global_cluster_arn: builtins.str,
    global_cluster_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDBClusterParameterGroupRef, IDBClusterRef, IDBInstanceRef, IDBSubnetGroupRef, IEventSubscriptionRef, IGlobalClusterRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
