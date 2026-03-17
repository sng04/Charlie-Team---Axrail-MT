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
    jsii_type="aws-cdk-lib.interfaces.aws_athena.CapacityReservationReference",
    jsii_struct_bases=[],
    name_mapping={"capacity_reservation_arn": "capacityReservationArn"},
)
class CapacityReservationReference:
    def __init__(self, *, capacity_reservation_arn: builtins.str) -> None:
        '''A reference to a CapacityReservation resource.

        :param capacity_reservation_arn: The Arn of the CapacityReservation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_athena as interfaces_athena
            
            capacity_reservation_reference = interfaces_athena.CapacityReservationReference(
                capacity_reservation_arn="capacityReservationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed03e15637dfd04e8cb942727955453b165a7628fd36cdd7fbe6cb826d5452e4)
            check_type(argname="argument capacity_reservation_arn", value=capacity_reservation_arn, expected_type=type_hints["capacity_reservation_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity_reservation_arn": capacity_reservation_arn,
        }

    @builtins.property
    def capacity_reservation_arn(self) -> builtins.str:
        '''The Arn of the CapacityReservation resource.'''
        result = self._values.get("capacity_reservation_arn")
        assert result is not None, "Required property 'capacity_reservation_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CapacityReservationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_athena.DataCatalogReference",
    jsii_struct_bases=[],
    name_mapping={"data_catalog_name": "dataCatalogName"},
)
class DataCatalogReference:
    def __init__(self, *, data_catalog_name: builtins.str) -> None:
        '''A reference to a DataCatalog resource.

        :param data_catalog_name: The Name of the DataCatalog resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_athena as interfaces_athena
            
            data_catalog_reference = interfaces_athena.DataCatalogReference(
                data_catalog_name="dataCatalogName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4d331c6538b87bd92e94c1c887faa87b351a321589953355092c63f8d11852a)
            check_type(argname="argument data_catalog_name", value=data_catalog_name, expected_type=type_hints["data_catalog_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_catalog_name": data_catalog_name,
        }

    @builtins.property
    def data_catalog_name(self) -> builtins.str:
        '''The Name of the DataCatalog resource.'''
        result = self._values.get("data_catalog_name")
        assert result is not None, "Required property 'data_catalog_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataCatalogReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_athena.ICapacityReservationRef")
class ICapacityReservationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityReservation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="capacityReservationRef")
    def capacity_reservation_ref(self) -> "CapacityReservationReference":
        '''(experimental) A reference to a CapacityReservation resource.

        :stability: experimental
        '''
        ...


