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
    jsii_type="aws-cdk-lib.interfaces.aws_codeconnections.ConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"connection_arn": "connectionArn"},
)
class ConnectionReference:
    def __init__(self, *, connection_arn: builtins.str) -> None:
        '''A reference to a Connection resource.

        :param connection_arn: The ConnectionArn of the Connection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codeconnections as interfaces_codeconnections
            
            connection_reference = interfaces_codeconnections.ConnectionReference(
                connection_arn="connectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32e0a1f51a1af2deb607f1a2c1b7b7ea71617b002e04bbe9b16a3f34414d70ed)
            check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_arn": connection_arn,
        }

    @builtins.property
    def connection_arn(self) -> builtins.str:
        '''The ConnectionArn of the Connection resource.'''
        result = self._values.get("connection_arn")
        assert result is not None, "Required property 'connection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_codeconnections.IConnectionRef")
class IConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        ...


class _IConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codeconnections.IConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionReference", jsii.get(self, "connectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionRef).__jsii_proxy_class__ = lambda : _IConnectionRefProxy


__all__ = [
    "ConnectionReference",
    "IConnectionRef",
]

publication.publish()

def _typecheckingstub__32e0a1f51a1af2deb607f1a2c1b7b7ea71617b002e04bbe9b16a3f34414d70ed(
    *,
    connection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
