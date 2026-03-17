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
    jsii_type="aws-cdk-lib.interfaces.aws_dynamodb.GlobalTableReference",
    jsii_struct_bases=[],
    name_mapping={"global_table_arn": "globalTableArn", "table_name": "tableName"},
)
class GlobalTableReference:
    def __init__(
        self,
        *,
        global_table_arn: builtins.str,
        table_name: builtins.str,
    ) -> None:
        '''A reference to a GlobalTable resource.

        :param global_table_arn: The ARN of the GlobalTable resource.
        :param table_name: The TableName of the GlobalTable resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dynamodb as interfaces_dynamodb
            
            global_table_reference = interfaces_dynamodb.GlobalTableReference(
                global_table_arn="globalTableArn",
                table_name="tableName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6270d28eb00f1c7aaa0618efc5efa6bde94ef3afc9af55397e196de36f008c1)
            check_type(argname="argument global_table_arn", value=global_table_arn, expected_type=type_hints["global_table_arn"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_table_arn": global_table_arn,
            "table_name": table_name,
        }

    @builtins.property
    def global_table_arn(self) -> builtins.str:
        '''The ARN of the GlobalTable resource.'''
        result = self._values.get("global_table_arn")
        assert result is not None, "Required property 'global_table_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''The TableName of the GlobalTable resource.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlobalTableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dynamodb.IGlobalTableRef")
class IGlobalTableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalTable.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="globalTableRef")
    def global_table_ref(self) -> "GlobalTableReference":
        '''(experimental) A reference to a GlobalTable resource.

        :stability: experimental
        '''
        ...


class _IGlobalTableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalTable.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dynamodb.IGlobalTableRef"

    @builtins.property
    @jsii.member(jsii_name="globalTableRef")
    def global_table_ref(self) -> "GlobalTableReference":
        '''(experimental) A reference to a GlobalTable resource.

        :stability: experimental
        '''
        return typing.cast("GlobalTableReference", jsii.get(self, "globalTableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGlobalTableRef).__jsii_proxy_class__ = lambda : _IGlobalTableRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dynamodb.ITableRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dynamodb.ITableRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_dynamodb.TableReference",
    jsii_struct_bases=[],
    name_mapping={"table_arn": "tableArn", "table_name": "tableName"},
)
class TableReference:
    def __init__(self, *, table_arn: builtins.str, table_name: builtins.str) -> None:
        '''A reference to a Table resource.

        :param table_arn: The ARN of the Table resource.
        :param table_name: The TableName of the Table resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dynamodb as interfaces_dynamodb
            
            table_reference = interfaces_dynamodb.TableReference(
                table_arn="tableArn",
                table_name="tableName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c9915de6003c317a1c7befc808c20d44a9823a94b613f2c1a5353c8a9180d97)
            check_type(argname="argument table_arn", value=table_arn, expected_type=type_hints["table_arn"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_arn": table_arn,
            "table_name": table_name,
        }

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
    "GlobalTableReference",
    "IGlobalTableRef",
    "ITableRef",
    "TableReference",
]

publication.publish()

def _typecheckingstub__d6270d28eb00f1c7aaa0618efc5efa6bde94ef3afc9af55397e196de36f008c1(
    *,
    global_table_arn: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9915de6003c317a1c7befc808c20d44a9823a94b613f2c1a5353c8a9180d97(
    *,
    table_arn: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IGlobalTableRef, ITableRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
