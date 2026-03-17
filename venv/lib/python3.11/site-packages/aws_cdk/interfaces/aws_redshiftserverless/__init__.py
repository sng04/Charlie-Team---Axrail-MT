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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_redshiftserverless.INamespaceRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshiftserverless.INamespaceRef"

    @builtins.property
    @jsii.member(jsii_name="namespaceRef")
    def namespace_ref(self) -> "NamespaceReference":
        '''(experimental) A reference to a Namespace resource.

        :stability: experimental
        '''
        return typing.cast("NamespaceReference", jsii.get(self, "namespaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INamespaceRef).__jsii_proxy_class__ = lambda : _INamespaceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_redshiftserverless.ISnapshotRef")
class ISnapshotRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Snapshot.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="snapshotRef")
    def snapshot_ref(self) -> "SnapshotReference":
        '''(experimental) A reference to a Snapshot resource.

        :stability: experimental
        '''
        ...


class _ISnapshotRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Snapshot.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshiftserverless.ISnapshotRef"

    @builtins.property
    @jsii.member(jsii_name="snapshotRef")
    def snapshot_ref(self) -> "SnapshotReference":
        '''(experimental) A reference to a Snapshot resource.

        :stability: experimental
        '''
        return typing.cast("SnapshotReference", jsii.get(self, "snapshotRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISnapshotRef).__jsii_proxy_class__ = lambda : _ISnapshotRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_redshiftserverless.IWorkgroupRef"
)
class IWorkgroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workgroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workgroupRef")
    def workgroup_ref(self) -> "WorkgroupReference":
        '''(experimental) A reference to a Workgroup resource.

        :stability: experimental
        '''
        ...


class _IWorkgroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workgroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_redshiftserverless.IWorkgroupRef"

    @builtins.property
    @jsii.member(jsii_name="workgroupRef")
    def workgroup_ref(self) -> "WorkgroupReference":
        '''(experimental) A reference to a Workgroup resource.

        :stability: experimental
        '''
        return typing.cast("WorkgroupReference", jsii.get(self, "workgroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkgroupRef).__jsii_proxy_class__ = lambda : _IWorkgroupRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_redshiftserverless.NamespaceReference",
    jsii_struct_bases=[],
    name_mapping={"namespace_name": "namespaceName"},
)
class NamespaceReference:
    def __init__(self, *, namespace_name: builtins.str) -> None:
        '''A reference to a Namespace resource.

        :param namespace_name: The NamespaceName of the Namespace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshiftserverless as interfaces_redshiftserverless
            
            namespace_reference = interfaces_redshiftserverless.NamespaceReference(
                namespace_name="namespaceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb47b5ad1846229985e2e40d4fc80ad91bfd5c560018da49be206fd628154053)
            check_type(argname="argument namespace_name", value=namespace_name, expected_type=type_hints["namespace_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "namespace_name": namespace_name,
        }

    @builtins.property
    def namespace_name(self) -> builtins.str:
        '''The NamespaceName of the Namespace resource.'''
        result = self._values.get("namespace_name")
        assert result is not None, "Required property 'namespace_name' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_redshiftserverless.SnapshotReference",
    jsii_struct_bases=[],
    name_mapping={"snapshot_name": "snapshotName"},
)
class SnapshotReference:
    def __init__(self, *, snapshot_name: builtins.str) -> None:
        '''A reference to a Snapshot resource.

        :param snapshot_name: The SnapshotName of the Snapshot resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshiftserverless as interfaces_redshiftserverless
            
            snapshot_reference = interfaces_redshiftserverless.SnapshotReference(
                snapshot_name="snapshotName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74fe30cf9dcd3013012d493eb5cf4a8fd167f4aebc1b526478f43197ed27b09b)
            check_type(argname="argument snapshot_name", value=snapshot_name, expected_type=type_hints["snapshot_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "snapshot_name": snapshot_name,
        }

    @builtins.property
    def snapshot_name(self) -> builtins.str:
        '''The SnapshotName of the Snapshot resource.'''
        result = self._values.get("snapshot_name")
        assert result is not None, "Required property 'snapshot_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SnapshotReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_redshiftserverless.WorkgroupReference",
    jsii_struct_bases=[],
    name_mapping={"workgroup_name": "workgroupName"},
)
class WorkgroupReference:
    def __init__(self, *, workgroup_name: builtins.str) -> None:
        '''A reference to a Workgroup resource.

        :param workgroup_name: The WorkgroupName of the Workgroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_redshiftserverless as interfaces_redshiftserverless
            
            workgroup_reference = interfaces_redshiftserverless.WorkgroupReference(
                workgroup_name="workgroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55c1cec7cb09d8068c5498b75c2b2ce1723ddd0f4dcedf266da3ea6045d1d962)
            check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workgroup_name": workgroup_name,
        }

    @builtins.property
    def workgroup_name(self) -> builtins.str:
        '''The WorkgroupName of the Workgroup resource.'''
        result = self._values.get("workgroup_name")
        assert result is not None, "Required property 'workgroup_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkgroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "INamespaceRef",
    "ISnapshotRef",
    "IWorkgroupRef",
    "NamespaceReference",
    "SnapshotReference",
    "WorkgroupReference",
]

publication.publish()

def _typecheckingstub__bb47b5ad1846229985e2e40d4fc80ad91bfd5c560018da49be206fd628154053(
    *,
    namespace_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74fe30cf9dcd3013012d493eb5cf4a8fd167f4aebc1b526478f43197ed27b09b(
    *,
    snapshot_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55c1cec7cb09d8068c5498b75c2b2ce1723ddd0f4dcedf266da3ea6045d1d962(
    *,
    workgroup_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [INamespaceRef, ISnapshotRef, IWorkgroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
