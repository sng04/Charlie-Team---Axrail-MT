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
    jsii_type="aws-cdk-lib.interfaces.aws_ssm.AssociationReference",
    jsii_struct_bases=[],
    name_mapping={"association_id": "associationId"},
)
class AssociationReference:
    def __init__(self, *, association_id: builtins.str) -> None:
        '''A reference to a Association resource.

        :param association_id: The AssociationId of the Association resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssm as interfaces_ssm
            
            association_reference = interfaces_ssm.AssociationReference(
                association_id="associationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__775cc1fff0c5bb13a3195ec65e12083c34d45a6e8ae92b01ac08b89b1d2dc956)
            check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_id": association_id,
        }

    @builtins.property
    def association_id(self) -> builtins.str:
        '''The AssociationId of the Association resource.'''
        result = self._values.get("association_id")
        assert result is not None, "Required property 'association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssm.DocumentReference",
    jsii_struct_bases=[],
    name_mapping={"document_name": "documentName"},
)
class DocumentReference:
    def __init__(self, *, document_name: builtins.str) -> None:
        '''A reference to a Document resource.

        :param document_name: The Name of the Document resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssm as interfaces_ssm
            
            document_reference = interfaces_ssm.DocumentReference(
                document_name="documentName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcb6101d3c62b0309a6bc1a2847a94afe116c447d404db2cbbf9e653f97509ab)
            check_type(argname="argument document_name", value=document_name, expected_type=type_hints["document_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "document_name": document_name,
        }

    @builtins.property
    def document_name(self) -> builtins.str:
        '''The Name of the Document resource.'''
        result = self._values.get("document_name")
        assert result is not None, "Required property 'document_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DocumentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssm.IAssociationRef")
class IAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Association.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="associationRef")
    def association_ref(self) -> "AssociationReference":
        '''(experimental) A reference to a Association resource.

        :stability: experimental
        '''
        ...


class _IAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Association.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssm.IAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="associationRef")
    def association_ref(self) -> "AssociationReference":
        '''(experimental) A reference to a Association resource.

        :stability: experimental
        '''
        return typing.cast("AssociationReference", jsii.get(self, "associationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssociationRef).__jsii_proxy_class__ = lambda : _IAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssm.IDocumentRef")
class IDocumentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Document.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="documentRef")
    def document_ref(self) -> "DocumentReference":
        '''(experimental) A reference to a Document resource.

        :stability: experimental
        '''
        ...


