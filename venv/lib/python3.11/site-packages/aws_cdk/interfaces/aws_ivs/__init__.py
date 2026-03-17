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
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.ChannelReference",
    jsii_struct_bases=[],
    name_mapping={"channel_arn": "channelArn"},
)
class ChannelReference:
    def __init__(self, *, channel_arn: builtins.str) -> None:
        '''A reference to a Channel resource.

        :param channel_arn: The Arn of the Channel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivs as interfaces_ivs
            
            channel_reference = interfaces_ivs.ChannelReference(
                channel_arn="channelArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e339be0e2b8a2e7786775e7d7a073c0d9b1b21d2186633192278591cee6af2e1)
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_arn": channel_arn,
        }

    @builtins.property
    def channel_arn(self) -> builtins.str:
        '''The Arn of the Channel resource.'''
        result = self._values.get("channel_arn")
        assert result is not None, "Required property 'channel_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.EncoderConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"encoder_configuration_arn": "encoderConfigurationArn"},
)
class EncoderConfigurationReference:
    def __init__(self, *, encoder_configuration_arn: builtins.str) -> None:
        '''A reference to a EncoderConfiguration resource.

        :param encoder_configuration_arn: The Arn of the EncoderConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivs as interfaces_ivs
            
            encoder_configuration_reference = interfaces_ivs.EncoderConfigurationReference(
                encoder_configuration_arn="encoderConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__506569603443e93b498d806eec145a27033c1e925e3f127178b87759f2386a54)
            check_type(argname="argument encoder_configuration_arn", value=encoder_configuration_arn, expected_type=type_hints["encoder_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encoder_configuration_arn": encoder_configuration_arn,
        }

    @builtins.property
    def encoder_configuration_arn(self) -> builtins.str:
        '''The Arn of the EncoderConfiguration resource.'''
        result = self._values.get("encoder_configuration_arn")
        assert result is not None, "Required property 'encoder_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EncoderConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ivs.IChannelRef")
class IChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Channel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        ...


class _IChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Channel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivs.IChannelRef"

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        return typing.cast("ChannelReference", jsii.get(self, "channelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelRef).__jsii_proxy_class__ = lambda : _IChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ivs.IEncoderConfigurationRef")
class IEncoderConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EncoderConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="encoderConfigurationRef")
    def encoder_configuration_ref(self) -> "EncoderConfigurationReference":
        '''(experimental) A reference to a EncoderConfiguration resource.

        :stability: experimental
        '''
        ...


class _IEncoderConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EncoderConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivs.IEncoderConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="encoderConfigurationRef")
    def encoder_configuration_ref(self) -> "EncoderConfigurationReference":
        '''(experimental) A reference to a EncoderConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("EncoderConfigurationReference", jsii.get(self, "encoderConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEncoderConfigurationRef).__jsii_proxy_class__ = lambda : _IEncoderConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ivs.IIngestConfigurationRef")
class IIngestConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IngestConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ingestConfigurationRef")
    def ingest_configuration_ref(self) -> "IngestConfigurationReference":
        '''(experimental) A reference to a IngestConfiguration resource.

        :stability: experimental
        '''
        ...


class _IIngestConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IngestConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivs.IIngestConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="ingestConfigurationRef")
    def ingest_configuration_ref(self) -> "IngestConfigurationReference":
        '''(experimental) A reference to a IngestConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("IngestConfigurationReference", jsii.get(self, "ingestConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIngestConfigurationRef).__jsii_proxy_class__ = lambda : _IIngestConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ivs.IPlaybackKeyPairRef")
class IPlaybackKeyPairRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PlaybackKeyPair.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="playbackKeyPairRef")
    def playback_key_pair_ref(self) -> "PlaybackKeyPairReference":
        '''(experimental) A reference to a PlaybackKeyPair resource.

        :stability: experimental
        '''
        ...


class _IPlaybackKeyPairRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PlaybackKeyPair.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivs.IPlaybackKeyPairRef"

    @builtins.property
    @jsii.member(jsii_name="playbackKeyPairRef")
    def playback_key_pair_ref(self) -> "PlaybackKeyPairReference":
        '''(experimental) A reference to a PlaybackKeyPair resource.

        :stability: experimental
        '''
        return typing.cast("PlaybackKeyPairReference", jsii.get(self, "playbackKeyPairRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPlaybackKeyPairRef).__jsii_proxy_class__ = lambda : _IPlaybackKeyPairRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.IPlaybackRestrictionPolicyRef"
)
class IPlaybackRestrictionPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PlaybackRestrictionPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="playbackRestrictionPolicyRef")
    def playback_restriction_policy_ref(self) -> "PlaybackRestrictionPolicyReference":
        '''(experimental) A reference to a PlaybackRestrictionPolicy resource.

        :stability: experimental
        '''
        ...


