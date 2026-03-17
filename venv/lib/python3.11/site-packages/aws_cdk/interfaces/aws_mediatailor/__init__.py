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
    jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.ChannelPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"channel_name": "channelName"},
)
class ChannelPolicyReference:
    def __init__(self, *, channel_name: builtins.str) -> None:
        '''A reference to a ChannelPolicy resource.

        :param channel_name: The ChannelName of the ChannelPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediatailor as interfaces_mediatailor
            
            channel_policy_reference = interfaces_mediatailor.ChannelPolicyReference(
                channel_name="channelName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f37e3165ac2608b7c2ff156f4a425a53d6485953bf8becaaebe7f54f07c8a588)
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_name": channel_name,
        }

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The ChannelName of the ChannelPolicy resource.'''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.ChannelReference",
    jsii_struct_bases=[],
    name_mapping={"channel_arn": "channelArn", "channel_name": "channelName"},
)
class ChannelReference:
    def __init__(
        self,
        *,
        channel_arn: builtins.str,
        channel_name: builtins.str,
    ) -> None:
        '''A reference to a Channel resource.

        :param channel_arn: The ARN of the Channel resource.
        :param channel_name: The ChannelName of the Channel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediatailor as interfaces_mediatailor
            
            channel_reference = interfaces_mediatailor.ChannelReference(
                channel_arn="channelArn",
                channel_name="channelName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__086dd4896fac32f634b3a32200eb3a76698c4796f218c2131a16e38813adaf31)
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_arn": channel_arn,
            "channel_name": channel_name,
        }

    @builtins.property
    def channel_arn(self) -> builtins.str:
        '''The ARN of the Channel resource.'''
        result = self._values.get("channel_arn")
        assert result is not None, "Required property 'channel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The ChannelName of the Channel resource.'''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.IChannelPolicyRef")
class IChannelPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelPolicyRef")
    def channel_policy_ref(self) -> "ChannelPolicyReference":
        '''(experimental) A reference to a ChannelPolicy resource.

        :stability: experimental
        '''
        ...


