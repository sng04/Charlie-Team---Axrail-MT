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
    jsii_type="aws-cdk-lib.interfaces.aws_xray.GroupReference",
    jsii_struct_bases=[],
    name_mapping={"group_arn": "groupArn"},
)
class GroupReference:
    def __init__(self, *, group_arn: builtins.str) -> None:
        '''A reference to a Group resource.

        :param group_arn: The GroupARN of the Group resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_xray as interfaces_xray
            
            group_reference = interfaces_xray.GroupReference(
                group_arn="groupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c277b540ae0e906660c46acb746a05bd99c406b5d0dab26cfc7aa6a969d4a00)
            check_type(argname="argument group_arn", value=group_arn, expected_type=type_hints["group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_arn": group_arn,
        }

    @builtins.property
    def group_arn(self) -> builtins.str:
        '''The GroupARN of the Group resource.'''
        result = self._values.get("group_arn")
        assert result is not None, "Required property 'group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_xray.IGroupRef")
class IGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Group.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="groupRef")
    def group_ref(self) -> "GroupReference":
        '''(experimental) A reference to a Group resource.

        :stability: experimental
        '''
        ...


class _IGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Group.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_xray.IGroupRef"

    @builtins.property
    @jsii.member(jsii_name="groupRef")
    def group_ref(self) -> "GroupReference":
        '''(experimental) A reference to a Group resource.

        :stability: experimental
        '''
        return typing.cast("GroupReference", jsii.get(self, "groupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupRef).__jsii_proxy_class__ = lambda : _IGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_xray.IResourcePolicyRef")
class IResourcePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        ...


class _IResourcePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourcePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_xray.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_xray.ISamplingRuleRef")
class ISamplingRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SamplingRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="samplingRuleRef")
    def sampling_rule_ref(self) -> "SamplingRuleReference":
        '''(experimental) A reference to a SamplingRule resource.

        :stability: experimental
        '''
        ...


class _ISamplingRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SamplingRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_xray.ISamplingRuleRef"

    @builtins.property
    @jsii.member(jsii_name="samplingRuleRef")
    def sampling_rule_ref(self) -> "SamplingRuleReference":
        '''(experimental) A reference to a SamplingRule resource.

        :stability: experimental
        '''
        return typing.cast("SamplingRuleReference", jsii.get(self, "samplingRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISamplingRuleRef).__jsii_proxy_class__ = lambda : _ISamplingRuleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_xray.ITransactionSearchConfigRef"
)
class ITransactionSearchConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TransactionSearchConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="transactionSearchConfigRef")
    def transaction_search_config_ref(self) -> "TransactionSearchConfigReference":
        '''(experimental) A reference to a TransactionSearchConfig resource.

        :stability: experimental
        '''
        ...


class _ITransactionSearchConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TransactionSearchConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_xray.ITransactionSearchConfigRef"

    @builtins.property
    @jsii.member(jsii_name="transactionSearchConfigRef")
    def transaction_search_config_ref(self) -> "TransactionSearchConfigReference":
        '''(experimental) A reference to a TransactionSearchConfig resource.

        :stability: experimental
        '''
        return typing.cast("TransactionSearchConfigReference", jsii.get(self, "transactionSearchConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITransactionSearchConfigRef).__jsii_proxy_class__ = lambda : _ITransactionSearchConfigRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_xray.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_name": "policyName"},
)
class ResourcePolicyReference:
    def __init__(self, *, policy_name: builtins.str) -> None:
        '''A reference to a ResourcePolicy resource.

        :param policy_name: The PolicyName of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_xray as interfaces_xray
            
            resource_policy_reference = interfaces_xray.ResourcePolicyReference(
                policy_name="policyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6db68017a8c8a933208986bd2ac9e71fb490fb0f7c8aa1c3274fe32251c1c1f)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_name": policy_name,
        }

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The PolicyName of the ResourcePolicy resource.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_xray.SamplingRuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class SamplingRuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a SamplingRule resource.

        :param rule_arn: The RuleARN of the SamplingRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_xray as interfaces_xray
            
            sampling_rule_reference = interfaces_xray.SamplingRuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e98ab4fbf5fab19fefaeb048e4f14c0f39ec155f5da9d47fce27c6c338163185)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The RuleARN of the SamplingRule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SamplingRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_xray.TransactionSearchConfigReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class TransactionSearchConfigReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a TransactionSearchConfig resource.

        :param account_id: The AccountId of the TransactionSearchConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_xray as interfaces_xray
            
            transaction_search_config_reference = interfaces_xray.TransactionSearchConfigReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e1e8020cbb38bf1ee4e587d392e5fbaef3b16cd3c0e4689e37c535a09c390f4)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the TransactionSearchConfig resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TransactionSearchConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GroupReference",
    "IGroupRef",
    "IResourcePolicyRef",
    "ISamplingRuleRef",
    "ITransactionSearchConfigRef",
    "ResourcePolicyReference",
    "SamplingRuleReference",
    "TransactionSearchConfigReference",
]

publication.publish()

def _typecheckingstub__1c277b540ae0e906660c46acb746a05bd99c406b5d0dab26cfc7aa6a969d4a00(
    *,
    group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6db68017a8c8a933208986bd2ac9e71fb490fb0f7c8aa1c3274fe32251c1c1f(
    *,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e98ab4fbf5fab19fefaeb048e4f14c0f39ec155f5da9d47fce27c6c338163185(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e1e8020cbb38bf1ee4e587d392e5fbaef3b16cd3c0e4689e37c535a09c390f4(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IGroupRef, IResourcePolicyRef, ISamplingRuleRef, ITransactionSearchConfigRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
