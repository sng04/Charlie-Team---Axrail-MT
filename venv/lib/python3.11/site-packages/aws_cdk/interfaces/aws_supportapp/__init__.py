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
    jsii_type="aws-cdk-lib.interfaces.aws_supportapp.AccountAliasReference",
    jsii_struct_bases=[],
    name_mapping={"account_alias_resource_id": "accountAliasResourceId"},
)
class AccountAliasReference:
    def __init__(self, *, account_alias_resource_id: builtins.str) -> None:
        '''A reference to a AccountAlias resource.

        :param account_alias_resource_id: The AccountAliasResourceId of the AccountAlias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_supportapp as interfaces_supportapp
            
            account_alias_reference = interfaces_supportapp.AccountAliasReference(
                account_alias_resource_id="accountAliasResourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cbfc73ad02b0cfbbd572dade878ab0cc7dd9fd45df162fe838240830498ae41)
            check_type(argname="argument account_alias_resource_id", value=account_alias_resource_id, expected_type=type_hints["account_alias_resource_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_alias_resource_id": account_alias_resource_id,
        }

    @builtins.property
    def account_alias_resource_id(self) -> builtins.str:
        '''The AccountAliasResourceId of the AccountAlias resource.'''
        result = self._values.get("account_alias_resource_id")
        assert result is not None, "Required property 'account_alias_resource_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccountAliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_supportapp.IAccountAliasRef")
class IAccountAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AccountAlias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accountAliasRef")
    def account_alias_ref(self) -> "AccountAliasReference":
        '''(experimental) A reference to a AccountAlias resource.

        :stability: experimental
        '''
        ...


class _IAccountAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AccountAlias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_supportapp.IAccountAliasRef"

    @builtins.property
    @jsii.member(jsii_name="accountAliasRef")
    def account_alias_ref(self) -> "AccountAliasReference":
        '''(experimental) A reference to a AccountAlias resource.

        :stability: experimental
        '''
        return typing.cast("AccountAliasReference", jsii.get(self, "accountAliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccountAliasRef).__jsii_proxy_class__ = lambda : _IAccountAliasRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_supportapp.ISlackChannelConfigurationRef"
)
class ISlackChannelConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SlackChannelConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="slackChannelConfigurationRef")
    def slack_channel_configuration_ref(self) -> "SlackChannelConfigurationReference":
        '''(experimental) A reference to a SlackChannelConfiguration resource.

        :stability: experimental
        '''
        ...


class _ISlackChannelConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SlackChannelConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_supportapp.ISlackChannelConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="slackChannelConfigurationRef")
    def slack_channel_configuration_ref(self) -> "SlackChannelConfigurationReference":
        '''(experimental) A reference to a SlackChannelConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("SlackChannelConfigurationReference", jsii.get(self, "slackChannelConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISlackChannelConfigurationRef).__jsii_proxy_class__ = lambda : _ISlackChannelConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_supportapp.ISlackWorkspaceConfigurationRef"
)
class ISlackWorkspaceConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SlackWorkspaceConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="slackWorkspaceConfigurationRef")
    def slack_workspace_configuration_ref(
        self,
    ) -> "SlackWorkspaceConfigurationReference":
        '''(experimental) A reference to a SlackWorkspaceConfiguration resource.

        :stability: experimental
        '''
        ...


class _ISlackWorkspaceConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SlackWorkspaceConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_supportapp.ISlackWorkspaceConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="slackWorkspaceConfigurationRef")
    def slack_workspace_configuration_ref(
        self,
    ) -> "SlackWorkspaceConfigurationReference":
        '''(experimental) A reference to a SlackWorkspaceConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("SlackWorkspaceConfigurationReference", jsii.get(self, "slackWorkspaceConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISlackWorkspaceConfigurationRef).__jsii_proxy_class__ = lambda : _ISlackWorkspaceConfigurationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_supportapp.SlackChannelConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"channel_id": "channelId", "team_id": "teamId"},
)
class SlackChannelConfigurationReference:
    def __init__(self, *, channel_id: builtins.str, team_id: builtins.str) -> None:
        '''A reference to a SlackChannelConfiguration resource.

        :param channel_id: The ChannelId of the SlackChannelConfiguration resource.
        :param team_id: The TeamId of the SlackChannelConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_supportapp as interfaces_supportapp
            
            slack_channel_configuration_reference = interfaces_supportapp.SlackChannelConfigurationReference(
                channel_id="channelId",
                team_id="teamId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e11716b41ce775987ee786a99354fa1bf2262378e41747b3c3d74d34d8e69e1d)
            check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_id": channel_id,
            "team_id": team_id,
        }

    @builtins.property
    def channel_id(self) -> builtins.str:
        '''The ChannelId of the SlackChannelConfiguration resource.'''
        result = self._values.get("channel_id")
        assert result is not None, "Required property 'channel_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def team_id(self) -> builtins.str:
        '''The TeamId of the SlackChannelConfiguration resource.'''
        result = self._values.get("team_id")
        assert result is not None, "Required property 'team_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SlackChannelConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_supportapp.SlackWorkspaceConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"team_id": "teamId"},
)
class SlackWorkspaceConfigurationReference:
    def __init__(self, *, team_id: builtins.str) -> None:
        '''A reference to a SlackWorkspaceConfiguration resource.

        :param team_id: The TeamId of the SlackWorkspaceConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_supportapp as interfaces_supportapp
            
            slack_workspace_configuration_reference = interfaces_supportapp.SlackWorkspaceConfigurationReference(
                team_id="teamId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a4a00a40fa7ba351842c19f70c6a2bc11715a667c30ed25e62c63ea25d6599)
            check_type(argname="argument team_id", value=team_id, expected_type=type_hints["team_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "team_id": team_id,
        }

    @builtins.property
    def team_id(self) -> builtins.str:
        '''The TeamId of the SlackWorkspaceConfiguration resource.'''
        result = self._values.get("team_id")
        assert result is not None, "Required property 'team_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SlackWorkspaceConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccountAliasReference",
    "IAccountAliasRef",
    "ISlackChannelConfigurationRef",
    "ISlackWorkspaceConfigurationRef",
    "SlackChannelConfigurationReference",
    "SlackWorkspaceConfigurationReference",
]

publication.publish()

def _typecheckingstub__3cbfc73ad02b0cfbbd572dade878ab0cc7dd9fd45df162fe838240830498ae41(
    *,
    account_alias_resource_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e11716b41ce775987ee786a99354fa1bf2262378e41747b3c3d74d34d8e69e1d(
    *,
    channel_id: builtins.str,
    team_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a4a00a40fa7ba351842c19f70c6a2bc11715a667c30ed25e62c63ea25d6599(
    *,
    team_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccountAliasRef, ISlackChannelConfigurationRef, ISlackWorkspaceConfigurationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
