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
    jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.AutoScalingGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling_group_arn": "autoScalingGroupArn",
        "auto_scaling_group_name": "autoScalingGroupName",
    },
)
class AutoScalingGroupReference:
    def __init__(
        self,
        *,
        auto_scaling_group_arn: builtins.str,
        auto_scaling_group_name: builtins.str,
    ) -> None:
        '''A reference to a AutoScalingGroup resource.

        :param auto_scaling_group_arn: The ARN of the AutoScalingGroup resource.
        :param auto_scaling_group_name: The AutoScalingGroupName of the AutoScalingGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_autoscaling as interfaces_autoscaling
            
            auto_scaling_group_reference = interfaces_autoscaling.AutoScalingGroupReference(
                auto_scaling_group_arn="autoScalingGroupArn",
                auto_scaling_group_name="autoScalingGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad45614f4e540bae613323f2166957137deb5300bd434a60a612b05401cb8925)
            check_type(argname="argument auto_scaling_group_arn", value=auto_scaling_group_arn, expected_type=type_hints["auto_scaling_group_arn"])
            check_type(argname="argument auto_scaling_group_name", value=auto_scaling_group_name, expected_type=type_hints["auto_scaling_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_scaling_group_arn": auto_scaling_group_arn,
            "auto_scaling_group_name": auto_scaling_group_name,
        }

    @builtins.property
    def auto_scaling_group_arn(self) -> builtins.str:
        '''The ARN of the AutoScalingGroup resource.'''
        result = self._values.get("auto_scaling_group_arn")
        assert result is not None, "Required property 'auto_scaling_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_scaling_group_name(self) -> builtins.str:
        '''The AutoScalingGroupName of the AutoScalingGroup resource.'''
        result = self._values.get("auto_scaling_group_name")
        assert result is not None, "Required property 'auto_scaling_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoScalingGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.IAutoScalingGroupRef"
)
class IAutoScalingGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AutoScalingGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroupRef")
    def auto_scaling_group_ref(self) -> "AutoScalingGroupReference":
        '''(experimental) A reference to a AutoScalingGroup resource.

        :stability: experimental
        '''
        ...


class _IAutoScalingGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AutoScalingGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_autoscaling.IAutoScalingGroupRef"

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroupRef")
    def auto_scaling_group_ref(self) -> "AutoScalingGroupReference":
        '''(experimental) A reference to a AutoScalingGroup resource.

        :stability: experimental
        '''
        return typing.cast("AutoScalingGroupReference", jsii.get(self, "autoScalingGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAutoScalingGroupRef).__jsii_proxy_class__ = lambda : _IAutoScalingGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.ILaunchConfigurationRef"
)
class ILaunchConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="launchConfigurationRef")
    def launch_configuration_ref(self) -> "LaunchConfigurationReference":
        '''(experimental) A reference to a LaunchConfiguration resource.

        :stability: experimental
        '''
        ...


class _ILaunchConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LaunchConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_autoscaling.ILaunchConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="launchConfigurationRef")
    def launch_configuration_ref(self) -> "LaunchConfigurationReference":
        '''(experimental) A reference to a LaunchConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("LaunchConfigurationReference", jsii.get(self, "launchConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILaunchConfigurationRef).__jsii_proxy_class__ = lambda : _ILaunchConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.ILifecycleHookRef")
class ILifecycleHookRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LifecycleHook.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="lifecycleHookRef")
    def lifecycle_hook_ref(self) -> "LifecycleHookReference":
        '''(experimental) A reference to a LifecycleHook resource.

        :stability: experimental
        '''
        ...


