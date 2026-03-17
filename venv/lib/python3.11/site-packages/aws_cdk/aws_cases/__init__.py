r'''
# AWS::Cases Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_cases as cases
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Cases construct libraries](https://constructs.dev/search?q=cases)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Cases resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cases.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Cases](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Cases.html).

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
from ..interfaces.aws_cases import (
    CaseRuleReference as _CaseRuleReference_d0790989,
    DomainReference as _DomainReference_d2c6c2d3,
    FieldReference as _FieldReference_fe6fb375,
    ICaseRuleRef as _ICaseRuleRef_1c88c99d,
    IDomainRef as _IDomainRef_33d4824f,
    IFieldRef as _IFieldRef_7e261b31,
    ILayoutRef as _ILayoutRef_a52de4c5,
    ITemplateRef as _ITemplateRef_ec2e69cd,
    LayoutReference as _LayoutReference_04b63999,
    TemplateReference as _TemplateReference_bdb1c2f7,
)


@jsii.implements(_IInspectable_c2943556, _ICaseRuleRef_1c88c99d, _ITaggableV2_4e6798f8)
class CfnCaseRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cases.CfnCaseRule",
):
    '''Creates a new case rule.

    In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see `Add case field conditions to a case template <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-caserule.html
    :cloudformationResource: AWS::Cases::CaseRule
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cases as cases
        
        # empty_value: Any
        
        cfn_case_rule = cases.CfnCaseRule(self, "MyCfnCaseRule",
            name="name",
            rule=cases.CfnCaseRule.CaseRuleDetailsProperty(
                hidden=cases.CfnCaseRule.HiddenCaseRuleProperty(
                    conditions=[cases.CfnCaseRule.BooleanConditionProperty(
                        equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                            operand_one=cases.CfnCaseRule.OperandOneProperty(
                                field_id="fieldId"
                            ),
                            operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            ),
                            result=False
                        ),
                        not_equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                            operand_one=cases.CfnCaseRule.OperandOneProperty(
                                field_id="fieldId"
                            ),
                            operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            ),
                            result=False
                        )
                    )],
                    default_value=False
                ),
                required=cases.CfnCaseRule.RequiredCaseRuleProperty(
                    conditions=[cases.CfnCaseRule.BooleanConditionProperty(
                        equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                            operand_one=cases.CfnCaseRule.OperandOneProperty(
                                field_id="fieldId"
                            ),
                            operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            ),
                            result=False
                        ),
                        not_equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                            operand_one=cases.CfnCaseRule.OperandOneProperty(
                                field_id="fieldId"
                            ),
                            operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            ),
                            result=False
                        )
                    )],
                    default_value=False
                )
            ),
        
            # the properties below are optional
            description="description",
            domain_id="domainId",
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
        rule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCaseRule.CaseRuleDetailsProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        domain_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Cases::CaseRule``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Name of the case rule.
        :param rule: Represents what rule type should take place, under what conditions.
        :param description: Description of a case rule.
        :param domain_id: Unique identifier of a Cases domain.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be714901cc3ca1265b6c09c9f45312daac0e3e7940822b521a65617830120426)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCaseRuleProps(
            name=name,
            rule=rule,
            description=description,
            domain_id=domain_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForCaseRule")
    @builtins.classmethod
    def arn_for_case_rule(cls, resource: "_ICaseRuleRef_1c88c99d") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93467cf9959aadeb4bb3766dca0729fe8561ee38e3a3d2aa0f1f70184f6902c1)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForCaseRule", [resource]))

    @jsii.member(jsii_name="isCfnCaseRule")
    @builtins.classmethod
    def is_cfn_case_rule(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnCaseRule.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56b6abd99447f46ba474b9bf59ef52a71bba5deda488de30582b742741386881)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnCaseRule", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f4c2b65b4cd2bc733d8cdee680e57ec542975387b8295a77e3ee37f7f2fb2e2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__249e9f89fcddd0f18df11526741587a09da7f1d6618c67bc49d9ac6da0d69acc)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCaseRuleArn")
    def attr_case_rule_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the case rule.

        :cloudformationAttribute: CaseRuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCaseRuleArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCaseRuleId")
    def attr_case_rule_id(self) -> builtins.str:
        '''Unique identifier of a case rule.

        :cloudformationAttribute: CaseRuleId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCaseRuleId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp when the resource was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''Timestamp when the resource was created or last modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="caseRuleRef")
    def case_rule_ref(self) -> "_CaseRuleReference_d0790989":
        '''A reference to a CaseRule resource.'''
        return typing.cast("_CaseRuleReference_d0790989", jsii.get(self, "caseRuleRef"))

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
        '''Name of the case rule.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13dd45cca814c5bbdd6da4202994c0857c4726f2e7e84a76e317304c2d048f57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnCaseRule.CaseRuleDetailsProperty"]:
        '''Represents what rule type should take place, under what conditions.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCaseRule.CaseRuleDetailsProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnCaseRule.CaseRuleDetailsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92dc9febd4bacceeaaf366a99c7f47d67e0938c0f5952e8411347591f2ad99c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of a case rule.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64603d496c22f204cecfd9754c6a349ffe0d3326259667929019e3f1a55ca96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of a Cases domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainId"))

    @domain_id.setter
    def domain_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b3b90d538392a789f67fa43295f64d877e42dd4d7fd21c5b49ffaa52e6c5ed8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db91d0aa4955cf40c2c3524d4ad515c6dc33982f09f95c20e6f8bb73f47e9faf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnCaseRule.BooleanConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"equal_to": "equalTo", "not_equal_to": "notEqualTo"},
    )
    class BooleanConditionProperty:
        def __init__(
            self,
            *,
            equal_to: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCaseRule.BooleanOperandsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            not_equal_to: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCaseRule.BooleanOperandsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Boolean condition for a rule.

            In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see `Add case field conditions to a case template <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ .

            :param equal_to: Tests that operandOne is equal to operandTwo.
            :param not_equal_to: Tests that operandOne is not equal to operandTwo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-booleancondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                # empty_value: Any
                
                boolean_condition_property = cases.CfnCaseRule.BooleanConditionProperty(
                    equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                        operand_one=cases.CfnCaseRule.OperandOneProperty(
                            field_id="fieldId"
                        ),
                        operand_two=cases.CfnCaseRule.OperandTwoProperty(
                            boolean_value=False,
                            double_value=123,
                            empty_value=empty_value,
                            string_value="stringValue"
                        ),
                        result=False
                    ),
                    not_equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                        operand_one=cases.CfnCaseRule.OperandOneProperty(
                            field_id="fieldId"
                        ),
                        operand_two=cases.CfnCaseRule.OperandTwoProperty(
                            boolean_value=False,
                            double_value=123,
                            empty_value=empty_value,
                            string_value="stringValue"
                        ),
                        result=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__df4249487c59524cb034fa3797a87de6b9254c5de1f35f9224cd3c3b632552b3)
                check_type(argname="argument equal_to", value=equal_to, expected_type=type_hints["equal_to"])
                check_type(argname="argument not_equal_to", value=not_equal_to, expected_type=type_hints["not_equal_to"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if equal_to is not None:
                self._values["equal_to"] = equal_to
            if not_equal_to is not None:
                self._values["not_equal_to"] = not_equal_to

        @builtins.property
        def equal_to(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.BooleanOperandsProperty"]]:
            '''Tests that operandOne is equal to operandTwo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-booleancondition.html#cfn-cases-caserule-booleancondition-equalto
            '''
            result = self._values.get("equal_to")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.BooleanOperandsProperty"]], result)

        @builtins.property
        def not_equal_to(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.BooleanOperandsProperty"]]:
            '''Tests that operandOne is not equal to operandTwo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-booleancondition.html#cfn-cases-caserule-booleancondition-notequalto
            '''
            result = self._values.get("not_equal_to")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.BooleanOperandsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BooleanConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnCaseRule.BooleanOperandsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "operand_one": "operandOne",
            "operand_two": "operandTwo",
            "result": "result",
        },
    )
    class BooleanOperandsProperty:
        def __init__(
            self,
            *,
            operand_one: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCaseRule.OperandOneProperty", typing.Dict[builtins.str, typing.Any]]],
            operand_two: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCaseRule.OperandTwoProperty", typing.Dict[builtins.str, typing.Any]]],
            result: typing.Union[builtins.bool, "_IResolvable_da3f097b"],
        ) -> None:
            '''Boolean operands for a condition.

            In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see `Add case field conditions to a case template <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ .

            :param operand_one: Represents the left hand operand in the condition.
            :param operand_two: Represents the right hand operand in the condition.
            :param result: The value of the outer rule if the condition evaluates to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-booleanoperands.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                # empty_value: Any
                
                boolean_operands_property = cases.CfnCaseRule.BooleanOperandsProperty(
                    operand_one=cases.CfnCaseRule.OperandOneProperty(
                        field_id="fieldId"
                    ),
                    operand_two=cases.CfnCaseRule.OperandTwoProperty(
                        boolean_value=False,
                        double_value=123,
                        empty_value=empty_value,
                        string_value="stringValue"
                    ),
                    result=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35693153797cf629f05fba2faef88f79c12830dde58774367117b676866e613c)
                check_type(argname="argument operand_one", value=operand_one, expected_type=type_hints["operand_one"])
                check_type(argname="argument operand_two", value=operand_two, expected_type=type_hints["operand_two"])
                check_type(argname="argument result", value=result, expected_type=type_hints["result"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "operand_one": operand_one,
                "operand_two": operand_two,
                "result": result,
            }

        @builtins.property
        def operand_one(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnCaseRule.OperandOneProperty"]:
            '''Represents the left hand operand in the condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-booleanoperands.html#cfn-cases-caserule-booleanoperands-operandone
            '''
            result = self._values.get("operand_one")
            assert result is not None, "Required property 'operand_one' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCaseRule.OperandOneProperty"], result)

        @builtins.property
        def operand_two(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnCaseRule.OperandTwoProperty"]:
            '''Represents the right hand operand in the condition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-booleanoperands.html#cfn-cases-caserule-booleanoperands-operandtwo
            '''
            result = self._values.get("operand_two")
            assert result is not None, "Required property 'operand_two' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCaseRule.OperandTwoProperty"], result)

        @builtins.property
        def result(self) -> typing.Union[builtins.bool, "_IResolvable_da3f097b"]:
            '''The value of the outer rule if the condition evaluates to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-booleanoperands.html#cfn-cases-caserule-booleanoperands-result
            '''
            result = self._values.get("result")
            assert result is not None, "Required property 'result' is missing"
            return typing.cast(typing.Union[builtins.bool, "_IResolvable_da3f097b"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BooleanOperandsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnCaseRule.CaseRuleDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"hidden": "hidden", "required": "required"},
    )
    class CaseRuleDetailsProperty:
        def __init__(
            self,
            *,
            hidden: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCaseRule.HiddenCaseRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            required: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCaseRule.RequiredCaseRuleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Represents what rule type should take place, under what conditions.

            In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see `Add case field conditions to a case template <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ .

            :param hidden: Whether a field is visible, based on values in other fields.
            :param required: Required rule type, used to indicate whether a field is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-caseruledetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                # empty_value: Any
                
                case_rule_details_property = cases.CfnCaseRule.CaseRuleDetailsProperty(
                    hidden=cases.CfnCaseRule.HiddenCaseRuleProperty(
                        conditions=[cases.CfnCaseRule.BooleanConditionProperty(
                            equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                                operand_one=cases.CfnCaseRule.OperandOneProperty(
                                    field_id="fieldId"
                                ),
                                operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                    boolean_value=False,
                                    double_value=123,
                                    empty_value=empty_value,
                                    string_value="stringValue"
                                ),
                                result=False
                            ),
                            not_equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                                operand_one=cases.CfnCaseRule.OperandOneProperty(
                                    field_id="fieldId"
                                ),
                                operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                    boolean_value=False,
                                    double_value=123,
                                    empty_value=empty_value,
                                    string_value="stringValue"
                                ),
                                result=False
                            )
                        )],
                        default_value=False
                    ),
                    required=cases.CfnCaseRule.RequiredCaseRuleProperty(
                        conditions=[cases.CfnCaseRule.BooleanConditionProperty(
                            equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                                operand_one=cases.CfnCaseRule.OperandOneProperty(
                                    field_id="fieldId"
                                ),
                                operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                    boolean_value=False,
                                    double_value=123,
                                    empty_value=empty_value,
                                    string_value="stringValue"
                                ),
                                result=False
                            ),
                            not_equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                                operand_one=cases.CfnCaseRule.OperandOneProperty(
                                    field_id="fieldId"
                                ),
                                operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                    boolean_value=False,
                                    double_value=123,
                                    empty_value=empty_value,
                                    string_value="stringValue"
                                ),
                                result=False
                            )
                        )],
                        default_value=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc3771a6a1ed4894f94f30a934757635b8650efee028c69611f77a028c228477)
                check_type(argname="argument hidden", value=hidden, expected_type=type_hints["hidden"])
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if hidden is not None:
                self._values["hidden"] = hidden
            if required is not None:
                self._values["required"] = required

        @builtins.property
        def hidden(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.HiddenCaseRuleProperty"]]:
            '''Whether a field is visible, based on values in other fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-caseruledetails.html#cfn-cases-caserule-caseruledetails-hidden
            '''
            result = self._values.get("hidden")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.HiddenCaseRuleProperty"]], result)

        @builtins.property
        def required(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.RequiredCaseRuleProperty"]]:
            '''Required rule type, used to indicate whether a field is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-caseruledetails.html#cfn-cases-caserule-caseruledetails-required
            '''
            result = self._values.get("required")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.RequiredCaseRuleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CaseRuleDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnCaseRule.HiddenCaseRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"conditions": "conditions", "default_value": "defaultValue"},
    )
    class HiddenCaseRuleProperty:
        def __init__(
            self,
            *,
            conditions: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCaseRule.BooleanConditionProperty", typing.Dict[builtins.str, typing.Any]]]]],
            default_value: typing.Union[builtins.bool, "_IResolvable_da3f097b"],
        ) -> None:
            '''A rule that controls field visibility based on conditions.

            Fields can be shown or hidden dynamically based on values in other fields.

            :param conditions: A list of conditions that determine field visibility.
            :param default_value: Whether the field is hidden when no conditions match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-hiddencaserule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                # empty_value: Any
                
                hidden_case_rule_property = cases.CfnCaseRule.HiddenCaseRuleProperty(
                    conditions=[cases.CfnCaseRule.BooleanConditionProperty(
                        equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                            operand_one=cases.CfnCaseRule.OperandOneProperty(
                                field_id="fieldId"
                            ),
                            operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            ),
                            result=False
                        ),
                        not_equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                            operand_one=cases.CfnCaseRule.OperandOneProperty(
                                field_id="fieldId"
                            ),
                            operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            ),
                            result=False
                        )
                    )],
                    default_value=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab16d965f772c647d0f3f9a94708326a10c2cbf8f8e1826203c8df82b75c5b25)
                check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "conditions": conditions,
                "default_value": default_value,
            }

        @builtins.property
        def conditions(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.BooleanConditionProperty"]]]:
            '''A list of conditions that determine field visibility.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-hiddencaserule.html#cfn-cases-caserule-hiddencaserule-conditions
            '''
            result = self._values.get("conditions")
            assert result is not None, "Required property 'conditions' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.BooleanConditionProperty"]]], result)

        @builtins.property
        def default_value(self) -> typing.Union[builtins.bool, "_IResolvable_da3f097b"]:
            '''Whether the field is hidden when no conditions match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-hiddencaserule.html#cfn-cases-caserule-hiddencaserule-defaultvalue
            '''
            result = self._values.get("default_value")
            assert result is not None, "Required property 'default_value' is missing"
            return typing.cast(typing.Union[builtins.bool, "_IResolvable_da3f097b"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HiddenCaseRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnCaseRule.OperandOneProperty",
        jsii_struct_bases=[],
        name_mapping={"field_id": "fieldId"},
    )
    class OperandOneProperty:
        def __init__(self, *, field_id: builtins.str) -> None:
            '''Represents the left hand operand in the condition.

            In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see `Add case field conditions to a case template <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ .

            :param field_id: The field ID that this operand should take the value of.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-operandone.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                operand_one_property = cases.CfnCaseRule.OperandOneProperty(
                    field_id="fieldId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f3ebdf598c47771ea6d6e5ad126842fc398674ea20c21b3cbeae3096f59eb3bc)
                check_type(argname="argument field_id", value=field_id, expected_type=type_hints["field_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_id": field_id,
            }

        @builtins.property
        def field_id(self) -> builtins.str:
            '''The field ID that this operand should take the value of.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-operandone.html#cfn-cases-caserule-operandone-fieldid
            '''
            result = self._values.get("field_id")
            assert result is not None, "Required property 'field_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OperandOneProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnCaseRule.OperandTwoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "boolean_value": "booleanValue",
            "double_value": "doubleValue",
            "empty_value": "emptyValue",
            "string_value": "stringValue",
        },
    )
    class OperandTwoProperty:
        def __init__(
            self,
            *,
            boolean_value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
            double_value: typing.Optional[jsii.Number] = None,
            empty_value: typing.Any = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents the right hand operand in the condition.

            In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see `Add case field conditions to a case template <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ .

            :param boolean_value: Boolean value type.
            :param double_value: Double value type.
            :param empty_value: Represents an empty operand value. In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see `Add case field conditions to a case template <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ .
            :param string_value: String value type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-operandtwo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                # empty_value: Any
                
                operand_two_property = cases.CfnCaseRule.OperandTwoProperty(
                    boolean_value=False,
                    double_value=123,
                    empty_value=empty_value,
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8521fb882be1d6ce495bee9db5b66d8a60a8e86f3b73198e53ab5bfb4a895afe)
                check_type(argname="argument boolean_value", value=boolean_value, expected_type=type_hints["boolean_value"])
                check_type(argname="argument double_value", value=double_value, expected_type=type_hints["double_value"])
                check_type(argname="argument empty_value", value=empty_value, expected_type=type_hints["empty_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if boolean_value is not None:
                self._values["boolean_value"] = boolean_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if empty_value is not None:
                self._values["empty_value"] = empty_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def boolean_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''Boolean value type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-operandtwo.html#cfn-cases-caserule-operandtwo-booleanvalue
            '''
            result = self._values.get("boolean_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        @builtins.property
        def double_value(self) -> typing.Optional[jsii.Number]:
            '''Double value type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-operandtwo.html#cfn-cases-caserule-operandtwo-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def empty_value(self) -> typing.Any:
            '''Represents an empty operand value.

            In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see `Add case field conditions to a case template <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-operandtwo.html#cfn-cases-caserule-operandtwo-emptyvalue
            '''
            result = self._values.get("empty_value")
            return typing.cast(typing.Any, result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''String value type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-operandtwo.html#cfn-cases-caserule-operandtwo-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OperandTwoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnCaseRule.RequiredCaseRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"conditions": "conditions", "default_value": "defaultValue"},
    )
    class RequiredCaseRuleProperty:
        def __init__(
            self,
            *,
            conditions: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCaseRule.BooleanConditionProperty", typing.Dict[builtins.str, typing.Any]]]]],
            default_value: typing.Union[builtins.bool, "_IResolvable_da3f097b"],
        ) -> None:
            '''Required rule type, used to indicate whether a field is required.

            In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see `Add case field conditions to a case template <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ .

            :param conditions: List of conditions for the required rule; the first condition to evaluate to true dictates the value of the rule.
            :param default_value: The value of the rule (that is, whether the field is required) should none of the conditions evaluate to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-requiredcaserule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                # empty_value: Any
                
                required_case_rule_property = cases.CfnCaseRule.RequiredCaseRuleProperty(
                    conditions=[cases.CfnCaseRule.BooleanConditionProperty(
                        equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                            operand_one=cases.CfnCaseRule.OperandOneProperty(
                                field_id="fieldId"
                            ),
                            operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            ),
                            result=False
                        ),
                        not_equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                            operand_one=cases.CfnCaseRule.OperandOneProperty(
                                field_id="fieldId"
                            ),
                            operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                boolean_value=False,
                                double_value=123,
                                empty_value=empty_value,
                                string_value="stringValue"
                            ),
                            result=False
                        )
                    )],
                    default_value=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c28b76d95a2316f80a4c07df9a415656b3bd000097eeb21fd7249e3eda3e22b1)
                check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
                check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "conditions": conditions,
                "default_value": default_value,
            }

        @builtins.property
        def conditions(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.BooleanConditionProperty"]]]:
            '''List of conditions for the required rule;

            the first condition to evaluate to true dictates the value of the rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-requiredcaserule.html#cfn-cases-caserule-requiredcaserule-conditions
            '''
            result = self._values.get("conditions")
            assert result is not None, "Required property 'conditions' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnCaseRule.BooleanConditionProperty"]]], result)

        @builtins.property
        def default_value(self) -> typing.Union[builtins.bool, "_IResolvable_da3f097b"]:
            '''The value of the rule (that is, whether the field is required) should none of the conditions evaluate to true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-caserule-requiredcaserule.html#cfn-cases-caserule-requiredcaserule-defaultvalue
            '''
            result = self._values.get("default_value")
            assert result is not None, "Required property 'default_value' is missing"
            return typing.cast(typing.Union[builtins.bool, "_IResolvable_da3f097b"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RequiredCaseRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cases.CfnCaseRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "rule": "rule",
        "description": "description",
        "domain_id": "domainId",
        "tags": "tags",
    },
)
class CfnCaseRuleProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        rule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCaseRule.CaseRuleDetailsProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        domain_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCaseRule``.

        :param name: Name of the case rule.
        :param rule: Represents what rule type should take place, under what conditions.
        :param description: Description of a case rule.
        :param domain_id: Unique identifier of a Cases domain.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-caserule.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cases as cases
            
            # empty_value: Any
            
            cfn_case_rule_props = cases.CfnCaseRuleProps(
                name="name",
                rule=cases.CfnCaseRule.CaseRuleDetailsProperty(
                    hidden=cases.CfnCaseRule.HiddenCaseRuleProperty(
                        conditions=[cases.CfnCaseRule.BooleanConditionProperty(
                            equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                                operand_one=cases.CfnCaseRule.OperandOneProperty(
                                    field_id="fieldId"
                                ),
                                operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                    boolean_value=False,
                                    double_value=123,
                                    empty_value=empty_value,
                                    string_value="stringValue"
                                ),
                                result=False
                            ),
                            not_equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                                operand_one=cases.CfnCaseRule.OperandOneProperty(
                                    field_id="fieldId"
                                ),
                                operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                    boolean_value=False,
                                    double_value=123,
                                    empty_value=empty_value,
                                    string_value="stringValue"
                                ),
                                result=False
                            )
                        )],
                        default_value=False
                    ),
                    required=cases.CfnCaseRule.RequiredCaseRuleProperty(
                        conditions=[cases.CfnCaseRule.BooleanConditionProperty(
                            equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                                operand_one=cases.CfnCaseRule.OperandOneProperty(
                                    field_id="fieldId"
                                ),
                                operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                    boolean_value=False,
                                    double_value=123,
                                    empty_value=empty_value,
                                    string_value="stringValue"
                                ),
                                result=False
                            ),
                            not_equal_to=cases.CfnCaseRule.BooleanOperandsProperty(
                                operand_one=cases.CfnCaseRule.OperandOneProperty(
                                    field_id="fieldId"
                                ),
                                operand_two=cases.CfnCaseRule.OperandTwoProperty(
                                    boolean_value=False,
                                    double_value=123,
                                    empty_value=empty_value,
                                    string_value="stringValue"
                                ),
                                result=False
                            )
                        )],
                        default_value=False
                    )
                ),
            
                # the properties below are optional
                description="description",
                domain_id="domainId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acdfca63e703957a2887afa7cda824f46a8e8e2c23e4d73ff036bed38b4af0fd)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "rule": rule,
        }
        if description is not None:
            self._values["description"] = description
        if domain_id is not None:
            self._values["domain_id"] = domain_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the case rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-caserule.html#cfn-cases-caserule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnCaseRule.CaseRuleDetailsProperty"]:
        '''Represents what rule type should take place, under what conditions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-caserule.html#cfn-cases-caserule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCaseRule.CaseRuleDetailsProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of a case rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-caserule.html#cfn-cases-caserule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_id(self) -> typing.Optional[builtins.str]:
        '''Unique identifier of a Cases domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-caserule.html#cfn-cases-caserule-domainid
        '''
        result = self._values.get("domain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-caserule.html#cfn-cases-caserule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCaseRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IDomainRef_33d4824f, _ITaggableV2_4e6798f8)
class CfnDomain(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cases.CfnDomain",
):
    '''Creates a domain, which is a container for all case data, such as cases, fields, templates and layouts.

    Each Amazon Connect instance can be associated with only one Cases domain.
    .. epigraph::

       This will not associate your connect instance to Cases domain. Instead, use the Amazon Connect `CreateIntegrationAssociation <https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateIntegrationAssociation.html>`_ API. You need specific IAM permissions to successfully associate the Cases domain. For more information, see `Onboard to Cases <https://docs.aws.amazon.com/connect/latest/adminguide/required-permissions-iam-cases.html#onboard-cases-iam>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-domain.html
    :cloudformationResource: AWS::Cases::Domain
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cases as cases
        
        cfn_domain = cases.CfnDomain(self, "MyCfnDomain",
            name="name",
        
            # the properties below are optional
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
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Cases::Domain``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the domain.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d298307ba0303a9fe1610ecc75a8c64a40ec633c78a7086fcf29107195ecc95e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainProps(name=name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDomain")
    @builtins.classmethod
    def arn_for_domain(cls, resource: "_IDomainRef_33d4824f") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd539bc6977de897be38e725e6f6c4c2590ae4659e4684ee78e8554b64d2e3c7)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDomain", [resource]))

    @jsii.member(jsii_name="isCfnDomain")
    @builtins.classmethod
    def is_cfn_domain(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDomain.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__295dd97e2c7a21b30ad43ac334e7cca35a83c02d41c91121f0a806ba56a49c65)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDomain", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a75062eae4f9c9d498de7b6d1ee80f581181c7d02a194552b0d581ffb1c398ba)
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
            type_hints = typing.get_type_hints(_typecheckingstub__116abd9be95df9971c61764ff30f094e9bd1dac949084d3b8fe64dbec5f2245c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''The timestamp when the Cases domain was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainArn")
    def attr_domain_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for the Cases domain.

        :cloudformationAttribute: DomainArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainId")
    def attr_domain_id(self) -> builtins.str:
        '''The unique identifier of the Cases domain.

        :cloudformationAttribute: DomainId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainId"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainStatus")
    def attr_domain_status(self) -> builtins.str:
        '''The status of the Cases domain.

        :cloudformationAttribute: DomainStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainStatus"))

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
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "_DomainReference_d2c6c2d3":
        '''A reference to a Domain resource.'''
        return typing.cast("_DomainReference_d2c6c2d3", jsii.get(self, "domainRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the domain.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c83159d7196ff79c0f6fa249f1db9fb9ccc50594779c0aa3a16171e66bd828c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__998f4debbdc1c26247b0286ad29fa49e7dbb53c3b893a589e9075532ccafc84a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cases.CfnDomainProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "tags": "tags"},
)
class CfnDomainProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDomain``.

        :param name: The name of the domain.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-domain.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cases as cases
            
            cfn_domain_props = cases.CfnDomainProps(
                name="name",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d88254a528e2b091b4329dbc80c35c7196bbee8b179f85fcb31572279262beb7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-domain.html#cfn-cases-domain-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-domain.html#cfn-cases-domain-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IFieldRef_7e261b31, _ITaggableV2_4e6798f8)
class CfnField(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cases.CfnField",
):
    '''Creates a field in the Cases domain.

    This field is used to define the case object model (that is, defines what data can be captured on cases) in a Cases domain.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-field.html
    :cloudformationResource: AWS::Cases::Field
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cases as cases
        
        cfn_field = cases.CfnField(self, "MyCfnField",
            name="name",
            type="type",
        
            # the properties below are optional
            attributes=cases.CfnField.FieldAttributesProperty(
                text=cases.CfnField.TextAttributesProperty(
                    is_multiline=False
                )
            ),
            description="description",
            domain_id="domainId",
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
        type: builtins.str,
        attributes: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnField.FieldAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        domain_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Cases::Field``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: Name of the field.
        :param type: Type of the field.
        :param attributes: Union of field attributes.
        :param description: Description of the field.
        :param domain_id: The unique identifier of the Cases domain.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd620a5620fd7cf34e28f8693796fb9f7ddd93fcd8c7695281c08776fd5637c4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFieldProps(
            name=name,
            type=type,
            attributes=attributes,
            description=description,
            domain_id=domain_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForField")
    @builtins.classmethod
    def arn_for_field(cls, resource: "_IFieldRef_7e261b31") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a27bd368427051c3694255650751a1197598780a0c7121b0b4b5d7291c4a1b5)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForField", [resource]))

    @jsii.member(jsii_name="isCfnField")
    @builtins.classmethod
    def is_cfn_field(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnField.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__566062392071e68ef8b0cf9595573f28d45f57385207a9e32450727a0b5ed13d)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnField", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c5fd8d77f5f953c376f74388e62da11d1f407de6f8a91a501869e14ce425f59)
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
            type_hints = typing.get_type_hints(_typecheckingstub__11cf77aa3a0c2eda415b9e175451eb47b72f48c2b11b952fff8b2482baadbba2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp at which the resource was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrFieldArn")
    def attr_field_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the field.

        :cloudformationAttribute: FieldArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFieldArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFieldId")
    def attr_field_id(self) -> builtins.str:
        '''Unique identifier of the field.

        :cloudformationAttribute: FieldId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFieldId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''Timestamp at which the resource was created or last modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrNamespace")
    def attr_namespace(self) -> builtins.str:
        '''Namespace of the field.

        :cloudformationAttribute: Namespace
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNamespace"))

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
    @jsii.member(jsii_name="fieldRef")
    def field_ref(self) -> "_FieldReference_fe6fb375":
        '''A reference to a Field resource.'''
        return typing.cast("_FieldReference_fe6fb375", jsii.get(self, "fieldRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the field.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9ecb0f4d6cc53f6ec951e68b2d051c56c71741a321f58509aede864cb5e6826)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''Type of the field.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d1ce71132b61a56132ed0e80dbe19e4967ff0b2b1c54f168b872efaa9e1cfea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnField.FieldAttributesProperty"]]:
        '''Union of field attributes.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnField.FieldAttributesProperty"]], jsii.get(self, "attributes"))

    @attributes.setter
    def attributes(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnField.FieldAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec9d872641de59c09d1a4aa0f22acf0a4b6384bca238c55b5acd984fda658ff1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attributes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the field.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8bb005f1b34005da816178413750d75ad68393cadf6b2e46830cb4281e557b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Cases domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainId"))

    @domain_id.setter
    def domain_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7ecc904aa381d23a54963bced6be7ceabe396747de3cba4c83b76632085446e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8dde35cd2abf2847d466bfc9448c8228fd804275187398cf2ef8bdeb0c284a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnField.FieldAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"text": "text"},
    )
    class FieldAttributesProperty:
        def __init__(
            self,
            *,
            text: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnField.TextAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Union of field attributes.

            :param text: Field attributes for Text field type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-field-fieldattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                field_attributes_property = cases.CfnField.FieldAttributesProperty(
                    text=cases.CfnField.TextAttributesProperty(
                        is_multiline=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__523ee0d133ea645c43762c2e235a9493a7f2cfc762459ff52a9acf636d7003cb)
                check_type(argname="argument text", value=text, expected_type=type_hints["text"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if text is not None:
                self._values["text"] = text

        @builtins.property
        def text(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnField.TextAttributesProperty"]]:
            '''Field attributes for Text field type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-field-fieldattributes.html#cfn-cases-field-fieldattributes-text
            '''
            result = self._values.get("text")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnField.TextAttributesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnField.TextAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"is_multiline": "isMultiline"},
    )
    class TextAttributesProperty:
        def __init__(
            self,
            *,
            is_multiline: typing.Union[builtins.bool, "_IResolvable_da3f097b"],
        ) -> None:
            '''Field attributes for Text field type.

            :param is_multiline: Attribute that defines rendering component and validation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-field-textattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                text_attributes_property = cases.CfnField.TextAttributesProperty(
                    is_multiline=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__740b2578760e7393305d88b48521a3000c613a1625cdd16b4967f671c06692ff)
                check_type(argname="argument is_multiline", value=is_multiline, expected_type=type_hints["is_multiline"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_multiline": is_multiline,
            }

        @builtins.property
        def is_multiline(self) -> typing.Union[builtins.bool, "_IResolvable_da3f097b"]:
            '''Attribute that defines rendering component and validation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-field-textattributes.html#cfn-cases-field-textattributes-ismultiline
            '''
            result = self._values.get("is_multiline")
            assert result is not None, "Required property 'is_multiline' is missing"
            return typing.cast(typing.Union[builtins.bool, "_IResolvable_da3f097b"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TextAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cases.CfnFieldProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "attributes": "attributes",
        "description": "description",
        "domain_id": "domainId",
        "tags": "tags",
    },
)
class CfnFieldProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        attributes: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnField.FieldAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        domain_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnField``.

        :param name: Name of the field.
        :param type: Type of the field.
        :param attributes: Union of field attributes.
        :param description: Description of the field.
        :param domain_id: The unique identifier of the Cases domain.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-field.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cases as cases
            
            cfn_field_props = cases.CfnFieldProps(
                name="name",
                type="type",
            
                # the properties below are optional
                attributes=cases.CfnField.FieldAttributesProperty(
                    text=cases.CfnField.TextAttributesProperty(
                        is_multiline=False
                    )
                ),
                description="description",
                domain_id="domainId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03d88f5f2a426612b3094a6a5e2b1d83000a584ac3ec25a332e2eed7bf494641)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if attributes is not None:
            self._values["attributes"] = attributes
        if description is not None:
            self._values["description"] = description
        if domain_id is not None:
            self._values["domain_id"] = domain_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the field.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-field.html#cfn-cases-field-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the field.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-field.html#cfn-cases-field-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def attributes(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnField.FieldAttributesProperty"]]:
        '''Union of field attributes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-field.html#cfn-cases-field-attributes
        '''
        result = self._values.get("attributes")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnField.FieldAttributesProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the field.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-field.html#cfn-cases-field-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Cases domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-field.html#cfn-cases-field-domainid
        '''
        result = self._values.get("domain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-field.html#cfn-cases-field-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFieldProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ILayoutRef_a52de4c5, _ITaggableV2_4e6798f8)
class CfnLayout(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cases.CfnLayout",
):
    '''Creates a layout in the Cases domain.

    Layouts define the following configuration in the top section and More Info tab of the Cases user interface:

    - Fields to display to the users
    - Field ordering

    .. epigraph::

       Title and Status fields cannot be part of layouts since they are not configurable.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-layout.html
    :cloudformationResource: AWS::Cases::Layout
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cases as cases
        
        cfn_layout = cases.CfnLayout(self, "MyCfnLayout",
            content=cases.CfnLayout.LayoutContentProperty(
                basic=cases.CfnLayout.BasicLayoutProperty(
                    more_info=cases.CfnLayout.LayoutSectionsProperty(
                        sections=[cases.CfnLayout.SectionProperty(
                            field_group=cases.CfnLayout.FieldGroupProperty(
                                fields=[cases.CfnLayout.FieldItemProperty(
                                    id="id"
                                )],
        
                                # the properties below are optional
                                name="name"
                            )
                        )]
                    ),
                    top_panel=cases.CfnLayout.LayoutSectionsProperty(
                        sections=[cases.CfnLayout.SectionProperty(
                            field_group=cases.CfnLayout.FieldGroupProperty(
                                fields=[cases.CfnLayout.FieldItemProperty(
                                    id="id"
                                )],
        
                                # the properties below are optional
                                name="name"
                            )
                        )]
                    )
                )
            ),
            name="name",
        
            # the properties below are optional
            domain_id="domainId",
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
        content: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLayout.LayoutContentProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        domain_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Cases::Layout``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param content: Object to store union of different versions of layout content.
        :param name: The name of the layout.
        :param domain_id: The unique identifier of the Cases domain.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c9fa7422f8ee22f63316bc5f01e73cff1246061d3b06956469d253d4a721ff2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLayoutProps(
            content=content, name=name, domain_id=domain_id, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForLayout")
    @builtins.classmethod
    def arn_for_layout(cls, resource: "_ILayoutRef_a52de4c5") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__306d13638a5891ae6181bcbd786fb8ff397f5025b2fee0f07d66db26d2c9f4a2)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForLayout", [resource]))

    @jsii.member(jsii_name="isCfnLayout")
    @builtins.classmethod
    def is_cfn_layout(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnLayout.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33e2d34da52e5162187fed27c9e71a4d14983ce37ffe60077d5e81ce122e83c2)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnLayout", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0108f8e268d5824ab934bec99da3797910ae831dc29b172eed25f527478b03b1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__979e050ce8841db5620a702590d6ee159b10a022921439387b4bb221ec6fc7f4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp at which the resource was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''Timestamp at which the resource was created or last modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLayoutArn")
    def attr_layout_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the newly created layout.

        :cloudformationAttribute: LayoutArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLayoutArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLayoutId")
    def attr_layout_id(self) -> builtins.str:
        '''The unique identifier of the layout.

        :cloudformationAttribute: LayoutId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLayoutId"))

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
    @jsii.member(jsii_name="layoutRef")
    def layout_ref(self) -> "_LayoutReference_04b63999":
        '''A reference to a Layout resource.'''
        return typing.cast("_LayoutReference_04b63999", jsii.get(self, "layoutRef"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnLayout.LayoutContentProperty"]:
        '''Object to store union of different versions of layout content.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLayout.LayoutContentProperty"], jsii.get(self, "content"))

    @content.setter
    def content(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnLayout.LayoutContentProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dacaa2887466f35305aed2bb0e241add3bde7d5ca3e29f59cef3c705eddf2dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the layout.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c70dc22f467d60c06701a6fc1654aa7442d219a686c18b125b3ee753d1c3125)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Cases domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainId"))

    @domain_id.setter
    def domain_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d00a3dab4c0a4f500e5ad5bbc5cf586a4e0469241193da7ba58edb230dd7ba7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec7b486db8f5df2a9d1f86e377af46e5cd73476965bd8092d57ecf9409531f89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnLayout.BasicLayoutProperty",
        jsii_struct_bases=[],
        name_mapping={"more_info": "moreInfo", "top_panel": "topPanel"},
    )
    class BasicLayoutProperty:
        def __init__(
            self,
            *,
            more_info: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLayout.LayoutSectionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            top_panel: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLayout.LayoutSectionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Content specific to ``BasicLayout`` type.

            It configures fields in the top panel and More Info tab of agent application.

            :param more_info: This represents sections in a tab of the page layout.
            :param top_panel: This represents sections in a panel of the page layout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-basiclayout.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                basic_layout_property = cases.CfnLayout.BasicLayoutProperty(
                    more_info=cases.CfnLayout.LayoutSectionsProperty(
                        sections=[cases.CfnLayout.SectionProperty(
                            field_group=cases.CfnLayout.FieldGroupProperty(
                                fields=[cases.CfnLayout.FieldItemProperty(
                                    id="id"
                                )],
                
                                # the properties below are optional
                                name="name"
                            )
                        )]
                    ),
                    top_panel=cases.CfnLayout.LayoutSectionsProperty(
                        sections=[cases.CfnLayout.SectionProperty(
                            field_group=cases.CfnLayout.FieldGroupProperty(
                                fields=[cases.CfnLayout.FieldItemProperty(
                                    id="id"
                                )],
                
                                # the properties below are optional
                                name="name"
                            )
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4a2e643956f0c7c7f9bb872169efbb8666fec7c3453bc760ca9439eac2ef515c)
                check_type(argname="argument more_info", value=more_info, expected_type=type_hints["more_info"])
                check_type(argname="argument top_panel", value=top_panel, expected_type=type_hints["top_panel"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if more_info is not None:
                self._values["more_info"] = more_info
            if top_panel is not None:
                self._values["top_panel"] = top_panel

        @builtins.property
        def more_info(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLayout.LayoutSectionsProperty"]]:
            '''This represents sections in a tab of the page layout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-basiclayout.html#cfn-cases-layout-basiclayout-moreinfo
            '''
            result = self._values.get("more_info")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLayout.LayoutSectionsProperty"]], result)

        @builtins.property
        def top_panel(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLayout.LayoutSectionsProperty"]]:
            '''This represents sections in a panel of the page layout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-basiclayout.html#cfn-cases-layout-basiclayout-toppanel
            '''
            result = self._values.get("top_panel")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLayout.LayoutSectionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BasicLayoutProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnLayout.FieldGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"fields": "fields", "name": "name"},
    )
    class FieldGroupProperty:
        def __init__(
            self,
            *,
            fields: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLayout.FieldItemProperty", typing.Dict[builtins.str, typing.Any]]]]],
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Object for a group of fields and associated properties.

            :param fields: Represents an ordered list containing field related information.
            :param name: Name of the field group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-fieldgroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                field_group_property = cases.CfnLayout.FieldGroupProperty(
                    fields=[cases.CfnLayout.FieldItemProperty(
                        id="id"
                    )],
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3b0eb2352a44ca01fdb5d4d03c0550ca7043a9bc6c2f6eb004909d76ef2a60dc)
                check_type(argname="argument fields", value=fields, expected_type=type_hints["fields"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "fields": fields,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def fields(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLayout.FieldItemProperty"]]]:
            '''Represents an ordered list containing field related information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-fieldgroup.html#cfn-cases-layout-fieldgroup-fields
            '''
            result = self._values.get("fields")
            assert result is not None, "Required property 'fields' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLayout.FieldItemProperty"]]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''Name of the field group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-fieldgroup.html#cfn-cases-layout-fieldgroup-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnLayout.FieldItemProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id"},
    )
    class FieldItemProperty:
        def __init__(self, *, id: builtins.str) -> None:
            '''Object for field related information.

            :param id: Unique identifier of a field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-fielditem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                field_item_property = cases.CfnLayout.FieldItemProperty(
                    id="id"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d434f4adf93e300cead8b6a0be0574c74c632908463751f04d0e23ec12ebac7)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''Unique identifier of a field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-fielditem.html#cfn-cases-layout-fielditem-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnLayout.LayoutContentProperty",
        jsii_struct_bases=[],
        name_mapping={"basic": "basic"},
    )
    class LayoutContentProperty:
        def __init__(
            self,
            *,
            basic: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLayout.BasicLayoutProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Object to store union of different versions of layout content.

            :param basic: Content specific to ``BasicLayout`` type. It configures fields in the top panel and More Info tab of agent application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-layoutcontent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                layout_content_property = cases.CfnLayout.LayoutContentProperty(
                    basic=cases.CfnLayout.BasicLayoutProperty(
                        more_info=cases.CfnLayout.LayoutSectionsProperty(
                            sections=[cases.CfnLayout.SectionProperty(
                                field_group=cases.CfnLayout.FieldGroupProperty(
                                    fields=[cases.CfnLayout.FieldItemProperty(
                                        id="id"
                                    )],
                
                                    # the properties below are optional
                                    name="name"
                                )
                            )]
                        ),
                        top_panel=cases.CfnLayout.LayoutSectionsProperty(
                            sections=[cases.CfnLayout.SectionProperty(
                                field_group=cases.CfnLayout.FieldGroupProperty(
                                    fields=[cases.CfnLayout.FieldItemProperty(
                                        id="id"
                                    )],
                
                                    # the properties below are optional
                                    name="name"
                                )
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e2a92fccd31f4424fc957a39a250a7df950f0965d3f5f0c686194ba6efd758c)
                check_type(argname="argument basic", value=basic, expected_type=type_hints["basic"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "basic": basic,
            }

        @builtins.property
        def basic(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnLayout.BasicLayoutProperty"]:
            '''Content specific to ``BasicLayout`` type.

            It configures fields in the top panel and More Info tab of agent application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-layoutcontent.html#cfn-cases-layout-layoutcontent-basic
            '''
            result = self._values.get("basic")
            assert result is not None, "Required property 'basic' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLayout.BasicLayoutProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LayoutContentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnLayout.LayoutSectionsProperty",
        jsii_struct_bases=[],
        name_mapping={"sections": "sections"},
    )
    class LayoutSectionsProperty:
        def __init__(
            self,
            *,
            sections: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLayout.SectionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Ordered list containing different kinds of sections that can be added.

            A LayoutSections object can only contain one section.

            :param sections: Ordered list containing different kinds of sections that can be added. A LayoutSections object can only contain one section.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-layoutsections.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                layout_sections_property = cases.CfnLayout.LayoutSectionsProperty(
                    sections=[cases.CfnLayout.SectionProperty(
                        field_group=cases.CfnLayout.FieldGroupProperty(
                            fields=[cases.CfnLayout.FieldItemProperty(
                                id="id"
                            )],
                
                            # the properties below are optional
                            name="name"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c648193b760caef809c0779b69738304d0be665065b6a45944ed01ac844bf81)
                check_type(argname="argument sections", value=sections, expected_type=type_hints["sections"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sections is not None:
                self._values["sections"] = sections

        @builtins.property
        def sections(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLayout.SectionProperty"]]]]:
            '''Ordered list containing different kinds of sections that can be added.

            A LayoutSections object can only contain one section.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-layoutsections.html#cfn-cases-layout-layoutsections-sections
            '''
            result = self._values.get("sections")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLayout.SectionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LayoutSectionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnLayout.SectionProperty",
        jsii_struct_bases=[],
        name_mapping={"field_group": "fieldGroup"},
    )
    class SectionProperty:
        def __init__(
            self,
            *,
            field_group: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLayout.FieldGroupProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''This represents a sections within a panel or tab of the page layout.

            :param field_group: Consists of a group of fields and associated properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-section.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                section_property = cases.CfnLayout.SectionProperty(
                    field_group=cases.CfnLayout.FieldGroupProperty(
                        fields=[cases.CfnLayout.FieldItemProperty(
                            id="id"
                        )],
                
                        # the properties below are optional
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7484ee0070e8c31b70a3661555d15fbc2a34da1584110d0e29517fe1dfd717f8)
                check_type(argname="argument field_group", value=field_group, expected_type=type_hints["field_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_group": field_group,
            }

        @builtins.property
        def field_group(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnLayout.FieldGroupProperty"]:
            '''Consists of a group of fields and associated properties.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-layout-section.html#cfn-cases-layout-section-fieldgroup
            '''
            result = self._values.get("field_group")
            assert result is not None, "Required property 'field_group' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLayout.FieldGroupProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SectionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cases.CfnLayoutProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "name": "name",
        "domain_id": "domainId",
        "tags": "tags",
    },
)
class CfnLayoutProps:
    def __init__(
        self,
        *,
        content: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLayout.LayoutContentProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        domain_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLayout``.

        :param content: Object to store union of different versions of layout content.
        :param name: The name of the layout.
        :param domain_id: The unique identifier of the Cases domain.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-layout.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cases as cases
            
            cfn_layout_props = cases.CfnLayoutProps(
                content=cases.CfnLayout.LayoutContentProperty(
                    basic=cases.CfnLayout.BasicLayoutProperty(
                        more_info=cases.CfnLayout.LayoutSectionsProperty(
                            sections=[cases.CfnLayout.SectionProperty(
                                field_group=cases.CfnLayout.FieldGroupProperty(
                                    fields=[cases.CfnLayout.FieldItemProperty(
                                        id="id"
                                    )],
            
                                    # the properties below are optional
                                    name="name"
                                )
                            )]
                        ),
                        top_panel=cases.CfnLayout.LayoutSectionsProperty(
                            sections=[cases.CfnLayout.SectionProperty(
                                field_group=cases.CfnLayout.FieldGroupProperty(
                                    fields=[cases.CfnLayout.FieldItemProperty(
                                        id="id"
                                    )],
            
                                    # the properties below are optional
                                    name="name"
                                )
                            )]
                        )
                    )
                ),
                name="name",
            
                # the properties below are optional
                domain_id="domainId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fd3424821bfebd52d96fdfb554e9999528562965d811208bffae571487d205a)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "name": name,
        }
        if domain_id is not None:
            self._values["domain_id"] = domain_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnLayout.LayoutContentProperty"]:
        '''Object to store union of different versions of layout content.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-layout.html#cfn-cases-layout-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLayout.LayoutContentProperty"], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the layout.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-layout.html#cfn-cases-layout-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Cases domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-layout.html#cfn-cases-layout-domainid
        '''
        result = self._values.get("domain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-layout.html#cfn-cases-layout-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLayoutProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITemplateRef_ec2e69cd, _ITaggableV2_4e6798f8)
class CfnTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cases.CfnTemplate",
):
    '''Creates a template in the Cases domain.

    This template is used to define the case object model (that is, to define what data can be captured on cases) in a Cases domain. A template must have a unique name within a domain, and it must reference existing field IDs and layout IDs. Additionally, multiple fields with same IDs are not allowed within the same Template. A template can be either Active or Inactive, as indicated by its status. Inactive templates cannot be used to create cases.

    Other template APIs are:

    - `DeleteTemplate <https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DeleteTemplate.html>`_
    - `GetTemplate <https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetTemplate.html>`_
    - `ListTemplates <https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_ListTemplates.html>`_
    - `UpdateTemplate <https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateTemplate.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-template.html
    :cloudformationResource: AWS::Cases::Template
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_cases as cases
        
        cfn_template = cases.CfnTemplate(self, "MyCfnTemplate",
            name="name",
        
            # the properties below are optional
            description="description",
            domain_id="domainId",
            layout_configuration=cases.CfnTemplate.LayoutConfigurationProperty(
                default_layout="defaultLayout"
            ),
            required_fields=[cases.CfnTemplate.RequiredFieldProperty(
                field_id="fieldId"
            )],
            rules=[cases.CfnTemplate.TemplateRuleProperty(
                case_rule_id="caseRuleId",
        
                # the properties below are optional
                field_id="fieldId"
            )],
            status="status",
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
        description: typing.Optional[builtins.str] = None,
        domain_id: typing.Optional[builtins.str] = None,
        layout_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTemplate.LayoutConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        required_fields: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTemplate.RequiredFieldProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        rules: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTemplate.TemplateRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::Cases::Template``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The template name.
        :param description: A brief description of the template.
        :param domain_id: The unique identifier of the Cases domain.
        :param layout_configuration: Object to store configuration of layouts associated to the template.
        :param required_fields: A list of fields that must contain a value for a case to be successfully created with this template.
        :param rules: A list of case rules (also known as `case field conditions <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ ) on a template.
        :param status: The status of the template.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73cc3fdeeca49d4acd0b26f8793d1789ed977f837657e631a6a8704b2ea4dadf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTemplateProps(
            name=name,
            description=description,
            domain_id=domain_id,
            layout_configuration=layout_configuration,
            required_fields=required_fields,
            rules=rules,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForTemplate")
    @builtins.classmethod
    def arn_for_template(cls, resource: "_ITemplateRef_ec2e69cd") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10194be066646d7553d60ae9a84c5428612f34f222b449a7dded0e031c48f45b)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForTemplate", [resource]))

    @jsii.member(jsii_name="isCfnTemplate")
    @builtins.classmethod
    def is_cfn_template(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnTemplate.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd4aa7fde6507a6cb44b05a7bbbbe3de6baf437b74d05d567b3944ce9934194)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnTemplate", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d5ca9d4e4726f53933eddd12b41a1eec755cd4277ca398ca0916238900db611)
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
            type_hints = typing.get_type_hints(_typecheckingstub__644ea6fc41bf09e6dd7724125dec8d3299b9f447d80992b72415c54fdb57010a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> builtins.str:
        '''Timestamp at which the resource was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> builtins.str:
        '''Timestamp at which the resource was created or last modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrTemplateArn")
    def attr_template_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the template.

        :cloudformationAttribute: TemplateArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTemplateArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTemplateId")
    def attr_template_id(self) -> builtins.str:
        '''A unique identifier of a template.

        :cloudformationAttribute: TemplateId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTemplateId"))

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
    @jsii.member(jsii_name="templateRef")
    def template_ref(self) -> "_TemplateReference_bdb1c2f7":
        '''A reference to a Template resource.'''
        return typing.cast("_TemplateReference_bdb1c2f7", jsii.get(self, "templateRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The template name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d32f739df5a6993b0962b41dcef7c5497cca792e9aa0baeb4177304b4ff8aa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A brief description of the template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06702e040037f55cc9c42127b813db9c4e47798e192c3679ba68db40f629f291)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainId")
    def domain_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Cases domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainId"))

    @domain_id.setter
    def domain_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8640bd6b75c3f459c543a292f6b4158364ab44364655fffed58777ef1e155d8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="layoutConfiguration")
    def layout_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTemplate.LayoutConfigurationProperty"]]:
        '''Object to store configuration of layouts associated to the template.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTemplate.LayoutConfigurationProperty"]], jsii.get(self, "layoutConfiguration"))

    @layout_configuration.setter
    def layout_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTemplate.LayoutConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a4efad9b266ccf2a52ab3a5b47dc451f4db6b64bdc86869c25b535f39b87073)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "layoutConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="requiredFields")
    def required_fields(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTemplate.RequiredFieldProperty"]]]]:
        '''A list of fields that must contain a value for a case to be successfully created with this template.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTemplate.RequiredFieldProperty"]]]], jsii.get(self, "requiredFields"))

    @required_fields.setter
    def required_fields(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTemplate.RequiredFieldProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39c8e5657497d18585aa40612f5c659b497d7100c68e09119054bef09c886659)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiredFields", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rules")
    def rules(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTemplate.TemplateRuleProperty"]]]]:
        '''A list of case rules (also known as `case field conditions <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ ) on a template.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTemplate.TemplateRuleProperty"]]]], jsii.get(self, "rules"))

    @rules.setter
    def rules(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTemplate.TemplateRuleProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e4d2480373a26a8932a2f3f9600edee09a7b7341d7cae66ca688361a829a902)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rules", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1845602f1bf12e2969e8169e27c8fc05d628f25d6b7293f446ce2d1df289615f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dab8a5124be0cf20b887d468c7c29a69f0103979087d557c61aca04da5d3d7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnTemplate.LayoutConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"default_layout": "defaultLayout"},
    )
    class LayoutConfigurationProperty:
        def __init__(
            self,
            *,
            default_layout: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Object to store configuration of layouts associated to the template.

            :param default_layout: Unique identifier of a layout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-template-layoutconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                layout_configuration_property = cases.CfnTemplate.LayoutConfigurationProperty(
                    default_layout="defaultLayout"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7522da781551341b0186e6159921fe8866252252460b6e230453a88fb5ff05db)
                check_type(argname="argument default_layout", value=default_layout, expected_type=type_hints["default_layout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if default_layout is not None:
                self._values["default_layout"] = default_layout

        @builtins.property
        def default_layout(self) -> typing.Optional[builtins.str]:
            '''Unique identifier of a layout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-template-layoutconfiguration.html#cfn-cases-template-layoutconfiguration-defaultlayout
            '''
            result = self._values.get("default_layout")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LayoutConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnTemplate.RequiredFieldProperty",
        jsii_struct_bases=[],
        name_mapping={"field_id": "fieldId"},
    )
    class RequiredFieldProperty:
        def __init__(self, *, field_id: builtins.str) -> None:
            '''List of fields that must have a value provided to create a case.

            :param field_id: Unique identifier of a field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-template-requiredfield.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                required_field_property = cases.CfnTemplate.RequiredFieldProperty(
                    field_id="fieldId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7844ca9f1c545389d048e75ce9713ce7fa6e686c01147be0a3b769226a12fe92)
                check_type(argname="argument field_id", value=field_id, expected_type=type_hints["field_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_id": field_id,
            }

        @builtins.property
        def field_id(self) -> builtins.str:
            '''Unique identifier of a field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-template-requiredfield.html#cfn-cases-template-requiredfield-fieldid
            '''
            result = self._values.get("field_id")
            assert result is not None, "Required property 'field_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RequiredFieldProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_cases.CfnTemplate.TemplateRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"case_rule_id": "caseRuleId", "field_id": "fieldId"},
    )
    class TemplateRuleProperty:
        def __init__(
            self,
            *,
            case_rule_id: builtins.str,
            field_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An association representing a case rule acting upon a field.

            In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see `Add case field conditions to a case template <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ .

            :param case_rule_id: Unique identifier of a case rule.
            :param field_id: Unique identifier of a field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-template-templaterule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_cases as cases
                
                template_rule_property = cases.CfnTemplate.TemplateRuleProperty(
                    case_rule_id="caseRuleId",
                
                    # the properties below are optional
                    field_id="fieldId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dfed0d0541f970d22fe2c5d2d295983f457dacecdfde60226277c8e9096c05c0)
                check_type(argname="argument case_rule_id", value=case_rule_id, expected_type=type_hints["case_rule_id"])
                check_type(argname="argument field_id", value=field_id, expected_type=type_hints["field_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "case_rule_id": case_rule_id,
            }
            if field_id is not None:
                self._values["field_id"] = field_id

        @builtins.property
        def case_rule_id(self) -> builtins.str:
            '''Unique identifier of a case rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-template-templaterule.html#cfn-cases-template-templaterule-caseruleid
            '''
            result = self._values.get("case_rule_id")
            assert result is not None, "Required property 'case_rule_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def field_id(self) -> typing.Optional[builtins.str]:
            '''Unique identifier of a field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cases-template-templaterule.html#cfn-cases-template-templaterule-fieldid
            '''
            result = self._values.get("field_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cases.CfnTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "domain_id": "domainId",
        "layout_configuration": "layoutConfiguration",
        "required_fields": "requiredFields",
        "rules": "rules",
        "status": "status",
        "tags": "tags",
    },
)
class CfnTemplateProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        domain_id: typing.Optional[builtins.str] = None,
        layout_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTemplate.LayoutConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        required_fields: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTemplate.RequiredFieldProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        rules: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTemplate.TemplateRuleProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTemplate``.

        :param name: The template name.
        :param description: A brief description of the template.
        :param domain_id: The unique identifier of the Cases domain.
        :param layout_configuration: Object to store configuration of layouts associated to the template.
        :param required_fields: A list of fields that must contain a value for a case to be successfully created with this template.
        :param rules: A list of case rules (also known as `case field conditions <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ ) on a template.
        :param status: The status of the template.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-template.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_cases as cases
            
            cfn_template_props = cases.CfnTemplateProps(
                name="name",
            
                # the properties below are optional
                description="description",
                domain_id="domainId",
                layout_configuration=cases.CfnTemplate.LayoutConfigurationProperty(
                    default_layout="defaultLayout"
                ),
                required_fields=[cases.CfnTemplate.RequiredFieldProperty(
                    field_id="fieldId"
                )],
                rules=[cases.CfnTemplate.TemplateRuleProperty(
                    case_rule_id="caseRuleId",
            
                    # the properties below are optional
                    field_id="fieldId"
                )],
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d72d677ae43261dfa31894b05572c5af9c659448dd41b3ed9918e215afc90e05)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_id", value=domain_id, expected_type=type_hints["domain_id"])
            check_type(argname="argument layout_configuration", value=layout_configuration, expected_type=type_hints["layout_configuration"])
            check_type(argname="argument required_fields", value=required_fields, expected_type=type_hints["required_fields"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if domain_id is not None:
            self._values["domain_id"] = domain_id
        if layout_configuration is not None:
            self._values["layout_configuration"] = layout_configuration
        if required_fields is not None:
            self._values["required_fields"] = required_fields
        if rules is not None:
            self._values["rules"] = rules
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The template name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-template.html#cfn-cases-template-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A brief description of the template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-template.html#cfn-cases-template-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the Cases domain.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-template.html#cfn-cases-template-domainid
        '''
        result = self._values.get("domain_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def layout_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTemplate.LayoutConfigurationProperty"]]:
        '''Object to store configuration of layouts associated to the template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-template.html#cfn-cases-template-layoutconfiguration
        '''
        result = self._values.get("layout_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTemplate.LayoutConfigurationProperty"]], result)

    @builtins.property
    def required_fields(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTemplate.RequiredFieldProperty"]]]]:
        '''A list of fields that must contain a value for a case to be successfully created with this template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-template.html#cfn-cases-template-requiredfields
        '''
        result = self._values.get("required_fields")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTemplate.RequiredFieldProperty"]]]], result)

    @builtins.property
    def rules(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTemplate.TemplateRuleProperty"]]]]:
        '''A list of case rules (also known as `case field conditions <https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html>`_ ) on a template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-template.html#cfn-cases-template-rules
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTemplate.TemplateRuleProperty"]]]], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The status of the template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-template.html#cfn-cases-template-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cases-template.html#cfn-cases-template-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCaseRule",
    "CfnCaseRuleProps",
    "CfnDomain",
    "CfnDomainProps",
    "CfnField",
    "CfnFieldProps",
    "CfnLayout",
    "CfnLayoutProps",
    "CfnTemplate",
    "CfnTemplateProps",
]

publication.publish()

def _typecheckingstub__be714901cc3ca1265b6c09c9f45312daac0e3e7940822b521a65617830120426(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCaseRule.CaseRuleDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    domain_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93467cf9959aadeb4bb3766dca0729fe8561ee38e3a3d2aa0f1f70184f6902c1(
    resource: _ICaseRuleRef_1c88c99d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56b6abd99447f46ba474b9bf59ef52a71bba5deda488de30582b742741386881(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f4c2b65b4cd2bc733d8cdee680e57ec542975387b8295a77e3ee37f7f2fb2e2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__249e9f89fcddd0f18df11526741587a09da7f1d6618c67bc49d9ac6da0d69acc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13dd45cca814c5bbdd6da4202994c0857c4726f2e7e84a76e317304c2d048f57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92dc9febd4bacceeaaf366a99c7f47d67e0938c0f5952e8411347591f2ad99c9(
    value: typing.Union[_IResolvable_da3f097b, CfnCaseRule.CaseRuleDetailsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64603d496c22f204cecfd9754c6a349ffe0d3326259667929019e3f1a55ca96(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b3b90d538392a789f67fa43295f64d877e42dd4d7fd21c5b49ffaa52e6c5ed8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db91d0aa4955cf40c2c3524d4ad515c6dc33982f09f95c20e6f8bb73f47e9faf(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df4249487c59524cb034fa3797a87de6b9254c5de1f35f9224cd3c3b632552b3(
    *,
    equal_to: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCaseRule.BooleanOperandsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    not_equal_to: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCaseRule.BooleanOperandsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35693153797cf629f05fba2faef88f79c12830dde58774367117b676866e613c(
    *,
    operand_one: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCaseRule.OperandOneProperty, typing.Dict[builtins.str, typing.Any]]],
    operand_two: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCaseRule.OperandTwoProperty, typing.Dict[builtins.str, typing.Any]]],
    result: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc3771a6a1ed4894f94f30a934757635b8650efee028c69611f77a028c228477(
    *,
    hidden: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCaseRule.HiddenCaseRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    required: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCaseRule.RequiredCaseRuleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab16d965f772c647d0f3f9a94708326a10c2cbf8f8e1826203c8df82b75c5b25(
    *,
    conditions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCaseRule.BooleanConditionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    default_value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3ebdf598c47771ea6d6e5ad126842fc398674ea20c21b3cbeae3096f59eb3bc(
    *,
    field_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8521fb882be1d6ce495bee9db5b66d8a60a8e86f3b73198e53ab5bfb4a895afe(
    *,
    boolean_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    double_value: typing.Optional[jsii.Number] = None,
    empty_value: typing.Any = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c28b76d95a2316f80a4c07df9a415656b3bd000097eeb21fd7249e3eda3e22b1(
    *,
    conditions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCaseRule.BooleanConditionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    default_value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acdfca63e703957a2887afa7cda824f46a8e8e2c23e4d73ff036bed38b4af0fd(
    *,
    name: builtins.str,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCaseRule.CaseRuleDetailsProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    domain_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d298307ba0303a9fe1610ecc75a8c64a40ec633c78a7086fcf29107195ecc95e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd539bc6977de897be38e725e6f6c4c2590ae4659e4684ee78e8554b64d2e3c7(
    resource: _IDomainRef_33d4824f,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__295dd97e2c7a21b30ad43ac334e7cca35a83c02d41c91121f0a806ba56a49c65(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a75062eae4f9c9d498de7b6d1ee80f581181c7d02a194552b0d581ffb1c398ba(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__116abd9be95df9971c61764ff30f094e9bd1dac949084d3b8fe64dbec5f2245c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c83159d7196ff79c0f6fa249f1db9fb9ccc50594779c0aa3a16171e66bd828c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__998f4debbdc1c26247b0286ad29fa49e7dbb53c3b893a589e9075532ccafc84a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d88254a528e2b091b4329dbc80c35c7196bbee8b179f85fcb31572279262beb7(
    *,
    name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd620a5620fd7cf34e28f8693796fb9f7ddd93fcd8c7695281c08776fd5637c4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnField.FieldAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    domain_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a27bd368427051c3694255650751a1197598780a0c7121b0b4b5d7291c4a1b5(
    resource: _IFieldRef_7e261b31,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__566062392071e68ef8b0cf9595573f28d45f57385207a9e32450727a0b5ed13d(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c5fd8d77f5f953c376f74388e62da11d1f407de6f8a91a501869e14ce425f59(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11cf77aa3a0c2eda415b9e175451eb47b72f48c2b11b952fff8b2482baadbba2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9ecb0f4d6cc53f6ec951e68b2d051c56c71741a321f58509aede864cb5e6826(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d1ce71132b61a56132ed0e80dbe19e4967ff0b2b1c54f168b872efaa9e1cfea(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec9d872641de59c09d1a4aa0f22acf0a4b6384bca238c55b5acd984fda658ff1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnField.FieldAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8bb005f1b34005da816178413750d75ad68393cadf6b2e46830cb4281e557b2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ecc904aa381d23a54963bced6be7ceabe396747de3cba4c83b76632085446e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8dde35cd2abf2847d466bfc9448c8228fd804275187398cf2ef8bdeb0c284a4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__523ee0d133ea645c43762c2e235a9493a7f2cfc762459ff52a9acf636d7003cb(
    *,
    text: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnField.TextAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__740b2578760e7393305d88b48521a3000c613a1625cdd16b4967f671c06692ff(
    *,
    is_multiline: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03d88f5f2a426612b3094a6a5e2b1d83000a584ac3ec25a332e2eed7bf494641(
    *,
    name: builtins.str,
    type: builtins.str,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnField.FieldAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    domain_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c9fa7422f8ee22f63316bc5f01e73cff1246061d3b06956469d253d4a721ff2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayout.LayoutContentProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    domain_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__306d13638a5891ae6181bcbd786fb8ff397f5025b2fee0f07d66db26d2c9f4a2(
    resource: _ILayoutRef_a52de4c5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33e2d34da52e5162187fed27c9e71a4d14983ce37ffe60077d5e81ce122e83c2(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0108f8e268d5824ab934bec99da3797910ae831dc29b172eed25f527478b03b1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979e050ce8841db5620a702590d6ee159b10a022921439387b4bb221ec6fc7f4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dacaa2887466f35305aed2bb0e241add3bde7d5ca3e29f59cef3c705eddf2dd(
    value: typing.Union[_IResolvable_da3f097b, CfnLayout.LayoutContentProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c70dc22f467d60c06701a6fc1654aa7442d219a686c18b125b3ee753d1c3125(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d00a3dab4c0a4f500e5ad5bbc5cf586a4e0469241193da7ba58edb230dd7ba7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec7b486db8f5df2a9d1f86e377af46e5cd73476965bd8092d57ecf9409531f89(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a2e643956f0c7c7f9bb872169efbb8666fec7c3453bc760ca9439eac2ef515c(
    *,
    more_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayout.LayoutSectionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    top_panel: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayout.LayoutSectionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b0eb2352a44ca01fdb5d4d03c0550ca7043a9bc6c2f6eb004909d76ef2a60dc(
    *,
    fields: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayout.FieldItemProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d434f4adf93e300cead8b6a0be0574c74c632908463751f04d0e23ec12ebac7(
    *,
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e2a92fccd31f4424fc957a39a250a7df950f0965d3f5f0c686194ba6efd758c(
    *,
    basic: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayout.BasicLayoutProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c648193b760caef809c0779b69738304d0be665065b6a45944ed01ac844bf81(
    *,
    sections: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayout.SectionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7484ee0070e8c31b70a3661555d15fbc2a34da1584110d0e29517fe1dfd717f8(
    *,
    field_group: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayout.FieldGroupProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fd3424821bfebd52d96fdfb554e9999528562965d811208bffae571487d205a(
    *,
    content: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLayout.LayoutContentProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    domain_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73cc3fdeeca49d4acd0b26f8793d1789ed977f837657e631a6a8704b2ea4dadf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_id: typing.Optional[builtins.str] = None,
    layout_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.LayoutConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    required_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.RequiredFieldProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10194be066646d7553d60ae9a84c5428612f34f222b449a7dded0e031c48f45b(
    resource: _ITemplateRef_ec2e69cd,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd4aa7fde6507a6cb44b05a7bbbbe3de6baf437b74d05d567b3944ce9934194(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d5ca9d4e4726f53933eddd12b41a1eec755cd4277ca398ca0916238900db611(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__644ea6fc41bf09e6dd7724125dec8d3299b9f447d80992b72415c54fdb57010a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d32f739df5a6993b0962b41dcef7c5497cca792e9aa0baeb4177304b4ff8aa1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06702e040037f55cc9c42127b813db9c4e47798e192c3679ba68db40f629f291(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8640bd6b75c3f459c543a292f6b4158364ab44364655fffed58777ef1e155d8e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4efad9b266ccf2a52ab3a5b47dc451f4db6b64bdc86869c25b535f39b87073(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTemplate.LayoutConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39c8e5657497d18585aa40612f5c659b497d7100c68e09119054bef09c886659(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTemplate.RequiredFieldProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e4d2480373a26a8932a2f3f9600edee09a7b7341d7cae66ca688361a829a902(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTemplate.TemplateRuleProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1845602f1bf12e2969e8169e27c8fc05d628f25d6b7293f446ce2d1df289615f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dab8a5124be0cf20b887d468c7c29a69f0103979087d557c61aca04da5d3d7c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7522da781551341b0186e6159921fe8866252252460b6e230453a88fb5ff05db(
    *,
    default_layout: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7844ca9f1c545389d048e75ce9713ce7fa6e686c01147be0a3b769226a12fe92(
    *,
    field_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfed0d0541f970d22fe2c5d2d295983f457dacecdfde60226277c8e9096c05c0(
    *,
    case_rule_id: builtins.str,
    field_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d72d677ae43261dfa31894b05572c5af9c659448dd41b3ed9918e215afc90e05(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    domain_id: typing.Optional[builtins.str] = None,
    layout_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.LayoutConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    required_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.RequiredFieldProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    rules: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateRuleProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
