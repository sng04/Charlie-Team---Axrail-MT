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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sns.ISubscriptionRef")
class ISubscriptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Subscription.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subscriptionRef")
    def subscription_ref(self) -> "SubscriptionReference":
        '''(experimental) A reference to a Subscription resource.

        :stability: experimental
        '''
        ...


class _ISubscriptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Subscription.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sns.ISubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="subscriptionRef")
    def subscription_ref(self) -> "SubscriptionReference":
        '''(experimental) A reference to a Subscription resource.

        :stability: experimental
        '''
        return typing.cast("SubscriptionReference", jsii.get(self, "subscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubscriptionRef).__jsii_proxy_class__ = lambda : _ISubscriptionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sns.ITopicInlinePolicyRef")
class ITopicInlinePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TopicInlinePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="topicInlinePolicyRef")
    def topic_inline_policy_ref(self) -> "TopicInlinePolicyReference":
        '''(experimental) A reference to a TopicInlinePolicy resource.

        :stability: experimental
        '''
        ...


class _ITopicInlinePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TopicInlinePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sns.ITopicInlinePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="topicInlinePolicyRef")
    def topic_inline_policy_ref(self) -> "TopicInlinePolicyReference":
        '''(experimental) A reference to a TopicInlinePolicy resource.

        :stability: experimental
        '''
        return typing.cast("TopicInlinePolicyReference", jsii.get(self, "topicInlinePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicInlinePolicyRef).__jsii_proxy_class__ = lambda : _ITopicInlinePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sns.ITopicPolicyRef")
class ITopicPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TopicPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="topicPolicyRef")
    def topic_policy_ref(self) -> "TopicPolicyReference":
        '''(experimental) A reference to a TopicPolicy resource.

        :stability: experimental
        '''
        ...


class _ITopicPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TopicPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sns.ITopicPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="topicPolicyRef")
    def topic_policy_ref(self) -> "TopicPolicyReference":
        '''(experimental) A reference to a TopicPolicy resource.

        :stability: experimental
        '''
        return typing.cast("TopicPolicyReference", jsii.get(self, "topicPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicPolicyRef).__jsii_proxy_class__ = lambda : _ITopicPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sns.ITopicRef")
class ITopicRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Topic.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="topicRef")
    def topic_ref(self) -> "TopicReference":
        '''(experimental) A reference to a Topic resource.

        :stability: experimental
        '''
        ...


class _ITopicRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Topic.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sns.ITopicRef"

    @builtins.property
    @jsii.member(jsii_name="topicRef")
    def topic_ref(self) -> "TopicReference":
        '''(experimental) A reference to a Topic resource.

        :stability: experimental
        '''
        return typing.cast("TopicReference", jsii.get(self, "topicRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicRef).__jsii_proxy_class__ = lambda : _ITopicRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sns.SubscriptionReference",
    jsii_struct_bases=[],
    name_mapping={"subscription_arn": "subscriptionArn"},
)
class SubscriptionReference:
    def __init__(self, *, subscription_arn: builtins.str) -> None:
        '''A reference to a Subscription resource.

        :param subscription_arn: The Arn of the Subscription resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sns as interfaces_sns
            
            subscription_reference = interfaces_sns.SubscriptionReference(
                subscription_arn="subscriptionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89cf0bf2547ca6929244d1f37c0dce591f5c5a0cc8f04eeb7aa817f5a463a51f)
            check_type(argname="argument subscription_arn", value=subscription_arn, expected_type=type_hints["subscription_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscription_arn": subscription_arn,
        }

    @builtins.property
    def subscription_arn(self) -> builtins.str:
        '''The Arn of the Subscription resource.'''
        result = self._values.get("subscription_arn")
        assert result is not None, "Required property 'subscription_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sns.TopicInlinePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"topic_arn": "topicArn"},
)
class TopicInlinePolicyReference:
    def __init__(self, *, topic_arn: builtins.str) -> None:
        '''A reference to a TopicInlinePolicy resource.

        :param topic_arn: The TopicArn of the TopicInlinePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sns as interfaces_sns
            
            topic_inline_policy_reference = interfaces_sns.TopicInlinePolicyReference(
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb085fa38430c5cfa8747237294a4dc3de6a403dd402472cc5a4d131c8e84903)
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topic_arn": topic_arn,
        }

    @builtins.property
    def topic_arn(self) -> builtins.str:
        '''The TopicArn of the TopicInlinePolicy resource.'''
        result = self._values.get("topic_arn")
        assert result is not None, "Required property 'topic_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicInlinePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sns.TopicPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"topic_policy_id": "topicPolicyId"},
)
class TopicPolicyReference:
    def __init__(self, *, topic_policy_id: builtins.str) -> None:
        '''A reference to a TopicPolicy resource.

        :param topic_policy_id: The Id of the TopicPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sns as interfaces_sns
            
            topic_policy_reference = interfaces_sns.TopicPolicyReference(
                topic_policy_id="topicPolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5649e84d5e7a6193ba61637cd7fec19395734081b8ba7aa185c5831c66686c8)
            check_type(argname="argument topic_policy_id", value=topic_policy_id, expected_type=type_hints["topic_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topic_policy_id": topic_policy_id,
        }

    @builtins.property
    def topic_policy_id(self) -> builtins.str:
        '''The Id of the TopicPolicy resource.'''
        result = self._values.get("topic_policy_id")
        assert result is not None, "Required property 'topic_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sns.TopicReference",
    jsii_struct_bases=[],
    name_mapping={"topic_arn": "topicArn"},
)
class TopicReference:
    def __init__(self, *, topic_arn: builtins.str) -> None:
        '''A reference to a Topic resource.

        :param topic_arn: The TopicArn of the Topic resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sns as interfaces_sns
            
            topic_reference = interfaces_sns.TopicReference(
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c49feb8183d28563dfe0d2424bf0e31d642a7c2b5e59b3a2a56f21a037c9336)
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topic_arn": topic_arn,
        }

    @builtins.property
    def topic_arn(self) -> builtins.str:
        '''The TopicArn of the Topic resource.'''
        result = self._values.get("topic_arn")
        assert result is not None, "Required property 'topic_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ISubscriptionRef",
    "ITopicInlinePolicyRef",
    "ITopicPolicyRef",
    "ITopicRef",
    "SubscriptionReference",
    "TopicInlinePolicyReference",
    "TopicPolicyReference",
    "TopicReference",
]

publication.publish()

def _typecheckingstub__89cf0bf2547ca6929244d1f37c0dce591f5c5a0cc8f04eeb7aa817f5a463a51f(
    *,
    subscription_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb085fa38430c5cfa8747237294a4dc3de6a403dd402472cc5a4d131c8e84903(
    *,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5649e84d5e7a6193ba61637cd7fec19395734081b8ba7aa185c5831c66686c8(
    *,
    topic_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c49feb8183d28563dfe0d2424bf0e31d642a7c2b5e59b3a2a56f21a037c9336(
    *,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ISubscriptionRef, ITopicInlinePolicyRef, ITopicPolicyRef, ITopicRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
