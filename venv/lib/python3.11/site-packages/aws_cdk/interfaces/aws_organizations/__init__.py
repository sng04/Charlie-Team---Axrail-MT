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
    jsii_type="aws-cdk-lib.interfaces.aws_organizations.AccountReference",
    jsii_struct_bases=[],
    name_mapping={"account_arn": "accountArn", "account_id": "accountId"},
)
class AccountReference:
    def __init__(self, *, account_arn: builtins.str, account_id: builtins.str) -> None:
        '''A reference to a Account resource.

        :param account_arn: The ARN of the Account resource.
        :param account_id: The AccountId of the Account resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_organizations as interfaces_organizations
            
            account_reference = interfaces_organizations.AccountReference(
                account_arn="accountArn",
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd6b8fa65f3c4580e07ac4d2231df3887b7b6560242fe51b3a0156ecd77cce5c)
            check_type(argname="argument account_arn", value=account_arn, expected_type=type_hints["account_arn"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_arn": account_arn,
            "account_id": account_id,
        }

    @builtins.property
    def account_arn(self) -> builtins.str:
        '''The ARN of the Account resource.'''
        result = self._values.get("account_arn")
        assert result is not None, "Required property 'account_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the Account resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_organizations.IAccountRef")
class IAccountRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Account.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accountRef")
    def account_ref(self) -> "AccountReference":
        '''(experimental) A reference to a Account resource.

        :stability: experimental
        '''
        ...


class _IAccountRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Account.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_organizations.IAccountRef"

    @builtins.property
    @jsii.member(jsii_name="accountRef")
    def account_ref(self) -> "AccountReference":
        '''(experimental) A reference to a Account resource.

        :stability: experimental
        '''
        return typing.cast("AccountReference", jsii.get(self, "accountRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccountRef).__jsii_proxy_class__ = lambda : _IAccountRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_organizations.IOrganizationRef")
class IOrganizationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Organization.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationRef")
    def organization_ref(self) -> "OrganizationReference":
        '''(experimental) A reference to a Organization resource.

        :stability: experimental
        '''
        ...


class _IOrganizationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Organization.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_organizations.IOrganizationRef"

    @builtins.property
    @jsii.member(jsii_name="organizationRef")
    def organization_ref(self) -> "OrganizationReference":
        '''(experimental) A reference to a Organization resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationReference", jsii.get(self, "organizationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationRef).__jsii_proxy_class__ = lambda : _IOrganizationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_organizations.IOrganizationalUnitRef"
)
class IOrganizationalUnitRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationalUnit.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitRef")
    def organizational_unit_ref(self) -> "OrganizationalUnitReference":
        '''(experimental) A reference to a OrganizationalUnit resource.

        :stability: experimental
        '''
        ...


