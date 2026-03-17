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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IIdentityPoolPrincipalTagRef"
)
class IIdentityPoolPrincipalTagRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityPoolPrincipalTag.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="identityPoolPrincipalTagRef")
    def identity_pool_principal_tag_ref(self) -> "IdentityPoolPrincipalTagReference":
        '''(experimental) A reference to a IdentityPoolPrincipalTag resource.

        :stability: experimental
        '''
        ...


class _IIdentityPoolPrincipalTagRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityPoolPrincipalTag.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IIdentityPoolPrincipalTagRef"

    @builtins.property
    @jsii.member(jsii_name="identityPoolPrincipalTagRef")
    def identity_pool_principal_tag_ref(self) -> "IdentityPoolPrincipalTagReference":
        '''(experimental) A reference to a IdentityPoolPrincipalTag resource.

        :stability: experimental
        '''
        return typing.cast("IdentityPoolPrincipalTagReference", jsii.get(self, "identityPoolPrincipalTagRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentityPoolPrincipalTagRef).__jsii_proxy_class__ = lambda : _IIdentityPoolPrincipalTagRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cognito.IIdentityPoolRef")
class IIdentityPoolRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityPool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="identityPoolRef")
    def identity_pool_ref(self) -> "IdentityPoolReference":
        '''(experimental) A reference to a IdentityPool resource.

        :stability: experimental
        '''
        ...


class _IIdentityPoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityPool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IIdentityPoolRef"

    @builtins.property
    @jsii.member(jsii_name="identityPoolRef")
    def identity_pool_ref(self) -> "IdentityPoolReference":
        '''(experimental) A reference to a IdentityPool resource.

        :stability: experimental
        '''
        return typing.cast("IdentityPoolReference", jsii.get(self, "identityPoolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentityPoolRef).__jsii_proxy_class__ = lambda : _IIdentityPoolRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IIdentityPoolRoleAttachmentRef"
)
class IIdentityPoolRoleAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityPoolRoleAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="identityPoolRoleAttachmentRef")
    def identity_pool_role_attachment_ref(
        self,
    ) -> "IdentityPoolRoleAttachmentReference":
        '''(experimental) A reference to a IdentityPoolRoleAttachment resource.

        :stability: experimental
        '''
        ...


class _IIdentityPoolRoleAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityPoolRoleAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IIdentityPoolRoleAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="identityPoolRoleAttachmentRef")
    def identity_pool_role_attachment_ref(
        self,
    ) -> "IdentityPoolRoleAttachmentReference":
        '''(experimental) A reference to a IdentityPoolRoleAttachment resource.

        :stability: experimental
        '''
        return typing.cast("IdentityPoolRoleAttachmentReference", jsii.get(self, "identityPoolRoleAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentityPoolRoleAttachmentRef).__jsii_proxy_class__ = lambda : _IIdentityPoolRoleAttachmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.ILogDeliveryConfigurationRef"
)
class ILogDeliveryConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LogDeliveryConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="logDeliveryConfigurationRef")
    def log_delivery_configuration_ref(self) -> "LogDeliveryConfigurationReference":
        '''(experimental) A reference to a LogDeliveryConfiguration resource.

        :stability: experimental
        '''
        ...