class _IDocumentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Document.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssm.IDocumentRef"

    @builtins.property
    @jsii.member(jsii_name="documentRef")
    def document_ref(self) -> "DocumentReference":
        '''(experimental) A reference to a Document resource.

        :stability: experimental
        '''
        return typing.cast("DocumentReference", jsii.get(self, "documentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDocumentRef).__jsii_proxy_class__ = lambda : _IDocumentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssm.IMaintenanceWindowRef")
class IMaintenanceWindowRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MaintenanceWindow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowRef")
    def maintenance_window_ref(self) -> "MaintenanceWindowReference":
        '''(experimental) A reference to a MaintenanceWindow resource.

        :stability: experimental
        '''
        ...


class _IMaintenanceWindowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MaintenanceWindow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssm.IMaintenanceWindowRef"

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowRef")
    def maintenance_window_ref(self) -> "MaintenanceWindowReference":
        '''(experimental) A reference to a MaintenanceWindow resource.

        :stability: experimental
        '''
        return typing.cast("MaintenanceWindowReference", jsii.get(self, "maintenanceWindowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMaintenanceWindowRef).__jsii_proxy_class__ = lambda : _IMaintenanceWindowRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssm.IMaintenanceWindowTargetRef")
class IMaintenanceWindowTargetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MaintenanceWindowTarget.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowTargetRef")
    def maintenance_window_target_ref(self) -> "MaintenanceWindowTargetReference":
        '''(experimental) A reference to a MaintenanceWindowTarget resource.

        :stability: experimental
        '''
        ...


class _IMaintenanceWindowTargetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MaintenanceWindowTarget.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssm.IMaintenanceWindowTargetRef"

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowTargetRef")
    def maintenance_window_target_ref(self) -> "MaintenanceWindowTargetReference":
        '''(experimental) A reference to a MaintenanceWindowTarget resource.

        :stability: experimental
        '''
        return typing.cast("MaintenanceWindowTargetReference", jsii.get(self, "maintenanceWindowTargetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMaintenanceWindowTargetRef).__jsii_proxy_class__ = lambda : _IMaintenanceWindowTargetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssm.IMaintenanceWindowTaskRef")
class IMaintenanceWindowTaskRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MaintenanceWindowTask.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowTaskRef")
    def maintenance_window_task_ref(self) -> "MaintenanceWindowTaskReference":
        '''(experimental) A reference to a MaintenanceWindowTask resource.

        :stability: experimental
        '''
        ...


class _IMaintenanceWindowTaskRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MaintenanceWindowTask.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssm.IMaintenanceWindowTaskRef"

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowTaskRef")
    def maintenance_window_task_ref(self) -> "MaintenanceWindowTaskReference":
        '''(experimental) A reference to a MaintenanceWindowTask resource.

        :stability: experimental
        '''
        return typing.cast("MaintenanceWindowTaskReference", jsii.get(self, "maintenanceWindowTaskRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMaintenanceWindowTaskRef).__jsii_proxy_class__ = lambda : _IMaintenanceWindowTaskRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssm.IParameterRef")
class IParameterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Parameter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="parameterRef")
    def parameter_ref(self) -> "ParameterReference":
        '''(experimental) A reference to a Parameter resource.

        :stability: experimental
        '''
        ...


class _IParameterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Parameter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssm.IParameterRef"

    @builtins.property
    @jsii.member(jsii_name="parameterRef")
    def parameter_ref(self) -> "ParameterReference":
        '''(experimental) A reference to a Parameter resource.

        :stability: experimental
        '''
        return typing.cast("ParameterReference", jsii.get(self, "parameterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParameterRef).__jsii_proxy_class__ = lambda : _IParameterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssm.IPatchBaselineRef")
class IPatchBaselineRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PatchBaseline.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="patchBaselineRef")
    def patch_baseline_ref(self) -> "PatchBaselineReference":
        '''(experimental) A reference to a PatchBaseline resource.

        :stability: experimental
        '''
        ...


class _IPatchBaselineRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PatchBaseline.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssm.IPatchBaselineRef"

    @builtins.property
    @jsii.member(jsii_name="patchBaselineRef")
    def patch_baseline_ref(self) -> "PatchBaselineReference":
        '''(experimental) A reference to a PatchBaseline resource.

        :stability: experimental
        '''
        return typing.cast("PatchBaselineReference", jsii.get(self, "patchBaselineRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPatchBaselineRef).__jsii_proxy_class__ = lambda : _IPatchBaselineRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssm.IResourceDataSyncRef")
class IResourceDataSyncRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceDataSync.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceDataSyncRef")
    def resource_data_sync_ref(self) -> "ResourceDataSyncReference":
        '''(experimental) A reference to a ResourceDataSync resource.

        :stability: experimental
        '''
        ...


class _IResourceDataSyncRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceDataSync.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssm.IResourceDataSyncRef"

    @builtins.property
    @jsii.member(jsii_name="resourceDataSyncRef")
    def resource_data_sync_ref(self) -> "ResourceDataSyncReference":
        '''(experimental) A reference to a ResourceDataSync resource.

        :stability: experimental
        '''
        return typing.cast("ResourceDataSyncReference", jsii.get(self, "resourceDataSyncRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceDataSyncRef).__jsii_proxy_class__ = lambda : _IResourceDataSyncRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ssm.IResourcePolicyRef")
class IResourcePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        ...


class _IResourcePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssm.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssm.MaintenanceWindowReference",
    jsii_struct_bases=[],
    name_mapping={"window_id": "windowId"},
)
class MaintenanceWindowReference:
    def __init__(self, *, window_id: builtins.str) -> None:
        '''A reference to a MaintenanceWindow resource.

        :param window_id: The WindowId of the MaintenanceWindow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssm as interfaces_ssm
            
            maintenance_window_reference = interfaces_ssm.MaintenanceWindowReference(
                window_id="windowId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cb33a09c3dfc7973432d718faac07715f6677b4083711351d04c330763c198d)
            check_type(argname="argument window_id", value=window_id, expected_type=type_hints["window_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "window_id": window_id,
        }

    @builtins.property
    def window_id(self) -> builtins.str:
        '''The WindowId of the MaintenanceWindow resource.'''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MaintenanceWindowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssm.MaintenanceWindowTargetReference",
    jsii_struct_bases=[],
    name_mapping={"window_id": "windowId", "window_target_id": "windowTargetId"},
)
class MaintenanceWindowTargetReference:
    def __init__(
        self,
        *,
        window_id: builtins.str,
        window_target_id: builtins.str,
    ) -> None:
        '''A reference to a MaintenanceWindowTarget resource.

        :param window_id: The WindowId of the MaintenanceWindowTarget resource.
        :param window_target_id: The WindowTargetId of the MaintenanceWindowTarget resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssm as interfaces_ssm
            
            maintenance_window_target_reference = interfaces_ssm.MaintenanceWindowTargetReference(
                window_id="windowId",
                window_target_id="windowTargetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc7aececd4d9fd7cb0a70989a13064463485da38e07d1eaa1206e9cd8f73d5d2)
            check_type(argname="argument window_id", value=window_id, expected_type=type_hints["window_id"])
            check_type(argname="argument window_target_id", value=window_target_id, expected_type=type_hints["window_target_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "window_id": window_id,
            "window_target_id": window_target_id,
        }

    @builtins.property
    def window_id(self) -> builtins.str:
        '''The WindowId of the MaintenanceWindowTarget resource.'''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def window_target_id(self) -> builtins.str:
        '''The WindowTargetId of the MaintenanceWindowTarget resource.'''
        result = self._values.get("window_target_id")
        assert result is not None, "Required property 'window_target_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MaintenanceWindowTargetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssm.MaintenanceWindowTaskReference",
    jsii_struct_bases=[],
    name_mapping={"window_id": "windowId", "window_task_id": "windowTaskId"},
)
class MaintenanceWindowTaskReference:
    def __init__(
        self,
        *,
        window_id: builtins.str,
        window_task_id: builtins.str,
    ) -> None:
        '''A reference to a MaintenanceWindowTask resource.

        :param window_id: The WindowId of the MaintenanceWindowTask resource.
        :param window_task_id: The WindowTaskId of the MaintenanceWindowTask resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssm as interfaces_ssm
            
            maintenance_window_task_reference = interfaces_ssm.MaintenanceWindowTaskReference(
                window_id="windowId",
                window_task_id="windowTaskId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a84f17a335bbe7c6ba37477bd79adba76a951afd9da1ec43ae2a7499c062733f)
            check_type(argname="argument window_id", value=window_id, expected_type=type_hints["window_id"])
            check_type(argname="argument window_task_id", value=window_task_id, expected_type=type_hints["window_task_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "window_id": window_id,
            "window_task_id": window_task_id,
        }

    @builtins.property
    def window_id(self) -> builtins.str:
        '''The WindowId of the MaintenanceWindowTask resource.'''
        result = self._values.get("window_id")
        assert result is not None, "Required property 'window_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def window_task_id(self) -> builtins.str:
        '''The WindowTaskId of the MaintenanceWindowTask resource.'''
        result = self._values.get("window_task_id")
        assert result is not None, "Required property 'window_task_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MaintenanceWindowTaskReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssm.ParameterReference",
    jsii_struct_bases=[],
    name_mapping={"parameter_name": "parameterName"},
)
class ParameterReference:
    def __init__(self, *, parameter_name: builtins.str) -> None:
        '''A reference to a Parameter resource.

        :param parameter_name: The Name of the Parameter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssm as interfaces_ssm
            
            parameter_reference = interfaces_ssm.ParameterReference(
                parameter_name="parameterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cda39a1fa0093c99b1bbd37f52b1d52b1ddd1c2c6ae9eb197226b61a63c9e49)
            check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_name": parameter_name,
        }

    @builtins.property
    def parameter_name(self) -> builtins.str:
        '''The Name of the Parameter resource.'''
        result = self._values.get("parameter_name")
        assert result is not None, "Required property 'parameter_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParameterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssm.PatchBaselineReference",
    jsii_struct_bases=[],
    name_mapping={"patch_baseline_id": "patchBaselineId"},
)
class PatchBaselineReference:
    def __init__(self, *, patch_baseline_id: builtins.str) -> None:
        '''A reference to a PatchBaseline resource.

        :param patch_baseline_id: The Id of the PatchBaseline resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssm as interfaces_ssm
            
            patch_baseline_reference = interfaces_ssm.PatchBaselineReference(
                patch_baseline_id="patchBaselineId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d38742fd3f9891646ab25cf167f2c29b28b5f57b8f0c6475eceb2a5c8a8ce7c7)
            check_type(argname="argument patch_baseline_id", value=patch_baseline_id, expected_type=type_hints["patch_baseline_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "patch_baseline_id": patch_baseline_id,
        }

    @builtins.property
    def patch_baseline_id(self) -> builtins.str:
        '''The Id of the PatchBaseline resource.'''
        result = self._values.get("patch_baseline_id")
        assert result is not None, "Required property 'patch_baseline_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PatchBaselineReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssm.ResourceDataSyncReference",
    jsii_struct_bases=[],
    name_mapping={"sync_name": "syncName"},
)
class ResourceDataSyncReference:
    def __init__(self, *, sync_name: builtins.str) -> None:
        '''A reference to a ResourceDataSync resource.

        :param sync_name: The SyncName of the ResourceDataSync resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssm as interfaces_ssm
            
            resource_data_sync_reference = interfaces_ssm.ResourceDataSyncReference(
                sync_name="syncName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c828c669554ca1cd6c34cbdf3b2e519d30f0114e72e73595e3ebbdb3b97abdea)
            check_type(argname="argument sync_name", value=sync_name, expected_type=type_hints["sync_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sync_name": sync_name,
        }

    @builtins.property
    def sync_name(self) -> builtins.str:
        '''The SyncName of the ResourceDataSync resource.'''
        result = self._values.get("sync_name")
        assert result is not None, "Required property 'sync_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceDataSyncReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssm.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_id": "policyId", "resource_arn": "resourceArn"},
)
class ResourcePolicyReference:
    def __init__(self, *, policy_id: builtins.str, resource_arn: builtins.str) -> None:
        '''A reference to a ResourcePolicy resource.

        :param policy_id: The PolicyId of the ResourcePolicy resource.
        :param resource_arn: The ResourceArn of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssm as interfaces_ssm
            
            resource_policy_reference = interfaces_ssm.ResourcePolicyReference(
                policy_id="policyId",
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__624afa9dab00ea919f3780ec78ff1eba149e1b5a7a7f48fbce5c7d0bf6b1d84f)
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_id": policy_id,
            "resource_arn": resource_arn,
        }

    @builtins.property
    def policy_id(self) -> builtins.str:
        '''The PolicyId of the ResourcePolicy resource.'''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceArn of the ResourcePolicy resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AssociationReference",
    "DocumentReference",
    "IAssociationRef",
    "IDocumentRef",
    "IMaintenanceWindowRef",
    "IMaintenanceWindowTargetRef",
    "IMaintenanceWindowTaskRef",
    "IParameterRef",
    "IPatchBaselineRef",
    "IResourceDataSyncRef",
    "IResourcePolicyRef",
    "MaintenanceWindowReference",
    "MaintenanceWindowTargetReference",
    "MaintenanceWindowTaskReference",
    "ParameterReference",
    "PatchBaselineReference",
    "ResourceDataSyncReference",
    "ResourcePolicyReference",
]

publication.publish()

def _typecheckingstub__775cc1fff0c5bb13a3195ec65e12083c34d45a6e8ae92b01ac08b89b1d2dc956(
    *,
    association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb6101d3c62b0309a6bc1a2847a94afe116c447d404db2cbbf9e653f97509ab(
    *,
    document_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb33a09c3dfc7973432d718faac07715f6677b4083711351d04c330763c198d(
    *,
    window_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc7aececd4d9fd7cb0a70989a13064463485da38e07d1eaa1206e9cd8f73d5d2(
    *,
    window_id: builtins.str,
    window_target_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a84f17a335bbe7c6ba37477bd79adba76a951afd9da1ec43ae2a7499c062733f(
    *,
    window_id: builtins.str,
    window_task_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cda39a1fa0093c99b1bbd37f52b1d52b1ddd1c2c6ae9eb197226b61a63c9e49(
    *,
    parameter_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d38742fd3f9891646ab25cf167f2c29b28b5f57b8f0c6475eceb2a5c8a8ce7c7(
    *,
    patch_baseline_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c828c669554ca1cd6c34cbdf3b2e519d30f0114e72e73595e3ebbdb3b97abdea(
    *,
    sync_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__624afa9dab00ea919f3780ec78ff1eba149e1b5a7a7f48fbce5c7d0bf6b1d84f(
    *,
    policy_id: builtins.str,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAssociationRef, IDocumentRef, IMaintenanceWindowRef, IMaintenanceWindowTargetRef, IMaintenanceWindowTaskRef, IParameterRef, IPatchBaselineRef, IResourceDataSyncRef, IResourcePolicyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
