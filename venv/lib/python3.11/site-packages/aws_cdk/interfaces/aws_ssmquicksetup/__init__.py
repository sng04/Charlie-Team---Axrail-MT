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
    jsii_type="aws-cdk-lib.interfaces.aws_ssmquicksetup.ConfigurationManagerReference",
    jsii_struct_bases=[],
    name_mapping={"manager_arn": "managerArn"},
)
class ConfigurationManagerReference:
    def __init__(self, *, manager_arn: builtins.str) -> None:
        '''A reference to a ConfigurationManager resource.

        :param manager_arn: The ManagerArn of the ConfigurationManager resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssmquicksetup as interfaces_ssmquicksetup
            
            configuration_manager_reference = interfaces_ssmquicksetup.ConfigurationManagerReference(
                manager_arn="managerArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd9c5ba99f12b20e7873d59bb2772ed2daac536bcf43b84d8de848b0faba8c67)
            check_type(argname="argument manager_arn", value=manager_arn, expected_type=type_hints["manager_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "manager_arn": manager_arn,
        }

    @builtins.property
    def manager_arn(self) -> builtins.str:
        '''The ManagerArn of the ConfigurationManager resource.'''
        result = self._values.get("manager_arn")
        assert result is not None, "Required property 'manager_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationManagerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ssmquicksetup.IConfigurationManagerRef"
)
class IConfigurationManagerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationManager.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationManagerRef")
    def configuration_manager_ref(self) -> "ConfigurationManagerReference":
        '''(experimental) A reference to a ConfigurationManager resource.

        :stability: experimental
        '''
        ...


class _IConfigurationManagerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConfigurationManager.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssmquicksetup.IConfigurationManagerRef"

    @builtins.property
    @jsii.member(jsii_name="configurationManagerRef")
    def configuration_manager_ref(self) -> "ConfigurationManagerReference":
        '''(experimental) A reference to a ConfigurationManager resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationManagerReference", jsii.get(self, "configurationManagerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationManagerRef).__jsii_proxy_class__ = lambda : _IConfigurationManagerRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ssmquicksetup.ILifecycleAutomationRef"
)
class ILifecycleAutomationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LifecycleAutomation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="lifecycleAutomationRef")
    def lifecycle_automation_ref(self) -> "LifecycleAutomationReference":
        '''(experimental) A reference to a LifecycleAutomation resource.

        :stability: experimental
        '''
        ...


class _ILifecycleAutomationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LifecycleAutomation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ssmquicksetup.ILifecycleAutomationRef"

    @builtins.property
    @jsii.member(jsii_name="lifecycleAutomationRef")
    def lifecycle_automation_ref(self) -> "LifecycleAutomationReference":
        '''(experimental) A reference to a LifecycleAutomation resource.

        :stability: experimental
        '''
        return typing.cast("LifecycleAutomationReference", jsii.get(self, "lifecycleAutomationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILifecycleAutomationRef).__jsii_proxy_class__ = lambda : _ILifecycleAutomationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ssmquicksetup.LifecycleAutomationReference",
    jsii_struct_bases=[],
    name_mapping={"association_id": "associationId"},
)
class LifecycleAutomationReference:
    def __init__(self, *, association_id: builtins.str) -> None:
        '''A reference to a LifecycleAutomation resource.

        :param association_id: The AssociationId of the LifecycleAutomation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ssmquicksetup as interfaces_ssmquicksetup
            
            lifecycle_automation_reference = interfaces_ssmquicksetup.LifecycleAutomationReference(
                association_id="associationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba44de012a17ba74c83b063dc9de1699921b659975aba2d2d6d8e3c18212b67d)
            check_type(argname="argument association_id", value=association_id, expected_type=type_hints["association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "association_id": association_id,
        }

    @builtins.property
    def association_id(self) -> builtins.str:
        '''The AssociationId of the LifecycleAutomation resource.'''
        result = self._values.get("association_id")
        assert result is not None, "Required property 'association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LifecycleAutomationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConfigurationManagerReference",
    "IConfigurationManagerRef",
    "ILifecycleAutomationRef",
    "LifecycleAutomationReference",
]

publication.publish()

def _typecheckingstub__fd9c5ba99f12b20e7873d59bb2772ed2daac536bcf43b84d8de848b0faba8c67(
    *,
    manager_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba44de012a17ba74c83b063dc9de1699921b659975aba2d2d6d8e3c18212b67d(
    *,
    association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConfigurationManagerRef, ILifecycleAutomationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