class _ILogDeliveryConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LogDeliveryConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.ILogDeliveryConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="logDeliveryConfigurationRef")
    def log_delivery_configuration_ref(self) -> "LogDeliveryConfigurationReference":
        '''(experimental) A reference to a LogDeliveryConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("LogDeliveryConfigurationReference", jsii.get(self, "logDeliveryConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogDeliveryConfigurationRef).__jsii_proxy_class__ = lambda : _ILogDeliveryConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IManagedLoginBrandingRef"
)
class IManagedLoginBrandingRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ManagedLoginBranding.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="managedLoginBrandingRef")
    def managed_login_branding_ref(self) -> "ManagedLoginBrandingReference":
        '''(experimental) A reference to a ManagedLoginBranding resource.

        :stability: experimental
        '''
        ...


class _IManagedLoginBrandingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ManagedLoginBranding.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IManagedLoginBrandingRef"

    @builtins.property
    @jsii.member(jsii_name="managedLoginBrandingRef")
    def managed_login_branding_ref(self) -> "ManagedLoginBrandingReference":
        '''(experimental) A reference to a ManagedLoginBranding resource.

        :stability: experimental
        '''
        return typing.cast("ManagedLoginBrandingReference", jsii.get(self, "managedLoginBrandingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IManagedLoginBrandingRef).__jsii_proxy_class__ = lambda : _IManagedLoginBrandingRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cognito.ITermsRef")
class ITermsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Terms.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="termsRef")
    def terms_ref(self) -> "TermsReference":
        '''(experimental) A reference to a Terms resource.

        :stability: experimental
        '''
        ...


class _ITermsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Terms.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.ITermsRef"

    @builtins.property
    @jsii.member(jsii_name="termsRef")
    def terms_ref(self) -> "TermsReference":
        '''(experimental) A reference to a Terms resource.

        :stability: experimental
        '''
        return typing.cast("TermsReference", jsii.get(self, "termsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITermsRef).__jsii_proxy_class__ = lambda : _ITermsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cognito.IUserPoolClientRef")
class IUserPoolClientRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolClient.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPoolClientRef")
    def user_pool_client_ref(self) -> "UserPoolClientReference":
        '''(experimental) A reference to a UserPoolClient resource.

        :stability: experimental
        '''
        ...


class _IUserPoolClientRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolClient.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IUserPoolClientRef"

    @builtins.property
    @jsii.member(jsii_name="userPoolClientRef")
    def user_pool_client_ref(self) -> "UserPoolClientReference":
        '''(experimental) A reference to a UserPoolClient resource.

        :stability: experimental
        '''
        return typing.cast("UserPoolClientReference", jsii.get(self, "userPoolClientRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolClientRef).__jsii_proxy_class__ = lambda : _IUserPoolClientRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cognito.IUserPoolDomainRef")
class IUserPoolDomainRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolDomain.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPoolDomainRef")
    def user_pool_domain_ref(self) -> "UserPoolDomainReference":
        '''(experimental) A reference to a UserPoolDomain resource.

        :stability: experimental
        '''
        ...


class _IUserPoolDomainRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolDomain.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IUserPoolDomainRef"

    @builtins.property
    @jsii.member(jsii_name="userPoolDomainRef")
    def user_pool_domain_ref(self) -> "UserPoolDomainReference":
        '''(experimental) A reference to a UserPoolDomain resource.

        :stability: experimental
        '''
        return typing.cast("UserPoolDomainReference", jsii.get(self, "userPoolDomainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolDomainRef).__jsii_proxy_class__ = lambda : _IUserPoolDomainRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cognito.IUserPoolGroupRef")
class IUserPoolGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPoolGroupRef")
    def user_pool_group_ref(self) -> "UserPoolGroupReference":
        '''(experimental) A reference to a UserPoolGroup resource.

        :stability: experimental
        '''
        ...


class _IUserPoolGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IUserPoolGroupRef"

    @builtins.property
    @jsii.member(jsii_name="userPoolGroupRef")
    def user_pool_group_ref(self) -> "UserPoolGroupReference":
        '''(experimental) A reference to a UserPoolGroup resource.

        :stability: experimental
        '''
        return typing.cast("UserPoolGroupReference", jsii.get(self, "userPoolGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolGroupRef).__jsii_proxy_class__ = lambda : _IUserPoolGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IUserPoolIdentityProviderRef"
)
class IUserPoolIdentityProviderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolIdentityProvider.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPoolIdentityProviderRef")
    def user_pool_identity_provider_ref(self) -> "UserPoolIdentityProviderReference":
        '''(experimental) A reference to a UserPoolIdentityProvider resource.

        :stability: experimental
        '''
        ...


class _IUserPoolIdentityProviderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolIdentityProvider.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IUserPoolIdentityProviderRef"

    @builtins.property
    @jsii.member(jsii_name="userPoolIdentityProviderRef")
    def user_pool_identity_provider_ref(self) -> "UserPoolIdentityProviderReference":
        '''(experimental) A reference to a UserPoolIdentityProvider resource.

        :stability: experimental
        '''
        return typing.cast("UserPoolIdentityProviderReference", jsii.get(self, "userPoolIdentityProviderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolIdentityProviderRef).__jsii_proxy_class__ = lambda : _IUserPoolIdentityProviderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cognito.IUserPoolRef")
class IUserPoolRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPoolRef")
    def user_pool_ref(self) -> "UserPoolReference":
        '''(experimental) A reference to a UserPool resource.

        :stability: experimental
        '''
        ...


class _IUserPoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IUserPoolRef"

    @builtins.property
    @jsii.member(jsii_name="userPoolRef")
    def user_pool_ref(self) -> "UserPoolReference":
        '''(experimental) A reference to a UserPool resource.

        :stability: experimental
        '''
        return typing.cast("UserPoolReference", jsii.get(self, "userPoolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolRef).__jsii_proxy_class__ = lambda : _IUserPoolRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IUserPoolResourceServerRef"
)
class IUserPoolResourceServerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolResourceServer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPoolResourceServerRef")
    def user_pool_resource_server_ref(self) -> "UserPoolResourceServerReference":
        '''(experimental) A reference to a UserPoolResourceServer resource.

        :stability: experimental
        '''
        ...


class _IUserPoolResourceServerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolResourceServer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IUserPoolResourceServerRef"

    @builtins.property
    @jsii.member(jsii_name="userPoolResourceServerRef")
    def user_pool_resource_server_ref(self) -> "UserPoolResourceServerReference":
        '''(experimental) A reference to a UserPoolResourceServer resource.

        :stability: experimental
        '''
        return typing.cast("UserPoolResourceServerReference", jsii.get(self, "userPoolResourceServerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolResourceServerRef).__jsii_proxy_class__ = lambda : _IUserPoolResourceServerRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IUserPoolRiskConfigurationAttachmentRef"
)
class IUserPoolRiskConfigurationAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolRiskConfigurationAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPoolRiskConfigurationAttachmentRef")
    def user_pool_risk_configuration_attachment_ref(
        self,
    ) -> "UserPoolRiskConfigurationAttachmentReference":
        '''(experimental) A reference to a UserPoolRiskConfigurationAttachment resource.

        :stability: experimental
        '''
        ...


class _IUserPoolRiskConfigurationAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolRiskConfigurationAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IUserPoolRiskConfigurationAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="userPoolRiskConfigurationAttachmentRef")
    def user_pool_risk_configuration_attachment_ref(
        self,
    ) -> "UserPoolRiskConfigurationAttachmentReference":
        '''(experimental) A reference to a UserPoolRiskConfigurationAttachment resource.

        :stability: experimental
        '''
        return typing.cast("UserPoolRiskConfigurationAttachmentReference", jsii.get(self, "userPoolRiskConfigurationAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolRiskConfigurationAttachmentRef).__jsii_proxy_class__ = lambda : _IUserPoolRiskConfigurationAttachmentRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IUserPoolUICustomizationAttachmentRef"
)
class IUserPoolUICustomizationAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolUICustomizationAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPoolUiCustomizationAttachmentRef")
    def user_pool_ui_customization_attachment_ref(
        self,
    ) -> "UserPoolUICustomizationAttachmentReference":
        '''(experimental) A reference to a UserPoolUICustomizationAttachment resource.

        :stability: experimental
        '''
        ...


class _IUserPoolUICustomizationAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolUICustomizationAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IUserPoolUICustomizationAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="userPoolUiCustomizationAttachmentRef")
    def user_pool_ui_customization_attachment_ref(
        self,
    ) -> "UserPoolUICustomizationAttachmentReference":
        '''(experimental) A reference to a UserPoolUICustomizationAttachment resource.

        :stability: experimental
        '''
        return typing.cast("UserPoolUICustomizationAttachmentReference", jsii.get(self, "userPoolUiCustomizationAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolUICustomizationAttachmentRef).__jsii_proxy_class__ = lambda : _IUserPoolUICustomizationAttachmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cognito.IUserPoolUserRef")
class IUserPoolUserRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolUser.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPoolUserRef")
    def user_pool_user_ref(self) -> "UserPoolUserReference":
        '''(experimental) A reference to a UserPoolUser resource.

        :stability: experimental
        '''
        ...


class _IUserPoolUserRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolUser.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IUserPoolUserRef"

    @builtins.property
    @jsii.member(jsii_name="userPoolUserRef")
    def user_pool_user_ref(self) -> "UserPoolUserReference":
        '''(experimental) A reference to a UserPoolUser resource.

        :stability: experimental
        '''
        return typing.cast("UserPoolUserReference", jsii.get(self, "userPoolUserRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolUserRef).__jsii_proxy_class__ = lambda : _IUserPoolUserRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IUserPoolUserToGroupAttachmentRef"
)
class IUserPoolUserToGroupAttachmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolUserToGroupAttachment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPoolUserToGroupAttachmentRef")
    def user_pool_user_to_group_attachment_ref(
        self,
    ) -> "UserPoolUserToGroupAttachmentReference":
        '''(experimental) A reference to a UserPoolUserToGroupAttachment resource.

        :stability: experimental
        '''
        ...


class _IUserPoolUserToGroupAttachmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPoolUserToGroupAttachment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cognito.IUserPoolUserToGroupAttachmentRef"

    @builtins.property
    @jsii.member(jsii_name="userPoolUserToGroupAttachmentRef")
    def user_pool_user_to_group_attachment_ref(
        self,
    ) -> "UserPoolUserToGroupAttachmentReference":
        '''(experimental) A reference to a UserPoolUserToGroupAttachment resource.

        :stability: experimental
        '''
        return typing.cast("UserPoolUserToGroupAttachmentReference", jsii.get(self, "userPoolUserToGroupAttachmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPoolUserToGroupAttachmentRef).__jsii_proxy_class__ = lambda : _IUserPoolUserToGroupAttachmentRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IdentityPoolPrincipalTagReference",
    jsii_struct_bases=[],
    name_mapping={
        "identity_pool_id": "identityPoolId",
        "identity_provider_name": "identityProviderName",
    },
)
class IdentityPoolPrincipalTagReference:
    def __init__(
        self,
        *,
        identity_pool_id: builtins.str,
        identity_provider_name: builtins.str,
    ) -> None:
        '''A reference to a IdentityPoolPrincipalTag resource.

        :param identity_pool_id: The IdentityPoolId of the IdentityPoolPrincipalTag resource.
        :param identity_provider_name: The IdentityProviderName of the IdentityPoolPrincipalTag resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            identity_pool_principal_tag_reference = interfaces_cognito.IdentityPoolPrincipalTagReference(
                identity_pool_id="identityPoolId",
                identity_provider_name="identityProviderName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cc5a043298fe466acf5a276ca3b197ad62c5bcb18683941cbbaa8c09e911e32)
            check_type(argname="argument identity_pool_id", value=identity_pool_id, expected_type=type_hints["identity_pool_id"])
            check_type(argname="argument identity_provider_name", value=identity_provider_name, expected_type=type_hints["identity_provider_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_pool_id": identity_pool_id,
            "identity_provider_name": identity_provider_name,
        }

    @builtins.property
    def identity_pool_id(self) -> builtins.str:
        '''The IdentityPoolId of the IdentityPoolPrincipalTag resource.'''
        result = self._values.get("identity_pool_id")
        assert result is not None, "Required property 'identity_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_provider_name(self) -> builtins.str:
        '''The IdentityProviderName of the IdentityPoolPrincipalTag resource.'''
        result = self._values.get("identity_provider_name")
        assert result is not None, "Required property 'identity_provider_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolPrincipalTagReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IdentityPoolReference",
    jsii_struct_bases=[],
    name_mapping={"identity_pool_id": "identityPoolId"},
)
class IdentityPoolReference:
    def __init__(self, *, identity_pool_id: builtins.str) -> None:
        '''A reference to a IdentityPool resource.

        :param identity_pool_id: The Id of the IdentityPool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            identity_pool_reference = interfaces_cognito.IdentityPoolReference(
                identity_pool_id="identityPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3218cf924075cf055c20b0abfab4803c9f0051b2030ff12c6e597bc58427dfb7)
            check_type(argname="argument identity_pool_id", value=identity_pool_id, expected_type=type_hints["identity_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_pool_id": identity_pool_id,
        }

    @builtins.property
    def identity_pool_id(self) -> builtins.str:
        '''The Id of the IdentityPool resource.'''
        result = self._values.get("identity_pool_id")
        assert result is not None, "Required property 'identity_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.IdentityPoolRoleAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"identity_pool_role_attachment_id": "identityPoolRoleAttachmentId"},
)
class IdentityPoolRoleAttachmentReference:
    def __init__(self, *, identity_pool_role_attachment_id: builtins.str) -> None:
        '''A reference to a IdentityPoolRoleAttachment resource.

        :param identity_pool_role_attachment_id: The Id of the IdentityPoolRoleAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            identity_pool_role_attachment_reference = interfaces_cognito.IdentityPoolRoleAttachmentReference(
                identity_pool_role_attachment_id="identityPoolRoleAttachmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34190b77eaab913a78d5fd3a05321ad0a4a80ef5dad716132f2829a4f41b7e84)
            check_type(argname="argument identity_pool_role_attachment_id", value=identity_pool_role_attachment_id, expected_type=type_hints["identity_pool_role_attachment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_pool_role_attachment_id": identity_pool_role_attachment_id,
        }

    @builtins.property
    def identity_pool_role_attachment_id(self) -> builtins.str:
        '''The Id of the IdentityPoolRoleAttachment resource.'''
        result = self._values.get("identity_pool_role_attachment_id")
        assert result is not None, "Required property 'identity_pool_role_attachment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityPoolRoleAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.LogDeliveryConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"log_delivery_configuration_id": "logDeliveryConfigurationId"},
)
class LogDeliveryConfigurationReference:
    def __init__(self, *, log_delivery_configuration_id: builtins.str) -> None:
        '''A reference to a LogDeliveryConfiguration resource.

        :param log_delivery_configuration_id: The Id of the LogDeliveryConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            log_delivery_configuration_reference = interfaces_cognito.LogDeliveryConfigurationReference(
                log_delivery_configuration_id="logDeliveryConfigurationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f875a38af4eb1dc456934c1548d778b55e784e77c015e50066366dbd0c9fdf49)
            check_type(argname="argument log_delivery_configuration_id", value=log_delivery_configuration_id, expected_type=type_hints["log_delivery_configuration_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "log_delivery_configuration_id": log_delivery_configuration_id,
        }

    @builtins.property
    def log_delivery_configuration_id(self) -> builtins.str:
        '''The Id of the LogDeliveryConfiguration resource.'''
        result = self._values.get("log_delivery_configuration_id")
        assert result is not None, "Required property 'log_delivery_configuration_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogDeliveryConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.ManagedLoginBrandingReference",
    jsii_struct_bases=[],
    name_mapping={
        "managed_login_branding_id": "managedLoginBrandingId",
        "user_pool_id": "userPoolId",
    },
)
class ManagedLoginBrandingReference:
    def __init__(
        self,
        *,
        managed_login_branding_id: builtins.str,
        user_pool_id: builtins.str,
    ) -> None:
        '''A reference to a ManagedLoginBranding resource.

        :param managed_login_branding_id: The ManagedLoginBrandingId of the ManagedLoginBranding resource.
        :param user_pool_id: The UserPoolId of the ManagedLoginBranding resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            managed_login_branding_reference = interfaces_cognito.ManagedLoginBrandingReference(
                managed_login_branding_id="managedLoginBrandingId",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac1ad7162157086c02de85b312a0a8bf64727f6ae88085d5c5c83cc3e3a7cba6)
            check_type(argname="argument managed_login_branding_id", value=managed_login_branding_id, expected_type=type_hints["managed_login_branding_id"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "managed_login_branding_id": managed_login_branding_id,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def managed_login_branding_id(self) -> builtins.str:
        '''The ManagedLoginBrandingId of the ManagedLoginBranding resource.'''
        result = self._values.get("managed_login_branding_id")
        assert result is not None, "Required property 'managed_login_branding_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the ManagedLoginBranding resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedLoginBrandingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.TermsReference",
    jsii_struct_bases=[],
    name_mapping={"terms_id": "termsId", "user_pool_id": "userPoolId"},
)
class TermsReference:
    def __init__(self, *, terms_id: builtins.str, user_pool_id: builtins.str) -> None:
        '''A reference to a Terms resource.

        :param terms_id: The TermsId of the Terms resource.
        :param user_pool_id: The UserPoolId of the Terms resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            terms_reference = interfaces_cognito.TermsReference(
                terms_id="termsId",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6ddddddef6f9c7269efe22a766f1ea54ea3dc4aaa13214f7e0825ea9ad0b54c)
            check_type(argname="argument terms_id", value=terms_id, expected_type=type_hints["terms_id"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "terms_id": terms_id,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def terms_id(self) -> builtins.str:
        '''The TermsId of the Terms resource.'''
        result = self._values.get("terms_id")
        assert result is not None, "Required property 'terms_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the Terms resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TermsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.UserPoolClientReference",
    jsii_struct_bases=[],
    name_mapping={"client_id": "clientId", "user_pool_id": "userPoolId"},
)
class UserPoolClientReference:
    def __init__(self, *, client_id: builtins.str, user_pool_id: builtins.str) -> None:
        '''A reference to a UserPoolClient resource.

        :param client_id: The ClientId of the UserPoolClient resource.
        :param user_pool_id: The UserPoolId of the UserPoolClient resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            user_pool_client_reference = interfaces_cognito.UserPoolClientReference(
                client_id="clientId",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a613d0899cb76353a656d3984ed3afd3693b73b15de1734d391036c385914ab5)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ClientId of the UserPoolClient resource.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the UserPoolClient resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolClientReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.UserPoolDomainReference",
    jsii_struct_bases=[],
    name_mapping={"domain": "domain", "user_pool_id": "userPoolId"},
)
class UserPoolDomainReference:
    def __init__(self, *, domain: builtins.str, user_pool_id: builtins.str) -> None:
        '''A reference to a UserPoolDomain resource.

        :param domain: The Domain of the UserPoolDomain resource.
        :param user_pool_id: The UserPoolId of the UserPoolDomain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            user_pool_domain_reference = interfaces_cognito.UserPoolDomainReference(
                domain="domain",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e04d3660137d2f7a094f9306f113279cc5683cf64083351968c05af3ff23911f)
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain": domain,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def domain(self) -> builtins.str:
        '''The Domain of the UserPoolDomain resource.'''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the UserPoolDomain resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolDomainReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.UserPoolGroupReference",
    jsii_struct_bases=[],
    name_mapping={"group_name": "groupName", "user_pool_id": "userPoolId"},
)
class UserPoolGroupReference:
    def __init__(self, *, group_name: builtins.str, user_pool_id: builtins.str) -> None:
        '''A reference to a UserPoolGroup resource.

        :param group_name: The GroupName of the UserPoolGroup resource.
        :param user_pool_id: The UserPoolId of the UserPoolGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            user_pool_group_reference = interfaces_cognito.UserPoolGroupReference(
                group_name="groupName",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c6ca4225c5a7c5b388611fc0b563c1763787a7fa970bdd53d66d8be5649e2d1)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name": group_name,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The GroupName of the UserPoolGroup resource.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the UserPoolGroup resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.UserPoolIdentityProviderReference",
    jsii_struct_bases=[],
    name_mapping={"provider_name": "providerName", "user_pool_id": "userPoolId"},
)
class UserPoolIdentityProviderReference:
    def __init__(
        self,
        *,
        provider_name: builtins.str,
        user_pool_id: builtins.str,
    ) -> None:
        '''A reference to a UserPoolIdentityProvider resource.

        :param provider_name: The ProviderName of the UserPoolIdentityProvider resource.
        :param user_pool_id: The UserPoolId of the UserPoolIdentityProvider resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            user_pool_identity_provider_reference = interfaces_cognito.UserPoolIdentityProviderReference(
                provider_name="providerName",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e38e75f1e049595e40dc4aee48f5d7f28836252b51b4773600008ee5bfea87e)
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "provider_name": provider_name,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def provider_name(self) -> builtins.str:
        '''The ProviderName of the UserPoolIdentityProvider resource.'''
        result = self._values.get("provider_name")
        assert result is not None, "Required property 'provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the UserPoolIdentityProvider resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolIdentityProviderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.UserPoolReference",
    jsii_struct_bases=[],
    name_mapping={"user_pool_arn": "userPoolArn", "user_pool_id": "userPoolId"},
)
class UserPoolReference:
    def __init__(
        self,
        *,
        user_pool_arn: builtins.str,
        user_pool_id: builtins.str,
    ) -> None:
        '''A reference to a UserPool resource.

        :param user_pool_arn: The ARN of the UserPool resource.
        :param user_pool_id: The UserPoolId of the UserPool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            user_pool_reference = interfaces_cognito.UserPoolReference(
                user_pool_arn="userPoolArn",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb2f639967e545264e9cd8ee88d1759d350388a6ebe4c5e79dbdf64e91462521)
            check_type(argname="argument user_pool_arn", value=user_pool_arn, expected_type=type_hints["user_pool_arn"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_pool_arn": user_pool_arn,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def user_pool_arn(self) -> builtins.str:
        '''The ARN of the UserPool resource.'''
        result = self._values.get("user_pool_arn")
        assert result is not None, "Required property 'user_pool_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the UserPool resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.UserPoolResourceServerReference",
    jsii_struct_bases=[],
    name_mapping={"identifier": "identifier", "user_pool_id": "userPoolId"},
)
class UserPoolResourceServerReference:
    def __init__(self, *, identifier: builtins.str, user_pool_id: builtins.str) -> None:
        '''A reference to a UserPoolResourceServer resource.

        :param identifier: The Identifier of the UserPoolResourceServer resource.
        :param user_pool_id: The UserPoolId of the UserPoolResourceServer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            user_pool_resource_server_reference = interfaces_cognito.UserPoolResourceServerReference(
                identifier="identifier",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45d481ebf1e9de348fb61a77e52f94542b582a07364ac6ca57e3a32db6daf21b)
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identifier": identifier,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def identifier(self) -> builtins.str:
        '''The Identifier of the UserPoolResourceServer resource.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the UserPoolResourceServer resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolResourceServerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.UserPoolRiskConfigurationAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"client_id": "clientId", "user_pool_id": "userPoolId"},
)
class UserPoolRiskConfigurationAttachmentReference:
    def __init__(self, *, client_id: builtins.str, user_pool_id: builtins.str) -> None:
        '''A reference to a UserPoolRiskConfigurationAttachment resource.

        :param client_id: The ClientId of the UserPoolRiskConfigurationAttachment resource.
        :param user_pool_id: The UserPoolId of the UserPoolRiskConfigurationAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            user_pool_risk_configuration_attachment_reference = interfaces_cognito.UserPoolRiskConfigurationAttachmentReference(
                client_id="clientId",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e89abfe80fc6ed500e877a7f0b753fff7e2ea69d20ea8301b0f5c95cc443ac3e)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ClientId of the UserPoolRiskConfigurationAttachment resource.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the UserPoolRiskConfigurationAttachment resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolRiskConfigurationAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.UserPoolUICustomizationAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={"client_id": "clientId", "user_pool_id": "userPoolId"},
)
class UserPoolUICustomizationAttachmentReference:
    def __init__(self, *, client_id: builtins.str, user_pool_id: builtins.str) -> None:
        '''A reference to a UserPoolUICustomizationAttachment resource.

        :param client_id: The ClientId of the UserPoolUICustomizationAttachment resource.
        :param user_pool_id: The UserPoolId of the UserPoolUICustomizationAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            user_pool_uICustomization_attachment_reference = interfaces_cognito.UserPoolUICustomizationAttachmentReference(
                client_id="clientId",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a0dc8ff8cccc49fdaec27f43141b983d0bbe2d7580800e65676265f6e19fbb6)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "client_id": client_id,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The ClientId of the UserPoolUICustomizationAttachment resource.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the UserPoolUICustomizationAttachment resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolUICustomizationAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.UserPoolUserReference",
    jsii_struct_bases=[],
    name_mapping={"username": "username", "user_pool_id": "userPoolId"},
)
class UserPoolUserReference:
    def __init__(self, *, username: builtins.str, user_pool_id: builtins.str) -> None:
        '''A reference to a UserPoolUser resource.

        :param username: The Username of the UserPoolUser resource.
        :param user_pool_id: The UserPoolId of the UserPoolUser resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            user_pool_user_reference = interfaces_cognito.UserPoolUserReference(
                username="username",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de0ef1e81a5938dc2ae0b2761d944f9880191753b1175d2e69c1d604b5a3aa4e)
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "username": username,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def username(self) -> builtins.str:
        '''The Username of the UserPoolUser resource.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the UserPoolUser resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolUserReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cognito.UserPoolUserToGroupAttachmentReference",
    jsii_struct_bases=[],
    name_mapping={
        "group_name": "groupName",
        "username": "username",
        "user_pool_id": "userPoolId",
    },
)
class UserPoolUserToGroupAttachmentReference:
    def __init__(
        self,
        *,
        group_name: builtins.str,
        username: builtins.str,
        user_pool_id: builtins.str,
    ) -> None:
        '''A reference to a UserPoolUserToGroupAttachment resource.

        :param group_name: The GroupName of the UserPoolUserToGroupAttachment resource.
        :param username: The Username of the UserPoolUserToGroupAttachment resource.
        :param user_pool_id: The UserPoolId of the UserPoolUserToGroupAttachment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cognito as interfaces_cognito
            
            user_pool_user_to_group_attachment_reference = interfaces_cognito.UserPoolUserToGroupAttachmentReference(
                group_name="groupName",
                username="username",
                user_pool_id="userPoolId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de98a26267d52b4593101085779f879caf7df79b9360db02490d4836383cb000)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            check_type(argname="argument user_pool_id", value=user_pool_id, expected_type=type_hints["user_pool_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name": group_name,
            "username": username,
            "user_pool_id": user_pool_id,
        }

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The GroupName of the UserPoolUserToGroupAttachment resource.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''The Username of the UserPoolUserToGroupAttachment resource.'''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_pool_id(self) -> builtins.str:
        '''The UserPoolId of the UserPoolUserToGroupAttachment resource.'''
        result = self._values.get("user_pool_id")
        assert result is not None, "Required property 'user_pool_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPoolUserToGroupAttachmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IIdentityPoolPrincipalTagRef",
    "IIdentityPoolRef",
    "IIdentityPoolRoleAttachmentRef",
    "ILogDeliveryConfigurationRef",
    "IManagedLoginBrandingRef",
    "ITermsRef",
    "IUserPoolClientRef",
    "IUserPoolDomainRef",
    "IUserPoolGroupRef",
    "IUserPoolIdentityProviderRef",
    "IUserPoolRef",
    "IUserPoolResourceServerRef",
    "IUserPoolRiskConfigurationAttachmentRef",
    "IUserPoolUICustomizationAttachmentRef",
    "IUserPoolUserRef",
    "IUserPoolUserToGroupAttachmentRef",
    "IdentityPoolPrincipalTagReference",
    "IdentityPoolReference",
    "IdentityPoolRoleAttachmentReference",
    "LogDeliveryConfigurationReference",
    "ManagedLoginBrandingReference",
    "TermsReference",
    "UserPoolClientReference",
    "UserPoolDomainReference",
    "UserPoolGroupReference",
    "UserPoolIdentityProviderReference",
    "UserPoolReference",
    "UserPoolResourceServerReference",
    "UserPoolRiskConfigurationAttachmentReference",
    "UserPoolUICustomizationAttachmentReference",
    "UserPoolUserReference",
    "UserPoolUserToGroupAttachmentReference",
]

