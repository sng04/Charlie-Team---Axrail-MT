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
    jsii_type="aws-cdk-lib.interfaces.aws_devopsguru.ILogAnomalyDetectionIntegrationRef"
)
class ILogAnomalyDetectionIntegrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LogAnomalyDetectionIntegration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="logAnomalyDetectionIntegrationRef")
    def log_anomaly_detection_integration_ref(
        self,
    ) -> "LogAnomalyDetectionIntegrationReference":
        '''(experimental) A reference to a LogAnomalyDetectionIntegration resource.

        :stability: experimental
        '''
        ...


class _ILogAnomalyDetectionIntegrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LogAnomalyDetectionIntegration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsguru.ILogAnomalyDetectionIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="logAnomalyDetectionIntegrationRef")
    def log_anomaly_detection_integration_ref(
        self,
    ) -> "LogAnomalyDetectionIntegrationReference":
        '''(experimental) A reference to a LogAnomalyDetectionIntegration resource.

        :stability: experimental
        '''
        return typing.cast("LogAnomalyDetectionIntegrationReference", jsii.get(self, "logAnomalyDetectionIntegrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILogAnomalyDetectionIntegrationRef).__jsii_proxy_class__ = lambda : _ILogAnomalyDetectionIntegrationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsguru.INotificationChannelRef"
)
class INotificationChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NotificationChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="notificationChannelRef")
    def notification_channel_ref(self) -> "NotificationChannelReference":
        '''(experimental) A reference to a NotificationChannel resource.

        :stability: experimental
        '''
        ...


class _INotificationChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NotificationChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsguru.INotificationChannelRef"

    @builtins.property
    @jsii.member(jsii_name="notificationChannelRef")
    def notification_channel_ref(self) -> "NotificationChannelReference":
        '''(experimental) A reference to a NotificationChannel resource.

        :stability: experimental
        '''
        return typing.cast("NotificationChannelReference", jsii.get(self, "notificationChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INotificationChannelRef).__jsii_proxy_class__ = lambda : _INotificationChannelRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsguru.IResourceCollectionRef"
)
class IResourceCollectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceCollection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceCollectionRef")
    def resource_collection_ref(self) -> "ResourceCollectionReference":
        '''(experimental) A reference to a ResourceCollection resource.

        :stability: experimental
        '''
        ...


class _IResourceCollectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceCollection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devopsguru.IResourceCollectionRef"

    @builtins.property
    @jsii.member(jsii_name="resourceCollectionRef")
    def resource_collection_ref(self) -> "ResourceCollectionReference":
        '''(experimental) A reference to a ResourceCollection resource.

        :stability: experimental
        '''
        return typing.cast("ResourceCollectionReference", jsii.get(self, "resourceCollectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceCollectionRef).__jsii_proxy_class__ = lambda : _IResourceCollectionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsguru.LogAnomalyDetectionIntegrationReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class LogAnomalyDetectionIntegrationReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a LogAnomalyDetectionIntegration resource.

        :param account_id: The AccountId of the LogAnomalyDetectionIntegration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsguru as interfaces_devopsguru
            
            log_anomaly_detection_integration_reference = interfaces_devopsguru.LogAnomalyDetectionIntegrationReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8964aa470316cc36c2cef5e22544eafde27f93179765eaf98abe34410ac94edc)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the LogAnomalyDetectionIntegration resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LogAnomalyDetectionIntegrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsguru.NotificationChannelReference",
    jsii_struct_bases=[],
    name_mapping={"notification_channel_id": "notificationChannelId"},
)
class NotificationChannelReference:
    def __init__(self, *, notification_channel_id: builtins.str) -> None:
        '''A reference to a NotificationChannel resource.

        :param notification_channel_id: The Id of the NotificationChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsguru as interfaces_devopsguru
            
            notification_channel_reference = interfaces_devopsguru.NotificationChannelReference(
                notification_channel_id="notificationChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dba4d922990dabf8257b8353769029927fee06eeffaf2d6a96777c6b45658d72)
            check_type(argname="argument notification_channel_id", value=notification_channel_id, expected_type=type_hints["notification_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "notification_channel_id": notification_channel_id,
        }

    @builtins.property
    def notification_channel_id(self) -> builtins.str:
        '''The Id of the NotificationChannel resource.'''
        result = self._values.get("notification_channel_id")
        assert result is not None, "Required property 'notification_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NotificationChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devopsguru.ResourceCollectionReference",
    jsii_struct_bases=[],
    name_mapping={"resource_collection_type": "resourceCollectionType"},
)
class ResourceCollectionReference:
    def __init__(self, *, resource_collection_type: builtins.str) -> None:
        '''A reference to a ResourceCollection resource.

        :param resource_collection_type: The ResourceCollectionType of the ResourceCollection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devopsguru as interfaces_devopsguru
            
            resource_collection_reference = interfaces_devopsguru.ResourceCollectionReference(
                resource_collection_type="resourceCollectionType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98b57dff9b9b656537f6db23cbddeabb95793a055b053043b911f9e5e4f4c5c9)
            check_type(argname="argument resource_collection_type", value=resource_collection_type, expected_type=type_hints["resource_collection_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_collection_type": resource_collection_type,
        }

    @builtins.property
    def resource_collection_type(self) -> builtins.str:
        '''The ResourceCollectionType of the ResourceCollection resource.'''
        result = self._values.get("resource_collection_type")
        assert result is not None, "Required property 'resource_collection_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceCollectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ILogAnomalyDetectionIntegrationRef",
    "INotificationChannelRef",
    "IResourceCollectionRef",
    "LogAnomalyDetectionIntegrationReference",
    "NotificationChannelReference",
    "ResourceCollectionReference",
]

publication.publish()

def _typecheckingstub__8964aa470316cc36c2cef5e22544eafde27f93179765eaf98abe34410ac94edc(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dba4d922990dabf8257b8353769029927fee06eeffaf2d6a96777c6b45658d72(
    *,
    notification_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98b57dff9b9b656537f6db23cbddeabb95793a055b053043b911f9e5e4f4c5c9(
    *,
    resource_collection_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ILogAnomalyDetectionIntegrationRef, INotificationChannelRef, IResourceCollectionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
