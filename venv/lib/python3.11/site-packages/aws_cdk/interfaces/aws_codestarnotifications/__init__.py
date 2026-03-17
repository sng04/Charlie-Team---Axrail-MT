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
    jsii_type="aws-cdk-lib.interfaces.aws_codestarnotifications.INotificationRuleRef"
)
class INotificationRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NotificationRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="notificationRuleRef")
    def notification_rule_ref(self) -> "NotificationRuleReference":
        '''(experimental) A reference to a NotificationRule resource.

        :stability: experimental
        '''
        ...


class _INotificationRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NotificationRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codestarnotifications.INotificationRuleRef"

    @builtins.property
    @jsii.member(jsii_name="notificationRuleRef")
    def notification_rule_ref(self) -> "NotificationRuleReference":
        '''(experimental) A reference to a NotificationRule resource.

        :stability: experimental
        '''
        return typing.cast("NotificationRuleReference", jsii.get(self, "notificationRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotificationRuleRef).__jsii_proxy_class__ = lambda : _INotificationRuleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codestarnotifications.NotificationRuleReference",
    jsii_struct_bases=[],
    name_mapping={"notification_rule_arn": "notificationRuleArn"},
)
class NotificationRuleReference:
    def __init__(self, *, notification_rule_arn: builtins.str) -> None:
        '''A reference to a NotificationRule resource.

        :param notification_rule_arn: The Arn of the NotificationRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codestarnotifications as interfaces_codestarnotifications
            
            notification_rule_reference = interfaces_codestarnotifications.NotificationRuleReference(
                notification_rule_arn="notificationRuleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c68ca248a86d9c3567f822c632ebbbe9e5112fae9ada146cafd5901533262e3a)
            check_type(argname="argument notification_rule_arn", value=notification_rule_arn, expected_type=type_hints["notification_rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "notification_rule_arn": notification_rule_arn,
        }

    @builtins.property
    def notification_rule_arn(self) -> builtins.str:
        '''The Arn of the NotificationRule resource.'''
        result = self._values.get("notification_rule_arn")
        assert result is not None, "Required property 'notification_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "INotificationRuleRef",
    "NotificationRuleReference",
]

publication.publish()

def _typecheckingstub__c68ca248a86d9c3567f822c632ebbbe9e5112fae9ada146cafd5901533262e3a(
    *,
    notification_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [INotificationRuleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
