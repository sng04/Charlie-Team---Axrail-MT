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
    jsii_type="aws-cdk-lib.interfaces.aws_billingconductor.BillingGroupReference",
    jsii_struct_bases=[],
    name_mapping={"billing_group_arn": "billingGroupArn"},
)
class BillingGroupReference:
    def __init__(self, *, billing_group_arn: builtins.str) -> None:
        '''A reference to a BillingGroup resource.

        :param billing_group_arn: The Arn of the BillingGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_billingconductor as interfaces_billingconductor
            
            billing_group_reference = interfaces_billingconductor.BillingGroupReference(
                billing_group_arn="billingGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d54d769b9fe153f3708e0f786510d168a65abb45df05c7ee52aec2f9dc1df4a)
            check_type(argname="argument billing_group_arn", value=billing_group_arn, expected_type=type_hints["billing_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "billing_group_arn": billing_group_arn,
        }

    @builtins.property
    def billing_group_arn(self) -> builtins.str:
        '''The Arn of the BillingGroup resource.'''
        result = self._values.get("billing_group_arn")
        assert result is not None, "Required property 'billing_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BillingGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_billingconductor.CustomLineItemReference",
    jsii_struct_bases=[],
    name_mapping={"custom_line_item_arn": "customLineItemArn"},
)
class CustomLineItemReference:
    def __init__(self, *, custom_line_item_arn: builtins.str) -> None:
        '''A reference to a CustomLineItem resource.

        :param custom_line_item_arn: The Arn of the CustomLineItem resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_billingconductor as interfaces_billingconductor
            
            custom_line_item_reference = interfaces_billingconductor.CustomLineItemReference(
                custom_line_item_arn="customLineItemArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a82dc4016ab3a9b979788b90a66c24114f2e92c31de7e50729b715f8f25fba9)
            check_type(argname="argument custom_line_item_arn", value=custom_line_item_arn, expected_type=type_hints["custom_line_item_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_line_item_arn": custom_line_item_arn,
        }

    @builtins.property
    def custom_line_item_arn(self) -> builtins.str:
        '''The Arn of the CustomLineItem resource.'''
        result = self._values.get("custom_line_item_arn")
        assert result is not None, "Required property 'custom_line_item_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomLineItemReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_billingconductor.IBillingGroupRef"
)
class IBillingGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BillingGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="billingGroupRef")
    def billing_group_ref(self) -> "BillingGroupReference":
        '''(experimental) A reference to a BillingGroup resource.

        :stability: experimental
        '''
        ...


