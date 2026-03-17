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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_signer.IProfilePermissionRef")
class IProfilePermissionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProfilePermission.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="profilePermissionRef")
    def profile_permission_ref(self) -> "ProfilePermissionReference":
        '''(experimental) A reference to a ProfilePermission resource.

        :stability: experimental
        '''
        ...


class _IProfilePermissionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProfilePermission.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_signer.IProfilePermissionRef"

    @builtins.property
    @jsii.member(jsii_name="profilePermissionRef")
    def profile_permission_ref(self) -> "ProfilePermissionReference":
        '''(experimental) A reference to a ProfilePermission resource.

        :stability: experimental
        '''
        return typing.cast("ProfilePermissionReference", jsii.get(self, "profilePermissionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProfilePermissionRef).__jsii_proxy_class__ = lambda : _IProfilePermissionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_signer.ISigningProfileRef")
class ISigningProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SigningProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="signingProfileRef")
    def signing_profile_ref(self) -> "SigningProfileReference":
        '''(experimental) A reference to a SigningProfile resource.

        :stability: experimental
        '''
        ...


class _ISigningProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SigningProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_signer.ISigningProfileRef"

    @builtins.property
    @jsii.member(jsii_name="signingProfileRef")
    def signing_profile_ref(self) -> "SigningProfileReference":
        '''(experimental) A reference to a SigningProfile resource.

        :stability: experimental
        '''
        return typing.cast("SigningProfileReference", jsii.get(self, "signingProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISigningProfileRef).__jsii_proxy_class__ = lambda : _ISigningProfileRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_signer.ProfilePermissionReference",
    jsii_struct_bases=[],
    name_mapping={"profile_name": "profileName", "statement_id": "statementId"},
)
class ProfilePermissionReference:
    def __init__(
        self,
        *,
        profile_name: builtins.str,
        statement_id: builtins.str,
    ) -> None:
        '''A reference to a ProfilePermission resource.

        :param profile_name: The ProfileName of the ProfilePermission resource.
        :param statement_id: The StatementId of the ProfilePermission resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_signer as interfaces_signer
            
            profile_permission_reference = interfaces_signer.ProfilePermissionReference(
                profile_name="profileName",
                statement_id="statementId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b408623badd1daa0c9bab1c1c66a31c6dde7f44a78b64930391b12ddae517f85)
            check_type(argname="argument profile_name", value=profile_name, expected_type=type_hints["profile_name"])
            check_type(argname="argument statement_id", value=statement_id, expected_type=type_hints["statement_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profile_name": profile_name,
            "statement_id": statement_id,
        }

    @builtins.property
    def profile_name(self) -> builtins.str:
        '''The ProfileName of the ProfilePermission resource.'''
        result = self._values.get("profile_name")
        assert result is not None, "Required property 'profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statement_id(self) -> builtins.str:
        '''The StatementId of the ProfilePermission resource.'''
        result = self._values.get("statement_id")
        assert result is not None, "Required property 'statement_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProfilePermissionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_signer.SigningProfileReference",
    jsii_struct_bases=[],
    name_mapping={"signing_profile_arn": "signingProfileArn"},
)
class SigningProfileReference:
    def __init__(self, *, signing_profile_arn: builtins.str) -> None:
        '''A reference to a SigningProfile resource.

        :param signing_profile_arn: The Arn of the SigningProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_signer as interfaces_signer
            
            signing_profile_reference = interfaces_signer.SigningProfileReference(
                signing_profile_arn="signingProfileArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf7fe5abd2cff30ba0a2b5a91b7d87a7e246390d9d00b650173e6e0eb5f27fab)
            check_type(argname="argument signing_profile_arn", value=signing_profile_arn, expected_type=type_hints["signing_profile_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "signing_profile_arn": signing_profile_arn,
        }

    @builtins.property
    def signing_profile_arn(self) -> builtins.str:
        '''The Arn of the SigningProfile resource.'''
        result = self._values.get("signing_profile_arn")
        assert result is not None, "Required property 'signing_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SigningProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IProfilePermissionRef",
    "ISigningProfileRef",
    "ProfilePermissionReference",
    "SigningProfileReference",
]

publication.publish()

def _typecheckingstub__b408623badd1daa0c9bab1c1c66a31c6dde7f44a78b64930391b12ddae517f85(
    *,
    profile_name: builtins.str,
    statement_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf7fe5abd2cff30ba0a2b5a91b7d87a7e246390d9d00b650173e6e0eb5f27fab(
    *,
    signing_profile_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IProfilePermissionRef, ISigningProfileRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
