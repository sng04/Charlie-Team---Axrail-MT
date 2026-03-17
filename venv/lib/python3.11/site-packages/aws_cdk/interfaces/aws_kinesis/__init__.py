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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kinesis.IResourcePolicyRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesis.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kinesis.IStreamConsumerRef")
class IStreamConsumerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StreamConsumer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="streamConsumerRef")
    def stream_consumer_ref(self) -> "StreamConsumerReference":
        '''(experimental) A reference to a StreamConsumer resource.

        :stability: experimental
        '''
        ...


class _IStreamConsumerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StreamConsumer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesis.IStreamConsumerRef"

    @builtins.property
    @jsii.member(jsii_name="streamConsumerRef")
    def stream_consumer_ref(self) -> "StreamConsumerReference":
        '''(experimental) A reference to a StreamConsumer resource.

        :stability: experimental
        '''
        return typing.cast("StreamConsumerReference", jsii.get(self, "streamConsumerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStreamConsumerRef).__jsii_proxy_class__ = lambda : _IStreamConsumerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kinesis.IStreamRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesis.IStreamRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesis.ResourcePolicyReference",
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
            from aws_cdk.interfaces import aws_kinesis as interfaces_kinesis
            
            resource_policy_reference = interfaces_kinesis.ResourcePolicyReference(
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc8b8026038243f2a82e78ac417c2745222bcec45406ef7cd33042584c0499dd)
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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesis.StreamConsumerReference",
    jsii_struct_bases=[],
    name_mapping={"consumer_arn": "consumerArn"},
)
class StreamConsumerReference:
    def __init__(self, *, consumer_arn: builtins.str) -> None:
        '''A reference to a StreamConsumer resource.

        :param consumer_arn: The ConsumerARN of the StreamConsumer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kinesis as interfaces_kinesis
            
            stream_consumer_reference = interfaces_kinesis.StreamConsumerReference(
                consumer_arn="consumerArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ddde013fbaae2b35c3b65e40d19fc082d5fbb082ebd16269678ff8ab218e7b8)
            check_type(argname="argument consumer_arn", value=consumer_arn, expected_type=type_hints["consumer_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "consumer_arn": consumer_arn,
        }

    @builtins.property
    def consumer_arn(self) -> builtins.str:
        '''The ConsumerARN of the StreamConsumer resource.'''
        result = self._values.get("consumer_arn")
        assert result is not None, "Required property 'consumer_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamConsumerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kinesis.StreamReference",
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
            from aws_cdk.interfaces import aws_kinesis as interfaces_kinesis
            
            stream_reference = interfaces_kinesis.StreamReference(
                stream_arn="streamArn",
                stream_name="streamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a89c24e0df4bcb2183d6d3bcf92b9d89d9bab43c08e28b678309d4dab937f9b4)
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
    "IResourcePolicyRef",
    "IStreamConsumerRef",
    "IStreamRef",
    "ResourcePolicyReference",
    "StreamConsumerReference",
    "StreamReference",
]

publication.publish()

def _typecheckingstub__fc8b8026038243f2a82e78ac417c2745222bcec45406ef7cd33042584c0499dd(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ddde013fbaae2b35c3b65e40d19fc082d5fbb082ebd16269678ff8ab218e7b8(
    *,
    consumer_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a89c24e0df4bcb2183d6d3bcf92b9d89d9bab43c08e28b678309d4dab937f9b4(
    *,
    stream_arn: builtins.str,
    stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IResourcePolicyRef, IStreamConsumerRef, IStreamRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
