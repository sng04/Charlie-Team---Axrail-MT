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
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.ADMChannelReference",
    jsii_struct_bases=[],
    name_mapping={"adm_channel_id": "admChannelId"},
)
class ADMChannelReference:
    def __init__(self, *, adm_channel_id: builtins.str) -> None:
        '''A reference to a ADMChannel resource.

        :param adm_channel_id: The Id of the ADMChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            a_dMChannel_reference = interfaces_pinpoint.ADMChannelReference(
                adm_channel_id="admChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c66344866d57b2c61e87a53457006c0e900b38b698cdb217466ed7caa7d21d30)
            check_type(argname="argument adm_channel_id", value=adm_channel_id, expected_type=type_hints["adm_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "adm_channel_id": adm_channel_id,
        }

    @builtins.property
    def adm_channel_id(self) -> builtins.str:
        '''The Id of the ADMChannel resource.'''
        result = self._values.get("adm_channel_id")
        assert result is not None, "Required property 'adm_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ADMChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.APNSChannelReference",
    jsii_struct_bases=[],
    name_mapping={"apns_channel_id": "apnsChannelId"},
)
class APNSChannelReference:
    def __init__(self, *, apns_channel_id: builtins.str) -> None:
        '''A reference to a APNSChannel resource.

        :param apns_channel_id: The Id of the APNSChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            a_pNSChannel_reference = interfaces_pinpoint.APNSChannelReference(
                apns_channel_id="apnsChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a496ce49e220f7813d622667dcfaedd8e2168f11f3b2c9e2d2897832fd3ab9bd)
            check_type(argname="argument apns_channel_id", value=apns_channel_id, expected_type=type_hints["apns_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "apns_channel_id": apns_channel_id,
        }

    @builtins.property
    def apns_channel_id(self) -> builtins.str:
        '''The Id of the APNSChannel resource.'''
        result = self._values.get("apns_channel_id")
        assert result is not None, "Required property 'apns_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "APNSChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.APNSSandboxChannelReference",
    jsii_struct_bases=[],
    name_mapping={"apns_sandbox_channel_id": "apnsSandboxChannelId"},
)
class APNSSandboxChannelReference:
    def __init__(self, *, apns_sandbox_channel_id: builtins.str) -> None:
        '''A reference to a APNSSandboxChannel resource.

        :param apns_sandbox_channel_id: The Id of the APNSSandboxChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            a_pNSSandbox_channel_reference = interfaces_pinpoint.APNSSandboxChannelReference(
                apns_sandbox_channel_id="apnsSandboxChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b94d95c331fe8bd2e4c6c5e6e85996744c1a65f3b436aeac431abbb19e43dffd)
            check_type(argname="argument apns_sandbox_channel_id", value=apns_sandbox_channel_id, expected_type=type_hints["apns_sandbox_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "apns_sandbox_channel_id": apns_sandbox_channel_id,
        }

    @builtins.property
    def apns_sandbox_channel_id(self) -> builtins.str:
        '''The Id of the APNSSandboxChannel resource.'''
        result = self._values.get("apns_sandbox_channel_id")
        assert result is not None, "Required property 'apns_sandbox_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "APNSSandboxChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.APNSVoipChannelReference",
    jsii_struct_bases=[],
    name_mapping={"apns_voip_channel_id": "apnsVoipChannelId"},
)
class APNSVoipChannelReference:
    def __init__(self, *, apns_voip_channel_id: builtins.str) -> None:
        '''A reference to a APNSVoipChannel resource.

        :param apns_voip_channel_id: The Id of the APNSVoipChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            a_pNSVoip_channel_reference = interfaces_pinpoint.APNSVoipChannelReference(
                apns_voip_channel_id="apnsVoipChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d20e3efb22a5a77e26b385ce38c50e440a81f1b4039542add7de29ef13fb222a)
            check_type(argname="argument apns_voip_channel_id", value=apns_voip_channel_id, expected_type=type_hints["apns_voip_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "apns_voip_channel_id": apns_voip_channel_id,
        }

    @builtins.property
    def apns_voip_channel_id(self) -> builtins.str:
        '''The Id of the APNSVoipChannel resource.'''
        result = self._values.get("apns_voip_channel_id")
        assert result is not None, "Required property 'apns_voip_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "APNSVoipChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.APNSVoipSandboxChannelReference",
    jsii_struct_bases=[],
    name_mapping={"apns_voip_sandbox_channel_id": "apnsVoipSandboxChannelId"},
)
class APNSVoipSandboxChannelReference:
    def __init__(self, *, apns_voip_sandbox_channel_id: builtins.str) -> None:
        '''A reference to a APNSVoipSandboxChannel resource.

        :param apns_voip_sandbox_channel_id: The Id of the APNSVoipSandboxChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            a_pNSVoip_sandbox_channel_reference = interfaces_pinpoint.APNSVoipSandboxChannelReference(
                apns_voip_sandbox_channel_id="apnsVoipSandboxChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f6b0a4afdfa151ba7b3ccd79e7b1be578515d0c8cd7e37dbd00c215e812d864)
            check_type(argname="argument apns_voip_sandbox_channel_id", value=apns_voip_sandbox_channel_id, expected_type=type_hints["apns_voip_sandbox_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "apns_voip_sandbox_channel_id": apns_voip_sandbox_channel_id,
        }

    @builtins.property
    def apns_voip_sandbox_channel_id(self) -> builtins.str:
        '''The Id of the APNSVoipSandboxChannel resource.'''
        result = self._values.get("apns_voip_sandbox_channel_id")
        assert result is not None, "Required property 'apns_voip_sandbox_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "APNSVoipSandboxChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.AppReference",
    jsii_struct_bases=[],
    name_mapping={"app_arn": "appArn", "app_id": "appId"},
)
class AppReference:
    def __init__(self, *, app_arn: builtins.str, app_id: builtins.str) -> None:
        '''A reference to a App resource.

        :param app_arn: The ARN of the App resource.
        :param app_id: The Id of the App resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            app_reference = interfaces_pinpoint.AppReference(
                app_arn="appArn",
                app_id="appId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47f9f51d19cf6bb2505181b94960ee58497234e95a8cb312c5b8b732fdfa2191)
            check_type(argname="argument app_arn", value=app_arn, expected_type=type_hints["app_arn"])
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_arn": app_arn,
            "app_id": app_id,
        }

    @builtins.property
    def app_arn(self) -> builtins.str:
        '''The ARN of the App resource.'''
        result = self._values.get("app_arn")
        assert result is not None, "Required property 'app_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_id(self) -> builtins.str:
        '''The Id of the App resource.'''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.ApplicationSettingsReference",
    jsii_struct_bases=[],
    name_mapping={"application_settings_id": "applicationSettingsId"},
)
class ApplicationSettingsReference:
    def __init__(self, *, application_settings_id: builtins.str) -> None:
        '''A reference to a ApplicationSettings resource.

        :param application_settings_id: The Id of the ApplicationSettings resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            application_settings_reference = interfaces_pinpoint.ApplicationSettingsReference(
                application_settings_id="applicationSettingsId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db9052113d2b53ec08d341c550acb86b274f0fc0ea21deb1b4345d037133c469)
            check_type(argname="argument application_settings_id", value=application_settings_id, expected_type=type_hints["application_settings_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_settings_id": application_settings_id,
        }

    @builtins.property
    def application_settings_id(self) -> builtins.str:
        '''The Id of the ApplicationSettings resource.'''
        result = self._values.get("application_settings_id")
        assert result is not None, "Required property 'application_settings_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationSettingsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.BaiduChannelReference",
    jsii_struct_bases=[],
    name_mapping={"baidu_channel_id": "baiduChannelId"},
)
class BaiduChannelReference:
    def __init__(self, *, baidu_channel_id: builtins.str) -> None:
        '''A reference to a BaiduChannel resource.

        :param baidu_channel_id: The Id of the BaiduChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            baidu_channel_reference = interfaces_pinpoint.BaiduChannelReference(
                baidu_channel_id="baiduChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__491989d5301704adbe9e8c97d33163a8252bcacb817aa52b0e5d7bcfbe90fcd1)
            check_type(argname="argument baidu_channel_id", value=baidu_channel_id, expected_type=type_hints["baidu_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "baidu_channel_id": baidu_channel_id,
        }

    @builtins.property
    def baidu_channel_id(self) -> builtins.str:
        '''The Id of the BaiduChannel resource.'''
        result = self._values.get("baidu_channel_id")
        assert result is not None, "Required property 'baidu_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaiduChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.CampaignReference",
    jsii_struct_bases=[],
    name_mapping={"campaign_arn": "campaignArn", "campaign_id": "campaignId"},
)
class CampaignReference:
    def __init__(
        self,
        *,
        campaign_arn: builtins.str,
        campaign_id: builtins.str,
    ) -> None:
        '''A reference to a Campaign resource.

        :param campaign_arn: The ARN of the Campaign resource.
        :param campaign_id: The CampaignId of the Campaign resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            campaign_reference = interfaces_pinpoint.CampaignReference(
                campaign_arn="campaignArn",
                campaign_id="campaignId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcf64db1b1596dc4aa37057576b9a0db604c629f6fab5b122a9fc764eeec65af)
            check_type(argname="argument campaign_arn", value=campaign_arn, expected_type=type_hints["campaign_arn"])
            check_type(argname="argument campaign_id", value=campaign_id, expected_type=type_hints["campaign_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "campaign_arn": campaign_arn,
            "campaign_id": campaign_id,
        }

    @builtins.property
    def campaign_arn(self) -> builtins.str:
        '''The ARN of the Campaign resource.'''
        result = self._values.get("campaign_arn")
        assert result is not None, "Required property 'campaign_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def campaign_id(self) -> builtins.str:
        '''The CampaignId of the Campaign resource.'''
        result = self._values.get("campaign_id")
        assert result is not None, "Required property 'campaign_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CampaignReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.EmailChannelReference",
    jsii_struct_bases=[],
    name_mapping={"email_channel_id": "emailChannelId"},
)
class EmailChannelReference:
    def __init__(self, *, email_channel_id: builtins.str) -> None:
        '''A reference to a EmailChannel resource.

        :param email_channel_id: The Id of the EmailChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            email_channel_reference = interfaces_pinpoint.EmailChannelReference(
                email_channel_id="emailChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d2c4016fc9671888b08731a815286889bd95745893730b746ec6246a930569)
            check_type(argname="argument email_channel_id", value=email_channel_id, expected_type=type_hints["email_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email_channel_id": email_channel_id,
        }

    @builtins.property
    def email_channel_id(self) -> builtins.str:
        '''The Id of the EmailChannel resource.'''
        result = self._values.get("email_channel_id")
        assert result is not None, "Required property 'email_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmailChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.EmailTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "email_template_arn": "emailTemplateArn",
        "email_template_id": "emailTemplateId",
    },
)
class EmailTemplateReference:
    def __init__(
        self,
        *,
        email_template_arn: builtins.str,
        email_template_id: builtins.str,
    ) -> None:
        '''A reference to a EmailTemplate resource.

        :param email_template_arn: The ARN of the EmailTemplate resource.
        :param email_template_id: The Id of the EmailTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            email_template_reference = interfaces_pinpoint.EmailTemplateReference(
                email_template_arn="emailTemplateArn",
                email_template_id="emailTemplateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8869b0aa99806f8520c0ab61fa32beba3955adf2febe0942549ac0cce8fabf79)
            check_type(argname="argument email_template_arn", value=email_template_arn, expected_type=type_hints["email_template_arn"])
            check_type(argname="argument email_template_id", value=email_template_id, expected_type=type_hints["email_template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email_template_arn": email_template_arn,
            "email_template_id": email_template_id,
        }

    @builtins.property
    def email_template_arn(self) -> builtins.str:
        '''The ARN of the EmailTemplate resource.'''
        result = self._values.get("email_template_arn")
        assert result is not None, "Required property 'email_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email_template_id(self) -> builtins.str:
        '''The Id of the EmailTemplate resource.'''
        result = self._values.get("email_template_id")
        assert result is not None, "Required property 'email_template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmailTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.EventStreamReference",
    jsii_struct_bases=[],
    name_mapping={"event_stream_id": "eventStreamId"},
)
class EventStreamReference:
    def __init__(self, *, event_stream_id: builtins.str) -> None:
        '''A reference to a EventStream resource.

        :param event_stream_id: The Id of the EventStream resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            event_stream_reference = interfaces_pinpoint.EventStreamReference(
                event_stream_id="eventStreamId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b3328b21045c7e33dc1f9e42d52efa3dd71cb2d8b7bd5d7f47167668d353ede)
            check_type(argname="argument event_stream_id", value=event_stream_id, expected_type=type_hints["event_stream_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_stream_id": event_stream_id,
        }

    @builtins.property
    def event_stream_id(self) -> builtins.str:
        '''The Id of the EventStream resource.'''
        result = self._values.get("event_stream_id")
        assert result is not None, "Required property 'event_stream_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventStreamReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.GCMChannelReference",
    jsii_struct_bases=[],
    name_mapping={"gcm_channel_id": "gcmChannelId"},
)
class GCMChannelReference:
    def __init__(self, *, gcm_channel_id: builtins.str) -> None:
        '''A reference to a GCMChannel resource.

        :param gcm_channel_id: The Id of the GCMChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            g_cMChannel_reference = interfaces_pinpoint.GCMChannelReference(
                gcm_channel_id="gcmChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b116ef27b30e0b0006ee7bfa943a8e2906335c3cb406d959b4feae4b1c9c2f1d)
            check_type(argname="argument gcm_channel_id", value=gcm_channel_id, expected_type=type_hints["gcm_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gcm_channel_id": gcm_channel_id,
        }

    @builtins.property
    def gcm_channel_id(self) -> builtins.str:
        '''The Id of the GCMChannel resource.'''
        result = self._values.get("gcm_channel_id")
        assert result is not None, "Required property 'gcm_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GCMChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IADMChannelRef")
class IADMChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ADMChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="admChannelRef")
    def adm_channel_ref(self) -> "ADMChannelReference":
        '''(experimental) A reference to a ADMChannel resource.

        :stability: experimental
        '''
        ...


class _IADMChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ADMChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IADMChannelRef"

    @builtins.property
    @jsii.member(jsii_name="admChannelRef")
    def adm_channel_ref(self) -> "ADMChannelReference":
        '''(experimental) A reference to a ADMChannel resource.

        :stability: experimental
        '''
        return typing.cast("ADMChannelReference", jsii.get(self, "admChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IADMChannelRef).__jsii_proxy_class__ = lambda : _IADMChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IAPNSChannelRef")
class IAPNSChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a APNSChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apnsChannelRef")
    def apns_channel_ref(self) -> "APNSChannelReference":
        '''(experimental) A reference to a APNSChannel resource.

        :stability: experimental
        '''
        ...


class _IAPNSChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a APNSChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IAPNSChannelRef"

    @builtins.property
    @jsii.member(jsii_name="apnsChannelRef")
    def apns_channel_ref(self) -> "APNSChannelReference":
        '''(experimental) A reference to a APNSChannel resource.

        :stability: experimental
        '''
        return typing.cast("APNSChannelReference", jsii.get(self, "apnsChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAPNSChannelRef).__jsii_proxy_class__ = lambda : _IAPNSChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IAPNSSandboxChannelRef")
class IAPNSSandboxChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a APNSSandboxChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apnsSandboxChannelRef")
    def apns_sandbox_channel_ref(self) -> "APNSSandboxChannelReference":
        '''(experimental) A reference to a APNSSandboxChannel resource.

        :stability: experimental
        '''
        ...


class _IAPNSSandboxChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a APNSSandboxChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IAPNSSandboxChannelRef"

    @builtins.property
    @jsii.member(jsii_name="apnsSandboxChannelRef")
    def apns_sandbox_channel_ref(self) -> "APNSSandboxChannelReference":
        '''(experimental) A reference to a APNSSandboxChannel resource.

        :stability: experimental
        '''
        return typing.cast("APNSSandboxChannelReference", jsii.get(self, "apnsSandboxChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAPNSSandboxChannelRef).__jsii_proxy_class__ = lambda : _IAPNSSandboxChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IAPNSVoipChannelRef")
class IAPNSVoipChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a APNSVoipChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apnsVoipChannelRef")
    def apns_voip_channel_ref(self) -> "APNSVoipChannelReference":
        '''(experimental) A reference to a APNSVoipChannel resource.

        :stability: experimental
        '''
        ...


class _IAPNSVoipChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a APNSVoipChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IAPNSVoipChannelRef"

    @builtins.property
    @jsii.member(jsii_name="apnsVoipChannelRef")
    def apns_voip_channel_ref(self) -> "APNSVoipChannelReference":
        '''(experimental) A reference to a APNSVoipChannel resource.

        :stability: experimental
        '''
        return typing.cast("APNSVoipChannelReference", jsii.get(self, "apnsVoipChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAPNSVoipChannelRef).__jsii_proxy_class__ = lambda : _IAPNSVoipChannelRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IAPNSVoipSandboxChannelRef"
)
class IAPNSVoipSandboxChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a APNSVoipSandboxChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apnsVoipSandboxChannelRef")
    def apns_voip_sandbox_channel_ref(self) -> "APNSVoipSandboxChannelReference":
        '''(experimental) A reference to a APNSVoipSandboxChannel resource.

        :stability: experimental
        '''
        ...


class _IAPNSVoipSandboxChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a APNSVoipSandboxChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IAPNSVoipSandboxChannelRef"

    @builtins.property
    @jsii.member(jsii_name="apnsVoipSandboxChannelRef")
    def apns_voip_sandbox_channel_ref(self) -> "APNSVoipSandboxChannelReference":
        '''(experimental) A reference to a APNSVoipSandboxChannel resource.

        :stability: experimental
        '''
        return typing.cast("APNSVoipSandboxChannelReference", jsii.get(self, "apnsVoipSandboxChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAPNSVoipSandboxChannelRef).__jsii_proxy_class__ = lambda : _IAPNSVoipSandboxChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IAppRef")
class IAppRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        ...


class _IAppRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a App.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IAppRef"

    @builtins.property
    @jsii.member(jsii_name="appRef")
    def app_ref(self) -> "AppReference":
        '''(experimental) A reference to a App resource.

        :stability: experimental
        '''
        return typing.cast("AppReference", jsii.get(self, "appRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAppRef).__jsii_proxy_class__ = lambda : _IAppRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IApplicationSettingsRef"
)
class IApplicationSettingsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationSettings.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationSettingsRef")
    def application_settings_ref(self) -> "ApplicationSettingsReference":
        '''(experimental) A reference to a ApplicationSettings resource.

        :stability: experimental
        '''
        ...


class _IApplicationSettingsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationSettings.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IApplicationSettingsRef"

    @builtins.property
    @jsii.member(jsii_name="applicationSettingsRef")
    def application_settings_ref(self) -> "ApplicationSettingsReference":
        '''(experimental) A reference to a ApplicationSettings resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationSettingsReference", jsii.get(self, "applicationSettingsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationSettingsRef).__jsii_proxy_class__ = lambda : _IApplicationSettingsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IBaiduChannelRef")
class IBaiduChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BaiduChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="baiduChannelRef")
    def baidu_channel_ref(self) -> "BaiduChannelReference":
        '''(experimental) A reference to a BaiduChannel resource.

        :stability: experimental
        '''
        ...


class _IBaiduChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BaiduChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IBaiduChannelRef"

    @builtins.property
    @jsii.member(jsii_name="baiduChannelRef")
    def baidu_channel_ref(self) -> "BaiduChannelReference":
        '''(experimental) A reference to a BaiduChannel resource.

        :stability: experimental
        '''
        return typing.cast("BaiduChannelReference", jsii.get(self, "baiduChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBaiduChannelRef).__jsii_proxy_class__ = lambda : _IBaiduChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.ICampaignRef")
class ICampaignRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Campaign.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="campaignRef")
    def campaign_ref(self) -> "CampaignReference":
        '''(experimental) A reference to a Campaign resource.

        :stability: experimental
        '''
        ...


class _ICampaignRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Campaign.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.ICampaignRef"

    @builtins.property
    @jsii.member(jsii_name="campaignRef")
    def campaign_ref(self) -> "CampaignReference":
        '''(experimental) A reference to a Campaign resource.

        :stability: experimental
        '''
        return typing.cast("CampaignReference", jsii.get(self, "campaignRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICampaignRef).__jsii_proxy_class__ = lambda : _ICampaignRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IEmailChannelRef")
class IEmailChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EmailChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="emailChannelRef")
    def email_channel_ref(self) -> "EmailChannelReference":
        '''(experimental) A reference to a EmailChannel resource.

        :stability: experimental
        '''
        ...


class _IEmailChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EmailChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IEmailChannelRef"

    @builtins.property
    @jsii.member(jsii_name="emailChannelRef")
    def email_channel_ref(self) -> "EmailChannelReference":
        '''(experimental) A reference to a EmailChannel resource.

        :stability: experimental
        '''
        return typing.cast("EmailChannelReference", jsii.get(self, "emailChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEmailChannelRef).__jsii_proxy_class__ = lambda : _IEmailChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IEmailTemplateRef")
class IEmailTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EmailTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="emailTemplateRef")
    def email_template_ref(self) -> "EmailTemplateReference":
        '''(experimental) A reference to a EmailTemplate resource.

        :stability: experimental
        '''
        ...


class _IEmailTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EmailTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IEmailTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="emailTemplateRef")
    def email_template_ref(self) -> "EmailTemplateReference":
        '''(experimental) A reference to a EmailTemplate resource.

        :stability: experimental
        '''
        return typing.cast("EmailTemplateReference", jsii.get(self, "emailTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEmailTemplateRef).__jsii_proxy_class__ = lambda : _IEmailTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IEventStreamRef")
class IEventStreamRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventStream.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventStreamRef")
    def event_stream_ref(self) -> "EventStreamReference":
        '''(experimental) A reference to a EventStream resource.

        :stability: experimental
        '''
        ...


class _IEventStreamRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventStream.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IEventStreamRef"

    @builtins.property
    @jsii.member(jsii_name="eventStreamRef")
    def event_stream_ref(self) -> "EventStreamReference":
        '''(experimental) A reference to a EventStream resource.

        :stability: experimental
        '''
        return typing.cast("EventStreamReference", jsii.get(self, "eventStreamRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventStreamRef).__jsii_proxy_class__ = lambda : _IEventStreamRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IGCMChannelRef")
class IGCMChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GCMChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gcmChannelRef")
    def gcm_channel_ref(self) -> "GCMChannelReference":
        '''(experimental) A reference to a GCMChannel resource.

        :stability: experimental
        '''
        ...


class _IGCMChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GCMChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IGCMChannelRef"

    @builtins.property
    @jsii.member(jsii_name="gcmChannelRef")
    def gcm_channel_ref(self) -> "GCMChannelReference":
        '''(experimental) A reference to a GCMChannel resource.

        :stability: experimental
        '''
        return typing.cast("GCMChannelReference", jsii.get(self, "gcmChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGCMChannelRef).__jsii_proxy_class__ = lambda : _IGCMChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IInAppTemplateRef")
class IInAppTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InAppTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="inAppTemplateRef")
    def in_app_template_ref(self) -> "InAppTemplateReference":
        '''(experimental) A reference to a InAppTemplate resource.

        :stability: experimental
        '''
        ...


class _IInAppTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InAppTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IInAppTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="inAppTemplateRef")
    def in_app_template_ref(self) -> "InAppTemplateReference":
        '''(experimental) A reference to a InAppTemplate resource.

        :stability: experimental
        '''
        return typing.cast("InAppTemplateReference", jsii.get(self, "inAppTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInAppTemplateRef).__jsii_proxy_class__ = lambda : _IInAppTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IPushTemplateRef")
class IPushTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PushTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pushTemplateRef")
    def push_template_ref(self) -> "PushTemplateReference":
        '''(experimental) A reference to a PushTemplate resource.

        :stability: experimental
        '''
        ...


class _IPushTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PushTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IPushTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="pushTemplateRef")
    def push_template_ref(self) -> "PushTemplateReference":
        '''(experimental) A reference to a PushTemplate resource.

        :stability: experimental
        '''
        return typing.cast("PushTemplateReference", jsii.get(self, "pushTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPushTemplateRef).__jsii_proxy_class__ = lambda : _IPushTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.ISMSChannelRef")
class ISMSChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SMSChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="smsChannelRef")
    def sms_channel_ref(self) -> "SMSChannelReference":
        '''(experimental) A reference to a SMSChannel resource.

        :stability: experimental
        '''
        ...


class _ISMSChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SMSChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.ISMSChannelRef"

    @builtins.property
    @jsii.member(jsii_name="smsChannelRef")
    def sms_channel_ref(self) -> "SMSChannelReference":
        '''(experimental) A reference to a SMSChannel resource.

        :stability: experimental
        '''
        return typing.cast("SMSChannelReference", jsii.get(self, "smsChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISMSChannelRef).__jsii_proxy_class__ = lambda : _ISMSChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.ISegmentRef")
class ISegmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Segment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="segmentRef")
    def segment_ref(self) -> "SegmentReference":
        '''(experimental) A reference to a Segment resource.

        :stability: experimental
        '''
        ...


class _ISegmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Segment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.ISegmentRef"

    @builtins.property
    @jsii.member(jsii_name="segmentRef")
    def segment_ref(self) -> "SegmentReference":
        '''(experimental) A reference to a Segment resource.

        :stability: experimental
        '''
        return typing.cast("SegmentReference", jsii.get(self, "segmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISegmentRef).__jsii_proxy_class__ = lambda : _ISegmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.ISmsTemplateRef")
class ISmsTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SmsTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="smsTemplateRef")
    def sms_template_ref(self) -> "SmsTemplateReference":
        '''(experimental) A reference to a SmsTemplate resource.

        :stability: experimental
        '''
        ...


class _ISmsTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SmsTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.ISmsTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="smsTemplateRef")
    def sms_template_ref(self) -> "SmsTemplateReference":
        '''(experimental) A reference to a SmsTemplate resource.

        :stability: experimental
        '''
        return typing.cast("SmsTemplateReference", jsii.get(self, "smsTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISmsTemplateRef).__jsii_proxy_class__ = lambda : _ISmsTemplateRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.IVoiceChannelRef")
class IVoiceChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VoiceChannel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="voiceChannelRef")
    def voice_channel_ref(self) -> "VoiceChannelReference":
        '''(experimental) A reference to a VoiceChannel resource.

        :stability: experimental
        '''
        ...