class _ICapacityReservationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityReservation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_athena.ICapacityReservationRef"

    @builtins.property
    @jsii.member(jsii_name="capacityReservationRef")
    def capacity_reservation_ref(self) -> "CapacityReservationReference":
        '''(experimental) A reference to a CapacityReservation resource.

        :stability: experimental
        '''
        return typing.cast("CapacityReservationReference", jsii.get(self, "capacityReservationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICapacityReservationRef).__jsii_proxy_class__ = lambda : _ICapacityReservationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_athena.IDataCatalogRef")
class IDataCatalogRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataCatalog.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataCatalogRef")
    def data_catalog_ref(self) -> "DataCatalogReference":
        '''(experimental) A reference to a DataCatalog resource.

        :stability: experimental
        '''
        ...


class _IDataCatalogRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataCatalog.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_athena.IDataCatalogRef"

    @builtins.property
    @jsii.member(jsii_name="dataCatalogRef")
    def data_catalog_ref(self) -> "DataCatalogReference":
        '''(experimental) A reference to a DataCatalog resource.

        :stability: experimental
        '''
        return typing.cast("DataCatalogReference", jsii.get(self, "dataCatalogRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataCatalogRef).__jsii_proxy_class__ = lambda : _IDataCatalogRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_athena.INamedQueryRef")
class INamedQueryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NamedQuery.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="namedQueryRef")
    def named_query_ref(self) -> "NamedQueryReference":
        '''(experimental) A reference to a NamedQuery resource.

        :stability: experimental
        '''
        ...


class _INamedQueryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NamedQuery.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_athena.INamedQueryRef"

    @builtins.property
    @jsii.member(jsii_name="namedQueryRef")
    def named_query_ref(self) -> "NamedQueryReference":
        '''(experimental) A reference to a NamedQuery resource.

        :stability: experimental
        '''
        return typing.cast("NamedQueryReference", jsii.get(self, "namedQueryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INamedQueryRef).__jsii_proxy_class__ = lambda : _INamedQueryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_athena.IPreparedStatementRef")
class IPreparedStatementRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PreparedStatement.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="preparedStatementRef")
    def prepared_statement_ref(self) -> "PreparedStatementReference":
        '''(experimental) A reference to a PreparedStatement resource.

        :stability: experimental
        '''
        ...


class _IPreparedStatementRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PreparedStatement.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_athena.IPreparedStatementRef"

    @builtins.property
    @jsii.member(jsii_name="preparedStatementRef")
    def prepared_statement_ref(self) -> "PreparedStatementReference":
        '''(experimental) A reference to a PreparedStatement resource.

        :stability: experimental
        '''
        return typing.cast("PreparedStatementReference", jsii.get(self, "preparedStatementRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPreparedStatementRef).__jsii_proxy_class__ = lambda : _IPreparedStatementRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_athena.IWorkGroupRef")
class IWorkGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WorkGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workGroupRef")
    def work_group_ref(self) -> "WorkGroupReference":
        '''(experimental) A reference to a WorkGroup resource.

        :stability: experimental
        '''
        ...


class _IWorkGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WorkGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_athena.IWorkGroupRef"

    @builtins.property
    @jsii.member(jsii_name="workGroupRef")
    def work_group_ref(self) -> "WorkGroupReference":
        '''(experimental) A reference to a WorkGroup resource.

        :stability: experimental
        '''
        return typing.cast("WorkGroupReference", jsii.get(self, "workGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkGroupRef).__jsii_proxy_class__ = lambda : _IWorkGroupRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_athena.NamedQueryReference",
    jsii_struct_bases=[],
    name_mapping={"named_query_id": "namedQueryId"},
)
class NamedQueryReference:
    def __init__(self, *, named_query_id: builtins.str) -> None:
        '''A reference to a NamedQuery resource.

        :param named_query_id: The NamedQueryId of the NamedQuery resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_athena as interfaces_athena
            
            named_query_reference = interfaces_athena.NamedQueryReference(
                named_query_id="namedQueryId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb78f814f219b554ae585d86189d76c3b565202bcc84e2e82015de6a6033c74e)
            check_type(argname="argument named_query_id", value=named_query_id, expected_type=type_hints["named_query_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "named_query_id": named_query_id,
        }

    @builtins.property
    def named_query_id(self) -> builtins.str:
        '''The NamedQueryId of the NamedQuery resource.'''
        result = self._values.get("named_query_id")
        assert result is not None, "Required property 'named_query_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamedQueryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_athena.PreparedStatementReference",
    jsii_struct_bases=[],
    name_mapping={"statement_name": "statementName", "work_group": "workGroup"},
)
class PreparedStatementReference:
    def __init__(
        self,
        *,
        statement_name: builtins.str,
        work_group: builtins.str,
    ) -> None:
        '''A reference to a PreparedStatement resource.

        :param statement_name: The StatementName of the PreparedStatement resource.
        :param work_group: The WorkGroup of the PreparedStatement resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_athena as interfaces_athena
            
            prepared_statement_reference = interfaces_athena.PreparedStatementReference(
                statement_name="statementName",
                work_group="workGroup"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e79cee1079d75d49425539c959b6360f318a9ea2bf4dfcd757f3656094c91a8)
            check_type(argname="argument statement_name", value=statement_name, expected_type=type_hints["statement_name"])
            check_type(argname="argument work_group", value=work_group, expected_type=type_hints["work_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "statement_name": statement_name,
            "work_group": work_group,
        }

    @builtins.property
    def statement_name(self) -> builtins.str:
        '''The StatementName of the PreparedStatement resource.'''
        result = self._values.get("statement_name")
        assert result is not None, "Required property 'statement_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def work_group(self) -> builtins.str:
        '''The WorkGroup of the PreparedStatement resource.'''
        result = self._values.get("work_group")
        assert result is not None, "Required property 'work_group' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PreparedStatementReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_athena.WorkGroupReference",
    jsii_struct_bases=[],
    name_mapping={"work_group_name": "workGroupName"},
)
class WorkGroupReference:
    def __init__(self, *, work_group_name: builtins.str) -> None:
        '''A reference to a WorkGroup resource.

        :param work_group_name: The Name of the WorkGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_athena as interfaces_athena
            
            work_group_reference = interfaces_athena.WorkGroupReference(
                work_group_name="workGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf5da3b7d36495d1cd424f8484a3dd86b735b00d96d9015bccbe52ba012f3bab)
            check_type(argname="argument work_group_name", value=work_group_name, expected_type=type_hints["work_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "work_group_name": work_group_name,
        }

    @builtins.property
    def work_group_name(self) -> builtins.str:
        '''The Name of the WorkGroup resource.'''
        result = self._values.get("work_group_name")
        assert result is not None, "Required property 'work_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CapacityReservationReference",
    "DataCatalogReference",
    "ICapacityReservationRef",
    "IDataCatalogRef",
    "INamedQueryRef",
    "IPreparedStatementRef",
    "IWorkGroupRef",
    "NamedQueryReference",
    "PreparedStatementReference",
    "WorkGroupReference",
]

publication.publish()

def _typecheckingstub__ed03e15637dfd04e8cb942727955453b165a7628fd36cdd7fbe6cb826d5452e4(
    *,
    capacity_reservation_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4d331c6538b87bd92e94c1c887faa87b351a321589953355092c63f8d11852a(
    *,
    data_catalog_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb78f814f219b554ae585d86189d76c3b565202bcc84e2e82015de6a6033c74e(
    *,
    named_query_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e79cee1079d75d49425539c959b6360f318a9ea2bf4dfcd757f3656094c91a8(
    *,
    statement_name: builtins.str,
    work_group: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf5da3b7d36495d1cd424f8484a3dd86b735b00d96d9015bccbe52ba012f3bab(
    *,
    work_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICapacityReservationRef, IDataCatalogRef, INamedQueryRef, IPreparedStatementRef, IWorkGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
