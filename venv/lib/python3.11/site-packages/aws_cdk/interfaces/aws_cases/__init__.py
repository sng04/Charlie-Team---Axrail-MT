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
    jsii_type="aws-cdk-lib.interfaces.aws_cases.CaseRuleReference",
    jsii_struct_bases=[],
    name_mapping={"case_rule_arn": "caseRuleArn"},
)
class CaseRuleReference:
    def __init__(self, *, case_rule_arn: builtins.str) -> None:
        '''A reference to a CaseRule resource.

        :param case_rule_arn: The CaseRuleArn of the CaseRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cases as interfaces_cases
            
            case_rule_reference = interfaces_cases.CaseRuleReference(
                case_rule_arn="caseRuleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04d900fba4db4547b064b2cd8142a6512b831496af39d45be4d747639a3d4747)
            check_type(argname="argument case_rule_arn", value=case_rule_arn, expected_type=type_hints["case_rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "case_rule_arn": case_rule_arn,
        }

    @builtins.property
    def case_rule_arn(self) -> builtins.str:
        '''The CaseRuleArn of the CaseRule resource.'''
        result = self._values.get("case_rule_arn")
        assert result is not None, "Required property 'case_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CaseRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cases.DomainReference",
    jsii_struct_bases=[],
    name_mapping={"domain_arn": "domainArn"},
)
class DomainReference:
    def __init__(self, *, domain_arn: builtins.str) -> None:
        '''A reference to a Domain resource.

        :param domain_arn: The DomainArn of the Domain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cases as interfaces_cases
            
            domain_reference = interfaces_cases.DomainReference(
                domain_arn="domainArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbbd76f8cb8d0c6b8a7307c4fbf2405936d1ce5337dd93fa6a38b46f389c1655)
            check_type(argname="argument domain_arn", value=domain_arn, expected_type=type_hints["domain_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_arn": domain_arn,
        }

    @builtins.property
    def domain_arn(self) -> builtins.str:
        '''The DomainArn of the Domain resource.'''
        result = self._values.get("domain_arn")
        assert result is not None, "Required property 'domain_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cases.FieldReference",
    jsii_struct_bases=[],
    name_mapping={"field_arn": "fieldArn"},
)
class FieldReference:
    def __init__(self, *, field_arn: builtins.str) -> None:
        '''A reference to a Field resource.

        :param field_arn: The FieldArn of the Field resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cases as interfaces_cases
            
            field_reference = interfaces_cases.FieldReference(
                field_arn="fieldArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aac15e2b434e7f90607bc53e92c6fec1325787725a821e612ff548e78a1e964)
            check_type(argname="argument field_arn", value=field_arn, expected_type=type_hints["field_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "field_arn": field_arn,
        }

    @builtins.property
    def field_arn(self) -> builtins.str:
        '''The FieldArn of the Field resource.'''
        result = self._values.get("field_arn")
        assert result is not None, "Required property 'field_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FieldReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cases.ICaseRuleRef")
class ICaseRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CaseRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="caseRuleRef")
    def case_rule_ref(self) -> "CaseRuleReference":
        '''(experimental) A reference to a CaseRule resource.

        :stability: experimental
        '''
        ...


class _ICaseRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CaseRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cases.ICaseRuleRef"

    @builtins.property
    @jsii.member(jsii_name="caseRuleRef")
    def case_rule_ref(self) -> "CaseRuleReference":
        '''(experimental) A reference to a CaseRule resource.

        :stability: experimental
        '''
        return typing.cast("CaseRuleReference", jsii.get(self, "caseRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICaseRuleRef).__jsii_proxy_class__ = lambda : _ICaseRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cases.IDomainRef")
class IDomainRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Domain.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        ...


class _IDomainRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Domain.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cases.IDomainRef"

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        return typing.cast("DomainReference", jsii.get(self, "domainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainRef).__jsii_proxy_class__ = lambda : _IDomainRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cases.IFieldRef")
class IFieldRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Field.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fieldRef")
    def field_ref(self) -> "FieldReference":
        '''(experimental) A reference to a Field resource.

        :stability: experimental
        '''
        ...


class _IFieldRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Field.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cases.IFieldRef"

    @builtins.property
    @jsii.member(jsii_name="fieldRef")
    def field_ref(self) -> "FieldReference":
        '''(experimental) A reference to a Field resource.

        :stability: experimental
        '''
        return typing.cast("FieldReference", jsii.get(self, "fieldRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFieldRef).__jsii_proxy_class__ = lambda : _IFieldRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cases.ILayoutRef")
class ILayoutRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Layout.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="layoutRef")
    def layout_ref(self) -> "LayoutReference":
        '''(experimental) A reference to a Layout resource.

        :stability: experimental
        '''
        ...


class _ILayoutRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Layout.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cases.ILayoutRef"

    @builtins.property
    @jsii.member(jsii_name="layoutRef")
    def layout_ref(self) -> "LayoutReference":
        '''(experimental) A reference to a Layout resource.

        :stability: experimental
        '''
        return typing.cast("LayoutReference", jsii.get(self, "layoutRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILayoutRef).__jsii_proxy_class__ = lambda : _ILayoutRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cases.ITemplateRef")
class ITemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Template.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="templateRef")
    def template_ref(self) -> "TemplateReference":
        '''(experimental) A reference to a Template resource.

        :stability: experimental
        '''
        ...


class _ITemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Template.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cases.ITemplateRef"

    @builtins.property
    @jsii.member(jsii_name="templateRef")
    def template_ref(self) -> "TemplateReference":
        '''(experimental) A reference to a Template resource.

        :stability: experimental
        '''
        return typing.cast("TemplateReference", jsii.get(self, "templateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITemplateRef).__jsii_proxy_class__ = lambda : _ITemplateRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cases.LayoutReference",
    jsii_struct_bases=[],
    name_mapping={"layout_arn": "layoutArn"},
)
class LayoutReference:
    def __init__(self, *, layout_arn: builtins.str) -> None:
        '''A reference to a Layout resource.

        :param layout_arn: The LayoutArn of the Layout resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cases as interfaces_cases
            
            layout_reference = interfaces_cases.LayoutReference(
                layout_arn="layoutArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e6d380b7626ed495afd5dc2c0d3925b3dbde53f0779e1131e693a84a920f2ea)
            check_type(argname="argument layout_arn", value=layout_arn, expected_type=type_hints["layout_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "layout_arn": layout_arn,
        }

    @builtins.property
    def layout_arn(self) -> builtins.str:
        '''The LayoutArn of the Layout resource.'''
        result = self._values.get("layout_arn")
        assert result is not None, "Required property 'layout_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LayoutReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cases.TemplateReference",
    jsii_struct_bases=[],
    name_mapping={"template_arn": "templateArn"},
)
class TemplateReference:
    def __init__(self, *, template_arn: builtins.str) -> None:
        '''A reference to a Template resource.

        :param template_arn: The TemplateArn of the Template resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cases as interfaces_cases
            
            template_reference = interfaces_cases.TemplateReference(
                template_arn="templateArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e79abfdc3314e46c0458acb7321ed640fc64b358a0e8a6232d6d4d08185eb8d7)
            check_type(argname="argument template_arn", value=template_arn, expected_type=type_hints["template_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_arn": template_arn,
        }

    @builtins.property
    def template_arn(self) -> builtins.str:
        '''The TemplateArn of the Template resource.'''
        result = self._values.get("template_arn")
        assert result is not None, "Required property 'template_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CaseRuleReference",
    "DomainReference",
    "FieldReference",
    "ICaseRuleRef",
    "IDomainRef",
    "IFieldRef",
    "ILayoutRef",
    "ITemplateRef",
    "LayoutReference",
    "TemplateReference",
]

publication.publish()

def _typecheckingstub__04d900fba4db4547b064b2cd8142a6512b831496af39d45be4d747639a3d4747(
    *,
    case_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbbd76f8cb8d0c6b8a7307c4fbf2405936d1ce5337dd93fa6a38b46f389c1655(
    *,
    domain_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aac15e2b434e7f90607bc53e92c6fec1325787725a821e612ff548e78a1e964(
    *,
    field_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e6d380b7626ed495afd5dc2c0d3925b3dbde53f0779e1131e693a84a920f2ea(
    *,
    layout_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e79abfdc3314e46c0458acb7321ed640fc64b358a0e8a6232d6d4d08185eb8d7(
    *,
    template_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICaseRuleRef, IDomainRef, IFieldRef, ILayoutRef, ITemplateRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