class _IChannelPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediatailor.IChannelPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="channelPolicyRef")
    def channel_policy_ref(self) -> "ChannelPolicyReference":
        '''(experimental) A reference to a ChannelPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ChannelPolicyReference", jsii.get(self, "channelPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelPolicyRef).__jsii_proxy_class__ = lambda : _IChannelPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.IChannelRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediatailor.IChannelRef"

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        return typing.cast("ChannelReference", jsii.get(self, "channelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelRef).__jsii_proxy_class__ = lambda : _IChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.ILiveSourceRef")
class ILiveSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LiveSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="liveSourceRef")
    def live_source_ref(self) -> "LiveSourceReference":
        '''(experimental) A reference to a LiveSource resource.

        :stability: experimental
        '''
        ...


class _ILiveSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LiveSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediatailor.ILiveSourceRef"

    @builtins.property
    @jsii.member(jsii_name="liveSourceRef")
    def live_source_ref(self) -> "LiveSourceReference":
        '''(experimental) A reference to a LiveSource resource.

        :stability: experimental
        '''
        return typing.cast("LiveSourceReference", jsii.get(self, "liveSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILiveSourceRef).__jsii_proxy_class__ = lambda : _ILiveSourceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.IPlaybackConfigurationRef"
)
class IPlaybackConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PlaybackConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="playbackConfigurationRef")
    def playback_configuration_ref(self) -> "PlaybackConfigurationReference":
        '''(experimental) A reference to a PlaybackConfiguration resource.

        :stability: experimental
        '''
        ...


class _IPlaybackConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PlaybackConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediatailor.IPlaybackConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="playbackConfigurationRef")
    def playback_configuration_ref(self) -> "PlaybackConfigurationReference":
        '''(experimental) A reference to a PlaybackConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("PlaybackConfigurationReference", jsii.get(self, "playbackConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPlaybackConfigurationRef).__jsii_proxy_class__ = lambda : _IPlaybackConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.ISourceLocationRef")
class ISourceLocationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SourceLocation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sourceLocationRef")
    def source_location_ref(self) -> "SourceLocationReference":
        '''(experimental) A reference to a SourceLocation resource.

        :stability: experimental
        '''
        ...


class _ISourceLocationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SourceLocation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediatailor.ISourceLocationRef"

    @builtins.property
    @jsii.member(jsii_name="sourceLocationRef")
    def source_location_ref(self) -> "SourceLocationReference":
        '''(experimental) A reference to a SourceLocation resource.

        :stability: experimental
        '''
        return typing.cast("SourceLocationReference", jsii.get(self, "sourceLocationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISourceLocationRef).__jsii_proxy_class__ = lambda : _ISourceLocationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.IVodSourceRef")
class IVodSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VodSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vodSourceRef")
    def vod_source_ref(self) -> "VodSourceReference":
        '''(experimental) A reference to a VodSource resource.

        :stability: experimental
        '''
        ...


class _IVodSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VodSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediatailor.IVodSourceRef"

    @builtins.property
    @jsii.member(jsii_name="vodSourceRef")
    def vod_source_ref(self) -> "VodSourceReference":
        '''(experimental) A reference to a VodSource resource.

        :stability: experimental
        '''
        return typing.cast("VodSourceReference", jsii.get(self, "vodSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVodSourceRef).__jsii_proxy_class__ = lambda : _IVodSourceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.LiveSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "live_source_arn": "liveSourceArn",
        "live_source_name": "liveSourceName",
        "source_location_name": "sourceLocationName",
    },
)
class LiveSourceReference:
    def __init__(
        self,
        *,
        live_source_arn: builtins.str,
        live_source_name: builtins.str,
        source_location_name: builtins.str,
    ) -> None:
        '''A reference to a LiveSource resource.

        :param live_source_arn: The ARN of the LiveSource resource.
        :param live_source_name: The LiveSourceName of the LiveSource resource.
        :param source_location_name: The SourceLocationName of the LiveSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediatailor as interfaces_mediatailor
            
            live_source_reference = interfaces_mediatailor.LiveSourceReference(
                live_source_arn="liveSourceArn",
                live_source_name="liveSourceName",
                source_location_name="sourceLocationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a564cf5f5dcac0d7efa00a183776f0f63bb3a946621e96d6ec491e8c4d2136bd)
            check_type(argname="argument live_source_arn", value=live_source_arn, expected_type=type_hints["live_source_arn"])
            check_type(argname="argument live_source_name", value=live_source_name, expected_type=type_hints["live_source_name"])
            check_type(argname="argument source_location_name", value=source_location_name, expected_type=type_hints["source_location_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "live_source_arn": live_source_arn,
            "live_source_name": live_source_name,
            "source_location_name": source_location_name,
        }

    @builtins.property
    def live_source_arn(self) -> builtins.str:
        '''The ARN of the LiveSource resource.'''
        result = self._values.get("live_source_arn")
        assert result is not None, "Required property 'live_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def live_source_name(self) -> builtins.str:
        '''The LiveSourceName of the LiveSource resource.'''
        result = self._values.get("live_source_name")
        assert result is not None, "Required property 'live_source_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_location_name(self) -> builtins.str:
        '''The SourceLocationName of the LiveSource resource.'''
        result = self._values.get("source_location_name")
        assert result is not None, "Required property 'source_location_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LiveSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.PlaybackConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "playback_configuration_arn": "playbackConfigurationArn",
        "playback_configuration_name": "playbackConfigurationName",
    },
)
class PlaybackConfigurationReference:
    def __init__(
        self,
        *,
        playback_configuration_arn: builtins.str,
        playback_configuration_name: builtins.str,
    ) -> None:
        '''A reference to a PlaybackConfiguration resource.

        :param playback_configuration_arn: The ARN of the PlaybackConfiguration resource.
        :param playback_configuration_name: The Name of the PlaybackConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediatailor as interfaces_mediatailor
            
            playback_configuration_reference = interfaces_mediatailor.PlaybackConfigurationReference(
                playback_configuration_arn="playbackConfigurationArn",
                playback_configuration_name="playbackConfigurationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf613545aa68f893fc0bd727d1eeee7017a21e18e95230dc9096d2f25abdac09)
            check_type(argname="argument playback_configuration_arn", value=playback_configuration_arn, expected_type=type_hints["playback_configuration_arn"])
            check_type(argname="argument playback_configuration_name", value=playback_configuration_name, expected_type=type_hints["playback_configuration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "playback_configuration_arn": playback_configuration_arn,
            "playback_configuration_name": playback_configuration_name,
        }

    @builtins.property
    def playback_configuration_arn(self) -> builtins.str:
        '''The ARN of the PlaybackConfiguration resource.'''
        result = self._values.get("playback_configuration_arn")
        assert result is not None, "Required property 'playback_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def playback_configuration_name(self) -> builtins.str:
        '''The Name of the PlaybackConfiguration resource.'''
        result = self._values.get("playback_configuration_name")
        assert result is not None, "Required property 'playback_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PlaybackConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.SourceLocationReference",
    jsii_struct_bases=[],
    name_mapping={
        "source_location_arn": "sourceLocationArn",
        "source_location_name": "sourceLocationName",
    },
)
class SourceLocationReference:
    def __init__(
        self,
        *,
        source_location_arn: builtins.str,
        source_location_name: builtins.str,
    ) -> None:
        '''A reference to a SourceLocation resource.

        :param source_location_arn: The ARN of the SourceLocation resource.
        :param source_location_name: The SourceLocationName of the SourceLocation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediatailor as interfaces_mediatailor
            
            source_location_reference = interfaces_mediatailor.SourceLocationReference(
                source_location_arn="sourceLocationArn",
                source_location_name="sourceLocationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58e44b714a33a6fdedacf6bb2020c3d928b4ae4ce7b026dc15f5b3d45016165f)
            check_type(argname="argument source_location_arn", value=source_location_arn, expected_type=type_hints["source_location_arn"])
            check_type(argname="argument source_location_name", value=source_location_name, expected_type=type_hints["source_location_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_location_arn": source_location_arn,
            "source_location_name": source_location_name,
        }

    @builtins.property
    def source_location_arn(self) -> builtins.str:
        '''The ARN of the SourceLocation resource.'''
        result = self._values.get("source_location_arn")
        assert result is not None, "Required property 'source_location_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_location_name(self) -> builtins.str:
        '''The SourceLocationName of the SourceLocation resource.'''
        result = self._values.get("source_location_name")
        assert result is not None, "Required property 'source_location_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SourceLocationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediatailor.VodSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "source_location_name": "sourceLocationName",
        "vod_source_arn": "vodSourceArn",
        "vod_source_name": "vodSourceName",
    },
)
class VodSourceReference:
    def __init__(
        self,
        *,
        source_location_name: builtins.str,
        vod_source_arn: builtins.str,
        vod_source_name: builtins.str,
    ) -> None:
        '''A reference to a VodSource resource.

        :param source_location_name: The SourceLocationName of the VodSource resource.
        :param vod_source_arn: The ARN of the VodSource resource.
        :param vod_source_name: The VodSourceName of the VodSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediatailor as interfaces_mediatailor
            
            vod_source_reference = interfaces_mediatailor.VodSourceReference(
                source_location_name="sourceLocationName",
                vod_source_arn="vodSourceArn",
                vod_source_name="vodSourceName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6a76b4e25fe3c65837b46020060418da7098205d91980c8a0d2168660ccb85d)
            check_type(argname="argument source_location_name", value=source_location_name, expected_type=type_hints["source_location_name"])
            check_type(argname="argument vod_source_arn", value=vod_source_arn, expected_type=type_hints["vod_source_arn"])
            check_type(argname="argument vod_source_name", value=vod_source_name, expected_type=type_hints["vod_source_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_location_name": source_location_name,
            "vod_source_arn": vod_source_arn,
            "vod_source_name": vod_source_name,
        }

    @builtins.property
    def source_location_name(self) -> builtins.str:
        '''The SourceLocationName of the VodSource resource.'''
        result = self._values.get("source_location_name")
        assert result is not None, "Required property 'source_location_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vod_source_arn(self) -> builtins.str:
        '''The ARN of the VodSource resource.'''
        result = self._values.get("vod_source_arn")
        assert result is not None, "Required property 'vod_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vod_source_name(self) -> builtins.str:
        '''The VodSourceName of the VodSource resource.'''
        result = self._values.get("vod_source_name")
        assert result is not None, "Required property 'vod_source_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VodSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ChannelPolicyReference",
    "ChannelReference",
    "IChannelPolicyRef",
    "IChannelRef",
    "ILiveSourceRef",
    "IPlaybackConfigurationRef",
    "ISourceLocationRef",
    "IVodSourceRef",
    "LiveSourceReference",
    "PlaybackConfigurationReference",
    "SourceLocationReference",
    "VodSourceReference",
]

publication.publish()

def _typecheckingstub__f37e3165ac2608b7c2ff156f4a425a53d6485953bf8becaaebe7f54f07c8a588(
    *,
    channel_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__086dd4896fac32f634b3a32200eb3a76698c4796f218c2131a16e38813adaf31(
    *,
    channel_arn: builtins.str,
    channel_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a564cf5f5dcac0d7efa00a183776f0f63bb3a946621e96d6ec491e8c4d2136bd(
    *,
    live_source_arn: builtins.str,
    live_source_name: builtins.str,
    source_location_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf613545aa68f893fc0bd727d1eeee7017a21e18e95230dc9096d2f25abdac09(
    *,
    playback_configuration_arn: builtins.str,
    playback_configuration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58e44b714a33a6fdedacf6bb2020c3d928b4ae4ce7b026dc15f5b3d45016165f(
    *,
    source_location_arn: builtins.str,
    source_location_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6a76b4e25fe3c65837b46020060418da7098205d91980c8a0d2168660ccb85d(
    *,
    source_location_name: builtins.str,
    vod_source_arn: builtins.str,
    vod_source_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IChannelPolicyRef, IChannelRef, ILiveSourceRef, IPlaybackConfigurationRef, ISourceLocationRef, IVodSourceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
