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
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackagev2.ChannelGroupReference",
    jsii_struct_bases=[],
    name_mapping={"channel_group_arn": "channelGroupArn"},
)
class ChannelGroupReference:
    def __init__(self, *, channel_group_arn: builtins.str) -> None:
        '''A reference to a ChannelGroup resource.

        :param channel_group_arn: The Arn of the ChannelGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediapackagev2 as interfaces_mediapackagev2
            
            channel_group_reference = interfaces_mediapackagev2.ChannelGroupReference(
                channel_group_arn="channelGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99924e78ca2a4d8adabc019160be260ec6b23d89acdfbe75931a04e4b2481238)
            check_type(argname="argument channel_group_arn", value=channel_group_arn, expected_type=type_hints["channel_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_group_arn": channel_group_arn,
        }

    @builtins.property
    def channel_group_arn(self) -> builtins.str:
        '''The Arn of the ChannelGroup resource.'''
        result = self._values.get("channel_group_arn")
        assert result is not None, "Required property 'channel_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackagev2.ChannelPolicyReference",
    jsii_struct_bases=[],
    name_mapping={
        "channel_group_name": "channelGroupName",
        "channel_name": "channelName",
    },
)
class ChannelPolicyReference:
    def __init__(
        self,
        *,
        channel_group_name: builtins.str,
        channel_name: builtins.str,
    ) -> None:
        '''A reference to a ChannelPolicy resource.

        :param channel_group_name: The ChannelGroupName of the ChannelPolicy resource.
        :param channel_name: The ChannelName of the ChannelPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediapackagev2 as interfaces_mediapackagev2
            
            channel_policy_reference = interfaces_mediapackagev2.ChannelPolicyReference(
                channel_group_name="channelGroupName",
                channel_name="channelName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39c79d2d8a36e2f448c2e9bcc20085e56a4c013770464b08f6fe065436ed858c)
            check_type(argname="argument channel_group_name", value=channel_group_name, expected_type=type_hints["channel_group_name"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
        }

    @builtins.property
    def channel_group_name(self) -> builtins.str:
        '''The ChannelGroupName of the ChannelPolicy resource.'''
        result = self._values.get("channel_group_name")
        assert result is not None, "Required property 'channel_group_name' is missing"
        return typing.cast(builtins.str, result)

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
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackagev2.ChannelReference",
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
            from aws_cdk.interfaces import aws_mediapackagev2 as interfaces_mediapackagev2
            
            channel_reference = interfaces_mediapackagev2.ChannelReference(
                channel_arn="channelArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e732e0925992b2d33f6eaaf633b6bf398af46820b1473b7637d1a0afb5206d9e)
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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediapackagev2.IChannelGroupRef")
class IChannelGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelGroupRef")
    def channel_group_ref(self) -> "ChannelGroupReference":
        '''(experimental) A reference to a ChannelGroup resource.

        :stability: experimental
        '''
        ...


class _IChannelGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediapackagev2.IChannelGroupRef"

    @builtins.property
    @jsii.member(jsii_name="channelGroupRef")
    def channel_group_ref(self) -> "ChannelGroupReference":
        '''(experimental) A reference to a ChannelGroup resource.

        :stability: experimental
        '''
        return typing.cast("ChannelGroupReference", jsii.get(self, "channelGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelGroupRef).__jsii_proxy_class__ = lambda : _IChannelGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackagev2.IChannelPolicyRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediapackagev2.IChannelPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="channelPolicyRef")
    def channel_policy_ref(self) -> "ChannelPolicyReference":
        '''(experimental) A reference to a ChannelPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ChannelPolicyReference", jsii.get(self, "channelPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelPolicyRef).__jsii_proxy_class__ = lambda : _IChannelPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediapackagev2.IChannelRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediapackagev2.IChannelRef"

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        return typing.cast("ChannelReference", jsii.get(self, "channelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelRef).__jsii_proxy_class__ = lambda : _IChannelRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackagev2.IOriginEndpointPolicyRef"
)
class IOriginEndpointPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OriginEndpointPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="originEndpointPolicyRef")
    def origin_endpoint_policy_ref(self) -> "OriginEndpointPolicyReference":
        '''(experimental) A reference to a OriginEndpointPolicy resource.

        :stability: experimental
        '''
        ...


class _IOriginEndpointPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OriginEndpointPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediapackagev2.IOriginEndpointPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="originEndpointPolicyRef")
    def origin_endpoint_policy_ref(self) -> "OriginEndpointPolicyReference":
        '''(experimental) A reference to a OriginEndpointPolicy resource.

        :stability: experimental
        '''
        return typing.cast("OriginEndpointPolicyReference", jsii.get(self, "originEndpointPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOriginEndpointPolicyRef).__jsii_proxy_class__ = lambda : _IOriginEndpointPolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackagev2.IOriginEndpointRef"
)
class IOriginEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OriginEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="originEndpointRef")
    def origin_endpoint_ref(self) -> "OriginEndpointReference":
        '''(experimental) A reference to a OriginEndpoint resource.

        :stability: experimental
        '''
        ...


class _IOriginEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OriginEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediapackagev2.IOriginEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="originEndpointRef")
    def origin_endpoint_ref(self) -> "OriginEndpointReference":
        '''(experimental) A reference to a OriginEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("OriginEndpointReference", jsii.get(self, "originEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOriginEndpointRef).__jsii_proxy_class__ = lambda : _IOriginEndpointRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackagev2.OriginEndpointPolicyReference",
    jsii_struct_bases=[],
    name_mapping={
        "channel_group_name": "channelGroupName",
        "channel_name": "channelName",
        "origin_endpoint_name": "originEndpointName",
    },
)
class OriginEndpointPolicyReference:
    def __init__(
        self,
        *,
        channel_group_name: builtins.str,
        channel_name: builtins.str,
        origin_endpoint_name: builtins.str,
    ) -> None:
        '''A reference to a OriginEndpointPolicy resource.

        :param channel_group_name: The ChannelGroupName of the OriginEndpointPolicy resource.
        :param channel_name: The ChannelName of the OriginEndpointPolicy resource.
        :param origin_endpoint_name: The OriginEndpointName of the OriginEndpointPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediapackagev2 as interfaces_mediapackagev2
            
            origin_endpoint_policy_reference = interfaces_mediapackagev2.OriginEndpointPolicyReference(
                channel_group_name="channelGroupName",
                channel_name="channelName",
                origin_endpoint_name="originEndpointName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e3d421537158c7e68c3c3ee992e39ba62d0b1457471667b2c9a1fe1d63ed729)
            check_type(argname="argument channel_group_name", value=channel_group_name, expected_type=type_hints["channel_group_name"])
            check_type(argname="argument channel_name", value=channel_name, expected_type=type_hints["channel_name"])
            check_type(argname="argument origin_endpoint_name", value=origin_endpoint_name, expected_type=type_hints["origin_endpoint_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_group_name": channel_group_name,
            "channel_name": channel_name,
            "origin_endpoint_name": origin_endpoint_name,
        }

    @builtins.property
    def channel_group_name(self) -> builtins.str:
        '''The ChannelGroupName of the OriginEndpointPolicy resource.'''
        result = self._values.get("channel_group_name")
        assert result is not None, "Required property 'channel_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_name(self) -> builtins.str:
        '''The ChannelName of the OriginEndpointPolicy resource.'''
        result = self._values.get("channel_name")
        assert result is not None, "Required property 'channel_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin_endpoint_name(self) -> builtins.str:
        '''The OriginEndpointName of the OriginEndpointPolicy resource.'''
        result = self._values.get("origin_endpoint_name")
        assert result is not None, "Required property 'origin_endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginEndpointPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackagev2.OriginEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"origin_endpoint_arn": "originEndpointArn"},
)
class OriginEndpointReference:
    def __init__(self, *, origin_endpoint_arn: builtins.str) -> None:
        '''A reference to a OriginEndpoint resource.

        :param origin_endpoint_arn: The Arn of the OriginEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediapackagev2 as interfaces_mediapackagev2
            
            origin_endpoint_reference = interfaces_mediapackagev2.OriginEndpointReference(
                origin_endpoint_arn="originEndpointArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__986e99cfc6c05e847589a9fe3fcd6145bb56221bd4038e96bd8bcffbdfb6817f)
            check_type(argname="argument origin_endpoint_arn", value=origin_endpoint_arn, expected_type=type_hints["origin_endpoint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "origin_endpoint_arn": origin_endpoint_arn,
        }

    @builtins.property
    def origin_endpoint_arn(self) -> builtins.str:
        '''The Arn of the OriginEndpoint resource.'''
        result = self._values.get("origin_endpoint_arn")
        assert result is not None, "Required property 'origin_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ChannelGroupReference",
    "ChannelPolicyReference",
    "ChannelReference",
    "IChannelGroupRef",
    "IChannelPolicyRef",
    "IChannelRef",
    "IOriginEndpointPolicyRef",
    "IOriginEndpointRef",
    "OriginEndpointPolicyReference",
    "OriginEndpointReference",
]

publication.publish()

def _typecheckingstub__99924e78ca2a4d8adabc019160be260ec6b23d89acdfbe75931a04e4b2481238(
    *,
    channel_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39c79d2d8a36e2f448c2e9bcc20085e56a4c013770464b08f6fe065436ed858c(
    *,
    channel_group_name: builtins.str,
    channel_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e732e0925992b2d33f6eaaf633b6bf398af46820b1473b7637d1a0afb5206d9e(
    *,
    channel_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e3d421537158c7e68c3c3ee992e39ba62d0b1457471667b2c9a1fe1d63ed729(
    *,
    channel_group_name: builtins.str,
    channel_name: builtins.str,
    origin_endpoint_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986e99cfc6c05e847589a9fe3fcd6145bb56221bd4038e96bd8bcffbdfb6817f(
    *,
    origin_endpoint_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IChannelGroupRef, IChannelPolicyRef, IChannelRef, IOriginEndpointPolicyRef, IOriginEndpointRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
