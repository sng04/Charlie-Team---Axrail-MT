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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sqs.IQueueInlinePolicyRef")
class IQueueInlinePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a QueueInlinePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queueInlinePolicyRef")
    def queue_inline_policy_ref(self) -> "QueueInlinePolicyReference":
        '''(experimental) A reference to a QueueInlinePolicy resource.

        :stability: experimental
        '''
        ...


class _IQueueInlinePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a QueueInlinePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sqs.IQueueInlinePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="queueInlinePolicyRef")
    def queue_inline_policy_ref(self) -> "QueueInlinePolicyReference":
        '''(experimental) A reference to a QueueInlinePolicy resource.

        :stability: experimental
        '''
        return typing.cast("QueueInlinePolicyReference", jsii.get(self, "queueInlinePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueueInlinePolicyRef).__jsii_proxy_class__ = lambda : _IQueueInlinePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sqs.IQueuePolicyRef")
class IQueuePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a QueuePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queuePolicyRef")
    def queue_policy_ref(self) -> "QueuePolicyReference":
        '''(experimental) A reference to a QueuePolicy resource.

        :stability: experimental
        '''
        ...


class _IQueuePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a QueuePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sqs.IQueuePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="queuePolicyRef")
    def queue_policy_ref(self) -> "QueuePolicyReference":
        '''(experimental) A reference to a QueuePolicy resource.

        :stability: experimental
        '''
        return typing.cast("QueuePolicyReference", jsii.get(self, "queuePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueuePolicyRef).__jsii_proxy_class__ = lambda : _IQueuePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sqs.IQueueRef")
class IQueueRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Queue.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queueRef")
    def queue_ref(self) -> "QueueReference":
        '''(experimental) A reference to a Queue resource.

        :stability: experimental
        '''
        ...


class _IQueueRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Queue.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sqs.IQueueRef"

    @builtins.property
    @jsii.member(jsii_name="queueRef")
    def queue_ref(self) -> "QueueReference":
        '''(experimental) A reference to a Queue resource.

        :stability: experimental
        '''
        return typing.cast("QueueReference", jsii.get(self, "queueRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueueRef).__jsii_proxy_class__ = lambda : _IQueueRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sqs.QueueInlinePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"queue": "queue"},
)
class QueueInlinePolicyReference:
    def __init__(self, *, queue: builtins.str) -> None:
        '''A reference to a QueueInlinePolicy resource.

        :param queue: The Queue of the QueueInlinePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sqs as interfaces_sqs
            
            queue_inline_policy_reference = interfaces_sqs.QueueInlinePolicyReference(
                queue="queue"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__459eaf07910b8b59d59b589c04159ce4824d3873eb821449fccb810bc69946d5)
            check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "queue": queue,
        }

    @builtins.property
    def queue(self) -> builtins.str:
        '''The Queue of the QueueInlinePolicy resource.'''
        result = self._values.get("queue")
        assert result is not None, "Required property 'queue' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueInlinePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sqs.QueuePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"queue_policy_id": "queuePolicyId"},
)
class QueuePolicyReference:
    def __init__(self, *, queue_policy_id: builtins.str) -> None:
        '''A reference to a QueuePolicy resource.

        :param queue_policy_id: The Id of the QueuePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sqs as interfaces_sqs
            
            queue_policy_reference = interfaces_sqs.QueuePolicyReference(
                queue_policy_id="queuePolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__553c34733710cc11b4a73ad74d1a85bd5e2cea05d27b8a723847ea2a61f80ef3)
            check_type(argname="argument queue_policy_id", value=queue_policy_id, expected_type=type_hints["queue_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "queue_policy_id": queue_policy_id,
        }

    @builtins.property
    def queue_policy_id(self) -> builtins.str:
        '''The Id of the QueuePolicy resource.'''
        result = self._values.get("queue_policy_id")
        assert result is not None, "Required property 'queue_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueuePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sqs.QueueReference",
    jsii_struct_bases=[],
    name_mapping={"queue_arn": "queueArn", "queue_url": "queueUrl"},
)
class QueueReference:
    def __init__(self, *, queue_arn: builtins.str, queue_url: builtins.str) -> None:
        '''A reference to a Queue resource.

        :param queue_arn: The ARN of the Queue resource.
        :param queue_url: The QueueUrl of the Queue resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sqs as interfaces_sqs
            
            queue_reference = interfaces_sqs.QueueReference(
                queue_arn="queueArn",
                queue_url="queueUrl"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b79780c1c2cc7db23bb1950ad51f4452bf282a738a20f08da924c777ec4c171)
            check_type(argname="argument queue_arn", value=queue_arn, expected_type=type_hints["queue_arn"])
            check_type(argname="argument queue_url", value=queue_url, expected_type=type_hints["queue_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "queue_arn": queue_arn,
            "queue_url": queue_url,
        }

    @builtins.property
    def queue_arn(self) -> builtins.str:
        '''The ARN of the Queue resource.'''
        result = self._values.get("queue_arn")
        assert result is not None, "Required property 'queue_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def queue_url(self) -> builtins.str:
        '''The QueueUrl of the Queue resource.'''
        result = self._values.get("queue_url")
        assert result is not None, "Required property 'queue_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IQueueInlinePolicyRef",
    "IQueuePolicyRef",
    "IQueueRef",
    "QueueInlinePolicyReference",
    "QueuePolicyReference",
    "QueueReference",
]

publication.publish()

def _typecheckingstub__459eaf07910b8b59d59b589c04159ce4824d3873eb821449fccb810bc69946d5(
    *,
    queue: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__553c34733710cc11b4a73ad74d1a85bd5e2cea05d27b8a723847ea2a61f80ef3(
    *,
    queue_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b79780c1c2cc7db23bb1950ad51f4452bf282a738a20f08da924c777ec4c171(
    *,
    queue_arn: builtins.str,
    queue_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IQueueInlinePolicyRef, IQueuePolicyRef, IQueueRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
