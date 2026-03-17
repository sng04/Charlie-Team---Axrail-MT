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
    jsii_type="aws-cdk-lib.interfaces.aws_config.AggregationAuthorizationReference",
    jsii_struct_bases=[],
    name_mapping={
        "aggregation_authorization_arn": "aggregationAuthorizationArn",
        "authorized_account_id": "authorizedAccountId",
        "authorized_aws_region": "authorizedAwsRegion",
    },
)
class AggregationAuthorizationReference:
    def __init__(
        self,
        *,
        aggregation_authorization_arn: builtins.str,
        authorized_account_id: builtins.str,
        authorized_aws_region: builtins.str,
    ) -> None:
        '''A reference to a AggregationAuthorization resource.

        :param aggregation_authorization_arn: The ARN of the AggregationAuthorization resource.
        :param authorized_account_id: The AuthorizedAccountId of the AggregationAuthorization resource.
        :param authorized_aws_region: The AuthorizedAwsRegion of the AggregationAuthorization resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_config as interfaces_config
            
            aggregation_authorization_reference = interfaces_config.AggregationAuthorizationReference(
                aggregation_authorization_arn="aggregationAuthorizationArn",
                authorized_account_id="authorizedAccountId",
                authorized_aws_region="authorizedAwsRegion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f475612b63168745aeaf0d7324ecb1c67eeb25f65b3d360fecc77d49f8706e41)
            check_type(argname="argument aggregation_authorization_arn", value=aggregation_authorization_arn, expected_type=type_hints["aggregation_authorization_arn"])
            check_type(argname="argument authorized_account_id", value=authorized_account_id, expected_type=type_hints["authorized_account_id"])
            check_type(argname="argument authorized_aws_region", value=authorized_aws_region, expected_type=type_hints["authorized_aws_region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aggregation_authorization_arn": aggregation_authorization_arn,
            "authorized_account_id": authorized_account_id,
            "authorized_aws_region": authorized_aws_region,
        }

    @builtins.property
    def aggregation_authorization_arn(self) -> builtins.str:
        '''The ARN of the AggregationAuthorization resource.'''
        result = self._values.get("aggregation_authorization_arn")
        assert result is not None, "Required property 'aggregation_authorization_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorized_account_id(self) -> builtins.str:
        '''The AuthorizedAccountId of the AggregationAuthorization resource.'''
        result = self._values.get("authorized_account_id")
        assert result is not None, "Required property 'authorized_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorized_aws_region(self) -> builtins.str:
        '''The AuthorizedAwsRegion of the AggregationAuthorization resource.'''
        result = self._values.get("authorized_aws_region")
        assert result is not None, "Required property 'authorized_aws_region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AggregationAuthorizationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_config.ConfigRuleReference",
    jsii_struct_bases=[],
    name_mapping={
        "config_rule_arn": "configRuleArn",
        "config_rule_name": "configRuleName",
    },
)
class ConfigRuleReference:
    def __init__(
        self,
        *,
        config_rule_arn: builtins.str,
        config_rule_name: builtins.str,
    ) -> None:
        '''A reference to a ConfigRule resource.

        :param config_rule_arn: The ARN of the ConfigRule resource.
        :param config_rule_name: The ConfigRuleName of the ConfigRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_config as interfaces_config
            
            config_rule_reference = interfaces_config.ConfigRuleReference(
                config_rule_arn="configRuleArn",
                config_rule_name="configRuleName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7bcc26b81961a1ca16b6a6b27418661f3859ae5eee0d9c655d69641ad34ebe0)
            check_type(argname="argument config_rule_arn", value=config_rule_arn, expected_type=type_hints["config_rule_arn"])
            check_type(argname="argument config_rule_name", value=config_rule_name, expected_type=type_hints["config_rule_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_rule_arn": config_rule_arn,
            "config_rule_name": config_rule_name,
        }

    @builtins.property
    def config_rule_arn(self) -> builtins.str:
        '''The ARN of the ConfigRule resource.'''
        result = self._values.get("config_rule_arn")
        assert result is not None, "Required property 'config_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config_rule_name(self) -> builtins.str:
        '''The ConfigRuleName of the ConfigRule resource.'''
        result = self._values.get("config_rule_name")
        assert result is not None, "Required property 'config_rule_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_config.ConfigurationAggregatorReference",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_aggregator_arn": "configurationAggregatorArn",
        "configuration_aggregator_name": "configurationAggregatorName",
    },
)
class ConfigurationAggregatorReference:
    def __init__(
        self,
        *,
        configuration_aggregator_arn: builtins.str,
        configuration_aggregator_name: builtins.str,
    ) -> None:
        '''A reference to a ConfigurationAggregator resource.

        :param configuration_aggregator_arn: The ARN of the ConfigurationAggregator resource.
        :param configuration_aggregator_name: The ConfigurationAggregatorName of the ConfigurationAggregator resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_config as interfaces_config
            
            configuration_aggregator_reference = interfaces_config.ConfigurationAggregatorReference(
                configuration_aggregator_arn="configurationAggregatorArn",
                configuration_aggregator_name="configurationAggregatorName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4857da1b529671a1a7c545b945a1d22a77f03b0a279d1e47b82b9ac7cde5c7d)
            check_type(argname="argument configuration_aggregator_arn", value=configuration_aggregator_arn, expected_type=type_hints["configuration_aggregator_arn"])
            check_type(argname="argument configuration_aggregator_name", value=configuration_aggregator_name, expected_type=type_hints["configuration_aggregator_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_aggregator_arn": configuration_aggregator_arn,
            "configuration_aggregator_name": configuration_aggregator_name,
        }

    @builtins.property
    def configuration_aggregator_arn(self) -> builtins.str:
        '''The ARN of the ConfigurationAggregator resource.'''
        result = self._values.get("configuration_aggregator_arn")
        assert result is not None, "Required property 'configuration_aggregator_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_aggregator_name(self) -> builtins.str:
        '''The ConfigurationAggregatorName of the ConfigurationAggregator resource.'''
        result = self._values.get("configuration_aggregator_name")
        assert result is not None, "Required property 'configuration_aggregator_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationAggregatorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_config.ConfigurationRecorderReference",
    jsii_struct_bases=[],
    name_mapping={"configuration_recorder_id": "configurationRecorderId"},
)
class ConfigurationRecorderReference:
    def __init__(self, *, configuration_recorder_id: builtins.str) -> None:
        '''A reference to a ConfigurationRecorder resource.

        :param configuration_recorder_id: The Id of the ConfigurationRecorder resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_config as interfaces_config
            
            configuration_recorder_reference = interfaces_config.ConfigurationRecorderReference(
                configuration_recorder_id="configurationRecorderId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63416909aacc16f4b663be48b88e6851d224326d56dfd0b80c8619fd734ddf59)
            check_type(argname="argument configuration_recorder_id", value=configuration_recorder_id, expected_type=type_hints["configuration_recorder_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_recorder_id": configuration_recorder_id,
        }

    @builtins.property
    def configuration_recorder_id(self) -> builtins.str:
        '''The Id of the ConfigurationRecorder resource.'''
        result = self._values.get("configuration_recorder_id")
        assert result is not None, "Required property 'configuration_recorder_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationRecorderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_config.ConformancePackReference",
    jsii_struct_bases=[],
    name_mapping={"conformance_pack_name": "conformancePackName"},
)
class ConformancePackReference:
    def __init__(self, *, conformance_pack_name: builtins.str) -> None:
        '''A reference to a ConformancePack resource.

        :param conformance_pack_name: The ConformancePackName of the ConformancePack resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_config as interfaces_config
            
            conformance_pack_reference = interfaces_config.ConformancePackReference(
                conformance_pack_name="conformancePackName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d9ef7123d37db2269e5cdf462a02624d8d1913289786ec44f2e6bdf362833de)
            check_type(argname="argument conformance_pack_name", value=conformance_pack_name, expected_type=type_hints["conformance_pack_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "conformance_pack_name": conformance_pack_name,
        }

    @builtins.property
    def conformance_pack_name(self) -> builtins.str:
        '''The ConformancePackName of the ConformancePack resource.'''
        result = self._values.get("conformance_pack_name")
        assert result is not None, "Required property 'conformance_pack_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConformancePackReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_config.DeliveryChannelReference",
    jsii_struct_bases=[],
    name_mapping={"delivery_channel_id": "deliveryChannelId"},
)
class DeliveryChannelReference:
    def __init__(self, *, delivery_channel_id: builtins.str) -> None:
        '''A reference to a DeliveryChannel resource.

        :param delivery_channel_id: The Id of the DeliveryChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_config as interfaces_config
            
            delivery_channel_reference = interfaces_config.DeliveryChannelReference(
                delivery_channel_id="deliveryChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__472166aca23b37c534f827dac5b5eac75427b1c455eacd9bbddb8e1b3b7dc081)
            check_type(argname="argument delivery_channel_id", value=delivery_channel_id, expected_type=type_hints["delivery_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delivery_channel_id": delivery_channel_id,
        }

    @builtins.property
    def delivery_channel_id(self) -> builtins.str:
        '''The Id of the DeliveryChannel resource.'''
        result = self._values.get("delivery_channel_id")
        assert result is not None, "Required property 'delivery_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeliveryChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_config.IAggregationAuthorizationRef"
)
class IAggregationAuthorizationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AggregationAuthorization.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aggregationAuthorizationRef")
    def aggregation_authorization_ref(self) -> "AggregationAuthorizationReference":
        '''(experimental) A reference to a AggregationAuthorization resource.

        :stability: experimental
        '''
        ...


class _IAggregationAuthorizationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AggregationAuthorization.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_config.IAggregationAuthorizationRef"

    @builtins.property
    @jsii.member(jsii_name="aggregationAuthorizationRef")
    def aggregation_authorization_ref(self) -> "AggregationAuthorizationReference":
        '''(experimental) A reference to a AggregationAuthorization resource.

        :stability: experimental
        '''
        return typing.cast("AggregationAuthorizationReference", jsii.get(self, "aggregationAuthorizationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAggregationAuthorizationRef).__jsii_proxy_class__ = lambda : _IAggregationAuthorizationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_config.IConfigRuleRef")
class IConfigRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configRuleRef")
    def config_rule_ref(self) -> "ConfigRuleReference":
        '''(experimental) A reference to a ConfigRule resource.

        :stability: experimental
        '''
        ...


class _IConfigRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_config.IConfigRuleRef"

    @builtins.property
    @jsii.member(jsii_name="configRuleRef")
    def config_rule_ref(self) -> "ConfigRuleReference":
        '''(experimental) A reference to a ConfigRule resource.

        :stability: experimental
        '''
        return typing.cast("ConfigRuleReference", jsii.get(self, "configRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigRuleRef).__jsii_proxy_class__ = lambda : _IConfigRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_config.IConfigurationAggregatorRef"
)
class IConfigurationAggregatorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationAggregator.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationAggregatorRef")
    def configuration_aggregator_ref(self) -> "ConfigurationAggregatorReference":
        '''(experimental) A reference to a ConfigurationAggregator resource.

        :stability: experimental
        '''
        ...


class _IConfigurationAggregatorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationAggregator.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_config.IConfigurationAggregatorRef"

    @builtins.property
    @jsii.member(jsii_name="configurationAggregatorRef")
    def configuration_aggregator_ref(self) -> "ConfigurationAggregatorReference":
        '''(experimental) A reference to a ConfigurationAggregator resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationAggregatorReference", jsii.get(self, "configurationAggregatorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationAggregatorRef).__jsii_proxy_class__ = lambda : _IConfigurationAggregatorRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_config.IConfigurationRecorderRef"
)
class IConfigurationRecorderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationRecorder.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationRecorderRef")
    def configuration_recorder_ref(self) -> "ConfigurationRecorderReference":
        '''(experimental) A reference to a ConfigurationRecorder resource.

        :stability: experimental
        '''
        ...


class _IConfigurationRecorderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationRecorder.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_config.IConfigurationRecorderRef"

    @builtins.property
    @jsii.member(jsii_name="configurationRecorderRef")
    def configuration_recorder_ref(self) -> "ConfigurationRecorderReference":
        '''(experimental) A reference to a ConfigurationRecorder resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationRecorderReference", jsii.get(self, "configurationRecorderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationRecorderRef).__jsii_proxy_class__ = lambda : _IConfigurationRecorderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_config.IConformancePackRef")
class IConformancePackRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConformancePack.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="conformancePackRef")
    def conformance_pack_ref(self) -> "ConformancePackReference":
        '''(experimental) A reference to a ConformancePack resource.

        :stability: experimental
        '''
        ...


class _IConformancePackRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConformancePack.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_config.IConformancePackRef"

    @builtins.property
    @jsii.member(jsii_name="conformancePackRef")
    def conformance_pack_ref(self) -> "ConformancePackReference":
        '''(experimental) A reference to a ConformancePack resource.

        :stability: experimental
        '''
        return typing.cast("ConformancePackReference", jsii.get(self, "conformancePackRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConformancePackRef).__jsii_proxy_class__ = lambda : _IConformancePackRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_config.IDeliveryChannelRef")
class IDeliveryChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeliveryChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deliveryChannelRef")
    def delivery_channel_ref(self) -> "DeliveryChannelReference":
        '''(experimental) A reference to a DeliveryChannel resource.

        :stability: experimental
        '''
        ...


class _IDeliveryChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeliveryChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_config.IDeliveryChannelRef"

    @builtins.property
    @jsii.member(jsii_name="deliveryChannelRef")
    def delivery_channel_ref(self) -> "DeliveryChannelReference":
        '''(experimental) A reference to a DeliveryChannel resource.

        :stability: experimental
        '''
        return typing.cast("DeliveryChannelReference", jsii.get(self, "deliveryChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeliveryChannelRef).__jsii_proxy_class__ = lambda : _IDeliveryChannelRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_config.IOrganizationConfigRuleRef"
)
class IOrganizationConfigRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationConfigRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationConfigRuleRef")
    def organization_config_rule_ref(self) -> "OrganizationConfigRuleReference":
        '''(experimental) A reference to a OrganizationConfigRule resource.

        :stability: experimental
        '''
        ...


class _IOrganizationConfigRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationConfigRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_config.IOrganizationConfigRuleRef"

    @builtins.property
    @jsii.member(jsii_name="organizationConfigRuleRef")
    def organization_config_rule_ref(self) -> "OrganizationConfigRuleReference":
        '''(experimental) A reference to a OrganizationConfigRule resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationConfigRuleReference", jsii.get(self, "organizationConfigRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationConfigRuleRef).__jsii_proxy_class__ = lambda : _IOrganizationConfigRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_config.IOrganizationConformancePackRef"
)
class IOrganizationConformancePackRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationConformancePack.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationConformancePackRef")
    def organization_conformance_pack_ref(
        self,
    ) -> "OrganizationConformancePackReference":
        '''(experimental) A reference to a OrganizationConformancePack resource.

        :stability: experimental
        '''
        ...


class _IOrganizationConformancePackRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationConformancePack.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_config.IOrganizationConformancePackRef"

    @builtins.property
    @jsii.member(jsii_name="organizationConformancePackRef")
    def organization_conformance_pack_ref(
        self,
    ) -> "OrganizationConformancePackReference":
        '''(experimental) A reference to a OrganizationConformancePack resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationConformancePackReference", jsii.get(self, "organizationConformancePackRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationConformancePackRef).__jsii_proxy_class__ = lambda : _IOrganizationConformancePackRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_config.IRemediationConfigurationRef"
)
class IRemediationConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RemediationConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="remediationConfigurationRef")
    def remediation_configuration_ref(self) -> "RemediationConfigurationReference":
        '''(experimental) A reference to a RemediationConfiguration resource.

        :stability: experimental
        '''
        ...


class _IRemediationConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RemediationConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_config.IRemediationConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="remediationConfigurationRef")
    def remediation_configuration_ref(self) -> "RemediationConfigurationReference":
        '''(experimental) A reference to a RemediationConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("RemediationConfigurationReference", jsii.get(self, "remediationConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRemediationConfigurationRef).__jsii_proxy_class__ = lambda : _IRemediationConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_config.IStoredQueryRef")
class IStoredQueryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StoredQuery.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="storedQueryRef")
    def stored_query_ref(self) -> "StoredQueryReference":
        '''(experimental) A reference to a StoredQuery resource.

        :stability: experimental
        '''
        ...


class _IStoredQueryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StoredQuery.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_config.IStoredQueryRef"

    @builtins.property
    @jsii.member(jsii_name="storedQueryRef")
    def stored_query_ref(self) -> "StoredQueryReference":
        '''(experimental) A reference to a StoredQuery resource.

        :stability: experimental
        '''
        return typing.cast("StoredQueryReference", jsii.get(self, "storedQueryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStoredQueryRef).__jsii_proxy_class__ = lambda : _IStoredQueryRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_config.OrganizationConfigRuleReference",
    jsii_struct_bases=[],
    name_mapping={"organization_config_rule_id": "organizationConfigRuleId"},
)
class OrganizationConfigRuleReference:
    def __init__(self, *, organization_config_rule_id: builtins.str) -> None:
        '''A reference to a OrganizationConfigRule resource.

        :param organization_config_rule_id: The Id of the OrganizationConfigRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_config as interfaces_config
            
            organization_config_rule_reference = interfaces_config.OrganizationConfigRuleReference(
                organization_config_rule_id="organizationConfigRuleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb822d1d5dc6ff37fc69eed1ccccc256efb622e5273788e4c1abbf28a9278368)
            check_type(argname="argument organization_config_rule_id", value=organization_config_rule_id, expected_type=type_hints["organization_config_rule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "organization_config_rule_id": organization_config_rule_id,
        }

    @builtins.property
    def organization_config_rule_id(self) -> builtins.str:
        '''The Id of the OrganizationConfigRule resource.'''
        result = self._values.get("organization_config_rule_id")
        assert result is not None, "Required property 'organization_config_rule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationConfigRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_config.OrganizationConformancePackReference",
    jsii_struct_bases=[],
    name_mapping={
        "organization_conformance_pack_name": "organizationConformancePackName",
    },
)
class OrganizationConformancePackReference:
    def __init__(self, *, organization_conformance_pack_name: builtins.str) -> None:
        '''A reference to a OrganizationConformancePack resource.

        :param organization_conformance_pack_name: The OrganizationConformancePackName of the OrganizationConformancePack resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_config as interfaces_config
            
            organization_conformance_pack_reference = interfaces_config.OrganizationConformancePackReference(
                organization_conformance_pack_name="organizationConformancePackName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5daef4318559c53f3db81583c1922e04cf23be4f5e212436f0518974f39373fa)
            check_type(argname="argument organization_conformance_pack_name", value=organization_conformance_pack_name, expected_type=type_hints["organization_conformance_pack_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "organization_conformance_pack_name": organization_conformance_pack_name,
        }

    @builtins.property
    def organization_conformance_pack_name(self) -> builtins.str:
        '''The OrganizationConformancePackName of the OrganizationConformancePack resource.'''
        result = self._values.get("organization_conformance_pack_name")
        assert result is not None, "Required property 'organization_conformance_pack_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationConformancePackReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_config.RemediationConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"remediation_configuration_id": "remediationConfigurationId"},
)
class RemediationConfigurationReference:
    def __init__(self, *, remediation_configuration_id: builtins.str) -> None:
        '''A reference to a RemediationConfiguration resource.

        :param remediation_configuration_id: The Id of the RemediationConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_config as interfaces_config
            
            remediation_configuration_reference = interfaces_config.RemediationConfigurationReference(
                remediation_configuration_id="remediationConfigurationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aa8b82b87534836247bd222bc3affa2d1dbc927e8eef996b059f116a6d32def)
            check_type(argname="argument remediation_configuration_id", value=remediation_configuration_id, expected_type=type_hints["remediation_configuration_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "remediation_configuration_id": remediation_configuration_id,
        }

    @builtins.property
    def remediation_configuration_id(self) -> builtins.str:
        '''The Id of the RemediationConfiguration resource.'''
        result = self._values.get("remediation_configuration_id")
        assert result is not None, "Required property 'remediation_configuration_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RemediationConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_config.StoredQueryReference",
    jsii_struct_bases=[],
    name_mapping={"query_name": "queryName"},
)
class StoredQueryReference:
    def __init__(self, *, query_name: builtins.str) -> None:
        '''A reference to a StoredQuery resource.

        :param query_name: The QueryName of the StoredQuery resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_config as interfaces_config
            
            stored_query_reference = interfaces_config.StoredQueryReference(
                query_name="queryName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c93366677a5cf67294d183ffdb934354d0e522169238280163adf19f524e71af)
            check_type(argname="argument query_name", value=query_name, expected_type=type_hints["query_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "query_name": query_name,
        }

    @builtins.property
    def query_name(self) -> builtins.str:
        '''The QueryName of the StoredQuery resource.'''
        result = self._values.get("query_name")
        assert result is not None, "Required property 'query_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StoredQueryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AggregationAuthorizationReference",
    "ConfigRuleReference",
    "ConfigurationAggregatorReference",
    "ConfigurationRecorderReference",
    "ConformancePackReference",
    "DeliveryChannelReference",
    "IAggregationAuthorizationRef",
    "IConfigRuleRef",
    "IConfigurationAggregatorRef",
    "IConfigurationRecorderRef",
    "IConformancePackRef",
    "IDeliveryChannelRef",
    "IOrganizationConfigRuleRef",
    "IOrganizationConformancePackRef",
    "IRemediationConfigurationRef",
    "IStoredQueryRef",
    "OrganizationConfigRuleReference",
    "OrganizationConformancePackReference",
    "RemediationConfigurationReference",
    "StoredQueryReference",
]

publication.publish()

def _typecheckingstub__f475612b63168745aeaf0d7324ecb1c67eeb25f65b3d360fecc77d49f8706e41(
    *,
    aggregation_authorization_arn: builtins.str,
    authorized_account_id: builtins.str,
    authorized_aws_region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7bcc26b81961a1ca16b6a6b27418661f3859ae5eee0d9c655d69641ad34ebe0(
    *,
    config_rule_arn: builtins.str,
    config_rule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4857da1b529671a1a7c545b945a1d22a77f03b0a279d1e47b82b9ac7cde5c7d(
    *,
    configuration_aggregator_arn: builtins.str,
    configuration_aggregator_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63416909aacc16f4b663be48b88e6851d224326d56dfd0b80c8619fd734ddf59(
    *,
    configuration_recorder_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d9ef7123d37db2269e5cdf462a02624d8d1913289786ec44f2e6bdf362833de(
    *,
    conformance_pack_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__472166aca23b37c534f827dac5b5eac75427b1c455eacd9bbddb8e1b3b7dc081(
    *,
    delivery_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb822d1d5dc6ff37fc69eed1ccccc256efb622e5273788e4c1abbf28a9278368(
    *,
    organization_config_rule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5daef4318559c53f3db81583c1922e04cf23be4f5e212436f0518974f39373fa(
    *,
    organization_conformance_pack_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa8b82b87534836247bd222bc3affa2d1dbc927e8eef996b059f116a6d32def(
    *,
    remediation_configuration_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c93366677a5cf67294d183ffdb934354d0e522169238280163adf19f524e71af(
    *,
    query_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAggregationAuthorizationRef, IConfigRuleRef, IConfigurationAggregatorRef, IConfigurationRecorderRef, IConformancePackRef, IDeliveryChannelRef, IOrganizationConfigRuleRef, IOrganizationConformancePackRef, IRemediationConfigurationRef, IStoredQueryRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
