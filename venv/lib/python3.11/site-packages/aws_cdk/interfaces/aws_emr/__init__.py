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
    jsii_type="aws-cdk-lib.interfaces.aws_emr.ClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_id": "clusterId"},
)
class ClusterReference:
    def __init__(self, *, cluster_id: builtins.str) -> None:
        '''A reference to a Cluster resource.

        :param cluster_id: The Id of the Cluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emr as interfaces_emr
            
            cluster_reference = interfaces_emr.ClusterReference(
                cluster_id="clusterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb26faf26da6b6e132c7248c008afeda83d3b7eb2e886a3e304114ba22354966)
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_id": cluster_id,
        }

    @builtins.property
    def cluster_id(self) -> builtins.str:
        '''The Id of the Cluster resource.'''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_emr.IClusterRef")
class IClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Cluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        ...


class _IClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Cluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emr.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_emr.IInstanceFleetConfigRef")
class IInstanceFleetConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceFleetConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceFleetConfigRef")
    def instance_fleet_config_ref(self) -> "InstanceFleetConfigReference":
        '''(experimental) A reference to a InstanceFleetConfig resource.

        :stability: experimental
        '''
        ...


class _IInstanceFleetConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceFleetConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emr.IInstanceFleetConfigRef"

    @builtins.property
    @jsii.member(jsii_name="instanceFleetConfigRef")
    def instance_fleet_config_ref(self) -> "InstanceFleetConfigReference":
        '''(experimental) A reference to a InstanceFleetConfig resource.

        :stability: experimental
        '''
        return typing.cast("InstanceFleetConfigReference", jsii.get(self, "instanceFleetConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceFleetConfigRef).__jsii_proxy_class__ = lambda : _IInstanceFleetConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_emr.IInstanceGroupConfigRef")
class IInstanceGroupConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceGroupConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceGroupConfigRef")
    def instance_group_config_ref(self) -> "InstanceGroupConfigReference":
        '''(experimental) A reference to a InstanceGroupConfig resource.

        :stability: experimental
        '''
        ...


class _IInstanceGroupConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceGroupConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emr.IInstanceGroupConfigRef"

    @builtins.property
    @jsii.member(jsii_name="instanceGroupConfigRef")
    def instance_group_config_ref(self) -> "InstanceGroupConfigReference":
        '''(experimental) A reference to a InstanceGroupConfig resource.

        :stability: experimental
        '''
        return typing.cast("InstanceGroupConfigReference", jsii.get(self, "instanceGroupConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceGroupConfigRef).__jsii_proxy_class__ = lambda : _IInstanceGroupConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_emr.ISecurityConfigurationRef")
class ISecurityConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationRef")
    def security_configuration_ref(self) -> "SecurityConfigurationReference":
        '''(experimental) A reference to a SecurityConfiguration resource.

        :stability: experimental
        '''
        ...


class _ISecurityConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emr.ISecurityConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationRef")
    def security_configuration_ref(self) -> "SecurityConfigurationReference":
        '''(experimental) A reference to a SecurityConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("SecurityConfigurationReference", jsii.get(self, "securityConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityConfigurationRef).__jsii_proxy_class__ = lambda : _ISecurityConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_emr.IStepRef")
class IStepRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Step.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stepRef")
    def step_ref(self) -> "StepReference":
        '''(experimental) A reference to a Step resource.

        :stability: experimental
        '''
        ...


class _IStepRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Step.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emr.IStepRef"

    @builtins.property
    @jsii.member(jsii_name="stepRef")
    def step_ref(self) -> "StepReference":
        '''(experimental) A reference to a Step resource.

        :stability: experimental
        '''
        return typing.cast("StepReference", jsii.get(self, "stepRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStepRef).__jsii_proxy_class__ = lambda : _IStepRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_emr.IStudioRef")
class IStudioRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Studio.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="studioRef")
    def studio_ref(self) -> "StudioReference":
        '''(experimental) A reference to a Studio resource.

        :stability: experimental
        '''
        ...


class _IStudioRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Studio.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emr.IStudioRef"

    @builtins.property
    @jsii.member(jsii_name="studioRef")
    def studio_ref(self) -> "StudioReference":
        '''(experimental) A reference to a Studio resource.

        :stability: experimental
        '''
        return typing.cast("StudioReference", jsii.get(self, "studioRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStudioRef).__jsii_proxy_class__ = lambda : _IStudioRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_emr.IStudioSessionMappingRef")
class IStudioSessionMappingRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StudioSessionMapping.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="studioSessionMappingRef")
    def studio_session_mapping_ref(self) -> "StudioSessionMappingReference":
        '''(experimental) A reference to a StudioSessionMapping resource.

        :stability: experimental
        '''
        ...


class _IStudioSessionMappingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StudioSessionMapping.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emr.IStudioSessionMappingRef"

    @builtins.property
    @jsii.member(jsii_name="studioSessionMappingRef")
    def studio_session_mapping_ref(self) -> "StudioSessionMappingReference":
        '''(experimental) A reference to a StudioSessionMapping resource.

        :stability: experimental
        '''
        return typing.cast("StudioSessionMappingReference", jsii.get(self, "studioSessionMappingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStudioSessionMappingRef).__jsii_proxy_class__ = lambda : _IStudioSessionMappingRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_emr.IWALWorkspaceRef")
class IWALWorkspaceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WALWorkspace.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="walWorkspaceRef")
    def wal_workspace_ref(self) -> "WALWorkspaceReference":
        '''(experimental) A reference to a WALWorkspace resource.

        :stability: experimental
        '''
        ...


class _IWALWorkspaceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WALWorkspace.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_emr.IWALWorkspaceRef"

    @builtins.property
    @jsii.member(jsii_name="walWorkspaceRef")
    def wal_workspace_ref(self) -> "WALWorkspaceReference":
        '''(experimental) A reference to a WALWorkspace resource.

        :stability: experimental
        '''
        return typing.cast("WALWorkspaceReference", jsii.get(self, "walWorkspaceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWALWorkspaceRef).__jsii_proxy_class__ = lambda : _IWALWorkspaceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_emr.InstanceFleetConfigReference",
    jsii_struct_bases=[],
    name_mapping={"instance_fleet_config_id": "instanceFleetConfigId"},
)
class InstanceFleetConfigReference:
    def __init__(self, *, instance_fleet_config_id: builtins.str) -> None:
        '''A reference to a InstanceFleetConfig resource.

        :param instance_fleet_config_id: The Id of the InstanceFleetConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emr as interfaces_emr
            
            instance_fleet_config_reference = interfaces_emr.InstanceFleetConfigReference(
                instance_fleet_config_id="instanceFleetConfigId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eab7877a2d45d234b1d3068bffb62e7ebde897f5a905ade3c3ea3d070f83dbb2)
            check_type(argname="argument instance_fleet_config_id", value=instance_fleet_config_id, expected_type=type_hints["instance_fleet_config_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_fleet_config_id": instance_fleet_config_id,
        }

    @builtins.property
    def instance_fleet_config_id(self) -> builtins.str:
        '''The Id of the InstanceFleetConfig resource.'''
        result = self._values.get("instance_fleet_config_id")
        assert result is not None, "Required property 'instance_fleet_config_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceFleetConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_emr.InstanceGroupConfigReference",
    jsii_struct_bases=[],
    name_mapping={"instance_group_config_id": "instanceGroupConfigId"},
)
class InstanceGroupConfigReference:
    def __init__(self, *, instance_group_config_id: builtins.str) -> None:
        '''A reference to a InstanceGroupConfig resource.

        :param instance_group_config_id: The Id of the InstanceGroupConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emr as interfaces_emr
            
            instance_group_config_reference = interfaces_emr.InstanceGroupConfigReference(
                instance_group_config_id="instanceGroupConfigId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2e30f6fa847b8c87ef7ee08003bc534b03a5fe699d12bbffc55fbfd68d6628a)
            check_type(argname="argument instance_group_config_id", value=instance_group_config_id, expected_type=type_hints["instance_group_config_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_group_config_id": instance_group_config_id,
        }

    @builtins.property
    def instance_group_config_id(self) -> builtins.str:
        '''The Id of the InstanceGroupConfig resource.'''
        result = self._values.get("instance_group_config_id")
        assert result is not None, "Required property 'instance_group_config_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceGroupConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_emr.SecurityConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"security_configuration_name": "securityConfigurationName"},
)
class SecurityConfigurationReference:
    def __init__(self, *, security_configuration_name: builtins.str) -> None:
        '''A reference to a SecurityConfiguration resource.

        :param security_configuration_name: The Name of the SecurityConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emr as interfaces_emr
            
            security_configuration_reference = interfaces_emr.SecurityConfigurationReference(
                security_configuration_name="securityConfigurationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb700029a26f9af3fd64d96b6c5893bf9edb318eb93b8651a3d20e6bd81f9e34)
            check_type(argname="argument security_configuration_name", value=security_configuration_name, expected_type=type_hints["security_configuration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_configuration_name": security_configuration_name,
        }

    @builtins.property
    def security_configuration_name(self) -> builtins.str:
        '''The Name of the SecurityConfiguration resource.'''
        result = self._values.get("security_configuration_name")
        assert result is not None, "Required property 'security_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_emr.StepReference",
    jsii_struct_bases=[],
    name_mapping={"step_id": "stepId"},
)
class StepReference:
    def __init__(self, *, step_id: builtins.str) -> None:
        '''A reference to a Step resource.

        :param step_id: The Id of the Step resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emr as interfaces_emr
            
            step_reference = interfaces_emr.StepReference(
                step_id="stepId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__444fc315d7e16b117550af1e8318e44802b5a06f3fc0f7f20510a37113d8a87b)
            check_type(argname="argument step_id", value=step_id, expected_type=type_hints["step_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "step_id": step_id,
        }

    @builtins.property
    def step_id(self) -> builtins.str:
        '''The Id of the Step resource.'''
        result = self._values.get("step_id")
        assert result is not None, "Required property 'step_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StepReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_emr.StudioReference",
    jsii_struct_bases=[],
    name_mapping={"studio_arn": "studioArn", "studio_id": "studioId"},
)
class StudioReference:
    def __init__(self, *, studio_arn: builtins.str, studio_id: builtins.str) -> None:
        '''A reference to a Studio resource.

        :param studio_arn: The ARN of the Studio resource.
        :param studio_id: The StudioId of the Studio resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emr as interfaces_emr
            
            studio_reference = interfaces_emr.StudioReference(
                studio_arn="studioArn",
                studio_id="studioId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a600ab6bdf8ffaa929e128dab66554f33dcfe16b4066fb6aa63bcc126770cda)
            check_type(argname="argument studio_arn", value=studio_arn, expected_type=type_hints["studio_arn"])
            check_type(argname="argument studio_id", value=studio_id, expected_type=type_hints["studio_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "studio_arn": studio_arn,
            "studio_id": studio_id,
        }

    @builtins.property
    def studio_arn(self) -> builtins.str:
        '''The ARN of the Studio resource.'''
        result = self._values.get("studio_arn")
        assert result is not None, "Required property 'studio_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''The StudioId of the Studio resource.'''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StudioReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_emr.StudioSessionMappingReference",
    jsii_struct_bases=[],
    name_mapping={
        "identity_name": "identityName",
        "identity_type": "identityType",
        "studio_id": "studioId",
    },
)
class StudioSessionMappingReference:
    def __init__(
        self,
        *,
        identity_name: builtins.str,
        identity_type: builtins.str,
        studio_id: builtins.str,
    ) -> None:
        '''A reference to a StudioSessionMapping resource.

        :param identity_name: The IdentityName of the StudioSessionMapping resource.
        :param identity_type: The IdentityType of the StudioSessionMapping resource.
        :param studio_id: The StudioId of the StudioSessionMapping resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emr as interfaces_emr
            
            studio_session_mapping_reference = interfaces_emr.StudioSessionMappingReference(
                identity_name="identityName",
                identity_type="identityType",
                studio_id="studioId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b27823da82ec66c90255b69477281f26ccdf943552114a84aad8f5a11659918d)
            check_type(argname="argument identity_name", value=identity_name, expected_type=type_hints["identity_name"])
            check_type(argname="argument identity_type", value=identity_type, expected_type=type_hints["identity_type"])
            check_type(argname="argument studio_id", value=studio_id, expected_type=type_hints["studio_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_name": identity_name,
            "identity_type": identity_type,
            "studio_id": studio_id,
        }

    @builtins.property
    def identity_name(self) -> builtins.str:
        '''The IdentityName of the StudioSessionMapping resource.'''
        result = self._values.get("identity_name")
        assert result is not None, "Required property 'identity_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_type(self) -> builtins.str:
        '''The IdentityType of the StudioSessionMapping resource.'''
        result = self._values.get("identity_type")
        assert result is not None, "Required property 'identity_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def studio_id(self) -> builtins.str:
        '''The StudioId of the StudioSessionMapping resource.'''
        result = self._values.get("studio_id")
        assert result is not None, "Required property 'studio_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StudioSessionMappingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_emr.WALWorkspaceReference",
    jsii_struct_bases=[],
    name_mapping={"wal_workspace_name": "walWorkspaceName"},
)
class WALWorkspaceReference:
    def __init__(self, *, wal_workspace_name: builtins.str) -> None:
        '''A reference to a WALWorkspace resource.

        :param wal_workspace_name: The WALWorkspaceName of the WALWorkspace resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_emr as interfaces_emr
            
            w_aLWorkspace_reference = interfaces_emr.WALWorkspaceReference(
                wal_workspace_name="walWorkspaceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__017fbf9161ded0e36a82795be0af3523a833328b1deac1d84b1997641128cd10)
            check_type(argname="argument wal_workspace_name", value=wal_workspace_name, expected_type=type_hints["wal_workspace_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "wal_workspace_name": wal_workspace_name,
        }

    @builtins.property
    def wal_workspace_name(self) -> builtins.str:
        '''The WALWorkspaceName of the WALWorkspace resource.'''
        result = self._values.get("wal_workspace_name")
        assert result is not None, "Required property 'wal_workspace_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WALWorkspaceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ClusterReference",
    "IClusterRef",
    "IInstanceFleetConfigRef",
    "IInstanceGroupConfigRef",
    "ISecurityConfigurationRef",
    "IStepRef",
    "IStudioRef",
    "IStudioSessionMappingRef",
    "IWALWorkspaceRef",
    "InstanceFleetConfigReference",
    "InstanceGroupConfigReference",
    "SecurityConfigurationReference",
    "StepReference",
    "StudioReference",
    "StudioSessionMappingReference",
    "WALWorkspaceReference",
]

publication.publish()

def _typecheckingstub__eb26faf26da6b6e132c7248c008afeda83d3b7eb2e886a3e304114ba22354966(
    *,
    cluster_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eab7877a2d45d234b1d3068bffb62e7ebde897f5a905ade3c3ea3d070f83dbb2(
    *,
    instance_fleet_config_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2e30f6fa847b8c87ef7ee08003bc534b03a5fe699d12bbffc55fbfd68d6628a(
    *,
    instance_group_config_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb700029a26f9af3fd64d96b6c5893bf9edb318eb93b8651a3d20e6bd81f9e34(
    *,
    security_configuration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__444fc315d7e16b117550af1e8318e44802b5a06f3fc0f7f20510a37113d8a87b(
    *,
    step_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a600ab6bdf8ffaa929e128dab66554f33dcfe16b4066fb6aa63bcc126770cda(
    *,
    studio_arn: builtins.str,
    studio_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b27823da82ec66c90255b69477281f26ccdf943552114a84aad8f5a11659918d(
    *,
    identity_name: builtins.str,
    identity_type: builtins.str,
    studio_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__017fbf9161ded0e36a82795be0af3523a833328b1deac1d84b1997641128cd10(
    *,
    wal_workspace_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IClusterRef, IInstanceFleetConfigRef, IInstanceGroupConfigRef, ISecurityConfigurationRef, IStepRef, IStudioRef, IStudioSessionMappingRef, IWALWorkspaceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
