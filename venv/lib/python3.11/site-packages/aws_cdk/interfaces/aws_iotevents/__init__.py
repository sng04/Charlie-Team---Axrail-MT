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
    jsii_type="aws-cdk-lib.interfaces.aws_iotevents.AlarmModelReference",
    jsii_struct_bases=[],
    name_mapping={"alarm_model_name": "alarmModelName"},
)
class AlarmModelReference:
    def __init__(self, *, alarm_model_name: builtins.str) -> None:
        '''A reference to a AlarmModel resource.

        :param alarm_model_name: The AlarmModelName of the AlarmModel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotevents as interfaces_iotevents
            
            alarm_model_reference = interfaces_iotevents.AlarmModelReference(
                alarm_model_name="alarmModelName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3f5fb40489a6692b5219544b6e9b6f22fb245be10dcaf37b5d5df5a1624c951)
            check_type(argname="argument alarm_model_name", value=alarm_model_name, expected_type=type_hints["alarm_model_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alarm_model_name": alarm_model_name,
        }

    @builtins.property
    def alarm_model_name(self) -> builtins.str:
        '''The AlarmModelName of the AlarmModel resource.'''
        result = self._values.get("alarm_model_name")
        assert result is not None, "Required property 'alarm_model_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AlarmModelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotevents.DetectorModelReference",
    jsii_struct_bases=[],
    name_mapping={"detector_model_name": "detectorModelName"},
)
class DetectorModelReference:
    def __init__(self, *, detector_model_name: builtins.str) -> None:
        '''A reference to a DetectorModel resource.

        :param detector_model_name: The DetectorModelName of the DetectorModel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotevents as interfaces_iotevents
            
            detector_model_reference = interfaces_iotevents.DetectorModelReference(
                detector_model_name="detectorModelName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a8998b12acad1694c766801dbc029eb3ebb0dd5fc872d69134a88ce04fc4b18)
            check_type(argname="argument detector_model_name", value=detector_model_name, expected_type=type_hints["detector_model_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "detector_model_name": detector_model_name,
        }

    @builtins.property
    def detector_model_name(self) -> builtins.str:
        '''The DetectorModelName of the DetectorModel resource.'''
        result = self._values.get("detector_model_name")
        assert result is not None, "Required property 'detector_model_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DetectorModelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotevents.IAlarmModelRef")
class IAlarmModelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AlarmModel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="alarmModelRef")
    def alarm_model_ref(self) -> "AlarmModelReference":
        '''(experimental) A reference to a AlarmModel resource.

        :stability: experimental
        '''
        ...


class _IAlarmModelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AlarmModel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotevents.IAlarmModelRef"

    @builtins.property
    @jsii.member(jsii_name="alarmModelRef")
    def alarm_model_ref(self) -> "AlarmModelReference":
        '''(experimental) A reference to a AlarmModel resource.

        :stability: experimental
        '''
        return typing.cast("AlarmModelReference", jsii.get(self, "alarmModelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAlarmModelRef).__jsii_proxy_class__ = lambda : _IAlarmModelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotevents.IDetectorModelRef")
class IDetectorModelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DetectorModel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="detectorModelRef")
    def detector_model_ref(self) -> "DetectorModelReference":
        '''(experimental) A reference to a DetectorModel resource.

        :stability: experimental
        '''
        ...


class _IDetectorModelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DetectorModel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotevents.IDetectorModelRef"

    @builtins.property
    @jsii.member(jsii_name="detectorModelRef")
    def detector_model_ref(self) -> "DetectorModelReference":
        '''(experimental) A reference to a DetectorModel resource.

        :stability: experimental
        '''
        return typing.cast("DetectorModelReference", jsii.get(self, "detectorModelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDetectorModelRef).__jsii_proxy_class__ = lambda : _IDetectorModelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotevents.IInputRef")
class IInputRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Input.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="inputRef")
    def input_ref(self) -> "InputReference":
        '''(experimental) A reference to a Input resource.

        :stability: experimental
        '''
        ...


class _IInputRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Input.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotevents.IInputRef"

    @builtins.property
    @jsii.member(jsii_name="inputRef")
    def input_ref(self) -> "InputReference":
        '''(experimental) A reference to a Input resource.

        :stability: experimental
        '''
        return typing.cast("InputReference", jsii.get(self, "inputRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInputRef).__jsii_proxy_class__ = lambda : _IInputRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iotevents.InputReference",
    jsii_struct_bases=[],
    name_mapping={"input_name": "inputName"},
)
class InputReference:
    def __init__(self, *, input_name: builtins.str) -> None:
        '''A reference to a Input resource.

        :param input_name: The InputName of the Input resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotevents as interfaces_iotevents
            
            input_reference = interfaces_iotevents.InputReference(
                input_name="inputName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92d11322c255495c3c986a6caebfb9f15d4066a0a881da36bca49fb7931f84aa)
            check_type(argname="argument input_name", value=input_name, expected_type=type_hints["input_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_name": input_name,
        }

    @builtins.property
    def input_name(self) -> builtins.str:
        '''The InputName of the Input resource.'''
        result = self._values.get("input_name")
        assert result is not None, "Required property 'input_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InputReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AlarmModelReference",
    "DetectorModelReference",
    "IAlarmModelRef",
    "IDetectorModelRef",
    "IInputRef",
    "InputReference",
]

publication.publish()

def _typecheckingstub__d3f5fb40489a6692b5219544b6e9b6f22fb245be10dcaf37b5d5df5a1624c951(
    *,
    alarm_model_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a8998b12acad1694c766801dbc029eb3ebb0dd5fc872d69134a88ce04fc4b18(
    *,
    detector_model_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92d11322c255495c3c986a6caebfb9f15d4066a0a881da36bca49fb7931f84aa(
    *,
    input_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAlarmModelRef, IDetectorModelRef, IInputRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
