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
    jsii_type="aws-cdk-lib.interfaces.aws_iam.AccessKeyReference",
    jsii_struct_bases=[],
    name_mapping={"access_key_id": "accessKeyId"},
)
class AccessKeyReference:
    def __init__(self, *, access_key_id: builtins.str) -> None:
        '''A reference to a AccessKey resource.

        :param access_key_id: The Id of the AccessKey resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            access_key_reference = interfaces_iam.AccessKeyReference(
                access_key_id="accessKeyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fdf978f313644fc2895c99a1a87de980e5c5ff112c8f959a8d3a00d764056d6)
            check_type(argname="argument access_key_id", value=access_key_id, expected_type=type_hints["access_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_key_id": access_key_id,
        }

    @builtins.property
    def access_key_id(self) -> builtins.str:
        '''The Id of the AccessKey resource.'''
        result = self._values.get("access_key_id")
        assert result is not None, "Required property 'access_key_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessKeyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.GroupPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"group_name": "groupName", "policy_name": "policyName"},
)
class GroupPolicyReference:
    def __init__(self, *, group_name: builtins.str, policy_name: builtins.str) -> None:
        '''A reference to a GroupPolicy resource.

        :param group_name: The GroupName of the GroupPolicy resource.
        :param policy_name: The PolicyName of the GroupPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            group_policy_reference = interfaces_iam.GroupPolicyReference(
                group_name="groupName",
                policy_name="policyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a92e2164c75bf6bcfba84804dfd379fe7ae5bbacff8cfb251fa4518fecbd9e3)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name": group_name,
            "policy_name": policy_name,
        }

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The GroupName of the GroupPolicy resource.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The PolicyName of the GroupPolicy resource.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.GroupReference",
    jsii_struct_bases=[],
    name_mapping={"group_arn": "groupArn", "group_name": "groupName"},
)
class GroupReference:
    def __init__(self, *, group_arn: builtins.str, group_name: builtins.str) -> None:
        '''A reference to a Group resource.

        :param group_arn: The ARN of the Group resource.
        :param group_name: The GroupName of the Group resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            group_reference = interfaces_iam.GroupReference(
                group_arn="groupArn",
                group_name="groupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48c8635b06f4f7a207b37033ec5b2f54d63a6bd398917fd397f0d89e84491b56)
            check_type(argname="argument group_arn", value=group_arn, expected_type=type_hints["group_arn"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_arn": group_arn,
            "group_name": group_name,
        }

    @builtins.property
    def group_arn(self) -> builtins.str:
        '''The ARN of the Group resource.'''
        result = self._values.get("group_arn")
        assert result is not None, "Required property 'group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The GroupName of the Group resource.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IAccessKeyRef")
class IAccessKeyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccessKey.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessKeyRef")
    def access_key_ref(self) -> "AccessKeyReference":
        '''(experimental) A reference to a AccessKey resource.

        :stability: experimental
        '''
        ...


class _IAccessKeyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccessKey.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IAccessKeyRef"

    @builtins.property
    @jsii.member(jsii_name="accessKeyRef")
    def access_key_ref(self) -> "AccessKeyReference":
        '''(experimental) A reference to a AccessKey resource.

        :stability: experimental
        '''
        return typing.cast("AccessKeyReference", jsii.get(self, "accessKeyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessKeyRef).__jsii_proxy_class__ = lambda : _IAccessKeyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IGroupPolicyRef")
class IGroupPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GroupPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="groupPolicyRef")
    def group_policy_ref(self) -> "GroupPolicyReference":
        '''(experimental) A reference to a GroupPolicy resource.

        :stability: experimental
        '''
        ...


class _IGroupPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GroupPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IGroupPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="groupPolicyRef")
    def group_policy_ref(self) -> "GroupPolicyReference":
        '''(experimental) A reference to a GroupPolicy resource.

        :stability: experimental
        '''
        return typing.cast("GroupPolicyReference", jsii.get(self, "groupPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupPolicyRef).__jsii_proxy_class__ = lambda : _IGroupPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IGroupRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IGroupRef"

    @builtins.property
    @jsii.member(jsii_name="groupRef")
    def group_ref(self) -> "GroupReference":
        '''(experimental) A reference to a Group resource.

        :stability: experimental
        '''
        return typing.cast("GroupReference", jsii.get(self, "groupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupRef).__jsii_proxy_class__ = lambda : _IGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IInstanceProfileRef")
class IInstanceProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceProfileRef")
    def instance_profile_ref(self) -> "InstanceProfileReference":
        '''(experimental) A reference to a InstanceProfile resource.

        :stability: experimental
        '''
        ...


class _IInstanceProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IInstanceProfileRef"

    @builtins.property
    @jsii.member(jsii_name="instanceProfileRef")
    def instance_profile_ref(self) -> "InstanceProfileReference":
        '''(experimental) A reference to a InstanceProfile resource.

        :stability: experimental
        '''
        return typing.cast("InstanceProfileReference", jsii.get(self, "instanceProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceProfileRef).__jsii_proxy_class__ = lambda : _IInstanceProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IManagedPolicyRef")
class IManagedPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ManagedPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="managedPolicyRef")
    def managed_policy_ref(self) -> "ManagedPolicyReference":
        '''(experimental) A reference to a ManagedPolicy resource.

        :stability: experimental
        '''
        ...


class _IManagedPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ManagedPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IManagedPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="managedPolicyRef")
    def managed_policy_ref(self) -> "ManagedPolicyReference":
        '''(experimental) A reference to a ManagedPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ManagedPolicyReference", jsii.get(self, "managedPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IManagedPolicyRef).__jsii_proxy_class__ = lambda : _IManagedPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IOIDCProviderRef")
class IOIDCProviderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OIDCProvider.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="oidcProviderRef")
    def oidc_provider_ref(self) -> "OIDCProviderReference":
        '''(experimental) A reference to a OIDCProvider resource.

        :stability: experimental
        '''
        ...


class _IOIDCProviderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OIDCProvider.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IOIDCProviderRef"

    @builtins.property
    @jsii.member(jsii_name="oidcProviderRef")
    def oidc_provider_ref(self) -> "OIDCProviderReference":
        '''(experimental) A reference to a OIDCProvider resource.

        :stability: experimental
        '''
        return typing.cast("OIDCProviderReference", jsii.get(self, "oidcProviderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOIDCProviderRef).__jsii_proxy_class__ = lambda : _IOIDCProviderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IPolicyRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="policyRef")
    def policy_ref(self) -> "PolicyReference":
        '''(experimental) A reference to a Policy resource.

        :stability: experimental
        '''
        return typing.cast("PolicyReference", jsii.get(self, "policyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPolicyRef).__jsii_proxy_class__ = lambda : _IPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IRolePolicyRef")
class IRolePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RolePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="rolePolicyRef")
    def role_policy_ref(self) -> "RolePolicyReference":
        '''(experimental) A reference to a RolePolicy resource.

        :stability: experimental
        '''
        ...


class _IRolePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RolePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IRolePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="rolePolicyRef")
    def role_policy_ref(self) -> "RolePolicyReference":
        '''(experimental) A reference to a RolePolicy resource.

        :stability: experimental
        '''
        return typing.cast("RolePolicyReference", jsii.get(self, "rolePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRolePolicyRef).__jsii_proxy_class__ = lambda : _IRolePolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IRoleRef")
class IRoleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Role.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="roleRef")
    def role_ref(self) -> "RoleReference":
        '''(experimental) A reference to a Role resource.

        :stability: experimental
        '''
        ...


class _IRoleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Role.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IRoleRef"

    @builtins.property
    @jsii.member(jsii_name="roleRef")
    def role_ref(self) -> "RoleReference":
        '''(experimental) A reference to a Role resource.

        :stability: experimental
        '''
        return typing.cast("RoleReference", jsii.get(self, "roleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRoleRef).__jsii_proxy_class__ = lambda : _IRoleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.ISAMLProviderRef")
class ISAMLProviderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SAMLProvider.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="samlProviderRef")
    def saml_provider_ref(self) -> "SAMLProviderReference":
        '''(experimental) A reference to a SAMLProvider resource.

        :stability: experimental
        '''
        ...


class _ISAMLProviderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SAMLProvider.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.ISAMLProviderRef"

    @builtins.property
    @jsii.member(jsii_name="samlProviderRef")
    def saml_provider_ref(self) -> "SAMLProviderReference":
        '''(experimental) A reference to a SAMLProvider resource.

        :stability: experimental
        '''
        return typing.cast("SAMLProviderReference", jsii.get(self, "samlProviderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISAMLProviderRef).__jsii_proxy_class__ = lambda : _ISAMLProviderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IServerCertificateRef")
class IServerCertificateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServerCertificate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serverCertificateRef")
    def server_certificate_ref(self) -> "ServerCertificateReference":
        '''(experimental) A reference to a ServerCertificate resource.

        :stability: experimental
        '''
        ...


class _IServerCertificateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServerCertificate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IServerCertificateRef"

    @builtins.property
    @jsii.member(jsii_name="serverCertificateRef")
    def server_certificate_ref(self) -> "ServerCertificateReference":
        '''(experimental) A reference to a ServerCertificate resource.

        :stability: experimental
        '''
        return typing.cast("ServerCertificateReference", jsii.get(self, "serverCertificateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServerCertificateRef).__jsii_proxy_class__ = lambda : _IServerCertificateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IServiceLinkedRoleRef")
class IServiceLinkedRoleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceLinkedRole.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceLinkedRoleRef")
    def service_linked_role_ref(self) -> "ServiceLinkedRoleReference":
        '''(experimental) A reference to a ServiceLinkedRole resource.

        :stability: experimental
        '''
        ...


class _IServiceLinkedRoleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceLinkedRole.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IServiceLinkedRoleRef"

    @builtins.property
    @jsii.member(jsii_name="serviceLinkedRoleRef")
    def service_linked_role_ref(self) -> "ServiceLinkedRoleReference":
        '''(experimental) A reference to a ServiceLinkedRole resource.

        :stability: experimental
        '''
        return typing.cast("ServiceLinkedRoleReference", jsii.get(self, "serviceLinkedRoleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceLinkedRoleRef).__jsii_proxy_class__ = lambda : _IServiceLinkedRoleRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IUserPolicyRef")
class IUserPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userPolicyRef")
    def user_policy_ref(self) -> "UserPolicyReference":
        '''(experimental) A reference to a UserPolicy resource.

        :stability: experimental
        '''
        ...


class _IUserPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IUserPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="userPolicyRef")
    def user_policy_ref(self) -> "UserPolicyReference":
        '''(experimental) A reference to a UserPolicy resource.

        :stability: experimental
        '''
        return typing.cast("UserPolicyReference", jsii.get(self, "userPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserPolicyRef).__jsii_proxy_class__ = lambda : _IUserPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IUserRef")
class IUserRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a User.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userRef")
    def user_ref(self) -> "UserReference":
        '''(experimental) A reference to a User resource.

        :stability: experimental
        '''
        ...


class _IUserRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a User.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IUserRef"

    @builtins.property
    @jsii.member(jsii_name="userRef")
    def user_ref(self) -> "UserReference":
        '''(experimental) A reference to a User resource.

        :stability: experimental
        '''
        return typing.cast("UserReference", jsii.get(self, "userRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserRef).__jsii_proxy_class__ = lambda : _IUserRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IUserToGroupAdditionRef")
class IUserToGroupAdditionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserToGroupAddition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userToGroupAdditionRef")
    def user_to_group_addition_ref(self) -> "UserToGroupAdditionReference":
        '''(experimental) A reference to a UserToGroupAddition resource.

        :stability: experimental
        '''
        ...


class _IUserToGroupAdditionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserToGroupAddition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IUserToGroupAdditionRef"

    @builtins.property
    @jsii.member(jsii_name="userToGroupAdditionRef")
    def user_to_group_addition_ref(self) -> "UserToGroupAdditionReference":
        '''(experimental) A reference to a UserToGroupAddition resource.

        :stability: experimental
        '''
        return typing.cast("UserToGroupAdditionReference", jsii.get(self, "userToGroupAdditionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserToGroupAdditionRef).__jsii_proxy_class__ = lambda : _IUserToGroupAdditionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iam.IVirtualMFADeviceRef")
class IVirtualMFADeviceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualMFADevice.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="virtualMfaDeviceRef")
    def virtual_mfa_device_ref(self) -> "VirtualMFADeviceReference":
        '''(experimental) A reference to a VirtualMFADevice resource.

        :stability: experimental
        '''
        ...


class _IVirtualMFADeviceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VirtualMFADevice.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iam.IVirtualMFADeviceRef"

    @builtins.property
    @jsii.member(jsii_name="virtualMfaDeviceRef")
    def virtual_mfa_device_ref(self) -> "VirtualMFADeviceReference":
        '''(experimental) A reference to a VirtualMFADevice resource.

        :stability: experimental
        '''
        return typing.cast("VirtualMFADeviceReference", jsii.get(self, "virtualMfaDeviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVirtualMFADeviceRef).__jsii_proxy_class__ = lambda : _IVirtualMFADeviceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.InstanceProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "instance_profile_arn": "instanceProfileArn",
        "instance_profile_name": "instanceProfileName",
    },
)
class InstanceProfileReference:
    def __init__(
        self,
        *,
        instance_profile_arn: builtins.str,
        instance_profile_name: builtins.str,
    ) -> None:
        '''A reference to a InstanceProfile resource.

        :param instance_profile_arn: The ARN of the InstanceProfile resource.
        :param instance_profile_name: The InstanceProfileName of the InstanceProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            instance_profile_reference = interfaces_iam.InstanceProfileReference(
                instance_profile_arn="instanceProfileArn",
                instance_profile_name="instanceProfileName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e278c65645b8f47fd7ab3d7f254a6f4ac872019a1d58d6cd116d14aebb6c382)
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
            check_type(argname="argument instance_profile_name", value=instance_profile_name, expected_type=type_hints["instance_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_profile_arn": instance_profile_arn,
            "instance_profile_name": instance_profile_name,
        }

    @builtins.property
    def instance_profile_arn(self) -> builtins.str:
        '''The ARN of the InstanceProfile resource.'''
        result = self._values.get("instance_profile_arn")
        assert result is not None, "Required property 'instance_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_profile_name(self) -> builtins.str:
        '''The InstanceProfileName of the InstanceProfile resource.'''
        result = self._values.get("instance_profile_name")
        assert result is not None, "Required property 'instance_profile_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.ManagedPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_arn": "policyArn"},
)
class ManagedPolicyReference:
    def __init__(self, *, policy_arn: builtins.str) -> None:
        '''A reference to a ManagedPolicy resource.

        :param policy_arn: The PolicyArn of the ManagedPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            managed_policy_reference = interfaces_iam.ManagedPolicyReference(
                policy_arn="policyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5ede49b7b72dccd002b041b171ec9cb172ace16b07ccc90a21255cbcb1e760e)
            check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_arn": policy_arn,
        }

    @builtins.property
    def policy_arn(self) -> builtins.str:
        '''The PolicyArn of the ManagedPolicy resource.'''
        result = self._values.get("policy_arn")
        assert result is not None, "Required property 'policy_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.OIDCProviderReference",
    jsii_struct_bases=[],
    name_mapping={"oidc_provider_arn": "oidcProviderArn"},
)
class OIDCProviderReference:
    def __init__(self, *, oidc_provider_arn: builtins.str) -> None:
        '''A reference to a OIDCProvider resource.

        :param oidc_provider_arn: The Arn of the OIDCProvider resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            o_iDCProvider_reference = interfaces_iam.OIDCProviderReference(
                oidc_provider_arn="oidcProviderArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fdcd0c708983fab5326e867388d77dc6bcf3d79a19cd0bc79f0f69e83bbcc8c)
            check_type(argname="argument oidc_provider_arn", value=oidc_provider_arn, expected_type=type_hints["oidc_provider_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "oidc_provider_arn": oidc_provider_arn,
        }

    @builtins.property
    def oidc_provider_arn(self) -> builtins.str:
        '''The Arn of the OIDCProvider resource.'''
        result = self._values.get("oidc_provider_arn")
        assert result is not None, "Required property 'oidc_provider_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OIDCProviderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.PolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_id": "policyId"},
)
class PolicyReference:
    def __init__(self, *, policy_id: builtins.str) -> None:
        '''A reference to a Policy resource.

        :param policy_id: The Id of the Policy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            policy_reference = interfaces_iam.PolicyReference(
                policy_id="policyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b1927f9850fdf1b98b3abd6fed75aa0b487e2270ee89d7d5991ea4f89e74a56)
            check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_id": policy_id,
        }

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
    jsii_type="aws-cdk-lib.interfaces.aws_iam.RolePolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_name": "policyName", "role_name": "roleName"},
)
class RolePolicyReference:
    def __init__(self, *, policy_name: builtins.str, role_name: builtins.str) -> None:
        '''A reference to a RolePolicy resource.

        :param policy_name: The PolicyName of the RolePolicy resource.
        :param role_name: The RoleName of the RolePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            role_policy_reference = interfaces_iam.RolePolicyReference(
                policy_name="policyName",
                role_name="roleName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92a77912e091d2e0f4bb1ad8633d3018aa38cf6213036728f95381f487c8cee0)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_name": policy_name,
            "role_name": role_name,
        }

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The PolicyName of the RolePolicy resource.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_name(self) -> builtins.str:
        '''The RoleName of the RolePolicy resource.'''
        result = self._values.get("role_name")
        assert result is not None, "Required property 'role_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RolePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.RoleReference",
    jsii_struct_bases=[],
    name_mapping={"role_arn": "roleArn", "role_name": "roleName"},
)
class RoleReference:
    def __init__(self, *, role_arn: builtins.str, role_name: builtins.str) -> None:
        '''A reference to a Role resource.

        :param role_arn: The ARN of the Role resource.
        :param role_name: The RoleName of the Role resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            role_reference = interfaces_iam.RoleReference(
                role_arn="roleArn",
                role_name="roleName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4780c9aede30855235614eeb6da66db193c83a1f04685e3fa06e35bae882342b)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
            "role_name": role_name,
        }

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The ARN of the Role resource.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_name(self) -> builtins.str:
        '''The RoleName of the Role resource.'''
        result = self._values.get("role_name")
        assert result is not None, "Required property 'role_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.SAMLProviderReference",
    jsii_struct_bases=[],
    name_mapping={"saml_provider_arn": "samlProviderArn"},
)
class SAMLProviderReference:
    def __init__(self, *, saml_provider_arn: builtins.str) -> None:
        '''A reference to a SAMLProvider resource.

        :param saml_provider_arn: The Arn of the SAMLProvider resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            s_aMLProvider_reference = interfaces_iam.SAMLProviderReference(
                saml_provider_arn="samlProviderArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d012d2ab10f0ab78f39627eb6bdc0c97b1f1342ca2fd51e11d63cfc59e3b3d86)
            check_type(argname="argument saml_provider_arn", value=saml_provider_arn, expected_type=type_hints["saml_provider_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "saml_provider_arn": saml_provider_arn,
        }

    @builtins.property
    def saml_provider_arn(self) -> builtins.str:
        '''The Arn of the SAMLProvider resource.'''
        result = self._values.get("saml_provider_arn")
        assert result is not None, "Required property 'saml_provider_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SAMLProviderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.ServerCertificateReference",
    jsii_struct_bases=[],
    name_mapping={
        "server_certificate_arn": "serverCertificateArn",
        "server_certificate_name": "serverCertificateName",
    },
)
class ServerCertificateReference:
    def __init__(
        self,
        *,
        server_certificate_arn: builtins.str,
        server_certificate_name: builtins.str,
    ) -> None:
        '''A reference to a ServerCertificate resource.

        :param server_certificate_arn: The ARN of the ServerCertificate resource.
        :param server_certificate_name: The ServerCertificateName of the ServerCertificate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            server_certificate_reference = interfaces_iam.ServerCertificateReference(
                server_certificate_arn="serverCertificateArn",
                server_certificate_name="serverCertificateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9632d820af333095fd417c185685286fd7db0c977eb8eea44a8209ae8f3f9fc)
            check_type(argname="argument server_certificate_arn", value=server_certificate_arn, expected_type=type_hints["server_certificate_arn"])
            check_type(argname="argument server_certificate_name", value=server_certificate_name, expected_type=type_hints["server_certificate_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "server_certificate_arn": server_certificate_arn,
            "server_certificate_name": server_certificate_name,
        }

    @builtins.property
    def server_certificate_arn(self) -> builtins.str:
        '''The ARN of the ServerCertificate resource.'''
        result = self._values.get("server_certificate_arn")
        assert result is not None, "Required property 'server_certificate_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_certificate_name(self) -> builtins.str:
        '''The ServerCertificateName of the ServerCertificate resource.'''
        result = self._values.get("server_certificate_name")
        assert result is not None, "Required property 'server_certificate_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerCertificateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.ServiceLinkedRoleReference",
    jsii_struct_bases=[],
    name_mapping={"role_name": "roleName"},
)
class ServiceLinkedRoleReference:
    def __init__(self, *, role_name: builtins.str) -> None:
        '''A reference to a ServiceLinkedRole resource.

        :param role_name: The RoleName of the ServiceLinkedRole resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            service_linked_role_reference = interfaces_iam.ServiceLinkedRoleReference(
                role_name="roleName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0aa119a901d7a9697858a5ced3b58046a1e27cff84f716e2f86013f941bf7a09)
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_name": role_name,
        }

    @builtins.property
    def role_name(self) -> builtins.str:
        '''The RoleName of the ServiceLinkedRole resource.'''
        result = self._values.get("role_name")
        assert result is not None, "Required property 'role_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceLinkedRoleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.UserPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"policy_name": "policyName", "user_name": "userName"},
)
class UserPolicyReference:
    def __init__(self, *, policy_name: builtins.str, user_name: builtins.str) -> None:
        '''A reference to a UserPolicy resource.

        :param policy_name: The PolicyName of the UserPolicy resource.
        :param user_name: The UserName of the UserPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            user_policy_reference = interfaces_iam.UserPolicyReference(
                policy_name="policyName",
                user_name="userName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cab5a96542e550e4b334265e989b83972253ea21d0828d076d7c4b0ccb745e5)
            check_type(argname="argument policy_name", value=policy_name, expected_type=type_hints["policy_name"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy_name": policy_name,
            "user_name": user_name,
        }

    @builtins.property
    def policy_name(self) -> builtins.str:
        '''The PolicyName of the UserPolicy resource.'''
        result = self._values.get("policy_name")
        assert result is not None, "Required property 'policy_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The UserName of the UserPolicy resource.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.UserReference",
    jsii_struct_bases=[],
    name_mapping={"user_arn": "userArn", "user_name": "userName"},
)
class UserReference:
    def __init__(self, *, user_arn: builtins.str, user_name: builtins.str) -> None:
        '''A reference to a User resource.

        :param user_arn: The ARN of the User resource.
        :param user_name: The UserName of the User resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            user_reference = interfaces_iam.UserReference(
                user_arn="userArn",
                user_name="userName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fad3b9b7a23c350b5548423788a9bef4f969359516c6348af88289a88db1dde9)
            check_type(argname="argument user_arn", value=user_arn, expected_type=type_hints["user_arn"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_arn": user_arn,
            "user_name": user_name,
        }

    @builtins.property
    def user_arn(self) -> builtins.str:
        '''The ARN of the User resource.'''
        result = self._values.get("user_arn")
        assert result is not None, "Required property 'user_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The UserName of the User resource.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.UserToGroupAdditionReference",
    jsii_struct_bases=[],
    name_mapping={"user_to_group_addition_id": "userToGroupAdditionId"},
)
class UserToGroupAdditionReference:
    def __init__(self, *, user_to_group_addition_id: builtins.str) -> None:
        '''A reference to a UserToGroupAddition resource.

        :param user_to_group_addition_id: The Id of the UserToGroupAddition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            user_to_group_addition_reference = interfaces_iam.UserToGroupAdditionReference(
                user_to_group_addition_id="userToGroupAdditionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14666140aa4ecbff94af7251b3f36479108da56c1e3c695b9a978c2102d4d6cd)
            check_type(argname="argument user_to_group_addition_id", value=user_to_group_addition_id, expected_type=type_hints["user_to_group_addition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_to_group_addition_id": user_to_group_addition_id,
        }

    @builtins.property
    def user_to_group_addition_id(self) -> builtins.str:
        '''The Id of the UserToGroupAddition resource.'''
        result = self._values.get("user_to_group_addition_id")
        assert result is not None, "Required property 'user_to_group_addition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserToGroupAdditionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_iam.VirtualMFADeviceReference",
    jsii_struct_bases=[],
    name_mapping={"serial_number": "serialNumber"},
)
class VirtualMFADeviceReference:
    def __init__(self, *, serial_number: builtins.str) -> None:
        '''A reference to a VirtualMFADevice resource.

        :param serial_number: The SerialNumber of the VirtualMFADevice resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iam as interfaces_iam
            
            virtual_mFADevice_reference = interfaces_iam.VirtualMFADeviceReference(
                serial_number="serialNumber"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15d8382904decd1526f54845e59f8f82ecf72689c0d49dff56ad55e42cfe314b)
            check_type(argname="argument serial_number", value=serial_number, expected_type=type_hints["serial_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "serial_number": serial_number,
        }

    @builtins.property
    def serial_number(self) -> builtins.str:
        '''The SerialNumber of the VirtualMFADevice resource.'''
        result = self._values.get("serial_number")
        assert result is not None, "Required property 'serial_number' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VirtualMFADeviceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessKeyReference",
    "GroupPolicyReference",
    "GroupReference",
    "IAccessKeyRef",
    "IGroupPolicyRef",
    "IGroupRef",
    "IInstanceProfileRef",
    "IManagedPolicyRef",
    "IOIDCProviderRef",
    "IPolicyRef",
    "IRolePolicyRef",
    "IRoleRef",
    "ISAMLProviderRef",
    "IServerCertificateRef",
    "IServiceLinkedRoleRef",
    "IUserPolicyRef",
    "IUserRef",
    "IUserToGroupAdditionRef",
    "IVirtualMFADeviceRef",
    "InstanceProfileReference",
    "ManagedPolicyReference",
    "OIDCProviderReference",
    "PolicyReference",
    "RolePolicyReference",
    "RoleReference",
    "SAMLProviderReference",
    "ServerCertificateReference",
    "ServiceLinkedRoleReference",
    "UserPolicyReference",
    "UserReference",
    "UserToGroupAdditionReference",
    "VirtualMFADeviceReference",
]

publication.publish()

def _typecheckingstub__1fdf978f313644fc2895c99a1a87de980e5c5ff112c8f959a8d3a00d764056d6(
    *,
    access_key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a92e2164c75bf6bcfba84804dfd379fe7ae5bbacff8cfb251fa4518fecbd9e3(
    *,
    group_name: builtins.str,
    policy_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48c8635b06f4f7a207b37033ec5b2f54d63a6bd398917fd397f0d89e84491b56(
    *,
    group_arn: builtins.str,
    group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e278c65645b8f47fd7ab3d7f254a6f4ac872019a1d58d6cd116d14aebb6c382(
    *,
    instance_profile_arn: builtins.str,
    instance_profile_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5ede49b7b72dccd002b041b171ec9cb172ace16b07ccc90a21255cbcb1e760e(
    *,
    policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fdcd0c708983fab5326e867388d77dc6bcf3d79a19cd0bc79f0f69e83bbcc8c(
    *,
    oidc_provider_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b1927f9850fdf1b98b3abd6fed75aa0b487e2270ee89d7d5991ea4f89e74a56(
    *,
    policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a77912e091d2e0f4bb1ad8633d3018aa38cf6213036728f95381f487c8cee0(
    *,
    policy_name: builtins.str,
    role_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4780c9aede30855235614eeb6da66db193c83a1f04685e3fa06e35bae882342b(
    *,
    role_arn: builtins.str,
    role_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d012d2ab10f0ab78f39627eb6bdc0c97b1f1342ca2fd51e11d63cfc59e3b3d86(
    *,
    saml_provider_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9632d820af333095fd417c185685286fd7db0c977eb8eea44a8209ae8f3f9fc(
    *,
    server_certificate_arn: builtins.str,
    server_certificate_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0aa119a901d7a9697858a5ced3b58046a1e27cff84f716e2f86013f941bf7a09(
    *,
    role_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cab5a96542e550e4b334265e989b83972253ea21d0828d076d7c4b0ccb745e5(
    *,
    policy_name: builtins.str,
    user_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fad3b9b7a23c350b5548423788a9bef4f969359516c6348af88289a88db1dde9(
    *,
    user_arn: builtins.str,
    user_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14666140aa4ecbff94af7251b3f36479108da56c1e3c695b9a978c2102d4d6cd(
    *,
    user_to_group_addition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15d8382904decd1526f54845e59f8f82ecf72689c0d49dff56ad55e42cfe314b(
    *,
    serial_number: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessKeyRef, IGroupPolicyRef, IGroupRef, IInstanceProfileRef, IManagedPolicyRef, IOIDCProviderRef, IPolicyRef, IRolePolicyRef, IRoleRef, ISAMLProviderRef, IServerCertificateRef, IServiceLinkedRoleRef, IUserPolicyRef, IUserRef, IUserToGroupAdditionRef, IVirtualMFADeviceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
