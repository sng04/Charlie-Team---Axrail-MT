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
    jsii_type="aws-cdk-lib.interfaces.aws_verifiedpermissions.IIdentitySourceRef"
)
class IIdentitySourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdentitySource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="identitySourceRef")
    def identity_source_ref(self) -> "IdentitySourceReference":
        '''(experimental) A reference to a IdentitySource resource.

        :stability: experimental
        '''
        ...


class _IIdentitySourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdentitySource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_verifiedpermissions.IIdentitySourceRef"

    @builtins.property
    @jsii.member(jsii_name="identitySourceRef")
    def identity_source_ref(self) -> "IdentitySourceReference":
        '''(experimental) A reference to a IdentitySource resource.

        :stability: experimental
        '''
        return typing.cast("IdentitySourceReference", jsii.get(self, "identitySourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentitySourceRef).__jsii_proxy_class__ = lambda : _IIdentitySourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_verifiedpermissions.IPolicyRef")
class IPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Policy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="policyRef")
    def policy_ref(self) -> "PolicyReference":
        '''(experimental) A reference to a Policy resource.

        :stability: experimental
        '''
        ...


class _IPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Policy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_verifiedpermissions.IPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="policyRef")
    def policy_ref(self) -> "PolicyReference":
        '''(experimental) A reference to a Policy resource.

        :stability: experimental
        '''
        return typing.cast("PolicyReference", jsii.get(self, "policyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyRef).__jsii_proxy_class__ = lambda : _IPolicyRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_verifiedpermissions.IPolicyStoreRef"
)
class IPolicyStoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyStore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="policyStoreRef")
    def policy_store_ref(self) -> "PolicyStoreReference":
        '''(experimental) A reference to a PolicyStore resource.

        :stability: experimental
        '''
        ...


class _IPolicyStoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyStore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_verifiedpermissions.IPolicyStoreRef"

    @builtins.property
    @jsii.member(jsii_name="policyStoreRef")
    def policy_store_ref(self) -> "PolicyStoreReference":
        '''(experimental) A reference to a PolicyStore resource.

        :stability: experimental
        '''
        return typing.cast("PolicyStoreReference", jsii.get(self, "policyStoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyStoreRef).__jsii_proxy_class__ = lambda : _IPolicyStoreRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_verifiedpermissions.IPolicyTemplateRef"
)
class IPolicyTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="policyTemplateRef")
    def policy_template_ref(self) -> "PolicyTemplateReference":
        '''(experimental) A reference to a PolicyTemplate resource.

        :stability: experimental
        '''
        ...


