r'''
# AWS::ComputeOptimizer Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_computeoptimizer as computeoptimizer
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ComputeOptimizer construct libraries](https://constructs.dev/search?q=computeoptimizer)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ComputeOptimizer resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ComputeOptimizer.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ComputeOptimizer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ComputeOptimizer.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
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

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_computeoptimizer import (
    AutomationRuleReference as _AutomationRuleReference_9f2f6bfe,
    IAutomationRuleRef as _IAutomationRuleRef_e164f41f,
)


@jsii.implements(_IInspectable_c2943556, _IAutomationRuleRef_e164f41f, _ITaggableV2_4e6798f8)
class CfnAutomationRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_computeoptimizer.CfnAutomationRule",
):
    '''Creates an AWS Compute Optimizer automation rule that automatically implements recommended actions based on your defined criteria and schedule.

    Automation rules are global resources that manage automated actions across all AWS Regions where Compute Optimizer Automation is available. Organization-level rules can only be created by the management account or delegated administrator.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html
    :cloudformationResource: AWS::ComputeOptimizer::AutomationRule
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_computeoptimizer as computeoptimizer
        
        cfn_automation_rule = computeoptimizer.CfnAutomationRule(self, "MyCfnAutomationRule",
            name="name",
            recommended_action_types=["recommendedActionTypes"],
            rule_type="ruleType",
            schedule=computeoptimizer.CfnAutomationRule.ScheduleProperty(
                execution_window_in_minutes=123,
                schedule_expression="scheduleExpression",
                schedule_expression_timezone="scheduleExpressionTimezone"
            ),
            status="status",
        
            # the properties below are optional
            criteria=computeoptimizer.CfnAutomationRule.CriteriaProperty(
                ebs_volume_size_in_gib=[computeoptimizer.CfnAutomationRule.IntegerCriteriaConditionProperty(
                    comparison="comparison",
                    values=[123]
                )],
                ebs_volume_type=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                    comparison="comparison",
                    values=["values"]
                )],
                estimated_monthly_savings=[computeoptimizer.CfnAutomationRule.DoubleCriteriaConditionProperty(
                    comparison="comparison",
                    values=[123]
                )],
                look_back_period_in_days=[computeoptimizer.CfnAutomationRule.IntegerCriteriaConditionProperty(
                    comparison="comparison",
                    values=[123]
                )],
                region=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                    comparison="comparison",
                    values=["values"]
                )],
                resource_arn=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                    comparison="comparison",
                    values=["values"]
                )],
                resource_tag=[computeoptimizer.CfnAutomationRule.ResourceTagsCriteriaConditionProperty(
                    comparison="comparison",
                    key="key",
                    values=["values"]
                )],
                restart_needed=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                    comparison="comparison",
                    values=["values"]
                )]
            ),
            description="description",
            organization_configuration=computeoptimizer.CfnAutomationRule.OrganizationConfigurationProperty(
                account_ids=["accountIds"],
                rule_apply_order="ruleApplyOrder"
            ),
            priority="priority",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        recommended_action_types: typing.Sequence[builtins.str],
        rule_type: builtins.str,
        schedule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]],
        status: builtins.str,
        criteria: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.CriteriaProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        organization_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.OrganizationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        priority: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ComputeOptimizer::AutomationRule``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the automation rule.
        :param recommended_action_types: The types of recommended actions this rule will implement.
        :param rule_type: The type of automation rule.
        :param schedule: 
        :param status: The status of the automation rule.
        :param criteria: 
        :param description: The description of the automation rule.
        :param organization_configuration: 
        :param priority: Rule priority within its group.
        :param tags: Tags associated with the automation rule.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96a666753f76c538bcce8b208bd4fe982327d0cdf14f919daa387b8c3329361e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAutomationRuleProps(
            name=name,
            recommended_action_types=recommended_action_types,
            rule_type=rule_type,
            schedule=schedule,
            status=status,
            criteria=criteria,
            description=description,
            organization_configuration=organization_configuration,
            priority=priority,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnAutomationRule")
    @builtins.classmethod
    def is_cfn_automation_rule(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAutomationRule.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__480292f6f2d1bff94dcd7a3d57b42386a76a0e6ae04ad090a1db868019e4ec37)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAutomationRule", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f486a97f146f9b0f4b1190fbc2f9660b7d307fc7c14989fd309fc943e8a3a91)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a8520f0d2d6d74ec45a1f2082e83d3e732e6939a22c2ddc79d991f420302e3a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccountId")
    def attr_account_id(self) -> builtins.str:
        '''The AWS account ID that owns the automation rule.

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''The timestamp when the automation rule was created.

        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTimestamp")
    def attr_last_updated_timestamp(self) -> builtins.str:
        '''The timestamp when the automation rule was last updated.

        :cloudformationAttribute: LastUpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the automation rule.

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleId")
    def attr_rule_id(self) -> builtins.str:
        '''The unique identifier of the automation rule.

        :cloudformationAttribute: RuleId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleId"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleRevision")
    def attr_rule_revision(self) -> builtins.str:
        '''The revision number of the automation rule.

        :cloudformationAttribute: RuleRevision
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleRevision"))

    @builtins.property
    @jsii.member(jsii_name="automationRuleRef")
    def automation_rule_ref(self) -> "_AutomationRuleReference_9f2f6bfe":
        '''A reference to a AutomationRule resource.'''
        return typing.cast("_AutomationRuleReference_9f2f6bfe", jsii.get(self, "automationRuleRef"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the automation rule.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12432e1def54ab4a8f04be84e5c6032d7e4e0a9729dd56c51d2a540eba8e288f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recommendedActionTypes")
    def recommended_action_types(self) -> typing.List[builtins.str]:
        '''The types of recommended actions this rule will implement.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "recommendedActionTypes"))

    @recommended_action_types.setter
    def recommended_action_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a69f6615b451a52d4025f39af3ea110a1c305a7cdf1975b5123db464c9ffcf3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recommendedActionTypes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleType")
    def rule_type(self) -> builtins.str:
        '''The type of automation rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleType"))

    @rule_type.setter
    def rule_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c023ccc3b14f458b3a26d5ffc7c47fd30417efe1fe064fd6fd8bfd72e6d5e36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.ScheduleProperty"]:
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.ScheduleProperty"], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.ScheduleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cefdf23808a2bdd45df2cf7fdfa0ed6c8e067eb54cff24649619ea00c07799a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        '''The status of the automation rule.'''
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5587f4f44ca9843d0dc165c34e813a55d83d5f5c1836a85325aaad770147bdf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="criteria")
    def criteria(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.CriteriaProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.CriteriaProperty"]], jsii.get(self, "criteria"))

    @criteria.setter
    def criteria(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.CriteriaProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__289c65c0a5bac1427b11926c90763f1770bba7a367f702daa76bf305c29df78e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "criteria", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the automation rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ee341245a5bb3d3bb5f3425b715d93b07153893d5c394f7062a07979fa20b91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="organizationConfiguration")
    def organization_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.OrganizationConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.OrganizationConfigurationProperty"]], jsii.get(self, "organizationConfiguration"))

    @organization_configuration.setter
    def organization_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.OrganizationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8693308b84990e1940e6d8125c64fb152e7c9a52301f3933e9018615cc0c821b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organizationConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> typing.Optional[builtins.str]:
        '''Rule priority within its group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68a0a555e99d5fd4d7f6532a47a52406a7b848025f50626d6fb58f632c8e83e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags associated with the automation rule.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fd58f76e153d14a2da3d1d4038d7af1ef5ef2e85cee2b7eff1735fa6050e261)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_computeoptimizer.CfnAutomationRule.CriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ebs_volume_size_in_gib": "ebsVolumeSizeInGib",
            "ebs_volume_type": "ebsVolumeType",
            "estimated_monthly_savings": "estimatedMonthlySavings",
            "look_back_period_in_days": "lookBackPeriodInDays",
            "region": "region",
            "resource_arn": "resourceArn",
            "resource_tag": "resourceTag",
            "restart_needed": "restartNeeded",
        },
    )
    class CriteriaProperty:
        def __init__(
            self,
            *,
            ebs_volume_size_in_gib: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.IntegerCriteriaConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ebs_volume_type: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.StringCriteriaConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            estimated_monthly_savings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.DoubleCriteriaConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            look_back_period_in_days: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.IntegerCriteriaConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            region: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.StringCriteriaConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_arn: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.StringCriteriaConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_tag: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.ResourceTagsCriteriaConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            restart_needed: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.StringCriteriaConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param ebs_volume_size_in_gib: 
            :param ebs_volume_type: 
            :param estimated_monthly_savings: 
            :param look_back_period_in_days: 
            :param region: 
            :param resource_arn: 
            :param resource_tag: 
            :param restart_needed: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-criteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_computeoptimizer as computeoptimizer
                
                criteria_property = computeoptimizer.CfnAutomationRule.CriteriaProperty(
                    ebs_volume_size_in_gib=[computeoptimizer.CfnAutomationRule.IntegerCriteriaConditionProperty(
                        comparison="comparison",
                        values=[123]
                    )],
                    ebs_volume_type=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                        comparison="comparison",
                        values=["values"]
                    )],
                    estimated_monthly_savings=[computeoptimizer.CfnAutomationRule.DoubleCriteriaConditionProperty(
                        comparison="comparison",
                        values=[123]
                    )],
                    look_back_period_in_days=[computeoptimizer.CfnAutomationRule.IntegerCriteriaConditionProperty(
                        comparison="comparison",
                        values=[123]
                    )],
                    region=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                        comparison="comparison",
                        values=["values"]
                    )],
                    resource_arn=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                        comparison="comparison",
                        values=["values"]
                    )],
                    resource_tag=[computeoptimizer.CfnAutomationRule.ResourceTagsCriteriaConditionProperty(
                        comparison="comparison",
                        key="key",
                        values=["values"]
                    )],
                    restart_needed=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                        comparison="comparison",
                        values=["values"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2221beabcf689a62effe3e9503319e5b021178f2776807f8a84226f47b1072b5)
                check_type(argname="argument ebs_volume_size_in_gib", value=ebs_volume_size_in_gib, expected_type=type_hints["ebs_volume_size_in_gib"])
                check_type(argname="argument ebs_volume_type", value=ebs_volume_type, expected_type=type_hints["ebs_volume_type"])
                check_type(argname="argument estimated_monthly_savings", value=estimated_monthly_savings, expected_type=type_hints["estimated_monthly_savings"])
                check_type(argname="argument look_back_period_in_days", value=look_back_period_in_days, expected_type=type_hints["look_back_period_in_days"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
                check_type(argname="argument resource_tag", value=resource_tag, expected_type=type_hints["resource_tag"])
                check_type(argname="argument restart_needed", value=restart_needed, expected_type=type_hints["restart_needed"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ebs_volume_size_in_gib is not None:
                self._values["ebs_volume_size_in_gib"] = ebs_volume_size_in_gib
            if ebs_volume_type is not None:
                self._values["ebs_volume_type"] = ebs_volume_type
            if estimated_monthly_savings is not None:
                self._values["estimated_monthly_savings"] = estimated_monthly_savings
            if look_back_period_in_days is not None:
                self._values["look_back_period_in_days"] = look_back_period_in_days
            if region is not None:
                self._values["region"] = region
            if resource_arn is not None:
                self._values["resource_arn"] = resource_arn
            if resource_tag is not None:
                self._values["resource_tag"] = resource_tag
            if restart_needed is not None:
                self._values["restart_needed"] = restart_needed

        @builtins.property
        def ebs_volume_size_in_gib(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.IntegerCriteriaConditionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-criteria.html#cfn-computeoptimizer-automationrule-criteria-ebsvolumesizeingib
            '''
            result = self._values.get("ebs_volume_size_in_gib")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.IntegerCriteriaConditionProperty"]]]], result)

        @builtins.property
        def ebs_volume_type(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.StringCriteriaConditionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-criteria.html#cfn-computeoptimizer-automationrule-criteria-ebsvolumetype
            '''
            result = self._values.get("ebs_volume_type")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.StringCriteriaConditionProperty"]]]], result)

        @builtins.property
        def estimated_monthly_savings(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.DoubleCriteriaConditionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-criteria.html#cfn-computeoptimizer-automationrule-criteria-estimatedmonthlysavings
            '''
            result = self._values.get("estimated_monthly_savings")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.DoubleCriteriaConditionProperty"]]]], result)

        @builtins.property
        def look_back_period_in_days(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.IntegerCriteriaConditionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-criteria.html#cfn-computeoptimizer-automationrule-criteria-lookbackperiodindays
            '''
            result = self._values.get("look_back_period_in_days")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.IntegerCriteriaConditionProperty"]]]], result)

        @builtins.property
        def region(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.StringCriteriaConditionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-criteria.html#cfn-computeoptimizer-automationrule-criteria-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.StringCriteriaConditionProperty"]]]], result)

        @builtins.property
        def resource_arn(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.StringCriteriaConditionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-criteria.html#cfn-computeoptimizer-automationrule-criteria-resourcearn
            '''
            result = self._values.get("resource_arn")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.StringCriteriaConditionProperty"]]]], result)

        @builtins.property
        def resource_tag(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.ResourceTagsCriteriaConditionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-criteria.html#cfn-computeoptimizer-automationrule-criteria-resourcetag
            '''
            result = self._values.get("resource_tag")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.ResourceTagsCriteriaConditionProperty"]]]], result)

        @builtins.property
        def restart_needed(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.StringCriteriaConditionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-criteria.html#cfn-computeoptimizer-automationrule-criteria-restartneeded
            '''
            result = self._values.get("restart_needed")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.StringCriteriaConditionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_computeoptimizer.CfnAutomationRule.DoubleCriteriaConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "values": "values"},
    )
    class DoubleCriteriaConditionProperty:
        def __init__(
            self,
            *,
            comparison: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Union[typing.Sequence[jsii.Number], "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''
            :param comparison: 
            :param values: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-doublecriteriacondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_computeoptimizer as computeoptimizer
                
                double_criteria_condition_property = computeoptimizer.CfnAutomationRule.DoubleCriteriaConditionProperty(
                    comparison="comparison",
                    values=[123]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d9dce0c17f96960de6116298c67e2feb2bf6a7257e20aa39bd6dd3c36b4cbc9f)
                check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if comparison is not None:
                self._values["comparison"] = comparison
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def comparison(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-doublecriteriacondition.html#cfn-computeoptimizer-automationrule-doublecriteriacondition-comparison
            '''
            result = self._values.get("comparison")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(
            self,
        ) -> typing.Optional[typing.Union[typing.List[jsii.Number], "_IResolvable_da3f097b"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-doublecriteriacondition.html#cfn-computeoptimizer-automationrule-doublecriteriacondition-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.Union[typing.List[jsii.Number], "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DoubleCriteriaConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_computeoptimizer.CfnAutomationRule.IntegerCriteriaConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "values": "values"},
    )
    class IntegerCriteriaConditionProperty:
        def __init__(
            self,
            *,
            comparison: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Union[typing.Sequence[jsii.Number], "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''
            :param comparison: 
            :param values: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-integercriteriacondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_computeoptimizer as computeoptimizer
                
                integer_criteria_condition_property = computeoptimizer.CfnAutomationRule.IntegerCriteriaConditionProperty(
                    comparison="comparison",
                    values=[123]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63a1a744e2a11f80314f00a1509ab739f3ac5c054f9f670718151b5e36cfb5ce)
                check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if comparison is not None:
                self._values["comparison"] = comparison
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def comparison(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-integercriteriacondition.html#cfn-computeoptimizer-automationrule-integercriteriacondition-comparison
            '''
            result = self._values.get("comparison")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(
            self,
        ) -> typing.Optional[typing.Union[typing.List[jsii.Number], "_IResolvable_da3f097b"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-integercriteriacondition.html#cfn-computeoptimizer-automationrule-integercriteriacondition-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.Union[typing.List[jsii.Number], "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegerCriteriaConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_computeoptimizer.CfnAutomationRule.OrganizationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_ids": "accountIds",
            "rule_apply_order": "ruleApplyOrder",
        },
    )
    class OrganizationConfigurationProperty:
        def __init__(
            self,
            *,
            account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            rule_apply_order: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param account_ids: List of account IDs where the organization rule applies.
            :param rule_apply_order: When the rule should be applied relative to account rules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-organizationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_computeoptimizer as computeoptimizer
                
                organization_configuration_property = computeoptimizer.CfnAutomationRule.OrganizationConfigurationProperty(
                    account_ids=["accountIds"],
                    rule_apply_order="ruleApplyOrder"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__23f66489eba80548b6b94027d2051adc2b1428ef11d2360412fe72167a8dbabe)
                check_type(argname="argument account_ids", value=account_ids, expected_type=type_hints["account_ids"])
                check_type(argname="argument rule_apply_order", value=rule_apply_order, expected_type=type_hints["rule_apply_order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if account_ids is not None:
                self._values["account_ids"] = account_ids
            if rule_apply_order is not None:
                self._values["rule_apply_order"] = rule_apply_order

        @builtins.property
        def account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of account IDs where the organization rule applies.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-organizationconfiguration.html#cfn-computeoptimizer-automationrule-organizationconfiguration-accountids
            '''
            result = self._values.get("account_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def rule_apply_order(self) -> typing.Optional[builtins.str]:
            '''When the rule should be applied relative to account rules.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-organizationconfiguration.html#cfn-computeoptimizer-automationrule-organizationconfiguration-ruleapplyorder
            '''
            result = self._values.get("rule_apply_order")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OrganizationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_computeoptimizer.CfnAutomationRule.ResourceTagsCriteriaConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "key": "key", "values": "values"},
    )
    class ResourceTagsCriteriaConditionProperty:
        def __init__(
            self,
            *,
            comparison: typing.Optional[builtins.str] = None,
            key: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param comparison: 
            :param key: 
            :param values: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_computeoptimizer as computeoptimizer
                
                resource_tags_criteria_condition_property = computeoptimizer.CfnAutomationRule.ResourceTagsCriteriaConditionProperty(
                    comparison="comparison",
                    key="key",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cdcf2ae259b8562f6d66cb179cd5ce41ecfa75902600227ae3631ea1396db569)
                check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if comparison is not None:
                self._values["comparison"] = comparison
            if key is not None:
                self._values["key"] = key
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def comparison(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition.html#cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-comparison
            '''
            result = self._values.get("comparison")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition.html#cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-resourcetagscriteriacondition.html#cfn-computeoptimizer-automationrule-resourcetagscriteriacondition-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceTagsCriteriaConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_computeoptimizer.CfnAutomationRule.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "execution_window_in_minutes": "executionWindowInMinutes",
            "schedule_expression": "scheduleExpression",
            "schedule_expression_timezone": "scheduleExpressionTimezone",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            execution_window_in_minutes: typing.Optional[jsii.Number] = None,
            schedule_expression: typing.Optional[builtins.str] = None,
            schedule_expression_timezone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param execution_window_in_minutes: Execution window duration in minutes.
            :param schedule_expression: Schedule expression (e.g., cron or rate expression).
            :param schedule_expression_timezone: IANA timezone identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_computeoptimizer as computeoptimizer
                
                schedule_property = computeoptimizer.CfnAutomationRule.ScheduleProperty(
                    execution_window_in_minutes=123,
                    schedule_expression="scheduleExpression",
                    schedule_expression_timezone="scheduleExpressionTimezone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4bf7de7511c121ed491996afe46004f5a86ee28c95724278fbc25812f44bc65b)
                check_type(argname="argument execution_window_in_minutes", value=execution_window_in_minutes, expected_type=type_hints["execution_window_in_minutes"])
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
                check_type(argname="argument schedule_expression_timezone", value=schedule_expression_timezone, expected_type=type_hints["schedule_expression_timezone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if execution_window_in_minutes is not None:
                self._values["execution_window_in_minutes"] = execution_window_in_minutes
            if schedule_expression is not None:
                self._values["schedule_expression"] = schedule_expression
            if schedule_expression_timezone is not None:
                self._values["schedule_expression_timezone"] = schedule_expression_timezone

        @builtins.property
        def execution_window_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''Execution window duration in minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-schedule.html#cfn-computeoptimizer-automationrule-schedule-executionwindowinminutes
            '''
            result = self._values.get("execution_window_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_expression(self) -> typing.Optional[builtins.str]:
            '''Schedule expression (e.g., cron or rate expression).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-schedule.html#cfn-computeoptimizer-automationrule-schedule-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def schedule_expression_timezone(self) -> typing.Optional[builtins.str]:
            '''IANA timezone identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-schedule.html#cfn-computeoptimizer-automationrule-schedule-scheduleexpressiontimezone
            '''
            result = self._values.get("schedule_expression_timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "values": "values"},
    )
    class StringCriteriaConditionProperty:
        def __init__(
            self,
            *,
            comparison: typing.Optional[builtins.str] = None,
            values: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param comparison: 
            :param values: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-stringcriteriacondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_computeoptimizer as computeoptimizer
                
                string_criteria_condition_property = computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                    comparison="comparison",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a0c234cd251c7890ce9b10e125fa4606918e5c69ee8a2cd6f0bcab295a4edc0c)
                check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if comparison is not None:
                self._values["comparison"] = comparison
            if values is not None:
                self._values["values"] = values

        @builtins.property
        def comparison(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-stringcriteriacondition.html#cfn-computeoptimizer-automationrule-stringcriteriacondition-comparison
            '''
            result = self._values.get("comparison")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def values(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-computeoptimizer-automationrule-stringcriteriacondition.html#cfn-computeoptimizer-automationrule-stringcriteriacondition-values
            '''
            result = self._values.get("values")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StringCriteriaConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_computeoptimizer.CfnAutomationRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "recommended_action_types": "recommendedActionTypes",
        "rule_type": "ruleType",
        "schedule": "schedule",
        "status": "status",
        "criteria": "criteria",
        "description": "description",
        "organization_configuration": "organizationConfiguration",
        "priority": "priority",
        "tags": "tags",
    },
)
class CfnAutomationRuleProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        recommended_action_types: typing.Sequence[builtins.str],
        rule_type: builtins.str,
        schedule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]],
        status: builtins.str,
        criteria: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.CriteriaProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        organization_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAutomationRule.OrganizationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        priority: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAutomationRule``.

        :param name: The name of the automation rule.
        :param recommended_action_types: The types of recommended actions this rule will implement.
        :param rule_type: The type of automation rule.
        :param schedule: 
        :param status: The status of the automation rule.
        :param criteria: 
        :param description: The description of the automation rule.
        :param organization_configuration: 
        :param priority: Rule priority within its group.
        :param tags: Tags associated with the automation rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_computeoptimizer as computeoptimizer
            
            cfn_automation_rule_props = computeoptimizer.CfnAutomationRuleProps(
                name="name",
                recommended_action_types=["recommendedActionTypes"],
                rule_type="ruleType",
                schedule=computeoptimizer.CfnAutomationRule.ScheduleProperty(
                    execution_window_in_minutes=123,
                    schedule_expression="scheduleExpression",
                    schedule_expression_timezone="scheduleExpressionTimezone"
                ),
                status="status",
            
                # the properties below are optional
                criteria=computeoptimizer.CfnAutomationRule.CriteriaProperty(
                    ebs_volume_size_in_gib=[computeoptimizer.CfnAutomationRule.IntegerCriteriaConditionProperty(
                        comparison="comparison",
                        values=[123]
                    )],
                    ebs_volume_type=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                        comparison="comparison",
                        values=["values"]
                    )],
                    estimated_monthly_savings=[computeoptimizer.CfnAutomationRule.DoubleCriteriaConditionProperty(
                        comparison="comparison",
                        values=[123]
                    )],
                    look_back_period_in_days=[computeoptimizer.CfnAutomationRule.IntegerCriteriaConditionProperty(
                        comparison="comparison",
                        values=[123]
                    )],
                    region=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                        comparison="comparison",
                        values=["values"]
                    )],
                    resource_arn=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                        comparison="comparison",
                        values=["values"]
                    )],
                    resource_tag=[computeoptimizer.CfnAutomationRule.ResourceTagsCriteriaConditionProperty(
                        comparison="comparison",
                        key="key",
                        values=["values"]
                    )],
                    restart_needed=[computeoptimizer.CfnAutomationRule.StringCriteriaConditionProperty(
                        comparison="comparison",
                        values=["values"]
                    )]
                ),
                description="description",
                organization_configuration=computeoptimizer.CfnAutomationRule.OrganizationConfigurationProperty(
                    account_ids=["accountIds"],
                    rule_apply_order="ruleApplyOrder"
                ),
                priority="priority",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__929667fe90449fbcfe9926f80a0cba1fdf4f24a92c992f3b1f7bb0d8c5fa25f1)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument recommended_action_types", value=recommended_action_types, expected_type=type_hints["recommended_action_types"])
            check_type(argname="argument rule_type", value=rule_type, expected_type=type_hints["rule_type"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument organization_configuration", value=organization_configuration, expected_type=type_hints["organization_configuration"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "recommended_action_types": recommended_action_types,
            "rule_type": rule_type,
            "schedule": schedule,
            "status": status,
        }
        if criteria is not None:
            self._values["criteria"] = criteria
        if description is not None:
            self._values["description"] = description
        if organization_configuration is not None:
            self._values["organization_configuration"] = organization_configuration
        if priority is not None:
            self._values["priority"] = priority
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the automation rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html#cfn-computeoptimizer-automationrule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def recommended_action_types(self) -> typing.List[builtins.str]:
        '''The types of recommended actions this rule will implement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html#cfn-computeoptimizer-automationrule-recommendedactiontypes
        '''
        result = self._values.get("recommended_action_types")
        assert result is not None, "Required property 'recommended_action_types' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def rule_type(self) -> builtins.str:
        '''The type of automation rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html#cfn-computeoptimizer-automationrule-ruletype
        '''
        result = self._values.get("rule_type")
        assert result is not None, "Required property 'rule_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.ScheduleProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html#cfn-computeoptimizer-automationrule-schedule
        '''
        result = self._values.get("schedule")
        assert result is not None, "Required property 'schedule' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.ScheduleProperty"], result)

    @builtins.property
    def status(self) -> builtins.str:
        '''The status of the automation rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html#cfn-computeoptimizer-automationrule-status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def criteria(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.CriteriaProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html#cfn-computeoptimizer-automationrule-criteria
        '''
        result = self._values.get("criteria")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.CriteriaProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the automation rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html#cfn-computeoptimizer-automationrule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.OrganizationConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html#cfn-computeoptimizer-automationrule-organizationconfiguration
        '''
        result = self._values.get("organization_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAutomationRule.OrganizationConfigurationProperty"]], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        '''Rule priority within its group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html#cfn-computeoptimizer-automationrule-priority
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags associated with the automation rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-computeoptimizer-automationrule.html#cfn-computeoptimizer-automationrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAutomationRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAutomationRule",
    "CfnAutomationRuleProps",
]

publication.publish()

def _typecheckingstub__96a666753f76c538bcce8b208bd4fe982327d0cdf14f919daa387b8c3329361e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    recommended_action_types: typing.Sequence[builtins.str],
    rule_type: builtins.str,
    schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
    status: builtins.str,
    criteria: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.CriteriaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    organization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.OrganizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    priority: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__480292f6f2d1bff94dcd7a3d57b42386a76a0e6ae04ad090a1db868019e4ec37(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f486a97f146f9b0f4b1190fbc2f9660b7d307fc7c14989fd309fc943e8a3a91(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a8520f0d2d6d74ec45a1f2082e83d3e732e6939a22c2ddc79d991f420302e3a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12432e1def54ab4a8f04be84e5c6032d7e4e0a9729dd56c51d2a540eba8e288f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a69f6615b451a52d4025f39af3ea110a1c305a7cdf1975b5123db464c9ffcf3f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c023ccc3b14f458b3a26d5ffc7c47fd30417efe1fe064fd6fd8bfd72e6d5e36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cefdf23808a2bdd45df2cf7fdfa0ed6c8e067eb54cff24649619ea00c07799a(
    value: typing.Union[_IResolvable_da3f097b, CfnAutomationRule.ScheduleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5587f4f44ca9843d0dc165c34e813a55d83d5f5c1836a85325aaad770147bdf6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__289c65c0a5bac1427b11926c90763f1770bba7a367f702daa76bf305c29df78e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAutomationRule.CriteriaProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ee341245a5bb3d3bb5f3425b715d93b07153893d5c394f7062a07979fa20b91(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8693308b84990e1940e6d8125c64fb152e7c9a52301f3933e9018615cc0c821b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAutomationRule.OrganizationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68a0a555e99d5fd4d7f6532a47a52406a7b848025f50626d6fb58f632c8e83e4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fd58f76e153d14a2da3d1d4038d7af1ef5ef2e85cee2b7eff1735fa6050e261(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2221beabcf689a62effe3e9503319e5b021178f2776807f8a84226f47b1072b5(
    *,
    ebs_volume_size_in_gib: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.IntegerCriteriaConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ebs_volume_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringCriteriaConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    estimated_monthly_savings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.DoubleCriteriaConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    look_back_period_in_days: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.IntegerCriteriaConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    region: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringCriteriaConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringCriteriaConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_tag: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.ResourceTagsCriteriaConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    restart_needed: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.StringCriteriaConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9dce0c17f96960de6116298c67e2feb2bf6a7257e20aa39bd6dd3c36b4cbc9f(
    *,
    comparison: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Union[typing.Sequence[jsii.Number], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63a1a744e2a11f80314f00a1509ab739f3ac5c054f9f670718151b5e36cfb5ce(
    *,
    comparison: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Union[typing.Sequence[jsii.Number], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23f66489eba80548b6b94027d2051adc2b1428ef11d2360412fe72167a8dbabe(
    *,
    account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    rule_apply_order: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdcf2ae259b8562f6d66cb179cd5ce41ecfa75902600227ae3631ea1396db569(
    *,
    comparison: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf7de7511c121ed491996afe46004f5a86ee28c95724278fbc25812f44bc65b(
    *,
    execution_window_in_minutes: typing.Optional[jsii.Number] = None,
    schedule_expression: typing.Optional[builtins.str] = None,
    schedule_expression_timezone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0c234cd251c7890ce9b10e125fa4606918e5c69ee8a2cd6f0bcab295a4edc0c(
    *,
    comparison: typing.Optional[builtins.str] = None,
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__929667fe90449fbcfe9926f80a0cba1fdf4f24a92c992f3b1f7bb0d8c5fa25f1(
    *,
    name: builtins.str,
    recommended_action_types: typing.Sequence[builtins.str],
    rule_type: builtins.str,
    schedule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]],
    status: builtins.str,
    criteria: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.CriteriaProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    organization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAutomationRule.OrganizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    priority: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
