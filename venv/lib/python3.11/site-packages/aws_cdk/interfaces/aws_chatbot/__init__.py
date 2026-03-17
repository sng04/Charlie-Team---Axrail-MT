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
    jsii_type="aws-cdk-lib.interfaces.aws_chatbot.CustomActionReference",
    jsii_struct_bases=[],
    name_mapping={"custom_action_arn": "customActionArn"},
)
class CustomActionReference:
    def __init__(self, *, custom_action_arn: builtins.str) -> None:
        '''A reference to a CustomAction resource.

        :param custom_action_arn: The CustomActionArn of the CustomAction resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chatbot as interfaces_chatbot
            
            custom_action_reference = interfaces_chatbot.CustomActionReference(
                custom_action_arn="customActionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fb90d4fa48d9894f917d57846d278eba7ea1e6bfd3bfd59b16908a4f85c1307)
            check_type(argname="argument custom_action_arn", value=custom_action_arn, expected_type=type_hints["custom_action_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_action_arn": custom_action_arn,
        }

    @builtins.property
    def custom_action_arn(self) -> builtins.str:
        '''The CustomActionArn of the CustomAction resource.'''
        result = self._values.get("custom_action_arn")
        assert result is not None, "Required property 'custom_action_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomActionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_chatbot.ICustomActionRef")
class ICustomActionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomAction.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customActionRef")
    def custom_action_ref(self) -> "CustomActionReference":
        '''(experimental) A reference to a CustomAction resource.

        :stability: experimental
        '''
        ...


class _ICustomActionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomAction.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chatbot.ICustomActionRef"

    @builtins.property
    @jsii.member(jsii_name="customActionRef")
    def custom_action_ref(self) -> "CustomActionReference":
        '''(experimental) A reference to a CustomAction resource.

        :stability: experimental
        '''
        return typing.cast("CustomActionReference", jsii.get(self, "customActionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomActionRef).__jsii_proxy_class__ = lambda : _ICustomActionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_chatbot.IMicrosoftTeamsChannelConfigurationRef"
)
class IMicrosoftTeamsChannelConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MicrosoftTeamsChannelConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="microsoftTeamsChannelConfigurationRef")
    def microsoft_teams_channel_configuration_ref(
        self,
    ) -> "MicrosoftTeamsChannelConfigurationReference":
        '''(experimental) A reference to a MicrosoftTeamsChannelConfiguration resource.

        :stability: experimental
        '''
        ...


class _IMicrosoftTeamsChannelConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MicrosoftTeamsChannelConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chatbot.IMicrosoftTeamsChannelConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="microsoftTeamsChannelConfigurationRef")
    def microsoft_teams_channel_configuration_ref(
        self,
    ) -> "MicrosoftTeamsChannelConfigurationReference":
        '''(experimental) A reference to a MicrosoftTeamsChannelConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("MicrosoftTeamsChannelConfigurationReference", jsii.get(self, "microsoftTeamsChannelConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMicrosoftTeamsChannelConfigurationRef).__jsii_proxy_class__ = lambda : _IMicrosoftTeamsChannelConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_chatbot.ISlackChannelConfigurationRef"
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_chatbot.ISlackChannelConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="slackChannelConfigurationRef")
    def slack_channel_configuration_ref(self) -> "SlackChannelConfigurationReference":
        '''(experimental) A reference to a SlackChannelConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("SlackChannelConfigurationReference", jsii.get(self, "slackChannelConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISlackChannelConfigurationRef).__jsii_proxy_class__ = lambda : _ISlackChannelConfigurationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chatbot.MicrosoftTeamsChannelConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "microsoft_teams_channel_configuration_arn": "microsoftTeamsChannelConfigurationArn",
    },
)
class MicrosoftTeamsChannelConfigurationReference:
    def __init__(
        self,
        *,
        microsoft_teams_channel_configuration_arn: builtins.str,
    ) -> None:
        '''A reference to a MicrosoftTeamsChannelConfiguration resource.

        :param microsoft_teams_channel_configuration_arn: The Arn of the MicrosoftTeamsChannelConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chatbot as interfaces_chatbot
            
            microsoft_teams_channel_configuration_reference = interfaces_chatbot.MicrosoftTeamsChannelConfigurationReference(
                microsoft_teams_channel_configuration_arn="microsoftTeamsChannelConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f3d28b11300d54dce65640e5e1bc1fd14d4e67a6351d040492c48666baf809d)
            check_type(argname="argument microsoft_teams_channel_configuration_arn", value=microsoft_teams_channel_configuration_arn, expected_type=type_hints["microsoft_teams_channel_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "microsoft_teams_channel_configuration_arn": microsoft_teams_channel_configuration_arn,
        }

    @builtins.property
    def microsoft_teams_channel_configuration_arn(self) -> builtins.str:
        '''The Arn of the MicrosoftTeamsChannelConfiguration resource.'''
        result = self._values.get("microsoft_teams_channel_configuration_arn")
        assert result is not None, "Required property 'microsoft_teams_channel_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MicrosoftTeamsChannelConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_chatbot.SlackChannelConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"slack_channel_configuration_arn": "slackChannelConfigurationArn"},
)
class SlackChannelConfigurationReference:
    def __init__(self, *, slack_channel_configuration_arn: builtins.str) -> None:
        '''A reference to a SlackChannelConfiguration resource.

        :param slack_channel_configuration_arn: The Arn of the SlackChannelConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_chatbot as interfaces_chatbot
            
            slack_channel_configuration_reference = interfaces_chatbot.SlackChannelConfigurationReference(
                slack_channel_configuration_arn="slackChannelConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d3c2972c2b588e2114bbc9a1c4896bdbc0f6f708168fee57c58fc9caca79de8)
            check_type(argname="argument slack_channel_configuration_arn", value=slack_channel_configuration_arn, expected_type=type_hints["slack_channel_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "slack_channel_configuration_arn": slack_channel_configuration_arn,
        }

    @builtins.property
    def slack_channel_configuration_arn(self) -> builtins.str:
        '''The Arn of the SlackChannelConfiguration resource.'''
        result = self._values.get("slack_channel_configuration_arn")
        assert result is not None, "Required property 'slack_channel_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SlackChannelConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CustomActionReference",
    "ICustomActionRef",
    "IMicrosoftTeamsChannelConfigurationRef",
    "ISlackChannelConfigurationRef",
    "MicrosoftTeamsChannelConfigurationReference",
    "SlackChannelConfigurationReference",
]

publication.publish()

def _typecheckingstub__3fb90d4fa48d9894f917d57846d278eba7ea1e6bfd3bfd59b16908a4f85c1307(
    *,
    custom_action_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f3d28b11300d54dce65640e5e1bc1fd14d4e67a6351d040492c48666baf809d(
    *,
    microsoft_teams_channel_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d3c2972c2b588e2114bbc9a1c4896bdbc0f6f708168fee57c58fc9caca79de8(
    *,
    slack_channel_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICustomActionRef, IMicrosoftTeamsChannelConfigurationRef, ISlackChannelConfigurationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
