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
    jsii_type="aws-cdk-lib.interfaces.aws_gameliftstreams.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_arn": "applicationArn"},
)
class ApplicationReference:
    def __init__(self, *, application_arn: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_arn: The Arn of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gameliftstreams as interfaces_gameliftstreams
            
            application_reference = interfaces_gameliftstreams.ApplicationReference(
                application_arn="applicationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35306b5b8d8c66b00c7d1e6d65a6f1af5408b110514ee0c3419a34e3054b4e3c)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The Arn of the Application resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gameliftstreams.IApplicationRef")
class IApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        ...


class _IApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gameliftstreams.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gameliftstreams.IStreamGroupRef")
class IStreamGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StreamGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="streamGroupRef")
    def stream_group_ref(self) -> "StreamGroupReference":
        '''(experimental) A reference to a StreamGroup resource.

        :stability: experimental
        '''
        ...


class _IStreamGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StreamGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gameliftstreams.IStreamGroupRef"

    @builtins.property
    @jsii.member(jsii_name="streamGroupRef")
    def stream_group_ref(self) -> "StreamGroupReference":
        '''(experimental) A reference to a StreamGroup resource.

        :stability: experimental
        '''
        return typing.cast("StreamGroupReference", jsii.get(self, "streamGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStreamGroupRef).__jsii_proxy_class__ = lambda : _IStreamGroupRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gameliftstreams.StreamGroupReference",
    jsii_struct_bases=[],
    name_mapping={"stream_group_arn": "streamGroupArn"},
)
class StreamGroupReference:
    def __init__(self, *, stream_group_arn: builtins.str) -> None:
        '''A reference to a StreamGroup resource.

        :param stream_group_arn: The Arn of the StreamGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gameliftstreams as interfaces_gameliftstreams
            
            stream_group_reference = interfaces_gameliftstreams.StreamGroupReference(
                stream_group_arn="streamGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fa442282ee200b2d3d65ba2874ba074141e7ca047d701ce1eb4fd06ce617b59)
            check_type(argname="argument stream_group_arn", value=stream_group_arn, expected_type=type_hints["stream_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stream_group_arn": stream_group_arn,
        }

    @builtins.property
    def stream_group_arn(self) -> builtins.str:
        '''The Arn of the StreamGroup resource.'''
        result = self._values.get("stream_group_arn")
        assert result is not None, "Required property 'stream_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StreamGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApplicationReference",
    "IApplicationRef",
    "IStreamGroupRef",
    "StreamGroupReference",
]

publication.publish()

def _typecheckingstub__35306b5b8d8c66b00c7d1e6d65a6f1af5408b110514ee0c3419a34e3054b4e3c(
    *,
    application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fa442282ee200b2d3d65ba2874ba074141e7ca047d701ce1eb4fd06ce617b59(
    *,
    stream_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef, IStreamGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
