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
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.FirewallDomainListReference",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_domain_list_arn": "firewallDomainListArn",
        "firewall_domain_list_id": "firewallDomainListId",
    },
)
class FirewallDomainListReference:
    def __init__(
        self,
        *,
        firewall_domain_list_arn: builtins.str,
        firewall_domain_list_id: builtins.str,
    ) -> None:
        '''A reference to a FirewallDomainList resource.

        :param firewall_domain_list_arn: The ARN of the FirewallDomainList resource.
        :param firewall_domain_list_id: The Id of the FirewallDomainList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            firewall_domain_list_reference = interfaces_route53resolver.FirewallDomainListReference(
                firewall_domain_list_arn="firewallDomainListArn",
                firewall_domain_list_id="firewallDomainListId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bf26bc13d02b48d108b0edfc29fb7bc53aef5731dbe1b57caba69dd98ecbfac)
            check_type(argname="argument firewall_domain_list_arn", value=firewall_domain_list_arn, expected_type=type_hints["firewall_domain_list_arn"])
            check_type(argname="argument firewall_domain_list_id", value=firewall_domain_list_id, expected_type=type_hints["firewall_domain_list_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_domain_list_arn": firewall_domain_list_arn,
            "firewall_domain_list_id": firewall_domain_list_id,
        }

    @builtins.property
    def firewall_domain_list_arn(self) -> builtins.str:
        '''The ARN of the FirewallDomainList resource.'''
        result = self._values.get("firewall_domain_list_arn")
        assert result is not None, "Required property 'firewall_domain_list_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firewall_domain_list_id(self) -> builtins.str:
        '''The Id of the FirewallDomainList resource.'''
        result = self._values.get("firewall_domain_list_id")
        assert result is not None, "Required property 'firewall_domain_list_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallDomainListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.FirewallRuleGroupAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_rule_group_association_arn": "firewallRuleGroupAssociationArn",
        "firewall_rule_group_association_id": "firewallRuleGroupAssociationId",
    },
)
class FirewallRuleGroupAssociationReference:
    def __init__(
        self,
        *,
        firewall_rule_group_association_arn: builtins.str,
        firewall_rule_group_association_id: builtins.str,
    ) -> None:
        '''A reference to a FirewallRuleGroupAssociation resource.

        :param firewall_rule_group_association_arn: The ARN of the FirewallRuleGroupAssociation resource.
        :param firewall_rule_group_association_id: The Id of the FirewallRuleGroupAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            firewall_rule_group_association_reference = interfaces_route53resolver.FirewallRuleGroupAssociationReference(
                firewall_rule_group_association_arn="firewallRuleGroupAssociationArn",
                firewall_rule_group_association_id="firewallRuleGroupAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46e8ff6df398f45a730cf43a6bbe148b653b85a105d71099a1c4fae3f1c35344)
            check_type(argname="argument firewall_rule_group_association_arn", value=firewall_rule_group_association_arn, expected_type=type_hints["firewall_rule_group_association_arn"])
            check_type(argname="argument firewall_rule_group_association_id", value=firewall_rule_group_association_id, expected_type=type_hints["firewall_rule_group_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_rule_group_association_arn": firewall_rule_group_association_arn,
            "firewall_rule_group_association_id": firewall_rule_group_association_id,
        }

    @builtins.property
    def firewall_rule_group_association_arn(self) -> builtins.str:
        '''The ARN of the FirewallRuleGroupAssociation resource.'''
        result = self._values.get("firewall_rule_group_association_arn")
        assert result is not None, "Required property 'firewall_rule_group_association_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firewall_rule_group_association_id(self) -> builtins.str:
        '''The Id of the FirewallRuleGroupAssociation resource.'''
        result = self._values.get("firewall_rule_group_association_id")
        assert result is not None, "Required property 'firewall_rule_group_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallRuleGroupAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.FirewallRuleGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "firewall_rule_group_arn": "firewallRuleGroupArn",
        "firewall_rule_group_id": "firewallRuleGroupId",
    },
)
class FirewallRuleGroupReference:
    def __init__(
        self,
        *,
        firewall_rule_group_arn: builtins.str,
        firewall_rule_group_id: builtins.str,
    ) -> None:
        '''A reference to a FirewallRuleGroup resource.

        :param firewall_rule_group_arn: The ARN of the FirewallRuleGroup resource.
        :param firewall_rule_group_id: The Id of the FirewallRuleGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            firewall_rule_group_reference = interfaces_route53resolver.FirewallRuleGroupReference(
                firewall_rule_group_arn="firewallRuleGroupArn",
                firewall_rule_group_id="firewallRuleGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3bb3b7e45198a710b1aebc5a8bde8be5e78ec122d40eda2d11f6a9553edc365)
            check_type(argname="argument firewall_rule_group_arn", value=firewall_rule_group_arn, expected_type=type_hints["firewall_rule_group_arn"])
            check_type(argname="argument firewall_rule_group_id", value=firewall_rule_group_id, expected_type=type_hints["firewall_rule_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "firewall_rule_group_arn": firewall_rule_group_arn,
            "firewall_rule_group_id": firewall_rule_group_id,
        }

    @builtins.property
    def firewall_rule_group_arn(self) -> builtins.str:
        '''The ARN of the FirewallRuleGroup resource.'''
        result = self._values.get("firewall_rule_group_arn")
        assert result is not None, "Required property 'firewall_rule_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def firewall_rule_group_id(self) -> builtins.str:
        '''The Id of the FirewallRuleGroup resource.'''
        result = self._values.get("firewall_rule_group_id")
        assert result is not None, "Required property 'firewall_rule_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FirewallRuleGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IFirewallDomainListRef"
)
class IFirewallDomainListRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallDomainList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="firewallDomainListRef")
    def firewall_domain_list_ref(self) -> "FirewallDomainListReference":
        '''(experimental) A reference to a FirewallDomainList resource.

        :stability: experimental
        '''
        ...


class _IFirewallDomainListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallDomainList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IFirewallDomainListRef"

    @builtins.property
    @jsii.member(jsii_name="firewallDomainListRef")
    def firewall_domain_list_ref(self) -> "FirewallDomainListReference":
        '''(experimental) A reference to a FirewallDomainList resource.

        :stability: experimental
        '''
        return typing.cast("FirewallDomainListReference", jsii.get(self, "firewallDomainListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFirewallDomainListRef).__jsii_proxy_class__ = lambda : _IFirewallDomainListRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IFirewallRuleGroupAssociationRef"
)
class IFirewallRuleGroupAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallRuleGroupAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="firewallRuleGroupAssociationRef")
    def firewall_rule_group_association_ref(
        self,
    ) -> "FirewallRuleGroupAssociationReference":
        '''(experimental) A reference to a FirewallRuleGroupAssociation resource.

        :stability: experimental
        '''
        ...


class _IFirewallRuleGroupAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallRuleGroupAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IFirewallRuleGroupAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="firewallRuleGroupAssociationRef")
    def firewall_rule_group_association_ref(
        self,
    ) -> "FirewallRuleGroupAssociationReference":
        '''(experimental) A reference to a FirewallRuleGroupAssociation resource.

        :stability: experimental
        '''
        return typing.cast("FirewallRuleGroupAssociationReference", jsii.get(self, "firewallRuleGroupAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFirewallRuleGroupAssociationRef).__jsii_proxy_class__ = lambda : _IFirewallRuleGroupAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IFirewallRuleGroupRef"
)
class IFirewallRuleGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallRuleGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="firewallRuleGroupRef")
    def firewall_rule_group_ref(self) -> "FirewallRuleGroupReference":
        '''(experimental) A reference to a FirewallRuleGroup resource.

        :stability: experimental
        '''
        ...


class _IFirewallRuleGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FirewallRuleGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IFirewallRuleGroupRef"

    @builtins.property
    @jsii.member(jsii_name="firewallRuleGroupRef")
    def firewall_rule_group_ref(self) -> "FirewallRuleGroupReference":
        '''(experimental) A reference to a FirewallRuleGroup resource.

        :stability: experimental
        '''
        return typing.cast("FirewallRuleGroupReference", jsii.get(self, "firewallRuleGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFirewallRuleGroupRef).__jsii_proxy_class__ = lambda : _IFirewallRuleGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IOutpostResolverRef"
)
class IOutpostResolverRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OutpostResolver.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="outpostResolverRef")
    def outpost_resolver_ref(self) -> "OutpostResolverReference":
        '''(experimental) A reference to a OutpostResolver resource.

        :stability: experimental
        '''
        ...


class _IOutpostResolverRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OutpostResolver.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IOutpostResolverRef"

    @builtins.property
    @jsii.member(jsii_name="outpostResolverRef")
    def outpost_resolver_ref(self) -> "OutpostResolverReference":
        '''(experimental) A reference to a OutpostResolver resource.

        :stability: experimental
        '''
        return typing.cast("OutpostResolverReference", jsii.get(self, "outpostResolverRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOutpostResolverRef).__jsii_proxy_class__ = lambda : _IOutpostResolverRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IResolverConfigRef"
)
class IResolverConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resolverConfigRef")
    def resolver_config_ref(self) -> "ResolverConfigReference":
        '''(experimental) A reference to a ResolverConfig resource.

        :stability: experimental
        '''
        ...


class _IResolverConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IResolverConfigRef"

    @builtins.property
    @jsii.member(jsii_name="resolverConfigRef")
    def resolver_config_ref(self) -> "ResolverConfigReference":
        '''(experimental) A reference to a ResolverConfig resource.

        :stability: experimental
        '''
        return typing.cast("ResolverConfigReference", jsii.get(self, "resolverConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolverConfigRef).__jsii_proxy_class__ = lambda : _IResolverConfigRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IResolverDNSSECConfigRef"
)
class IResolverDNSSECConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverDNSSECConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resolverDnssecConfigRef")
    def resolver_dnssec_config_ref(self) -> "ResolverDNSSECConfigReference":
        '''(experimental) A reference to a ResolverDNSSECConfig resource.

        :stability: experimental
        '''
        ...


class _IResolverDNSSECConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverDNSSECConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IResolverDNSSECConfigRef"

    @builtins.property
    @jsii.member(jsii_name="resolverDnssecConfigRef")
    def resolver_dnssec_config_ref(self) -> "ResolverDNSSECConfigReference":
        '''(experimental) A reference to a ResolverDNSSECConfig resource.

        :stability: experimental
        '''
        return typing.cast("ResolverDNSSECConfigReference", jsii.get(self, "resolverDnssecConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolverDNSSECConfigRef).__jsii_proxy_class__ = lambda : _IResolverDNSSECConfigRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IResolverEndpointRef"
)
class IResolverEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resolverEndpointRef")
    def resolver_endpoint_ref(self) -> "ResolverEndpointReference":
        '''(experimental) A reference to a ResolverEndpoint resource.

        :stability: experimental
        '''
        ...


class _IResolverEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IResolverEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="resolverEndpointRef")
    def resolver_endpoint_ref(self) -> "ResolverEndpointReference":
        '''(experimental) A reference to a ResolverEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("ResolverEndpointReference", jsii.get(self, "resolverEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolverEndpointRef).__jsii_proxy_class__ = lambda : _IResolverEndpointRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IResolverQueryLoggingConfigAssociationRef"
)
class IResolverQueryLoggingConfigAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverQueryLoggingConfigAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resolverQueryLoggingConfigAssociationRef")
    def resolver_query_logging_config_association_ref(
        self,
    ) -> "ResolverQueryLoggingConfigAssociationReference":
        '''(experimental) A reference to a ResolverQueryLoggingConfigAssociation resource.

        :stability: experimental
        '''
        ...


class _IResolverQueryLoggingConfigAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverQueryLoggingConfigAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IResolverQueryLoggingConfigAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="resolverQueryLoggingConfigAssociationRef")
    def resolver_query_logging_config_association_ref(
        self,
    ) -> "ResolverQueryLoggingConfigAssociationReference":
        '''(experimental) A reference to a ResolverQueryLoggingConfigAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ResolverQueryLoggingConfigAssociationReference", jsii.get(self, "resolverQueryLoggingConfigAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolverQueryLoggingConfigAssociationRef).__jsii_proxy_class__ = lambda : _IResolverQueryLoggingConfigAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IResolverQueryLoggingConfigRef"
)
class IResolverQueryLoggingConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverQueryLoggingConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resolverQueryLoggingConfigRef")
    def resolver_query_logging_config_ref(
        self,
    ) -> "ResolverQueryLoggingConfigReference":
        '''(experimental) A reference to a ResolverQueryLoggingConfig resource.

        :stability: experimental
        '''
        ...


class _IResolverQueryLoggingConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverQueryLoggingConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IResolverQueryLoggingConfigRef"

    @builtins.property
    @jsii.member(jsii_name="resolverQueryLoggingConfigRef")
    def resolver_query_logging_config_ref(
        self,
    ) -> "ResolverQueryLoggingConfigReference":
        '''(experimental) A reference to a ResolverQueryLoggingConfig resource.

        :stability: experimental
        '''
        return typing.cast("ResolverQueryLoggingConfigReference", jsii.get(self, "resolverQueryLoggingConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolverQueryLoggingConfigRef).__jsii_proxy_class__ = lambda : _IResolverQueryLoggingConfigRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IResolverRuleAssociationRef"
)
class IResolverRuleAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverRuleAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resolverRuleAssociationRef")
    def resolver_rule_association_ref(self) -> "ResolverRuleAssociationReference":
        '''(experimental) A reference to a ResolverRuleAssociation resource.

        :stability: experimental
        '''
        ...


class _IResolverRuleAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverRuleAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IResolverRuleAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="resolverRuleAssociationRef")
    def resolver_rule_association_ref(self) -> "ResolverRuleAssociationReference":
        '''(experimental) A reference to a ResolverRuleAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ResolverRuleAssociationReference", jsii.get(self, "resolverRuleAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolverRuleAssociationRef).__jsii_proxy_class__ = lambda : _IResolverRuleAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.IResolverRuleRef"
)
class IResolverRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resolverRuleRef")
    def resolver_rule_ref(self) -> "ResolverRuleReference":
        '''(experimental) A reference to a ResolverRule resource.

        :stability: experimental
        '''
        ...


