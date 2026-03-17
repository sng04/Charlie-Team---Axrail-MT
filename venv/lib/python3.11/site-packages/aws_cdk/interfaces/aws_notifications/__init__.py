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
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.ChannelAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "channel_association_arn": "channelAssociationArn",
        "notification_configuration_arn": "notificationConfigurationArn",
    },
)
class ChannelAssociationReference:
    def __init__(
        self,
        *,
        channel_association_arn: builtins.str,
        notification_configuration_arn: builtins.str,
    ) -> None:
        '''A reference to a ChannelAssociation resource.

        :param channel_association_arn: The Arn of the ChannelAssociation resource.
        :param notification_configuration_arn: The NotificationConfigurationArn of the ChannelAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_notifications as interfaces_notifications
            
            channel_association_reference = interfaces_notifications.ChannelAssociationReference(
                channel_association_arn="channelAssociationArn",
                notification_configuration_arn="notificationConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6010b83c0e961b495968bf982b1b332200c1ef952cd03723212c88e8566ff20c)
            check_type(argname="argument channel_association_arn", value=channel_association_arn, expected_type=type_hints["channel_association_arn"])
            check_type(argname="argument notification_configuration_arn", value=notification_configuration_arn, expected_type=type_hints["notification_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_association_arn": channel_association_arn,
            "notification_configuration_arn": notification_configuration_arn,
        }

    @builtins.property
    def channel_association_arn(self) -> builtins.str:
        '''The Arn of the ChannelAssociation resource.'''
        result = self._values.get("channel_association_arn")
        assert result is not None, "Required property 'channel_association_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification_configuration_arn(self) -> builtins.str:
        '''The NotificationConfigurationArn of the ChannelAssociation resource.'''
        result = self._values.get("notification_configuration_arn")
        assert result is not None, "Required property 'notification_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.EventRuleReference",
    jsii_struct_bases=[],
    name_mapping={"event_rule_arn": "eventRuleArn"},
)
class EventRuleReference:
    def __init__(self, *, event_rule_arn: builtins.str) -> None:
        '''A reference to a EventRule resource.

        :param event_rule_arn: The Arn of the EventRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_notifications as interfaces_notifications
            
            event_rule_reference = interfaces_notifications.EventRuleReference(
                event_rule_arn="eventRuleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d554d222f11444ec376e8b5910505d101ae7fa862f804905ac07fa8a8ae874b2)
            check_type(argname="argument event_rule_arn", value=event_rule_arn, expected_type=type_hints["event_rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_rule_arn": event_rule_arn,
        }

    @builtins.property
    def event_rule_arn(self) -> builtins.str:
        '''The Arn of the EventRule resource.'''
        result = self._values.get("event_rule_arn")
        assert result is not None, "Required property 'event_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.IChannelAssociationRef"
)
class IChannelAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelAssociationRef")
    def channel_association_ref(self) -> "ChannelAssociationReference":
        '''(experimental) A reference to a ChannelAssociation resource.

        :stability: experimental
        '''
        ...


class _IChannelAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ChannelAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_notifications.IChannelAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="channelAssociationRef")
    def channel_association_ref(self) -> "ChannelAssociationReference":
        '''(experimental) A reference to a ChannelAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ChannelAssociationReference", jsii.get(self, "channelAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelAssociationRef).__jsii_proxy_class__ = lambda : _IChannelAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_notifications.IEventRuleRef")
class IEventRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventRuleRef")
    def event_rule_ref(self) -> "EventRuleReference":
        '''(experimental) A reference to a EventRule resource.

        :stability: experimental
        '''
        ...


class _IEventRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_notifications.IEventRuleRef"

    @builtins.property
    @jsii.member(jsii_name="eventRuleRef")
    def event_rule_ref(self) -> "EventRuleReference":
        '''(experimental) A reference to a EventRule resource.

        :stability: experimental
        '''
        return typing.cast("EventRuleReference", jsii.get(self, "eventRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventRuleRef).__jsii_proxy_class__ = lambda : _IEventRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.IManagedNotificationAccountContactAssociationRef"
)
class IManagedNotificationAccountContactAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ManagedNotificationAccountContactAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="managedNotificationAccountContactAssociationRef")
    def managed_notification_account_contact_association_ref(
        self,
    ) -> "ManagedNotificationAccountContactAssociationReference":
        '''(experimental) A reference to a ManagedNotificationAccountContactAssociation resource.

        :stability: experimental
        '''
        ...


class _IManagedNotificationAccountContactAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ManagedNotificationAccountContactAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_notifications.IManagedNotificationAccountContactAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="managedNotificationAccountContactAssociationRef")
    def managed_notification_account_contact_association_ref(
        self,
    ) -> "ManagedNotificationAccountContactAssociationReference":
        '''(experimental) A reference to a ManagedNotificationAccountContactAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ManagedNotificationAccountContactAssociationReference", jsii.get(self, "managedNotificationAccountContactAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IManagedNotificationAccountContactAssociationRef).__jsii_proxy_class__ = lambda : _IManagedNotificationAccountContactAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.IManagedNotificationAdditionalChannelAssociationRef"
)
class IManagedNotificationAdditionalChannelAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ManagedNotificationAdditionalChannelAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="managedNotificationAdditionalChannelAssociationRef")
    def managed_notification_additional_channel_association_ref(
        self,
    ) -> "ManagedNotificationAdditionalChannelAssociationReference":
        '''(experimental) A reference to a ManagedNotificationAdditionalChannelAssociation resource.

        :stability: experimental
        '''
        ...


class _IManagedNotificationAdditionalChannelAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ManagedNotificationAdditionalChannelAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_notifications.IManagedNotificationAdditionalChannelAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="managedNotificationAdditionalChannelAssociationRef")
    def managed_notification_additional_channel_association_ref(
        self,
    ) -> "ManagedNotificationAdditionalChannelAssociationReference":
        '''(experimental) A reference to a ManagedNotificationAdditionalChannelAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ManagedNotificationAdditionalChannelAssociationReference", jsii.get(self, "managedNotificationAdditionalChannelAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IManagedNotificationAdditionalChannelAssociationRef).__jsii_proxy_class__ = lambda : _IManagedNotificationAdditionalChannelAssociationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.INotificationConfigurationRef"
)
class INotificationConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NotificationConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="notificationConfigurationRef")
    def notification_configuration_ref(self) -> "NotificationConfigurationReference":
        '''(experimental) A reference to a NotificationConfiguration resource.

        :stability: experimental
        '''
        ...


class _INotificationConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NotificationConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_notifications.INotificationConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="notificationConfigurationRef")
    def notification_configuration_ref(self) -> "NotificationConfigurationReference":
        '''(experimental) A reference to a NotificationConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("NotificationConfigurationReference", jsii.get(self, "notificationConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotificationConfigurationRef).__jsii_proxy_class__ = lambda : _INotificationConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.INotificationHubRef"
)
class INotificationHubRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NotificationHub.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="notificationHubRef")
    def notification_hub_ref(self) -> "NotificationHubReference":
        '''(experimental) A reference to a NotificationHub resource.

        :stability: experimental
        '''
        ...


