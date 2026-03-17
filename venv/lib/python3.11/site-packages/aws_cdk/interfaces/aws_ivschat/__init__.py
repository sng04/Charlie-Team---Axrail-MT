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
    jsii_type="aws-cdk-lib.interfaces.aws_ivschat.ILoggingConfigurationRef"
)
class ILoggingConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LoggingConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="loggingConfigurationRef")
    def logging_configuration_ref(self) -> "LoggingConfigurationReference":
        '''(experimental) A reference to a LoggingConfiguration resource.

        :stability: experimental
        '''
        ...


class _ILoggingConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LoggingConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivschat.ILoggingConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="loggingConfigurationRef")
    def logging_configuration_ref(self) -> "LoggingConfigurationReference":
        '''(experimental) A reference to a LoggingConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("LoggingConfigurationReference", jsii.get(self, "loggingConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILoggingConfigurationRef).__jsii_proxy_class__ = lambda : _ILoggingConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ivschat.IRoomRef")
class IRoomRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Room.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="roomRef")
    def room_ref(self) -> "RoomReference":
        '''(experimental) A reference to a Room resource.

        :stability: experimental
        '''
        ...


class _IRoomRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Room.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivschat.IRoomRef"

    @builtins.property
    @jsii.member(jsii_name="roomRef")
    def room_ref(self) -> "RoomReference":
        '''(experimental) A reference to a Room resource.

        :stability: experimental
        '''
        return typing.cast("RoomReference", jsii.get(self, "roomRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRoomRef).__jsii_proxy_class__ = lambda : _IRoomRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivschat.LoggingConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"logging_configuration_arn": "loggingConfigurationArn"},
)
class LoggingConfigurationReference:
    def __init__(self, *, logging_configuration_arn: builtins.str) -> None:
        '''A reference to a LoggingConfiguration resource.

        :param logging_configuration_arn: The Arn of the LoggingConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivschat as interfaces_ivschat
            
            logging_configuration_reference = interfaces_ivschat.LoggingConfigurationReference(
                logging_configuration_arn="loggingConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15baa939451564d0eef5ba7191562fdfa0149f13ee4af21603974ecc4ebe2e69)
            check_type(argname="argument logging_configuration_arn", value=logging_configuration_arn, expected_type=type_hints["logging_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "logging_configuration_arn": logging_configuration_arn,
        }

    @builtins.property
    def logging_configuration_arn(self) -> builtins.str:
        '''The Arn of the LoggingConfiguration resource.'''
        result = self._values.get("logging_configuration_arn")
        assert result is not None, "Required property 'logging_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivschat.RoomReference",
    jsii_struct_bases=[],
    name_mapping={"room_arn": "roomArn"},
)
class RoomReference:
    def __init__(self, *, room_arn: builtins.str) -> None:
        '''A reference to a Room resource.

        :param room_arn: The Arn of the Room resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivschat as interfaces_ivschat
            
            room_reference = interfaces_ivschat.RoomReference(
                room_arn="roomArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a5951398c1c95d97cc9ebc1f43e1d5c7dcdf44ec60c9edff45d1d9ce1f8883d)
            check_type(argname="argument room_arn", value=room_arn, expected_type=type_hints["room_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "room_arn": room_arn,
        }

    @builtins.property
    def room_arn(self) -> builtins.str:
        '''The Arn of the Room resource.'''
        result = self._values.get("room_arn")
        assert result is not None, "Required property 'room_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoomReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ILoggingConfigurationRef",
    "IRoomRef",
    "LoggingConfigurationReference",
    "RoomReference",
]

publication.publish()

def _typecheckingstub__15baa939451564d0eef5ba7191562fdfa0149f13ee4af21603974ecc4ebe2e69(
    *,
    logging_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a5951398c1c95d97cc9ebc1f43e1d5c7dcdf44ec60c9edff45d1d9ce1f8883d(
    *,
    room_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ILoggingConfigurationRef, IRoomRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
