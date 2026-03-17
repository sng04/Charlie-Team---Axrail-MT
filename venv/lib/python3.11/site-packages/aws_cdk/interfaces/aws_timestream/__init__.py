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
    jsii_type="aws-cdk-lib.interfaces.aws_timestream.DatabaseReference",
    jsii_struct_bases=[],
    name_mapping={"database_arn": "databaseArn", "database_name": "databaseName"},
)
class DatabaseReference:
    def __init__(
        self,
        *,
        database_arn: builtins.str,
        database_name: builtins.str,
    ) -> None:
        '''A reference to a Database resource.

        :param database_arn: The ARN of the Database resource.
        :param database_name: The DatabaseName of the Database resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_timestream as interfaces_timestream
            
            database_reference = interfaces_timestream.DatabaseReference(
                database_arn="databaseArn",
                database_name="databaseName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f77d2bae58103bc359e516b09f6a3553472665a4ec6b584e2a0a662b39572a3a)
            check_type(argname="argument database_arn", value=database_arn, expected_type=type_hints["database_arn"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_arn": database_arn,
            "database_name": database_name,
        }

    @builtins.property
    def database_arn(self) -> builtins.str:
        '''The ARN of the Database resource.'''
        result = self._values.get("database_arn")
        assert result is not None, "Required property 'database_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The DatabaseName of the Database resource.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_timestream.IDatabaseRef")
class IDatabaseRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Database.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="databaseRef")
    def database_ref(self) -> "DatabaseReference":
        '''(experimental) A reference to a Database resource.

        :stability: experimental
        '''
        ...


class _IDatabaseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Database.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_timestream.IDatabaseRef"

    @builtins.property
    @jsii.member(jsii_name="databaseRef")
    def database_ref(self) -> "DatabaseReference":
        '''(experimental) A reference to a Database resource.

        :stability: experimental
        '''
        return typing.cast("DatabaseReference", jsii.get(self, "databaseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseRef).__jsii_proxy_class__ = lambda : _IDatabaseRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_timestream.IInfluxDBClusterRef")
class IInfluxDBClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InfluxDBCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="influxDbClusterRef")
    def influx_db_cluster_ref(self) -> "InfluxDBClusterReference":
        '''(experimental) A reference to a InfluxDBCluster resource.

        :stability: experimental
        '''
        ...


class _IInfluxDBClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InfluxDBCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_timestream.IInfluxDBClusterRef"

    @builtins.property
    @jsii.member(jsii_name="influxDbClusterRef")
    def influx_db_cluster_ref(self) -> "InfluxDBClusterReference":
        '''(experimental) A reference to a InfluxDBCluster resource.

        :stability: experimental
        '''
        return typing.cast("InfluxDBClusterReference", jsii.get(self, "influxDbClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInfluxDBClusterRef).__jsii_proxy_class__ = lambda : _IInfluxDBClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_timestream.IInfluxDBInstanceRef")
class IInfluxDBInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InfluxDBInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="influxDbInstanceRef")
    def influx_db_instance_ref(self) -> "InfluxDBInstanceReference":
        '''(experimental) A reference to a InfluxDBInstance resource.

        :stability: experimental
        '''
        ...


class _IInfluxDBInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InfluxDBInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_timestream.IInfluxDBInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="influxDbInstanceRef")
    def influx_db_instance_ref(self) -> "InfluxDBInstanceReference":
        '''(experimental) A reference to a InfluxDBInstance resource.

        :stability: experimental
        '''
        return typing.cast("InfluxDBInstanceReference", jsii.get(self, "influxDbInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInfluxDBInstanceRef).__jsii_proxy_class__ = lambda : _IInfluxDBInstanceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_timestream.IScheduledQueryRef")
class IScheduledQueryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduledQuery.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scheduledQueryRef")
    def scheduled_query_ref(self) -> "ScheduledQueryReference":
        '''(experimental) A reference to a ScheduledQuery resource.

        :stability: experimental
        '''
        ...


class _IScheduledQueryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduledQuery.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_timestream.IScheduledQueryRef"

    @builtins.property
    @jsii.member(jsii_name="scheduledQueryRef")
    def scheduled_query_ref(self) -> "ScheduledQueryReference":
        '''(experimental) A reference to a ScheduledQuery resource.

        :stability: experimental
        '''
        return typing.cast("ScheduledQueryReference", jsii.get(self, "scheduledQueryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScheduledQueryRef).__jsii_proxy_class__ = lambda : _IScheduledQueryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_timestream.ITableRef")
class ITableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Table.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tableRef")
    def table_ref(self) -> "TableReference":
        '''(experimental) A reference to a Table resource.

        :stability: experimental
        '''
        ...


class _ITableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Table.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_timestream.ITableRef"

    @builtins.property
    @jsii.member(jsii_name="tableRef")
    def table_ref(self) -> "TableReference":
        '''(experimental) A reference to a Table resource.

        :stability: experimental
        '''
        return typing.cast("TableReference", jsii.get(self, "tableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITableRef).__jsii_proxy_class__ = lambda : _ITableRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_timestream.InfluxDBClusterReference",
    jsii_struct_bases=[],
    name_mapping={
        "influx_db_cluster_arn": "influxDbClusterArn",
        "influx_db_cluster_id": "influxDbClusterId",
    },
)
class InfluxDBClusterReference:
    def __init__(
        self,
        *,
        influx_db_cluster_arn: builtins.str,
        influx_db_cluster_id: builtins.str,
    ) -> None:
        '''A reference to a InfluxDBCluster resource.

        :param influx_db_cluster_arn: The ARN of the InfluxDBCluster resource.
        :param influx_db_cluster_id: The Id of the InfluxDBCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_timestream as interfaces_timestream
            
            influx_dBCluster_reference = interfaces_timestream.InfluxDBClusterReference(
                influx_db_cluster_arn="influxDbClusterArn",
                influx_db_cluster_id="influxDbClusterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71b0ab1bc40e1d98c240e3df814cb220ae4647f1ec01dd4c7332cc4aea76a2cc)
            check_type(argname="argument influx_db_cluster_arn", value=influx_db_cluster_arn, expected_type=type_hints["influx_db_cluster_arn"])
            check_type(argname="argument influx_db_cluster_id", value=influx_db_cluster_id, expected_type=type_hints["influx_db_cluster_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "influx_db_cluster_arn": influx_db_cluster_arn,
            "influx_db_cluster_id": influx_db_cluster_id,
        }

    @builtins.property
    def influx_db_cluster_arn(self) -> builtins.str:
        '''The ARN of the InfluxDBCluster resource.'''
        result = self._values.get("influx_db_cluster_arn")
        assert result is not None, "Required property 'influx_db_cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def influx_db_cluster_id(self) -> builtins.str:
        '''The Id of the InfluxDBCluster resource.'''
        result = self._values.get("influx_db_cluster_id")
        assert result is not None, "Required property 'influx_db_cluster_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InfluxDBClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_timestream.InfluxDBInstanceReference",
    jsii_struct_bases=[],
    name_mapping={
        "influx_db_instance_arn": "influxDbInstanceArn",
        "influx_db_instance_id": "influxDbInstanceId",
    },
)
class InfluxDBInstanceReference:
    def __init__(
        self,
        *,
        influx_db_instance_arn: builtins.str,
        influx_db_instance_id: builtins.str,
    ) -> None:
        '''A reference to a InfluxDBInstance resource.

        :param influx_db_instance_arn: The ARN of the InfluxDBInstance resource.
        :param influx_db_instance_id: The Id of the InfluxDBInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_timestream as interfaces_timestream
            
            influx_dBInstance_reference = interfaces_timestream.InfluxDBInstanceReference(
                influx_db_instance_arn="influxDbInstanceArn",
                influx_db_instance_id="influxDbInstanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__397aac9d607a62cab6b8bdf7168b8cfb1607a2534996567b166ee4714911de27)
            check_type(argname="argument influx_db_instance_arn", value=influx_db_instance_arn, expected_type=type_hints["influx_db_instance_arn"])
            check_type(argname="argument influx_db_instance_id", value=influx_db_instance_id, expected_type=type_hints["influx_db_instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "influx_db_instance_arn": influx_db_instance_arn,
            "influx_db_instance_id": influx_db_instance_id,
        }

    @builtins.property
    def influx_db_instance_arn(self) -> builtins.str:
        '''The ARN of the InfluxDBInstance resource.'''
        result = self._values.get("influx_db_instance_arn")
        assert result is not None, "Required property 'influx_db_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def influx_db_instance_id(self) -> builtins.str:
        '''The Id of the InfluxDBInstance resource.'''
        result = self._values.get("influx_db_instance_id")
        assert result is not None, "Required property 'influx_db_instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InfluxDBInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_timestream.ScheduledQueryReference",
    jsii_struct_bases=[],
    name_mapping={"scheduled_query_arn": "scheduledQueryArn"},
)
class ScheduledQueryReference:
    def __init__(self, *, scheduled_query_arn: builtins.str) -> None:
        '''A reference to a ScheduledQuery resource.

        :param scheduled_query_arn: The Arn of the ScheduledQuery resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_timestream as interfaces_timestream
            
            scheduled_query_reference = interfaces_timestream.ScheduledQueryReference(
                scheduled_query_arn="scheduledQueryArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcdcdbf31574908e2756c1d04b734baf4db0eca0f10b8ac19aaa61992b78d6d8)
            check_type(argname="argument scheduled_query_arn", value=scheduled_query_arn, expected_type=type_hints["scheduled_query_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scheduled_query_arn": scheduled_query_arn,
        }

    @builtins.property
    def scheduled_query_arn(self) -> builtins.str:
        '''The Arn of the ScheduledQuery resource.'''
        result = self._values.get("scheduled_query_arn")
        assert result is not None, "Required property 'scheduled_query_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduledQueryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_timestream.TableReference",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "table_arn": "tableArn",
        "table_name": "tableName",
    },
)
class TableReference:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        table_arn: builtins.str,
        table_name: builtins.str,
    ) -> None:
        '''A reference to a Table resource.

        :param database_name: The DatabaseName of the Table resource.
        :param table_arn: The ARN of the Table resource.
        :param table_name: The TableName of the Table resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_timestream as interfaces_timestream
            
            table_reference = interfaces_timestream.TableReference(
                database_name="databaseName",
                table_arn="tableArn",
                table_name="tableName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__049ab22138340cfe02e26aa8b1e344151cb526a4f6008de057ba3654f9021656)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument table_arn", value=table_arn, expected_type=type_hints["table_arn"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "table_arn": table_arn,
            "table_name": table_name,
        }

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The DatabaseName of the Table resource.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_arn(self) -> builtins.str:
        '''The ARN of the Table resource.'''
        result = self._values.get("table_arn")
        assert result is not None, "Required property 'table_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''The TableName of the Table resource.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DatabaseReference",
    "IDatabaseRef",
    "IInfluxDBClusterRef",
    "IInfluxDBInstanceRef",
    "IScheduledQueryRef",
    "ITableRef",
    "InfluxDBClusterReference",
    "InfluxDBInstanceReference",
    "ScheduledQueryReference",
    "TableReference",
]

publication.publish()

def _typecheckingstub__f77d2bae58103bc359e516b09f6a3553472665a4ec6b584e2a0a662b39572a3a(
    *,
    database_arn: builtins.str,
    database_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b0ab1bc40e1d98c240e3df814cb220ae4647f1ec01dd4c7332cc4aea76a2cc(
    *,
    influx_db_cluster_arn: builtins.str,
    influx_db_cluster_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__397aac9d607a62cab6b8bdf7168b8cfb1607a2534996567b166ee4714911de27(
    *,
    influx_db_instance_arn: builtins.str,
    influx_db_instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcdcdbf31574908e2756c1d04b734baf4db0eca0f10b8ac19aaa61992b78d6d8(
    *,
    scheduled_query_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__049ab22138340cfe02e26aa8b1e344151cb526a4f6008de057ba3654f9021656(
    *,
    database_name: builtins.str,
    table_arn: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDatabaseRef, IInfluxDBClusterRef, IInfluxDBInstanceRef, IScheduledQueryRef, ITableRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
