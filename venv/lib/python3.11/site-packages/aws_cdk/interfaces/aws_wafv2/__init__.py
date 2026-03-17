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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafv2.IIPSetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafv2.IIPSetRef"

    @builtins.property
    @jsii.member(jsii_name="ipSetRef")
    def ip_set_ref(self) -> "IPSetReference":
        '''(experimental) A reference to a IPSet resource.

        :stability: experimental
        '''
        return typing.cast("IPSetReference", jsii.get(self, "ipSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIPSetRef).__jsii_proxy_class__ = lambda : _IIPSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafv2.ILoggingConfigurationRef")
class ILoggingConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LoggingConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="loggingConfigurationRef")
    def logging_configuration_ref(self) -> "LoggingConfigurationReference":
        '''(experimental) A reference to a LoggingConfiguration resource.

        :stability: experimental
        '''
        ...


class _ILoggingConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LoggingConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafv2.ILoggingConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="loggingConfigurationRef")
    def logging_configuration_ref(self) -> "LoggingConfigurationReference":
        '''(experimental) A reference to a LoggingConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("LoggingConfigurationReference", jsii.get(self, "loggingConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILoggingConfigurationRef).__jsii_proxy_class__ = lambda : _ILoggingConfigurationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafv2.IPSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "ip_set_arn": "ipSetArn",
        "ip_set_id": "ipSetId",
        "ip_set_name": "ipSetName",
        "scope": "scope",
    },
)
class IPSetReference:
    def __init__(
        self,
        *,
        ip_set_arn: builtins.str,
        ip_set_id: builtins.str,
        ip_set_name: builtins.str,
        scope: builtins.str,
    ) -> None:
        '''A reference to a IPSet resource.

        :param ip_set_arn: The ARN of the IPSet resource.
        :param ip_set_id: The Id of the IPSet resource.
        :param ip_set_name: The Name of the IPSet resource.
        :param scope: The Scope of the IPSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafv2 as interfaces_wafv2
            
            i_pSet_reference = {
                "ip_set_arn": "ipSetArn",
                "ip_set_id": "ipSetId",
                "ip_set_name": "ipSetName",
                "scope": "scope"
            }
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14da68e48e2759634fcb6d667f58e1f3455fdbcdc35a8d57126e96392bffb906)
            check_type(argname="argument ip_set_arn", value=ip_set_arn, expected_type=type_hints["ip_set_arn"])
            check_type(argname="argument ip_set_id", value=ip_set_id, expected_type=type_hints["ip_set_id"])
            check_type(argname="argument ip_set_name", value=ip_set_name, expected_type=type_hints["ip_set_name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_set_arn": ip_set_arn,
            "ip_set_id": ip_set_id,
            "ip_set_name": ip_set_name,
            "scope": scope,
        }

    @builtins.property
    def ip_set_arn(self) -> builtins.str:
        '''The ARN of the IPSet resource.'''
        result = self._values.get("ip_set_arn")
        assert result is not None, "Required property 'ip_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_set_id(self) -> builtins.str:
        '''The Id of the IPSet resource.'''
        result = self._values.get("ip_set_id")
        assert result is not None, "Required property 'ip_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ip_set_name(self) -> builtins.str:
        '''The Name of the IPSet resource.'''
        result = self._values.get("ip_set_name")
        assert result is not None, "Required property 'ip_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''The Scope of the IPSet resource.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IPSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafv2.IRegexPatternSetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafv2.IRegexPatternSetRef"

    @builtins.property
    @jsii.member(jsii_name="regexPatternSetRef")
    def regex_pattern_set_ref(self) -> "RegexPatternSetReference":
        '''(experimental) A reference to a RegexPatternSet resource.

        :stability: experimental
        '''
        return typing.cast("RegexPatternSetReference", jsii.get(self, "regexPatternSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRegexPatternSetRef).__jsii_proxy_class__ = lambda : _IRegexPatternSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafv2.IRuleGroupRef")
class IRuleGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RuleGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ruleGroupRef")
    def rule_group_ref(self) -> "RuleGroupReference":
        '''(experimental) A reference to a RuleGroup resource.

        :stability: experimental
        '''
        ...


class _IRuleGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RuleGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafv2.IRuleGroupRef"

    @builtins.property
    @jsii.member(jsii_name="ruleGroupRef")
    def rule_group_ref(self) -> "RuleGroupReference":
        '''(experimental) A reference to a RuleGroup resource.

        :stability: experimental
        '''
        return typing.cast("RuleGroupReference", jsii.get(self, "ruleGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuleGroupRef).__jsii_proxy_class__ = lambda : _IRuleGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafv2.IWebACLAssociationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafv2.IWebACLAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="webAclAssociationRef")
    def web_acl_association_ref(self) -> "WebACLAssociationReference":
        '''(experimental) A reference to a WebACLAssociation resource.

        :stability: experimental
        '''
        return typing.cast("WebACLAssociationReference", jsii.get(self, "webAclAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWebACLAssociationRef).__jsii_proxy_class__ = lambda : _IWebACLAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_wafv2.IWebACLRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_wafv2.IWebACLRef"

    @builtins.property
    @jsii.member(jsii_name="webAclRef")
    def web_acl_ref(self) -> "WebACLReference":
        '''(experimental) A reference to a WebACL resource.

        :stability: experimental
        '''
        return typing.cast("WebACLReference", jsii.get(self, "webAclRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWebACLRef).__jsii_proxy_class__ = lambda : _IWebACLRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafv2.LoggingConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class LoggingConfigurationReference:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''A reference to a LoggingConfiguration resource.

        :param resource_arn: The ResourceArn of the LoggingConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafv2 as interfaces_wafv2
            
            logging_configuration_reference = interfaces_wafv2.LoggingConfigurationReference(
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4859d0350218b56ebbc8a74d6bcb2403960e6f3670ca0d6acf5f1459043e8ca1)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceArn of the LoggingConfiguration resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggingConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafv2.RegexPatternSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "regex_pattern_set_arn": "regexPatternSetArn",
        "regex_pattern_set_id": "regexPatternSetId",
        "regex_pattern_set_name": "regexPatternSetName",
        "scope": "scope",
    },
)
class RegexPatternSetReference:
    def __init__(
        self,
        *,
        regex_pattern_set_arn: builtins.str,
        regex_pattern_set_id: builtins.str,
        regex_pattern_set_name: builtins.str,
        scope: builtins.str,
    ) -> None:
        '''A reference to a RegexPatternSet resource.

        :param regex_pattern_set_arn: The ARN of the RegexPatternSet resource.
        :param regex_pattern_set_id: The Id of the RegexPatternSet resource.
        :param regex_pattern_set_name: The Name of the RegexPatternSet resource.
        :param scope: The Scope of the RegexPatternSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafv2 as interfaces_wafv2
            
            regex_pattern_set_reference = interfaces_wafv2.RegexPatternSetReference(
                regex_pattern_set_arn="regexPatternSetArn",
                regex_pattern_set_id="regexPatternSetId",
                regex_pattern_set_name="regexPatternSetName",
                scope="scope"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6eda1259f5a2452f2a4a8269ea6fd32d99cbde97603d6e2aba9faae69a159f7)
            check_type(argname="argument regex_pattern_set_arn", value=regex_pattern_set_arn, expected_type=type_hints["regex_pattern_set_arn"])
            check_type(argname="argument regex_pattern_set_id", value=regex_pattern_set_id, expected_type=type_hints["regex_pattern_set_id"])
            check_type(argname="argument regex_pattern_set_name", value=regex_pattern_set_name, expected_type=type_hints["regex_pattern_set_name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "regex_pattern_set_arn": regex_pattern_set_arn,
            "regex_pattern_set_id": regex_pattern_set_id,
            "regex_pattern_set_name": regex_pattern_set_name,
            "scope": scope,
        }

    @builtins.property
    def regex_pattern_set_arn(self) -> builtins.str:
        '''The ARN of the RegexPatternSet resource.'''
        result = self._values.get("regex_pattern_set_arn")
        assert result is not None, "Required property 'regex_pattern_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regex_pattern_set_id(self) -> builtins.str:
        '''The Id of the RegexPatternSet resource.'''
        result = self._values.get("regex_pattern_set_id")
        assert result is not None, "Required property 'regex_pattern_set_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def regex_pattern_set_name(self) -> builtins.str:
        '''The Name of the RegexPatternSet resource.'''
        result = self._values.get("regex_pattern_set_name")
        assert result is not None, "Required property 'regex_pattern_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''The Scope of the RegexPatternSet resource.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_wafv2.RuleGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "rule_group_arn": "ruleGroupArn",
        "rule_group_id": "ruleGroupId",
        "rule_group_name": "ruleGroupName",
        "scope": "scope",
    },
)
class RuleGroupReference:
    def __init__(
        self,
        *,
        rule_group_arn: builtins.str,
        rule_group_id: builtins.str,
        rule_group_name: builtins.str,
        scope: builtins.str,
    ) -> None:
        '''A reference to a RuleGroup resource.

        :param rule_group_arn: The ARN of the RuleGroup resource.
        :param rule_group_id: The Id of the RuleGroup resource.
        :param rule_group_name: The Name of the RuleGroup resource.
        :param scope: The Scope of the RuleGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafv2 as interfaces_wafv2
            
            rule_group_reference = interfaces_wafv2.RuleGroupReference(
                rule_group_arn="ruleGroupArn",
                rule_group_id="ruleGroupId",
                rule_group_name="ruleGroupName",
                scope="scope"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf76cfdfd6afba6918b3ce47752f91fcc44704d0247d474e30612f5149f2406)
            check_type(argname="argument rule_group_arn", value=rule_group_arn, expected_type=type_hints["rule_group_arn"])
            check_type(argname="argument rule_group_id", value=rule_group_id, expected_type=type_hints["rule_group_id"])
            check_type(argname="argument rule_group_name", value=rule_group_name, expected_type=type_hints["rule_group_name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_group_arn": rule_group_arn,
            "rule_group_id": rule_group_id,
            "rule_group_name": rule_group_name,
            "scope": scope,
        }

    @builtins.property
    def rule_group_arn(self) -> builtins.str:
        '''The ARN of the RuleGroup resource.'''
        result = self._values.get("rule_group_arn")
        assert result is not None, "Required property 'rule_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_group_id(self) -> builtins.str:
        '''The Id of the RuleGroup resource.'''
        result = self._values.get("rule_group_id")
        assert result is not None, "Required property 'rule_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_group_name(self) -> builtins.str:
        '''The Name of the RuleGroup resource.'''
        result = self._values.get("rule_group_name")
        assert result is not None, "Required property 'rule_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''The Scope of the RuleGroup resource.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_wafv2.WebACLAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn", "web_acl_arn": "webAclArn"},
)
class WebACLAssociationReference:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        web_acl_arn: builtins.str,
    ) -> None:
        '''A reference to a WebACLAssociation resource.

        :param resource_arn: The ResourceArn of the WebACLAssociation resource.
        :param web_acl_arn: The WebACLArn of the WebACLAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafv2 as interfaces_wafv2
            
            web_aCLAssociation_reference = interfaces_wafv2.WebACLAssociationReference(
                resource_arn="resourceArn",
                web_acl_arn="webAclArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9367e8c7c3f396f7d9dfa4cf2f55e4e2c21e1d9e67d8a37c42c4c3646fef66c)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument web_acl_arn", value=web_acl_arn, expected_type=type_hints["web_acl_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "web_acl_arn": web_acl_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceArn of the WebACLAssociation resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def web_acl_arn(self) -> builtins.str:
        '''The WebACLArn of the WebACLAssociation resource.'''
        result = self._values.get("web_acl_arn")
        assert result is not None, "Required property 'web_acl_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_wafv2.WebACLReference",
    jsii_struct_bases=[],
    name_mapping={
        "scope": "scope",
        "web_acl_arn": "webAclArn",
        "web_acl_id": "webAclId",
        "web_acl_name": "webAclName",
    },
)
class WebACLReference:
    def __init__(
        self,
        *,
        scope: builtins.str,
        web_acl_arn: builtins.str,
        web_acl_id: builtins.str,
        web_acl_name: builtins.str,
    ) -> None:
        '''A reference to a WebACL resource.

        :param scope: The Scope of the WebACL resource.
        :param web_acl_arn: The ARN of the WebACL resource.
        :param web_acl_id: The Id of the WebACL resource.
        :param web_acl_name: The Name of the WebACL resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_wafv2 as interfaces_wafv2
            
            web_aCLReference = interfaces_wafv2.WebACLReference(
                scope="scope",
                web_acl_arn="webAclArn",
                web_acl_id="webAclId",
                web_acl_name="webAclName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61d452f06c88f870c265edc3923363f145d35580ac212156b5e078800454ce22)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument web_acl_arn", value=web_acl_arn, expected_type=type_hints["web_acl_arn"])
            check_type(argname="argument web_acl_id", value=web_acl_id, expected_type=type_hints["web_acl_id"])
            check_type(argname="argument web_acl_name", value=web_acl_name, expected_type=type_hints["web_acl_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scope": scope,
            "web_acl_arn": web_acl_arn,
            "web_acl_id": web_acl_id,
            "web_acl_name": web_acl_name,
        }

    @builtins.property
    def scope(self) -> builtins.str:
        '''The Scope of the WebACL resource.'''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def web_acl_arn(self) -> builtins.str:
        '''The ARN of the WebACL resource.'''
        result = self._values.get("web_acl_arn")
        assert result is not None, "Required property 'web_acl_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def web_acl_id(self) -> builtins.str:
        '''The Id of the WebACL resource.'''
        result = self._values.get("web_acl_id")
        assert result is not None, "Required property 'web_acl_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def web_acl_name(self) -> builtins.str:
        '''The Name of the WebACL resource.'''
        result = self._values.get("web_acl_name")
        assert result is not None, "Required property 'web_acl_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebACLReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IIPSetRef",
    "ILoggingConfigurationRef",
    "IPSetReference",
    "IRegexPatternSetRef",
    "IRuleGroupRef",
    "IWebACLAssociationRef",
    "IWebACLRef",
    "LoggingConfigurationReference",
    "RegexPatternSetReference",
    "RuleGroupReference",
    "WebACLAssociationReference",
    "WebACLReference",
]

publication.publish()

def _typecheckingstub__14da68e48e2759634fcb6d667f58e1f3455fdbcdc35a8d57126e96392bffb906(
    *,
    ip_set_arn: builtins.str,
    ip_set_id: builtins.str,
    ip_set_name: builtins.str,
    scope: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4859d0350218b56ebbc8a74d6bcb2403960e6f3670ca0d6acf5f1459043e8ca1(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6eda1259f5a2452f2a4a8269ea6fd32d99cbde97603d6e2aba9faae69a159f7(
    *,
    regex_pattern_set_arn: builtins.str,
    regex_pattern_set_id: builtins.str,
    regex_pattern_set_name: builtins.str,
    scope: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf76cfdfd6afba6918b3ce47752f91fcc44704d0247d474e30612f5149f2406(
    *,
    rule_group_arn: builtins.str,
    rule_group_id: builtins.str,
    rule_group_name: builtins.str,
    scope: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9367e8c7c3f396f7d9dfa4cf2f55e4e2c21e1d9e67d8a37c42c4c3646fef66c(
    *,
    resource_arn: builtins.str,
    web_acl_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61d452f06c88f870c265edc3923363f145d35580ac212156b5e078800454ce22(
    *,
    scope: builtins.str,
    web_acl_arn: builtins.str,
    web_acl_id: builtins.str,
    web_acl_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IIPSetRef, ILoggingConfigurationRef, IRegexPatternSetRef, IRuleGroupRef, IWebACLAssociationRef, IWebACLRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
