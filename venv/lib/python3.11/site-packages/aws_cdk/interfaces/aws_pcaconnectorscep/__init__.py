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
    jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorscep.ChallengeReference",
    jsii_struct_bases=[],
    name_mapping={"challenge_arn": "challengeArn"},
)
class ChallengeReference:
    def __init__(self, *, challenge_arn: builtins.str) -> None:
        '''A reference to a Challenge resource.

        :param challenge_arn: The ChallengeArn of the Challenge resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pcaconnectorscep as interfaces_pcaconnectorscep
            
            challenge_reference = interfaces_pcaconnectorscep.ChallengeReference(
                challenge_arn="challengeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f42f3eded91548c5cdf6356bdbb15dc2560cdc2a1771659684ac1fa382f9f1fb)
            check_type(argname="argument challenge_arn", value=challenge_arn, expected_type=type_hints["challenge_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "challenge_arn": challenge_arn,
        }

    @builtins.property
    def challenge_arn(self) -> builtins.str:
        '''The ChallengeArn of the Challenge resource.'''
        result = self._values.get("challenge_arn")
        assert result is not None, "Required property 'challenge_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChallengeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorscep.ConnectorReference",
    jsii_struct_bases=[],
    name_mapping={"connector_arn": "connectorArn"},
)
class ConnectorReference:
    def __init__(self, *, connector_arn: builtins.str) -> None:
        '''A reference to a Connector resource.

        :param connector_arn: The ConnectorArn of the Connector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pcaconnectorscep as interfaces_pcaconnectorscep
            
            connector_reference = interfaces_pcaconnectorscep.ConnectorReference(
                connector_arn="connectorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1486192b1d2e48e8a3a7c89fff86f9653db0e71de2ca530880d5b6ed21a6017d)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
        }

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The ConnectorArn of the Connector resource.'''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorscep.IChallengeRef")
class IChallengeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Challenge.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="challengeRef")
    def challenge_ref(self) -> "ChallengeReference":
        '''(experimental) A reference to a Challenge resource.

        :stability: experimental
        '''
        ...


class _IChallengeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Challenge.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pcaconnectorscep.IChallengeRef"

    @builtins.property
    @jsii.member(jsii_name="challengeRef")
    def challenge_ref(self) -> "ChallengeReference":
        '''(experimental) A reference to a Challenge resource.

        :stability: experimental
        '''
        return typing.cast("ChallengeReference", jsii.get(self, "challengeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChallengeRef).__jsii_proxy_class__ = lambda : _IChallengeRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pcaconnectorscep.IConnectorRef")
class IConnectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        ...


class _IConnectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pcaconnectorscep.IConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorReference", jsii.get(self, "connectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorRef).__jsii_proxy_class__ = lambda : _IConnectorRefProxy


__all__ = [
    "ChallengeReference",
    "ConnectorReference",
    "IChallengeRef",
    "IConnectorRef",
]

publication.publish()

def _typecheckingstub__f42f3eded91548c5cdf6356bdbb15dc2560cdc2a1771659684ac1fa382f9f1fb(
    *,
    challenge_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1486192b1d2e48e8a3a7c89fff86f9653db0e71de2ca530880d5b6ed21a6017d(
    *,
    connector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IChallengeRef, IConnectorRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
