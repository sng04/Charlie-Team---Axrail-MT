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
    jsii_type="aws-cdk-lib.interfaces.aws_arczonalshift.AutoshiftObserverNotificationStatusReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId", "region": "region"},
)
class AutoshiftObserverNotificationStatusReference:
    def __init__(self, *, account_id: builtins.str, region: builtins.str) -> None:
        '''A reference to a AutoshiftObserverNotificationStatus resource.

        :param account_id: The AccountId of the AutoshiftObserverNotificationStatus resource.
        :param region: The Region of the AutoshiftObserverNotificationStatus resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_arczonalshift as interfaces_arczonalshift
            
            autoshift_observer_notification_status_reference = interfaces_arczonalshift.AutoshiftObserverNotificationStatusReference(
                account_id="accountId",
                region="region"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__422e28e21945e6da877936196f73e4cac2f7296d7ffd7776aa700ddab34d739f)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
            "region": region,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the AutoshiftObserverNotificationStatus resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region(self) -> builtins.str:
        '''The Region of the AutoshiftObserverNotificationStatus resource.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoshiftObserverNotificationStatusReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_arczonalshift.IAutoshiftObserverNotificationStatusRef"
)
class IAutoshiftObserverNotificationStatusRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AutoshiftObserverNotificationStatus.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="autoshiftObserverNotificationStatusRef")
    def autoshift_observer_notification_status_ref(
        self,
    ) -> "AutoshiftObserverNotificationStatusReference":
        '''(experimental) A reference to a AutoshiftObserverNotificationStatus resource.

        :stability: experimental
        '''
        ...


class _IAutoshiftObserverNotificationStatusRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AutoshiftObserverNotificationStatus.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_arczonalshift.IAutoshiftObserverNotificationStatusRef"

    @builtins.property
    @jsii.member(jsii_name="autoshiftObserverNotificationStatusRef")
    def autoshift_observer_notification_status_ref(
        self,
    ) -> "AutoshiftObserverNotificationStatusReference":
        '''(experimental) A reference to a AutoshiftObserverNotificationStatus resource.

        :stability: experimental
        '''
        return typing.cast("AutoshiftObserverNotificationStatusReference", jsii.get(self, "autoshiftObserverNotificationStatusRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAutoshiftObserverNotificationStatusRef).__jsii_proxy_class__ = lambda : _IAutoshiftObserverNotificationStatusRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_arczonalshift.IZonalAutoshiftConfigurationRef"
)
class IZonalAutoshiftConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ZonalAutoshiftConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="zonalAutoshiftConfigurationRef")
    def zonal_autoshift_configuration_ref(
        self,
    ) -> "ZonalAutoshiftConfigurationReference":
        '''(experimental) A reference to a ZonalAutoshiftConfiguration resource.

        :stability: experimental
        '''
        ...


class _IZonalAutoshiftConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ZonalAutoshiftConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_arczonalshift.IZonalAutoshiftConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="zonalAutoshiftConfigurationRef")
    def zonal_autoshift_configuration_ref(
        self,
    ) -> "ZonalAutoshiftConfigurationReference":
        '''(experimental) A reference to a ZonalAutoshiftConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("ZonalAutoshiftConfigurationReference", jsii.get(self, "zonalAutoshiftConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IZonalAutoshiftConfigurationRef).__jsii_proxy_class__ = lambda : _IZonalAutoshiftConfigurationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_arczonalshift.ZonalAutoshiftConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"resource_identifier": "resourceIdentifier"},
)
class ZonalAutoshiftConfigurationReference:
    def __init__(self, *, resource_identifier: builtins.str) -> None:
        '''A reference to a ZonalAutoshiftConfiguration resource.

        :param resource_identifier: The ResourceIdentifier of the ZonalAutoshiftConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_arczonalshift as interfaces_arczonalshift
            
            zonal_autoshift_configuration_reference = interfaces_arczonalshift.ZonalAutoshiftConfigurationReference(
                resource_identifier="resourceIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff582391de5dba5d4309cecaee8eba57bcb8b930c562ef6df17dc498036ce54)
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_identifier": resource_identifier,
        }

    @builtins.property
    def resource_identifier(self) -> builtins.str:
        '''The ResourceIdentifier of the ZonalAutoshiftConfiguration resource.'''
        result = self._values.get("resource_identifier")
        assert result is not None, "Required property 'resource_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZonalAutoshiftConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AutoshiftObserverNotificationStatusReference",
    "IAutoshiftObserverNotificationStatusRef",
    "IZonalAutoshiftConfigurationRef",
    "ZonalAutoshiftConfigurationReference",
]

publication.publish()

def _typecheckingstub__422e28e21945e6da877936196f73e4cac2f7296d7ffd7776aa700ddab34d739f(
    *,
    account_id: builtins.str,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff582391de5dba5d4309cecaee8eba57bcb8b930c562ef6df17dc498036ce54(
    *,
    resource_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAutoshiftObserverNotificationStatusRef, IZonalAutoshiftConfigurationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
