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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_arcregionswitch.IPlanRef")
class IPlanRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Plan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="planRef")
    def plan_ref(self) -> "PlanReference":
        '''(experimental) A reference to a Plan resource.

        :stability: experimental
        '''
        ...


class _IPlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Plan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_arcregionswitch.IPlanRef"

    @builtins.property
    @jsii.member(jsii_name="planRef")
    def plan_ref(self) -> "PlanReference":
        '''(experimental) A reference to a Plan resource.

        :stability: experimental
        '''
        return typing.cast("PlanReference", jsii.get(self, "planRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPlanRef).__jsii_proxy_class__ = lambda : _IPlanRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_arcregionswitch.PlanReference",
    jsii_struct_bases=[],
    name_mapping={"plan_arn": "planArn"},
)
class PlanReference:
    def __init__(self, *, plan_arn: builtins.str) -> None:
        '''A reference to a Plan resource.

        :param plan_arn: The Arn of the Plan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_arcregionswitch as interfaces_arcregionswitch
            
            plan_reference = interfaces_arcregionswitch.PlanReference(
                plan_arn="planArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c35c1f6f8c13e2b1ec7c7575886ac5c8acce9ee848c17006dfb247e27a3e75b)
            check_type(argname="argument plan_arn", value=plan_arn, expected_type=type_hints["plan_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "plan_arn": plan_arn,
        }

    @builtins.property
    def plan_arn(self) -> builtins.str:
        '''The Arn of the Plan resource.'''
        result = self._values.get("plan_arn")
        assert result is not None, "Required property 'plan_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IPlanRef",
    "PlanReference",
]

publication.publish()

def _typecheckingstub__8c35c1f6f8c13e2b1ec7c7575886ac5c8acce9ee848c17006dfb247e27a3e75b(
    *,
    plan_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IPlanRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
