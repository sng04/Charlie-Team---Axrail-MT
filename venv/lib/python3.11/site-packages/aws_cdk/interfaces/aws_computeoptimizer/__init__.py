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
    jsii_type="aws-cdk-lib.interfaces.aws_computeoptimizer.AutomationRuleReference",
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
            from aws_cdk.interfaces import aws_computeoptimizer as interfaces_computeoptimizer
            
            automation_rule_reference = interfaces_computeoptimizer.AutomationRuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b467d274fec88fac442a237bab798e6f60af1a9747315e2bdae021b593c97d5a)
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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_computeoptimizer.IAutomationRuleRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_computeoptimizer.IAutomationRuleRef"

    @builtins.property
    @jsii.member(jsii_name="automationRuleRef")
    def automation_rule_ref(self) -> "AutomationRuleReference":
        '''(experimental) A reference to a AutomationRule resource.

        :stability: experimental
        '''
        return typing.cast("AutomationRuleReference", jsii.get(self, "automationRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAutomationRuleRef).__jsii_proxy_class__ = lambda : _IAutomationRuleRefProxy


__all__ = [
    "AutomationRuleReference",
    "IAutomationRuleRef",
]

publication.publish()

def _typecheckingstub__b467d274fec88fac442a237bab798e6f60af1a9747315e2bdae021b593c97d5a(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAutomationRuleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
