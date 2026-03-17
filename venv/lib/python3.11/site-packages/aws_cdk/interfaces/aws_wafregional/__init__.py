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
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.ByteMatchSetReference",
    jsii_struct_bases=[],
    name_mapping={"byte_match_set_id": "byteMatchSetId"},
)
class ByteMatchSetReference:
    def __init__(self, *, byte_match_set_id: builtins.str) -> None:
        '''A reference to a ByteMatchSet resource.

        :param byte_match_set_id: The Id of the ByteMatchSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            byte_match_set_reference = interfaces_wafregional.ByteMatchSetReference(
                byte_match_set_id="byteMatchSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c5242b03519b42eaddea8d40e8c6e1b1aec2b38f769fb03503ad1b31d290971)
            check_type(argname="argument byte_match_set_id", value=byte_match_set_id, expected_type=type_hints["byte_match_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "byte_match_set_id": byte_match_set_id,
        }

    @builtins.property
    def byte_match_set_id(self) -> builtins.str:
        '''The Id of the ByteMatchSet resource.'''
        result = self._values.get("byte_match_set_id")
        assert result is not None, "Required property 'byte_match_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ByteMatchSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.GeoMatchSetReference",
    jsii_struct_bases=[],
    name_mapping={"geo_match_set_id": "geoMatchSetId"},
)
class GeoMatchSetReference:
    def __init__(self, *, geo_match_set_id: builtins.str) -> None:
        '''A reference to a GeoMatchSet resource.

        :param geo_match_set_id: The Id of the GeoMatchSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            geo_match_set_reference = interfaces_wafregional.GeoMatchSetReference(
                geo_match_set_id="geoMatchSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79848d2813c5e96bd3fe6056e79b805772e4a6c6a1a4d87616cd28413b36a84c)
            check_type(argname="argument geo_match_set_id", value=geo_match_set_id, expected_type=type_hints["geo_match_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "geo_match_set_id": geo_match_set_id,
        }

    @builtins.property
    def geo_match_set_id(self) -> builtins.str:
        '''The Id of the GeoMatchSet resource.'''
        result = self._values.get("geo_match_set_id")
        assert result is not None, "Required property 'geo_match_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GeoMatchSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafregional.IByteMatchSetRef")
class IByteMatchSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ByteMatchSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="byteMatchSetRef")
    def byte_match_set_ref(self) -> "ByteMatchSetReference":
        '''(experimental) A reference to a ByteMatchSet resource.

        :stability: experimental
        '''
        ...


class _IByteMatchSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ByteMatchSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.IByteMatchSetRef"

    @builtins.property
    @jsii.member(jsii_name="byteMatchSetRef")
    def byte_match_set_ref(self) -> "ByteMatchSetReference":
        '''(experimental) A reference to a ByteMatchSet resource.

        :stability: experimental
        '''
        return typing.cast("ByteMatchSetReference", jsii.get(self, "byteMatchSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IByteMatchSetRef).__jsii_proxy_class__ = lambda : _IByteMatchSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafregional.IGeoMatchSetRef")
class IGeoMatchSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GeoMatchSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="geoMatchSetRef")
    def geo_match_set_ref(self) -> "GeoMatchSetReference":
        '''(experimental) A reference to a GeoMatchSet resource.

        :stability: experimental
        '''
        ...


