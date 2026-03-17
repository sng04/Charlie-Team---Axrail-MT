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
    jsii_type="aws-cdk-lib.interfaces.aws_cloudtrail.ChannelReference",
    jsii_struct_bases=[],
    name_mapping={"channel_arn": "channelArn"},
)
class ChannelReference:
    def __init__(self, *, channel_arn: builtins.str) -> None:
        '''A reference to a Channel resource.

        :param channel_arn: The ChannelArn of the Channel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudtrail as interfaces_cloudtrail
            
            channel_reference = interfaces_cloudtrail.ChannelReference(
                channel_arn="channelArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b1e4534590f5416c5abc69bf46a6e6f6977c7e439529c2cae4fd40303f444e5)
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_arn": channel_arn,
        }

    @builtins.property
    def channel_arn(self) -> builtins.str:
        '''The ChannelArn of the Channel resource.'''
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
    jsii_type="aws-cdk-lib.interfaces.aws_cloudtrail.DashboardReference",
    jsii_struct_bases=[],
    name_mapping={"dashboard_arn": "dashboardArn"},
)
class DashboardReference:
    def __init__(self, *, dashboard_arn: builtins.str) -> None:
        '''A reference to a Dashboard resource.

        :param dashboard_arn: The DashboardArn of the Dashboard resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudtrail as interfaces_cloudtrail
            
            dashboard_reference = interfaces_cloudtrail.DashboardReference(
                dashboard_arn="dashboardArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__605da928544d77164ada0eea8dbdcc59414c1ab694eb78c7f32c3d9912778901)
            check_type(argname="argument dashboard_arn", value=dashboard_arn, expected_type=type_hints["dashboard_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dashboard_arn": dashboard_arn,
        }

    @builtins.property
    def dashboard_arn(self) -> builtins.str:
        '''The DashboardArn of the Dashboard resource.'''
        result = self._values.get("dashboard_arn")
        assert result is not None, "Required property 'dashboard_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DashboardReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudtrail.EventDataStoreReference",
    jsii_struct_bases=[],
    name_mapping={"event_data_store_arn": "eventDataStoreArn"},
)
class EventDataStoreReference:
    def __init__(self, *, event_data_store_arn: builtins.str) -> None:
        '''A reference to a EventDataStore resource.

        :param event_data_store_arn: The EventDataStoreArn of the EventDataStore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudtrail as interfaces_cloudtrail
            
            event_data_store_reference = interfaces_cloudtrail.EventDataStoreReference(
                event_data_store_arn="eventDataStoreArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4579736f6ca2c03f650e12878b6ad5b99bec759b9a3ed1e253fe7cda8a48fe54)
            check_type(argname="argument event_data_store_arn", value=event_data_store_arn, expected_type=type_hints["event_data_store_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_data_store_arn": event_data_store_arn,
        }

    @builtins.property
    def event_data_store_arn(self) -> builtins.str:
        '''The EventDataStoreArn of the EventDataStore resource.'''
        result = self._values.get("event_data_store_arn")
        assert result is not None, "Required property 'event_data_store_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventDataStoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudtrail.IChannelRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudtrail.IChannelRef"

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        return typing.cast("ChannelReference", jsii.get(self, "channelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelRef).__jsii_proxy_class__ = lambda : _IChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudtrail.IDashboardRef")
class IDashboardRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Dashboard.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dashboardRef")
    def dashboard_ref(self) -> "DashboardReference":
        '''(experimental) A reference to a Dashboard resource.

        :stability: experimental
        '''
        ...


class _IDashboardRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Dashboard.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudtrail.IDashboardRef"

    @builtins.property
    @jsii.member(jsii_name="dashboardRef")
    def dashboard_ref(self) -> "DashboardReference":
        '''(experimental) A reference to a Dashboard resource.

        :stability: experimental
        '''
        return typing.cast("DashboardReference", jsii.get(self, "dashboardRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDashboardRef).__jsii_proxy_class__ = lambda : _IDashboardRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudtrail.IEventDataStoreRef")
class IEventDataStoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventDataStore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventDataStoreRef")
    def event_data_store_ref(self) -> "EventDataStoreReference":
        '''(experimental) A reference to a EventDataStore resource.

        :stability: experimental
        '''
        ...


class _IEventDataStoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventDataStore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudtrail.IEventDataStoreRef"

    @builtins.property
    @jsii.member(jsii_name="eventDataStoreRef")
    def event_data_store_ref(self) -> "EventDataStoreReference":
        '''(experimental) A reference to a EventDataStore resource.

        :stability: experimental
        '''
        return typing.cast("EventDataStoreReference", jsii.get(self, "eventDataStoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventDataStoreRef).__jsii_proxy_class__ = lambda : _IEventDataStoreRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudtrail.IResourcePolicyRef")
class IResourcePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        ...


class _IResourcePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudtrail.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudtrail.ITrailRef")
class ITrailRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Trail.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trailRef")
    def trail_ref(self) -> "TrailReference":
        '''(experimental) A reference to a Trail resource.

        :stability: experimental
        '''
        ...


class _ITrailRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Trail.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudtrail.ITrailRef"

    @builtins.property
    @jsii.member(jsii_name="trailRef")
    def trail_ref(self) -> "TrailReference":
        '''(experimental) A reference to a Trail resource.

        :stability: experimental
        '''
        return typing.cast("TrailReference", jsii.get(self, "trailRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrailRef).__jsii_proxy_class__ = lambda : _ITrailRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudtrail.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class ResourcePolicyReference:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''A reference to a ResourcePolicy resource.

        :param resource_arn: The ResourceArn of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudtrail as interfaces_cloudtrail
            
            resource_policy_reference = interfaces_cloudtrail.ResourcePolicyReference(
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6ea9fdfa2d0910c22924359c901c3896e7e2aaf13d6d7af06d5d809bb80f690)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceArn of the ResourcePolicy resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudtrail.TrailReference",
    jsii_struct_bases=[],
    name_mapping={"trail_arn": "trailArn", "trail_name": "trailName"},
)
class TrailReference:
    def __init__(self, *, trail_arn: builtins.str, trail_name: builtins.str) -> None:
        '''A reference to a Trail resource.

        :param trail_arn: The ARN of the Trail resource.
        :param trail_name: The TrailName of the Trail resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudtrail as interfaces_cloudtrail
            
            trail_reference = interfaces_cloudtrail.TrailReference(
                trail_arn="trailArn",
                trail_name="trailName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17ef5cd44b172d4230f3ac5aad3c0dc9b570706c99daec1f3da2bbce4d02d724)
            check_type(argname="argument trail_arn", value=trail_arn, expected_type=type_hints["trail_arn"])
            check_type(argname="argument trail_name", value=trail_name, expected_type=type_hints["trail_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trail_arn": trail_arn,
            "trail_name": trail_name,
        }

    @builtins.property
    def trail_arn(self) -> builtins.str:
        '''The ARN of the Trail resource.'''
        result = self._values.get("trail_arn")
        assert result is not None, "Required property 'trail_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trail_name(self) -> builtins.str:
        '''The TrailName of the Trail resource.'''
        result = self._values.get("trail_name")
        assert result is not None, "Required property 'trail_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrailReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ChannelReference",
    "DashboardReference",
    "EventDataStoreReference",
    "IChannelRef",
    "IDashboardRef",
    "IEventDataStoreRef",
    "IResourcePolicyRef",
    "ITrailRef",
    "ResourcePolicyReference",
    "TrailReference",
]

publication.publish()

def _typecheckingstub__6b1e4534590f5416c5abc69bf46a6e6f6977c7e439529c2cae4fd40303f444e5(
    *,
    channel_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__605da928544d77164ada0eea8dbdcc59414c1ab694eb78c7f32c3d9912778901(
    *,
    dashboard_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4579736f6ca2c03f650e12878b6ad5b99bec759b9a3ed1e253fe7cda8a48fe54(
    *,
    event_data_store_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6ea9fdfa2d0910c22924359c901c3896e7e2aaf13d6d7af06d5d809bb80f690(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17ef5cd44b172d4230f3ac5aad3c0dc9b570706c99daec1f3da2bbce4d02d724(
    *,
    trail_arn: builtins.str,
    trail_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IChannelRef, IDashboardRef, IEventDataStoreRef, IResourcePolicyRef, ITrailRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
