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
    jsii_type="aws-cdk-lib.interfaces.aws_kendraranking.ExecutionPlanReference",
    jsii_struct_bases=[],
    name_mapping={
        "execution_plan_arn": "executionPlanArn",
        "execution_plan_id": "executionPlanId",
    },
)
class ExecutionPlanReference:
    def __init__(
        self,
        *,
        execution_plan_arn: builtins.str,
        execution_plan_id: builtins.str,
    ) -> None:
        '''A reference to a ExecutionPlan resource.

        :param execution_plan_arn: The ARN of the ExecutionPlan resource.
        :param execution_plan_id: The Id of the ExecutionPlan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kendraranking as interfaces_kendraranking
            
            execution_plan_reference = interfaces_kendraranking.ExecutionPlanReference(
                execution_plan_arn="executionPlanArn",
                execution_plan_id="executionPlanId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e055b81d18492bc61c740a983801875cc6377a2e8e6b39d2d2b7a2a0d27879)
            check_type(argname="argument execution_plan_arn", value=execution_plan_arn, expected_type=type_hints["execution_plan_arn"])
            check_type(argname="argument execution_plan_id", value=execution_plan_id, expected_type=type_hints["execution_plan_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "execution_plan_arn": execution_plan_arn,
            "execution_plan_id": execution_plan_id,
        }

    @builtins.property
    def execution_plan_arn(self) -> builtins.str:
        '''The ARN of the ExecutionPlan resource.'''
        result = self._values.get("execution_plan_arn")
        assert result is not None, "Required property 'execution_plan_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def execution_plan_id(self) -> builtins.str:
        '''The Id of the ExecutionPlan resource.'''
        result = self._values.get("execution_plan_id")
        assert result is not None, "Required property 'execution_plan_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExecutionPlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kendraranking.IExecutionPlanRef")
class IExecutionPlanRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ExecutionPlan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="executionPlanRef")
    def execution_plan_ref(self) -> "ExecutionPlanReference":
        '''(experimental) A reference to a ExecutionPlan resource.

        :stability: experimental
        '''
        ...


class _IExecutionPlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ExecutionPlan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kendraranking.IExecutionPlanRef"

    @builtins.property
    @jsii.member(jsii_name="executionPlanRef")
    def execution_plan_ref(self) -> "ExecutionPlanReference":
        '''(experimental) A reference to a ExecutionPlan resource.

        :stability: experimental
        '''
        return typing.cast("ExecutionPlanReference", jsii.get(self, "executionPlanRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExecutionPlanRef).__jsii_proxy_class__ = lambda : _IExecutionPlanRefProxy


__all__ = [
    "ExecutionPlanReference",
    "IExecutionPlanRef",
]

publication.publish()

def _typecheckingstub__d7e055b81d18492bc61c740a983801875cc6377a2e8e6b39d2d2b7a2a0d27879(
    *,
    execution_plan_arn: builtins.str,
    execution_plan_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IExecutionPlanRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