class _ILifecycleHookRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LifecycleHook.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_autoscaling.ILifecycleHookRef"

    @builtins.property
    @jsii.member(jsii_name="lifecycleHookRef")
    def lifecycle_hook_ref(self) -> "LifecycleHookReference":
        '''(experimental) A reference to a LifecycleHook resource.

        :stability: experimental
        '''
        return typing.cast("LifecycleHookReference", jsii.get(self, "lifecycleHookRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILifecycleHookRef).__jsii_proxy_class__ = lambda : _ILifecycleHookRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.IScalingPolicyRef")
class IScalingPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ScalingPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scalingPolicyRef")
    def scaling_policy_ref(self) -> "ScalingPolicyReference":
        '''(experimental) A reference to a ScalingPolicy resource.

        :stability: experimental
        '''
        ...


class _IScalingPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ScalingPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_autoscaling.IScalingPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="scalingPolicyRef")
    def scaling_policy_ref(self) -> "ScalingPolicyReference":
        '''(experimental) A reference to a ScalingPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ScalingPolicyReference", jsii.get(self, "scalingPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScalingPolicyRef).__jsii_proxy_class__ = lambda : _IScalingPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.IScheduledActionRef")
class IScheduledActionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduledAction.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scheduledActionRef")
    def scheduled_action_ref(self) -> "ScheduledActionReference":
        '''(experimental) A reference to a ScheduledAction resource.

        :stability: experimental
        '''
        ...


class _IScheduledActionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduledAction.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_autoscaling.IScheduledActionRef"

    @builtins.property
    @jsii.member(jsii_name="scheduledActionRef")
    def scheduled_action_ref(self) -> "ScheduledActionReference":
        '''(experimental) A reference to a ScheduledAction resource.

        :stability: experimental
        '''
        return typing.cast("ScheduledActionReference", jsii.get(self, "scheduledActionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScheduledActionRef).__jsii_proxy_class__ = lambda : _IScheduledActionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.IWarmPoolRef")
class IWarmPoolRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WarmPool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="warmPoolRef")
    def warm_pool_ref(self) -> "WarmPoolReference":
        '''(experimental) A reference to a WarmPool resource.

        :stability: experimental
        '''
        ...


class _IWarmPoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WarmPool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_autoscaling.IWarmPoolRef"

    @builtins.property
    @jsii.member(jsii_name="warmPoolRef")
    def warm_pool_ref(self) -> "WarmPoolReference":
        '''(experimental) A reference to a WarmPool resource.

        :stability: experimental
        '''
        return typing.cast("WarmPoolReference", jsii.get(self, "warmPoolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWarmPoolRef).__jsii_proxy_class__ = lambda : _IWarmPoolRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.LaunchConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"launch_configuration_name": "launchConfigurationName"},
)
class LaunchConfigurationReference:
    def __init__(self, *, launch_configuration_name: builtins.str) -> None:
        '''A reference to a LaunchConfiguration resource.

        :param launch_configuration_name: The LaunchConfigurationName of the LaunchConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_autoscaling as interfaces_autoscaling
            
            launch_configuration_reference = interfaces_autoscaling.LaunchConfigurationReference(
                launch_configuration_name="launchConfigurationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3fa8a982c10d16bbd63e360d6f0e8cff9f8feaecd45456bd47c23b1269b8d34)
            check_type(argname="argument launch_configuration_name", value=launch_configuration_name, expected_type=type_hints["launch_configuration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "launch_configuration_name": launch_configuration_name,
        }

    @builtins.property
    def launch_configuration_name(self) -> builtins.str:
        '''The LaunchConfigurationName of the LaunchConfiguration resource.'''
        result = self._values.get("launch_configuration_name")
        assert result is not None, "Required property 'launch_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LaunchConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.LifecycleHookReference",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling_group_name": "autoScalingGroupName",
        "lifecycle_hook_name": "lifecycleHookName",
    },
)
class LifecycleHookReference:
    def __init__(
        self,
        *,
        auto_scaling_group_name: builtins.str,
        lifecycle_hook_name: builtins.str,
    ) -> None:
        '''A reference to a LifecycleHook resource.

        :param auto_scaling_group_name: The AutoScalingGroupName of the LifecycleHook resource.
        :param lifecycle_hook_name: The LifecycleHookName of the LifecycleHook resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_autoscaling as interfaces_autoscaling
            
            lifecycle_hook_reference = interfaces_autoscaling.LifecycleHookReference(
                auto_scaling_group_name="autoScalingGroupName",
                lifecycle_hook_name="lifecycleHookName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ced7483939a52f1ec5b5da2200247858df3161c0baf391c68b5f88e83421f0c)
            check_type(argname="argument auto_scaling_group_name", value=auto_scaling_group_name, expected_type=type_hints["auto_scaling_group_name"])
            check_type(argname="argument lifecycle_hook_name", value=lifecycle_hook_name, expected_type=type_hints["lifecycle_hook_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_scaling_group_name": auto_scaling_group_name,
            "lifecycle_hook_name": lifecycle_hook_name,
        }

    @builtins.property
    def auto_scaling_group_name(self) -> builtins.str:
        '''The AutoScalingGroupName of the LifecycleHook resource.'''
        result = self._values.get("auto_scaling_group_name")
        assert result is not None, "Required property 'auto_scaling_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lifecycle_hook_name(self) -> builtins.str:
        '''The LifecycleHookName of the LifecycleHook resource.'''
        result = self._values.get("lifecycle_hook_name")
        assert result is not None, "Required property 'lifecycle_hook_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LifecycleHookReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.ScalingPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"scaling_policy_arn": "scalingPolicyArn"},
)
class ScalingPolicyReference:
    def __init__(self, *, scaling_policy_arn: builtins.str) -> None:
        '''A reference to a ScalingPolicy resource.

        :param scaling_policy_arn: The Arn of the ScalingPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_autoscaling as interfaces_autoscaling
            
            scaling_policy_reference = interfaces_autoscaling.ScalingPolicyReference(
                scaling_policy_arn="scalingPolicyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f19fc8b2662ee23dbd839ce57c057a1df4351872941878b457a13bed57b62f16)
            check_type(argname="argument scaling_policy_arn", value=scaling_policy_arn, expected_type=type_hints["scaling_policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scaling_policy_arn": scaling_policy_arn,
        }

    @builtins.property
    def scaling_policy_arn(self) -> builtins.str:
        '''The Arn of the ScalingPolicy resource.'''
        result = self._values.get("scaling_policy_arn")
        assert result is not None, "Required property 'scaling_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.ScheduledActionReference",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling_group_name": "autoScalingGroupName",
        "scheduled_action_name": "scheduledActionName",
    },
)
class ScheduledActionReference:
    def __init__(
        self,
        *,
        auto_scaling_group_name: builtins.str,
        scheduled_action_name: builtins.str,
    ) -> None:
        '''A reference to a ScheduledAction resource.

        :param auto_scaling_group_name: The AutoScalingGroupName of the ScheduledAction resource.
        :param scheduled_action_name: The ScheduledActionName of the ScheduledAction resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_autoscaling as interfaces_autoscaling
            
            scheduled_action_reference = interfaces_autoscaling.ScheduledActionReference(
                auto_scaling_group_name="autoScalingGroupName",
                scheduled_action_name="scheduledActionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b4d80dbd2ead593879b1bc9f78e71f88eb4873cb4d8d137e9a3f1496e3008c)
            check_type(argname="argument auto_scaling_group_name", value=auto_scaling_group_name, expected_type=type_hints["auto_scaling_group_name"])
            check_type(argname="argument scheduled_action_name", value=scheduled_action_name, expected_type=type_hints["scheduled_action_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_scaling_group_name": auto_scaling_group_name,
            "scheduled_action_name": scheduled_action_name,
        }

    @builtins.property
    def auto_scaling_group_name(self) -> builtins.str:
        '''The AutoScalingGroupName of the ScheduledAction resource.'''
        result = self._values.get("auto_scaling_group_name")
        assert result is not None, "Required property 'auto_scaling_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scheduled_action_name(self) -> builtins.str:
        '''The ScheduledActionName of the ScheduledAction resource.'''
        result = self._values.get("scheduled_action_name")
        assert result is not None, "Required property 'scheduled_action_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduledActionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_autoscaling.WarmPoolReference",
    jsii_struct_bases=[],
    name_mapping={"auto_scaling_group_name": "autoScalingGroupName"},
)
class WarmPoolReference:
    def __init__(self, *, auto_scaling_group_name: builtins.str) -> None:
        '''A reference to a WarmPool resource.

        :param auto_scaling_group_name: The AutoScalingGroupName of the WarmPool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_autoscaling as interfaces_autoscaling
            
            warm_pool_reference = interfaces_autoscaling.WarmPoolReference(
                auto_scaling_group_name="autoScalingGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d87eff8ecb72679c107374932e5c8d2d0e0f062a50f3493c2042083b741dba86)
            check_type(argname="argument auto_scaling_group_name", value=auto_scaling_group_name, expected_type=type_hints["auto_scaling_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_scaling_group_name": auto_scaling_group_name,
        }

    @builtins.property
    def auto_scaling_group_name(self) -> builtins.str:
        '''The AutoScalingGroupName of the WarmPool resource.'''
        result = self._values.get("auto_scaling_group_name")
        assert result is not None, "Required property 'auto_scaling_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WarmPoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AutoScalingGroupReference",
    "IAutoScalingGroupRef",
    "ILaunchConfigurationRef",
    "ILifecycleHookRef",
    "IScalingPolicyRef",
    "IScheduledActionRef",
    "IWarmPoolRef",
    "LaunchConfigurationReference",
    "LifecycleHookReference",
    "ScalingPolicyReference",
    "ScheduledActionReference",
    "WarmPoolReference",
]

publication.publish()

def _typecheckingstub__ad45614f4e540bae613323f2166957137deb5300bd434a60a612b05401cb8925(
    *,
    auto_scaling_group_arn: builtins.str,
    auto_scaling_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3fa8a982c10d16bbd63e360d6f0e8cff9f8feaecd45456bd47c23b1269b8d34(
    *,
    launch_configuration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ced7483939a52f1ec5b5da2200247858df3161c0baf391c68b5f88e83421f0c(
    *,
    auto_scaling_group_name: builtins.str,
    lifecycle_hook_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f19fc8b2662ee23dbd839ce57c057a1df4351872941878b457a13bed57b62f16(
    *,
    scaling_policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b4d80dbd2ead593879b1bc9f78e71f88eb4873cb4d8d137e9a3f1496e3008c(
    *,
    auto_scaling_group_name: builtins.str,
    scheduled_action_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d87eff8ecb72679c107374932e5c8d2d0e0f062a50f3493c2042083b741dba86(
    *,
    auto_scaling_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAutoScalingGroupRef, ILaunchConfigurationRef, ILifecycleHookRef, IScalingPolicyRef, IScheduledActionRef, IWarmPoolRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
