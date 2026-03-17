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
    jsii_type="aws-cdk-lib.interfaces.aws_rolesanywhere.CRLReference",
    jsii_struct_bases=[],
    name_mapping={"crl_id": "crlId"},
)
class CRLReference:
    def __init__(self, *, crl_id: builtins.str) -> None:
        '''A reference to a CRL resource.

        :param crl_id: The CrlId of the CRL resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rolesanywhere as interfaces_rolesanywhere
            
            c_rLReference = interfaces_rolesanywhere.CRLReference(
                crl_id="crlId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__916ec2d2aae5ecd1575ceef844e6bfb54c8909e4505f26fc504bb20a36638078)
            check_type(argname="argument crl_id", value=crl_id, expected_type=type_hints["crl_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "crl_id": crl_id,
        }

    @builtins.property
    def crl_id(self) -> builtins.str:
        '''The CrlId of the CRL resource.'''
        result = self._values.get("crl_id")
        assert result is not None, "Required property 'crl_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CRLReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rolesanywhere.ICRLRef")
class ICRLRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CRL.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="crlRef")
    def crl_ref(self) -> "CRLReference":
        '''(experimental) A reference to a CRL resource.

        :stability: experimental
        '''
        ...


class _ICRLRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CRL.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rolesanywhere.ICRLRef"

    @builtins.property
    @jsii.member(jsii_name="crlRef")
    def crl_ref(self) -> "CRLReference":
        '''(experimental) A reference to a CRL resource.

        :stability: experimental
        '''
        return typing.cast("CRLReference", jsii.get(self, "crlRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICRLRef).__jsii_proxy_class__ = lambda : _ICRLRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rolesanywhere.IProfileRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rolesanywhere.IProfileRef"

    @builtins.property
    @jsii.member(jsii_name="profileRef")
    def profile_ref(self) -> "ProfileReference":
        '''(experimental) A reference to a Profile resource.

        :stability: experimental
        '''
        return typing.cast("ProfileReference", jsii.get(self, "profileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProfileRef).__jsii_proxy_class__ = lambda : _IProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_rolesanywhere.ITrustAnchorRef")
class ITrustAnchorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TrustAnchor.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="trustAnchorRef")
    def trust_anchor_ref(self) -> "TrustAnchorReference":
        '''(experimental) A reference to a TrustAnchor resource.

        :stability: experimental
        '''
        ...


class _ITrustAnchorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TrustAnchor.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_rolesanywhere.ITrustAnchorRef"

    @builtins.property
    @jsii.member(jsii_name="trustAnchorRef")
    def trust_anchor_ref(self) -> "TrustAnchorReference":
        '''(experimental) A reference to a TrustAnchor resource.

        :stability: experimental
        '''
        return typing.cast("TrustAnchorReference", jsii.get(self, "trustAnchorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITrustAnchorRef).__jsii_proxy_class__ = lambda : _ITrustAnchorRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_rolesanywhere.ProfileReference",
    jsii_struct_bases=[],
    name_mapping={"profile_arn": "profileArn", "profile_id": "profileId"},
)
class ProfileReference:
    def __init__(self, *, profile_arn: builtins.str, profile_id: builtins.str) -> None:
        '''A reference to a Profile resource.

        :param profile_arn: The ARN of the Profile resource.
        :param profile_id: The ProfileId of the Profile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rolesanywhere as interfaces_rolesanywhere
            
            profile_reference = interfaces_rolesanywhere.ProfileReference(
                profile_arn="profileArn",
                profile_id="profileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ca44262455fa0fcdcf355663380e4b88f61ee6a7c456ed6594ecfc33f16c5da)
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
        '''The ProfileId of the Profile resource.'''
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
    jsii_type="aws-cdk-lib.interfaces.aws_rolesanywhere.TrustAnchorReference",
    jsii_struct_bases=[],
    name_mapping={
        "trust_anchor_arn": "trustAnchorArn",
        "trust_anchor_id": "trustAnchorId",
    },
)
class TrustAnchorReference:
    def __init__(
        self,
        *,
        trust_anchor_arn: builtins.str,
        trust_anchor_id: builtins.str,
    ) -> None:
        '''A reference to a TrustAnchor resource.

        :param trust_anchor_arn: The ARN of the TrustAnchor resource.
        :param trust_anchor_id: The TrustAnchorId of the TrustAnchor resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_rolesanywhere as interfaces_rolesanywhere
            
            trust_anchor_reference = interfaces_rolesanywhere.TrustAnchorReference(
                trust_anchor_arn="trustAnchorArn",
                trust_anchor_id="trustAnchorId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__219d4bcadedca24e22886d453073aaa28b70678fe7cefdfdc821bb719ffb99e0)
            check_type(argname="argument trust_anchor_arn", value=trust_anchor_arn, expected_type=type_hints["trust_anchor_arn"])
            check_type(argname="argument trust_anchor_id", value=trust_anchor_id, expected_type=type_hints["trust_anchor_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trust_anchor_arn": trust_anchor_arn,
            "trust_anchor_id": trust_anchor_id,
        }

    @builtins.property
    def trust_anchor_arn(self) -> builtins.str:
        '''The ARN of the TrustAnchor resource.'''
        result = self._values.get("trust_anchor_arn")
        assert result is not None, "Required property 'trust_anchor_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trust_anchor_id(self) -> builtins.str:
        '''The TrustAnchorId of the TrustAnchor resource.'''
        result = self._values.get("trust_anchor_id")
        assert result is not None, "Required property 'trust_anchor_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrustAnchorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CRLReference",
    "ICRLRef",
    "IProfileRef",
    "ITrustAnchorRef",
    "ProfileReference",
    "TrustAnchorReference",
]

publication.publish()

def _typecheckingstub__916ec2d2aae5ecd1575ceef844e6bfb54c8909e4505f26fc504bb20a36638078(
    *,
    crl_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ca44262455fa0fcdcf355663380e4b88f61ee6a7c456ed6594ecfc33f16c5da(
    *,
    profile_arn: builtins.str,
    profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__219d4bcadedca24e22886d453073aaa28b70678fe7cefdfdc821bb719ffb99e0(
    *,
    trust_anchor_arn: builtins.str,
    trust_anchor_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICRLRef, IProfileRef, ITrustAnchorRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
