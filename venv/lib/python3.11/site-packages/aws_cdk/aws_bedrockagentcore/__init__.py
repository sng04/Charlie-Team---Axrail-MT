r'''
# AWS::BedrockAgentCore Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_bedrockagentcore as bedrockagentcore
```

L2 constructs for this service are available in the [`@aws-cdk/aws-bedrock-agentcore-alpha`](https://www.npmjs.com/package/@aws-cdk/aws-bedrock-agentcore-alpha) package.

You can also use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::BedrockAgentCore resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BedrockAgentCore.html) directly.
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
from ..interfaces.aws_bedrockagentcore import (
    BrowserCustomReference as _BrowserCustomReference_ceb8fdba,
    BrowserProfileReference as _BrowserProfileReference_7d69eac7,
    CodeInterpreterCustomReference as _CodeInterpreterCustomReference_0b253bc0,
    EvaluatorReference as _EvaluatorReference_a3ac0235,
    GatewayReference as _GatewayReference_350c3a07,
    GatewayTargetReference as _GatewayTargetReference_8759ec47,
    IBrowserCustomRef as _IBrowserCustomRef_f12bfa35,
    IBrowserProfileRef as _IBrowserProfileRef_87a4b1a8,
    ICodeInterpreterCustomRef as _ICodeInterpreterCustomRef_2d5c05fb,
    IEvaluatorRef as _IEvaluatorRef_21d364d2,
    IGatewayRef as _IGatewayRef_a3ed30fe,
    IGatewayTargetRef as _IGatewayTargetRef_e3008479,
    IMemoryRef as _IMemoryRef_2d13cc89,
    IOnlineEvaluationConfigRef as _IOnlineEvaluationConfigRef_cf19cabf,
    IPolicyEngineRef as _IPolicyEngineRef_6d885cfc,
    IPolicyRef as _IPolicyRef_ceb8b108,
    IRuntimeEndpointRef as _IRuntimeEndpointRef_7a1c67f8,
    IRuntimeRef as _IRuntimeRef_00302e12,
    IWorkloadIdentityRef as _IWorkloadIdentityRef_dc6077a7,
    MemoryReference as _MemoryReference_a1aef278,
    OnlineEvaluationConfigReference as _OnlineEvaluationConfigReference_13c14f3c,
    PolicyEngineReference as _PolicyEngineReference_471db68b,
    PolicyReference as _PolicyReference_d2f6bd10,
    RuntimeEndpointReference as _RuntimeEndpointReference_dff8b038,
    RuntimeReference as _RuntimeReference_bdb3da48,
    WorkloadIdentityReference as _WorkloadIdentityReference_255b3126,
)


@jsii.implements(_IInspectable_c2943556, _IBrowserCustomRef_f12bfa35, _ITaggableV2_4e6798f8)
class CfnBrowserCustom(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom",
):
    '''AgentCore Browser tool provides a fast, secure, cloud-based browser runtime to enable AI agents to interact with websites at scale.

    For more information about using the custom browser, see `Interact with web applications using Amazon Bedrock AgentCore Browser <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html
    :cloudformationResource: AWS::BedrockAgentCore::BrowserCustom
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_browser_custom = bedrockagentcore.CfnBrowserCustom(self, "MyCfnBrowserCustom",
            name="name",
            network_configuration=bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty(
                network_mode="networkMode",
        
                # the properties below are optional
                vpc_config=bedrockagentcore.CfnBrowserCustom.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            ),
        
            # the properties below are optional
            browser_signing=bedrockagentcore.CfnBrowserCustom.BrowserSigningProperty(
                enabled=False
            ),
            description="description",
            execution_role_arn="executionRoleArn",
            recording_config=bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty(
                enabled=False,
                s3_location=bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                    bucket="bucket",
                    prefix="prefix"
                )
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        network_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnBrowserCustom.BrowserNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        browser_signing: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBrowserCustom.BrowserSigningProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        recording_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBrowserCustom.RecordingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::BrowserCustom``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the custom browser.
        :param network_configuration: The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.
        :param browser_signing: Browser signing configuration.
        :param description: The custom browser.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role.
        :param recording_config: THe custom browser configuration.
        :param tags: The tags for the custom browser.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e817ad5ee6496ab54cf569758c4d73da62a4d6f5cf0c34866960f6e4677343e1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBrowserCustomProps(
            name=name,
            network_configuration=network_configuration,
            browser_signing=browser_signing,
            description=description,
            execution_role_arn=execution_role_arn,
            recording_config=recording_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForBrowserCustom")
    @builtins.classmethod
    def arn_for_browser_custom(
        cls,
        resource: "_IBrowserCustomRef_f12bfa35",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3938521d3e1fa00869a698ba3a1fa8867e2077f1c510f1bd54cf729929cc8448)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForBrowserCustom", [resource]))

    @jsii.member(jsii_name="fromBrowserCustomArn")
    @builtins.classmethod
    def from_browser_custom_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IBrowserCustomRef_f12bfa35":
        '''Creates a new IBrowserCustomRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd42b7f7bd38d71e50eb92224f822287bc042051c2eb613dcae193e1e3cb986c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IBrowserCustomRef_f12bfa35", jsii.sinvoke(cls, "fromBrowserCustomArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromBrowserId")
    @builtins.classmethod
    def from_browser_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        browser_id: builtins.str,
    ) -> "_IBrowserCustomRef_f12bfa35":
        '''Creates a new IBrowserCustomRef from a browserId.

        :param scope: -
        :param id: -
        :param browser_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a5d38dc7619d36a2a4f39c13ec237b55f560a41ac9a162b787880e8e6ba2f47)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument browser_id", value=browser_id, expected_type=type_hints["browser_id"])
        return typing.cast("_IBrowserCustomRef_f12bfa35", jsii.sinvoke(cls, "fromBrowserId", [scope, id, browser_id]))

    @jsii.member(jsii_name="isCfnBrowserCustom")
    @builtins.classmethod
    def is_cfn_browser_custom(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnBrowserCustom.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b61de9c51c69f66cbc156b98a64f55d58e5c07baf4719635d93d5421943cf1cc)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnBrowserCustom", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12637c5685b21eb50c5acd05eb9308d8266fc2816549a6a2816d9399823e8551)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f14f4b2516dbe32242e98828488dc4abcc900e39ac20507ae2fd0d16a3a0457c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBrowserArn")
    def attr_browser_arn(self) -> builtins.str:
        '''The ARN for the custom browser.

        :cloudformationAttribute: BrowserArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBrowserArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBrowserId")
    def attr_browser_id(self) -> builtins.str:
        '''The ID for the custom browser.

        :cloudformationAttribute: BrowserId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBrowserId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time at which the custom browser was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''The reason for failure if the browser creation or operation failed.

        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The time at which the custom browser was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the custom browser.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="browserCustomRef")
    def browser_custom_ref(self) -> "_BrowserCustomReference_ceb8fdba":
        '''A reference to a BrowserCustom resource.'''
        return typing.cast("_BrowserCustomReference_ceb8fdba", jsii.get(self, "browserCustomRef"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the custom browser.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7c7dc0414899a74bed53146d246f036f214f82b031723849419726e12bcee67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.BrowserNetworkConfigurationProperty"]:
        '''The network configuration for a code interpreter.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.BrowserNetworkConfigurationProperty"], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.BrowserNetworkConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89dfccc35ccd0a377234eb3e008038ad66200df7a4f3c63bf61ebf273a7f42e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="browserSigning")
    def browser_signing(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.BrowserSigningProperty"]]:
        '''Browser signing configuration.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.BrowserSigningProperty"]], jsii.get(self, "browserSigning"))

    @browser_signing.setter
    def browser_signing(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.BrowserSigningProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81fba2b1346993fe8f90531b960f456b9bae96a895915ce3c4c9fa5127ad0a23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "browserSigning", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The custom browser.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d16faa304c4f18b8bba1ee70b209c47d9944346a1e88926b4ee4ea5fe723fd64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dd292342e1165d23c8ce68a72d30c745d42a2586b394e8bcb4aa1ec13e9cc74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="recordingConfig")
    def recording_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.RecordingConfigProperty"]]:
        '''THe custom browser configuration.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.RecordingConfigProperty"]], jsii.get(self, "recordingConfig"))

    @recording_config.setter
    def recording_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.RecordingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__089c5a25d69d7c7abf4193f45206b584472351088cbe92835bb014923a48f2e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordingConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the custom browser.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22e813ff9c64c23f175682396c7a13b02b9193809d3629b73f2ecac10192c8c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"network_mode": "networkMode", "vpc_config": "vpcConfig"},
    )
    class BrowserNetworkConfigurationProperty:
        def __init__(
            self,
            *,
            network_mode: builtins.str,
            vpc_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBrowserCustom.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The network configuration.

            :param network_mode: The network mode.
            :param vpc_config: Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                browser_network_configuration_property = bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty(
                    network_mode="networkMode",
                
                    # the properties below are optional
                    vpc_config=bedrockagentcore.CfnBrowserCustom.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0d5bebf1ad5159cc9014318eaa4c540145c82225bd9e29170035b0a29d0ee07)
                check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
                check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_mode": network_mode,
            }
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def network_mode(self) -> builtins.str:
            '''The network mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration.html#cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-networkmode
            '''
            result = self._values.get("network_mode")
            assert result is not None, "Required property 'network_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.VpcConfigProperty"]]:
            '''Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-browsernetworkconfiguration.html#cfn-bedrockagentcore-browsercustom-browsernetworkconfiguration-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrowserNetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.BrowserSigningProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class BrowserSigningProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''Browser signing configuration.

            :param enabled: Default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-browsersigning.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                browser_signing_property = bedrockagentcore.CfnBrowserCustom.BrowserSigningProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7e53c5d43f81573d2efdf7d45e9c80191cee07ad5d1b9262ad41ee43c45059d9)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''
            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-browsersigning.html#cfn-bedrockagentcore-browsercustom-browsersigning-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BrowserSigningProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "s3_location": "s3Location"},
    )
    class RecordingConfigProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
            s3_location: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBrowserCustom.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The recording configuration.

            :param enabled: The recording configuration for a browser. This structure defines how browser sessions are recorded. Default: - false
            :param s3_location: The S3 location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-recordingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                recording_config_property = bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty(
                    enabled=False,
                    s3_location=bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                        bucket="bucket",
                        prefix="prefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__754929ea2dabad59807821380b38b3ef1b1955a5473f5469b18a7dcc81600948)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if s3_location is not None:
                self._values["s3_location"] = s3_location

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''The recording configuration for a browser.

            This structure defines how browser sessions are recorded.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-recordingconfig.html#cfn-bedrockagentcore-browsercustom-recordingconfig-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        @builtins.property
        def s3_location(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.S3LocationProperty"]]:
            '''The S3 location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-recordingconfig.html#cfn-bedrockagentcore-browsercustom-recordingconfig-s3location
            '''
            result = self._values.get("s3_location")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.S3LocationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "prefix": "prefix"},
    )
    class S3LocationProperty:
        def __init__(self, *, bucket: builtins.str, prefix: builtins.str) -> None:
            '''The S3 location.

            :param bucket: The S3 location bucket name.
            :param prefix: The S3 location object prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                s3_location_property = bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                    bucket="bucket",
                    prefix="prefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6787b09f9e077c274ab79cdf45ea5157eec8aea8960e77f8e128fab67b3cbc26)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "prefix": prefix,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The S3 location bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-s3location.html#cfn-bedrockagentcore-browsercustom-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def prefix(self) -> builtins.str:
            '''The S3 location object prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-s3location.html#cfn-bedrockagentcore-browsercustom-s3location-prefix
            '''
            result = self._values.get("prefix")
            assert result is not None, "Required property 'prefix' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustom.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_groups": "securityGroups", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_groups: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Network mode configuration for VPC.

            :param security_groups: Security groups for VPC.
            :param subnets: Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                vpc_config_property = bedrockagentcore.CfnBrowserCustom.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46efbe5ee20e23cd9dc9ee29c1cd041e741b8a0aeb2c0ea76ed3cb6cab180dad)
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_groups": security_groups,
                "subnets": subnets,
            }

        @builtins.property
        def security_groups(self) -> typing.List[builtins.str]:
            '''Security groups for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-vpcconfig.html#cfn-bedrockagentcore-browsercustom-vpcconfig-securitygroups
            '''
            result = self._values.get("security_groups")
            assert result is not None, "Required property 'security_groups' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-browsercustom-vpcconfig.html#cfn-bedrockagentcore-browsercustom-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserCustomProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "network_configuration": "networkConfiguration",
        "browser_signing": "browserSigning",
        "description": "description",
        "execution_role_arn": "executionRoleArn",
        "recording_config": "recordingConfig",
        "tags": "tags",
    },
)
class CfnBrowserCustomProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        network_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnBrowserCustom.BrowserNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        browser_signing: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBrowserCustom.BrowserSigningProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        recording_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBrowserCustom.RecordingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBrowserCustom``.

        :param name: The name of the custom browser.
        :param network_configuration: The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.
        :param browser_signing: Browser signing configuration.
        :param description: The custom browser.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role.
        :param recording_config: THe custom browser configuration.
        :param tags: The tags for the custom browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_browser_custom_props = bedrockagentcore.CfnBrowserCustomProps(
                name="name",
                network_configuration=bedrockagentcore.CfnBrowserCustom.BrowserNetworkConfigurationProperty(
                    network_mode="networkMode",
            
                    # the properties below are optional
                    vpc_config=bedrockagentcore.CfnBrowserCustom.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                ),
            
                # the properties below are optional
                browser_signing=bedrockagentcore.CfnBrowserCustom.BrowserSigningProperty(
                    enabled=False
                ),
                description="description",
                execution_role_arn="executionRoleArn",
                recording_config=bedrockagentcore.CfnBrowserCustom.RecordingConfigProperty(
                    enabled=False,
                    s3_location=bedrockagentcore.CfnBrowserCustom.S3LocationProperty(
                        bucket="bucket",
                        prefix="prefix"
                    )
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08f9adb5e20b52bbdc47438decbd54e3ebb4b1976cbf46432a19597fc6589c39)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument browser_signing", value=browser_signing, expected_type=type_hints["browser_signing"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument recording_config", value=recording_config, expected_type=type_hints["recording_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if browser_signing is not None:
            self._values["browser_signing"] = browser_signing
        if description is not None:
            self._values["description"] = description
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if recording_config is not None:
            self._values["recording_config"] = recording_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the custom browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.BrowserNetworkConfigurationProperty"]:
        '''The network configuration for a code interpreter.

        This structure defines how the code interpreter connects to the network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.BrowserNetworkConfigurationProperty"], result)

    @builtins.property
    def browser_signing(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.BrowserSigningProperty"]]:
        '''Browser signing configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-browsersigning
        '''
        result = self._values.get("browser_signing")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.BrowserSigningProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The custom browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recording_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.RecordingConfigProperty"]]:
        '''THe custom browser configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-recordingconfig
        '''
        result = self._values.get("recording_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBrowserCustom.RecordingConfigProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the custom browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browsercustom.html#cfn-bedrockagentcore-browsercustom-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBrowserCustomProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IBrowserProfileRef_87a4b1a8, _ITaggableV2_4e6798f8)
class CfnBrowserProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserProfile",
):
    '''Resource definition for AWS::BedrockAgentCore::BrowserProfile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browserprofile.html
    :cloudformationResource: AWS::BedrockAgentCore::BrowserProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_browser_profile = bedrockagentcore.CfnBrowserProfile(self, "MyCfnBrowserProfile",
            name="name",
        
            # the properties below are optional
            description="description",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::BrowserProfile``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the browser profile.
        :param description: The description of the browser profile.
        :param tags: A map of tag keys and values.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7473f1faa9bfc03705a3d4572354312e5dd4b5bb47ae1b3a9a2ca09618c09558)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBrowserProfileProps(name=name, description=description, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForBrowserProfile")
    @builtins.classmethod
    def arn_for_browser_profile(
        cls,
        resource: "_IBrowserProfileRef_87a4b1a8",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdecc7ab99fa67b91a7bb897ed0d5da420e0fc98db0e44fb43c5e4573c36e7a2)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForBrowserProfile", [resource]))

    @jsii.member(jsii_name="isCfnBrowserProfile")
    @builtins.classmethod
    def is_cfn_browser_profile(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnBrowserProfile.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ade26e9a57cff73b5718f778b22e6e84dde0ded65b13a8b5acef370b2ee67804)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnBrowserProfile", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5babb21bf2a8458092196b97ee681b85e69bab2ae47419298b051be21a395742)
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
            type_hints = typing.get_type_hints(_typecheckingstub__97ccc42c3721a989048610856613cdee96f1a401698e93e9abda9a99b25f14f3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''Timestamp when the browser profile was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastSavedAt")
    def attr_last_saved_at(self) -> builtins.str:
        '''Timestamp when the browser profile was last saved.

        :cloudformationAttribute: LastSavedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastSavedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLastSavedBrowserId")
    def attr_last_saved_browser_id(self) -> builtins.str:
        '''ID of the last saved browser.

        :cloudformationAttribute: LastSavedBrowserId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastSavedBrowserId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastSavedBrowserSessionId")
    def attr_last_saved_browser_session_id(self) -> builtins.str:
        '''ID of the last saved browser session.

        :cloudformationAttribute: LastSavedBrowserSessionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastSavedBrowserSessionId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''Timestamp when the browser profile was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileArn")
    def attr_profile_arn(self) -> builtins.str:
        '''The ARN of a BrowserProfile resource.

        :cloudformationAttribute: ProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileId")
    def attr_profile_id(self) -> builtins.str:
        '''The id of the browser profile.

        :cloudformationAttribute: ProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Status of browser profile.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="browserProfileRef")
    def browser_profile_ref(self) -> "_BrowserProfileReference_7d69eac7":
        '''A reference to a BrowserProfile resource.'''
        return typing.cast("_BrowserProfileReference_7d69eac7", jsii.get(self, "browserProfileRef"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the browser profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae6651c726fc48203e39af1e8661928e84a4323ff2a0d8a55574653b31bf76d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the browser profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1b17f49e9d7bf2a0d0045e14abceca289c01f8a4b4a4f70e5297e2aa8cef7d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tag keys and values.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6885ed668d838f82c9f283a9d7037bb9609ab538bb3bce79981a0e79df9f52b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnBrowserProfileProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "description": "description", "tags": "tags"},
)
class CfnBrowserProfileProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBrowserProfile``.

        :param name: The name of the browser profile.
        :param description: The description of the browser profile.
        :param tags: A map of tag keys and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browserprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_browser_profile_props = bedrockagentcore.CfnBrowserProfileProps(
                name="name",
            
                # the properties below are optional
                description="description",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06ddbf18be8902484b8315b3f45a334e6e9cddb8b83448c8197da614062d18ee)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the browser profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browserprofile.html#cfn-bedrockagentcore-browserprofile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the browser profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browserprofile.html#cfn-bedrockagentcore-browserprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of tag keys and values.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-browserprofile.html#cfn-bedrockagentcore-browserprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBrowserProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ICodeInterpreterCustomRef_2d5c05fb, _ITaggableV2_4e6798f8)
class CfnCodeInterpreterCustom(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustom",
):
    '''The AgentCore Code Interpreter tool enables agents to securely execute code in isolated sandbox environments.

    It offers advanced configuration support and seamless integration with popular frameworks.

    For more information about using the custom code interpreter, see `Execute code and analyze data using Amazon Bedrock AgentCore Code Interpreter <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html
    :cloudformationResource: AWS::BedrockAgentCore::CodeInterpreterCustom
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_code_interpreter_custom = bedrockagentcore.CfnCodeInterpreterCustom(self, "MyCfnCodeInterpreterCustom",
            name="name",
            network_configuration=bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty(
                network_mode="networkMode",
        
                # the properties below are optional
                vpc_config=bedrockagentcore.CfnCodeInterpreterCustom.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            ),
        
            # the properties below are optional
            description="description",
            execution_role_arn="executionRoleArn",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        network_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::CodeInterpreterCustom``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the code interpreter.
        :param network_configuration: The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.
        :param description: The code interpreter description.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role.
        :param tags: The tags for the code interpreter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aaa167a6af98d626969b5bd2de9377658de4e8d04df0b48dc5916f9e503a029)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCodeInterpreterCustomProps(
            name=name,
            network_configuration=network_configuration,
            description=description,
            execution_role_arn=execution_role_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForCodeInterpreterCustom")
    @builtins.classmethod
    def arn_for_code_interpreter_custom(
        cls,
        resource: "_ICodeInterpreterCustomRef_2d5c05fb",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__975674ea4f6bb8a0c20e661871dd773f758b19950b1cf17839dc6587ebb65590)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForCodeInterpreterCustom", [resource]))

    @jsii.member(jsii_name="fromCodeInterpreterCustomArn")
    @builtins.classmethod
    def from_code_interpreter_custom_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_ICodeInterpreterCustomRef_2d5c05fb":
        '''Creates a new ICodeInterpreterCustomRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdf8490c04291f6972f1dc00b876398eb5886b19291a588f52fdbb4fc2e4e156)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_ICodeInterpreterCustomRef_2d5c05fb", jsii.sinvoke(cls, "fromCodeInterpreterCustomArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromCodeInterpreterId")
    @builtins.classmethod
    def from_code_interpreter_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        code_interpreter_id: builtins.str,
    ) -> "_ICodeInterpreterCustomRef_2d5c05fb":
        '''Creates a new ICodeInterpreterCustomRef from a codeInterpreterId.

        :param scope: -
        :param id: -
        :param code_interpreter_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2e6193c6a8378455a4decc0c525a09a78674fd7ad426e58017e57035bc1789a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument code_interpreter_id", value=code_interpreter_id, expected_type=type_hints["code_interpreter_id"])
        return typing.cast("_ICodeInterpreterCustomRef_2d5c05fb", jsii.sinvoke(cls, "fromCodeInterpreterId", [scope, id, code_interpreter_id]))

    @jsii.member(jsii_name="isCfnCodeInterpreterCustom")
    @builtins.classmethod
    def is_cfn_code_interpreter_custom(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnCodeInterpreterCustom.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__510c722b77a53a3aba328ff9805ff6391701fb5ea56c15887eebad76692d70a0)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnCodeInterpreterCustom", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab4b7a28e87b1af264773dfddc0e9da46bb99c921aa85fb942fcc7ca03680597)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bf6d68ae9ee508df2d25ca9f4fa9a800c1215c05ac37929135ce20e393a44113)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCodeInterpreterArn")
    def attr_code_interpreter_arn(self) -> builtins.str:
        '''The code interpreter Amazon Resource Name (ARN).

        :cloudformationAttribute: CodeInterpreterArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCodeInterpreterArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCodeInterpreterId")
    def attr_code_interpreter_id(self) -> builtins.str:
        '''The ID of the code interpreter.

        :cloudformationAttribute: CodeInterpreterId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCodeInterpreterId"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time at which the code interpreter was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''The reason for failure if the code interpreter creation or operation failed.

        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The time at which the code interpreter was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the custom code interpreter.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="codeInterpreterCustomRef")
    def code_interpreter_custom_ref(self) -> "_CodeInterpreterCustomReference_0b253bc0":
        '''A reference to a CodeInterpreterCustom resource.'''
        return typing.cast("_CodeInterpreterCustomReference_0b253bc0", jsii.get(self, "codeInterpreterCustomRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the code interpreter.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c58fa8bcb0ec87d3b6f75396018d3eeff06205adbf6ade289f0ac1710d71c909)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"]:
        '''The network configuration for a code interpreter.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a36911cef74e5cac559eb0b558b639739fba4dccbbc8a224553a0f0a0cace3cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The code interpreter description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f33607ff407017e2c7ecefbc727c6f7660550a46fe6b356799810d75ccf8d662)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__597443cc8b5cdaed2db807a1545702d23f8f925435f13cd3d17111236aba2428)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the code interpreter.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__466065bbc5e5f3997568d60c567b51bbc4a9a4900e6ce6da9f9499f85329a3a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"network_mode": "networkMode", "vpc_config": "vpcConfig"},
    )
    class CodeInterpreterNetworkConfigurationProperty:
        def __init__(
            self,
            *,
            network_mode: builtins.str,
            vpc_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeInterpreterCustom.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The network configuration.

            :param network_mode: The network mode.
            :param vpc_config: Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                code_interpreter_network_configuration_property = bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty(
                    network_mode="networkMode",
                
                    # the properties below are optional
                    vpc_config=bedrockagentcore.CfnCodeInterpreterCustom.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eae1295735d5d0996afa02b88ef9dddbd193fc77b25f7b69433fd57c1240bb3a)
                check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
                check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_mode": network_mode,
            }
            if vpc_config is not None:
                self._values["vpc_config"] = vpc_config

        @builtins.property
        def network_mode(self) -> builtins.str:
            '''The network mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration.html#cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-networkmode
            '''
            result = self._values.get("network_mode")
            assert result is not None, "Required property 'network_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_config(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeInterpreterCustom.VpcConfigProperty"]]:
            '''Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration.html#cfn-bedrockagentcore-codeinterpretercustom-codeinterpreternetworkconfiguration-vpcconfig
            '''
            result = self._values.get("vpc_config")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnCodeInterpreterCustom.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeInterpreterNetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustom.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_groups": "securityGroups", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_groups: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Network mode configuration for VPC.

            :param security_groups: Security groups for VPC.
            :param subnets: Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                vpc_config_property = bedrockagentcore.CfnCodeInterpreterCustom.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__97c8e6007d5911afbd85662033d4936d1846dbfdc6caa2fb2e69de26653ccc32)
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_groups": security_groups,
                "subnets": subnets,
            }

        @builtins.property
        def security_groups(self) -> typing.List[builtins.str]:
            '''Security groups for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig.html#cfn-bedrockagentcore-codeinterpretercustom-vpcconfig-securitygroups
            '''
            result = self._values.get("security_groups")
            assert result is not None, "Required property 'security_groups' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-codeinterpretercustom-vpcconfig.html#cfn-bedrockagentcore-codeinterpretercustom-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnCodeInterpreterCustomProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "network_configuration": "networkConfiguration",
        "description": "description",
        "execution_role_arn": "executionRoleArn",
        "tags": "tags",
    },
)
class CfnCodeInterpreterCustomProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        network_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        execution_role_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCodeInterpreterCustom``.

        :param name: The name of the code interpreter.
        :param network_configuration: The network configuration for a code interpreter. This structure defines how the code interpreter connects to the network.
        :param description: The code interpreter description.
        :param execution_role_arn: The Amazon Resource Name (ARN) of the execution role.
        :param tags: The tags for the code interpreter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_code_interpreter_custom_props = bedrockagentcore.CfnCodeInterpreterCustomProps(
                name="name",
                network_configuration=bedrockagentcore.CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty(
                    network_mode="networkMode",
            
                    # the properties below are optional
                    vpc_config=bedrockagentcore.CfnCodeInterpreterCustom.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                ),
            
                # the properties below are optional
                description="description",
                execution_role_arn="executionRoleArn",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b5217aa9ccd0ec964b92c3a48855bb1494914c435606fcee5b0faefd790d264)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            self._values["description"] = description
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the code interpreter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"]:
        '''The network configuration for a code interpreter.

        This structure defines how the code interpreter connects to the network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The code interpreter description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the execution role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the code interpreter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-codeinterpretercustom.html#cfn-bedrockagentcore-codeinterpretercustom-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCodeInterpreterCustomProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IEvaluatorRef_21d364d2, _ITaggableV2_4e6798f8)
class CfnEvaluator(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnEvaluator",
):
    '''Resource Type definition for AWS::BedrockAgentCore::Evaluator - Creates a custom evaluator for agent quality assessment using LLM-as-a-Judge configurations.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-evaluator.html
    :cloudformationResource: AWS::BedrockAgentCore::Evaluator
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        # additional_model_request_fields: Any
        
        cfn_evaluator = bedrockagentcore.CfnEvaluator(self, "MyCfnEvaluator",
            evaluator_config=bedrockagentcore.CfnEvaluator.EvaluatorConfigProperty(
                llm_as_aJudge=bedrockagentcore.CfnEvaluator.LlmAsAJudgeEvaluatorConfigProperty(
                    instructions="instructions",
                    model_config=bedrockagentcore.CfnEvaluator.EvaluatorModelConfigProperty(
                        bedrock_evaluator_model_config=bedrockagentcore.CfnEvaluator.BedrockEvaluatorModelConfigProperty(
                            model_id="modelId",
        
                            # the properties below are optional
                            additional_model_request_fields=additional_model_request_fields,
                            inference_config=bedrockagentcore.CfnEvaluator.InferenceConfigurationProperty(
                                max_tokens=123,
                                temperature=123,
                                top_p=123
                            )
                        )
                    ),
                    rating_scale=bedrockagentcore.CfnEvaluator.RatingScaleProperty(
                        categorical=[bedrockagentcore.CfnEvaluator.CategoricalScaleDefinitionProperty(
                            definition="definition",
                            label="label"
                        )],
                        numerical=[bedrockagentcore.CfnEvaluator.NumericalScaleDefinitionProperty(
                            definition="definition",
                            label="label",
                            value=123
                        )]
                    )
                )
            ),
            evaluator_name="evaluatorName",
            level="level",
        
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
        evaluator_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnEvaluator.EvaluatorConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        evaluator_name: builtins.str,
        level: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::Evaluator``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param evaluator_config: The configuration that defines how an evaluator assesses agent performance.
        :param evaluator_name: The name of the evaluator. Must be unique within your account.
        :param level: 
        :param description: The description of the evaluator.
        :param tags: A list of tags to assign to the evaluator.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__141b6fd05e9e051e0fb07fbc9903cbc471c6f95bd2ce599524db7f08eb59d089)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEvaluatorProps(
            evaluator_config=evaluator_config,
            evaluator_name=evaluator_name,
            level=level,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForEvaluator")
    @builtins.classmethod
    def arn_for_evaluator(cls, resource: "_IEvaluatorRef_21d364d2") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2241f7871310f76bc950be554b9e50e0182d60385049f460dfd13459d3e0757)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForEvaluator", [resource]))

    @jsii.member(jsii_name="isCfnEvaluator")
    @builtins.classmethod
    def is_cfn_evaluator(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnEvaluator.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24f5b2764d1f145a52271003ddf7f12ab5fc8df06fcd5d57f8407543371dd7cc)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnEvaluator", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e88dc5c3acd247cf0c5817871be6840db2e01fa9976082dea7654fb298e73dd3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a74e1010c78d5affb59aa69c26b246dc322ef02ba3fe68b5cafecce92faa0934)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the evaluator was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrEvaluatorArn")
    def attr_evaluator_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the evaluator.

        :cloudformationAttribute: EvaluatorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEvaluatorArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEvaluatorId")
    def attr_evaluator_id(self) -> builtins.str:
        '''The unique identifier of the evaluator.

        :cloudformationAttribute: EvaluatorId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEvaluatorId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the evaluator was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="evaluatorRef")
    def evaluator_ref(self) -> "_EvaluatorReference_a3ac0235":
        '''A reference to a Evaluator resource.'''
        return typing.cast("_EvaluatorReference_a3ac0235", jsii.get(self, "evaluatorRef"))

    @builtins.property
    @jsii.member(jsii_name="evaluatorConfig")
    def evaluator_config(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnEvaluator.EvaluatorConfigProperty"]:
        '''The configuration that defines how an evaluator assesses agent performance.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnEvaluator.EvaluatorConfigProperty"], jsii.get(self, "evaluatorConfig"))

    @evaluator_config.setter
    def evaluator_config(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnEvaluator.EvaluatorConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d85156d59d54c7ee85e1018a2dbc04869c0befafd49c7f39bed6f8bdf1c0e7c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluatorConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="evaluatorName")
    def evaluator_name(self) -> builtins.str:
        '''The name of the evaluator.'''
        return typing.cast(builtins.str, jsii.get(self, "evaluatorName"))

    @evaluator_name.setter
    def evaluator_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fb35f2e87b3efb7648fbd87d13f3e5ff4e7e4f353ccab015439c65775fa4f4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluatorName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @level.setter
    def level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5ba897fceb746066253f02e4acaa94a0805d38e5dd7eb06a70ada74a5171c7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the evaluator.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9476feb3976d508ab93e23993f8958690b378207ccac9c804c8644598ec4e9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A list of tags to assign to the evaluator.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9be07f5133cae95a44b8c1e5e5925d27341ddb21585adfa558cf87a9d4ed266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnEvaluator.BedrockEvaluatorModelConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "model_id": "modelId",
            "additional_model_request_fields": "additionalModelRequestFields",
            "inference_config": "inferenceConfig",
        },
    )
    class BedrockEvaluatorModelConfigProperty:
        def __init__(
            self,
            *,
            model_id: builtins.str,
            additional_model_request_fields: typing.Any = None,
            inference_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEvaluator.InferenceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration for using Amazon Bedrock models in evaluator assessments.

            :param model_id: The identifier of the Amazon Bedrock model to use for evaluation.
            :param additional_model_request_fields: Additional model-specific request fields.
            :param inference_config: The inference configuration parameters that control model behavior during evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # additional_model_request_fields: Any
                
                bedrock_evaluator_model_config_property = bedrockagentcore.CfnEvaluator.BedrockEvaluatorModelConfigProperty(
                    model_id="modelId",
                
                    # the properties below are optional
                    additional_model_request_fields=additional_model_request_fields,
                    inference_config=bedrockagentcore.CfnEvaluator.InferenceConfigurationProperty(
                        max_tokens=123,
                        temperature=123,
                        top_p=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e685cb926c5b55ad4c85e5270f7d5645516c749d48c98cdcd779d7548a53c95f)
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
                check_type(argname="argument additional_model_request_fields", value=additional_model_request_fields, expected_type=type_hints["additional_model_request_fields"])
                check_type(argname="argument inference_config", value=inference_config, expected_type=type_hints["inference_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "model_id": model_id,
            }
            if additional_model_request_fields is not None:
                self._values["additional_model_request_fields"] = additional_model_request_fields
            if inference_config is not None:
                self._values["inference_config"] = inference_config

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The identifier of the Amazon Bedrock model to use for evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig.html#cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def additional_model_request_fields(self) -> typing.Any:
            '''Additional model-specific request fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig.html#cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-additionalmodelrequestfields
            '''
            result = self._values.get("additional_model_request_fields")
            return typing.cast(typing.Any, result)

        @builtins.property
        def inference_config(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEvaluator.InferenceConfigurationProperty"]]:
            '''The inference configuration parameters that control model behavior during evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-bedrockevaluatormodelconfig.html#cfn-bedrockagentcore-evaluator-bedrockevaluatormodelconfig-inferenceconfig
            '''
            result = self._values.get("inference_config")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEvaluator.InferenceConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BedrockEvaluatorModelConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnEvaluator.CategoricalScaleDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"definition": "definition", "label": "label"},
    )
    class CategoricalScaleDefinitionProperty:
        def __init__(self, *, definition: builtins.str, label: builtins.str) -> None:
            '''A categorical rating scale option.

            :param definition: The description that explains what this categorical rating represents.
            :param label: The label of this categorical rating option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                categorical_scale_definition_property = bedrockagentcore.CfnEvaluator.CategoricalScaleDefinitionProperty(
                    definition="definition",
                    label="label"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0138c4dab895be263ca856078c54d7f7dc17e4a1e5fa14530ef199b887cb5326)
                check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
                check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "definition": definition,
                "label": label,
            }

        @builtins.property
        def definition(self) -> builtins.str:
            '''The description that explains what this categorical rating represents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition.html#cfn-bedrockagentcore-evaluator-categoricalscaledefinition-definition
            '''
            result = self._values.get("definition")
            assert result is not None, "Required property 'definition' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def label(self) -> builtins.str:
            '''The label of this categorical rating option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-categoricalscaledefinition.html#cfn-bedrockagentcore-evaluator-categoricalscaledefinition-label
            '''
            result = self._values.get("label")
            assert result is not None, "Required property 'label' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CategoricalScaleDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnEvaluator.EvaluatorConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"llm_as_a_judge": "llmAsAJudge"},
    )
    class EvaluatorConfigProperty:
        def __init__(
            self,
            *,
            llm_as_a_judge: typing.Union["_IResolvable_da3f097b", typing.Union["CfnEvaluator.LlmAsAJudgeEvaluatorConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The configuration that defines how an evaluator assesses agent performance.

            :param llm_as_a_judge: The configuration for LLM-as-a-Judge evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-evaluatorconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # additional_model_request_fields: Any
                
                evaluator_config_property = bedrockagentcore.CfnEvaluator.EvaluatorConfigProperty(
                    llm_as_aJudge=bedrockagentcore.CfnEvaluator.LlmAsAJudgeEvaluatorConfigProperty(
                        instructions="instructions",
                        model_config=bedrockagentcore.CfnEvaluator.EvaluatorModelConfigProperty(
                            bedrock_evaluator_model_config=bedrockagentcore.CfnEvaluator.BedrockEvaluatorModelConfigProperty(
                                model_id="modelId",
                
                                # the properties below are optional
                                additional_model_request_fields=additional_model_request_fields,
                                inference_config=bedrockagentcore.CfnEvaluator.InferenceConfigurationProperty(
                                    max_tokens=123,
                                    temperature=123,
                                    top_p=123
                                )
                            )
                        ),
                        rating_scale=bedrockagentcore.CfnEvaluator.RatingScaleProperty(
                            categorical=[bedrockagentcore.CfnEvaluator.CategoricalScaleDefinitionProperty(
                                definition="definition",
                                label="label"
                            )],
                            numerical=[bedrockagentcore.CfnEvaluator.NumericalScaleDefinitionProperty(
                                definition="definition",
                                label="label",
                                value=123
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68fedf7916817af17038fada535f709885d9e4602b0228fd6e545877cc7a08c4)
                check_type(argname="argument llm_as_a_judge", value=llm_as_a_judge, expected_type=type_hints["llm_as_a_judge"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "llm_as_a_judge": llm_as_a_judge,
            }

        @builtins.property
        def llm_as_a_judge(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnEvaluator.LlmAsAJudgeEvaluatorConfigProperty"]:
            '''The configuration for LLM-as-a-Judge evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-evaluatorconfig.html#cfn-bedrockagentcore-evaluator-evaluatorconfig-llmasajudge
            '''
            result = self._values.get("llm_as_a_judge")
            assert result is not None, "Required property 'llm_as_a_judge' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnEvaluator.LlmAsAJudgeEvaluatorConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluatorConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnEvaluator.EvaluatorModelConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"bedrock_evaluator_model_config": "bedrockEvaluatorModelConfig"},
    )
    class EvaluatorModelConfigProperty:
        def __init__(
            self,
            *,
            bedrock_evaluator_model_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnEvaluator.BedrockEvaluatorModelConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The model configuration that specifies which foundation model to use for evaluation.

            :param bedrock_evaluator_model_config: The configuration for using Amazon Bedrock models in evaluator assessments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-evaluatormodelconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # additional_model_request_fields: Any
                
                evaluator_model_config_property = bedrockagentcore.CfnEvaluator.EvaluatorModelConfigProperty(
                    bedrock_evaluator_model_config=bedrockagentcore.CfnEvaluator.BedrockEvaluatorModelConfigProperty(
                        model_id="modelId",
                
                        # the properties below are optional
                        additional_model_request_fields=additional_model_request_fields,
                        inference_config=bedrockagentcore.CfnEvaluator.InferenceConfigurationProperty(
                            max_tokens=123,
                            temperature=123,
                            top_p=123
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e199bbf333dd5891de717038547bcf88b9e5114ac6040f7d31e54c8cb0f17f02)
                check_type(argname="argument bedrock_evaluator_model_config", value=bedrock_evaluator_model_config, expected_type=type_hints["bedrock_evaluator_model_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bedrock_evaluator_model_config": bedrock_evaluator_model_config,
            }

        @builtins.property
        def bedrock_evaluator_model_config(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnEvaluator.BedrockEvaluatorModelConfigProperty"]:
            '''The configuration for using Amazon Bedrock models in evaluator assessments.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-evaluatormodelconfig.html#cfn-bedrockagentcore-evaluator-evaluatormodelconfig-bedrockevaluatormodelconfig
            '''
            result = self._values.get("bedrock_evaluator_model_config")
            assert result is not None, "Required property 'bedrock_evaluator_model_config' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnEvaluator.BedrockEvaluatorModelConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluatorModelConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnEvaluator.InferenceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_tokens": "maxTokens",
            "temperature": "temperature",
            "top_p": "topP",
        },
    )
    class InferenceConfigurationProperty:
        def __init__(
            self,
            *,
            max_tokens: typing.Optional[jsii.Number] = None,
            temperature: typing.Optional[jsii.Number] = None,
            top_p: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The inference configuration parameters that control model behavior during evaluation.

            :param max_tokens: The maximum number of tokens to generate in the model response.
            :param temperature: The temperature value that controls randomness in the model's responses.
            :param top_p: The top-p sampling parameter that controls the diversity of the model's responses.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-inferenceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                inference_configuration_property = bedrockagentcore.CfnEvaluator.InferenceConfigurationProperty(
                    max_tokens=123,
                    temperature=123,
                    top_p=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe32f79956eba54fe76f4cfd3e9550d9001beda9560e6f4c55b2f8ab94aa98c2)
                check_type(argname="argument max_tokens", value=max_tokens, expected_type=type_hints["max_tokens"])
                check_type(argname="argument temperature", value=temperature, expected_type=type_hints["temperature"])
                check_type(argname="argument top_p", value=top_p, expected_type=type_hints["top_p"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if max_tokens is not None:
                self._values["max_tokens"] = max_tokens
            if temperature is not None:
                self._values["temperature"] = temperature
            if top_p is not None:
                self._values["top_p"] = top_p

        @builtins.property
        def max_tokens(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of tokens to generate in the model response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-inferenceconfiguration.html#cfn-bedrockagentcore-evaluator-inferenceconfiguration-maxtokens
            '''
            result = self._values.get("max_tokens")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def temperature(self) -> typing.Optional[jsii.Number]:
            '''The temperature value that controls randomness in the model's responses.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-inferenceconfiguration.html#cfn-bedrockagentcore-evaluator-inferenceconfiguration-temperature
            '''
            result = self._values.get("temperature")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def top_p(self) -> typing.Optional[jsii.Number]:
            '''The top-p sampling parameter that controls the diversity of the model's responses.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-inferenceconfiguration.html#cfn-bedrockagentcore-evaluator-inferenceconfiguration-topp
            '''
            result = self._values.get("top_p")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InferenceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnEvaluator.LlmAsAJudgeEvaluatorConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instructions": "instructions",
            "model_config": "modelConfig",
            "rating_scale": "ratingScale",
        },
    )
    class LlmAsAJudgeEvaluatorConfigProperty:
        def __init__(
            self,
            *,
            instructions: builtins.str,
            model_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnEvaluator.EvaluatorModelConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            rating_scale: typing.Union["_IResolvable_da3f097b", typing.Union["CfnEvaluator.RatingScaleProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The configuration for LLM-as-a-Judge evaluation.

            :param instructions: The evaluation instructions that guide the language model in assessing agent performance.
            :param model_config: The model configuration that specifies which foundation model to use for evaluation.
            :param rating_scale: The rating scale that defines how evaluators should score agent performance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # additional_model_request_fields: Any
                
                llm_as_aJudge_evaluator_config_property = bedrockagentcore.CfnEvaluator.LlmAsAJudgeEvaluatorConfigProperty(
                    instructions="instructions",
                    model_config=bedrockagentcore.CfnEvaluator.EvaluatorModelConfigProperty(
                        bedrock_evaluator_model_config=bedrockagentcore.CfnEvaluator.BedrockEvaluatorModelConfigProperty(
                            model_id="modelId",
                
                            # the properties below are optional
                            additional_model_request_fields=additional_model_request_fields,
                            inference_config=bedrockagentcore.CfnEvaluator.InferenceConfigurationProperty(
                                max_tokens=123,
                                temperature=123,
                                top_p=123
                            )
                        )
                    ),
                    rating_scale=bedrockagentcore.CfnEvaluator.RatingScaleProperty(
                        categorical=[bedrockagentcore.CfnEvaluator.CategoricalScaleDefinitionProperty(
                            definition="definition",
                            label="label"
                        )],
                        numerical=[bedrockagentcore.CfnEvaluator.NumericalScaleDefinitionProperty(
                            definition="definition",
                            label="label",
                            value=123
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f28079328036f363d453150c70a76fbc17cbd2c7dab0942689bd59b9411b642a)
                check_type(argname="argument instructions", value=instructions, expected_type=type_hints["instructions"])
                check_type(argname="argument model_config", value=model_config, expected_type=type_hints["model_config"])
                check_type(argname="argument rating_scale", value=rating_scale, expected_type=type_hints["rating_scale"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instructions": instructions,
                "model_config": model_config,
                "rating_scale": rating_scale,
            }

        @builtins.property
        def instructions(self) -> builtins.str:
            '''The evaluation instructions that guide the language model in assessing agent performance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig.html#cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-instructions
            '''
            result = self._values.get("instructions")
            assert result is not None, "Required property 'instructions' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_config(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnEvaluator.EvaluatorModelConfigProperty"]:
            '''The model configuration that specifies which foundation model to use for evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig.html#cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-modelconfig
            '''
            result = self._values.get("model_config")
            assert result is not None, "Required property 'model_config' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnEvaluator.EvaluatorModelConfigProperty"], result)

        @builtins.property
        def rating_scale(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnEvaluator.RatingScaleProperty"]:
            '''The rating scale that defines how evaluators should score agent performance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig.html#cfn-bedrockagentcore-evaluator-llmasajudgeevaluatorconfig-ratingscale
            '''
            result = self._values.get("rating_scale")
            assert result is not None, "Required property 'rating_scale' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnEvaluator.RatingScaleProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LlmAsAJudgeEvaluatorConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnEvaluator.NumericalScaleDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"definition": "definition", "label": "label", "value": "value"},
    )
    class NumericalScaleDefinitionProperty:
        def __init__(
            self,
            *,
            definition: builtins.str,
            label: builtins.str,
            value: jsii.Number,
        ) -> None:
            '''A numerical rating scale option.

            :param definition: The description that explains what this numerical rating represents.
            :param label: The label that describes this numerical rating option.
            :param value: The numerical value for this rating scale option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-numericalscaledefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                numerical_scale_definition_property = bedrockagentcore.CfnEvaluator.NumericalScaleDefinitionProperty(
                    definition="definition",
                    label="label",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e284be9755c11642d2b6734206454332b1166d2726612dba743e01c1a4f1a83)
                check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
                check_type(argname="argument label", value=label, expected_type=type_hints["label"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "definition": definition,
                "label": label,
                "value": value,
            }

        @builtins.property
        def definition(self) -> builtins.str:
            '''The description that explains what this numerical rating represents.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-numericalscaledefinition.html#cfn-bedrockagentcore-evaluator-numericalscaledefinition-definition
            '''
            result = self._values.get("definition")
            assert result is not None, "Required property 'definition' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def label(self) -> builtins.str:
            '''The label that describes this numerical rating option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-numericalscaledefinition.html#cfn-bedrockagentcore-evaluator-numericalscaledefinition-label
            '''
            result = self._values.get("label")
            assert result is not None, "Required property 'label' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''The numerical value for this rating scale option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-numericalscaledefinition.html#cfn-bedrockagentcore-evaluator-numericalscaledefinition-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NumericalScaleDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnEvaluator.RatingScaleProperty",
        jsii_struct_bases=[],
        name_mapping={"categorical": "categorical", "numerical": "numerical"},
    )
    class RatingScaleProperty:
        def __init__(
            self,
            *,
            categorical: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEvaluator.CategoricalScaleDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            numerical: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEvaluator.NumericalScaleDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The rating scale that defines how evaluators should score agent performance.

            :param categorical: 
            :param numerical: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-ratingscale.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                rating_scale_property = bedrockagentcore.CfnEvaluator.RatingScaleProperty(
                    categorical=[bedrockagentcore.CfnEvaluator.CategoricalScaleDefinitionProperty(
                        definition="definition",
                        label="label"
                    )],
                    numerical=[bedrockagentcore.CfnEvaluator.NumericalScaleDefinitionProperty(
                        definition="definition",
                        label="label",
                        value=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4b52b8f960640a8f01b882a7550bb6dcc23bf2b1121733ac830f9f26c80b3027)
                check_type(argname="argument categorical", value=categorical, expected_type=type_hints["categorical"])
                check_type(argname="argument numerical", value=numerical, expected_type=type_hints["numerical"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if categorical is not None:
                self._values["categorical"] = categorical
            if numerical is not None:
                self._values["numerical"] = numerical

        @builtins.property
        def categorical(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnEvaluator.CategoricalScaleDefinitionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-ratingscale.html#cfn-bedrockagentcore-evaluator-ratingscale-categorical
            '''
            result = self._values.get("categorical")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnEvaluator.CategoricalScaleDefinitionProperty"]]]], result)

        @builtins.property
        def numerical(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnEvaluator.NumericalScaleDefinitionProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-evaluator-ratingscale.html#cfn-bedrockagentcore-evaluator-ratingscale-numerical
            '''
            result = self._values.get("numerical")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnEvaluator.NumericalScaleDefinitionProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RatingScaleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnEvaluatorProps",
    jsii_struct_bases=[],
    name_mapping={
        "evaluator_config": "evaluatorConfig",
        "evaluator_name": "evaluatorName",
        "level": "level",
        "description": "description",
        "tags": "tags",
    },
)
class CfnEvaluatorProps:
    def __init__(
        self,
        *,
        evaluator_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnEvaluator.EvaluatorConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        evaluator_name: builtins.str,
        level: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEvaluator``.

        :param evaluator_config: The configuration that defines how an evaluator assesses agent performance.
        :param evaluator_name: The name of the evaluator. Must be unique within your account.
        :param level: 
        :param description: The description of the evaluator.
        :param tags: A list of tags to assign to the evaluator.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-evaluator.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            # additional_model_request_fields: Any
            
            cfn_evaluator_props = bedrockagentcore.CfnEvaluatorProps(
                evaluator_config=bedrockagentcore.CfnEvaluator.EvaluatorConfigProperty(
                    llm_as_aJudge=bedrockagentcore.CfnEvaluator.LlmAsAJudgeEvaluatorConfigProperty(
                        instructions="instructions",
                        model_config=bedrockagentcore.CfnEvaluator.EvaluatorModelConfigProperty(
                            bedrock_evaluator_model_config=bedrockagentcore.CfnEvaluator.BedrockEvaluatorModelConfigProperty(
                                model_id="modelId",
            
                                # the properties below are optional
                                additional_model_request_fields=additional_model_request_fields,
                                inference_config=bedrockagentcore.CfnEvaluator.InferenceConfigurationProperty(
                                    max_tokens=123,
                                    temperature=123,
                                    top_p=123
                                )
                            )
                        ),
                        rating_scale=bedrockagentcore.CfnEvaluator.RatingScaleProperty(
                            categorical=[bedrockagentcore.CfnEvaluator.CategoricalScaleDefinitionProperty(
                                definition="definition",
                                label="label"
                            )],
                            numerical=[bedrockagentcore.CfnEvaluator.NumericalScaleDefinitionProperty(
                                definition="definition",
                                label="label",
                                value=123
                            )]
                        )
                    )
                ),
                evaluator_name="evaluatorName",
                level="level",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c769c32f0049d1195b80f5b76b8b678dcf5ad1c67ed7fa7571832bf6792ef2f3)
            check_type(argname="argument evaluator_config", value=evaluator_config, expected_type=type_hints["evaluator_config"])
            check_type(argname="argument evaluator_name", value=evaluator_name, expected_type=type_hints["evaluator_name"])
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "evaluator_config": evaluator_config,
            "evaluator_name": evaluator_name,
            "level": level,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def evaluator_config(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnEvaluator.EvaluatorConfigProperty"]:
        '''The configuration that defines how an evaluator assesses agent performance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-evaluator.html#cfn-bedrockagentcore-evaluator-evaluatorconfig
        '''
        result = self._values.get("evaluator_config")
        assert result is not None, "Required property 'evaluator_config' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnEvaluator.EvaluatorConfigProperty"], result)

    @builtins.property
    def evaluator_name(self) -> builtins.str:
        '''The name of the evaluator.

        Must be unique within your account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-evaluator.html#cfn-bedrockagentcore-evaluator-evaluatorname
        '''
        result = self._values.get("evaluator_name")
        assert result is not None, "Required property 'evaluator_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def level(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-evaluator.html#cfn-bedrockagentcore-evaluator-level
        '''
        result = self._values.get("level")
        assert result is not None, "Required property 'level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the evaluator.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-evaluator.html#cfn-bedrockagentcore-evaluator-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A list of tags to assign to the evaluator.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-evaluator.html#cfn-bedrockagentcore-evaluator-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEvaluatorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IGatewayRef_a3ed30fe, _ITaggableV2_4e6798f8)
class CfnGateway(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway",
):
    '''Amazon Bedrock AgentCore Gateway provides a unified connectivity layer between agents and the tools and resources they need to interact with.

    For more information about creating a gateway, see `Set up an Amazon Bedrock AgentCore gateway <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html
    :cloudformationResource: AWS::BedrockAgentCore::Gateway
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_gateway = bedrockagentcore.CfnGateway(self, "MyCfnGateway",
            authorizer_type="authorizerType",
            name="name",
            protocol_type="protocolType",
            role_arn="roleArn",
        
            # the properties below are optional
            authorizer_configuration=bedrockagentcore.CfnGateway.AuthorizerConfigurationProperty(
                custom_jwt_authorizer=bedrockagentcore.CfnGateway.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
        
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"],
                    allowed_scopes=["allowedScopes"],
                    custom_claims=[bedrockagentcore.CfnGateway.CustomClaimValidationTypeProperty(
                        authorizing_claim_match_value=bedrockagentcore.CfnGateway.AuthorizingClaimMatchValueTypeProperty(
                            claim_match_operator="claimMatchOperator",
                            claim_match_value=bedrockagentcore.CfnGateway.ClaimMatchValueTypeProperty(
                                match_value_string="matchValueString",
                                match_value_string_list=["matchValueStringList"]
                            )
                        ),
                        inbound_token_claim_name="inboundTokenClaimName",
                        inbound_token_claim_value_type="inboundTokenClaimValueType"
                    )]
                )
            ),
            description="description",
            exception_level="exceptionLevel",
            interceptor_configurations=[bedrockagentcore.CfnGateway.GatewayInterceptorConfigurationProperty(
                interception_points=["interceptionPoints"],
                interceptor=bedrockagentcore.CfnGateway.InterceptorConfigurationProperty(
                    lambda_=bedrockagentcore.CfnGateway.LambdaInterceptorConfigurationProperty(
                        arn="arn"
                    )
                ),
        
                # the properties below are optional
                input_configuration=bedrockagentcore.CfnGateway.InterceptorInputConfigurationProperty(
                    pass_request_headers=False
                )
            )],
            kms_key_arn="kmsKeyArn",
            protocol_configuration=bedrockagentcore.CfnGateway.GatewayProtocolConfigurationProperty(
                mcp=bedrockagentcore.CfnGateway.MCPGatewayConfigurationProperty(
                    instructions="instructions",
                    search_type="searchType",
                    supported_versions=["supportedVersions"]
                )
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        authorizer_type: builtins.str,
        name: builtins.str,
        protocol_type: builtins.str,
        role_arn: builtins.str,
        authorizer_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        exception_level: typing.Optional[builtins.str] = None,
        interceptor_configurations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.GatewayInterceptorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        protocol_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.GatewayProtocolConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::Gateway``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param authorizer_type: The authorizer type for the gateway.
        :param name: The name for the gateway.
        :param protocol_type: The protocol type for the gateway target.
        :param role_arn: 
        :param authorizer_configuration: 
        :param description: The description for the gateway.
        :param exception_level: The exception level for the gateway.
        :param interceptor_configurations: 
        :param kms_key_arn: The KMS key ARN for the gateway.
        :param protocol_configuration: The protocol configuration for the gateway target.
        :param tags: The tags for the gateway.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__718d4d7128ca57b0228b268f1204c5574e63e51d4e7701a53fd67a1e8ec17c63)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGatewayProps(
            authorizer_type=authorizer_type,
            name=name,
            protocol_type=protocol_type,
            role_arn=role_arn,
            authorizer_configuration=authorizer_configuration,
            description=description,
            exception_level=exception_level,
            interceptor_configurations=interceptor_configurations,
            kms_key_arn=kms_key_arn,
            protocol_configuration=protocol_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForGateway")
    @builtins.classmethod
    def arn_for_gateway(cls, resource: "_IGatewayRef_a3ed30fe") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c4c1faa26b1254e7e81bc3fba266c51f8b0763206acf1eb473d1904042a366e)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForGateway", [resource]))

    @jsii.member(jsii_name="isCfnGateway")
    @builtins.classmethod
    def is_cfn_gateway(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnGateway.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f42a0d18f9ffc74f0e48860c5e4ddcf51e6d14b3b472636555bf41fbb6963f3)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnGateway", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1253940d92e3f35d08808461458766f65528b0878c674311aabd74aa0a76ce30)
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
            type_hints = typing.get_type_hints(_typecheckingstub__67e1eb8798612291b5b13aae1ac0d9cb4513c21df38593628be4d5e2fe660886)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time at which the gateway was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayArn")
    def attr_gateway_arn(self) -> builtins.str:
        '''The ARN for the gateway.

        :cloudformationAttribute: GatewayArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayArn"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayIdentifier")
    def attr_gateway_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: GatewayIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayUrl")
    def attr_gateway_url(self) -> builtins.str:
        '''The gateway URL for the gateway.

        :cloudformationAttribute: GatewayUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status for the gateway.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReasons")
    def attr_status_reasons(self) -> typing.List[builtins.str]:
        '''The status reasons for the gateway.

        :cloudformationAttribute: StatusReasons
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrStatusReasons"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkloadIdentityDetails")
    def attr_workload_identity_details(self) -> "_IResolvable_da3f097b":
        '''
        :cloudformationAttribute: WorkloadIdentityDetails
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrWorkloadIdentityDetails"))

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
    @jsii.member(jsii_name="gatewayRef")
    def gateway_ref(self) -> "_GatewayReference_350c3a07":
        '''A reference to a Gateway resource.'''
        return typing.cast("_GatewayReference_350c3a07", jsii.get(self, "gatewayRef"))

    @builtins.property
    @jsii.member(jsii_name="authorizerType")
    def authorizer_type(self) -> builtins.str:
        '''The authorizer type for the gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "authorizerType"))

    @authorizer_type.setter
    def authorizer_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3733b65f293d2d9f1304c9c6a4cfd4c4aa4a9dca54f65a221b403a9fa85809d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__faac8d45eefa612f06e0139bc26af7005d13df5a552a63d10084bfbc444fd266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocolType")
    def protocol_type(self) -> builtins.str:
        '''The protocol type for the gateway target.'''
        return typing.cast(builtins.str, jsii.get(self, "protocolType"))

    @protocol_type.setter
    def protocol_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d2ccf9c2c13ca5a79d82fee59155dfbaa87d3d17ccc1f27959c635732127d90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a750b424a29fb58f4f0dcc52028237d740f0b0b92d8420600048da5b20537f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="authorizerConfiguration")
    def authorizer_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.AuthorizerConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.AuthorizerConfigurationProperty"]], jsii.get(self, "authorizerConfiguration"))

    @authorizer_configuration.setter
    def authorizer_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.AuthorizerConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c34ffb86639149c1c6323ad6aa1ec7b9f7d9e7f17a5f5306e5d67d30110ba83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b89e3b58faac93b47a86d253bd377ccfed6b64d0088167686a5ce5a6f01bc27b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="exceptionLevel")
    def exception_level(self) -> typing.Optional[builtins.str]:
        '''The exception level for the gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exceptionLevel"))

    @exception_level.setter
    def exception_level(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__791936566b3e629fd378dc6a46c31b1a5134acc616fbd9ed9eebc092ed3be3e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exceptionLevel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="interceptorConfigurations")
    def interceptor_configurations(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayInterceptorConfigurationProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayInterceptorConfigurationProperty"]]]], jsii.get(self, "interceptorConfigurations"))

    @interceptor_configurations.setter
    def interceptor_configurations(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayInterceptorConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fa23efd99303a8f763464c84881ac739adef3c104051bc1d3f02ad8262450c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interceptorConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The KMS key ARN for the gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d2d9d8c84164d38a9976889d155298546ea61a787e120117719ee748ac6cf6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocolConfiguration")
    def protocol_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayProtocolConfigurationProperty"]]:
        '''The protocol configuration for the gateway target.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayProtocolConfigurationProperty"]], jsii.get(self, "protocolConfiguration"))

    @protocol_configuration.setter
    def protocol_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayProtocolConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05982d11a516cc3cf2e986a22173b4993c5267490c660a8f123f9c141f3f117b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the gateway.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8136c8abfebcb699dd26d8e65dbb8e7a922f1cdc2f58375541b3436f139609a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.AuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_jwt_authorizer": "customJwtAuthorizer"},
    )
    class AuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            custom_jwt_authorizer: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.CustomJWTAuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param custom_jwt_authorizer: The authorizer configuration for the gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-authorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                authorizer_configuration_property = bedrockagentcore.CfnGateway.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=bedrockagentcore.CfnGateway.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
                
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"],
                        allowed_scopes=["allowedScopes"],
                        custom_claims=[bedrockagentcore.CfnGateway.CustomClaimValidationTypeProperty(
                            authorizing_claim_match_value=bedrockagentcore.CfnGateway.AuthorizingClaimMatchValueTypeProperty(
                                claim_match_operator="claimMatchOperator",
                                claim_match_value=bedrockagentcore.CfnGateway.ClaimMatchValueTypeProperty(
                                    match_value_string="matchValueString",
                                    match_value_string_list=["matchValueStringList"]
                                )
                            ),
                            inbound_token_claim_name="inboundTokenClaimName",
                            inbound_token_claim_value_type="inboundTokenClaimValueType"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__788309d24193b18115a31defebe9337a71550513b7163a4a603f72832a42ab79)
                check_type(argname="argument custom_jwt_authorizer", value=custom_jwt_authorizer, expected_type=type_hints["custom_jwt_authorizer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "custom_jwt_authorizer": custom_jwt_authorizer,
            }

        @builtins.property
        def custom_jwt_authorizer(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnGateway.CustomJWTAuthorizerConfigurationProperty"]:
            '''The authorizer configuration for the gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-authorizerconfiguration.html#cfn-bedrockagentcore-gateway-authorizerconfiguration-customjwtauthorizer
            '''
            result = self._values.get("custom_jwt_authorizer")
            assert result is not None, "Required property 'custom_jwt_authorizer' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGateway.CustomJWTAuthorizerConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.AuthorizingClaimMatchValueTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "claim_match_operator": "claimMatchOperator",
            "claim_match_value": "claimMatchValue",
        },
    )
    class AuthorizingClaimMatchValueTypeProperty:
        def __init__(
            self,
            *,
            claim_match_operator: builtins.str,
            claim_match_value: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.ClaimMatchValueTypeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The value or values in the custom claim to match and relationship of match.

            :param claim_match_operator: The relationship between the claim field value and the value or values being matched.
            :param claim_match_value: The value or values in the custom claim to match for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-authorizingclaimmatchvaluetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                authorizing_claim_match_value_type_property = bedrockagentcore.CfnGateway.AuthorizingClaimMatchValueTypeProperty(
                    claim_match_operator="claimMatchOperator",
                    claim_match_value=bedrockagentcore.CfnGateway.ClaimMatchValueTypeProperty(
                        match_value_string="matchValueString",
                        match_value_string_list=["matchValueStringList"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__112b8d24bc38c0672ed793eba77bfe0cf27779ec1b6d92d7be444d118bc83903)
                check_type(argname="argument claim_match_operator", value=claim_match_operator, expected_type=type_hints["claim_match_operator"])
                check_type(argname="argument claim_match_value", value=claim_match_value, expected_type=type_hints["claim_match_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "claim_match_operator": claim_match_operator,
                "claim_match_value": claim_match_value,
            }

        @builtins.property
        def claim_match_operator(self) -> builtins.str:
            '''The relationship between the claim field value and the value or values being matched.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-authorizingclaimmatchvaluetype.html#cfn-bedrockagentcore-gateway-authorizingclaimmatchvaluetype-claimmatchoperator
            '''
            result = self._values.get("claim_match_operator")
            assert result is not None, "Required property 'claim_match_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def claim_match_value(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnGateway.ClaimMatchValueTypeProperty"]:
            '''The value or values in the custom claim to match for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-authorizingclaimmatchvaluetype.html#cfn-bedrockagentcore-gateway-authorizingclaimmatchvaluetype-claimmatchvalue
            '''
            result = self._values.get("claim_match_value")
            assert result is not None, "Required property 'claim_match_value' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGateway.ClaimMatchValueTypeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizingClaimMatchValueTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.ClaimMatchValueTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "match_value_string": "matchValueString",
            "match_value_string_list": "matchValueStringList",
        },
    )
    class ClaimMatchValueTypeProperty:
        def __init__(
            self,
            *,
            match_value_string: typing.Optional[builtins.str] = None,
            match_value_string_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The value or values in the custom claim to match for.

            :param match_value_string: The string value to match for.
            :param match_value_string_list: The list of strings to check for a match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-claimmatchvaluetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                claim_match_value_type_property = bedrockagentcore.CfnGateway.ClaimMatchValueTypeProperty(
                    match_value_string="matchValueString",
                    match_value_string_list=["matchValueStringList"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__952f117dc1f1b6b566aad149f8da1ff097edfd2bc2daad409806c1b726178c95)
                check_type(argname="argument match_value_string", value=match_value_string, expected_type=type_hints["match_value_string"])
                check_type(argname="argument match_value_string_list", value=match_value_string_list, expected_type=type_hints["match_value_string_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if match_value_string is not None:
                self._values["match_value_string"] = match_value_string
            if match_value_string_list is not None:
                self._values["match_value_string_list"] = match_value_string_list

        @builtins.property
        def match_value_string(self) -> typing.Optional[builtins.str]:
            '''The string value to match for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-claimmatchvaluetype.html#cfn-bedrockagentcore-gateway-claimmatchvaluetype-matchvaluestring
            '''
            result = self._values.get("match_value_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def match_value_string_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of strings to check for a match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-claimmatchvaluetype.html#cfn-bedrockagentcore-gateway-claimmatchvaluetype-matchvaluestringlist
            '''
            result = self._values.get("match_value_string_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClaimMatchValueTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.CustomClaimValidationTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorizing_claim_match_value": "authorizingClaimMatchValue",
            "inbound_token_claim_name": "inboundTokenClaimName",
            "inbound_token_claim_value_type": "inboundTokenClaimValueType",
        },
    )
    class CustomClaimValidationTypeProperty:
        def __init__(
            self,
            *,
            authorizing_claim_match_value: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.AuthorizingClaimMatchValueTypeProperty", typing.Dict[builtins.str, typing.Any]]],
            inbound_token_claim_name: builtins.str,
            inbound_token_claim_value_type: builtins.str,
        ) -> None:
            '''Required custom claim.

            :param authorizing_claim_match_value: The value or values in the custom claim to match and relationship of match.
            :param inbound_token_claim_name: The name of the custom claim to validate.
            :param inbound_token_claim_value_type: Token claim data type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customclaimvalidationtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_claim_validation_type_property = bedrockagentcore.CfnGateway.CustomClaimValidationTypeProperty(
                    authorizing_claim_match_value=bedrockagentcore.CfnGateway.AuthorizingClaimMatchValueTypeProperty(
                        claim_match_operator="claimMatchOperator",
                        claim_match_value=bedrockagentcore.CfnGateway.ClaimMatchValueTypeProperty(
                            match_value_string="matchValueString",
                            match_value_string_list=["matchValueStringList"]
                        )
                    ),
                    inbound_token_claim_name="inboundTokenClaimName",
                    inbound_token_claim_value_type="inboundTokenClaimValueType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__281a42b48773fc98dfce972077d5fadbe244532c4820ce9f7f40d8d292180dd3)
                check_type(argname="argument authorizing_claim_match_value", value=authorizing_claim_match_value, expected_type=type_hints["authorizing_claim_match_value"])
                check_type(argname="argument inbound_token_claim_name", value=inbound_token_claim_name, expected_type=type_hints["inbound_token_claim_name"])
                check_type(argname="argument inbound_token_claim_value_type", value=inbound_token_claim_value_type, expected_type=type_hints["inbound_token_claim_value_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorizing_claim_match_value": authorizing_claim_match_value,
                "inbound_token_claim_name": inbound_token_claim_name,
                "inbound_token_claim_value_type": inbound_token_claim_value_type,
            }

        @builtins.property
        def authorizing_claim_match_value(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnGateway.AuthorizingClaimMatchValueTypeProperty"]:
            '''The value or values in the custom claim to match and relationship of match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customclaimvalidationtype.html#cfn-bedrockagentcore-gateway-customclaimvalidationtype-authorizingclaimmatchvalue
            '''
            result = self._values.get("authorizing_claim_match_value")
            assert result is not None, "Required property 'authorizing_claim_match_value' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGateway.AuthorizingClaimMatchValueTypeProperty"], result)

        @builtins.property
        def inbound_token_claim_name(self) -> builtins.str:
            '''The name of the custom claim to validate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customclaimvalidationtype.html#cfn-bedrockagentcore-gateway-customclaimvalidationtype-inboundtokenclaimname
            '''
            result = self._values.get("inbound_token_claim_name")
            assert result is not None, "Required property 'inbound_token_claim_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def inbound_token_claim_value_type(self) -> builtins.str:
            '''Token claim data type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customclaimvalidationtype.html#cfn-bedrockagentcore-gateway-customclaimvalidationtype-inboundtokenclaimvaluetype
            '''
            result = self._values.get("inbound_token_claim_value_type")
            assert result is not None, "Required property 'inbound_token_claim_value_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomClaimValidationTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.CustomJWTAuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "discovery_url": "discoveryUrl",
            "allowed_audience": "allowedAudience",
            "allowed_clients": "allowedClients",
            "allowed_scopes": "allowedScopes",
            "custom_claims": "customClaims",
        },
    )
    class CustomJWTAuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            discovery_url: builtins.str,
            allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
            custom_claims: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.CustomClaimValidationTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param discovery_url: The discovery URL for the authorizer configuration.
            :param allowed_audience: The allowed audience authorized for the gateway target.
            :param allowed_clients: 
            :param allowed_scopes: 
            :param custom_claims: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_jWTAuthorizer_configuration_property = bedrockagentcore.CfnGateway.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
                
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"],
                    allowed_scopes=["allowedScopes"],
                    custom_claims=[bedrockagentcore.CfnGateway.CustomClaimValidationTypeProperty(
                        authorizing_claim_match_value=bedrockagentcore.CfnGateway.AuthorizingClaimMatchValueTypeProperty(
                            claim_match_operator="claimMatchOperator",
                            claim_match_value=bedrockagentcore.CfnGateway.ClaimMatchValueTypeProperty(
                                match_value_string="matchValueString",
                                match_value_string_list=["matchValueStringList"]
                            )
                        ),
                        inbound_token_claim_name="inboundTokenClaimName",
                        inbound_token_claim_value_type="inboundTokenClaimValueType"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8cc4944f630bec36007bb93b09eab3e99763f1bed11457e642c0ab535144159e)
                check_type(argname="argument discovery_url", value=discovery_url, expected_type=type_hints["discovery_url"])
                check_type(argname="argument allowed_audience", value=allowed_audience, expected_type=type_hints["allowed_audience"])
                check_type(argname="argument allowed_clients", value=allowed_clients, expected_type=type_hints["allowed_clients"])
                check_type(argname="argument allowed_scopes", value=allowed_scopes, expected_type=type_hints["allowed_scopes"])
                check_type(argname="argument custom_claims", value=custom_claims, expected_type=type_hints["custom_claims"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "discovery_url": discovery_url,
            }
            if allowed_audience is not None:
                self._values["allowed_audience"] = allowed_audience
            if allowed_clients is not None:
                self._values["allowed_clients"] = allowed_clients
            if allowed_scopes is not None:
                self._values["allowed_scopes"] = allowed_scopes
            if custom_claims is not None:
                self._values["custom_claims"] = custom_claims

        @builtins.property
        def discovery_url(self) -> builtins.str:
            '''The discovery URL for the authorizer configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-discoveryurl
            '''
            result = self._values.get("discovery_url")
            assert result is not None, "Required property 'discovery_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_audience(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The allowed audience authorized for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedaudience
            '''
            result = self._values.get("allowed_audience")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_clients(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedclients
            '''
            result = self._values.get("allowed_clients")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-allowedscopes
            '''
            result = self._values.get("allowed_scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def custom_claims(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.CustomClaimValidationTypeProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-gateway-customjwtauthorizerconfiguration-customclaims
            '''
            result = self._values.get("custom_claims")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.CustomClaimValidationTypeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomJWTAuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.GatewayInterceptorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "interception_points": "interceptionPoints",
            "interceptor": "interceptor",
            "input_configuration": "inputConfiguration",
        },
    )
    class GatewayInterceptorConfigurationProperty:
        def __init__(
            self,
            *,
            interception_points: typing.Sequence[builtins.str],
            interceptor: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.InterceptorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            input_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.InterceptorInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param interception_points: 
            :param interceptor: 
            :param input_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                gateway_interceptor_configuration_property = bedrockagentcore.CfnGateway.GatewayInterceptorConfigurationProperty(
                    interception_points=["interceptionPoints"],
                    interceptor=bedrockagentcore.CfnGateway.InterceptorConfigurationProperty(
                        lambda_=bedrockagentcore.CfnGateway.LambdaInterceptorConfigurationProperty(
                            arn="arn"
                        )
                    ),
                
                    # the properties below are optional
                    input_configuration=bedrockagentcore.CfnGateway.InterceptorInputConfigurationProperty(
                        pass_request_headers=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__715cb5162dd44f0620c0da9c35156ecbbe6adcf966dd3dabfefa1ba61c16a0aa)
                check_type(argname="argument interception_points", value=interception_points, expected_type=type_hints["interception_points"])
                check_type(argname="argument interceptor", value=interceptor, expected_type=type_hints["interceptor"])
                check_type(argname="argument input_configuration", value=input_configuration, expected_type=type_hints["input_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "interception_points": interception_points,
                "interceptor": interceptor,
            }
            if input_configuration is not None:
                self._values["input_configuration"] = input_configuration

        @builtins.property
        def interception_points(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration.html#cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-interceptionpoints
            '''
            result = self._values.get("interception_points")
            assert result is not None, "Required property 'interception_points' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def interceptor(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnGateway.InterceptorConfigurationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration.html#cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-interceptor
            '''
            result = self._values.get("interceptor")
            assert result is not None, "Required property 'interceptor' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGateway.InterceptorConfigurationProperty"], result)

        @builtins.property
        def input_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.InterceptorInputConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-gatewayinterceptorconfiguration.html#cfn-bedrockagentcore-gateway-gatewayinterceptorconfiguration-inputconfiguration
            '''
            result = self._values.get("input_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.InterceptorInputConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayInterceptorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.GatewayProtocolConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"mcp": "mcp"},
    )
    class GatewayProtocolConfigurationProperty:
        def __init__(
            self,
            *,
            mcp: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.MCPGatewayConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The protocol configuration.

            :param mcp: The gateway protocol configuration for MCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                gateway_protocol_configuration_property = bedrockagentcore.CfnGateway.GatewayProtocolConfigurationProperty(
                    mcp=bedrockagentcore.CfnGateway.MCPGatewayConfigurationProperty(
                        instructions="instructions",
                        search_type="searchType",
                        supported_versions=["supportedVersions"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__381e09b484f23635acaed28352a759fdd9ac853b91ce6a848c9ed3892887eb7c)
                check_type(argname="argument mcp", value=mcp, expected_type=type_hints["mcp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mcp": mcp,
            }

        @builtins.property
        def mcp(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnGateway.MCPGatewayConfigurationProperty"]:
            '''The gateway protocol configuration for MCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-gatewayprotocolconfiguration.html#cfn-bedrockagentcore-gateway-gatewayprotocolconfiguration-mcp
            '''
            result = self._values.get("mcp")
            assert result is not None, "Required property 'mcp' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGateway.MCPGatewayConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayProtocolConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.InterceptorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_": "lambda"},
    )
    class InterceptorConfigurationProperty:
        def __init__(
            self,
            *,
            lambda_: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.LambdaInterceptorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param lambda_: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-interceptorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                interceptor_configuration_property = bedrockagentcore.CfnGateway.InterceptorConfigurationProperty(
                    lambda_=bedrockagentcore.CfnGateway.LambdaInterceptorConfigurationProperty(
                        arn="arn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4ca22e725c6291ac4361eed78ba4e61d1c53d3ed16f378864154be6a22b3fbdc)
                check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_": lambda_,
            }

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnGateway.LambdaInterceptorConfigurationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-interceptorconfiguration.html#cfn-bedrockagentcore-gateway-interceptorconfiguration-lambda
            '''
            result = self._values.get("lambda_")
            assert result is not None, "Required property 'lambda_' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGateway.LambdaInterceptorConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InterceptorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.InterceptorInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"pass_request_headers": "passRequestHeaders"},
    )
    class InterceptorInputConfigurationProperty:
        def __init__(
            self,
            *,
            pass_request_headers: typing.Union[builtins.bool, "_IResolvable_da3f097b"],
        ) -> None:
            '''
            :param pass_request_headers: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-interceptorinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                interceptor_input_configuration_property = bedrockagentcore.CfnGateway.InterceptorInputConfigurationProperty(
                    pass_request_headers=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1a99f30cc6576d66eb555d4d72e4d8cc323b7560bf001996fd8ea8a3cbcdee5f)
                check_type(argname="argument pass_request_headers", value=pass_request_headers, expected_type=type_hints["pass_request_headers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "pass_request_headers": pass_request_headers,
            }

        @builtins.property
        def pass_request_headers(
            self,
        ) -> typing.Union[builtins.bool, "_IResolvable_da3f097b"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-interceptorinputconfiguration.html#cfn-bedrockagentcore-gateway-interceptorinputconfiguration-passrequestheaders
            '''
            result = self._values.get("pass_request_headers")
            assert result is not None, "Required property 'pass_request_headers' is missing"
            return typing.cast(typing.Union[builtins.bool, "_IResolvable_da3f097b"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InterceptorInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.LambdaInterceptorConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class LambdaInterceptorConfigurationProperty:
        def __init__(self, *, arn: builtins.str) -> None:
            '''
            :param arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-lambdainterceptorconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                lambda_interceptor_configuration_property = bedrockagentcore.CfnGateway.LambdaInterceptorConfigurationProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4fdc3a3b136445d808e02f01ce34f7cf7f93adae6e8dae1f234c0991d3782da4)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-lambdainterceptorconfiguration.html#cfn-bedrockagentcore-gateway-lambdainterceptorconfiguration-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaInterceptorConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.MCPGatewayConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instructions": "instructions",
            "search_type": "searchType",
            "supported_versions": "supportedVersions",
        },
    )
    class MCPGatewayConfigurationProperty:
        def __init__(
            self,
            *,
            instructions: typing.Optional[builtins.str] = None,
            search_type: typing.Optional[builtins.str] = None,
            supported_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The gateway configuration for MCP.

            :param instructions: 
            :param search_type: The MCP gateway configuration search type.
            :param supported_versions: The supported versions for the MCP configuration for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                m_cPGateway_configuration_property = bedrockagentcore.CfnGateway.MCPGatewayConfigurationProperty(
                    instructions="instructions",
                    search_type="searchType",
                    supported_versions=["supportedVersions"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__caff723b1f8dc289e3e0d1f554fe16628873911a93ec8c36ed92f59cde7798c4)
                check_type(argname="argument instructions", value=instructions, expected_type=type_hints["instructions"])
                check_type(argname="argument search_type", value=search_type, expected_type=type_hints["search_type"])
                check_type(argname="argument supported_versions", value=supported_versions, expected_type=type_hints["supported_versions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if instructions is not None:
                self._values["instructions"] = instructions
            if search_type is not None:
                self._values["search_type"] = search_type
            if supported_versions is not None:
                self._values["supported_versions"] = supported_versions

        @builtins.property
        def instructions(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration.html#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-instructions
            '''
            result = self._values.get("instructions")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def search_type(self) -> typing.Optional[builtins.str]:
            '''The MCP gateway configuration search type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration.html#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-searchtype
            '''
            result = self._values.get("search_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def supported_versions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The supported versions for the MCP configuration for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-mcpgatewayconfiguration.html#cfn-bedrockagentcore-gateway-mcpgatewayconfiguration-supportedversions
            '''
            result = self._values.get("supported_versions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MCPGatewayConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGateway.WorkloadIdentityDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"workload_identity_arn": "workloadIdentityArn"},
    )
    class WorkloadIdentityDetailsProperty:
        def __init__(self, *, workload_identity_arn: builtins.str) -> None:
            '''The workload identity details for the gateway.

            :param workload_identity_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-workloadidentitydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                workload_identity_details_property = bedrockagentcore.CfnGateway.WorkloadIdentityDetailsProperty(
                    workload_identity_arn="workloadIdentityArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e940e88ca017f9ccde7a0419db94aaed6321cc4f2368ad6aa9fe229c8d1d8a3a)
                check_type(argname="argument workload_identity_arn", value=workload_identity_arn, expected_type=type_hints["workload_identity_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workload_identity_arn": workload_identity_arn,
            }

        @builtins.property
        def workload_identity_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gateway-workloadidentitydetails.html#cfn-bedrockagentcore-gateway-workloadidentitydetails-workloadidentityarn
            '''
            result = self._values.get("workload_identity_arn")
            assert result is not None, "Required property 'workload_identity_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkloadIdentityDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "authorizer_type": "authorizerType",
        "name": "name",
        "protocol_type": "protocolType",
        "role_arn": "roleArn",
        "authorizer_configuration": "authorizerConfiguration",
        "description": "description",
        "exception_level": "exceptionLevel",
        "interceptor_configurations": "interceptorConfigurations",
        "kms_key_arn": "kmsKeyArn",
        "protocol_configuration": "protocolConfiguration",
        "tags": "tags",
    },
)
class CfnGatewayProps:
    def __init__(
        self,
        *,
        authorizer_type: builtins.str,
        name: builtins.str,
        protocol_type: builtins.str,
        role_arn: builtins.str,
        authorizer_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        exception_level: typing.Optional[builtins.str] = None,
        interceptor_configurations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.GatewayInterceptorConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        protocol_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.GatewayProtocolConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGateway``.

        :param authorizer_type: The authorizer type for the gateway.
        :param name: The name for the gateway.
        :param protocol_type: The protocol type for the gateway target.
        :param role_arn: 
        :param authorizer_configuration: 
        :param description: The description for the gateway.
        :param exception_level: The exception level for the gateway.
        :param interceptor_configurations: 
        :param kms_key_arn: The KMS key ARN for the gateway.
        :param protocol_configuration: The protocol configuration for the gateway target.
        :param tags: The tags for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_gateway_props = bedrockagentcore.CfnGatewayProps(
                authorizer_type="authorizerType",
                name="name",
                protocol_type="protocolType",
                role_arn="roleArn",
            
                # the properties below are optional
                authorizer_configuration=bedrockagentcore.CfnGateway.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=bedrockagentcore.CfnGateway.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
            
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"],
                        allowed_scopes=["allowedScopes"],
                        custom_claims=[bedrockagentcore.CfnGateway.CustomClaimValidationTypeProperty(
                            authorizing_claim_match_value=bedrockagentcore.CfnGateway.AuthorizingClaimMatchValueTypeProperty(
                                claim_match_operator="claimMatchOperator",
                                claim_match_value=bedrockagentcore.CfnGateway.ClaimMatchValueTypeProperty(
                                    match_value_string="matchValueString",
                                    match_value_string_list=["matchValueStringList"]
                                )
                            ),
                            inbound_token_claim_name="inboundTokenClaimName",
                            inbound_token_claim_value_type="inboundTokenClaimValueType"
                        )]
                    )
                ),
                description="description",
                exception_level="exceptionLevel",
                interceptor_configurations=[bedrockagentcore.CfnGateway.GatewayInterceptorConfigurationProperty(
                    interception_points=["interceptionPoints"],
                    interceptor=bedrockagentcore.CfnGateway.InterceptorConfigurationProperty(
                        lambda_=bedrockagentcore.CfnGateway.LambdaInterceptorConfigurationProperty(
                            arn="arn"
                        )
                    ),
            
                    # the properties below are optional
                    input_configuration=bedrockagentcore.CfnGateway.InterceptorInputConfigurationProperty(
                        pass_request_headers=False
                    )
                )],
                kms_key_arn="kmsKeyArn",
                protocol_configuration=bedrockagentcore.CfnGateway.GatewayProtocolConfigurationProperty(
                    mcp=bedrockagentcore.CfnGateway.MCPGatewayConfigurationProperty(
                        instructions="instructions",
                        search_type="searchType",
                        supported_versions=["supportedVersions"]
                    )
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__790df6c55e75e75d6f8c8a9a5518586d5e4ae350e3bfc4555e2ed4bf3c572f31)
            check_type(argname="argument authorizer_type", value=authorizer_type, expected_type=type_hints["authorizer_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol_type", value=protocol_type, expected_type=type_hints["protocol_type"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument authorizer_configuration", value=authorizer_configuration, expected_type=type_hints["authorizer_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument exception_level", value=exception_level, expected_type=type_hints["exception_level"])
            check_type(argname="argument interceptor_configurations", value=interceptor_configurations, expected_type=type_hints["interceptor_configurations"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument protocol_configuration", value=protocol_configuration, expected_type=type_hints["protocol_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authorizer_type": authorizer_type,
            "name": name,
            "protocol_type": protocol_type,
            "role_arn": role_arn,
        }
        if authorizer_configuration is not None:
            self._values["authorizer_configuration"] = authorizer_configuration
        if description is not None:
            self._values["description"] = description
        if exception_level is not None:
            self._values["exception_level"] = exception_level
        if interceptor_configurations is not None:
            self._values["interceptor_configurations"] = interceptor_configurations
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if protocol_configuration is not None:
            self._values["protocol_configuration"] = protocol_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def authorizer_type(self) -> builtins.str:
        '''The authorizer type for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-authorizertype
        '''
        result = self._values.get("authorizer_type")
        assert result is not None, "Required property 'authorizer_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol_type(self) -> builtins.str:
        '''The protocol type for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-protocoltype
        '''
        result = self._values.get("protocol_type")
        assert result is not None, "Required property 'protocol_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.AuthorizerConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-authorizerconfiguration
        '''
        result = self._values.get("authorizer_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.AuthorizerConfigurationProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exception_level(self) -> typing.Optional[builtins.str]:
        '''The exception level for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-exceptionlevel
        '''
        result = self._values.get("exception_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def interceptor_configurations(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayInterceptorConfigurationProperty"]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-interceptorconfigurations
        '''
        result = self._values.get("interceptor_configurations")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayInterceptorConfigurationProperty"]]]], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The KMS key ARN for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayProtocolConfigurationProperty"]]:
        '''The protocol configuration for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-protocolconfiguration
        '''
        result = self._values.get("protocol_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayProtocolConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gateway.html#cfn-bedrockagentcore-gateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IGatewayTargetRef_e3008479)
class CfnGatewayTarget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget",
):
    '''After creating a gateway, you can add targets, which define the tools that your gateway will host.

    For more information about adding gateway targets, see `Add targets to an existing gateway <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-building-adding-targets.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html
    :cloudformationResource: AWS::BedrockAgentCore::GatewayTarget
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
        
        cfn_gateway_target = bedrockagentcore.CfnGatewayTarget(self, "MyCfnGatewayTarget",
            name="name",
            target_configuration=bedrockagentcore.CfnGatewayTarget.TargetConfigurationProperty(
                mcp=bedrockagentcore.CfnGatewayTarget.McpTargetConfigurationProperty(
                    api_gateway=bedrockagentcore.CfnGatewayTarget.ApiGatewayTargetConfigurationProperty(
                        api_gateway_tool_configuration=bedrockagentcore.CfnGatewayTarget.ApiGatewayToolConfigurationProperty(
                            tool_filters=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolFilterProperty(
                                filter_path="filterPath",
                                methods=["methods"]
                            )],
        
                            # the properties below are optional
                            tool_overrides=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolOverrideProperty(
                                method="method",
                                name="name",
                                path="path",
        
                                # the properties below are optional
                                description="description"
                            )]
                        ),
                        rest_api_id="restApiId",
                        stage="stage"
                    ),
                    lambda_=bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty(
                        lambda_arn="lambdaArn",
                        tool_schema=bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                            inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                                description="description",
                                input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                    type="type",
        
                                    # the properties below are optional
                                    description="description",
                                    items=schema_definition_property_,
                                    properties={
                                        "properties_key": schema_definition_property_
                                    },
                                    required=["required"]
                                ),
                                name="name",
        
                                # the properties below are optional
                                output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                    type="type",
        
                                    # the properties below are optional
                                    description="description",
                                    items=schema_definition_property_,
                                    properties={
                                        "properties_key": schema_definition_property_
                                    },
                                    required=["required"]
                                )
                            )],
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        )
                    ),
                    mcp_server=bedrockagentcore.CfnGatewayTarget.McpServerTargetConfigurationProperty(
                        endpoint="endpoint"
                    ),
                    open_api_schema=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                        inline_payload="inlinePayload",
                        s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                            bucket_owner_account_id="bucketOwnerAccountId",
                            uri="uri"
                        )
                    ),
                    smithy_model=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                        inline_payload="inlinePayload",
                        s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                            bucket_owner_account_id="bucketOwnerAccountId",
                            uri="uri"
                        )
                    )
                )
            ),
        
            # the properties below are optional
            credential_provider_configurations=[bedrockagentcore.CfnGatewayTarget.CredentialProviderConfigurationProperty(
                credential_provider_type="credentialProviderType",
        
                # the properties below are optional
                credential_provider=bedrockagentcore.CfnGatewayTarget.CredentialProviderProperty(
                    api_key_credential_provider=bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty(
                        provider_arn="providerArn",
        
                        # the properties below are optional
                        credential_location="credentialLocation",
                        credential_parameter_name="credentialParameterName",
                        credential_prefix="credentialPrefix"
                    ),
                    oauth_credential_provider=bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty(
                        provider_arn="providerArn",
                        scopes=["scopes"],
        
                        # the properties below are optional
                        custom_parameters={
                            "custom_parameters_key": "customParameters"
                        },
                        default_return_url="defaultReturnUrl",
                        grant_type="grantType"
                    )
                )
            )],
            description="description",
            gateway_identifier="gatewayIdentifier",
            metadata_configuration=bedrockagentcore.CfnGatewayTarget.MetadataConfigurationProperty(
                allowed_query_parameters=["allowedQueryParameters"],
                allowed_request_headers=["allowedRequestHeaders"],
                allowed_response_headers=["allowedResponseHeaders"]
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        target_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.TargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        credential_provider_configurations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.CredentialProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        gateway_identifier: typing.Optional[builtins.str] = None,
        metadata_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.MetadataConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::GatewayTarget``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name for the gateway target.
        :param target_configuration: The target configuration for the Smithy model target.
        :param credential_provider_configurations: The OAuth credential provider configuration.
        :param description: The description for the gateway target.
        :param gateway_identifier: The gateway ID for the gateway target.
        :param metadata_configuration: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ca4172cb2708dfeb7420a18b960df15915d2da8589b9495c034bd700c3bd768)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGatewayTargetProps(
            name=name,
            target_configuration=target_configuration,
            credential_provider_configurations=credential_provider_configurations,
            description=description,
            gateway_identifier=gateway_identifier,
            metadata_configuration=metadata_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnGatewayTarget")
    @builtins.classmethod
    def is_cfn_gateway_target(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnGatewayTarget.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__854a661aa5307cc2007308cd63202762f3651b891f3718a702a07e46ccb0bfc7)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnGatewayTarget", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__facd54b7bb4cca942a82b0859b83ffbee83d2b5964da7507bd01ce76b51602d7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0f55ddaf00701b9be96b4083ffcf99e108df2b912a7fa6a0930aacc493dc19b3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time at which the gateway target was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayArn")
    def attr_gateway_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: GatewayArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLastSynchronizedAt")
    def attr_last_synchronized_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: LastSynchronizedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastSynchronizedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status for the gateway target.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReasons")
    def attr_status_reasons(self) -> typing.List[builtins.str]:
        '''The status reasons for the gateway target.

        :cloudformationAttribute: StatusReasons
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrStatusReasons"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetId")
    def attr_target_id(self) -> builtins.str:
        '''The target ID for the gateway target.

        :cloudformationAttribute: TargetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetId"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The time at which the resource was updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="gatewayTargetRef")
    def gateway_target_ref(self) -> "_GatewayTargetReference_8759ec47":
        '''A reference to a GatewayTarget resource.'''
        return typing.cast("_GatewayTargetReference_8759ec47", jsii.get(self, "gatewayTargetRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the gateway target.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac4fb979142cd31fef07a02c2a4b5e3d0eb49bf962781821346eac630d16fcc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="targetConfiguration")
    def target_configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.TargetConfigurationProperty"]:
        '''The target configuration for the Smithy model target.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.TargetConfigurationProperty"], jsii.get(self, "targetConfiguration"))

    @target_configuration.setter
    def target_configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.TargetConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8d18e620b511ca77468615f894540073998d43a19f84c7bd4555618e80c9a3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="credentialProviderConfigurations")
    def credential_provider_configurations(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.CredentialProviderConfigurationProperty"]]]]:
        '''The OAuth credential provider configuration.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.CredentialProviderConfigurationProperty"]]]], jsii.get(self, "credentialProviderConfigurations"))

    @credential_provider_configurations.setter
    def credential_provider_configurations(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.CredentialProviderConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__087a7adedbf9e4e0e6abc10f84df215c78eebc146c64c53668096978e91820bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialProviderConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the gateway target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88eae40375f8237511c7176b5010bb5247cb77ff6160f37b46d60eac254c2403)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gatewayIdentifier")
    def gateway_identifier(self) -> typing.Optional[builtins.str]:
        '''The gateway ID for the gateway target.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gatewayIdentifier"))

    @gateway_identifier.setter
    def gateway_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4c9f5798e9b6c54f5080d4aef35f1a5d286541a90ad283e95cae82b7a8e7de1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metadataConfiguration")
    def metadata_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.MetadataConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.MetadataConfigurationProperty"]], jsii.get(self, "metadataConfiguration"))

    @metadata_configuration.setter
    def metadata_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.MetadataConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00f16ea27eb83e4b32e092f110d089664b10c9e879d89f80aef450f9dc884a25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataConfiguration", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ApiGatewayTargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "api_gateway_tool_configuration": "apiGatewayToolConfiguration",
            "rest_api_id": "restApiId",
            "stage": "stage",
        },
    )
    class ApiGatewayTargetConfigurationProperty:
        def __init__(
            self,
            *,
            api_gateway_tool_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.ApiGatewayToolConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            rest_api_id: builtins.str,
            stage: builtins.str,
        ) -> None:
            '''
            :param api_gateway_tool_configuration: 
            :param rest_api_id: 
            :param stage: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                api_gateway_target_configuration_property = bedrockagentcore.CfnGatewayTarget.ApiGatewayTargetConfigurationProperty(
                    api_gateway_tool_configuration=bedrockagentcore.CfnGatewayTarget.ApiGatewayToolConfigurationProperty(
                        tool_filters=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolFilterProperty(
                            filter_path="filterPath",
                            methods=["methods"]
                        )],
                
                        # the properties below are optional
                        tool_overrides=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolOverrideProperty(
                            method="method",
                            name="name",
                            path="path",
                
                            # the properties below are optional
                            description="description"
                        )]
                    ),
                    rest_api_id="restApiId",
                    stage="stage"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cd9d5dad412e0ebe1edd2df618041d10540bb992843eb766dfcbf3cfc4a59471)
                check_type(argname="argument api_gateway_tool_configuration", value=api_gateway_tool_configuration, expected_type=type_hints["api_gateway_tool_configuration"])
                check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
                check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_gateway_tool_configuration": api_gateway_tool_configuration,
                "rest_api_id": rest_api_id,
                "stage": stage,
            }

        @builtins.property
        def api_gateway_tool_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiGatewayToolConfigurationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-apigatewaytoolconfiguration
            '''
            result = self._values.get("api_gateway_tool_configuration")
            assert result is not None, "Required property 'api_gateway_tool_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiGatewayToolConfigurationProperty"], result)

        @builtins.property
        def rest_api_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-restapiid
            '''
            result = self._values.get("rest_api_id")
            assert result is not None, "Required property 'rest_api_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def stage(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytargetconfiguration-stage
            '''
            result = self._values.get("stage")
            assert result is not None, "Required property 'stage' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiGatewayTargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ApiGatewayToolConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "tool_filters": "toolFilters",
            "tool_overrides": "toolOverrides",
        },
    )
    class ApiGatewayToolConfigurationProperty:
        def __init__(
            self,
            *,
            tool_filters: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.ApiGatewayToolFilterProperty", typing.Dict[builtins.str, typing.Any]]]]],
            tool_overrides: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.ApiGatewayToolOverrideProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''
            :param tool_filters: 
            :param tool_overrides: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                api_gateway_tool_configuration_property = bedrockagentcore.CfnGatewayTarget.ApiGatewayToolConfigurationProperty(
                    tool_filters=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolFilterProperty(
                        filter_path="filterPath",
                        methods=["methods"]
                    )],
                
                    # the properties below are optional
                    tool_overrides=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolOverrideProperty(
                        method="method",
                        name="name",
                        path="path",
                
                        # the properties below are optional
                        description="description"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c2555658d10c3f76b5e73f49cc83804d6ab06bb7d23b35ffd199342c484c2e7f)
                check_type(argname="argument tool_filters", value=tool_filters, expected_type=type_hints["tool_filters"])
                check_type(argname="argument tool_overrides", value=tool_overrides, expected_type=type_hints["tool_overrides"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "tool_filters": tool_filters,
            }
            if tool_overrides is not None:
                self._values["tool_overrides"] = tool_overrides

        @builtins.property
        def tool_filters(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiGatewayToolFilterProperty"]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-toolfilters
            '''
            result = self._values.get("tool_filters")
            assert result is not None, "Required property 'tool_filters' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiGatewayToolFilterProperty"]]], result)

        @builtins.property
        def tool_overrides(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiGatewayToolOverrideProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolconfiguration-tooloverrides
            '''
            result = self._values.get("tool_overrides")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiGatewayToolOverrideProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiGatewayToolConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ApiGatewayToolFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"filter_path": "filterPath", "methods": "methods"},
    )
    class ApiGatewayToolFilterProperty:
        def __init__(
            self,
            *,
            filter_path: builtins.str,
            methods: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param filter_path: 
            :param methods: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                api_gateway_tool_filter_property = bedrockagentcore.CfnGatewayTarget.ApiGatewayToolFilterProperty(
                    filter_path="filterPath",
                    methods=["methods"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dda3c870c61fb6006992eac9669c748230298d7c2b484443727b9e07c21f2f6e)
                check_type(argname="argument filter_path", value=filter_path, expected_type=type_hints["filter_path"])
                check_type(argname="argument methods", value=methods, expected_type=type_hints["methods"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "filter_path": filter_path,
                "methods": methods,
            }

        @builtins.property
        def filter_path(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolfilter.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-filterpath
            '''
            result = self._values.get("filter_path")
            assert result is not None, "Required property 'filter_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def methods(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytoolfilter.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytoolfilter-methods
            '''
            result = self._values.get("methods")
            assert result is not None, "Required property 'methods' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiGatewayToolFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ApiGatewayToolOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={
            "method": "method",
            "name": "name",
            "path": "path",
            "description": "description",
        },
    )
    class ApiGatewayToolOverrideProperty:
        def __init__(
            self,
            *,
            method: builtins.str,
            name: builtins.str,
            path: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param method: 
            :param name: 
            :param path: 
            :param description: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                api_gateway_tool_override_property = bedrockagentcore.CfnGatewayTarget.ApiGatewayToolOverrideProperty(
                    method="method",
                    name="name",
                    path="path",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__00479c551dd620558403acae09d625ae65f82b950181b59baa770ce5504b9141)
                check_type(argname="argument method", value=method, expected_type=type_hints["method"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "method": method,
                "name": name,
                "path": path,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def method(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-method
            '''
            result = self._values.get("method")
            assert result is not None, "Required property 'method' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def path(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apigatewaytooloverride.html#cfn-bedrockagentcore-gatewaytarget-apigatewaytooloverride-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiGatewayToolOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "provider_arn": "providerArn",
            "credential_location": "credentialLocation",
            "credential_parameter_name": "credentialParameterName",
            "credential_prefix": "credentialPrefix",
        },
    )
    class ApiKeyCredentialProviderProperty:
        def __init__(
            self,
            *,
            provider_arn: builtins.str,
            credential_location: typing.Optional[builtins.str] = None,
            credential_parameter_name: typing.Optional[builtins.str] = None,
            credential_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The API key credential provider for the gateway target.

            :param provider_arn: The provider ARN for the gateway target.
            :param credential_location: The credential location for the gateway target.
            :param credential_parameter_name: The credential parameter name for the provider for the gateway target.
            :param credential_prefix: The API key credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                api_key_credential_provider_property = bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty(
                    provider_arn="providerArn",
                
                    # the properties below are optional
                    credential_location="credentialLocation",
                    credential_parameter_name="credentialParameterName",
                    credential_prefix="credentialPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a33b2b3f3a682c83f92cbd3e15b4552ff1592eb43e06b8e26d9bb1e8f1003ecd)
                check_type(argname="argument provider_arn", value=provider_arn, expected_type=type_hints["provider_arn"])
                check_type(argname="argument credential_location", value=credential_location, expected_type=type_hints["credential_location"])
                check_type(argname="argument credential_parameter_name", value=credential_parameter_name, expected_type=type_hints["credential_parameter_name"])
                check_type(argname="argument credential_prefix", value=credential_prefix, expected_type=type_hints["credential_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "provider_arn": provider_arn,
            }
            if credential_location is not None:
                self._values["credential_location"] = credential_location
            if credential_parameter_name is not None:
                self._values["credential_parameter_name"] = credential_parameter_name
            if credential_prefix is not None:
                self._values["credential_prefix"] = credential_prefix

        @builtins.property
        def provider_arn(self) -> builtins.str:
            '''The provider ARN for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-providerarn
            '''
            result = self._values.get("provider_arn")
            assert result is not None, "Required property 'provider_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def credential_location(self) -> typing.Optional[builtins.str]:
            '''The credential location for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentiallocation
            '''
            result = self._values.get("credential_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def credential_parameter_name(self) -> typing.Optional[builtins.str]:
            '''The credential parameter name for the provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentialparametername
            '''
            result = self._values.get("credential_parameter_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def credential_prefix(self) -> typing.Optional[builtins.str]:
            '''The API key credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apikeycredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-apikeycredentialprovider-credentialprefix
            '''
            result = self._values.get("credential_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiKeyCredentialProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"inline_payload": "inlinePayload", "s3": "s3"},
    )
    class ApiSchemaConfigurationProperty:
        def __init__(
            self,
            *,
            inline_payload: typing.Optional[builtins.str] = None,
            s3: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.S3ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The API schema configuration for the gateway target.

            :param inline_payload: The inline payload for the gateway.
            :param s3: The API schema configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                api_schema_configuration_property = bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                    inline_payload="inlinePayload",
                    s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                        bucket_owner_account_id="bucketOwnerAccountId",
                        uri="uri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__309e9dda1e6dfcce4b7777150028f4c6782bdc89a099f0ac87ab71e9967a8277)
                check_type(argname="argument inline_payload", value=inline_payload, expected_type=type_hints["inline_payload"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if inline_payload is not None:
                self._values["inline_payload"] = inline_payload
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def inline_payload(self) -> typing.Optional[builtins.str]:
            '''The inline payload for the gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration.html#cfn-bedrockagentcore-gatewaytarget-apischemaconfiguration-inlinepayload
            '''
            result = self._values.get("inline_payload")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.S3ConfigurationProperty"]]:
            '''The API schema configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-apischemaconfiguration.html#cfn-bedrockagentcore-gatewaytarget-apischemaconfiguration-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.S3ConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiSchemaConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.CredentialProviderConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "credential_provider_type": "credentialProviderType",
            "credential_provider": "credentialProvider",
        },
    )
    class CredentialProviderConfigurationProperty:
        def __init__(
            self,
            *,
            credential_provider_type: builtins.str,
            credential_provider: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.CredentialProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The credential provider configuration for the gateway target.

            :param credential_provider_type: The credential provider type for the gateway target.
            :param credential_provider: The credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                credential_provider_configuration_property = bedrockagentcore.CfnGatewayTarget.CredentialProviderConfigurationProperty(
                    credential_provider_type="credentialProviderType",
                
                    # the properties below are optional
                    credential_provider=bedrockagentcore.CfnGatewayTarget.CredentialProviderProperty(
                        api_key_credential_provider=bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty(
                            provider_arn="providerArn",
                
                            # the properties below are optional
                            credential_location="credentialLocation",
                            credential_parameter_name="credentialParameterName",
                            credential_prefix="credentialPrefix"
                        ),
                        oauth_credential_provider=bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty(
                            provider_arn="providerArn",
                            scopes=["scopes"],
                
                            # the properties below are optional
                            custom_parameters={
                                "custom_parameters_key": "customParameters"
                            },
                            default_return_url="defaultReturnUrl",
                            grant_type="grantType"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__149dd633d64001d8edf5b8db5417ed0fc1bfaecff9240452d6911051ec05238e)
                check_type(argname="argument credential_provider_type", value=credential_provider_type, expected_type=type_hints["credential_provider_type"])
                check_type(argname="argument credential_provider", value=credential_provider, expected_type=type_hints["credential_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "credential_provider_type": credential_provider_type,
            }
            if credential_provider is not None:
                self._values["credential_provider"] = credential_provider

        @builtins.property
        def credential_provider_type(self) -> builtins.str:
            '''The credential provider type for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration.html#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-credentialprovidertype
            '''
            result = self._values.get("credential_provider_type")
            assert result is not None, "Required property 'credential_provider_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def credential_provider(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.CredentialProviderProperty"]]:
            '''The credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialproviderconfiguration.html#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfiguration-credentialprovider
            '''
            result = self._values.get("credential_provider")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.CredentialProviderProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CredentialProviderConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.CredentialProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "api_key_credential_provider": "apiKeyCredentialProvider",
            "oauth_credential_provider": "oauthCredentialProvider",
        },
    )
    class CredentialProviderProperty:
        def __init__(
            self,
            *,
            api_key_credential_provider: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.ApiKeyCredentialProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            oauth_credential_provider: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.OAuthCredentialProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param api_key_credential_provider: The API key credential provider.
            :param oauth_credential_provider: The OAuth credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                credential_provider_property = bedrockagentcore.CfnGatewayTarget.CredentialProviderProperty(
                    api_key_credential_provider=bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty(
                        provider_arn="providerArn",
                
                        # the properties below are optional
                        credential_location="credentialLocation",
                        credential_parameter_name="credentialParameterName",
                        credential_prefix="credentialPrefix"
                    ),
                    oauth_credential_provider=bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty(
                        provider_arn="providerArn",
                        scopes=["scopes"],
                
                        # the properties below are optional
                        custom_parameters={
                            "custom_parameters_key": "customParameters"
                        },
                        default_return_url="defaultReturnUrl",
                        grant_type="grantType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__db13937427760cb24e319f55daf7a1b38d00d0bb009b7b145665b608c53b0f5c)
                check_type(argname="argument api_key_credential_provider", value=api_key_credential_provider, expected_type=type_hints["api_key_credential_provider"])
                check_type(argname="argument oauth_credential_provider", value=oauth_credential_provider, expected_type=type_hints["oauth_credential_provider"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if api_key_credential_provider is not None:
                self._values["api_key_credential_provider"] = api_key_credential_provider
            if oauth_credential_provider is not None:
                self._values["oauth_credential_provider"] = oauth_credential_provider

        @builtins.property
        def api_key_credential_provider(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiKeyCredentialProviderProperty"]]:
            '''The API key credential provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialprovider.html#cfn-bedrockagentcore-gatewaytarget-credentialprovider-apikeycredentialprovider
            '''
            result = self._values.get("api_key_credential_provider")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiKeyCredentialProviderProperty"]], result)

        @builtins.property
        def oauth_credential_provider(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.OAuthCredentialProviderProperty"]]:
            '''The OAuth credential provider for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-credentialprovider.html#cfn-bedrockagentcore-gatewaytarget-credentialprovider-oauthcredentialprovider
            '''
            result = self._values.get("oauth_credential_provider")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.OAuthCredentialProviderProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CredentialProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_arn": "lambdaArn", "tool_schema": "toolSchema"},
    )
    class McpLambdaTargetConfigurationProperty:
        def __init__(
            self,
            *,
            lambda_arn: builtins.str,
            tool_schema: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.ToolSchemaProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The Lambda target configuration.

            :param lambda_arn: The ARN of the Lambda target configuration.
            :param tool_schema: The tool schema configuration for the gateway target MCP configuration for Lambda.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                mcp_lambda_target_configuration_property = bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty(
                    lambda_arn="lambdaArn",
                    tool_schema=bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                        inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                            description="description",
                            input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                type="type",
                
                                # the properties below are optional
                                description="description",
                                items=schema_definition_property_,
                                properties={
                                    "properties_key": schema_definition_property_
                                },
                                required=["required"]
                            ),
                            name="name",
                
                            # the properties below are optional
                            output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                type="type",
                
                                # the properties below are optional
                                description="description",
                                items=schema_definition_property_,
                                properties={
                                    "properties_key": schema_definition_property_
                                },
                                required=["required"]
                            )
                        )],
                        s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                            bucket_owner_account_id="bucketOwnerAccountId",
                            uri="uri"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e6ba80f262600990b7647765d60a5f51fb86eeeaf8708f22bc73e4794e784785)
                check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
                check_type(argname="argument tool_schema", value=tool_schema, expected_type=type_hints["tool_schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_arn": lambda_arn,
                "tool_schema": tool_schema,
            }

        @builtins.property
        def lambda_arn(self) -> builtins.str:
            '''The ARN of the Lambda target configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            assert result is not None, "Required property 'lambda_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def tool_schema(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ToolSchemaProperty"]:
            '''The tool schema configuration for the gateway target MCP configuration for Lambda.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcplambdatargetconfiguration-toolschema
            '''
            result = self._values.get("tool_schema")
            assert result is not None, "Required property 'tool_schema' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ToolSchemaProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "McpLambdaTargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.McpServerTargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint": "endpoint"},
    )
    class McpServerTargetConfigurationProperty:
        def __init__(self, *, endpoint: builtins.str) -> None:
            '''
            :param endpoint: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                mcp_server_target_configuration_property = bedrockagentcore.CfnGatewayTarget.McpServerTargetConfigurationProperty(
                    endpoint="endpoint"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d73da9473e37697d875f5f3c74a1ab3e3ace8090917b37837b001996968f456a)
                check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "endpoint": endpoint,
            }

        @builtins.property
        def endpoint(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcpservertargetconfiguration-endpoint
            '''
            result = self._values.get("endpoint")
            assert result is not None, "Required property 'endpoint' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "McpServerTargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.McpTargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "api_gateway": "apiGateway",
            "lambda_": "lambda",
            "mcp_server": "mcpServer",
            "open_api_schema": "openApiSchema",
            "smithy_model": "smithyModel",
        },
    )
    class McpTargetConfigurationProperty:
        def __init__(
            self,
            *,
            api_gateway: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.ApiGatewayTargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lambda_: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.McpLambdaTargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            mcp_server: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.McpServerTargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            open_api_schema: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.ApiSchemaConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            smithy_model: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.ApiSchemaConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The MCP target configuration for the gateway target.

            :param api_gateway: 
            :param lambda_: The Lambda MCP configuration for the gateway target.
            :param mcp_server: 
            :param open_api_schema: The OpenApi schema for the gateway target MCP configuration.
            :param smithy_model: The target configuration for the Smithy model target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                mcp_target_configuration_property = bedrockagentcore.CfnGatewayTarget.McpTargetConfigurationProperty(
                    api_gateway=bedrockagentcore.CfnGatewayTarget.ApiGatewayTargetConfigurationProperty(
                        api_gateway_tool_configuration=bedrockagentcore.CfnGatewayTarget.ApiGatewayToolConfigurationProperty(
                            tool_filters=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolFilterProperty(
                                filter_path="filterPath",
                                methods=["methods"]
                            )],
                
                            # the properties below are optional
                            tool_overrides=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolOverrideProperty(
                                method="method",
                                name="name",
                                path="path",
                
                                # the properties below are optional
                                description="description"
                            )]
                        ),
                        rest_api_id="restApiId",
                        stage="stage"
                    ),
                    lambda_=bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty(
                        lambda_arn="lambdaArn",
                        tool_schema=bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                            inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                                description="description",
                                input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                    type="type",
                
                                    # the properties below are optional
                                    description="description",
                                    items=schema_definition_property_,
                                    properties={
                                        "properties_key": schema_definition_property_
                                    },
                                    required=["required"]
                                ),
                                name="name",
                
                                # the properties below are optional
                                output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                    type="type",
                
                                    # the properties below are optional
                                    description="description",
                                    items=schema_definition_property_,
                                    properties={
                                        "properties_key": schema_definition_property_
                                    },
                                    required=["required"]
                                )
                            )],
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        )
                    ),
                    mcp_server=bedrockagentcore.CfnGatewayTarget.McpServerTargetConfigurationProperty(
                        endpoint="endpoint"
                    ),
                    open_api_schema=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                        inline_payload="inlinePayload",
                        s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                            bucket_owner_account_id="bucketOwnerAccountId",
                            uri="uri"
                        )
                    ),
                    smithy_model=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                        inline_payload="inlinePayload",
                        s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                            bucket_owner_account_id="bucketOwnerAccountId",
                            uri="uri"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b1d88210caa384ede03a06bee42d13165c8bf4cc4206a236d795c44da216e3c)
                check_type(argname="argument api_gateway", value=api_gateway, expected_type=type_hints["api_gateway"])
                check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
                check_type(argname="argument mcp_server", value=mcp_server, expected_type=type_hints["mcp_server"])
                check_type(argname="argument open_api_schema", value=open_api_schema, expected_type=type_hints["open_api_schema"])
                check_type(argname="argument smithy_model", value=smithy_model, expected_type=type_hints["smithy_model"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if api_gateway is not None:
                self._values["api_gateway"] = api_gateway
            if lambda_ is not None:
                self._values["lambda_"] = lambda_
            if mcp_server is not None:
                self._values["mcp_server"] = mcp_server
            if open_api_schema is not None:
                self._values["open_api_schema"] = open_api_schema
            if smithy_model is not None:
                self._values["smithy_model"] = smithy_model

        @builtins.property
        def api_gateway(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiGatewayTargetConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-apigateway
            '''
            result = self._values.get("api_gateway")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiGatewayTargetConfigurationProperty"]], result)

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.McpLambdaTargetConfigurationProperty"]]:
            '''The Lambda MCP configuration for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-lambda
            '''
            result = self._values.get("lambda_")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.McpLambdaTargetConfigurationProperty"]], result)

        @builtins.property
        def mcp_server(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.McpServerTargetConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-mcpserver
            '''
            result = self._values.get("mcp_server")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.McpServerTargetConfigurationProperty"]], result)

        @builtins.property
        def open_api_schema(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiSchemaConfigurationProperty"]]:
            '''The OpenApi schema for the gateway target MCP configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-openapischema
            '''
            result = self._values.get("open_api_schema")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiSchemaConfigurationProperty"]], result)

        @builtins.property
        def smithy_model(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiSchemaConfigurationProperty"]]:
            '''The target configuration for the Smithy model target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-mcptargetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-mcptargetconfiguration-smithymodel
            '''
            result = self._values.get("smithy_model")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ApiSchemaConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "McpTargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.MetadataConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allowed_query_parameters": "allowedQueryParameters",
            "allowed_request_headers": "allowedRequestHeaders",
            "allowed_response_headers": "allowedResponseHeaders",
        },
    )
    class MetadataConfigurationProperty:
        def __init__(
            self,
            *,
            allowed_query_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_request_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_response_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param allowed_query_parameters: 
            :param allowed_request_headers: 
            :param allowed_response_headers: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                metadata_configuration_property = bedrockagentcore.CfnGatewayTarget.MetadataConfigurationProperty(
                    allowed_query_parameters=["allowedQueryParameters"],
                    allowed_request_headers=["allowedRequestHeaders"],
                    allowed_response_headers=["allowedResponseHeaders"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__65b76f9cd39a5276e0183029480a0bf70be6f57ac0853a3a5be14eeecae86c0c)
                check_type(argname="argument allowed_query_parameters", value=allowed_query_parameters, expected_type=type_hints["allowed_query_parameters"])
                check_type(argname="argument allowed_request_headers", value=allowed_request_headers, expected_type=type_hints["allowed_request_headers"])
                check_type(argname="argument allowed_response_headers", value=allowed_response_headers, expected_type=type_hints["allowed_response_headers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allowed_query_parameters is not None:
                self._values["allowed_query_parameters"] = allowed_query_parameters
            if allowed_request_headers is not None:
                self._values["allowed_request_headers"] = allowed_request_headers
            if allowed_response_headers is not None:
                self._values["allowed_response_headers"] = allowed_response_headers

        @builtins.property
        def allowed_query_parameters(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration.html#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedqueryparameters
            '''
            result = self._values.get("allowed_query_parameters")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_request_headers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration.html#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedrequestheaders
            '''
            result = self._values.get("allowed_request_headers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_response_headers(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-metadataconfiguration.html#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration-allowedresponseheaders
            '''
            result = self._values.get("allowed_response_headers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetadataConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty",
        jsii_struct_bases=[],
        name_mapping={
            "provider_arn": "providerArn",
            "scopes": "scopes",
            "custom_parameters": "customParameters",
            "default_return_url": "defaultReturnUrl",
            "grant_type": "grantType",
        },
    )
    class OAuthCredentialProviderProperty:
        def __init__(
            self,
            *,
            provider_arn: builtins.str,
            scopes: typing.Sequence[builtins.str],
            custom_parameters: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]] = None,
            default_return_url: typing.Optional[builtins.str] = None,
            grant_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The OAuth credential provider for the gateway target.

            :param provider_arn: The provider ARN for the gateway target.
            :param scopes: The OAuth credential provider scopes.
            :param custom_parameters: The OAuth credential provider.
            :param default_return_url: Return URL for OAuth callback.
            :param grant_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                o_auth_credential_provider_property = bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty(
                    provider_arn="providerArn",
                    scopes=["scopes"],
                
                    # the properties below are optional
                    custom_parameters={
                        "custom_parameters_key": "customParameters"
                    },
                    default_return_url="defaultReturnUrl",
                    grant_type="grantType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c602c1e6012421bcbacb23364333a8030b673b0a8e3ebad72fba42b295c2f64)
                check_type(argname="argument provider_arn", value=provider_arn, expected_type=type_hints["provider_arn"])
                check_type(argname="argument scopes", value=scopes, expected_type=type_hints["scopes"])
                check_type(argname="argument custom_parameters", value=custom_parameters, expected_type=type_hints["custom_parameters"])
                check_type(argname="argument default_return_url", value=default_return_url, expected_type=type_hints["default_return_url"])
                check_type(argname="argument grant_type", value=grant_type, expected_type=type_hints["grant_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "provider_arn": provider_arn,
                "scopes": scopes,
            }
            if custom_parameters is not None:
                self._values["custom_parameters"] = custom_parameters
            if default_return_url is not None:
                self._values["default_return_url"] = default_return_url
            if grant_type is not None:
                self._values["grant_type"] = grant_type

        @builtins.property
        def provider_arn(self) -> builtins.str:
            '''The provider ARN for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-providerarn
            '''
            result = self._values.get("provider_arn")
            assert result is not None, "Required property 'provider_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def scopes(self) -> typing.List[builtins.str]:
            '''The OAuth credential provider scopes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-scopes
            '''
            result = self._values.get("scopes")
            assert result is not None, "Required property 'scopes' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def custom_parameters(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]]:
            '''The OAuth credential provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-customparameters
            '''
            result = self._values.get("custom_parameters")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]], result)

        @builtins.property
        def default_return_url(self) -> typing.Optional[builtins.str]:
            '''Return URL for OAuth callback.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-defaultreturnurl
            '''
            result = self._values.get("default_return_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def grant_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-oauthcredentialprovider.html#cfn-bedrockagentcore-gatewaytarget-oauthcredentialprovider-granttype
            '''
            result = self._values.get("grant_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OAuthCredentialProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_owner_account_id": "bucketOwnerAccountId", "uri": "uri"},
    )
    class S3ConfigurationProperty:
        def __init__(
            self,
            *,
            bucket_owner_account_id: typing.Optional[builtins.str] = None,
            uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The S3 configuration for the gateway target.

            :param bucket_owner_account_id: The S3 configuration bucket owner account ID for the gateway target.
            :param uri: The configuration URI for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-s3configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                s3_configuration_property = bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                    bucket_owner_account_id="bucketOwnerAccountId",
                    uri="uri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0f0b1feb9921a2069b72a9a314cb583fbbc6b6fc8af438b2e8f420e03d0368f7)
                check_type(argname="argument bucket_owner_account_id", value=bucket_owner_account_id, expected_type=type_hints["bucket_owner_account_id"])
                check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_owner_account_id is not None:
                self._values["bucket_owner_account_id"] = bucket_owner_account_id
            if uri is not None:
                self._values["uri"] = uri

        @builtins.property
        def bucket_owner_account_id(self) -> typing.Optional[builtins.str]:
            '''The S3 configuration bucket owner account ID for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-s3configuration.html#cfn-bedrockagentcore-gatewaytarget-s3configuration-bucketowneraccountid
            '''
            result = self._values.get("bucket_owner_account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def uri(self) -> typing.Optional[builtins.str]:
            '''The configuration URI for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-s3configuration.html#cfn-bedrockagentcore-gatewaytarget-s3configuration-uri
            '''
            result = self._values.get("uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "description": "description",
            "items": "items",
            "properties": "properties",
            "required": "required",
        },
    )
    class SchemaDefinitionProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            description: typing.Optional[builtins.str] = None,
            items: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.SchemaDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            properties: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.SchemaDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            required: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The schema definition for the gateway target.

            :param type: The scheme definition type for the gateway target.
            :param description: The workload identity details for the gateway.
            :param items: 
            :param properties: The schema definition properties for the gateway target.
            :param required: The schema definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                schema_definition_property = bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                    type="type",
                
                    # the properties below are optional
                    description="description",
                    items=schema_definition_property_,
                    properties={
                        "properties_key": schema_definition_property_
                    },
                    required=["required"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc512741cd348cf43b33e4ea0df31aae8766e6990dc0675d9111d9a7eb5f9c6a)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument items", value=items, expected_type=type_hints["items"])
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if description is not None:
                self._values["description"] = description
            if items is not None:
                self._values["items"] = items
            if properties is not None:
                self._values["properties"] = properties
            if required is not None:
                self._values["required"] = required

        @builtins.property
        def type(self) -> builtins.str:
            '''The scheme definition type for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html#cfn-bedrockagentcore-gatewaytarget-schemadefinition-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The workload identity details for the gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html#cfn-bedrockagentcore-gatewaytarget-schemadefinition-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def items(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.SchemaDefinitionProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html#cfn-bedrockagentcore-gatewaytarget-schemadefinition-items
            '''
            result = self._values.get("items")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.SchemaDefinitionProperty"]], result)

        @builtins.property
        def properties(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.SchemaDefinitionProperty"]]]]:
            '''The schema definition properties for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html#cfn-bedrockagentcore-gatewaytarget-schemadefinition-properties
            '''
            result = self._values.get("properties")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.SchemaDefinitionProperty"]]]], result)

        @builtins.property
        def required(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The schema definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-schemadefinition.html#cfn-bedrockagentcore-gatewaytarget-schemadefinition-required
            '''
            result = self._values.get("required")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.TargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"mcp": "mcp"},
    )
    class TargetConfigurationProperty:
        def __init__(
            self,
            *,
            mcp: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.McpTargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The target configuration.

            :param mcp: The target configuration definition for MCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                target_configuration_property = bedrockagentcore.CfnGatewayTarget.TargetConfigurationProperty(
                    mcp=bedrockagentcore.CfnGatewayTarget.McpTargetConfigurationProperty(
                        api_gateway=bedrockagentcore.CfnGatewayTarget.ApiGatewayTargetConfigurationProperty(
                            api_gateway_tool_configuration=bedrockagentcore.CfnGatewayTarget.ApiGatewayToolConfigurationProperty(
                                tool_filters=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolFilterProperty(
                                    filter_path="filterPath",
                                    methods=["methods"]
                                )],
                
                                # the properties below are optional
                                tool_overrides=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolOverrideProperty(
                                    method="method",
                                    name="name",
                                    path="path",
                
                                    # the properties below are optional
                                    description="description"
                                )]
                            ),
                            rest_api_id="restApiId",
                            stage="stage"
                        ),
                        lambda_=bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty(
                            lambda_arn="lambdaArn",
                            tool_schema=bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                                inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                                    description="description",
                                    input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                        type="type",
                
                                        # the properties below are optional
                                        description="description",
                                        items=schema_definition_property_,
                                        properties={
                                            "properties_key": schema_definition_property_
                                        },
                                        required=["required"]
                                    ),
                                    name="name",
                
                                    # the properties below are optional
                                    output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                        type="type",
                
                                        # the properties below are optional
                                        description="description",
                                        items=schema_definition_property_,
                                        properties={
                                            "properties_key": schema_definition_property_
                                        },
                                        required=["required"]
                                    )
                                )],
                                s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                    bucket_owner_account_id="bucketOwnerAccountId",
                                    uri="uri"
                                )
                            )
                        ),
                        mcp_server=bedrockagentcore.CfnGatewayTarget.McpServerTargetConfigurationProperty(
                            endpoint="endpoint"
                        ),
                        open_api_schema=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                            inline_payload="inlinePayload",
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        ),
                        smithy_model=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                            inline_payload="inlinePayload",
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a64335e118208df2b03631e56ce84dab935a9d2c9dee1c27c584de679d4dcd6)
                check_type(argname="argument mcp", value=mcp, expected_type=type_hints["mcp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mcp": mcp,
            }

        @builtins.property
        def mcp(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.McpTargetConfigurationProperty"]:
            '''The target configuration definition for MCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-targetconfiguration.html#cfn-bedrockagentcore-gatewaytarget-targetconfiguration-mcp
            '''
            result = self._values.get("mcp")
            assert result is not None, "Required property 'mcp' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.McpTargetConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "description": "description",
            "input_schema": "inputSchema",
            "name": "name",
            "output_schema": "outputSchema",
        },
    )
    class ToolDefinitionProperty:
        def __init__(
            self,
            *,
            description: builtins.str,
            input_schema: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.SchemaDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
            name: builtins.str,
            output_schema: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.SchemaDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The tool definition for the gateway.

            :param description: 
            :param input_schema: The input schema for the gateway target.
            :param name: The tool name.
            :param output_schema: The tool definition output schema for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                tool_definition_property = bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                    description="description",
                    input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                        type="type",
                
                        # the properties below are optional
                        description="description",
                        items=schema_definition_property_,
                        properties={
                            "properties_key": schema_definition_property_
                        },
                        required=["required"]
                    ),
                    name="name",
                
                    # the properties below are optional
                    output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                        type="type",
                
                        # the properties below are optional
                        description="description",
                        items=schema_definition_property_,
                        properties={
                            "properties_key": schema_definition_property_
                        },
                        required=["required"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c9a8204fd6db934022c917c4dc62346cf5269b544292d1bac5ed2aae995a300)
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument input_schema", value=input_schema, expected_type=type_hints["input_schema"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument output_schema", value=output_schema, expected_type=type_hints["output_schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "description": description,
                "input_schema": input_schema,
                "name": name,
            }
            if output_schema is not None:
                self._values["output_schema"] = output_schema

        @builtins.property
        def description(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html#cfn-bedrockagentcore-gatewaytarget-tooldefinition-description
            '''
            result = self._values.get("description")
            assert result is not None, "Required property 'description' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def input_schema(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.SchemaDefinitionProperty"]:
            '''The input schema for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html#cfn-bedrockagentcore-gatewaytarget-tooldefinition-inputschema
            '''
            result = self._values.get("input_schema")
            assert result is not None, "Required property 'input_schema' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.SchemaDefinitionProperty"], result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The tool name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html#cfn-bedrockagentcore-gatewaytarget-tooldefinition-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def output_schema(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.SchemaDefinitionProperty"]]:
            '''The tool definition output schema for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-tooldefinition.html#cfn-bedrockagentcore-gatewaytarget-tooldefinition-outputschema
            '''
            result = self._values.get("output_schema")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.SchemaDefinitionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ToolDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty",
        jsii_struct_bases=[],
        name_mapping={"inline_payload": "inlinePayload", "s3": "s3"},
    )
    class ToolSchemaProperty:
        def __init__(
            self,
            *,
            inline_payload: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.ToolDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            s3: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.S3ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The tool schema for the gateway target.

            :param inline_payload: The inline payload for the gateway target.
            :param s3: The S3 tool schema for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-toolschema.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
                
                tool_schema_property = bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                    inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                        description="description",
                        input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                            type="type",
                
                            # the properties below are optional
                            description="description",
                            items=schema_definition_property_,
                            properties={
                                "properties_key": schema_definition_property_
                            },
                            required=["required"]
                        ),
                        name="name",
                
                        # the properties below are optional
                        output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                            type="type",
                
                            # the properties below are optional
                            description="description",
                            items=schema_definition_property_,
                            properties={
                                "properties_key": schema_definition_property_
                            },
                            required=["required"]
                        )
                    )],
                    s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                        bucket_owner_account_id="bucketOwnerAccountId",
                        uri="uri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ff8fed96fdad56eb717513408b41cd94cf1c34461313bbb4de520c38aeab416)
                check_type(argname="argument inline_payload", value=inline_payload, expected_type=type_hints["inline_payload"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if inline_payload is not None:
                self._values["inline_payload"] = inline_payload
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def inline_payload(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ToolDefinitionProperty"]]]]:
            '''The inline payload for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-toolschema.html#cfn-bedrockagentcore-gatewaytarget-toolschema-inlinepayload
            '''
            result = self._values.get("inline_payload")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.ToolDefinitionProperty"]]]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.S3ConfigurationProperty"]]:
            '''The S3 tool schema for the gateway target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-gatewaytarget-toolschema.html#cfn-bedrockagentcore-gatewaytarget-toolschema-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.S3ConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ToolSchemaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnGatewayTargetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "target_configuration": "targetConfiguration",
        "credential_provider_configurations": "credentialProviderConfigurations",
        "description": "description",
        "gateway_identifier": "gatewayIdentifier",
        "metadata_configuration": "metadataConfiguration",
    },
)
class CfnGatewayTargetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        target_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.TargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        credential_provider_configurations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.CredentialProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        gateway_identifier: typing.Optional[builtins.str] = None,
        metadata_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGatewayTarget.MetadataConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGatewayTarget``.

        :param name: The name for the gateway target.
        :param target_configuration: The target configuration for the Smithy model target.
        :param credential_provider_configurations: The OAuth credential provider configuration.
        :param description: The description for the gateway target.
        :param gateway_identifier: The gateway ID for the gateway target.
        :param metadata_configuration: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            # schema_definition_property_: bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty
            
            cfn_gateway_target_props = bedrockagentcore.CfnGatewayTargetProps(
                name="name",
                target_configuration=bedrockagentcore.CfnGatewayTarget.TargetConfigurationProperty(
                    mcp=bedrockagentcore.CfnGatewayTarget.McpTargetConfigurationProperty(
                        api_gateway=bedrockagentcore.CfnGatewayTarget.ApiGatewayTargetConfigurationProperty(
                            api_gateway_tool_configuration=bedrockagentcore.CfnGatewayTarget.ApiGatewayToolConfigurationProperty(
                                tool_filters=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolFilterProperty(
                                    filter_path="filterPath",
                                    methods=["methods"]
                                )],
            
                                # the properties below are optional
                                tool_overrides=[bedrockagentcore.CfnGatewayTarget.ApiGatewayToolOverrideProperty(
                                    method="method",
                                    name="name",
                                    path="path",
            
                                    # the properties below are optional
                                    description="description"
                                )]
                            ),
                            rest_api_id="restApiId",
                            stage="stage"
                        ),
                        lambda_=bedrockagentcore.CfnGatewayTarget.McpLambdaTargetConfigurationProperty(
                            lambda_arn="lambdaArn",
                            tool_schema=bedrockagentcore.CfnGatewayTarget.ToolSchemaProperty(
                                inline_payload=[bedrockagentcore.CfnGatewayTarget.ToolDefinitionProperty(
                                    description="description",
                                    input_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                        type="type",
            
                                        # the properties below are optional
                                        description="description",
                                        items=schema_definition_property_,
                                        properties={
                                            "properties_key": schema_definition_property_
                                        },
                                        required=["required"]
                                    ),
                                    name="name",
            
                                    # the properties below are optional
                                    output_schema=bedrockagentcore.CfnGatewayTarget.SchemaDefinitionProperty(
                                        type="type",
            
                                        # the properties below are optional
                                        description="description",
                                        items=schema_definition_property_,
                                        properties={
                                            "properties_key": schema_definition_property_
                                        },
                                        required=["required"]
                                    )
                                )],
                                s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                    bucket_owner_account_id="bucketOwnerAccountId",
                                    uri="uri"
                                )
                            )
                        ),
                        mcp_server=bedrockagentcore.CfnGatewayTarget.McpServerTargetConfigurationProperty(
                            endpoint="endpoint"
                        ),
                        open_api_schema=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                            inline_payload="inlinePayload",
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        ),
                        smithy_model=bedrockagentcore.CfnGatewayTarget.ApiSchemaConfigurationProperty(
                            inline_payload="inlinePayload",
                            s3=bedrockagentcore.CfnGatewayTarget.S3ConfigurationProperty(
                                bucket_owner_account_id="bucketOwnerAccountId",
                                uri="uri"
                            )
                        )
                    )
                ),
            
                # the properties below are optional
                credential_provider_configurations=[bedrockagentcore.CfnGatewayTarget.CredentialProviderConfigurationProperty(
                    credential_provider_type="credentialProviderType",
            
                    # the properties below are optional
                    credential_provider=bedrockagentcore.CfnGatewayTarget.CredentialProviderProperty(
                        api_key_credential_provider=bedrockagentcore.CfnGatewayTarget.ApiKeyCredentialProviderProperty(
                            provider_arn="providerArn",
            
                            # the properties below are optional
                            credential_location="credentialLocation",
                            credential_parameter_name="credentialParameterName",
                            credential_prefix="credentialPrefix"
                        ),
                        oauth_credential_provider=bedrockagentcore.CfnGatewayTarget.OAuthCredentialProviderProperty(
                            provider_arn="providerArn",
                            scopes=["scopes"],
            
                            # the properties below are optional
                            custom_parameters={
                                "custom_parameters_key": "customParameters"
                            },
                            default_return_url="defaultReturnUrl",
                            grant_type="grantType"
                        )
                    )
                )],
                description="description",
                gateway_identifier="gatewayIdentifier",
                metadata_configuration=bedrockagentcore.CfnGatewayTarget.MetadataConfigurationProperty(
                    allowed_query_parameters=["allowedQueryParameters"],
                    allowed_request_headers=["allowedRequestHeaders"],
                    allowed_response_headers=["allowedResponseHeaders"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__367178269f9a78c89b5ba5e07b10a309050b4b3eaefd55c5ee6f30ddad20209f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target_configuration", value=target_configuration, expected_type=type_hints["target_configuration"])
            check_type(argname="argument credential_provider_configurations", value=credential_provider_configurations, expected_type=type_hints["credential_provider_configurations"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument gateway_identifier", value=gateway_identifier, expected_type=type_hints["gateway_identifier"])
            check_type(argname="argument metadata_configuration", value=metadata_configuration, expected_type=type_hints["metadata_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "target_configuration": target_configuration,
        }
        if credential_provider_configurations is not None:
            self._values["credential_provider_configurations"] = credential_provider_configurations
        if description is not None:
            self._values["description"] = description
        if gateway_identifier is not None:
            self._values["gateway_identifier"] = gateway_identifier
        if metadata_configuration is not None:
            self._values["metadata_configuration"] = metadata_configuration

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.TargetConfigurationProperty"]:
        '''The target configuration for the Smithy model target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-targetconfiguration
        '''
        result = self._values.get("target_configuration")
        assert result is not None, "Required property 'target_configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.TargetConfigurationProperty"], result)

    @builtins.property
    def credential_provider_configurations(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.CredentialProviderConfigurationProperty"]]]]:
        '''The OAuth credential provider configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-credentialproviderconfigurations
        '''
        result = self._values.get("credential_provider_configurations")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.CredentialProviderConfigurationProperty"]]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_identifier(self) -> typing.Optional[builtins.str]:
        '''The gateway ID for the gateway target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-gatewayidentifier
        '''
        result = self._values.get("gateway_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.MetadataConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-gatewaytarget.html#cfn-bedrockagentcore-gatewaytarget-metadataconfiguration
        '''
        result = self._values.get("metadata_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnGatewayTarget.MetadataConfigurationProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGatewayTargetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IMemoryRef_2d13cc89, _ITaggableV2_4e6798f8)
class CfnMemory(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory",
):
    '''Memory allows AI agents to maintain both immediate and long-term knowledge, enabling context-aware and personalized interactions.

    For more information about using Memory in Amazon Bedrock AgentCore, see `Host agent or tools with Amazon Bedrock AgentCore Memory <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-getting-started.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html
    :cloudformationResource: AWS::BedrockAgentCore::Memory
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_memory = bedrockagentcore.CfnMemory(self, "MyCfnMemory",
            event_expiry_duration=123,
            name="name",
        
            # the properties below are optional
            description="description",
            encryption_key_arn="encryptionKeyArn",
            memory_execution_role_arn="memoryExecutionRoleArn",
            memory_strategies=[bedrockagentcore.CfnMemory.MemoryStrategyProperty(
                custom_memory_strategy=bedrockagentcore.CfnMemory.CustomMemoryStrategyProperty(
                    name="name",
        
                    # the properties below are optional
                    configuration=bedrockagentcore.CfnMemory.CustomConfigurationInputProperty(
                        episodic_override=bedrockagentcore.CfnMemory.EpisodicOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            extraction=bedrockagentcore.CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            reflection=bedrockagentcore.CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId",
        
                                # the properties below are optional
                                namespaces=["namespaces"]
                            )
                        ),
                        self_managed_configuration=bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                            historical_context_window_size=123,
                            invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                                payload_delivery_bucket_name="payloadDeliveryBucketName",
                                topic_arn="topicArn"
                            ),
                            trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                                message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                                    message_count=123
                                ),
                                time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                                    idle_session_timeout=123
                                ),
                                token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                                    token_count=123
                                )
                            )]
                        ),
                        semantic_override=bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        ),
                        summary_override=bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        ),
                        user_preference_override=bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        )
                    ),
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                ),
                episodic_memory_strategy=bedrockagentcore.CfnMemory.EpisodicMemoryStrategyProperty(
                    name="name",
        
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    reflection_configuration=bedrockagentcore.CfnMemory.EpisodicReflectionConfigurationInputProperty(
                        namespaces=["namespaces"]
                    ),
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                ),
                semantic_memory_strategy=bedrockagentcore.CfnMemory.SemanticMemoryStrategyProperty(
                    name="name",
        
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                ),
                summary_memory_strategy=bedrockagentcore.CfnMemory.SummaryMemoryStrategyProperty(
                    name="name",
        
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                ),
                user_preference_memory_strategy=bedrockagentcore.CfnMemory.UserPreferenceMemoryStrategyProperty(
                    name="name",
        
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            )],
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        event_expiry_duration: jsii.Number,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        memory_execution_role_arn: typing.Optional[builtins.str] = None,
        memory_strategies: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.MemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::Memory``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param event_expiry_duration: The event expiry configuration.
        :param name: The memory name.
        :param description: Description of the Memory resource.
        :param encryption_key_arn: The memory encryption key Amazon Resource Name (ARN).
        :param memory_execution_role_arn: The memory role ARN.
        :param memory_strategies: The memory strategies.
        :param tags: The tags for the resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b95a7255db9df73ca225a32aecd624481667f18f3308ba77ce3fbf7d7e1cf4f0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMemoryProps(
            event_expiry_duration=event_expiry_duration,
            name=name,
            description=description,
            encryption_key_arn=encryption_key_arn,
            memory_execution_role_arn=memory_execution_role_arn,
            memory_strategies=memory_strategies,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForMemory")
    @builtins.classmethod
    def arn_for_memory(cls, resource: "_IMemoryRef_2d13cc89") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efd26aeb6a65d79b61f16a74d7d3f32c4d43bcea29520d215020f825921c572d)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForMemory", [resource]))

    @jsii.member(jsii_name="isCfnMemory")
    @builtins.classmethod
    def is_cfn_memory(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnMemory.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0daa51afcc3d4bc4c908dda067499db502f905d7a250174c02a9849a22623426)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnMemory", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b76cbb12d67c915a322289eef0caf05911a64361531f525f945065e6fbd1b0b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__29efd6b6b9a6ac1e7281cd85ae63e9d6002789f18830f68a7cec0a0d012ac382)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the memory record was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''
        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrMemoryArn")
    def attr_memory_arn(self) -> builtins.str:
        '''ARN of the Memory resource.

        :cloudformationAttribute: MemoryArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMemoryArn"))

    @builtins.property
    @jsii.member(jsii_name="attrMemoryId")
    def attr_memory_id(self) -> builtins.str:
        '''The memory ID.

        :cloudformationAttribute: MemoryId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMemoryId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The memory status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="memoryRef")
    def memory_ref(self) -> "_MemoryReference_a1aef278":
        '''A reference to a Memory resource.'''
        return typing.cast("_MemoryReference_a1aef278", jsii.get(self, "memoryRef"))

    @builtins.property
    @jsii.member(jsii_name="eventExpiryDuration")
    def event_expiry_duration(self) -> jsii.Number:
        '''The event expiry configuration.'''
        return typing.cast(jsii.Number, jsii.get(self, "eventExpiryDuration"))

    @event_expiry_duration.setter
    def event_expiry_duration(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c376bc3bd26c18cf626509568f040ac75ef52a68ef8a39ca3e5b6b8308374496)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventExpiryDuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The memory name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f948061bc9aba0eb248f047c217bd96c19cf47d09da3c7b9708380caf387394f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the Memory resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93e29c7f80206ddbc4de97f028b669d82daf8dd5c65b29ae535035b57cd461ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyArn")
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The memory encryption key Amazon Resource Name (ARN).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyArn"))

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b682a270f87cf6f76b16e70568b3e20c1994f4ff375efed9e59f3ff29cce80cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memoryExecutionRoleArn")
    def memory_execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The memory role ARN.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "memoryExecutionRoleArn"))

    @memory_execution_role_arn.setter
    def memory_execution_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bd6b17fbf9c4464799eba94f4be79124e7c5491b62da83c1a8bd39d6f2a0def)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryExecutionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="memoryStrategies")
    def memory_strategies(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnMemory.MemoryStrategyProperty"]]]]:
        '''The memory strategies.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnMemory.MemoryStrategyProperty"]]]], jsii.get(self, "memoryStrategies"))

    @memory_strategies.setter
    def memory_strategies(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnMemory.MemoryStrategyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b18515e6738d6694af7855ee5a84c8940fcfa482c5e51f03ea9e0abda4a56765)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memoryStrategies", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the resources.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20937c3b9ee32cb1df4d7eaf09c5da2b921076b8dab073c8f61380cb9b64e33b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.CustomConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "episodic_override": "episodicOverride",
            "self_managed_configuration": "selfManagedConfiguration",
            "semantic_override": "semanticOverride",
            "summary_override": "summaryOverride",
            "user_preference_override": "userPreferenceOverride",
        },
    )
    class CustomConfigurationInputProperty:
        def __init__(
            self,
            *,
            episodic_override: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.EpisodicOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            self_managed_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.SelfManagedConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            semantic_override: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.SemanticOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            summary_override: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.SummaryOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user_preference_override: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.UserPreferenceOverrideProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory configuration input.

            :param episodic_override: 
            :param self_managed_configuration: The custom configuration input.
            :param semantic_override: The memory override configuration.
            :param summary_override: The memory configuration override.
            :param user_preference_override: The memory user preference override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_configuration_input_property = bedrockagentcore.CfnMemory.CustomConfigurationInputProperty(
                    episodic_override=bedrockagentcore.CfnMemory.EpisodicOverrideProperty(
                        consolidation=bedrockagentcore.CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        ),
                        extraction=bedrockagentcore.CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        ),
                        reflection=bedrockagentcore.CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId",
                
                            # the properties below are optional
                            namespaces=["namespaces"]
                        )
                    ),
                    self_managed_configuration=bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                        historical_context_window_size=123,
                        invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                            payload_delivery_bucket_name="payloadDeliveryBucketName",
                            topic_arn="topicArn"
                        ),
                        trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                            message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                                message_count=123
                            ),
                            time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                                idle_session_timeout=123
                            ),
                            token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                                token_count=123
                            )
                        )]
                    ),
                    semantic_override=bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                        consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        ),
                        extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        )
                    ),
                    summary_override=bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                        consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        )
                    ),
                    user_preference_override=bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                        consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        ),
                        extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                            append_to_prompt="appendToPrompt",
                            model_id="modelId"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__80b393ad440afaf6b639d0ad3fdd1431e23bc8fa4658d92c51bbe3ae892ec72e)
                check_type(argname="argument episodic_override", value=episodic_override, expected_type=type_hints["episodic_override"])
                check_type(argname="argument self_managed_configuration", value=self_managed_configuration, expected_type=type_hints["self_managed_configuration"])
                check_type(argname="argument semantic_override", value=semantic_override, expected_type=type_hints["semantic_override"])
                check_type(argname="argument summary_override", value=summary_override, expected_type=type_hints["summary_override"])
                check_type(argname="argument user_preference_override", value=user_preference_override, expected_type=type_hints["user_preference_override"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if episodic_override is not None:
                self._values["episodic_override"] = episodic_override
            if self_managed_configuration is not None:
                self._values["self_managed_configuration"] = self_managed_configuration
            if semantic_override is not None:
                self._values["semantic_override"] = semantic_override
            if summary_override is not None:
                self._values["summary_override"] = summary_override
            if user_preference_override is not None:
                self._values["user_preference_override"] = user_preference_override

        @builtins.property
        def episodic_override(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicOverrideProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html#cfn-bedrockagentcore-memory-customconfigurationinput-episodicoverride
            '''
            result = self._values.get("episodic_override")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicOverrideProperty"]], result)

        @builtins.property
        def self_managed_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SelfManagedConfigurationProperty"]]:
            '''The custom configuration input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html#cfn-bedrockagentcore-memory-customconfigurationinput-selfmanagedconfiguration
            '''
            result = self._values.get("self_managed_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SelfManagedConfigurationProperty"]], result)

        @builtins.property
        def semantic_override(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SemanticOverrideProperty"]]:
            '''The memory override configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html#cfn-bedrockagentcore-memory-customconfigurationinput-semanticoverride
            '''
            result = self._values.get("semantic_override")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SemanticOverrideProperty"]], result)

        @builtins.property
        def summary_override(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SummaryOverrideProperty"]]:
            '''The memory configuration override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html#cfn-bedrockagentcore-memory-customconfigurationinput-summaryoverride
            '''
            result = self._values.get("summary_override")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SummaryOverrideProperty"]], result)

        @builtins.property
        def user_preference_override(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.UserPreferenceOverrideProperty"]]:
            '''The memory user preference override.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-customconfigurationinput.html#cfn-bedrockagentcore-memory-customconfigurationinput-userpreferenceoverride
            '''
            result = self._values.get("user_preference_override")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.UserPreferenceOverrideProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.CustomMemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "configuration": "configuration",
            "created_at": "createdAt",
            "description": "description",
            "namespaces": "namespaces",
            "status": "status",
            "strategy_id": "strategyId",
            "type": "type",
            "updated_at": "updatedAt",
        },
    )
    class CustomMemoryStrategyProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.CustomConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            created_at: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            status: typing.Optional[builtins.str] = None,
            strategy_id: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The memory strategy.

            :param name: The memory strategy name.
            :param configuration: The memory strategy configuration.
            :param created_at: Creation timestamp of the memory strategy.
            :param description: The memory strategy description.
            :param namespaces: The memory strategy namespaces.
            :param status: The memory strategy status.
            :param strategy_id: The memory strategy ID.
            :param type: The memory strategy type.
            :param updated_at: The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_memory_strategy_property = bedrockagentcore.CfnMemory.CustomMemoryStrategyProperty(
                    name="name",
                
                    # the properties below are optional
                    configuration=bedrockagentcore.CfnMemory.CustomConfigurationInputProperty(
                        episodic_override=bedrockagentcore.CfnMemory.EpisodicOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            extraction=bedrockagentcore.CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            reflection=bedrockagentcore.CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId",
                
                                # the properties below are optional
                                namespaces=["namespaces"]
                            )
                        ),
                        self_managed_configuration=bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                            historical_context_window_size=123,
                            invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                                payload_delivery_bucket_name="payloadDeliveryBucketName",
                                topic_arn="topicArn"
                            ),
                            trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                                message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                                    message_count=123
                                ),
                                time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                                    idle_session_timeout=123
                                ),
                                token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                                    token_count=123
                                )
                            )]
                        ),
                        semantic_override=bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        ),
                        summary_override=bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        ),
                        user_preference_override=bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                            consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            ),
                            extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                                append_to_prompt="appendToPrompt",
                                model_id="modelId"
                            )
                        )
                    ),
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68f9ef2809f813258bef3dcd9ec460d2f237f2127d9f7cb9aae3256166ba8183)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument strategy_id", value=strategy_id, expected_type=type_hints["strategy_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if configuration is not None:
                self._values["configuration"] = configuration
            if created_at is not None:
                self._values["created_at"] = created_at
            if description is not None:
                self._values["description"] = description
            if namespaces is not None:
                self._values["namespaces"] = namespaces
            if status is not None:
                self._values["status"] = status
            if strategy_id is not None:
                self._values["strategy_id"] = strategy_id
            if type is not None:
                self._values["type"] = type
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def name(self) -> builtins.str:
            '''The memory strategy name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.CustomConfigurationInputProperty"]]:
            '''The memory strategy configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-configuration
            '''
            result = self._values.get("configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.CustomConfigurationInputProperty"]], result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''Creation timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The memory strategy description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The memory strategy namespaces.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-namespaces
            '''
            result = self._values.get("namespaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The memory strategy status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strategy_id(self) -> typing.Optional[builtins.str]:
            '''The memory strategy ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-strategyid
            '''
            result = self._values.get("strategy_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The memory strategy type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-custommemorystrategy.html#cfn-bedrockagentcore-memory-custommemorystrategy-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomMemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.EpisodicMemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "created_at": "createdAt",
            "description": "description",
            "namespaces": "namespaces",
            "reflection_configuration": "reflectionConfiguration",
            "status": "status",
            "strategy_id": "strategyId",
            "type": "type",
            "updated_at": "updatedAt",
        },
    )
    class EpisodicMemoryStrategyProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            created_at: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            reflection_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.EpisodicReflectionConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            status: typing.Optional[builtins.str] = None,
            strategy_id: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param name: Name of the Memory resource.
            :param created_at: Creation timestamp of the memory strategy.
            :param description: Description of the Memory resource.
            :param namespaces: List of namespaces for memory strategy.
            :param reflection_configuration: 
            :param status: Status of the memory strategy.
            :param strategy_id: Unique identifier for the memory strategy.
            :param type: Type of memory strategy.
            :param updated_at: Last update timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicmemorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                episodic_memory_strategy_property = bedrockagentcore.CfnMemory.EpisodicMemoryStrategyProperty(
                    name="name",
                
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    reflection_configuration=bedrockagentcore.CfnMemory.EpisodicReflectionConfigurationInputProperty(
                        namespaces=["namespaces"]
                    ),
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4010f11a9f956fe10befa570e47005124fa04732849c4143a5219ad033db3bff)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
                check_type(argname="argument reflection_configuration", value=reflection_configuration, expected_type=type_hints["reflection_configuration"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument strategy_id", value=strategy_id, expected_type=type_hints["strategy_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if created_at is not None:
                self._values["created_at"] = created_at
            if description is not None:
                self._values["description"] = description
            if namespaces is not None:
                self._values["namespaces"] = namespaces
            if reflection_configuration is not None:
                self._values["reflection_configuration"] = reflection_configuration
            if status is not None:
                self._values["status"] = status
            if strategy_id is not None:
                self._values["strategy_id"] = strategy_id
            if type is not None:
                self._values["type"] = type
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def name(self) -> builtins.str:
            '''Name of the Memory resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicmemorystrategy.html#cfn-bedrockagentcore-memory-episodicmemorystrategy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''Creation timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicmemorystrategy.html#cfn-bedrockagentcore-memory-episodicmemorystrategy-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''Description of the Memory resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicmemorystrategy.html#cfn-bedrockagentcore-memory-episodicmemorystrategy-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of namespaces for memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicmemorystrategy.html#cfn-bedrockagentcore-memory-episodicmemorystrategy-namespaces
            '''
            result = self._values.get("namespaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def reflection_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicReflectionConfigurationInputProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicmemorystrategy.html#cfn-bedrockagentcore-memory-episodicmemorystrategy-reflectionconfiguration
            '''
            result = self._values.get("reflection_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicReflectionConfigurationInputProperty"]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Status of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicmemorystrategy.html#cfn-bedrockagentcore-memory-episodicmemorystrategy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strategy_id(self) -> typing.Optional[builtins.str]:
            '''Unique identifier for the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicmemorystrategy.html#cfn-bedrockagentcore-memory-episodicmemorystrategy-strategyid
            '''
            result = self._values.get("strategy_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''Type of memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicmemorystrategy.html#cfn-bedrockagentcore-memory-episodicmemorystrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''Last update timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicmemorystrategy.html#cfn-bedrockagentcore-memory-episodicmemorystrategy-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EpisodicMemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class EpisodicOverrideConsolidationConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''
            :param append_to_prompt: Text prompt for model instructions.
            :param model_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverrideconsolidationconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                episodic_override_consolidation_configuration_input_property = bedrockagentcore.CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9aa1a71d684023e3bf516c1377383806779b05133a8783b948bbcea97001dbd1)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''Text prompt for model instructions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-episodicoverrideconsolidationconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-episodicoverrideconsolidationconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EpisodicOverrideConsolidationConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class EpisodicOverrideExtractionConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''
            :param append_to_prompt: Text prompt for model instructions.
            :param model_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverrideextractionconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                episodic_override_extraction_configuration_input_property = bedrockagentcore.CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57f6e2b335649583bd753b07454a443607a3c1a4b900aeb0d79184b7f9fea550)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''Text prompt for model instructions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverrideextractionconfigurationinput.html#cfn-bedrockagentcore-memory-episodicoverrideextractionconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverrideextractionconfigurationinput.html#cfn-bedrockagentcore-memory-episodicoverrideextractionconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EpisodicOverrideExtractionConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.EpisodicOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={
            "consolidation": "consolidation",
            "extraction": "extraction",
            "reflection": "reflection",
        },
    )
    class EpisodicOverrideProperty:
        def __init__(
            self,
            *,
            consolidation: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            extraction: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            reflection: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param consolidation: 
            :param extraction: 
            :param reflection: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                episodic_override_property = bedrockagentcore.CfnMemory.EpisodicOverrideProperty(
                    consolidation=bedrockagentcore.CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    ),
                    extraction=bedrockagentcore.CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    ),
                    reflection=bedrockagentcore.CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId",
                
                        # the properties below are optional
                        namespaces=["namespaces"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b710e8660112018a6354eb5ae8c4e7aa27f0cd362be38426220fd00b83c09a8)
                check_type(argname="argument consolidation", value=consolidation, expected_type=type_hints["consolidation"])
                check_type(argname="argument extraction", value=extraction, expected_type=type_hints["extraction"])
                check_type(argname="argument reflection", value=reflection, expected_type=type_hints["reflection"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if consolidation is not None:
                self._values["consolidation"] = consolidation
            if extraction is not None:
                self._values["extraction"] = extraction
            if reflection is not None:
                self._values["reflection"] = reflection

        @builtins.property
        def consolidation(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverride.html#cfn-bedrockagentcore-memory-episodicoverride-consolidation
            '''
            result = self._values.get("consolidation")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty"]], result)

        @builtins.property
        def extraction(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverride.html#cfn-bedrockagentcore-memory-episodicoverride-extraction
            '''
            result = self._values.get("extraction")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty"]], result)

        @builtins.property
        def reflection(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverride.html#cfn-bedrockagentcore-memory-episodicoverride-reflection
            '''
            result = self._values.get("reflection")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EpisodicOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "append_to_prompt": "appendToPrompt",
            "model_id": "modelId",
            "namespaces": "namespaces",
        },
    )
    class EpisodicOverrideReflectionConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
            namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param append_to_prompt: Text prompt for model instructions.
            :param model_id: 
            :param namespaces: List of namespaces for memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverridereflectionconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                episodic_override_reflection_configuration_input_property = bedrockagentcore.CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId",
                
                    # the properties below are optional
                    namespaces=["namespaces"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__df10fcf9a92c0373c158e2aa4763d8107995e1f7b4403a8c8001a6afe3424ad4)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }
            if namespaces is not None:
                self._values["namespaces"] = namespaces

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''Text prompt for model instructions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverridereflectionconfigurationinput.html#cfn-bedrockagentcore-memory-episodicoverridereflectionconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverridereflectionconfigurationinput.html#cfn-bedrockagentcore-memory-episodicoverridereflectionconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of namespaces for memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicoverridereflectionconfigurationinput.html#cfn-bedrockagentcore-memory-episodicoverridereflectionconfigurationinput-namespaces
            '''
            result = self._values.get("namespaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EpisodicOverrideReflectionConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.EpisodicReflectionConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"namespaces": "namespaces"},
    )
    class EpisodicReflectionConfigurationInputProperty:
        def __init__(self, *, namespaces: typing.Sequence[builtins.str]) -> None:
            '''
            :param namespaces: List of namespaces for memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicreflectionconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                episodic_reflection_configuration_input_property = bedrockagentcore.CfnMemory.EpisodicReflectionConfigurationInputProperty(
                    namespaces=["namespaces"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d10801b6b457e9912061807464c00e48d36901349246d4c00671ab17eaee367)
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "namespaces": namespaces,
            }

        @builtins.property
        def namespaces(self) -> typing.List[builtins.str]:
            '''List of namespaces for memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-episodicreflectionconfigurationinput.html#cfn-bedrockagentcore-memory-episodicreflectionconfigurationinput-namespaces
            '''
            result = self._values.get("namespaces")
            assert result is not None, "Required property 'namespaces' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EpisodicReflectionConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "payload_delivery_bucket_name": "payloadDeliveryBucketName",
            "topic_arn": "topicArn",
        },
    )
    class InvocationConfigurationInputProperty:
        def __init__(
            self,
            *,
            payload_delivery_bucket_name: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The memory invocation configuration input.

            :param payload_delivery_bucket_name: The message invocation configuration information for the bucket name.
            :param topic_arn: The memory trigger condition topic Amazon Resource Name (ARN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-invocationconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                invocation_configuration_input_property = bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                    payload_delivery_bucket_name="payloadDeliveryBucketName",
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__44e7fa751a69795001dc84cc0fd23b36ae6952ce8c475d549b7599b3353a7c9a)
                check_type(argname="argument payload_delivery_bucket_name", value=payload_delivery_bucket_name, expected_type=type_hints["payload_delivery_bucket_name"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if payload_delivery_bucket_name is not None:
                self._values["payload_delivery_bucket_name"] = payload_delivery_bucket_name
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def payload_delivery_bucket_name(self) -> typing.Optional[builtins.str]:
            '''The message invocation configuration information for the bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-invocationconfigurationinput.html#cfn-bedrockagentcore-memory-invocationconfigurationinput-payloaddeliverybucketname
            '''
            result = self._values.get("payload_delivery_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The memory trigger condition topic Amazon Resource Name (ARN).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-invocationconfigurationinput.html#cfn-bedrockagentcore-memory-invocationconfigurationinput-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InvocationConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.MemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_memory_strategy": "customMemoryStrategy",
            "episodic_memory_strategy": "episodicMemoryStrategy",
            "semantic_memory_strategy": "semanticMemoryStrategy",
            "summary_memory_strategy": "summaryMemoryStrategy",
            "user_preference_memory_strategy": "userPreferenceMemoryStrategy",
        },
    )
    class MemoryStrategyProperty:
        def __init__(
            self,
            *,
            custom_memory_strategy: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.CustomMemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            episodic_memory_strategy: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.EpisodicMemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            semantic_memory_strategy: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.SemanticMemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            summary_memory_strategy: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.SummaryMemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            user_preference_memory_strategy: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.UserPreferenceMemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory strategy.

            :param custom_memory_strategy: The memory strategy.
            :param episodic_memory_strategy: 
            :param semantic_memory_strategy: The memory strategy.
            :param summary_memory_strategy: The memory strategy summary.
            :param user_preference_memory_strategy: The memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                memory_strategy_property = bedrockagentcore.CfnMemory.MemoryStrategyProperty(
                    custom_memory_strategy=bedrockagentcore.CfnMemory.CustomMemoryStrategyProperty(
                        name="name",
                
                        # the properties below are optional
                        configuration=bedrockagentcore.CfnMemory.CustomConfigurationInputProperty(
                            episodic_override=bedrockagentcore.CfnMemory.EpisodicOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                extraction=bedrockagentcore.CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                reflection=bedrockagentcore.CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId",
                
                                    # the properties below are optional
                                    namespaces=["namespaces"]
                                )
                            ),
                            self_managed_configuration=bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                                historical_context_window_size=123,
                                invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                                    payload_delivery_bucket_name="payloadDeliveryBucketName",
                                    topic_arn="topicArn"
                                ),
                                trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                                    message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                                        message_count=123
                                    ),
                                    time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                                        idle_session_timeout=123
                                    ),
                                    token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                                        token_count=123
                                    )
                                )]
                            ),
                            semantic_override=bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            ),
                            summary_override=bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            ),
                            user_preference_override=bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            )
                        ),
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    episodic_memory_strategy=bedrockagentcore.CfnMemory.EpisodicMemoryStrategyProperty(
                        name="name",
                
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        reflection_configuration=bedrockagentcore.CfnMemory.EpisodicReflectionConfigurationInputProperty(
                            namespaces=["namespaces"]
                        ),
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    semantic_memory_strategy=bedrockagentcore.CfnMemory.SemanticMemoryStrategyProperty(
                        name="name",
                
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    summary_memory_strategy=bedrockagentcore.CfnMemory.SummaryMemoryStrategyProperty(
                        name="name",
                
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    user_preference_memory_strategy=bedrockagentcore.CfnMemory.UserPreferenceMemoryStrategyProperty(
                        name="name",
                
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7fa25b2413ebaf6794a4e0d96d4404f578a37b86cd501369f7c93f8d049e8e7)
                check_type(argname="argument custom_memory_strategy", value=custom_memory_strategy, expected_type=type_hints["custom_memory_strategy"])
                check_type(argname="argument episodic_memory_strategy", value=episodic_memory_strategy, expected_type=type_hints["episodic_memory_strategy"])
                check_type(argname="argument semantic_memory_strategy", value=semantic_memory_strategy, expected_type=type_hints["semantic_memory_strategy"])
                check_type(argname="argument summary_memory_strategy", value=summary_memory_strategy, expected_type=type_hints["summary_memory_strategy"])
                check_type(argname="argument user_preference_memory_strategy", value=user_preference_memory_strategy, expected_type=type_hints["user_preference_memory_strategy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_memory_strategy is not None:
                self._values["custom_memory_strategy"] = custom_memory_strategy
            if episodic_memory_strategy is not None:
                self._values["episodic_memory_strategy"] = episodic_memory_strategy
            if semantic_memory_strategy is not None:
                self._values["semantic_memory_strategy"] = semantic_memory_strategy
            if summary_memory_strategy is not None:
                self._values["summary_memory_strategy"] = summary_memory_strategy
            if user_preference_memory_strategy is not None:
                self._values["user_preference_memory_strategy"] = user_preference_memory_strategy

        @builtins.property
        def custom_memory_strategy(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.CustomMemoryStrategyProperty"]]:
            '''The memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html#cfn-bedrockagentcore-memory-memorystrategy-custommemorystrategy
            '''
            result = self._values.get("custom_memory_strategy")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.CustomMemoryStrategyProperty"]], result)

        @builtins.property
        def episodic_memory_strategy(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicMemoryStrategyProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html#cfn-bedrockagentcore-memory-memorystrategy-episodicmemorystrategy
            '''
            result = self._values.get("episodic_memory_strategy")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.EpisodicMemoryStrategyProperty"]], result)

        @builtins.property
        def semantic_memory_strategy(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SemanticMemoryStrategyProperty"]]:
            '''The memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html#cfn-bedrockagentcore-memory-memorystrategy-semanticmemorystrategy
            '''
            result = self._values.get("semantic_memory_strategy")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SemanticMemoryStrategyProperty"]], result)

        @builtins.property
        def summary_memory_strategy(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SummaryMemoryStrategyProperty"]]:
            '''The memory strategy summary.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html#cfn-bedrockagentcore-memory-memorystrategy-summarymemorystrategy
            '''
            result = self._values.get("summary_memory_strategy")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SummaryMemoryStrategyProperty"]], result)

        @builtins.property
        def user_preference_memory_strategy(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.UserPreferenceMemoryStrategyProperty"]]:
            '''The memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-memorystrategy.html#cfn-bedrockagentcore-memory-memorystrategy-userpreferencememorystrategy
            '''
            result = self._values.get("user_preference_memory_strategy")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.UserPreferenceMemoryStrategyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty",
        jsii_struct_bases=[],
        name_mapping={"message_count": "messageCount"},
    )
    class MessageBasedTriggerInputProperty:
        def __init__(
            self,
            *,
            message_count: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The message based trigger input.

            :param message_count: The memory trigger condition input for the message based trigger message count.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-messagebasedtriggerinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                message_based_trigger_input_property = bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                    message_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f26f0bfb6bb91a96529926b34610d43ded0571d826aa8ac6cb6e63367e9ea089)
                check_type(argname="argument message_count", value=message_count, expected_type=type_hints["message_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if message_count is not None:
                self._values["message_count"] = message_count

        @builtins.property
        def message_count(self) -> typing.Optional[jsii.Number]:
            '''The memory trigger condition input for the message based trigger message count.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-messagebasedtriggerinput.html#cfn-bedrockagentcore-memory-messagebasedtriggerinput-messagecount
            '''
            result = self._values.get("message_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MessageBasedTriggerInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "historical_context_window_size": "historicalContextWindowSize",
            "invocation_configuration": "invocationConfiguration",
            "trigger_conditions": "triggerConditions",
        },
    )
    class SelfManagedConfigurationProperty:
        def __init__(
            self,
            *,
            historical_context_window_size: typing.Optional[jsii.Number] = None,
            invocation_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.InvocationConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            trigger_conditions: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.TriggerConditionInputProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The self managed configuration.

            :param historical_context_window_size: The memory configuration for self managed.
            :param invocation_configuration: The self managed configuration.
            :param trigger_conditions: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-selfmanagedconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                self_managed_configuration_property = bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                    historical_context_window_size=123,
                    invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                        payload_delivery_bucket_name="payloadDeliveryBucketName",
                        topic_arn="topicArn"
                    ),
                    trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                        message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                            message_count=123
                        ),
                        time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                            idle_session_timeout=123
                        ),
                        token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                            token_count=123
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e4fcd7b9f7c5c0bb0c80ff54635936b78ada2b3d24596ba7cd43b9ece93f804c)
                check_type(argname="argument historical_context_window_size", value=historical_context_window_size, expected_type=type_hints["historical_context_window_size"])
                check_type(argname="argument invocation_configuration", value=invocation_configuration, expected_type=type_hints["invocation_configuration"])
                check_type(argname="argument trigger_conditions", value=trigger_conditions, expected_type=type_hints["trigger_conditions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if historical_context_window_size is not None:
                self._values["historical_context_window_size"] = historical_context_window_size
            if invocation_configuration is not None:
                self._values["invocation_configuration"] = invocation_configuration
            if trigger_conditions is not None:
                self._values["trigger_conditions"] = trigger_conditions

        @builtins.property
        def historical_context_window_size(self) -> typing.Optional[jsii.Number]:
            '''The memory configuration for self managed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-selfmanagedconfiguration.html#cfn-bedrockagentcore-memory-selfmanagedconfiguration-historicalcontextwindowsize
            '''
            result = self._values.get("historical_context_window_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def invocation_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.InvocationConfigurationInputProperty"]]:
            '''The self managed configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-selfmanagedconfiguration.html#cfn-bedrockagentcore-memory-selfmanagedconfiguration-invocationconfiguration
            '''
            result = self._values.get("invocation_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.InvocationConfigurationInputProperty"]], result)

        @builtins.property
        def trigger_conditions(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnMemory.TriggerConditionInputProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-selfmanagedconfiguration.html#cfn-bedrockagentcore-memory-selfmanagedconfiguration-triggerconditions
            '''
            result = self._values.get("trigger_conditions")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnMemory.TriggerConditionInputProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SelfManagedConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SemanticMemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "created_at": "createdAt",
            "description": "description",
            "namespaces": "namespaces",
            "status": "status",
            "strategy_id": "strategyId",
            "type": "type",
            "updated_at": "updatedAt",
        },
    )
    class SemanticMemoryStrategyProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            created_at: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            status: typing.Optional[builtins.str] = None,
            strategy_id: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The memory strategy.

            :param name: The memory strategy name.
            :param created_at: Creation timestamp of the memory strategy.
            :param description: The memory strategy description.
            :param namespaces: The memory strategy namespaces.
            :param status: Status of the memory strategy.
            :param strategy_id: The memory strategy ID.
            :param type: The memory strategy type.
            :param updated_at: Last update timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                semantic_memory_strategy_property = bedrockagentcore.CfnMemory.SemanticMemoryStrategyProperty(
                    name="name",
                
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fdd1426fa7487dcb02499d9f810acd963031578a3c30fd4be0b076b09a32b124)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument strategy_id", value=strategy_id, expected_type=type_hints["strategy_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if created_at is not None:
                self._values["created_at"] = created_at
            if description is not None:
                self._values["description"] = description
            if namespaces is not None:
                self._values["namespaces"] = namespaces
            if status is not None:
                self._values["status"] = status
            if strategy_id is not None:
                self._values["strategy_id"] = strategy_id
            if type is not None:
                self._values["type"] = type
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def name(self) -> builtins.str:
            '''The memory strategy name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''Creation timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The memory strategy description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The memory strategy namespaces.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-namespaces
            '''
            result = self._values.get("namespaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Status of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strategy_id(self) -> typing.Optional[builtins.str]:
            '''The memory strategy ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-strategyid
            '''
            result = self._values.get("strategy_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The memory strategy type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''Last update timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticmemorystrategy.html#cfn-bedrockagentcore-memory-semanticmemorystrategy-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SemanticMemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class SemanticOverrideConsolidationConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''The memory override configuration.

            :param append_to_prompt: The override configuration.
            :param model_id: The memory override model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                semantic_override_consolidation_configuration_input_property = bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__393b5baf9d5b39c6498ec7dde998e56d10f272578b90e6901d6e5717c4d0b79d)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''The override configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The memory override model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-semanticoverrideconsolidationconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SemanticOverrideConsolidationConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class SemanticOverrideExtractionConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''The memory override configuration.

            :param append_to_prompt: The extraction configuration.
            :param model_id: The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                semantic_override_extraction_configuration_input_property = bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__669cd3ffc171b2cd7f3a4c3d6196e5a075449bedd07119892324a275601cf283)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''The extraction configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput.html#cfn-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput.html#cfn-bedrockagentcore-memory-semanticoverrideextractionconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SemanticOverrideExtractionConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SemanticOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"consolidation": "consolidation", "extraction": "extraction"},
    )
    class SemanticOverrideProperty:
        def __init__(
            self,
            *,
            consolidation: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            extraction: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.SemanticOverrideExtractionConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory override.

            :param consolidation: The memory override consolidation.
            :param extraction: The memory override extraction.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                semantic_override_property = bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                    consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    ),
                    extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c4fcd9046e68a8e9401f48408f0a4870f5c13f714c342e2085d178557990c4ee)
                check_type(argname="argument consolidation", value=consolidation, expected_type=type_hints["consolidation"])
                check_type(argname="argument extraction", value=extraction, expected_type=type_hints["extraction"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if consolidation is not None:
                self._values["consolidation"] = consolidation
            if extraction is not None:
                self._values["extraction"] = extraction

        @builtins.property
        def consolidation(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty"]]:
            '''The memory override consolidation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverride.html#cfn-bedrockagentcore-memory-semanticoverride-consolidation
            '''
            result = self._values.get("consolidation")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty"]], result)

        @builtins.property
        def extraction(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SemanticOverrideExtractionConfigurationInputProperty"]]:
            '''The memory override extraction.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-semanticoverride.html#cfn-bedrockagentcore-memory-semanticoverride-extraction
            '''
            result = self._values.get("extraction")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SemanticOverrideExtractionConfigurationInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SemanticOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SummaryMemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "created_at": "createdAt",
            "description": "description",
            "namespaces": "namespaces",
            "status": "status",
            "strategy_id": "strategyId",
            "type": "type",
            "updated_at": "updatedAt",
        },
    )
    class SummaryMemoryStrategyProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            created_at: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            status: typing.Optional[builtins.str] = None,
            strategy_id: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The memory strategy.

            :param name: The memory strategy name.
            :param created_at: Creation timestamp of the memory strategy.
            :param description: The memory strategy description.
            :param namespaces: The summary memory strategy.
            :param status: The memory strategy status.
            :param strategy_id: The memory strategy ID.
            :param type: The memory strategy type.
            :param updated_at: The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                summary_memory_strategy_property = bedrockagentcore.CfnMemory.SummaryMemoryStrategyProperty(
                    name="name",
                
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eee517e4354bf11f650f3de6c9e3789b5ced3c958c97582b32deda0a2643b376)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument strategy_id", value=strategy_id, expected_type=type_hints["strategy_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if created_at is not None:
                self._values["created_at"] = created_at
            if description is not None:
                self._values["description"] = description
            if namespaces is not None:
                self._values["namespaces"] = namespaces
            if status is not None:
                self._values["status"] = status
            if strategy_id is not None:
                self._values["strategy_id"] = strategy_id
            if type is not None:
                self._values["type"] = type
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def name(self) -> builtins.str:
            '''The memory strategy name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''Creation timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The memory strategy description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The summary memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-namespaces
            '''
            result = self._values.get("namespaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The memory strategy status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strategy_id(self) -> typing.Optional[builtins.str]:
            '''The memory strategy ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-strategyid
            '''
            result = self._values.get("strategy_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The memory strategy type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summarymemorystrategy.html#cfn-bedrockagentcore-memory-summarymemorystrategy-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SummaryMemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class SummaryOverrideConsolidationConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''The consolidation configuration.

            :param append_to_prompt: The memory override configuration.
            :param model_id: The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                summary_override_consolidation_configuration_input_property = bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c990b6378d188092fe95d78caab0eb586836dc0ca2194f9cbf3788c24c6ec053)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''The memory override configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-summaryoverrideconsolidationconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SummaryOverrideConsolidationConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.SummaryOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"consolidation": "consolidation"},
    )
    class SummaryOverrideProperty:
        def __init__(
            self,
            *,
            consolidation: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory summary override.

            :param consolidation: The memory override consolidation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summaryoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                summary_override_property = bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                    consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b23ed198bcd958ec3a014c4dd2d6c418b82bc1895ca1b0af24503f002e61d492)
                check_type(argname="argument consolidation", value=consolidation, expected_type=type_hints["consolidation"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if consolidation is not None:
                self._values["consolidation"] = consolidation

        @builtins.property
        def consolidation(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty"]]:
            '''The memory override consolidation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-summaryoverride.html#cfn-bedrockagentcore-memory-summaryoverride-consolidation
            '''
            result = self._values.get("consolidation")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SummaryOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty",
        jsii_struct_bases=[],
        name_mapping={"idle_session_timeout": "idleSessionTimeout"},
    )
    class TimeBasedTriggerInputProperty:
        def __init__(
            self,
            *,
            idle_session_timeout: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The memory trigger condition input for the time based trigger.

            :param idle_session_timeout: The memory trigger condition input for the session timeout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-timebasedtriggerinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                time_based_trigger_input_property = bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                    idle_session_timeout=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0cf65bf0b7de7a122f8fdf3c50a61ba88dd5248ad841dd004cb6bd0f7174ec45)
                check_type(argname="argument idle_session_timeout", value=idle_session_timeout, expected_type=type_hints["idle_session_timeout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if idle_session_timeout is not None:
                self._values["idle_session_timeout"] = idle_session_timeout

        @builtins.property
        def idle_session_timeout(self) -> typing.Optional[jsii.Number]:
            '''The memory trigger condition input for the session timeout.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-timebasedtriggerinput.html#cfn-bedrockagentcore-memory-timebasedtriggerinput-idlesessiontimeout
            '''
            result = self._values.get("idle_session_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeBasedTriggerInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty",
        jsii_struct_bases=[],
        name_mapping={"token_count": "tokenCount"},
    )
    class TokenBasedTriggerInputProperty:
        def __init__(self, *, token_count: typing.Optional[jsii.Number] = None) -> None:
            '''The token based trigger input.

            :param token_count: The token based trigger token count.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                token_based_trigger_input_property = bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                    token_count=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__171b0765936a13c6e7c17456605ec3e2bc9c36685a864e8c11187bfd9a4bc89a)
                check_type(argname="argument token_count", value=token_count, expected_type=type_hints["token_count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if token_count is not None:
                self._values["token_count"] = token_count

        @builtins.property
        def token_count(self) -> typing.Optional[jsii.Number]:
            '''The token based trigger token count.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-tokenbasedtriggerinput.html#cfn-bedrockagentcore-memory-tokenbasedtriggerinput-tokencount
            '''
            result = self._values.get("token_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TokenBasedTriggerInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.TriggerConditionInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "message_based_trigger": "messageBasedTrigger",
            "time_based_trigger": "timeBasedTrigger",
            "token_based_trigger": "tokenBasedTrigger",
        },
    )
    class TriggerConditionInputProperty:
        def __init__(
            self,
            *,
            message_based_trigger: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.MessageBasedTriggerInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            time_based_trigger: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.TimeBasedTriggerInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            token_based_trigger: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.TokenBasedTriggerInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory trigger condition input.

            :param message_based_trigger: The memory trigger condition input for the message based trigger.
            :param time_based_trigger: The memory trigger condition input.
            :param token_based_trigger: The trigger condition information for a token based trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-triggerconditioninput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                trigger_condition_input_property = bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                    message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                        message_count=123
                    ),
                    time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                        idle_session_timeout=123
                    ),
                    token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                        token_count=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9ca3b096b467bf1778a21961da57f12ce16cf0ef63aeee1b912577f66fdb48cb)
                check_type(argname="argument message_based_trigger", value=message_based_trigger, expected_type=type_hints["message_based_trigger"])
                check_type(argname="argument time_based_trigger", value=time_based_trigger, expected_type=type_hints["time_based_trigger"])
                check_type(argname="argument token_based_trigger", value=token_based_trigger, expected_type=type_hints["token_based_trigger"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if message_based_trigger is not None:
                self._values["message_based_trigger"] = message_based_trigger
            if time_based_trigger is not None:
                self._values["time_based_trigger"] = time_based_trigger
            if token_based_trigger is not None:
                self._values["token_based_trigger"] = token_based_trigger

        @builtins.property
        def message_based_trigger(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.MessageBasedTriggerInputProperty"]]:
            '''The memory trigger condition input for the message based trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-triggerconditioninput.html#cfn-bedrockagentcore-memory-triggerconditioninput-messagebasedtrigger
            '''
            result = self._values.get("message_based_trigger")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.MessageBasedTriggerInputProperty"]], result)

        @builtins.property
        def time_based_trigger(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.TimeBasedTriggerInputProperty"]]:
            '''The memory trigger condition input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-triggerconditioninput.html#cfn-bedrockagentcore-memory-triggerconditioninput-timebasedtrigger
            '''
            result = self._values.get("time_based_trigger")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.TimeBasedTriggerInputProperty"]], result)

        @builtins.property
        def token_based_trigger(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.TokenBasedTriggerInputProperty"]]:
            '''The trigger condition information for a token based trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-triggerconditioninput.html#cfn-bedrockagentcore-memory-triggerconditioninput-tokenbasedtrigger
            '''
            result = self._values.get("token_based_trigger")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.TokenBasedTriggerInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerConditionInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.UserPreferenceMemoryStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "created_at": "createdAt",
            "description": "description",
            "namespaces": "namespaces",
            "status": "status",
            "strategy_id": "strategyId",
            "type": "type",
            "updated_at": "updatedAt",
        },
    )
    class UserPreferenceMemoryStrategyProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            created_at: typing.Optional[builtins.str] = None,
            description: typing.Optional[builtins.str] = None,
            namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
            status: typing.Optional[builtins.str] = None,
            strategy_id: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            updated_at: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The memory strategy.

            :param name: The memory strategy name.
            :param created_at: Creation timestamp of the memory strategy.
            :param description: The memory strategy description.
            :param namespaces: The memory namespaces.
            :param status: The memory strategy status.
            :param strategy_id: The memory strategy ID.
            :param type: The memory strategy type.
            :param updated_at: The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                user_preference_memory_strategy_property = bedrockagentcore.CfnMemory.UserPreferenceMemoryStrategyProperty(
                    name="name",
                
                    # the properties below are optional
                    created_at="createdAt",
                    description="description",
                    namespaces=["namespaces"],
                    status="status",
                    strategy_id="strategyId",
                    type="type",
                    updated_at="updatedAt"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__404072c850abd871eb86ee8d04d20a311da6fb4147c983194a800b234cbf1e04)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument created_at", value=created_at, expected_type=type_hints["created_at"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument namespaces", value=namespaces, expected_type=type_hints["namespaces"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument strategy_id", value=strategy_id, expected_type=type_hints["strategy_id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }
            if created_at is not None:
                self._values["created_at"] = created_at
            if description is not None:
                self._values["description"] = description
            if namespaces is not None:
                self._values["namespaces"] = namespaces
            if status is not None:
                self._values["status"] = status
            if strategy_id is not None:
                self._values["strategy_id"] = strategy_id
            if type is not None:
                self._values["type"] = type
            if updated_at is not None:
                self._values["updated_at"] = updated_at

        @builtins.property
        def name(self) -> builtins.str:
            '''The memory strategy name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def created_at(self) -> typing.Optional[builtins.str]:
            '''Creation timestamp of the memory strategy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-createdat
            '''
            result = self._values.get("created_at")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The memory strategy description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespaces(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The memory namespaces.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-namespaces
            '''
            result = self._values.get("namespaces")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The memory strategy status.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def strategy_id(self) -> typing.Optional[builtins.str]:
            '''The memory strategy ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-strategyid
            '''
            result = self._values.get("strategy_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The memory strategy type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def updated_at(self) -> typing.Optional[builtins.str]:
            '''The memory strategy update date and time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferencememorystrategy.html#cfn-bedrockagentcore-memory-userpreferencememorystrategy-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPreferenceMemoryStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class UserPreferenceOverrideConsolidationConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''The configuration input.

            :param append_to_prompt: The memory configuration.
            :param model_id: The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                user_preference_override_consolidation_configuration_input_property = bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ccf5e9da18deac0b8b6ae4a435ef031fafc5037acda6e9b5a2f31d25335ea0ad)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''The memory configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The memory override configuration model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput.html#cfn-bedrockagentcore-memory-userpreferenceoverrideconsolidationconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPreferenceOverrideConsolidationConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty",
        jsii_struct_bases=[],
        name_mapping={"append_to_prompt": "appendToPrompt", "model_id": "modelId"},
    )
    class UserPreferenceOverrideExtractionConfigurationInputProperty:
        def __init__(
            self,
            *,
            append_to_prompt: builtins.str,
            model_id: builtins.str,
        ) -> None:
            '''The memory override configuration.

            :param append_to_prompt: The extraction configuration.
            :param model_id: The memory override for the model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                user_preference_override_extraction_configuration_input_property = bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                    append_to_prompt="appendToPrompt",
                    model_id="modelId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e2496eed790ccc12ab395eda9327489aa843786babbb42e3d6238d462a4c629)
                check_type(argname="argument append_to_prompt", value=append_to_prompt, expected_type=type_hints["append_to_prompt"])
                check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "append_to_prompt": append_to_prompt,
                "model_id": model_id,
            }

        @builtins.property
        def append_to_prompt(self) -> builtins.str:
            '''The extraction configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput.html#cfn-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-appendtoprompt
            '''
            result = self._values.get("append_to_prompt")
            assert result is not None, "Required property 'append_to_prompt' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def model_id(self) -> builtins.str:
            '''The memory override for the model ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput.html#cfn-bedrockagentcore-memory-userpreferenceoverrideextractionconfigurationinput-modelid
            '''
            result = self._values.get("model_id")
            assert result is not None, "Required property 'model_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPreferenceOverrideExtractionConfigurationInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty",
        jsii_struct_bases=[],
        name_mapping={"consolidation": "consolidation", "extraction": "extraction"},
    )
    class UserPreferenceOverrideProperty:
        def __init__(
            self,
            *,
            consolidation: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            extraction: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The memory user preference override.

            :param consolidation: The memory override consolidation information.
            :param extraction: The memory user preferences for extraction.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverride.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                user_preference_override_property = bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                    consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    ),
                    extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                        append_to_prompt="appendToPrompt",
                        model_id="modelId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a657a70bb10847e586abd34f2ecc11ddcafa4b88002f03b52b85d085202adcfd)
                check_type(argname="argument consolidation", value=consolidation, expected_type=type_hints["consolidation"])
                check_type(argname="argument extraction", value=extraction, expected_type=type_hints["extraction"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if consolidation is not None:
                self._values["consolidation"] = consolidation
            if extraction is not None:
                self._values["extraction"] = extraction

        @builtins.property
        def consolidation(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty"]]:
            '''The memory override consolidation information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverride.html#cfn-bedrockagentcore-memory-userpreferenceoverride-consolidation
            '''
            result = self._values.get("consolidation")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty"]], result)

        @builtins.property
        def extraction(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty"]]:
            '''The memory user preferences for extraction.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-memory-userpreferenceoverride.html#cfn-bedrockagentcore-memory-userpreferenceoverride-extraction
            '''
            result = self._values.get("extraction")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UserPreferenceOverrideProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnMemoryProps",
    jsii_struct_bases=[],
    name_mapping={
        "event_expiry_duration": "eventExpiryDuration",
        "name": "name",
        "description": "description",
        "encryption_key_arn": "encryptionKeyArn",
        "memory_execution_role_arn": "memoryExecutionRoleArn",
        "memory_strategies": "memoryStrategies",
        "tags": "tags",
    },
)
class CfnMemoryProps:
    def __init__(
        self,
        *,
        event_expiry_duration: jsii.Number,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        memory_execution_role_arn: typing.Optional[builtins.str] = None,
        memory_strategies: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnMemory.MemoryStrategyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMemory``.

        :param event_expiry_duration: The event expiry configuration.
        :param name: The memory name.
        :param description: Description of the Memory resource.
        :param encryption_key_arn: The memory encryption key Amazon Resource Name (ARN).
        :param memory_execution_role_arn: The memory role ARN.
        :param memory_strategies: The memory strategies.
        :param tags: The tags for the resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_memory_props = bedrockagentcore.CfnMemoryProps(
                event_expiry_duration=123,
                name="name",
            
                # the properties below are optional
                description="description",
                encryption_key_arn="encryptionKeyArn",
                memory_execution_role_arn="memoryExecutionRoleArn",
                memory_strategies=[bedrockagentcore.CfnMemory.MemoryStrategyProperty(
                    custom_memory_strategy=bedrockagentcore.CfnMemory.CustomMemoryStrategyProperty(
                        name="name",
            
                        # the properties below are optional
                        configuration=bedrockagentcore.CfnMemory.CustomConfigurationInputProperty(
                            episodic_override=bedrockagentcore.CfnMemory.EpisodicOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                extraction=bedrockagentcore.CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                reflection=bedrockagentcore.CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId",
            
                                    # the properties below are optional
                                    namespaces=["namespaces"]
                                )
                            ),
                            self_managed_configuration=bedrockagentcore.CfnMemory.SelfManagedConfigurationProperty(
                                historical_context_window_size=123,
                                invocation_configuration=bedrockagentcore.CfnMemory.InvocationConfigurationInputProperty(
                                    payload_delivery_bucket_name="payloadDeliveryBucketName",
                                    topic_arn="topicArn"
                                ),
                                trigger_conditions=[bedrockagentcore.CfnMemory.TriggerConditionInputProperty(
                                    message_based_trigger=bedrockagentcore.CfnMemory.MessageBasedTriggerInputProperty(
                                        message_count=123
                                    ),
                                    time_based_trigger=bedrockagentcore.CfnMemory.TimeBasedTriggerInputProperty(
                                        idle_session_timeout=123
                                    ),
                                    token_based_trigger=bedrockagentcore.CfnMemory.TokenBasedTriggerInputProperty(
                                        token_count=123
                                    )
                                )]
                            ),
                            semantic_override=bedrockagentcore.CfnMemory.SemanticOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                extraction=bedrockagentcore.CfnMemory.SemanticOverrideExtractionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            ),
                            summary_override=bedrockagentcore.CfnMemory.SummaryOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            ),
                            user_preference_override=bedrockagentcore.CfnMemory.UserPreferenceOverrideProperty(
                                consolidation=bedrockagentcore.CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                ),
                                extraction=bedrockagentcore.CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty(
                                    append_to_prompt="appendToPrompt",
                                    model_id="modelId"
                                )
                            )
                        ),
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    episodic_memory_strategy=bedrockagentcore.CfnMemory.EpisodicMemoryStrategyProperty(
                        name="name",
            
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        reflection_configuration=bedrockagentcore.CfnMemory.EpisodicReflectionConfigurationInputProperty(
                            namespaces=["namespaces"]
                        ),
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    semantic_memory_strategy=bedrockagentcore.CfnMemory.SemanticMemoryStrategyProperty(
                        name="name",
            
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    summary_memory_strategy=bedrockagentcore.CfnMemory.SummaryMemoryStrategyProperty(
                        name="name",
            
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    ),
                    user_preference_memory_strategy=bedrockagentcore.CfnMemory.UserPreferenceMemoryStrategyProperty(
                        name="name",
            
                        # the properties below are optional
                        created_at="createdAt",
                        description="description",
                        namespaces=["namespaces"],
                        status="status",
                        strategy_id="strategyId",
                        type="type",
                        updated_at="updatedAt"
                    )
                )],
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28dda218e5909d8e89c4ab4ee9bac6335e1f1cde1c399e1ac3c1c739ece89e19)
            check_type(argname="argument event_expiry_duration", value=event_expiry_duration, expected_type=type_hints["event_expiry_duration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_key_arn", value=encryption_key_arn, expected_type=type_hints["encryption_key_arn"])
            check_type(argname="argument memory_execution_role_arn", value=memory_execution_role_arn, expected_type=type_hints["memory_execution_role_arn"])
            check_type(argname="argument memory_strategies", value=memory_strategies, expected_type=type_hints["memory_strategies"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_expiry_duration": event_expiry_duration,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if encryption_key_arn is not None:
            self._values["encryption_key_arn"] = encryption_key_arn
        if memory_execution_role_arn is not None:
            self._values["memory_execution_role_arn"] = memory_execution_role_arn
        if memory_strategies is not None:
            self._values["memory_strategies"] = memory_strategies
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def event_expiry_duration(self) -> jsii.Number:
        '''The event expiry configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-eventexpiryduration
        '''
        result = self._values.get("event_expiry_duration")
        assert result is not None, "Required property 'event_expiry_duration' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The memory name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the Memory resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The memory encryption key Amazon Resource Name (ARN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-encryptionkeyarn
        '''
        result = self._values.get("encryption_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory_execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''The memory role ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-memoryexecutionrolearn
        '''
        result = self._values.get("memory_execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def memory_strategies(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnMemory.MemoryStrategyProperty"]]]]:
        '''The memory strategies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-memorystrategies
        '''
        result = self._values.get("memory_strategies")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnMemory.MemoryStrategyProperty"]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-memory.html#cfn-bedrockagentcore-memory-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMemoryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IOnlineEvaluationConfigRef_cf19cabf, _ITaggableV2_4e6798f8)
class CfnOnlineEvaluationConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig",
):
    '''Resource Type definition for AWS::BedrockAgentCore::OnlineEvaluationConfig - Creates an online evaluation configuration for continuous monitoring of agent performance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-onlineevaluationconfig.html
    :cloudformationResource: AWS::BedrockAgentCore::OnlineEvaluationConfig
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_online_evaluation_config = bedrockagentcore.CfnOnlineEvaluationConfig(self, "MyCfnOnlineEvaluationConfig",
            data_source_config=bedrockagentcore.CfnOnlineEvaluationConfig.DataSourceConfigProperty(
                cloud_watch_logs=bedrockagentcore.CfnOnlineEvaluationConfig.CloudWatchLogsInputConfigProperty(
                    log_group_names=["logGroupNames"],
                    service_names=["serviceNames"]
                )
            ),
            evaluation_execution_role_arn="evaluationExecutionRoleArn",
            evaluators=[bedrockagentcore.CfnOnlineEvaluationConfig.EvaluatorReferenceProperty(
                evaluator_id="evaluatorId"
            )],
            online_evaluation_config_name="onlineEvaluationConfigName",
            rule=bedrockagentcore.CfnOnlineEvaluationConfig.RuleProperty(
                sampling_config=bedrockagentcore.CfnOnlineEvaluationConfig.SamplingConfigProperty(
                    sampling_percentage=123
                ),
        
                # the properties below are optional
                filters=[bedrockagentcore.CfnOnlineEvaluationConfig.FilterProperty(
                    key="key",
                    operator="operator",
                    value=bedrockagentcore.CfnOnlineEvaluationConfig.FilterValueProperty(
                        boolean_value=False,
                        double_value=123,
                        string_value="stringValue"
                    )
                )],
                session_config=bedrockagentcore.CfnOnlineEvaluationConfig.SessionConfigProperty(
                    session_timeout_minutes=123
                )
            ),
        
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
        data_source_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.DataSourceConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        evaluation_execution_role_arn: builtins.str,
        evaluators: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.EvaluatorReferenceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        online_evaluation_config_name: builtins.str,
        rule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.RuleProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::OnlineEvaluationConfig``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_source_config: The configuration that specifies where to read agent traces for online evaluation.
        :param evaluation_execution_role_arn: The Amazon Resource Name (ARN) of the IAM role that grants permissions for evaluation.
        :param evaluators: The list of evaluators to apply during online evaluation.
        :param online_evaluation_config_name: The name of the online evaluation configuration. Must be unique within your account.
        :param rule: The evaluation rule that defines sampling configuration, filtering criteria, and session detection settings.
        :param description: The description of the online evaluation configuration.
        :param tags: A list of tags to assign to the online evaluation configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aa0e93d03096cdb556ed3eb9ee7b341e52b0d24c88655e4061d5de404c807ed)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOnlineEvaluationConfigProps(
            data_source_config=data_source_config,
            evaluation_execution_role_arn=evaluation_execution_role_arn,
            evaluators=evaluators,
            online_evaluation_config_name=online_evaluation_config_name,
            rule=rule,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForOnlineEvaluationConfig")
    @builtins.classmethod
    def arn_for_online_evaluation_config(
        cls,
        resource: "_IOnlineEvaluationConfigRef_cf19cabf",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90c4c9bc0bd65c4957d82632ee0e6857bd64fa695b00eff8e97cfe4bbb58212a)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForOnlineEvaluationConfig", [resource]))

    @jsii.member(jsii_name="isCfnOnlineEvaluationConfig")
    @builtins.classmethod
    def is_cfn_online_evaluation_config(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnOnlineEvaluationConfig.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__197c10ea28d6b7fcd6d734a0f7527f987482843ef77aba73be70ab37f3274a87)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnOnlineEvaluationConfig", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__174e31db4a9e05f32574075e0d5d9ca13a10fd3d3f58880897c11aee769870b3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2605ec5d933033d8b4e2a10590a11c2b518e3dc4ada8dd7f8cb9fb3b71bfaec1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the online evaluation configuration was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrExecutionStatus")
    def attr_execution_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: ExecutionStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrExecutionStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrOnlineEvaluationConfigArn")
    def attr_online_evaluation_config_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the online evaluation configuration.

        :cloudformationAttribute: OnlineEvaluationConfigArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOnlineEvaluationConfigArn"))

    @builtins.property
    @jsii.member(jsii_name="attrOnlineEvaluationConfigId")
    def attr_online_evaluation_config_id(self) -> builtins.str:
        '''The unique identifier of the online evaluation configuration.

        :cloudformationAttribute: OnlineEvaluationConfigId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOnlineEvaluationConfigId"))

    @builtins.property
    @jsii.member(jsii_name="attrOutputConfig")
    def attr_output_config(self) -> "_IResolvable_da3f097b":
        '''The configuration that specifies where evaluation results should be written.

        :cloudformationAttribute: OutputConfig
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrOutputConfig"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the online evaluation configuration was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="onlineEvaluationConfigRef")
    def online_evaluation_config_ref(
        self,
    ) -> "_OnlineEvaluationConfigReference_13c14f3c":
        '''A reference to a OnlineEvaluationConfig resource.'''
        return typing.cast("_OnlineEvaluationConfigReference_13c14f3c", jsii.get(self, "onlineEvaluationConfigRef"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceConfig")
    def data_source_config(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.DataSourceConfigProperty"]:
        '''The configuration that specifies where to read agent traces for online evaluation.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.DataSourceConfigProperty"], jsii.get(self, "dataSourceConfig"))

    @data_source_config.setter
    def data_source_config(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.DataSourceConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdec6581e7d868222d3bc0bf43dc993d50bc9f422198fc013c1856f442104865)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="evaluationExecutionRoleArn")
    def evaluation_execution_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants permissions for evaluation.'''
        return typing.cast(builtins.str, jsii.get(self, "evaluationExecutionRoleArn"))

    @evaluation_execution_role_arn.setter
    def evaluation_execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8f1e9b72c99731112fc077560a4c69257c903d6826ca03adba993e9cafec8e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationExecutionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="evaluators")
    def evaluators(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.EvaluatorReferenceProperty"]]]:
        '''The list of evaluators to apply during online evaluation.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.EvaluatorReferenceProperty"]]], jsii.get(self, "evaluators"))

    @evaluators.setter
    def evaluators(
        self,
        value: typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.EvaluatorReferenceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6203a39418b156df1e66640712fbe71f2ddf1f83ac789902b76160c12690a251)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluators", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="onlineEvaluationConfigName")
    def online_evaluation_config_name(self) -> builtins.str:
        '''The name of the online evaluation configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "onlineEvaluationConfigName"))

    @online_evaluation_config_name.setter
    def online_evaluation_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d075f3152c3d233d71d9aad22ce139f2486815a5e44ccde4015d161724a5efda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlineEvaluationConfigName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.RuleProperty"]:
        '''The evaluation rule that defines sampling configuration, filtering criteria, and session detection settings.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.RuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.RuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cf46c720a151dc4eed5fc818c0539ab15e6aced33ff2153a91d7d9a58b47cc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the online evaluation configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9329e42c1ed6716c18f0ba3ed3c4061991e8232ee68b38584dd695b80a862ccb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A list of tags to assign to the online evaluation configuration.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64aa9583ff086b054a843cddaea1d6ba93b7d4aca2beac24d850e42c20b5bac3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig.CloudWatchLogsInputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_group_names": "logGroupNames",
            "service_names": "serviceNames",
        },
    )
    class CloudWatchLogsInputConfigProperty:
        def __init__(
            self,
            *,
            log_group_names: typing.Sequence[builtins.str],
            service_names: typing.Sequence[builtins.str],
        ) -> None:
            '''The configuration for reading agent traces from CloudWatch logs.

            :param log_group_names: The list of CloudWatch log group names to monitor for agent traces.
            :param service_names: The list of service names to filter traces within the specified log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                cloud_watch_logs_input_config_property = bedrockagentcore.CfnOnlineEvaluationConfig.CloudWatchLogsInputConfigProperty(
                    log_group_names=["logGroupNames"],
                    service_names=["serviceNames"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__06d804c8e6fc6685724ca2260796166f7384dcb1ccbf41dd1fa2700163b0ad02)
                check_type(argname="argument log_group_names", value=log_group_names, expected_type=type_hints["log_group_names"])
                check_type(argname="argument service_names", value=service_names, expected_type=type_hints["service_names"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_names": log_group_names,
                "service_names": service_names,
            }

        @builtins.property
        def log_group_names(self) -> typing.List[builtins.str]:
            '''The list of CloudWatch log group names to monitor for agent traces.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-loggroupnames
            '''
            result = self._values.get("log_group_names")
            assert result is not None, "Required property 'log_group_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def service_names(self) -> typing.List[builtins.str]:
            '''The list of service names to filter traces within the specified log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchlogsinputconfig-servicenames
            '''
            result = self._values.get("service_names")
            assert result is not None, "Required property 'service_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsInputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig.CloudWatchOutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName"},
    )
    class CloudWatchOutputConfigProperty:
        def __init__(
            self,
            *,
            log_group_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The CloudWatch configuration for writing evaluation results.

            :param log_group_name: The CloudWatch log group name for evaluation results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                cloud_watch_output_config_property = bedrockagentcore.CfnOnlineEvaluationConfig.CloudWatchOutputConfigProperty(
                    log_group_name="logGroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9fba0fe46886c9e6934bd149cf7b10f76eeb83adfa2cc2a2020d0587e70423c9)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_group_name is not None:
                self._values["log_group_name"] = log_group_name

        @builtins.property
        def log_group_name(self) -> typing.Optional[builtins.str]:
            '''The CloudWatch log group name for evaluation results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-cloudwatchoutputconfig-loggroupname
            '''
            result = self._values.get("log_group_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchOutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig.DataSourceConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_logs": "cloudWatchLogs"},
    )
    class DataSourceConfigProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.CloudWatchLogsInputConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The configuration that specifies where to read agent traces for online evaluation.

            :param cloud_watch_logs: The configuration for reading agent traces from CloudWatch logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-datasourceconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                data_source_config_property = bedrockagentcore.CfnOnlineEvaluationConfig.DataSourceConfigProperty(
                    cloud_watch_logs=bedrockagentcore.CfnOnlineEvaluationConfig.CloudWatchLogsInputConfigProperty(
                        log_group_names=["logGroupNames"],
                        service_names=["serviceNames"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e9e9c1632a43c17755ee22dab7b1cbedd703f1dd6049647d3cdfcc0b43a33016)
                check_type(argname="argument cloud_watch_logs", value=cloud_watch_logs, expected_type=type_hints["cloud_watch_logs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch_logs": cloud_watch_logs,
            }

        @builtins.property
        def cloud_watch_logs(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.CloudWatchLogsInputConfigProperty"]:
            '''The configuration for reading agent traces from CloudWatch logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-datasourceconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-datasourceconfig-cloudwatchlogs
            '''
            result = self._values.get("cloud_watch_logs")
            assert result is not None, "Required property 'cloud_watch_logs' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.CloudWatchLogsInputConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataSourceConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig.EvaluatorReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"evaluator_id": "evaluatorId"},
    )
    class EvaluatorReferenceProperty:
        def __init__(self, *, evaluator_id: builtins.str) -> None:
            '''The reference to an evaluator used in online evaluation configurations.

            :param evaluator_id: The unique identifier of the evaluator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-evaluatorreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                evaluator_reference_property = bedrockagentcore.CfnOnlineEvaluationConfig.EvaluatorReferenceProperty(
                    evaluator_id="evaluatorId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a44db4de7a49610956caf53195620a14d4d68d5a98645ab3f5ff7cb927a9ac54)
                check_type(argname="argument evaluator_id", value=evaluator_id, expected_type=type_hints["evaluator_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "evaluator_id": evaluator_id,
            }

        @builtins.property
        def evaluator_id(self) -> builtins.str:
            '''The unique identifier of the evaluator.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-evaluatorreference.html#cfn-bedrockagentcore-onlineevaluationconfig-evaluatorreference-evaluatorid
            '''
            result = self._values.get("evaluator_id")
            assert result is not None, "Required property 'evaluator_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EvaluatorReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "operator": "operator", "value": "value"},
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            key: builtins.str,
            operator: builtins.str,
            value: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.FilterValueProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The filter that applies conditions to agent traces during online evaluation.

            :param key: The key or field name to filter on within the agent trace data.
            :param operator: The comparison operator to use for filtering.
            :param value: The value used in filter comparisons.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                filter_property = bedrockagentcore.CfnOnlineEvaluationConfig.FilterProperty(
                    key="key",
                    operator="operator",
                    value=bedrockagentcore.CfnOnlineEvaluationConfig.FilterValueProperty(
                        boolean_value=False,
                        double_value=123,
                        string_value="stringValue"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f3af31c16195143a16e0eb30f3c7e34f8a0807321ad86daeb9e4fc31e3f37d3d)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "operator": operator,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key or field name to filter on within the agent trace data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-filter.html#cfn-bedrockagentcore-onlineevaluationconfig-filter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def operator(self) -> builtins.str:
            '''The comparison operator to use for filtering.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-filter.html#cfn-bedrockagentcore-onlineevaluationconfig-filter-operator
            '''
            result = self._values.get("operator")
            assert result is not None, "Required property 'operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.FilterValueProperty"]:
            '''The value used in filter comparisons.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-filter.html#cfn-bedrockagentcore-onlineevaluationconfig-filter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.FilterValueProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig.FilterValueProperty",
        jsii_struct_bases=[],
        name_mapping={
            "boolean_value": "booleanValue",
            "double_value": "doubleValue",
            "string_value": "stringValue",
        },
    )
    class FilterValueProperty:
        def __init__(
            self,
            *,
            boolean_value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
            double_value: typing.Optional[jsii.Number] = None,
            string_value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The value used in filter comparisons.

            :param boolean_value: The boolean value for true/false filtering conditions.
            :param double_value: The numeric value for numerical filtering.
            :param string_value: The string value for text-based filtering.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                filter_value_property = bedrockagentcore.CfnOnlineEvaluationConfig.FilterValueProperty(
                    boolean_value=False,
                    double_value=123,
                    string_value="stringValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b42f86596813ff2e3e66267d5100485bb51a02b655555985649c33361c96f19)
                check_type(argname="argument boolean_value", value=boolean_value, expected_type=type_hints["boolean_value"])
                check_type(argname="argument double_value", value=double_value, expected_type=type_hints["double_value"])
                check_type(argname="argument string_value", value=string_value, expected_type=type_hints["string_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if boolean_value is not None:
                self._values["boolean_value"] = boolean_value
            if double_value is not None:
                self._values["double_value"] = double_value
            if string_value is not None:
                self._values["string_value"] = string_value

        @builtins.property
        def boolean_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''The boolean value for true/false filtering conditions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue.html#cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-booleanvalue
            '''
            result = self._values.get("boolean_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        @builtins.property
        def double_value(self) -> typing.Optional[jsii.Number]:
            '''The numeric value for numerical filtering.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue.html#cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-doublevalue
            '''
            result = self._values.get("double_value")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def string_value(self) -> typing.Optional[builtins.str]:
            '''The string value for text-based filtering.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-filtervalue.html#cfn-bedrockagentcore-onlineevaluationconfig-filtervalue-stringvalue
            '''
            result = self._values.get("string_value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterValueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig.OutputConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_config": "cloudWatchConfig"},
    )
    class OutputConfigProperty:
        def __init__(
            self,
            *,
            cloud_watch_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.CloudWatchOutputConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration that specifies where evaluation results should be written.

            :param cloud_watch_config: The CloudWatch configuration for writing evaluation results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-outputconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                output_config_property = bedrockagentcore.CfnOnlineEvaluationConfig.OutputConfigProperty(
                    cloud_watch_config=bedrockagentcore.CfnOnlineEvaluationConfig.CloudWatchOutputConfigProperty(
                        log_group_name="logGroupName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__901f04239ac1d631f611bae7e5b46abe7106c2310714eeae85eb20759dad8182)
                check_type(argname="argument cloud_watch_config", value=cloud_watch_config, expected_type=type_hints["cloud_watch_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_config is not None:
                self._values["cloud_watch_config"] = cloud_watch_config

        @builtins.property
        def cloud_watch_config(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.CloudWatchOutputConfigProperty"]]:
            '''The CloudWatch configuration for writing evaluation results.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-outputconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-outputconfig-cloudwatchconfig
            '''
            result = self._values.get("cloud_watch_config")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.CloudWatchOutputConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OutputConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "sampling_config": "samplingConfig",
            "filters": "filters",
            "session_config": "sessionConfig",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            sampling_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.SamplingConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            filters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.FilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            session_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.SessionConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The evaluation rule that defines sampling configuration, filtering criteria, and session detection settings.

            :param sampling_config: The configuration that controls what percentage of agent traces are sampled for evaluation.
            :param filters: The list of filters that determine which agent traces should be included in the evaluation.
            :param session_config: The configuration that defines how agent sessions are detected.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                rule_property = bedrockagentcore.CfnOnlineEvaluationConfig.RuleProperty(
                    sampling_config=bedrockagentcore.CfnOnlineEvaluationConfig.SamplingConfigProperty(
                        sampling_percentage=123
                    ),
                
                    # the properties below are optional
                    filters=[bedrockagentcore.CfnOnlineEvaluationConfig.FilterProperty(
                        key="key",
                        operator="operator",
                        value=bedrockagentcore.CfnOnlineEvaluationConfig.FilterValueProperty(
                            boolean_value=False,
                            double_value=123,
                            string_value="stringValue"
                        )
                    )],
                    session_config=bedrockagentcore.CfnOnlineEvaluationConfig.SessionConfigProperty(
                        session_timeout_minutes=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d26dc57868bb2276aa712667113ed9c9d243f98c5821e624a9c99a224d918c0)
                check_type(argname="argument sampling_config", value=sampling_config, expected_type=type_hints["sampling_config"])
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
                check_type(argname="argument session_config", value=session_config, expected_type=type_hints["session_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sampling_config": sampling_config,
            }
            if filters is not None:
                self._values["filters"] = filters
            if session_config is not None:
                self._values["session_config"] = session_config

        @builtins.property
        def sampling_config(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.SamplingConfigProperty"]:
            '''The configuration that controls what percentage of agent traces are sampled for evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-rule.html#cfn-bedrockagentcore-onlineevaluationconfig-rule-samplingconfig
            '''
            result = self._values.get("sampling_config")
            assert result is not None, "Required property 'sampling_config' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.SamplingConfigProperty"], result)

        @builtins.property
        def filters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.FilterProperty"]]]]:
            '''The list of filters that determine which agent traces should be included in the evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-rule.html#cfn-bedrockagentcore-onlineevaluationconfig-rule-filters
            '''
            result = self._values.get("filters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.FilterProperty"]]]], result)

        @builtins.property
        def session_config(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.SessionConfigProperty"]]:
            '''The configuration that defines how agent sessions are detected.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-rule.html#cfn-bedrockagentcore-onlineevaluationconfig-rule-sessionconfig
            '''
            result = self._values.get("session_config")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.SessionConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig.SamplingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"sampling_percentage": "samplingPercentage"},
    )
    class SamplingConfigProperty:
        def __init__(self, *, sampling_percentage: jsii.Number) -> None:
            '''The configuration that controls what percentage of agent traces are sampled for evaluation.

            :param sampling_percentage: The percentage of agent traces to sample for evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-samplingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                sampling_config_property = bedrockagentcore.CfnOnlineEvaluationConfig.SamplingConfigProperty(
                    sampling_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1e4b82a47eb409b6be018392f32b388af0c03327656d5cdcf118e6dff7977b6f)
                check_type(argname="argument sampling_percentage", value=sampling_percentage, expected_type=type_hints["sampling_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sampling_percentage": sampling_percentage,
            }

        @builtins.property
        def sampling_percentage(self) -> jsii.Number:
            '''The percentage of agent traces to sample for evaluation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-samplingconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-samplingconfig-samplingpercentage
            '''
            result = self._values.get("sampling_percentage")
            assert result is not None, "Required property 'sampling_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SamplingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfig.SessionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"session_timeout_minutes": "sessionTimeoutMinutes"},
    )
    class SessionConfigProperty:
        def __init__(self, *, session_timeout_minutes: jsii.Number) -> None:
            '''The configuration that defines how agent sessions are detected.

            :param session_timeout_minutes: The number of minutes of inactivity after which an agent session is considered complete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-sessionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                session_config_property = bedrockagentcore.CfnOnlineEvaluationConfig.SessionConfigProperty(
                    session_timeout_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a2e489fef922673116efb3ad1b62ccdb82d7343318d520456ba5e2d6e89b2afb)
                check_type(argname="argument session_timeout_minutes", value=session_timeout_minutes, expected_type=type_hints["session_timeout_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "session_timeout_minutes": session_timeout_minutes,
            }

        @builtins.property
        def session_timeout_minutes(self) -> jsii.Number:
            '''The number of minutes of inactivity after which an agent session is considered complete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-onlineevaluationconfig-sessionconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-sessionconfig-sessiontimeoutminutes
            '''
            result = self._values.get("session_timeout_minutes")
            assert result is not None, "Required property 'session_timeout_minutes' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SessionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnOnlineEvaluationConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_source_config": "dataSourceConfig",
        "evaluation_execution_role_arn": "evaluationExecutionRoleArn",
        "evaluators": "evaluators",
        "online_evaluation_config_name": "onlineEvaluationConfigName",
        "rule": "rule",
        "description": "description",
        "tags": "tags",
    },
)
class CfnOnlineEvaluationConfigProps:
    def __init__(
        self,
        *,
        data_source_config: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.DataSourceConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        evaluation_execution_role_arn: builtins.str,
        evaluators: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.EvaluatorReferenceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        online_evaluation_config_name: builtins.str,
        rule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOnlineEvaluationConfig.RuleProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOnlineEvaluationConfig``.

        :param data_source_config: The configuration that specifies where to read agent traces for online evaluation.
        :param evaluation_execution_role_arn: The Amazon Resource Name (ARN) of the IAM role that grants permissions for evaluation.
        :param evaluators: The list of evaluators to apply during online evaluation.
        :param online_evaluation_config_name: The name of the online evaluation configuration. Must be unique within your account.
        :param rule: The evaluation rule that defines sampling configuration, filtering criteria, and session detection settings.
        :param description: The description of the online evaluation configuration.
        :param tags: A list of tags to assign to the online evaluation configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-onlineevaluationconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_online_evaluation_config_props = bedrockagentcore.CfnOnlineEvaluationConfigProps(
                data_source_config=bedrockagentcore.CfnOnlineEvaluationConfig.DataSourceConfigProperty(
                    cloud_watch_logs=bedrockagentcore.CfnOnlineEvaluationConfig.CloudWatchLogsInputConfigProperty(
                        log_group_names=["logGroupNames"],
                        service_names=["serviceNames"]
                    )
                ),
                evaluation_execution_role_arn="evaluationExecutionRoleArn",
                evaluators=[bedrockagentcore.CfnOnlineEvaluationConfig.EvaluatorReferenceProperty(
                    evaluator_id="evaluatorId"
                )],
                online_evaluation_config_name="onlineEvaluationConfigName",
                rule=bedrockagentcore.CfnOnlineEvaluationConfig.RuleProperty(
                    sampling_config=bedrockagentcore.CfnOnlineEvaluationConfig.SamplingConfigProperty(
                        sampling_percentage=123
                    ),
            
                    # the properties below are optional
                    filters=[bedrockagentcore.CfnOnlineEvaluationConfig.FilterProperty(
                        key="key",
                        operator="operator",
                        value=bedrockagentcore.CfnOnlineEvaluationConfig.FilterValueProperty(
                            boolean_value=False,
                            double_value=123,
                            string_value="stringValue"
                        )
                    )],
                    session_config=bedrockagentcore.CfnOnlineEvaluationConfig.SessionConfigProperty(
                        session_timeout_minutes=123
                    )
                ),
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0027d3063b3949a340eab6076bb9ce68daa108d23e44efbf30f9a1211d0261e5)
            check_type(argname="argument data_source_config", value=data_source_config, expected_type=type_hints["data_source_config"])
            check_type(argname="argument evaluation_execution_role_arn", value=evaluation_execution_role_arn, expected_type=type_hints["evaluation_execution_role_arn"])
            check_type(argname="argument evaluators", value=evaluators, expected_type=type_hints["evaluators"])
            check_type(argname="argument online_evaluation_config_name", value=online_evaluation_config_name, expected_type=type_hints["online_evaluation_config_name"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_source_config": data_source_config,
            "evaluation_execution_role_arn": evaluation_execution_role_arn,
            "evaluators": evaluators,
            "online_evaluation_config_name": online_evaluation_config_name,
            "rule": rule,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def data_source_config(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.DataSourceConfigProperty"]:
        '''The configuration that specifies where to read agent traces for online evaluation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-onlineevaluationconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-datasourceconfig
        '''
        result = self._values.get("data_source_config")
        assert result is not None, "Required property 'data_source_config' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.DataSourceConfigProperty"], result)

    @builtins.property
    def evaluation_execution_role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants permissions for evaluation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-onlineevaluationconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-evaluationexecutionrolearn
        '''
        result = self._values.get("evaluation_execution_role_arn")
        assert result is not None, "Required property 'evaluation_execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def evaluators(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.EvaluatorReferenceProperty"]]]:
        '''The list of evaluators to apply during online evaluation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-onlineevaluationconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-evaluators
        '''
        result = self._values.get("evaluators")
        assert result is not None, "Required property 'evaluators' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.EvaluatorReferenceProperty"]]], result)

    @builtins.property
    def online_evaluation_config_name(self) -> builtins.str:
        '''The name of the online evaluation configuration.

        Must be unique within your account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-onlineevaluationconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-onlineevaluationconfigname
        '''
        result = self._values.get("online_evaluation_config_name")
        assert result is not None, "Required property 'online_evaluation_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.RuleProperty"]:
        '''The evaluation rule that defines sampling configuration, filtering criteria, and session detection settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-onlineevaluationconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOnlineEvaluationConfig.RuleProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the online evaluation configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-onlineevaluationconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A list of tags to assign to the online evaluation configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-onlineevaluationconfig.html#cfn-bedrockagentcore-onlineevaluationconfig-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOnlineEvaluationConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IPolicyRef_ceb8b108)
class CfnPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnPolicy",
):
    '''Resource Type definition for AWS::BedrockAgentCore::Policy.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policy.html
    :cloudformationResource: AWS::BedrockAgentCore::Policy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_policy = bedrockagentcore.CfnPolicy(self, "MyCfnPolicy",
            definition=bedrockagentcore.CfnPolicy.PolicyDefinitionProperty(
                cedar=bedrockagentcore.CfnPolicy.CedarPolicyProperty(
                    statement="statement"
                )
            ),
            name="name",
            policy_engine_id="policyEngineId",
        
            # the properties below are optional
            description="description",
            validation_mode="validationMode"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        definition: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPolicy.PolicyDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        policy_engine_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        validation_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::Policy``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param definition: The definition structure for policies. Encapsulates different policy formats.
        :param name: The customer-assigned immutable name for the policy. Must be unique within the policy engine.
        :param policy_engine_id: The identifier of the policy engine which contains this policy.
        :param description: A human-readable description of the policy's purpose and functionality.
        :param validation_mode: The validation mode for the policy. Determines how Cedar analyzer validation results are handled.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0df0ec34c1700a2fd80d71aa113459b1f257b8a6040e2dac1057827afc8f5d2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyProps(
            definition=definition,
            name=name,
            policy_engine_id=policy_engine_id,
            description=description,
            validation_mode=validation_mode,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForPolicy")
    @builtins.classmethod
    def arn_for_policy(cls, resource: "_IPolicyRef_ceb8b108") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a816e5e2df5c6422bb1b1425f808d869fb6346315014ecb535bc6ef61807b51)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForPolicy", [resource]))

    @jsii.member(jsii_name="isCfnPolicy")
    @builtins.classmethod
    def is_cfn_policy(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnPolicy.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e91554c5d78a87cee0dcc173750b965564cc04c6f7914d1203eda44a959ddbe)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnPolicy", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60ea8f973b55390f2cec1d7d6883b362c9bcebcabd3ad90203d8003b259cc15a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__90aa01410268a0a9b8329f1730f233722091722e470d4250502fb81196d7aaa9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the policy was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyArn")
    def attr_policy_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the policy.

        :cloudformationAttribute: PolicyArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyId")
    def attr_policy_id(self) -> builtins.str:
        '''The unique identifier for the policy.

        :cloudformationAttribute: PolicyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReasons")
    def attr_status_reasons(self) -> typing.List[builtins.str]:
        '''Additional information about the policy status.

        :cloudformationAttribute: StatusReasons
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrStatusReasons"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the policy was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policyRef")
    def policy_ref(self) -> "_PolicyReference_d2f6bd10":
        '''A reference to a Policy resource.'''
        return typing.cast("_PolicyReference_d2f6bd10", jsii.get(self, "policyRef"))

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnPolicy.PolicyDefinitionProperty"]:
        '''The definition structure for policies.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPolicy.PolicyDefinitionProperty"], jsii.get(self, "definition"))

    @definition.setter
    def definition(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnPolicy.PolicyDefinitionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50b7eef4611f94f2995d764a972bab6f09b1ad87de0e3c55ef05b5ef7a2ce77f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The customer-assigned immutable name for the policy.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fb243c83cba8b4cece81df4ce8b043bd043afc8a22739fa364e09cb5a0172a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="policyEngineId")
    def policy_engine_id(self) -> builtins.str:
        '''The identifier of the policy engine which contains this policy.'''
        return typing.cast(builtins.str, jsii.get(self, "policyEngineId"))

    @policy_engine_id.setter
    def policy_engine_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60f6d37f81d7766e81b7e5afe51a2b3830f091c1efc676ca8f71909ca61dc2c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyEngineId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the policy's purpose and functionality.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76a62df0bf0572336e2f28e5a6426bde1f261612e5e0c84a7839f62c6771062a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="validationMode")
    def validation_mode(self) -> typing.Optional[builtins.str]:
        '''The validation mode for the policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validationMode"))

    @validation_mode.setter
    def validation_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e182f5e6fcaeb9a8106b8902eb058d4494505efd524ef30250a9e7b351ecbca9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validationMode", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnPolicy.CedarPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={"statement": "statement"},
    )
    class CedarPolicyProperty:
        def __init__(self, *, statement: builtins.str) -> None:
            '''A Cedar policy statement within the AgentCore Policy system.

            :param statement: The Cedar policy statement that defines the authorization logic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-policy-cedarpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                cedar_policy_property = bedrockagentcore.CfnPolicy.CedarPolicyProperty(
                    statement="statement"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd4c98edc5615559914b5f68ccb2078c51b044946e201c8db3860329b3824d87)
                check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "statement": statement,
            }

        @builtins.property
        def statement(self) -> builtins.str:
            '''The Cedar policy statement that defines the authorization logic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-policy-cedarpolicy.html#cfn-bedrockagentcore-policy-cedarpolicy-statement
            '''
            result = self._values.get("statement")
            assert result is not None, "Required property 'statement' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CedarPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnPolicy.PolicyDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"cedar": "cedar"},
    )
    class PolicyDefinitionProperty:
        def __init__(
            self,
            *,
            cedar: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPolicy.CedarPolicyProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The definition structure for policies.

            Encapsulates different policy formats.

            :param cedar: A Cedar policy statement within the AgentCore Policy system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-policy-policydefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                policy_definition_property = bedrockagentcore.CfnPolicy.PolicyDefinitionProperty(
                    cedar=bedrockagentcore.CfnPolicy.CedarPolicyProperty(
                        statement="statement"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6794e02be8a07b494523ce530bdb5da6ec840b4e6342043fc96304f1d964632)
                check_type(argname="argument cedar", value=cedar, expected_type=type_hints["cedar"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cedar": cedar,
            }

        @builtins.property
        def cedar(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnPolicy.CedarPolicyProperty"]:
            '''A Cedar policy statement within the AgentCore Policy system.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-policy-policydefinition.html#cfn-bedrockagentcore-policy-policydefinition-cedar
            '''
            result = self._values.get("cedar")
            assert result is not None, "Required property 'cedar' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPolicy.CedarPolicyProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _IPolicyEngineRef_6d885cfc, _ITaggableV2_4e6798f8)
class CfnPolicyEngine(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnPolicyEngine",
):
    '''Resource Type definition for AWS::BedrockAgentCore::PolicyEngine.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policyengine.html
    :cloudformationResource: AWS::BedrockAgentCore::PolicyEngine
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_policy_engine = bedrockagentcore.CfnPolicyEngine(self, "MyCfnPolicyEngine",
            name="name",
        
            # the properties below are optional
            description="description",
            encryption_key_arn="encryptionKeyArn",
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
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::PolicyEngine``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The customer-assigned immutable name for the policy engine.
        :param description: A human-readable description of the policy engine's purpose and scope.
        :param encryption_key_arn: The ARN of the KMS key used to encrypt the policy engine data.
        :param tags: A list of tags to assign to the policy engine.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4684b4b63ba85bd5dc7e5f6733555e789f7d88f65ee00f5c487dfa126d7d66a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyEngineProps(
            name=name,
            description=description,
            encryption_key_arn=encryption_key_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForPolicyEngine")
    @builtins.classmethod
    def arn_for_policy_engine(
        cls,
        resource: "_IPolicyEngineRef_6d885cfc",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d723add61d7456bc287abcb7c2d34c95e4a9b40b0262b2e977f594db1e112a7)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForPolicyEngine", [resource]))

    @jsii.member(jsii_name="isCfnPolicyEngine")
    @builtins.classmethod
    def is_cfn_policy_engine(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnPolicyEngine.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59e6805c5178d527b1123a3cbf1f0ed0ac21a3f1c2183a86f13cf97df9dfd42d)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnPolicyEngine", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99bc04a5a5e66cb6d659f81b4ca399b70db0cc9d00d7826dba5b19ac18eb3320)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a640866ee40ff74b9b0ee9128a48548073cba59e18f794d91bbf0866e5b9aa8a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the policy engine was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyEngineArn")
    def attr_policy_engine_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the policy engine.

        :cloudformationAttribute: PolicyEngineArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyEngineArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyEngineId")
    def attr_policy_engine_id(self) -> builtins.str:
        '''The unique identifier for the policy engine.

        :cloudformationAttribute: PolicyEngineId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyEngineId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReasons")
    def attr_status_reasons(self) -> typing.List[builtins.str]:
        '''Additional information about the policy engine status.

        :cloudformationAttribute: StatusReasons
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrStatusReasons"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the policy engine was last updated.

        :cloudformationAttribute: UpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdatedAt"))

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
    @jsii.member(jsii_name="policyEngineRef")
    def policy_engine_ref(self) -> "_PolicyEngineReference_471db68b":
        '''A reference to a PolicyEngine resource.'''
        return typing.cast("_PolicyEngineReference_471db68b", jsii.get(self, "policyEngineRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The customer-assigned immutable name for the policy engine.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35ac69c1793e7303c1dfe586ac140b18e9794de8ad51c5575ee3590b2e81efb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the policy engine's purpose and scope.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21dd4fe5af219c86bdbd3e23a682d03cc71ff9b8174dae386145a37d5c2f867e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyArn")
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the KMS key used to encrypt the policy engine data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyArn"))

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d9709f935befd653e89210289122143b738739fbfeed30480fbdd76a67d0042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKeyArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A list of tags to assign to the policy engine.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a9c73af7cca4aa195504171baebe7bcb53d06bd21f6e242c33bf4700692135d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnPolicyEngineProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "encryption_key_arn": "encryptionKeyArn",
        "tags": "tags",
    },
)
class CfnPolicyEngineProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicyEngine``.

        :param name: The customer-assigned immutable name for the policy engine.
        :param description: A human-readable description of the policy engine's purpose and scope.
        :param encryption_key_arn: The ARN of the KMS key used to encrypt the policy engine data.
        :param tags: A list of tags to assign to the policy engine.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policyengine.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_policy_engine_props = bedrockagentcore.CfnPolicyEngineProps(
                name="name",
            
                # the properties below are optional
                description="description",
                encryption_key_arn="encryptionKeyArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__743592ad2798d644b313c682b278dfac01eb5a93d7b7fe59943eaddab0ca5a1f)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_key_arn", value=encryption_key_arn, expected_type=type_hints["encryption_key_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if encryption_key_arn is not None:
            self._values["encryption_key_arn"] = encryption_key_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The customer-assigned immutable name for the policy engine.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policyengine.html#cfn-bedrockagentcore-policyengine-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the policy engine's purpose and scope.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policyengine.html#cfn-bedrockagentcore-policyengine-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the KMS key used to encrypt the policy engine data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policyengine.html#cfn-bedrockagentcore-policyengine-encryptionkeyarn
        '''
        result = self._values.get("encryption_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A list of tags to assign to the policy engine.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policyengine.html#cfn-bedrockagentcore-policyengine-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyEngineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "definition": "definition",
        "name": "name",
        "policy_engine_id": "policyEngineId",
        "description": "description",
        "validation_mode": "validationMode",
    },
)
class CfnPolicyProps:
    def __init__(
        self,
        *,
        definition: typing.Union["_IResolvable_da3f097b", typing.Union["CfnPolicy.PolicyDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        policy_engine_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        validation_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicy``.

        :param definition: The definition structure for policies. Encapsulates different policy formats.
        :param name: The customer-assigned immutable name for the policy. Must be unique within the policy engine.
        :param policy_engine_id: The identifier of the policy engine which contains this policy.
        :param description: A human-readable description of the policy's purpose and functionality.
        :param validation_mode: The validation mode for the policy. Determines how Cedar analyzer validation results are handled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_policy_props = bedrockagentcore.CfnPolicyProps(
                definition=bedrockagentcore.CfnPolicy.PolicyDefinitionProperty(
                    cedar=bedrockagentcore.CfnPolicy.CedarPolicyProperty(
                        statement="statement"
                    )
                ),
                name="name",
                policy_engine_id="policyEngineId",
            
                # the properties below are optional
                description="description",
                validation_mode="validationMode"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95094990d09b6f6bc15ab83744a973bf7541ebc86b713d23c0165d6234555308)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy_engine_id", value=policy_engine_id, expected_type=type_hints["policy_engine_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument validation_mode", value=validation_mode, expected_type=type_hints["validation_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "definition": definition,
            "name": name,
            "policy_engine_id": policy_engine_id,
        }
        if description is not None:
            self._values["description"] = description
        if validation_mode is not None:
            self._values["validation_mode"] = validation_mode

    @builtins.property
    def definition(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnPolicy.PolicyDefinitionProperty"]:
        '''The definition structure for policies.

        Encapsulates different policy formats.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policy.html#cfn-bedrockagentcore-policy-definition
        '''
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnPolicy.PolicyDefinitionProperty"], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The customer-assigned immutable name for the policy.

        Must be unique within the policy engine.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policy.html#cfn-bedrockagentcore-policy-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy_engine_id(self) -> builtins.str:
        '''The identifier of the policy engine which contains this policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policy.html#cfn-bedrockagentcore-policy-policyengineid
        '''
        result = self._values.get("policy_engine_id")
        assert result is not None, "Required property 'policy_engine_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the policy's purpose and functionality.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policy.html#cfn-bedrockagentcore-policy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validation_mode(self) -> typing.Optional[builtins.str]:
        '''The validation mode for the policy.

        Determines how Cedar analyzer validation results are handled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-policy.html#cfn-bedrockagentcore-policy-validationmode
        '''
        result = self._values.get("validation_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IRuntimeRef_00302e12, _ITaggableV2_4e6798f8)
class CfnRuntime(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime",
):
    '''Contains information about an agent runtime. An agent runtime is the execution environment for a Amazon Bedrock Agent.

    AgentCore Runtime is a secure, serverless runtime purpose-built for deploying and scaling dynamic AI agents and tools using any open-source framework including LangGraph, CrewAI, and Strands Agents, any protocol, and any model.

    For more information about using agent runtime in Amazon Bedrock AgentCore, see `Host agent or tools with Amazon Bedrock AgentCore Runtime <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html
    :cloudformationResource: AWS::BedrockAgentCore::Runtime
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_runtime = bedrockagentcore.CfnRuntime(self, "MyCfnRuntime",
            agent_runtime_artifact=bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                code_configuration=bedrockagentcore.CfnRuntime.CodeConfigurationProperty(
                    code=bedrockagentcore.CfnRuntime.CodeProperty(
                        s3=bedrockagentcore.CfnRuntime.S3LocationProperty(
                            bucket="bucket",
                            prefix="prefix",
        
                            # the properties below are optional
                            version_id="versionId"
                        )
                    ),
                    entry_point=["entryPoint"],
                    runtime="runtime"
                ),
                container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri="containerUri"
                )
            ),
            agent_runtime_name="agentRuntimeName",
            network_configuration=bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(
                network_mode="networkMode",
        
                # the properties below are optional
                network_mode_config=bedrockagentcore.CfnRuntime.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            authorizer_configuration=bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
        
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"],
                    allowed_scopes=["allowedScopes"],
                    custom_claims=[bedrockagentcore.CfnRuntime.CustomClaimValidationTypeProperty(
                        authorizing_claim_match_value=bedrockagentcore.CfnRuntime.AuthorizingClaimMatchValueTypeProperty(
                            claim_match_operator="claimMatchOperator",
                            claim_match_value=bedrockagentcore.CfnRuntime.ClaimMatchValueTypeProperty(
                                match_value_string="matchValueString",
                                match_value_string_list=["matchValueStringList"]
                            )
                        ),
                        inbound_token_claim_name="inboundTokenClaimName",
                        inbound_token_claim_value_type="inboundTokenClaimValueType"
                    )]
                )
            ),
            description="description",
            environment_variables={
                "environment_variables_key": "environmentVariables"
            },
            lifecycle_configuration=bedrockagentcore.CfnRuntime.LifecycleConfigurationProperty(
                idle_runtime_session_timeout=123,
                max_lifetime=123
            ),
            protocol_configuration="protocolConfiguration",
            request_header_configuration=bedrockagentcore.CfnRuntime.RequestHeaderConfigurationProperty(
                request_header_allowlist=["requestHeaderAllowlist"]
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        agent_runtime_artifact: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.AgentRuntimeArtifactProperty", typing.Dict[builtins.str, typing.Any]]],
        agent_runtime_name: builtins.str,
        network_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        authorizer_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]] = None,
        lifecycle_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.LifecycleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        protocol_configuration: typing.Optional[builtins.str] = None,
        request_header_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.RequestHeaderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::Runtime``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_runtime_artifact: The artifact of the agent.
        :param agent_runtime_name: The name of the AgentCore Runtime endpoint.
        :param network_configuration: The network configuration.
        :param role_arn: The Amazon Resource Name (ARN) for for the role.
        :param authorizer_configuration: Represents inbound authorization configuration options used to authenticate incoming requests.
        :param description: The agent runtime description.
        :param environment_variables: The environment variables for the agent.
        :param lifecycle_configuration: Configuration for managing the lifecycle of runtime sessions and resources.
        :param protocol_configuration: The protocol configuration for an agent runtime. This structure defines how the agent runtime communicates with clients.
        :param request_header_configuration: Configuration for HTTP request headers.
        :param tags: The tags for the agent.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8f75c2b58380182b53165109480fecdbf9bcd35c2fcfcfea5141466ba05b7e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuntimeProps(
            agent_runtime_artifact=agent_runtime_artifact,
            agent_runtime_name=agent_runtime_name,
            network_configuration=network_configuration,
            role_arn=role_arn,
            authorizer_configuration=authorizer_configuration,
            description=description,
            environment_variables=environment_variables,
            lifecycle_configuration=lifecycle_configuration,
            protocol_configuration=protocol_configuration,
            request_header_configuration=request_header_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForRuntime")
    @builtins.classmethod
    def arn_for_runtime(cls, resource: "_IRuntimeRef_00302e12") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479c61f7c7f79ce5de0ca6bc78388693d928e50602c049521e888404369b8c81)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForRuntime", [resource]))

    @jsii.member(jsii_name="isCfnRuntime")
    @builtins.classmethod
    def is_cfn_runtime(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnRuntime.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64de4894e52d23f2312943e0eaaba7eff4dbdb44d5dc64e873e7a65d9d67e7bd)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnRuntime", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41eb1aeeb420a432d00eafdf7061763658f434f8c1b3fac5748e0b80cf168cda)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ffbc19212156590bcfcec54a917d56095cf1d0e95a1f4f4107501a8cf457feb7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeArn")
    def attr_agent_runtime_arn(self) -> builtins.str:
        '''The agent runtime ARN.

        :cloudformationAttribute: AgentRuntimeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeId")
    def attr_agent_runtime_id(self) -> builtins.str:
        '''The ID for the agent runtime.

        :cloudformationAttribute: AgentRuntimeId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeId"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeVersion")
    def attr_agent_runtime_version(self) -> builtins.str:
        '''The version for the agent runtime.

        :cloudformationAttribute: AgentRuntimeVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time at which the runtime was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''The reason for failure if the agent is in a failed state.

        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The time at which the runtime was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status for the agent runtime.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkloadIdentityDetails")
    def attr_workload_identity_details(self) -> "_IResolvable_da3f097b":
        '''Configuration for workload identity.

        :cloudformationAttribute: WorkloadIdentityDetails
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrWorkloadIdentityDetails"))

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
    @jsii.member(jsii_name="runtimeRef")
    def runtime_ref(self) -> "_RuntimeReference_bdb3da48":
        '''A reference to a Runtime resource.'''
        return typing.cast("_RuntimeReference_bdb3da48", jsii.get(self, "runtimeRef"))

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeArtifact")
    def agent_runtime_artifact(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnRuntime.AgentRuntimeArtifactProperty"]:
        '''The artifact of the agent.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRuntime.AgentRuntimeArtifactProperty"], jsii.get(self, "agentRuntimeArtifact"))

    @agent_runtime_artifact.setter
    def agent_runtime_artifact(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnRuntime.AgentRuntimeArtifactProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9afa965e1f7852c99b813a59ddc326e4e8b2e629273fff790e48abcc309421fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeArtifact", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeName")
    def agent_runtime_name(self) -> builtins.str:
        '''The name of the AgentCore Runtime endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "agentRuntimeName"))

    @agent_runtime_name.setter
    def agent_runtime_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20e5f3a5d4d3f3cf24f87565ebb2f7c531ed9e006970eb5a59dee4eeed670f19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnRuntime.NetworkConfigurationProperty"]:
        '''The network configuration.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRuntime.NetworkConfigurationProperty"], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnRuntime.NetworkConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76a3b80aa643920bb76e97b49e6d7c54f3367df4203a420045d6d631a4d54658)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for for the role.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__712719ad084eaaa1f88407e6da1dd4ed68fa570a04329676de9d476fde02ebfe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="authorizerConfiguration")
    def authorizer_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.AuthorizerConfigurationProperty"]]:
        '''Represents inbound authorization configuration options used to authenticate incoming requests.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.AuthorizerConfigurationProperty"]], jsii.get(self, "authorizerConfiguration"))

    @authorizer_configuration.setter
    def authorizer_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.AuthorizerConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577d498b775175712bf02d50d4dc0a7fa74d069187c6c0daba641442a844c29e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The agent runtime description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86887c96ad11d54aa9be7288cd5dfe9a9b3cb370236b2cf8c98f0ea09d7246e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="environmentVariables")
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]]:
        '''The environment variables for the agent.'''
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]], jsii.get(self, "environmentVariables"))

    @environment_variables.setter
    def environment_variables(
        self,
        value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27b52f571e16cbee3d0cb6aef888169b2fdf172a92199c29075b1bbfe5eb3091)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentVariables", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfiguration")
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.LifecycleConfigurationProperty"]]:
        '''Configuration for managing the lifecycle of runtime sessions and resources.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.LifecycleConfigurationProperty"]], jsii.get(self, "lifecycleConfiguration"))

    @lifecycle_configuration.setter
    def lifecycle_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.LifecycleConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fa017855df5800a745ab54e05af1f928ca7fbff9580670f50aa611ef9670585)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocolConfiguration")
    def protocol_configuration(self) -> typing.Optional[builtins.str]:
        '''The protocol configuration for an agent runtime.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolConfiguration"))

    @protocol_configuration.setter
    def protocol_configuration(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd16ca9a4cf1077fb69bea991264277b990667565406b724c960232073239095)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="requestHeaderConfiguration")
    def request_header_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.RequestHeaderConfigurationProperty"]]:
        '''Configuration for HTTP request headers.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.RequestHeaderConfigurationProperty"]], jsii.get(self, "requestHeaderConfiguration"))

    @request_header_configuration.setter
    def request_header_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.RequestHeaderConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0964845eb3d77c8d88078f56bcf318b9fe4fa50078a5bf150216455e4bc0cde0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestHeaderConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the agent.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13c0ee18c00618ce3d55cf861e88265d3db540867ff55146671310649d3ccaee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty",
        jsii_struct_bases=[],
        name_mapping={
            "code_configuration": "codeConfiguration",
            "container_configuration": "containerConfiguration",
        },
    )
    class AgentRuntimeArtifactProperty:
        def __init__(
            self,
            *,
            code_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.CodeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            container_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.ContainerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The artifact of the agent.

            :param code_configuration: Representation of a code configuration.
            :param container_configuration: Representation of a container configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-agentruntimeartifact.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                agent_runtime_artifact_property = bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                    code_configuration=bedrockagentcore.CfnRuntime.CodeConfigurationProperty(
                        code=bedrockagentcore.CfnRuntime.CodeProperty(
                            s3=bedrockagentcore.CfnRuntime.S3LocationProperty(
                                bucket="bucket",
                                prefix="prefix",
                
                                # the properties below are optional
                                version_id="versionId"
                            )
                        ),
                        entry_point=["entryPoint"],
                        runtime="runtime"
                    ),
                    container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                        container_uri="containerUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__51346444ae527a839c6fcfd4fd456eeea9b11da43bf9dadd9b152cfc716ecfd2)
                check_type(argname="argument code_configuration", value=code_configuration, expected_type=type_hints["code_configuration"])
                check_type(argname="argument container_configuration", value=container_configuration, expected_type=type_hints["container_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if code_configuration is not None:
                self._values["code_configuration"] = code_configuration
            if container_configuration is not None:
                self._values["container_configuration"] = container_configuration

        @builtins.property
        def code_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.CodeConfigurationProperty"]]:
            '''Representation of a code configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-agentruntimeartifact.html#cfn-bedrockagentcore-runtime-agentruntimeartifact-codeconfiguration
            '''
            result = self._values.get("code_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.CodeConfigurationProperty"]], result)

        @builtins.property
        def container_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.ContainerConfigurationProperty"]]:
            '''Representation of a container configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-agentruntimeartifact.html#cfn-bedrockagentcore-runtime-agentruntimeartifact-containerconfiguration
            '''
            result = self._values.get("container_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.ContainerConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AgentRuntimeArtifactProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_jwt_authorizer": "customJwtAuthorizer"},
    )
    class AuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            custom_jwt_authorizer: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.CustomJWTAuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The authorizer configuration.

            :param custom_jwt_authorizer: Represents inbound authorization configuration options used to authenticate incoming requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-authorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                authorizer_configuration_property = bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
                
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"],
                        allowed_scopes=["allowedScopes"],
                        custom_claims=[bedrockagentcore.CfnRuntime.CustomClaimValidationTypeProperty(
                            authorizing_claim_match_value=bedrockagentcore.CfnRuntime.AuthorizingClaimMatchValueTypeProperty(
                                claim_match_operator="claimMatchOperator",
                                claim_match_value=bedrockagentcore.CfnRuntime.ClaimMatchValueTypeProperty(
                                    match_value_string="matchValueString",
                                    match_value_string_list=["matchValueStringList"]
                                )
                            ),
                            inbound_token_claim_name="inboundTokenClaimName",
                            inbound_token_claim_value_type="inboundTokenClaimValueType"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bb18338480d08b211086521e0155635de6c3b54cf6ebbb5a7ee690c697991b4b)
                check_type(argname="argument custom_jwt_authorizer", value=custom_jwt_authorizer, expected_type=type_hints["custom_jwt_authorizer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_jwt_authorizer is not None:
                self._values["custom_jwt_authorizer"] = custom_jwt_authorizer

        @builtins.property
        def custom_jwt_authorizer(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.CustomJWTAuthorizerConfigurationProperty"]]:
            '''Represents inbound authorization configuration options used to authenticate incoming requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-authorizerconfiguration.html#cfn-bedrockagentcore-runtime-authorizerconfiguration-customjwtauthorizer
            '''
            result = self._values.get("custom_jwt_authorizer")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.CustomJWTAuthorizerConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.AuthorizingClaimMatchValueTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "claim_match_operator": "claimMatchOperator",
            "claim_match_value": "claimMatchValue",
        },
    )
    class AuthorizingClaimMatchValueTypeProperty:
        def __init__(
            self,
            *,
            claim_match_operator: builtins.str,
            claim_match_value: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.ClaimMatchValueTypeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The value or values in the custom claim to match and relationship of match.

            :param claim_match_operator: The relationship between the claim field value and the value or values being matched.
            :param claim_match_value: The value or values in the custom claim to match for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-authorizingclaimmatchvaluetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                authorizing_claim_match_value_type_property = bedrockagentcore.CfnRuntime.AuthorizingClaimMatchValueTypeProperty(
                    claim_match_operator="claimMatchOperator",
                    claim_match_value=bedrockagentcore.CfnRuntime.ClaimMatchValueTypeProperty(
                        match_value_string="matchValueString",
                        match_value_string_list=["matchValueStringList"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aec3caa15f03a36412929e5d8590d844c0a42d206d41633945c4edef06d42b12)
                check_type(argname="argument claim_match_operator", value=claim_match_operator, expected_type=type_hints["claim_match_operator"])
                check_type(argname="argument claim_match_value", value=claim_match_value, expected_type=type_hints["claim_match_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "claim_match_operator": claim_match_operator,
                "claim_match_value": claim_match_value,
            }

        @builtins.property
        def claim_match_operator(self) -> builtins.str:
            '''The relationship between the claim field value and the value or values being matched.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-authorizingclaimmatchvaluetype.html#cfn-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-claimmatchoperator
            '''
            result = self._values.get("claim_match_operator")
            assert result is not None, "Required property 'claim_match_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def claim_match_value(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRuntime.ClaimMatchValueTypeProperty"]:
            '''The value or values in the custom claim to match for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-authorizingclaimmatchvaluetype.html#cfn-bedrockagentcore-runtime-authorizingclaimmatchvaluetype-claimmatchvalue
            '''
            result = self._values.get("claim_match_value")
            assert result is not None, "Required property 'claim_match_value' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRuntime.ClaimMatchValueTypeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizingClaimMatchValueTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.ClaimMatchValueTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "match_value_string": "matchValueString",
            "match_value_string_list": "matchValueStringList",
        },
    )
    class ClaimMatchValueTypeProperty:
        def __init__(
            self,
            *,
            match_value_string: typing.Optional[builtins.str] = None,
            match_value_string_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The value or values in the custom claim to match for.

            :param match_value_string: The string value to match for.
            :param match_value_string_list: The list of strings to check for a match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-claimmatchvaluetype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                claim_match_value_type_property = bedrockagentcore.CfnRuntime.ClaimMatchValueTypeProperty(
                    match_value_string="matchValueString",
                    match_value_string_list=["matchValueStringList"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f1e5bed0c52ceaf858fa532930be858f1c52ad0f687c28a4365fff6aa1dde945)
                check_type(argname="argument match_value_string", value=match_value_string, expected_type=type_hints["match_value_string"])
                check_type(argname="argument match_value_string_list", value=match_value_string_list, expected_type=type_hints["match_value_string_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if match_value_string is not None:
                self._values["match_value_string"] = match_value_string
            if match_value_string_list is not None:
                self._values["match_value_string_list"] = match_value_string_list

        @builtins.property
        def match_value_string(self) -> typing.Optional[builtins.str]:
            '''The string value to match for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-claimmatchvaluetype.html#cfn-bedrockagentcore-runtime-claimmatchvaluetype-matchvaluestring
            '''
            result = self._values.get("match_value_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def match_value_string_list(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The list of strings to check for a match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-claimmatchvaluetype.html#cfn-bedrockagentcore-runtime-claimmatchvaluetype-matchvaluestringlist
            '''
            result = self._values.get("match_value_string_list")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ClaimMatchValueTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.CodeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "code": "code",
            "entry_point": "entryPoint",
            "runtime": "runtime",
        },
    )
    class CodeConfigurationProperty:
        def __init__(
            self,
            *,
            code: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.CodeProperty", typing.Dict[builtins.str, typing.Any]]],
            entry_point: typing.Sequence[builtins.str],
            runtime: builtins.str,
        ) -> None:
            '''Representation of a code configuration.

            :param code: Object represents source code from zip file.
            :param entry_point: List of entry points.
            :param runtime: Managed runtime types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-codeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                code_configuration_property = bedrockagentcore.CfnRuntime.CodeConfigurationProperty(
                    code=bedrockagentcore.CfnRuntime.CodeProperty(
                        s3=bedrockagentcore.CfnRuntime.S3LocationProperty(
                            bucket="bucket",
                            prefix="prefix",
                
                            # the properties below are optional
                            version_id="versionId"
                        )
                    ),
                    entry_point=["entryPoint"],
                    runtime="runtime"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f41e2d1a7603e72b05b2b9f19fd3ed1212f3de3311dceb488af789649eda5a1)
                check_type(argname="argument code", value=code, expected_type=type_hints["code"])
                check_type(argname="argument entry_point", value=entry_point, expected_type=type_hints["entry_point"])
                check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "code": code,
                "entry_point": entry_point,
                "runtime": runtime,
            }

        @builtins.property
        def code(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRuntime.CodeProperty"]:
            '''Object represents source code from zip file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-codeconfiguration.html#cfn-bedrockagentcore-runtime-codeconfiguration-code
            '''
            result = self._values.get("code")
            assert result is not None, "Required property 'code' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRuntime.CodeProperty"], result)

        @builtins.property
        def entry_point(self) -> typing.List[builtins.str]:
            '''List of entry points.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-codeconfiguration.html#cfn-bedrockagentcore-runtime-codeconfiguration-entrypoint
            '''
            result = self._values.get("entry_point")
            assert result is not None, "Required property 'entry_point' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def runtime(self) -> builtins.str:
            '''Managed runtime types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-codeconfiguration.html#cfn-bedrockagentcore-runtime-codeconfiguration-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.CodeProperty",
        jsii_struct_bases=[],
        name_mapping={"s3": "s3"},
    )
    class CodeProperty:
        def __init__(
            self,
            *,
            s3: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Object represents source code from zip file.

            :param s3: S3 Location Configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-code.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                code_property = bedrockagentcore.CfnRuntime.CodeProperty(
                    s3=bedrockagentcore.CfnRuntime.S3LocationProperty(
                        bucket="bucket",
                        prefix="prefix",
                
                        # the properties below are optional
                        version_id="versionId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__02b939e505c2d1d50e2de1a34b344b0803317afa1a475dde7482c11135e9ad61)
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3 is not None:
                self._values["s3"] = s3

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.S3LocationProperty"]]:
            '''S3 Location Configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-code.html#cfn-bedrockagentcore-runtime-code-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.S3LocationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.ContainerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"container_uri": "containerUri"},
    )
    class ContainerConfigurationProperty:
        def __init__(self, *, container_uri: builtins.str) -> None:
            '''The container configuration.

            :param container_uri: The container Uri.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-containerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                container_configuration_property = bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                    container_uri="containerUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0740ce1d3425c4e128b2f49784ee2a02ae6e81129ade5290d001575f4ecacb8)
                check_type(argname="argument container_uri", value=container_uri, expected_type=type_hints["container_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "container_uri": container_uri,
            }

        @builtins.property
        def container_uri(self) -> builtins.str:
            '''The container Uri.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-containerconfiguration.html#cfn-bedrockagentcore-runtime-containerconfiguration-containeruri
            '''
            result = self._values.get("container_uri")
            assert result is not None, "Required property 'container_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.CustomClaimValidationTypeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorizing_claim_match_value": "authorizingClaimMatchValue",
            "inbound_token_claim_name": "inboundTokenClaimName",
            "inbound_token_claim_value_type": "inboundTokenClaimValueType",
        },
    )
    class CustomClaimValidationTypeProperty:
        def __init__(
            self,
            *,
            authorizing_claim_match_value: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.AuthorizingClaimMatchValueTypeProperty", typing.Dict[builtins.str, typing.Any]]],
            inbound_token_claim_name: builtins.str,
            inbound_token_claim_value_type: builtins.str,
        ) -> None:
            '''Required custom claim.

            :param authorizing_claim_match_value: The value or values in the custom claim to match and relationship of match.
            :param inbound_token_claim_name: The name of the custom claim to validate.
            :param inbound_token_claim_value_type: Token claim data type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customclaimvalidationtype.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_claim_validation_type_property = bedrockagentcore.CfnRuntime.CustomClaimValidationTypeProperty(
                    authorizing_claim_match_value=bedrockagentcore.CfnRuntime.AuthorizingClaimMatchValueTypeProperty(
                        claim_match_operator="claimMatchOperator",
                        claim_match_value=bedrockagentcore.CfnRuntime.ClaimMatchValueTypeProperty(
                            match_value_string="matchValueString",
                            match_value_string_list=["matchValueStringList"]
                        )
                    ),
                    inbound_token_claim_name="inboundTokenClaimName",
                    inbound_token_claim_value_type="inboundTokenClaimValueType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__711e5e4ff145f76afd81911a3f92a921a0e7add7ab92dc4fe87d49ff367447dd)
                check_type(argname="argument authorizing_claim_match_value", value=authorizing_claim_match_value, expected_type=type_hints["authorizing_claim_match_value"])
                check_type(argname="argument inbound_token_claim_name", value=inbound_token_claim_name, expected_type=type_hints["inbound_token_claim_name"])
                check_type(argname="argument inbound_token_claim_value_type", value=inbound_token_claim_value_type, expected_type=type_hints["inbound_token_claim_value_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorizing_claim_match_value": authorizing_claim_match_value,
                "inbound_token_claim_name": inbound_token_claim_name,
                "inbound_token_claim_value_type": inbound_token_claim_value_type,
            }

        @builtins.property
        def authorizing_claim_match_value(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRuntime.AuthorizingClaimMatchValueTypeProperty"]:
            '''The value or values in the custom claim to match and relationship of match.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customclaimvalidationtype.html#cfn-bedrockagentcore-runtime-customclaimvalidationtype-authorizingclaimmatchvalue
            '''
            result = self._values.get("authorizing_claim_match_value")
            assert result is not None, "Required property 'authorizing_claim_match_value' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRuntime.AuthorizingClaimMatchValueTypeProperty"], result)

        @builtins.property
        def inbound_token_claim_name(self) -> builtins.str:
            '''The name of the custom claim to validate.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customclaimvalidationtype.html#cfn-bedrockagentcore-runtime-customclaimvalidationtype-inboundtokenclaimname
            '''
            result = self._values.get("inbound_token_claim_name")
            assert result is not None, "Required property 'inbound_token_claim_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def inbound_token_claim_value_type(self) -> builtins.str:
            '''Token claim data type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customclaimvalidationtype.html#cfn-bedrockagentcore-runtime-customclaimvalidationtype-inboundtokenclaimvaluetype
            '''
            result = self._values.get("inbound_token_claim_value_type")
            assert result is not None, "Required property 'inbound_token_claim_value_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomClaimValidationTypeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "discovery_url": "discoveryUrl",
            "allowed_audience": "allowedAudience",
            "allowed_clients": "allowedClients",
            "allowed_scopes": "allowedScopes",
            "custom_claims": "customClaims",
        },
    )
    class CustomJWTAuthorizerConfigurationProperty:
        def __init__(
            self,
            *,
            discovery_url: builtins.str,
            allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
            allowed_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
            custom_claims: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.CustomClaimValidationTypeProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration for custom JWT authorizer.

            :param discovery_url: The configuration authorization.
            :param allowed_audience: Represents inbound authorization configuration options used to authenticate incoming requests.
            :param allowed_clients: Represents individual client IDs that are validated in the incoming JWT token validation process.
            :param allowed_scopes: List of allowed scopes.
            :param custom_claims: List of required custom claims.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                custom_jWTAuthorizer_configuration_property = bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                    discovery_url="discoveryUrl",
                
                    # the properties below are optional
                    allowed_audience=["allowedAudience"],
                    allowed_clients=["allowedClients"],
                    allowed_scopes=["allowedScopes"],
                    custom_claims=[bedrockagentcore.CfnRuntime.CustomClaimValidationTypeProperty(
                        authorizing_claim_match_value=bedrockagentcore.CfnRuntime.AuthorizingClaimMatchValueTypeProperty(
                            claim_match_operator="claimMatchOperator",
                            claim_match_value=bedrockagentcore.CfnRuntime.ClaimMatchValueTypeProperty(
                                match_value_string="matchValueString",
                                match_value_string_list=["matchValueStringList"]
                            )
                        ),
                        inbound_token_claim_name="inboundTokenClaimName",
                        inbound_token_claim_value_type="inboundTokenClaimValueType"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6479ff33c6925aa85dcd6d4587cd46a0d073bd9992bb93c306d366f07cda2391)
                check_type(argname="argument discovery_url", value=discovery_url, expected_type=type_hints["discovery_url"])
                check_type(argname="argument allowed_audience", value=allowed_audience, expected_type=type_hints["allowed_audience"])
                check_type(argname="argument allowed_clients", value=allowed_clients, expected_type=type_hints["allowed_clients"])
                check_type(argname="argument allowed_scopes", value=allowed_scopes, expected_type=type_hints["allowed_scopes"])
                check_type(argname="argument custom_claims", value=custom_claims, expected_type=type_hints["custom_claims"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "discovery_url": discovery_url,
            }
            if allowed_audience is not None:
                self._values["allowed_audience"] = allowed_audience
            if allowed_clients is not None:
                self._values["allowed_clients"] = allowed_clients
            if allowed_scopes is not None:
                self._values["allowed_scopes"] = allowed_scopes
            if custom_claims is not None:
                self._values["custom_claims"] = custom_claims

        @builtins.property
        def discovery_url(self) -> builtins.str:
            '''The configuration authorization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-discoveryurl
            '''
            result = self._values.get("discovery_url")
            assert result is not None, "Required property 'discovery_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allowed_audience(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents inbound authorization configuration options used to authenticate incoming requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedaudience
            '''
            result = self._values.get("allowed_audience")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_clients(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents individual client IDs that are validated in the incoming JWT token validation process.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedclients
            '''
            result = self._values.get("allowed_clients")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allowed_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of allowed scopes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-allowedscopes
            '''
            result = self._values.get("allowed_scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def custom_claims(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnRuntime.CustomClaimValidationTypeProperty"]]]]:
            '''List of required custom claims.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-customjwtauthorizerconfiguration.html#cfn-bedrockagentcore-runtime-customjwtauthorizerconfiguration-customclaims
            '''
            result = self._values.get("custom_claims")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnRuntime.CustomClaimValidationTypeProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomJWTAuthorizerConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.LifecycleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "idle_runtime_session_timeout": "idleRuntimeSessionTimeout",
            "max_lifetime": "maxLifetime",
        },
    )
    class LifecycleConfigurationProperty:
        def __init__(
            self,
            *,
            idle_runtime_session_timeout: typing.Optional[jsii.Number] = None,
            max_lifetime: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration for managing the lifecycle of runtime sessions and resources.

            :param idle_runtime_session_timeout: Timeout in seconds for idle runtime sessions.
            :param max_lifetime: Maximum lifetime in seconds for runtime sessions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-lifecycleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                lifecycle_configuration_property = bedrockagentcore.CfnRuntime.LifecycleConfigurationProperty(
                    idle_runtime_session_timeout=123,
                    max_lifetime=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7dbc8b9876a11d54d81ef95ffe47ee5c649dfccb99ee31d9fba5b23defef9a4)
                check_type(argname="argument idle_runtime_session_timeout", value=idle_runtime_session_timeout, expected_type=type_hints["idle_runtime_session_timeout"])
                check_type(argname="argument max_lifetime", value=max_lifetime, expected_type=type_hints["max_lifetime"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if idle_runtime_session_timeout is not None:
                self._values["idle_runtime_session_timeout"] = idle_runtime_session_timeout
            if max_lifetime is not None:
                self._values["max_lifetime"] = max_lifetime

        @builtins.property
        def idle_runtime_session_timeout(self) -> typing.Optional[jsii.Number]:
            '''Timeout in seconds for idle runtime sessions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-lifecycleconfiguration.html#cfn-bedrockagentcore-runtime-lifecycleconfiguration-idleruntimesessiontimeout
            '''
            result = self._values.get("idle_runtime_session_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_lifetime(self) -> typing.Optional[jsii.Number]:
            '''Maximum lifetime in seconds for runtime sessions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-lifecycleconfiguration.html#cfn-bedrockagentcore-runtime-lifecycleconfiguration-maxlifetime
            '''
            result = self._values.get("max_lifetime")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecycleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_mode": "networkMode",
            "network_mode_config": "networkModeConfig",
        },
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            network_mode: builtins.str,
            network_mode_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The network configuration for the agent.

            :param network_mode: The network mode.
            :param network_mode_config: Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                network_configuration_property = bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(
                    network_mode="networkMode",
                
                    # the properties below are optional
                    network_mode_config=bedrockagentcore.CfnRuntime.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7ef3688e7eda46e5ab607f7c059dd5ed308816790e532f38188518d3a7c9b0f)
                check_type(argname="argument network_mode", value=network_mode, expected_type=type_hints["network_mode"])
                check_type(argname="argument network_mode_config", value=network_mode_config, expected_type=type_hints["network_mode_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_mode": network_mode,
            }
            if network_mode_config is not None:
                self._values["network_mode_config"] = network_mode_config

        @builtins.property
        def network_mode(self) -> builtins.str:
            '''The network mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-networkconfiguration.html#cfn-bedrockagentcore-runtime-networkconfiguration-networkmode
            '''
            result = self._values.get("network_mode")
            assert result is not None, "Required property 'network_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_mode_config(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.VpcConfigProperty"]]:
            '''Network mode configuration for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-networkconfiguration.html#cfn-bedrockagentcore-runtime-networkconfiguration-networkmodeconfig
            '''
            result = self._values.get("network_mode_config")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.VpcConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.RequestHeaderConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"request_header_allowlist": "requestHeaderAllowlist"},
    )
    class RequestHeaderConfigurationProperty:
        def __init__(
            self,
            *,
            request_header_allowlist: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration for HTTP request headers.

            :param request_header_allowlist: List of allowed HTTP headers for agent runtime requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-requestheaderconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                request_header_configuration_property = bedrockagentcore.CfnRuntime.RequestHeaderConfigurationProperty(
                    request_header_allowlist=["requestHeaderAllowlist"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e84a0bf594bf7173d323308d7c226c002caf3ffc7491c328dcd26a42c198c3e2)
                check_type(argname="argument request_header_allowlist", value=request_header_allowlist, expected_type=type_hints["request_header_allowlist"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if request_header_allowlist is not None:
                self._values["request_header_allowlist"] = request_header_allowlist

        @builtins.property
        def request_header_allowlist(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''List of allowed HTTP headers for agent runtime requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-requestheaderconfiguration.html#cfn-bedrockagentcore-runtime-requestheaderconfiguration-requestheaderallowlist
            '''
            result = self._values.get("request_header_allowlist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RequestHeaderConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "prefix": "prefix",
            "version_id": "versionId",
        },
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            prefix: builtins.str,
            version_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''S3 Location Configuration.

            :param bucket: S3 bucket name.
            :param prefix: S3 object key prefix.
            :param version_id: S3 object version ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                s3_location_property = bedrockagentcore.CfnRuntime.S3LocationProperty(
                    bucket="bucket",
                    prefix="prefix",
                
                    # the properties below are optional
                    version_id="versionId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7c4beadb07e8c6b725d20f4621457e58be14242062fb450da57aa4e91639c8f)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
                check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "prefix": prefix,
            }
            if version_id is not None:
                self._values["version_id"] = version_id

        @builtins.property
        def bucket(self) -> builtins.str:
            '''S3 bucket name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-s3location.html#cfn-bedrockagentcore-runtime-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def prefix(self) -> builtins.str:
            '''S3 object key prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-s3location.html#cfn-bedrockagentcore-runtime-s3location-prefix
            '''
            result = self._values.get("prefix")
            assert result is not None, "Required property 'prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version_id(self) -> typing.Optional[builtins.str]:
            '''S3 object version ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-s3location.html#cfn-bedrockagentcore-runtime-s3location-versionid
            '''
            result = self._values.get("version_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"security_groups": "securityGroups", "subnets": "subnets"},
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_groups: typing.Sequence[builtins.str],
            subnets: typing.Sequence[builtins.str],
        ) -> None:
            '''Network mode configuration for VPC.

            :param security_groups: Security groups for VPC.
            :param subnets: Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                vpc_config_property = bedrockagentcore.CfnRuntime.VpcConfigProperty(
                    security_groups=["securityGroups"],
                    subnets=["subnets"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3e546c3d4da6e03e6ff8e890d2d32819d3e7c17149a4f17d0e75c9569fa3aad9)
                check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
                check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_groups": security_groups,
                "subnets": subnets,
            }

        @builtins.property
        def security_groups(self) -> typing.List[builtins.str]:
            '''Security groups for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-vpcconfig.html#cfn-bedrockagentcore-runtime-vpcconfig-securitygroups
            '''
            result = self._values.get("security_groups")
            assert result is not None, "Required property 'security_groups' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnets(self) -> typing.List[builtins.str]:
            '''Subnets for VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-vpcconfig.html#cfn-bedrockagentcore-runtime-vpcconfig-subnets
            '''
            result = self._values.get("subnets")
            assert result is not None, "Required property 'subnets' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntime.WorkloadIdentityDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"workload_identity_arn": "workloadIdentityArn"},
    )
    class WorkloadIdentityDetailsProperty:
        def __init__(self, *, workload_identity_arn: builtins.str) -> None:
            '''The workload identity details for the agent.

            :param workload_identity_arn: The Amazon Resource Name (ARN) for the workload identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-workloadidentitydetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_bedrockagentcore as bedrockagentcore
                
                workload_identity_details_property = bedrockagentcore.CfnRuntime.WorkloadIdentityDetailsProperty(
                    workload_identity_arn="workloadIdentityArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68380bfa2496b392a6192eeab7bae5b15e67d93a4946dff9481dca7e2b9da401)
                check_type(argname="argument workload_identity_arn", value=workload_identity_arn, expected_type=type_hints["workload_identity_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "workload_identity_arn": workload_identity_arn,
            }

        @builtins.property
        def workload_identity_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) for the workload identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-bedrockagentcore-runtime-workloadidentitydetails.html#cfn-bedrockagentcore-runtime-workloadidentitydetails-workloadidentityarn
            '''
            result = self._values.get("workload_identity_arn")
            assert result is not None, "Required property 'workload_identity_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkloadIdentityDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _IRuntimeEndpointRef_7a1c67f8, _ITaggableV2_4e6798f8)
class CfnRuntimeEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntimeEndpoint",
):
    '''AgentCore Runtime is a secure, serverless runtime purpose-built for deploying and scaling dynamic AI agents and tools using any open-source framework including LangGraph, CrewAI, and Strands Agents, any protocol, and any model.

    For more information about using agent runtime endpoints in Amazon Bedrock AgentCore, see `AgentCore Runtime versioning and endpoints <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agent-runtime-versioning.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html
    :cloudformationResource: AWS::BedrockAgentCore::RuntimeEndpoint
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_runtime_endpoint = bedrockagentcore.CfnRuntimeEndpoint(self, "MyCfnRuntimeEndpoint",
            agent_runtime_id="agentRuntimeId",
            name="name",
        
            # the properties below are optional
            agent_runtime_version="agentRuntimeVersion",
            description="description",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        agent_runtime_id: builtins.str,
        name: builtins.str,
        agent_runtime_version: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::RuntimeEndpoint``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param agent_runtime_id: The agent runtime ID.
        :param name: The name of the AgentCore Runtime endpoint.
        :param agent_runtime_version: The version of the agent.
        :param description: Contains information about an agent runtime endpoint. An agent runtime is the execution environment for a Amazon Bedrock Agent.
        :param tags: The tags for the AgentCore Runtime endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f889c0edf8dd4715192bf69e6433f02f671ca35ed9b8e8f7622b298a7b14955a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRuntimeEndpointProps(
            agent_runtime_id=agent_runtime_id,
            name=name,
            agent_runtime_version=agent_runtime_version,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnRuntimeEndpoint")
    @builtins.classmethod
    def is_cfn_runtime_endpoint(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnRuntimeEndpoint.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__817ffbdbbe724c4d150b381c3527e3473cdef2580396b28edcec84f8ca910c17)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnRuntimeEndpoint", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e6a578bb33afa13fb1d85d1b682fc96e67f21a5fb168de296365084e02f261)
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
            type_hints = typing.get_type_hints(_typecheckingstub__91be73ce07416705255e5e1569db31b3f488f1376320ddae8d8803981071f602)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeArn")
    def attr_agent_runtime_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the runtime agent.

        :cloudformationAttribute: AgentRuntimeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAgentRuntimeEndpointArn")
    def attr_agent_runtime_endpoint_arn(self) -> builtins.str:
        '''The endpoint Amazon Resource Name (ARN).

        :cloudformationAttribute: AgentRuntimeEndpointArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgentRuntimeEndpointArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The time at which the endpoint was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''The reason for failure if the memory is in a failed state.

        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the runtime endpoint.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedAt")
    def attr_last_updated_at(self) -> builtins.str:
        '''The time at which the endpoint was last updated.

        :cloudformationAttribute: LastUpdatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLastUpdatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrLiveVersion")
    def attr_live_version(self) -> builtins.str:
        '''The live version for the runtime endpoint.

        :cloudformationAttribute: LiveVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLiveVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the runtime endpoint.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrTargetVersion")
    def attr_target_version(self) -> builtins.str:
        '''The target version.

        :cloudformationAttribute: TargetVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTargetVersion"))

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
    @jsii.member(jsii_name="runtimeEndpointRef")
    def runtime_endpoint_ref(self) -> "_RuntimeEndpointReference_dff8b038":
        '''A reference to a RuntimeEndpoint resource.'''
        return typing.cast("_RuntimeEndpointReference_dff8b038", jsii.get(self, "runtimeEndpointRef"))

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeId")
    def agent_runtime_id(self) -> builtins.str:
        '''The agent runtime ID.'''
        return typing.cast(builtins.str, jsii.get(self, "agentRuntimeId"))

    @agent_runtime_id.setter
    def agent_runtime_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ceb50df9e5593b49d2fbdc6aac8e77c6be9322ee82ceea79d7d86478e1a9d74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the AgentCore Runtime endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f380de6caf6e91bd3b0399e46b356f219d19dd4297d832ed74437f4653be82c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="agentRuntimeVersion")
    def agent_runtime_version(self) -> typing.Optional[builtins.str]:
        '''The version of the agent.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "agentRuntimeVersion"))

    @agent_runtime_version.setter
    def agent_runtime_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45c0052c9218918d9940523a8d7f016f7eaf5fe73a714ee05b2ba7a94aa9df9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "agentRuntimeVersion", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Contains information about an agent runtime endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479a4b8aa6bb0db70941c7bc7a41e153fdbf533d62d2c2dc2ae2edf57fb46e99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the AgentCore Runtime endpoint.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1df913b08f181c8777324479d4caab3dc1c0e41137ac1db4a0b10f478ad63ce7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntimeEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_runtime_id": "agentRuntimeId",
        "name": "name",
        "agent_runtime_version": "agentRuntimeVersion",
        "description": "description",
        "tags": "tags",
    },
)
class CfnRuntimeEndpointProps:
    def __init__(
        self,
        *,
        agent_runtime_id: builtins.str,
        name: builtins.str,
        agent_runtime_version: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuntimeEndpoint``.

        :param agent_runtime_id: The agent runtime ID.
        :param name: The name of the AgentCore Runtime endpoint.
        :param agent_runtime_version: The version of the agent.
        :param description: Contains information about an agent runtime endpoint. An agent runtime is the execution environment for a Amazon Bedrock Agent.
        :param tags: The tags for the AgentCore Runtime endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_runtime_endpoint_props = bedrockagentcore.CfnRuntimeEndpointProps(
                agent_runtime_id="agentRuntimeId",
                name="name",
            
                # the properties below are optional
                agent_runtime_version="agentRuntimeVersion",
                description="description",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03746d507f3e8e95afbebc436c73d1ac1fc643ccea60f817b99b76cb41ccf5fb)
            check_type(argname="argument agent_runtime_id", value=agent_runtime_id, expected_type=type_hints["agent_runtime_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument agent_runtime_version", value=agent_runtime_version, expected_type=type_hints["agent_runtime_version"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_runtime_id": agent_runtime_id,
            "name": name,
        }
        if agent_runtime_version is not None:
            self._values["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_runtime_id(self) -> builtins.str:
        '''The agent runtime ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-agentruntimeid
        '''
        result = self._values.get("agent_runtime_id")
        assert result is not None, "Required property 'agent_runtime_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the AgentCore Runtime endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def agent_runtime_version(self) -> typing.Optional[builtins.str]:
        '''The version of the agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-agentruntimeversion
        '''
        result = self._values.get("agent_runtime_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Contains information about an agent runtime endpoint.

        An agent runtime is the execution environment for a Amazon Bedrock Agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the AgentCore Runtime endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtimeendpoint.html#cfn-bedrockagentcore-runtimeendpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuntimeEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnRuntimeProps",
    jsii_struct_bases=[],
    name_mapping={
        "agent_runtime_artifact": "agentRuntimeArtifact",
        "agent_runtime_name": "agentRuntimeName",
        "network_configuration": "networkConfiguration",
        "role_arn": "roleArn",
        "authorizer_configuration": "authorizerConfiguration",
        "description": "description",
        "environment_variables": "environmentVariables",
        "lifecycle_configuration": "lifecycleConfiguration",
        "protocol_configuration": "protocolConfiguration",
        "request_header_configuration": "requestHeaderConfiguration",
        "tags": "tags",
    },
)
class CfnRuntimeProps:
    def __init__(
        self,
        *,
        agent_runtime_artifact: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.AgentRuntimeArtifactProperty", typing.Dict[builtins.str, typing.Any]]],
        agent_runtime_name: builtins.str,
        network_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        authorizer_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.AuthorizerConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]] = None,
        lifecycle_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.LifecycleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        protocol_configuration: typing.Optional[builtins.str] = None,
        request_header_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRuntime.RequestHeaderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRuntime``.

        :param agent_runtime_artifact: The artifact of the agent.
        :param agent_runtime_name: The name of the AgentCore Runtime endpoint.
        :param network_configuration: The network configuration.
        :param role_arn: The Amazon Resource Name (ARN) for for the role.
        :param authorizer_configuration: Represents inbound authorization configuration options used to authenticate incoming requests.
        :param description: The agent runtime description.
        :param environment_variables: The environment variables for the agent.
        :param lifecycle_configuration: Configuration for managing the lifecycle of runtime sessions and resources.
        :param protocol_configuration: The protocol configuration for an agent runtime. This structure defines how the agent runtime communicates with clients.
        :param request_header_configuration: Configuration for HTTP request headers.
        :param tags: The tags for the agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_runtime_props = bedrockagentcore.CfnRuntimeProps(
                agent_runtime_artifact=bedrockagentcore.CfnRuntime.AgentRuntimeArtifactProperty(
                    code_configuration=bedrockagentcore.CfnRuntime.CodeConfigurationProperty(
                        code=bedrockagentcore.CfnRuntime.CodeProperty(
                            s3=bedrockagentcore.CfnRuntime.S3LocationProperty(
                                bucket="bucket",
                                prefix="prefix",
            
                                # the properties below are optional
                                version_id="versionId"
                            )
                        ),
                        entry_point=["entryPoint"],
                        runtime="runtime"
                    ),
                    container_configuration=bedrockagentcore.CfnRuntime.ContainerConfigurationProperty(
                        container_uri="containerUri"
                    )
                ),
                agent_runtime_name="agentRuntimeName",
                network_configuration=bedrockagentcore.CfnRuntime.NetworkConfigurationProperty(
                    network_mode="networkMode",
            
                    # the properties below are optional
                    network_mode_config=bedrockagentcore.CfnRuntime.VpcConfigProperty(
                        security_groups=["securityGroups"],
                        subnets=["subnets"]
                    )
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                authorizer_configuration=bedrockagentcore.CfnRuntime.AuthorizerConfigurationProperty(
                    custom_jwt_authorizer=bedrockagentcore.CfnRuntime.CustomJWTAuthorizerConfigurationProperty(
                        discovery_url="discoveryUrl",
            
                        # the properties below are optional
                        allowed_audience=["allowedAudience"],
                        allowed_clients=["allowedClients"],
                        allowed_scopes=["allowedScopes"],
                        custom_claims=[bedrockagentcore.CfnRuntime.CustomClaimValidationTypeProperty(
                            authorizing_claim_match_value=bedrockagentcore.CfnRuntime.AuthorizingClaimMatchValueTypeProperty(
                                claim_match_operator="claimMatchOperator",
                                claim_match_value=bedrockagentcore.CfnRuntime.ClaimMatchValueTypeProperty(
                                    match_value_string="matchValueString",
                                    match_value_string_list=["matchValueStringList"]
                                )
                            ),
                            inbound_token_claim_name="inboundTokenClaimName",
                            inbound_token_claim_value_type="inboundTokenClaimValueType"
                        )]
                    )
                ),
                description="description",
                environment_variables={
                    "environment_variables_key": "environmentVariables"
                },
                lifecycle_configuration=bedrockagentcore.CfnRuntime.LifecycleConfigurationProperty(
                    idle_runtime_session_timeout=123,
                    max_lifetime=123
                ),
                protocol_configuration="protocolConfiguration",
                request_header_configuration=bedrockagentcore.CfnRuntime.RequestHeaderConfigurationProperty(
                    request_header_allowlist=["requestHeaderAllowlist"]
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e489b12cef85647a902e6bba6db3bf5f3ef1a856b74cf0fc5a7f8d1d0fa4a4b)
            check_type(argname="argument agent_runtime_artifact", value=agent_runtime_artifact, expected_type=type_hints["agent_runtime_artifact"])
            check_type(argname="argument agent_runtime_name", value=agent_runtime_name, expected_type=type_hints["agent_runtime_name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument authorizer_configuration", value=authorizer_configuration, expected_type=type_hints["authorizer_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument lifecycle_configuration", value=lifecycle_configuration, expected_type=type_hints["lifecycle_configuration"])
            check_type(argname="argument protocol_configuration", value=protocol_configuration, expected_type=type_hints["protocol_configuration"])
            check_type(argname="argument request_header_configuration", value=request_header_configuration, expected_type=type_hints["request_header_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "agent_runtime_artifact": agent_runtime_artifact,
            "agent_runtime_name": agent_runtime_name,
            "network_configuration": network_configuration,
            "role_arn": role_arn,
        }
        if authorizer_configuration is not None:
            self._values["authorizer_configuration"] = authorizer_configuration
        if description is not None:
            self._values["description"] = description
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if lifecycle_configuration is not None:
            self._values["lifecycle_configuration"] = lifecycle_configuration
        if protocol_configuration is not None:
            self._values["protocol_configuration"] = protocol_configuration
        if request_header_configuration is not None:
            self._values["request_header_configuration"] = request_header_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def agent_runtime_artifact(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnRuntime.AgentRuntimeArtifactProperty"]:
        '''The artifact of the agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-agentruntimeartifact
        '''
        result = self._values.get("agent_runtime_artifact")
        assert result is not None, "Required property 'agent_runtime_artifact' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRuntime.AgentRuntimeArtifactProperty"], result)

    @builtins.property
    def agent_runtime_name(self) -> builtins.str:
        '''The name of the AgentCore Runtime endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-agentruntimename
        '''
        result = self._values.get("agent_runtime_name")
        assert result is not None, "Required property 'agent_runtime_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnRuntime.NetworkConfigurationProperty"]:
        '''The network configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        assert result is not None, "Required property 'network_configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRuntime.NetworkConfigurationProperty"], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for for the role.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.AuthorizerConfigurationProperty"]]:
        '''Represents inbound authorization configuration options used to authenticate incoming requests.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-authorizerconfiguration
        '''
        result = self._values.get("authorizer_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.AuthorizerConfigurationProperty"]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The agent runtime description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]]:
        '''The environment variables for the agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-environmentvariables
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]], result)

    @builtins.property
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.LifecycleConfigurationProperty"]]:
        '''Configuration for managing the lifecycle of runtime sessions and resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-lifecycleconfiguration
        '''
        result = self._values.get("lifecycle_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.LifecycleConfigurationProperty"]], result)

    @builtins.property
    def protocol_configuration(self) -> typing.Optional[builtins.str]:
        '''The protocol configuration for an agent runtime.

        This structure defines how the agent runtime communicates with clients.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-protocolconfiguration
        '''
        result = self._values.get("protocol_configuration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_header_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.RequestHeaderConfigurationProperty"]]:
        '''Configuration for HTTP request headers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-requestheaderconfiguration
        '''
        result = self._values.get("request_header_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRuntime.RequestHeaderConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The tags for the agent.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-runtime.html#cfn-bedrockagentcore-runtime-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRuntimeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IWorkloadIdentityRef_dc6077a7, _ITaggableV2_4e6798f8)
class CfnWorkloadIdentity(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnWorkloadIdentity",
):
    '''Creates a workload identity for Amazon Bedrock AgentCore.

    A workload identity provides OAuth2-based authentication for resources associated with agent runtimes.

    For more information about using workload identities in Amazon Bedrock AgentCore, see `Managing workload identities <https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/workload-identity.html>`_ .

    See the *Properties* section below for descriptions of both the required and optional properties.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-workloadidentity.html
    :cloudformationResource: AWS::BedrockAgentCore::WorkloadIdentity
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_bedrockagentcore as bedrockagentcore
        
        cfn_workload_identity = bedrockagentcore.CfnWorkloadIdentity(self, "MyCfnWorkloadIdentity",
            name="name",
        
            # the properties below are optional
            allowed_resource_oauth2_return_urls=["allowedResourceOauth2ReturnUrls"],
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
        name: builtins.str,
        allowed_resource_oauth2_return_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::BedrockAgentCore::WorkloadIdentity``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the workload identity. The name must be unique within your account.
        :param allowed_resource_oauth2_return_urls: The list of allowed OAuth2 return URLs for resources associated with this workload identity.
        :param tags: The tags for the workload identity.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09a8e6f0ae71da08ac7a3937e8dcaa170d25c76feb84006a0b53e9e688f16c17)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkloadIdentityProps(
            name=name,
            allowed_resource_oauth2_return_urls=allowed_resource_oauth2_return_urls,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForWorkloadIdentity")
    @builtins.classmethod
    def arn_for_workload_identity(
        cls,
        resource: "_IWorkloadIdentityRef_dc6077a7",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d17bbc0e09dbed545a31bdb5536b2bc6164ac952e9964c0b9fb5b066c0ad1639)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForWorkloadIdentity", [resource]))

    @jsii.member(jsii_name="isCfnWorkloadIdentity")
    @builtins.classmethod
    def is_cfn_workload_identity(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnWorkloadIdentity.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc71f5a7a0caee1d1f13462070b832ea0f00bf8762d51e41cb3870cc836ef87b)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnWorkloadIdentity", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__766a926b6ea4d718606dac6820c9d33d069b4c27a0844ba0d55f325ade157e6c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__488009317eeca5f98d0be9fbcd30e71ec79ca306a6ab22b48b1feab3c04d0f94)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedTime")
    def attr_created_time(self) -> "_IResolvable_da3f097b":
        '''The timestamp when the workload identity was created.

        :cloudformationAttribute: CreatedTime
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrCreatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastUpdatedTime")
    def attr_last_updated_time(self) -> "_IResolvable_da3f097b":
        '''The timestamp when the workload identity was last updated.

        :cloudformationAttribute: LastUpdatedTime
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrLastUpdatedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkloadIdentityArn")
    def attr_workload_identity_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the workload identity.

        :cloudformationAttribute: WorkloadIdentityArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkloadIdentityArn"))

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
    @jsii.member(jsii_name="workloadIdentityRef")
    def workload_identity_ref(self) -> "_WorkloadIdentityReference_255b3126":
        '''A reference to a WorkloadIdentity resource.'''
        return typing.cast("_WorkloadIdentityReference_255b3126", jsii.get(self, "workloadIdentityRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the workload identity.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46dd6904ea9e85082bdbdcd42c00d119b0b4a4f43c5b3a1f5c273c0eb5d89289)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="allowedResourceOauth2ReturnUrls")
    def allowed_resource_oauth2_return_urls(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of allowed OAuth2 return URLs for resources associated with this workload identity.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedResourceOauth2ReturnUrls"))

    @allowed_resource_oauth2_return_urls.setter
    def allowed_resource_oauth2_return_urls(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b3780d06fd0cd5b35919591809dff38c541131cad0233fc83e2f1a65e282dc8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedResourceOauth2ReturnUrls", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags for the workload identity.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d24890b8ce488c10d666570acfa91e9c0c2c358e35cc3bbad1ef37fc9bad1869)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_bedrockagentcore.CfnWorkloadIdentityProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "allowed_resource_oauth2_return_urls": "allowedResourceOauth2ReturnUrls",
        "tags": "tags",
    },
)
class CfnWorkloadIdentityProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        allowed_resource_oauth2_return_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkloadIdentity``.

        :param name: The name of the workload identity. The name must be unique within your account.
        :param allowed_resource_oauth2_return_urls: The list of allowed OAuth2 return URLs for resources associated with this workload identity.
        :param tags: The tags for the workload identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-workloadidentity.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_bedrockagentcore as bedrockagentcore
            
            cfn_workload_identity_props = bedrockagentcore.CfnWorkloadIdentityProps(
                name="name",
            
                # the properties below are optional
                allowed_resource_oauth2_return_urls=["allowedResourceOauth2ReturnUrls"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5358b1efbb0f18624add0a9e7d27cb517f7d9ceed952fcd31225012dfd0e89c6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument allowed_resource_oauth2_return_urls", value=allowed_resource_oauth2_return_urls, expected_type=type_hints["allowed_resource_oauth2_return_urls"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if allowed_resource_oauth2_return_urls is not None:
            self._values["allowed_resource_oauth2_return_urls"] = allowed_resource_oauth2_return_urls
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the workload identity.

        The name must be unique within your account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-workloadidentity.html#cfn-bedrockagentcore-workloadidentity-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allowed_resource_oauth2_return_urls(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of allowed OAuth2 return URLs for resources associated with this workload identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-workloadidentity.html#cfn-bedrockagentcore-workloadidentity-allowedresourceoauth2returnurls
        '''
        result = self._values.get("allowed_resource_oauth2_return_urls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags for the workload identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-bedrockagentcore-workloadidentity.html#cfn-bedrockagentcore-workloadidentity-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkloadIdentityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBrowserCustom",
    "CfnBrowserCustomProps",
    "CfnBrowserProfile",
    "CfnBrowserProfileProps",
    "CfnCodeInterpreterCustom",
    "CfnCodeInterpreterCustomProps",
    "CfnEvaluator",
    "CfnEvaluatorProps",
    "CfnGateway",
    "CfnGatewayProps",
    "CfnGatewayTarget",
    "CfnGatewayTargetProps",
    "CfnMemory",
    "CfnMemoryProps",
    "CfnOnlineEvaluationConfig",
    "CfnOnlineEvaluationConfigProps",
    "CfnPolicy",
    "CfnPolicyEngine",
    "CfnPolicyEngineProps",
    "CfnPolicyProps",
    "CfnRuntime",
    "CfnRuntimeEndpoint",
    "CfnRuntimeEndpointProps",
    "CfnRuntimeProps",
    "CfnWorkloadIdentity",
    "CfnWorkloadIdentityProps",
]

publication.publish()

def _typecheckingstub__e817ad5ee6496ab54cf569758c4d73da62a4d6f5cf0c34866960f6e4677343e1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.BrowserNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    browser_signing: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.BrowserSigningProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.RecordingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3938521d3e1fa00869a698ba3a1fa8867e2077f1c510f1bd54cf729929cc8448(
    resource: _IBrowserCustomRef_f12bfa35,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd42b7f7bd38d71e50eb92224f822287bc042051c2eb613dcae193e1e3cb986c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a5d38dc7619d36a2a4f39c13ec237b55f560a41ac9a162b787880e8e6ba2f47(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    browser_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b61de9c51c69f66cbc156b98a64f55d58e5c07baf4719635d93d5421943cf1cc(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12637c5685b21eb50c5acd05eb9308d8266fc2816549a6a2816d9399823e8551(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14f4b2516dbe32242e98828488dc4abcc900e39ac20507ae2fd0d16a3a0457c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7c7dc0414899a74bed53146d246f036f214f82b031723849419726e12bcee67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89dfccc35ccd0a377234eb3e008038ad66200df7a4f3c63bf61ebf273a7f42e(
    value: typing.Union[_IResolvable_da3f097b, CfnBrowserCustom.BrowserNetworkConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81fba2b1346993fe8f90531b960f456b9bae96a895915ce3c4c9fa5127ad0a23(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBrowserCustom.BrowserSigningProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d16faa304c4f18b8bba1ee70b209c47d9944346a1e88926b4ee4ea5fe723fd64(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dd292342e1165d23c8ce68a72d30c745d42a2586b394e8bcb4aa1ec13e9cc74(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__089c5a25d69d7c7abf4193f45206b584472351088cbe92835bb014923a48f2e7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBrowserCustom.RecordingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22e813ff9c64c23f175682396c7a13b02b9193809d3629b73f2ecac10192c8c2(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0d5bebf1ad5159cc9014318eaa4c540145c82225bd9e29170035b0a29d0ee07(
    *,
    network_mode: builtins.str,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e53c5d43f81573d2efdf7d45e9c80191cee07ad5d1b9262ad41ee43c45059d9(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__754929ea2dabad59807821380b38b3ef1b1955a5473f5469b18a7dcc81600948(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6787b09f9e077c274ab79cdf45ea5157eec8aea8960e77f8e128fab67b3cbc26(
    *,
    bucket: builtins.str,
    prefix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46efbe5ee20e23cd9dc9ee29c1cd041e741b8a0aeb2c0ea76ed3cb6cab180dad(
    *,
    security_groups: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08f9adb5e20b52bbdc47438decbd54e3ebb4b1976cbf46432a19597fc6589c39(
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.BrowserNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    browser_signing: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.BrowserSigningProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    recording_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBrowserCustom.RecordingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7473f1faa9bfc03705a3d4572354312e5dd4b5bb47ae1b3a9a2ca09618c09558(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdecc7ab99fa67b91a7bb897ed0d5da420e0fc98db0e44fb43c5e4573c36e7a2(
    resource: _IBrowserProfileRef_87a4b1a8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ade26e9a57cff73b5718f778b22e6e84dde0ded65b13a8b5acef370b2ee67804(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5babb21bf2a8458092196b97ee681b85e69bab2ae47419298b051be21a395742(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ccc42c3721a989048610856613cdee96f1a401698e93e9abda9a99b25f14f3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae6651c726fc48203e39af1e8661928e84a4323ff2a0d8a55574653b31bf76d0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1b17f49e9d7bf2a0d0045e14abceca289c01f8a4b4a4f70e5297e2aa8cef7d3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6885ed668d838f82c9f283a9d7037bb9609ab538bb3bce79981a0e79df9f52b6(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06ddbf18be8902484b8315b3f45a334e6e9cddb8b83448c8197da614062d18ee(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aaa167a6af98d626969b5bd2de9377658de4e8d04df0b48dc5916f9e503a029(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__975674ea4f6bb8a0c20e661871dd773f758b19950b1cf17839dc6587ebb65590(
    resource: _ICodeInterpreterCustomRef_2d5c05fb,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdf8490c04291f6972f1dc00b876398eb5886b19291a588f52fdbb4fc2e4e156(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e6193c6a8378455a4decc0c525a09a78674fd7ad426e58017e57035bc1789a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    code_interpreter_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__510c722b77a53a3aba328ff9805ff6391701fb5ea56c15887eebad76692d70a0(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab4b7a28e87b1af264773dfddc0e9da46bb99c921aa85fb942fcc7ca03680597(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf6d68ae9ee508df2d25ca9f4fa9a800c1215c05ac37929135ce20e393a44113(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c58fa8bcb0ec87d3b6f75396018d3eeff06205adbf6ade289f0ac1710d71c909(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a36911cef74e5cac559eb0b558b639739fba4dccbbc8a224553a0f0a0cace3cd(
    value: typing.Union[_IResolvable_da3f097b, CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f33607ff407017e2c7ecefbc727c6f7660550a46fe6b356799810d75ccf8d662(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597443cc8b5cdaed2db807a1545702d23f8f925435f13cd3d17111236aba2428(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__466065bbc5e5f3997568d60c567b51bbc4a9a4900e6ce6da9f9499f85329a3a4(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae1295735d5d0996afa02b88ef9dddbd193fc77b25f7b69433fd57c1240bb3a(
    *,
    network_mode: builtins.str,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeInterpreterCustom.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97c8e6007d5911afbd85662033d4936d1846dbfdc6caa2fb2e69de26653ccc32(
    *,
    security_groups: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b5217aa9ccd0ec964b92c3a48855bb1494914c435606fcee5b0faefd790d264(
    *,
    name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCodeInterpreterCustom.CodeInterpreterNetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    execution_role_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__141b6fd05e9e051e0fb07fbc9903cbc471c6f95bd2ce599524db7f08eb59d089(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    evaluator_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluator.EvaluatorConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    evaluator_name: builtins.str,
    level: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2241f7871310f76bc950be554b9e50e0182d60385049f460dfd13459d3e0757(
    resource: _IEvaluatorRef_21d364d2,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24f5b2764d1f145a52271003ddf7f12ab5fc8df06fcd5d57f8407543371dd7cc(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e88dc5c3acd247cf0c5817871be6840db2e01fa9976082dea7654fb298e73dd3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a74e1010c78d5affb59aa69c26b246dc322ef02ba3fe68b5cafecce92faa0934(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d85156d59d54c7ee85e1018a2dbc04869c0befafd49c7f39bed6f8bdf1c0e7c0(
    value: typing.Union[_IResolvable_da3f097b, CfnEvaluator.EvaluatorConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fb35f2e87b3efb7648fbd87d13f3e5ff4e7e4f353ccab015439c65775fa4f4e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5ba897fceb746066253f02e4acaa94a0805d38e5dd7eb06a70ada74a5171c7c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9476feb3976d508ab93e23993f8958690b378207ccac9c804c8644598ec4e9d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9be07f5133cae95a44b8c1e5e5925d27341ddb21585adfa558cf87a9d4ed266(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e685cb926c5b55ad4c85e5270f7d5645516c749d48c98cdcd779d7548a53c95f(
    *,
    model_id: builtins.str,
    additional_model_request_fields: typing.Any = None,
    inference_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluator.InferenceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0138c4dab895be263ca856078c54d7f7dc17e4a1e5fa14530ef199b887cb5326(
    *,
    definition: builtins.str,
    label: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68fedf7916817af17038fada535f709885d9e4602b0228fd6e545877cc7a08c4(
    *,
    llm_as_a_judge: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluator.LlmAsAJudgeEvaluatorConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e199bbf333dd5891de717038547bcf88b9e5114ac6040f7d31e54c8cb0f17f02(
    *,
    bedrock_evaluator_model_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluator.BedrockEvaluatorModelConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe32f79956eba54fe76f4cfd3e9550d9001beda9560e6f4c55b2f8ab94aa98c2(
    *,
    max_tokens: typing.Optional[jsii.Number] = None,
    temperature: typing.Optional[jsii.Number] = None,
    top_p: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28079328036f363d453150c70a76fbc17cbd2c7dab0942689bd59b9411b642a(
    *,
    instructions: builtins.str,
    model_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluator.EvaluatorModelConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    rating_scale: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluator.RatingScaleProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e284be9755c11642d2b6734206454332b1166d2726612dba743e01c1a4f1a83(
    *,
    definition: builtins.str,
    label: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b52b8f960640a8f01b882a7550bb6dcc23bf2b1121733ac830f9f26c80b3027(
    *,
    categorical: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluator.CategoricalScaleDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    numerical: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluator.NumericalScaleDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c769c32f0049d1195b80f5b76b8b678dcf5ad1c67ed7fa7571832bf6792ef2f3(
    *,
    evaluator_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnEvaluator.EvaluatorConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    evaluator_name: builtins.str,
    level: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__718d4d7128ca57b0228b268f1204c5574e63e51d4e7701a53fd67a1e8ec17c63(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authorizer_type: builtins.str,
    name: builtins.str,
    protocol_type: builtins.str,
    role_arn: builtins.str,
    authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    exception_level: typing.Optional[builtins.str] = None,
    interceptor_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayInterceptorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    protocol_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayProtocolConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c4c1faa26b1254e7e81bc3fba266c51f8b0763206acf1eb473d1904042a366e(
    resource: _IGatewayRef_a3ed30fe,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f42a0d18f9ffc74f0e48860c5e4ddcf51e6d14b3b472636555bf41fbb6963f3(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1253940d92e3f35d08808461458766f65528b0878c674311aabd74aa0a76ce30(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67e1eb8798612291b5b13aae1ac0d9cb4513c21df38593628be4d5e2fe660886(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3733b65f293d2d9f1304c9c6a4cfd4c4aa4a9dca54f65a221b403a9fa85809d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faac8d45eefa612f06e0139bc26af7005d13df5a552a63d10084bfbc444fd266(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d2ccf9c2c13ca5a79d82fee59155dfbaa87d3d17ccc1f27959c635732127d90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a750b424a29fb58f4f0dcc52028237d740f0b0b92d8420600048da5b20537f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c34ffb86639149c1c6323ad6aa1ec7b9f7d9e7f17a5f5306e5d67d30110ba83(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGateway.AuthorizerConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b89e3b58faac93b47a86d253bd377ccfed6b64d0088167686a5ce5a6f01bc27b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__791936566b3e629fd378dc6a46c31b1a5134acc616fbd9ed9eebc092ed3be3e8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa23efd99303a8f763464c84881ac739adef3c104051bc1d3f02ad8262450c5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayInterceptorConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d2d9d8c84164d38a9976889d155298546ea61a787e120117719ee748ac6cf6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05982d11a516cc3cf2e986a22173b4993c5267490c660a8f123f9c141f3f117b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayProtocolConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8136c8abfebcb699dd26d8e65dbb8e7a922f1cdc2f58375541b3436f139609a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__788309d24193b18115a31defebe9337a71550513b7163a4a603f72832a42ab79(
    *,
    custom_jwt_authorizer: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.CustomJWTAuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112b8d24bc38c0672ed793eba77bfe0cf27779ec1b6d92d7be444d118bc83903(
    *,
    claim_match_operator: builtins.str,
    claim_match_value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.ClaimMatchValueTypeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__952f117dc1f1b6b566aad149f8da1ff097edfd2bc2daad409806c1b726178c95(
    *,
    match_value_string: typing.Optional[builtins.str] = None,
    match_value_string_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__281a42b48773fc98dfce972077d5fadbe244532c4820ce9f7f40d8d292180dd3(
    *,
    authorizing_claim_match_value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.AuthorizingClaimMatchValueTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    inbound_token_claim_name: builtins.str,
    inbound_token_claim_value_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc4944f630bec36007bb93b09eab3e99763f1bed11457e642c0ab535144159e(
    *,
    discovery_url: builtins.str,
    allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_claims: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.CustomClaimValidationTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__715cb5162dd44f0620c0da9c35156ecbbe6adcf966dd3dabfefa1ba61c16a0aa(
    *,
    interception_points: typing.Sequence[builtins.str],
    interceptor: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.InterceptorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    input_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.InterceptorInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__381e09b484f23635acaed28352a759fdd9ac853b91ce6a848c9ed3892887eb7c(
    *,
    mcp: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.MCPGatewayConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ca22e725c6291ac4361eed78ba4e61d1c53d3ed16f378864154be6a22b3fbdc(
    *,
    lambda_: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.LambdaInterceptorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a99f30cc6576d66eb555d4d72e4d8cc323b7560bf001996fd8ea8a3cbcdee5f(
    *,
    pass_request_headers: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fdc3a3b136445d808e02f01ce34f7cf7f93adae6e8dae1f234c0991d3782da4(
    *,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__caff723b1f8dc289e3e0d1f554fe16628873911a93ec8c36ed92f59cde7798c4(
    *,
    instructions: typing.Optional[builtins.str] = None,
    search_type: typing.Optional[builtins.str] = None,
    supported_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e940e88ca017f9ccde7a0419db94aaed6321cc4f2368ad6aa9fe229c8d1d8a3a(
    *,
    workload_identity_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__790df6c55e75e75d6f8c8a9a5518586d5e4ae350e3bfc4555e2ed4bf3c572f31(
    *,
    authorizer_type: builtins.str,
    name: builtins.str,
    protocol_type: builtins.str,
    role_arn: builtins.str,
    authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    exception_level: typing.Optional[builtins.str] = None,
    interceptor_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayInterceptorConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    protocol_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayProtocolConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ca4172cb2708dfeb7420a18b960df15915d2da8589b9495c034bd700c3bd768(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    target_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.TargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    credential_provider_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.CredentialProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    gateway_identifier: typing.Optional[builtins.str] = None,
    metadata_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.MetadataConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__854a661aa5307cc2007308cd63202762f3651b891f3718a702a07e46ccb0bfc7(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__facd54b7bb4cca942a82b0859b83ffbee83d2b5964da7507bd01ce76b51602d7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f55ddaf00701b9be96b4083ffcf99e108df2b912a7fa6a0930aacc493dc19b3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4fb979142cd31fef07a02c2a4b5e3d0eb49bf962781821346eac630d16fcc8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8d18e620b511ca77468615f894540073998d43a19f84c7bd4555618e80c9a3d(
    value: typing.Union[_IResolvable_da3f097b, CfnGatewayTarget.TargetConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__087a7adedbf9e4e0e6abc10f84df215c78eebc146c64c53668096978e91820bd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGatewayTarget.CredentialProviderConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88eae40375f8237511c7176b5010bb5247cb77ff6160f37b46d60eac254c2403(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4c9f5798e9b6c54f5080d4aef35f1a5d286541a90ad283e95cae82b7a8e7de1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00f16ea27eb83e4b32e092f110d089664b10c9e879d89f80aef450f9dc884a25(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGatewayTarget.MetadataConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd9d5dad412e0ebe1edd2df618041d10540bb992843eb766dfcbf3cfc4a59471(
    *,
    api_gateway_tool_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ApiGatewayToolConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    rest_api_id: builtins.str,
    stage: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2555658d10c3f76b5e73f49cc83804d6ab06bb7d23b35ffd199342c484c2e7f(
    *,
    tool_filters: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ApiGatewayToolFilterProperty, typing.Dict[builtins.str, typing.Any]]]]],
    tool_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ApiGatewayToolOverrideProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dda3c870c61fb6006992eac9669c748230298d7c2b484443727b9e07c21f2f6e(
    *,
    filter_path: builtins.str,
    methods: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00479c551dd620558403acae09d625ae65f82b950181b59baa770ce5504b9141(
    *,
    method: builtins.str,
    name: builtins.str,
    path: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a33b2b3f3a682c83f92cbd3e15b4552ff1592eb43e06b8e26d9bb1e8f1003ecd(
    *,
    provider_arn: builtins.str,
    credential_location: typing.Optional[builtins.str] = None,
    credential_parameter_name: typing.Optional[builtins.str] = None,
    credential_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__309e9dda1e6dfcce4b7777150028f4c6782bdc89a099f0ac87ab71e9967a8277(
    *,
    inline_payload: typing.Optional[builtins.str] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.S3ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__149dd633d64001d8edf5b8db5417ed0fc1bfaecff9240452d6911051ec05238e(
    *,
    credential_provider_type: builtins.str,
    credential_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.CredentialProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db13937427760cb24e319f55daf7a1b38d00d0bb009b7b145665b608c53b0f5c(
    *,
    api_key_credential_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ApiKeyCredentialProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    oauth_credential_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.OAuthCredentialProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6ba80f262600990b7647765d60a5f51fb86eeeaf8708f22bc73e4794e784785(
    *,
    lambda_arn: builtins.str,
    tool_schema: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ToolSchemaProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d73da9473e37697d875f5f3c74a1ab3e3ace8090917b37837b001996968f456a(
    *,
    endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b1d88210caa384ede03a06bee42d13165c8bf4cc4206a236d795c44da216e3c(
    *,
    api_gateway: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ApiGatewayTargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.McpLambdaTargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mcp_server: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.McpServerTargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    open_api_schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ApiSchemaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    smithy_model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ApiSchemaConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65b76f9cd39a5276e0183029480a0bf70be6f57ac0853a3a5be14eeecae86c0c(
    *,
    allowed_query_parameters: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_request_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_response_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c602c1e6012421bcbacb23364333a8030b673b0a8e3ebad72fba42b295c2f64(
    *,
    provider_arn: builtins.str,
    scopes: typing.Sequence[builtins.str],
    custom_parameters: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    default_return_url: typing.Optional[builtins.str] = None,
    grant_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f0b1feb9921a2069b72a9a314cb583fbbc6b6fc8af438b2e8f420e03d0368f7(
    *,
    bucket_owner_account_id: typing.Optional[builtins.str] = None,
    uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc512741cd348cf43b33e4ea0df31aae8766e6990dc0675d9111d9a7eb5f9c6a(
    *,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    items: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    required: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a64335e118208df2b03631e56ce84dab935a9d2c9dee1c27c584de679d4dcd6(
    *,
    mcp: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.McpTargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c9a8204fd6db934022c917c4dc62346cf5269b544292d1bac5ed2aae995a300(
    *,
    description: builtins.str,
    input_schema: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    output_schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ff8fed96fdad56eb717513408b41cd94cf1c34461313bbb4de520c38aeab416(
    *,
    inline_payload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.ToolDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.S3ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367178269f9a78c89b5ba5e07b10a309050b4b3eaefd55c5ee6f30ddad20209f(
    *,
    name: builtins.str,
    target_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.TargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    credential_provider_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.CredentialProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    description: typing.Optional[builtins.str] = None,
    gateway_identifier: typing.Optional[builtins.str] = None,
    metadata_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGatewayTarget.MetadataConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b95a7255db9df73ca225a32aecd624481667f18f3308ba77ce3fbf7d7e1cf4f0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    event_expiry_duration: jsii.Number,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    memory_execution_role_arn: typing.Optional[builtins.str] = None,
    memory_strategies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.MemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efd26aeb6a65d79b61f16a74d7d3f32c4d43bcea29520d215020f825921c572d(
    resource: _IMemoryRef_2d13cc89,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0daa51afcc3d4bc4c908dda067499db502f905d7a250174c02a9849a22623426(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b76cbb12d67c915a322289eef0caf05911a64361531f525f945065e6fbd1b0b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29efd6b6b9a6ac1e7281cd85ae63e9d6002789f18830f68a7cec0a0d012ac382(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c376bc3bd26c18cf626509568f040ac75ef52a68ef8a39ca3e5b6b8308374496(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f948061bc9aba0eb248f047c217bd96c19cf47d09da3c7b9708380caf387394f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93e29c7f80206ddbc4de97f028b669d82daf8dd5c65b29ae535035b57cd461ed(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b682a270f87cf6f76b16e70568b3e20c1994f4ff375efed9e59f3ff29cce80cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bd6b17fbf9c4464799eba94f4be79124e7c5491b62da83c1a8bd39d6f2a0def(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b18515e6738d6694af7855ee5a84c8940fcfa482c5e51f03ea9e0abda4a56765(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMemory.MemoryStrategyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20937c3b9ee32cb1df4d7eaf09c5da2b921076b8dab073c8f61380cb9b64e33b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80b393ad440afaf6b639d0ad3fdd1431e23bc8fa4658d92c51bbe3ae892ec72e(
    *,
    episodic_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.EpisodicOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    self_managed_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SelfManagedConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    semantic_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SemanticOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    summary_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SummaryOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_preference_override: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.UserPreferenceOverrideProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68f9ef2809f813258bef3dcd9ec460d2f237f2127d9f7cb9aae3256166ba8183(
    *,
    name: builtins.str,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.CustomConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    created_at: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    strategy_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4010f11a9f956fe10befa570e47005124fa04732849c4143a5219ad033db3bff(
    *,
    name: builtins.str,
    created_at: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    reflection_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.EpisodicReflectionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    status: typing.Optional[builtins.str] = None,
    strategy_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aa1a71d684023e3bf516c1377383806779b05133a8783b948bbcea97001dbd1(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f6e2b335649583bd753b07454a443607a3c1a4b900aeb0d79184b7f9fea550(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b710e8660112018a6354eb5ae8c4e7aa27f0cd362be38426220fd00b83c09a8(
    *,
    consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.EpisodicOverrideConsolidationConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    extraction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.EpisodicOverrideExtractionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    reflection: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.EpisodicOverrideReflectionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df10fcf9a92c0373c158e2aa4763d8107995e1f7b4403a8c8001a6afe3424ad4(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d10801b6b457e9912061807464c00e48d36901349246d4c00671ab17eaee367(
    *,
    namespaces: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44e7fa751a69795001dc84cc0fd23b36ae6952ce8c475d549b7599b3353a7c9a(
    *,
    payload_delivery_bucket_name: typing.Optional[builtins.str] = None,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7fa25b2413ebaf6794a4e0d96d4404f578a37b86cd501369f7c93f8d049e8e7(
    *,
    custom_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.CustomMemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    episodic_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.EpisodicMemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    semantic_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SemanticMemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    summary_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SummaryMemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    user_preference_memory_strategy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.UserPreferenceMemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f26f0bfb6bb91a96529926b34610d43ded0571d826aa8ac6cb6e63367e9ea089(
    *,
    message_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4fcd7b9f7c5c0bb0c80ff54635936b78ada2b3d24596ba7cd43b9ece93f804c(
    *,
    historical_context_window_size: typing.Optional[jsii.Number] = None,
    invocation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.InvocationConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    trigger_conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.TriggerConditionInputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdd1426fa7487dcb02499d9f810acd963031578a3c30fd4be0b076b09a32b124(
    *,
    name: builtins.str,
    created_at: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    strategy_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393b5baf9d5b39c6498ec7dde998e56d10f272578b90e6901d6e5717c4d0b79d(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__669cd3ffc171b2cd7f3a4c3d6196e5a075449bedd07119892324a275601cf283(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4fcd9046e68a8e9401f48408f0a4870f5c13f714c342e2085d178557990c4ee(
    *,
    consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SemanticOverrideConsolidationConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    extraction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SemanticOverrideExtractionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eee517e4354bf11f650f3de6c9e3789b5ced3c958c97582b32deda0a2643b376(
    *,
    name: builtins.str,
    created_at: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    strategy_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c990b6378d188092fe95d78caab0eb586836dc0ca2194f9cbf3788c24c6ec053(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b23ed198bcd958ec3a014c4dd2d6c418b82bc1895ca1b0af24503f002e61d492(
    *,
    consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.SummaryOverrideConsolidationConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cf65bf0b7de7a122f8fdf3c50a61ba88dd5248ad841dd004cb6bd0f7174ec45(
    *,
    idle_session_timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__171b0765936a13c6e7c17456605ec3e2bc9c36685a864e8c11187bfd9a4bc89a(
    *,
    token_count: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca3b096b467bf1778a21961da57f12ce16cf0ef63aeee1b912577f66fdb48cb(
    *,
    message_based_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.MessageBasedTriggerInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_based_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.TimeBasedTriggerInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    token_based_trigger: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.TokenBasedTriggerInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404072c850abd871eb86ee8d04d20a311da6fb4147c983194a800b234cbf1e04(
    *,
    name: builtins.str,
    created_at: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    namespaces: typing.Optional[typing.Sequence[builtins.str]] = None,
    status: typing.Optional[builtins.str] = None,
    strategy_id: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    updated_at: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccf5e9da18deac0b8b6ae4a435ef031fafc5037acda6e9b5a2f31d25335ea0ad(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e2496eed790ccc12ab395eda9327489aa843786babbb42e3d6238d462a4c629(
    *,
    append_to_prompt: builtins.str,
    model_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a657a70bb10847e586abd34f2ecc11ddcafa4b88002f03b52b85d085202adcfd(
    *,
    consolidation: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.UserPreferenceOverrideConsolidationConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    extraction: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.UserPreferenceOverrideExtractionConfigurationInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28dda218e5909d8e89c4ab4ee9bac6335e1f1cde1c399e1ac3c1c739ece89e19(
    *,
    event_expiry_duration: jsii.Number,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    memory_execution_role_arn: typing.Optional[builtins.str] = None,
    memory_strategies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMemory.MemoryStrategyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aa0e93d03096cdb556ed3eb9ee7b341e52b0d24c88655e4061d5de404c807ed(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_source_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.DataSourceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    evaluation_execution_role_arn: builtins.str,
    evaluators: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.EvaluatorReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    online_evaluation_config_name: builtins.str,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.RuleProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90c4c9bc0bd65c4957d82632ee0e6857bd64fa695b00eff8e97cfe4bbb58212a(
    resource: _IOnlineEvaluationConfigRef_cf19cabf,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__197c10ea28d6b7fcd6d734a0f7527f987482843ef77aba73be70ab37f3274a87(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__174e31db4a9e05f32574075e0d5d9ca13a10fd3d3f58880897c11aee769870b3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2605ec5d933033d8b4e2a10590a11c2b518e3dc4ada8dd7f8cb9fb3b71bfaec1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdec6581e7d868222d3bc0bf43dc993d50bc9f422198fc013c1856f442104865(
    value: typing.Union[_IResolvable_da3f097b, CfnOnlineEvaluationConfig.DataSourceConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f1e9b72c99731112fc077560a4c69257c903d6826ca03adba993e9cafec8e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6203a39418b156df1e66640712fbe71f2ddf1f83ac789902b76160c12690a251(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnOnlineEvaluationConfig.EvaluatorReferenceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d075f3152c3d233d71d9aad22ce139f2486815a5e44ccde4015d161724a5efda(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cf46c720a151dc4eed5fc818c0539ab15e6aced33ff2153a91d7d9a58b47cc2(
    value: typing.Union[_IResolvable_da3f097b, CfnOnlineEvaluationConfig.RuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9329e42c1ed6716c18f0ba3ed3c4061991e8232ee68b38584dd695b80a862ccb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64aa9583ff086b054a843cddaea1d6ba93b7d4aca2beac24d850e42c20b5bac3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06d804c8e6fc6685724ca2260796166f7384dcb1ccbf41dd1fa2700163b0ad02(
    *,
    log_group_names: typing.Sequence[builtins.str],
    service_names: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fba0fe46886c9e6934bd149cf7b10f76eeb83adfa2cc2a2020d0587e70423c9(
    *,
    log_group_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9e9c1632a43c17755ee22dab7b1cbedd703f1dd6049647d3cdfcc0b43a33016(
    *,
    cloud_watch_logs: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.CloudWatchLogsInputConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a44db4de7a49610956caf53195620a14d4d68d5a98645ab3f5ff7cb927a9ac54(
    *,
    evaluator_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3af31c16195143a16e0eb30f3c7e34f8a0807321ad86daeb9e4fc31e3f37d3d(
    *,
    key: builtins.str,
    operator: builtins.str,
    value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.FilterValueProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b42f86596813ff2e3e66267d5100485bb51a02b655555985649c33361c96f19(
    *,
    boolean_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    double_value: typing.Optional[jsii.Number] = None,
    string_value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901f04239ac1d631f611bae7e5b46abe7106c2310714eeae85eb20759dad8182(
    *,
    cloud_watch_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.CloudWatchOutputConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d26dc57868bb2276aa712667113ed9c9d243f98c5821e624a9c99a224d918c0(
    *,
    sampling_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.SamplingConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.FilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    session_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.SessionConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e4b82a47eb409b6be018392f32b388af0c03327656d5cdcf118e6dff7977b6f(
    *,
    sampling_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e489fef922673116efb3ad1b62ccdb82d7343318d520456ba5e2d6e89b2afb(
    *,
    session_timeout_minutes: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0027d3063b3949a340eab6076bb9ce68daa108d23e44efbf30f9a1211d0261e5(
    *,
    data_source_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.DataSourceConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    evaluation_execution_role_arn: builtins.str,
    evaluators: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.EvaluatorReferenceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    online_evaluation_config_name: builtins.str,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOnlineEvaluationConfig.RuleProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0df0ec34c1700a2fd80d71aa113459b1f257b8a6040e2dac1057827afc8f5d2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.PolicyDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    policy_engine_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    validation_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a816e5e2df5c6422bb1b1425f808d869fb6346315014ecb535bc6ef61807b51(
    resource: _IPolicyRef_ceb8b108,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e91554c5d78a87cee0dcc173750b965564cc04c6f7914d1203eda44a959ddbe(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60ea8f973b55390f2cec1d7d6883b362c9bcebcabd3ad90203d8003b259cc15a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90aa01410268a0a9b8329f1730f233722091722e470d4250502fb81196d7aaa9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50b7eef4611f94f2995d764a972bab6f09b1ad87de0e3c55ef05b5ef7a2ce77f(
    value: typing.Union[_IResolvable_da3f097b, CfnPolicy.PolicyDefinitionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fb243c83cba8b4cece81df4ce8b043bd043afc8a22739fa364e09cb5a0172a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60f6d37f81d7766e81b7e5afe51a2b3830f091c1efc676ca8f71909ca61dc2c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a62df0bf0572336e2f28e5a6426bde1f261612e5e0c84a7839f62c6771062a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e182f5e6fcaeb9a8106b8902eb058d4494505efd524ef30250a9e7b351ecbca9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd4c98edc5615559914b5f68ccb2078c51b044946e201c8db3860329b3824d87(
    *,
    statement: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6794e02be8a07b494523ce530bdb5da6ec840b4e6342043fc96304f1d964632(
    *,
    cedar: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.CedarPolicyProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4684b4b63ba85bd5dc7e5f6733555e789f7d88f65ee00f5c487dfa126d7d66a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d723add61d7456bc287abcb7c2d34c95e4a9b40b0262b2e977f594db1e112a7(
    resource: _IPolicyEngineRef_6d885cfc,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59e6805c5178d527b1123a3cbf1f0ed0ac21a3f1c2183a86f13cf97df9dfd42d(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99bc04a5a5e66cb6d659f81b4ca399b70db0cc9d00d7826dba5b19ac18eb3320(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a640866ee40ff74b9b0ee9128a48548073cba59e18f794d91bbf0866e5b9aa8a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ac69c1793e7303c1dfe586ac140b18e9794de8ad51c5575ee3590b2e81efb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21dd4fe5af219c86bdbd3e23a682d03cc71ff9b8174dae386145a37d5c2f867e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d9709f935befd653e89210289122143b738739fbfeed30480fbdd76a67d0042(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a9c73af7cca4aa195504171baebe7bcb53d06bd21f6e242c33bf4700692135d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__743592ad2798d644b313c682b278dfac01eb5a93d7b7fe59943eaddab0ca5a1f(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95094990d09b6f6bc15ab83744a973bf7541ebc86b713d23c0165d6234555308(
    *,
    definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.PolicyDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    policy_engine_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    validation_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f75c2b58380182b53165109480fecdbf9bcd35c2fcfcfea5141466ba05b7e7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_runtime_artifact: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AgentRuntimeArtifactProperty, typing.Dict[builtins.str, typing.Any]]],
    agent_runtime_name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    protocol_configuration: typing.Optional[builtins.str] = None,
    request_header_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.RequestHeaderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479c61f7c7f79ce5de0ca6bc78388693d928e50602c049521e888404369b8c81(
    resource: _IRuntimeRef_00302e12,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64de4894e52d23f2312943e0eaaba7eff4dbdb44d5dc64e873e7a65d9d67e7bd(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41eb1aeeb420a432d00eafdf7061763658f434f8c1b3fac5748e0b80cf168cda(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ffbc19212156590bcfcec54a917d56095cf1d0e95a1f4f4107501a8cf457feb7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9afa965e1f7852c99b813a59ddc326e4e8b2e629273fff790e48abcc309421fb(
    value: typing.Union[_IResolvable_da3f097b, CfnRuntime.AgentRuntimeArtifactProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20e5f3a5d4d3f3cf24f87565ebb2f7c531ed9e006970eb5a59dee4eeed670f19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76a3b80aa643920bb76e97b49e6d7c54f3367df4203a420045d6d631a4d54658(
    value: typing.Union[_IResolvable_da3f097b, CfnRuntime.NetworkConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__712719ad084eaaa1f88407e6da1dd4ed68fa570a04329676de9d476fde02ebfe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577d498b775175712bf02d50d4dc0a7fa74d069187c6c0daba641442a844c29e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRuntime.AuthorizerConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86887c96ad11d54aa9be7288cd5dfe9a9b3cb370236b2cf8c98f0ea09d7246e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27b52f571e16cbee3d0cb6aef888169b2fdf172a92199c29075b1bbfe5eb3091(
    value: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fa017855df5800a745ab54e05af1f928ca7fbff9580670f50aa611ef9670585(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRuntime.LifecycleConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd16ca9a4cf1077fb69bea991264277b990667565406b724c960232073239095(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0964845eb3d77c8d88078f56bcf318b9fe4fa50078a5bf150216455e4bc0cde0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRuntime.RequestHeaderConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13c0ee18c00618ce3d55cf861e88265d3db540867ff55146671310649d3ccaee(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51346444ae527a839c6fcfd4fd456eeea9b11da43bf9dadd9b152cfc716ecfd2(
    *,
    code_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.CodeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    container_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.ContainerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb18338480d08b211086521e0155635de6c3b54cf6ebbb5a7ee690c697991b4b(
    *,
    custom_jwt_authorizer: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.CustomJWTAuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aec3caa15f03a36412929e5d8590d844c0a42d206d41633945c4edef06d42b12(
    *,
    claim_match_operator: builtins.str,
    claim_match_value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.ClaimMatchValueTypeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1e5bed0c52ceaf858fa532930be858f1c52ad0f687c28a4365fff6aa1dde945(
    *,
    match_value_string: typing.Optional[builtins.str] = None,
    match_value_string_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f41e2d1a7603e72b05b2b9f19fd3ed1212f3de3311dceb488af789649eda5a1(
    *,
    code: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.CodeProperty, typing.Dict[builtins.str, typing.Any]]],
    entry_point: typing.Sequence[builtins.str],
    runtime: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02b939e505c2d1d50e2de1a34b344b0803317afa1a475dde7482c11135e9ad61(
    *,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0740ce1d3425c4e128b2f49784ee2a02ae6e81129ade5290d001575f4ecacb8(
    *,
    container_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__711e5e4ff145f76afd81911a3f92a921a0e7add7ab92dc4fe87d49ff367447dd(
    *,
    authorizing_claim_match_value: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AuthorizingClaimMatchValueTypeProperty, typing.Dict[builtins.str, typing.Any]]],
    inbound_token_claim_name: builtins.str,
    inbound_token_claim_value_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6479ff33c6925aa85dcd6d4587cd46a0d073bd9992bb93c306d366f07cda2391(
    *,
    discovery_url: builtins.str,
    allowed_audience: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_clients: typing.Optional[typing.Sequence[builtins.str]] = None,
    allowed_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_claims: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.CustomClaimValidationTypeProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7dbc8b9876a11d54d81ef95ffe47ee5c649dfccb99ee31d9fba5b23defef9a4(
    *,
    idle_runtime_session_timeout: typing.Optional[jsii.Number] = None,
    max_lifetime: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7ef3688e7eda46e5ab607f7c059dd5ed308816790e532f38188518d3a7c9b0f(
    *,
    network_mode: builtins.str,
    network_mode_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e84a0bf594bf7173d323308d7c226c002caf3ffc7491c328dcd26a42c198c3e2(
    *,
    request_header_allowlist: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c4beadb07e8c6b725d20f4621457e58be14242062fb450da57aa4e91639c8f(
    *,
    bucket: builtins.str,
    prefix: builtins.str,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e546c3d4da6e03e6ff8e890d2d32819d3e7c17149a4f17d0e75c9569fa3aad9(
    *,
    security_groups: typing.Sequence[builtins.str],
    subnets: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68380bfa2496b392a6192eeab7bae5b15e67d93a4946dff9481dca7e2b9da401(
    *,
    workload_identity_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f889c0edf8dd4715192bf69e6433f02f671ca35ed9b8e8f7622b298a7b14955a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    agent_runtime_id: builtins.str,
    name: builtins.str,
    agent_runtime_version: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__817ffbdbbe724c4d150b381c3527e3473cdef2580396b28edcec84f8ca910c17(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e6a578bb33afa13fb1d85d1b682fc96e67f21a5fb168de296365084e02f261(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91be73ce07416705255e5e1569db31b3f488f1376320ddae8d8803981071f602(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ceb50df9e5593b49d2fbdc6aac8e77c6be9322ee82ceea79d7d86478e1a9d74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f380de6caf6e91bd3b0399e46b356f219d19dd4297d832ed74437f4653be82c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45c0052c9218918d9940523a8d7f016f7eaf5fe73a714ee05b2ba7a94aa9df9f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479a4b8aa6bb0db70941c7bc7a41e153fdbf533d62d2c2dc2ae2edf57fb46e99(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1df913b08f181c8777324479d4caab3dc1c0e41137ac1db4a0b10f478ad63ce7(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03746d507f3e8e95afbebc436c73d1ac1fc643ccea60f817b99b76cb41ccf5fb(
    *,
    agent_runtime_id: builtins.str,
    name: builtins.str,
    agent_runtime_version: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e489b12cef85647a902e6bba6db3bf5f3ef1a856b74cf0fc5a7f8d1d0fa4a4b(
    *,
    agent_runtime_artifact: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AgentRuntimeArtifactProperty, typing.Dict[builtins.str, typing.Any]]],
    agent_runtime_name: builtins.str,
    network_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    authorizer_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.AuthorizerConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    environment_variables: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    protocol_configuration: typing.Optional[builtins.str] = None,
    request_header_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRuntime.RequestHeaderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09a8e6f0ae71da08ac7a3937e8dcaa170d25c76feb84006a0b53e9e688f16c17(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    allowed_resource_oauth2_return_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d17bbc0e09dbed545a31bdb5536b2bc6164ac952e9964c0b9fb5b066c0ad1639(
    resource: _IWorkloadIdentityRef_dc6077a7,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc71f5a7a0caee1d1f13462070b832ea0f00bf8762d51e41cb3870cc836ef87b(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766a926b6ea4d718606dac6820c9d33d069b4c27a0844ba0d55f325ade157e6c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__488009317eeca5f98d0be9fbcd30e71ec79ca306a6ab22b48b1feab3c04d0f94(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46dd6904ea9e85082bdbdcd42c00d119b0b4a4f43c5b3a1f5c273c0eb5d89289(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b3780d06fd0cd5b35919591809dff38c541131cad0233fc83e2f1a65e282dc8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d24890b8ce488c10d666570acfa91e9c0c2c358e35cc3bbad1ef37fc9bad1869(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5358b1efbb0f18624add0a9e7d27cb517f7d9ceed952fcd31225012dfd0e89c6(
    *,
    name: builtins.str,
    allowed_resource_oauth2_return_urls: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
