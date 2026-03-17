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
    jsii_type="aws-cdk-lib.interfaces.aws_applicationautoscaling.IScalableTargetRef"
)
class IScalableTargetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ScalableTarget.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scalableTargetRef")
    def scalable_target_ref(self) -> "ScalableTargetReference":
        '''(experimental) A reference to a ScalableTarget resource.

        :stability: experimental
        '''
        ...


class _IScalableTargetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ScalableTarget.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_applicationautoscaling.IScalableTargetRef"

    @builtins.property
    @jsii.member(jsii_name="scalableTargetRef")
    def scalable_target_ref(self) -> "ScalableTargetReference":
        '''(experimental) A reference to a ScalableTarget resource.

        :stability: experimental
        '''
        return typing.cast("ScalableTargetReference", jsii.get(self, "scalableTargetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScalableTargetRef).__jsii_proxy_class__ = lambda : _IScalableTargetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_applicationautoscaling.IScalingPolicyRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_applicationautoscaling.IScalingPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="scalingPolicyRef")
    def scaling_policy_ref(self) -> "ScalingPolicyReference":
        '''(experimental) A reference to a ScalingPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ScalingPolicyReference", jsii.get(self, "scalingPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScalingPolicyRef).__jsii_proxy_class__ = lambda : _IScalingPolicyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_applicationautoscaling.ScalableTargetReference",
    jsii_struct_bases=[],
    name_mapping={
        "resource_id": "resourceId",
        "scalable_dimension": "scalableDimension",
        "service_namespace": "serviceNamespace",
    },
)
class ScalableTargetReference:
    def __init__(
        self,
        *,
        resource_id: builtins.str,
        scalable_dimension: builtins.str,
        service_namespace: builtins.str,
    ) -> None:
        '''A reference to a ScalableTarget resource.

        :param resource_id: The ResourceId of the ScalableTarget resource.
        :param scalable_dimension: The ScalableDimension of the ScalableTarget resource.
        :param service_namespace: The ServiceNamespace of the ScalableTarget resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_applicationautoscaling as interfaces_applicationautoscaling
            
            scalable_target_reference = interfaces_applicationautoscaling.ScalableTargetReference(
                resource_id="resourceId",
                scalable_dimension="scalableDimension",
                service_namespace="serviceNamespace"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79b0d23171b4fcbed5c9ae0a8a7c14eea7aa845c597a7df4ed09f50c065bb4dd)
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument scalable_dimension", value=scalable_dimension, expected_type=type_hints["scalable_dimension"])
            check_type(argname="argument service_namespace", value=service_namespace, expected_type=type_hints["service_namespace"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_id": resource_id,
            "scalable_dimension": scalable_dimension,
            "service_namespace": service_namespace,
        }

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The ResourceId of the ScalableTarget resource.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        '''The ScalableDimension of the ScalableTarget resource.'''
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_namespace(self) -> builtins.str:
        '''The ServiceNamespace of the ScalableTarget resource.'''
        result = self._values.get("service_namespace")
        assert result is not None, "Required property 'service_namespace' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalableTargetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_applicationautoscaling.ScalingPolicyReference",
    jsii_struct_bases=[],
    name_mapping={
        "scalable_dimension": "scalableDimension",
        "scaling_policy_arn": "scalingPolicyArn",
    },
)
class ScalingPolicyReference:
    def __init__(
        self,
        *,
        scalable_dimension: builtins.str,
        scaling_policy_arn: builtins.str,
    ) -> None:
        '''A reference to a ScalingPolicy resource.

        :param scalable_dimension: The ScalableDimension of the ScalingPolicy resource.
        :param scaling_policy_arn: The Arn of the ScalingPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_applicationautoscaling as interfaces_applicationautoscaling
            
            scaling_policy_reference = interfaces_applicationautoscaling.ScalingPolicyReference(
                scalable_dimension="scalableDimension",
                scaling_policy_arn="scalingPolicyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__498c5015ed26a2b8e991461356d344690b175358634465fb173ebd5f71bb3d27)
            check_type(argname="argument scalable_dimension", value=scalable_dimension, expected_type=type_hints["scalable_dimension"])
            check_type(argname="argument scaling_policy_arn", value=scaling_policy_arn, expected_type=type_hints["scaling_policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scalable_dimension": scalable_dimension,
            "scaling_policy_arn": scaling_policy_arn,
        }

    @builtins.property
    def scalable_dimension(self) -> builtins.str:
        '''The ScalableDimension of the ScalingPolicy resource.'''
        result = self._values.get("scalable_dimension")
        assert result is not None, "Required property 'scalable_dimension' is missing"
        return typing.cast(builtins.str, result)

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


__all__ = [
    "IScalableTargetRef",
    "IScalingPolicyRef",
    "ScalableTargetReference",
    "ScalingPolicyReference",
]

publication.publish()

def _typecheckingstub__79b0d23171b4fcbed5c9ae0a8a7c14eea7aa845c597a7df4ed09f50c065bb4dd(
    *,
    resource_id: builtins.str,
    scalable_dimension: builtins.str,
    service_namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__498c5015ed26a2b8e991461356d344690b175358634465fb173ebd5f71bb3d27(
    *,
    scalable_dimension: builtins.str,
    scaling_policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IScalableTargetRef, IScalingPolicyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
