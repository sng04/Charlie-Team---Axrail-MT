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
    jsii_type="aws-cdk-lib.interfaces.aws_waf.ByteMatchSetReference",
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
            from aws_cdk.interfaces import aws_waf as interfaces_waf
            
            byte_match_set_reference = interfaces_waf.ByteMatchSetReference(
                byte_match_set_id="byteMatchSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25df697b9ab17fe1b773d854b2f5c70aa159a6fb8d6756627245e05ed77a4b31)
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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_waf.IByteMatchSetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_waf.IByteMatchSetRef"

    @builtins.property
    @jsii.member(jsii_name="byteMatchSetRef")
    def byte_match_set_ref(self) -> "ByteMatchSetReference":
        '''(experimental) A reference to a ByteMatchSet resource.

        :stability: experimental
        '''
        return typing.cast("ByteMatchSetReference", jsii.get(self, "byteMatchSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IByteMatchSetRef).__jsii_proxy_class__ = lambda : _IByteMatchSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_waf.IIPSetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_waf.IIPSetRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_waf.IPSetReference",
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
            from aws_cdk.interfaces import aws_waf as interfaces_waf
            
            i_pSet_reference = {
                "ip_set_id": "ipSetId"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35cdf0c2cdfab07f6acf02567f8ab2a59bc9c91ce52aa62128f6acabcd469724)
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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_waf.IRuleRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_waf.IRuleRef"

    @builtins.property
    @jsii.member(jsii_name="ruleRef")
    def rule_ref(self) -> "RuleReference":
        '''(experimental) A reference to a Rule resource.

        :stability: experimental
        '''
        return typing.cast("RuleReference", jsii.get(self, "ruleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuleRef).__jsii_proxy_class__ = lambda : _IRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_waf.ISizeConstraintSetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_waf.ISizeConstraintSetRef"

    @builtins.property
    @jsii.member(jsii_name="sizeConstraintSetRef")
    def size_constraint_set_ref(self) -> "SizeConstraintSetReference":
        '''(experimental) A reference to a SizeConstraintSet resource.

        :stability: experimental
        '''
        return typing.cast("SizeConstraintSetReference", jsii.get(self, "sizeConstraintSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISizeConstraintSetRef).__jsii_proxy_class__ = lambda : _ISizeConstraintSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_waf.ISqlInjectionMatchSetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_waf.ISqlInjectionMatchSetRef"

    @builtins.property
    @jsii.member(jsii_name="sqlInjectionMatchSetRef")
    def sql_injection_match_set_ref(self) -> "SqlInjectionMatchSetReference":
        '''(experimental) A reference to a SqlInjectionMatchSet resource.

        :stability: experimental
        '''
        return typing.cast("SqlInjectionMatchSetReference", jsii.get(self, "sqlInjectionMatchSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISqlInjectionMatchSetRef).__jsii_proxy_class__ = lambda : _ISqlInjectionMatchSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_waf.IWebACLRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_waf.IWebACLRef"

    @builtins.property
    @jsii.member(jsii_name="webAclRef")
    def web_acl_ref(self) -> "WebACLReference":
        '''(experimental) A reference to a WebACL resource.

        :stability: experimental
        '''
        return typing.cast("WebACLReference", jsii.get(self, "webAclRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWebACLRef).__jsii_proxy_class__ = lambda : _IWebACLRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_waf.IXssMatchSetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_waf.IXssMatchSetRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_waf.RuleReference",
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
            from aws_cdk.interfaces import aws_waf as interfaces_waf
            
            rule_reference = interfaces_waf.RuleReference(
                rule_id="ruleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74149078d582bf68f4aacb1a305d1d3f2fb45ef261ccc56e7c63591ae7891f54)
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
    jsii_type="aws-cdk-lib.interfaces.aws_waf.SizeConstraintSetReference",
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
            from aws_cdk.interfaces import aws_waf as interfaces_waf
            
            size_constraint_set_reference = interfaces_waf.SizeConstraintSetReference(
                size_constraint_set_id="sizeConstraintSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__889a99e81fb5a8b4397ad10771420e66c45fd8386b16f0211edae8fdfd3c8a9f)
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
    jsii_type="aws-cdk-lib.interfaces.aws_waf.SqlInjectionMatchSetReference",
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
            from aws_cdk.interfaces import aws_waf as interfaces_waf
            
            sql_injection_match_set_reference = interfaces_waf.SqlInjectionMatchSetReference(
                sql_injection_match_set_id="sqlInjectionMatchSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b37e736344b81273bb8636bc1ea52a0a94dfcff852b60dd7acd02273847608d2)
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
    jsii_type="aws-cdk-lib.interfaces.aws_waf.WebACLReference",
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
            from aws_cdk.interfaces import aws_waf as interfaces_waf
            
            web_aCLReference = interfaces_waf.WebACLReference(
                web_acl_id="webAclId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4616ed55dce429e29803eeaefdfe2153afe64613d3092f3533830df30b7cb020)
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
    jsii_type="aws-cdk-lib.interfaces.aws_waf.XssMatchSetReference",
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
            from aws_cdk.interfaces import aws_waf as interfaces_waf
            
            xss_match_set_reference = interfaces_waf.XssMatchSetReference(
                xss_match_set_id="xssMatchSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0941d18d86d76f76e620d1215586bd4683d80fbb7ca0f33f98d02a056a327c3)
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
    "IByteMatchSetRef",
    "IIPSetRef",
    "IPSetReference",
    "IRuleRef",
    "ISizeConstraintSetRef",
    "ISqlInjectionMatchSetRef",
    "IWebACLRef",
    "IXssMatchSetRef",
    "RuleReference",
    "SizeConstraintSetReference",
    "SqlInjectionMatchSetReference",
    "WebACLReference",
    "XssMatchSetReference",
]

publication.publish()

def _typecheckingstub__25df697b9ab17fe1b773d854b2f5c70aa159a6fb8d6756627245e05ed77a4b31(
    *,
    byte_match_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35cdf0c2cdfab07f6acf02567f8ab2a59bc9c91ce52aa62128f6acabcd469724(
    *,
    ip_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74149078d582bf68f4aacb1a305d1d3f2fb45ef261ccc56e7c63591ae7891f54(
    *,
    rule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__889a99e81fb5a8b4397ad10771420e66c45fd8386b16f0211edae8fdfd3c8a9f(
    *,
    size_constraint_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b37e736344b81273bb8636bc1ea52a0a94dfcff852b60dd7acd02273847608d2(
    *,
    sql_injection_match_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4616ed55dce429e29803eeaefdfe2153afe64613d3092f3533830df30b7cb020(
    *,
    web_acl_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0941d18d86d76f76e620d1215586bd4683d80fbb7ca0f33f98d02a056a327c3(
    *,
    xss_match_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IByteMatchSetRef, IIPSetRef, IRuleRef, ISizeConstraintSetRef, ISqlInjectionMatchSetRef, IWebACLRef, IXssMatchSetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
