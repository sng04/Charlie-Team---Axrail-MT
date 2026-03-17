r'''
# AWS::KinesisVideo Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_kinesisvideo as kinesisvideo
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for KinesisVideo construct libraries](https://constructs.dev/search?q=kinesisvideo)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::KinesisVideo resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisVideo.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::KinesisVideo](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_KinesisVideo.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_kinesisvideo import (
    ISignalingChannelRef as _ISignalingChannelRef_cbe8a964,
    IStreamRef as _IStreamRef_ff0d232b,
    SignalingChannelReference as _SignalingChannelReference_d0bc575a,
    StreamReference as _StreamReference_d8523c8e,
)


@jsii.implements(_IInspectable_c2943556, _ISignalingChannelRef_cbe8a964, _ITaggable_36806126)
class CfnSignalingChannel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisvideo.CfnSignalingChannel",
):
    '''Specifies a signaling channel.

    ``CreateSignalingChannel`` is an asynchronous operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-signalingchannel.html
    :cloudformationResource: AWS::KinesisVideo::SignalingChannel
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kinesisvideo as kinesisvideo
        
        cfn_signaling_channel = kinesisvideo.CfnSignalingChannel(self, "MyCfnSignalingChannel",
            message_ttl_seconds=123,
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            type="type"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        message_ttl_seconds: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::KinesisVideo::SignalingChannel``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param message_ttl_seconds: The period of time (in seconds) a signaling channel retains undelivered messages before they are discarded. Use ``API_UpdateSignalingChannel`` to update this value.
        :param name: A name for the signaling channel that you are creating. It must be unique for each AWS account and AWS Region .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param type: A type of the signaling channel that you are creating. Currently, ``SINGLE_MASTER`` is the only supported channel type.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58eea5563d65f986204277ab06c42f79f4e2ffc4cdc5b476a7662b9247883cd5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSignalingChannelProps(
            message_ttl_seconds=message_ttl_seconds, name=name, tags=tags, type=type
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSignalingChannel")
    @builtins.classmethod
    def arn_for_signaling_channel(
        cls,
        resource: "_ISignalingChannelRef_cbe8a964",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f943a12cf61d205b3e198fcb6b11456495270986d52e4c7b0e3cc5ff66520815)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSignalingChannel", [resource]))

    @jsii.member(jsii_name="isCfnSignalingChannel")
    @builtins.classmethod
    def is_cfn_signaling_channel(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSignalingChannel.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__619de6b6f20e948ac88e1396eaed694621afc258b72203a155b49e47da202c92)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSignalingChannel", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14c02801acfed3f47e58cd286b44774b56dac9699b2b4f0efbfa7cb846e9a8f0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__04d8fc8613cab4f404eaa5a411eb316a217c578efe3f1042ff7e9c7ae1a20d54)
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
        '''The Amazon Resource Name (ARN) of the signaling channel.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="signalingChannelRef")
    def signaling_channel_ref(self) -> "_SignalingChannelReference_d0bc575a":
        '''A reference to a SignalingChannel resource.'''
        return typing.cast("_SignalingChannelReference_d0bc575a", jsii.get(self, "signalingChannelRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="messageTtlSeconds")
    def message_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''The period of time (in seconds) a signaling channel retains undelivered messages before they are discarded.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "messageTtlSeconds"))

    @message_ttl_seconds.setter
    def message_ttl_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c723690059f227147456e4325e85267353954b76fb6f1f3ebaf081cc4db573a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "messageTtlSeconds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the signaling channel that you are creating.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3c37814ef5cdb9a7768ca5c31dd1391998e936ab96884cc6e1d2b76020d74c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e54f13767d9e88cdb8458933a141b77459f96d266266c2d15f01e595f8a4f364)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        '''A type of the signaling channel that you are creating.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65142c82be8394948ea812bc9b8f7602a7ce5c477c87477a319ed039a4c2fdd4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisvideo.CfnSignalingChannelProps",
    jsii_struct_bases=[],
    name_mapping={
        "message_ttl_seconds": "messageTtlSeconds",
        "name": "name",
        "tags": "tags",
        "type": "type",
    },
)
class CfnSignalingChannelProps:
    def __init__(
        self,
        *,
        message_ttl_seconds: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSignalingChannel``.

        :param message_ttl_seconds: The period of time (in seconds) a signaling channel retains undelivered messages before they are discarded. Use ``API_UpdateSignalingChannel`` to update this value.
        :param name: A name for the signaling channel that you are creating. It must be unique for each AWS account and AWS Region .
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        :param type: A type of the signaling channel that you are creating. Currently, ``SINGLE_MASTER`` is the only supported channel type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-signalingchannel.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kinesisvideo as kinesisvideo
            
            cfn_signaling_channel_props = kinesisvideo.CfnSignalingChannelProps(
                message_ttl_seconds=123,
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b54efbb13d30ecdaf3fde9f6d6c355925b3f6647db068f9a07e7f409326d7e74)
            check_type(argname="argument message_ttl_seconds", value=message_ttl_seconds, expected_type=type_hints["message_ttl_seconds"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if message_ttl_seconds is not None:
            self._values["message_ttl_seconds"] = message_ttl_seconds
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def message_ttl_seconds(self) -> typing.Optional[jsii.Number]:
        '''The period of time (in seconds) a signaling channel retains undelivered messages before they are discarded.

        Use ``API_UpdateSignalingChannel`` to update this value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-signalingchannel.html#cfn-kinesisvideo-signalingchannel-messagettlseconds
        '''
        result = self._values.get("message_ttl_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A name for the signaling channel that you are creating.

        It must be unique for each AWS account and AWS Region .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-signalingchannel.html#cfn-kinesisvideo-signalingchannel-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-signalingchannel.html#cfn-kinesisvideo-signalingchannel-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''A type of the signaling channel that you are creating.

        Currently, ``SINGLE_MASTER`` is the only supported channel type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-signalingchannel.html#cfn-kinesisvideo-signalingchannel-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSignalingChannelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IStreamRef_ff0d232b, _ITaggable_36806126)
class CfnStream(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_kinesisvideo.CfnStream",
):
    '''Specifies a new Kinesis video stream.

    When you create a new stream, Kinesis Video Streams assigns it a version number. When you change the stream's metadata, Kinesis Video Streams updates the version.

    ``CreateStream`` is an asynchronous operation.

    For information about how the service works, see `How it Works <https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/how-it-works.html>`_ .

    You must have permissions for the ``KinesisVideo:CreateStream`` action.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-stream.html
    :cloudformationResource: AWS::KinesisVideo::Stream
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_kinesisvideo as kinesisvideo
        
        cfn_stream = kinesisvideo.CfnStream(self, "MyCfnStream",
            data_retention_in_hours=123,
            device_name="deviceName",
            kms_key_id="kmsKeyId",
            media_type="mediaType",
            name="name",
            stream_storage_configuration=kinesisvideo.CfnStream.StreamStorageConfigurationProperty(
                default_storage_tier="defaultStorageTier"
            ),
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
        data_retention_in_hours: typing.Optional[jsii.Number] = None,
        device_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        media_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        stream_storage_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnStream.StreamStorageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::KinesisVideo::Stream``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_retention_in_hours: How long the stream retains data, in hours.
        :param device_name: The name of the device that is associated with the stream.
        :param kms_key_id: The ID of the AWS Key Management Service ( AWS ) key that Kinesis Video Streams uses to encrypt data on the stream.
        :param media_type: The ``MediaType`` of the stream.
        :param name: The name of the stream.
        :param stream_storage_configuration: The configuration for stream storage, including the default storage tier for stream data. This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ec46ef966c55301f1d7f90935a5a7340c3d7ee98963234b59d16d191c12645f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStreamProps(
            data_retention_in_hours=data_retention_in_hours,
            device_name=device_name,
            kms_key_id=kms_key_id,
            media_type=media_type,
            name=name,
            stream_storage_configuration=stream_storage_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForStream")
    @builtins.classmethod
    def arn_for_stream(cls, resource: "_IStreamRef_ff0d232b") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d38301bab4e9a780a923b10ea8c1ff4821d9241fed12ad8d638b9bf035dbb82e)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForStream", [resource]))

    @jsii.member(jsii_name="isCfnStream")
    @builtins.classmethod
    def is_cfn_stream(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnStream.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9f778dacdea02c1501883a5f1b0b7fc6733f60cad294d68e73bbfee8c08bf72)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnStream", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cce8d8f4e1ffc1f91558eea316dc5656b61eced6fd4e5ed8f9c5d2aedaeb00f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b2eaeb2463d77f12c25cfffaa90b0228c8ad3367c833e28aa8d5ea28acb3a5be)
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
        '''The Amazon Resource Name (ARN) of the stream.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="streamRef")
    def stream_ref(self) -> "_StreamReference_d8523c8e":
        '''A reference to a Stream resource.'''
        return typing.cast("_StreamReference_d8523c8e", jsii.get(self, "streamRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="dataRetentionInHours")
    def data_retention_in_hours(self) -> typing.Optional[jsii.Number]:
        '''How long the stream retains data, in hours.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataRetentionInHours"))

    @data_retention_in_hours.setter
    def data_retention_in_hours(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5989e41645eadecef42c0bdf99f770e2e3f8c8b44548248c846904becce9d21f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataRetentionInHours", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="deviceName")
    def device_name(self) -> typing.Optional[builtins.str]:
        '''The name of the device that is associated with the stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deviceName"))

    @device_name.setter
    def device_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__053aef53b51f16780f6be104ce8bd9054ddb361b7605af31bf2c1c461ac7d906)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deviceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service ( AWS  ) key that Kinesis Video Streams uses to encrypt data on the stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e694945b3a2d644d84a7fd5258fc39dc4b1a0f4363002922bd0fe2393010068b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mediaType")
    def media_type(self) -> typing.Optional[builtins.str]:
        '''The ``MediaType`` of the stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mediaType"))

    @media_type.setter
    def media_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__506e77b7c44b037a2897266c4a2a2a29610a8b5792ba5770f2a7606eae862412)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42f11c245ea7a28ba3c7727c31351ffc7b0f10775943c038ec944523d1ac9786)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="streamStorageConfiguration")
    def stream_storage_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnStream.StreamStorageConfigurationProperty"]]:
        '''The configuration for stream storage, including the default storage tier for stream data.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnStream.StreamStorageConfigurationProperty"]], jsii.get(self, "streamStorageConfiguration"))

    @stream_storage_configuration.setter
    def stream_storage_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnStream.StreamStorageConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__353e31ad55994ee34db35f925ed1ba94ca68ffb3ce97ad064feb40830721c5c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamStorageConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__916b61187a1fea0754be9981eeeb345ba75e61b6417bbde10d8246657f4cff69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_kinesisvideo.CfnStream.StreamStorageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"default_storage_tier": "defaultStorageTier"},
    )
    class StreamStorageConfigurationProperty:
        def __init__(
            self,
            *,
            default_storage_tier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for stream storage, including the default storage tier for stream data.

            This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.

            :param default_storage_tier: The default storage tier for the stream data. This setting determines the storage class used for stream data, affecting both performance characteristics and storage costs. Available storage tiers: - ``HOT`` - Optimized for frequent access with the lowest latency and highest performance. Ideal for real-time applications and frequently accessed data. - ``WARM`` - Balanced performance and cost for moderately accessed data. Suitable for data that is accessed regularly but not continuously. Default: - "HOT"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisvideo-stream-streamstorageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_kinesisvideo as kinesisvideo
                
                stream_storage_configuration_property = kinesisvideo.CfnStream.StreamStorageConfigurationProperty(
                    default_storage_tier="defaultStorageTier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0b7b767c6dc68700d380e90c6d53c4b73ae75797443dc5990f82cd0fd0ed319)
                check_type(argname="argument default_storage_tier", value=default_storage_tier, expected_type=type_hints["default_storage_tier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if default_storage_tier is not None:
                self._values["default_storage_tier"] = default_storage_tier

        @builtins.property
        def default_storage_tier(self) -> typing.Optional[builtins.str]:
            '''The default storage tier for the stream data.

            This setting determines the storage class used for stream data, affecting both performance characteristics and storage costs.

            Available storage tiers:

            - ``HOT`` - Optimized for frequent access with the lowest latency and highest performance. Ideal for real-time applications and frequently accessed data.
            - ``WARM`` - Balanced performance and cost for moderately accessed data. Suitable for data that is accessed regularly but not continuously.

            :default: - "HOT"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kinesisvideo-stream-streamstorageconfiguration.html#cfn-kinesisvideo-stream-streamstorageconfiguration-defaultstoragetier
            '''
            result = self._values.get("default_storage_tier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamStorageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_kinesisvideo.CfnStreamProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_retention_in_hours": "dataRetentionInHours",
        "device_name": "deviceName",
        "kms_key_id": "kmsKeyId",
        "media_type": "mediaType",
        "name": "name",
        "stream_storage_configuration": "streamStorageConfiguration",
        "tags": "tags",
    },
)
class CfnStreamProps:
    def __init__(
        self,
        *,
        data_retention_in_hours: typing.Optional[jsii.Number] = None,
        device_name: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        media_type: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        stream_storage_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnStream.StreamStorageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnStream``.

        :param data_retention_in_hours: How long the stream retains data, in hours.
        :param device_name: The name of the device that is associated with the stream.
        :param kms_key_id: The ID of the AWS Key Management Service ( AWS ) key that Kinesis Video Streams uses to encrypt data on the stream.
        :param media_type: The ``MediaType`` of the stream.
        :param name: The name of the stream.
        :param stream_storage_configuration: The configuration for stream storage, including the default storage tier for stream data. This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-stream.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_kinesisvideo as kinesisvideo
            
            cfn_stream_props = kinesisvideo.CfnStreamProps(
                data_retention_in_hours=123,
                device_name="deviceName",
                kms_key_id="kmsKeyId",
                media_type="mediaType",
                name="name",
                stream_storage_configuration=kinesisvideo.CfnStream.StreamStorageConfigurationProperty(
                    default_storage_tier="defaultStorageTier"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99fe3ebad84d54122e4e37ffa968edc213c9518bca26ea24531a78c1fa0e2c8d)
            check_type(argname="argument data_retention_in_hours", value=data_retention_in_hours, expected_type=type_hints["data_retention_in_hours"])
            check_type(argname="argument device_name", value=device_name, expected_type=type_hints["device_name"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument media_type", value=media_type, expected_type=type_hints["media_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument stream_storage_configuration", value=stream_storage_configuration, expected_type=type_hints["stream_storage_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if data_retention_in_hours is not None:
            self._values["data_retention_in_hours"] = data_retention_in_hours
        if device_name is not None:
            self._values["device_name"] = device_name
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if media_type is not None:
            self._values["media_type"] = media_type
        if name is not None:
            self._values["name"] = name
        if stream_storage_configuration is not None:
            self._values["stream_storage_configuration"] = stream_storage_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_retention_in_hours(self) -> typing.Optional[jsii.Number]:
        '''How long the stream retains data, in hours.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-stream.html#cfn-kinesisvideo-stream-dataretentioninhours
        '''
        result = self._values.get("data_retention_in_hours")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def device_name(self) -> typing.Optional[builtins.str]:
        '''The name of the device that is associated with the stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-stream.html#cfn-kinesisvideo-stream-devicename
        '''
        result = self._values.get("device_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the AWS Key Management Service ( AWS  ) key that Kinesis Video Streams uses to encrypt data on the stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-stream.html#cfn-kinesisvideo-stream-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def media_type(self) -> typing.Optional[builtins.str]:
        '''The ``MediaType`` of the stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-stream.html#cfn-kinesisvideo-stream-mediatype
        '''
        result = self._values.get("media_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-stream.html#cfn-kinesisvideo-stream-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stream_storage_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnStream.StreamStorageConfigurationProperty"]]:
        '''The configuration for stream storage, including the default storage tier for stream data.

        This configuration determines how stream data is stored and accessed, with different tiers offering varying levels of performance and cost optimization.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-stream.html#cfn-kinesisvideo-stream-streamstorageconfiguration
        '''
        result = self._values.get("stream_storage_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnStream.StreamStorageConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kinesisvideo-stream.html#cfn-kinesisvideo-stream-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStreamProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSignalingChannel",
    "CfnSignalingChannelProps",
    "CfnStream",
    "CfnStreamProps",
]

publication.publish()

def _typecheckingstub__58eea5563d65f986204277ab06c42f79f4e2ffc4cdc5b476a7662b9247883cd5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    message_ttl_seconds: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f943a12cf61d205b3e198fcb6b11456495270986d52e4c7b0e3cc5ff66520815(
    resource: _ISignalingChannelRef_cbe8a964,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619de6b6f20e948ac88e1396eaed694621afc258b72203a155b49e47da202c92(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14c02801acfed3f47e58cd286b44774b56dac9699b2b4f0efbfa7cb846e9a8f0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04d8fc8613cab4f404eaa5a411eb316a217c578efe3f1042ff7e9c7ae1a20d54(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c723690059f227147456e4325e85267353954b76fb6f1f3ebaf081cc4db573a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3c37814ef5cdb9a7768ca5c31dd1391998e936ab96884cc6e1d2b76020d74c6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e54f13767d9e88cdb8458933a141b77459f96d266266c2d15f01e595f8a4f364(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65142c82be8394948ea812bc9b8f7602a7ce5c477c87477a319ed039a4c2fdd4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b54efbb13d30ecdaf3fde9f6d6c355925b3f6647db068f9a07e7f409326d7e74(
    *,
    message_ttl_seconds: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec46ef966c55301f1d7f90935a5a7340c3d7ee98963234b59d16d191c12645f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_retention_in_hours: typing.Optional[jsii.Number] = None,
    device_name: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    media_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    stream_storage_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStream.StreamStorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d38301bab4e9a780a923b10ea8c1ff4821d9241fed12ad8d638b9bf035dbb82e(
    resource: _IStreamRef_ff0d232b,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9f778dacdea02c1501883a5f1b0b7fc6733f60cad294d68e73bbfee8c08bf72(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cce8d8f4e1ffc1f91558eea316dc5656b61eced6fd4e5ed8f9c5d2aedaeb00f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2eaeb2463d77f12c25cfffaa90b0228c8ad3367c833e28aa8d5ea28acb3a5be(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5989e41645eadecef42c0bdf99f770e2e3f8c8b44548248c846904becce9d21f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__053aef53b51f16780f6be104ce8bd9054ddb361b7605af31bf2c1c461ac7d906(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e694945b3a2d644d84a7fd5258fc39dc4b1a0f4363002922bd0fe2393010068b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__506e77b7c44b037a2897266c4a2a2a29610a8b5792ba5770f2a7606eae862412(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42f11c245ea7a28ba3c7727c31351ffc7b0f10775943c038ec944523d1ac9786(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__353e31ad55994ee34db35f925ed1ba94ca68ffb3ce97ad064feb40830721c5c9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStream.StreamStorageConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916b61187a1fea0754be9981eeeb345ba75e61b6417bbde10d8246657f4cff69(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b7b767c6dc68700d380e90c6d53c4b73ae75797443dc5990f82cd0fd0ed319(
    *,
    default_storage_tier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99fe3ebad84d54122e4e37ffa968edc213c9518bca26ea24531a78c1fa0e2c8d(
    *,
    data_retention_in_hours: typing.Optional[jsii.Number] = None,
    device_name: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    media_type: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    stream_storage_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStream.StreamStorageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
