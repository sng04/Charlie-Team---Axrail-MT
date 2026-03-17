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
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.ChannelPlacementGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "channel_placement_group_arn": "channelPlacementGroupArn",
        "channel_placement_group_id": "channelPlacementGroupId",
        "cluster_id": "clusterId",
    },
)
class ChannelPlacementGroupReference:
    def __init__(
        self,
        *,
        channel_placement_group_arn: builtins.str,
        channel_placement_group_id: builtins.str,
        cluster_id: builtins.str,
    ) -> None:
        '''A reference to a ChannelPlacementGroup resource.

        :param channel_placement_group_arn: The ARN of the ChannelPlacementGroup resource.
        :param channel_placement_group_id: The Id of the ChannelPlacementGroup resource.
        :param cluster_id: The ClusterId of the ChannelPlacementGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            channel_placement_group_reference = interfaces_medialive.ChannelPlacementGroupReference(
                channel_placement_group_arn="channelPlacementGroupArn",
                channel_placement_group_id="channelPlacementGroupId",
                cluster_id="clusterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2594b5679b696601793eabfd9a92b876df7ce2e10561dab10dc2df738a901103)
            check_type(argname="argument channel_placement_group_arn", value=channel_placement_group_arn, expected_type=type_hints["channel_placement_group_arn"])
            check_type(argname="argument channel_placement_group_id", value=channel_placement_group_id, expected_type=type_hints["channel_placement_group_id"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_placement_group_arn": channel_placement_group_arn,
            "channel_placement_group_id": channel_placement_group_id,
            "cluster_id": cluster_id,
        }

    @builtins.property
    def channel_placement_group_arn(self) -> builtins.str:
        '''The ARN of the ChannelPlacementGroup resource.'''
        result = self._values.get("channel_placement_group_arn")
        assert result is not None, "Required property 'channel_placement_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_placement_group_id(self) -> builtins.str:
        '''The Id of the ChannelPlacementGroup resource.'''
        result = self._values.get("channel_placement_group_id")
        assert result is not None, "Required property 'channel_placement_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_id(self) -> builtins.str:
        '''The ClusterId of the ChannelPlacementGroup resource.'''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelPlacementGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.ChannelReference",
    jsii_struct_bases=[],
    name_mapping={"channel_arn": "channelArn", "channel_id": "channelId"},
)
class ChannelReference:
    def __init__(self, *, channel_arn: builtins.str, channel_id: builtins.str) -> None:
        '''A reference to a Channel resource.

        :param channel_arn: The ARN of the Channel resource.
        :param channel_id: The Id of the Channel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            channel_reference = interfaces_medialive.ChannelReference(
                channel_arn="channelArn",
                channel_id="channelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3424c9ee02b610e364190527124edc268cdd6c9efaa9da647a18f8aadb89b182)
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
            check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_arn": channel_arn,
            "channel_id": channel_id,
        }

    @builtins.property
    def channel_arn(self) -> builtins.str:
        '''The ARN of the Channel resource.'''
        result = self._values.get("channel_arn")
        assert result is not None, "Required property 'channel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_id(self) -> builtins.str:
        '''The Id of the Channel resource.'''
        result = self._values.get("channel_id")
        assert result is not None, "Required property 'channel_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.CloudWatchAlarmTemplateGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_watch_alarm_template_group_arn": "cloudWatchAlarmTemplateGroupArn",
        "identifier": "identifier",
    },
)
class CloudWatchAlarmTemplateGroupReference:
    def __init__(
        self,
        *,
        cloud_watch_alarm_template_group_arn: builtins.str,
        identifier: builtins.str,
    ) -> None:
        '''A reference to a CloudWatchAlarmTemplateGroup resource.

        :param cloud_watch_alarm_template_group_arn: The ARN of the CloudWatchAlarmTemplateGroup resource.
        :param identifier: The Identifier of the CloudWatchAlarmTemplateGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            cloud_watch_alarm_template_group_reference = interfaces_medialive.CloudWatchAlarmTemplateGroupReference(
                cloud_watch_alarm_template_group_arn="cloudWatchAlarmTemplateGroupArn",
                identifier="identifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2237a7176b9f7f8fece68e5e003c85f152fb677bf9a604533f5352200070295d)
            check_type(argname="argument cloud_watch_alarm_template_group_arn", value=cloud_watch_alarm_template_group_arn, expected_type=type_hints["cloud_watch_alarm_template_group_arn"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_watch_alarm_template_group_arn": cloud_watch_alarm_template_group_arn,
            "identifier": identifier,
        }

    @builtins.property
    def cloud_watch_alarm_template_group_arn(self) -> builtins.str:
        '''The ARN of the CloudWatchAlarmTemplateGroup resource.'''
        result = self._values.get("cloud_watch_alarm_template_group_arn")
        assert result is not None, "Required property 'cloud_watch_alarm_template_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''The Identifier of the CloudWatchAlarmTemplateGroup resource.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudWatchAlarmTemplateGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.CloudWatchAlarmTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "cloud_watch_alarm_template_arn": "cloudWatchAlarmTemplateArn",
        "identifier": "identifier",
    },
)
class CloudWatchAlarmTemplateReference:
    def __init__(
        self,
        *,
        cloud_watch_alarm_template_arn: builtins.str,
        identifier: builtins.str,
    ) -> None:
        '''A reference to a CloudWatchAlarmTemplate resource.

        :param cloud_watch_alarm_template_arn: The ARN of the CloudWatchAlarmTemplate resource.
        :param identifier: The Identifier of the CloudWatchAlarmTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            cloud_watch_alarm_template_reference = interfaces_medialive.CloudWatchAlarmTemplateReference(
                cloud_watch_alarm_template_arn="cloudWatchAlarmTemplateArn",
                identifier="identifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0e6e463bc22e2a0a7e51c0c5d7f822d7b6d34e1671b47ff9d1c0a484d8af701)
            check_type(argname="argument cloud_watch_alarm_template_arn", value=cloud_watch_alarm_template_arn, expected_type=type_hints["cloud_watch_alarm_template_arn"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_watch_alarm_template_arn": cloud_watch_alarm_template_arn,
            "identifier": identifier,
        }

    @builtins.property
    def cloud_watch_alarm_template_arn(self) -> builtins.str:
        '''The ARN of the CloudWatchAlarmTemplate resource.'''
        result = self._values.get("cloud_watch_alarm_template_arn")
        assert result is not None, "Required property 'cloud_watch_alarm_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''The Identifier of the CloudWatchAlarmTemplate resource.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudWatchAlarmTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.ClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn", "cluster_id": "clusterId"},
)
class ClusterReference:
    def __init__(self, *, cluster_arn: builtins.str, cluster_id: builtins.str) -> None:
        '''A reference to a Cluster resource.

        :param cluster_arn: The ARN of the Cluster resource.
        :param cluster_id: The Id of the Cluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            cluster_reference = interfaces_medialive.ClusterReference(
                cluster_arn="clusterArn",
                cluster_id="clusterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea04f54c56889a507377738279e129f40a6ec5128a64229bc7e18bc36df2bb0e)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
            "cluster_id": cluster_id,
        }

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The ARN of the Cluster resource.'''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_id(self) -> builtins.str:
        '''The Id of the Cluster resource.'''
        result = self._values.get("cluster_id")
        assert result is not None, "Required property 'cluster_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.EventBridgeRuleTemplateGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "event_bridge_rule_template_group_arn": "eventBridgeRuleTemplateGroupArn",
        "identifier": "identifier",
    },
)
class EventBridgeRuleTemplateGroupReference:
    def __init__(
        self,
        *,
        event_bridge_rule_template_group_arn: builtins.str,
        identifier: builtins.str,
    ) -> None:
        '''A reference to a EventBridgeRuleTemplateGroup resource.

        :param event_bridge_rule_template_group_arn: The ARN of the EventBridgeRuleTemplateGroup resource.
        :param identifier: The Identifier of the EventBridgeRuleTemplateGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            event_bridge_rule_template_group_reference = interfaces_medialive.EventBridgeRuleTemplateGroupReference(
                event_bridge_rule_template_group_arn="eventBridgeRuleTemplateGroupArn",
                identifier="identifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d44b8b3e7eb345036043cd9e7fcf1dd0d1b52371d7cdd71e6c635e44a0f1cdf)
            check_type(argname="argument event_bridge_rule_template_group_arn", value=event_bridge_rule_template_group_arn, expected_type=type_hints["event_bridge_rule_template_group_arn"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_bridge_rule_template_group_arn": event_bridge_rule_template_group_arn,
            "identifier": identifier,
        }

    @builtins.property
    def event_bridge_rule_template_group_arn(self) -> builtins.str:
        '''The ARN of the EventBridgeRuleTemplateGroup resource.'''
        result = self._values.get("event_bridge_rule_template_group_arn")
        assert result is not None, "Required property 'event_bridge_rule_template_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''The Identifier of the EventBridgeRuleTemplateGroup resource.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventBridgeRuleTemplateGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.EventBridgeRuleTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "event_bridge_rule_template_arn": "eventBridgeRuleTemplateArn",
        "identifier": "identifier",
    },
)
class EventBridgeRuleTemplateReference:
    def __init__(
        self,
        *,
        event_bridge_rule_template_arn: builtins.str,
        identifier: builtins.str,
    ) -> None:
        '''A reference to a EventBridgeRuleTemplate resource.

        :param event_bridge_rule_template_arn: The ARN of the EventBridgeRuleTemplate resource.
        :param identifier: The Identifier of the EventBridgeRuleTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            event_bridge_rule_template_reference = interfaces_medialive.EventBridgeRuleTemplateReference(
                event_bridge_rule_template_arn="eventBridgeRuleTemplateArn",
                identifier="identifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a411db26e5fd25aebb1257aec9f28a79a2215ef5c86d4a423fd6ce7007ae088a)
            check_type(argname="argument event_bridge_rule_template_arn", value=event_bridge_rule_template_arn, expected_type=type_hints["event_bridge_rule_template_arn"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_bridge_rule_template_arn": event_bridge_rule_template_arn,
            "identifier": identifier,
        }

    @builtins.property
    def event_bridge_rule_template_arn(self) -> builtins.str:
        '''The ARN of the EventBridgeRuleTemplate resource.'''
        result = self._values.get("event_bridge_rule_template_arn")
        assert result is not None, "Required property 'event_bridge_rule_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''The Identifier of the EventBridgeRuleTemplate resource.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventBridgeRuleTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.IChannelPlacementGroupRef"
)
class IChannelPlacementGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelPlacementGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelPlacementGroupRef")
    def channel_placement_group_ref(self) -> "ChannelPlacementGroupReference":
        '''(experimental) A reference to a ChannelPlacementGroup resource.

        :stability: experimental
        '''
        ...


class _IChannelPlacementGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelPlacementGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.IChannelPlacementGroupRef"

    @builtins.property
    @jsii.member(jsii_name="channelPlacementGroupRef")
    def channel_placement_group_ref(self) -> "ChannelPlacementGroupReference":
        '''(experimental) A reference to a ChannelPlacementGroup resource.

        :stability: experimental
        '''
        return typing.cast("ChannelPlacementGroupReference", jsii.get(self, "channelPlacementGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelPlacementGroupRef).__jsii_proxy_class__ = lambda : _IChannelPlacementGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_medialive.IChannelRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.IChannelRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.ICloudWatchAlarmTemplateGroupRef"
)
class ICloudWatchAlarmTemplateGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CloudWatchAlarmTemplateGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cloudWatchAlarmTemplateGroupRef")
    def cloud_watch_alarm_template_group_ref(
        self,
    ) -> "CloudWatchAlarmTemplateGroupReference":
        '''(experimental) A reference to a CloudWatchAlarmTemplateGroup resource.

        :stability: experimental
        '''
        ...


class _ICloudWatchAlarmTemplateGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CloudWatchAlarmTemplateGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.ICloudWatchAlarmTemplateGroupRef"

    @builtins.property
    @jsii.member(jsii_name="cloudWatchAlarmTemplateGroupRef")
    def cloud_watch_alarm_template_group_ref(
        self,
    ) -> "CloudWatchAlarmTemplateGroupReference":
        '''(experimental) A reference to a CloudWatchAlarmTemplateGroup resource.

        :stability: experimental
        '''
        return typing.cast("CloudWatchAlarmTemplateGroupReference", jsii.get(self, "cloudWatchAlarmTemplateGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICloudWatchAlarmTemplateGroupRef).__jsii_proxy_class__ = lambda : _ICloudWatchAlarmTemplateGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.ICloudWatchAlarmTemplateRef"
)
class ICloudWatchAlarmTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CloudWatchAlarmTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cloudWatchAlarmTemplateRef")
    def cloud_watch_alarm_template_ref(self) -> "CloudWatchAlarmTemplateReference":
        '''(experimental) A reference to a CloudWatchAlarmTemplate resource.

        :stability: experimental
        '''
        ...


class _ICloudWatchAlarmTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CloudWatchAlarmTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.ICloudWatchAlarmTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="cloudWatchAlarmTemplateRef")
    def cloud_watch_alarm_template_ref(self) -> "CloudWatchAlarmTemplateReference":
        '''(experimental) A reference to a CloudWatchAlarmTemplate resource.

        :stability: experimental
        '''
        return typing.cast("CloudWatchAlarmTemplateReference", jsii.get(self, "cloudWatchAlarmTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICloudWatchAlarmTemplateRef).__jsii_proxy_class__ = lambda : _ICloudWatchAlarmTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_medialive.IClusterRef")
class IClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Cluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        ...


class _IClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Cluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.IEventBridgeRuleTemplateGroupRef"
)
class IEventBridgeRuleTemplateGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventBridgeRuleTemplateGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventBridgeRuleTemplateGroupRef")
    def event_bridge_rule_template_group_ref(
        self,
    ) -> "EventBridgeRuleTemplateGroupReference":
        '''(experimental) A reference to a EventBridgeRuleTemplateGroup resource.

        :stability: experimental
        '''
        ...


class _IEventBridgeRuleTemplateGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventBridgeRuleTemplateGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.IEventBridgeRuleTemplateGroupRef"

    @builtins.property
    @jsii.member(jsii_name="eventBridgeRuleTemplateGroupRef")
    def event_bridge_rule_template_group_ref(
        self,
    ) -> "EventBridgeRuleTemplateGroupReference":
        '''(experimental) A reference to a EventBridgeRuleTemplateGroup resource.

        :stability: experimental
        '''
        return typing.cast("EventBridgeRuleTemplateGroupReference", jsii.get(self, "eventBridgeRuleTemplateGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventBridgeRuleTemplateGroupRef).__jsii_proxy_class__ = lambda : _IEventBridgeRuleTemplateGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.IEventBridgeRuleTemplateRef"
)
class IEventBridgeRuleTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventBridgeRuleTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventBridgeRuleTemplateRef")
    def event_bridge_rule_template_ref(self) -> "EventBridgeRuleTemplateReference":
        '''(experimental) A reference to a EventBridgeRuleTemplate resource.

        :stability: experimental
        '''
        ...


class _IEventBridgeRuleTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventBridgeRuleTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.IEventBridgeRuleTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="eventBridgeRuleTemplateRef")
    def event_bridge_rule_template_ref(self) -> "EventBridgeRuleTemplateReference":
        '''(experimental) A reference to a EventBridgeRuleTemplate resource.

        :stability: experimental
        '''
        return typing.cast("EventBridgeRuleTemplateReference", jsii.get(self, "eventBridgeRuleTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventBridgeRuleTemplateRef).__jsii_proxy_class__ = lambda : _IEventBridgeRuleTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_medialive.IInputRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.IInputRef"

    @builtins.property
    @jsii.member(jsii_name="inputRef")
    def input_ref(self) -> "InputReference":
        '''(experimental) A reference to a Input resource.

        :stability: experimental
        '''
        return typing.cast("InputReference", jsii.get(self, "inputRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInputRef).__jsii_proxy_class__ = lambda : _IInputRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.IInputSecurityGroupRef"
)
class IInputSecurityGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InputSecurityGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="inputSecurityGroupRef")
    def input_security_group_ref(self) -> "InputSecurityGroupReference":
        '''(experimental) A reference to a InputSecurityGroup resource.

        :stability: experimental
        '''
        ...


class _IInputSecurityGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InputSecurityGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.IInputSecurityGroupRef"

    @builtins.property
    @jsii.member(jsii_name="inputSecurityGroupRef")
    def input_security_group_ref(self) -> "InputSecurityGroupReference":
        '''(experimental) A reference to a InputSecurityGroup resource.

        :stability: experimental
        '''
        return typing.cast("InputSecurityGroupReference", jsii.get(self, "inputSecurityGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInputSecurityGroupRef).__jsii_proxy_class__ = lambda : _IInputSecurityGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_medialive.IMultiplexRef")
class IMultiplexRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Multiplex.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="multiplexRef")
    def multiplex_ref(self) -> "MultiplexReference":
        '''(experimental) A reference to a Multiplex resource.

        :stability: experimental
        '''
        ...


class _IMultiplexRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Multiplex.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.IMultiplexRef"

    @builtins.property
    @jsii.member(jsii_name="multiplexRef")
    def multiplex_ref(self) -> "MultiplexReference":
        '''(experimental) A reference to a Multiplex resource.

        :stability: experimental
        '''
        return typing.cast("MultiplexReference", jsii.get(self, "multiplexRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMultiplexRef).__jsii_proxy_class__ = lambda : _IMultiplexRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_medialive.IMultiplexprogramRef")
class IMultiplexprogramRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Multiplexprogram.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="multiplexprogramRef")
    def multiplexprogram_ref(self) -> "MultiplexprogramReference":
        '''(experimental) A reference to a Multiplexprogram resource.

        :stability: experimental
        '''
        ...


class _IMultiplexprogramRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Multiplexprogram.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.IMultiplexprogramRef"

    @builtins.property
    @jsii.member(jsii_name="multiplexprogramRef")
    def multiplexprogram_ref(self) -> "MultiplexprogramReference":
        '''(experimental) A reference to a Multiplexprogram resource.

        :stability: experimental
        '''
        return typing.cast("MultiplexprogramReference", jsii.get(self, "multiplexprogramRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMultiplexprogramRef).__jsii_proxy_class__ = lambda : _IMultiplexprogramRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_medialive.INetworkRef")
class INetworkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Network.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkRef")
    def network_ref(self) -> "NetworkReference":
        '''(experimental) A reference to a Network resource.

        :stability: experimental
        '''
        ...


class _INetworkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Network.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.INetworkRef"

    @builtins.property
    @jsii.member(jsii_name="networkRef")
    def network_ref(self) -> "NetworkReference":
        '''(experimental) A reference to a Network resource.

        :stability: experimental
        '''
        return typing.cast("NetworkReference", jsii.get(self, "networkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkRef).__jsii_proxy_class__ = lambda : _INetworkRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_medialive.ISdiSourceRef")
class ISdiSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SdiSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sdiSourceRef")
    def sdi_source_ref(self) -> "SdiSourceReference":
        '''(experimental) A reference to a SdiSource resource.

        :stability: experimental
        '''
        ...


class _ISdiSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SdiSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.ISdiSourceRef"

    @builtins.property
    @jsii.member(jsii_name="sdiSourceRef")
    def sdi_source_ref(self) -> "SdiSourceReference":
        '''(experimental) A reference to a SdiSource resource.

        :stability: experimental
        '''
        return typing.cast("SdiSourceReference", jsii.get(self, "sdiSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISdiSourceRef).__jsii_proxy_class__ = lambda : _ISdiSourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_medialive.ISignalMapRef")
class ISignalMapRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SignalMap.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="signalMapRef")
    def signal_map_ref(self) -> "SignalMapReference":
        '''(experimental) A reference to a SignalMap resource.

        :stability: experimental
        '''
        ...


class _ISignalMapRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SignalMap.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_medialive.ISignalMapRef"

    @builtins.property
    @jsii.member(jsii_name="signalMapRef")
    def signal_map_ref(self) -> "SignalMapReference":
        '''(experimental) A reference to a SignalMap resource.

        :stability: experimental
        '''
        return typing.cast("SignalMapReference", jsii.get(self, "signalMapRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISignalMapRef).__jsii_proxy_class__ = lambda : _ISignalMapRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.InputReference",
    jsii_struct_bases=[],
    name_mapping={"input_arn": "inputArn", "input_id": "inputId"},
)
class InputReference:
    def __init__(self, *, input_arn: builtins.str, input_id: builtins.str) -> None:
        '''A reference to a Input resource.

        :param input_arn: The ARN of the Input resource.
        :param input_id: The Id of the Input resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            input_reference = interfaces_medialive.InputReference(
                input_arn="inputArn",
                input_id="inputId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0420ad5d30bc8a7593b1aae5d5e3cfa6012530ba66b985625a2cfdefb9868319)
            check_type(argname="argument input_arn", value=input_arn, expected_type=type_hints["input_arn"])
            check_type(argname="argument input_id", value=input_id, expected_type=type_hints["input_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_arn": input_arn,
            "input_id": input_id,
        }

    @builtins.property
    def input_arn(self) -> builtins.str:
        '''The ARN of the Input resource.'''
        result = self._values.get("input_arn")
        assert result is not None, "Required property 'input_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_id(self) -> builtins.str:
        '''The Id of the Input resource.'''
        result = self._values.get("input_id")
        assert result is not None, "Required property 'input_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InputReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.InputSecurityGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "input_security_group_arn": "inputSecurityGroupArn",
        "input_security_group_id": "inputSecurityGroupId",
    },
)
class InputSecurityGroupReference:
    def __init__(
        self,
        *,
        input_security_group_arn: builtins.str,
        input_security_group_id: builtins.str,
    ) -> None:
        '''A reference to a InputSecurityGroup resource.

        :param input_security_group_arn: The ARN of the InputSecurityGroup resource.
        :param input_security_group_id: The Id of the InputSecurityGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            input_security_group_reference = interfaces_medialive.InputSecurityGroupReference(
                input_security_group_arn="inputSecurityGroupArn",
                input_security_group_id="inputSecurityGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfbe88aef6243ace17125340ec34385482c350fc3764bb70d213586419bb55fd)
            check_type(argname="argument input_security_group_arn", value=input_security_group_arn, expected_type=type_hints["input_security_group_arn"])
            check_type(argname="argument input_security_group_id", value=input_security_group_id, expected_type=type_hints["input_security_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "input_security_group_arn": input_security_group_arn,
            "input_security_group_id": input_security_group_id,
        }

    @builtins.property
    def input_security_group_arn(self) -> builtins.str:
        '''The ARN of the InputSecurityGroup resource.'''
        result = self._values.get("input_security_group_arn")
        assert result is not None, "Required property 'input_security_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def input_security_group_id(self) -> builtins.str:
        '''The Id of the InputSecurityGroup resource.'''
        result = self._values.get("input_security_group_id")
        assert result is not None, "Required property 'input_security_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InputSecurityGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.MultiplexReference",
    jsii_struct_bases=[],
    name_mapping={"multiplex_arn": "multiplexArn", "multiplex_id": "multiplexId"},
)
class MultiplexReference:
    def __init__(
        self,
        *,
        multiplex_arn: builtins.str,
        multiplex_id: builtins.str,
    ) -> None:
        '''A reference to a Multiplex resource.

        :param multiplex_arn: The ARN of the Multiplex resource.
        :param multiplex_id: The Id of the Multiplex resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            multiplex_reference = interfaces_medialive.MultiplexReference(
                multiplex_arn="multiplexArn",
                multiplex_id="multiplexId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f2c089e4eff55785f2b294bd33efb3d92e81ea7d1b30f5308cc5d4a8950524d)
            check_type(argname="argument multiplex_arn", value=multiplex_arn, expected_type=type_hints["multiplex_arn"])
            check_type(argname="argument multiplex_id", value=multiplex_id, expected_type=type_hints["multiplex_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "multiplex_arn": multiplex_arn,
            "multiplex_id": multiplex_id,
        }

    @builtins.property
    def multiplex_arn(self) -> builtins.str:
        '''The ARN of the Multiplex resource.'''
        result = self._values.get("multiplex_arn")
        assert result is not None, "Required property 'multiplex_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def multiplex_id(self) -> builtins.str:
        '''The Id of the Multiplex resource.'''
        result = self._values.get("multiplex_id")
        assert result is not None, "Required property 'multiplex_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultiplexReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.MultiplexprogramReference",
    jsii_struct_bases=[],
    name_mapping={"multiplex_id": "multiplexId", "program_name": "programName"},
)
class MultiplexprogramReference:
    def __init__(
        self,
        *,
        multiplex_id: builtins.str,
        program_name: builtins.str,
    ) -> None:
        '''A reference to a Multiplexprogram resource.

        :param multiplex_id: The MultiplexId of the Multiplexprogram resource.
        :param program_name: The ProgramName of the Multiplexprogram resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            multiplexprogram_reference = interfaces_medialive.MultiplexprogramReference(
                multiplex_id="multiplexId",
                program_name="programName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcaa0c6f668b17a435397d563e8885f40fe151588d065268e06d594f2ee1c18f)
            check_type(argname="argument multiplex_id", value=multiplex_id, expected_type=type_hints["multiplex_id"])
            check_type(argname="argument program_name", value=program_name, expected_type=type_hints["program_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "multiplex_id": multiplex_id,
            "program_name": program_name,
        }

    @builtins.property
    def multiplex_id(self) -> builtins.str:
        '''The MultiplexId of the Multiplexprogram resource.'''
        result = self._values.get("multiplex_id")
        assert result is not None, "Required property 'multiplex_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def program_name(self) -> builtins.str:
        '''The ProgramName of the Multiplexprogram resource.'''
        result = self._values.get("program_name")
        assert result is not None, "Required property 'program_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultiplexprogramReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.NetworkReference",
    jsii_struct_bases=[],
    name_mapping={"network_arn": "networkArn", "network_id": "networkId"},
)
class NetworkReference:
    def __init__(self, *, network_arn: builtins.str, network_id: builtins.str) -> None:
        '''A reference to a Network resource.

        :param network_arn: The ARN of the Network resource.
        :param network_id: The Id of the Network resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            network_reference = interfaces_medialive.NetworkReference(
                network_arn="networkArn",
                network_id="networkId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf8824f54434f31b2fdbb5c0467b07d8f1dab750d26e38b7b446af20b711745)
            check_type(argname="argument network_arn", value=network_arn, expected_type=type_hints["network_arn"])
            check_type(argname="argument network_id", value=network_id, expected_type=type_hints["network_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_arn": network_arn,
            "network_id": network_id,
        }

    @builtins.property
    def network_arn(self) -> builtins.str:
        '''The ARN of the Network resource.'''
        result = self._values.get("network_arn")
        assert result is not None, "Required property 'network_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_id(self) -> builtins.str:
        '''The Id of the Network resource.'''
        result = self._values.get("network_id")
        assert result is not None, "Required property 'network_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.SdiSourceReference",
    jsii_struct_bases=[],
    name_mapping={"sdi_source_arn": "sdiSourceArn", "sdi_source_id": "sdiSourceId"},
)
class SdiSourceReference:
    def __init__(
        self,
        *,
        sdi_source_arn: builtins.str,
        sdi_source_id: builtins.str,
    ) -> None:
        '''A reference to a SdiSource resource.

        :param sdi_source_arn: The ARN of the SdiSource resource.
        :param sdi_source_id: The Id of the SdiSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            sdi_source_reference = interfaces_medialive.SdiSourceReference(
                sdi_source_arn="sdiSourceArn",
                sdi_source_id="sdiSourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f600af46c39ab21e65823f674665253250ef9cc92b937fb0aaf7db85de0951f8)
            check_type(argname="argument sdi_source_arn", value=sdi_source_arn, expected_type=type_hints["sdi_source_arn"])
            check_type(argname="argument sdi_source_id", value=sdi_source_id, expected_type=type_hints["sdi_source_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sdi_source_arn": sdi_source_arn,
            "sdi_source_id": sdi_source_id,
        }

    @builtins.property
    def sdi_source_arn(self) -> builtins.str:
        '''The ARN of the SdiSource resource.'''
        result = self._values.get("sdi_source_arn")
        assert result is not None, "Required property 'sdi_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sdi_source_id(self) -> builtins.str:
        '''The Id of the SdiSource resource.'''
        result = self._values.get("sdi_source_id")
        assert result is not None, "Required property 'sdi_source_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SdiSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_medialive.SignalMapReference",
    jsii_struct_bases=[],
    name_mapping={"identifier": "identifier", "signal_map_arn": "signalMapArn"},
)
class SignalMapReference:
    def __init__(
        self,
        *,
        identifier: builtins.str,
        signal_map_arn: builtins.str,
    ) -> None:
        '''A reference to a SignalMap resource.

        :param identifier: The Identifier of the SignalMap resource.
        :param signal_map_arn: The ARN of the SignalMap resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_medialive as interfaces_medialive
            
            signal_map_reference = interfaces_medialive.SignalMapReference(
                identifier="identifier",
                signal_map_arn="signalMapArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99c643daeb09c2839c551125ac2e17246f1f3168fd4c3d255cb37734413af90f)
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument signal_map_arn", value=signal_map_arn, expected_type=type_hints["signal_map_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identifier": identifier,
            "signal_map_arn": signal_map_arn,
        }

    @builtins.property
    def identifier(self) -> builtins.str:
        '''The Identifier of the SignalMap resource.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signal_map_arn(self) -> builtins.str:
        '''The ARN of the SignalMap resource.'''
        result = self._values.get("signal_map_arn")
        assert result is not None, "Required property 'signal_map_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SignalMapReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ChannelPlacementGroupReference",
    "ChannelReference",
    "CloudWatchAlarmTemplateGroupReference",
    "CloudWatchAlarmTemplateReference",
    "ClusterReference",
    "EventBridgeRuleTemplateGroupReference",
    "EventBridgeRuleTemplateReference",
    "IChannelPlacementGroupRef",
    "IChannelRef",
    "ICloudWatchAlarmTemplateGroupRef",
    "ICloudWatchAlarmTemplateRef",
    "IClusterRef",
    "IEventBridgeRuleTemplateGroupRef",
    "IEventBridgeRuleTemplateRef",
    "IInputRef",
    "IInputSecurityGroupRef",
    "IMultiplexRef",
    "IMultiplexprogramRef",
    "INetworkRef",
    "ISdiSourceRef",
    "ISignalMapRef",
    "InputReference",
    "InputSecurityGroupReference",
    "MultiplexReference",
    "MultiplexprogramReference",
    "NetworkReference",
    "SdiSourceReference",
    "SignalMapReference",
]

publication.publish()

def _typecheckingstub__2594b5679b696601793eabfd9a92b876df7ce2e10561dab10dc2df738a901103(
    *,
    channel_placement_group_arn: builtins.str,
    channel_placement_group_id: builtins.str,
    cluster_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3424c9ee02b610e364190527124edc268cdd6c9efaa9da647a18f8aadb89b182(
    *,
    channel_arn: builtins.str,
    channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2237a7176b9f7f8fece68e5e003c85f152fb677bf9a604533f5352200070295d(
    *,
    cloud_watch_alarm_template_group_arn: builtins.str,
    identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0e6e463bc22e2a0a7e51c0c5d7f822d7b6d34e1671b47ff9d1c0a484d8af701(
    *,
    cloud_watch_alarm_template_arn: builtins.str,
    identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea04f54c56889a507377738279e129f40a6ec5128a64229bc7e18bc36df2bb0e(
    *,
    cluster_arn: builtins.str,
    cluster_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d44b8b3e7eb345036043cd9e7fcf1dd0d1b52371d7cdd71e6c635e44a0f1cdf(
    *,
    event_bridge_rule_template_group_arn: builtins.str,
    identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a411db26e5fd25aebb1257aec9f28a79a2215ef5c86d4a423fd6ce7007ae088a(
    *,
    event_bridge_rule_template_arn: builtins.str,
    identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0420ad5d30bc8a7593b1aae5d5e3cfa6012530ba66b985625a2cfdefb9868319(
    *,
    input_arn: builtins.str,
    input_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfbe88aef6243ace17125340ec34385482c350fc3764bb70d213586419bb55fd(
    *,
    input_security_group_arn: builtins.str,
    input_security_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f2c089e4eff55785f2b294bd33efb3d92e81ea7d1b30f5308cc5d4a8950524d(
    *,
    multiplex_arn: builtins.str,
    multiplex_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcaa0c6f668b17a435397d563e8885f40fe151588d065268e06d594f2ee1c18f(
    *,
    multiplex_id: builtins.str,
    program_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf8824f54434f31b2fdbb5c0467b07d8f1dab750d26e38b7b446af20b711745(
    *,
    network_arn: builtins.str,
    network_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f600af46c39ab21e65823f674665253250ef9cc92b937fb0aaf7db85de0951f8(
    *,
    sdi_source_arn: builtins.str,
    sdi_source_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99c643daeb09c2839c551125ac2e17246f1f3168fd4c3d255cb37734413af90f(
    *,
    identifier: builtins.str,
    signal_map_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IChannelPlacementGroupRef, IChannelRef, ICloudWatchAlarmTemplateGroupRef, ICloudWatchAlarmTemplateRef, IClusterRef, IEventBridgeRuleTemplateGroupRef, IEventBridgeRuleTemplateRef, IInputRef, IInputSecurityGroupRef, IMultiplexRef, IMultiplexprogramRef, INetworkRef, ISdiSourceRef, ISignalMapRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
