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
    jsii_type="aws-cdk-lib.interfaces.aws_route53profiles.IProfileAssociationRef"
)
class IProfileAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProfileAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="profileAssociationRef")
    def profile_association_ref(self) -> "ProfileAssociationReference":
        '''(experimental) A reference to a ProfileAssociation resource.

        :stability: experimental
        '''
        ...


class _IProfileAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProfileAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53profiles.IProfileAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="profileAssociationRef")
    def profile_association_ref(self) -> "ProfileAssociationReference":
        '''(experimental) A reference to a ProfileAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ProfileAssociationReference", jsii.get(self, "profileAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProfileAssociationRef).__jsii_proxy_class__ = lambda : _IProfileAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_route53profiles.IProfileRef")
class IProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Profile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="profileRef")
    def profile_ref(self) -> "ProfileReference":
        '''(experimental) A reference to a Profile resource.

        :stability: experimental
        '''
        ...


class _IProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Profile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53profiles.IProfileRef"

    @builtins.property
    @jsii.member(jsii_name="profileRef")
    def profile_ref(self) -> "ProfileReference":
        '''(experimental) A reference to a Profile resource.

        :stability: experimental
        '''
        return typing.cast("ProfileReference", jsii.get(self, "profileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProfileRef).__jsii_proxy_class__ = lambda : _IProfileRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53profiles.IProfileResourceAssociationRef"
)
class IProfileResourceAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProfileResourceAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="profileResourceAssociationRef")
    def profile_resource_association_ref(self) -> "ProfileResourceAssociationReference":
        '''(experimental) A reference to a ProfileResourceAssociation resource.

        :stability: experimental
        '''
        ...


class _IProfileResourceAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProfileResourceAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53profiles.IProfileResourceAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="profileResourceAssociationRef")
    def profile_resource_association_ref(self) -> "ProfileResourceAssociationReference":
        '''(experimental) A reference to a ProfileResourceAssociation resource.

        :stability: experimental
        '''
        return typing.cast("ProfileResourceAssociationReference", jsii.get(self, "profileResourceAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProfileResourceAssociationRef).__jsii_proxy_class__ = lambda : _IProfileResourceAssociationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53profiles.ProfileAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "profile_association_id": "profileAssociationId",
        "resource_id": "resourceId",
    },
)
class ProfileAssociationReference:
    def __init__(
        self,
        *,
        profile_association_id: builtins.str,
        resource_id: builtins.str,
    ) -> None:
        '''A reference to a ProfileAssociation resource.

        :param profile_association_id: The Id of the ProfileAssociation resource.
        :param resource_id: The ResourceId of the ProfileAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53profiles as interfaces_route53profiles
            
            profile_association_reference = interfaces_route53profiles.ProfileAssociationReference(
                profile_association_id="profileAssociationId",
                resource_id="resourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c14bfb3f68cb45840b17a7bd76e4e892aad98ea5651c00283cc519cc2283f930)
            check_type(argname="argument profile_association_id", value=profile_association_id, expected_type=type_hints["profile_association_id"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profile_association_id": profile_association_id,
            "resource_id": resource_id,
        }

    @builtins.property
    def profile_association_id(self) -> builtins.str:
        '''The Id of the ProfileAssociation resource.'''
        result = self._values.get("profile_association_id")
        assert result is not None, "Required property 'profile_association_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The ResourceId of the ProfileAssociation resource.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProfileAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53profiles.ProfileReference",
    jsii_struct_bases=[],
    name_mapping={"profile_arn": "profileArn", "profile_id": "profileId"},
)
class ProfileReference:
    def __init__(self, *, profile_arn: builtins.str, profile_id: builtins.str) -> None:
        '''A reference to a Profile resource.

        :param profile_arn: The ARN of the Profile resource.
        :param profile_id: The Id of the Profile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53profiles as interfaces_route53profiles
            
            profile_reference = interfaces_route53profiles.ProfileReference(
                profile_arn="profileArn",
                profile_id="profileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__862c9c917fd96a114e9333311140bdc2d9f20e3806a3663e5ba49f5a884ac2e5)
            check_type(argname="argument profile_arn", value=profile_arn, expected_type=type_hints["profile_arn"])
            check_type(argname="argument profile_id", value=profile_id, expected_type=type_hints["profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profile_arn": profile_arn,
            "profile_id": profile_id,
        }

    @builtins.property
    def profile_arn(self) -> builtins.str:
        '''The ARN of the Profile resource.'''
        result = self._values.get("profile_arn")
        assert result is not None, "Required property 'profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_id(self) -> builtins.str:
        '''The Id of the Profile resource.'''
        result = self._values.get("profile_id")
        assert result is not None, "Required property 'profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53profiles.ProfileResourceAssociationReference",
    jsii_struct_bases=[],
    name_mapping={"profile_resource_association_id": "profileResourceAssociationId"},
)
class ProfileResourceAssociationReference:
    def __init__(self, *, profile_resource_association_id: builtins.str) -> None:
        '''A reference to a ProfileResourceAssociation resource.

        :param profile_resource_association_id: The Id of the ProfileResourceAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53profiles as interfaces_route53profiles
            
            profile_resource_association_reference = interfaces_route53profiles.ProfileResourceAssociationReference(
                profile_resource_association_id="profileResourceAssociationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__841fb0a3599d35cd3bb0f27d2574c9e9ea2c11c85d4815a38063f0d9340f6cb6)
            check_type(argname="argument profile_resource_association_id", value=profile_resource_association_id, expected_type=type_hints["profile_resource_association_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profile_resource_association_id": profile_resource_association_id,
        }

    @builtins.property
    def profile_resource_association_id(self) -> builtins.str:
        '''The Id of the ProfileResourceAssociation resource.'''
        result = self._values.get("profile_resource_association_id")
        assert result is not None, "Required property 'profile_resource_association_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProfileResourceAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IProfileAssociationRef",
    "IProfileRef",
    "IProfileResourceAssociationRef",
    "ProfileAssociationReference",
    "ProfileReference",
    "ProfileResourceAssociationReference",
]

publication.publish()

def _typecheckingstub__c14bfb3f68cb45840b17a7bd76e4e892aad98ea5651c00283cc519cc2283f930(
    *,
    profile_association_id: builtins.str,
    resource_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__862c9c917fd96a114e9333311140bdc2d9f20e3806a3663e5ba49f5a884ac2e5(
    *,
    profile_arn: builtins.str,
    profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__841fb0a3599d35cd3bb0f27d2574c9e9ea2c11c85d4815a38063f0d9340f6cb6(
    *,
    profile_resource_association_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IProfileAssociationRef, IProfileRef, IProfileResourceAssociationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
