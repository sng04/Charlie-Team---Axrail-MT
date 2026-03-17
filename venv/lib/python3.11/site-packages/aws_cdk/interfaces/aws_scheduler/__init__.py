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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_scheduler.IScheduleGroupRef")
class IScheduleGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduleGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scheduleGroupRef")
    def schedule_group_ref(self) -> "ScheduleGroupReference":
        '''(experimental) A reference to a ScheduleGroup resource.

        :stability: experimental
        '''
        ...


class _IScheduleGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ScheduleGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_scheduler.IScheduleGroupRef"

    @builtins.property
    @jsii.member(jsii_name="scheduleGroupRef")
    def schedule_group_ref(self) -> "ScheduleGroupReference":
        '''(experimental) A reference to a ScheduleGroup resource.

        :stability: experimental
        '''
        return typing.cast("ScheduleGroupReference", jsii.get(self, "scheduleGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScheduleGroupRef).__jsii_proxy_class__ = lambda : _IScheduleGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_scheduler.IScheduleRef")
class IScheduleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Schedule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scheduleRef")
    def schedule_ref(self) -> "ScheduleReference":
        '''(experimental) A reference to a Schedule resource.

        :stability: experimental
        '''
        ...


class _IScheduleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Schedule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_scheduler.IScheduleRef"

    @builtins.property
    @jsii.member(jsii_name="scheduleRef")
    def schedule_ref(self) -> "ScheduleReference":
        '''(experimental) A reference to a Schedule resource.

        :stability: experimental
        '''
        return typing.cast("ScheduleReference", jsii.get(self, "scheduleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScheduleRef).__jsii_proxy_class__ = lambda : _IScheduleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_scheduler.ScheduleGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "schedule_group_arn": "scheduleGroupArn",
        "schedule_group_name": "scheduleGroupName",
    },
)
class ScheduleGroupReference:
    def __init__(
        self,
        *,
        schedule_group_arn: builtins.str,
        schedule_group_name: builtins.str,
    ) -> None:
        '''A reference to a ScheduleGroup resource.

        :param schedule_group_arn: The ARN of the ScheduleGroup resource.
        :param schedule_group_name: The Name of the ScheduleGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_scheduler as interfaces_scheduler
            
            schedule_group_reference = interfaces_scheduler.ScheduleGroupReference(
                schedule_group_arn="scheduleGroupArn",
                schedule_group_name="scheduleGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c0331a61fbe34d5659eca4761c749e131a6e43ed11955e0e47052daf4ecc959)
            check_type(argname="argument schedule_group_arn", value=schedule_group_arn, expected_type=type_hints["schedule_group_arn"])
            check_type(argname="argument schedule_group_name", value=schedule_group_name, expected_type=type_hints["schedule_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schedule_group_arn": schedule_group_arn,
            "schedule_group_name": schedule_group_name,
        }

    @builtins.property
    def schedule_group_arn(self) -> builtins.str:
        '''The ARN of the ScheduleGroup resource.'''
        result = self._values.get("schedule_group_arn")
        assert result is not None, "Required property 'schedule_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule_group_name(self) -> builtins.str:
        '''The Name of the ScheduleGroup resource.'''
        result = self._values.get("schedule_group_name")
        assert result is not None, "Required property 'schedule_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduleGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_scheduler.ScheduleReference",
    jsii_struct_bases=[],
    name_mapping={"schedule_arn": "scheduleArn", "schedule_name": "scheduleName"},
)
class ScheduleReference:
    def __init__(
        self,
        *,
        schedule_arn: builtins.str,
        schedule_name: builtins.str,
    ) -> None:
        '''A reference to a Schedule resource.

        :param schedule_arn: The ARN of the Schedule resource.
        :param schedule_name: The Name of the Schedule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_scheduler as interfaces_scheduler
            
            schedule_reference = interfaces_scheduler.ScheduleReference(
                schedule_arn="scheduleArn",
                schedule_name="scheduleName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43cf3d36c1e7a88d70fef5d5ed4f38794e5a22bf7f20c9685e90387b7cc9b59e)
            check_type(argname="argument schedule_arn", value=schedule_arn, expected_type=type_hints["schedule_arn"])
            check_type(argname="argument schedule_name", value=schedule_name, expected_type=type_hints["schedule_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schedule_arn": schedule_arn,
            "schedule_name": schedule_name,
        }

    @builtins.property
    def schedule_arn(self) -> builtins.str:
        '''The ARN of the Schedule resource.'''
        result = self._values.get("schedule_arn")
        assert result is not None, "Required property 'schedule_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule_name(self) -> builtins.str:
        '''The Name of the Schedule resource.'''
        result = self._values.get("schedule_name")
        assert result is not None, "Required property 'schedule_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScheduleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IScheduleGroupRef",
    "IScheduleRef",
    "ScheduleGroupReference",
    "ScheduleReference",
]

publication.publish()

def _typecheckingstub__1c0331a61fbe34d5659eca4761c749e131a6e43ed11955e0e47052daf4ecc959(
    *,
    schedule_group_arn: builtins.str,
    schedule_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43cf3d36c1e7a88d70fef5d5ed4f38794e5a22bf7f20c9685e90387b7cc9b59e(
    *,
    schedule_arn: builtins.str,
    schedule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IScheduleGroupRef, IScheduleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
