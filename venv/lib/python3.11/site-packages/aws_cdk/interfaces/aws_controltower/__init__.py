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
    jsii_type="aws-cdk-lib.interfaces.aws_controltower.EnabledBaselineReference",
    jsii_struct_bases=[],
    name_mapping={"enabled_baseline_identifier": "enabledBaselineIdentifier"},
)
class EnabledBaselineReference:
    def __init__(self, *, enabled_baseline_identifier: builtins.str) -> None:
        '''A reference to a EnabledBaseline resource.

        :param enabled_baseline_identifier: The EnabledBaselineIdentifier of the EnabledBaseline resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_controltower as interfaces_controltower
            
            enabled_baseline_reference = interfaces_controltower.EnabledBaselineReference(
                enabled_baseline_identifier="enabledBaselineIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__131ca4cc561cbb4aa73ec0084a3232b76e8f345bad523722000b9a6806841282)
            check_type(argname="argument enabled_baseline_identifier", value=enabled_baseline_identifier, expected_type=type_hints["enabled_baseline_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "enabled_baseline_identifier": enabled_baseline_identifier,
        }

    @builtins.property
    def enabled_baseline_identifier(self) -> builtins.str:
        '''The EnabledBaselineIdentifier of the EnabledBaseline resource.'''
        result = self._values.get("enabled_baseline_identifier")
        assert result is not None, "Required property 'enabled_baseline_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnabledBaselineReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_controltower.EnabledControlReference",
    jsii_struct_bases=[],
    name_mapping={
        "control_identifier": "controlIdentifier",
        "target_identifier": "targetIdentifier",
    },
)
class EnabledControlReference:
    def __init__(
        self,
        *,
        control_identifier: builtins.str,
        target_identifier: builtins.str,
    ) -> None:
        '''A reference to a EnabledControl resource.

        :param control_identifier: The ControlIdentifier of the EnabledControl resource.
        :param target_identifier: The TargetIdentifier of the EnabledControl resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_controltower as interfaces_controltower
            
            enabled_control_reference = interfaces_controltower.EnabledControlReference(
                control_identifier="controlIdentifier",
                target_identifier="targetIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cb9591522b427f0e2c9e99083beb4f143ec50e993bdc26049fcce9d1b5fd5f4)
            check_type(argname="argument control_identifier", value=control_identifier, expected_type=type_hints["control_identifier"])
            check_type(argname="argument target_identifier", value=target_identifier, expected_type=type_hints["target_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "control_identifier": control_identifier,
            "target_identifier": target_identifier,
        }

    @builtins.property
    def control_identifier(self) -> builtins.str:
        '''The ControlIdentifier of the EnabledControl resource.'''
        result = self._values.get("control_identifier")
        assert result is not None, "Required property 'control_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_identifier(self) -> builtins.str:
        '''The TargetIdentifier of the EnabledControl resource.'''
        result = self._values.get("target_identifier")
        assert result is not None, "Required property 'target_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnabledControlReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_controltower.IEnabledBaselineRef"
)
class IEnabledBaselineRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EnabledBaseline.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="enabledBaselineRef")
    def enabled_baseline_ref(self) -> "EnabledBaselineReference":
        '''(experimental) A reference to a EnabledBaseline resource.

        :stability: experimental
        '''
        ...


class _IEnabledBaselineRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EnabledBaseline.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_controltower.IEnabledBaselineRef"

    @builtins.property
    @jsii.member(jsii_name="enabledBaselineRef")
    def enabled_baseline_ref(self) -> "EnabledBaselineReference":
        '''(experimental) A reference to a EnabledBaseline resource.

        :stability: experimental
        '''
        return typing.cast("EnabledBaselineReference", jsii.get(self, "enabledBaselineRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnabledBaselineRef).__jsii_proxy_class__ = lambda : _IEnabledBaselineRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_controltower.IEnabledControlRef")
class IEnabledControlRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EnabledControl.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="enabledControlRef")
    def enabled_control_ref(self) -> "EnabledControlReference":
        '''(experimental) A reference to a EnabledControl resource.

        :stability: experimental
        '''
        ...


