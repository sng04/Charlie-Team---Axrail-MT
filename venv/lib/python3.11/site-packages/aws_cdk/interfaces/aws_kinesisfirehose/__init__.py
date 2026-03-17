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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisfirehose.DeliveryStreamReference",
    jsii_struct_bases=[],
    name_mapping={
        "delivery_stream_arn": "deliveryStreamArn",
        "delivery_stream_name": "deliveryStreamName",
    },
)
class DeliveryStreamReference:
    def __init__(
        self,
        *,
        delivery_stream_arn: builtins.str,
        delivery_stream_name: builtins.str,
    ) -> None:
        '''A reference to a DeliveryStream resource.

        :param delivery_stream_arn: The ARN of the DeliveryStream resource.
        :param delivery_stream_name: The DeliveryStreamName of the DeliveryStream resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kinesisfirehose as interfaces_kinesisfirehose
            
            delivery_stream_reference = interfaces_kinesisfirehose.DeliveryStreamReference(
                delivery_stream_arn="deliveryStreamArn",
                delivery_stream_name="deliveryStreamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f067c56f25fa525ea834d9b7e5531147bcecdb28339803d134d281e9f9215ae0)
            check_type(argname="argument delivery_stream_arn", value=delivery_stream_arn, expected_type=type_hints["delivery_stream_arn"])
            check_type(argname="argument delivery_stream_name", value=delivery_stream_name, expected_type=type_hints["delivery_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delivery_stream_arn": delivery_stream_arn,
            "delivery_stream_name": delivery_stream_name,
        }

    @builtins.property
    def delivery_stream_arn(self) -> builtins.str:
        '''The ARN of the DeliveryStream resource.'''
        result = self._values.get("delivery_stream_arn")
        assert result is not None, "Required property 'delivery_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def delivery_stream_name(self) -> builtins.str:
        '''The DeliveryStreamName of the DeliveryStream resource.'''
        result = self._values.get("delivery_stream_name")
        assert result is not None, "Required property 'delivery_stream_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeliveryStreamReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisfirehose.IDeliveryStreamRef"
)
class IDeliveryStreamRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeliveryStream.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamRef")
    def delivery_stream_ref(self) -> "DeliveryStreamReference":
        '''(experimental) A reference to a DeliveryStream resource.

        :stability: experimental
        '''
        ...


class _IDeliveryStreamRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeliveryStream.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesisfirehose.IDeliveryStreamRef"

    @builtins.property
    @jsii.member(jsii_name="deliveryStreamRef")
    def delivery_stream_ref(self) -> "DeliveryStreamReference":
        '''(experimental) A reference to a DeliveryStream resource.

        :stability: experimental
        '''
        return typing.cast("DeliveryStreamReference", jsii.get(self, "deliveryStreamRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeliveryStreamRef).__jsii_proxy_class__ = lambda : _IDeliveryStreamRefProxy


__all__ = [
    "DeliveryStreamReference",
    "IDeliveryStreamRef",
]

publication.publish()

def _typecheckingstub__f067c56f25fa525ea834d9b7e5531147bcecdb28339803d134d281e9f9215ae0(
    *,
    delivery_stream_arn: builtins.str,
    delivery_stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDeliveryStreamRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
