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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3tables.INamespaceRef")
class INamespaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Namespace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="namespaceRef")
    def namespace_ref(self) -> "NamespaceReference":
        '''(experimental) A reference to a Namespace resource.

        :stability: experimental
        '''
        ...


class _INamespaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Namespace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3tables.INamespaceRef"

    @builtins.property
    @jsii.member(jsii_name="namespaceRef")
    def namespace_ref(self) -> "NamespaceReference":
        '''(experimental) A reference to a Namespace resource.

        :stability: experimental
        '''
        return typing.cast("NamespaceReference", jsii.get(self, "namespaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INamespaceRef).__jsii_proxy_class__ = lambda : _INamespaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3tables.ITableBucketPolicyRef")
class ITableBucketPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TableBucketPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tableBucketPolicyRef")
    def table_bucket_policy_ref(self) -> "TableBucketPolicyReference":
        '''(experimental) A reference to a TableBucketPolicy resource.

        :stability: experimental
        '''
        ...


class _ITableBucketPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TableBucketPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3tables.ITableBucketPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="tableBucketPolicyRef")
    def table_bucket_policy_ref(self) -> "TableBucketPolicyReference":
        '''(experimental) A reference to a TableBucketPolicy resource.

        :stability: experimental
        '''
        return typing.cast("TableBucketPolicyReference", jsii.get(self, "tableBucketPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITableBucketPolicyRef).__jsii_proxy_class__ = lambda : _ITableBucketPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3tables.ITableBucketRef")
class ITableBucketRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TableBucket.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tableBucketRef")
    def table_bucket_ref(self) -> "TableBucketReference":
        '''(experimental) A reference to a TableBucket resource.

        :stability: experimental
        '''
        ...


class _ITableBucketRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TableBucket.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3tables.ITableBucketRef"

    @builtins.property
    @jsii.member(jsii_name="tableBucketRef")
    def table_bucket_ref(self) -> "TableBucketReference":
        '''(experimental) A reference to a TableBucket resource.

        :stability: experimental
        '''
        return typing.cast("TableBucketReference", jsii.get(self, "tableBucketRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITableBucketRef).__jsii_proxy_class__ = lambda : _ITableBucketRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3tables.ITablePolicyRef")
class ITablePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TablePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tablePolicyRef")
    def table_policy_ref(self) -> "TablePolicyReference":
        '''(experimental) A reference to a TablePolicy resource.

        :stability: experimental
        '''
        ...


class _ITablePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TablePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3tables.ITablePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="tablePolicyRef")
    def table_policy_ref(self) -> "TablePolicyReference":
        '''(experimental) A reference to a TablePolicy resource.

        :stability: experimental
        '''
        return typing.cast("TablePolicyReference", jsii.get(self, "tablePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITablePolicyRef).__jsii_proxy_class__ = lambda : _ITablePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_s3tables.ITableRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_s3tables.ITableRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_s3tables.NamespaceReference",
    jsii_struct_bases=[],
    name_mapping={"namespace": "namespace", "table_bucket_arn": "tableBucketArn"},
)
class NamespaceReference:
    def __init__(
        self,
        *,
        namespace: builtins.str,
        table_bucket_arn: builtins.str,
    ) -> None:
        '''A reference to a Namespace resource.

        :param namespace: The Namespace of the Namespace resource.
        :param table_bucket_arn: The TableBucketARN of the Namespace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3tables as interfaces_s3tables
            
            namespace_reference = interfaces_s3tables.NamespaceReference(
                namespace="namespace",
                table_bucket_arn="tableBucketArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__769c2eb3c2914dbd75fc67980d6fd8dc4704fe32d9503bb3d89c0052dc522e22)
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument table_bucket_arn", value=table_bucket_arn, expected_type=type_hints["table_bucket_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "namespace": namespace,
            "table_bucket_arn": table_bucket_arn,
        }

    @builtins.property
    def namespace(self) -> builtins.str:
        '''The Namespace of the Namespace resource.'''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_bucket_arn(self) -> builtins.str:
        '''The TableBucketARN of the Namespace resource.'''
        result = self._values.get("table_bucket_arn")
        assert result is not None, "Required property 'table_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NamespaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3tables.TableBucketPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"table_bucket_arn": "tableBucketArn"},
)
class TableBucketPolicyReference:
    def __init__(self, *, table_bucket_arn: builtins.str) -> None:
        '''A reference to a TableBucketPolicy resource.

        :param table_bucket_arn: The TableBucketARN of the TableBucketPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3tables as interfaces_s3tables
            
            table_bucket_policy_reference = interfaces_s3tables.TableBucketPolicyReference(
                table_bucket_arn="tableBucketArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac3df4e653a51813567ce9a1405bcbffaaab69af66c1bdd8a4ff9e5759c4ef47)
            check_type(argname="argument table_bucket_arn", value=table_bucket_arn, expected_type=type_hints["table_bucket_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_bucket_arn": table_bucket_arn,
        }

    @builtins.property
    def table_bucket_arn(self) -> builtins.str:
        '''The TableBucketARN of the TableBucketPolicy resource.'''
        result = self._values.get("table_bucket_arn")
        assert result is not None, "Required property 'table_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableBucketPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3tables.TableBucketReference",
    jsii_struct_bases=[],
    name_mapping={"table_bucket_arn": "tableBucketArn"},
)
class TableBucketReference:
    def __init__(self, *, table_bucket_arn: builtins.str) -> None:
        '''A reference to a TableBucket resource.

        :param table_bucket_arn: The TableBucketARN of the TableBucket resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3tables as interfaces_s3tables
            
            table_bucket_reference = interfaces_s3tables.TableBucketReference(
                table_bucket_arn="tableBucketArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab47e4b70198d3821edeaa467fb3b68145e801287014631d803d69036d4647bf)
            check_type(argname="argument table_bucket_arn", value=table_bucket_arn, expected_type=type_hints["table_bucket_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_bucket_arn": table_bucket_arn,
        }

    @builtins.property
    def table_bucket_arn(self) -> builtins.str:
        '''The TableBucketARN of the TableBucket resource.'''
        result = self._values.get("table_bucket_arn")
        assert result is not None, "Required property 'table_bucket_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableBucketReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3tables.TablePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"table_arn": "tableArn"},
)
class TablePolicyReference:
    def __init__(self, *, table_arn: builtins.str) -> None:
        '''A reference to a TablePolicy resource.

        :param table_arn: The TableARN of the TablePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3tables as interfaces_s3tables
            
            table_policy_reference = interfaces_s3tables.TablePolicyReference(
                table_arn="tableArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42326fef6bef2084b71f2902b0cc9888ea9338c0e1c16e36a9a255fbf3c3d98e)
            check_type(argname="argument table_arn", value=table_arn, expected_type=type_hints["table_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_arn": table_arn,
        }

    @builtins.property
    def table_arn(self) -> builtins.str:
        '''The TableARN of the TablePolicy resource.'''
        result = self._values.get("table_arn")
        assert result is not None, "Required property 'table_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TablePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_s3tables.TableReference",
    jsii_struct_bases=[],
    name_mapping={"table_arn": "tableArn"},
)
class TableReference:
    def __init__(self, *, table_arn: builtins.str) -> None:
        '''A reference to a Table resource.

        :param table_arn: The TableARN of the Table resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_s3tables as interfaces_s3tables
            
            table_reference = interfaces_s3tables.TableReference(
                table_arn="tableArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2df438cc32b11b0de6320fbbdc2453915a1766092e7471e03d5d8fc7b0dd698b)
            check_type(argname="argument table_arn", value=table_arn, expected_type=type_hints["table_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_arn": table_arn,
        }

    @builtins.property
    def table_arn(self) -> builtins.str:
        '''The TableARN of the Table resource.'''
        result = self._values.get("table_arn")
        assert result is not None, "Required property 'table_arn' is missing"
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
    "INamespaceRef",
    "ITableBucketPolicyRef",
    "ITableBucketRef",
    "ITablePolicyRef",
    "ITableRef",
    "NamespaceReference",
    "TableBucketPolicyReference",
    "TableBucketReference",
    "TablePolicyReference",
    "TableReference",
]

publication.publish()

def _typecheckingstub__769c2eb3c2914dbd75fc67980d6fd8dc4704fe32d9503bb3d89c0052dc522e22(
    *,
    namespace: builtins.str,
    table_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac3df4e653a51813567ce9a1405bcbffaaab69af66c1bdd8a4ff9e5759c4ef47(
    *,
    table_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab47e4b70198d3821edeaa467fb3b68145e801287014631d803d69036d4647bf(
    *,
    table_bucket_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42326fef6bef2084b71f2902b0cc9888ea9338c0e1c16e36a9a255fbf3c3d98e(
    *,
    table_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2df438cc32b11b0de6320fbbdc2453915a1766092e7471e03d5d8fc7b0dd698b(
    *,
    table_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [INamespaceRef, ITableBucketPolicyRef, ITableBucketRef, ITablePolicyRef, ITableRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