class _IOrganizationalUnitRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OrganizationalUnit.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_organizations.IOrganizationalUnitRef"

    @builtins.property
    @jsii.member(jsii_name="organizationalUnitRef")
    def organizational_unit_ref(self) -> "OrganizationalUnitReference":
        '''(experimental) A reference to a OrganizationalUnit resource.

        :stability: experimental
        '''
        return typing.cast("OrganizationalUnitReference", jsii.get(self, "organizationalUnitRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOrganizationalUnitRef).__jsii_proxy_class__ = lambda : _IOrganizationalUnitRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_organizations.IPolicyRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_organizations.IPolicyRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_organizations.IResourcePolicyRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_organizations.IResourcePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="resourcePolicyRef")
    def resource_policy_ref(self) -> "ResourcePolicyReference":
        '''(experimental) A reference to a ResourcePolicy resource.

        :stability: experimental
        '''
        return typing.cast("ResourcePolicyReference", jsii.get(self, "resourcePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourcePolicyRef).__jsii_proxy_class__ = lambda : _IResourcePolicyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_organizations.OrganizationReference",
    jsii_struct_bases=[],
    name_mapping={
        "organization_arn": "organizationArn",
        "organization_id": "organizationId",
    },
)
class OrganizationReference:
    def __init__(
        self,
        *,
        organization_arn: builtins.str,
        organization_id: builtins.str,
    ) -> None:
        '''A reference to a Organization resource.

        :param organization_arn: The ARN of the Organization resource.
        :param organization_id: The Id of the Organization resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_organizations as interfaces_organizations
            
            organization_reference = interfaces_organizations.OrganizationReference(
                organization_arn="organizationArn",
                organization_id="organizationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89608f5e8332dfc5999c43181436b80fbc3bacb4fac5fd4d600ddc71652d0b75)
            check_type(argname="argument organization_arn", value=organization_arn, expected_type=type_hints["organization_arn"])
            check_type(argname="argument organization_id", value=organization_id, expected_type=type_hints["organization_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "organization_arn": organization_arn,
            "organization_id": organization_id,
        }

    @builtins.property
    def organization_arn(self) -> builtins.str:
        '''The ARN of the Organization resource.'''
        result = self._values.get("organization_arn")
        assert result is not None, "Required property 'organization_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization_id(self) -> builtins.str:
        '''The Id of the Organization resource.'''
        result = self._values.get("organization_id")
        assert result is not None, "Required property 'organization_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_organizations.OrganizationalUnitReference",
    jsii_struct_bases=[],
    name_mapping={
        "organizational_unit_arn": "organizationalUnitArn",
        "organizational_unit_id": "organizationalUnitId",
    },
)
class OrganizationalUnitReference:
    def __init__(
        self,
        *,
        organizational_unit_arn: builtins.str,
        organizational_unit_id: builtins.str,
    ) -> None:
        '''A reference to a OrganizationalUnit resource.

        :param organizational_unit_arn: The ARN of the OrganizationalUnit resource.
        :param organizational_unit_id: The Id of the OrganizationalUnit resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_organizations as interfaces_organizations
            
            organizational_unit_reference = interfaces_organizations.OrganizationalUnitReference(
                organizational_unit_arn="organizationalUnitArn",
                organizational_unit_id="organizationalUnitId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f9f2db731c8c3a89089e777e67f0a7af1e9fc441ee36d7250cd2178c34553d7)
            check_type(argname="argument organizational_unit_arn", value=organizational_unit_arn, expected_type=type_hints["organizational_unit_arn"])
            check_type(argname="argument organizational_unit_id", value=organizational_unit_id, expected_type=type_hints["organizational_unit_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "organizational_unit_arn": organizational_unit_arn,
            "organizational_unit_id": organizational_unit_id,
        }

    @builtins.property
    def organizational_unit_arn(self) -> builtins.str:
        '''The ARN of the OrganizationalUnit resource.'''
        result = self._values.get("organizational_unit_arn")
        assert result is not None, "Required property 'organizational_unit_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organizational_unit_id(self) -> builtins.str:
        '''The Id of the OrganizationalUnit resource.'''
        result = self._values.get("organizational_unit_id")
        assert result is not None, "Required property 'organizational_unit_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrganizationalUnitReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_organizations.PolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_arn": "policyArn", "policy_id": "policyId"},
)
class PolicyReference:
    def __init__(self, *, policy_arn: builtins.str, policy_id: builtins.str) -> None:
        '''A reference to a Policy resource.

        :param policy_arn: The ARN of the Policy resource.
        :param policy_id: The Id of the Policy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_organizations as interfaces_organizations
            
            policy_reference = interfaces_organizations.PolicyReference(
                policy_arn="policyArn",
                policy_id="policyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b9a32cc5bbc4489223ecc11644e600a5b7ee7a1c950c929a863f306aa504f98)
            check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_arn": policy_arn,
            "policy_id": policy_id,
        }

    @builtins.property
    def policy_arn(self) -> builtins.str:
        '''The ARN of the Policy resource.'''
        result = self._values.get("policy_arn")
        assert result is not None, "Required property 'policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_id(self) -> builtins.str:
        '''The Id of the Policy resource.'''
        result = self._values.get("policy_id")
        assert result is not None, "Required property 'policy_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_organizations.ResourcePolicyReference",
    jsii_struct_bases=[],
    name_mapping={
        "resource_policy_arn": "resourcePolicyArn",
        "resource_policy_id": "resourcePolicyId",
    },
)
class ResourcePolicyReference:
    def __init__(
        self,
        *,
        resource_policy_arn: builtins.str,
        resource_policy_id: builtins.str,
    ) -> None:
        '''A reference to a ResourcePolicy resource.

        :param resource_policy_arn: The ARN of the ResourcePolicy resource.
        :param resource_policy_id: The Id of the ResourcePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_organizations as interfaces_organizations
            
            resource_policy_reference = interfaces_organizations.ResourcePolicyReference(
                resource_policy_arn="resourcePolicyArn",
                resource_policy_id="resourcePolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abbe13c83cac6f9dbb616b66a4475fa9c68a4cf2432f4cf832f68c9a1f2abb62)
            check_type(argname="argument resource_policy_arn", value=resource_policy_arn, expected_type=type_hints["resource_policy_arn"])
            check_type(argname="argument resource_policy_id", value=resource_policy_id, expected_type=type_hints["resource_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_policy_arn": resource_policy_arn,
            "resource_policy_id": resource_policy_id,
        }

    @builtins.property
    def resource_policy_arn(self) -> builtins.str:
        '''The ARN of the ResourcePolicy resource.'''
        result = self._values.get("resource_policy_arn")
        assert result is not None, "Required property 'resource_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_policy_id(self) -> builtins.str:
        '''The Id of the ResourcePolicy resource.'''
        result = self._values.get("resource_policy_id")
        assert result is not None, "Required property 'resource_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourcePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccountReference",
    "IAccountRef",
    "IOrganizationRef",
    "IOrganizationalUnitRef",
    "IPolicyRef",
    "IResourcePolicyRef",
    "OrganizationReference",
    "OrganizationalUnitReference",
    "PolicyReference",
    "ResourcePolicyReference",
]

publication.publish()

def _typecheckingstub__bd6b8fa65f3c4580e07ac4d2231df3887b7b6560242fe51b3a0156ecd77cce5c(
    *,
    account_arn: builtins.str,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89608f5e8332dfc5999c43181436b80fbc3bacb4fac5fd4d600ddc71652d0b75(
    *,
    organization_arn: builtins.str,
    organization_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f9f2db731c8c3a89089e777e67f0a7af1e9fc441ee36d7250cd2178c34553d7(
    *,
    organizational_unit_arn: builtins.str,
    organizational_unit_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9a32cc5bbc4489223ecc11644e600a5b7ee7a1c950c929a863f306aa504f98(
    *,
    policy_arn: builtins.str,
    policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abbe13c83cac6f9dbb616b66a4475fa9c68a4cf2432f4cf832f68c9a1f2abb62(
    *,
    resource_policy_arn: builtins.str,
    resource_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccountRef, IOrganizationRef, IOrganizationalUnitRef, IPolicyRef, IResourcePolicyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
