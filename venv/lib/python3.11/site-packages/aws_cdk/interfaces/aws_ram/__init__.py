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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ram.IPermissionRef")
class IPermissionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Permission.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="permissionRef")
    def permission_ref(self) -> "PermissionReference":
        '''(experimental) A reference to a Permission resource.

        :stability: experimental
        '''
        ...


class _IPermissionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Permission.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ram.IPermissionRef"

    @builtins.property
    @jsii.member(jsii_name="permissionRef")
    def permission_ref(self) -> "PermissionReference":
        '''(experimental) A reference to a Permission resource.

        :stability: experimental
        '''
        return typing.cast("PermissionReference", jsii.get(self, "permissionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPermissionRef).__jsii_proxy_class__ = lambda : _IPermissionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ram.IResourceShareRef")
class IResourceShareRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceShare.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceShareRef")
    def resource_share_ref(self) -> "ResourceShareReference":
        '''(experimental) A reference to a ResourceShare resource.

        :stability: experimental
        '''
        ...


class _IResourceShareRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceShare.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ram.IResourceShareRef"

    @builtins.property
    @jsii.member(jsii_name="resourceShareRef")
    def resource_share_ref(self) -> "ResourceShareReference":
        '''(experimental) A reference to a ResourceShare resource.

        :stability: experimental
        '''
        return typing.cast("ResourceShareReference", jsii.get(self, "resourceShareRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceShareRef).__jsii_proxy_class__ = lambda : _IResourceShareRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ram.PermissionReference",
    jsii_struct_bases=[],
    name_mapping={"permission_arn": "permissionArn"},
)
class PermissionReference:
    def __init__(self, *, permission_arn: builtins.str) -> None:
        '''A reference to a Permission resource.

        :param permission_arn: The Arn of the Permission resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ram as interfaces_ram
            
            permission_reference = interfaces_ram.PermissionReference(
                permission_arn="permissionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfa3f97bc406de95182cb7061f24b81a30b9ef1f6b5ab54e34b402acd5885658)
            check_type(argname="argument permission_arn", value=permission_arn, expected_type=type_hints["permission_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permission_arn": permission_arn,
        }

    @builtins.property
    def permission_arn(self) -> builtins.str:
        '''The Arn of the Permission resource.'''
        result = self._values.get("permission_arn")
        assert result is not None, "Required property 'permission_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PermissionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ram.ResourceShareReference",
    jsii_struct_bases=[],
    name_mapping={"resource_share_arn": "resourceShareArn"},
)
class ResourceShareReference:
    def __init__(self, *, resource_share_arn: builtins.str) -> None:
        '''A reference to a ResourceShare resource.

        :param resource_share_arn: The Arn of the ResourceShare resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ram as interfaces_ram
            
            resource_share_reference = interfaces_ram.ResourceShareReference(
                resource_share_arn="resourceShareArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d05e6d9a057d581bc15e590623c6799f543dd64365bd5d095ac352a0fd449d36)
            check_type(argname="argument resource_share_arn", value=resource_share_arn, expected_type=type_hints["resource_share_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_share_arn": resource_share_arn,
        }

    @builtins.property
    def resource_share_arn(self) -> builtins.str:
        '''The Arn of the ResourceShare resource.'''
        result = self._values.get("resource_share_arn")
        assert result is not None, "Required property 'resource_share_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceShareReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IPermissionRef",
    "IResourceShareRef",
    "PermissionReference",
    "ResourceShareReference",
]

publication.publish()

def _typecheckingstub__cfa3f97bc406de95182cb7061f24b81a30b9ef1f6b5ab54e34b402acd5885658(
    *,
    permission_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d05e6d9a057d581bc15e590623c6799f543dd64365bd5d095ac352a0fd449d36(
    *,
    resource_share_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IPermissionRef, IResourceShareRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
