r'''
# AWS::SMSVOICE Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_smsvoice as smsvoice
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SMSVOICE construct libraries](https://constructs.dev/search?q=smsvoice)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SMSVOICE resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SMSVOICE.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SMSVOICE](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SMSVOICE.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
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

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_smsvoice import (
    ConfigurationSetReference as _ConfigurationSetReference_540b1fe3,
    IConfigurationSetRef as _IConfigurationSetRef_be3ec7c2,
    IOptOutListRef as _IOptOutListRef_1d44f5f8,
    IPhoneNumberRef as _IPhoneNumberRef_7c6c9ced,
    IPoolRef as _IPoolRef_897848fa,
    IProtectConfigurationRef as _IProtectConfigurationRef_e1ab5693,
    IResourcePolicyRef as _IResourcePolicyRef_99a2534c,
    ISenderIdRef as _ISenderIdRef_c6023099,
    OptOutListReference as _OptOutListReference_e0a13902,
    PhoneNumberReference as _PhoneNumberReference_c338f1b9,
    PoolReference as _PoolReference_a27a62c2,
    ProtectConfigurationReference as _ProtectConfigurationReference_c0c38d05,
    ResourcePolicyReference as _ResourcePolicyReference_b377e19e,
    SenderIdReference as _SenderIdReference_10c27954,
)


@jsii.implements(_IInspectable_c2943556, _IConfigurationSetRef_be3ec7c2, _ITaggableV2_4e6798f8)
class CfnConfigurationSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnConfigurationSet",
):
    '''Creates a new configuration set.

    After you create the configuration set, you can add one or more event destinations to it.

    A configuration set is a set of rules that you apply to the SMS and voice messages that you send.

    When you send a message, you can optionally specify a single configuration set.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-configurationset.html
    :cloudformationResource: AWS::SMSVOICE::ConfigurationSet
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_smsvoice as smsvoice
        
        cfn_configuration_set = smsvoice.CfnConfigurationSet(self, "MyCfnConfigurationSet",
            configuration_set_name="configurationSetName",
            default_sender_id="defaultSenderId",
            event_destinations=[smsvoice.CfnConfigurationSet.EventDestinationProperty(
                enabled=False,
                event_destination_name="eventDestinationName",
                matching_event_types=["matchingEventTypes"],
        
                # the properties below are optional
                cloud_watch_logs_destination=smsvoice.CfnConfigurationSet.CloudWatchLogsDestinationProperty(
                    iam_role_arn="iamRoleArn",
                    log_group_arn="logGroupArn"
                ),
                kinesis_firehose_destination=smsvoice.CfnConfigurationSet.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                ),
                sns_destination=smsvoice.CfnConfigurationSet.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            )],
            message_feedback_enabled=False,
            protect_configuration_id="protectConfigurationId",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        configuration_set_name: typing.Optional[builtins.str] = None,
        default_sender_id: typing.Optional[builtins.str] = None,
        event_destinations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfigurationSet.EventDestinationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        message_feedback_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        protect_configuration_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SMSVOICE::ConfigurationSet``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration_set_name: The name of the ConfigurationSet.
        :param default_sender_id: The default sender ID used by the ConfigurationSet.
        :param event_destinations: An array of EventDestination objects that describe any events to log and where to log them.
        :param message_feedback_enabled: Set to true to enable feedback for the message.
        :param protect_configuration_id: The unique identifier for the protect configuration.
        :param tags: An array of key and value pair tags that's associated with the new configuration set.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40dfc64df6dc2c0a72f2a15a90352d0f45df52177e2673d853e93c45f6ff9bfe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationSetProps(
            configuration_set_name=configuration_set_name,
            default_sender_id=default_sender_id,
            event_destinations=event_destinations,
            message_feedback_enabled=message_feedback_enabled,
            protect_configuration_id=protect_configuration_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForConfigurationSet")
    @builtins.classmethod
    def arn_for_configuration_set(
        cls,
        resource: "_IConfigurationSetRef_be3ec7c2",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04de3b646c1d1d3fc07c65ce19d9174446aaf197c899c5e2b9702589553a45d7)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForConfigurationSet", [resource]))

    @jsii.member(jsii_name="fromConfigurationSetArn")
    @builtins.classmethod
    def from_configuration_set_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IConfigurationSetRef_be3ec7c2":
        '''Creates a new IConfigurationSetRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd09a8e0a95f96b6bf6ade58869d230ef8c16df306e2dba74636ef174182860e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IConfigurationSetRef_be3ec7c2", jsii.sinvoke(cls, "fromConfigurationSetArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromConfigurationSetName")
    @builtins.classmethod
    def from_configuration_set_name(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        configuration_set_name: builtins.str,
    ) -> "_IConfigurationSetRef_be3ec7c2":
        '''Creates a new IConfigurationSetRef from a configurationSetName.

        :param scope: -
        :param id: -
        :param configuration_set_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2808c7d63f3da460cc51d6d5193de4fa41ad6dd91676f0cdf055c67e7f58e61)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
        return typing.cast("_IConfigurationSetRef_be3ec7c2", jsii.sinvoke(cls, "fromConfigurationSetName", [scope, id, configuration_set_name]))

    @jsii.member(jsii_name="isCfnConfigurationSet")
    @builtins.classmethod
    def is_cfn_configuration_set(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnConfigurationSet.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94624c95308275f4e88fd0bcfb044adfc2050601e54cefb8f850aea329e02d30)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnConfigurationSet", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b8914b55c8c9175cb9d85ebbc19bd9b2ce8ee1fa9391da5cfe4b1d45d0285f4)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b90e7a4776972d39f70067111684f2db6512204052e5e5368d9053b54bac6e9e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the ConfigurationSet.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="configurationSetRef")
    def configuration_set_ref(self) -> "_ConfigurationSetReference_540b1fe3":
        '''A reference to a ConfigurationSet resource.'''
        return typing.cast("_ConfigurationSetReference_540b1fe3", jsii.get(self, "configurationSetRef"))

    @builtins.property
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> typing.Optional[builtins.str]:
        '''The name of the ConfigurationSet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationSetName"))

    @configuration_set_name.setter
    def configuration_set_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9544d5ead16000fe8542a97ab4304b9e73471d41cf77a7fcc7c28d0bf4588e3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationSetName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultSenderId")
    def default_sender_id(self) -> typing.Optional[builtins.str]:
        '''The default sender ID used by the ConfigurationSet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultSenderId"))

    @default_sender_id.setter
    def default_sender_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186ea9a50af63ea8848866e4b7a25b25d580298e214617e976cdc49fd323660a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultSenderId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eventDestinations")
    def event_destinations(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.EventDestinationProperty"]]]]:
        '''An array of EventDestination objects that describe any events to log and where to log them.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.EventDestinationProperty"]]]], jsii.get(self, "eventDestinations"))

    @event_destinations.setter
    def event_destinations(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.EventDestinationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2057faf5fb512456c4bc44fe35430b7693158df99536b671cd30ec082b564004)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDestinations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="messageFeedbackEnabled")
    def message_feedback_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Set to true to enable feedback for the message.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "messageFeedbackEnabled"))

    @message_feedback_enabled.setter
    def message_feedback_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1700a269dd97f8f5889c42356bc0625812eb38d345cd6ab0a47dc65604b9ef5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageFeedbackEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protectConfigurationId")
    def protect_configuration_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for the protect configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protectConfigurationId"))

    @protect_configuration_id.setter
    def protect_configuration_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33df2949530ac82bfead10df97e9fd3007e7ef3723aea6ac4426bd0d08d7c469)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectConfigurationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key and value pair tags that's associated with the new configuration set.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aeb00cd60ff4e73014460e95c4362f82c1d73f0b45e4e453a05465afef34da6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnConfigurationSet.CloudWatchLogsDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"iam_role_arn": "iamRoleArn", "log_group_arn": "logGroupArn"},
    )
    class CloudWatchLogsDestinationProperty:
        def __init__(
            self,
            *,
            iam_role_arn: builtins.str,
            log_group_arn: builtins.str,
        ) -> None:
            '''Contains the destination configuration to use when publishing message sending events.

            :param iam_role_arn: The Amazon Resource Name (ARN) of an AWS Identity and Access Management role that is able to write event data to an Amazon CloudWatch destination.
            :param log_group_arn: The name of the Amazon CloudWatch log group that you want to record events in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-cloudwatchlogsdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                cloud_watch_logs_destination_property = smsvoice.CfnConfigurationSet.CloudWatchLogsDestinationProperty(
                    iam_role_arn="iamRoleArn",
                    log_group_arn="logGroupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__24be119a3ef65de30f1eb147ba1a3eac5f2a81fdd8f8285d98a680dc254f34e1)
                check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "iam_role_arn": iam_role_arn,
                "log_group_arn": log_group_arn,
            }

        @builtins.property
        def iam_role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of an AWS Identity and Access Management role that is able to write event data to an Amazon CloudWatch destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-cloudwatchlogsdestination.html#cfn-smsvoice-configurationset-cloudwatchlogsdestination-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            assert result is not None, "Required property 'iam_role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_group_arn(self) -> builtins.str:
            '''The name of the Amazon CloudWatch log group that you want to record events in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-cloudwatchlogsdestination.html#cfn-smsvoice-configurationset-cloudwatchlogsdestination-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            assert result is not None, "Required property 'log_group_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnConfigurationSet.EventDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "event_destination_name": "eventDestinationName",
            "matching_event_types": "matchingEventTypes",
            "cloud_watch_logs_destination": "cloudWatchLogsDestination",
            "kinesis_firehose_destination": "kinesisFirehoseDestination",
            "sns_destination": "snsDestination",
        },
    )
    class EventDestinationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, "_IResolvable_da3f097b"],
            event_destination_name: builtins.str,
            matching_event_types: typing.Sequence[builtins.str],
            cloud_watch_logs_destination: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfigurationSet.CloudWatchLogsDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_firehose_destination: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfigurationSet.KinesisFirehoseDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sns_destination: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfigurationSet.SnsDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about an event destination.

            Event destinations are associated with configuration sets, which enable you to publish message sending events to CloudWatch, Firehose, or Amazon SNS.

            :param enabled: When set to true events will be logged.
            :param event_destination_name: The name of the EventDestination.
            :param matching_event_types: An array of event types that determine which events to log. .. epigraph:: The ``TEXT_SENT`` event type is not supported.
            :param cloud_watch_logs_destination: An object that contains information about an event destination that sends logging events to Amazon CloudWatch logs.
            :param kinesis_firehose_destination: An object that contains information about an event destination for logging to Amazon Data Firehose.
            :param sns_destination: An object that contains information about an event destination that sends logging events to Amazon SNS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-eventdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                event_destination_property = smsvoice.CfnConfigurationSet.EventDestinationProperty(
                    enabled=False,
                    event_destination_name="eventDestinationName",
                    matching_event_types=["matchingEventTypes"],
                
                    # the properties below are optional
                    cloud_watch_logs_destination=smsvoice.CfnConfigurationSet.CloudWatchLogsDestinationProperty(
                        iam_role_arn="iamRoleArn",
                        log_group_arn="logGroupArn"
                    ),
                    kinesis_firehose_destination=smsvoice.CfnConfigurationSet.KinesisFirehoseDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn",
                        iam_role_arn="iamRoleArn"
                    ),
                    sns_destination=smsvoice.CfnConfigurationSet.SnsDestinationProperty(
                        topic_arn="topicArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__136edfd45f7d2c0b5dbe4db8977656e8be370d61eec90532e5a6d3d075f0d814)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument event_destination_name", value=event_destination_name, expected_type=type_hints["event_destination_name"])
                check_type(argname="argument matching_event_types", value=matching_event_types, expected_type=type_hints["matching_event_types"])
                check_type(argname="argument cloud_watch_logs_destination", value=cloud_watch_logs_destination, expected_type=type_hints["cloud_watch_logs_destination"])
                check_type(argname="argument kinesis_firehose_destination", value=kinesis_firehose_destination, expected_type=type_hints["kinesis_firehose_destination"])
                check_type(argname="argument sns_destination", value=sns_destination, expected_type=type_hints["sns_destination"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
                "event_destination_name": event_destination_name,
                "matching_event_types": matching_event_types,
            }
            if cloud_watch_logs_destination is not None:
                self._values["cloud_watch_logs_destination"] = cloud_watch_logs_destination
            if kinesis_firehose_destination is not None:
                self._values["kinesis_firehose_destination"] = kinesis_firehose_destination
            if sns_destination is not None:
                self._values["sns_destination"] = sns_destination

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, "_IResolvable_da3f097b"]:
            '''When set to true events will be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-eventdestination.html#cfn-smsvoice-configurationset-eventdestination-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, "_IResolvable_da3f097b"], result)

        @builtins.property
        def event_destination_name(self) -> builtins.str:
            '''The name of the EventDestination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-eventdestination.html#cfn-smsvoice-configurationset-eventdestination-eventdestinationname
            '''
            result = self._values.get("event_destination_name")
            assert result is not None, "Required property 'event_destination_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def matching_event_types(self) -> typing.List[builtins.str]:
            '''An array of event types that determine which events to log.

            .. epigraph::

               The ``TEXT_SENT`` event type is not supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-eventdestination.html#cfn-smsvoice-configurationset-eventdestination-matchingeventtypes
            '''
            result = self._values.get("matching_event_types")
            assert result is not None, "Required property 'matching_event_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def cloud_watch_logs_destination(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.CloudWatchLogsDestinationProperty"]]:
            '''An object that contains information about an event destination that sends logging events to Amazon CloudWatch logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-eventdestination.html#cfn-smsvoice-configurationset-eventdestination-cloudwatchlogsdestination
            '''
            result = self._values.get("cloud_watch_logs_destination")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.CloudWatchLogsDestinationProperty"]], result)

        @builtins.property
        def kinesis_firehose_destination(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.KinesisFirehoseDestinationProperty"]]:
            '''An object that contains information about an event destination for logging to Amazon Data Firehose.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-eventdestination.html#cfn-smsvoice-configurationset-eventdestination-kinesisfirehosedestination
            '''
            result = self._values.get("kinesis_firehose_destination")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.KinesisFirehoseDestinationProperty"]], result)

        @builtins.property
        def sns_destination(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.SnsDestinationProperty"]]:
            '''An object that contains information about an event destination that sends logging events to Amazon SNS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-eventdestination.html#cfn-smsvoice-configurationset-eventdestination-snsdestination
            '''
            result = self._values.get("sns_destination")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.SnsDestinationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnConfigurationSet.KinesisFirehoseDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_arn": "deliveryStreamArn",
            "iam_role_arn": "iamRoleArn",
        },
    )
    class KinesisFirehoseDestinationProperty:
        def __init__(
            self,
            *,
            delivery_stream_arn: builtins.str,
            iam_role_arn: builtins.str,
        ) -> None:
            '''Contains the delivery stream Amazon Resource Name (ARN), and the ARN of the AWS Identity and Access Management (IAM) role associated with a Firehose event destination.

            Event destinations, such as Firehose, are associated with configuration sets, which enable you to publish message sending events.

            :param delivery_stream_arn: The Amazon Resource Name (ARN) of the delivery stream.
            :param iam_role_arn: The ARN of an AWS Identity and Access Management role that is able to write event data to an Amazon Data Firehose destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-kinesisfirehosedestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                kinesis_firehose_destination_property = smsvoice.CfnConfigurationSet.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__58b63fc19b4a1791f46cfa02c2314f7bd36e3c4e54eceb6eb28919afd11059d7)
                check_type(argname="argument delivery_stream_arn", value=delivery_stream_arn, expected_type=type_hints["delivery_stream_arn"])
                check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delivery_stream_arn": delivery_stream_arn,
                "iam_role_arn": iam_role_arn,
            }

        @builtins.property
        def delivery_stream_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the delivery stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-kinesisfirehosedestination.html#cfn-smsvoice-configurationset-kinesisfirehosedestination-deliverystreamarn
            '''
            result = self._values.get("delivery_stream_arn")
            assert result is not None, "Required property 'delivery_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iam_role_arn(self) -> builtins.str:
            '''The ARN of an AWS Identity and Access Management role that is able to write event data to an Amazon Data Firehose destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-kinesisfirehosedestination.html#cfn-smsvoice-configurationset-kinesisfirehosedestination-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            assert result is not None, "Required property 'iam_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnConfigurationSet.SnsDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class SnsDestinationProperty:
        def __init__(self, *, topic_arn: builtins.str) -> None:
            '''An object that defines an Amazon SNS destination for events.

            You can use Amazon SNS to send notification when certain events occur.

            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-snsdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                sns_destination_property = smsvoice.CfnConfigurationSet.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e91819987879ee4dec183c370f8f16a53dffc5fa977336312072fb1db406fdaa)
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topic_arn": topic_arn,
            }

        @builtins.property
        def topic_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic that you want to publish events to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-configurationset-snsdestination.html#cfn-smsvoice-configurationset-snsdestination-topicarn
            '''
            result = self._values.get("topic_arn")
            assert result is not None, "Required property 'topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnConfigurationSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_name": "configurationSetName",
        "default_sender_id": "defaultSenderId",
        "event_destinations": "eventDestinations",
        "message_feedback_enabled": "messageFeedbackEnabled",
        "protect_configuration_id": "protectConfigurationId",
        "tags": "tags",
    },
)
class CfnConfigurationSetProps:
    def __init__(
        self,
        *,
        configuration_set_name: typing.Optional[builtins.str] = None,
        default_sender_id: typing.Optional[builtins.str] = None,
        event_destinations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnConfigurationSet.EventDestinationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        message_feedback_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        protect_configuration_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationSet``.

        :param configuration_set_name: The name of the ConfigurationSet.
        :param default_sender_id: The default sender ID used by the ConfigurationSet.
        :param event_destinations: An array of EventDestination objects that describe any events to log and where to log them.
        :param message_feedback_enabled: Set to true to enable feedback for the message.
        :param protect_configuration_id: The unique identifier for the protect configuration.
        :param tags: An array of key and value pair tags that's associated with the new configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-configurationset.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_smsvoice as smsvoice
            
            cfn_configuration_set_props = smsvoice.CfnConfigurationSetProps(
                configuration_set_name="configurationSetName",
                default_sender_id="defaultSenderId",
                event_destinations=[smsvoice.CfnConfigurationSet.EventDestinationProperty(
                    enabled=False,
                    event_destination_name="eventDestinationName",
                    matching_event_types=["matchingEventTypes"],
            
                    # the properties below are optional
                    cloud_watch_logs_destination=smsvoice.CfnConfigurationSet.CloudWatchLogsDestinationProperty(
                        iam_role_arn="iamRoleArn",
                        log_group_arn="logGroupArn"
                    ),
                    kinesis_firehose_destination=smsvoice.CfnConfigurationSet.KinesisFirehoseDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn",
                        iam_role_arn="iamRoleArn"
                    ),
                    sns_destination=smsvoice.CfnConfigurationSet.SnsDestinationProperty(
                        topic_arn="topicArn"
                    )
                )],
                message_feedback_enabled=False,
                protect_configuration_id="protectConfigurationId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__259d6b5c44c463276b6d9a529504479acbd49524ef7bd8a0d1d913ca2d1a58a3)
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
            check_type(argname="argument default_sender_id", value=default_sender_id, expected_type=type_hints["default_sender_id"])
            check_type(argname="argument event_destinations", value=event_destinations, expected_type=type_hints["event_destinations"])
            check_type(argname="argument message_feedback_enabled", value=message_feedback_enabled, expected_type=type_hints["message_feedback_enabled"])
            check_type(argname="argument protect_configuration_id", value=protect_configuration_id, expected_type=type_hints["protect_configuration_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if configuration_set_name is not None:
            self._values["configuration_set_name"] = configuration_set_name
        if default_sender_id is not None:
            self._values["default_sender_id"] = default_sender_id
        if event_destinations is not None:
            self._values["event_destinations"] = event_destinations
        if message_feedback_enabled is not None:
            self._values["message_feedback_enabled"] = message_feedback_enabled
        if protect_configuration_id is not None:
            self._values["protect_configuration_id"] = protect_configuration_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configuration_set_name(self) -> typing.Optional[builtins.str]:
        '''The name of the ConfigurationSet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-configurationset.html#cfn-smsvoice-configurationset-configurationsetname
        '''
        result = self._values.get("configuration_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_sender_id(self) -> typing.Optional[builtins.str]:
        '''The default sender ID used by the ConfigurationSet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-configurationset.html#cfn-smsvoice-configurationset-defaultsenderid
        '''
        result = self._values.get("default_sender_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def event_destinations(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.EventDestinationProperty"]]]]:
        '''An array of EventDestination objects that describe any events to log and where to log them.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-configurationset.html#cfn-smsvoice-configurationset-eventdestinations
        '''
        result = self._values.get("event_destinations")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnConfigurationSet.EventDestinationProperty"]]]], result)

    @builtins.property
    def message_feedback_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Set to true to enable feedback for the message.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-configurationset.html#cfn-smsvoice-configurationset-messagefeedbackenabled
        '''
        result = self._values.get("message_feedback_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def protect_configuration_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for the protect configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-configurationset.html#cfn-smsvoice-configurationset-protectconfigurationid
        '''
        result = self._values.get("protect_configuration_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key and value pair tags that's associated with the new configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-configurationset.html#cfn-smsvoice-configurationset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IOptOutListRef_1d44f5f8, _ITaggableV2_4e6798f8)
class CfnOptOutList(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnOptOutList",
):
    '''Creates a new opt-out list.

    If the opt-out list name already exists, an error is returned.

    An opt-out list is a list of phone numbers that are opted out, meaning you can't send SMS or voice messages to them. If end user replies with the keyword "STOP," an entry for the phone number is added to the opt-out list. In addition to STOP, your recipients can use any supported opt-out keyword, such as CANCEL or OPTOUT. For a list of supported opt-out keywords, see `SMS opt out <https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-keywords.html>`_ in the End User Messaging  User Guide.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-optoutlist.html
    :cloudformationResource: AWS::SMSVOICE::OptOutList
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_smsvoice as smsvoice
        
        cfn_opt_out_list = smsvoice.CfnOptOutList(self, "MyCfnOptOutList",
            opt_out_list_name="optOutListName",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        opt_out_list_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SMSVOICE::OptOutList``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param opt_out_list_name: The name of the OptOutList.
        :param tags: An array of tags (key and value pairs) to associate with the new OptOutList.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea38a41fadafddeabec02441f39c67873aa2e47aa1a61c10bd392305083031cc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOptOutListProps(opt_out_list_name=opt_out_list_name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForOptOutList")
    @builtins.classmethod
    def arn_for_opt_out_list(cls, resource: "_IOptOutListRef_1d44f5f8") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18d3377f373ff69f5f3a69ff24c03e8e55d0375f6a23941598b25909cc72b307)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForOptOutList", [resource]))

    @jsii.member(jsii_name="fromOptOutListArn")
    @builtins.classmethod
    def from_opt_out_list_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IOptOutListRef_1d44f5f8":
        '''Creates a new IOptOutListRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__124a7f8a72ebe536ef9b7171326a8506b93040fca900f1f72574cfb0fcf6615a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IOptOutListRef_1d44f5f8", jsii.sinvoke(cls, "fromOptOutListArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromOptOutListName")
    @builtins.classmethod
    def from_opt_out_list_name(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        opt_out_list_name: builtins.str,
    ) -> "_IOptOutListRef_1d44f5f8":
        '''Creates a new IOptOutListRef from a optOutListName.

        :param scope: -
        :param id: -
        :param opt_out_list_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__622c503ac8ae593c9642ed89cd09ede46c174901d31e6df008c2338639830854)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument opt_out_list_name", value=opt_out_list_name, expected_type=type_hints["opt_out_list_name"])
        return typing.cast("_IOptOutListRef_1d44f5f8", jsii.sinvoke(cls, "fromOptOutListName", [scope, id, opt_out_list_name]))

    @jsii.member(jsii_name="isCfnOptOutList")
    @builtins.classmethod
    def is_cfn_opt_out_list(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnOptOutList.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e62047306ca7777385cf98893796b700c601e221b8666242bc34282feabd1e1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnOptOutList", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5630a2d0159373226ec89552708a8f793a351be99f553dcc655511073c80a14d)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2c7567ba9b82c785acaef7a9a31d670d66d6324b4250270a7b78caf5a610f3f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the ``OptOutList`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="optOutListRef")
    def opt_out_list_ref(self) -> "_OptOutListReference_e0a13902":
        '''A reference to a OptOutList resource.'''
        return typing.cast("_OptOutListReference_e0a13902", jsii.get(self, "optOutListRef"))

    @builtins.property
    @jsii.member(jsii_name="optOutListName")
    def opt_out_list_name(self) -> typing.Optional[builtins.str]:
        '''The name of the OptOutList.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optOutListName"))

    @opt_out_list_name.setter
    def opt_out_list_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6977ae7d56495d20d799b91baa1ff8181a6a95f332ee17575071e0fb1eb4e0c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optOutListName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of tags (key and value pairs) to associate with the new OptOutList.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35f7671a5586fbcab6fa7a0f53bc16a7df7f5b446336ced45e9ee9df5e1ba997)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnOptOutListProps",
    jsii_struct_bases=[],
    name_mapping={"opt_out_list_name": "optOutListName", "tags": "tags"},
)
class CfnOptOutListProps:
    def __init__(
        self,
        *,
        opt_out_list_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOptOutList``.

        :param opt_out_list_name: The name of the OptOutList.
        :param tags: An array of tags (key and value pairs) to associate with the new OptOutList.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-optoutlist.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_smsvoice as smsvoice
            
            cfn_opt_out_list_props = smsvoice.CfnOptOutListProps(
                opt_out_list_name="optOutListName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e14e4fd94b66cfd8dd4c43fcb451f3af9853476744da6a554feeac6fa9de3e)
            check_type(argname="argument opt_out_list_name", value=opt_out_list_name, expected_type=type_hints["opt_out_list_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if opt_out_list_name is not None:
            self._values["opt_out_list_name"] = opt_out_list_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def opt_out_list_name(self) -> typing.Optional[builtins.str]:
        '''The name of the OptOutList.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-optoutlist.html#cfn-smsvoice-optoutlist-optoutlistname
        '''
        result = self._values.get("opt_out_list_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of tags (key and value pairs) to associate with the new OptOutList.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-optoutlist.html#cfn-smsvoice-optoutlist-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOptOutListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IPhoneNumberRef_7c6c9ced, _ITaggableV2_4e6798f8)
class CfnPhoneNumber(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnPhoneNumber",
):
    '''Request an origination phone number for use in your account.

    For more information on phone number request see `Request a phone number <https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-request.html>`_ in the *End User Messaging  User Guide* .
    .. epigraph::

       Registering phone numbers is not supported by AWS CloudFormation . You can import phone numbers and sender IDs that are automatically provisioned at registration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html
    :cloudformationResource: AWS::SMSVOICE::PhoneNumber
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_smsvoice as smsvoice
        
        cfn_phone_number = smsvoice.CfnPhoneNumber(self, "MyCfnPhoneNumber",
            iso_country_code="isoCountryCode",
            mandatory_keywords=smsvoice.CfnPhoneNumber.MandatoryKeywordsProperty(
                help=smsvoice.CfnPhoneNumber.MandatoryKeywordProperty(
                    message="message"
                ),
                stop=smsvoice.CfnPhoneNumber.MandatoryKeywordProperty(
                    message="message"
                )
            ),
            number_capabilities=["numberCapabilities"],
            number_type="numberType",
        
            # the properties below are optional
            deletion_protection_enabled=False,
            optional_keywords=[smsvoice.CfnPhoneNumber.OptionalKeywordProperty(
                action="action",
                keyword="keyword",
                message="message"
            )],
            opt_out_list_name="optOutListName",
            self_managed_opt_outs_enabled=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            two_way=smsvoice.CfnPhoneNumber.TwoWayProperty(
                enabled=False,
        
                # the properties below are optional
                channel_arn="channelArn",
                channel_role="channelRole"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        iso_country_code: builtins.str,
        mandatory_keywords: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPhoneNumber.MandatoryKeywordsProperty", typing.Dict[builtins.str, typing.Any]]],
        number_capabilities: typing.Sequence[builtins.str],
        number_type: builtins.str,
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        optional_keywords: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPhoneNumber.OptionalKeywordProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        opt_out_list_name: typing.Optional[builtins.str] = None,
        self_managed_opt_outs_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        two_way: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPhoneNumber.TwoWayProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SMSVOICE::PhoneNumber``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param iso_country_code: The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
        :param mandatory_keywords: Creates or updates a ``MandatoryKeyword`` configuration on an origination phone number For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging User Guide.
        :param number_capabilities: Indicates if the phone number will be used for text messages, voice messages, or both.
        :param number_type: The type of phone number to request. .. epigraph:: The ``ShortCode`` number type is not supported in AWS CloudFormation .
        :param deletion_protection_enabled: By default this is set to false. When set to true the phone number can't be deleted.
        :param optional_keywords: A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, End User Messaging responds with a customizable message. Optional keywords are differentiated from mandatory keywords. For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging User Guide.
        :param opt_out_list_name: The name of the OptOutList associated with the phone number.
        :param self_managed_opt_outs_enabled: When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out request. For more information see `Self-managed opt-outs <https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-self-managed.html>`_
        :param tags: An array of tags (key and value pairs) to associate with the requested phone number.
        :param two_way: Describes the two-way SMS configuration for a phone number. For more information, see `Two-way SMS messaging <https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms.html>`_ in the End User Messaging User Guide.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32252c96682ee51fe1d1c58cae6b6350f48d46d59b1d32994ea66401975b964d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPhoneNumberProps(
            iso_country_code=iso_country_code,
            mandatory_keywords=mandatory_keywords,
            number_capabilities=number_capabilities,
            number_type=number_type,
            deletion_protection_enabled=deletion_protection_enabled,
            optional_keywords=optional_keywords,
            opt_out_list_name=opt_out_list_name,
            self_managed_opt_outs_enabled=self_managed_opt_outs_enabled,
            tags=tags,
            two_way=two_way,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForPhoneNumber")
    @builtins.classmethod
    def arn_for_phone_number(
        cls,
        resource: "_IPhoneNumberRef_7c6c9ced",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f0507c4ca0adc8b9805dec32c85b04d0a70473ab9802f6bdc0b7e20a73538e8)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForPhoneNumber", [resource]))

    @jsii.member(jsii_name="fromPhoneNumberArn")
    @builtins.classmethod
    def from_phone_number_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IPhoneNumberRef_7c6c9ced":
        '''Creates a new IPhoneNumberRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dfc18d9f79d711e366b295b9bc0e833aa10566992f8cba470cdf07bb5e180e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IPhoneNumberRef_7c6c9ced", jsii.sinvoke(cls, "fromPhoneNumberArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromPhoneNumberId")
    @builtins.classmethod
    def from_phone_number_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        phone_number_id: builtins.str,
    ) -> "_IPhoneNumberRef_7c6c9ced":
        '''Creates a new IPhoneNumberRef from a phoneNumberId.

        :param scope: -
        :param id: -
        :param phone_number_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f23d5045dfaa44877e6d3c4cb6efd3e609dbb687fa2b056b6a62d4ef75a4f62)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument phone_number_id", value=phone_number_id, expected_type=type_hints["phone_number_id"])
        return typing.cast("_IPhoneNumberRef_7c6c9ced", jsii.sinvoke(cls, "fromPhoneNumberId", [scope, id, phone_number_id]))

    @jsii.member(jsii_name="isCfnPhoneNumber")
    @builtins.classmethod
    def is_cfn_phone_number(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnPhoneNumber.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ed59bbfbccb8fa8a24f8e2c591a74b55ce69364757c63f990bf7ba3c3ba22de)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnPhoneNumber", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3790bd7e3f6d7b04591d9b408e55b3ef461fabc7e864e5952080929d0ba44a15)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40e9d59fae1d01e88a2819b8b9178800aed746c4dce8d3f2966540129b00b0a1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ``PhoneNumber`` 's Amazon Resource Name (ARN).

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPhoneNumber")
    def attr_phone_number(self) -> builtins.str:
        '''The phone number in E.164 format.

        :cloudformationAttribute: PhoneNumber
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPhoneNumber"))

    @builtins.property
    @jsii.member(jsii_name="attrPhoneNumberId")
    def attr_phone_number_id(self) -> builtins.str:
        '''The unique identifier for the phone number.

        :cloudformationAttribute: PhoneNumberId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPhoneNumberId"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="phoneNumberRef")
    def phone_number_ref(self) -> "_PhoneNumberReference_c338f1b9":
        '''A reference to a PhoneNumber resource.'''
        return typing.cast("_PhoneNumberReference_c338f1b9", jsii.get(self, "phoneNumberRef"))

    @builtins.property
    @jsii.member(jsii_name="isoCountryCode")
    def iso_country_code(self) -> builtins.str:
        '''The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.'''
        return typing.cast(builtins.str, jsii.get(self, "isoCountryCode"))

    @iso_country_code.setter
    def iso_country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3daefae7d41f3fa1c90cfb87146384791ee02c03a5d3a0408e3e5de6616d27f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isoCountryCode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mandatoryKeywords")
    def mandatory_keywords(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.MandatoryKeywordsProperty"]:
        '''Creates or updates a ``MandatoryKeyword`` configuration on an origination phone number For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.MandatoryKeywordsProperty"], jsii.get(self, "mandatoryKeywords"))

    @mandatory_keywords.setter
    def mandatory_keywords(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.MandatoryKeywordsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ad292d2f30a2e7553a75e0648343c13f6d37e2c991e6ccfd9770c6cea89b4e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mandatoryKeywords", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="numberCapabilities")
    def number_capabilities(self) -> typing.List[builtins.str]:
        '''Indicates if the phone number will be used for text messages, voice messages, or both.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "numberCapabilities"))

    @number_capabilities.setter
    def number_capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e9985ae1545495747fd53a2ed838fb3cbdfd61c9c5bbd83714551bb40074671)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberCapabilities", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="numberType")
    def number_type(self) -> builtins.str:
        '''The type of phone number to request.'''
        return typing.cast(builtins.str, jsii.get(self, "numberType"))

    @number_type.setter
    def number_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20e8aed3a5492034d382aada9cca5055d1a5f90debfb0ada0b8ecbd5f6a1f4a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numberType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionEnabled")
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''By default this is set to false.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "deletionProtectionEnabled"))

    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ce7c946e28467484eeaef46ab5c378bc4d7cf5fabda1308e46f327ee70c4e86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtectionEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="optionalKeywords")
    def optional_keywords(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.OptionalKeywordProperty"]]]]:
        '''A keyword is a word that you can search for on a particular phone number or pool.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.OptionalKeywordProperty"]]]], jsii.get(self, "optionalKeywords"))

    @optional_keywords.setter
    def optional_keywords(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.OptionalKeywordProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2775cd03531ef2f5f4bb38b83c1e7e323c18a0def6ec05b2c4d012ace1ee4d30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionalKeywords", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="optOutListName")
    def opt_out_list_name(self) -> typing.Optional[builtins.str]:
        '''The name of the OptOutList associated with the phone number.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optOutListName"))

    @opt_out_list_name.setter
    def opt_out_list_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56421d9c352121c21655ab5960b103facff7e83cb1168aa10daabb27bea523e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optOutListName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="selfManagedOptOutsEnabled")
    def self_managed_opt_outs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging  automatically replies with a customizable message and adds the end recipient to the OptOutList.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "selfManagedOptOutsEnabled"))

    @self_managed_opt_outs_enabled.setter
    def self_managed_opt_outs_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04bf768fe622599912b3a021c396ad4d893de46bcad374eb200ccebe72a3dfd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selfManagedOptOutsEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of tags (key and value pairs) to associate with the requested phone number.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a29c798a3abd770efeb946661639d64644ab5a22b5c349f873ed430dd74b78c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="twoWay")
    def two_way(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.TwoWayProperty"]]:
        '''Describes the two-way SMS configuration for a phone number.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.TwoWayProperty"]], jsii.get(self, "twoWay"))

    @two_way.setter
    def two_way(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.TwoWayProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d4007552b2a5c50d580a9b5ece55fcd38284b10f7943be06e671add40a07f4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "twoWay", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnPhoneNumber.MandatoryKeywordProperty",
        jsii_struct_bases=[],
        name_mapping={"message": "message"},
    )
    class MandatoryKeywordProperty:
        def __init__(self, *, message: builtins.str) -> None:
            '''The keywords ``HELP`` and ``STOP`` are mandatory keywords that each phone number must have.

            For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

            :param message: The message associated with the keyword.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-mandatorykeyword.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                mandatory_keyword_property = smsvoice.CfnPhoneNumber.MandatoryKeywordProperty(
                    message="message"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5e074639964bff18f1f8daf8a4ed0ce8129ab17f01eb32a431c9c79a86d1255)
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "message": message,
            }

        @builtins.property
        def message(self) -> builtins.str:
            '''The message associated with the keyword.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-mandatorykeyword.html#cfn-smsvoice-phonenumber-mandatorykeyword-message
            '''
            result = self._values.get("message")
            assert result is not None, "Required property 'message' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MandatoryKeywordProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnPhoneNumber.MandatoryKeywordsProperty",
        jsii_struct_bases=[],
        name_mapping={"help": "help", "stop": "stop"},
    )
    class MandatoryKeywordsProperty:
        def __init__(
            self,
            *,
            help: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPhoneNumber.MandatoryKeywordProperty", typing.Dict[builtins.str, typing.Any]]],
            stop: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPhoneNumber.MandatoryKeywordProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The keywords ``HELP`` and ``STOP`` are mandatory keywords that each phone number must have.

            For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

            :param help: Specifies the ``HELP`` keyword that customers use to obtain customer support for this phone number. For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging User Guide.
            :param stop: Specifies the ``STOP`` keyword that customers use to opt out of receiving messages from this phone number. For more information, see `Required opt-out keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-required.html>`_ in the End User Messaging User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-mandatorykeywords.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                mandatory_keywords_property = smsvoice.CfnPhoneNumber.MandatoryKeywordsProperty(
                    help=smsvoice.CfnPhoneNumber.MandatoryKeywordProperty(
                        message="message"
                    ),
                    stop=smsvoice.CfnPhoneNumber.MandatoryKeywordProperty(
                        message="message"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa76e2295a1af1a67472d918d805b489816187f735ec76ae1339b5a83284d30d)
                check_type(argname="argument help", value=help, expected_type=type_hints["help"])
                check_type(argname="argument stop", value=stop, expected_type=type_hints["stop"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "help": help,
                "stop": stop,
            }

        @builtins.property
        def help(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.MandatoryKeywordProperty"]:
            '''Specifies the ``HELP`` keyword that customers use to obtain customer support for this phone number.

            For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-mandatorykeywords.html#cfn-smsvoice-phonenumber-mandatorykeywords-help
            '''
            result = self._values.get("help")
            assert result is not None, "Required property 'help' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.MandatoryKeywordProperty"], result)

        @builtins.property
        def stop(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.MandatoryKeywordProperty"]:
            '''Specifies the ``STOP`` keyword that customers use to opt out of receiving messages from this phone number.

            For more information, see `Required opt-out keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-required.html>`_ in the End User Messaging  User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-mandatorykeywords.html#cfn-smsvoice-phonenumber-mandatorykeywords-stop
            '''
            result = self._values.get("stop")
            assert result is not None, "Required property 'stop' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.MandatoryKeywordProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MandatoryKeywordsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnPhoneNumber.OptionalKeywordProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action", "keyword": "keyword", "message": "message"},
    )
    class OptionalKeywordProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            keyword: builtins.str,
            message: builtins.str,
        ) -> None:
            '''The ``OptionalKeyword`` configuration.

            For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

            :param action: The action to perform when the keyword is used.
            :param keyword: The new keyword to add.
            :param message: The message associated with the keyword.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-optionalkeyword.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                optional_keyword_property = smsvoice.CfnPhoneNumber.OptionalKeywordProperty(
                    action="action",
                    keyword="keyword",
                    message="message"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9808c2e33055bb3bc02e4746aeecf872f1d29195fd50764e4cf01373eb6e2164)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument keyword", value=keyword, expected_type=type_hints["keyword"])
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "keyword": keyword,
                "message": message,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''The action to perform when the keyword is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-optionalkeyword.html#cfn-smsvoice-phonenumber-optionalkeyword-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def keyword(self) -> builtins.str:
            '''The new keyword to add.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-optionalkeyword.html#cfn-smsvoice-phonenumber-optionalkeyword-keyword
            '''
            result = self._values.get("keyword")
            assert result is not None, "Required property 'keyword' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def message(self) -> builtins.str:
            '''The message associated with the keyword.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-optionalkeyword.html#cfn-smsvoice-phonenumber-optionalkeyword-message
            '''
            result = self._values.get("message")
            assert result is not None, "Required property 'message' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OptionalKeywordProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnPhoneNumber.TwoWayProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "channel_arn": "channelArn",
            "channel_role": "channelRole",
        },
    )
    class TwoWayProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, "_IResolvable_da3f097b"],
            channel_arn: typing.Optional[builtins.str] = None,
            channel_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The phone number's two-way SMS configuration object.

            :param enabled: By default this is set to false. When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.
            :param channel_arn: The Amazon Resource Name (ARN) of the two way channel.
            :param channel_role: An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-twoway.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                two_way_property = smsvoice.CfnPhoneNumber.TwoWayProperty(
                    enabled=False,
                
                    # the properties below are optional
                    channel_arn="channelArn",
                    channel_role="channelRole"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__67ff2e896f2988f660e4ee2793f64f4dc62d209cbf013b2753d3b0347a66ee8c)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
                check_type(argname="argument channel_role", value=channel_role, expected_type=type_hints["channel_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if channel_arn is not None:
                self._values["channel_arn"] = channel_arn
            if channel_role is not None:
                self._values["channel_role"] = channel_role

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, "_IResolvable_da3f097b"]:
            '''By default this is set to false.

            When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-twoway.html#cfn-smsvoice-phonenumber-twoway-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, "_IResolvable_da3f097b"], result)

        @builtins.property
        def channel_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the two way channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-twoway.html#cfn-smsvoice-phonenumber-twoway-channelarn
            '''
            result = self._values.get("channel_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def channel_role(self) -> typing.Optional[builtins.str]:
            '''An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-phonenumber-twoway.html#cfn-smsvoice-phonenumber-twoway-channelrole
            '''
            result = self._values.get("channel_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TwoWayProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnPhoneNumberProps",
    jsii_struct_bases=[],
    name_mapping={
        "iso_country_code": "isoCountryCode",
        "mandatory_keywords": "mandatoryKeywords",
        "number_capabilities": "numberCapabilities",
        "number_type": "numberType",
        "deletion_protection_enabled": "deletionProtectionEnabled",
        "optional_keywords": "optionalKeywords",
        "opt_out_list_name": "optOutListName",
        "self_managed_opt_outs_enabled": "selfManagedOptOutsEnabled",
        "tags": "tags",
        "two_way": "twoWay",
    },
)
class CfnPhoneNumberProps:
    def __init__(
        self,
        *,
        iso_country_code: builtins.str,
        mandatory_keywords: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPhoneNumber.MandatoryKeywordsProperty", typing.Dict[builtins.str, typing.Any]]],
        number_capabilities: typing.Sequence[builtins.str],
        number_type: builtins.str,
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        optional_keywords: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPhoneNumber.OptionalKeywordProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        opt_out_list_name: typing.Optional[builtins.str] = None,
        self_managed_opt_outs_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        two_way: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPhoneNumber.TwoWayProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPhoneNumber``.

        :param iso_country_code: The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
        :param mandatory_keywords: Creates or updates a ``MandatoryKeyword`` configuration on an origination phone number For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging User Guide.
        :param number_capabilities: Indicates if the phone number will be used for text messages, voice messages, or both.
        :param number_type: The type of phone number to request. .. epigraph:: The ``ShortCode`` number type is not supported in AWS CloudFormation .
        :param deletion_protection_enabled: By default this is set to false. When set to true the phone number can't be deleted.
        :param optional_keywords: A keyword is a word that you can search for on a particular phone number or pool. It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, End User Messaging responds with a customizable message. Optional keywords are differentiated from mandatory keywords. For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging User Guide.
        :param opt_out_list_name: The name of the OptOutList associated with the phone number.
        :param self_managed_opt_outs_enabled: When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out request. For more information see `Self-managed opt-outs <https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-self-managed.html>`_
        :param tags: An array of tags (key and value pairs) to associate with the requested phone number.
        :param two_way: Describes the two-way SMS configuration for a phone number. For more information, see `Two-way SMS messaging <https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms.html>`_ in the End User Messaging User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_smsvoice as smsvoice
            
            cfn_phone_number_props = smsvoice.CfnPhoneNumberProps(
                iso_country_code="isoCountryCode",
                mandatory_keywords=smsvoice.CfnPhoneNumber.MandatoryKeywordsProperty(
                    help=smsvoice.CfnPhoneNumber.MandatoryKeywordProperty(
                        message="message"
                    ),
                    stop=smsvoice.CfnPhoneNumber.MandatoryKeywordProperty(
                        message="message"
                    )
                ),
                number_capabilities=["numberCapabilities"],
                number_type="numberType",
            
                # the properties below are optional
                deletion_protection_enabled=False,
                optional_keywords=[smsvoice.CfnPhoneNumber.OptionalKeywordProperty(
                    action="action",
                    keyword="keyword",
                    message="message"
                )],
                opt_out_list_name="optOutListName",
                self_managed_opt_outs_enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                two_way=smsvoice.CfnPhoneNumber.TwoWayProperty(
                    enabled=False,
            
                    # the properties below are optional
                    channel_arn="channelArn",
                    channel_role="channelRole"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b70b72342e4afd37b29a5920f6cf7f0c27b8afc2a3cf6820cba50a42c515dbed)
            check_type(argname="argument iso_country_code", value=iso_country_code, expected_type=type_hints["iso_country_code"])
            check_type(argname="argument mandatory_keywords", value=mandatory_keywords, expected_type=type_hints["mandatory_keywords"])
            check_type(argname="argument number_capabilities", value=number_capabilities, expected_type=type_hints["number_capabilities"])
            check_type(argname="argument number_type", value=number_type, expected_type=type_hints["number_type"])
            check_type(argname="argument deletion_protection_enabled", value=deletion_protection_enabled, expected_type=type_hints["deletion_protection_enabled"])
            check_type(argname="argument optional_keywords", value=optional_keywords, expected_type=type_hints["optional_keywords"])
            check_type(argname="argument opt_out_list_name", value=opt_out_list_name, expected_type=type_hints["opt_out_list_name"])
            check_type(argname="argument self_managed_opt_outs_enabled", value=self_managed_opt_outs_enabled, expected_type=type_hints["self_managed_opt_outs_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument two_way", value=two_way, expected_type=type_hints["two_way"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "iso_country_code": iso_country_code,
            "mandatory_keywords": mandatory_keywords,
            "number_capabilities": number_capabilities,
            "number_type": number_type,
        }
        if deletion_protection_enabled is not None:
            self._values["deletion_protection_enabled"] = deletion_protection_enabled
        if optional_keywords is not None:
            self._values["optional_keywords"] = optional_keywords
        if opt_out_list_name is not None:
            self._values["opt_out_list_name"] = opt_out_list_name
        if self_managed_opt_outs_enabled is not None:
            self._values["self_managed_opt_outs_enabled"] = self_managed_opt_outs_enabled
        if tags is not None:
            self._values["tags"] = tags
        if two_way is not None:
            self._values["two_way"] = two_way

    @builtins.property
    def iso_country_code(self) -> builtins.str:
        '''The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html#cfn-smsvoice-phonenumber-isocountrycode
        '''
        result = self._values.get("iso_country_code")
        assert result is not None, "Required property 'iso_country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mandatory_keywords(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.MandatoryKeywordsProperty"]:
        '''Creates or updates a ``MandatoryKeyword`` configuration on an origination phone number For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html#cfn-smsvoice-phonenumber-mandatorykeywords
        '''
        result = self._values.get("mandatory_keywords")
        assert result is not None, "Required property 'mandatory_keywords' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.MandatoryKeywordsProperty"], result)

    @builtins.property
    def number_capabilities(self) -> typing.List[builtins.str]:
        '''Indicates if the phone number will be used for text messages, voice messages, or both.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html#cfn-smsvoice-phonenumber-numbercapabilities
        '''
        result = self._values.get("number_capabilities")
        assert result is not None, "Required property 'number_capabilities' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def number_type(self) -> builtins.str:
        '''The type of phone number to request.

        .. epigraph::

           The ``ShortCode`` number type is not supported in AWS CloudFormation .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html#cfn-smsvoice-phonenumber-numbertype
        '''
        result = self._values.get("number_type")
        assert result is not None, "Required property 'number_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''By default this is set to false.

        When set to true the phone number can't be deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html#cfn-smsvoice-phonenumber-deletionprotectionenabled
        '''
        result = self._values.get("deletion_protection_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def optional_keywords(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.OptionalKeywordProperty"]]]]:
        '''A keyword is a word that you can search for on a particular phone number or pool.

        It is also a specific word or phrase that an end user can send to your number to elicit a response, such as an informational message or a special offer. When your number receives a message that begins with a keyword, End User Messaging  responds with a customizable message. Optional keywords are differentiated from mandatory keywords. For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html#cfn-smsvoice-phonenumber-optionalkeywords
        '''
        result = self._values.get("optional_keywords")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.OptionalKeywordProperty"]]]], result)

    @builtins.property
    def opt_out_list_name(self) -> typing.Optional[builtins.str]:
        '''The name of the OptOutList associated with the phone number.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html#cfn-smsvoice-phonenumber-optoutlistname
        '''
        result = self._values.get("opt_out_list_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def self_managed_opt_outs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''When set to false and an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging  automatically replies with a customizable message and adds the end recipient to the OptOutList.

        When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out request. For more information see `Self-managed opt-outs <https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-self-managed.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html#cfn-smsvoice-phonenumber-selfmanagedoptoutsenabled
        '''
        result = self._values.get("self_managed_opt_outs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of tags (key and value pairs) to associate with the requested phone number.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html#cfn-smsvoice-phonenumber-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def two_way(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.TwoWayProperty"]]:
        '''Describes the two-way SMS configuration for a phone number.

        For more information, see `Two-way SMS messaging <https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms.html>`_ in the End User Messaging  User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-phonenumber.html#cfn-smsvoice-phonenumber-twoway
        '''
        result = self._values.get("two_way")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPhoneNumber.TwoWayProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPhoneNumberProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IPoolRef_897848fa, _ITaggableV2_4e6798f8)
class CfnPool(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnPool",
):
    '''Creates a new pool and associates the specified origination identity to the pool.

    A pool can include one or more phone numbers and SenderIds that are associated with your AWS account.

    The new pool inherits its configuration from the specified origination identity. This includes keywords, message type, opt-out list, two-way configuration, and self-managed opt-out configuration. Deletion protection isn't inherited from the origination identity and defaults to false.

    If the origination identity is a phone number and is already associated with another pool, an error is returned. A sender ID can be associated with multiple pools.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html
    :cloudformationResource: AWS::SMSVOICE::Pool
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_smsvoice as smsvoice
        
        cfn_pool = smsvoice.CfnPool(self, "MyCfnPool",
            mandatory_keywords=smsvoice.CfnPool.MandatoryKeywordsProperty(
                help=smsvoice.CfnPool.MandatoryKeywordProperty(
                    message="message"
                ),
                stop=smsvoice.CfnPool.MandatoryKeywordProperty(
                    message="message"
                )
            ),
            origination_identities=["originationIdentities"],
        
            # the properties below are optional
            deletion_protection_enabled=False,
            optional_keywords=[smsvoice.CfnPool.OptionalKeywordProperty(
                action="action",
                keyword="keyword",
                message="message"
            )],
            opt_out_list_name="optOutListName",
            self_managed_opt_outs_enabled=False,
            shared_routes_enabled=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            two_way=smsvoice.CfnPool.TwoWayProperty(
                enabled=False,
        
                # the properties below are optional
                channel_arn="channelArn",
                channel_role="channelRole"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        mandatory_keywords: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPool.MandatoryKeywordsProperty", typing.Dict[builtins.str, typing.Any]]],
        origination_identities: typing.Sequence[builtins.str],
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        optional_keywords: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPool.OptionalKeywordProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        opt_out_list_name: typing.Optional[builtins.str] = None,
        self_managed_opt_outs_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        shared_routes_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        two_way: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPool.TwoWayProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SMSVOICE::Pool``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param mandatory_keywords: Creates or updates the pool's ``MandatoryKeyword`` configuration. For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging User Guide.
        :param origination_identities: The list of origination identities to apply to the pool, either ``PhoneNumberArn`` or ``SenderIdArn`` . For more information, see `Registrations <https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations.html>`_ in the End User Messaging User Guide. .. epigraph:: If you are using a shared End User Messaging resource then you must use the full Amazon Resource Name (ARN).
        :param deletion_protection_enabled: When set to true the pool can't be deleted.
        :param optional_keywords: Specifies any optional keywords to associate with the pool. For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging User Guide.
        :param opt_out_list_name: The name of the OptOutList associated with the pool.
        :param self_managed_opt_outs_enabled: When set to false, an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests. For more information see `Self-managed opt-outs <https://docs.aws.amazon.com//pinpoint/latest/userguide/settings-sms-managing.html#settings-account-sms-self-managed-opt-out>`_
        :param shared_routes_enabled: Allows you to enable shared routes on your pool. By default, this is set to ``False`` . If you set this value to ``True`` , your messages are sent using phone numbers or sender IDs (depending on the country) that are shared with other users. In some countries, such as the United States, senders aren't allowed to use shared routes and must use a dedicated phone number or short code.
        :param tags: An array of tags (key and value pairs) associated with the pool.
        :param two_way: Describes the two-way SMS configuration for a phone number. For more information, see `Two-way SMS messaging <https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms.html>`_ in the End User Messaging User Guide.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59ec152307c1b9f9d8e2674741d58c16f421e0af6e557203e2d5863f8dd4ec54)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPoolProps(
            mandatory_keywords=mandatory_keywords,
            origination_identities=origination_identities,
            deletion_protection_enabled=deletion_protection_enabled,
            optional_keywords=optional_keywords,
            opt_out_list_name=opt_out_list_name,
            self_managed_opt_outs_enabled=self_managed_opt_outs_enabled,
            shared_routes_enabled=shared_routes_enabled,
            tags=tags,
            two_way=two_way,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForPool")
    @builtins.classmethod
    def arn_for_pool(cls, resource: "_IPoolRef_897848fa") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c213e5cd801b66ee29fd451845c5bf494a7f8228b76c98e75498ab918e235763)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForPool", [resource]))

    @jsii.member(jsii_name="fromPoolArn")
    @builtins.classmethod
    def from_pool_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IPoolRef_897848fa":
        '''Creates a new IPoolRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44b74b415a2e8fb8ef92df3df07db6ad2cc85726f2444e9b9d644550e1c607ba)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IPoolRef_897848fa", jsii.sinvoke(cls, "fromPoolArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromPoolId")
    @builtins.classmethod
    def from_pool_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        pool_id: builtins.str,
    ) -> "_IPoolRef_897848fa":
        '''Creates a new IPoolRef from a poolId.

        :param scope: -
        :param id: -
        :param pool_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce42e7a80b4b0868c7483a5f4ddc88ae813c01332c1d0dba0f0e1977d2a9e8f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument pool_id", value=pool_id, expected_type=type_hints["pool_id"])
        return typing.cast("_IPoolRef_897848fa", jsii.sinvoke(cls, "fromPoolId", [scope, id, pool_id]))

    @jsii.member(jsii_name="isCfnPool")
    @builtins.classmethod
    def is_cfn_pool(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnPool.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ebc5f274b1e6a6650f7be9f66a81775132163958c26b513bb3c519de35b6a7c5)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnPool", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646191d64123d913d9874d1256f9666fa44f2c2849e5f6977d435e871d608fea)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ac43d06983df817c39af941ddbd3c6b1c117b5abd772a788ebb97e746ebe6f7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name of the ``Pool`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPoolId")
    def attr_pool_id(self) -> builtins.str:
        '''The unique identifier for the pool.

        :cloudformationAttribute: PoolId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPoolId"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="poolRef")
    def pool_ref(self) -> "_PoolReference_a27a62c2":
        '''A reference to a Pool resource.'''
        return typing.cast("_PoolReference_a27a62c2", jsii.get(self, "poolRef"))

    @builtins.property
    @jsii.member(jsii_name="mandatoryKeywords")
    def mandatory_keywords(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnPool.MandatoryKeywordsProperty"]:
        '''Creates or updates the pool's ``MandatoryKeyword`` configuration.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPool.MandatoryKeywordsProperty"], jsii.get(self, "mandatoryKeywords"))

    @mandatory_keywords.setter
    def mandatory_keywords(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnPool.MandatoryKeywordsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfd14c3ecd877946c0643f80a4e0a099266dc357dd1c9f2fded20c2ed6068511)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mandatoryKeywords", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="originationIdentities")
    def origination_identities(self) -> typing.List[builtins.str]:
        '''The list of origination identities to apply to the pool, either ``PhoneNumberArn`` or ``SenderIdArn`` .'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "originationIdentities"))

    @origination_identities.setter
    def origination_identities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__909ac003d5ef554f022f835ef0908ed75231f120d614c558f2c5f51d5395a2ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originationIdentities", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionEnabled")
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''When set to true the pool can't be deleted.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "deletionProtectionEnabled"))

    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a973c88578554a2711f55af1a74d5bf3a851e51c2372e0b21001f10f4008325)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtectionEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="optionalKeywords")
    def optional_keywords(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPool.OptionalKeywordProperty"]]]]:
        '''Specifies any optional keywords to associate with the pool.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPool.OptionalKeywordProperty"]]]], jsii.get(self, "optionalKeywords"))

    @optional_keywords.setter
    def optional_keywords(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPool.OptionalKeywordProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b2ca5a55c40a8062edab9da92a8bb55730ecbfd143187de51da50b4e36607bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optionalKeywords", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="optOutListName")
    def opt_out_list_name(self) -> typing.Optional[builtins.str]:
        '''The name of the OptOutList associated with the pool.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "optOutListName"))

    @opt_out_list_name.setter
    def opt_out_list_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0921e48fa38e4645222261d2452034ec6e83d8e11c7f323b339eb5394183aa57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "optOutListName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="selfManagedOptOutsEnabled")
    def self_managed_opt_outs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''When set to false, an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging  automatically replies with a customizable message and adds the end recipient to the OptOutList.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "selfManagedOptOutsEnabled"))

    @self_managed_opt_outs_enabled.setter
    def self_managed_opt_outs_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50cb9c95473e3f15cee6cae1601c885f0fc786075af4a6607253cea1cc7c1057)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selfManagedOptOutsEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sharedRoutesEnabled")
    def shared_routes_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Allows you to enable shared routes on your pool.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "sharedRoutesEnabled"))

    @shared_routes_enabled.setter
    def shared_routes_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acfab5fb52186d7cf51c246789b7a8942e05a66e5b635a2323438e15ebf3a85c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedRoutesEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of tags (key and value pairs) associated with the pool.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80c94b1b39a42b8df6f133aad39a3eaf660a2fa0ae43777c636d9f46c4f0fbf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="twoWay")
    def two_way(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPool.TwoWayProperty"]]:
        '''Describes the two-way SMS configuration for a phone number.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPool.TwoWayProperty"]], jsii.get(self, "twoWay"))

    @two_way.setter
    def two_way(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPool.TwoWayProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98c3832bba752985f1cbf4bfdbf7efe14a8cf5d35ff7b69c2bc40a36bdc85123)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "twoWay", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnPool.MandatoryKeywordProperty",
        jsii_struct_bases=[],
        name_mapping={"message": "message"},
    )
    class MandatoryKeywordProperty:
        def __init__(self, *, message: builtins.str) -> None:
            '''The keywords ``HELP`` and ``STOP`` are mandatory keywords that each phone number must have.

            For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

            :param message: The message associated with the keyword.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-mandatorykeyword.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                mandatory_keyword_property = smsvoice.CfnPool.MandatoryKeywordProperty(
                    message="message"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ec4eab2ae9eab5ae372f5d39ce690d92ced957d23383cb67280aa740d1c77965)
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "message": message,
            }

        @builtins.property
        def message(self) -> builtins.str:
            '''The message associated with the keyword.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-mandatorykeyword.html#cfn-smsvoice-pool-mandatorykeyword-message
            '''
            result = self._values.get("message")
            assert result is not None, "Required property 'message' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MandatoryKeywordProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnPool.MandatoryKeywordsProperty",
        jsii_struct_bases=[],
        name_mapping={"help": "help", "stop": "stop"},
    )
    class MandatoryKeywordsProperty:
        def __init__(
            self,
            *,
            help: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPool.MandatoryKeywordProperty", typing.Dict[builtins.str, typing.Any]]],
            stop: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPool.MandatoryKeywordProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The manadatory keywords, ``HELP`` and ``STOP`` to add to the pool.

            For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

            :param help: Specifies the pool's ``HELP`` keyword. For more information, see `Opt out list required keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-keywords.html>`_ in the End User Messaging User Guide.
            :param stop: Specifies the pool's opt-out keyword. For more information, see `Required opt-out keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-required.html>`_ in the End User Messaging User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-mandatorykeywords.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                mandatory_keywords_property = smsvoice.CfnPool.MandatoryKeywordsProperty(
                    help=smsvoice.CfnPool.MandatoryKeywordProperty(
                        message="message"
                    ),
                    stop=smsvoice.CfnPool.MandatoryKeywordProperty(
                        message="message"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d7eb7bde31c4c3c5dd4d55c4b13717b0ee740b2f78679df8f186da6740203bc)
                check_type(argname="argument help", value=help, expected_type=type_hints["help"])
                check_type(argname="argument stop", value=stop, expected_type=type_hints["stop"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "help": help,
                "stop": stop,
            }

        @builtins.property
        def help(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnPool.MandatoryKeywordProperty"]:
            '''Specifies the pool's ``HELP`` keyword.

            For more information, see `Opt out list required keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/opt-out-list-keywords.html>`_ in the End User Messaging  User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-mandatorykeywords.html#cfn-smsvoice-pool-mandatorykeywords-help
            '''
            result = self._values.get("help")
            assert result is not None, "Required property 'help' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPool.MandatoryKeywordProperty"], result)

        @builtins.property
        def stop(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnPool.MandatoryKeywordProperty"]:
            '''Specifies the pool's opt-out keyword.

            For more information, see `Required opt-out keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords-required.html>`_ in the End User Messaging  User Guide.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-mandatorykeywords.html#cfn-smsvoice-pool-mandatorykeywords-stop
            '''
            result = self._values.get("stop")
            assert result is not None, "Required property 'stop' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPool.MandatoryKeywordProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MandatoryKeywordsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnPool.OptionalKeywordProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action", "keyword": "keyword", "message": "message"},
    )
    class OptionalKeywordProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            keyword: builtins.str,
            message: builtins.str,
        ) -> None:
            '''The pool's ``OptionalKeyword`` configuration.

            For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

            :param action: The action to perform when the keyword is used.
            :param keyword: The new keyword to add.
            :param message: The message associated with the keyword.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-optionalkeyword.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                optional_keyword_property = smsvoice.CfnPool.OptionalKeywordProperty(
                    action="action",
                    keyword="keyword",
                    message="message"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a53e8a8737df62937a61e4bdd29555e45b8fb476b28f08a4c6a174843bbc0f89)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument keyword", value=keyword, expected_type=type_hints["keyword"])
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "keyword": keyword,
                "message": message,
            }

        @builtins.property
        def action(self) -> builtins.str:
            '''The action to perform when the keyword is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-optionalkeyword.html#cfn-smsvoice-pool-optionalkeyword-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def keyword(self) -> builtins.str:
            '''The new keyword to add.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-optionalkeyword.html#cfn-smsvoice-pool-optionalkeyword-keyword
            '''
            result = self._values.get("keyword")
            assert result is not None, "Required property 'keyword' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def message(self) -> builtins.str:
            '''The message associated with the keyword.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-optionalkeyword.html#cfn-smsvoice-pool-optionalkeyword-message
            '''
            result = self._values.get("message")
            assert result is not None, "Required property 'message' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OptionalKeywordProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnPool.TwoWayProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enabled": "enabled",
            "channel_arn": "channelArn",
            "channel_role": "channelRole",
        },
    )
    class TwoWayProperty:
        def __init__(
            self,
            *,
            enabled: typing.Union[builtins.bool, "_IResolvable_da3f097b"],
            channel_arn: typing.Optional[builtins.str] = None,
            channel_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The pool's two-way SMS configuration object.

            :param enabled: By default this is set to false. When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.
            :param channel_arn: The Amazon Resource Name (ARN) of the two way channel.
            :param channel_role: An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-twoway.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                two_way_property = smsvoice.CfnPool.TwoWayProperty(
                    enabled=False,
                
                    # the properties below are optional
                    channel_arn="channelArn",
                    channel_role="channelRole"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e85b91eb6b2f50f5a971419d7521040342911deee5fc2d8e19a9a52d3f97c44)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
                check_type(argname="argument channel_role", value=channel_role, expected_type=type_hints["channel_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "enabled": enabled,
            }
            if channel_arn is not None:
                self._values["channel_arn"] = channel_arn
            if channel_role is not None:
                self._values["channel_role"] = channel_role

        @builtins.property
        def enabled(self) -> typing.Union[builtins.bool, "_IResolvable_da3f097b"]:
            '''By default this is set to false.

            When set to true you can receive incoming text messages from your end recipients using the TwoWayChannelArn.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-twoway.html#cfn-smsvoice-pool-twoway-enabled
            '''
            result = self._values.get("enabled")
            assert result is not None, "Required property 'enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, "_IResolvable_da3f097b"], result)

        @builtins.property
        def channel_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the two way channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-twoway.html#cfn-smsvoice-pool-twoway-channelarn
            '''
            result = self._values.get("channel_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def channel_role(self) -> typing.Optional[builtins.str]:
            '''An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-pool-twoway.html#cfn-smsvoice-pool-twoway-channelrole
            '''
            result = self._values.get("channel_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TwoWayProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnPoolProps",
    jsii_struct_bases=[],
    name_mapping={
        "mandatory_keywords": "mandatoryKeywords",
        "origination_identities": "originationIdentities",
        "deletion_protection_enabled": "deletionProtectionEnabled",
        "optional_keywords": "optionalKeywords",
        "opt_out_list_name": "optOutListName",
        "self_managed_opt_outs_enabled": "selfManagedOptOutsEnabled",
        "shared_routes_enabled": "sharedRoutesEnabled",
        "tags": "tags",
        "two_way": "twoWay",
    },
)
class CfnPoolProps:
    def __init__(
        self,
        *,
        mandatory_keywords: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPool.MandatoryKeywordsProperty", typing.Dict[builtins.str, typing.Any]]],
        origination_identities: typing.Sequence[builtins.str],
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        optional_keywords: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPool.OptionalKeywordProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        opt_out_list_name: typing.Optional[builtins.str] = None,
        self_managed_opt_outs_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        shared_routes_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        two_way: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPool.TwoWayProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPool``.

        :param mandatory_keywords: Creates or updates the pool's ``MandatoryKeyword`` configuration. For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging User Guide.
        :param origination_identities: The list of origination identities to apply to the pool, either ``PhoneNumberArn`` or ``SenderIdArn`` . For more information, see `Registrations <https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations.html>`_ in the End User Messaging User Guide. .. epigraph:: If you are using a shared End User Messaging resource then you must use the full Amazon Resource Name (ARN).
        :param deletion_protection_enabled: When set to true the pool can't be deleted.
        :param optional_keywords: Specifies any optional keywords to associate with the pool. For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging User Guide.
        :param opt_out_list_name: The name of the OptOutList associated with the pool.
        :param self_managed_opt_outs_enabled: When set to false, an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests. For more information see `Self-managed opt-outs <https://docs.aws.amazon.com//pinpoint/latest/userguide/settings-sms-managing.html#settings-account-sms-self-managed-opt-out>`_
        :param shared_routes_enabled: Allows you to enable shared routes on your pool. By default, this is set to ``False`` . If you set this value to ``True`` , your messages are sent using phone numbers or sender IDs (depending on the country) that are shared with other users. In some countries, such as the United States, senders aren't allowed to use shared routes and must use a dedicated phone number or short code.
        :param tags: An array of tags (key and value pairs) associated with the pool.
        :param two_way: Describes the two-way SMS configuration for a phone number. For more information, see `Two-way SMS messaging <https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms.html>`_ in the End User Messaging User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_smsvoice as smsvoice
            
            cfn_pool_props = smsvoice.CfnPoolProps(
                mandatory_keywords=smsvoice.CfnPool.MandatoryKeywordsProperty(
                    help=smsvoice.CfnPool.MandatoryKeywordProperty(
                        message="message"
                    ),
                    stop=smsvoice.CfnPool.MandatoryKeywordProperty(
                        message="message"
                    )
                ),
                origination_identities=["originationIdentities"],
            
                # the properties below are optional
                deletion_protection_enabled=False,
                optional_keywords=[smsvoice.CfnPool.OptionalKeywordProperty(
                    action="action",
                    keyword="keyword",
                    message="message"
                )],
                opt_out_list_name="optOutListName",
                self_managed_opt_outs_enabled=False,
                shared_routes_enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                two_way=smsvoice.CfnPool.TwoWayProperty(
                    enabled=False,
            
                    # the properties below are optional
                    channel_arn="channelArn",
                    channel_role="channelRole"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9949eaef09160ab08c0556130c6a54f66b5bab92951d0608bd8f05d3071a5abd)
            check_type(argname="argument mandatory_keywords", value=mandatory_keywords, expected_type=type_hints["mandatory_keywords"])
            check_type(argname="argument origination_identities", value=origination_identities, expected_type=type_hints["origination_identities"])
            check_type(argname="argument deletion_protection_enabled", value=deletion_protection_enabled, expected_type=type_hints["deletion_protection_enabled"])
            check_type(argname="argument optional_keywords", value=optional_keywords, expected_type=type_hints["optional_keywords"])
            check_type(argname="argument opt_out_list_name", value=opt_out_list_name, expected_type=type_hints["opt_out_list_name"])
            check_type(argname="argument self_managed_opt_outs_enabled", value=self_managed_opt_outs_enabled, expected_type=type_hints["self_managed_opt_outs_enabled"])
            check_type(argname="argument shared_routes_enabled", value=shared_routes_enabled, expected_type=type_hints["shared_routes_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument two_way", value=two_way, expected_type=type_hints["two_way"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mandatory_keywords": mandatory_keywords,
            "origination_identities": origination_identities,
        }
        if deletion_protection_enabled is not None:
            self._values["deletion_protection_enabled"] = deletion_protection_enabled
        if optional_keywords is not None:
            self._values["optional_keywords"] = optional_keywords
        if opt_out_list_name is not None:
            self._values["opt_out_list_name"] = opt_out_list_name
        if self_managed_opt_outs_enabled is not None:
            self._values["self_managed_opt_outs_enabled"] = self_managed_opt_outs_enabled
        if shared_routes_enabled is not None:
            self._values["shared_routes_enabled"] = shared_routes_enabled
        if tags is not None:
            self._values["tags"] = tags
        if two_way is not None:
            self._values["two_way"] = two_way

    @builtins.property
    def mandatory_keywords(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnPool.MandatoryKeywordsProperty"]:
        '''Creates or updates the pool's ``MandatoryKeyword`` configuration.

        For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html#cfn-smsvoice-pool-mandatorykeywords
        '''
        result = self._values.get("mandatory_keywords")
        assert result is not None, "Required property 'mandatory_keywords' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPool.MandatoryKeywordsProperty"], result)

    @builtins.property
    def origination_identities(self) -> typing.List[builtins.str]:
        '''The list of origination identities to apply to the pool, either ``PhoneNumberArn`` or ``SenderIdArn`` .

        For more information, see `Registrations <https://docs.aws.amazon.com/sms-voice/latest/userguide/registrations.html>`_ in the End User Messaging  User Guide.
        .. epigraph::

           If you are using a shared End User Messaging  resource then you must use the full Amazon Resource Name (ARN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html#cfn-smsvoice-pool-originationidentities
        '''
        result = self._values.get("origination_identities")
        assert result is not None, "Required property 'origination_identities' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''When set to true the pool can't be deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html#cfn-smsvoice-pool-deletionprotectionenabled
        '''
        result = self._values.get("deletion_protection_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def optional_keywords(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPool.OptionalKeywordProperty"]]]]:
        '''Specifies any optional keywords to associate with the pool.

        For more information, see `Keywords <https://docs.aws.amazon.com/sms-voice/latest/userguide/keywords.html>`_ in the End User Messaging  User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html#cfn-smsvoice-pool-optionalkeywords
        '''
        result = self._values.get("optional_keywords")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPool.OptionalKeywordProperty"]]]], result)

    @builtins.property
    def opt_out_list_name(self) -> typing.Optional[builtins.str]:
        '''The name of the OptOutList associated with the pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html#cfn-smsvoice-pool-optoutlistname
        '''
        result = self._values.get("opt_out_list_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def self_managed_opt_outs_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''When set to false, an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, End User Messaging  automatically replies with a customizable message and adds the end recipient to the OptOutList.

        When set to true you're responsible for responding to HELP and STOP requests. You're also responsible for tracking and honoring opt-out requests. For more information see `Self-managed opt-outs <https://docs.aws.amazon.com//pinpoint/latest/userguide/settings-sms-managing.html#settings-account-sms-self-managed-opt-out>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html#cfn-smsvoice-pool-selfmanagedoptoutsenabled
        '''
        result = self._values.get("self_managed_opt_outs_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def shared_routes_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Allows you to enable shared routes on your pool.

        By default, this is set to ``False`` . If you set this value to ``True`` , your messages are sent using phone numbers or sender IDs (depending on the country) that are shared with other users. In some countries, such as the United States, senders aren't allowed to use shared routes and must use a dedicated phone number or short code.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html#cfn-smsvoice-pool-sharedroutesenabled
        '''
        result = self._values.get("shared_routes_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of tags (key and value pairs) associated with the pool.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html#cfn-smsvoice-pool-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def two_way(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPool.TwoWayProperty"]]:
        '''Describes the two-way SMS configuration for a phone number.

        For more information, see `Two-way SMS messaging <https://docs.aws.amazon.com/sms-voice/latest/userguide/two-way-sms.html>`_ in the End User Messaging  User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-pool.html#cfn-smsvoice-pool-twoway
        '''
        result = self._values.get("two_way")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnPool.TwoWayProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IProtectConfigurationRef_e1ab5693, _ITaggableV2_4e6798f8)
class CfnProtectConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnProtectConfiguration",
):
    '''Create a new protect configuration.

    By default all country rule sets for each capability are set to ``ALLOW`` . A protect configurations name is stored as a Tag with the key set to ``Name`` and value as the name of the protect configuration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-protectconfiguration.html
    :cloudformationResource: AWS::SMSVOICE::ProtectConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_smsvoice as smsvoice
        
        cfn_protect_configuration = smsvoice.CfnProtectConfiguration(self, "MyCfnProtectConfiguration",
            country_rule_set=smsvoice.CfnProtectConfiguration.CountryRuleSetProperty(
                mms=[smsvoice.CfnProtectConfiguration.CountryRuleProperty(
                    country_code="countryCode",
                    protect_status="protectStatus"
                )],
                sms=[smsvoice.CfnProtectConfiguration.CountryRuleProperty(
                    country_code="countryCode",
                    protect_status="protectStatus"
                )],
                voice=[smsvoice.CfnProtectConfiguration.CountryRuleProperty(
                    country_code="countryCode",
                    protect_status="protectStatus"
                )]
            ),
            deletion_protection_enabled=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        country_rule_set: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnProtectConfiguration.CountryRuleSetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SMSVOICE::ProtectConfiguration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param country_rule_set: The set of ``CountryRules`` you specify to control which countries End User Messaging can send your messages to.
        :param deletion_protection_enabled: The status of deletion protection for the protect configuration. When set to true deletion protection is enabled. By default this is set to false.
        :param tags: An array of key and value pair tags that are associated with the resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3395de3209762a050f467d1fe0a98e4e81c55a9fa41d448e97b764225b94b11b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProtectConfigurationProps(
            country_rule_set=country_rule_set,
            deletion_protection_enabled=deletion_protection_enabled,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForProtectConfiguration")
    @builtins.classmethod
    def arn_for_protect_configuration(
        cls,
        resource: "_IProtectConfigurationRef_e1ab5693",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4038c61100766d71fab98889f2bbd57b9867902fd26f9e153acff749784440a4)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForProtectConfiguration", [resource]))

    @jsii.member(jsii_name="fromProtectConfigurationArn")
    @builtins.classmethod
    def from_protect_configuration_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IProtectConfigurationRef_e1ab5693":
        '''Creates a new IProtectConfigurationRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30a9d4af727d92ea133d23d5c13cb27130f80d90393dc02c481aa8e3278db26b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IProtectConfigurationRef_e1ab5693", jsii.sinvoke(cls, "fromProtectConfigurationArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromProtectConfigurationId")
    @builtins.classmethod
    def from_protect_configuration_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        protect_configuration_id: builtins.str,
    ) -> "_IProtectConfigurationRef_e1ab5693":
        '''Creates a new IProtectConfigurationRef from a protectConfigurationId.

        :param scope: -
        :param id: -
        :param protect_configuration_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa99a78e7c983e2ce15b9de8f681c35d2e97ff106cdb14797363208ff8fa2678)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument protect_configuration_id", value=protect_configuration_id, expected_type=type_hints["protect_configuration_id"])
        return typing.cast("_IProtectConfigurationRef_e1ab5693", jsii.sinvoke(cls, "fromProtectConfigurationId", [scope, id, protect_configuration_id]))

    @jsii.member(jsii_name="isCfnProtectConfiguration")
    @builtins.classmethod
    def is_cfn_protect_configuration(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnProtectConfiguration.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__316ece6d1df217c605229af4827f471ac066dd7863df85300e302d27eef123b1)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnProtectConfiguration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6093fb47c5b0a611eabf40e86a7bee9346024756d80420e8a57fe0de5453a18)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__126400bcb940604c8cd58c2f9c800cc69399e0f1fa7e9c15c3691a17e178d223)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the protect configuration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProtectConfigurationId")
    def attr_protect_configuration_id(self) -> builtins.str:
        '''The unique identifier for the protect configuration.

        :cloudformationAttribute: ProtectConfigurationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProtectConfigurationId"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="protectConfigurationRef")
    def protect_configuration_ref(self) -> "_ProtectConfigurationReference_c0c38d05":
        '''A reference to a ProtectConfiguration resource.'''
        return typing.cast("_ProtectConfigurationReference_c0c38d05", jsii.get(self, "protectConfigurationRef"))

    @builtins.property
    @jsii.member(jsii_name="countryRuleSet")
    def country_rule_set(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleSetProperty"]]:
        '''The set of ``CountryRules`` you specify to control which countries End User Messaging  can send your messages to.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleSetProperty"]], jsii.get(self, "countryRuleSet"))

    @country_rule_set.setter
    def country_rule_set(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleSetProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7688334aed3a536c2764f4570242ec488d7d2c28ffdc2e8acbe59bb8451f565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "countryRuleSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionEnabled")
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''The status of deletion protection for the protect configuration.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "deletionProtectionEnabled"))

    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dbdba6d79324e688bba9234d140d000e34ef557e1f8ce69b4c2334f65476a8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtectionEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key and value pair tags that are associated with the resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__426d023d6055eb2207d58490fb47ae5f69dff7c3c65aeea366fd1f204322407d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnProtectConfiguration.CountryRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "country_code": "countryCode",
            "protect_status": "protectStatus",
        },
    )
    class CountryRuleProperty:
        def __init__(
            self,
            *,
            country_code: builtins.str,
            protect_status: builtins.str,
        ) -> None:
            '''Specifies the type of protection to use for a country.

            For example, to set Canada as allowed, the ``CountryRule`` would be formatted as follows:

            ``{ "CountryCode": "CA", "ProtectStatus": "ALLOW" }``

            :param country_code: The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
            :param protect_status: The types of protection that can be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-protectconfiguration-countryrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                country_rule_property = smsvoice.CfnProtectConfiguration.CountryRuleProperty(
                    country_code="countryCode",
                    protect_status="protectStatus"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b78ebb9a5c2b273433377393613fec8c11697888ad94acc7f2c5eed1017f30a)
                check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
                check_type(argname="argument protect_status", value=protect_status, expected_type=type_hints["protect_status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "country_code": country_code,
                "protect_status": protect_status,
            }

        @builtins.property
        def country_code(self) -> builtins.str:
            '''The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-protectconfiguration-countryrule.html#cfn-smsvoice-protectconfiguration-countryrule-countrycode
            '''
            result = self._values.get("country_code")
            assert result is not None, "Required property 'country_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protect_status(self) -> builtins.str:
            '''The types of protection that can be used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-protectconfiguration-countryrule.html#cfn-smsvoice-protectconfiguration-countryrule-protectstatus
            '''
            result = self._values.get("protect_status")
            assert result is not None, "Required property 'protect_status' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CountryRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_smsvoice.CfnProtectConfiguration.CountryRuleSetProperty",
        jsii_struct_bases=[],
        name_mapping={"mms": "mms", "sms": "sms", "voice": "voice"},
    )
    class CountryRuleSetProperty:
        def __init__(
            self,
            *,
            mms: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnProtectConfiguration.CountryRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            sms: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnProtectConfiguration.CountryRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            voice: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnProtectConfiguration.CountryRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The set of ``CountryRules`` you specify to control which countries End User Messaging  can send your messages to.

            .. epigraph::

               If you don't specify all available ISO country codes in the ``CountryRuleSet`` for each number capability, the CloudFormation drift detection feature will detect drift. This is because End User Messaging  always returns all country codes.

            :param mms: The set of ``CountryRule`` s to control which destination countries End User Messaging can send your MMS messages to.
            :param sms: The set of ``CountryRule`` s to control which destination countries End User Messaging can send your SMS messages to.
            :param voice: The set of ``CountryRule`` s to control which destination countries End User Messaging can send your VOICE messages to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-protectconfiguration-countryruleset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_smsvoice as smsvoice
                
                country_rule_set_property = smsvoice.CfnProtectConfiguration.CountryRuleSetProperty(
                    mms=[smsvoice.CfnProtectConfiguration.CountryRuleProperty(
                        country_code="countryCode",
                        protect_status="protectStatus"
                    )],
                    sms=[smsvoice.CfnProtectConfiguration.CountryRuleProperty(
                        country_code="countryCode",
                        protect_status="protectStatus"
                    )],
                    voice=[smsvoice.CfnProtectConfiguration.CountryRuleProperty(
                        country_code="countryCode",
                        protect_status="protectStatus"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__81f93bccabab2bfa8d607d10049ef5df87296c85f8ebd25e0c1c13ee505638ff)
                check_type(argname="argument mms", value=mms, expected_type=type_hints["mms"])
                check_type(argname="argument sms", value=sms, expected_type=type_hints["sms"])
                check_type(argname="argument voice", value=voice, expected_type=type_hints["voice"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if mms is not None:
                self._values["mms"] = mms
            if sms is not None:
                self._values["sms"] = sms
            if voice is not None:
                self._values["voice"] = voice

        @builtins.property
        def mms(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleProperty"]]]]:
            '''The set of ``CountryRule`` s to control which destination countries End User Messaging  can send your MMS messages to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-protectconfiguration-countryruleset.html#cfn-smsvoice-protectconfiguration-countryruleset-mms
            '''
            result = self._values.get("mms")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleProperty"]]]], result)

        @builtins.property
        def sms(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleProperty"]]]]:
            '''The set of ``CountryRule`` s to control which destination countries End User Messaging  can send your SMS messages to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-protectconfiguration-countryruleset.html#cfn-smsvoice-protectconfiguration-countryruleset-sms
            '''
            result = self._values.get("sms")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleProperty"]]]], result)

        @builtins.property
        def voice(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleProperty"]]]]:
            '''The set of ``CountryRule`` s to control which destination countries End User Messaging  can send your VOICE messages to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-smsvoice-protectconfiguration-countryruleset.html#cfn-smsvoice-protectconfiguration-countryruleset-voice
            '''
            result = self._values.get("voice")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CountryRuleSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnProtectConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "country_rule_set": "countryRuleSet",
        "deletion_protection_enabled": "deletionProtectionEnabled",
        "tags": "tags",
    },
)
class CfnProtectConfigurationProps:
    def __init__(
        self,
        *,
        country_rule_set: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnProtectConfiguration.CountryRuleSetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProtectConfiguration``.

        :param country_rule_set: The set of ``CountryRules`` you specify to control which countries End User Messaging can send your messages to.
        :param deletion_protection_enabled: The status of deletion protection for the protect configuration. When set to true deletion protection is enabled. By default this is set to false.
        :param tags: An array of key and value pair tags that are associated with the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-protectconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_smsvoice as smsvoice
            
            cfn_protect_configuration_props = smsvoice.CfnProtectConfigurationProps(
                country_rule_set=smsvoice.CfnProtectConfiguration.CountryRuleSetProperty(
                    mms=[smsvoice.CfnProtectConfiguration.CountryRuleProperty(
                        country_code="countryCode",
                        protect_status="protectStatus"
                    )],
                    sms=[smsvoice.CfnProtectConfiguration.CountryRuleProperty(
                        country_code="countryCode",
                        protect_status="protectStatus"
                    )],
                    voice=[smsvoice.CfnProtectConfiguration.CountryRuleProperty(
                        country_code="countryCode",
                        protect_status="protectStatus"
                    )]
                ),
                deletion_protection_enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78062d029c984e0fa8e4c182345051e18cb19671a3a88fec3a04ea748b2d3ea8)
            check_type(argname="argument country_rule_set", value=country_rule_set, expected_type=type_hints["country_rule_set"])
            check_type(argname="argument deletion_protection_enabled", value=deletion_protection_enabled, expected_type=type_hints["deletion_protection_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if country_rule_set is not None:
            self._values["country_rule_set"] = country_rule_set
        if deletion_protection_enabled is not None:
            self._values["deletion_protection_enabled"] = deletion_protection_enabled
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def country_rule_set(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleSetProperty"]]:
        '''The set of ``CountryRules`` you specify to control which countries End User Messaging  can send your messages to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-protectconfiguration.html#cfn-smsvoice-protectconfiguration-countryruleset
        '''
        result = self._values.get("country_rule_set")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnProtectConfiguration.CountryRuleSetProperty"]], result)

    @builtins.property
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''The status of deletion protection for the protect configuration.

        When set to true deletion protection is enabled. By default this is set to false.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-protectconfiguration.html#cfn-smsvoice-protectconfiguration-deletionprotectionenabled
        '''
        result = self._values.get("deletion_protection_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key and value pair tags that are associated with the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-protectconfiguration.html#cfn-smsvoice-protectconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProtectConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IResourcePolicyRef_99a2534c)
class CfnResourcePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnResourcePolicy",
):
    '''Attaches a resource-based policy to a End User Messaging  resource(phone number, sender Id, phone poll, or opt-out list) that is used for sharing the resource.

    A shared resource can be a Pool, Opt-out list, Sender Id, or Phone number. For more information about resource-based policies, see `Working with shared resources <https://docs.aws.amazon.com/sms-voice/latest/userguide/shared-resources.html>`_ in the *End User Messaging  User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-resourcepolicy.html
    :cloudformationResource: AWS::SMSVOICE::ResourcePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_smsvoice as smsvoice
        
        # policy_document: Any
        
        cfn_resource_policy = smsvoice.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            policy_document=policy_document,
            resource_arn="resourceArn"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        policy_document: typing.Any,
        resource_arn: builtins.str,
    ) -> None:
        '''Create a new ``AWS::SMSVOICE::ResourcePolicy``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy_document: The JSON formatted resource-based policy to attach.
        :param resource_arn: The Amazon Resource Name (ARN) of the End User Messaging resource attached to the resource-based policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c761f216c3c857d8d515932ebd2444a6befe013279fe63864342547680d1115d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(
            policy_document=policy_document, resource_arn=resource_arn
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnResourcePolicy")
    @builtins.classmethod
    def is_cfn_resource_policy(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnResourcePolicy.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3cd151f4b665403a22c1254145ca08f99a360d4b4c186d8c85b0031f85e780)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnResourcePolicy", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44a964822d891ae695297d7c3a58540daae45f123040853e030d7ffb06387086)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__635deb5e16af752b1c299ada1d1bfd632b9ca21f34fd295d69073e5d2416ce83)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "_ResourcePolicyReference_b377e19e":
        '''A reference to a ResourcePolicy resource.'''
        return typing.cast("_ResourcePolicyReference_b377e19e", jsii.get(self, "resourcePolicyRef"))

    @builtins.property
    @jsii.member(jsii_name="policyDocument")
    def policy_document(self) -> typing.Any:
        '''The JSON formatted resource-based policy to attach.'''
        return typing.cast(typing.Any, jsii.get(self, "policyDocument"))

    @policy_document.setter
    def policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a78fbd4533c352d8648be0f639d4450452998ccf2ffac29dc1b66dc02d207b3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyDocument", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the End User Messaging  resource attached to the resource-based policy.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8aa28206c4f9b177dc462240fc0847f3c51410a6c2d2d6e506145ebcaad78170)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"policy_document": "policyDocument", "resource_arn": "resourceArn"},
)
class CfnResourcePolicyProps:
    def __init__(
        self,
        *,
        policy_document: typing.Any,
        resource_arn: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param policy_document: The JSON formatted resource-based policy to attach.
        :param resource_arn: The Amazon Resource Name (ARN) of the End User Messaging resource attached to the resource-based policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_smsvoice as smsvoice
            
            # policy_document: Any
            
            cfn_resource_policy_props = smsvoice.CfnResourcePolicyProps(
                policy_document=policy_document,
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52e1771fac2c1d0d2462745e3a14b0f3c7951b49866b77d8397eb55313b71662)
            check_type(argname="argument policy_document", value=policy_document, expected_type=type_hints["policy_document"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_document": policy_document,
            "resource_arn": resource_arn,
        }

    @builtins.property
    def policy_document(self) -> typing.Any:
        '''The JSON formatted resource-based policy to attach.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-resourcepolicy.html#cfn-smsvoice-resourcepolicy-policydocument
        '''
        result = self._values.get("policy_document")
        assert result is not None, "Required property 'policy_document' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the End User Messaging  resource attached to the resource-based policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-resourcepolicy.html#cfn-smsvoice-resourcepolicy-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ISenderIdRef_c6023099, _ITaggableV2_4e6798f8)
class CfnSenderId(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnSenderId",
):
    '''Request a new sender ID that doesn't require registration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-senderid.html
    :cloudformationResource: AWS::SMSVOICE::SenderId
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_smsvoice as smsvoice
        
        cfn_sender_id = smsvoice.CfnSenderId(self, "MyCfnSenderId",
            iso_country_code="isoCountryCode",
            sender_id="senderId",
        
            # the properties below are optional
            deletion_protection_enabled=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        iso_country_code: builtins.str,
        sender_id: builtins.str,
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::SMSVOICE::SenderId``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param iso_country_code: The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
        :param sender_id: The sender ID string to request.
        :param deletion_protection_enabled: By default this is set to false. When set to true the sender ID can't be deleted.
        :param tags: An array of tags (key and value pairs) to associate with the sender ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__579e8861eeec43305720b40c1d4cd3b273ca5261f965f0fa1cc4ee0e0a84e828)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSenderIdProps(
            iso_country_code=iso_country_code,
            sender_id=sender_id,
            deletion_protection_enabled=deletion_protection_enabled,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSenderId")
    @builtins.classmethod
    def arn_for_sender_id(cls, resource: "_ISenderIdRef_c6023099") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15bd52eff7a89cfde63e4f10bba79d1608ba416f3480f0d08b441514256cd305)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSenderId", [resource]))

    @jsii.member(jsii_name="isCfnSenderId")
    @builtins.classmethod
    def is_cfn_sender_id(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSenderId.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71e8852ba0bb67abcbad6b0eae3f811e39e6debb830f5e6bc7cb8ceea5d9b38c)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSenderId", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__824bd75372c0cb805352438204088f4be0bdaf1e2b369e61edb178255f394f92)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1804375aac96c7387e0282832029782ac01dfd43c99ec449a00918e05bac9bb1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name of the ``SenderId`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="senderIdRef")
    def sender_id_ref(self) -> "_SenderIdReference_10c27954":
        '''A reference to a SenderId resource.'''
        return typing.cast("_SenderIdReference_10c27954", jsii.get(self, "senderIdRef"))

    @builtins.property
    @jsii.member(jsii_name="isoCountryCode")
    def iso_country_code(self) -> builtins.str:
        '''The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.'''
        return typing.cast(builtins.str, jsii.get(self, "isoCountryCode"))

    @iso_country_code.setter
    def iso_country_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__504871ed12b07cce4e2a7fb88d40940361b5a8458ac4310092d47e2989d57d6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isoCountryCode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="senderId")
    def sender_id(self) -> builtins.str:
        '''The sender ID string to request.'''
        return typing.cast(builtins.str, jsii.get(self, "senderId"))

    @sender_id.setter
    def sender_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78c3b032bfb2bfb0c519137cf645e257ba65541833202fa1c11e4de0df7a78b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "senderId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionEnabled")
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''By default this is set to false.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "deletionProtectionEnabled"))

    @deletion_protection_enabled.setter
    def deletion_protection_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91773bda3ac0eb8138096da1ce6b25e2934b8604161e1ed8b5b998a2e2a57883)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtectionEnabled", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of tags (key and value pairs) to associate with the sender ID.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__032142149c9722a7758daf53b4af657dc1c49bbf0817db09eaabeb3076cf7c07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_smsvoice.CfnSenderIdProps",
    jsii_struct_bases=[],
    name_mapping={
        "iso_country_code": "isoCountryCode",
        "sender_id": "senderId",
        "deletion_protection_enabled": "deletionProtectionEnabled",
        "tags": "tags",
    },
)
class CfnSenderIdProps:
    def __init__(
        self,
        *,
        iso_country_code: builtins.str,
        sender_id: builtins.str,
        deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSenderId``.

        :param iso_country_code: The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
        :param sender_id: The sender ID string to request.
        :param deletion_protection_enabled: By default this is set to false. When set to true the sender ID can't be deleted.
        :param tags: An array of tags (key and value pairs) to associate with the sender ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-senderid.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_smsvoice as smsvoice
            
            cfn_sender_id_props = smsvoice.CfnSenderIdProps(
                iso_country_code="isoCountryCode",
                sender_id="senderId",
            
                # the properties below are optional
                deletion_protection_enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4efc3bfced2a81fa707bcebc646c7b881da4e547ba3c3005837a6b500a365e2)
            check_type(argname="argument iso_country_code", value=iso_country_code, expected_type=type_hints["iso_country_code"])
            check_type(argname="argument sender_id", value=sender_id, expected_type=type_hints["sender_id"])
            check_type(argname="argument deletion_protection_enabled", value=deletion_protection_enabled, expected_type=type_hints["deletion_protection_enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "iso_country_code": iso_country_code,
            "sender_id": sender_id,
        }
        if deletion_protection_enabled is not None:
            self._values["deletion_protection_enabled"] = deletion_protection_enabled
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def iso_country_code(self) -> builtins.str:
        '''The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-senderid.html#cfn-smsvoice-senderid-isocountrycode
        '''
        result = self._values.get("iso_country_code")
        assert result is not None, "Required property 'iso_country_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sender_id(self) -> builtins.str:
        '''The sender ID string to request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-senderid.html#cfn-smsvoice-senderid-senderid
        '''
        result = self._values.get("sender_id")
        assert result is not None, "Required property 'sender_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deletion_protection_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''By default this is set to false.

        When set to true the sender ID can't be deleted.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-senderid.html#cfn-smsvoice-senderid-deletionprotectionenabled
        '''
        result = self._values.get("deletion_protection_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of tags (key and value pairs) to associate with the sender ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-smsvoice-senderid.html#cfn-smsvoice-senderid-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSenderIdProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConfigurationSet",
    "CfnConfigurationSetProps",
    "CfnOptOutList",
    "CfnOptOutListProps",
    "CfnPhoneNumber",
    "CfnPhoneNumberProps",
    "CfnPool",
    "CfnPoolProps",
    "CfnProtectConfiguration",
    "CfnProtectConfigurationProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
    "CfnSenderId",
    "CfnSenderIdProps",
]

publication.publish()

def _typecheckingstub__40dfc64df6dc2c0a72f2a15a90352d0f45df52177e2673d853e93c45f6ff9bfe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration_set_name: typing.Optional[builtins.str] = None,
    default_sender_id: typing.Optional[builtins.str] = None,
    event_destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    message_feedback_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    protect_configuration_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04de3b646c1d1d3fc07c65ce19d9174446aaf197c899c5e2b9702589553a45d7(
    resource: _IConfigurationSetRef_be3ec7c2,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd09a8e0a95f96b6bf6ade58869d230ef8c16df306e2dba74636ef174182860e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2808c7d63f3da460cc51d6d5193de4fa41ad6dd91676f0cdf055c67e7f58e61(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    configuration_set_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94624c95308275f4e88fd0bcfb044adfc2050601e54cefb8f850aea329e02d30(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b8914b55c8c9175cb9d85ebbc19bd9b2ce8ee1fa9391da5cfe4b1d45d0285f4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b90e7a4776972d39f70067111684f2db6512204052e5e5368d9053b54bac6e9e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9544d5ead16000fe8542a97ab4304b9e73471d41cf77a7fcc7c28d0bf4588e3e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__186ea9a50af63ea8848866e4b7a25b25d580298e214617e976cdc49fd323660a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2057faf5fb512456c4bc44fe35430b7693158df99536b671cd30ec082b564004(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.EventDestinationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1700a269dd97f8f5889c42356bc0625812eb38d345cd6ab0a47dc65604b9ef5c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33df2949530ac82bfead10df97e9fd3007e7ef3723aea6ac4426bd0d08d7c469(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aeb00cd60ff4e73014460e95c4362f82c1d73f0b45e4e453a05465afef34da6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24be119a3ef65de30f1eb147ba1a3eac5f2a81fdd8f8285d98a680dc254f34e1(
    *,
    iam_role_arn: builtins.str,
    log_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__136edfd45f7d2c0b5dbe4db8977656e8be370d61eec90532e5a6d3d075f0d814(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    event_destination_name: builtins.str,
    matching_event_types: typing.Sequence[builtins.str],
    cloud_watch_logs_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.CloudWatchLogsDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_firehose_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.KinesisFirehoseDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sns_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.SnsDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58b63fc19b4a1791f46cfa02c2314f7bd36e3c4e54eceb6eb28919afd11059d7(
    *,
    delivery_stream_arn: builtins.str,
    iam_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e91819987879ee4dec183c370f8f16a53dffc5fa977336312072fb1db406fdaa(
    *,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__259d6b5c44c463276b6d9a529504479acbd49524ef7bd8a0d1d913ca2d1a58a3(
    *,
    configuration_set_name: typing.Optional[builtins.str] = None,
    default_sender_id: typing.Optional[builtins.str] = None,
    event_destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    message_feedback_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    protect_configuration_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea38a41fadafddeabec02441f39c67873aa2e47aa1a61c10bd392305083031cc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    opt_out_list_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18d3377f373ff69f5f3a69ff24c03e8e55d0375f6a23941598b25909cc72b307(
    resource: _IOptOutListRef_1d44f5f8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124a7f8a72ebe536ef9b7171326a8506b93040fca900f1f72574cfb0fcf6615a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__622c503ac8ae593c9642ed89cd09ede46c174901d31e6df008c2338639830854(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    opt_out_list_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e62047306ca7777385cf98893796b700c601e221b8666242bc34282feabd1e1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5630a2d0159373226ec89552708a8f793a351be99f553dcc655511073c80a14d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2c7567ba9b82c785acaef7a9a31d670d66d6324b4250270a7b78caf5a610f3f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6977ae7d56495d20d799b91baa1ff8181a6a95f332ee17575071e0fb1eb4e0c5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35f7671a5586fbcab6fa7a0f53bc16a7df7f5b446336ced45e9ee9df5e1ba997(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e14e4fd94b66cfd8dd4c43fcb451f3af9853476744da6a554feeac6fa9de3e(
    *,
    opt_out_list_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32252c96682ee51fe1d1c58cae6b6350f48d46d59b1d32994ea66401975b964d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    iso_country_code: builtins.str,
    mandatory_keywords: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPhoneNumber.MandatoryKeywordsProperty, typing.Dict[builtins.str, typing.Any]]],
    number_capabilities: typing.Sequence[builtins.str],
    number_type: builtins.str,
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    optional_keywords: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPhoneNumber.OptionalKeywordProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    opt_out_list_name: typing.Optional[builtins.str] = None,
    self_managed_opt_outs_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    two_way: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPhoneNumber.TwoWayProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f0507c4ca0adc8b9805dec32c85b04d0a70473ab9802f6bdc0b7e20a73538e8(
    resource: _IPhoneNumberRef_7c6c9ced,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dfc18d9f79d711e366b295b9bc0e833aa10566992f8cba470cdf07bb5e180e7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f23d5045dfaa44877e6d3c4cb6efd3e609dbb687fa2b056b6a62d4ef75a4f62(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    phone_number_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ed59bbfbccb8fa8a24f8e2c591a74b55ce69364757c63f990bf7ba3c3ba22de(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3790bd7e3f6d7b04591d9b408e55b3ef461fabc7e864e5952080929d0ba44a15(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40e9d59fae1d01e88a2819b8b9178800aed746c4dce8d3f2966540129b00b0a1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3daefae7d41f3fa1c90cfb87146384791ee02c03a5d3a0408e3e5de6616d27f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ad292d2f30a2e7553a75e0648343c13f6d37e2c991e6ccfd9770c6cea89b4e3(
    value: typing.Union[_IResolvable_da3f097b, CfnPhoneNumber.MandatoryKeywordsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e9985ae1545495747fd53a2ed838fb3cbdfd61c9c5bbd83714551bb40074671(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e8aed3a5492034d382aada9cca5055d1a5f90debfb0ada0b8ecbd5f6a1f4a9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ce7c946e28467484eeaef46ab5c378bc4d7cf5fabda1308e46f327ee70c4e86(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2775cd03531ef2f5f4bb38b83c1e7e323c18a0def6ec05b2c4d012ace1ee4d30(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPhoneNumber.OptionalKeywordProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56421d9c352121c21655ab5960b103facff7e83cb1168aa10daabb27bea523e0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04bf768fe622599912b3a021c396ad4d893de46bcad374eb200ccebe72a3dfd4(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a29c798a3abd770efeb946661639d64644ab5a22b5c349f873ed430dd74b78c6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d4007552b2a5c50d580a9b5ece55fcd38284b10f7943be06e671add40a07f4c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPhoneNumber.TwoWayProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e074639964bff18f1f8daf8a4ed0ce8129ab17f01eb32a431c9c79a86d1255(
    *,
    message: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa76e2295a1af1a67472d918d805b489816187f735ec76ae1339b5a83284d30d(
    *,
    help: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPhoneNumber.MandatoryKeywordProperty, typing.Dict[builtins.str, typing.Any]]],
    stop: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPhoneNumber.MandatoryKeywordProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9808c2e33055bb3bc02e4746aeecf872f1d29195fd50764e4cf01373eb6e2164(
    *,
    action: builtins.str,
    keyword: builtins.str,
    message: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67ff2e896f2988f660e4ee2793f64f4dc62d209cbf013b2753d3b0347a66ee8c(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    channel_arn: typing.Optional[builtins.str] = None,
    channel_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b70b72342e4afd37b29a5920f6cf7f0c27b8afc2a3cf6820cba50a42c515dbed(
    *,
    iso_country_code: builtins.str,
    mandatory_keywords: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPhoneNumber.MandatoryKeywordsProperty, typing.Dict[builtins.str, typing.Any]]],
    number_capabilities: typing.Sequence[builtins.str],
    number_type: builtins.str,
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    optional_keywords: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPhoneNumber.OptionalKeywordProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    opt_out_list_name: typing.Optional[builtins.str] = None,
    self_managed_opt_outs_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    two_way: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPhoneNumber.TwoWayProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59ec152307c1b9f9d8e2674741d58c16f421e0af6e557203e2d5863f8dd4ec54(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    mandatory_keywords: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPool.MandatoryKeywordsProperty, typing.Dict[builtins.str, typing.Any]]],
    origination_identities: typing.Sequence[builtins.str],
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    optional_keywords: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPool.OptionalKeywordProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    opt_out_list_name: typing.Optional[builtins.str] = None,
    self_managed_opt_outs_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    shared_routes_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    two_way: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPool.TwoWayProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c213e5cd801b66ee29fd451845c5bf494a7f8228b76c98e75498ab918e235763(
    resource: _IPoolRef_897848fa,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44b74b415a2e8fb8ef92df3df07db6ad2cc85726f2444e9b9d644550e1c607ba(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce42e7a80b4b0868c7483a5f4ddc88ae813c01332c1d0dba0f0e1977d2a9e8f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ebc5f274b1e6a6650f7be9f66a81775132163958c26b513bb3c519de35b6a7c5(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646191d64123d913d9874d1256f9666fa44f2c2849e5f6977d435e871d608fea(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ac43d06983df817c39af941ddbd3c6b1c117b5abd772a788ebb97e746ebe6f7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfd14c3ecd877946c0643f80a4e0a099266dc357dd1c9f2fded20c2ed6068511(
    value: typing.Union[_IResolvable_da3f097b, CfnPool.MandatoryKeywordsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__909ac003d5ef554f022f835ef0908ed75231f120d614c558f2c5f51d5395a2ff(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a973c88578554a2711f55af1a74d5bf3a851e51c2372e0b21001f10f4008325(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b2ca5a55c40a8062edab9da92a8bb55730ecbfd143187de51da50b4e36607bd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPool.OptionalKeywordProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0921e48fa38e4645222261d2452034ec6e83d8e11c7f323b339eb5394183aa57(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50cb9c95473e3f15cee6cae1601c885f0fc786075af4a6607253cea1cc7c1057(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acfab5fb52186d7cf51c246789b7a8942e05a66e5b635a2323438e15ebf3a85c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80c94b1b39a42b8df6f133aad39a3eaf660a2fa0ae43777c636d9f46c4f0fbf8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c3832bba752985f1cbf4bfdbf7efe14a8cf5d35ff7b69c2bc40a36bdc85123(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPool.TwoWayProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec4eab2ae9eab5ae372f5d39ce690d92ced957d23383cb67280aa740d1c77965(
    *,
    message: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d7eb7bde31c4c3c5dd4d55c4b13717b0ee740b2f78679df8f186da6740203bc(
    *,
    help: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPool.MandatoryKeywordProperty, typing.Dict[builtins.str, typing.Any]]],
    stop: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPool.MandatoryKeywordProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53e8a8737df62937a61e4bdd29555e45b8fb476b28f08a4c6a174843bbc0f89(
    *,
    action: builtins.str,
    keyword: builtins.str,
    message: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e85b91eb6b2f50f5a971419d7521040342911deee5fc2d8e19a9a52d3f97c44(
    *,
    enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    channel_arn: typing.Optional[builtins.str] = None,
    channel_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9949eaef09160ab08c0556130c6a54f66b5bab92951d0608bd8f05d3071a5abd(
    *,
    mandatory_keywords: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPool.MandatoryKeywordsProperty, typing.Dict[builtins.str, typing.Any]]],
    origination_identities: typing.Sequence[builtins.str],
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    optional_keywords: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPool.OptionalKeywordProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    opt_out_list_name: typing.Optional[builtins.str] = None,
    self_managed_opt_outs_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    shared_routes_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    two_way: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPool.TwoWayProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3395de3209762a050f467d1fe0a98e4e81c55a9fa41d448e97b764225b94b11b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    country_rule_set: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProtectConfiguration.CountryRuleSetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4038c61100766d71fab98889f2bbd57b9867902fd26f9e153acff749784440a4(
    resource: _IProtectConfigurationRef_e1ab5693,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30a9d4af727d92ea133d23d5c13cb27130f80d90393dc02c481aa8e3278db26b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa99a78e7c983e2ce15b9de8f681c35d2e97ff106cdb14797363208ff8fa2678(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    protect_configuration_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__316ece6d1df217c605229af4827f471ac066dd7863df85300e302d27eef123b1(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6093fb47c5b0a611eabf40e86a7bee9346024756d80420e8a57fe0de5453a18(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__126400bcb940604c8cd58c2f9c800cc69399e0f1fa7e9c15c3691a17e178d223(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7688334aed3a536c2764f4570242ec488d7d2c28ffdc2e8acbe59bb8451f565(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProtectConfiguration.CountryRuleSetProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dbdba6d79324e688bba9234d140d000e34ef557e1f8ce69b4c2334f65476a8b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__426d023d6055eb2207d58490fb47ae5f69dff7c3c65aeea366fd1f204322407d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b78ebb9a5c2b273433377393613fec8c11697888ad94acc7f2c5eed1017f30a(
    *,
    country_code: builtins.str,
    protect_status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81f93bccabab2bfa8d607d10049ef5df87296c85f8ebd25e0c1c13ee505638ff(
    *,
    mms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProtectConfiguration.CountryRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    sms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProtectConfiguration.CountryRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    voice: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProtectConfiguration.CountryRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78062d029c984e0fa8e4c182345051e18cb19671a3a88fec3a04ea748b2d3ea8(
    *,
    country_rule_set: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProtectConfiguration.CountryRuleSetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c761f216c3c857d8d515932ebd2444a6befe013279fe63864342547680d1115d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy_document: typing.Any,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3cd151f4b665403a22c1254145ca08f99a360d4b4c186d8c85b0031f85e780(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44a964822d891ae695297d7c3a58540daae45f123040853e030d7ffb06387086(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__635deb5e16af752b1c299ada1d1bfd632b9ca21f34fd295d69073e5d2416ce83(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a78fbd4533c352d8648be0f639d4450452998ccf2ffac29dc1b66dc02d207b3(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8aa28206c4f9b177dc462240fc0847f3c51410a6c2d2d6e506145ebcaad78170(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52e1771fac2c1d0d2462745e3a14b0f3c7951b49866b77d8397eb55313b71662(
    *,
    policy_document: typing.Any,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__579e8861eeec43305720b40c1d4cd3b273ca5261f965f0fa1cc4ee0e0a84e828(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    iso_country_code: builtins.str,
    sender_id: builtins.str,
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15bd52eff7a89cfde63e4f10bba79d1608ba416f3480f0d08b441514256cd305(
    resource: _ISenderIdRef_c6023099,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71e8852ba0bb67abcbad6b0eae3f811e39e6debb830f5e6bc7cb8ceea5d9b38c(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824bd75372c0cb805352438204088f4be0bdaf1e2b369e61edb178255f394f92(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1804375aac96c7387e0282832029782ac01dfd43c99ec449a00918e05bac9bb1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__504871ed12b07cce4e2a7fb88d40940361b5a8458ac4310092d47e2989d57d6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78c3b032bfb2bfb0c519137cf645e257ba65541833202fa1c11e4de0df7a78b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91773bda3ac0eb8138096da1ce6b25e2934b8604161e1ed8b5b998a2e2a57883(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032142149c9722a7758daf53b4af657dc1c49bbf0817db09eaabeb3076cf7c07(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4efc3bfced2a81fa707bcebc646c7b881da4e547ba3c3005837a6b500a365e2(
    *,
    iso_country_code: builtins.str,
    sender_id: builtins.str,
    deletion_protection_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
