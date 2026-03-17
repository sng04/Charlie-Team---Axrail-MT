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
    jsii_type="aws-cdk-lib.interfaces.aws_shield.DRTAccessReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class DRTAccessReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a DRTAccess resource.

        :param account_id: The AccountId of the DRTAccess resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_shield as interfaces_shield
            
            d_rTAccess_reference = interfaces_shield.DRTAccessReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c545dfa10e119e09d934a80388431e03d628ebfb7dfdf25de1ed7a8f359bdab)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the DRTAccess resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DRTAccessReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_shield.IDRTAccessRef")
class IDRTAccessRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DRTAccess.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="drtAccessRef")
    def drt_access_ref(self) -> "DRTAccessReference":
        '''(experimental) A reference to a DRTAccess resource.

        :stability: experimental
        '''
        ...


class _IDRTAccessRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DRTAccess.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_shield.IDRTAccessRef"

    @builtins.property
    @jsii.member(jsii_name="drtAccessRef")
    def drt_access_ref(self) -> "DRTAccessReference":
        '''(experimental) A reference to a DRTAccess resource.

        :stability: experimental
        '''
        return typing.cast("DRTAccessReference", jsii.get(self, "drtAccessRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDRTAccessRef).__jsii_proxy_class__ = lambda : _IDRTAccessRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_shield.IProactiveEngagementRef")
class IProactiveEngagementRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProactiveEngagement.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="proactiveEngagementRef")
    def proactive_engagement_ref(self) -> "ProactiveEngagementReference":
        '''(experimental) A reference to a ProactiveEngagement resource.

        :stability: experimental
        '''
        ...


class _IProactiveEngagementRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProactiveEngagement.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_shield.IProactiveEngagementRef"

    @builtins.property
    @jsii.member(jsii_name="proactiveEngagementRef")
    def proactive_engagement_ref(self) -> "ProactiveEngagementReference":
        '''(experimental) A reference to a ProactiveEngagement resource.

        :stability: experimental
        '''
        return typing.cast("ProactiveEngagementReference", jsii.get(self, "proactiveEngagementRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProactiveEngagementRef).__jsii_proxy_class__ = lambda : _IProactiveEngagementRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_shield.IProtectionGroupRef")
class IProtectionGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProtectionGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="protectionGroupRef")
    def protection_group_ref(self) -> "ProtectionGroupReference":
        '''(experimental) A reference to a ProtectionGroup resource.

        :stability: experimental
        '''
        ...


class _IProtectionGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProtectionGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_shield.IProtectionGroupRef"

    @builtins.property
    @jsii.member(jsii_name="protectionGroupRef")
    def protection_group_ref(self) -> "ProtectionGroupReference":
        '''(experimental) A reference to a ProtectionGroup resource.

        :stability: experimental
        '''
        return typing.cast("ProtectionGroupReference", jsii.get(self, "protectionGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProtectionGroupRef).__jsii_proxy_class__ = lambda : _IProtectionGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_shield.IProtectionRef")
class IProtectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Protection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="protectionRef")
    def protection_ref(self) -> "ProtectionReference":
        '''(experimental) A reference to a Protection resource.

        :stability: experimental
        '''
        ...


class _IProtectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Protection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_shield.IProtectionRef"

    @builtins.property
    @jsii.member(jsii_name="protectionRef")
    def protection_ref(self) -> "ProtectionReference":
        '''(experimental) A reference to a Protection resource.

        :stability: experimental
        '''
        return typing.cast("ProtectionReference", jsii.get(self, "protectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProtectionRef).__jsii_proxy_class__ = lambda : _IProtectionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_shield.ProactiveEngagementReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class ProactiveEngagementReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a ProactiveEngagement resource.

        :param account_id: The AccountId of the ProactiveEngagement resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_shield as interfaces_shield
            
            proactive_engagement_reference = interfaces_shield.ProactiveEngagementReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21e3ebb891870591f9b9a601404eeba0bbdae86deea6f634e8d5139eb6919bdc)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the ProactiveEngagement resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProactiveEngagementReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_shield.ProtectionGroupReference",
    jsii_struct_bases=[],
    name_mapping={"protection_group_arn": "protectionGroupArn"},
)
class ProtectionGroupReference:
    def __init__(self, *, protection_group_arn: builtins.str) -> None:
        '''A reference to a ProtectionGroup resource.

        :param protection_group_arn: The ProtectionGroupArn of the ProtectionGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_shield as interfaces_shield
            
            protection_group_reference = interfaces_shield.ProtectionGroupReference(
                protection_group_arn="protectionGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d2f6c7867abd13c5b07ca40981bf4bb9d2ab2accfc1c0453d6e5c36ac42f95)
            check_type(argname="argument protection_group_arn", value=protection_group_arn, expected_type=type_hints["protection_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protection_group_arn": protection_group_arn,
        }

    @builtins.property
    def protection_group_arn(self) -> builtins.str:
        '''The ProtectionGroupArn of the ProtectionGroup resource.'''
        result = self._values.get("protection_group_arn")
        assert result is not None, "Required property 'protection_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProtectionGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_shield.ProtectionReference",
    jsii_struct_bases=[],
    name_mapping={"protection_arn": "protectionArn"},
)
class ProtectionReference:
    def __init__(self, *, protection_arn: builtins.str) -> None:
        '''A reference to a Protection resource.

        :param protection_arn: The ProtectionArn of the Protection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_shield as interfaces_shield
            
            protection_reference = interfaces_shield.ProtectionReference(
                protection_arn="protectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d82aa4373a567c70356037dfc648acbb0ce1642fc9816eaea93efcf0413edc32)
            check_type(argname="argument protection_arn", value=protection_arn, expected_type=type_hints["protection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "protection_arn": protection_arn,
        }

    @builtins.property
    def protection_arn(self) -> builtins.str:
        '''The ProtectionArn of the Protection resource.'''
        result = self._values.get("protection_arn")
        assert result is not None, "Required property 'protection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProtectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DRTAccessReference",
    "IDRTAccessRef",
    "IProactiveEngagementRef",
    "IProtectionGroupRef",
    "IProtectionRef",
    "ProactiveEngagementReference",
    "ProtectionGroupReference",
    "ProtectionReference",
]

publication.publish()

def _typecheckingstub__3c545dfa10e119e09d934a80388431e03d628ebfb7dfdf25de1ed7a8f359bdab(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21e3ebb891870591f9b9a601404eeba0bbdae86deea6f634e8d5139eb6919bdc(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d2f6c7867abd13c5b07ca40981bf4bb9d2ab2accfc1c0453d6e5c36ac42f95(
    *,
    protection_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d82aa4373a567c70356037dfc648acbb0ce1642fc9816eaea93efcf0413edc32(
    *,
    protection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDRTAccessRef, IProactiveEngagementRef, IProtectionGroupRef, IProtectionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
