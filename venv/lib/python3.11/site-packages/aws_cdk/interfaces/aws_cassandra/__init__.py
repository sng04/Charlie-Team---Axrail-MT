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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cassandra.IKeyspaceRef")
class IKeyspaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Keyspace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="keyspaceRef")
    def keyspace_ref(self) -> "KeyspaceReference":
        '''(experimental) A reference to a Keyspace resource.

        :stability: experimental
        '''
        ...


class _IKeyspaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Keyspace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cassandra.IKeyspaceRef"

    @builtins.property
    @jsii.member(jsii_name="keyspaceRef")
    def keyspace_ref(self) -> "KeyspaceReference":
        '''(experimental) A reference to a Keyspace resource.

        :stability: experimental
        '''
        return typing.cast("KeyspaceReference", jsii.get(self, "keyspaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKeyspaceRef).__jsii_proxy_class__ = lambda : _IKeyspaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cassandra.ITableRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cassandra.ITableRef"

    @builtins.property
    @jsii.member(jsii_name="tableRef")
    def table_ref(self) -> "TableReference":
        '''(experimental) A reference to a Table resource.

        :stability: experimental
        '''
        return typing.cast("TableReference", jsii.get(self, "tableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITableRef).__jsii_proxy_class__ = lambda : _ITableRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cassandra.ITypeRef")
class ITypeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Type.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="typeRef")
    def type_ref(self) -> "TypeReference":
        '''(experimental) A reference to a Type resource.

        :stability: experimental
        '''
        ...


class _ITypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Type.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cassandra.ITypeRef"

    @builtins.property
    @jsii.member(jsii_name="typeRef")
    def type_ref(self) -> "TypeReference":
        '''(experimental) A reference to a Type resource.

        :stability: experimental
        '''
        return typing.cast("TypeReference", jsii.get(self, "typeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITypeRef).__jsii_proxy_class__ = lambda : _ITypeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cassandra.KeyspaceReference",
    jsii_struct_bases=[],
    name_mapping={"keyspace_name": "keyspaceName"},
)
class KeyspaceReference:
    def __init__(self, *, keyspace_name: builtins.str) -> None:
        '''A reference to a Keyspace resource.

        :param keyspace_name: The KeyspaceName of the Keyspace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cassandra as interfaces_cassandra
            
            keyspace_reference = interfaces_cassandra.KeyspaceReference(
                keyspace_name="keyspaceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc0d753836cd041e1b05ee95877283f6b5b750f64e052cdef38fb1696ddc1f71)
            check_type(argname="argument keyspace_name", value=keyspace_name, expected_type=type_hints["keyspace_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "keyspace_name": keyspace_name,
        }

    @builtins.property
    def keyspace_name(self) -> builtins.str:
        '''The KeyspaceName of the Keyspace resource.'''
        result = self._values.get("keyspace_name")
        assert result is not None, "Required property 'keyspace_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeyspaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cassandra.TableReference",
    jsii_struct_bases=[],
    name_mapping={"keyspace_name": "keyspaceName", "table_name": "tableName"},
)
class TableReference:
    def __init__(
        self,
        *,
        keyspace_name: builtins.str,
        table_name: builtins.str,
    ) -> None:
        '''A reference to a Table resource.

        :param keyspace_name: The KeyspaceName of the Table resource.
        :param table_name: The TableName of the Table resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cassandra as interfaces_cassandra
            
            table_reference = interfaces_cassandra.TableReference(
                keyspace_name="keyspaceName",
                table_name="tableName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d9110ed91ad7506d3d63c21f49e4f422ab7dfc099f42a7a3ed964067e567abc)
            check_type(argname="argument keyspace_name", value=keyspace_name, expected_type=type_hints["keyspace_name"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "keyspace_name": keyspace_name,
            "table_name": table_name,
        }

    @builtins.property
    def keyspace_name(self) -> builtins.str:
        '''The KeyspaceName of the Table resource.'''
        result = self._values.get("keyspace_name")
        assert result is not None, "Required property 'keyspace_name' is missing"
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


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cassandra.TypeReference",
    jsii_struct_bases=[],
    name_mapping={"keyspace_name": "keyspaceName", "type_name": "typeName"},
)
class TypeReference:
    def __init__(self, *, keyspace_name: builtins.str, type_name: builtins.str) -> None:
        '''A reference to a Type resource.

        :param keyspace_name: The KeyspaceName of the Type resource.
        :param type_name: The TypeName of the Type resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cassandra as interfaces_cassandra
            
            type_reference = interfaces_cassandra.TypeReference(
                keyspace_name="keyspaceName",
                type_name="typeName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a94f1d1b9cf43e51c9c314f470a36db3a2060e9c64df91318dd46ed316ba5d0)
            check_type(argname="argument keyspace_name", value=keyspace_name, expected_type=type_hints["keyspace_name"])
            check_type(argname="argument type_name", value=type_name, expected_type=type_hints["type_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "keyspace_name": keyspace_name,
            "type_name": type_name,
        }

    @builtins.property
    def keyspace_name(self) -> builtins.str:
        '''The KeyspaceName of the Type resource.'''
        result = self._values.get("keyspace_name")
        assert result is not None, "Required property 'keyspace_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type_name(self) -> builtins.str:
        '''The TypeName of the Type resource.'''
        result = self._values.get("type_name")
        assert result is not None, "Required property 'type_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IKeyspaceRef",
    "ITableRef",
    "ITypeRef",
    "KeyspaceReference",
    "TableReference",
    "TypeReference",
]

publication.publish()

def _typecheckingstub__fc0d753836cd041e1b05ee95877283f6b5b750f64e052cdef38fb1696ddc1f71(
    *,
    keyspace_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d9110ed91ad7506d3d63c21f49e4f422ab7dfc099f42a7a3ed964067e567abc(
    *,
    keyspace_name: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a94f1d1b9cf43e51c9c314f470a36db3a2060e9c64df91318dd46ed316ba5d0(
    *,
    keyspace_name: builtins.str,
    type_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IKeyspaceRef, ITableRef, ITypeRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