class _INotificationHubRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NotificationHub.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_notifications.INotificationHubRef"

    @builtins.property
    @jsii.member(jsii_name="notificationHubRef")
    def notification_hub_ref(self) -> "NotificationHubReference":
        '''(experimental) A reference to a NotificationHub resource.

        :stability: experimental
        '''
        return typing.cast("NotificationHubReference", jsii.get(self, "notificationHubRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotificationHubRef).__jsii_proxy_class__ = lambda : _INotificationHubRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.IOrganizationalUnitAssociationRef"
)
class IOrganizationalUnitAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationalUnitAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitAssociationRef")
    def organizational_unit_association_ref(
        self,
    ) -> "OrganizationalUnitAssociationReference":
        '''(experimental) A reference to a OrganizationalUnitAssociation resource.

        :stability: experimental
        '''
        ...


class _IOrganizationalUnitAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationalUnitAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_notifications.IOrganizationalUnitAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitAssociationRef")
    def organizational_unit_association_ref(
        self,
    ) -> "OrganizationalUnitAssociationReference":
        '''(experimental) A reference to a OrganizationalUnitAssociation resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationalUnitAssociationReference", jsii.get(self, "organizationalUnitAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationalUnitAssociationRef).__jsii_proxy_class__ = lambda : _IOrganizationalUnitAssociationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.ManagedNotificationAccountContactAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "contact_identifier": "contactIdentifier",
        "managed_notification_configuration_arn": "managedNotificationConfigurationArn",
    },
)
class ManagedNotificationAccountContactAssociationReference:
    def __init__(
        self,
        *,
        contact_identifier: builtins.str,
        managed_notification_configuration_arn: builtins.str,
    ) -> None:
        '''A reference to a ManagedNotificationAccountContactAssociation resource.

        :param contact_identifier: The ContactIdentifier of the ManagedNotificationAccountContactAssociation resource.
        :param managed_notification_configuration_arn: The ManagedNotificationConfigurationArn of the ManagedNotificationAccountContactAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_notifications as interfaces_notifications
            
            managed_notification_account_contact_association_reference = interfaces_notifications.ManagedNotificationAccountContactAssociationReference(
                contact_identifier="contactIdentifier",
                managed_notification_configuration_arn="managedNotificationConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__205eda7b62484f9f0ee487c4bfac941cc581fb66dd709b17aa1b1985e72e951b)
            check_type(argname="argument contact_identifier", value=contact_identifier, expected_type=type_hints["contact_identifier"])
            check_type(argname="argument managed_notification_configuration_arn", value=managed_notification_configuration_arn, expected_type=type_hints["managed_notification_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "contact_identifier": contact_identifier,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }

    @builtins.property
    def contact_identifier(self) -> builtins.str:
        '''The ContactIdentifier of the ManagedNotificationAccountContactAssociation resource.'''
        result = self._values.get("contact_identifier")
        assert result is not None, "Required property 'contact_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_notification_configuration_arn(self) -> builtins.str:
        '''The ManagedNotificationConfigurationArn of the ManagedNotificationAccountContactAssociation resource.'''
        result = self._values.get("managed_notification_configuration_arn")
        assert result is not None, "Required property 'managed_notification_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedNotificationAccountContactAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.ManagedNotificationAdditionalChannelAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "channel_arn": "channelArn",
        "managed_notification_configuration_arn": "managedNotificationConfigurationArn",
    },
)
class ManagedNotificationAdditionalChannelAssociationReference:
    def __init__(
        self,
        *,
        channel_arn: builtins.str,
        managed_notification_configuration_arn: builtins.str,
    ) -> None:
        '''A reference to a ManagedNotificationAdditionalChannelAssociation resource.

        :param channel_arn: The ChannelArn of the ManagedNotificationAdditionalChannelAssociation resource.
        :param managed_notification_configuration_arn: The ManagedNotificationConfigurationArn of the ManagedNotificationAdditionalChannelAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_notifications as interfaces_notifications
            
            managed_notification_additional_channel_association_reference = interfaces_notifications.ManagedNotificationAdditionalChannelAssociationReference(
                channel_arn="channelArn",
                managed_notification_configuration_arn="managedNotificationConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4afedf31a01cbe5df87d942fb09a8752930c429a86620292d1777d1879c2b6e)
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
            check_type(argname="argument managed_notification_configuration_arn", value=managed_notification_configuration_arn, expected_type=type_hints["managed_notification_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_arn": channel_arn,
            "managed_notification_configuration_arn": managed_notification_configuration_arn,
        }

    @builtins.property
    def channel_arn(self) -> builtins.str:
        '''The ChannelArn of the ManagedNotificationAdditionalChannelAssociation resource.'''
        result = self._values.get("channel_arn")
        assert result is not None, "Required property 'channel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def managed_notification_configuration_arn(self) -> builtins.str:
        '''The ManagedNotificationConfigurationArn of the ManagedNotificationAdditionalChannelAssociation resource.'''
        result = self._values.get("managed_notification_configuration_arn")
        assert result is not None, "Required property 'managed_notification_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedNotificationAdditionalChannelAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.NotificationConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"notification_configuration_arn": "notificationConfigurationArn"},
)
class NotificationConfigurationReference:
    def __init__(self, *, notification_configuration_arn: builtins.str) -> None:
        '''A reference to a NotificationConfiguration resource.

        :param notification_configuration_arn: The Arn of the NotificationConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_notifications as interfaces_notifications
            
            notification_configuration_reference = interfaces_notifications.NotificationConfigurationReference(
                notification_configuration_arn="notificationConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32d95bddb5a77a8a242a3cc12774adf022463c8a08bc89038e822748db2124f8)
            check_type(argname="argument notification_configuration_arn", value=notification_configuration_arn, expected_type=type_hints["notification_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "notification_configuration_arn": notification_configuration_arn,
        }

    @builtins.property
    def notification_configuration_arn(self) -> builtins.str:
        '''The Arn of the NotificationConfiguration resource.'''
        result = self._values.get("notification_configuration_arn")
        assert result is not None, "Required property 'notification_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.NotificationHubReference",
    jsii_struct_bases=[],
    name_mapping={"region": "region"},
)
class NotificationHubReference:
    def __init__(self, *, region: builtins.str) -> None:
        '''A reference to a NotificationHub resource.

        :param region: The Region of the NotificationHub resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_notifications as interfaces_notifications
            
            notification_hub_reference = interfaces_notifications.NotificationHubReference(
                region="region"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1f95e96b3dcd9198f5f6ea848cc9f5a988a94228b6fca344796f1f7c36f0cb9)
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "region": region,
        }

    @builtins.property
    def region(self) -> builtins.str:
        '''The Region of the NotificationHub resource.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationHubReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_notifications.OrganizationalUnitAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "notification_configuration_arn": "notificationConfigurationArn",
        "organizational_unit_id": "organizationalUnitId",
    },
)
class OrganizationalUnitAssociationReference:
    def __init__(
        self,
        *,
        notification_configuration_arn: builtins.str,
        organizational_unit_id: builtins.str,
    ) -> None:
        '''A reference to a OrganizationalUnitAssociation resource.

        :param notification_configuration_arn: The NotificationConfigurationArn of the OrganizationalUnitAssociation resource.
        :param organizational_unit_id: The OrganizationalUnitId of the OrganizationalUnitAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_notifications as interfaces_notifications
            
            organizational_unit_association_reference = interfaces_notifications.OrganizationalUnitAssociationReference(
                notification_configuration_arn="notificationConfigurationArn",
                organizational_unit_id="organizationalUnitId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcaff237a7248361a31927e9a4f9c14ade302aab28c6800b2db503a071b3af2a)
            check_type(argname="argument notification_configuration_arn", value=notification_configuration_arn, expected_type=type_hints["notification_configuration_arn"])
            check_type(argname="argument organizational_unit_id", value=organizational_unit_id, expected_type=type_hints["organizational_unit_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "notification_configuration_arn": notification_configuration_arn,
            "organizational_unit_id": organizational_unit_id,
        }

    @builtins.property
    def notification_configuration_arn(self) -> builtins.str:
        '''The NotificationConfigurationArn of the OrganizationalUnitAssociation resource.'''
        result = self._values.get("notification_configuration_arn")
        assert result is not None, "Required property 'notification_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organizational_unit_id(self) -> builtins.str:
        '''The OrganizationalUnitId of the OrganizationalUnitAssociation resource.'''
        result = self._values.get("organizational_unit_id")
        assert result is not None, "Required property 'organizational_unit_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationalUnitAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ChannelAssociationReference",
    "EventRuleReference",
    "IChannelAssociationRef",
    "IEventRuleRef",
    "IManagedNotificationAccountContactAssociationRef",
    "IManagedNotificationAdditionalChannelAssociationRef",
    "INotificationConfigurationRef",
    "INotificationHubRef",
    "IOrganizationalUnitAssociationRef",
    "ManagedNotificationAccountContactAssociationReference",
    "ManagedNotificationAdditionalChannelAssociationReference",
    "NotificationConfigurationReference",
    "NotificationHubReference",
    "OrganizationalUnitAssociationReference",
]

publication.publish()

def _typecheckingstub__6010b83c0e961b495968bf982b1b332200c1ef952cd03723212c88e8566ff20c(
    *,
    channel_association_arn: builtins.str,
    notification_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d554d222f11444ec376e8b5910505d101ae7fa862f804905ac07fa8a8ae874b2(
    *,
    event_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__205eda7b62484f9f0ee487c4bfac941cc581fb66dd709b17aa1b1985e72e951b(
    *,
    contact_identifier: builtins.str,
    managed_notification_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4afedf31a01cbe5df87d942fb09a8752930c429a86620292d1777d1879c2b6e(
    *,
    channel_arn: builtins.str,
    managed_notification_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32d95bddb5a77a8a242a3cc12774adf022463c8a08bc89038e822748db2124f8(
    *,
    notification_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1f95e96b3dcd9198f5f6ea848cc9f5a988a94228b6fca344796f1f7c36f0cb9(
    *,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcaff237a7248361a31927e9a4f9c14ade302aab28c6800b2db503a071b3af2a(
    *,
    notification_configuration_arn: builtins.str,
    organizational_unit_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IChannelAssociationRef, IEventRuleRef, IManagedNotificationAccountContactAssociationRef, IManagedNotificationAdditionalChannelAssociationRef, INotificationConfigurationRef, INotificationHubRef, IOrganizationalUnitAssociationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
