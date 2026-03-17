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
    jsii_type="aws-cdk-lib.interfaces.aws_ses.ConfigurationSetEventDestinationReference",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_event_destination_id": "configurationSetEventDestinationId",
    },
)
class ConfigurationSetEventDestinationReference:
    def __init__(self, *, configuration_set_event_destination_id: builtins.str) -> None:
        '''A reference to a ConfigurationSetEventDestination resource.

        :param configuration_set_event_destination_id: The Id of the ConfigurationSetEventDestination resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            configuration_set_event_destination_reference = interfaces_ses.ConfigurationSetEventDestinationReference(
                configuration_set_event_destination_id="configurationSetEventDestinationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__233e229dac98a6018ca0e6d41c128dd532e86367935bcb73cbcaf6d97404701f)
            check_type(argname="argument configuration_set_event_destination_id", value=configuration_set_event_destination_id, expected_type=type_hints["configuration_set_event_destination_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_set_event_destination_id": configuration_set_event_destination_id,
        }

    @builtins.property
    def configuration_set_event_destination_id(self) -> builtins.str:
        '''The Id of the ConfigurationSetEventDestination resource.'''
        result = self._values.get("configuration_set_event_destination_id")
        assert result is not None, "Required property 'configuration_set_event_destination_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationSetEventDestinationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.ConfigurationSetReference",
    jsii_struct_bases=[],
    name_mapping={"configuration_set_name": "configurationSetName"},
)
class ConfigurationSetReference:
    def __init__(self, *, configuration_set_name: builtins.str) -> None:
        '''A reference to a ConfigurationSet resource.

        :param configuration_set_name: The Name of the ConfigurationSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            configuration_set_reference = interfaces_ses.ConfigurationSetReference(
                configuration_set_name="configurationSetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b5ae328c9b7ac2d7bc907cf4efe09aa28d00f7f96b67d9ed14120c682a116c9)
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_set_name": configuration_set_name,
        }

    @builtins.property
    def configuration_set_name(self) -> builtins.str:
        '''The Name of the ConfigurationSet resource.'''
        result = self._values.get("configuration_set_name")
        assert result is not None, "Required property 'configuration_set_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.ContactListReference",
    jsii_struct_bases=[],
    name_mapping={"contact_list_name": "contactListName"},
)
class ContactListReference:
    def __init__(self, *, contact_list_name: builtins.str) -> None:
        '''A reference to a ContactList resource.

        :param contact_list_name: The ContactListName of the ContactList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            contact_list_reference = interfaces_ses.ContactListReference(
                contact_list_name="contactListName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf2861ff3744b9c917ef3e590b8a64df3604ae487bb1f4e654554a0d15dd6703)
            check_type(argname="argument contact_list_name", value=contact_list_name, expected_type=type_hints["contact_list_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_list_name": contact_list_name,
        }

    @builtins.property
    def contact_list_name(self) -> builtins.str:
        '''The ContactListName of the ContactList resource.'''
        result = self._values.get("contact_list_name")
        assert result is not None, "Required property 'contact_list_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContactListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.CustomVerificationEmailTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"template_name": "templateName"},
)
class CustomVerificationEmailTemplateReference:
    def __init__(self, *, template_name: builtins.str) -> None:
        '''A reference to a CustomVerificationEmailTemplate resource.

        :param template_name: The TemplateName of the CustomVerificationEmailTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            custom_verification_email_template_reference = interfaces_ses.CustomVerificationEmailTemplateReference(
                template_name="templateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eee22c43f539103bf5c9a3012ec0e02b3d53fefdbe06140992d58a1c5943859b)
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_name": template_name,
        }

    @builtins.property
    def template_name(self) -> builtins.str:
        '''The TemplateName of the CustomVerificationEmailTemplate resource.'''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomVerificationEmailTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.DedicatedIpPoolReference",
    jsii_struct_bases=[],
    name_mapping={"pool_name": "poolName"},
)
class DedicatedIpPoolReference:
    def __init__(self, *, pool_name: builtins.str) -> None:
        '''A reference to a DedicatedIpPool resource.

        :param pool_name: The PoolName of the DedicatedIpPool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            dedicated_ip_pool_reference = interfaces_ses.DedicatedIpPoolReference(
                pool_name="poolName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b96dd5318bf107e0627b56848ee58eb242f0abb737a14fd282245dda453b702)
            check_type(argname="argument pool_name", value=pool_name, expected_type=type_hints["pool_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "pool_name": pool_name,
        }

    @builtins.property
    def pool_name(self) -> builtins.str:
        '''The PoolName of the DedicatedIpPool resource.'''
        result = self._values.get("pool_name")
        assert result is not None, "Required property 'pool_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DedicatedIpPoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.EmailIdentityReference",
    jsii_struct_bases=[],
    name_mapping={"email_identity": "emailIdentity"},
)
class EmailIdentityReference:
    def __init__(self, *, email_identity: builtins.str) -> None:
        '''A reference to a EmailIdentity resource.

        :param email_identity: The EmailIdentity of the EmailIdentity resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            email_identity_reference = interfaces_ses.EmailIdentityReference(
                email_identity="emailIdentity"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78d4b405750ad37e2ceb18cc71d146af078abd3d3df476b2b7acf90c5f293cba)
            check_type(argname="argument email_identity", value=email_identity, expected_type=type_hints["email_identity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email_identity": email_identity,
        }

    @builtins.property
    def email_identity(self) -> builtins.str:
        '''The EmailIdentity of the EmailIdentity resource.'''
        result = self._values.get("email_identity")
        assert result is not None, "Required property 'email_identity' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmailIdentityReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.IConfigurationSetEventDestinationRef"
)
class IConfigurationSetEventDestinationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationSetEventDestination.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationSetEventDestinationRef")
    def configuration_set_event_destination_ref(
        self,
    ) -> "ConfigurationSetEventDestinationReference":
        '''(experimental) A reference to a ConfigurationSetEventDestination resource.

        :stability: experimental
        '''
        ...


class _IConfigurationSetEventDestinationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationSetEventDestination.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IConfigurationSetEventDestinationRef"

    @builtins.property
    @jsii.member(jsii_name="configurationSetEventDestinationRef")
    def configuration_set_event_destination_ref(
        self,
    ) -> "ConfigurationSetEventDestinationReference":
        '''(experimental) A reference to a ConfigurationSetEventDestination resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationSetEventDestinationReference", jsii.get(self, "configurationSetEventDestinationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationSetEventDestinationRef).__jsii_proxy_class__ = lambda : _IConfigurationSetEventDestinationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IConfigurationSetRef")
class IConfigurationSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationSetRef")
    def configuration_set_ref(self) -> "ConfigurationSetReference":
        '''(experimental) A reference to a ConfigurationSet resource.

        :stability: experimental
        '''
        ...


class _IConfigurationSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IConfigurationSetRef"

    @builtins.property
    @jsii.member(jsii_name="configurationSetRef")
    def configuration_set_ref(self) -> "ConfigurationSetReference":
        '''(experimental) A reference to a ConfigurationSet resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationSetReference", jsii.get(self, "configurationSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationSetRef).__jsii_proxy_class__ = lambda : _IConfigurationSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IContactListRef")
class IContactListRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContactList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="contactListRef")
    def contact_list_ref(self) -> "ContactListReference":
        '''(experimental) A reference to a ContactList resource.

        :stability: experimental
        '''
        ...