class _IPlaybackRestrictionPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PlaybackRestrictionPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivs.IPlaybackRestrictionPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="playbackRestrictionPolicyRef")
    def playback_restriction_policy_ref(self) -> "PlaybackRestrictionPolicyReference":
        '''(experimental) A reference to a PlaybackRestrictionPolicy resource.

        :stability: experimental
        '''
        return typing.cast("PlaybackRestrictionPolicyReference", jsii.get(self, "playbackRestrictionPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPlaybackRestrictionPolicyRef).__jsii_proxy_class__ = lambda : _IPlaybackRestrictionPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ivs.IPublicKeyRef")
class IPublicKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PublicKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="publicKeyRef")
    def public_key_ref(self) -> "PublicKeyReference":
        '''(experimental) A reference to a PublicKey resource.

        :stability: experimental
        '''
        ...


class _IPublicKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PublicKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivs.IPublicKeyRef"

    @builtins.property
    @jsii.member(jsii_name="publicKeyRef")
    def public_key_ref(self) -> "PublicKeyReference":
        '''(experimental) A reference to a PublicKey resource.

        :stability: experimental
        '''
        return typing.cast("PublicKeyReference", jsii.get(self, "publicKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublicKeyRef).__jsii_proxy_class__ = lambda : _IPublicKeyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ivs.IRecordingConfigurationRef")
class IRecordingConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RecordingConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="recordingConfigurationRef")
    def recording_configuration_ref(self) -> "RecordingConfigurationReference":
        '''(experimental) A reference to a RecordingConfiguration resource.

        :stability: experimental
        '''
        ...


class _IRecordingConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RecordingConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivs.IRecordingConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="recordingConfigurationRef")
    def recording_configuration_ref(self) -> "RecordingConfigurationReference":
        '''(experimental) A reference to a RecordingConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("RecordingConfigurationReference", jsii.get(self, "recordingConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRecordingConfigurationRef).__jsii_proxy_class__ = lambda : _IRecordingConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ivs.IStageRef")
class IStageRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Stage.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stageRef")
    def stage_ref(self) -> "StageReference":
        '''(experimental) A reference to a Stage resource.

        :stability: experimental
        '''
        ...


class _IStageRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Stage.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivs.IStageRef"

    @builtins.property
    @jsii.member(jsii_name="stageRef")
    def stage_ref(self) -> "StageReference":
        '''(experimental) A reference to a Stage resource.

        :stability: experimental
        '''
        return typing.cast("StageReference", jsii.get(self, "stageRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStageRef).__jsii_proxy_class__ = lambda : _IStageRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ivs.IStorageConfigurationRef")
class IStorageConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StorageConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="storageConfigurationRef")
    def storage_configuration_ref(self) -> "StorageConfigurationReference":
        '''(experimental) A reference to a StorageConfiguration resource.

        :stability: experimental
        '''
        ...


class _IStorageConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StorageConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivs.IStorageConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="storageConfigurationRef")
    def storage_configuration_ref(self) -> "StorageConfigurationReference":
        '''(experimental) A reference to a StorageConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("StorageConfigurationReference", jsii.get(self, "storageConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStorageConfigurationRef).__jsii_proxy_class__ = lambda : _IStorageConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ivs.IStreamKeyRef")
class IStreamKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StreamKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="streamKeyRef")
    def stream_key_ref(self) -> "StreamKeyReference":
        '''(experimental) A reference to a StreamKey resource.

        :stability: experimental
        '''
        ...


