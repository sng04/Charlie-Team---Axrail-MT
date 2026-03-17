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
    jsii_type="aws-cdk-lib.interfaces.aws_ce.AnomalyMonitorReference",
    jsii_struct_bases=[],
    name_mapping={"monitor_arn": "monitorArn"},
)
class AnomalyMonitorReference:
    def __init__(self, *, monitor_arn: builtins.str) -> None:
        '''A reference to a AnomalyMonitor resource.

        :param monitor_arn: The MonitorArn of the AnomalyMonitor resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ce as interfaces_ce
            
            anomaly_monitor_reference = interfaces_ce.AnomalyMonitorReference(
                monitor_arn="monitorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed3609e8a43465e6a53b43b8a8a35257a1c5f3993b9489c9e006a1be44dff216)
            check_type(argname="argument monitor_arn", value=monitor_arn, expected_type=type_hints["monitor_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "monitor_arn": monitor_arn,
        }

    @builtins.property
    def monitor_arn(self) -> builtins.str:
        '''The MonitorArn of the AnomalyMonitor resource.'''
        result = self._values.get("monitor_arn")
        assert result is not None, "Required property 'monitor_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnomalyMonitorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ce.AnomalySubscriptionReference",
    jsii_struct_bases=[],
    name_mapping={"subscription_arn": "subscriptionArn"},
)
class AnomalySubscriptionReference:
    def __init__(self, *, subscription_arn: builtins.str) -> None:
        '''A reference to a AnomalySubscription resource.

        :param subscription_arn: The SubscriptionArn of the AnomalySubscription resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ce as interfaces_ce
            
            anomaly_subscription_reference = interfaces_ce.AnomalySubscriptionReference(
                subscription_arn="subscriptionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__106a89614cd42a7f8720180d08e75010e04cb9c0d2f2a8a4fd2833455de784f5)
            check_type(argname="argument subscription_arn", value=subscription_arn, expected_type=type_hints["subscription_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscription_arn": subscription_arn,
        }

    @builtins.property
    def subscription_arn(self) -> builtins.str:
        '''The SubscriptionArn of the AnomalySubscription resource.'''
        result = self._values.get("subscription_arn")
        assert result is not None, "Required property 'subscription_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnomalySubscriptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ce.CostCategoryReference",
    jsii_struct_bases=[],
    name_mapping={"cost_category_arn": "costCategoryArn"},
)
class CostCategoryReference:
    def __init__(self, *, cost_category_arn: builtins.str) -> None:
        '''A reference to a CostCategory resource.

        :param cost_category_arn: The Arn of the CostCategory resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ce as interfaces_ce
            
            cost_category_reference = interfaces_ce.CostCategoryReference(
                cost_category_arn="costCategoryArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bec5afaf1a6a4d600e9135f783e3d10198ee5f54398e1cd009aa8863a8efb94)
            check_type(argname="argument cost_category_arn", value=cost_category_arn, expected_type=type_hints["cost_category_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cost_category_arn": cost_category_arn,
        }

    @builtins.property
    def cost_category_arn(self) -> builtins.str:
        '''The Arn of the CostCategory resource.'''
        result = self._values.get("cost_category_arn")
        assert result is not None, "Required property 'cost_category_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CostCategoryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ce.IAnomalyMonitorRef")
class IAnomalyMonitorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AnomalyMonitor.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="anomalyMonitorRef")
    def anomaly_monitor_ref(self) -> "AnomalyMonitorReference":
        '''(experimental) A reference to a AnomalyMonitor resource.

        :stability: experimental
        '''
        ...


class _IAnomalyMonitorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AnomalyMonitor.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ce.IAnomalyMonitorRef"

    @builtins.property
    @jsii.member(jsii_name="anomalyMonitorRef")
    def anomaly_monitor_ref(self) -> "AnomalyMonitorReference":
        '''(experimental) A reference to a AnomalyMonitor resource.

        :stability: experimental
        '''
        return typing.cast("AnomalyMonitorReference", jsii.get(self, "anomalyMonitorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnomalyMonitorRef).__jsii_proxy_class__ = lambda : _IAnomalyMonitorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ce.IAnomalySubscriptionRef")
class IAnomalySubscriptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AnomalySubscription.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="anomalySubscriptionRef")
    def anomaly_subscription_ref(self) -> "AnomalySubscriptionReference":
        '''(experimental) A reference to a AnomalySubscription resource.

        :stability: experimental
        '''
        ...


class _IAnomalySubscriptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AnomalySubscription.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ce.IAnomalySubscriptionRef"

    @builtins.property
    @jsii.member(jsii_name="anomalySubscriptionRef")
    def anomaly_subscription_ref(self) -> "AnomalySubscriptionReference":
        '''(experimental) A reference to a AnomalySubscription resource.

        :stability: experimental
        '''
        return typing.cast("AnomalySubscriptionReference", jsii.get(self, "anomalySubscriptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnomalySubscriptionRef).__jsii_proxy_class__ = lambda : _IAnomalySubscriptionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ce.ICostCategoryRef")
class ICostCategoryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CostCategory.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="costCategoryRef")
    def cost_category_ref(self) -> "CostCategoryReference":
        '''(experimental) A reference to a CostCategory resource.

        :stability: experimental
        '''
        ...


class _ICostCategoryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CostCategory.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ce.ICostCategoryRef"

    @builtins.property
    @jsii.member(jsii_name="costCategoryRef")
    def cost_category_ref(self) -> "CostCategoryReference":
        '''(experimental) A reference to a CostCategory resource.

        :stability: experimental
        '''
        return typing.cast("CostCategoryReference", jsii.get(self, "costCategoryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICostCategoryRef).__jsii_proxy_class__ = lambda : _ICostCategoryRefProxy


__all__ = [
    "AnomalyMonitorReference",
    "AnomalySubscriptionReference",
    "CostCategoryReference",
    "IAnomalyMonitorRef",
    "IAnomalySubscriptionRef",
    "ICostCategoryRef",
]

publication.publish()

def _typecheckingstub__ed3609e8a43465e6a53b43b8a8a35257a1c5f3993b9489c9e006a1be44dff216(
    *,
    monitor_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__106a89614cd42a7f8720180d08e75010e04cb9c0d2f2a8a4fd2833455de784f5(
    *,
    subscription_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bec5afaf1a6a4d600e9135f783e3d10198ee5f54398e1cd009aa8863a8efb94(
    *,
    cost_category_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAnomalyMonitorRef, IAnomalySubscriptionRef, ICostCategoryRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
