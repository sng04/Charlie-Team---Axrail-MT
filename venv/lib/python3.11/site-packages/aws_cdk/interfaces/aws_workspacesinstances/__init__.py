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
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesinstances.IVolumeAssociationRef"
)
class IVolumeAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VolumeAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="volumeAssociationRef")
    def volume_association_ref(self) -> "VolumeAssociationReference":
        '''(experimental) A reference to a VolumeAssociation resource.

        :stability: experimental
        '''
        ...


class _IVolumeAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VolumeAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesinstances.IVolumeAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="volumeAssociationRef")
    def volume_association_ref(self) -> "VolumeAssociationReference":
        '''(experimental) A reference to a VolumeAssociation resource.

        :stability: experimental
        '''
        return typing.cast("VolumeAssociationReference", jsii.get(self, "volumeAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVolumeAssociationRef).__jsii_proxy_class__ = lambda : _IVolumeAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_workspacesinstances.IVolumeRef")
class IVolumeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        ...


class _IVolumeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Volume.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesinstances.IVolumeRef"

    @builtins.property
    @jsii.member(jsii_name="volumeRef")
    def volume_ref(self) -> "VolumeReference":
        '''(experimental) A reference to a Volume resource.

        :stability: experimental
        '''
        return typing.cast("VolumeReference", jsii.get(self, "volumeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVolumeRef).__jsii_proxy_class__ = lambda : _IVolumeRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesinstances.IWorkspaceInstanceRef"
)
class IWorkspaceInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WorkspaceInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workspaceInstanceRef")
    def workspace_instance_ref(self) -> "WorkspaceInstanceReference":
        '''(experimental) A reference to a WorkspaceInstance resource.

        :stability: experimental
        '''
        ...


class _IWorkspaceInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WorkspaceInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesinstances.IWorkspaceInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="workspaceInstanceRef")
    def workspace_instance_ref(self) -> "WorkspaceInstanceReference":
        '''(experimental) A reference to a WorkspaceInstance resource.

        :stability: experimental
        '''
        return typing.cast("WorkspaceInstanceReference", jsii.get(self, "workspaceInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkspaceInstanceRef).__jsii_proxy_class__ = lambda : _IWorkspaceInstanceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesinstances.VolumeAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "device": "device",
        "volume_id": "volumeId",
        "workspace_instance_id": "workspaceInstanceId",
    },
)
class VolumeAssociationReference:
    def __init__(
        self,
        *,
        device: builtins.str,
        volume_id: builtins.str,
        workspace_instance_id: builtins.str,
    ) -> None:
        '''A reference to a VolumeAssociation resource.

        :param device: The Device of the VolumeAssociation resource.
        :param volume_id: The VolumeId of the VolumeAssociation resource.
        :param workspace_instance_id: The WorkspaceInstanceId of the VolumeAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesinstances as interfaces_workspacesinstances
            
            volume_association_reference = interfaces_workspacesinstances.VolumeAssociationReference(
                device="device",
                volume_id="volumeId",
                workspace_instance_id="workspaceInstanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d42d044ad84f26aeab835fd848713813856201672e3db8bf912fd1950d1358d)
            check_type(argname="argument device", value=device, expected_type=type_hints["device"])
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument workspace_instance_id", value=workspace_instance_id, expected_type=type_hints["workspace_instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device": device,
            "volume_id": volume_id,
            "workspace_instance_id": workspace_instance_id,
        }

    @builtins.property
    def device(self) -> builtins.str:
        '''The Device of the VolumeAssociation resource.'''
        result = self._values.get("device")
        assert result is not None, "Required property 'device' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''The VolumeId of the VolumeAssociation resource.'''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_instance_id(self) -> builtins.str:
        '''The WorkspaceInstanceId of the VolumeAssociation resource.'''
        result = self._values.get("workspace_instance_id")
        assert result is not None, "Required property 'workspace_instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesinstances.VolumeReference",
    jsii_struct_bases=[],
    name_mapping={"volume_id": "volumeId"},
)
class VolumeReference:
    def __init__(self, *, volume_id: builtins.str) -> None:
        '''A reference to a Volume resource.

        :param volume_id: The VolumeId of the Volume resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesinstances as interfaces_workspacesinstances
            
            volume_reference = interfaces_workspacesinstances.VolumeReference(
                volume_id="volumeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a5be902e3139cc25c1339cd41edb16f2edda06d3d7beeedc8807600812fa200)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "volume_id": volume_id,
        }

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''The VolumeId of the Volume resource.'''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VolumeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesinstances.WorkspaceInstanceReference",
    jsii_struct_bases=[],
    name_mapping={"workspace_instance_id": "workspaceInstanceId"},
)
class WorkspaceInstanceReference:
    def __init__(self, *, workspace_instance_id: builtins.str) -> None:
        '''A reference to a WorkspaceInstance resource.

        :param workspace_instance_id: The WorkspaceInstanceId of the WorkspaceInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesinstances as interfaces_workspacesinstances
            
            workspace_instance_reference = interfaces_workspacesinstances.WorkspaceInstanceReference(
                workspace_instance_id="workspaceInstanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8743a728d792bfcf97090c84123155e04f8d9d3e8fa8f5fc38c5ac12f517080)
            check_type(argname="argument workspace_instance_id", value=workspace_instance_id, expected_type=type_hints["workspace_instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workspace_instance_id": workspace_instance_id,
        }

    @builtins.property
    def workspace_instance_id(self) -> builtins.str:
        '''The WorkspaceInstanceId of the WorkspaceInstance resource.'''
        result = self._values.get("workspace_instance_id")
        assert result is not None, "Required property 'workspace_instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspaceInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IVolumeAssociationRef",
    "IVolumeRef",
    "IWorkspaceInstanceRef",
    "VolumeAssociationReference",
    "VolumeReference",
    "WorkspaceInstanceReference",
]

publication.publish()

def _typecheckingstub__8d42d044ad84f26aeab835fd848713813856201672e3db8bf912fd1950d1358d(
    *,
    device: builtins.str,
    volume_id: builtins.str,
    workspace_instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a5be902e3139cc25c1339cd41edb16f2edda06d3d7beeedc8807600812fa200(
    *,
    volume_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8743a728d792bfcf97090c84123155e04f8d9d3e8fa8f5fc38c5ac12f517080(
    *,
    workspace_instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IVolumeAssociationRef, IVolumeRef, IWorkspaceInstanceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
