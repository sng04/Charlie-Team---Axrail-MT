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
    jsii_type="aws-cdk-lib.interfaces.aws_mpa.ApprovalTeamReference",
    jsii_struct_bases=[],
    name_mapping={"approval_team_arn": "approvalTeamArn"},
)
class ApprovalTeamReference:
    def __init__(self, *, approval_team_arn: builtins.str) -> None:
        '''A reference to a ApprovalTeam resource.

        :param approval_team_arn: The Arn of the ApprovalTeam resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mpa as interfaces_mpa
            
            approval_team_reference = interfaces_mpa.ApprovalTeamReference(
                approval_team_arn="approvalTeamArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb827691e116abc15c72115b6794a63e52afb6f97d7d3d73b4c9d6f9de8ffe41)
            check_type(argname="argument approval_team_arn", value=approval_team_arn, expected_type=type_hints["approval_team_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "approval_team_arn": approval_team_arn,
        }

    @builtins.property
    def approval_team_arn(self) -> builtins.str:
        '''The Arn of the ApprovalTeam resource.'''
        result = self._values.get("approval_team_arn")
        assert result is not None, "Required property 'approval_team_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApprovalTeamReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mpa.IApprovalTeamRef")
class IApprovalTeamRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApprovalTeam.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="approvalTeamRef")
    def approval_team_ref(self) -> "ApprovalTeamReference":
        '''(experimental) A reference to a ApprovalTeam resource.

        :stability: experimental
        '''
        ...


class _IApprovalTeamRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApprovalTeam.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mpa.IApprovalTeamRef"

    @builtins.property
    @jsii.member(jsii_name="approvalTeamRef")
    def approval_team_ref(self) -> "ApprovalTeamReference":
        '''(experimental) A reference to a ApprovalTeam resource.

        :stability: experimental
        '''
        return typing.cast("ApprovalTeamReference", jsii.get(self, "approvalTeamRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApprovalTeamRef).__jsii_proxy_class__ = lambda : _IApprovalTeamRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mpa.IIdentitySourceRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mpa.IIdentitySourceRef"

    @builtins.property
    @jsii.member(jsii_name="identitySourceRef")
    def identity_source_ref(self) -> "IdentitySourceReference":
        '''(experimental) A reference to a IdentitySource resource.

        :stability: experimental
        '''
        return typing.cast("IdentitySourceReference", jsii.get(self, "identitySourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentitySourceRef).__jsii_proxy_class__ = lambda : _IIdentitySourceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mpa.IdentitySourceReference",
    jsii_struct_bases=[],
    name_mapping={"identity_source_arn": "identitySourceArn"},
)
class IdentitySourceReference:
    def __init__(self, *, identity_source_arn: builtins.str) -> None:
        '''A reference to a IdentitySource resource.

        :param identity_source_arn: The IdentitySourceArn of the IdentitySource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mpa as interfaces_mpa
            
            identity_source_reference = interfaces_mpa.IdentitySourceReference(
                identity_source_arn="identitySourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__123592926dad4bbf6c98d1e1274b2a10c87fde0ca416b42fdb327d8ddcd1812e)
            check_type(argname="argument identity_source_arn", value=identity_source_arn, expected_type=type_hints["identity_source_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_source_arn": identity_source_arn,
        }

    @builtins.property
    def identity_source_arn(self) -> builtins.str:
        '''The IdentitySourceArn of the IdentitySource resource.'''
        result = self._values.get("identity_source_arn")
        assert result is not None, "Required property 'identity_source_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentitySourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApprovalTeamReference",
    "IApprovalTeamRef",
    "IIdentitySourceRef",
    "IdentitySourceReference",
]

publication.publish()

def _typecheckingstub__fb827691e116abc15c72115b6794a63e52afb6f97d7d3d73b4c9d6f9de8ffe41(
    *,
    approval_team_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__123592926dad4bbf6c98d1e1274b2a10c87fde0ca416b42fdb327d8ddcd1812e(
    *,
    identity_source_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApprovalTeamRef, IIdentitySourceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
