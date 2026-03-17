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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisvideo.ISignalingChannelRef"
)
class ISignalingChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SignalingChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="signalingChannelRef")
    def signaling_channel_ref(self) -> "SignalingChannelReference":
        '''(experimental) A reference to a SignalingChannel resource.

        :stability: experimental
        '''
        ...


class _ISignalingChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SignalingChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesisvideo.ISignalingChannelRef"

    @builtins.property
    @jsii.member(jsii_name="signalingChannelRef")
    def signaling_channel_ref(self) -> "SignalingChannelReference":
        '''(experimental) A reference to a SignalingChannel resource.

        :stability: experimental
        '''
        return typing.cast("SignalingChannelReference", jsii.get(self, "signalingChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISignalingChannelRef).__jsii_proxy_class__ = lambda : _ISignalingChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kinesisvideo.IStreamRef")
class IStreamRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Stream.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="streamRef")
    def stream_ref(self) -> "StreamReference":
        '''(experimental) A reference to a Stream resource.

        :stability: experimental
        '''
        ...


class _IStreamRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Stream.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesisvideo.IStreamRef"

    @builtins.property
    @jsii.member(jsii_name="streamRef")
    def stream_ref(self) -> "StreamReference":
        '''(experimental) A reference to a Stream resource.

        :stability: experimental
        '''
        return typing.cast("StreamReference", jsii.get(self, "streamRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStreamRef).__jsii_proxy_class__ = lambda : _IStreamRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisvideo.SignalingChannelReference",
    jsii_struct_bases=[],
    name_mapping={
        "signaling_channel_arn": "signalingChannelArn",
        "signaling_channel_name": "signalingChannelName",
    },
)
class SignalingChannelReference:
    def __init__(
        self,
        *,
        signaling_channel_arn: builtins.str,
        signaling_channel_name: builtins.str,
    ) -> None:
        '''A reference to a SignalingChannel resource.

        :param signaling_channel_arn: The ARN of the SignalingChannel resource.
        :param signaling_channel_name: The Name of the SignalingChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kinesisvideo as interfaces_kinesisvideo
            
            signaling_channel_reference = interfaces_kinesisvideo.SignalingChannelReference(
                signaling_channel_arn="signalingChannelArn",
                signaling_channel_name="signalingChannelName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbea6590cf1ac5b2b7fc82135c5f8152ce6412db807b9ba354a4d6a67a6efc30)
            check_type(argname="argument signaling_channel_arn", value=signaling_channel_arn, expected_type=type_hints["signaling_channel_arn"])
            check_type(argname="argument signaling_channel_name", value=signaling_channel_name, expected_type=type_hints["signaling_channel_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "signaling_channel_arn": signaling_channel_arn,
            "signaling_channel_name": signaling_channel_name,
        }

    @builtins.property
    def signaling_channel_arn(self) -> builtins.str:
        '''The ARN of the SignalingChannel resource.'''
        result = self._values.get("signaling_channel_arn")
        assert result is not None, "Required property 'signaling_channel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signaling_channel_name(self) -> builtins.str:
        '''The Name of the SignalingChannel resource.'''
        result = self._values.get("signaling_channel_name")
        assert result is not None, "Required property 'signaling_channel_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalingChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisvideo.StreamReference",
    jsii_struct_bases=[],
    name_mapping={"stream_arn": "streamArn", "stream_name": "streamName"},
)
class StreamReference:
    def __init__(self, *, stream_arn: builtins.str, stream_name: builtins.str) -> None:
        '''A reference to a Stream resource.

        :param stream_arn: The ARN of the Stream resource.
        :param stream_name: The Name of the Stream resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kinesisvideo as interfaces_kinesisvideo
            
            stream_reference = interfaces_kinesisvideo.StreamReference(
                stream_arn="streamArn",
                stream_name="streamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b76bbb99572ea75459b1873aa00c8966861ac72d3d36547885c0f47e9bc51921)
            check_type(argname="argument stream_arn", value=stream_arn, expected_type=type_hints["stream_arn"])
            check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stream_arn": stream_arn,
            "stream_name": stream_name,
        }

    @builtins.property
    def stream_arn(self) -> builtins.str:
        '''The ARN of the Stream resource.'''
        result = self._values.get("stream_arn")
        assert result is not None, "Required property 'stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_name(self) -> builtins.str:
        '''The Name of the Stream resource.'''
        result = self._values.get("stream_name")
        assert result is not None, "Required property 'stream_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ISignalingChannelRef",
    "IStreamRef",
    "SignalingChannelReference",
    "StreamReference",
]

publication.publish()

def _typecheckingstub__bbea6590cf1ac5b2b7fc82135c5f8152ce6412db807b9ba354a4d6a67a6efc30(
    *,
    signaling_channel_arn: builtins.str,
    signaling_channel_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b76bbb99572ea75459b1873aa00c8966861ac72d3d36547885c0f47e9bc51921(
    *,
    stream_arn: builtins.str,
    stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ISignalingChannelRef, IStreamRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