class _IGeoMatchSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GeoMatchSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.IGeoMatchSetRef"

    @builtins.property
    @jsii.member(jsii_name="geoMatchSetRef")
    def geo_match_set_ref(self) -> "GeoMatchSetReference":
        '''(experimental) A reference to a GeoMatchSet resource.

        :stability: experimental
        '''
        return typing.cast("GeoMatchSetReference", jsii.get(self, "geoMatchSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGeoMatchSetRef).__jsii_proxy_class__ = lambda : _IGeoMatchSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafregional.IIPSetRef")
class IIPSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IPSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ipSetRef")
    def ip_set_ref(self) -> "IPSetReference":
        '''(experimental) A reference to a IPSet resource.

        :stability: experimental
        '''
        ...


class _IIPSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IPSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.IIPSetRef"

    @builtins.property
    @jsii.member(jsii_name="ipSetRef")
    def ip_set_ref(self) -> "IPSetReference":
        '''(experimental) A reference to a IPSet resource.

        :stability: experimental
        '''
        return typing.cast("IPSetReference", jsii.get(self, "ipSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPSetRef).__jsii_proxy_class__ = lambda : _IIPSetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.IPSetReference",
    jsii_struct_bases=[],
    name_mapping={"ip_set_id": "ipSetId"},
)
class IPSetReference:
    def __init__(self, *, ip_set_id: builtins.str) -> None:
        '''A reference to a IPSet resource.

        :param ip_set_id: The Id of the IPSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            i_pSet_reference = {
                "ip_set_id": "ipSetId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__824e111909716f371eb35683cfb41e38a7aa3dccb70d4b56aefc506ed36d7aee)
            check_type(argname="argument ip_set_id", value=ip_set_id, expected_type=type_hints["ip_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_set_id": ip_set_id,
        }

    @builtins.property
    def ip_set_id(self) -> builtins.str:
        '''The Id of the IPSet resource.'''
        result = self._values.get("ip_set_id")
        assert result is not None, "Required property 'ip_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafregional.IRateBasedRuleRef")
class IRateBasedRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RateBasedRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="rateBasedRuleRef")
    def rate_based_rule_ref(self) -> "RateBasedRuleReference":
        '''(experimental) A reference to a RateBasedRule resource.

        :stability: experimental
        '''
        ...


class _IRateBasedRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RateBasedRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.IRateBasedRuleRef"

    @builtins.property
    @jsii.member(jsii_name="rateBasedRuleRef")
    def rate_based_rule_ref(self) -> "RateBasedRuleReference":
        '''(experimental) A reference to a RateBasedRule resource.

        :stability: experimental
        '''
        return typing.cast("RateBasedRuleReference", jsii.get(self, "rateBasedRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRateBasedRuleRef).__jsii_proxy_class__ = lambda : _IRateBasedRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafregional.IRegexPatternSetRef")
class IRegexPatternSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RegexPatternSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="regexPatternSetRef")
    def regex_pattern_set_ref(self) -> "RegexPatternSetReference":
        '''(experimental) A reference to a RegexPatternSet resource.

        :stability: experimental
        '''
        ...


class _IRegexPatternSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RegexPatternSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.IRegexPatternSetRef"

    @builtins.property
    @jsii.member(jsii_name="regexPatternSetRef")
    def regex_pattern_set_ref(self) -> "RegexPatternSetReference":
        '''(experimental) A reference to a RegexPatternSet resource.

        :stability: experimental
        '''
        return typing.cast("RegexPatternSetReference", jsii.get(self, "regexPatternSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRegexPatternSetRef).__jsii_proxy_class__ = lambda : _IRegexPatternSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafregional.IRuleRef")
class IRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Rule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ruleRef")
    def rule_ref(self) -> "RuleReference":
        '''(experimental) A reference to a Rule resource.

        :stability: experimental
        '''
        ...


class _IRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Rule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.IRuleRef"

    @builtins.property
    @jsii.member(jsii_name="ruleRef")
    def rule_ref(self) -> "RuleReference":
        '''(experimental) A reference to a Rule resource.

        :stability: experimental
        '''
        return typing.cast("RuleReference", jsii.get(self, "ruleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuleRef).__jsii_proxy_class__ = lambda : _IRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.ISizeConstraintSetRef"
)
class ISizeConstraintSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SizeConstraintSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sizeConstraintSetRef")
    def size_constraint_set_ref(self) -> "SizeConstraintSetReference":
        '''(experimental) A reference to a SizeConstraintSet resource.

        :stability: experimental
        '''
        ...


class _ISizeConstraintSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SizeConstraintSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.ISizeConstraintSetRef"

    @builtins.property
    @jsii.member(jsii_name="sizeConstraintSetRef")
    def size_constraint_set_ref(self) -> "SizeConstraintSetReference":
        '''(experimental) A reference to a SizeConstraintSet resource.

        :stability: experimental
        '''
        return typing.cast("SizeConstraintSetReference", jsii.get(self, "sizeConstraintSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISizeConstraintSetRef).__jsii_proxy_class__ = lambda : _ISizeConstraintSetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.ISqlInjectionMatchSetRef"
)
class ISqlInjectionMatchSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SqlInjectionMatchSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sqlInjectionMatchSetRef")
    def sql_injection_match_set_ref(self) -> "SqlInjectionMatchSetReference":
        '''(experimental) A reference to a SqlInjectionMatchSet resource.

        :stability: experimental
        '''
        ...


class _ISqlInjectionMatchSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SqlInjectionMatchSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.ISqlInjectionMatchSetRef"

    @builtins.property
    @jsii.member(jsii_name="sqlInjectionMatchSetRef")
    def sql_injection_match_set_ref(self) -> "SqlInjectionMatchSetReference":
        '''(experimental) A reference to a SqlInjectionMatchSet resource.

        :stability: experimental
        '''
        return typing.cast("SqlInjectionMatchSetReference", jsii.get(self, "sqlInjectionMatchSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISqlInjectionMatchSetRef).__jsii_proxy_class__ = lambda : _ISqlInjectionMatchSetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.IWebACLAssociationRef"
)
class IWebACLAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WebACLAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="webAclAssociationRef")
    def web_acl_association_ref(self) -> "WebACLAssociationReference":
        '''(experimental) A reference to a WebACLAssociation resource.

        :stability: experimental
        '''
        ...


class _IWebACLAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WebACLAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.IWebACLAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="webAclAssociationRef")
    def web_acl_association_ref(self) -> "WebACLAssociationReference":
        '''(experimental) A reference to a WebACLAssociation resource.

        :stability: experimental
        '''
        return typing.cast("WebACLAssociationReference", jsii.get(self, "webAclAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWebACLAssociationRef).__jsii_proxy_class__ = lambda : _IWebACLAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafregional.IWebACLRef")
class IWebACLRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WebACL.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="webAclRef")
    def web_acl_ref(self) -> "WebACLReference":
        '''(experimental) A reference to a WebACL resource.

        :stability: experimental
        '''
        ...


class _IWebACLRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WebACL.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.IWebACLRef"

    @builtins.property
    @jsii.member(jsii_name="webAclRef")
    def web_acl_ref(self) -> "WebACLReference":
        '''(experimental) A reference to a WebACL resource.

        :stability: experimental
        '''
        return typing.cast("WebACLReference", jsii.get(self, "webAclRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWebACLRef).__jsii_proxy_class__ = lambda : _IWebACLRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafregional.IXssMatchSetRef")
class IXssMatchSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a XssMatchSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="xssMatchSetRef")
    def xss_match_set_ref(self) -> "XssMatchSetReference":
        '''(experimental) A reference to a XssMatchSet resource.

        :stability: experimental
        '''
        ...


class _IXssMatchSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a XssMatchSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafregional.IXssMatchSetRef"

    @builtins.property
    @jsii.member(jsii_name="xssMatchSetRef")
    def xss_match_set_ref(self) -> "XssMatchSetReference":
        '''(experimental) A reference to a XssMatchSet resource.

        :stability: experimental
        '''
        return typing.cast("XssMatchSetReference", jsii.get(self, "xssMatchSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IXssMatchSetRef).__jsii_proxy_class__ = lambda : _IXssMatchSetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.RateBasedRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rate_based_rule_id": "rateBasedRuleId"},
)
class RateBasedRuleReference:
    def __init__(self, *, rate_based_rule_id: builtins.str) -> None:
        '''A reference to a RateBasedRule resource.

        :param rate_based_rule_id: The Id of the RateBasedRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            rate_based_rule_reference = interfaces_wafregional.RateBasedRuleReference(
                rate_based_rule_id="rateBasedRuleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81db54a77e02a647e5dc515cb8d66e6e75aa045cd1574a9d8d86f87b958f61c9)
            check_type(argname="argument rate_based_rule_id", value=rate_based_rule_id, expected_type=type_hints["rate_based_rule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rate_based_rule_id": rate_based_rule_id,
        }

    @builtins.property
    def rate_based_rule_id(self) -> builtins.str:
        '''The Id of the RateBasedRule resource.'''
        result = self._values.get("rate_based_rule_id")
        assert result is not None, "Required property 'rate_based_rule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RateBasedRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.RegexPatternSetReference",
    jsii_struct_bases=[],
    name_mapping={"regex_pattern_set_id": "regexPatternSetId"},
)
class RegexPatternSetReference:
    def __init__(self, *, regex_pattern_set_id: builtins.str) -> None:
        '''A reference to a RegexPatternSet resource.

        :param regex_pattern_set_id: The Id of the RegexPatternSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            regex_pattern_set_reference = interfaces_wafregional.RegexPatternSetReference(
                regex_pattern_set_id="regexPatternSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f6fba8fa5d507bd8cd6f2daef20d6267e7fcb92bd0e0d4605e2395ce65ea7b0)
            check_type(argname="argument regex_pattern_set_id", value=regex_pattern_set_id, expected_type=type_hints["regex_pattern_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "regex_pattern_set_id": regex_pattern_set_id,
        }

    @builtins.property
    def regex_pattern_set_id(self) -> builtins.str:
        '''The Id of the RegexPatternSet resource.'''
        result = self._values.get("regex_pattern_set_id")
        assert result is not None, "Required property 'regex_pattern_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegexPatternSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.RuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_id": "ruleId"},
)
class RuleReference:
    def __init__(self, *, rule_id: builtins.str) -> None:
        '''A reference to a Rule resource.

        :param rule_id: The Id of the Rule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            rule_reference = interfaces_wafregional.RuleReference(
                rule_id="ruleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beab9ed97b2ca66c05ff1bd4a4aeac9321dfdcae55c8e44a8ddc8d31e98fcbc8)
            check_type(argname="argument rule_id", value=rule_id, expected_type=type_hints["rule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_id": rule_id,
        }

    @builtins.property
    def rule_id(self) -> builtins.str:
        '''The Id of the Rule resource.'''
        result = self._values.get("rule_id")
        assert result is not None, "Required property 'rule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.SizeConstraintSetReference",
    jsii_struct_bases=[],
    name_mapping={"size_constraint_set_id": "sizeConstraintSetId"},
)
class SizeConstraintSetReference:
    def __init__(self, *, size_constraint_set_id: builtins.str) -> None:
        '''A reference to a SizeConstraintSet resource.

        :param size_constraint_set_id: The Id of the SizeConstraintSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            size_constraint_set_reference = interfaces_wafregional.SizeConstraintSetReference(
                size_constraint_set_id="sizeConstraintSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbf71bc612dac3843be385c1f8764cbf3946eb26f33d9049ee734b2feae1d98d)
            check_type(argname="argument size_constraint_set_id", value=size_constraint_set_id, expected_type=type_hints["size_constraint_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "size_constraint_set_id": size_constraint_set_id,
        }

    @builtins.property
    def size_constraint_set_id(self) -> builtins.str:
        '''The Id of the SizeConstraintSet resource.'''
        result = self._values.get("size_constraint_set_id")
        assert result is not None, "Required property 'size_constraint_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SizeConstraintSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.SqlInjectionMatchSetReference",
    jsii_struct_bases=[],
    name_mapping={"sql_injection_match_set_id": "sqlInjectionMatchSetId"},
)
class SqlInjectionMatchSetReference:
    def __init__(self, *, sql_injection_match_set_id: builtins.str) -> None:
        '''A reference to a SqlInjectionMatchSet resource.

        :param sql_injection_match_set_id: The Id of the SqlInjectionMatchSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            sql_injection_match_set_reference = interfaces_wafregional.SqlInjectionMatchSetReference(
                sql_injection_match_set_id="sqlInjectionMatchSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cafca5e879e55ba27e8470f19be5dfb9c9df705225f94ffffb464600dd6abe89)
            check_type(argname="argument sql_injection_match_set_id", value=sql_injection_match_set_id, expected_type=type_hints["sql_injection_match_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sql_injection_match_set_id": sql_injection_match_set_id,
        }

    @builtins.property
    def sql_injection_match_set_id(self) -> builtins.str:
        '''The Id of the SqlInjectionMatchSet resource.'''
        result = self._values.get("sql_injection_match_set_id")
        assert result is not None, "Required property 'sql_injection_match_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SqlInjectionMatchSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.WebACLAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"web_acl_association_id": "webAclAssociationId"},
)
class WebACLAssociationReference:
    def __init__(self, *, web_acl_association_id: builtins.str) -> None:
        '''A reference to a WebACLAssociation resource.

        :param web_acl_association_id: The Id of the WebACLAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            web_aCLAssociation_reference = interfaces_wafregional.WebACLAssociationReference(
                web_acl_association_id="webAclAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74e89533b81011c5b244f93732cee12c0864534018cf9e5683181319342e442b)
            check_type(argname="argument web_acl_association_id", value=web_acl_association_id, expected_type=type_hints["web_acl_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "web_acl_association_id": web_acl_association_id,
        }

    @builtins.property
    def web_acl_association_id(self) -> builtins.str:
        '''The Id of the WebACLAssociation resource.'''
        result = self._values.get("web_acl_association_id")
        assert result is not None, "Required property 'web_acl_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebACLAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.WebACLReference",
    jsii_struct_bases=[],
    name_mapping={"web_acl_id": "webAclId"},
)
class WebACLReference:
    def __init__(self, *, web_acl_id: builtins.str) -> None:
        '''A reference to a WebACL resource.

        :param web_acl_id: The Id of the WebACL resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            web_aCLReference = interfaces_wafregional.WebACLReference(
                web_acl_id="webAclId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16735856d20fa8f6f18629c8eaa9dad98fe6d8619a811b622699e16b070c69f0)
            check_type(argname="argument web_acl_id", value=web_acl_id, expected_type=type_hints["web_acl_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "web_acl_id": web_acl_id,
        }

    @builtins.property
    def web_acl_id(self) -> builtins.str:
        '''The Id of the WebACL resource.'''
        result = self._values.get("web_acl_id")
        assert result is not None, "Required property 'web_acl_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebACLReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafregional.XssMatchSetReference",
    jsii_struct_bases=[],
    name_mapping={"xss_match_set_id": "xssMatchSetId"},
)
class XssMatchSetReference:
    def __init__(self, *, xss_match_set_id: builtins.str) -> None:
        '''A reference to a XssMatchSet resource.

        :param xss_match_set_id: The Id of the XssMatchSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafregional as interfaces_wafregional
            
            xss_match_set_reference = interfaces_wafregional.XssMatchSetReference(
                xss_match_set_id="xssMatchSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1320556cb83fe8f40d7cdaba6e324fe0fd13bc9a8d2d16cdd6e6d2df5351bfb)
            check_type(argname="argument xss_match_set_id", value=xss_match_set_id, expected_type=type_hints["xss_match_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "xss_match_set_id": xss_match_set_id,
        }

    @builtins.property
    def xss_match_set_id(self) -> builtins.str:
        '''The Id of the XssMatchSet resource.'''
        result = self._values.get("xss_match_set_id")
        assert result is not None, "Required property 'xss_match_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "XssMatchSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ByteMatchSetReference",
    "GeoMatchSetReference",
    "IByteMatchSetRef",
    "IGeoMatchSetRef",
    "IIPSetRef",
    "IPSetReference",
    "IRateBasedRuleRef",
    "IRegexPatternSetRef",
    "IRuleRef",
    "ISizeConstraintSetRef",
    "ISqlInjectionMatchSetRef",
    "IWebACLAssociationRef",
    "IWebACLRef",
    "IXssMatchSetRef",
    "RateBasedRuleReference",
    "RegexPatternSetReference",
    "RuleReference",
    "SizeConstraintSetReference",
    "SqlInjectionMatchSetReference",
    "WebACLAssociationReference",
    "WebACLReference",
    "XssMatchSetReference",
]

publication.publish()

def _typecheckingstub__5c5242b03519b42eaddea8d40e8c6e1b1aec2b38f769fb03503ad1b31d290971(
    *,
    byte_match_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79848d2813c5e96bd3fe6056e79b805772e4a6c6a1a4d87616cd28413b36a84c(
    *,
    geo_match_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824e111909716f371eb35683cfb41e38a7aa3dccb70d4b56aefc506ed36d7aee(
    *,
    ip_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81db54a77e02a647e5dc515cb8d66e6e75aa045cd1574a9d8d86f87b958f61c9(
    *,
    rate_based_rule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f6fba8fa5d507bd8cd6f2daef20d6267e7fcb92bd0e0d4605e2395ce65ea7b0(
    *,
    regex_pattern_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beab9ed97b2ca66c05ff1bd4a4aeac9321dfdcae55c8e44a8ddc8d31e98fcbc8(
    *,
    rule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbf71bc612dac3843be385c1f8764cbf3946eb26f33d9049ee734b2feae1d98d(
    *,
    size_constraint_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cafca5e879e55ba27e8470f19be5dfb9c9df705225f94ffffb464600dd6abe89(
    *,
    sql_injection_match_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74e89533b81011c5b244f93732cee12c0864534018cf9e5683181319342e442b(
    *,
    web_acl_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16735856d20fa8f6f18629c8eaa9dad98fe6d8619a811b622699e16b070c69f0(
    *,
    web_acl_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1320556cb83fe8f40d7cdaba6e324fe0fd13bc9a8d2d16cdd6e6d2df5351bfb(
    *,
    xss_match_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IByteMatchSetRef, IGeoMatchSetRef, IIPSetRef, IRateBasedRuleRef, IRegexPatternSetRef, IRuleRef, ISizeConstraintSetRef, ISqlInjectionMatchSetRef, IWebACLAssociationRef, IWebACLRef, IXssMatchSetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