publication.publish()

def _typecheckingstub__6cc5a043298fe466acf5a276ca3b197ad62c5bcb18683941cbbaa8c09e911e32(
    *,
    identity_pool_id: builtins.str,
    identity_provider_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3218cf924075cf055c20b0abfab4803c9f0051b2030ff12c6e597bc58427dfb7(
    *,
    identity_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34190b77eaab913a78d5fd3a05321ad0a4a80ef5dad716132f2829a4f41b7e84(
    *,
    identity_pool_role_attachment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f875a38af4eb1dc456934c1548d778b55e784e77c015e50066366dbd0c9fdf49(
    *,
    log_delivery_configuration_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac1ad7162157086c02de85b312a0a8bf64727f6ae88085d5c5c83cc3e3a7cba6(
    *,
    managed_login_branding_id: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6ddddddef6f9c7269efe22a766f1ea54ea3dc4aaa13214f7e0825ea9ad0b54c(
    *,
    terms_id: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a613d0899cb76353a656d3984ed3afd3693b73b15de1734d391036c385914ab5(
    *,
    client_id: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e04d3660137d2f7a094f9306f113279cc5683cf64083351968c05af3ff23911f(
    *,
    domain: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c6ca4225c5a7c5b388611fc0b563c1763787a7fa970bdd53d66d8be5649e2d1(
    *,
    group_name: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e38e75f1e049595e40dc4aee48f5d7f28836252b51b4773600008ee5bfea87e(
    *,
    provider_name: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb2f639967e545264e9cd8ee88d1759d350388a6ebe4c5e79dbdf64e91462521(
    *,
    user_pool_arn: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45d481ebf1e9de348fb61a77e52f94542b582a07364ac6ca57e3a32db6daf21b(
    *,
    identifier: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e89abfe80fc6ed500e877a7f0b753fff7e2ea69d20ea8301b0f5c95cc443ac3e(
    *,
    client_id: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a0dc8ff8cccc49fdaec27f43141b983d0bbe2d7580800e65676265f6e19fbb6(
    *,
    client_id: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de0ef1e81a5938dc2ae0b2761d944f9880191753b1175d2e69c1d604b5a3aa4e(
    *,
    username: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de98a26267d52b4593101085779f879caf7df79b9360db02490d4836383cb000(
    *,
    group_name: builtins.str,
    username: builtins.str,
    user_pool_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IIdentityPoolPrincipalTagRef, IIdentityPoolRef, IIdentityPoolRoleAttachmentRef, ILogDeliveryConfigurationRef, IManagedLoginBrandingRef, ITermsRef, IUserPoolClientRef, IUserPoolDomainRef, IUserPoolGroupRef, IUserPoolIdentityProviderRef, IUserPoolRef, IUserPoolResourceServerRef, IUserPoolRiskConfigurationAttachmentRef, IUserPoolUICustomizationAttachmentRef, IUserPoolUserRef, IUserPoolUserToGroupAttachmentRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
