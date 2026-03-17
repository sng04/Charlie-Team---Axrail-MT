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
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.AggregatorV2Reference",
    jsii_struct_bases=[],
    name_mapping={"aggregator_v2_arn": "aggregatorV2Arn"},
)
class AggregatorV2Reference:
    def __init__(self, *, aggregator_v2_arn: builtins.str) -> None:
        '''A reference to a AggregatorV2 resource.

        :param aggregator_v2_arn: The AggregatorV2Arn of the AggregatorV2 resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            aggregator_v2_reference = interfaces_securityhub.AggregatorV2Reference(
                aggregator_v2_arn="aggregatorV2Arn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35a220db7509efb96c8abd58d83c974df0d1ec6221841ce0031c7e29166870a6)
            check_type(argname="argument aggregator_v2_arn", value=aggregator_v2_arn, expected_type=type_hints["aggregator_v2_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aggregator_v2_arn": aggregator_v2_arn,
        }

    @builtins.property
    def aggregator_v2_arn(self) -> builtins.str:
        '''The AggregatorV2Arn of the AggregatorV2 resource.'''
        result = self._values.get("aggregator_v2_arn")
        assert result is not None, "Required property 'aggregator_v2_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AggregatorV2Reference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.AutomationRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class AutomationRuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a AutomationRule resource.

        :param rule_arn: The RuleArn of the AutomationRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            automation_rule_reference = interfaces_securityhub.AutomationRuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fc12b37b5b474e26a7ab22d75e02c9702e3dccd822e93295efe42823eb6e5bf)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleArn of the AutomationRule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutomationRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.AutomationRuleV2Reference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class AutomationRuleV2Reference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a AutomationRuleV2 resource.

        :param rule_arn: The RuleArn of the AutomationRuleV2 resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            automation_rule_v2_reference = interfaces_securityhub.AutomationRuleV2Reference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aef4997ae46bca6cfa7dd6194511cb0c8e4c744827ab27202ec5bf7628e5b6e8)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleArn of the AutomationRuleV2 resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutomationRuleV2Reference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.ConfigurationPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"configuration_policy_arn": "configurationPolicyArn"},
)
class ConfigurationPolicyReference:
    def __init__(self, *, configuration_policy_arn: builtins.str) -> None:
        '''A reference to a ConfigurationPolicy resource.

        :param configuration_policy_arn: The Arn of the ConfigurationPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            configuration_policy_reference = interfaces_securityhub.ConfigurationPolicyReference(
                configuration_policy_arn="configurationPolicyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4bf6c068777f6837cd16457e25121201ab0e5a04344d176fc401dc42df6811)
            check_type(argname="argument configuration_policy_arn", value=configuration_policy_arn, expected_type=type_hints["configuration_policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_policy_arn": configuration_policy_arn,
        }

    @builtins.property
    def configuration_policy_arn(self) -> builtins.str:
        '''The Arn of the ConfigurationPolicy resource.'''
        result = self._values.get("configuration_policy_arn")
        assert result is not None, "Required property 'configuration_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.ConnectorV2Reference",
    jsii_struct_bases=[],
    name_mapping={"connector_arn": "connectorArn"},
)
class ConnectorV2Reference:
    def __init__(self, *, connector_arn: builtins.str) -> None:
        '''A reference to a ConnectorV2 resource.

        :param connector_arn: The ConnectorArn of the ConnectorV2 resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            connector_v2_reference = interfaces_securityhub.ConnectorV2Reference(
                connector_arn="connectorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87f9de0b840b9c41998aae229688e8a483801310a2dadbbcf7777f01d538ebb1)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
        }

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The ConnectorArn of the ConnectorV2 resource.'''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorV2Reference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.DelegatedAdminReference",
    jsii_struct_bases=[],
    name_mapping={"delegated_admin_identifier": "delegatedAdminIdentifier"},
)
class DelegatedAdminReference:
    def __init__(self, *, delegated_admin_identifier: builtins.str) -> None:
        '''A reference to a DelegatedAdmin resource.

        :param delegated_admin_identifier: The DelegatedAdminIdentifier of the DelegatedAdmin resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            delegated_admin_reference = interfaces_securityhub.DelegatedAdminReference(
                delegated_admin_identifier="delegatedAdminIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02fcb283a9643cdb1e80efe749afc53bd727fa2a227498840453efc18e4d0b32)
            check_type(argname="argument delegated_admin_identifier", value=delegated_admin_identifier, expected_type=type_hints["delegated_admin_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delegated_admin_identifier": delegated_admin_identifier,
        }

    @builtins.property
    def delegated_admin_identifier(self) -> builtins.str:
        '''The DelegatedAdminIdentifier of the DelegatedAdmin resource.'''
        result = self._values.get("delegated_admin_identifier")
        assert result is not None, "Required property 'delegated_admin_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DelegatedAdminReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.FindingAggregatorReference",
    jsii_struct_bases=[],
    name_mapping={"finding_aggregator_arn": "findingAggregatorArn"},
)
class FindingAggregatorReference:
    def __init__(self, *, finding_aggregator_arn: builtins.str) -> None:
        '''A reference to a FindingAggregator resource.

        :param finding_aggregator_arn: The FindingAggregatorArn of the FindingAggregator resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            finding_aggregator_reference = interfaces_securityhub.FindingAggregatorReference(
                finding_aggregator_arn="findingAggregatorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8d6cf95ba857b951122e47526fc001b1f55ba2dc693a043cb41135baa3cfdc9)
            check_type(argname="argument finding_aggregator_arn", value=finding_aggregator_arn, expected_type=type_hints["finding_aggregator_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "finding_aggregator_arn": finding_aggregator_arn,
        }

    @builtins.property
    def finding_aggregator_arn(self) -> builtins.str:
        '''The FindingAggregatorArn of the FindingAggregator resource.'''
        result = self._values.get("finding_aggregator_arn")
        assert result is not None, "Required property 'finding_aggregator_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FindingAggregatorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.HubReference",
    jsii_struct_bases=[],
    name_mapping={"hub_arn": "hubArn"},
)
class HubReference:
    def __init__(self, *, hub_arn: builtins.str) -> None:
        '''A reference to a Hub resource.

        :param hub_arn: The ARN of the Hub resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            hub_reference = interfaces_securityhub.HubReference(
                hub_arn="hubArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64fd84efb35583fcc0b4b4b1177deb0cf485141b0d3945ccb8a69a000febb7ec)
            check_type(argname="argument hub_arn", value=hub_arn, expected_type=type_hints["hub_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hub_arn": hub_arn,
        }

    @builtins.property
    def hub_arn(self) -> builtins.str:
        '''The ARN of the Hub resource.'''
        result = self._values.get("hub_arn")
        assert result is not None, "Required property 'hub_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HubReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.HubV2Reference",
    jsii_struct_bases=[],
    name_mapping={"hub_v2_arn": "hubV2Arn"},
)
class HubV2Reference:
    def __init__(self, *, hub_v2_arn: builtins.str) -> None:
        '''A reference to a HubV2 resource.

        :param hub_v2_arn: The HubV2Arn of the HubV2 resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            hub_v2_reference = interfaces_securityhub.HubV2Reference(
                hub_v2_arn="hubV2Arn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a9f49271093222ae0ce6374cb3465f6580021ffb6cb531e479d887c30c358af)
            check_type(argname="argument hub_v2_arn", value=hub_v2_arn, expected_type=type_hints["hub_v2_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hub_v2_arn": hub_v2_arn,
        }

    @builtins.property
    def hub_v2_arn(self) -> builtins.str:
        '''The HubV2Arn of the HubV2 resource.'''
        result = self._values.get("hub_v2_arn")
        assert result is not None, "Required property 'hub_v2_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HubV2Reference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IAggregatorV2Ref")
class IAggregatorV2Ref(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AggregatorV2.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aggregatorV2Ref")
    def aggregator_v2_ref(self) -> "AggregatorV2Reference":
        '''(experimental) A reference to a AggregatorV2 resource.

        :stability: experimental
        '''
        ...


class _IAggregatorV2RefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AggregatorV2.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IAggregatorV2Ref"

    @builtins.property
    @jsii.member(jsii_name="aggregatorV2Ref")
    def aggregator_v2_ref(self) -> "AggregatorV2Reference":
        '''(experimental) A reference to a AggregatorV2 resource.

        :stability: experimental
        '''
        return typing.cast("AggregatorV2Reference", jsii.get(self, "aggregatorV2Ref"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAggregatorV2Ref).__jsii_proxy_class__ = lambda : _IAggregatorV2RefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IAutomationRuleRef")
class IAutomationRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AutomationRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="automationRuleRef")
    def automation_rule_ref(self) -> "AutomationRuleReference":
        '''(experimental) A reference to a AutomationRule resource.

        :stability: experimental
        '''
        ...


class _IAutomationRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AutomationRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IAutomationRuleRef"

    @builtins.property
    @jsii.member(jsii_name="automationRuleRef")
    def automation_rule_ref(self) -> "AutomationRuleReference":
        '''(experimental) A reference to a AutomationRule resource.

        :stability: experimental
        '''
        return typing.cast("AutomationRuleReference", jsii.get(self, "automationRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAutomationRuleRef).__jsii_proxy_class__ = lambda : _IAutomationRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IAutomationRuleV2Ref"
)
class IAutomationRuleV2Ref(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AutomationRuleV2.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="automationRuleV2Ref")
    def automation_rule_v2_ref(self) -> "AutomationRuleV2Reference":
        '''(experimental) A reference to a AutomationRuleV2 resource.

        :stability: experimental
        '''
        ...


class _IAutomationRuleV2RefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AutomationRuleV2.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IAutomationRuleV2Ref"

    @builtins.property
    @jsii.member(jsii_name="automationRuleV2Ref")
    def automation_rule_v2_ref(self) -> "AutomationRuleV2Reference":
        '''(experimental) A reference to a AutomationRuleV2 resource.

        :stability: experimental
        '''
        return typing.cast("AutomationRuleV2Reference", jsii.get(self, "automationRuleV2Ref"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAutomationRuleV2Ref).__jsii_proxy_class__ = lambda : _IAutomationRuleV2RefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IConfigurationPolicyRef"
)
class IConfigurationPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationPolicyRef")
    def configuration_policy_ref(self) -> "ConfigurationPolicyReference":
        '''(experimental) A reference to a ConfigurationPolicy resource.

        :stability: experimental
        '''
        ...


class _IConfigurationPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IConfigurationPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="configurationPolicyRef")
    def configuration_policy_ref(self) -> "ConfigurationPolicyReference":
        '''(experimental) A reference to a ConfigurationPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationPolicyReference", jsii.get(self, "configurationPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationPolicyRef).__jsii_proxy_class__ = lambda : _IConfigurationPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IConnectorV2Ref")
class IConnectorV2Ref(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectorV2.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectorV2Ref")
    def connector_v2_ref(self) -> "ConnectorV2Reference":
        '''(experimental) A reference to a ConnectorV2 resource.

        :stability: experimental
        '''
        ...


class _IConnectorV2RefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectorV2.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IConnectorV2Ref"

    @builtins.property
    @jsii.member(jsii_name="connectorV2Ref")
    def connector_v2_ref(self) -> "ConnectorV2Reference":
        '''(experimental) A reference to a ConnectorV2 resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorV2Reference", jsii.get(self, "connectorV2Ref"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorV2Ref).__jsii_proxy_class__ = lambda : _IConnectorV2RefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IDelegatedAdminRef")
class IDelegatedAdminRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DelegatedAdmin.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="delegatedAdminRef")
    def delegated_admin_ref(self) -> "DelegatedAdminReference":
        '''(experimental) A reference to a DelegatedAdmin resource.

        :stability: experimental
        '''
        ...


class _IDelegatedAdminRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DelegatedAdmin.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IDelegatedAdminRef"

    @builtins.property
    @jsii.member(jsii_name="delegatedAdminRef")
    def delegated_admin_ref(self) -> "DelegatedAdminReference":
        '''(experimental) A reference to a DelegatedAdmin resource.

        :stability: experimental
        '''
        return typing.cast("DelegatedAdminReference", jsii.get(self, "delegatedAdminRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDelegatedAdminRef).__jsii_proxy_class__ = lambda : _IDelegatedAdminRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IFindingAggregatorRef"
)
class IFindingAggregatorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FindingAggregator.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="findingAggregatorRef")
    def finding_aggregator_ref(self) -> "FindingAggregatorReference":
        '''(experimental) A reference to a FindingAggregator resource.

        :stability: experimental
        '''
        ...


class _IFindingAggregatorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FindingAggregator.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IFindingAggregatorRef"

    @builtins.property
    @jsii.member(jsii_name="findingAggregatorRef")
    def finding_aggregator_ref(self) -> "FindingAggregatorReference":
        '''(experimental) A reference to a FindingAggregator resource.

        :stability: experimental
        '''
        return typing.cast("FindingAggregatorReference", jsii.get(self, "findingAggregatorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFindingAggregatorRef).__jsii_proxy_class__ = lambda : _IFindingAggregatorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IHubRef")
class IHubRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Hub.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hubRef")
    def hub_ref(self) -> "HubReference":
        '''(experimental) A reference to a Hub resource.

        :stability: experimental
        '''
        ...


class _IHubRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Hub.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IHubRef"

    @builtins.property
    @jsii.member(jsii_name="hubRef")
    def hub_ref(self) -> "HubReference":
        '''(experimental) A reference to a Hub resource.

        :stability: experimental
        '''
        return typing.cast("HubReference", jsii.get(self, "hubRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHubRef).__jsii_proxy_class__ = lambda : _IHubRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IHubV2Ref")
class IHubV2Ref(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HubV2.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hubV2Ref")
    def hub_v2_ref(self) -> "HubV2Reference":
        '''(experimental) A reference to a HubV2 resource.

        :stability: experimental
        '''
        ...


class _IHubV2RefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HubV2.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IHubV2Ref"

    @builtins.property
    @jsii.member(jsii_name="hubV2Ref")
    def hub_v2_ref(self) -> "HubV2Reference":
        '''(experimental) A reference to a HubV2 resource.

        :stability: experimental
        '''
        return typing.cast("HubV2Reference", jsii.get(self, "hubV2Ref"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHubV2Ref).__jsii_proxy_class__ = lambda : _IHubV2RefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IInsightRef")
class IInsightRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Insight.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="insightRef")
    def insight_ref(self) -> "InsightReference":
        '''(experimental) A reference to a Insight resource.

        :stability: experimental
        '''
        ...


class _IInsightRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Insight.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IInsightRef"

    @builtins.property
    @jsii.member(jsii_name="insightRef")
    def insight_ref(self) -> "InsightReference":
        '''(experimental) A reference to a Insight resource.

        :stability: experimental
        '''
        return typing.cast("InsightReference", jsii.get(self, "insightRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInsightRef).__jsii_proxy_class__ = lambda : _IInsightRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IOrganizationConfigurationRef"
)
class IOrganizationConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationConfigurationRef")
    def organization_configuration_ref(self) -> "OrganizationConfigurationReference":
        '''(experimental) A reference to a OrganizationConfiguration resource.

        :stability: experimental
        '''
        ...


class _IOrganizationConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IOrganizationConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="organizationConfigurationRef")
    def organization_configuration_ref(self) -> "OrganizationConfigurationReference":
        '''(experimental) A reference to a OrganizationConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationConfigurationReference", jsii.get(self, "organizationConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationConfigurationRef).__jsii_proxy_class__ = lambda : _IOrganizationConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IPolicyAssociationRef"
)
class IPolicyAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="policyAssociationRef")
    def policy_association_ref(self) -> "PolicyAssociationReference":
        '''(experimental) A reference to a PolicyAssociation resource.

        :stability: experimental
        '''
        ...


class _IPolicyAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IPolicyAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="policyAssociationRef")
    def policy_association_ref(self) -> "PolicyAssociationReference":
        '''(experimental) A reference to a PolicyAssociation resource.

        :stability: experimental
        '''
        return typing.cast("PolicyAssociationReference", jsii.get(self, "policyAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyAssociationRef).__jsii_proxy_class__ = lambda : _IPolicyAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IProductSubscriptionRef"
)
class IProductSubscriptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProductSubscription.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="productSubscriptionRef")
    def product_subscription_ref(self) -> "ProductSubscriptionReference":
        '''(experimental) A reference to a ProductSubscription resource.

        :stability: experimental
        '''
        ...


class _IProductSubscriptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProductSubscription.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IProductSubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="productSubscriptionRef")
    def product_subscription_ref(self) -> "ProductSubscriptionReference":
        '''(experimental) A reference to a ProductSubscription resource.

        :stability: experimental
        '''
        return typing.cast("ProductSubscriptionReference", jsii.get(self, "productSubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProductSubscriptionRef).__jsii_proxy_class__ = lambda : _IProductSubscriptionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityhub.ISecurityControlRef")
class ISecurityControlRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityControl.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityControlRef")
    def security_control_ref(self) -> "SecurityControlReference":
        '''(experimental) A reference to a SecurityControl resource.

        :stability: experimental
        '''
        ...


class _ISecurityControlRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityControl.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.ISecurityControlRef"

    @builtins.property
    @jsii.member(jsii_name="securityControlRef")
    def security_control_ref(self) -> "SecurityControlReference":
        '''(experimental) A reference to a SecurityControl resource.

        :stability: experimental
        '''
        return typing.cast("SecurityControlReference", jsii.get(self, "securityControlRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityControlRef).__jsii_proxy_class__ = lambda : _ISecurityControlRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_securityhub.IStandardRef")
class IStandardRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Standard.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="standardRef")
    def standard_ref(self) -> "StandardReference":
        '''(experimental) A reference to a Standard resource.

        :stability: experimental
        '''
        ...


class _IStandardRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Standard.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_securityhub.IStandardRef"

    @builtins.property
    @jsii.member(jsii_name="standardRef")
    def standard_ref(self) -> "StandardReference":
        '''(experimental) A reference to a Standard resource.

        :stability: experimental
        '''
        return typing.cast("StandardReference", jsii.get(self, "standardRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStandardRef).__jsii_proxy_class__ = lambda : _IStandardRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.InsightReference",
    jsii_struct_bases=[],
    name_mapping={"insight_arn": "insightArn"},
)
class InsightReference:
    def __init__(self, *, insight_arn: builtins.str) -> None:
        '''A reference to a Insight resource.

        :param insight_arn: The InsightArn of the Insight resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            insight_reference = interfaces_securityhub.InsightReference(
                insight_arn="insightArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0458c101ffc14948dabba2554b5917f46d43912d82bfaa6a51dcca94609e8d40)
            check_type(argname="argument insight_arn", value=insight_arn, expected_type=type_hints["insight_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "insight_arn": insight_arn,
        }

    @builtins.property
    def insight_arn(self) -> builtins.str:
        '''The InsightArn of the Insight resource.'''
        result = self._values.get("insight_arn")
        assert result is not None, "Required property 'insight_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InsightReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.OrganizationConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "organization_configuration_identifier": "organizationConfigurationIdentifier",
    },
)
class OrganizationConfigurationReference:
    def __init__(self, *, organization_configuration_identifier: builtins.str) -> None:
        '''A reference to a OrganizationConfiguration resource.

        :param organization_configuration_identifier: The OrganizationConfigurationIdentifier of the OrganizationConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            organization_configuration_reference = interfaces_securityhub.OrganizationConfigurationReference(
                organization_configuration_identifier="organizationConfigurationIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e68192f516aaa64f02830db5695b88046d18593c6a5693c3c8aec0f225a6be1)
            check_type(argname="argument organization_configuration_identifier", value=organization_configuration_identifier, expected_type=type_hints["organization_configuration_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "organization_configuration_identifier": organization_configuration_identifier,
        }

    @builtins.property
    def organization_configuration_identifier(self) -> builtins.str:
        '''The OrganizationConfigurationIdentifier of the OrganizationConfiguration resource.'''
        result = self._values.get("organization_configuration_identifier")
        assert result is not None, "Required property 'organization_configuration_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.PolicyAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"association_identifier": "associationIdentifier"},
)
class PolicyAssociationReference:
    def __init__(self, *, association_identifier: builtins.str) -> None:
        '''A reference to a PolicyAssociation resource.

        :param association_identifier: The AssociationIdentifier of the PolicyAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            policy_association_reference = interfaces_securityhub.PolicyAssociationReference(
                association_identifier="associationIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e0a6ff2ea35ae8bb02106e26430281b639559a6f3d415ea2feb07cfb1b0edb)
            check_type(argname="argument association_identifier", value=association_identifier, expected_type=type_hints["association_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_identifier": association_identifier,
        }

    @builtins.property
    def association_identifier(self) -> builtins.str:
        '''The AssociationIdentifier of the PolicyAssociation resource.'''
        result = self._values.get("association_identifier")
        assert result is not None, "Required property 'association_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.ProductSubscriptionReference",
    jsii_struct_bases=[],
    name_mapping={"product_subscription_arn": "productSubscriptionArn"},
)
class ProductSubscriptionReference:
    def __init__(self, *, product_subscription_arn: builtins.str) -> None:
        '''A reference to a ProductSubscription resource.

        :param product_subscription_arn: The ProductSubscriptionArn of the ProductSubscription resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            product_subscription_reference = interfaces_securityhub.ProductSubscriptionReference(
                product_subscription_arn="productSubscriptionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4f1213ac1e04edaababb0118ef15710338e2f048be32080871c4e3703f095c2)
            check_type(argname="argument product_subscription_arn", value=product_subscription_arn, expected_type=type_hints["product_subscription_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "product_subscription_arn": product_subscription_arn,
        }

    @builtins.property
    def product_subscription_arn(self) -> builtins.str:
        '''The ProductSubscriptionArn of the ProductSubscription resource.'''
        result = self._values.get("product_subscription_arn")
        assert result is not None, "Required property 'product_subscription_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProductSubscriptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.SecurityControlReference",
    jsii_struct_bases=[],
    name_mapping={"security_control_id": "securityControlId"},
)
class SecurityControlReference:
    def __init__(self, *, security_control_id: builtins.str) -> None:
        '''A reference to a SecurityControl resource.

        :param security_control_id: The SecurityControlId of the SecurityControl resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            security_control_reference = interfaces_securityhub.SecurityControlReference(
                security_control_id="securityControlId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__171752d544f357353cc747f6a154ec8a7a3de86e88c0cb55f1f127dbfbd3278c)
            check_type(argname="argument security_control_id", value=security_control_id, expected_type=type_hints["security_control_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_control_id": security_control_id,
        }

    @builtins.property
    def security_control_id(self) -> builtins.str:
        '''The SecurityControlId of the SecurityControl resource.'''
        result = self._values.get("security_control_id")
        assert result is not None, "Required property 'security_control_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityControlReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_securityhub.StandardReference",
    jsii_struct_bases=[],
    name_mapping={"standards_subscription_arn": "standardsSubscriptionArn"},
)
class StandardReference:
    def __init__(self, *, standards_subscription_arn: builtins.str) -> None:
        '''A reference to a Standard resource.

        :param standards_subscription_arn: The StandardsSubscriptionArn of the Standard resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_securityhub as interfaces_securityhub
            
            standard_reference = interfaces_securityhub.StandardReference(
                standards_subscription_arn="standardsSubscriptionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db55b49984acf12a9808e2ad6d880d3718370198d6511f8d5a94f8981a8a4f5)
            check_type(argname="argument standards_subscription_arn", value=standards_subscription_arn, expected_type=type_hints["standards_subscription_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "standards_subscription_arn": standards_subscription_arn,
        }

    @builtins.property
    def standards_subscription_arn(self) -> builtins.str:
        '''The StandardsSubscriptionArn of the Standard resource.'''
        result = self._values.get("standards_subscription_arn")
        assert result is not None, "Required property 'standards_subscription_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StandardReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AggregatorV2Reference",
    "AutomationRuleReference",
    "AutomationRuleV2Reference",
    "ConfigurationPolicyReference",
    "ConnectorV2Reference",
    "DelegatedAdminReference",
    "FindingAggregatorReference",
    "HubReference",
    "HubV2Reference",
    "IAggregatorV2Ref",
    "IAutomationRuleRef",
    "IAutomationRuleV2Ref",
    "IConfigurationPolicyRef",
    "IConnectorV2Ref",
    "IDelegatedAdminRef",
    "IFindingAggregatorRef",
    "IHubRef",
    "IHubV2Ref",
    "IInsightRef",
    "IOrganizationConfigurationRef",
    "IPolicyAssociationRef",
    "IProductSubscriptionRef",
    "ISecurityControlRef",
    "IStandardRef",
    "InsightReference",
    "OrganizationConfigurationReference",
    "PolicyAssociationReference",
    "ProductSubscriptionReference",
    "SecurityControlReference",
    "StandardReference",
]

publication.publish()

def _typecheckingstub__35a220db7509efb96c8abd58d83c974df0d1ec6221841ce0031c7e29166870a6(
    *,
    aggregator_v2_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fc12b37b5b474e26a7ab22d75e02c9702e3dccd822e93295efe42823eb6e5bf(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aef4997ae46bca6cfa7dd6194511cb0c8e4c744827ab27202ec5bf7628e5b6e8(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4bf6c068777f6837cd16457e25121201ab0e5a04344d176fc401dc42df6811(
    *,
    configuration_policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f9de0b840b9c41998aae229688e8a483801310a2dadbbcf7777f01d538ebb1(
    *,
    connector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02fcb283a9643cdb1e80efe749afc53bd727fa2a227498840453efc18e4d0b32(
    *,
    delegated_admin_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8d6cf95ba857b951122e47526fc001b1f55ba2dc693a043cb41135baa3cfdc9(
    *,
    finding_aggregator_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64fd84efb35583fcc0b4b4b1177deb0cf485141b0d3945ccb8a69a000febb7ec(
    *,
    hub_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a9f49271093222ae0ce6374cb3465f6580021ffb6cb531e479d887c30c358af(
    *,
    hub_v2_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0458c101ffc14948dabba2554b5917f46d43912d82bfaa6a51dcca94609e8d40(
    *,
    insight_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e68192f516aaa64f02830db5695b88046d18593c6a5693c3c8aec0f225a6be1(
    *,
    organization_configuration_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e0a6ff2ea35ae8bb02106e26430281b639559a6f3d415ea2feb07cfb1b0edb(
    *,
    association_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4f1213ac1e04edaababb0118ef15710338e2f048be32080871c4e3703f095c2(
    *,
    product_subscription_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__171752d544f357353cc747f6a154ec8a7a3de86e88c0cb55f1f127dbfbd3278c(
    *,
    security_control_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db55b49984acf12a9808e2ad6d880d3718370198d6511f8d5a94f8981a8a4f5(
    *,
    standards_subscription_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAggregatorV2Ref, IAutomationRuleRef, IAutomationRuleV2Ref, IConfigurationPolicyRef, IConnectorV2Ref, IDelegatedAdminRef, IFindingAggregatorRef, IHubRef, IHubV2Ref, IInsightRef, IOrganizationConfigurationRef, IPolicyAssociationRef, IProductSubscriptionRef, ISecurityControlRef, IStandardRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