class _IResolverRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResolverRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53resolver.IResolverRuleRef"

    @builtins.property
    @jsii.member(jsii_name="resolverRuleRef")
    def resolver_rule_ref(self) -> "ResolverRuleReference":
        '''(experimental) A reference to a ResolverRule resource.

        :stability: experimental
        '''
        return typing.cast("ResolverRuleReference", jsii.get(self, "resolverRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResolverRuleRef).__jsii_proxy_class__ = lambda : _IResolverRuleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.OutpostResolverReference",
    jsii_struct_bases=[],
    name_mapping={
        "outpost_resolver_arn": "outpostResolverArn",
        "outpost_resolver_id": "outpostResolverId",
    },
)
class OutpostResolverReference:
    def __init__(
        self,
        *,
        outpost_resolver_arn: builtins.str,
        outpost_resolver_id: builtins.str,
    ) -> None:
        '''A reference to a OutpostResolver resource.

        :param outpost_resolver_arn: The ARN of the OutpostResolver resource.
        :param outpost_resolver_id: The Id of the OutpostResolver resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            outpost_resolver_reference = interfaces_route53resolver.OutpostResolverReference(
                outpost_resolver_arn="outpostResolverArn",
                outpost_resolver_id="outpostResolverId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d8c072a122db5e03c5c035dc2260fb48d219428c3dfd96ee6e4b0a9f5d7d40)
            check_type(argname="argument outpost_resolver_arn", value=outpost_resolver_arn, expected_type=type_hints["outpost_resolver_arn"])
            check_type(argname="argument outpost_resolver_id", value=outpost_resolver_id, expected_type=type_hints["outpost_resolver_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "outpost_resolver_arn": outpost_resolver_arn,
            "outpost_resolver_id": outpost_resolver_id,
        }

    @builtins.property
    def outpost_resolver_arn(self) -> builtins.str:
        '''The ARN of the OutpostResolver resource.'''
        result = self._values.get("outpost_resolver_arn")
        assert result is not None, "Required property 'outpost_resolver_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def outpost_resolver_id(self) -> builtins.str:
        '''The Id of the OutpostResolver resource.'''
        result = self._values.get("outpost_resolver_id")
        assert result is not None, "Required property 'outpost_resolver_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OutpostResolverReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.ResolverConfigReference",
    jsii_struct_bases=[],
    name_mapping={"resource_id": "resourceId"},
)
class ResolverConfigReference:
    def __init__(self, *, resource_id: builtins.str) -> None:
        '''A reference to a ResolverConfig resource.

        :param resource_id: The ResourceId of the ResolverConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            resolver_config_reference = interfaces_route53resolver.ResolverConfigReference(
                resource_id="resourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58d5ae0ee1df899dbc217fd0725240d397063fd50893944ebf4629ab012e0cf7)
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_id": resource_id,
        }

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The ResourceId of the ResolverConfig resource.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.ResolverDNSSECConfigReference",
    jsii_struct_bases=[],
    name_mapping={"resolver_dnssec_config_id": "resolverDnssecConfigId"},
)
class ResolverDNSSECConfigReference:
    def __init__(self, *, resolver_dnssec_config_id: builtins.str) -> None:
        '''A reference to a ResolverDNSSECConfig resource.

        :param resolver_dnssec_config_id: The Id of the ResolverDNSSECConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            resolver_dNSSECConfig_reference = interfaces_route53resolver.ResolverDNSSECConfigReference(
                resolver_dnssec_config_id="resolverDnssecConfigId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dce2b54750214517feba4541a02f77768c4e02fa2592d2d4b50dd650c3ead18c)
            check_type(argname="argument resolver_dnssec_config_id", value=resolver_dnssec_config_id, expected_type=type_hints["resolver_dnssec_config_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resolver_dnssec_config_id": resolver_dnssec_config_id,
        }

    @builtins.property
    def resolver_dnssec_config_id(self) -> builtins.str:
        '''The Id of the ResolverDNSSECConfig resource.'''
        result = self._values.get("resolver_dnssec_config_id")
        assert result is not None, "Required property 'resolver_dnssec_config_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverDNSSECConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.ResolverEndpointReference",
    jsii_struct_bases=[],
    name_mapping={
        "resolver_endpoint_arn": "resolverEndpointArn",
        "resolver_endpoint_id": "resolverEndpointId",
    },
)
class ResolverEndpointReference:
    def __init__(
        self,
        *,
        resolver_endpoint_arn: builtins.str,
        resolver_endpoint_id: builtins.str,
    ) -> None:
        '''A reference to a ResolverEndpoint resource.

        :param resolver_endpoint_arn: The ARN of the ResolverEndpoint resource.
        :param resolver_endpoint_id: The ResolverEndpointId of the ResolverEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            resolver_endpoint_reference = interfaces_route53resolver.ResolverEndpointReference(
                resolver_endpoint_arn="resolverEndpointArn",
                resolver_endpoint_id="resolverEndpointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4aa7f314e764cb5c357ca22e41a1690a70f58c4ba08cf363ed38c3b51b2fda7)
            check_type(argname="argument resolver_endpoint_arn", value=resolver_endpoint_arn, expected_type=type_hints["resolver_endpoint_arn"])
            check_type(argname="argument resolver_endpoint_id", value=resolver_endpoint_id, expected_type=type_hints["resolver_endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resolver_endpoint_arn": resolver_endpoint_arn,
            "resolver_endpoint_id": resolver_endpoint_id,
        }

    @builtins.property
    def resolver_endpoint_arn(self) -> builtins.str:
        '''The ARN of the ResolverEndpoint resource.'''
        result = self._values.get("resolver_endpoint_arn")
        assert result is not None, "Required property 'resolver_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resolver_endpoint_id(self) -> builtins.str:
        '''The ResolverEndpointId of the ResolverEndpoint resource.'''
        result = self._values.get("resolver_endpoint_id")
        assert result is not None, "Required property 'resolver_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.ResolverQueryLoggingConfigAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "resolver_query_logging_config_association_id": "resolverQueryLoggingConfigAssociationId",
    },
)
class ResolverQueryLoggingConfigAssociationReference:
    def __init__(
        self,
        *,
        resolver_query_logging_config_association_id: builtins.str,
    ) -> None:
        '''A reference to a ResolverQueryLoggingConfigAssociation resource.

        :param resolver_query_logging_config_association_id: The Id of the ResolverQueryLoggingConfigAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            resolver_query_logging_config_association_reference = interfaces_route53resolver.ResolverQueryLoggingConfigAssociationReference(
                resolver_query_logging_config_association_id="resolverQueryLoggingConfigAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dff8c1f9e9bdd8143b0cfdd2a91d4f3f8431700a7ffe8b2a2f5c97cea7e2c5fe)
            check_type(argname="argument resolver_query_logging_config_association_id", value=resolver_query_logging_config_association_id, expected_type=type_hints["resolver_query_logging_config_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resolver_query_logging_config_association_id": resolver_query_logging_config_association_id,
        }

    @builtins.property
    def resolver_query_logging_config_association_id(self) -> builtins.str:
        '''The Id of the ResolverQueryLoggingConfigAssociation resource.'''
        result = self._values.get("resolver_query_logging_config_association_id")
        assert result is not None, "Required property 'resolver_query_logging_config_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverQueryLoggingConfigAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.ResolverQueryLoggingConfigReference",
    jsii_struct_bases=[],
    name_mapping={
        "resolver_query_logging_config_arn": "resolverQueryLoggingConfigArn",
        "resolver_query_logging_config_id": "resolverQueryLoggingConfigId",
    },
)
class ResolverQueryLoggingConfigReference:
    def __init__(
        self,
        *,
        resolver_query_logging_config_arn: builtins.str,
        resolver_query_logging_config_id: builtins.str,
    ) -> None:
        '''A reference to a ResolverQueryLoggingConfig resource.

        :param resolver_query_logging_config_arn: The ARN of the ResolverQueryLoggingConfig resource.
        :param resolver_query_logging_config_id: The Id of the ResolverQueryLoggingConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            resolver_query_logging_config_reference = interfaces_route53resolver.ResolverQueryLoggingConfigReference(
                resolver_query_logging_config_arn="resolverQueryLoggingConfigArn",
                resolver_query_logging_config_id="resolverQueryLoggingConfigId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0d5364a381ebab5d7aaa2797878ad7ea3ed07d3f527d78983ec42a2786415b6)
            check_type(argname="argument resolver_query_logging_config_arn", value=resolver_query_logging_config_arn, expected_type=type_hints["resolver_query_logging_config_arn"])
            check_type(argname="argument resolver_query_logging_config_id", value=resolver_query_logging_config_id, expected_type=type_hints["resolver_query_logging_config_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resolver_query_logging_config_arn": resolver_query_logging_config_arn,
            "resolver_query_logging_config_id": resolver_query_logging_config_id,
        }

    @builtins.property
    def resolver_query_logging_config_arn(self) -> builtins.str:
        '''The ARN of the ResolverQueryLoggingConfig resource.'''
        result = self._values.get("resolver_query_logging_config_arn")
        assert result is not None, "Required property 'resolver_query_logging_config_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resolver_query_logging_config_id(self) -> builtins.str:
        '''The Id of the ResolverQueryLoggingConfig resource.'''
        result = self._values.get("resolver_query_logging_config_id")
        assert result is not None, "Required property 'resolver_query_logging_config_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverQueryLoggingConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.ResolverRuleAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"resolver_rule_association_id": "resolverRuleAssociationId"},
)
class ResolverRuleAssociationReference:
    def __init__(self, *, resolver_rule_association_id: builtins.str) -> None:
        '''A reference to a ResolverRuleAssociation resource.

        :param resolver_rule_association_id: The ResolverRuleAssociationId of the ResolverRuleAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            resolver_rule_association_reference = interfaces_route53resolver.ResolverRuleAssociationReference(
                resolver_rule_association_id="resolverRuleAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57338d9a3b847259ab09be21e8fbf419560901185878b5668c79766211dbc4b0)
            check_type(argname="argument resolver_rule_association_id", value=resolver_rule_association_id, expected_type=type_hints["resolver_rule_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resolver_rule_association_id": resolver_rule_association_id,
        }

    @builtins.property
    def resolver_rule_association_id(self) -> builtins.str:
        '''The ResolverRuleAssociationId of the ResolverRuleAssociation resource.'''
        result = self._values.get("resolver_rule_association_id")
        assert result is not None, "Required property 'resolver_rule_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverRuleAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53resolver.ResolverRuleReference",
    jsii_struct_bases=[],
    name_mapping={
        "resolver_rule_arn": "resolverRuleArn",
        "resolver_rule_id": "resolverRuleId",
    },
)
class ResolverRuleReference:
    def __init__(
        self,
        *,
        resolver_rule_arn: builtins.str,
        resolver_rule_id: builtins.str,
    ) -> None:
        '''A reference to a ResolverRule resource.

        :param resolver_rule_arn: The ARN of the ResolverRule resource.
        :param resolver_rule_id: The ResolverRuleId of the ResolverRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53resolver as interfaces_route53resolver
            
            resolver_rule_reference = interfaces_route53resolver.ResolverRuleReference(
                resolver_rule_arn="resolverRuleArn",
                resolver_rule_id="resolverRuleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6baf9e71960d6a8381d3bcfa8868ee7ce3bb3b4f7b1146e63b09c3a0a704dea7)
            check_type(argname="argument resolver_rule_arn", value=resolver_rule_arn, expected_type=type_hints["resolver_rule_arn"])
            check_type(argname="argument resolver_rule_id", value=resolver_rule_id, expected_type=type_hints["resolver_rule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resolver_rule_arn": resolver_rule_arn,
            "resolver_rule_id": resolver_rule_id,
        }

    @builtins.property
    def resolver_rule_arn(self) -> builtins.str:
        '''The ARN of the ResolverRule resource.'''
        result = self._values.get("resolver_rule_arn")
        assert result is not None, "Required property 'resolver_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resolver_rule_id(self) -> builtins.str:
        '''The ResolverRuleId of the ResolverRule resource.'''
        result = self._values.get("resolver_rule_id")
        assert result is not None, "Required property 'resolver_rule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResolverRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "FirewallDomainListReference",
    "FirewallRuleGroupAssociationReference",
    "FirewallRuleGroupReference",
    "IFirewallDomainListRef",
    "IFirewallRuleGroupAssociationRef",
    "IFirewallRuleGroupRef",
    "IOutpostResolverRef",
    "IResolverConfigRef",
    "IResolverDNSSECConfigRef",
    "IResolverEndpointRef",
    "IResolverQueryLoggingConfigAssociationRef",
    "IResolverQueryLoggingConfigRef",
    "IResolverRuleAssociationRef",
    "IResolverRuleRef",
    "OutpostResolverReference",
    "ResolverConfigReference",
    "ResolverDNSSECConfigReference",
    "ResolverEndpointReference",
    "ResolverQueryLoggingConfigAssociationReference",
    "ResolverQueryLoggingConfigReference",
    "ResolverRuleAssociationReference",
    "ResolverRuleReference",
]

publication.publish()

def _typecheckingstub__1bf26bc13d02b48d108b0edfc29fb7bc53aef5731dbe1b57caba69dd98ecbfac(
    *,
    firewall_domain_list_arn: builtins.str,
    firewall_domain_list_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46e8ff6df398f45a730cf43a6bbe148b653b85a105d71099a1c4fae3f1c35344(
    *,
    firewall_rule_group_association_arn: builtins.str,
    firewall_rule_group_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3bb3b7e45198a710b1aebc5a8bde8be5e78ec122d40eda2d11f6a9553edc365(
    *,
    firewall_rule_group_arn: builtins.str,
    firewall_rule_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d8c072a122db5e03c5c035dc2260fb48d219428c3dfd96ee6e4b0a9f5d7d40(
    *,
    outpost_resolver_arn: builtins.str,
    outpost_resolver_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58d5ae0ee1df899dbc217fd0725240d397063fd50893944ebf4629ab012e0cf7(
    *,
    resource_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dce2b54750214517feba4541a02f77768c4e02fa2592d2d4b50dd650c3ead18c(
    *,
    resolver_dnssec_config_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4aa7f314e764cb5c357ca22e41a1690a70f58c4ba08cf363ed38c3b51b2fda7(
    *,
    resolver_endpoint_arn: builtins.str,
    resolver_endpoint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dff8c1f9e9bdd8143b0cfdd2a91d4f3f8431700a7ffe8b2a2f5c97cea7e2c5fe(
    *,
    resolver_query_logging_config_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0d5364a381ebab5d7aaa2797878ad7ea3ed07d3f527d78983ec42a2786415b6(
    *,
    resolver_query_logging_config_arn: builtins.str,
    resolver_query_logging_config_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57338d9a3b847259ab09be21e8fbf419560901185878b5668c79766211dbc4b0(
    *,
    resolver_rule_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6baf9e71960d6a8381d3bcfa8868ee7ce3bb3b4f7b1146e63b09c3a0a704dea7(
    *,
    resolver_rule_arn: builtins.str,
    resolver_rule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IFirewallDomainListRef, IFirewallRuleGroupAssociationRef, IFirewallRuleGroupRef, IOutpostResolverRef, IResolverConfigRef, IResolverDNSSECConfigRef, IResolverEndpointRef, IResolverQueryLoggingConfigAssociationRef, IResolverQueryLoggingConfigRef, IResolverRuleAssociationRef, IResolverRuleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
