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
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.AccessLogSubscriptionReference",
    jsii_struct_bases=[],
    name_mapping={"access_log_subscription_arn": "accessLogSubscriptionArn"},
)
class AccessLogSubscriptionReference:
    def __init__(self, *, access_log_subscription_arn: builtins.str) -> None:
        '''A reference to a AccessLogSubscription resource.

        :param access_log_subscription_arn: The Arn of the AccessLogSubscription resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            access_log_subscription_reference = interfaces_vpclattice.AccessLogSubscriptionReference(
                access_log_subscription_arn="accessLogSubscriptionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eee6fd0541b13ea53ebc8ac1ffc56bc5e0359ce79eb968e43350edd24063121d)
            check_type(argname="argument access_log_subscription_arn", value=access_log_subscription_arn, expected_type=type_hints["access_log_subscription_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_log_subscription_arn": access_log_subscription_arn,
        }

    @builtins.property
    def access_log_subscription_arn(self) -> builtins.str:
        '''The Arn of the AccessLogSubscription resource.'''
        result = self._values.get("access_log_subscription_arn")
        assert result is not None, "Required property 'access_log_subscription_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessLogSubscriptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.AuthPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"resource_identifier": "resourceIdentifier"},
)
class AuthPolicyReference:
    def __init__(self, *, resource_identifier: builtins.str) -> None:
        '''A reference to a AuthPolicy resource.

        :param resource_identifier: The ResourceIdentifier of the AuthPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            auth_policy_reference = interfaces_vpclattice.AuthPolicyReference(
                resource_identifier="resourceIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b4222593547993629599ee186ee2a7ac5673c4cd311653690629108d2b945f1)
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_identifier": resource_identifier,
        }

    @builtins.property
    def resource_identifier(self) -> builtins.str:
        '''The ResourceIdentifier of the AuthPolicy resource.'''
        result = self._values.get("resource_identifier")
        assert result is not None, "Required property 'resource_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AuthPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.DomainVerificationReference",
    jsii_struct_bases=[],
    name_mapping={"domain_verification_arn": "domainVerificationArn"},
)
class DomainVerificationReference:
    def __init__(self, *, domain_verification_arn: builtins.str) -> None:
        '''A reference to a DomainVerification resource.

        :param domain_verification_arn: The Arn of the DomainVerification resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            domain_verification_reference = interfaces_vpclattice.DomainVerificationReference(
                domain_verification_arn="domainVerificationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ef18a4e614451bd32b33743bc39d1adf9ef27a0a1833a41e87b1c46cc07d2a7)
            check_type(argname="argument domain_verification_arn", value=domain_verification_arn, expected_type=type_hints["domain_verification_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_verification_arn": domain_verification_arn,
        }

    @builtins.property
    def domain_verification_arn(self) -> builtins.str:
        '''The Arn of the DomainVerification resource.'''
        result = self._values.get("domain_verification_arn")
        assert result is not None, "Required property 'domain_verification_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainVerificationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IAccessLogSubscriptionRef"
)
class IAccessLogSubscriptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessLogSubscription.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessLogSubscriptionRef")
    def access_log_subscription_ref(self) -> "AccessLogSubscriptionReference":
        '''(experimental) A reference to a AccessLogSubscription resource.

        :stability: experimental
        '''
        ...


class _IAccessLogSubscriptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessLogSubscription.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IAccessLogSubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="accessLogSubscriptionRef")
    def access_log_subscription_ref(self) -> "AccessLogSubscriptionReference":
        '''(experimental) A reference to a AccessLogSubscription resource.

        :stability: experimental
        '''
        return typing.cast("AccessLogSubscriptionReference", jsii.get(self, "accessLogSubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessLogSubscriptionRef).__jsii_proxy_class__ = lambda : _IAccessLogSubscriptionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IAuthPolicyRef")
class IAuthPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AuthPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="authPolicyRef")
    def auth_policy_ref(self) -> "AuthPolicyReference":
        '''(experimental) A reference to a AuthPolicy resource.

        :stability: experimental
        '''
        ...


class _IAuthPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AuthPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IAuthPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="authPolicyRef")
    def auth_policy_ref(self) -> "AuthPolicyReference":
        '''(experimental) A reference to a AuthPolicy resource.

        :stability: experimental
        '''
        return typing.cast("AuthPolicyReference", jsii.get(self, "authPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAuthPolicyRef).__jsii_proxy_class__ = lambda : _IAuthPolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IDomainVerificationRef"
)
class IDomainVerificationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DomainVerification.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainVerificationRef")
    def domain_verification_ref(self) -> "DomainVerificationReference":
        '''(experimental) A reference to a DomainVerification resource.

        :stability: experimental
        '''
        ...


class _IDomainVerificationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DomainVerification.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IDomainVerificationRef"

    @builtins.property
    @jsii.member(jsii_name="domainVerificationRef")
    def domain_verification_ref(self) -> "DomainVerificationReference":
        '''(experimental) A reference to a DomainVerification resource.

        :stability: experimental
        '''
        return typing.cast("DomainVerificationReference", jsii.get(self, "domainVerificationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainVerificationRef).__jsii_proxy_class__ = lambda : _IDomainVerificationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IListenerRef")
class IListenerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Listener.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="listenerRef")
    def listener_ref(self) -> "ListenerReference":
        '''(experimental) A reference to a Listener resource.

        :stability: experimental
        '''
        ...


class _IListenerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Listener.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IListenerRef"

    @builtins.property
    @jsii.member(jsii_name="listenerRef")
    def listener_ref(self) -> "ListenerReference":
        '''(experimental) A reference to a Listener resource.

        :stability: experimental
        '''
        return typing.cast("ListenerReference", jsii.get(self, "listenerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IListenerRef).__jsii_proxy_class__ = lambda : _IListenerRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IResourceConfigurationRef"
)
class IResourceConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceConfigurationRef")
    def resource_configuration_ref(self) -> "ResourceConfigurationReference":
        '''(experimental) A reference to a ResourceConfiguration resource.

        :stability: experimental
        '''
        ...


class _IResourceConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IResourceConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="resourceConfigurationRef")
    def resource_configuration_ref(self) -> "ResourceConfigurationReference":
        '''(experimental) A reference to a ResourceConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("ResourceConfigurationReference", jsii.get(self, "resourceConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceConfigurationRef).__jsii_proxy_class__ = lambda : _IResourceConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IResourceGatewayRef")
class IResourceGatewayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceGateway.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceGatewayRef")
    def resource_gateway_ref(self) -> "ResourceGatewayReference":
        '''(experimental) A reference to a ResourceGateway resource.

        :stability: experimental
        '''
        ...


class _IResourceGatewayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceGateway.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IResourceGatewayRef"

    @builtins.property
    @jsii.member(jsii_name="resourceGatewayRef")
    def resource_gateway_ref(self) -> "ResourceGatewayReference":
        '''(experimental) A reference to a ResourceGateway resource.

        :stability: experimental
        '''
        return typing.cast("ResourceGatewayReference", jsii.get(self, "resourceGatewayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceGatewayRef).__jsii_proxy_class__ = lambda : _IResourceGatewayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IResourcePolicyRef")
class IResourcePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        ...


class _IResourcePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IRuleRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IRuleRef"

    @builtins.property
    @jsii.member(jsii_name="ruleRef")
    def rule_ref(self) -> "RuleReference":
        '''(experimental) A reference to a Rule resource.

        :stability: experimental
        '''
        return typing.cast("RuleReference", jsii.get(self, "ruleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuleRef).__jsii_proxy_class__ = lambda : _IRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IServiceNetworkRef")
class IServiceNetworkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceNetwork.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceNetworkRef")
    def service_network_ref(self) -> "ServiceNetworkReference":
        '''(experimental) A reference to a ServiceNetwork resource.

        :stability: experimental
        '''
        ...


class _IServiceNetworkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceNetwork.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IServiceNetworkRef"

    @builtins.property
    @jsii.member(jsii_name="serviceNetworkRef")
    def service_network_ref(self) -> "ServiceNetworkReference":
        '''(experimental) A reference to a ServiceNetwork resource.

        :stability: experimental
        '''
        return typing.cast("ServiceNetworkReference", jsii.get(self, "serviceNetworkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceNetworkRef).__jsii_proxy_class__ = lambda : _IServiceNetworkRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IServiceNetworkResourceAssociationRef"
)
class IServiceNetworkResourceAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceNetworkResourceAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceNetworkResourceAssociationRef")
    def service_network_resource_association_ref(
        self,
    ) -> "ServiceNetworkResourceAssociationReference":
        '''(experimental) A reference to a ServiceNetworkResourceAssociation resource.

        :stability: experimental
        '''
        ...


class _IServiceNetworkResourceAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceNetworkResourceAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IServiceNetworkResourceAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="serviceNetworkResourceAssociationRef")
    def service_network_resource_association_ref(
        self,
    ) -> "ServiceNetworkResourceAssociationReference":
        '''(experimental) A reference to a ServiceNetworkResourceAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ServiceNetworkResourceAssociationReference", jsii.get(self, "serviceNetworkResourceAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceNetworkResourceAssociationRef).__jsii_proxy_class__ = lambda : _IServiceNetworkResourceAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IServiceNetworkServiceAssociationRef"
)
class IServiceNetworkServiceAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceNetworkServiceAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceNetworkServiceAssociationRef")
    def service_network_service_association_ref(
        self,
    ) -> "ServiceNetworkServiceAssociationReference":
        '''(experimental) A reference to a ServiceNetworkServiceAssociation resource.

        :stability: experimental
        '''
        ...


class _IServiceNetworkServiceAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceNetworkServiceAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IServiceNetworkServiceAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="serviceNetworkServiceAssociationRef")
    def service_network_service_association_ref(
        self,
    ) -> "ServiceNetworkServiceAssociationReference":
        '''(experimental) A reference to a ServiceNetworkServiceAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ServiceNetworkServiceAssociationReference", jsii.get(self, "serviceNetworkServiceAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceNetworkServiceAssociationRef).__jsii_proxy_class__ = lambda : _IServiceNetworkServiceAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IServiceNetworkVpcAssociationRef"
)
class IServiceNetworkVpcAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceNetworkVpcAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceNetworkVpcAssociationRef")
    def service_network_vpc_association_ref(
        self,
    ) -> "ServiceNetworkVpcAssociationReference":
        '''(experimental) A reference to a ServiceNetworkVpcAssociation resource.

        :stability: experimental
        '''
        ...


class _IServiceNetworkVpcAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceNetworkVpcAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IServiceNetworkVpcAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="serviceNetworkVpcAssociationRef")
    def service_network_vpc_association_ref(
        self,
    ) -> "ServiceNetworkVpcAssociationReference":
        '''(experimental) A reference to a ServiceNetworkVpcAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ServiceNetworkVpcAssociationReference", jsii.get(self, "serviceNetworkVpcAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceNetworkVpcAssociationRef).__jsii_proxy_class__ = lambda : _IServiceNetworkVpcAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.IServiceRef")
class IServiceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        ...


class _IServiceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.IServiceRef"

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        return typing.cast("ServiceReference", jsii.get(self, "serviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceRef).__jsii_proxy_class__ = lambda : _IServiceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.ITargetGroupRef")
class ITargetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TargetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="targetGroupRef")
    def target_group_ref(self) -> "TargetGroupReference":
        '''(experimental) A reference to a TargetGroup resource.

        :stability: experimental
        '''
        ...


class _ITargetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TargetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_vpclattice.ITargetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="targetGroupRef")
    def target_group_ref(self) -> "TargetGroupReference":
        '''(experimental) A reference to a TargetGroup resource.

        :stability: experimental
        '''
        return typing.cast("TargetGroupReference", jsii.get(self, "targetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITargetGroupRef).__jsii_proxy_class__ = lambda : _ITargetGroupRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.ListenerReference",
    jsii_struct_bases=[],
    name_mapping={"listener_arn": "listenerArn"},
)
class ListenerReference:
    def __init__(self, *, listener_arn: builtins.str) -> None:
        '''A reference to a Listener resource.

        :param listener_arn: The Arn of the Listener resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            listener_reference = interfaces_vpclattice.ListenerReference(
                listener_arn="listenerArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__965fa1eba5e1af07399f1753a49579bbc9eaba99382ef68fe7f40a2f74c8f6c5)
            check_type(argname="argument listener_arn", value=listener_arn, expected_type=type_hints["listener_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "listener_arn": listener_arn,
        }

    @builtins.property
    def listener_arn(self) -> builtins.str:
        '''The Arn of the Listener resource.'''
        result = self._values.get("listener_arn")
        assert result is not None, "Required property 'listener_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ListenerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.ResourceConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"resource_configuration_arn": "resourceConfigurationArn"},
)
class ResourceConfigurationReference:
    def __init__(self, *, resource_configuration_arn: builtins.str) -> None:
        '''A reference to a ResourceConfiguration resource.

        :param resource_configuration_arn: The Arn of the ResourceConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            resource_configuration_reference = interfaces_vpclattice.ResourceConfigurationReference(
                resource_configuration_arn="resourceConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01aa1731f7400fd0fbbd0ab9e562e01167b82272f7ae845c5ba128ef8c3f653c)
            check_type(argname="argument resource_configuration_arn", value=resource_configuration_arn, expected_type=type_hints["resource_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_configuration_arn": resource_configuration_arn,
        }

    @builtins.property
    def resource_configuration_arn(self) -> builtins.str:
        '''The Arn of the ResourceConfiguration resource.'''
        result = self._values.get("resource_configuration_arn")
        assert result is not None, "Required property 'resource_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.ResourceGatewayReference",
    jsii_struct_bases=[],
    name_mapping={"resource_gateway_arn": "resourceGatewayArn"},
)
class ResourceGatewayReference:
    def __init__(self, *, resource_gateway_arn: builtins.str) -> None:
        '''A reference to a ResourceGateway resource.

        :param resource_gateway_arn: The Arn of the ResourceGateway resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            resource_gateway_reference = interfaces_vpclattice.ResourceGatewayReference(
                resource_gateway_arn="resourceGatewayArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eeeed4911e0d5b52f7c408387c0bd049c15579a4b74cd3572476a786d4753eb)
            check_type(argname="argument resource_gateway_arn", value=resource_gateway_arn, expected_type=type_hints["resource_gateway_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_gateway_arn": resource_gateway_arn,
        }

    @builtins.property
    def resource_gateway_arn(self) -> builtins.str:
        '''The Arn of the ResourceGateway resource.'''
        result = self._values.get("resource_gateway_arn")
        assert result is not None, "Required property 'resource_gateway_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceGatewayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"resource_arn": "resourceArn"},
)
class ResourcePolicyReference:
    def __init__(self, *, resource_arn: builtins.str) -> None:
        '''A reference to a ResourcePolicy resource.

        :param resource_arn: The ResourceArn of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            resource_policy_reference = interfaces_vpclattice.ResourcePolicyReference(
                resource_arn="resourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__979a24e39dd99ef98df1c5a8972fbad3c260a89832ff509fd71b9fa660ea698e)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceArn of the ResourcePolicy resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.RuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class RuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a Rule resource.

        :param rule_arn: The Arn of the Rule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            rule_reference = interfaces_vpclattice.RuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c31697e252076f82b6f5809ae5f1f181f88393d4517665f9a0a4199acae70a5d)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The Arn of the Rule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.ServiceNetworkReference",
    jsii_struct_bases=[],
    name_mapping={"service_network_arn": "serviceNetworkArn"},
)
class ServiceNetworkReference:
    def __init__(self, *, service_network_arn: builtins.str) -> None:
        '''A reference to a ServiceNetwork resource.

        :param service_network_arn: The Arn of the ServiceNetwork resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            service_network_reference = interfaces_vpclattice.ServiceNetworkReference(
                service_network_arn="serviceNetworkArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6b48f322c42a5f3c8df7ec325e22835870e9672b9e4889c1209482c9f3752a0)
            check_type(argname="argument service_network_arn", value=service_network_arn, expected_type=type_hints["service_network_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_network_arn": service_network_arn,
        }

    @builtins.property
    def service_network_arn(self) -> builtins.str:
        '''The Arn of the ServiceNetwork resource.'''
        result = self._values.get("service_network_arn")
        assert result is not None, "Required property 'service_network_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceNetworkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.ServiceNetworkResourceAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "service_network_resource_association_arn": "serviceNetworkResourceAssociationArn",
    },
)
class ServiceNetworkResourceAssociationReference:
    def __init__(
        self,
        *,
        service_network_resource_association_arn: builtins.str,
    ) -> None:
        '''A reference to a ServiceNetworkResourceAssociation resource.

        :param service_network_resource_association_arn: The Arn of the ServiceNetworkResourceAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            service_network_resource_association_reference = interfaces_vpclattice.ServiceNetworkResourceAssociationReference(
                service_network_resource_association_arn="serviceNetworkResourceAssociationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3f3a759e496df615d490ce6d7b13e4b0e5bcd68e9359b341b1eb6a49fefec2a)
            check_type(argname="argument service_network_resource_association_arn", value=service_network_resource_association_arn, expected_type=type_hints["service_network_resource_association_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_network_resource_association_arn": service_network_resource_association_arn,
        }

    @builtins.property
    def service_network_resource_association_arn(self) -> builtins.str:
        '''The Arn of the ServiceNetworkResourceAssociation resource.'''
        result = self._values.get("service_network_resource_association_arn")
        assert result is not None, "Required property 'service_network_resource_association_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceNetworkResourceAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.ServiceNetworkServiceAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "service_network_service_association_arn": "serviceNetworkServiceAssociationArn",
    },
)
class ServiceNetworkServiceAssociationReference:
    def __init__(
        self,
        *,
        service_network_service_association_arn: builtins.str,
    ) -> None:
        '''A reference to a ServiceNetworkServiceAssociation resource.

        :param service_network_service_association_arn: The Arn of the ServiceNetworkServiceAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            service_network_service_association_reference = interfaces_vpclattice.ServiceNetworkServiceAssociationReference(
                service_network_service_association_arn="serviceNetworkServiceAssociationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1058a21f7886e4433c3556e40928eb116b3a6aeb9d2d6acdf1cf89fd60310902)
            check_type(argname="argument service_network_service_association_arn", value=service_network_service_association_arn, expected_type=type_hints["service_network_service_association_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_network_service_association_arn": service_network_service_association_arn,
        }

    @builtins.property
    def service_network_service_association_arn(self) -> builtins.str:
        '''The Arn of the ServiceNetworkServiceAssociation resource.'''
        result = self._values.get("service_network_service_association_arn")
        assert result is not None, "Required property 'service_network_service_association_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceNetworkServiceAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.ServiceNetworkVpcAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "service_network_vpc_association_arn": "serviceNetworkVpcAssociationArn",
    },
)
class ServiceNetworkVpcAssociationReference:
    def __init__(self, *, service_network_vpc_association_arn: builtins.str) -> None:
        '''A reference to a ServiceNetworkVpcAssociation resource.

        :param service_network_vpc_association_arn: The Arn of the ServiceNetworkVpcAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            service_network_vpc_association_reference = interfaces_vpclattice.ServiceNetworkVpcAssociationReference(
                service_network_vpc_association_arn="serviceNetworkVpcAssociationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df01d5099e197e14c354e1d86f9d79642c3c274bea656dd0c1afb850adc133b2)
            check_type(argname="argument service_network_vpc_association_arn", value=service_network_vpc_association_arn, expected_type=type_hints["service_network_vpc_association_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_network_vpc_association_arn": service_network_vpc_association_arn,
        }

    @builtins.property
    def service_network_vpc_association_arn(self) -> builtins.str:
        '''The Arn of the ServiceNetworkVpcAssociation resource.'''
        result = self._values.get("service_network_vpc_association_arn")
        assert result is not None, "Required property 'service_network_vpc_association_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceNetworkVpcAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.ServiceReference",
    jsii_struct_bases=[],
    name_mapping={"service_arn": "serviceArn"},
)
class ServiceReference:
    def __init__(self, *, service_arn: builtins.str) -> None:
        '''A reference to a Service resource.

        :param service_arn: The Arn of the Service resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            service_reference = interfaces_vpclattice.ServiceReference(
                service_arn="serviceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44f1d49d464523b529c3f2efb035ca9ff8374bda21eac01e5e2858a53c52ce1a)
            check_type(argname="argument service_arn", value=service_arn, expected_type=type_hints["service_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_arn": service_arn,
        }

    @builtins.property
    def service_arn(self) -> builtins.str:
        '''The Arn of the Service resource.'''
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_vpclattice.TargetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"target_group_arn": "targetGroupArn"},
)
class TargetGroupReference:
    def __init__(self, *, target_group_arn: builtins.str) -> None:
        '''A reference to a TargetGroup resource.

        :param target_group_arn: The Arn of the TargetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_vpclattice as interfaces_vpclattice
            
            target_group_reference = interfaces_vpclattice.TargetGroupReference(
                target_group_arn="targetGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41490e38d96c29ab679d2317b367a7029adf48425cfcd15e0615e8325d1d57ae)
            check_type(argname="argument target_group_arn", value=target_group_arn, expected_type=type_hints["target_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_group_arn": target_group_arn,
        }

    @builtins.property
    def target_group_arn(self) -> builtins.str:
        '''The Arn of the TargetGroup resource.'''
        result = self._values.get("target_group_arn")
        assert result is not None, "Required property 'target_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TargetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessLogSubscriptionReference",
    "AuthPolicyReference",
    "DomainVerificationReference",
    "IAccessLogSubscriptionRef",
    "IAuthPolicyRef",
    "IDomainVerificationRef",
    "IListenerRef",
    "IResourceConfigurationRef",
    "IResourceGatewayRef",
    "IResourcePolicyRef",
    "IRuleRef",
    "IServiceNetworkRef",
    "IServiceNetworkResourceAssociationRef",
    "IServiceNetworkServiceAssociationRef",
    "IServiceNetworkVpcAssociationRef",
    "IServiceRef",
    "ITargetGroupRef",
    "ListenerReference",
    "ResourceConfigurationReference",
    "ResourceGatewayReference",
    "ResourcePolicyReference",
    "RuleReference",
    "ServiceNetworkReference",
    "ServiceNetworkResourceAssociationReference",
    "ServiceNetworkServiceAssociationReference",
    "ServiceNetworkVpcAssociationReference",
    "ServiceReference",
    "TargetGroupReference",
]

publication.publish()

def _typecheckingstub__eee6fd0541b13ea53ebc8ac1ffc56bc5e0359ce79eb968e43350edd24063121d(
    *,
    access_log_subscription_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b4222593547993629599ee186ee2a7ac5673c4cd311653690629108d2b945f1(
    *,
    resource_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ef18a4e614451bd32b33743bc39d1adf9ef27a0a1833a41e87b1c46cc07d2a7(
    *,
    domain_verification_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__965fa1eba5e1af07399f1753a49579bbc9eaba99382ef68fe7f40a2f74c8f6c5(
    *,
    listener_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01aa1731f7400fd0fbbd0ab9e562e01167b82272f7ae845c5ba128ef8c3f653c(
    *,
    resource_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eeeed4911e0d5b52f7c408387c0bd049c15579a4b74cd3572476a786d4753eb(
    *,
    resource_gateway_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979a24e39dd99ef98df1c5a8972fbad3c260a89832ff509fd71b9fa660ea698e(
    *,
    resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c31697e252076f82b6f5809ae5f1f181f88393d4517665f9a0a4199acae70a5d(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6b48f322c42a5f3c8df7ec325e22835870e9672b9e4889c1209482c9f3752a0(
    *,
    service_network_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3f3a759e496df615d490ce6d7b13e4b0e5bcd68e9359b341b1eb6a49fefec2a(
    *,
    service_network_resource_association_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1058a21f7886e4433c3556e40928eb116b3a6aeb9d2d6acdf1cf89fd60310902(
    *,
    service_network_service_association_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df01d5099e197e14c354e1d86f9d79642c3c274bea656dd0c1afb850adc133b2(
    *,
    service_network_vpc_association_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44f1d49d464523b529c3f2efb035ca9ff8374bda21eac01e5e2858a53c52ce1a(
    *,
    service_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41490e38d96c29ab679d2317b367a7029adf48425cfcd15e0615e8325d1d57ae(
    *,
    target_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessLogSubscriptionRef, IAuthPolicyRef, IDomainVerificationRef, IListenerRef, IResourceConfigurationRef, IResourceGatewayRef, IResourcePolicyRef, IRuleRef, IServiceNetworkRef, IServiceNetworkResourceAssociationRef, IServiceNetworkServiceAssociationRef, IServiceNetworkVpcAssociationRef, IServiceRef, ITargetGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