class _IBillingGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BillingGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_billingconductor.IBillingGroupRef"

    @builtins.property
    @jsii.member(jsii_name="billingGroupRef")
    def billing_group_ref(self) -> "BillingGroupReference":
        '''(experimental) A reference to a BillingGroup resource.

        :stability: experimental
        '''
        return typing.cast("BillingGroupReference", jsii.get(self, "billingGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBillingGroupRef).__jsii_proxy_class__ = lambda : _IBillingGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_billingconductor.ICustomLineItemRef"
)
class ICustomLineItemRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomLineItem.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customLineItemRef")
    def custom_line_item_ref(self) -> "CustomLineItemReference":
        '''(experimental) A reference to a CustomLineItem resource.

        :stability: experimental
        '''
        ...


class _ICustomLineItemRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomLineItem.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_billingconductor.ICustomLineItemRef"

    @builtins.property
    @jsii.member(jsii_name="customLineItemRef")
    def custom_line_item_ref(self) -> "CustomLineItemReference":
        '''(experimental) A reference to a CustomLineItem resource.

        :stability: experimental
        '''
        return typing.cast("CustomLineItemReference", jsii.get(self, "customLineItemRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomLineItemRef).__jsii_proxy_class__ = lambda : _ICustomLineItemRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_billingconductor.IPricingPlanRef"
)
class IPricingPlanRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PricingPlan.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pricingPlanRef")
    def pricing_plan_ref(self) -> "PricingPlanReference":
        '''(experimental) A reference to a PricingPlan resource.

        :stability: experimental
        '''
        ...


class _IPricingPlanRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PricingPlan.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_billingconductor.IPricingPlanRef"

    @builtins.property
    @jsii.member(jsii_name="pricingPlanRef")
    def pricing_plan_ref(self) -> "PricingPlanReference":
        '''(experimental) A reference to a PricingPlan resource.

        :stability: experimental
        '''
        return typing.cast("PricingPlanReference", jsii.get(self, "pricingPlanRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPricingPlanRef).__jsii_proxy_class__ = lambda : _IPricingPlanRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_billingconductor.IPricingRuleRef"
)
class IPricingRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PricingRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pricingRuleRef")
    def pricing_rule_ref(self) -> "PricingRuleReference":
        '''(experimental) A reference to a PricingRule resource.

        :stability: experimental
        '''
        ...


class _IPricingRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PricingRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_billingconductor.IPricingRuleRef"

    @builtins.property
    @jsii.member(jsii_name="pricingRuleRef")
    def pricing_rule_ref(self) -> "PricingRuleReference":
        '''(experimental) A reference to a PricingRule resource.

        :stability: experimental
        '''
        return typing.cast("PricingRuleReference", jsii.get(self, "pricingRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPricingRuleRef).__jsii_proxy_class__ = lambda : _IPricingRuleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_billingconductor.PricingPlanReference",
    jsii_struct_bases=[],
    name_mapping={"pricing_plan_arn": "pricingPlanArn"},
)
class PricingPlanReference:
    def __init__(self, *, pricing_plan_arn: builtins.str) -> None:
        '''A reference to a PricingPlan resource.

        :param pricing_plan_arn: The Arn of the PricingPlan resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_billingconductor as interfaces_billingconductor
            
            pricing_plan_reference = interfaces_billingconductor.PricingPlanReference(
                pricing_plan_arn="pricingPlanArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__960acf25d202e1e2af55f5a5486c9581bf43462e420a2bb571581e33d90d89fa)
            check_type(argname="argument pricing_plan_arn", value=pricing_plan_arn, expected_type=type_hints["pricing_plan_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pricing_plan_arn": pricing_plan_arn,
        }

    @builtins.property
    def pricing_plan_arn(self) -> builtins.str:
        '''The Arn of the PricingPlan resource.'''
        result = self._values.get("pricing_plan_arn")
        assert result is not None, "Required property 'pricing_plan_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PricingPlanReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_billingconductor.PricingRuleReference",
    jsii_struct_bases=[],
    name_mapping={"pricing_rule_arn": "pricingRuleArn"},
)
class PricingRuleReference:
    def __init__(self, *, pricing_rule_arn: builtins.str) -> None:
        '''A reference to a PricingRule resource.

        :param pricing_rule_arn: The Arn of the PricingRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_billingconductor as interfaces_billingconductor
            
            pricing_rule_reference = interfaces_billingconductor.PricingRuleReference(
                pricing_rule_arn="pricingRuleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e77af8ffff79b80d2d85e8f1c2cca957ed086ed0f75da346afd52cb5e2d7741)
            check_type(argname="argument pricing_rule_arn", value=pricing_rule_arn, expected_type=type_hints["pricing_rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pricing_rule_arn": pricing_rule_arn,
        }

    @builtins.property
    def pricing_rule_arn(self) -> builtins.str:
        '''The Arn of the PricingRule resource.'''
        result = self._values.get("pricing_rule_arn")
        assert result is not None, "Required property 'pricing_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PricingRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BillingGroupReference",
    "CustomLineItemReference",
    "IBillingGroupRef",
    "ICustomLineItemRef",
    "IPricingPlanRef",
    "IPricingRuleRef",
    "PricingPlanReference",
    "PricingRuleReference",
]

publication.publish()

def _typecheckingstub__7d54d769b9fe153f3708e0f786510d168a65abb45df05c7ee52aec2f9dc1df4a(
    *,
    billing_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a82dc4016ab3a9b979788b90a66c24114f2e92c31de7e50729b715f8f25fba9(
    *,
    custom_line_item_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__960acf25d202e1e2af55f5a5486c9581bf43462e420a2bb571581e33d90d89fa(
    *,
    pricing_plan_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e77af8ffff79b80d2d85e8f1c2cca957ed086ed0f75da346afd52cb5e2d7741(
    *,
    pricing_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBillingGroupRef, ICustomLineItemRef, IPricingPlanRef, IPricingRuleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