class _IPolicyTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PolicyTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_verifiedpermissions.IPolicyTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="policyTemplateRef")
    def policy_template_ref(self) -> "PolicyTemplateReference":
        '''(experimental) A reference to a PolicyTemplate resource.

        :stability: experimental
        '''
        return typing.cast("PolicyTemplateReference", jsii.get(self, "policyTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyTemplateRef).__jsii_proxy_class__ = lambda : _IPolicyTemplateRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_verifiedpermissions.IdentitySourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "identity_source_id": "identitySourceId",
        "policy_store_id": "policyStoreId",
    },
)
class IdentitySourceReference:
    def __init__(
        self,
        *,
        identity_source_id: builtins.str,
        policy_store_id: builtins.str,
    ) -> None:
        '''A reference to a IdentitySource resource.

        :param identity_source_id: The IdentitySourceId of the IdentitySource resource.
        :param policy_store_id: The PolicyStoreId of the IdentitySource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_verifiedpermissions as interfaces_verifiedpermissions
            
            identity_source_reference = interfaces_verifiedpermissions.IdentitySourceReference(
                identity_source_id="identitySourceId",
                policy_store_id="policyStoreId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6a67a3160dab101c31f8f18416473cfed8992943cb03475cec2e7087f8a3c7a)
            check_type(argname="argument identity_source_id", value=identity_source_id, expected_type=type_hints["identity_source_id"])
            check_type(argname="argument policy_store_id", value=policy_store_id, expected_type=type_hints["policy_store_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_source_id": identity_source_id,
            "policy_store_id": policy_store_id,
        }

    @builtins.property
    def identity_source_id(self) -> builtins.str:
        '''The IdentitySourceId of the IdentitySource resource.'''
        result = self._values.get("identity_source_id")
        assert result is not None, "Required property 'identity_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_store_id(self) -> builtins.str:
        '''The PolicyStoreId of the IdentitySource resource.'''
        result = self._values.get("policy_store_id")
        assert result is not None, "Required property 'policy_store_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentitySourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_verifiedpermissions.PolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_id": "policyId", "policy_store_id": "policyStoreId"},
)
class PolicyReference:
    def __init__(
        self,
        *,
        policy_id: builtins.str,
        policy_store_id: builtins.str,
    ) -> None:
        '''A reference to a Policy resource.

        :param policy_id: The PolicyId of the Policy resource.
        :param policy_store_id: The PolicyStoreId of the Policy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_verifiedpermissions as interfaces_verifiedpermissions
            
            policy_reference = interfaces_verifiedpermissions.PolicyReference(
                policy_id="policyId",
                policy_store_id="policyStoreId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd88b46fd9f517ec78a02f82d07146189c4b425becf99cd859c0f39ca4cbd6b5)
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
            check_type(argname="argument policy_store_id", value=policy_store_id, expected_type=type_hints["policy_store_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_id": policy_id,
            "policy_store_id": policy_store_id,
        }

    @builtins.property
    def policy_id(self) -> builtins.str:
        '''The PolicyId of the Policy resource.'''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_store_id(self) -> builtins.str:
        '''The PolicyStoreId of the Policy resource.'''
        result = self._values.get("policy_store_id")
        assert result is not None, "Required property 'policy_store_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_verifiedpermissions.PolicyStoreReference",
    jsii_struct_bases=[],
    name_mapping={
        "policy_store_arn": "policyStoreArn",
        "policy_store_id": "policyStoreId",
    },
)
class PolicyStoreReference:
    def __init__(
        self,
        *,
        policy_store_arn: builtins.str,
        policy_store_id: builtins.str,
    ) -> None:
        '''A reference to a PolicyStore resource.

        :param policy_store_arn: The ARN of the PolicyStore resource.
        :param policy_store_id: The PolicyStoreId of the PolicyStore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_verifiedpermissions as interfaces_verifiedpermissions
            
            policy_store_reference = interfaces_verifiedpermissions.PolicyStoreReference(
                policy_store_arn="policyStoreArn",
                policy_store_id="policyStoreId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0ab09d050895f8245a50aa20d70e6b1e44a4969307ed3206e87ef0e591e7142)
            check_type(argname="argument policy_store_arn", value=policy_store_arn, expected_type=type_hints["policy_store_arn"])
            check_type(argname="argument policy_store_id", value=policy_store_id, expected_type=type_hints["policy_store_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_store_arn": policy_store_arn,
            "policy_store_id": policy_store_id,
        }

    @builtins.property
    def policy_store_arn(self) -> builtins.str:
        '''The ARN of the PolicyStore resource.'''
        result = self._values.get("policy_store_arn")
        assert result is not None, "Required property 'policy_store_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_store_id(self) -> builtins.str:
        '''The PolicyStoreId of the PolicyStore resource.'''
        result = self._values.get("policy_store_id")
        assert result is not None, "Required property 'policy_store_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyStoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_verifiedpermissions.PolicyTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "policy_store_id": "policyStoreId",
        "policy_template_id": "policyTemplateId",
    },
)
class PolicyTemplateReference:
    def __init__(
        self,
        *,
        policy_store_id: builtins.str,
        policy_template_id: builtins.str,
    ) -> None:
        '''A reference to a PolicyTemplate resource.

        :param policy_store_id: The PolicyStoreId of the PolicyTemplate resource.
        :param policy_template_id: The PolicyTemplateId of the PolicyTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_verifiedpermissions as interfaces_verifiedpermissions
            
            policy_template_reference = interfaces_verifiedpermissions.PolicyTemplateReference(
                policy_store_id="policyStoreId",
                policy_template_id="policyTemplateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d203176b01786ac1ce3e258885a0ac0d5e52f4964f225414a30b2099fe0e1797)
            check_type(argname="argument policy_store_id", value=policy_store_id, expected_type=type_hints["policy_store_id"])
            check_type(argname="argument policy_template_id", value=policy_template_id, expected_type=type_hints["policy_template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_store_id": policy_store_id,
            "policy_template_id": policy_template_id,
        }

    @builtins.property
    def policy_store_id(self) -> builtins.str:
        '''The PolicyStoreId of the PolicyTemplate resource.'''
        result = self._values.get("policy_store_id")
        assert result is not None, "Required property 'policy_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_template_id(self) -> builtins.str:
        '''The PolicyTemplateId of the PolicyTemplate resource.'''
        result = self._values.get("policy_template_id")
        assert result is not None, "Required property 'policy_template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PolicyTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IIdentitySourceRef",
    "IPolicyRef",
    "IPolicyStoreRef",
    "IPolicyTemplateRef",
    "IdentitySourceReference",
    "PolicyReference",
    "PolicyStoreReference",
    "PolicyTemplateReference",
]

publication.publish()

def _typecheckingstub__a6a67a3160dab101c31f8f18416473cfed8992943cb03475cec2e7087f8a3c7a(
    *,
    identity_source_id: builtins.str,
    policy_store_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd88b46fd9f517ec78a02f82d07146189c4b425becf99cd859c0f39ca4cbd6b5(
    *,
    policy_id: builtins.str,
    policy_store_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0ab09d050895f8245a50aa20d70e6b1e44a4969307ed3206e87ef0e591e7142(
    *,
    policy_store_arn: builtins.str,
    policy_store_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d203176b01786ac1ce3e258885a0ac0d5e52f4964f225414a30b2099fe0e1797(
    *,
    policy_store_id: builtins.str,
    policy_template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IIdentitySourceRef, IPolicyRef, IPolicyStoreRef, IPolicyTemplateRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