class _IEnabledControlRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EnabledControl.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_controltower.IEnabledControlRef"

    @builtins.property
    @jsii.member(jsii_name="enabledControlRef")
    def enabled_control_ref(self) -> "EnabledControlReference":
        '''(experimental) A reference to a EnabledControl resource.

        :stability: experimental
        '''
        return typing.cast("EnabledControlReference", jsii.get(self, "enabledControlRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnabledControlRef).__jsii_proxy_class__ = lambda : _IEnabledControlRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_controltower.ILandingZoneRef")
class ILandingZoneRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LandingZone.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="landingZoneRef")
    def landing_zone_ref(self) -> "LandingZoneReference":
        '''(experimental) A reference to a LandingZone resource.

        :stability: experimental
        '''
        ...


class _ILandingZoneRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LandingZone.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_controltower.ILandingZoneRef"

    @builtins.property
    @jsii.member(jsii_name="landingZoneRef")
    def landing_zone_ref(self) -> "LandingZoneReference":
        '''(experimental) A reference to a LandingZone resource.

        :stability: experimental
        '''
        return typing.cast("LandingZoneReference", jsii.get(self, "landingZoneRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILandingZoneRef).__jsii_proxy_class__ = lambda : _ILandingZoneRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_controltower.LandingZoneReference",
    jsii_struct_bases=[],
    name_mapping={
        "landing_zone_arn": "landingZoneArn",
        "landing_zone_identifier": "landingZoneIdentifier",
    },
)
class LandingZoneReference:
    def __init__(
        self,
        *,
        landing_zone_arn: builtins.str,
        landing_zone_identifier: builtins.str,
    ) -> None:
        '''A reference to a LandingZone resource.

        :param landing_zone_arn: The ARN of the LandingZone resource.
        :param landing_zone_identifier: The LandingZoneIdentifier of the LandingZone resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_controltower as interfaces_controltower
            
            landing_zone_reference = interfaces_controltower.LandingZoneReference(
                landing_zone_arn="landingZoneArn",
                landing_zone_identifier="landingZoneIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__433a90da81f818d83b8df0e666ab36391cc14c2e043d9d9957de21c1d16101d6)
            check_type(argname="argument landing_zone_arn", value=landing_zone_arn, expected_type=type_hints["landing_zone_arn"])
            check_type(argname="argument landing_zone_identifier", value=landing_zone_identifier, expected_type=type_hints["landing_zone_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "landing_zone_arn": landing_zone_arn,
            "landing_zone_identifier": landing_zone_identifier,
        }

    @builtins.property
    def landing_zone_arn(self) -> builtins.str:
        '''The ARN of the LandingZone resource.'''
        result = self._values.get("landing_zone_arn")
        assert result is not None, "Required property 'landing_zone_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def landing_zone_identifier(self) -> builtins.str:
        '''The LandingZoneIdentifier of the LandingZone resource.'''
        result = self._values.get("landing_zone_identifier")
        assert result is not None, "Required property 'landing_zone_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LandingZoneReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "EnabledBaselineReference",
    "EnabledControlReference",
    "IEnabledBaselineRef",
    "IEnabledControlRef",
    "ILandingZoneRef",
    "LandingZoneReference",
]

publication.publish()

def _typecheckingstub__131ca4cc561cbb4aa73ec0084a3232b76e8f345bad523722000b9a6806841282(
    *,
    enabled_baseline_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb9591522b427f0e2c9e99083beb4f143ec50e993bdc26049fcce9d1b5fd5f4(
    *,
    control_identifier: builtins.str,
    target_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__433a90da81f818d83b8df0e666ab36391cc14c2e043d9d9957de21c1d16101d6(
    *,
    landing_zone_arn: builtins.str,
    landing_zone_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IEnabledBaselineRef, IEnabledControlRef, ILandingZoneRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
