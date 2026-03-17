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
    jsii_type="aws-cdk-lib.interfaces.aws_amazonmq.BrokerReference",
    jsii_struct_bases=[],
    name_mapping={"broker_arn": "brokerArn", "broker_id": "brokerId"},
)
class BrokerReference:
    def __init__(self, *, broker_arn: builtins.str, broker_id: builtins.str) -> None:
        '''A reference to a Broker resource.

        :param broker_arn: The ARN of the Broker resource.
        :param broker_id: The Id of the Broker resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_amazonmq as interfaces_amazonmq
            
            broker_reference = interfaces_amazonmq.BrokerReference(
                broker_arn="brokerArn",
                broker_id="brokerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7d08349f61fc490387b85ccf5a6eb11eb8a3d49c1f4ba826886363e86a23921)
            check_type(argname="argument broker_arn", value=broker_arn, expected_type=type_hints["broker_arn"])
            check_type(argname="argument broker_id", value=broker_id, expected_type=type_hints["broker_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "broker_arn": broker_arn,
            "broker_id": broker_id,
        }

    @builtins.property
    def broker_arn(self) -> builtins.str:
        '''The ARN of the Broker resource.'''
        result = self._values.get("broker_arn")
        assert result is not None, "Required property 'broker_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def broker_id(self) -> builtins.str:
        '''The Id of the Broker resource.'''
        result = self._values.get("broker_id")
        assert result is not None, "Required property 'broker_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BrokerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_amazonmq.ConfigurationAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"configuration_association_id": "configurationAssociationId"},
)
class ConfigurationAssociationReference:
    def __init__(self, *, configuration_association_id: builtins.str) -> None:
        '''A reference to a ConfigurationAssociation resource.

        :param configuration_association_id: The Id of the ConfigurationAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_amazonmq as interfaces_amazonmq
            
            configuration_association_reference = interfaces_amazonmq.ConfigurationAssociationReference(
                configuration_association_id="configurationAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70bf962895c64c8a2e129db032a13df81d4e347faf07b4624eb97b9c35103c9e)
            check_type(argname="argument configuration_association_id", value=configuration_association_id, expected_type=type_hints["configuration_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_association_id": configuration_association_id,
        }

    @builtins.property
    def configuration_association_id(self) -> builtins.str:
        '''The Id of the ConfigurationAssociation resource.'''
        result = self._values.get("configuration_association_id")
        assert result is not None, "Required property 'configuration_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_amazonmq.ConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_arn": "configurationArn",
        "configuration_id": "configurationId",
    },
)
class ConfigurationReference:
    def __init__(
        self,
        *,
        configuration_arn: builtins.str,
        configuration_id: builtins.str,
    ) -> None:
        '''A reference to a Configuration resource.

        :param configuration_arn: The ARN of the Configuration resource.
        :param configuration_id: The Id of the Configuration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_amazonmq as interfaces_amazonmq
            
            configuration_reference = interfaces_amazonmq.ConfigurationReference(
                configuration_arn="configurationArn",
                configuration_id="configurationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8917d10bff03fbb5e9fa4d782baed352b8ca363bfbeaeb9e2263ec9859fd491)
            check_type(argname="argument configuration_arn", value=configuration_arn, expected_type=type_hints["configuration_arn"])
            check_type(argname="argument configuration_id", value=configuration_id, expected_type=type_hints["configuration_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_arn": configuration_arn,
            "configuration_id": configuration_id,
        }

    @builtins.property
    def configuration_arn(self) -> builtins.str:
        '''The ARN of the Configuration resource.'''
        result = self._values.get("configuration_arn")
        assert result is not None, "Required property 'configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_id(self) -> builtins.str:
        '''The Id of the Configuration resource.'''
        result = self._values.get("configuration_id")
        assert result is not None, "Required property 'configuration_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_amazonmq.IBrokerRef")
class IBrokerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Broker.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="brokerRef")
    def broker_ref(self) -> "BrokerReference":
        '''(experimental) A reference to a Broker resource.

        :stability: experimental
        '''
        ...


class _IBrokerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Broker.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_amazonmq.IBrokerRef"

    @builtins.property
    @jsii.member(jsii_name="brokerRef")
    def broker_ref(self) -> "BrokerReference":
        '''(experimental) A reference to a Broker resource.

        :stability: experimental
        '''
        return typing.cast("BrokerReference", jsii.get(self, "brokerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBrokerRef).__jsii_proxy_class__ = lambda : _IBrokerRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_amazonmq.IConfigurationAssociationRef"
)
class IConfigurationAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationAssociationRef")
    def configuration_association_ref(self) -> "ConfigurationAssociationReference":
        '''(experimental) A reference to a ConfigurationAssociation resource.

        :stability: experimental
        '''
        ...


class _IConfigurationAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_amazonmq.IConfigurationAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="configurationAssociationRef")
    def configuration_association_ref(self) -> "ConfigurationAssociationReference":
        '''(experimental) A reference to a ConfigurationAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationAssociationReference", jsii.get(self, "configurationAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationAssociationRef).__jsii_proxy_class__ = lambda : _IConfigurationAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_amazonmq.IConfigurationRef")
class IConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Configuration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationRef")
    def configuration_ref(self) -> "ConfigurationReference":
        '''(experimental) A reference to a Configuration resource.

        :stability: experimental
        '''
        ...


class _IConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Configuration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_amazonmq.IConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="configurationRef")
    def configuration_ref(self) -> "ConfigurationReference":
        '''(experimental) A reference to a Configuration resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationReference", jsii.get(self, "configurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationRef).__jsii_proxy_class__ = lambda : _IConfigurationRefProxy


__all__ = [
    "BrokerReference",
    "ConfigurationAssociationReference",
    "ConfigurationReference",
    "IBrokerRef",
    "IConfigurationAssociationRef",
    "IConfigurationRef",
]

publication.publish()

def _typecheckingstub__e7d08349f61fc490387b85ccf5a6eb11eb8a3d49c1f4ba826886363e86a23921(
    *,
    broker_arn: builtins.str,
    broker_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70bf962895c64c8a2e129db032a13df81d4e347faf07b4624eb97b9c35103c9e(
    *,
    configuration_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8917d10bff03fbb5e9fa4d782baed352b8ca363bfbeaeb9e2263ec9859fd491(
    *,
    configuration_arn: builtins.str,
    configuration_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBrokerRef, IConfigurationAssociationRef, IConfigurationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
