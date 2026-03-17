r'''
# AWS::RTBFabric Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_rtbfabric as rtbfabric
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for RTBFabric construct libraries](https://constructs.dev/search?q=rtbfabric)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::RTBFabric resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RTBFabric.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::RTBFabric](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RTBFabric.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
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

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_ec2 import (
    ISecurityGroupRef as _ISecurityGroupRef_efa4ff18,
    ISubnetRef as _ISubnetRef_ac31e361,
    IVPCRef as _IVPCRef_f02a11df,
)
from ..interfaces.aws_rtbfabric import (
    IInboundExternalLinkRef as _IInboundExternalLinkRef_087c1bc6,
    ILinkRef as _ILinkRef_1c71e733,
    IOutboundExternalLinkRef as _IOutboundExternalLinkRef_06bb6289,
    IRequesterGatewayRef as _IRequesterGatewayRef_d92bcdf1,
    IResponderGatewayRef as _IResponderGatewayRef_2bdaa070,
    InboundExternalLinkReference as _InboundExternalLinkReference_89bab665,
    LinkReference as _LinkReference_a62a8bc7,
    OutboundExternalLinkReference as _OutboundExternalLinkReference_b1d46069,
    RequesterGatewayReference as _RequesterGatewayReference_37e2965b,
    ResponderGatewayReference as _ResponderGatewayReference_a8195bef,
)


@jsii.implements(_IInspectable_c2943556, _IInboundExternalLinkRef_087c1bc6, _ITaggableV2_4e6798f8)
class CfnInboundExternalLink(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rtbfabric.CfnInboundExternalLink",
):
    '''Resource Type definition for AWS::RTBFabric::InboundExternalLink Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-inboundexternallink.html
    :cloudformationResource: AWS::RTBFabric::InboundExternalLink
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rtbfabric as rtbfabric
        
        cfn_inbound_external_link = rtbfabric.CfnInboundExternalLink(self, "MyCfnInboundExternalLink",
            gateway_id="gatewayId",
            link_log_settings=rtbfabric.CfnInboundExternalLink.LinkLogSettingsProperty(
                application_logs=rtbfabric.CfnInboundExternalLink.ApplicationLogsProperty(
                    link_application_log_sampling=rtbfabric.CfnInboundExternalLink.LinkApplicationLogSamplingProperty(
                        error_log=123,
                        filter_log=123
                    )
                )
            ),
        
            # the properties below are optional
            link_attributes=rtbfabric.CfnInboundExternalLink.LinkAttributesProperty(
                customer_provided_id="customerProvidedId",
                responder_error_masking=[rtbfabric.CfnInboundExternalLink.ResponderErrorMaskingForHttpCodeProperty(
                    action="action",
                    http_code="httpCode",
                    logging_types=["loggingTypes"],
        
                    # the properties below are optional
                    response_logging_percentage=123
                )]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        gateway_id: builtins.str,
        link_log_settings: typing.Union["_IResolvable_da3f097b", typing.Union["CfnInboundExternalLink.LinkLogSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        link_attributes: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnInboundExternalLink.LinkAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::RTBFabric::InboundExternalLink``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param gateway_id: 
        :param link_log_settings: 
        :param link_attributes: 
        :param tags: Tags to assign to the Link.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a5afae55006ef90edfe40aa8e5117e329b49d245830f9f3781bf45c5ee1d498)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInboundExternalLinkProps(
            gateway_id=gateway_id,
            link_log_settings=link_log_settings,
            link_attributes=link_attributes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForInboundExternalLink")
    @builtins.classmethod
    def arn_for_inbound_external_link(
        cls,
        resource: "_IInboundExternalLinkRef_087c1bc6",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e45579c24ba39e7cbd88d8a1dcb187104127b5c4c031b298b39214f40fb1a36e)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForInboundExternalLink", [resource]))

    @jsii.member(jsii_name="isCfnInboundExternalLink")
    @builtins.classmethod
    def is_cfn_inbound_external_link(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnInboundExternalLink.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1943b47f9f91218da538fb23adeca699c3f23ed379e5dc88cefa0f1b8902d146)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnInboundExternalLink", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10a4ab8875cef05923631df17dd17458d37380c77a9c313974f23f57ebce0981)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f050a879dccb667647d261549cd380d2361df83488e749feb3fb74cb71c0d0f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrLinkId")
    def attr_link_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: LinkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkId"))

    @builtins.property
    @jsii.member(jsii_name="attrLinkStatus")
    def attr_link_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: LinkStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedTimestamp")
    def attr_updated_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="inboundExternalLinkRef")
    def inbound_external_link_ref(self) -> "_InboundExternalLinkReference_89bab665":
        '''A reference to a InboundExternalLink resource.'''
        return typing.cast("_InboundExternalLinkReference_89bab665", jsii.get(self, "inboundExternalLinkRef"))

    @builtins.property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayId"))

    @gateway_id.setter
    def gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb7adaf4ee57468585d346f35e67e07997a1e20abf84b582fc810dff92d7e2c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="linkLogSettings")
    def link_log_settings(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkLogSettingsProperty"]:
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkLogSettingsProperty"], jsii.get(self, "linkLogSettings"))

    @link_log_settings.setter
    def link_log_settings(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkLogSettingsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf1ee8508990492f8168ad7b68f62077e25e97d32af167928f013ed58b2c4d15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkLogSettings", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="linkAttributes")
    def link_attributes(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkAttributesProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkAttributesProperty"]], jsii.get(self, "linkAttributes"))

    @link_attributes.setter
    def link_attributes(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5745f3776bc1df4e80af5ddcc1b274597b1aab22d6cd1cf3d3f615d1fba4c3f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkAttributes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags to assign to the Link.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13f41f0dd733ffddc6dae564597b6fd8c0c31c02cd444ba959242500384e99aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnInboundExternalLink.ApplicationLogsProperty",
        jsii_struct_bases=[],
        name_mapping={"link_application_log_sampling": "linkApplicationLogSampling"},
    )
    class ApplicationLogsProperty:
        def __init__(
            self,
            *,
            link_application_log_sampling: typing.Union["_IResolvable_da3f097b", typing.Union["CfnInboundExternalLink.LinkApplicationLogSamplingProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param link_application_log_sampling: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-applicationlogs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                application_logs_property = rtbfabric.CfnInboundExternalLink.ApplicationLogsProperty(
                    link_application_log_sampling=rtbfabric.CfnInboundExternalLink.LinkApplicationLogSamplingProperty(
                        error_log=123,
                        filter_log=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9a2c31093a0bae40e89e39fd987b13c3e5cb84ca6d6dc8f166577487829dc8d4)
                check_type(argname="argument link_application_log_sampling", value=link_application_log_sampling, expected_type=type_hints["link_application_log_sampling"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "link_application_log_sampling": link_application_log_sampling,
            }

        @builtins.property
        def link_application_log_sampling(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkApplicationLogSamplingProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-applicationlogs.html#cfn-rtbfabric-inboundexternallink-applicationlogs-linkapplicationlogsampling
            '''
            result = self._values.get("link_application_log_sampling")
            assert result is not None, "Required property 'link_application_log_sampling' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkApplicationLogSamplingProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationLogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnInboundExternalLink.LinkApplicationLogSamplingProperty",
        jsii_struct_bases=[],
        name_mapping={"error_log": "errorLog", "filter_log": "filterLog"},
    )
    class LinkApplicationLogSamplingProperty:
        def __init__(self, *, error_log: jsii.Number, filter_log: jsii.Number) -> None:
            '''
            :param error_log: 
            :param filter_log: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-linkapplicationlogsampling.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                link_application_log_sampling_property = rtbfabric.CfnInboundExternalLink.LinkApplicationLogSamplingProperty(
                    error_log=123,
                    filter_log=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1140756e9bc43fe93422c9e7b90ea26b4cffbc73394ce1e5eb83064206adf56f)
                check_type(argname="argument error_log", value=error_log, expected_type=type_hints["error_log"])
                check_type(argname="argument filter_log", value=filter_log, expected_type=type_hints["filter_log"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "error_log": error_log,
                "filter_log": filter_log,
            }

        @builtins.property
        def error_log(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-linkapplicationlogsampling.html#cfn-rtbfabric-inboundexternallink-linkapplicationlogsampling-errorlog
            '''
            result = self._values.get("error_log")
            assert result is not None, "Required property 'error_log' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def filter_log(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-linkapplicationlogsampling.html#cfn-rtbfabric-inboundexternallink-linkapplicationlogsampling-filterlog
            '''
            result = self._values.get("filter_log")
            assert result is not None, "Required property 'filter_log' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinkApplicationLogSamplingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnInboundExternalLink.LinkAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_provided_id": "customerProvidedId",
            "responder_error_masking": "responderErrorMasking",
        },
    )
    class LinkAttributesProperty:
        def __init__(
            self,
            *,
            customer_provided_id: typing.Optional[builtins.str] = None,
            responder_error_masking: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnInboundExternalLink.ResponderErrorMaskingForHttpCodeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param customer_provided_id: 
            :param responder_error_masking: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-linkattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                link_attributes_property = rtbfabric.CfnInboundExternalLink.LinkAttributesProperty(
                    customer_provided_id="customerProvidedId",
                    responder_error_masking=[rtbfabric.CfnInboundExternalLink.ResponderErrorMaskingForHttpCodeProperty(
                        action="action",
                        http_code="httpCode",
                        logging_types=["loggingTypes"],
                
                        # the properties below are optional
                        response_logging_percentage=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f4ea72d051bc93d14ed2cae48b106a31ab27e9978c0bc23487c53cf7fe21dd5)
                check_type(argname="argument customer_provided_id", value=customer_provided_id, expected_type=type_hints["customer_provided_id"])
                check_type(argname="argument responder_error_masking", value=responder_error_masking, expected_type=type_hints["responder_error_masking"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_provided_id is not None:
                self._values["customer_provided_id"] = customer_provided_id
            if responder_error_masking is not None:
                self._values["responder_error_masking"] = responder_error_masking

        @builtins.property
        def customer_provided_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-linkattributes.html#cfn-rtbfabric-inboundexternallink-linkattributes-customerprovidedid
            '''
            result = self._values.get("customer_provided_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def responder_error_masking(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.ResponderErrorMaskingForHttpCodeProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-linkattributes.html#cfn-rtbfabric-inboundexternallink-linkattributes-respondererrormasking
            '''
            result = self._values.get("responder_error_masking")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.ResponderErrorMaskingForHttpCodeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinkAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnInboundExternalLink.LinkLogSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"application_logs": "applicationLogs"},
    )
    class LinkLogSettingsProperty:
        def __init__(
            self,
            *,
            application_logs: typing.Union["_IResolvable_da3f097b", typing.Union["CfnInboundExternalLink.ApplicationLogsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param application_logs: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-linklogsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                link_log_settings_property = rtbfabric.CfnInboundExternalLink.LinkLogSettingsProperty(
                    application_logs=rtbfabric.CfnInboundExternalLink.ApplicationLogsProperty(
                        link_application_log_sampling=rtbfabric.CfnInboundExternalLink.LinkApplicationLogSamplingProperty(
                            error_log=123,
                            filter_log=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c4b3acd881daca8e2c440e2d628c27b2f1ce93a4b4d05d722b1f810b3bbdeeb3)
                check_type(argname="argument application_logs", value=application_logs, expected_type=type_hints["application_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_logs": application_logs,
            }

        @builtins.property
        def application_logs(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.ApplicationLogsProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-linklogsettings.html#cfn-rtbfabric-inboundexternallink-linklogsettings-applicationlogs
            '''
            result = self._values.get("application_logs")
            assert result is not None, "Required property 'application_logs' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.ApplicationLogsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinkLogSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnInboundExternalLink.ResponderErrorMaskingForHttpCodeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "http_code": "httpCode",
            "logging_types": "loggingTypes",
            "response_logging_percentage": "responseLoggingPercentage",
        },
    )
    class ResponderErrorMaskingForHttpCodeProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            http_code: builtins.str,
            logging_types: typing.Sequence[builtins.str],
            response_logging_percentage: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param action: 
            :param http_code: 
            :param logging_types: 
            :param response_logging_percentage: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                responder_error_masking_for_http_code_property = rtbfabric.CfnInboundExternalLink.ResponderErrorMaskingForHttpCodeProperty(
                    action="action",
                    http_code="httpCode",
                    logging_types=["loggingTypes"],
                
                    # the properties below are optional
                    response_logging_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d9aa166adda80a00eaa1e13fdf8247afcbddf7768a6b4c8415c5e4e9a9dcb5d)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument http_code", value=http_code, expected_type=type_hints["http_code"])
                check_type(argname="argument logging_types", value=logging_types, expected_type=type_hints["logging_types"])
                check_type(argname="argument response_logging_percentage", value=response_logging_percentage, expected_type=type_hints["response_logging_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "http_code": http_code,
                "logging_types": logging_types,
            }
            if response_logging_percentage is not None:
                self._values["response_logging_percentage"] = response_logging_percentage

        @builtins.property
        def action(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode.html#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def http_code(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode.html#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-httpcode
            '''
            result = self._values.get("http_code")
            assert result is not None, "Required property 'http_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def logging_types(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode.html#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-loggingtypes
            '''
            result = self._values.get("logging_types")
            assert result is not None, "Required property 'logging_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def response_logging_percentage(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode.html#cfn-rtbfabric-inboundexternallink-respondererrormaskingforhttpcode-responseloggingpercentage
            '''
            result = self._values.get("response_logging_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResponderErrorMaskingForHttpCodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rtbfabric.CfnInboundExternalLinkProps",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_id": "gatewayId",
        "link_log_settings": "linkLogSettings",
        "link_attributes": "linkAttributes",
        "tags": "tags",
    },
)
class CfnInboundExternalLinkProps:
    def __init__(
        self,
        *,
        gateway_id: builtins.str,
        link_log_settings: typing.Union["_IResolvable_da3f097b", typing.Union["CfnInboundExternalLink.LinkLogSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        link_attributes: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnInboundExternalLink.LinkAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInboundExternalLink``.

        :param gateway_id: 
        :param link_log_settings: 
        :param link_attributes: 
        :param tags: Tags to assign to the Link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-inboundexternallink.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rtbfabric as rtbfabric
            
            cfn_inbound_external_link_props = rtbfabric.CfnInboundExternalLinkProps(
                gateway_id="gatewayId",
                link_log_settings=rtbfabric.CfnInboundExternalLink.LinkLogSettingsProperty(
                    application_logs=rtbfabric.CfnInboundExternalLink.ApplicationLogsProperty(
                        link_application_log_sampling=rtbfabric.CfnInboundExternalLink.LinkApplicationLogSamplingProperty(
                            error_log=123,
                            filter_log=123
                        )
                    )
                ),
            
                # the properties below are optional
                link_attributes=rtbfabric.CfnInboundExternalLink.LinkAttributesProperty(
                    customer_provided_id="customerProvidedId",
                    responder_error_masking=[rtbfabric.CfnInboundExternalLink.ResponderErrorMaskingForHttpCodeProperty(
                        action="action",
                        http_code="httpCode",
                        logging_types=["loggingTypes"],
            
                        # the properties below are optional
                        response_logging_percentage=123
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d15a9ea48568fa6d17bb53d9622c841d5242e53e66d3e303799545a8370eb3dc)
            check_type(argname="argument gateway_id", value=gateway_id, expected_type=type_hints["gateway_id"])
            check_type(argname="argument link_log_settings", value=link_log_settings, expected_type=type_hints["link_log_settings"])
            check_type(argname="argument link_attributes", value=link_attributes, expected_type=type_hints["link_attributes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_id": gateway_id,
            "link_log_settings": link_log_settings,
        }
        if link_attributes is not None:
            self._values["link_attributes"] = link_attributes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def gateway_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-inboundexternallink.html#cfn-rtbfabric-inboundexternallink-gatewayid
        '''
        result = self._values.get("gateway_id")
        assert result is not None, "Required property 'gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_log_settings(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkLogSettingsProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-inboundexternallink.html#cfn-rtbfabric-inboundexternallink-linklogsettings
        '''
        result = self._values.get("link_log_settings")
        assert result is not None, "Required property 'link_log_settings' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkLogSettingsProperty"], result)

    @builtins.property
    def link_attributes(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkAttributesProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-inboundexternallink.html#cfn-rtbfabric-inboundexternallink-linkattributes
        '''
        result = self._values.get("link_attributes")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnInboundExternalLink.LinkAttributesProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags to assign to the Link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-inboundexternallink.html#cfn-rtbfabric-inboundexternallink-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInboundExternalLinkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ILinkRef_1c71e733, _ITaggableV2_4e6798f8)
class CfnLink(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink",
):
    '''Creates a new link between gateways.

    Establishes a connection that allows gateways to communicate and exchange bid requests and responses.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-link.html
    :cloudformationResource: AWS::RTBFabric::Link
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rtbfabric as rtbfabric
        
        cfn_link = rtbfabric.CfnLink(self, "MyCfnLink",
            gateway_id="gatewayId",
            link_log_settings=rtbfabric.CfnLink.LinkLogSettingsProperty(
                application_logs=rtbfabric.CfnLink.ApplicationLogsProperty(
                    link_application_log_sampling=rtbfabric.CfnLink.LinkApplicationLogSamplingProperty(
                        error_log=123,
                        filter_log=123
                    )
                )
            ),
            peer_gateway_id="peerGatewayId",
        
            # the properties below are optional
            http_responder_allowed=False,
            link_attributes=rtbfabric.CfnLink.LinkAttributesProperty(
                customer_provided_id="customerProvidedId",
                responder_error_masking=[rtbfabric.CfnLink.ResponderErrorMaskingForHttpCodeProperty(
                    action="action",
                    http_code="httpCode",
                    logging_types=["loggingTypes"],
        
                    # the properties below are optional
                    response_logging_percentage=123
                )]
            ),
            module_configuration_list=[rtbfabric.CfnLink.ModuleConfigurationProperty(
                name="name",
        
                # the properties below are optional
                depends_on=["dependsOn"],
                module_parameters=rtbfabric.CfnLink.ModuleParametersProperty(
                    no_bid=rtbfabric.CfnLink.NoBidModuleParametersProperty(
                        pass_through_percentage=123,
                        reason="reason",
                        reason_code=123
                    ),
                    open_rtb_attribute=rtbfabric.CfnLink.OpenRtbAttributeModuleParametersProperty(
                        action=rtbfabric.CfnLink.ActionProperty(
                            header_tag=rtbfabric.CfnLink.HeaderTagActionProperty(
                                name="name",
                                value="value"
                            ),
                            no_bid=rtbfabric.CfnLink.NoBidActionProperty(
                                no_bid_reason_code=123
                            )
                        ),
                        filter_configuration=[rtbfabric.CfnLink.FilterProperty(
                            criteria=[rtbfabric.CfnLink.FilterCriterionProperty(
                                path="path",
                                values=["values"]
                            )]
                        )],
                        filter_type="filterType",
                        holdback_percentage=123
                    )
                ),
                version="version"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        gateway_id: builtins.str,
        link_log_settings: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.LinkLogSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        peer_gateway_id: builtins.str,
        http_responder_allowed: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        link_attributes: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.LinkAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        module_configuration_list: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.ModuleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::RTBFabric::Link``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param gateway_id: The unique identifier of the gateway.
        :param link_log_settings: Settings for the application logs.
        :param peer_gateway_id: The unique identifier of the peer gateway.
        :param http_responder_allowed: Boolean to specify if an HTTP responder is allowed.
        :param link_attributes: Attributes of the link.
        :param module_configuration_list: 
        :param tags: A map of the key-value pairs of the tag or tags to assign to the resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33e403b84fbb081fd16a0097272c1b774ceb7dfcf2ef00e8d7edb2e0fe7cec74)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLinkProps(
            gateway_id=gateway_id,
            link_log_settings=link_log_settings,
            peer_gateway_id=peer_gateway_id,
            http_responder_allowed=http_responder_allowed,
            link_attributes=link_attributes,
            module_configuration_list=module_configuration_list,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForLink")
    @builtins.classmethod
    def arn_for_link(cls, resource: "_ILinkRef_1c71e733") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8441d9ec3f0e33dc15a6b6f9feae93734b736d627e3b8c39efcec62db2104c90)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForLink", [resource]))

    @jsii.member(jsii_name="isCfnLink")
    @builtins.classmethod
    def is_cfn_link(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnLink.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8c5e17bdd0c74102b57d33eeaaf08efbc39f50454b30bdc54f29e0df1e47e9)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnLink", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc9bc5027acac07a275a06b167f0f8790f36a2fef049c4c738abc9a498a67b72)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3d7d7182ae1421ce2250b4c41ee061920faaa9e8beb8ee36659bc44bfca4d7c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrLinkDirection")
    def attr_link_direction(self) -> builtins.str:
        '''
        :cloudformationAttribute: LinkDirection
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkDirection"))

    @builtins.property
    @jsii.member(jsii_name="attrLinkId")
    def attr_link_id(self) -> builtins.str:
        '''The unique identifier of the link.

        :cloudformationAttribute: LinkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkId"))

    @builtins.property
    @jsii.member(jsii_name="attrLinkStatus")
    def attr_link_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: LinkStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedTimestamp")
    def attr_updated_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="linkRef")
    def link_ref(self) -> "_LinkReference_a62a8bc7":
        '''A reference to a Link resource.'''
        return typing.cast("_LinkReference_a62a8bc7", jsii.get(self, "linkRef"))

    @builtins.property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> builtins.str:
        '''The unique identifier of the gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "gatewayId"))

    @gateway_id.setter
    def gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd77fe8e257ed257fd9cc2835f29e82e4e5c9092b9320846e746cb8385d83132)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="linkLogSettings")
    def link_log_settings(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnLink.LinkLogSettingsProperty"]:
        '''Settings for the application logs.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLink.LinkLogSettingsProperty"], jsii.get(self, "linkLogSettings"))

    @link_log_settings.setter
    def link_log_settings(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnLink.LinkLogSettingsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab7e556ca0c98de786d1067094aa52ffc4810802cdeabb970d57fd2e6e7032cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkLogSettings", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="peerGatewayId")
    def peer_gateway_id(self) -> builtins.str:
        '''The unique identifier of the peer gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "peerGatewayId"))

    @peer_gateway_id.setter
    def peer_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1e08aa7186c8b3f2bcce904bac17f4f0dffb3848b35af4cb2707c3ecf5fdc87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerGatewayId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="httpResponderAllowed")
    def http_responder_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Boolean to specify if an HTTP responder is allowed.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "httpResponderAllowed"))

    @http_responder_allowed.setter
    def http_responder_allowed(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48b3206215bae9d2e48e79793f9ffd87062a4b1724e8972850cbacafec752632)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpResponderAllowed", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="linkAttributes")
    def link_attributes(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.LinkAttributesProperty"]]:
        '''Attributes of the link.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.LinkAttributesProperty"]], jsii.get(self, "linkAttributes"))

    @link_attributes.setter
    def link_attributes(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.LinkAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1ab4741f8f8f4356c5390e467941454f9741185b5834e0d5c912d2df062bb22)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkAttributes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="moduleConfigurationList")
    def module_configuration_list(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.ModuleConfigurationProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.ModuleConfigurationProperty"]]]], jsii.get(self, "moduleConfigurationList"))

    @module_configuration_list.setter
    def module_configuration_list(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.ModuleConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfe068c99595620eaa7b9882ede77a4ac9cf63b8112fdeb95ec82ba2220f47c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "moduleConfigurationList", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A map of the key-value pairs of the tag or tags to assign to the resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89f50ed2507493ec960d7f22a7f5e59b8cd846866c52a44638fb170da225c31a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"header_tag": "headerTag", "no_bid": "noBid"},
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            header_tag: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.HeaderTagActionProperty", typing.Dict[builtins.str, typing.Any]]],
            no_bid: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.NoBidActionProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Describes a bid action.

            :param header_tag: Describes the header tag for a bid action.
            :param no_bid: Describes the parameters of a no bid module.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                action_property = rtbfabric.CfnLink.ActionProperty(
                    header_tag=rtbfabric.CfnLink.HeaderTagActionProperty(
                        name="name",
                        value="value"
                    ),
                    no_bid=rtbfabric.CfnLink.NoBidActionProperty(
                        no_bid_reason_code=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d6894eb0ca15bfc1becb971f044daaafc323280b5c36040bf05b97a7db16c1c6)
                check_type(argname="argument header_tag", value=header_tag, expected_type=type_hints["header_tag"])
                check_type(argname="argument no_bid", value=no_bid, expected_type=type_hints["no_bid"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "header_tag": header_tag,
                "no_bid": no_bid,
            }

        @builtins.property
        def header_tag(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnLink.HeaderTagActionProperty"]:
            '''Describes the header tag for a bid action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-action.html#cfn-rtbfabric-link-action-headertag
            '''
            result = self._values.get("header_tag")
            assert result is not None, "Required property 'header_tag' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLink.HeaderTagActionProperty"], result)

        @builtins.property
        def no_bid(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnLink.NoBidActionProperty"]:
            '''Describes the parameters of a no bid module.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-action.html#cfn-rtbfabric-link-action-nobid
            '''
            result = self._values.get("no_bid")
            assert result is not None, "Required property 'no_bid' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLink.NoBidActionProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.ApplicationLogsProperty",
        jsii_struct_bases=[],
        name_mapping={"link_application_log_sampling": "linkApplicationLogSampling"},
    )
    class ApplicationLogsProperty:
        def __init__(
            self,
            *,
            link_application_log_sampling: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.LinkApplicationLogSamplingProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Describes the configuration of a link application log.

            :param link_application_log_sampling: Describes a link application log sample.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-applicationlogs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                application_logs_property = rtbfabric.CfnLink.ApplicationLogsProperty(
                    link_application_log_sampling=rtbfabric.CfnLink.LinkApplicationLogSamplingProperty(
                        error_log=123,
                        filter_log=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__386c1f58d2f3cd26972e49e1d069f69cd28a5e0106e1e75cdd6b149047a40486)
                check_type(argname="argument link_application_log_sampling", value=link_application_log_sampling, expected_type=type_hints["link_application_log_sampling"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "link_application_log_sampling": link_application_log_sampling,
            }

        @builtins.property
        def link_application_log_sampling(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnLink.LinkApplicationLogSamplingProperty"]:
            '''Describes a link application log sample.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-applicationlogs.html#cfn-rtbfabric-link-applicationlogs-linkapplicationlogsampling
            '''
            result = self._values.get("link_application_log_sampling")
            assert result is not None, "Required property 'link_application_log_sampling' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLink.LinkApplicationLogSamplingProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationLogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.FilterCriterionProperty",
        jsii_struct_bases=[],
        name_mapping={"path": "path", "values": "values"},
    )
    class FilterCriterionProperty:
        def __init__(
            self,
            *,
            path: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''Describes the criteria for a filter.

            :param path: The path to filter.
            :param values: The value to filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-filtercriterion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                filter_criterion_property = rtbfabric.CfnLink.FilterCriterionProperty(
                    path="path",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__976a810fd8399ef10076aa8ff21db3814228728d51cbe483206baf947e14d22a)
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "path": path,
                "values": values,
            }

        @builtins.property
        def path(self) -> builtins.str:
            '''The path to filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-filtercriterion.html#cfn-rtbfabric-link-filtercriterion-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The value to filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-filtercriterion.html#cfn-rtbfabric-link-filtercriterion-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterCriterionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"criteria": "criteria"},
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            criteria: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.FilterCriterionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Describes the configuration of a filter.

            :param criteria: Describes the criteria for a filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                filter_property = rtbfabric.CfnLink.FilterProperty(
                    criteria=[rtbfabric.CfnLink.FilterCriterionProperty(
                        path="path",
                        values=["values"]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bcc0e2535e30885c51d63b7ca099b67d5c103991ad0d521226fd949185ecf18a)
                check_type(argname="argument criteria", value=criteria, expected_type=type_hints["criteria"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "criteria": criteria,
            }

        @builtins.property
        def criteria(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.FilterCriterionProperty"]]]:
            '''Describes the criteria for a filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-filter.html#cfn-rtbfabric-link-filter-criteria
            '''
            result = self._values.get("criteria")
            assert result is not None, "Required property 'criteria' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.FilterCriterionProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.HeaderTagActionProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class HeaderTagActionProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''Describes the header tag for a bid action.

            :param name: The name of the bid action.
            :param value: The value of the bid action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-headertagaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                header_tag_action_property = rtbfabric.CfnLink.HeaderTagActionProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48d14abad5b3d72432a046c98d69a1dbaed71327059ccfad80adc96630cb3dd4)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the bid action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-headertagaction.html#cfn-rtbfabric-link-headertagaction-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of the bid action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-headertagaction.html#cfn-rtbfabric-link-headertagaction-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HeaderTagActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.LinkApplicationLogSamplingProperty",
        jsii_struct_bases=[],
        name_mapping={"error_log": "errorLog", "filter_log": "filterLog"},
    )
    class LinkApplicationLogSamplingProperty:
        def __init__(self, *, error_log: jsii.Number, filter_log: jsii.Number) -> None:
            '''Describes a link application log sample.

            :param error_log: An error log entry.
            :param filter_log: A filter log entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-linkapplicationlogsampling.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                link_application_log_sampling_property = rtbfabric.CfnLink.LinkApplicationLogSamplingProperty(
                    error_log=123,
                    filter_log=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc1221d9bdb6ac10224d2e809d5a57a5e79c1624f9b25a6d8868856fb5441212)
                check_type(argname="argument error_log", value=error_log, expected_type=type_hints["error_log"])
                check_type(argname="argument filter_log", value=filter_log, expected_type=type_hints["filter_log"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "error_log": error_log,
                "filter_log": filter_log,
            }

        @builtins.property
        def error_log(self) -> jsii.Number:
            '''An error log entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-linkapplicationlogsampling.html#cfn-rtbfabric-link-linkapplicationlogsampling-errorlog
            '''
            result = self._values.get("error_log")
            assert result is not None, "Required property 'error_log' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def filter_log(self) -> jsii.Number:
            '''A filter log entry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-linkapplicationlogsampling.html#cfn-rtbfabric-link-linkapplicationlogsampling-filterlog
            '''
            result = self._values.get("filter_log")
            assert result is not None, "Required property 'filter_log' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinkApplicationLogSamplingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.LinkAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_provided_id": "customerProvidedId",
            "responder_error_masking": "responderErrorMasking",
        },
    )
    class LinkAttributesProperty:
        def __init__(
            self,
            *,
            customer_provided_id: typing.Optional[builtins.str] = None,
            responder_error_masking: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.ResponderErrorMaskingForHttpCodeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Describes the attributes of a link.

            :param customer_provided_id: The customer-provided unique identifier of the link.
            :param responder_error_masking: Describes the masking for HTTP error codes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-linkattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                link_attributes_property = rtbfabric.CfnLink.LinkAttributesProperty(
                    customer_provided_id="customerProvidedId",
                    responder_error_masking=[rtbfabric.CfnLink.ResponderErrorMaskingForHttpCodeProperty(
                        action="action",
                        http_code="httpCode",
                        logging_types=["loggingTypes"],
                
                        # the properties below are optional
                        response_logging_percentage=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d88f2ed7a2e18d0a7f048f2648cd6744718ec16fcf5c0c157a303ced0fe42a8)
                check_type(argname="argument customer_provided_id", value=customer_provided_id, expected_type=type_hints["customer_provided_id"])
                check_type(argname="argument responder_error_masking", value=responder_error_masking, expected_type=type_hints["responder_error_masking"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_provided_id is not None:
                self._values["customer_provided_id"] = customer_provided_id
            if responder_error_masking is not None:
                self._values["responder_error_masking"] = responder_error_masking

        @builtins.property
        def customer_provided_id(self) -> typing.Optional[builtins.str]:
            '''The customer-provided unique identifier of the link.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-linkattributes.html#cfn-rtbfabric-link-linkattributes-customerprovidedid
            '''
            result = self._values.get("customer_provided_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def responder_error_masking(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.ResponderErrorMaskingForHttpCodeProperty"]]]]:
            '''Describes the masking for HTTP error codes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-linkattributes.html#cfn-rtbfabric-link-linkattributes-respondererrormasking
            '''
            result = self._values.get("responder_error_masking")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.ResponderErrorMaskingForHttpCodeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinkAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.LinkLogSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"application_logs": "applicationLogs"},
    )
    class LinkLogSettingsProperty:
        def __init__(
            self,
            *,
            application_logs: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.ApplicationLogsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Describes the settings for a link log.

            :param application_logs: Describes the configuration of a link application log.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-linklogsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                link_log_settings_property = rtbfabric.CfnLink.LinkLogSettingsProperty(
                    application_logs=rtbfabric.CfnLink.ApplicationLogsProperty(
                        link_application_log_sampling=rtbfabric.CfnLink.LinkApplicationLogSamplingProperty(
                            error_log=123,
                            filter_log=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e62485742cc7a54f6e2603b3db9f4a68a14d224e255f6337f68e83e4464ec0de)
                check_type(argname="argument application_logs", value=application_logs, expected_type=type_hints["application_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_logs": application_logs,
            }

        @builtins.property
        def application_logs(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnLink.ApplicationLogsProperty"]:
            '''Describes the configuration of a link application log.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-linklogsettings.html#cfn-rtbfabric-link-linklogsettings-applicationlogs
            '''
            result = self._values.get("application_logs")
            assert result is not None, "Required property 'application_logs' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLink.ApplicationLogsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinkLogSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.ModuleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "depends_on": "dependsOn",
            "module_parameters": "moduleParameters",
            "version": "version",
        },
    )
    class ModuleConfigurationProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            depends_on: typing.Optional[typing.Sequence[builtins.str]] = None,
            module_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.ModuleParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the configuration of a module.

            :param name: The name of the module.
            :param depends_on: The dependencies of the module.
            :param module_parameters: Describes the parameters of a module.
            :param version: The version of the module.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-moduleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                module_configuration_property = rtbfabric.CfnLink.ModuleConfigurationProperty(
                    name="name",
                
                    # the properties below are optional
                    depends_on=["dependsOn"],
                    module_parameters=rtbfabric.CfnLink.ModuleParametersProperty(
                        no_bid=rtbfabric.CfnLink.NoBidModuleParametersProperty(
                            pass_through_percentage=123,
                            reason="reason",
                            reason_code=123
                        ),
                        open_rtb_attribute=rtbfabric.CfnLink.OpenRtbAttributeModuleParametersProperty(
                            action=rtbfabric.CfnLink.ActionProperty(
                                header_tag=rtbfabric.CfnLink.HeaderTagActionProperty(
                                    name="name",
                                    value="value"
                                ),
                                no_bid=rtbfabric.CfnLink.NoBidActionProperty(
                                    no_bid_reason_code=123
                                )
                            ),
                            filter_configuration=[rtbfabric.CfnLink.FilterProperty(
                                criteria=[rtbfabric.CfnLink.FilterCriterionProperty(
                                    path="path",
                                    values=["values"]
                                )]
                            )],
                            filter_type="filterType",
                            holdback_percentage=123
                        )
                    ),
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__82be0aba67824a4714ca848063dd6c387779b7a60080807fbc17ba6f58442821)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
                check_type(argname="argument module_parameters", value=module_parameters, expected_type=type_hints["module_parameters"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if depends_on is not None:
                self._values["depends_on"] = depends_on
            if module_parameters is not None:
                self._values["module_parameters"] = module_parameters
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the module.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-moduleconfiguration.html#cfn-rtbfabric-link-moduleconfiguration-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def depends_on(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The dependencies of the module.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-moduleconfiguration.html#cfn-rtbfabric-link-moduleconfiguration-dependson
            '''
            result = self._values.get("depends_on")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def module_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.ModuleParametersProperty"]]:
            '''Describes the parameters of a module.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-moduleconfiguration.html#cfn-rtbfabric-link-moduleconfiguration-moduleparameters
            '''
            result = self._values.get("module_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.ModuleParametersProperty"]], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version of the module.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-moduleconfiguration.html#cfn-rtbfabric-link-moduleconfiguration-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModuleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.ModuleParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"no_bid": "noBid", "open_rtb_attribute": "openRtbAttribute"},
    )
    class ModuleParametersProperty:
        def __init__(
            self,
            *,
            no_bid: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.NoBidModuleParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            open_rtb_attribute: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.OpenRtbAttributeModuleParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the parameters of a module.

            :param no_bid: Describes the parameters of a no bid module.
            :param open_rtb_attribute: Describes the parameters of an open RTB attribute module.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-moduleparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                module_parameters_property = rtbfabric.CfnLink.ModuleParametersProperty(
                    no_bid=rtbfabric.CfnLink.NoBidModuleParametersProperty(
                        pass_through_percentage=123,
                        reason="reason",
                        reason_code=123
                    ),
                    open_rtb_attribute=rtbfabric.CfnLink.OpenRtbAttributeModuleParametersProperty(
                        action=rtbfabric.CfnLink.ActionProperty(
                            header_tag=rtbfabric.CfnLink.HeaderTagActionProperty(
                                name="name",
                                value="value"
                            ),
                            no_bid=rtbfabric.CfnLink.NoBidActionProperty(
                                no_bid_reason_code=123
                            )
                        ),
                        filter_configuration=[rtbfabric.CfnLink.FilterProperty(
                            criteria=[rtbfabric.CfnLink.FilterCriterionProperty(
                                path="path",
                                values=["values"]
                            )]
                        )],
                        filter_type="filterType",
                        holdback_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__910c77dbedb644758dff1f600f9a05ab181cc893c92bc153462d376122dba51d)
                check_type(argname="argument no_bid", value=no_bid, expected_type=type_hints["no_bid"])
                check_type(argname="argument open_rtb_attribute", value=open_rtb_attribute, expected_type=type_hints["open_rtb_attribute"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if no_bid is not None:
                self._values["no_bid"] = no_bid
            if open_rtb_attribute is not None:
                self._values["open_rtb_attribute"] = open_rtb_attribute

        @builtins.property
        def no_bid(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.NoBidModuleParametersProperty"]]:
            '''Describes the parameters of a no bid module.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-moduleparameters.html#cfn-rtbfabric-link-moduleparameters-nobid
            '''
            result = self._values.get("no_bid")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.NoBidModuleParametersProperty"]], result)

        @builtins.property
        def open_rtb_attribute(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.OpenRtbAttributeModuleParametersProperty"]]:
            '''Describes the parameters of an open RTB attribute module.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-moduleparameters.html#cfn-rtbfabric-link-moduleparameters-openrtbattribute
            '''
            result = self._values.get("open_rtb_attribute")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.OpenRtbAttributeModuleParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ModuleParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.NoBidActionProperty",
        jsii_struct_bases=[],
        name_mapping={"no_bid_reason_code": "noBidReasonCode"},
    )
    class NoBidActionProperty:
        def __init__(
            self,
            *,
            no_bid_reason_code: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes a no bid action.

            :param no_bid_reason_code: The reason code for the no bid action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-nobidaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                no_bid_action_property = rtbfabric.CfnLink.NoBidActionProperty(
                    no_bid_reason_code=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d808313ff4cbeeb74cf4ac496addde75cf42f9a64b0c9069d77342b5f26420c6)
                check_type(argname="argument no_bid_reason_code", value=no_bid_reason_code, expected_type=type_hints["no_bid_reason_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if no_bid_reason_code is not None:
                self._values["no_bid_reason_code"] = no_bid_reason_code

        @builtins.property
        def no_bid_reason_code(self) -> typing.Optional[jsii.Number]:
            '''The reason code for the no bid action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-nobidaction.html#cfn-rtbfabric-link-nobidaction-nobidreasoncode
            '''
            result = self._values.get("no_bid_reason_code")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NoBidActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.NoBidModuleParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pass_through_percentage": "passThroughPercentage",
            "reason": "reason",
            "reason_code": "reasonCode",
        },
    )
    class NoBidModuleParametersProperty:
        def __init__(
            self,
            *,
            pass_through_percentage: typing.Optional[jsii.Number] = None,
            reason: typing.Optional[builtins.str] = None,
            reason_code: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the parameters of a no bid module.

            :param pass_through_percentage: The pass through percentage.
            :param reason: The reason description.
            :param reason_code: The reason code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-nobidmoduleparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                no_bid_module_parameters_property = rtbfabric.CfnLink.NoBidModuleParametersProperty(
                    pass_through_percentage=123,
                    reason="reason",
                    reason_code=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__65534e5849f21132ce42911f7b88232db1b4cc75a5d56fc3c669b59b4d829b0c)
                check_type(argname="argument pass_through_percentage", value=pass_through_percentage, expected_type=type_hints["pass_through_percentage"])
                check_type(argname="argument reason", value=reason, expected_type=type_hints["reason"])
                check_type(argname="argument reason_code", value=reason_code, expected_type=type_hints["reason_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if pass_through_percentage is not None:
                self._values["pass_through_percentage"] = pass_through_percentage
            if reason is not None:
                self._values["reason"] = reason
            if reason_code is not None:
                self._values["reason_code"] = reason_code

        @builtins.property
        def pass_through_percentage(self) -> typing.Optional[jsii.Number]:
            '''The pass through percentage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-nobidmoduleparameters.html#cfn-rtbfabric-link-nobidmoduleparameters-passthroughpercentage
            '''
            result = self._values.get("pass_through_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def reason(self) -> typing.Optional[builtins.str]:
            '''The reason description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-nobidmoduleparameters.html#cfn-rtbfabric-link-nobidmoduleparameters-reason
            '''
            result = self._values.get("reason")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def reason_code(self) -> typing.Optional[jsii.Number]:
            '''The reason code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-nobidmoduleparameters.html#cfn-rtbfabric-link-nobidmoduleparameters-reasoncode
            '''
            result = self._values.get("reason_code")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NoBidModuleParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.OpenRtbAttributeModuleParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "filter_configuration": "filterConfiguration",
            "filter_type": "filterType",
            "holdback_percentage": "holdbackPercentage",
        },
    )
    class OpenRtbAttributeModuleParametersProperty:
        def __init__(
            self,
            *,
            action: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.ActionProperty", typing.Dict[builtins.str, typing.Any]]],
            filter_configuration: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.FilterProperty", typing.Dict[builtins.str, typing.Any]]]]],
            filter_type: builtins.str,
            holdback_percentage: jsii.Number,
        ) -> None:
            '''Describes the parameters of an open RTB attribute module.

            :param action: Describes a bid action.
            :param filter_configuration: Describes the configuration of a filter.
            :param filter_type: The filter type.
            :param holdback_percentage: The hold back percentage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-openrtbattributemoduleparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                open_rtb_attribute_module_parameters_property = rtbfabric.CfnLink.OpenRtbAttributeModuleParametersProperty(
                    action=rtbfabric.CfnLink.ActionProperty(
                        header_tag=rtbfabric.CfnLink.HeaderTagActionProperty(
                            name="name",
                            value="value"
                        ),
                        no_bid=rtbfabric.CfnLink.NoBidActionProperty(
                            no_bid_reason_code=123
                        )
                    ),
                    filter_configuration=[rtbfabric.CfnLink.FilterProperty(
                        criteria=[rtbfabric.CfnLink.FilterCriterionProperty(
                            path="path",
                            values=["values"]
                        )]
                    )],
                    filter_type="filterType",
                    holdback_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0027d94142f38aa037892e813fefe1e1f6b9ef3d7a8927dcb4fe8fe3340158c5)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument filter_configuration", value=filter_configuration, expected_type=type_hints["filter_configuration"])
                check_type(argname="argument filter_type", value=filter_type, expected_type=type_hints["filter_type"])
                check_type(argname="argument holdback_percentage", value=holdback_percentage, expected_type=type_hints["holdback_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "filter_configuration": filter_configuration,
                "filter_type": filter_type,
                "holdback_percentage": holdback_percentage,
            }

        @builtins.property
        def action(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnLink.ActionProperty"]:
            '''Describes a bid action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-openrtbattributemoduleparameters.html#cfn-rtbfabric-link-openrtbattributemoduleparameters-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLink.ActionProperty"], result)

        @builtins.property
        def filter_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.FilterProperty"]]]:
            '''Describes the configuration of a filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-openrtbattributemoduleparameters.html#cfn-rtbfabric-link-openrtbattributemoduleparameters-filterconfiguration
            '''
            result = self._values.get("filter_configuration")
            assert result is not None, "Required property 'filter_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.FilterProperty"]]], result)

        @builtins.property
        def filter_type(self) -> builtins.str:
            '''The filter type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-openrtbattributemoduleparameters.html#cfn-rtbfabric-link-openrtbattributemoduleparameters-filtertype
            '''
            result = self._values.get("filter_type")
            assert result is not None, "Required property 'filter_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def holdback_percentage(self) -> jsii.Number:
            '''The hold back percentage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-openrtbattributemoduleparameters.html#cfn-rtbfabric-link-openrtbattributemoduleparameters-holdbackpercentage
            '''
            result = self._values.get("holdback_percentage")
            assert result is not None, "Required property 'holdback_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OpenRtbAttributeModuleParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLink.ResponderErrorMaskingForHttpCodeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "http_code": "httpCode",
            "logging_types": "loggingTypes",
            "response_logging_percentage": "responseLoggingPercentage",
        },
    )
    class ResponderErrorMaskingForHttpCodeProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            http_code: builtins.str,
            logging_types: typing.Sequence[builtins.str],
            response_logging_percentage: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the masking for HTTP error codes.

            :param action: The action for the error..
            :param http_code: The HTTP error code.
            :param logging_types: The error log type.
            :param response_logging_percentage: The percentage of response logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-respondererrormaskingforhttpcode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                responder_error_masking_for_http_code_property = rtbfabric.CfnLink.ResponderErrorMaskingForHttpCodeProperty(
                    action="action",
                    http_code="httpCode",
                    logging_types=["loggingTypes"],
                
                    # the properties below are optional
                    response_logging_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7a4d5a36bb204668cc9f3235d69b4d6dd33abe2f27737729656b5fd767fe6fcb)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument http_code", value=http_code, expected_type=type_hints["http_code"])
                check_type(argname="argument logging_types", value=logging_types, expected_type=type_hints["logging_types"])
                check_type(argname="argument response_logging_percentage", value=response_logging_percentage, expected_type=type_hints["response_logging_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "http_code": http_code,
                "logging_types": logging_types,
            }
            if response_logging_percentage is not None:
                self._values["response_logging_percentage"] = response_logging_percentage

        @builtins.property
        def action(self) -> builtins.str:
            '''The action for the error..

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-respondererrormaskingforhttpcode.html#cfn-rtbfabric-link-respondererrormaskingforhttpcode-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def http_code(self) -> builtins.str:
            '''The HTTP error code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-respondererrormaskingforhttpcode.html#cfn-rtbfabric-link-respondererrormaskingforhttpcode-httpcode
            '''
            result = self._values.get("http_code")
            assert result is not None, "Required property 'http_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def logging_types(self) -> typing.List[builtins.str]:
            '''The error log type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-respondererrormaskingforhttpcode.html#cfn-rtbfabric-link-respondererrormaskingforhttpcode-loggingtypes
            '''
            result = self._values.get("logging_types")
            assert result is not None, "Required property 'logging_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def response_logging_percentage(self) -> typing.Optional[jsii.Number]:
            '''The percentage of response logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-link-respondererrormaskingforhttpcode.html#cfn-rtbfabric-link-respondererrormaskingforhttpcode-responseloggingpercentage
            '''
            result = self._values.get("response_logging_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResponderErrorMaskingForHttpCodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rtbfabric.CfnLinkProps",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_id": "gatewayId",
        "link_log_settings": "linkLogSettings",
        "peer_gateway_id": "peerGatewayId",
        "http_responder_allowed": "httpResponderAllowed",
        "link_attributes": "linkAttributes",
        "module_configuration_list": "moduleConfigurationList",
        "tags": "tags",
    },
)
class CfnLinkProps:
    def __init__(
        self,
        *,
        gateway_id: builtins.str,
        link_log_settings: typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.LinkLogSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        peer_gateway_id: builtins.str,
        http_responder_allowed: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        link_attributes: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.LinkAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        module_configuration_list: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnLink.ModuleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLink``.

        :param gateway_id: The unique identifier of the gateway.
        :param link_log_settings: Settings for the application logs.
        :param peer_gateway_id: The unique identifier of the peer gateway.
        :param http_responder_allowed: Boolean to specify if an HTTP responder is allowed.
        :param link_attributes: Attributes of the link.
        :param module_configuration_list: 
        :param tags: A map of the key-value pairs of the tag or tags to assign to the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-link.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rtbfabric as rtbfabric
            
            cfn_link_props = rtbfabric.CfnLinkProps(
                gateway_id="gatewayId",
                link_log_settings=rtbfabric.CfnLink.LinkLogSettingsProperty(
                    application_logs=rtbfabric.CfnLink.ApplicationLogsProperty(
                        link_application_log_sampling=rtbfabric.CfnLink.LinkApplicationLogSamplingProperty(
                            error_log=123,
                            filter_log=123
                        )
                    )
                ),
                peer_gateway_id="peerGatewayId",
            
                # the properties below are optional
                http_responder_allowed=False,
                link_attributes=rtbfabric.CfnLink.LinkAttributesProperty(
                    customer_provided_id="customerProvidedId",
                    responder_error_masking=[rtbfabric.CfnLink.ResponderErrorMaskingForHttpCodeProperty(
                        action="action",
                        http_code="httpCode",
                        logging_types=["loggingTypes"],
            
                        # the properties below are optional
                        response_logging_percentage=123
                    )]
                ),
                module_configuration_list=[rtbfabric.CfnLink.ModuleConfigurationProperty(
                    name="name",
            
                    # the properties below are optional
                    depends_on=["dependsOn"],
                    module_parameters=rtbfabric.CfnLink.ModuleParametersProperty(
                        no_bid=rtbfabric.CfnLink.NoBidModuleParametersProperty(
                            pass_through_percentage=123,
                            reason="reason",
                            reason_code=123
                        ),
                        open_rtb_attribute=rtbfabric.CfnLink.OpenRtbAttributeModuleParametersProperty(
                            action=rtbfabric.CfnLink.ActionProperty(
                                header_tag=rtbfabric.CfnLink.HeaderTagActionProperty(
                                    name="name",
                                    value="value"
                                ),
                                no_bid=rtbfabric.CfnLink.NoBidActionProperty(
                                    no_bid_reason_code=123
                                )
                            ),
                            filter_configuration=[rtbfabric.CfnLink.FilterProperty(
                                criteria=[rtbfabric.CfnLink.FilterCriterionProperty(
                                    path="path",
                                    values=["values"]
                                )]
                            )],
                            filter_type="filterType",
                            holdback_percentage=123
                        )
                    ),
                    version="version"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__012c58c752deffb32adb9b9c3e8a29a8373d9f395d7e2679c67f05f37f77812a)
            check_type(argname="argument gateway_id", value=gateway_id, expected_type=type_hints["gateway_id"])
            check_type(argname="argument link_log_settings", value=link_log_settings, expected_type=type_hints["link_log_settings"])
            check_type(argname="argument peer_gateway_id", value=peer_gateway_id, expected_type=type_hints["peer_gateway_id"])
            check_type(argname="argument http_responder_allowed", value=http_responder_allowed, expected_type=type_hints["http_responder_allowed"])
            check_type(argname="argument link_attributes", value=link_attributes, expected_type=type_hints["link_attributes"])
            check_type(argname="argument module_configuration_list", value=module_configuration_list, expected_type=type_hints["module_configuration_list"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_id": gateway_id,
            "link_log_settings": link_log_settings,
            "peer_gateway_id": peer_gateway_id,
        }
        if http_responder_allowed is not None:
            self._values["http_responder_allowed"] = http_responder_allowed
        if link_attributes is not None:
            self._values["link_attributes"] = link_attributes
        if module_configuration_list is not None:
            self._values["module_configuration_list"] = module_configuration_list
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def gateway_id(self) -> builtins.str:
        '''The unique identifier of the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-link.html#cfn-rtbfabric-link-gatewayid
        '''
        result = self._values.get("gateway_id")
        assert result is not None, "Required property 'gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_log_settings(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnLink.LinkLogSettingsProperty"]:
        '''Settings for the application logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-link.html#cfn-rtbfabric-link-linklogsettings
        '''
        result = self._values.get("link_log_settings")
        assert result is not None, "Required property 'link_log_settings' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnLink.LinkLogSettingsProperty"], result)

    @builtins.property
    def peer_gateway_id(self) -> builtins.str:
        '''The unique identifier of the peer gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-link.html#cfn-rtbfabric-link-peergatewayid
        '''
        result = self._values.get("peer_gateway_id")
        assert result is not None, "Required property 'peer_gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def http_responder_allowed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Boolean to specify if an HTTP responder is allowed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-link.html#cfn-rtbfabric-link-httpresponderallowed
        '''
        result = self._values.get("http_responder_allowed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def link_attributes(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.LinkAttributesProperty"]]:
        '''Attributes of the link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-link.html#cfn-rtbfabric-link-linkattributes
        '''
        result = self._values.get("link_attributes")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnLink.LinkAttributesProperty"]], result)

    @builtins.property
    def module_configuration_list(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.ModuleConfigurationProperty"]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-link.html#cfn-rtbfabric-link-moduleconfigurationlist
        '''
        result = self._values.get("module_configuration_list")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnLink.ModuleConfigurationProperty"]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A map of the key-value pairs of the tag or tags to assign to the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-link.html#cfn-rtbfabric-link-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLinkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IOutboundExternalLinkRef_06bb6289, _ITaggableV2_4e6798f8)
class CfnOutboundExternalLink(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rtbfabric.CfnOutboundExternalLink",
):
    '''Resource Type definition for AWS::RTBFabric::OutboundExternalLink Resource Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-outboundexternallink.html
    :cloudformationResource: AWS::RTBFabric::OutboundExternalLink
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rtbfabric as rtbfabric
        
        cfn_outbound_external_link = rtbfabric.CfnOutboundExternalLink(self, "MyCfnOutboundExternalLink",
            gateway_id="gatewayId",
            link_log_settings=rtbfabric.CfnOutboundExternalLink.LinkLogSettingsProperty(
                application_logs=rtbfabric.CfnOutboundExternalLink.ApplicationLogsProperty(
                    link_application_log_sampling=rtbfabric.CfnOutboundExternalLink.LinkApplicationLogSamplingProperty(
                        error_log=123,
                        filter_log=123
                    )
                )
            ),
            public_endpoint="publicEndpoint",
        
            # the properties below are optional
            link_attributes=rtbfabric.CfnOutboundExternalLink.LinkAttributesProperty(
                customer_provided_id="customerProvidedId",
                responder_error_masking=[rtbfabric.CfnOutboundExternalLink.ResponderErrorMaskingForHttpCodeProperty(
                    action="action",
                    http_code="httpCode",
                    logging_types=["loggingTypes"],
        
                    # the properties below are optional
                    response_logging_percentage=123
                )]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        gateway_id: builtins.str,
        link_log_settings: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOutboundExternalLink.LinkLogSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        public_endpoint: builtins.str,
        link_attributes: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOutboundExternalLink.LinkAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::RTBFabric::OutboundExternalLink``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param gateway_id: 
        :param link_log_settings: 
        :param public_endpoint: 
        :param link_attributes: 
        :param tags: Tags to assign to the Link.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b83212e7efe505cb3ee08383229ed92a52ff4ae1914a3bae275aa32769a538f2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOutboundExternalLinkProps(
            gateway_id=gateway_id,
            link_log_settings=link_log_settings,
            public_endpoint=public_endpoint,
            link_attributes=link_attributes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForOutboundExternalLink")
    @builtins.classmethod
    def arn_for_outbound_external_link(
        cls,
        resource: "_IOutboundExternalLinkRef_06bb6289",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f750d09898fee559d9d8fea7e122b94e612d5000fc57a92e18a8f25e09f82fa3)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForOutboundExternalLink", [resource]))

    @jsii.member(jsii_name="isCfnOutboundExternalLink")
    @builtins.classmethod
    def is_cfn_outbound_external_link(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnOutboundExternalLink.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646cbb509a7c181366f50146e6d34dd1709c05a1bf1bee7ca9c1268e384db068)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnOutboundExternalLink", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94c554a77d3e3ec5d6846c452288c7fd3554604db45d13548cbe1057b1390676)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d29126bce97e6163947ad92cc93367b86d9ba45647deac7343b697994a0b0353)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrLinkId")
    def attr_link_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: LinkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkId"))

    @builtins.property
    @jsii.member(jsii_name="attrLinkStatus")
    def attr_link_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: LinkStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLinkStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedTimestamp")
    def attr_updated_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="outboundExternalLinkRef")
    def outbound_external_link_ref(self) -> "_OutboundExternalLinkReference_b1d46069":
        '''A reference to a OutboundExternalLink resource.'''
        return typing.cast("_OutboundExternalLinkReference_b1d46069", jsii.get(self, "outboundExternalLinkRef"))

    @builtins.property
    @jsii.member(jsii_name="gatewayId")
    def gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gatewayId"))

    @gateway_id.setter
    def gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__238843eabee398c3632a13fa1c1960dac944a8392e27b87e031688ea7cdf1ec6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="linkLogSettings")
    def link_log_settings(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkLogSettingsProperty"]:
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkLogSettingsProperty"], jsii.get(self, "linkLogSettings"))

    @link_log_settings.setter
    def link_log_settings(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkLogSettingsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26f049e3b14063d70306af34d8e4502f4010b3af3beefbbccf55ef545809a845)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkLogSettings", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="publicEndpoint")
    def public_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicEndpoint"))

    @public_endpoint.setter
    def public_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e4fb1b12fa9b92810ee792acd6f261cddb5b628377308f8f917d480acc5055)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicEndpoint", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="linkAttributes")
    def link_attributes(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkAttributesProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkAttributesProperty"]], jsii.get(self, "linkAttributes"))

    @link_attributes.setter
    def link_attributes(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6db7a26ace700bb14301fd54fb67deca8e1afc5000c0c296662435bef28b3372)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkAttributes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags to assign to the Link.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67ca7cd3c98009f70e07dfe4c683484c616d5a03de5ece23f5b3f87bdc80d986)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnOutboundExternalLink.ApplicationLogsProperty",
        jsii_struct_bases=[],
        name_mapping={"link_application_log_sampling": "linkApplicationLogSampling"},
    )
    class ApplicationLogsProperty:
        def __init__(
            self,
            *,
            link_application_log_sampling: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOutboundExternalLink.LinkApplicationLogSamplingProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param link_application_log_sampling: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-applicationlogs.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                application_logs_property = rtbfabric.CfnOutboundExternalLink.ApplicationLogsProperty(
                    link_application_log_sampling=rtbfabric.CfnOutboundExternalLink.LinkApplicationLogSamplingProperty(
                        error_log=123,
                        filter_log=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a9b229edccbdfb67f4339c40a0ca2e3b00d4634b2837ac239db564cec3868684)
                check_type(argname="argument link_application_log_sampling", value=link_application_log_sampling, expected_type=type_hints["link_application_log_sampling"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "link_application_log_sampling": link_application_log_sampling,
            }

        @builtins.property
        def link_application_log_sampling(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkApplicationLogSamplingProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-applicationlogs.html#cfn-rtbfabric-outboundexternallink-applicationlogs-linkapplicationlogsampling
            '''
            result = self._values.get("link_application_log_sampling")
            assert result is not None, "Required property 'link_application_log_sampling' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkApplicationLogSamplingProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationLogsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnOutboundExternalLink.LinkApplicationLogSamplingProperty",
        jsii_struct_bases=[],
        name_mapping={"error_log": "errorLog", "filter_log": "filterLog"},
    )
    class LinkApplicationLogSamplingProperty:
        def __init__(self, *, error_log: jsii.Number, filter_log: jsii.Number) -> None:
            '''
            :param error_log: 
            :param filter_log: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-linkapplicationlogsampling.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                link_application_log_sampling_property = rtbfabric.CfnOutboundExternalLink.LinkApplicationLogSamplingProperty(
                    error_log=123,
                    filter_log=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4795d6d14a69cfacf0369b73be38f15dc83058bfc07f12af59548536cd71d175)
                check_type(argname="argument error_log", value=error_log, expected_type=type_hints["error_log"])
                check_type(argname="argument filter_log", value=filter_log, expected_type=type_hints["filter_log"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "error_log": error_log,
                "filter_log": filter_log,
            }

        @builtins.property
        def error_log(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-linkapplicationlogsampling.html#cfn-rtbfabric-outboundexternallink-linkapplicationlogsampling-errorlog
            '''
            result = self._values.get("error_log")
            assert result is not None, "Required property 'error_log' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def filter_log(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-linkapplicationlogsampling.html#cfn-rtbfabric-outboundexternallink-linkapplicationlogsampling-filterlog
            '''
            result = self._values.get("filter_log")
            assert result is not None, "Required property 'filter_log' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinkApplicationLogSamplingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnOutboundExternalLink.LinkAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "customer_provided_id": "customerProvidedId",
            "responder_error_masking": "responderErrorMasking",
        },
    )
    class LinkAttributesProperty:
        def __init__(
            self,
            *,
            customer_provided_id: typing.Optional[builtins.str] = None,
            responder_error_masking: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOutboundExternalLink.ResponderErrorMaskingForHttpCodeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param customer_provided_id: 
            :param responder_error_masking: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-linkattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                link_attributes_property = rtbfabric.CfnOutboundExternalLink.LinkAttributesProperty(
                    customer_provided_id="customerProvidedId",
                    responder_error_masking=[rtbfabric.CfnOutboundExternalLink.ResponderErrorMaskingForHttpCodeProperty(
                        action="action",
                        http_code="httpCode",
                        logging_types=["loggingTypes"],
                
                        # the properties below are optional
                        response_logging_percentage=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ab7f89fad048d65160fee1cdd9ee351aa26472e598659007bfb8a25a6c2f20a8)
                check_type(argname="argument customer_provided_id", value=customer_provided_id, expected_type=type_hints["customer_provided_id"])
                check_type(argname="argument responder_error_masking", value=responder_error_masking, expected_type=type_hints["responder_error_masking"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if customer_provided_id is not None:
                self._values["customer_provided_id"] = customer_provided_id
            if responder_error_masking is not None:
                self._values["responder_error_masking"] = responder_error_masking

        @builtins.property
        def customer_provided_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-linkattributes.html#cfn-rtbfabric-outboundexternallink-linkattributes-customerprovidedid
            '''
            result = self._values.get("customer_provided_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def responder_error_masking(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.ResponderErrorMaskingForHttpCodeProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-linkattributes.html#cfn-rtbfabric-outboundexternallink-linkattributes-respondererrormasking
            '''
            result = self._values.get("responder_error_masking")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.ResponderErrorMaskingForHttpCodeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinkAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnOutboundExternalLink.LinkLogSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"application_logs": "applicationLogs"},
    )
    class LinkLogSettingsProperty:
        def __init__(
            self,
            *,
            application_logs: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOutboundExternalLink.ApplicationLogsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param application_logs: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-linklogsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                link_log_settings_property = rtbfabric.CfnOutboundExternalLink.LinkLogSettingsProperty(
                    application_logs=rtbfabric.CfnOutboundExternalLink.ApplicationLogsProperty(
                        link_application_log_sampling=rtbfabric.CfnOutboundExternalLink.LinkApplicationLogSamplingProperty(
                            error_log=123,
                            filter_log=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__52c438d627d877d014a66c5800991149741928cee0830d167e9a92376109f1fb)
                check_type(argname="argument application_logs", value=application_logs, expected_type=type_hints["application_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_logs": application_logs,
            }

        @builtins.property
        def application_logs(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.ApplicationLogsProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-linklogsettings.html#cfn-rtbfabric-outboundexternallink-linklogsettings-applicationlogs
            '''
            result = self._values.get("application_logs")
            assert result is not None, "Required property 'application_logs' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.ApplicationLogsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LinkLogSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnOutboundExternalLink.ResponderErrorMaskingForHttpCodeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "http_code": "httpCode",
            "logging_types": "loggingTypes",
            "response_logging_percentage": "responseLoggingPercentage",
        },
    )
    class ResponderErrorMaskingForHttpCodeProperty:
        def __init__(
            self,
            *,
            action: builtins.str,
            http_code: builtins.str,
            logging_types: typing.Sequence[builtins.str],
            response_logging_percentage: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param action: 
            :param http_code: 
            :param logging_types: 
            :param response_logging_percentage: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                responder_error_masking_for_http_code_property = rtbfabric.CfnOutboundExternalLink.ResponderErrorMaskingForHttpCodeProperty(
                    action="action",
                    http_code="httpCode",
                    logging_types=["loggingTypes"],
                
                    # the properties below are optional
                    response_logging_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c24dd49b3cfd077aaf0d4d437d27cc349742733f2fbf408918f211c3c1ebbe81)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument http_code", value=http_code, expected_type=type_hints["http_code"])
                check_type(argname="argument logging_types", value=logging_types, expected_type=type_hints["logging_types"])
                check_type(argname="argument response_logging_percentage", value=response_logging_percentage, expected_type=type_hints["response_logging_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "http_code": http_code,
                "logging_types": logging_types,
            }
            if response_logging_percentage is not None:
                self._values["response_logging_percentage"] = response_logging_percentage

        @builtins.property
        def action(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode.html#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def http_code(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode.html#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-httpcode
            '''
            result = self._values.get("http_code")
            assert result is not None, "Required property 'http_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def logging_types(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode.html#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-loggingtypes
            '''
            result = self._values.get("logging_types")
            assert result is not None, "Required property 'logging_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def response_logging_percentage(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode.html#cfn-rtbfabric-outboundexternallink-respondererrormaskingforhttpcode-responseloggingpercentage
            '''
            result = self._values.get("response_logging_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResponderErrorMaskingForHttpCodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rtbfabric.CfnOutboundExternalLinkProps",
    jsii_struct_bases=[],
    name_mapping={
        "gateway_id": "gatewayId",
        "link_log_settings": "linkLogSettings",
        "public_endpoint": "publicEndpoint",
        "link_attributes": "linkAttributes",
        "tags": "tags",
    },
)
class CfnOutboundExternalLinkProps:
    def __init__(
        self,
        *,
        gateway_id: builtins.str,
        link_log_settings: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOutboundExternalLink.LinkLogSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        public_endpoint: builtins.str,
        link_attributes: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOutboundExternalLink.LinkAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOutboundExternalLink``.

        :param gateway_id: 
        :param link_log_settings: 
        :param public_endpoint: 
        :param link_attributes: 
        :param tags: Tags to assign to the Link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-outboundexternallink.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rtbfabric as rtbfabric
            
            cfn_outbound_external_link_props = rtbfabric.CfnOutboundExternalLinkProps(
                gateway_id="gatewayId",
                link_log_settings=rtbfabric.CfnOutboundExternalLink.LinkLogSettingsProperty(
                    application_logs=rtbfabric.CfnOutboundExternalLink.ApplicationLogsProperty(
                        link_application_log_sampling=rtbfabric.CfnOutboundExternalLink.LinkApplicationLogSamplingProperty(
                            error_log=123,
                            filter_log=123
                        )
                    )
                ),
                public_endpoint="publicEndpoint",
            
                # the properties below are optional
                link_attributes=rtbfabric.CfnOutboundExternalLink.LinkAttributesProperty(
                    customer_provided_id="customerProvidedId",
                    responder_error_masking=[rtbfabric.CfnOutboundExternalLink.ResponderErrorMaskingForHttpCodeProperty(
                        action="action",
                        http_code="httpCode",
                        logging_types=["loggingTypes"],
            
                        # the properties below are optional
                        response_logging_percentage=123
                    )]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c76a09410a4a7820f14f2f07d663bc52013017381c28be06dd077613ba2c9385)
            check_type(argname="argument gateway_id", value=gateway_id, expected_type=type_hints["gateway_id"])
            check_type(argname="argument link_log_settings", value=link_log_settings, expected_type=type_hints["link_log_settings"])
            check_type(argname="argument public_endpoint", value=public_endpoint, expected_type=type_hints["public_endpoint"])
            check_type(argname="argument link_attributes", value=link_attributes, expected_type=type_hints["link_attributes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gateway_id": gateway_id,
            "link_log_settings": link_log_settings,
            "public_endpoint": public_endpoint,
        }
        if link_attributes is not None:
            self._values["link_attributes"] = link_attributes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def gateway_id(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-outboundexternallink.html#cfn-rtbfabric-outboundexternallink-gatewayid
        '''
        result = self._values.get("gateway_id")
        assert result is not None, "Required property 'gateway_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_log_settings(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkLogSettingsProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-outboundexternallink.html#cfn-rtbfabric-outboundexternallink-linklogsettings
        '''
        result = self._values.get("link_log_settings")
        assert result is not None, "Required property 'link_log_settings' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkLogSettingsProperty"], result)

    @builtins.property
    def public_endpoint(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-outboundexternallink.html#cfn-rtbfabric-outboundexternallink-publicendpoint
        '''
        result = self._values.get("public_endpoint")
        assert result is not None, "Required property 'public_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def link_attributes(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkAttributesProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-outboundexternallink.html#cfn-rtbfabric-outboundexternallink-linkattributes
        '''
        result = self._values.get("link_attributes")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOutboundExternalLink.LinkAttributesProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Tags to assign to the Link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-outboundexternallink.html#cfn-rtbfabric-outboundexternallink-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOutboundExternalLinkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IRequesterGatewayRef_d92bcdf1, _ITaggableV2_4e6798f8)
class CfnRequesterGateway(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rtbfabric.CfnRequesterGateway",
):
    '''Creates a requester gateway.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-requestergateway.html
    :cloudformationResource: AWS::RTBFabric::RequesterGateway
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rtbfabric as rtbfabric
        
        cfn_requester_gateway = rtbfabric.CfnRequesterGateway(self, "MyCfnRequesterGateway",
            security_group_ids=["securityGroupIds"],
            subnet_ids=["subnetIds"],
            vpc_id="vpcId",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        security_group_ids: typing.Sequence[typing.Union[builtins.str, "_ISecurityGroupRef_efa4ff18"]],
        subnet_ids: typing.Sequence[typing.Union[builtins.str, "_ISubnetRef_ac31e361"]],
        vpc_id: typing.Union[builtins.str, "_IVPCRef_f02a11df"],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::RTBFabric::RequesterGateway``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param security_group_ids: The unique identifiers of the security groups.
        :param subnet_ids: The unique identifiers of the subnets.
        :param vpc_id: The unique identifier of the Virtual Private Cloud (VPC).
        :param description: An optional description for the requester gateway.
        :param tags: A map of the key-value pairs of the tag or tags to assign to the resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f422ad74a878dd27ca273fe5fdb545d09c78a5ac256926db3df20c37e5494bcb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRequesterGatewayProps(
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForRequesterGateway")
    @builtins.classmethod
    def arn_for_requester_gateway(
        cls,
        resource: "_IRequesterGatewayRef_d92bcdf1",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfb862aae5f5ac5590b2e30cf6f7bd41dd788937fd184bc1afb6341c0375ea45)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForRequesterGateway", [resource]))

    @jsii.member(jsii_name="isCfnRequesterGateway")
    @builtins.classmethod
    def is_cfn_requester_gateway(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnRequesterGateway.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a9f5f2b085719975110c2c7cb3f46a272d19779c29aef9df8c208a56ded5141)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnRequesterGateway", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff35377957678a6c2c4554293556ba81f1ce2d415c840e7f565c3446b4392dd1)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5192ae4e650c287601015b07667412e24e64d55cbffc8ba03a9951b18d4480a0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrActiveLinksCount")
    def attr_active_links_count(self) -> jsii.Number:
        '''
        :cloudformationAttribute: ActiveLinksCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrActiveLinksCount"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''
        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayId")
    def attr_gateway_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: GatewayId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="attrRequesterGatewayStatus")
    def attr_requester_gateway_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: RequesterGatewayStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRequesterGatewayStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTotalLinksCount")
    def attr_total_links_count(self) -> jsii.Number:
        '''
        :cloudformationAttribute: TotalLinksCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrTotalLinksCount"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedTimestamp")
    def attr_updated_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="requesterGatewayRef")
    def requester_gateway_ref(self) -> "_RequesterGatewayReference_37e2965b":
        '''A reference to a RequesterGateway resource.'''
        return typing.cast("_RequesterGatewayReference_37e2965b", jsii.get(self, "requesterGatewayRef"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''The unique identifiers of the security groups.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ebd08ccd1118e6cce91167680f27e015cb9bcf5d9ff0aa2d840a6df61c14a67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The unique identifiers of the subnets.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04b0e885e38fc98486a407608eacb33c3b7349d40d018eb2a470fcca945931d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The unique identifier of the Virtual Private Cloud (VPC).'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__959c859af931f75a012fecdc9ac3acb6011d7aafb80c1e781b35c1cd405e51ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the requester gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1760b22a44b3e180e50000774882d4780c0aa85c37c931f50882d305890c95b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A map of the key-value pairs of the tag or tags to assign to the resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d27ee86984f1ea979cd85d326d12ed9f60279e658da842a417dc4a27e2ba07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rtbfabric.CfnRequesterGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "description": "description",
        "tags": "tags",
    },
)
class CfnRequesterGatewayProps:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[typing.Union[builtins.str, "_ISecurityGroupRef_efa4ff18"]],
        subnet_ids: typing.Sequence[typing.Union[builtins.str, "_ISubnetRef_ac31e361"]],
        vpc_id: typing.Union[builtins.str, "_IVPCRef_f02a11df"],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRequesterGateway``.

        :param security_group_ids: The unique identifiers of the security groups.
        :param subnet_ids: The unique identifiers of the subnets.
        :param vpc_id: The unique identifier of the Virtual Private Cloud (VPC).
        :param description: An optional description for the requester gateway.
        :param tags: A map of the key-value pairs of the tag or tags to assign to the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-requestergateway.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rtbfabric as rtbfabric
            
            cfn_requester_gateway_props = rtbfabric.CfnRequesterGatewayProps(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                vpc_id="vpcId",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e861505bd65d62c115117db14bdc56cdccfb7c596f849bc81dadfc3f63484f16)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def security_group_ids(
        self,
    ) -> typing.List[typing.Union[builtins.str, "_ISecurityGroupRef_efa4ff18"]]:
        '''The unique identifiers of the security groups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-requestergateway.html#cfn-rtbfabric-requestergateway-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[typing.Union[builtins.str, "_ISecurityGroupRef_efa4ff18"]], result)

    @builtins.property
    def subnet_ids(
        self,
    ) -> typing.List[typing.Union[builtins.str, "_ISubnetRef_ac31e361"]]:
        '''The unique identifiers of the subnets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-requestergateway.html#cfn-rtbfabric-requestergateway-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[typing.Union[builtins.str, "_ISubnetRef_ac31e361"]], result)

    @builtins.property
    def vpc_id(self) -> typing.Union[builtins.str, "_IVPCRef_f02a11df"]:
        '''The unique identifier of the Virtual Private Cloud (VPC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-requestergateway.html#cfn-rtbfabric-requestergateway-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(typing.Union[builtins.str, "_IVPCRef_f02a11df"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the requester gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-requestergateway.html#cfn-rtbfabric-requestergateway-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A map of the key-value pairs of the tag or tags to assign to the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-requestergateway.html#cfn-rtbfabric-requestergateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRequesterGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IResponderGatewayRef_2bdaa070, _ITaggableV2_4e6798f8)
class CfnResponderGateway(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rtbfabric.CfnResponderGateway",
):
    '''Creates a responder gateway.

    .. epigraph::

       A domain name or managed endpoint is required.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html
    :cloudformationResource: AWS::RTBFabric::ResponderGateway
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rtbfabric as rtbfabric
        
        cfn_responder_gateway = rtbfabric.CfnResponderGateway(self, "MyCfnResponderGateway",
            port=123,
            protocol="protocol",
            security_group_ids=["securityGroupIds"],
            subnet_ids=["subnetIds"],
            vpc_id="vpcId",
        
            # the properties below are optional
            description="description",
            domain_name="domainName",
            managed_endpoint_configuration=rtbfabric.CfnResponderGateway.ManagedEndpointConfigurationProperty(
                auto_scaling_groups_configuration=rtbfabric.CfnResponderGateway.AutoScalingGroupsConfigurationProperty(
                    auto_scaling_group_name_list=["autoScalingGroupNameList"],
                    role_arn="roleArn"
                ),
                eks_endpoints_configuration=rtbfabric.CfnResponderGateway.EksEndpointsConfigurationProperty(
                    cluster_api_server_ca_certificate_chain="clusterApiServerCaCertificateChain",
                    cluster_api_server_endpoint_uri="clusterApiServerEndpointUri",
                    cluster_name="clusterName",
                    endpoints_resource_name="endpointsResourceName",
                    endpoints_resource_namespace="endpointsResourceNamespace",
                    role_arn="roleArn"
                )
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            trust_store_configuration=rtbfabric.CfnResponderGateway.TrustStoreConfigurationProperty(
                certificate_authority_certificates=["certificateAuthorityCertificates"]
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        port: jsii.Number,
        protocol: builtins.str,
        security_group_ids: typing.Sequence[typing.Union[builtins.str, "_ISecurityGroupRef_efa4ff18"]],
        subnet_ids: typing.Sequence[typing.Union[builtins.str, "_ISubnetRef_ac31e361"]],
        vpc_id: typing.Union[builtins.str, "_IVPCRef_f02a11df"],
        description: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        managed_endpoint_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnResponderGateway.ManagedEndpointConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        trust_store_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnResponderGateway.TrustStoreConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::RTBFabric::ResponderGateway``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param port: The networking port to use.
        :param protocol: The networking protocol to use.
        :param security_group_ids: The unique identifiers of the security groups.
        :param subnet_ids: The unique identifiers of the subnets.
        :param vpc_id: The unique identifier of the Virtual Private Cloud (VPC).
        :param description: An optional description for the responder gateway.
        :param domain_name: The domain name for the responder gateway.
        :param managed_endpoint_configuration: The configuration for the managed endpoint.
        :param tags: A map of the key-value pairs of the tag or tags to assign to the resource.
        :param trust_store_configuration: The configuration of the trust store.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb840846f651123d9a88e886198c38a19418b49d00a405569125e9b5fc712905)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResponderGatewayProps(
            port=port,
            protocol=protocol,
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            description=description,
            domain_name=domain_name,
            managed_endpoint_configuration=managed_endpoint_configuration,
            tags=tags,
            trust_store_configuration=trust_store_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForResponderGateway")
    @builtins.classmethod
    def arn_for_responder_gateway(
        cls,
        resource: "_IResponderGatewayRef_2bdaa070",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d03c637f67985067e0671715031f91341dab89c06faa85ff0ef8ac5fda7755ad)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForResponderGateway", [resource]))

    @jsii.member(jsii_name="isCfnResponderGateway")
    @builtins.classmethod
    def is_cfn_responder_gateway(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnResponderGateway.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b74e42482b63ce0a50334b157f355ffb0e00bd0de13bb57fe8651a695fc0591)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnResponderGateway", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa2d13378cd55a42c745c0d3be558c5fe2209a8b5cd2de4699daa917018a45ff)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d93a404d017510da5888259e354ed9c153e827b5cf5f6d4ed51228828f69ab75)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTimestamp")
    def attr_created_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayId")
    def attr_gateway_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: GatewayId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="attrResponderGatewayStatus")
    def attr_responder_gateway_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: ResponderGatewayStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrResponderGatewayStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedTimestamp")
    def attr_updated_timestamp(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="responderGatewayRef")
    def responder_gateway_ref(self) -> "_ResponderGatewayReference_a8195bef":
        '''A reference to a ResponderGateway resource.'''
        return typing.cast("_ResponderGatewayReference_a8195bef", jsii.get(self, "responderGatewayRef"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        '''The networking port to use.'''
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__529ad6abfea2d47fdb6a4a85f0fa7ef44fe2dbb4cbce65f2a407af20ca308aff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        '''The networking protocol to use.'''
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de24b3918fda3107ad9b83c4fdf476736a5649552d61ca740a55c6f384f156d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''The unique identifiers of the security groups.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5807c201752fa8e41be9823d45b5e600b8b8957e00a7a2e746adf30a456151bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The unique identifiers of the subnets.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ca836d5fd162d5f81d5073a4c116fe81c8566c9b5abc50f51ed6984246da273)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The unique identifier of the Virtual Private Cloud (VPC).'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44015d889f5b99adbe6056ed6c8499be47c63f2c6c4914c9ad7283aacd918861)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the responder gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e6878cd3f2c8e8e361bc8d2c86209d26a1fb58fbe2d62b7edf129a163c2a858)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''The domain name for the responder gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__661744fbbe0ebbf7d0da02d43ad93534aa4716cfe31f0ca98ac17ceaff284331)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="managedEndpointConfiguration")
    def managed_endpoint_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.ManagedEndpointConfigurationProperty"]]:
        '''The configuration for the managed endpoint.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.ManagedEndpointConfigurationProperty"]], jsii.get(self, "managedEndpointConfiguration"))

    @managed_endpoint_configuration.setter
    def managed_endpoint_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.ManagedEndpointConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c62d5b7a0422ed5598bd291abfbec31946d1749e58220bce6017e5e6847b5c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedEndpointConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A map of the key-value pairs of the tag or tags to assign to the resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78481e43a5f64482056245022052cc21592112a8a52dc33921b1d7faf64c9cfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="trustStoreConfiguration")
    def trust_store_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.TrustStoreConfigurationProperty"]]:
        '''The configuration of the trust store.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.TrustStoreConfigurationProperty"]], jsii.get(self, "trustStoreConfiguration"))

    @trust_store_configuration.setter
    def trust_store_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.TrustStoreConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c35e12d72dbcce9576ddf9d51543995e06e6fe3b33fbd82dac8f968d6d8a2ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustStoreConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnResponderGateway.AutoScalingGroupsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_scaling_group_name_list": "autoScalingGroupNameList",
            "role_arn": "roleArn",
        },
    )
    class AutoScalingGroupsConfigurationProperty:
        def __init__(
            self,
            *,
            auto_scaling_group_name_list: typing.Sequence[builtins.str],
            role_arn: builtins.str,
        ) -> None:
            '''Describes the configuration of an auto scaling group.

            :param auto_scaling_group_name_list: The names of the auto scaling group.
            :param role_arn: The role ARN of the auto scaling group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-autoscalinggroupsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                auto_scaling_groups_configuration_property = rtbfabric.CfnResponderGateway.AutoScalingGroupsConfigurationProperty(
                    auto_scaling_group_name_list=["autoScalingGroupNameList"],
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d1c95602d43fb8271931e505ccc184bd0ec122d89dad878b15fd318423cdc0a5)
                check_type(argname="argument auto_scaling_group_name_list", value=auto_scaling_group_name_list, expected_type=type_hints["auto_scaling_group_name_list"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "auto_scaling_group_name_list": auto_scaling_group_name_list,
                "role_arn": role_arn,
            }

        @builtins.property
        def auto_scaling_group_name_list(self) -> typing.List[builtins.str]:
            '''The names of the auto scaling group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-autoscalinggroupsconfiguration.html#cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-autoscalinggroupnamelist
            '''
            result = self._values.get("auto_scaling_group_name_list")
            assert result is not None, "Required property 'auto_scaling_group_name_list' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The role ARN of the auto scaling group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-autoscalinggroupsconfiguration.html#cfn-rtbfabric-respondergateway-autoscalinggroupsconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingGroupsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnResponderGateway.EksEndpointsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cluster_api_server_ca_certificate_chain": "clusterApiServerCaCertificateChain",
            "cluster_api_server_endpoint_uri": "clusterApiServerEndpointUri",
            "cluster_name": "clusterName",
            "endpoints_resource_name": "endpointsResourceName",
            "endpoints_resource_namespace": "endpointsResourceNamespace",
            "role_arn": "roleArn",
        },
    )
    class EksEndpointsConfigurationProperty:
        def __init__(
            self,
            *,
            cluster_api_server_ca_certificate_chain: builtins.str,
            cluster_api_server_endpoint_uri: builtins.str,
            cluster_name: builtins.str,
            endpoints_resource_name: builtins.str,
            endpoints_resource_namespace: builtins.str,
            role_arn: builtins.str,
        ) -> None:
            '''Describes the configuration of an Amazon Elastic Kubernetes Service endpoint.

            :param cluster_api_server_ca_certificate_chain: The CA certificate chain of the cluster API server.
            :param cluster_api_server_endpoint_uri: The URI of the cluster API server endpoint.
            :param cluster_name: The name of the cluster.
            :param endpoints_resource_name: The name of the endpoint resource.
            :param endpoints_resource_namespace: The namespace of the endpoint resource.
            :param role_arn: The role ARN for the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                eks_endpoints_configuration_property = rtbfabric.CfnResponderGateway.EksEndpointsConfigurationProperty(
                    cluster_api_server_ca_certificate_chain="clusterApiServerCaCertificateChain",
                    cluster_api_server_endpoint_uri="clusterApiServerEndpointUri",
                    cluster_name="clusterName",
                    endpoints_resource_name="endpointsResourceName",
                    endpoints_resource_namespace="endpointsResourceNamespace",
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c39d19c6d36879baafff96889064035f106253849fe63133370a9cd6384f8f1)
                check_type(argname="argument cluster_api_server_ca_certificate_chain", value=cluster_api_server_ca_certificate_chain, expected_type=type_hints["cluster_api_server_ca_certificate_chain"])
                check_type(argname="argument cluster_api_server_endpoint_uri", value=cluster_api_server_endpoint_uri, expected_type=type_hints["cluster_api_server_endpoint_uri"])
                check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
                check_type(argname="argument endpoints_resource_name", value=endpoints_resource_name, expected_type=type_hints["endpoints_resource_name"])
                check_type(argname="argument endpoints_resource_namespace", value=endpoints_resource_namespace, expected_type=type_hints["endpoints_resource_namespace"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_api_server_ca_certificate_chain": cluster_api_server_ca_certificate_chain,
                "cluster_api_server_endpoint_uri": cluster_api_server_endpoint_uri,
                "cluster_name": cluster_name,
                "endpoints_resource_name": endpoints_resource_name,
                "endpoints_resource_namespace": endpoints_resource_namespace,
                "role_arn": role_arn,
            }

        @builtins.property
        def cluster_api_server_ca_certificate_chain(self) -> builtins.str:
            '''The CA certificate chain of the cluster API server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration.html#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clusterapiservercacertificatechain
            '''
            result = self._values.get("cluster_api_server_ca_certificate_chain")
            assert result is not None, "Required property 'cluster_api_server_ca_certificate_chain' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cluster_api_server_endpoint_uri(self) -> builtins.str:
            '''The URI of the cluster API server endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration.html#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clusterapiserverendpointuri
            '''
            result = self._values.get("cluster_api_server_endpoint_uri")
            assert result is not None, "Required property 'cluster_api_server_endpoint_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cluster_name(self) -> builtins.str:
            '''The name of the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration.html#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-clustername
            '''
            result = self._values.get("cluster_name")
            assert result is not None, "Required property 'cluster_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def endpoints_resource_name(self) -> builtins.str:
            '''The name of the endpoint resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration.html#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-endpointsresourcename
            '''
            result = self._values.get("endpoints_resource_name")
            assert result is not None, "Required property 'endpoints_resource_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def endpoints_resource_namespace(self) -> builtins.str:
            '''The namespace of the endpoint resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration.html#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-endpointsresourcenamespace
            '''
            result = self._values.get("endpoints_resource_namespace")
            assert result is not None, "Required property 'endpoints_resource_namespace' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The role ARN for the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-eksendpointsconfiguration.html#cfn-rtbfabric-respondergateway-eksendpointsconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksEndpointsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnResponderGateway.ManagedEndpointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_scaling_groups_configuration": "autoScalingGroupsConfiguration",
            "eks_endpoints_configuration": "eksEndpointsConfiguration",
        },
    )
    class ManagedEndpointConfigurationProperty:
        def __init__(
            self,
            *,
            auto_scaling_groups_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnResponderGateway.AutoScalingGroupsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            eks_endpoints_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnResponderGateway.EksEndpointsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the configuration of a managed endpoint.

            :param auto_scaling_groups_configuration: Describes the configuration of an auto scaling group.
            :param eks_endpoints_configuration: Describes the configuration of an Amazon Elastic Kubernetes Service endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-managedendpointconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                managed_endpoint_configuration_property = rtbfabric.CfnResponderGateway.ManagedEndpointConfigurationProperty(
                    auto_scaling_groups_configuration=rtbfabric.CfnResponderGateway.AutoScalingGroupsConfigurationProperty(
                        auto_scaling_group_name_list=["autoScalingGroupNameList"],
                        role_arn="roleArn"
                    ),
                    eks_endpoints_configuration=rtbfabric.CfnResponderGateway.EksEndpointsConfigurationProperty(
                        cluster_api_server_ca_certificate_chain="clusterApiServerCaCertificateChain",
                        cluster_api_server_endpoint_uri="clusterApiServerEndpointUri",
                        cluster_name="clusterName",
                        endpoints_resource_name="endpointsResourceName",
                        endpoints_resource_namespace="endpointsResourceNamespace",
                        role_arn="roleArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ec35a25a4306a45d1288fed4ad734e82e67a0cf2e49ef915d8568d687b0c56ee)
                check_type(argname="argument auto_scaling_groups_configuration", value=auto_scaling_groups_configuration, expected_type=type_hints["auto_scaling_groups_configuration"])
                check_type(argname="argument eks_endpoints_configuration", value=eks_endpoints_configuration, expected_type=type_hints["eks_endpoints_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auto_scaling_groups_configuration is not None:
                self._values["auto_scaling_groups_configuration"] = auto_scaling_groups_configuration
            if eks_endpoints_configuration is not None:
                self._values["eks_endpoints_configuration"] = eks_endpoints_configuration

        @builtins.property
        def auto_scaling_groups_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.AutoScalingGroupsConfigurationProperty"]]:
            '''Describes the configuration of an auto scaling group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-managedendpointconfiguration.html#cfn-rtbfabric-respondergateway-managedendpointconfiguration-autoscalinggroupsconfiguration
            '''
            result = self._values.get("auto_scaling_groups_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.AutoScalingGroupsConfigurationProperty"]], result)

        @builtins.property
        def eks_endpoints_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.EksEndpointsConfigurationProperty"]]:
            '''Describes the configuration of an Amazon Elastic Kubernetes Service endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-managedendpointconfiguration.html#cfn-rtbfabric-respondergateway-managedendpointconfiguration-eksendpointsconfiguration
            '''
            result = self._values.get("eks_endpoints_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.EksEndpointsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ManagedEndpointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rtbfabric.CfnResponderGateway.TrustStoreConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_authority_certificates": "certificateAuthorityCertificates",
        },
    )
    class TrustStoreConfigurationProperty:
        def __init__(
            self,
            *,
            certificate_authority_certificates: typing.Sequence[builtins.str],
        ) -> None:
            '''Describes the configuration of a trust store.

            :param certificate_authority_certificates: The certificate authority certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-truststoreconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rtbfabric as rtbfabric
                
                trust_store_configuration_property = rtbfabric.CfnResponderGateway.TrustStoreConfigurationProperty(
                    certificate_authority_certificates=["certificateAuthorityCertificates"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e6cdb06483a6be6c8f2015cdc677b1237ae909cbf1496feb35e652044d632315)
                check_type(argname="argument certificate_authority_certificates", value=certificate_authority_certificates, expected_type=type_hints["certificate_authority_certificates"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_authority_certificates": certificate_authority_certificates,
            }

        @builtins.property
        def certificate_authority_certificates(self) -> typing.List[builtins.str]:
            '''The certificate authority certificate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rtbfabric-respondergateway-truststoreconfiguration.html#cfn-rtbfabric-respondergateway-truststoreconfiguration-certificateauthoritycertificates
            '''
            result = self._values.get("certificate_authority_certificates")
            assert result is not None, "Required property 'certificate_authority_certificates' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrustStoreConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rtbfabric.CfnResponderGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "port": "port",
        "protocol": "protocol",
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "description": "description",
        "domain_name": "domainName",
        "managed_endpoint_configuration": "managedEndpointConfiguration",
        "tags": "tags",
        "trust_store_configuration": "trustStoreConfiguration",
    },
)
class CfnResponderGatewayProps:
    def __init__(
        self,
        *,
        port: jsii.Number,
        protocol: builtins.str,
        security_group_ids: typing.Sequence[typing.Union[builtins.str, "_ISecurityGroupRef_efa4ff18"]],
        subnet_ids: typing.Sequence[typing.Union[builtins.str, "_ISubnetRef_ac31e361"]],
        vpc_id: typing.Union[builtins.str, "_IVPCRef_f02a11df"],
        description: typing.Optional[builtins.str] = None,
        domain_name: typing.Optional[builtins.str] = None,
        managed_endpoint_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnResponderGateway.ManagedEndpointConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        trust_store_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnResponderGateway.TrustStoreConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResponderGateway``.

        :param port: The networking port to use.
        :param protocol: The networking protocol to use.
        :param security_group_ids: The unique identifiers of the security groups.
        :param subnet_ids: The unique identifiers of the subnets.
        :param vpc_id: The unique identifier of the Virtual Private Cloud (VPC).
        :param description: An optional description for the responder gateway.
        :param domain_name: The domain name for the responder gateway.
        :param managed_endpoint_configuration: The configuration for the managed endpoint.
        :param tags: A map of the key-value pairs of the tag or tags to assign to the resource.
        :param trust_store_configuration: The configuration of the trust store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rtbfabric as rtbfabric
            
            cfn_responder_gateway_props = rtbfabric.CfnResponderGatewayProps(
                port=123,
                protocol="protocol",
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                vpc_id="vpcId",
            
                # the properties below are optional
                description="description",
                domain_name="domainName",
                managed_endpoint_configuration=rtbfabric.CfnResponderGateway.ManagedEndpointConfigurationProperty(
                    auto_scaling_groups_configuration=rtbfabric.CfnResponderGateway.AutoScalingGroupsConfigurationProperty(
                        auto_scaling_group_name_list=["autoScalingGroupNameList"],
                        role_arn="roleArn"
                    ),
                    eks_endpoints_configuration=rtbfabric.CfnResponderGateway.EksEndpointsConfigurationProperty(
                        cluster_api_server_ca_certificate_chain="clusterApiServerCaCertificateChain",
                        cluster_api_server_endpoint_uri="clusterApiServerEndpointUri",
                        cluster_name="clusterName",
                        endpoints_resource_name="endpointsResourceName",
                        endpoints_resource_namespace="endpointsResourceNamespace",
                        role_arn="roleArn"
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                trust_store_configuration=rtbfabric.CfnResponderGateway.TrustStoreConfigurationProperty(
                    certificate_authority_certificates=["certificateAuthorityCertificates"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9eb5e991b472975a887a9142289f690ca12906379267bff2fae6a074009eacd)
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument managed_endpoint_configuration", value=managed_endpoint_configuration, expected_type=type_hints["managed_endpoint_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trust_store_configuration", value=trust_store_configuration, expected_type=type_hints["trust_store_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "port": port,
            "protocol": protocol,
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
        }
        if description is not None:
            self._values["description"] = description
        if domain_name is not None:
            self._values["domain_name"] = domain_name
        if managed_endpoint_configuration is not None:
            self._values["managed_endpoint_configuration"] = managed_endpoint_configuration
        if tags is not None:
            self._values["tags"] = tags
        if trust_store_configuration is not None:
            self._values["trust_store_configuration"] = trust_store_configuration

    @builtins.property
    def port(self) -> jsii.Number:
        '''The networking port to use.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html#cfn-rtbfabric-respondergateway-port
        '''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''The networking protocol to use.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html#cfn-rtbfabric-respondergateway-protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(
        self,
    ) -> typing.List[typing.Union[builtins.str, "_ISecurityGroupRef_efa4ff18"]]:
        '''The unique identifiers of the security groups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html#cfn-rtbfabric-respondergateway-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[typing.Union[builtins.str, "_ISecurityGroupRef_efa4ff18"]], result)

    @builtins.property
    def subnet_ids(
        self,
    ) -> typing.List[typing.Union[builtins.str, "_ISubnetRef_ac31e361"]]:
        '''The unique identifiers of the subnets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html#cfn-rtbfabric-respondergateway-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[typing.Union[builtins.str, "_ISubnetRef_ac31e361"]], result)

    @builtins.property
    def vpc_id(self) -> typing.Union[builtins.str, "_IVPCRef_f02a11df"]:
        '''The unique identifier of the Virtual Private Cloud (VPC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html#cfn-rtbfabric-respondergateway-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(typing.Union[builtins.str, "_IVPCRef_f02a11df"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description for the responder gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html#cfn-rtbfabric-respondergateway-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_name(self) -> typing.Optional[builtins.str]:
        '''The domain name for the responder gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html#cfn-rtbfabric-respondergateway-domainname
        '''
        result = self._values.get("domain_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed_endpoint_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.ManagedEndpointConfigurationProperty"]]:
        '''The configuration for the managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html#cfn-rtbfabric-respondergateway-managedendpointconfiguration
        '''
        result = self._values.get("managed_endpoint_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.ManagedEndpointConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A map of the key-value pairs of the tag or tags to assign to the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html#cfn-rtbfabric-respondergateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def trust_store_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.TrustStoreConfigurationProperty"]]:
        '''The configuration of the trust store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rtbfabric-respondergateway.html#cfn-rtbfabric-respondergateway-truststoreconfiguration
        '''
        result = self._values.get("trust_store_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnResponderGateway.TrustStoreConfigurationProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResponderGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnInboundExternalLink",
    "CfnInboundExternalLinkProps",
    "CfnLink",
    "CfnLinkProps",
    "CfnOutboundExternalLink",
    "CfnOutboundExternalLinkProps",
    "CfnRequesterGateway",
    "CfnRequesterGatewayProps",
    "CfnResponderGateway",
    "CfnResponderGatewayProps",
]

publication.publish()

def _typecheckingstub__1a5afae55006ef90edfe40aa8e5117e329b49d245830f9f3781bf45c5ee1d498(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    gateway_id: builtins.str,
    link_log_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInboundExternalLink.LinkLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    link_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInboundExternalLink.LinkAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e45579c24ba39e7cbd88d8a1dcb187104127b5c4c031b298b39214f40fb1a36e(
    resource: _IInboundExternalLinkRef_087c1bc6,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1943b47f9f91218da538fb23adeca699c3f23ed379e5dc88cefa0f1b8902d146(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10a4ab8875cef05923631df17dd17458d37380c77a9c313974f23f57ebce0981(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f050a879dccb667647d261549cd380d2361df83488e749feb3fb74cb71c0d0f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb7adaf4ee57468585d346f35e67e07997a1e20abf84b582fc810dff92d7e2c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf1ee8508990492f8168ad7b68f62077e25e97d32af167928f013ed58b2c4d15(
    value: typing.Union[_IResolvable_da3f097b, CfnInboundExternalLink.LinkLogSettingsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5745f3776bc1df4e80af5ddcc1b274597b1aab22d6cd1cf3d3f615d1fba4c3f7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnInboundExternalLink.LinkAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13f41f0dd733ffddc6dae564597b6fd8c0c31c02cd444ba959242500384e99aa(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a2c31093a0bae40e89e39fd987b13c3e5cb84ca6d6dc8f166577487829dc8d4(
    *,
    link_application_log_sampling: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInboundExternalLink.LinkApplicationLogSamplingProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1140756e9bc43fe93422c9e7b90ea26b4cffbc73394ce1e5eb83064206adf56f(
    *,
    error_log: jsii.Number,
    filter_log: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4ea72d051bc93d14ed2cae48b106a31ab27e9978c0bc23487c53cf7fe21dd5(
    *,
    customer_provided_id: typing.Optional[builtins.str] = None,
    responder_error_masking: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInboundExternalLink.ResponderErrorMaskingForHttpCodeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4b3acd881daca8e2c440e2d628c27b2f1ce93a4b4d05d722b1f810b3bbdeeb3(
    *,
    application_logs: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInboundExternalLink.ApplicationLogsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9aa166adda80a00eaa1e13fdf8247afcbddf7768a6b4c8415c5e4e9a9dcb5d(
    *,
    action: builtins.str,
    http_code: builtins.str,
    logging_types: typing.Sequence[builtins.str],
    response_logging_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d15a9ea48568fa6d17bb53d9622c841d5242e53e66d3e303799545a8370eb3dc(
    *,
    gateway_id: builtins.str,
    link_log_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnInboundExternalLink.LinkLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    link_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnInboundExternalLink.LinkAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33e403b84fbb081fd16a0097272c1b774ceb7dfcf2ef00e8d7edb2e0fe7cec74(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    gateway_id: builtins.str,
    link_log_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.LinkLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    peer_gateway_id: builtins.str,
    http_responder_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    link_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.LinkAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    module_configuration_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.ModuleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8441d9ec3f0e33dc15a6b6f9feae93734b736d627e3b8c39efcec62db2104c90(
    resource: _ILinkRef_1c71e733,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8c5e17bdd0c74102b57d33eeaaf08efbc39f50454b30bdc54f29e0df1e47e9(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9bc5027acac07a275a06b167f0f8790f36a2fef049c4c738abc9a498a67b72(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d7d7182ae1421ce2250b4c41ee061920faaa9e8beb8ee36659bc44bfca4d7c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd77fe8e257ed257fd9cc2835f29e82e4e5c9092b9320846e746cb8385d83132(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab7e556ca0c98de786d1067094aa52ffc4810802cdeabb970d57fd2e6e7032cc(
    value: typing.Union[_IResolvable_da3f097b, CfnLink.LinkLogSettingsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1e08aa7186c8b3f2bcce904bac17f4f0dffb3848b35af4cb2707c3ecf5fdc87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48b3206215bae9d2e48e79793f9ffd87062a4b1724e8972850cbacafec752632(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1ab4741f8f8f4356c5390e467941454f9741185b5834e0d5c912d2df062bb22(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnLink.LinkAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfe068c99595620eaa7b9882ede77a4ac9cf63b8112fdeb95ec82ba2220f47c9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnLink.ModuleConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89f50ed2507493ec960d7f22a7f5e59b8cd846866c52a44638fb170da225c31a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6894eb0ca15bfc1becb971f044daaafc323280b5c36040bf05b97a7db16c1c6(
    *,
    header_tag: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.HeaderTagActionProperty, typing.Dict[builtins.str, typing.Any]]],
    no_bid: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.NoBidActionProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__386c1f58d2f3cd26972e49e1d069f69cd28a5e0106e1e75cdd6b149047a40486(
    *,
    link_application_log_sampling: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.LinkApplicationLogSamplingProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__976a810fd8399ef10076aa8ff21db3814228728d51cbe483206baf947e14d22a(
    *,
    path: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcc0e2535e30885c51d63b7ca099b67d5c103991ad0d521226fd949185ecf18a(
    *,
    criteria: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.FilterCriterionProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d14abad5b3d72432a046c98d69a1dbaed71327059ccfad80adc96630cb3dd4(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc1221d9bdb6ac10224d2e809d5a57a5e79c1624f9b25a6d8868856fb5441212(
    *,
    error_log: jsii.Number,
    filter_log: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d88f2ed7a2e18d0a7f048f2648cd6744718ec16fcf5c0c157a303ced0fe42a8(
    *,
    customer_provided_id: typing.Optional[builtins.str] = None,
    responder_error_masking: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.ResponderErrorMaskingForHttpCodeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e62485742cc7a54f6e2603b3db9f4a68a14d224e255f6337f68e83e4464ec0de(
    *,
    application_logs: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.ApplicationLogsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82be0aba67824a4714ca848063dd6c387779b7a60080807fbc17ba6f58442821(
    *,
    name: builtins.str,
    depends_on: typing.Optional[typing.Sequence[builtins.str]] = None,
    module_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.ModuleParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__910c77dbedb644758dff1f600f9a05ab181cc893c92bc153462d376122dba51d(
    *,
    no_bid: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.NoBidModuleParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_rtb_attribute: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.OpenRtbAttributeModuleParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d808313ff4cbeeb74cf4ac496addde75cf42f9a64b0c9069d77342b5f26420c6(
    *,
    no_bid_reason_code: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65534e5849f21132ce42911f7b88232db1b4cc75a5d56fc3c669b59b4d829b0c(
    *,
    pass_through_percentage: typing.Optional[jsii.Number] = None,
    reason: typing.Optional[builtins.str] = None,
    reason_code: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0027d94142f38aa037892e813fefe1e1f6b9ef3d7a8927dcb4fe8fe3340158c5(
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    filter_configuration: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.FilterProperty, typing.Dict[builtins.str, typing.Any]]]]],
    filter_type: builtins.str,
    holdback_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a4d5a36bb204668cc9f3235d69b4d6dd33abe2f27737729656b5fd767fe6fcb(
    *,
    action: builtins.str,
    http_code: builtins.str,
    logging_types: typing.Sequence[builtins.str],
    response_logging_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__012c58c752deffb32adb9b9c3e8a29a8373d9f395d7e2679c67f05f37f77812a(
    *,
    gateway_id: builtins.str,
    link_log_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.LinkLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    peer_gateway_id: builtins.str,
    http_responder_allowed: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    link_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.LinkAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    module_configuration_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnLink.ModuleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b83212e7efe505cb3ee08383229ed92a52ff4ae1914a3bae275aa32769a538f2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    gateway_id: builtins.str,
    link_log_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOutboundExternalLink.LinkLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    public_endpoint: builtins.str,
    link_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOutboundExternalLink.LinkAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f750d09898fee559d9d8fea7e122b94e612d5000fc57a92e18a8f25e09f82fa3(
    resource: _IOutboundExternalLinkRef_06bb6289,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646cbb509a7c181366f50146e6d34dd1709c05a1bf1bee7ca9c1268e384db068(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94c554a77d3e3ec5d6846c452288c7fd3554604db45d13548cbe1057b1390676(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d29126bce97e6163947ad92cc93367b86d9ba45647deac7343b697994a0b0353(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__238843eabee398c3632a13fa1c1960dac944a8392e27b87e031688ea7cdf1ec6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26f049e3b14063d70306af34d8e4502f4010b3af3beefbbccf55ef545809a845(
    value: typing.Union[_IResolvable_da3f097b, CfnOutboundExternalLink.LinkLogSettingsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e4fb1b12fa9b92810ee792acd6f261cddb5b628377308f8f917d480acc5055(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6db7a26ace700bb14301fd54fb67deca8e1afc5000c0c296662435bef28b3372(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnOutboundExternalLink.LinkAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67ca7cd3c98009f70e07dfe4c683484c616d5a03de5ece23f5b3f87bdc80d986(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b229edccbdfb67f4339c40a0ca2e3b00d4634b2837ac239db564cec3868684(
    *,
    link_application_log_sampling: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOutboundExternalLink.LinkApplicationLogSamplingProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4795d6d14a69cfacf0369b73be38f15dc83058bfc07f12af59548536cd71d175(
    *,
    error_log: jsii.Number,
    filter_log: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab7f89fad048d65160fee1cdd9ee351aa26472e598659007bfb8a25a6c2f20a8(
    *,
    customer_provided_id: typing.Optional[builtins.str] = None,
    responder_error_masking: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOutboundExternalLink.ResponderErrorMaskingForHttpCodeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52c438d627d877d014a66c5800991149741928cee0830d167e9a92376109f1fb(
    *,
    application_logs: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOutboundExternalLink.ApplicationLogsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c24dd49b3cfd077aaf0d4d437d27cc349742733f2fbf408918f211c3c1ebbe81(
    *,
    action: builtins.str,
    http_code: builtins.str,
    logging_types: typing.Sequence[builtins.str],
    response_logging_percentage: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c76a09410a4a7820f14f2f07d663bc52013017381c28be06dd077613ba2c9385(
    *,
    gateway_id: builtins.str,
    link_log_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOutboundExternalLink.LinkLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    public_endpoint: builtins.str,
    link_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOutboundExternalLink.LinkAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f422ad74a878dd27ca273fe5fdb545d09c78a5ac256926db3df20c37e5494bcb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_group_ids: typing.Sequence[typing.Union[builtins.str, _ISecurityGroupRef_efa4ff18]],
    subnet_ids: typing.Sequence[typing.Union[builtins.str, _ISubnetRef_ac31e361]],
    vpc_id: typing.Union[builtins.str, _IVPCRef_f02a11df],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfb862aae5f5ac5590b2e30cf6f7bd41dd788937fd184bc1afb6341c0375ea45(
    resource: _IRequesterGatewayRef_d92bcdf1,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a9f5f2b085719975110c2c7cb3f46a272d19779c29aef9df8c208a56ded5141(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff35377957678a6c2c4554293556ba81f1ce2d415c840e7f565c3446b4392dd1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5192ae4e650c287601015b07667412e24e64d55cbffc8ba03a9951b18d4480a0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ebd08ccd1118e6cce91167680f27e015cb9bcf5d9ff0aa2d840a6df61c14a67(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04b0e885e38fc98486a407608eacb33c3b7349d40d018eb2a470fcca945931d4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__959c859af931f75a012fecdc9ac3acb6011d7aafb80c1e781b35c1cd405e51ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1760b22a44b3e180e50000774882d4780c0aa85c37c931f50882d305890c95b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d27ee86984f1ea979cd85d326d12ed9f60279e658da842a417dc4a27e2ba07(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e861505bd65d62c115117db14bdc56cdccfb7c596f849bc81dadfc3f63484f16(
    *,
    security_group_ids: typing.Sequence[typing.Union[builtins.str, _ISecurityGroupRef_efa4ff18]],
    subnet_ids: typing.Sequence[typing.Union[builtins.str, _ISubnetRef_ac31e361]],
    vpc_id: typing.Union[builtins.str, _IVPCRef_f02a11df],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb840846f651123d9a88e886198c38a19418b49d00a405569125e9b5fc712905(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    port: jsii.Number,
    protocol: builtins.str,
    security_group_ids: typing.Sequence[typing.Union[builtins.str, _ISecurityGroupRef_efa4ff18]],
    subnet_ids: typing.Sequence[typing.Union[builtins.str, _ISubnetRef_ac31e361]],
    vpc_id: typing.Union[builtins.str, _IVPCRef_f02a11df],
    description: typing.Optional[builtins.str] = None,
    domain_name: typing.Optional[builtins.str] = None,
    managed_endpoint_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResponderGateway.ManagedEndpointConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trust_store_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResponderGateway.TrustStoreConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d03c637f67985067e0671715031f91341dab89c06faa85ff0ef8ac5fda7755ad(
    resource: _IResponderGatewayRef_2bdaa070,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b74e42482b63ce0a50334b157f355ffb0e00bd0de13bb57fe8651a695fc0591(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa2d13378cd55a42c745c0d3be558c5fe2209a8b5cd2de4699daa917018a45ff(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d93a404d017510da5888259e354ed9c153e827b5cf5f6d4ed51228828f69ab75(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__529ad6abfea2d47fdb6a4a85f0fa7ef44fe2dbb4cbce65f2a407af20ca308aff(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de24b3918fda3107ad9b83c4fdf476736a5649552d61ca740a55c6f384f156d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5807c201752fa8e41be9823d45b5e600b8b8957e00a7a2e746adf30a456151bd(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ca836d5fd162d5f81d5073a4c116fe81c8566c9b5abc50f51ed6984246da273(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44015d889f5b99adbe6056ed6c8499be47c63f2c6c4914c9ad7283aacd918861(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e6878cd3f2c8e8e361bc8d2c86209d26a1fb58fbe2d62b7edf129a163c2a858(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__661744fbbe0ebbf7d0da02d43ad93534aa4716cfe31f0ca98ac17ceaff284331(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c62d5b7a0422ed5598bd291abfbec31946d1749e58220bce6017e5e6847b5c1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResponderGateway.ManagedEndpointConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78481e43a5f64482056245022052cc21592112a8a52dc33921b1d7faf64c9cfe(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c35e12d72dbcce9576ddf9d51543995e06e6fe3b33fbd82dac8f968d6d8a2ce(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnResponderGateway.TrustStoreConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1c95602d43fb8271931e505ccc184bd0ec122d89dad878b15fd318423cdc0a5(
    *,
    auto_scaling_group_name_list: typing.Sequence[builtins.str],
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c39d19c6d36879baafff96889064035f106253849fe63133370a9cd6384f8f1(
    *,
    cluster_api_server_ca_certificate_chain: builtins.str,
    cluster_api_server_endpoint_uri: builtins.str,
    cluster_name: builtins.str,
    endpoints_resource_name: builtins.str,
    endpoints_resource_namespace: builtins.str,
    role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec35a25a4306a45d1288fed4ad734e82e67a0cf2e49ef915d8568d687b0c56ee(
    *,
    auto_scaling_groups_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResponderGateway.AutoScalingGroupsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    eks_endpoints_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResponderGateway.EksEndpointsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6cdb06483a6be6c8f2015cdc677b1237ae909cbf1496feb35e652044d632315(
    *,
    certificate_authority_certificates: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9eb5e991b472975a887a9142289f690ca12906379267bff2fae6a074009eacd(
    *,
    port: jsii.Number,
    protocol: builtins.str,
    security_group_ids: typing.Sequence[typing.Union[builtins.str, _ISecurityGroupRef_efa4ff18]],
    subnet_ids: typing.Sequence[typing.Union[builtins.str, _ISubnetRef_ac31e361]],
    vpc_id: typing.Union[builtins.str, _IVPCRef_f02a11df],
    description: typing.Optional[builtins.str] = None,
    domain_name: typing.Optional[builtins.str] = None,
    managed_endpoint_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResponderGateway.ManagedEndpointConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trust_store_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnResponderGateway.TrustStoreConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
