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
    jsii_type="aws-cdk-lib.interfaces.aws_iottwinmaker.ComponentTypeReference",
    jsii_struct_bases=[],
    name_mapping={
        "component_type_arn": "componentTypeArn",
        "component_type_id": "componentTypeId",
        "workspace_id": "workspaceId",
    },
)
class ComponentTypeReference:
    def __init__(
        self,
        *,
        component_type_arn: builtins.str,
        component_type_id: builtins.str,
        workspace_id: builtins.str,
    ) -> None:
        '''A reference to a ComponentType resource.

        :param component_type_arn: The ARN of the ComponentType resource.
        :param component_type_id: The ComponentTypeId of the ComponentType resource.
        :param workspace_id: The WorkspaceId of the ComponentType resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iottwinmaker as interfaces_iottwinmaker
            
            component_type_reference = interfaces_iottwinmaker.ComponentTypeReference(
                component_type_arn="componentTypeArn",
                component_type_id="componentTypeId",
                workspace_id="workspaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dc685c1089bb9a53de50b842233c9155fdc148333fff5ed8fcc367aef938790)
            check_type(argname="argument component_type_arn", value=component_type_arn, expected_type=type_hints["component_type_arn"])
            check_type(argname="argument component_type_id", value=component_type_id, expected_type=type_hints["component_type_id"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "component_type_arn": component_type_arn,
            "component_type_id": component_type_id,
            "workspace_id": workspace_id,
        }

    @builtins.property
    def component_type_arn(self) -> builtins.str:
        '''The ARN of the ComponentType resource.'''
        result = self._values.get("component_type_arn")
        assert result is not None, "Required property 'component_type_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def component_type_id(self) -> builtins.str:
        '''The ComponentTypeId of the ComponentType resource.'''
        result = self._values.get("component_type_id")
        assert result is not None, "Required property 'component_type_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_id(self) -> builtins.str:
        '''The WorkspaceId of the ComponentType resource.'''
        result = self._values.get("workspace_id")
        assert result is not None, "Required property 'workspace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComponentTypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iottwinmaker.EntityReference",
    jsii_struct_bases=[],
    name_mapping={
        "entity_arn": "entityArn",
        "entity_id": "entityId",
        "workspace_id": "workspaceId",
    },
)
class EntityReference:
    def __init__(
        self,
        *,
        entity_arn: builtins.str,
        entity_id: builtins.str,
        workspace_id: builtins.str,
    ) -> None:
        '''A reference to a Entity resource.

        :param entity_arn: The ARN of the Entity resource.
        :param entity_id: The EntityId of the Entity resource.
        :param workspace_id: The WorkspaceId of the Entity resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iottwinmaker as interfaces_iottwinmaker
            
            entity_reference = interfaces_iottwinmaker.EntityReference(
                entity_arn="entityArn",
                entity_id="entityId",
                workspace_id="workspaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01af4d013f53806e57baa99c7c74a274a25ee2b767a2291fbf71578f88d3bcea)
            check_type(argname="argument entity_arn", value=entity_arn, expected_type=type_hints["entity_arn"])
            check_type(argname="argument entity_id", value=entity_id, expected_type=type_hints["entity_id"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "entity_arn": entity_arn,
            "entity_id": entity_id,
            "workspace_id": workspace_id,
        }

    @builtins.property
    def entity_arn(self) -> builtins.str:
        '''The ARN of the Entity resource.'''
        result = self._values.get("entity_arn")
        assert result is not None, "Required property 'entity_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def entity_id(self) -> builtins.str:
        '''The EntityId of the Entity resource.'''
        result = self._values.get("entity_id")
        assert result is not None, "Required property 'entity_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_id(self) -> builtins.str:
        '''The WorkspaceId of the Entity resource.'''
        result = self._values.get("workspace_id")
        assert result is not None, "Required property 'workspace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EntityReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iottwinmaker.IComponentTypeRef")
class IComponentTypeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ComponentType.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="componentTypeRef")
    def component_type_ref(self) -> "ComponentTypeReference":
        '''(experimental) A reference to a ComponentType resource.

        :stability: experimental
        '''
        ...


class _IComponentTypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ComponentType.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iottwinmaker.IComponentTypeRef"

    @builtins.property
    @jsii.member(jsii_name="componentTypeRef")
    def component_type_ref(self) -> "ComponentTypeReference":
        '''(experimental) A reference to a ComponentType resource.

        :stability: experimental
        '''
        return typing.cast("ComponentTypeReference", jsii.get(self, "componentTypeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IComponentTypeRef).__jsii_proxy_class__ = lambda : _IComponentTypeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iottwinmaker.IEntityRef")
class IEntityRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Entity.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="entityRef")
    def entity_ref(self) -> "EntityReference":
        '''(experimental) A reference to a Entity resource.

        :stability: experimental
        '''
        ...


