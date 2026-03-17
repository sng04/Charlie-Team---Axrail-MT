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
    jsii_type="aws-cdk-lib.interfaces.aws_efs.AccessPointReference",
    jsii_struct_bases=[],
    name_mapping={
        "access_point_arn": "accessPointArn",
        "access_point_id": "accessPointId",
    },
)
class AccessPointReference:
    def __init__(
        self,
        *,
        access_point_arn: builtins.str,
        access_point_id: builtins.str,
    ) -> None:
        '''A reference to a AccessPoint resource.

        :param access_point_arn: The ARN of the AccessPoint resource.
        :param access_point_id: The AccessPointId of the AccessPoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_efs as interfaces_efs
            
            access_point_reference = interfaces_efs.AccessPointReference(
                access_point_arn="accessPointArn",
                access_point_id="accessPointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc8aac9c1aa585347c168849365dd9636f4905e4a3e867b3057c0e1c6a564f16)
            check_type(argname="argument access_point_arn", value=access_point_arn, expected_type=type_hints["access_point_arn"])
            check_type(argname="argument access_point_id", value=access_point_id, expected_type=type_hints["access_point_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_point_arn": access_point_arn,
            "access_point_id": access_point_id,
        }

    @builtins.property
    def access_point_arn(self) -> builtins.str:
        '''The ARN of the AccessPoint resource.'''
        result = self._values.get("access_point_arn")
        assert result is not None, "Required property 'access_point_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_point_id(self) -> builtins.str:
        '''The AccessPointId of the AccessPoint resource.'''
        result = self._values.get("access_point_id")
        assert result is not None, "Required property 'access_point_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessPointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_efs.FileSystemReference",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_arn": "fileSystemArn",
        "file_system_id": "fileSystemId",
    },
)
class FileSystemReference:
    def __init__(
        self,
        *,
        file_system_arn: builtins.str,
        file_system_id: builtins.str,
    ) -> None:
        '''A reference to a FileSystem resource.

        :param file_system_arn: The ARN of the FileSystem resource.
        :param file_system_id: The FileSystemId of the FileSystem resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_efs as interfaces_efs
            
            file_system_reference = interfaces_efs.FileSystemReference(
                file_system_arn="fileSystemArn",
                file_system_id="fileSystemId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da743eccfedceff078b644fac06f6acbf8a8c050682bb0c7bc912f9c7baad218)
            check_type(argname="argument file_system_arn", value=file_system_arn, expected_type=type_hints["file_system_arn"])
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_arn": file_system_arn,
            "file_system_id": file_system_id,
        }

    @builtins.property
    def file_system_arn(self) -> builtins.str:
        '''The ARN of the FileSystem resource.'''
        result = self._values.get("file_system_arn")
        assert result is not None, "Required property 'file_system_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''The FileSystemId of the FileSystem resource.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FileSystemReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_efs.IAccessPointRef")
class IAccessPointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessPointRef")
    def access_point_ref(self) -> "AccessPointReference":
        '''(experimental) A reference to a AccessPoint resource.

        :stability: experimental
        '''
        ...


class _IAccessPointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessPoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_efs.IAccessPointRef"

    @builtins.property
    @jsii.member(jsii_name="accessPointRef")
    def access_point_ref(self) -> "AccessPointReference":
        '''(experimental) A reference to a AccessPoint resource.

        :stability: experimental
        '''
        return typing.cast("AccessPointReference", jsii.get(self, "accessPointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessPointRef).__jsii_proxy_class__ = lambda : _IAccessPointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_efs.IFileSystemRef")
class IFileSystemRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FileSystem.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fileSystemRef")
    def file_system_ref(self) -> "FileSystemReference":
        '''(experimental) A reference to a FileSystem resource.

        :stability: experimental
        '''
        ...


class _IFileSystemRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FileSystem.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_efs.IFileSystemRef"

    @builtins.property
    @jsii.member(jsii_name="fileSystemRef")
    def file_system_ref(self) -> "FileSystemReference":
        '''(experimental) A reference to a FileSystem resource.

        :stability: experimental
        '''
        return typing.cast("FileSystemReference", jsii.get(self, "fileSystemRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFileSystemRef).__jsii_proxy_class__ = lambda : _IFileSystemRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_efs.IMountTargetRef")
class IMountTargetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MountTarget.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mountTargetRef")
    def mount_target_ref(self) -> "MountTargetReference":
        '''(experimental) A reference to a MountTarget resource.

        :stability: experimental
        '''
        ...


class _IMountTargetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MountTarget.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_efs.IMountTargetRef"

    @builtins.property
    @jsii.member(jsii_name="mountTargetRef")
    def mount_target_ref(self) -> "MountTargetReference":
        '''(experimental) A reference to a MountTarget resource.

        :stability: experimental
        '''
        return typing.cast("MountTargetReference", jsii.get(self, "mountTargetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMountTargetRef).__jsii_proxy_class__ = lambda : _IMountTargetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_efs.MountTargetReference",
    jsii_struct_bases=[],
    name_mapping={"mount_target_id": "mountTargetId"},
)
class MountTargetReference:
    def __init__(self, *, mount_target_id: builtins.str) -> None:
        '''A reference to a MountTarget resource.

        :param mount_target_id: The Id of the MountTarget resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_efs as interfaces_efs
            
            mount_target_reference = interfaces_efs.MountTargetReference(
                mount_target_id="mountTargetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e67ed28e1235a9ff4338f4b06cbd755f1f65a645b5a3a98baefca6ec98a4d0c)
            check_type(argname="argument mount_target_id", value=mount_target_id, expected_type=type_hints["mount_target_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mount_target_id": mount_target_id,
        }

    @builtins.property
    def mount_target_id(self) -> builtins.str:
        '''The Id of the MountTarget resource.'''
        result = self._values.get("mount_target_id")
        assert result is not None, "Required property 'mount_target_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountTargetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessPointReference",
    "FileSystemReference",
    "IAccessPointRef",
    "IFileSystemRef",
    "IMountTargetRef",
    "MountTargetReference",
]

publication.publish()

def _typecheckingstub__fc8aac9c1aa585347c168849365dd9636f4905e4a3e867b3057c0e1c6a564f16(
    *,
    access_point_arn: builtins.str,
    access_point_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da743eccfedceff078b644fac06f6acbf8a8c050682bb0c7bc912f9c7baad218(
    *,
    file_system_arn: builtins.str,
    file_system_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e67ed28e1235a9ff4338f4b06cbd755f1f65a645b5a3a98baefca6ec98a4d0c(
    *,
    mount_target_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessPointRef, IFileSystemRef, IMountTargetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
