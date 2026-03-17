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
    jsii_type="aws-cdk-lib.interfaces.aws_applicationsignals.DiscoveryReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class DiscoveryReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a Discovery resource.

        :param account_id: The AccountId of the Discovery resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_applicationsignals as interfaces_applicationsignals
            
            discovery_reference = interfaces_applicationsignals.DiscoveryReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d112322af801022df3ed7ef5219c298595cb73261017876bd6694b76ab8779e7)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the Discovery resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DiscoveryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_applicationsignals.GroupingConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class GroupingConfigurationReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a GroupingConfiguration resource.

        :param account_id: The AccountId of the GroupingConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_applicationsignals as interfaces_applicationsignals
            
            grouping_configuration_reference = interfaces_applicationsignals.GroupingConfigurationReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63cfc8e32ddc4fa983bee8463cd6da319f6fe3561d33da2f7e1d761b2b201fc9)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the GroupingConfiguration resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupingConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_applicationsignals.IDiscoveryRef"
)
class IDiscoveryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Discovery.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="discoveryRef")
    def discovery_ref(self) -> "DiscoveryReference":
        '''(experimental) A reference to a Discovery resource.

        :stability: experimental
        '''
        ...


class _IDiscoveryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Discovery.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_applicationsignals.IDiscoveryRef"

    @builtins.property
    @jsii.member(jsii_name="discoveryRef")
    def discovery_ref(self) -> "DiscoveryReference":
        '''(experimental) A reference to a Discovery resource.

        :stability: experimental
        '''
        return typing.cast("DiscoveryReference", jsii.get(self, "discoveryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDiscoveryRef).__jsii_proxy_class__ = lambda : _IDiscoveryRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_applicationsignals.IGroupingConfigurationRef"
)
class IGroupingConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GroupingConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="groupingConfigurationRef")
    def grouping_configuration_ref(self) -> "GroupingConfigurationReference":
        '''(experimental) A reference to a GroupingConfiguration resource.

        :stability: experimental
        '''
        ...


class _IGroupingConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GroupingConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_applicationsignals.IGroupingConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="groupingConfigurationRef")
    def grouping_configuration_ref(self) -> "GroupingConfigurationReference":
        '''(experimental) A reference to a GroupingConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("GroupingConfigurationReference", jsii.get(self, "groupingConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupingConfigurationRef).__jsii_proxy_class__ = lambda : _IGroupingConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_applicationsignals.IServiceLevelObjectiveRef"
)
class IServiceLevelObjectiveRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceLevelObjective.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceLevelObjectiveRef")
    def service_level_objective_ref(self) -> "ServiceLevelObjectiveReference":
        '''(experimental) A reference to a ServiceLevelObjective resource.

        :stability: experimental
        '''
        ...


class _IServiceLevelObjectiveRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceLevelObjective.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_applicationsignals.IServiceLevelObjectiveRef"

    @builtins.property
    @jsii.member(jsii_name="serviceLevelObjectiveRef")
    def service_level_objective_ref(self) -> "ServiceLevelObjectiveReference":
        '''(experimental) A reference to a ServiceLevelObjective resource.

        :stability: experimental
        '''
        return typing.cast("ServiceLevelObjectiveReference", jsii.get(self, "serviceLevelObjectiveRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceLevelObjectiveRef).__jsii_proxy_class__ = lambda : _IServiceLevelObjectiveRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_applicationsignals.ServiceLevelObjectiveReference",
    jsii_struct_bases=[],
    name_mapping={"service_level_objective_arn": "serviceLevelObjectiveArn"},
)
class ServiceLevelObjectiveReference:
    def __init__(self, *, service_level_objective_arn: builtins.str) -> None:
        '''A reference to a ServiceLevelObjective resource.

        :param service_level_objective_arn: The Arn of the ServiceLevelObjective resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_applicationsignals as interfaces_applicationsignals
            
            service_level_objective_reference = interfaces_applicationsignals.ServiceLevelObjectiveReference(
                service_level_objective_arn="serviceLevelObjectiveArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2e32f6fff740d39f1d435dbac6302f0703af42f33b9a51669c9841041bb9140)
            check_type(argname="argument service_level_objective_arn", value=service_level_objective_arn, expected_type=type_hints["service_level_objective_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_level_objective_arn": service_level_objective_arn,
        }

    @builtins.property
    def service_level_objective_arn(self) -> builtins.str:
        '''The Arn of the ServiceLevelObjective resource.'''
        result = self._values.get("service_level_objective_arn")
        assert result is not None, "Required property 'service_level_objective_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLevelObjectiveReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DiscoveryReference",
    "GroupingConfigurationReference",
    "IDiscoveryRef",
    "IGroupingConfigurationRef",
    "IServiceLevelObjectiveRef",
    "ServiceLevelObjectiveReference",
]

publication.publish()

def _typecheckingstub__d112322af801022df3ed7ef5219c298595cb73261017876bd6694b76ab8779e7(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63cfc8e32ddc4fa983bee8463cd6da319f6fe3561d33da2f7e1d761b2b201fc9(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2e32f6fff740d39f1d435dbac6302f0703af42f33b9a51669c9841041bb9140(
    *,
    service_level_objective_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDiscoveryRef, IGroupingConfigurationRef, IServiceLevelObjectiveRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