class _IStreamKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StreamKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ivs.IStreamKeyRef"

    @builtins.property
    @jsii.member(jsii_name="streamKeyRef")
    def stream_key_ref(self) -> "StreamKeyReference":
        '''(experimental) A reference to a StreamKey resource.

        :stability: experimental
        '''
        return typing.cast("StreamKeyReference", jsii.get(self, "streamKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStreamKeyRef).__jsii_proxy_class__ = lambda : _IStreamKeyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.IngestConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"ingest_configuration_arn": "ingestConfigurationArn"},
)
class IngestConfigurationReference:
    def __init__(self, *, ingest_configuration_arn: builtins.str) -> None:
        '''A reference to a IngestConfiguration resource.

        :param ingest_configuration_arn: The Arn of the IngestConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivs as interfaces_ivs
            
            ingest_configuration_reference = interfaces_ivs.IngestConfigurationReference(
                ingest_configuration_arn="ingestConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8983c9ebd60cc15d50cf31bb43c4c04b6ee8d51e7e2a6f96a61772c154a0dc87)
            check_type(argname="argument ingest_configuration_arn", value=ingest_configuration_arn, expected_type=type_hints["ingest_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ingest_configuration_arn": ingest_configuration_arn,
        }

    @builtins.property
    def ingest_configuration_arn(self) -> builtins.str:
        '''The Arn of the IngestConfiguration resource.'''
        result = self._values.get("ingest_configuration_arn")
        assert result is not None, "Required property 'ingest_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IngestConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.PlaybackKeyPairReference",
    jsii_struct_bases=[],
    name_mapping={"playback_key_pair_arn": "playbackKeyPairArn"},
)
class PlaybackKeyPairReference:
    def __init__(self, *, playback_key_pair_arn: builtins.str) -> None:
        '''A reference to a PlaybackKeyPair resource.

        :param playback_key_pair_arn: The Arn of the PlaybackKeyPair resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivs as interfaces_ivs
            
            playback_key_pair_reference = interfaces_ivs.PlaybackKeyPairReference(
                playback_key_pair_arn="playbackKeyPairArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c175fee0dca6f668aa85f241c8660a0af4afbee9e4a2a4cb341884c88e42eb4)
            check_type(argname="argument playback_key_pair_arn", value=playback_key_pair_arn, expected_type=type_hints["playback_key_pair_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "playback_key_pair_arn": playback_key_pair_arn,
        }

    @builtins.property
    def playback_key_pair_arn(self) -> builtins.str:
        '''The Arn of the PlaybackKeyPair resource.'''
        result = self._values.get("playback_key_pair_arn")
        assert result is not None, "Required property 'playback_key_pair_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlaybackKeyPairReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.PlaybackRestrictionPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"playback_restriction_policy_arn": "playbackRestrictionPolicyArn"},
)
class PlaybackRestrictionPolicyReference:
    def __init__(self, *, playback_restriction_policy_arn: builtins.str) -> None:
        '''A reference to a PlaybackRestrictionPolicy resource.

        :param playback_restriction_policy_arn: The Arn of the PlaybackRestrictionPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivs as interfaces_ivs
            
            playback_restriction_policy_reference = interfaces_ivs.PlaybackRestrictionPolicyReference(
                playback_restriction_policy_arn="playbackRestrictionPolicyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf7183876fd6b6a73aefd70dc6d8329acf02be1b9b44a458ee1e39a4be78f452)
            check_type(argname="argument playback_restriction_policy_arn", value=playback_restriction_policy_arn, expected_type=type_hints["playback_restriction_policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "playback_restriction_policy_arn": playback_restriction_policy_arn,
        }

    @builtins.property
    def playback_restriction_policy_arn(self) -> builtins.str:
        '''The Arn of the PlaybackRestrictionPolicy resource.'''
        result = self._values.get("playback_restriction_policy_arn")
        assert result is not None, "Required property 'playback_restriction_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlaybackRestrictionPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.PublicKeyReference",
    jsii_struct_bases=[],
    name_mapping={"public_key_arn": "publicKeyArn"},
)
class PublicKeyReference:
    def __init__(self, *, public_key_arn: builtins.str) -> None:
        '''A reference to a PublicKey resource.

        :param public_key_arn: The Arn of the PublicKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivs as interfaces_ivs
            
            public_key_reference = interfaces_ivs.PublicKeyReference(
                public_key_arn="publicKeyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc6fecdb6785320bf110143fe154bc7d01ed9e098e59c4bc5e920c76720b65df)
            check_type(argname="argument public_key_arn", value=public_key_arn, expected_type=type_hints["public_key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "public_key_arn": public_key_arn,
        }

    @builtins.property
    def public_key_arn(self) -> builtins.str:
        '''The Arn of the PublicKey resource.'''
        result = self._values.get("public_key_arn")
        assert result is not None, "Required property 'public_key_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.RecordingConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"recording_configuration_arn": "recordingConfigurationArn"},
)
class RecordingConfigurationReference:
    def __init__(self, *, recording_configuration_arn: builtins.str) -> None:
        '''A reference to a RecordingConfiguration resource.

        :param recording_configuration_arn: The Arn of the RecordingConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivs as interfaces_ivs
            
            recording_configuration_reference = interfaces_ivs.RecordingConfigurationReference(
                recording_configuration_arn="recordingConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bf8be966bd4973856cf96ae0f38521f5f5e7d8e55a6a002137449f95f08102a)
            check_type(argname="argument recording_configuration_arn", value=recording_configuration_arn, expected_type=type_hints["recording_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "recording_configuration_arn": recording_configuration_arn,
        }

    @builtins.property
    def recording_configuration_arn(self) -> builtins.str:
        '''The Arn of the RecordingConfiguration resource.'''
        result = self._values.get("recording_configuration_arn")
        assert result is not None, "Required property 'recording_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordingConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.StageReference",
    jsii_struct_bases=[],
    name_mapping={"stage_arn": "stageArn"},
)
class StageReference:
    def __init__(self, *, stage_arn: builtins.str) -> None:
        '''A reference to a Stage resource.

        :param stage_arn: The Arn of the Stage resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivs as interfaces_ivs
            
            stage_reference = interfaces_ivs.StageReference(
                stage_arn="stageArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05830f910c45363d095acbbefde5caaea99d18ba8678a18749bb1659d2a11848)
            check_type(argname="argument stage_arn", value=stage_arn, expected_type=type_hints["stage_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stage_arn": stage_arn,
        }

    @builtins.property
    def stage_arn(self) -> builtins.str:
        '''The Arn of the Stage resource.'''
        result = self._values.get("stage_arn")
        assert result is not None, "Required property 'stage_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.StorageConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"storage_configuration_arn": "storageConfigurationArn"},
)
class StorageConfigurationReference:
    def __init__(self, *, storage_configuration_arn: builtins.str) -> None:
        '''A reference to a StorageConfiguration resource.

        :param storage_configuration_arn: The Arn of the StorageConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivs as interfaces_ivs
            
            storage_configuration_reference = interfaces_ivs.StorageConfigurationReference(
                storage_configuration_arn="storageConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35c60ac23b33bfe34d8b206b0ec97c28755476924acb5e245b1f2247a5a5c9a1)
            check_type(argname="argument storage_configuration_arn", value=storage_configuration_arn, expected_type=type_hints["storage_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_configuration_arn": storage_configuration_arn,
        }

    @builtins.property
    def storage_configuration_arn(self) -> builtins.str:
        '''The Arn of the StorageConfiguration resource.'''
        result = self._values.get("storage_configuration_arn")
        assert result is not None, "Required property 'storage_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ivs.StreamKeyReference",
    jsii_struct_bases=[],
    name_mapping={"stream_key_arn": "streamKeyArn"},
)
class StreamKeyReference:
    def __init__(self, *, stream_key_arn: builtins.str) -> None:
        '''A reference to a StreamKey resource.

        :param stream_key_arn: The Arn of the StreamKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ivs as interfaces_ivs
            
            stream_key_reference = interfaces_ivs.StreamKeyReference(
                stream_key_arn="streamKeyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0bde005d759333868f9b20462c76032aeeb517956f3679f2a954d0b2f4ce9ce)
            check_type(argname="argument stream_key_arn", value=stream_key_arn, expected_type=type_hints["stream_key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stream_key_arn": stream_key_arn,
        }

    @builtins.property
    def stream_key_arn(self) -> builtins.str:
        '''The Arn of the StreamKey resource.'''
        result = self._values.get("stream_key_arn")
        assert result is not None, "Required property 'stream_key_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ChannelReference",
    "EncoderConfigurationReference",
    "IChannelRef",
    "IEncoderConfigurationRef",
    "IIngestConfigurationRef",
    "IPlaybackKeyPairRef",
    "IPlaybackRestrictionPolicyRef",
    "IPublicKeyRef",
    "IRecordingConfigurationRef",
    "IStageRef",
    "IStorageConfigurationRef",
    "IStreamKeyRef",
    "IngestConfigurationReference",
    "PlaybackKeyPairReference",
    "PlaybackRestrictionPolicyReference",
    "PublicKeyReference",
    "RecordingConfigurationReference",
    "StageReference",
    "StorageConfigurationReference",
    "StreamKeyReference",
]

publication.publish()

def _typecheckingstub__e339be0e2b8a2e7786775e7d7a073c0d9b1b21d2186633192278591cee6af2e1(
    *,
    channel_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__506569603443e93b498d806eec145a27033c1e925e3f127178b87759f2386a54(
    *,
    encoder_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8983c9ebd60cc15d50cf31bb43c4c04b6ee8d51e7e2a6f96a61772c154a0dc87(
    *,
    ingest_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c175fee0dca6f668aa85f241c8660a0af4afbee9e4a2a4cb341884c88e42eb4(
    *,
    playback_key_pair_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf7183876fd6b6a73aefd70dc6d8329acf02be1b9b44a458ee1e39a4be78f452(
    *,
    playback_restriction_policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc6fecdb6785320bf110143fe154bc7d01ed9e098e59c4bc5e920c76720b65df(
    *,
    public_key_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bf8be966bd4973856cf96ae0f38521f5f5e7d8e55a6a002137449f95f08102a(
    *,
    recording_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05830f910c45363d095acbbefde5caaea99d18ba8678a18749bb1659d2a11848(
    *,
    stage_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35c60ac23b33bfe34d8b206b0ec97c28755476924acb5e245b1f2247a5a5c9a1(
    *,
    storage_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0bde005d759333868f9b20462c76032aeeb517956f3679f2a954d0b2f4ce9ce(
    *,
    stream_key_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IChannelRef, IEncoderConfigurationRef, IIngestConfigurationRef, IPlaybackKeyPairRef, IPlaybackRestrictionPolicyRef, IPublicKeyRef, IRecordingConfigurationRef, IStageRef, IStorageConfigurationRef, IStreamKeyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