class _IContactListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContactList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IContactListRef"

    @builtins.property
    @jsii.member(jsii_name="contactListRef")
    def contact_list_ref(self) -> "ContactListReference":
        '''(experimental) A reference to a ContactList resource.

        :stability: experimental
        '''
        return typing.cast("ContactListReference", jsii.get(self, "contactListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContactListRef).__jsii_proxy_class__ = lambda : _IContactListRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.ICustomVerificationEmailTemplateRef"
)
class ICustomVerificationEmailTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomVerificationEmailTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customVerificationEmailTemplateRef")
    def custom_verification_email_template_ref(
        self,
    ) -> "CustomVerificationEmailTemplateReference":
        '''(experimental) A reference to a CustomVerificationEmailTemplate resource.

        :stability: experimental
        '''
        ...


class _ICustomVerificationEmailTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomVerificationEmailTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.ICustomVerificationEmailTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="customVerificationEmailTemplateRef")
    def custom_verification_email_template_ref(
        self,
    ) -> "CustomVerificationEmailTemplateReference":
        '''(experimental) A reference to a CustomVerificationEmailTemplate resource.

        :stability: experimental
        '''
        return typing.cast("CustomVerificationEmailTemplateReference", jsii.get(self, "customVerificationEmailTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomVerificationEmailTemplateRef).__jsii_proxy_class__ = lambda : _ICustomVerificationEmailTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IDedicatedIpPoolRef")
class IDedicatedIpPoolRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DedicatedIpPool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dedicatedIpPoolRef")
    def dedicated_ip_pool_ref(self) -> "DedicatedIpPoolReference":
        '''(experimental) A reference to a DedicatedIpPool resource.

        :stability: experimental
        '''
        ...


class _IDedicatedIpPoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DedicatedIpPool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IDedicatedIpPoolRef"

    @builtins.property
    @jsii.member(jsii_name="dedicatedIpPoolRef")
    def dedicated_ip_pool_ref(self) -> "DedicatedIpPoolReference":
        '''(experimental) A reference to a DedicatedIpPool resource.

        :stability: experimental
        '''
        return typing.cast("DedicatedIpPoolReference", jsii.get(self, "dedicatedIpPoolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDedicatedIpPoolRef).__jsii_proxy_class__ = lambda : _IDedicatedIpPoolRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IEmailIdentityRef")
class IEmailIdentityRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EmailIdentity.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="emailIdentityRef")
    def email_identity_ref(self) -> "EmailIdentityReference":
        '''(experimental) A reference to a EmailIdentity resource.

        :stability: experimental
        '''
        ...


class _IEmailIdentityRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EmailIdentity.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IEmailIdentityRef"

    @builtins.property
    @jsii.member(jsii_name="emailIdentityRef")
    def email_identity_ref(self) -> "EmailIdentityReference":
        '''(experimental) A reference to a EmailIdentity resource.

        :stability: experimental
        '''
        return typing.cast("EmailIdentityReference", jsii.get(self, "emailIdentityRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEmailIdentityRef).__jsii_proxy_class__ = lambda : _IEmailIdentityRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.IMailManagerAddonInstanceRef"
)
class IMailManagerAddonInstanceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerAddonInstance.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mailManagerAddonInstanceRef")
    def mail_manager_addon_instance_ref(self) -> "MailManagerAddonInstanceReference":
        '''(experimental) A reference to a MailManagerAddonInstance resource.

        :stability: experimental
        '''
        ...


class _IMailManagerAddonInstanceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerAddonInstance.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IMailManagerAddonInstanceRef"

    @builtins.property
    @jsii.member(jsii_name="mailManagerAddonInstanceRef")
    def mail_manager_addon_instance_ref(self) -> "MailManagerAddonInstanceReference":
        '''(experimental) A reference to a MailManagerAddonInstance resource.

        :stability: experimental
        '''
        return typing.cast("MailManagerAddonInstanceReference", jsii.get(self, "mailManagerAddonInstanceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMailManagerAddonInstanceRef).__jsii_proxy_class__ = lambda : _IMailManagerAddonInstanceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.IMailManagerAddonSubscriptionRef"
)
class IMailManagerAddonSubscriptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerAddonSubscription.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mailManagerAddonSubscriptionRef")
    def mail_manager_addon_subscription_ref(
        self,
    ) -> "MailManagerAddonSubscriptionReference":
        '''(experimental) A reference to a MailManagerAddonSubscription resource.

        :stability: experimental
        '''
        ...


class _IMailManagerAddonSubscriptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerAddonSubscription.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IMailManagerAddonSubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="mailManagerAddonSubscriptionRef")
    def mail_manager_addon_subscription_ref(
        self,
    ) -> "MailManagerAddonSubscriptionReference":
        '''(experimental) A reference to a MailManagerAddonSubscription resource.

        :stability: experimental
        '''
        return typing.cast("MailManagerAddonSubscriptionReference", jsii.get(self, "mailManagerAddonSubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMailManagerAddonSubscriptionRef).__jsii_proxy_class__ = lambda : _IMailManagerAddonSubscriptionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IMailManagerAddressListRef")
class IMailManagerAddressListRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerAddressList.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mailManagerAddressListRef")
    def mail_manager_address_list_ref(self) -> "MailManagerAddressListReference":
        '''(experimental) A reference to a MailManagerAddressList resource.

        :stability: experimental
        '''
        ...


class _IMailManagerAddressListRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerAddressList.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IMailManagerAddressListRef"

    @builtins.property
    @jsii.member(jsii_name="mailManagerAddressListRef")
    def mail_manager_address_list_ref(self) -> "MailManagerAddressListReference":
        '''(experimental) A reference to a MailManagerAddressList resource.

        :stability: experimental
        '''
        return typing.cast("MailManagerAddressListReference", jsii.get(self, "mailManagerAddressListRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMailManagerAddressListRef).__jsii_proxy_class__ = lambda : _IMailManagerAddressListRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IMailManagerArchiveRef")
class IMailManagerArchiveRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerArchive.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mailManagerArchiveRef")
    def mail_manager_archive_ref(self) -> "MailManagerArchiveReference":
        '''(experimental) A reference to a MailManagerArchive resource.

        :stability: experimental
        '''
        ...


class _IMailManagerArchiveRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerArchive.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IMailManagerArchiveRef"

    @builtins.property
    @jsii.member(jsii_name="mailManagerArchiveRef")
    def mail_manager_archive_ref(self) -> "MailManagerArchiveReference":
        '''(experimental) A reference to a MailManagerArchive resource.

        :stability: experimental
        '''
        return typing.cast("MailManagerArchiveReference", jsii.get(self, "mailManagerArchiveRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMailManagerArchiveRef).__jsii_proxy_class__ = lambda : _IMailManagerArchiveRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IMailManagerIngressPointRef")
class IMailManagerIngressPointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerIngressPoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mailManagerIngressPointRef")
    def mail_manager_ingress_point_ref(self) -> "MailManagerIngressPointReference":
        '''(experimental) A reference to a MailManagerIngressPoint resource.

        :stability: experimental
        '''
        ...


class _IMailManagerIngressPointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerIngressPoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IMailManagerIngressPointRef"

    @builtins.property
    @jsii.member(jsii_name="mailManagerIngressPointRef")
    def mail_manager_ingress_point_ref(self) -> "MailManagerIngressPointReference":
        '''(experimental) A reference to a MailManagerIngressPoint resource.

        :stability: experimental
        '''
        return typing.cast("MailManagerIngressPointReference", jsii.get(self, "mailManagerIngressPointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMailManagerIngressPointRef).__jsii_proxy_class__ = lambda : _IMailManagerIngressPointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IMailManagerRelayRef")
class IMailManagerRelayRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerRelay.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mailManagerRelayRef")
    def mail_manager_relay_ref(self) -> "MailManagerRelayReference":
        '''(experimental) A reference to a MailManagerRelay resource.

        :stability: experimental
        '''
        ...


class _IMailManagerRelayRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerRelay.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IMailManagerRelayRef"

    @builtins.property
    @jsii.member(jsii_name="mailManagerRelayRef")
    def mail_manager_relay_ref(self) -> "MailManagerRelayReference":
        '''(experimental) A reference to a MailManagerRelay resource.

        :stability: experimental
        '''
        return typing.cast("MailManagerRelayReference", jsii.get(self, "mailManagerRelayRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMailManagerRelayRef).__jsii_proxy_class__ = lambda : _IMailManagerRelayRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IMailManagerRuleSetRef")
class IMailManagerRuleSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerRuleSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mailManagerRuleSetRef")
    def mail_manager_rule_set_ref(self) -> "MailManagerRuleSetReference":
        '''(experimental) A reference to a MailManagerRuleSet resource.

        :stability: experimental
        '''
        ...


class _IMailManagerRuleSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerRuleSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IMailManagerRuleSetRef"

    @builtins.property
    @jsii.member(jsii_name="mailManagerRuleSetRef")
    def mail_manager_rule_set_ref(self) -> "MailManagerRuleSetReference":
        '''(experimental) A reference to a MailManagerRuleSet resource.

        :stability: experimental
        '''
        return typing.cast("MailManagerRuleSetReference", jsii.get(self, "mailManagerRuleSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMailManagerRuleSetRef).__jsii_proxy_class__ = lambda : _IMailManagerRuleSetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.IMailManagerTrafficPolicyRef"
)
class IMailManagerTrafficPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerTrafficPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mailManagerTrafficPolicyRef")
    def mail_manager_traffic_policy_ref(self) -> "MailManagerTrafficPolicyReference":
        '''(experimental) A reference to a MailManagerTrafficPolicy resource.

        :stability: experimental
        '''
        ...


class _IMailManagerTrafficPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MailManagerTrafficPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IMailManagerTrafficPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="mailManagerTrafficPolicyRef")
    def mail_manager_traffic_policy_ref(self) -> "MailManagerTrafficPolicyReference":
        '''(experimental) A reference to a MailManagerTrafficPolicy resource.

        :stability: experimental
        '''
        return typing.cast("MailManagerTrafficPolicyReference", jsii.get(self, "mailManagerTrafficPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMailManagerTrafficPolicyRef).__jsii_proxy_class__ = lambda : _IMailManagerTrafficPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IMultiRegionEndpointRef")
class IMultiRegionEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MultiRegionEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="multiRegionEndpointRef")
    def multi_region_endpoint_ref(self) -> "MultiRegionEndpointReference":
        '''(experimental) A reference to a MultiRegionEndpoint resource.

        :stability: experimental
        '''
        ...


class _IMultiRegionEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MultiRegionEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IMultiRegionEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="multiRegionEndpointRef")
    def multi_region_endpoint_ref(self) -> "MultiRegionEndpointReference":
        '''(experimental) A reference to a MultiRegionEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("MultiRegionEndpointReference", jsii.get(self, "multiRegionEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMultiRegionEndpointRef).__jsii_proxy_class__ = lambda : _IMultiRegionEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IReceiptFilterRef")
class IReceiptFilterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReceiptFilter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="receiptFilterRef")
    def receipt_filter_ref(self) -> "ReceiptFilterReference":
        '''(experimental) A reference to a ReceiptFilter resource.

        :stability: experimental
        '''
        ...


class _IReceiptFilterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReceiptFilter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IReceiptFilterRef"

    @builtins.property
    @jsii.member(jsii_name="receiptFilterRef")
    def receipt_filter_ref(self) -> "ReceiptFilterReference":
        '''(experimental) A reference to a ReceiptFilter resource.

        :stability: experimental
        '''
        return typing.cast("ReceiptFilterReference", jsii.get(self, "receiptFilterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptFilterRef).__jsii_proxy_class__ = lambda : _IReceiptFilterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IReceiptRuleRef")
class IReceiptRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReceiptRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="receiptRuleRef")
    def receipt_rule_ref(self) -> "ReceiptRuleReference":
        '''(experimental) A reference to a ReceiptRule resource.

        :stability: experimental
        '''
        ...


class _IReceiptRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReceiptRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IReceiptRuleRef"

    @builtins.property
    @jsii.member(jsii_name="receiptRuleRef")
    def receipt_rule_ref(self) -> "ReceiptRuleReference":
        '''(experimental) A reference to a ReceiptRule resource.

        :stability: experimental
        '''
        return typing.cast("ReceiptRuleReference", jsii.get(self, "receiptRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRuleRef).__jsii_proxy_class__ = lambda : _IReceiptRuleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IReceiptRuleSetRef")
class IReceiptRuleSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReceiptRuleSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="receiptRuleSetRef")
    def receipt_rule_set_ref(self) -> "ReceiptRuleSetReference":
        '''(experimental) A reference to a ReceiptRuleSet resource.

        :stability: experimental
        '''
        ...


class _IReceiptRuleSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReceiptRuleSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IReceiptRuleSetRef"

    @builtins.property
    @jsii.member(jsii_name="receiptRuleSetRef")
    def receipt_rule_set_ref(self) -> "ReceiptRuleSetReference":
        '''(experimental) A reference to a ReceiptRuleSet resource.

        :stability: experimental
        '''
        return typing.cast("ReceiptRuleSetReference", jsii.get(self, "receiptRuleSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRuleSetRef).__jsii_proxy_class__ = lambda : _IReceiptRuleSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.ITemplateRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.ITemplateRef"

    @builtins.property
    @jsii.member(jsii_name="templateRef")
    def template_ref(self) -> "TemplateReference":
        '''(experimental) A reference to a Template resource.

        :stability: experimental
        '''
        return typing.cast("TemplateReference", jsii.get(self, "templateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITemplateRef).__jsii_proxy_class__ = lambda : _ITemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.ITenantRef")
class ITenantRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Tenant.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tenantRef")
    def tenant_ref(self) -> "TenantReference":
        '''(experimental) A reference to a Tenant resource.

        :stability: experimental
        '''
        ...


class _ITenantRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Tenant.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.ITenantRef"

    @builtins.property
    @jsii.member(jsii_name="tenantRef")
    def tenant_ref(self) -> "TenantReference":
        '''(experimental) A reference to a Tenant resource.

        :stability: experimental
        '''
        return typing.cast("TenantReference", jsii.get(self, "tenantRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITenantRef).__jsii_proxy_class__ = lambda : _ITenantRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ses.IVdmAttributesRef")
class IVdmAttributesRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VdmAttributes.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vdmAttributesRef")
    def vdm_attributes_ref(self) -> "VdmAttributesReference":
        '''(experimental) A reference to a VdmAttributes resource.

        :stability: experimental
        '''
        ...


class _IVdmAttributesRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VdmAttributes.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ses.IVdmAttributesRef"

    @builtins.property
    @jsii.member(jsii_name="vdmAttributesRef")
    def vdm_attributes_ref(self) -> "VdmAttributesReference":
        '''(experimental) A reference to a VdmAttributes resource.

        :stability: experimental
        '''
        return typing.cast("VdmAttributesReference", jsii.get(self, "vdmAttributesRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVdmAttributesRef).__jsii_proxy_class__ = lambda : _IVdmAttributesRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.MailManagerAddonInstanceReference",
    jsii_struct_bases=[],
    name_mapping={
        "addon_instance_arn": "addonInstanceArn",
        "addon_instance_id": "addonInstanceId",
    },
)
class MailManagerAddonInstanceReference:
    def __init__(
        self,
        *,
        addon_instance_arn: builtins.str,
        addon_instance_id: builtins.str,
    ) -> None:
        '''A reference to a MailManagerAddonInstance resource.

        :param addon_instance_arn: The ARN of the MailManagerAddonInstance resource.
        :param addon_instance_id: The AddonInstanceId of the MailManagerAddonInstance resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            mail_manager_addon_instance_reference = interfaces_ses.MailManagerAddonInstanceReference(
                addon_instance_arn="addonInstanceArn",
                addon_instance_id="addonInstanceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8992f803f7505e5c4e7f7ccc64a127ca7b7063494b30e9339e4be159c0cfad2)
            check_type(argname="argument addon_instance_arn", value=addon_instance_arn, expected_type=type_hints["addon_instance_arn"])
            check_type(argname="argument addon_instance_id", value=addon_instance_id, expected_type=type_hints["addon_instance_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "addon_instance_arn": addon_instance_arn,
            "addon_instance_id": addon_instance_id,
        }

    @builtins.property
    def addon_instance_arn(self) -> builtins.str:
        '''The ARN of the MailManagerAddonInstance resource.'''
        result = self._values.get("addon_instance_arn")
        assert result is not None, "Required property 'addon_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def addon_instance_id(self) -> builtins.str:
        '''The AddonInstanceId of the MailManagerAddonInstance resource.'''
        result = self._values.get("addon_instance_id")
        assert result is not None, "Required property 'addon_instance_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MailManagerAddonInstanceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.MailManagerAddonSubscriptionReference",
    jsii_struct_bases=[],
    name_mapping={
        "addon_subscription_arn": "addonSubscriptionArn",
        "addon_subscription_id": "addonSubscriptionId",
    },
)
class MailManagerAddonSubscriptionReference:
    def __init__(
        self,
        *,
        addon_subscription_arn: builtins.str,
        addon_subscription_id: builtins.str,
    ) -> None:
        '''A reference to a MailManagerAddonSubscription resource.

        :param addon_subscription_arn: The ARN of the MailManagerAddonSubscription resource.
        :param addon_subscription_id: The AddonSubscriptionId of the MailManagerAddonSubscription resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            mail_manager_addon_subscription_reference = interfaces_ses.MailManagerAddonSubscriptionReference(
                addon_subscription_arn="addonSubscriptionArn",
                addon_subscription_id="addonSubscriptionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06c8f0b71be4b35dd631e5b326b64de20a8a9419c00ee747d47feb81e8e24d10)
            check_type(argname="argument addon_subscription_arn", value=addon_subscription_arn, expected_type=type_hints["addon_subscription_arn"])
            check_type(argname="argument addon_subscription_id", value=addon_subscription_id, expected_type=type_hints["addon_subscription_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "addon_subscription_arn": addon_subscription_arn,
            "addon_subscription_id": addon_subscription_id,
        }

    @builtins.property
    def addon_subscription_arn(self) -> builtins.str:
        '''The ARN of the MailManagerAddonSubscription resource.'''
        result = self._values.get("addon_subscription_arn")
        assert result is not None, "Required property 'addon_subscription_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def addon_subscription_id(self) -> builtins.str:
        '''The AddonSubscriptionId of the MailManagerAddonSubscription resource.'''
        result = self._values.get("addon_subscription_id")
        assert result is not None, "Required property 'addon_subscription_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MailManagerAddonSubscriptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.MailManagerAddressListReference",
    jsii_struct_bases=[],
    name_mapping={
        "address_list_arn": "addressListArn",
        "address_list_id": "addressListId",
    },
)
class MailManagerAddressListReference:
    def __init__(
        self,
        *,
        address_list_arn: builtins.str,
        address_list_id: builtins.str,
    ) -> None:
        '''A reference to a MailManagerAddressList resource.

        :param address_list_arn: The ARN of the MailManagerAddressList resource.
        :param address_list_id: The AddressListId of the MailManagerAddressList resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            mail_manager_address_list_reference = interfaces_ses.MailManagerAddressListReference(
                address_list_arn="addressListArn",
                address_list_id="addressListId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c2b0da17cb6c3256946c402db92a74c797c3f05e0d39993ce9b3fa320c136fe)
            check_type(argname="argument address_list_arn", value=address_list_arn, expected_type=type_hints["address_list_arn"])
            check_type(argname="argument address_list_id", value=address_list_id, expected_type=type_hints["address_list_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "address_list_arn": address_list_arn,
            "address_list_id": address_list_id,
        }

    @builtins.property
    def address_list_arn(self) -> builtins.str:
        '''The ARN of the MailManagerAddressList resource.'''
        result = self._values.get("address_list_arn")
        assert result is not None, "Required property 'address_list_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def address_list_id(self) -> builtins.str:
        '''The AddressListId of the MailManagerAddressList resource.'''
        result = self._values.get("address_list_id")
        assert result is not None, "Required property 'address_list_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MailManagerAddressListReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.MailManagerArchiveReference",
    jsii_struct_bases=[],
    name_mapping={"archive_arn": "archiveArn", "archive_id": "archiveId"},
)
class MailManagerArchiveReference:
    def __init__(self, *, archive_arn: builtins.str, archive_id: builtins.str) -> None:
        '''A reference to a MailManagerArchive resource.

        :param archive_arn: The ARN of the MailManagerArchive resource.
        :param archive_id: The ArchiveId of the MailManagerArchive resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            mail_manager_archive_reference = interfaces_ses.MailManagerArchiveReference(
                archive_arn="archiveArn",
                archive_id="archiveId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d873d90f01d0f3d0d63356e5f39ba9bc18cfdf68b988be224e350d3631357471)
            check_type(argname="argument archive_arn", value=archive_arn, expected_type=type_hints["archive_arn"])
            check_type(argname="argument archive_id", value=archive_id, expected_type=type_hints["archive_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "archive_arn": archive_arn,
            "archive_id": archive_id,
        }

    @builtins.property
    def archive_arn(self) -> builtins.str:
        '''The ARN of the MailManagerArchive resource.'''
        result = self._values.get("archive_arn")
        assert result is not None, "Required property 'archive_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def archive_id(self) -> builtins.str:
        '''The ArchiveId of the MailManagerArchive resource.'''
        result = self._values.get("archive_id")
        assert result is not None, "Required property 'archive_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MailManagerArchiveReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.MailManagerIngressPointReference",
    jsii_struct_bases=[],
    name_mapping={
        "ingress_point_arn": "ingressPointArn",
        "ingress_point_id": "ingressPointId",
    },
)
class MailManagerIngressPointReference:
    def __init__(
        self,
        *,
        ingress_point_arn: builtins.str,
        ingress_point_id: builtins.str,
    ) -> None:
        '''A reference to a MailManagerIngressPoint resource.

        :param ingress_point_arn: The ARN of the MailManagerIngressPoint resource.
        :param ingress_point_id: The IngressPointId of the MailManagerIngressPoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            mail_manager_ingress_point_reference = interfaces_ses.MailManagerIngressPointReference(
                ingress_point_arn="ingressPointArn",
                ingress_point_id="ingressPointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8145e93ee23430220a5eda157c3db564cad6b152e32d494bde06e8d772a86c20)
            check_type(argname="argument ingress_point_arn", value=ingress_point_arn, expected_type=type_hints["ingress_point_arn"])
            check_type(argname="argument ingress_point_id", value=ingress_point_id, expected_type=type_hints["ingress_point_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ingress_point_arn": ingress_point_arn,
            "ingress_point_id": ingress_point_id,
        }

    @builtins.property
    def ingress_point_arn(self) -> builtins.str:
        '''The ARN of the MailManagerIngressPoint resource.'''
        result = self._values.get("ingress_point_arn")
        assert result is not None, "Required property 'ingress_point_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ingress_point_id(self) -> builtins.str:
        '''The IngressPointId of the MailManagerIngressPoint resource.'''
        result = self._values.get("ingress_point_id")
        assert result is not None, "Required property 'ingress_point_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MailManagerIngressPointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.MailManagerRelayReference",
    jsii_struct_bases=[],
    name_mapping={"relay_arn": "relayArn", "relay_id": "relayId"},
)
class MailManagerRelayReference:
    def __init__(self, *, relay_arn: builtins.str, relay_id: builtins.str) -> None:
        '''A reference to a MailManagerRelay resource.

        :param relay_arn: The ARN of the MailManagerRelay resource.
        :param relay_id: The RelayId of the MailManagerRelay resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            mail_manager_relay_reference = interfaces_ses.MailManagerRelayReference(
                relay_arn="relayArn",
                relay_id="relayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0562a03f6b72be06c19d5688e1c48764e8ded3478b41a82adc774cf5a0fbed07)
            check_type(argname="argument relay_arn", value=relay_arn, expected_type=type_hints["relay_arn"])
            check_type(argname="argument relay_id", value=relay_id, expected_type=type_hints["relay_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "relay_arn": relay_arn,
            "relay_id": relay_id,
        }

    @builtins.property
    def relay_arn(self) -> builtins.str:
        '''The ARN of the MailManagerRelay resource.'''
        result = self._values.get("relay_arn")
        assert result is not None, "Required property 'relay_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relay_id(self) -> builtins.str:
        '''The RelayId of the MailManagerRelay resource.'''
        result = self._values.get("relay_id")
        assert result is not None, "Required property 'relay_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MailManagerRelayReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.MailManagerRuleSetReference",
    jsii_struct_bases=[],
    name_mapping={"rule_set_arn": "ruleSetArn", "rule_set_id": "ruleSetId"},
)
class MailManagerRuleSetReference:
    def __init__(
        self,
        *,
        rule_set_arn: builtins.str,
        rule_set_id: builtins.str,
    ) -> None:
        '''A reference to a MailManagerRuleSet resource.

        :param rule_set_arn: The ARN of the MailManagerRuleSet resource.
        :param rule_set_id: The RuleSetId of the MailManagerRuleSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            mail_manager_rule_set_reference = interfaces_ses.MailManagerRuleSetReference(
                rule_set_arn="ruleSetArn",
                rule_set_id="ruleSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd5bafd074000bd08230593448d667674cbf8e9ec48c59888040334cc4a4b23)
            check_type(argname="argument rule_set_arn", value=rule_set_arn, expected_type=type_hints["rule_set_arn"])
            check_type(argname="argument rule_set_id", value=rule_set_id, expected_type=type_hints["rule_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_set_arn": rule_set_arn,
            "rule_set_id": rule_set_id,
        }

    @builtins.property
    def rule_set_arn(self) -> builtins.str:
        '''The ARN of the MailManagerRuleSet resource.'''
        result = self._values.get("rule_set_arn")
        assert result is not None, "Required property 'rule_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_set_id(self) -> builtins.str:
        '''The RuleSetId of the MailManagerRuleSet resource.'''
        result = self._values.get("rule_set_id")
        assert result is not None, "Required property 'rule_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MailManagerRuleSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.MailManagerTrafficPolicyReference",
    jsii_struct_bases=[],
    name_mapping={
        "traffic_policy_arn": "trafficPolicyArn",
        "traffic_policy_id": "trafficPolicyId",
    },
)
class MailManagerTrafficPolicyReference:
    def __init__(
        self,
        *,
        traffic_policy_arn: builtins.str,
        traffic_policy_id: builtins.str,
    ) -> None:
        '''A reference to a MailManagerTrafficPolicy resource.

        :param traffic_policy_arn: The ARN of the MailManagerTrafficPolicy resource.
        :param traffic_policy_id: The TrafficPolicyId of the MailManagerTrafficPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            mail_manager_traffic_policy_reference = interfaces_ses.MailManagerTrafficPolicyReference(
                traffic_policy_arn="trafficPolicyArn",
                traffic_policy_id="trafficPolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__205ca1074da01182de1ffa47ee6863235fb4c5979f395f404b9a0d9eb9befc57)
            check_type(argname="argument traffic_policy_arn", value=traffic_policy_arn, expected_type=type_hints["traffic_policy_arn"])
            check_type(argname="argument traffic_policy_id", value=traffic_policy_id, expected_type=type_hints["traffic_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "traffic_policy_arn": traffic_policy_arn,
            "traffic_policy_id": traffic_policy_id,
        }

    @builtins.property
    def traffic_policy_arn(self) -> builtins.str:
        '''The ARN of the MailManagerTrafficPolicy resource.'''
        result = self._values.get("traffic_policy_arn")
        assert result is not None, "Required property 'traffic_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def traffic_policy_id(self) -> builtins.str:
        '''The TrafficPolicyId of the MailManagerTrafficPolicy resource.'''
        result = self._values.get("traffic_policy_id")
        assert result is not None, "Required property 'traffic_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MailManagerTrafficPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.MultiRegionEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"endpoint_name": "endpointName"},
)
class MultiRegionEndpointReference:
    def __init__(self, *, endpoint_name: builtins.str) -> None:
        '''A reference to a MultiRegionEndpoint resource.

        :param endpoint_name: The EndpointName of the MultiRegionEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            multi_region_endpoint_reference = interfaces_ses.MultiRegionEndpointReference(
                endpoint_name="endpointName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29b32ebdcc43f241fd324d2e3a0484214701c12de78f535ef4527d5277fe7476)
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_name": endpoint_name,
        }

    @builtins.property
    def endpoint_name(self) -> builtins.str:
        '''The EndpointName of the MultiRegionEndpoint resource.'''
        result = self._values.get("endpoint_name")
        assert result is not None, "Required property 'endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultiRegionEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.ReceiptFilterReference",
    jsii_struct_bases=[],
    name_mapping={"receipt_filter_id": "receiptFilterId"},
)
class ReceiptFilterReference:
    def __init__(self, *, receipt_filter_id: builtins.str) -> None:
        '''A reference to a ReceiptFilter resource.

        :param receipt_filter_id: The Id of the ReceiptFilter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            receipt_filter_reference = interfaces_ses.ReceiptFilterReference(
                receipt_filter_id="receiptFilterId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d80635f2750aaab778cde9cd85371121e61ffafb06c9be630c4b577c2168f83)
            check_type(argname="argument receipt_filter_id", value=receipt_filter_id, expected_type=type_hints["receipt_filter_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "receipt_filter_id": receipt_filter_id,
        }

    @builtins.property
    def receipt_filter_id(self) -> builtins.str:
        '''The Id of the ReceiptFilter resource.'''
        result = self._values.get("receipt_filter_id")
        assert result is not None, "Required property 'receipt_filter_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptFilterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.ReceiptRuleReference",
    jsii_struct_bases=[],
    name_mapping={"receipt_rule_id": "receiptRuleId"},
)
class ReceiptRuleReference:
    def __init__(self, *, receipt_rule_id: builtins.str) -> None:
        '''A reference to a ReceiptRule resource.

        :param receipt_rule_id: The Id of the ReceiptRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            receipt_rule_reference = interfaces_ses.ReceiptRuleReference(
                receipt_rule_id="receiptRuleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__363cf68bbf8c488eefc1ebe3e54c3c412bdcb6eef06d4572cd6a7d1e38ab11d3)
            check_type(argname="argument receipt_rule_id", value=receipt_rule_id, expected_type=type_hints["receipt_rule_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "receipt_rule_id": receipt_rule_id,
        }

    @builtins.property
    def receipt_rule_id(self) -> builtins.str:
        '''The Id of the ReceiptRule resource.'''
        result = self._values.get("receipt_rule_id")
        assert result is not None, "Required property 'receipt_rule_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.ReceiptRuleSetReference",
    jsii_struct_bases=[],
    name_mapping={"rule_set_name": "ruleSetName"},
)
class ReceiptRuleSetReference:
    def __init__(self, *, rule_set_name: builtins.str) -> None:
        '''A reference to a ReceiptRuleSet resource.

        :param rule_set_name: The RuleSetName of the ReceiptRuleSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            receipt_rule_set_reference = interfaces_ses.ReceiptRuleSetReference(
                rule_set_name="ruleSetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a8b0af72ead1871122888635202efb56ab07d6d385015d5dd64c6af6d67de3df)
            check_type(argname="argument rule_set_name", value=rule_set_name, expected_type=type_hints["rule_set_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_set_name": rule_set_name,
        }

    @builtins.property
    def rule_set_name(self) -> builtins.str:
        '''The RuleSetName of the ReceiptRuleSet resource.'''
        result = self._values.get("rule_set_name")
        assert result is not None, "Required property 'rule_set_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.TemplateReference",
    jsii_struct_bases=[],
    name_mapping={"template_id": "templateId"},
)
class TemplateReference:
    def __init__(self, *, template_id: builtins.str) -> None:
        '''A reference to a Template resource.

        :param template_id: The Id of the Template resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            template_reference = interfaces_ses.TemplateReference(
                template_id="templateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bff65c596a54ecb144242af79ad669ad596182afa21c0c8114c0d19ebe54d151)
            check_type(argname="argument template_id", value=template_id, expected_type=type_hints["template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "template_id": template_id,
        }

    @builtins.property
    def template_id(self) -> builtins.str:
        '''The Id of the Template resource.'''
        result = self._values.get("template_id")
        assert result is not None, "Required property 'template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.TenantReference",
    jsii_struct_bases=[],
    name_mapping={"tenant_arn": "tenantArn", "tenant_name": "tenantName"},
)
class TenantReference:
    def __init__(self, *, tenant_arn: builtins.str, tenant_name: builtins.str) -> None:
        '''A reference to a Tenant resource.

        :param tenant_arn: The ARN of the Tenant resource.
        :param tenant_name: The TenantName of the Tenant resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            tenant_reference = interfaces_ses.TenantReference(
                tenant_arn="tenantArn",
                tenant_name="tenantName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fc549d98c71c6825704c4331407116c91f8bbba45ccba5c8e0a84c63f182d65)
            check_type(argname="argument tenant_arn", value=tenant_arn, expected_type=type_hints["tenant_arn"])
            check_type(argname="argument tenant_name", value=tenant_name, expected_type=type_hints["tenant_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tenant_arn": tenant_arn,
            "tenant_name": tenant_name,
        }

    @builtins.property
    def tenant_arn(self) -> builtins.str:
        '''The ARN of the Tenant resource.'''
        result = self._values.get("tenant_arn")
        assert result is not None, "Required property 'tenant_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_name(self) -> builtins.str:
        '''The TenantName of the Tenant resource.'''
        result = self._values.get("tenant_name")
        assert result is not None, "Required property 'tenant_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TenantReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ses.VdmAttributesReference",
    jsii_struct_bases=[],
    name_mapping={"vdm_attributes_resource_id": "vdmAttributesResourceId"},
)
class VdmAttributesReference:
    def __init__(self, *, vdm_attributes_resource_id: builtins.str) -> None:
        '''A reference to a VdmAttributes resource.

        :param vdm_attributes_resource_id: The VdmAttributesResourceId of the VdmAttributes resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ses as interfaces_ses
            
            vdm_attributes_reference = interfaces_ses.VdmAttributesReference(
                vdm_attributes_resource_id="vdmAttributesResourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__602c7efea7e375b6f852dbd10f664e586f718be768b824afd2b7d09c6f6d47af)
            check_type(argname="argument vdm_attributes_resource_id", value=vdm_attributes_resource_id, expected_type=type_hints["vdm_attributes_resource_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vdm_attributes_resource_id": vdm_attributes_resource_id,
        }

    @builtins.property
    def vdm_attributes_resource_id(self) -> builtins.str:
        '''The VdmAttributesResourceId of the VdmAttributes resource.'''
        result = self._values.get("vdm_attributes_resource_id")
        assert result is not None, "Required property 'vdm_attributes_resource_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VdmAttributesReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConfigurationSetEventDestinationReference",
    "ConfigurationSetReference",
    "ContactListReference",
    "CustomVerificationEmailTemplateReference",
    "DedicatedIpPoolReference",
    "EmailIdentityReference",
    "IConfigurationSetEventDestinationRef",
    "IConfigurationSetRef",
    "IContactListRef",
    "ICustomVerificationEmailTemplateRef",
    "IDedicatedIpPoolRef",
    "IEmailIdentityRef",
    "IMailManagerAddonInstanceRef",
    "IMailManagerAddonSubscriptionRef",
    "IMailManagerAddressListRef",
    "IMailManagerArchiveRef",
    "IMailManagerIngressPointRef",
    "IMailManagerRelayRef",
    "IMailManagerRuleSetRef",
    "IMailManagerTrafficPolicyRef",
    "IMultiRegionEndpointRef",
    "IReceiptFilterRef",
    "IReceiptRuleRef",
    "IReceiptRuleSetRef",
    "ITemplateRef",
    "ITenantRef",
    "IVdmAttributesRef",
    "MailManagerAddonInstanceReference",
    "MailManagerAddonSubscriptionReference",
    "MailManagerAddressListReference",
    "MailManagerArchiveReference",
    "MailManagerIngressPointReference",
    "MailManagerRelayReference",
    "MailManagerRuleSetReference",
    "MailManagerTrafficPolicyReference",
    "MultiRegionEndpointReference",
    "ReceiptFilterReference",
    "ReceiptRuleReference",
    "ReceiptRuleSetReference",
    "TemplateReference",
    "TenantReference",
    "VdmAttributesReference",
]

publication.publish()

def _typecheckingstub__233e229dac98a6018ca0e6d41c128dd532e86367935bcb73cbcaf6d97404701f(
    *,
    configuration_set_event_destination_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b5ae328c9b7ac2d7bc907cf4efe09aa28d00f7f96b67d9ed14120c682a116c9(
    *,
    configuration_set_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf2861ff3744b9c917ef3e590b8a64df3604ae487bb1f4e654554a0d15dd6703(
    *,
    contact_list_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eee22c43f539103bf5c9a3012ec0e02b3d53fefdbe06140992d58a1c5943859b(
    *,
    template_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b96dd5318bf107e0627b56848ee58eb242f0abb737a14fd282245dda453b702(
    *,
    pool_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78d4b405750ad37e2ceb18cc71d146af078abd3d3df476b2b7acf90c5f293cba(
    *,
    email_identity: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8992f803f7505e5c4e7f7ccc64a127ca7b7063494b30e9339e4be159c0cfad2(
    *,
    addon_instance_arn: builtins.str,
    addon_instance_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06c8f0b71be4b35dd631e5b326b64de20a8a9419c00ee747d47feb81e8e24d10(
    *,
    addon_subscription_arn: builtins.str,
    addon_subscription_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c2b0da17cb6c3256946c402db92a74c797c3f05e0d39993ce9b3fa320c136fe(
    *,
    address_list_arn: builtins.str,
    address_list_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d873d90f01d0f3d0d63356e5f39ba9bc18cfdf68b988be224e350d3631357471(
    *,
    archive_arn: builtins.str,
    archive_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8145e93ee23430220a5eda157c3db564cad6b152e32d494bde06e8d772a86c20(
    *,
    ingress_point_arn: builtins.str,
    ingress_point_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0562a03f6b72be06c19d5688e1c48764e8ded3478b41a82adc774cf5a0fbed07(
    *,
    relay_arn: builtins.str,
    relay_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fd5bafd074000bd08230593448d667674cbf8e9ec48c59888040334cc4a4b23(
    *,
    rule_set_arn: builtins.str,
    rule_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__205ca1074da01182de1ffa47ee6863235fb4c5979f395f404b9a0d9eb9befc57(
    *,
    traffic_policy_arn: builtins.str,
    traffic_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29b32ebdcc43f241fd324d2e3a0484214701c12de78f535ef4527d5277fe7476(
    *,
    endpoint_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d80635f2750aaab778cde9cd85371121e61ffafb06c9be630c4b577c2168f83(
    *,
    receipt_filter_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__363cf68bbf8c488eefc1ebe3e54c3c412bdcb6eef06d4572cd6a7d1e38ab11d3(
    *,
    receipt_rule_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8b0af72ead1871122888635202efb56ab07d6d385015d5dd64c6af6d67de3df(
    *,
    rule_set_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bff65c596a54ecb144242af79ad669ad596182afa21c0c8114c0d19ebe54d151(
    *,
    template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fc549d98c71c6825704c4331407116c91f8bbba45ccba5c8e0a84c63f182d65(
    *,
    tenant_arn: builtins.str,
    tenant_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__602c7efea7e375b6f852dbd10f664e586f718be768b824afd2b7d09c6f6d47af(
    *,
    vdm_attributes_resource_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConfigurationSetEventDestinationRef, IConfigurationSetRef, IContactListRef, ICustomVerificationEmailTemplateRef, IDedicatedIpPoolRef, IEmailIdentityRef, IMailManagerAddonInstanceRef, IMailManagerAddonSubscriptionRef, IMailManagerAddressListRef, IMailManagerArchiveRef, IMailManagerIngressPointRef, IMailManagerRelayRef, IMailManagerRuleSetRef, IMailManagerTrafficPolicyRef, IMultiRegionEndpointRef, IReceiptFilterRef, IReceiptRuleRef, IReceiptRuleSetRef, ITemplateRef, ITenantRef, IVdmAttributesRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
