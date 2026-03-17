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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_qldb.ILedgerRef")
class ILedgerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Ledger.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ledgerRef")
    def ledger_ref(self) -> "LedgerReference":
        '''(experimental) A reference to a Ledger resource.

        :stability: experimental
        '''
        ...


class _ILedgerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Ledger.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_qldb.ILedgerRef"

    @builtins.property
    @jsii.member(jsii_name="ledgerRef")
    def ledger_ref(self) -> "LedgerReference":
        '''(experimental) A reference to a Ledger resource.

        :stability: experimental
        '''
        return typing.cast("LedgerReference", jsii.get(self, "ledgerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILedgerRef).__jsii_proxy_class__ = lambda : _ILedgerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_qldb.IStreamRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_qldb.IStreamRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_qldb.LedgerReference",
    jsii_struct_bases=[],
    name_mapping={"ledger_id": "ledgerId"},
)
class LedgerReference:
    def __init__(self, *, ledger_id: builtins.str) -> None:
        '''A reference to a Ledger resource.

        :param ledger_id: The Id of the Ledger resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_qldb as interfaces_qldb
            
            ledger_reference = interfaces_qldb.LedgerReference(
                ledger_id="ledgerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d35dfa03f6a65253d6030611d9debe504406dc352632c923d7dd27060c29db3)
            check_type(argname="argument ledger_id", value=ledger_id, expected_type=type_hints["ledger_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ledger_id": ledger_id,
        }

    @builtins.property
    def ledger_id(self) -> builtins.str:
        '''The Id of the Ledger resource.'''
        result = self._values.get("ledger_id")
        assert result is not None, "Required property 'ledger_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LedgerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_qldb.StreamReference",
    jsii_struct_bases=[],
    name_mapping={
        "ledger_name": "ledgerName",
        "stream_arn": "streamArn",
        "stream_id": "streamId",
    },
)
class StreamReference:
    def __init__(
        self,
        *,
        ledger_name: builtins.str,
        stream_arn: builtins.str,
        stream_id: builtins.str,
    ) -> None:
        '''A reference to a Stream resource.

        :param ledger_name: The LedgerName of the Stream resource.
        :param stream_arn: The ARN of the Stream resource.
        :param stream_id: The Id of the Stream resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_qldb as interfaces_qldb
            
            stream_reference = interfaces_qldb.StreamReference(
                ledger_name="ledgerName",
                stream_arn="streamArn",
                stream_id="streamId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f3daacfed0da29e06d565867ef84aa514dbf53a1939364d24334cb876768614)
            check_type(argname="argument ledger_name", value=ledger_name, expected_type=type_hints["ledger_name"])
            check_type(argname="argument stream_arn", value=stream_arn, expected_type=type_hints["stream_arn"])
            check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ledger_name": ledger_name,
            "stream_arn": stream_arn,
            "stream_id": stream_id,
        }

    @builtins.property
    def ledger_name(self) -> builtins.str:
        '''The LedgerName of the Stream resource.'''
        result = self._values.get("ledger_name")
        assert result is not None, "Required property 'ledger_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_arn(self) -> builtins.str:
        '''The ARN of the Stream resource.'''
        result = self._values.get("stream_arn")
        assert result is not None, "Required property 'stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stream_id(self) -> builtins.str:
        '''The Id of the Stream resource.'''
        result = self._values.get("stream_id")
        assert result is not None, "Required property 'stream_id' is missing"
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
    "ILedgerRef",
    "IStreamRef",
    "LedgerReference",
    "StreamReference",
]

publication.publish()

def _typecheckingstub__4d35dfa03f6a65253d6030611d9debe504406dc352632c923d7dd27060c29db3(
    *,
    ledger_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f3daacfed0da29e06d565867ef84aa514dbf53a1939364d24334cb876768614(
    *,
    ledger_name: builtins.str,
    stream_arn: builtins.str,
    stream_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ILedgerRef, IStreamRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