class _IVoiceChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VoiceChannel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pinpoint.IVoiceChannelRef"

    @builtins.property
    @jsii.member(jsii_name="voiceChannelRef")
    def voice_channel_ref(self) -> "VoiceChannelReference":
        '''(experimental) A reference to a VoiceChannel resource.

        :stability: experimental
        '''
        return typing.cast("VoiceChannelReference", jsii.get(self, "voiceChannelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVoiceChannelRef).__jsii_proxy_class__ = lambda : _IVoiceChannelRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.InAppTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "in_app_template_arn": "inAppTemplateArn",
        "template_name": "templateName",
    },
)
class InAppTemplateReference:
    def __init__(
        self,
        *,
        in_app_template_arn: builtins.str,
        template_name: builtins.str,
    ) -> None:
        '''A reference to a InAppTemplate resource.

        :param in_app_template_arn: The ARN of the InAppTemplate resource.
        :param template_name: The TemplateName of the InAppTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            in_app_template_reference = interfaces_pinpoint.InAppTemplateReference(
                in_app_template_arn="inAppTemplateArn",
                template_name="templateName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f56c47521e8d4b1931531ec9e0af0b2b3b6bc5b13f909a73d6266fc1af62ac4)
            check_type(argname="argument in_app_template_arn", value=in_app_template_arn, expected_type=type_hints["in_app_template_arn"])
            check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "in_app_template_arn": in_app_template_arn,
            "template_name": template_name,
        }

    @builtins.property
    def in_app_template_arn(self) -> builtins.str:
        '''The ARN of the InAppTemplate resource.'''
        result = self._values.get("in_app_template_arn")
        assert result is not None, "Required property 'in_app_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def template_name(self) -> builtins.str:
        '''The TemplateName of the InAppTemplate resource.'''
        result = self._values.get("template_name")
        assert result is not None, "Required property 'template_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InAppTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.PushTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "push_template_arn": "pushTemplateArn",
        "push_template_id": "pushTemplateId",
    },
)
class PushTemplateReference:
    def __init__(
        self,
        *,
        push_template_arn: builtins.str,
        push_template_id: builtins.str,
    ) -> None:
        '''A reference to a PushTemplate resource.

        :param push_template_arn: The ARN of the PushTemplate resource.
        :param push_template_id: The Id of the PushTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            push_template_reference = interfaces_pinpoint.PushTemplateReference(
                push_template_arn="pushTemplateArn",
                push_template_id="pushTemplateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48eecae18daf78c49e57e56d7965bed0531fa14f9e724b6502d1de79e49720d7)
            check_type(argname="argument push_template_arn", value=push_template_arn, expected_type=type_hints["push_template_arn"])
            check_type(argname="argument push_template_id", value=push_template_id, expected_type=type_hints["push_template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "push_template_arn": push_template_arn,
            "push_template_id": push_template_id,
        }

    @builtins.property
    def push_template_arn(self) -> builtins.str:
        '''The ARN of the PushTemplate resource.'''
        result = self._values.get("push_template_arn")
        assert result is not None, "Required property 'push_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def push_template_id(self) -> builtins.str:
        '''The Id of the PushTemplate resource.'''
        result = self._values.get("push_template_id")
        assert result is not None, "Required property 'push_template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PushTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.SMSChannelReference",
    jsii_struct_bases=[],
    name_mapping={"sms_channel_id": "smsChannelId"},
)
class SMSChannelReference:
    def __init__(self, *, sms_channel_id: builtins.str) -> None:
        '''A reference to a SMSChannel resource.

        :param sms_channel_id: The Id of the SMSChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            s_mSChannel_reference = interfaces_pinpoint.SMSChannelReference(
                sms_channel_id="smsChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8cdc01c61bd6bad4cbba03bd46f565e09a4008938a8bcdbb113e8647fcb345f)
            check_type(argname="argument sms_channel_id", value=sms_channel_id, expected_type=type_hints["sms_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sms_channel_id": sms_channel_id,
        }

    @builtins.property
    def sms_channel_id(self) -> builtins.str:
        '''The Id of the SMSChannel resource.'''
        result = self._values.get("sms_channel_id")
        assert result is not None, "Required property 'sms_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SMSChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.SegmentReference",
    jsii_struct_bases=[],
    name_mapping={"segment_arn": "segmentArn", "segment_id": "segmentId"},
)
class SegmentReference:
    def __init__(self, *, segment_arn: builtins.str, segment_id: builtins.str) -> None:
        '''A reference to a Segment resource.

        :param segment_arn: The ARN of the Segment resource.
        :param segment_id: The SegmentId of the Segment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            segment_reference = interfaces_pinpoint.SegmentReference(
                segment_arn="segmentArn",
                segment_id="segmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43027cfe742ea4d035f9110cff172e42150a9c6d345f6e871757fb682dc7463d)
            check_type(argname="argument segment_arn", value=segment_arn, expected_type=type_hints["segment_arn"])
            check_type(argname="argument segment_id", value=segment_id, expected_type=type_hints["segment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "segment_arn": segment_arn,
            "segment_id": segment_id,
        }

    @builtins.property
    def segment_arn(self) -> builtins.str:
        '''The ARN of the Segment resource.'''
        result = self._values.get("segment_arn")
        assert result is not None, "Required property 'segment_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def segment_id(self) -> builtins.str:
        '''The SegmentId of the Segment resource.'''
        result = self._values.get("segment_id")
        assert result is not None, "Required property 'segment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SegmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.SmsTemplateReference",
    jsii_struct_bases=[],
    name_mapping={
        "sms_template_arn": "smsTemplateArn",
        "sms_template_id": "smsTemplateId",
    },
)
class SmsTemplateReference:
    def __init__(
        self,
        *,
        sms_template_arn: builtins.str,
        sms_template_id: builtins.str,
    ) -> None:
        '''A reference to a SmsTemplate resource.

        :param sms_template_arn: The ARN of the SmsTemplate resource.
        :param sms_template_id: The Id of the SmsTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            sms_template_reference = interfaces_pinpoint.SmsTemplateReference(
                sms_template_arn="smsTemplateArn",
                sms_template_id="smsTemplateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d53d3d1c75d95f24190fb2b5a34a27c2c9fce6930823096aef9e4b60c0f5b678)
            check_type(argname="argument sms_template_arn", value=sms_template_arn, expected_type=type_hints["sms_template_arn"])
            check_type(argname="argument sms_template_id", value=sms_template_id, expected_type=type_hints["sms_template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sms_template_arn": sms_template_arn,
            "sms_template_id": sms_template_id,
        }

    @builtins.property
    def sms_template_arn(self) -> builtins.str:
        '''The ARN of the SmsTemplate resource.'''
        result = self._values.get("sms_template_arn")
        assert result is not None, "Required property 'sms_template_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sms_template_id(self) -> builtins.str:
        '''The Id of the SmsTemplate resource.'''
        result = self._values.get("sms_template_id")
        assert result is not None, "Required property 'sms_template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SmsTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pinpoint.VoiceChannelReference",
    jsii_struct_bases=[],
    name_mapping={"voice_channel_id": "voiceChannelId"},
)
class VoiceChannelReference:
    def __init__(self, *, voice_channel_id: builtins.str) -> None:
        '''A reference to a VoiceChannel resource.

        :param voice_channel_id: The Id of the VoiceChannel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pinpoint as interfaces_pinpoint
            
            voice_channel_reference = interfaces_pinpoint.VoiceChannelReference(
                voice_channel_id="voiceChannelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f7509afe29cd2d53cd659467ac40979b94a308d323f9d02abea3143e0d45790)
            check_type(argname="argument voice_channel_id", value=voice_channel_id, expected_type=type_hints["voice_channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "voice_channel_id": voice_channel_id,
        }

    @builtins.property
    def voice_channel_id(self) -> builtins.str:
        '''The Id of the VoiceChannel resource.'''
        result = self._values.get("voice_channel_id")
        assert result is not None, "Required property 'voice_channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VoiceChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ADMChannelReference",
    "APNSChannelReference",
    "APNSSandboxChannelReference",
    "APNSVoipChannelReference",
    "APNSVoipSandboxChannelReference",
    "AppReference",
    "ApplicationSettingsReference",
    "BaiduChannelReference",
    "CampaignReference",
    "EmailChannelReference",
    "EmailTemplateReference",
    "EventStreamReference",
    "GCMChannelReference",
    "IADMChannelRef",
    "IAPNSChannelRef",
    "IAPNSSandboxChannelRef",
    "IAPNSVoipChannelRef",
    "IAPNSVoipSandboxChannelRef",
    "IAppRef",
    "IApplicationSettingsRef",
    "IBaiduChannelRef",
    "ICampaignRef",
    "IEmailChannelRef",
    "IEmailTemplateRef",
    "IEventStreamRef",
    "IGCMChannelRef",
    "IInAppTemplateRef",
    "IPushTemplateRef",
    "ISMSChannelRef",
    "ISegmentRef",
    "ISmsTemplateRef",
    "IVoiceChannelRef",
    "InAppTemplateReference",
    "PushTemplateReference",
    "SMSChannelReference",
    "SegmentReference",
    "SmsTemplateReference",
    "VoiceChannelReference",
]

publication.publish()

def _typecheckingstub__c66344866d57b2c61e87a53457006c0e900b38b698cdb217466ed7caa7d21d30(
    *,
    adm_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a496ce49e220f7813d622667dcfaedd8e2168f11f3b2c9e2d2897832fd3ab9bd(
    *,
    apns_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b94d95c331fe8bd2e4c6c5e6e85996744c1a65f3b436aeac431abbb19e43dffd(
    *,
    apns_sandbox_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d20e3efb22a5a77e26b385ce38c50e440a81f1b4039542add7de29ef13fb222a(
    *,
    apns_voip_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f6b0a4afdfa151ba7b3ccd79e7b1be578515d0c8cd7e37dbd00c215e812d864(
    *,
    apns_voip_sandbox_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47f9f51d19cf6bb2505181b94960ee58497234e95a8cb312c5b8b732fdfa2191(
    *,
    app_arn: builtins.str,
    app_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db9052113d2b53ec08d341c550acb86b274f0fc0ea21deb1b4345d037133c469(
    *,
    application_settings_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491989d5301704adbe9e8c97d33163a8252bcacb817aa52b0e5d7bcfbe90fcd1(
    *,
    baidu_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcf64db1b1596dc4aa37057576b9a0db604c629f6fab5b122a9fc764eeec65af(
    *,
    campaign_arn: builtins.str,
    campaign_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d2c4016fc9671888b08731a815286889bd95745893730b746ec6246a930569(
    *,
    email_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8869b0aa99806f8520c0ab61fa32beba3955adf2febe0942549ac0cce8fabf79(
    *,
    email_template_arn: builtins.str,
    email_template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b3328b21045c7e33dc1f9e42d52efa3dd71cb2d8b7bd5d7f47167668d353ede(
    *,
    event_stream_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b116ef27b30e0b0006ee7bfa943a8e2906335c3cb406d959b4feae4b1c9c2f1d(
    *,
    gcm_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f56c47521e8d4b1931531ec9e0af0b2b3b6bc5b13f909a73d6266fc1af62ac4(
    *,
    in_app_template_arn: builtins.str,
    template_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48eecae18daf78c49e57e56d7965bed0531fa14f9e724b6502d1de79e49720d7(
    *,
    push_template_arn: builtins.str,
    push_template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8cdc01c61bd6bad4cbba03bd46f565e09a4008938a8bcdbb113e8647fcb345f(
    *,
    sms_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43027cfe742ea4d035f9110cff172e42150a9c6d345f6e871757fb682dc7463d(
    *,
    segment_arn: builtins.str,
    segment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d53d3d1c75d95f24190fb2b5a34a27c2c9fce6930823096aef9e4b60c0f5b678(
    *,
    sms_template_arn: builtins.str,
    sms_template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f7509afe29cd2d53cd659467ac40979b94a308d323f9d02abea3143e0d45790(
    *,
    voice_channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IADMChannelRef, IAPNSChannelRef, IAPNSSandboxChannelRef, IAPNSVoipChannelRef, IAPNSVoipSandboxChannelRef, IAppRef, IApplicationSettingsRef, IBaiduChannelRef, ICampaignRef, IEmailChannelRef, IEmailTemplateRef, IEventStreamRef, IGCMChannelRef, IInAppTemplateRef, IPushTemplateRef, ISMSChannelRef, ISegmentRef, ISmsTemplateRef, IVoiceChannelRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