class _IEntityRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Entity.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iottwinmaker.IEntityRef"

    @builtins.property
    @jsii.member(jsii_name="entityRef")
    def entity_ref(self) -> "EntityReference":
        '''(experimental) A reference to a Entity resource.

        :stability: experimental
        '''
        return typing.cast("EntityReference", jsii.get(self, "entityRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEntityRef).__jsii_proxy_class__ = lambda : _IEntityRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iottwinmaker.ISceneRef")
class ISceneRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Scene.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sceneRef")
    def scene_ref(self) -> "SceneReference":
        '''(experimental) A reference to a Scene resource.

        :stability: experimental
        '''
        ...


class _ISceneRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Scene.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iottwinmaker.ISceneRef"

    @builtins.property
    @jsii.member(jsii_name="sceneRef")
    def scene_ref(self) -> "SceneReference":
        '''(experimental) A reference to a Scene resource.

        :stability: experimental
        '''
        return typing.cast("SceneReference", jsii.get(self, "sceneRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISceneRef).__jsii_proxy_class__ = lambda : _ISceneRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iottwinmaker.ISyncJobRef")
class ISyncJobRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SyncJob.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="syncJobRef")
    def sync_job_ref(self) -> "SyncJobReference":
        '''(experimental) A reference to a SyncJob resource.

        :stability: experimental
        '''
        ...


class _ISyncJobRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SyncJob.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iottwinmaker.ISyncJobRef"

    @builtins.property
    @jsii.member(jsii_name="syncJobRef")
    def sync_job_ref(self) -> "SyncJobReference":
        '''(experimental) A reference to a SyncJob resource.

        :stability: experimental
        '''
        return typing.cast("SyncJobReference", jsii.get(self, "syncJobRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISyncJobRef).__jsii_proxy_class__ = lambda : _ISyncJobRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iottwinmaker.IWorkspaceRef")
class IWorkspaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workspace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workspaceRef")
    def workspace_ref(self) -> "WorkspaceReference":
        '''(experimental) A reference to a Workspace resource.

        :stability: experimental
        '''
        ...


class _IWorkspaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workspace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iottwinmaker.IWorkspaceRef"

    @builtins.property
    @jsii.member(jsii_name="workspaceRef")
    def workspace_ref(self) -> "WorkspaceReference":
        '''(experimental) A reference to a Workspace resource.

        :stability: experimental
        '''
        return typing.cast("WorkspaceReference", jsii.get(self, "workspaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkspaceRef).__jsii_proxy_class__ = lambda : _IWorkspaceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iottwinmaker.SceneReference",
    jsii_struct_bases=[],
    name_mapping={
        "scene_arn": "sceneArn",
        "scene_id": "sceneId",
        "workspace_id": "workspaceId",
    },
)
class SceneReference:
    def __init__(
        self,
        *,
        scene_arn: builtins.str,
        scene_id: builtins.str,
        workspace_id: builtins.str,
    ) -> None:
        '''A reference to a Scene resource.

        :param scene_arn: The ARN of the Scene resource.
        :param scene_id: The SceneId of the Scene resource.
        :param workspace_id: The WorkspaceId of the Scene resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iottwinmaker as interfaces_iottwinmaker
            
            scene_reference = interfaces_iottwinmaker.SceneReference(
                scene_arn="sceneArn",
                scene_id="sceneId",
                workspace_id="workspaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f667fc053086b3ea2a81d4089672740702dd500bc1cbf71a567b116aab474c77)
            check_type(argname="argument scene_arn", value=scene_arn, expected_type=type_hints["scene_arn"])
            check_type(argname="argument scene_id", value=scene_id, expected_type=type_hints["scene_id"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scene_arn": scene_arn,
            "scene_id": scene_id,
            "workspace_id": workspace_id,
        }

    @builtins.property
    def scene_arn(self) -> builtins.str:
        '''The ARN of the Scene resource.'''
        result = self._values.get("scene_arn")
        assert result is not None, "Required property 'scene_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scene_id(self) -> builtins.str:
        '''The SceneId of the Scene resource.'''
        result = self._values.get("scene_id")
        assert result is not None, "Required property 'scene_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_id(self) -> builtins.str:
        '''The WorkspaceId of the Scene resource.'''
        result = self._values.get("workspace_id")
        assert result is not None, "Required property 'workspace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SceneReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iottwinmaker.SyncJobReference",
    jsii_struct_bases=[],
    name_mapping={
        "sync_job_arn": "syncJobArn",
        "sync_source": "syncSource",
        "workspace_id": "workspaceId",
    },
)
class SyncJobReference:
    def __init__(
        self,
        *,
        sync_job_arn: builtins.str,
        sync_source: builtins.str,
        workspace_id: builtins.str,
    ) -> None:
        '''A reference to a SyncJob resource.

        :param sync_job_arn: The ARN of the SyncJob resource.
        :param sync_source: The SyncSource of the SyncJob resource.
        :param workspace_id: The WorkspaceId of the SyncJob resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iottwinmaker as interfaces_iottwinmaker
            
            sync_job_reference = interfaces_iottwinmaker.SyncJobReference(
                sync_job_arn="syncJobArn",
                sync_source="syncSource",
                workspace_id="workspaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7450525f998dd1f23de2b8b96a6c1d4c86117ae84db291e29753a00d2b3ae80)
            check_type(argname="argument sync_job_arn", value=sync_job_arn, expected_type=type_hints["sync_job_arn"])
            check_type(argname="argument sync_source", value=sync_source, expected_type=type_hints["sync_source"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sync_job_arn": sync_job_arn,
            "sync_source": sync_source,
            "workspace_id": workspace_id,
        }

    @builtins.property
    def sync_job_arn(self) -> builtins.str:
        '''The ARN of the SyncJob resource.'''
        result = self._values.get("sync_job_arn")
        assert result is not None, "Required property 'sync_job_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sync_source(self) -> builtins.str:
        '''The SyncSource of the SyncJob resource.'''
        result = self._values.get("sync_source")
        assert result is not None, "Required property 'sync_source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_id(self) -> builtins.str:
        '''The WorkspaceId of the SyncJob resource.'''
        result = self._values.get("workspace_id")
        assert result is not None, "Required property 'workspace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyncJobReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iottwinmaker.WorkspaceReference",
    jsii_struct_bases=[],
    name_mapping={"workspace_arn": "workspaceArn", "workspace_id": "workspaceId"},
)
class WorkspaceReference:
    def __init__(
        self,
        *,
        workspace_arn: builtins.str,
        workspace_id: builtins.str,
    ) -> None:
        '''A reference to a Workspace resource.

        :param workspace_arn: The ARN of the Workspace resource.
        :param workspace_id: The WorkspaceId of the Workspace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iottwinmaker as interfaces_iottwinmaker
            
            workspace_reference = interfaces_iottwinmaker.WorkspaceReference(
                workspace_arn="workspaceArn",
                workspace_id="workspaceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cd3eb4cf296b893ef22d67a42efb8885efb092d0142b5a3c4c9949f2caa06d3)
            check_type(argname="argument workspace_arn", value=workspace_arn, expected_type=type_hints["workspace_arn"])
            check_type(argname="argument workspace_id", value=workspace_id, expected_type=type_hints["workspace_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workspace_arn": workspace_arn,
            "workspace_id": workspace_id,
        }

    @builtins.property
    def workspace_arn(self) -> builtins.str:
        '''The ARN of the Workspace resource.'''
        result = self._values.get("workspace_arn")
        assert result is not None, "Required property 'workspace_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workspace_id(self) -> builtins.str:
        '''The WorkspaceId of the Workspace resource.'''
        result = self._values.get("workspace_id")
        assert result is not None, "Required property 'workspace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkspaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ComponentTypeReference",
    "EntityReference",
    "IComponentTypeRef",
    "IEntityRef",
    "ISceneRef",
    "ISyncJobRef",
    "IWorkspaceRef",
    "SceneReference",
    "SyncJobReference",
    "WorkspaceReference",
]

publication.publish()

def _typecheckingstub__6dc685c1089bb9a53de50b842233c9155fdc148333fff5ed8fcc367aef938790(
    *,
    component_type_arn: builtins.str,
    component_type_id: builtins.str,
    workspace_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01af4d013f53806e57baa99c7c74a274a25ee2b767a2291fbf71578f88d3bcea(
    *,
    entity_arn: builtins.str,
    entity_id: builtins.str,
    workspace_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f667fc053086b3ea2a81d4089672740702dd500bc1cbf71a567b116aab474c77(
    *,
    scene_arn: builtins.str,
    scene_id: builtins.str,
    workspace_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7450525f998dd1f23de2b8b96a6c1d4c86117ae84db291e29753a00d2b3ae80(
    *,
    sync_job_arn: builtins.str,
    sync_source: builtins.str,
    workspace_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cd3eb4cf296b893ef22d67a42efb8885efb092d0142b5a3c4c9949f2caa06d3(
    *,
    workspace_arn: builtins.str,
    workspace_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IComponentTypeRef, IEntityRef, ISceneRef, ISyncJobRef, IWorkspaceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
