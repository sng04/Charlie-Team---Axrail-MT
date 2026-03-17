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
    jsii_type="aws-cdk-lib.interfaces.aws_identitystore.GroupMembershipReference",
    jsii_struct_bases=[],
    name_mapping={
        "identity_store_id": "identityStoreId",
        "membership_id": "membershipId",
    },
)
class GroupMembershipReference:
    def __init__(
        self,
        *,
        identity_store_id: builtins.str,
        membership_id: builtins.str,
    ) -> None:
        '''A reference to a GroupMembership resource.

        :param identity_store_id: The IdentityStoreId of the GroupMembership resource.
        :param membership_id: The MembershipId of the GroupMembership resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_identitystore as interfaces_identitystore
            
            group_membership_reference = interfaces_identitystore.GroupMembershipReference(
                identity_store_id="identityStoreId",
                membership_id="membershipId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ad67e884f84d186fa1812d68d8a77bb789c9d47e5eb0bbecfb0242fab3663ad)
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
            check_type(argname="argument membership_id", value=membership_id, expected_type=type_hints["membership_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_store_id": identity_store_id,
            "membership_id": membership_id,
        }

    @builtins.property
    def identity_store_id(self) -> builtins.str:
        '''The IdentityStoreId of the GroupMembership resource.'''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def membership_id(self) -> builtins.str:
        '''The MembershipId of the GroupMembership resource.'''
        result = self._values.get("membership_id")
        assert result is not None, "Required property 'membership_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupMembershipReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_identitystore.GroupReference",
    jsii_struct_bases=[],
    name_mapping={"group_id": "groupId", "identity_store_id": "identityStoreId"},
)
class GroupReference:
    def __init__(
        self,
        *,
        group_id: builtins.str,
        identity_store_id: builtins.str,
    ) -> None:
        '''A reference to a Group resource.

        :param group_id: The GroupId of the Group resource.
        :param identity_store_id: The IdentityStoreId of the Group resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_identitystore as interfaces_identitystore
            
            group_reference = interfaces_identitystore.GroupReference(
                group_id="groupId",
                identity_store_id="identityStoreId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80be5f97f6bbfe0c4f7499ffab050d76a52ab1f353eb507a8cf57c3a7ec0c030)
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
            check_type(argname="argument identity_store_id", value=identity_store_id, expected_type=type_hints["identity_store_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_id": group_id,
            "identity_store_id": identity_store_id,
        }

    @builtins.property
    def group_id(self) -> builtins.str:
        '''The GroupId of the Group resource.'''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_store_id(self) -> builtins.str:
        '''The IdentityStoreId of the Group resource.'''
        result = self._values.get("identity_store_id")
        assert result is not None, "Required property 'identity_store_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_identitystore.IGroupMembershipRef"
)
class IGroupMembershipRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GroupMembership.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="groupMembershipRef")
    def group_membership_ref(self) -> "GroupMembershipReference":
        '''(experimental) A reference to a GroupMembership resource.

        :stability: experimental
        '''
        ...


class _IGroupMembershipRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GroupMembership.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_identitystore.IGroupMembershipRef"

    @builtins.property
    @jsii.member(jsii_name="groupMembershipRef")
    def group_membership_ref(self) -> "GroupMembershipReference":
        '''(experimental) A reference to a GroupMembership resource.

        :stability: experimental
        '''
        return typing.cast("GroupMembershipReference", jsii.get(self, "groupMembershipRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupMembershipRef).__jsii_proxy_class__ = lambda : _IGroupMembershipRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_identitystore.IGroupRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_identitystore.IGroupRef"

    @builtins.property
    @jsii.member(jsii_name="groupRef")
    def group_ref(self) -> "GroupReference":
        '''(experimental) A reference to a Group resource.

        :stability: experimental
        '''
        return typing.cast("GroupReference", jsii.get(self, "groupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupRef).__jsii_proxy_class__ = lambda : _IGroupRefProxy


__all__ = [
    "GroupMembershipReference",
    "GroupReference",
    "IGroupMembershipRef",
    "IGroupRef",
]

publication.publish()

def _typecheckingstub__2ad67e884f84d186fa1812d68d8a77bb789c9d47e5eb0bbecfb0242fab3663ad(
    *,
    identity_store_id: builtins.str,
    membership_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80be5f97f6bbfe0c4f7499ffab050d76a52ab1f353eb507a8cf57c3a7ec0c030(
    *,
    group_id: builtins.str,
    identity_store_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IGroupMembershipRef, IGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
