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
    jsii_type="aws-cdk-lib.interfaces.aws_autoscalingplans.IScalingPlanRef"
)
class IScalingPlanRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ScalingPlan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scalingPlanRef")
    def scaling_plan_ref(self) -> "ScalingPlanReference":
        '''(experimental) A reference to a ScalingPlan resource.

        :stability: experimental
        '''
        ...


class _IScalingPlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ScalingPlan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_autoscalingplans.IScalingPlanRef"

    @builtins.property
    @jsii.member(jsii_name="scalingPlanRef")
    def scaling_plan_ref(self) -> "ScalingPlanReference":
        '''(experimental) A reference to a ScalingPlan resource.

        :stability: experimental
        '''
        return typing.cast("ScalingPlanReference", jsii.get(self, "scalingPlanRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScalingPlanRef).__jsii_proxy_class__ = lambda : _IScalingPlanRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_autoscalingplans.ScalingPlanReference",
    jsii_struct_bases=[],
    name_mapping={"scaling_plan_id": "scalingPlanId"},
)
class ScalingPlanReference:
    def __init__(self, *, scaling_plan_id: builtins.str) -> None:
        '''A reference to a ScalingPlan resource.

        :param scaling_plan_id: The Id of the ScalingPlan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_autoscalingplans as interfaces_autoscalingplans
            
            scaling_plan_reference = interfaces_autoscalingplans.ScalingPlanReference(
                scaling_plan_id="scalingPlanId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e3f4ae94ec3cbc8d1f487e18fd1852634f2bde6b1dcb4238c6532e9144624c1)
            check_type(argname="argument scaling_plan_id", value=scaling_plan_id, expected_type=type_hints["scaling_plan_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scaling_plan_id": scaling_plan_id,
        }

    @builtins.property
    def scaling_plan_id(self) -> builtins.str:
        '''The Id of the ScalingPlan resource.'''
        result = self._values.get("scaling_plan_id")
        assert result is not None, "Required property 'scaling_plan_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingPlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IScalingPlanRef",
    "ScalingPlanReference",
]

publication.publish()

def _typecheckingstub__9e3f4ae94ec3cbc8d1f487e18fd1852634f2bde6b1dcb4238c6532e9144624c1(
    *,
    scaling_plan_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IScalingPlanRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
