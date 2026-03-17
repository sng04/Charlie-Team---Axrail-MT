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
    jsii_type="aws-cdk-lib.interfaces.aws_stepfunctions.ActivityReference",
    jsii_struct_bases=[],
    name_mapping={"activity_arn": "activityArn"},
)
class ActivityReference:
    def __init__(self, *, activity_arn: builtins.str) -> None:
        '''A reference to a Activity resource.

        :param activity_arn: The Arn of the Activity resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_stepfunctions as interfaces_stepfunctions
            
            activity_reference = interfaces_stepfunctions.ActivityReference(
                activity_arn="activityArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b883848654dc545ce6d6eba57ce8a8774e3bc4971af04c81e4cc73a2f39c176d)
            check_type(argname="argument activity_arn", value=activity_arn, expected_type=type_hints["activity_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "activity_arn": activity_arn,
        }

    @builtins.property
    def activity_arn(self) -> builtins.str:
        '''The Arn of the Activity resource.'''
        result = self._values.get("activity_arn")
        assert result is not None, "Required property 'activity_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ActivityReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_stepfunctions.IActivityRef")
class IActivityRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Activity.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="activityRef")
    def activity_ref(self) -> "ActivityReference":
        '''(experimental) A reference to a Activity resource.

        :stability: experimental
        '''
        ...


class _IActivityRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Activity.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_stepfunctions.IActivityRef"

    @builtins.property
    @jsii.member(jsii_name="activityRef")
    def activity_ref(self) -> "ActivityReference":
        '''(experimental) A reference to a Activity resource.

        :stability: experimental
        '''
        return typing.cast("ActivityReference", jsii.get(self, "activityRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IActivityRef).__jsii_proxy_class__ = lambda : _IActivityRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_stepfunctions.IStateMachineAliasRef"
)
class IStateMachineAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StateMachineAlias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stateMachineAliasRef")
    def state_machine_alias_ref(self) -> "StateMachineAliasReference":
        '''(experimental) A reference to a StateMachineAlias resource.

        :stability: experimental
        '''
        ...


class _IStateMachineAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StateMachineAlias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_stepfunctions.IStateMachineAliasRef"

    @builtins.property
    @jsii.member(jsii_name="stateMachineAliasRef")
    def state_machine_alias_ref(self) -> "StateMachineAliasReference":
        '''(experimental) A reference to a StateMachineAlias resource.

        :stability: experimental
        '''
        return typing.cast("StateMachineAliasReference", jsii.get(self, "stateMachineAliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStateMachineAliasRef).__jsii_proxy_class__ = lambda : _IStateMachineAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_stepfunctions.IStateMachineRef")
class IStateMachineRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StateMachine.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stateMachineRef")
    def state_machine_ref(self) -> "StateMachineReference":
        '''(experimental) A reference to a StateMachine resource.

        :stability: experimental
        '''
        ...


class _IStateMachineRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StateMachine.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_stepfunctions.IStateMachineRef"

    @builtins.property
    @jsii.member(jsii_name="stateMachineRef")
    def state_machine_ref(self) -> "StateMachineReference":
        '''(experimental) A reference to a StateMachine resource.

        :stability: experimental
        '''
        return typing.cast("StateMachineReference", jsii.get(self, "stateMachineRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStateMachineRef).__jsii_proxy_class__ = lambda : _IStateMachineRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_stepfunctions.IStateMachineVersionRef"
)
class IStateMachineVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StateMachineVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stateMachineVersionRef")
    def state_machine_version_ref(self) -> "StateMachineVersionReference":
        '''(experimental) A reference to a StateMachineVersion resource.

        :stability: experimental
        '''
        ...


class _IStateMachineVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StateMachineVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_stepfunctions.IStateMachineVersionRef"

    @builtins.property
    @jsii.member(jsii_name="stateMachineVersionRef")
    def state_machine_version_ref(self) -> "StateMachineVersionReference":
        '''(experimental) A reference to a StateMachineVersion resource.

        :stability: experimental
        '''
        return typing.cast("StateMachineVersionReference", jsii.get(self, "stateMachineVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStateMachineVersionRef).__jsii_proxy_class__ = lambda : _IStateMachineVersionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_stepfunctions.StateMachineAliasReference",
    jsii_struct_bases=[],
    name_mapping={"state_machine_alias_arn": "stateMachineAliasArn"},
)
class StateMachineAliasReference:
    def __init__(self, *, state_machine_alias_arn: builtins.str) -> None:
        '''A reference to a StateMachineAlias resource.

        :param state_machine_alias_arn: The Arn of the StateMachineAlias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_stepfunctions as interfaces_stepfunctions
            
            state_machine_alias_reference = interfaces_stepfunctions.StateMachineAliasReference(
                state_machine_alias_arn="stateMachineAliasArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27983f4efaba15cf165f4fe31a4f13b29fea4be7879eab8b6f6c7bb9cfbfb9e8)
            check_type(argname="argument state_machine_alias_arn", value=state_machine_alias_arn, expected_type=type_hints["state_machine_alias_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "state_machine_alias_arn": state_machine_alias_arn,
        }

    @builtins.property
    def state_machine_alias_arn(self) -> builtins.str:
        '''The Arn of the StateMachineAlias resource.'''
        result = self._values.get("state_machine_alias_arn")
        assert result is not None, "Required property 'state_machine_alias_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StateMachineAliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_stepfunctions.StateMachineReference",
    jsii_struct_bases=[],
    name_mapping={"state_machine_arn": "stateMachineArn"},
)
class StateMachineReference:
    def __init__(self, *, state_machine_arn: builtins.str) -> None:
        '''A reference to a StateMachine resource.

        :param state_machine_arn: The Arn of the StateMachine resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_stepfunctions as interfaces_stepfunctions
            
            state_machine_reference = interfaces_stepfunctions.StateMachineReference(
                state_machine_arn="stateMachineArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2721be2130eb41d822ade793fb6254f7b2fddbe1de8735abc27a9d55856b3d0a)
            check_type(argname="argument state_machine_arn", value=state_machine_arn, expected_type=type_hints["state_machine_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "state_machine_arn": state_machine_arn,
        }

    @builtins.property
    def state_machine_arn(self) -> builtins.str:
        '''The Arn of the StateMachine resource.'''
        result = self._values.get("state_machine_arn")
        assert result is not None, "Required property 'state_machine_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StateMachineReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_stepfunctions.StateMachineVersionReference",
    jsii_struct_bases=[],
    name_mapping={"state_machine_version_arn": "stateMachineVersionArn"},
)
class StateMachineVersionReference:
    def __init__(self, *, state_machine_version_arn: builtins.str) -> None:
        '''A reference to a StateMachineVersion resource.

        :param state_machine_version_arn: The Arn of the StateMachineVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_stepfunctions as interfaces_stepfunctions
            
            state_machine_version_reference = interfaces_stepfunctions.StateMachineVersionReference(
                state_machine_version_arn="stateMachineVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dca710712489355ac7f99ff3ffb691ef5446206776073003adf3a1cbdcd8e93)
            check_type(argname="argument state_machine_version_arn", value=state_machine_version_arn, expected_type=type_hints["state_machine_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "state_machine_version_arn": state_machine_version_arn,
        }

    @builtins.property
    def state_machine_version_arn(self) -> builtins.str:
        '''The Arn of the StateMachineVersion resource.'''
        result = self._values.get("state_machine_version_arn")
        assert result is not None, "Required property 'state_machine_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StateMachineVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ActivityReference",
    "IActivityRef",
    "IStateMachineAliasRef",
    "IStateMachineRef",
    "IStateMachineVersionRef",
    "StateMachineAliasReference",
    "StateMachineReference",
    "StateMachineVersionReference",
]

publication.publish()

def _typecheckingstub__b883848654dc545ce6d6eba57ce8a8774e3bc4971af04c81e4cc73a2f39c176d(
    *,
    activity_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27983f4efaba15cf165f4fe31a4f13b29fea4be7879eab8b6f6c7bb9cfbfb9e8(
    *,
    state_machine_alias_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2721be2130eb41d822ade793fb6254f7b2fddbe1de8735abc27a9d55856b3d0a(
    *,
    state_machine_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dca710712489355ac7f99ff3ffb691ef5446206776073003adf3a1cbdcd8e93(
    *,
    state_machine_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IActivityRef, IStateMachineAliasRef, IStateMachineRef, IStateMachineVersionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
