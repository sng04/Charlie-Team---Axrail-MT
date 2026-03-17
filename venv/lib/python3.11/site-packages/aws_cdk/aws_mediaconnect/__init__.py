r'''
# AWS::MediaConnect Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mediaconnect as mediaconnect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MediaConnect construct libraries](https://constructs.dev/search?q=mediaconnect)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MediaConnect resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaConnect.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MediaConnect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaConnect.html).

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
from ..interfaces.aws_mediaconnect import (
    BridgeOutputReference as _BridgeOutputReference_4ac2cf5a,
    BridgeReference as _BridgeReference_7039ca9d,
    BridgeSourceReference as _BridgeSourceReference_fdd405eb,
    FlowEntitlementReference as _FlowEntitlementReference_2242862f,
    FlowOutputReference as _FlowOutputReference_30ed8edf,
    FlowReference as _FlowReference_cf80a510,
    FlowSourceReference as _FlowSourceReference_0d57ee68,
    FlowVpcInterfaceReference as _FlowVpcInterfaceReference_74070c82,
    GatewayReference as _GatewayReference_91ca4e85,
    IBridgeOutputRef as _IBridgeOutputRef_d8763e78,
    IBridgeRef as _IBridgeRef_2f2ab872,
    IBridgeSourceRef as _IBridgeSourceRef_8b16438d,
    IFlowEntitlementRef as _IFlowEntitlementRef_83db35bc,
    IFlowOutputRef as _IFlowOutputRef_be0a9d75,
    IFlowRef as _IFlowRef_c5e8f48d,
    IFlowSourceRef as _IFlowSourceRef_b94a8321,
    IFlowVpcInterfaceRef as _IFlowVpcInterfaceRef_d5bcec46,
    IGatewayRef as _IGatewayRef_4783a0c6,
    IRouterInputRef as _IRouterInputRef_6915df50,
    IRouterNetworkInterfaceRef as _IRouterNetworkInterfaceRef_05bd061c,
    IRouterOutputRef as _IRouterOutputRef_afa317cd,
    RouterInputReference as _RouterInputReference_b71c2141,
    RouterNetworkInterfaceReference as _RouterNetworkInterfaceReference_fdc8b08c,
    RouterOutputReference as _RouterOutputReference_12c4ea61,
)


@jsii.implements(_IInspectable_c2943556, _IBridgeRef_2f2ab872)
class CfnBridge(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge",
):
    '''The ``AWS::MediaConnect::Bridge`` resource defines a connection between your data center’s gateway instances and the cloud.

    For each bridge, you specify the type of bridge, transport protocol to use, and details for any outputs and failover.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html
    :cloudformationResource: AWS::MediaConnect::Bridge
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_bridge = mediaconnect.CfnBridge(self, "MyCfnBridge",
            name="name",
            placement_arn="placementArn",
            sources=[mediaconnect.CfnBridge.BridgeSourceProperty(
                flow_source=mediaconnect.CfnBridge.BridgeFlowSourceProperty(
                    flow_arn="flowArn",
                    name="name",
        
                    # the properties below are optional
                    flow_vpc_interface_attachment=mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                ),
                network_source=mediaconnect.CfnBridge.BridgeNetworkSourceProperty(
                    multicast_ip="multicastIp",
                    name="name",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
        
                    # the properties below are optional
                    multicast_source_settings=mediaconnect.CfnBridge.MulticastSourceSettingsProperty(
                        multicast_source_ip="multicastSourceIp"
                    )
                )
            )],
        
            # the properties below are optional
            egress_gateway_bridge=mediaconnect.CfnBridge.EgressGatewayBridgeProperty(
                max_bitrate=123
            ),
            ingress_gateway_bridge=mediaconnect.CfnBridge.IngressGatewayBridgeProperty(
                max_bitrate=123,
                max_outputs=123
            ),
            outputs=[mediaconnect.CfnBridge.BridgeOutputProperty(
                network_output=mediaconnect.CfnBridge.BridgeNetworkOutputProperty(
                    ip_address="ipAddress",
                    name="name",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
                    ttl=123
                )
            )],
            source_failover_config=mediaconnect.CfnBridge.FailoverConfigProperty(
                failover_mode="failoverMode",
        
                # the properties below are optional
                source_priority=mediaconnect.CfnBridge.SourcePriorityProperty(
                    primary_source="primarySource"
                ),
                state="state"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        placement_arn: builtins.str,
        sources: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.BridgeSourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        egress_gateway_bridge: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.EgressGatewayBridgeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ingress_gateway_bridge: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.IngressGatewayBridgeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        outputs: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.BridgeOutputProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        source_failover_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.FailoverConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::Bridge``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the bridge. This name can not be modified after the bridge is created.
        :param placement_arn: The bridge placement Amazon Resource Number (ARN).
        :param sources: The sources that you want to add to this bridge.
        :param egress_gateway_bridge: An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.
        :param ingress_gateway_bridge: An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.
        :param outputs: The outputs that you want to add to this bridge.
        :param source_failover_config: The settings for source failover.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21d1f093ae6c3ef104fbfbb93b13b3338230662ddb218fed6d74e5040acf931c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBridgeProps(
            name=name,
            placement_arn=placement_arn,
            sources=sources,
            egress_gateway_bridge=egress_gateway_bridge,
            ingress_gateway_bridge=ingress_gateway_bridge,
            outputs=outputs,
            source_failover_config=source_failover_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForBridge")
    @builtins.classmethod
    def arn_for_bridge(cls, resource: "_IBridgeRef_2f2ab872") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61c94f5a708599ab90700dbc916f984911d2356933cecac7cb8883e4716ef8e3)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForBridge", [resource]))

    @jsii.member(jsii_name="isCfnBridge")
    @builtins.classmethod
    def is_cfn_bridge(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnBridge.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efc0ae85c0d5def613a48526ecb28ec24a692b3f96ffc4f3733d1a84d3727827)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnBridge", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e83409273af3b66857452f9f32805fa3650ea56dd8bccf1a4cae459f1669317)
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
            type_hints = typing.get_type_hints(_typecheckingstub__34788268cca3ef6b9f17b00e64981600b0697ff2af1a873da5b2521e55e8f627)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBridgeArn")
    def attr_bridge_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the bridge.

        :cloudformationAttribute: BridgeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBridgeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBridgeState")
    def attr_bridge_state(self) -> builtins.str:
        '''The current status of the bridge.

        Possible values are: ACTIVE or STANDBY.

        :cloudformationAttribute: BridgeState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBridgeState"))

    @builtins.property
    @jsii.member(jsii_name="bridgeRef")
    def bridge_ref(self) -> "_BridgeReference_7039ca9d":
        '''A reference to a Bridge resource.'''
        return typing.cast("_BridgeReference_7039ca9d", jsii.get(self, "bridgeRef"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the bridge.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__897e5b31abf5fb8064d23feda8e8dab6abc8fc04b479fede8ec2f5a8f11283ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="placementArn")
    def placement_arn(self) -> builtins.str:
        '''The bridge placement Amazon Resource Number (ARN).'''
        return typing.cast(builtins.str, jsii.get(self, "placementArn"))

    @placement_arn.setter
    def placement_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c0d91a8143e25d3431f038cc493b72ff78caeb2aae6a8de25ef906162ed203)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeSourceProperty"]]]:
        '''The sources that you want to add to this bridge.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeSourceProperty"]]], jsii.get(self, "sources"))

    @sources.setter
    def sources(
        self,
        value: typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeSourceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c151228d22c29de1b22fb11c72513278ae8b19faf50c26128a49b5bb5cd8231e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="egressGatewayBridge")
    def egress_gateway_bridge(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.EgressGatewayBridgeProperty"]]:
        '''An egress bridge is a cloud-to-ground bridge.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.EgressGatewayBridgeProperty"]], jsii.get(self, "egressGatewayBridge"))

    @egress_gateway_bridge.setter
    def egress_gateway_bridge(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.EgressGatewayBridgeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8744f4915b3da8a1fb0b28e71cdd2260912dbea385353bb4a2378a0dcf2e1a19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressGatewayBridge", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ingressGatewayBridge")
    def ingress_gateway_bridge(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.IngressGatewayBridgeProperty"]]:
        '''An ingress bridge is a ground-to-cloud bridge.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.IngressGatewayBridgeProperty"]], jsii.get(self, "ingressGatewayBridge"))

    @ingress_gateway_bridge.setter
    def ingress_gateway_bridge(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.IngressGatewayBridgeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2370206c3aaeddbbe4f170d30b717ce583cd273a4a651e68abaf2042096869bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressGatewayBridge", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outputs")
    def outputs(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeOutputProperty"]]]]:
        '''The outputs that you want to add to this bridge.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeOutputProperty"]]]], jsii.get(self, "outputs"))

    @outputs.setter
    def outputs(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeOutputProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f0f04e00fdc529449b6434bd02be499c861ae34a03215caf6afedaf59974ca0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceFailoverConfig")
    def source_failover_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.FailoverConfigProperty"]]:
        '''The settings for source failover.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.FailoverConfigProperty"]], jsii.get(self, "sourceFailoverConfig"))

    @source_failover_config.setter
    def source_failover_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.FailoverConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a1d3ccb8b1bf31380b43926b18329ad07b95b13cfd50c81dfdcb52ed4700194)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFailoverConfig", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.BridgeFlowSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "flow_arn": "flowArn",
            "name": "name",
            "flow_vpc_interface_attachment": "flowVpcInterfaceAttachment",
        },
    )
    class BridgeFlowSourceProperty:
        def __init__(
            self,
            *,
            flow_arn: builtins.str,
            name: builtins.str,
            flow_vpc_interface_attachment: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source of the bridge.

            A flow source originates in MediaConnect as an existing cloud flow.

            :param flow_arn: The ARN of the cloud flow used as a source of this bridge.
            :param name: The name of the flow source.
            :param flow_vpc_interface_attachment: The name of the VPC interface attachment to use for this source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_flow_source_property = mediaconnect.CfnBridge.BridgeFlowSourceProperty(
                    flow_arn="flowArn",
                    name="name",
                
                    # the properties below are optional
                    flow_vpc_interface_attachment=mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c9a85716cc44ad0d338a783771f76c5420792553cd40338bc48069294fac934)
                check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument flow_vpc_interface_attachment", value=flow_vpc_interface_attachment, expected_type=type_hints["flow_vpc_interface_attachment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "flow_arn": flow_arn,
                "name": name,
            }
            if flow_vpc_interface_attachment is not None:
                self._values["flow_vpc_interface_attachment"] = flow_vpc_interface_attachment

        @builtins.property
        def flow_arn(self) -> builtins.str:
            '''The ARN of the cloud flow used as a source of this bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html#cfn-mediaconnect-bridge-bridgeflowsource-flowarn
            '''
            result = self._values.get("flow_arn")
            assert result is not None, "Required property 'flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html#cfn-mediaconnect-bridge-bridgeflowsource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def flow_vpc_interface_attachment(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.VpcInterfaceAttachmentProperty"]]:
            '''The name of the VPC interface attachment to use for this source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html#cfn-mediaconnect-bridge-bridgeflowsource-flowvpcinterfaceattachment
            '''
            result = self._values.get("flow_vpc_interface_attachment")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.VpcInterfaceAttachmentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeFlowSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.BridgeNetworkOutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ip_address": "ipAddress",
            "name": "name",
            "network_name": "networkName",
            "port": "port",
            "protocol": "protocol",
            "ttl": "ttl",
        },
    )
    class BridgeNetworkOutputProperty:
        def __init__(
            self,
            *,
            ip_address: builtins.str,
            name: builtins.str,
            network_name: builtins.str,
            port: jsii.Number,
            protocol: builtins.str,
            ttl: jsii.Number,
        ) -> None:
            '''The output of the bridge.

            A network output is delivered to your premises.

            :param ip_address: The network output IP address.
            :param name: The network output name.
            :param network_name: The network output's gateway network name.
            :param port: The network output's port.
            :param protocol: The network output protocol. .. epigraph:: AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
            :param ttl: The network output TTL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_network_output_property = mediaconnect.CfnBridge.BridgeNetworkOutputProperty(
                    ip_address="ipAddress",
                    name="name",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
                    ttl=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__621a738d7654729dd7b3374ce4f5872ae1b369d023ed93a125315923bc53acb5)
                check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ip_address": ip_address,
                "name": name,
                "network_name": network_name,
                "port": port,
                "protocol": protocol,
                "ttl": ttl,
            }

        @builtins.property
        def ip_address(self) -> builtins.str:
            '''The network output IP address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-ipaddress
            '''
            result = self._values.get("ip_address")
            assert result is not None, "Required property 'ip_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The network output name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_name(self) -> builtins.str:
            '''The network output's gateway network name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-networkname
            '''
            result = self._values.get("network_name")
            assert result is not None, "Required property 'network_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The network output's port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network output protocol.

            .. epigraph::

               AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ttl(self) -> jsii.Number:
            '''The network output TTL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-ttl
            '''
            result = self._values.get("ttl")
            assert result is not None, "Required property 'ttl' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeNetworkOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.BridgeNetworkSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "multicast_ip": "multicastIp",
            "name": "name",
            "network_name": "networkName",
            "port": "port",
            "protocol": "protocol",
            "multicast_source_settings": "multicastSourceSettings",
        },
    )
    class BridgeNetworkSourceProperty:
        def __init__(
            self,
            *,
            multicast_ip: builtins.str,
            name: builtins.str,
            network_name: builtins.str,
            port: jsii.Number,
            protocol: builtins.str,
            multicast_source_settings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.MulticastSourceSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source of the bridge.

            A network source originates at your premises.

            :param multicast_ip: The network source multicast IP.
            :param name: The name of the network source.
            :param network_name: The network source's gateway network name.
            :param port: The network source port.
            :param protocol: The network source protocol. .. epigraph:: AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
            :param multicast_source_settings: The settings related to the multicast source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_network_source_property = mediaconnect.CfnBridge.BridgeNetworkSourceProperty(
                    multicast_ip="multicastIp",
                    name="name",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
                
                    # the properties below are optional
                    multicast_source_settings=mediaconnect.CfnBridge.MulticastSourceSettingsProperty(
                        multicast_source_ip="multicastSourceIp"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1642b43f3173ebc33fe250c935a5af5006fe555caff2d5246139c99d6cfb0d9b)
                check_type(argname="argument multicast_ip", value=multicast_ip, expected_type=type_hints["multicast_ip"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument multicast_source_settings", value=multicast_source_settings, expected_type=type_hints["multicast_source_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "multicast_ip": multicast_ip,
                "name": name,
                "network_name": network_name,
                "port": port,
                "protocol": protocol,
            }
            if multicast_source_settings is not None:
                self._values["multicast_source_settings"] = multicast_source_settings

        @builtins.property
        def multicast_ip(self) -> builtins.str:
            '''The network source multicast IP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-multicastip
            '''
            result = self._values.get("multicast_ip")
            assert result is not None, "Required property 'multicast_ip' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the network source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_name(self) -> builtins.str:
            '''The network source's gateway network name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-networkname
            '''
            result = self._values.get("network_name")
            assert result is not None, "Required property 'network_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The network source port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network source protocol.

            .. epigraph::

               AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def multicast_source_settings(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.MulticastSourceSettingsProperty"]]:
            '''The settings related to the multicast source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-multicastsourcesettings
            '''
            result = self._values.get("multicast_source_settings")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.MulticastSourceSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeNetworkSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.BridgeOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"network_output": "networkOutput"},
    )
    class BridgeOutputProperty:
        def __init__(
            self,
            *,
            network_output: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.BridgeNetworkOutputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The output of the bridge.

            :param network_output: The output of the bridge. A network output is delivered to your premises.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_output_property = mediaconnect.CfnBridge.BridgeOutputProperty(
                    network_output=mediaconnect.CfnBridge.BridgeNetworkOutputProperty(
                        ip_address="ipAddress",
                        name="name",
                        network_name="networkName",
                        port=123,
                        protocol="protocol",
                        ttl=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dff659c89b605c1b1a727af90c48784adba90b01104dfd2da4ea33b042b8e12f)
                check_type(argname="argument network_output", value=network_output, expected_type=type_hints["network_output"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if network_output is not None:
                self._values["network_output"] = network_output

        @builtins.property
        def network_output(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeNetworkOutputProperty"]]:
            '''The output of the bridge.

            A network output is delivered to your premises.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeoutput.html#cfn-mediaconnect-bridge-bridgeoutput-networkoutput
            '''
            result = self._values.get("network_output")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeNetworkOutputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.BridgeSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"flow_source": "flowSource", "network_source": "networkSource"},
    )
    class BridgeSourceProperty:
        def __init__(
            self,
            *,
            flow_source: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.BridgeFlowSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            network_source: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.BridgeNetworkSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The bridge's source.

            :param flow_source: The source of the bridge. A flow source originates in MediaConnect as an existing cloud flow.
            :param network_source: The source of the bridge. A network source originates at your premises.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_source_property = mediaconnect.CfnBridge.BridgeSourceProperty(
                    flow_source=mediaconnect.CfnBridge.BridgeFlowSourceProperty(
                        flow_arn="flowArn",
                        name="name",
                
                        # the properties below are optional
                        flow_vpc_interface_attachment=mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty(
                            vpc_interface_name="vpcInterfaceName"
                        )
                    ),
                    network_source=mediaconnect.CfnBridge.BridgeNetworkSourceProperty(
                        multicast_ip="multicastIp",
                        name="name",
                        network_name="networkName",
                        port=123,
                        protocol="protocol",
                
                        # the properties below are optional
                        multicast_source_settings=mediaconnect.CfnBridge.MulticastSourceSettingsProperty(
                            multicast_source_ip="multicastSourceIp"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__048c12dd6c2d1c5e61292ef13f12e16c2c87cce382b5d57ada270cfd08a1b24d)
                check_type(argname="argument flow_source", value=flow_source, expected_type=type_hints["flow_source"])
                check_type(argname="argument network_source", value=network_source, expected_type=type_hints["network_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if flow_source is not None:
                self._values["flow_source"] = flow_source
            if network_source is not None:
                self._values["network_source"] = network_source

        @builtins.property
        def flow_source(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeFlowSourceProperty"]]:
            '''The source of the bridge.

            A flow source originates in MediaConnect as an existing cloud flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgesource.html#cfn-mediaconnect-bridge-bridgesource-flowsource
            '''
            result = self._values.get("flow_source")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeFlowSourceProperty"]], result)

        @builtins.property
        def network_source(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeNetworkSourceProperty"]]:
            '''The source of the bridge.

            A network source originates at your premises.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgesource.html#cfn-mediaconnect-bridge-bridgesource-networksource
            '''
            result = self._values.get("network_source")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeNetworkSourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.EgressGatewayBridgeProperty",
        jsii_struct_bases=[],
        name_mapping={"max_bitrate": "maxBitrate"},
    )
    class EgressGatewayBridgeProperty:
        def __init__(self, *, max_bitrate: jsii.Number) -> None:
            '''Create a bridge with the egress bridge type.

            An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.

            :param max_bitrate: The maximum expected bitrate (in bps) of the egress bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-egressgatewaybridge.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                egress_gateway_bridge_property = mediaconnect.CfnBridge.EgressGatewayBridgeProperty(
                    max_bitrate=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b88384d6e7eaf984035fe7a0fba90d12833212086c785ad13a9117af87f05ec0)
                check_type(argname="argument max_bitrate", value=max_bitrate, expected_type=type_hints["max_bitrate"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_bitrate": max_bitrate,
            }

        @builtins.property
        def max_bitrate(self) -> jsii.Number:
            '''The maximum expected bitrate (in bps) of the egress bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-egressgatewaybridge.html#cfn-mediaconnect-bridge-egressgatewaybridge-maxbitrate
            '''
            result = self._values.get("max_bitrate")
            assert result is not None, "Required property 'max_bitrate' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EgressGatewayBridgeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.FailoverConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failover_mode": "failoverMode",
            "source_priority": "sourcePriority",
            "state": "state",
        },
    )
    class FailoverConfigProperty:
        def __init__(
            self,
            *,
            failover_mode: builtins.str,
            source_priority: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.SourcePriorityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for source failover.

            :param failover_mode: The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams.
            :param source_priority: The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.
            :param state: The state of source failover on the flow. If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                failover_config_property = mediaconnect.CfnBridge.FailoverConfigProperty(
                    failover_mode="failoverMode",
                
                    # the properties below are optional
                    source_priority=mediaconnect.CfnBridge.SourcePriorityProperty(
                        primary_source="primarySource"
                    ),
                    state="state"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2344e6b90e667c45e503f080b931cc817ed70f01054abb50495f2670d204d2b3)
                check_type(argname="argument failover_mode", value=failover_mode, expected_type=type_hints["failover_mode"])
                check_type(argname="argument source_priority", value=source_priority, expected_type=type_hints["source_priority"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "failover_mode": failover_mode,
            }
            if source_priority is not None:
                self._values["source_priority"] = source_priority
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def failover_mode(self) -> builtins.str:
            '''The type of failover you choose for this flow.

            MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html#cfn-mediaconnect-bridge-failoverconfig-failovermode
            '''
            result = self._values.get("failover_mode")
            assert result is not None, "Required property 'failover_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_priority(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.SourcePriorityProperty"]]:
            '''The priority you want to assign to a source.

            You can have a primary stream and a backup stream or two equally prioritized streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html#cfn-mediaconnect-bridge-failoverconfig-sourcepriority
            '''
            result = self._values.get("source_priority")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.SourcePriorityProperty"]], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''The state of source failover on the flow.

            If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html#cfn-mediaconnect-bridge-failoverconfig-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailoverConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.IngressGatewayBridgeProperty",
        jsii_struct_bases=[],
        name_mapping={"max_bitrate": "maxBitrate", "max_outputs": "maxOutputs"},
    )
    class IngressGatewayBridgeProperty:
        def __init__(
            self,
            *,
            max_bitrate: jsii.Number,
            max_outputs: jsii.Number,
        ) -> None:
            '''Create a bridge with the ingress bridge type.

            An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.

            :param max_bitrate: The maximum expected bitrate (in bps) of the ingress bridge.
            :param max_outputs: The maximum number of outputs on the ingress bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-ingressgatewaybridge.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                ingress_gateway_bridge_property = mediaconnect.CfnBridge.IngressGatewayBridgeProperty(
                    max_bitrate=123,
                    max_outputs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__167e9f3b8055cd05eb90612891a377cb4cde612ba7f0ec6b9e69f7d2df6ce8e6)
                check_type(argname="argument max_bitrate", value=max_bitrate, expected_type=type_hints["max_bitrate"])
                check_type(argname="argument max_outputs", value=max_outputs, expected_type=type_hints["max_outputs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_bitrate": max_bitrate,
                "max_outputs": max_outputs,
            }

        @builtins.property
        def max_bitrate(self) -> jsii.Number:
            '''The maximum expected bitrate (in bps) of the ingress bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-ingressgatewaybridge.html#cfn-mediaconnect-bridge-ingressgatewaybridge-maxbitrate
            '''
            result = self._values.get("max_bitrate")
            assert result is not None, "Required property 'max_bitrate' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_outputs(self) -> jsii.Number:
            '''The maximum number of outputs on the ingress bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-ingressgatewaybridge.html#cfn-mediaconnect-bridge-ingressgatewaybridge-maxoutputs
            '''
            result = self._values.get("max_outputs")
            assert result is not None, "Required property 'max_outputs' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IngressGatewayBridgeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.MulticastSourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"multicast_source_ip": "multicastSourceIp"},
    )
    class MulticastSourceSettingsProperty:
        def __init__(
            self,
            *,
            multicast_source_ip: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings related to the multicast source.

            :param multicast_source_ip: The IP address of the source for source-specific multicast (SSM).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-multicastsourcesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                multicast_source_settings_property = mediaconnect.CfnBridge.MulticastSourceSettingsProperty(
                    multicast_source_ip="multicastSourceIp"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6e23d21827eb73665886579f4c9de765df4e5ab5b7f9a9d2336b912b8e357707)
                check_type(argname="argument multicast_source_ip", value=multicast_source_ip, expected_type=type_hints["multicast_source_ip"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if multicast_source_ip is not None:
                self._values["multicast_source_ip"] = multicast_source_ip

        @builtins.property
        def multicast_source_ip(self) -> typing.Optional[builtins.str]:
            '''The IP address of the source for source-specific multicast (SSM).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-multicastsourcesettings.html#cfn-mediaconnect-bridge-multicastsourcesettings-multicastsourceip
            '''
            result = self._values.get("multicast_source_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MulticastSourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.SourcePriorityProperty",
        jsii_struct_bases=[],
        name_mapping={"primary_source": "primarySource"},
    )
    class SourcePriorityProperty:
        def __init__(
            self,
            *,
            primary_source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The priority you want to assign to a source.

            You can have a primary stream and a backup stream or two equally prioritized streams.

            :param primary_source: The name of the source you choose as the primary source for this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-sourcepriority.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                source_priority_property = mediaconnect.CfnBridge.SourcePriorityProperty(
                    primary_source="primarySource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__58ccd453e30991d345c7d1533308b0d3e5827af4b03a42b43534f313026666a0)
                check_type(argname="argument primary_source", value=primary_source, expected_type=type_hints["primary_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if primary_source is not None:
                self._values["primary_source"] = primary_source

        @builtins.property
        def primary_source(self) -> typing.Optional[builtins.str]:
            '''The name of the source you choose as the primary source for this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-sourcepriority.html#cfn-mediaconnect-bridge-sourcepriority-primarysource
            '''
            result = self._values.get("primary_source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourcePriorityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for attaching a VPC interface to an resource.

            :param vpc_interface_name: The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-vpcinterfaceattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_attachment_property = mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d7119bd5cac44e94824a018e0819faa64fdc04125060ad413d57b0a00d0a8066)
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-vpcinterfaceattachment.html#cfn-mediaconnect-bridge-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _IBridgeOutputRef_d8763e78)
class CfnBridgeOutput(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeOutput",
):
    '''Adds outputs to an existing bridge.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html
    :cloudformationResource: AWS::MediaConnect::BridgeOutput
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_bridge_output = mediaconnect.CfnBridgeOutput(self, "MyCfnBridgeOutput",
            bridge_arn="bridgeArn",
            name="name",
            network_output=mediaconnect.CfnBridgeOutput.BridgeNetworkOutputProperty(
                ip_address="ipAddress",
                network_name="networkName",
                port=123,
                protocol="protocol",
                ttl=123
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        bridge_arn: builtins.str,
        name: builtins.str,
        network_output: typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridgeOutput.BridgeNetworkOutputProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Create a new ``AWS::MediaConnect::BridgeOutput``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bridge_arn: The Amazon Resource Name (ARN) of the bridge that you want to update.
        :param name: The network output name. This name is used to reference the output and must be unique among outputs in this bridge.
        :param network_output: The network output of the bridge. A network output is delivered to your premises.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37400ec0d6ede2ac41f09e81db31275470bfb18f7999012a07d588a5abfc45e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBridgeOutputProps(
            bridge_arn=bridge_arn, name=name, network_output=network_output
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnBridgeOutput")
    @builtins.classmethod
    def is_cfn_bridge_output(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnBridgeOutput.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc406bff1020285bbe72922bef2d2aefa766c79f162aca8ee2e4a24ff7ff76ef)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnBridgeOutput", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb205f08441d39d8e1889501076cfae52006c266e0dcc55675d37bdd36eecce7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8dfc4c93ee2ec8174192f41cba8f3d6deeacc3ee4b3eeb41940e9f61c1b8c0a5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="bridgeOutputRef")
    def bridge_output_ref(self) -> "_BridgeOutputReference_4ac2cf5a":
        '''A reference to a BridgeOutput resource.'''
        return typing.cast("_BridgeOutputReference_4ac2cf5a", jsii.get(self, "bridgeOutputRef"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="bridgeArn")
    def bridge_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the bridge that you want to update.'''
        return typing.cast(builtins.str, jsii.get(self, "bridgeArn"))

    @bridge_arn.setter
    def bridge_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__238bd53ec2ae6381eaaf2c652a080561d1722805471e9d898d9d8e2b66530295)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bridgeArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The network output name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4567364d21ca9ebe1a2f33abcf1e7bc00c0f6b671c2062fd3c6766537faf1fa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkOutput")
    def network_output(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnBridgeOutput.BridgeNetworkOutputProperty"]:
        '''The network output of the bridge.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnBridgeOutput.BridgeNetworkOutputProperty"], jsii.get(self, "networkOutput"))

    @network_output.setter
    def network_output(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnBridgeOutput.BridgeNetworkOutputProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78fe544a540a0346bab7b296adf77b0088521ed5104d3678ee517ee4d8b43eb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkOutput", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeOutput.BridgeNetworkOutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ip_address": "ipAddress",
            "network_name": "networkName",
            "port": "port",
            "protocol": "protocol",
            "ttl": "ttl",
        },
    )
    class BridgeNetworkOutputProperty:
        def __init__(
            self,
            *,
            ip_address: builtins.str,
            network_name: builtins.str,
            port: jsii.Number,
            protocol: builtins.str,
            ttl: jsii.Number,
        ) -> None:
            '''The output of the bridge.

            A network output is delivered to your premises.

            :param ip_address: The network output IP address.
            :param network_name: The network output's gateway network name.
            :param port: The network output's port.
            :param protocol: The network output protocol. .. epigraph:: AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
            :param ttl: The network output TTL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_network_output_property = mediaconnect.CfnBridgeOutput.BridgeNetworkOutputProperty(
                    ip_address="ipAddress",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
                    ttl=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c8d614c4eaf3e7a9715a54c7d8f6d68001dfdd34bed46af49b236cf97208c5b)
                check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
                check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ip_address": ip_address,
                "network_name": network_name,
                "port": port,
                "protocol": protocol,
                "ttl": ttl,
            }

        @builtins.property
        def ip_address(self) -> builtins.str:
            '''The network output IP address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ipaddress
            '''
            result = self._values.get("ip_address")
            assert result is not None, "Required property 'ip_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_name(self) -> builtins.str:
            '''The network output's gateway network name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-networkname
            '''
            result = self._values.get("network_name")
            assert result is not None, "Required property 'network_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The network output's port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network output protocol.

            .. epigraph::

               AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ttl(self) -> jsii.Number:
            '''The network output TTL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ttl
            '''
            result = self._values.get("ttl")
            assert result is not None, "Required property 'ttl' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeNetworkOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeOutputProps",
    jsii_struct_bases=[],
    name_mapping={
        "bridge_arn": "bridgeArn",
        "name": "name",
        "network_output": "networkOutput",
    },
)
class CfnBridgeOutputProps:
    def __init__(
        self,
        *,
        bridge_arn: builtins.str,
        name: builtins.str,
        network_output: typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridgeOutput.BridgeNetworkOutputProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnBridgeOutput``.

        :param bridge_arn: The Amazon Resource Name (ARN) of the bridge that you want to update.
        :param name: The network output name. This name is used to reference the output and must be unique among outputs in this bridge.
        :param network_output: The network output of the bridge. A network output is delivered to your premises.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_bridge_output_props = mediaconnect.CfnBridgeOutputProps(
                bridge_arn="bridgeArn",
                name="name",
                network_output=mediaconnect.CfnBridgeOutput.BridgeNetworkOutputProperty(
                    ip_address="ipAddress",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
                    ttl=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c246f60ce4e5ad45fa8b46aaba3a5dc86b8fbceb04cd700ed6ecc964f18f2a)
            check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_output", value=network_output, expected_type=type_hints["network_output"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bridge_arn": bridge_arn,
            "name": name,
            "network_output": network_output,
        }

    @builtins.property
    def bridge_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the bridge that you want to update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html#cfn-mediaconnect-bridgeoutput-bridgearn
        '''
        result = self._values.get("bridge_arn")
        assert result is not None, "Required property 'bridge_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The network output name.

        This name is used to reference the output and must be unique among outputs in this bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html#cfn-mediaconnect-bridgeoutput-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_output(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnBridgeOutput.BridgeNetworkOutputProperty"]:
        '''The network output of the bridge.

        A network output is delivered to your premises.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html#cfn-mediaconnect-bridgeoutput-networkoutput
        '''
        result = self._values.get("network_output")
        assert result is not None, "Required property 'network_output' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnBridgeOutput.BridgeNetworkOutputProperty"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBridgeOutputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "placement_arn": "placementArn",
        "sources": "sources",
        "egress_gateway_bridge": "egressGatewayBridge",
        "ingress_gateway_bridge": "ingressGatewayBridge",
        "outputs": "outputs",
        "source_failover_config": "sourceFailoverConfig",
    },
)
class CfnBridgeProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        placement_arn: builtins.str,
        sources: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.BridgeSourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        egress_gateway_bridge: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.EgressGatewayBridgeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ingress_gateway_bridge: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.IngressGatewayBridgeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        outputs: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.BridgeOutputProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        source_failover_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridge.FailoverConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBridge``.

        :param name: The name of the bridge. This name can not be modified after the bridge is created.
        :param placement_arn: The bridge placement Amazon Resource Number (ARN).
        :param sources: The sources that you want to add to this bridge.
        :param egress_gateway_bridge: An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.
        :param ingress_gateway_bridge: An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.
        :param outputs: The outputs that you want to add to this bridge.
        :param source_failover_config: The settings for source failover.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_bridge_props = mediaconnect.CfnBridgeProps(
                name="name",
                placement_arn="placementArn",
                sources=[mediaconnect.CfnBridge.BridgeSourceProperty(
                    flow_source=mediaconnect.CfnBridge.BridgeFlowSourceProperty(
                        flow_arn="flowArn",
                        name="name",
            
                        # the properties below are optional
                        flow_vpc_interface_attachment=mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty(
                            vpc_interface_name="vpcInterfaceName"
                        )
                    ),
                    network_source=mediaconnect.CfnBridge.BridgeNetworkSourceProperty(
                        multicast_ip="multicastIp",
                        name="name",
                        network_name="networkName",
                        port=123,
                        protocol="protocol",
            
                        # the properties below are optional
                        multicast_source_settings=mediaconnect.CfnBridge.MulticastSourceSettingsProperty(
                            multicast_source_ip="multicastSourceIp"
                        )
                    )
                )],
            
                # the properties below are optional
                egress_gateway_bridge=mediaconnect.CfnBridge.EgressGatewayBridgeProperty(
                    max_bitrate=123
                ),
                ingress_gateway_bridge=mediaconnect.CfnBridge.IngressGatewayBridgeProperty(
                    max_bitrate=123,
                    max_outputs=123
                ),
                outputs=[mediaconnect.CfnBridge.BridgeOutputProperty(
                    network_output=mediaconnect.CfnBridge.BridgeNetworkOutputProperty(
                        ip_address="ipAddress",
                        name="name",
                        network_name="networkName",
                        port=123,
                        protocol="protocol",
                        ttl=123
                    )
                )],
                source_failover_config=mediaconnect.CfnBridge.FailoverConfigProperty(
                    failover_mode="failoverMode",
            
                    # the properties below are optional
                    source_priority=mediaconnect.CfnBridge.SourcePriorityProperty(
                        primary_source="primarySource"
                    ),
                    state="state"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73e5019972892e93be93b465cdd4743483355d6d745af2863fcbd2ab360c88ef)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument placement_arn", value=placement_arn, expected_type=type_hints["placement_arn"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument egress_gateway_bridge", value=egress_gateway_bridge, expected_type=type_hints["egress_gateway_bridge"])
            check_type(argname="argument ingress_gateway_bridge", value=ingress_gateway_bridge, expected_type=type_hints["ingress_gateway_bridge"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument source_failover_config", value=source_failover_config, expected_type=type_hints["source_failover_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "placement_arn": placement_arn,
            "sources": sources,
        }
        if egress_gateway_bridge is not None:
            self._values["egress_gateway_bridge"] = egress_gateway_bridge
        if ingress_gateway_bridge is not None:
            self._values["ingress_gateway_bridge"] = ingress_gateway_bridge
        if outputs is not None:
            self._values["outputs"] = outputs
        if source_failover_config is not None:
            self._values["source_failover_config"] = source_failover_config

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the bridge.

        This name can not be modified after the bridge is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def placement_arn(self) -> builtins.str:
        '''The bridge placement Amazon Resource Number (ARN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-placementarn
        '''
        result = self._values.get("placement_arn")
        assert result is not None, "Required property 'placement_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeSourceProperty"]]]:
        '''The sources that you want to add to this bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-sources
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeSourceProperty"]]], result)

    @builtins.property
    def egress_gateway_bridge(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.EgressGatewayBridgeProperty"]]:
        '''An egress bridge is a cloud-to-ground bridge.

        The content comes from an existing MediaConnect flow and is delivered to your premises.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-egressgatewaybridge
        '''
        result = self._values.get("egress_gateway_bridge")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.EgressGatewayBridgeProperty"]], result)

    @builtins.property
    def ingress_gateway_bridge(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.IngressGatewayBridgeProperty"]]:
        '''An ingress bridge is a ground-to-cloud bridge.

        The content originates at your premises and is delivered to the cloud.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-ingressgatewaybridge
        '''
        result = self._values.get("ingress_gateway_bridge")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.IngressGatewayBridgeProperty"]], result)

    @builtins.property
    def outputs(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeOutputProperty"]]]]:
        '''The outputs that you want to add to this bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-outputs
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnBridge.BridgeOutputProperty"]]]], result)

    @builtins.property
    def source_failover_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.FailoverConfigProperty"]]:
        '''The settings for source failover.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-sourcefailoverconfig
        '''
        result = self._values.get("source_failover_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridge.FailoverConfigProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBridgeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IBridgeSourceRef_8b16438d)
class CfnBridgeSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSource",
):
    '''Adds sources to an existing bridge.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html
    :cloudformationResource: AWS::MediaConnect::BridgeSource
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_bridge_source = mediaconnect.CfnBridgeSource(self, "MyCfnBridgeSource",
            bridge_arn="bridgeArn",
            name="name",
        
            # the properties below are optional
            flow_source=mediaconnect.CfnBridgeSource.BridgeFlowSourceProperty(
                flow_arn="flowArn",
        
                # the properties below are optional
                flow_vpc_interface_attachment=mediaconnect.CfnBridgeSource.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            ),
            network_source=mediaconnect.CfnBridgeSource.BridgeNetworkSourceProperty(
                multicast_ip="multicastIp",
                network_name="networkName",
                port=123,
                protocol="protocol",
        
                # the properties below are optional
                multicast_source_settings=mediaconnect.CfnBridgeSource.MulticastSourceSettingsProperty(
                    multicast_source_ip="multicastSourceIp"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        bridge_arn: builtins.str,
        name: builtins.str,
        flow_source: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridgeSource.BridgeFlowSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        network_source: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridgeSource.BridgeNetworkSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::BridgeSource``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bridge_arn: The ARN of the bridge feeding this flow.
        :param name: The name of the flow source. This name is used to reference the source and must be unique among sources in this bridge.
        :param flow_source: The source of the flow.
        :param network_source: The source of the network.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e36e10c04a0f01de7ebc0521a5800daea1daa62e3bd343704ff6e84525f6f408)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBridgeSourceProps(
            bridge_arn=bridge_arn,
            name=name,
            flow_source=flow_source,
            network_source=network_source,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnBridgeSource")
    @builtins.classmethod
    def is_cfn_bridge_source(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnBridgeSource.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c9c15695da88b46044324b66fa4fc2c80ce78a1c90ef0b5016473957483a3e8)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnBridgeSource", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ee6617fa681b5aaf625fc2493bb4ea5b5e578a01029bdd7ba2b8647be429130)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64ce37bd7d5055cf2fb388e369c965f5e01fd162753e68839b53dd0443911c4b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="bridgeSourceRef")
    def bridge_source_ref(self) -> "_BridgeSourceReference_fdd405eb":
        '''A reference to a BridgeSource resource.'''
        return typing.cast("_BridgeSourceReference_fdd405eb", jsii.get(self, "bridgeSourceRef"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="bridgeArn")
    def bridge_arn(self) -> builtins.str:
        '''The ARN of the bridge feeding this flow.'''
        return typing.cast(builtins.str, jsii.get(self, "bridgeArn"))

    @bridge_arn.setter
    def bridge_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28bb545b11a59b0c10f19770b49da21586071508bfbed47b6b137ab43e2aaa5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bridgeArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the flow source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ff480997cae96d755e2b7e83019229c27702f843cafce3fc5647020ec7d7a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowSource")
    def flow_source(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.BridgeFlowSourceProperty"]]:
        '''The source of the flow.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.BridgeFlowSourceProperty"]], jsii.get(self, "flowSource"))

    @flow_source.setter
    def flow_source(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.BridgeFlowSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa9a2d6952ebe510d69e3877d36b01cb4f6aa83e11dfcf61576bdfaffa0dea74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowSource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkSource")
    def network_source(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.BridgeNetworkSourceProperty"]]:
        '''The source of the network.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.BridgeNetworkSourceProperty"]], jsii.get(self, "networkSource"))

    @network_source.setter
    def network_source(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.BridgeNetworkSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afb1ff783738c431282bcaa0dec602d425b3f5a39195a1f65e4e683ba344caea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkSource", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSource.BridgeFlowSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "flow_arn": "flowArn",
            "flow_vpc_interface_attachment": "flowVpcInterfaceAttachment",
        },
    )
    class BridgeFlowSourceProperty:
        def __init__(
            self,
            *,
            flow_arn: builtins.str,
            flow_vpc_interface_attachment: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridgeSource.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source of the bridge.

            A flow source originates in MediaConnect as an existing cloud flow.

            :param flow_arn: The ARN of the cloud flow used as a source of this bridge.
            :param flow_vpc_interface_attachment: The name of the VPC interface attachment to use for this source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgeflowsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_flow_source_property = mediaconnect.CfnBridgeSource.BridgeFlowSourceProperty(
                    flow_arn="flowArn",
                
                    # the properties below are optional
                    flow_vpc_interface_attachment=mediaconnect.CfnBridgeSource.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8bb9109e42561a117540865cd31be3adb19651461f90f2af2ac7c6ce75a0c13e)
                check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
                check_type(argname="argument flow_vpc_interface_attachment", value=flow_vpc_interface_attachment, expected_type=type_hints["flow_vpc_interface_attachment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "flow_arn": flow_arn,
            }
            if flow_vpc_interface_attachment is not None:
                self._values["flow_vpc_interface_attachment"] = flow_vpc_interface_attachment

        @builtins.property
        def flow_arn(self) -> builtins.str:
            '''The ARN of the cloud flow used as a source of this bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgeflowsource.html#cfn-mediaconnect-bridgesource-bridgeflowsource-flowarn
            '''
            result = self._values.get("flow_arn")
            assert result is not None, "Required property 'flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def flow_vpc_interface_attachment(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.VpcInterfaceAttachmentProperty"]]:
            '''The name of the VPC interface attachment to use for this source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgeflowsource.html#cfn-mediaconnect-bridgesource-bridgeflowsource-flowvpcinterfaceattachment
            '''
            result = self._values.get("flow_vpc_interface_attachment")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.VpcInterfaceAttachmentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeFlowSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSource.BridgeNetworkSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "multicast_ip": "multicastIp",
            "network_name": "networkName",
            "port": "port",
            "protocol": "protocol",
            "multicast_source_settings": "multicastSourceSettings",
        },
    )
    class BridgeNetworkSourceProperty:
        def __init__(
            self,
            *,
            multicast_ip: builtins.str,
            network_name: builtins.str,
            port: jsii.Number,
            protocol: builtins.str,
            multicast_source_settings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridgeSource.MulticastSourceSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source of the bridge.

            A network source originates at your premises.

            :param multicast_ip: The network source multicast IP.
            :param network_name: The network source's gateway network name.
            :param port: The network source port.
            :param protocol: The network source protocol. .. epigraph:: AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
            :param multicast_source_settings: The settings related to the multicast source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_network_source_property = mediaconnect.CfnBridgeSource.BridgeNetworkSourceProperty(
                    multicast_ip="multicastIp",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
                
                    # the properties below are optional
                    multicast_source_settings=mediaconnect.CfnBridgeSource.MulticastSourceSettingsProperty(
                        multicast_source_ip="multicastSourceIp"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__93b2199f774afbb32a622ba44ca26954c8e46e149f1bc0836b1dda198de28020)
                check_type(argname="argument multicast_ip", value=multicast_ip, expected_type=type_hints["multicast_ip"])
                check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument multicast_source_settings", value=multicast_source_settings, expected_type=type_hints["multicast_source_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "multicast_ip": multicast_ip,
                "network_name": network_name,
                "port": port,
                "protocol": protocol,
            }
            if multicast_source_settings is not None:
                self._values["multicast_source_settings"] = multicast_source_settings

        @builtins.property
        def multicast_ip(self) -> builtins.str:
            '''The network source multicast IP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-multicastip
            '''
            result = self._values.get("multicast_ip")
            assert result is not None, "Required property 'multicast_ip' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_name(self) -> builtins.str:
            '''The network source's gateway network name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-networkname
            '''
            result = self._values.get("network_name")
            assert result is not None, "Required property 'network_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The network source port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network source protocol.

            .. epigraph::

               AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def multicast_source_settings(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.MulticastSourceSettingsProperty"]]:
            '''The settings related to the multicast source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-multicastsourcesettings
            '''
            result = self._values.get("multicast_source_settings")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.MulticastSourceSettingsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeNetworkSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSource.MulticastSourceSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"multicast_source_ip": "multicastSourceIp"},
    )
    class MulticastSourceSettingsProperty:
        def __init__(
            self,
            *,
            multicast_source_ip: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings related to the multicast source.

            :param multicast_source_ip: The IP address of the source for source-specific multicast (SSM).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-multicastsourcesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                multicast_source_settings_property = mediaconnect.CfnBridgeSource.MulticastSourceSettingsProperty(
                    multicast_source_ip="multicastSourceIp"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__43fa91d86269952c92522f3e880b2f507aa1cc51cd5dbe28fb9249f61e4324cd)
                check_type(argname="argument multicast_source_ip", value=multicast_source_ip, expected_type=type_hints["multicast_source_ip"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if multicast_source_ip is not None:
                self._values["multicast_source_ip"] = multicast_source_ip

        @builtins.property
        def multicast_source_ip(self) -> typing.Optional[builtins.str]:
            '''The IP address of the source for source-specific multicast (SSM).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-multicastsourcesettings.html#cfn-mediaconnect-bridgesource-multicastsourcesettings-multicastsourceip
            '''
            result = self._values.get("multicast_source_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MulticastSourceSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSource.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for attaching a VPC interface to an resource.

            :param vpc_interface_name: The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-vpcinterfaceattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_attachment_property = mediaconnect.CfnBridgeSource.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e6d9b48314e46735258c941180d8e92fa25af944c2b991fb6827ccc97fa800b4)
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-vpcinterfaceattachment.html#cfn-mediaconnect-bridgesource-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "bridge_arn": "bridgeArn",
        "name": "name",
        "flow_source": "flowSource",
        "network_source": "networkSource",
    },
)
class CfnBridgeSourceProps:
    def __init__(
        self,
        *,
        bridge_arn: builtins.str,
        name: builtins.str,
        flow_source: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridgeSource.BridgeFlowSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        network_source: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnBridgeSource.BridgeNetworkSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBridgeSource``.

        :param bridge_arn: The ARN of the bridge feeding this flow.
        :param name: The name of the flow source. This name is used to reference the source and must be unique among sources in this bridge.
        :param flow_source: The source of the flow.
        :param network_source: The source of the network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_bridge_source_props = mediaconnect.CfnBridgeSourceProps(
                bridge_arn="bridgeArn",
                name="name",
            
                # the properties below are optional
                flow_source=mediaconnect.CfnBridgeSource.BridgeFlowSourceProperty(
                    flow_arn="flowArn",
            
                    # the properties below are optional
                    flow_vpc_interface_attachment=mediaconnect.CfnBridgeSource.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                ),
                network_source=mediaconnect.CfnBridgeSource.BridgeNetworkSourceProperty(
                    multicast_ip="multicastIp",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
            
                    # the properties below are optional
                    multicast_source_settings=mediaconnect.CfnBridgeSource.MulticastSourceSettingsProperty(
                        multicast_source_ip="multicastSourceIp"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f2a15e5c2c97898000fd91706ed5ee02d0a7d5d31640d04f545d4db3c27ec23)
            check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument flow_source", value=flow_source, expected_type=type_hints["flow_source"])
            check_type(argname="argument network_source", value=network_source, expected_type=type_hints["network_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bridge_arn": bridge_arn,
            "name": name,
        }
        if flow_source is not None:
            self._values["flow_source"] = flow_source
        if network_source is not None:
            self._values["network_source"] = network_source

    @builtins.property
    def bridge_arn(self) -> builtins.str:
        '''The ARN of the bridge feeding this flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-bridgearn
        '''
        result = self._values.get("bridge_arn")
        assert result is not None, "Required property 'bridge_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the flow source.

        This name is used to reference the source and must be unique among sources in this bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flow_source(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.BridgeFlowSourceProperty"]]:
        '''The source of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-flowsource
        '''
        result = self._values.get("flow_source")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.BridgeFlowSourceProperty"]], result)

    @builtins.property
    def network_source(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.BridgeNetworkSourceProperty"]]:
        '''The source of the network.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-networksource
        '''
        result = self._values.get("network_source")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnBridgeSource.BridgeNetworkSourceProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBridgeSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IFlowRef_c5e8f48d)
class CfnFlow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow",
):
    '''The ``AWS::MediaConnect::Flow`` resource defines a connection between one or more video sources and one or more outputs.

    For each flow, you specify the transport protocol to use, encryption information, and details for any outputs or entitlements that you want. AWS Elemental MediaConnect returns an ingest endpoint where you can send your live video as a single unicast stream. The service replicates and distributes the video to every output that you specify, whether inside or outside the AWS Cloud. You can also set up entitlements on a flow to allow other AWS accounts to access your content.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html
    :cloudformationResource: AWS::MediaConnect::Flow
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        # automatic: Any
        
        cfn_flow = mediaconnect.CfnFlow(self, "MyCfnFlow",
            name="name",
            source=mediaconnect.CfnFlow.SourceProperty(
                decryption=mediaconnect.CfnFlow.EncryptionProperty(
                    role_arn="roleArn",
        
                    # the properties below are optional
                    algorithm="algorithm",
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                ),
                description="description",
                entitlement_arn="entitlementArn",
                gateway_bridge_source=mediaconnect.CfnFlow.GatewayBridgeSourceProperty(
                    bridge_arn="bridgeArn",
        
                    # the properties below are optional
                    vpc_interface_attachment=mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                ),
                ingest_ip="ingestIp",
                ingest_port=123,
                max_bitrate=123,
                max_latency=123,
                max_sync_buffer=123,
                media_stream_source_configurations=[mediaconnect.CfnFlow.MediaStreamSourceConfigurationProperty(
                    encoding_name="encodingName",
                    media_stream_name="mediaStreamName",
        
                    # the properties below are optional
                    input_configurations=[mediaconnect.CfnFlow.InputConfigurationProperty(
                        input_port=123,
                        interface=mediaconnect.CfnFlow.InterfaceProperty(
                            name="name"
                        )
                    )]
                )],
                min_latency=123,
                name="name",
                protocol="protocol",
                router_integration_state="routerIntegrationState",
                router_integration_transit_decryption=mediaconnect.CfnFlow.FlowTransitEncryptionProperty(
                    encryption_key_configuration=mediaconnect.CfnFlow.FlowTransitEncryptionKeyConfigurationProperty(
                        automatic=automatic,
                        secrets_manager=mediaconnect.CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
        
                    # the properties below are optional
                    encryption_key_type="encryptionKeyType"
                ),
                sender_control_port=123,
                sender_ip_address="senderIpAddress",
                source_arn="sourceArn",
                source_ingest_port="sourceIngestPort",
                source_listener_address="sourceListenerAddress",
                source_listener_port=123,
                stream_id="streamId",
                vpc_interface_name="vpcInterfaceName",
                whitelist_cidr="whitelistCidr"
            ),
        
            # the properties below are optional
            availability_zone="availabilityZone",
            flow_size="flowSize",
            maintenance=mediaconnect.CfnFlow.MaintenanceProperty(
                maintenance_day="maintenanceDay",
                maintenance_start_hour="maintenanceStartHour"
            ),
            media_streams=[mediaconnect.CfnFlow.MediaStreamProperty(
                media_stream_id=123,
                media_stream_name="mediaStreamName",
                media_stream_type="mediaStreamType",
        
                # the properties below are optional
                attributes=mediaconnect.CfnFlow.MediaStreamAttributesProperty(
                    fmtp=mediaconnect.CfnFlow.FmtpProperty(
                        channel_order="channelOrder",
                        colorimetry="colorimetry",
                        exact_framerate="exactFramerate",
                        par="par",
                        range="range",
                        scan_mode="scanMode",
                        tcs="tcs"
                    ),
                    lang="lang"
                ),
                clock_rate=123,
                description="description",
                fmt=123,
                video_format="videoFormat"
            )],
            ndi_config=mediaconnect.CfnFlow.NdiConfigProperty(
                machine_name="machineName",
                ndi_discovery_servers=[mediaconnect.CfnFlow.NdiDiscoveryServerConfigProperty(
                    discovery_server_address="discoveryServerAddress",
                    vpc_interface_adapter="vpcInterfaceAdapter",
        
                    # the properties below are optional
                    discovery_server_port=123
                )],
                ndi_state="ndiState"
            ),
            source_failover_config=mediaconnect.CfnFlow.FailoverConfigProperty(
                failover_mode="failoverMode",
                recovery_window=123,
                source_priority=mediaconnect.CfnFlow.SourcePriorityProperty(
                    primary_source="primarySource"
                ),
                state="state"
            ),
            source_monitoring_config=mediaconnect.CfnFlow.SourceMonitoringConfigProperty(
                audio_monitoring_settings=[mediaconnect.CfnFlow.AudioMonitoringSettingProperty(
                    silent_audio=mediaconnect.CfnFlow.SilentAudioProperty(
                        state="state",
                        threshold_seconds=123
                    )
                )],
                content_quality_analysis_state="contentQualityAnalysisState",
                thumbnail_state="thumbnailState",
                video_monitoring_settings=[mediaconnect.CfnFlow.VideoMonitoringSettingProperty(
                    black_frames=mediaconnect.CfnFlow.BlackFramesProperty(
                        state="state",
                        threshold_seconds=123
                    ),
                    frozen_frames=mediaconnect.CfnFlow.FrozenFramesProperty(
                        state="state",
                        threshold_seconds=123
                    )
                )]
            ),
            vpc_interfaces=[mediaconnect.CfnFlow.VpcInterfaceProperty(
                name="name",
                role_arn="roleArn",
                security_group_ids=["securityGroupIds"],
                subnet_id="subnetId",
        
                # the properties below are optional
                network_interface_ids=["networkInterfaceIds"],
                network_interface_type="networkInterfaceType"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        source: typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.SourceProperty", typing.Dict[builtins.str, typing.Any]]],
        availability_zone: typing.Optional[builtins.str] = None,
        flow_size: typing.Optional[builtins.str] = None,
        maintenance: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.MaintenanceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        media_streams: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.MediaStreamProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ndi_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.NdiConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_failover_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.FailoverConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_monitoring_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.SourceMonitoringConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_interfaces: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.VpcInterfaceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::Flow``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the flow.
        :param source: The settings for the source that you want to use for the new flow.
        :param availability_zone: The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS Region.
        :param flow_size: Determines the processing capacity and feature set of the flow. Set this optional parameter to LARGE if you want to enable NDI outputs on the flow.
        :param maintenance: The maintenance settings you want to use for the flow.
        :param media_streams: The media streams that are associated with the flow. After you associate a media stream with a source, you can also associate it with outputs on the flow.
        :param ndi_config: Specifies the configuration settings for NDI outputs. Required when the flow includes NDI outputs.
        :param source_failover_config: The settings for source failover.
        :param source_monitoring_config: The settings for source monitoring.
        :param vpc_interfaces: The VPC Interfaces for this flow.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3568a95be2a886825b3db731f10e2fdea8be142c554d1e2055d7e22f5e6a3991)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowProps(
            name=name,
            source=source,
            availability_zone=availability_zone,
            flow_size=flow_size,
            maintenance=maintenance,
            media_streams=media_streams,
            ndi_config=ndi_config,
            source_failover_config=source_failover_config,
            source_monitoring_config=source_monitoring_config,
            vpc_interfaces=vpc_interfaces,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForFlow")
    @builtins.classmethod
    def arn_for_flow(cls, resource: "_IFlowRef_c5e8f48d") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c54b3021fd089afdcef76ee7ca3c18274773c4b4384f46a6700f34b567e51aa4)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForFlow", [resource]))

    @jsii.member(jsii_name="isCfnFlow")
    @builtins.classmethod
    def is_cfn_flow(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFlow.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b34fb3378a823873473e36770156bfc974eb22a36bab11daaf47bd382948fda7)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFlow", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3bf65a3dfd8c719cb8ba7cde45e0dc8693f2306db4dba4cd6da5e4727579cc7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8244ccdcee08a7984c185f2ee476300520ed80658ec1efcbcb9634a230a0687a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEgressIp")
    def attr_egress_ip(self) -> builtins.str:
        '''The IP address from which video will be sent to output destinations.

        :cloudformationAttribute: EgressIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEgressIp"))

    @builtins.property
    @jsii.member(jsii_name="attrFlowArn")
    def attr_flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow.

        :cloudformationAttribute: FlowArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFlowArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFlowAvailabilityZone")
    def attr_flow_availability_zone(self) -> builtins.str:
        '''The Availability Zone that the flow was created in.

        These options are limited to the Availability Zones within the current AWS Region.

        :cloudformationAttribute: FlowAvailabilityZone
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFlowAvailabilityZone"))

    @builtins.property
    @jsii.member(jsii_name="attrFlowNdiMachineName")
    def attr_flow_ndi_machine_name(self) -> builtins.str:
        '''This read-only value represents the automatically-generated NDI machine name that MediaConnect generated for this flow.

        These NDI machine names are only generated when you don't specify your own custom name.

        :cloudformationAttribute: FlowNdiMachineName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFlowNdiMachineName"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceIngestIp")
    def attr_source_ingest_ip(self) -> builtins.str:
        '''The IP address that the flow listens on for incoming content.

        :cloudformationAttribute: Source.IngestIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceIngestIp"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceSourceArn")
    def attr_source_source_arn(self) -> builtins.str:
        '''The ARN of the source.

        :cloudformationAttribute: Source.SourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceSourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceSourceIngestPort")
    def attr_source_source_ingest_port(self) -> builtins.str:
        '''The port that the flow listens on for incoming content.

        If the protocol of the source is Zixi, the port must be set to 2088.

        :cloudformationAttribute: Source.SourceIngestPort
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceSourceIngestPort"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="flowRef")
    def flow_ref(self) -> "_FlowReference_cf80a510":
        '''A reference to a Flow resource.'''
        return typing.cast("_FlowReference_cf80a510", jsii.get(self, "flowRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the flow.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b9dd07005f4a1ea040eea97dccca156a16f5e9f3f6686139fbd52108ac4c3b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> typing.Union["_IResolvable_da3f097b", "CfnFlow.SourceProperty"]:
        '''The settings for the source that you want to use for the new flow.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnFlow.SourceProperty"], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnFlow.SourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__869299c75adeb5a7d478686f55b98acba18c279372a76486ab2c6231b1e54e54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone that you want to create the flow in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__843065332a6d7586586605a6ec8a2bd932a36dd6774052d60e5f9fd8e52c280c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowSize")
    def flow_size(self) -> typing.Optional[builtins.str]:
        '''Determines the processing capacity and feature set of the flow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowSize"))

    @flow_size.setter
    def flow_size(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18797920a62f69ac5303a95d3356fc95d49473634b7f27d9e7ef811a4ad6cb34)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowSize", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maintenance")
    def maintenance(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.MaintenanceProperty"]]:
        '''The maintenance settings you want to use for the flow.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.MaintenanceProperty"]], jsii.get(self, "maintenance"))

    @maintenance.setter
    def maintenance(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.MaintenanceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd188e9c2d5f8f194cf0b4c16e8b355b0ebcec43d953e6b0c8b77128e640aab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenance", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mediaStreams")
    def media_streams(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.MediaStreamProperty"]]]]:
        '''The media streams that are associated with the flow.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.MediaStreamProperty"]]]], jsii.get(self, "mediaStreams"))

    @media_streams.setter
    def media_streams(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.MediaStreamProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c580931c160d15b8c0f43f0fe96dc390b640ae81cbc1900b00f369aaa3c3f6e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaStreams", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ndiConfig")
    def ndi_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.NdiConfigProperty"]]:
        '''Specifies the configuration settings for NDI outputs.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.NdiConfigProperty"]], jsii.get(self, "ndiConfig"))

    @ndi_config.setter
    def ndi_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.NdiConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f78a65c7535e71bd81a721df5718188077330f02b6d7cdd75ebb5693c7db1cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ndiConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceFailoverConfig")
    def source_failover_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FailoverConfigProperty"]]:
        '''The settings for source failover.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FailoverConfigProperty"]], jsii.get(self, "sourceFailoverConfig"))

    @source_failover_config.setter
    def source_failover_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FailoverConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7deae7edf526ef9a6af2e16b592ef198ecb0cc777d1c7d97f392933ad97ef6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFailoverConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceMonitoringConfig")
    def source_monitoring_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SourceMonitoringConfigProperty"]]:
        '''The settings for source monitoring.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SourceMonitoringConfigProperty"]], jsii.get(self, "sourceMonitoringConfig"))

    @source_monitoring_config.setter
    def source_monitoring_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SourceMonitoringConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03a0a0b12b76b8e0b7700d38b27d7f2ca928ad701fe5600b9bad475822621b98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceMonitoringConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcInterfaces")
    def vpc_interfaces(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.VpcInterfaceProperty"]]]]:
        '''The VPC Interfaces for this flow.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.VpcInterfaceProperty"]]]], jsii.get(self, "vpcInterfaces"))

    @vpc_interfaces.setter
    def vpc_interfaces(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.VpcInterfaceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e75424871a1b67422fa8fe727bf0720abe8ea217c131244844ca71d14e25f4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcInterfaces", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.AudioMonitoringSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"silent_audio": "silentAudio"},
    )
    class AudioMonitoringSettingProperty:
        def __init__(
            self,
            *,
            silent_audio: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.SilentAudioProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the configuration for audio stream metrics monitoring.

            :param silent_audio: Detects periods of silence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-audiomonitoringsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                audio_monitoring_setting_property = mediaconnect.CfnFlow.AudioMonitoringSettingProperty(
                    silent_audio=mediaconnect.CfnFlow.SilentAudioProperty(
                        state="state",
                        threshold_seconds=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1ac15d313eb79141f926e0599cfa8d16a302729713ebc92bf0a1af7adbf56f21)
                check_type(argname="argument silent_audio", value=silent_audio, expected_type=type_hints["silent_audio"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if silent_audio is not None:
                self._values["silent_audio"] = silent_audio

        @builtins.property
        def silent_audio(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SilentAudioProperty"]]:
            '''Detects periods of silence.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-audiomonitoringsetting.html#cfn-mediaconnect-flow-audiomonitoringsetting-silentaudio
            '''
            result = self._values.get("silent_audio")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SilentAudioProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AudioMonitoringSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.BlackFramesProperty",
        jsii_struct_bases=[],
        name_mapping={"state": "state", "threshold_seconds": "thresholdSeconds"},
    )
    class BlackFramesProperty:
        def __init__(
            self,
            *,
            state: typing.Optional[builtins.str] = None,
            threshold_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configures settings for the ``BlackFrames`` metric.

            :param state: Indicates whether the ``BlackFrames`` metric is enabled or disabled..
            :param threshold_seconds: Specifies the number of consecutive seconds of black frames that triggers an event or alert.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-blackframes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                black_frames_property = mediaconnect.CfnFlow.BlackFramesProperty(
                    state="state",
                    threshold_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8eed2a01102ad4205f67e0e6efdd3aaeca33633021098b7b3d1d73054d386f3)
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
                check_type(argname="argument threshold_seconds", value=threshold_seconds, expected_type=type_hints["threshold_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if state is not None:
                self._values["state"] = state
            if threshold_seconds is not None:
                self._values["threshold_seconds"] = threshold_seconds

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''Indicates whether the ``BlackFrames`` metric is enabled or disabled..

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-blackframes.html#cfn-mediaconnect-flow-blackframes-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def threshold_seconds(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of consecutive seconds of black frames that triggers an event or alert.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-blackframes.html#cfn-mediaconnect-flow-blackframes-thresholdseconds
            '''
            result = self._values.get("threshold_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlackFramesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "algorithm": "algorithm",
            "constant_initialization_vector": "constantInitializationVector",
            "device_id": "deviceId",
            "key_type": "keyType",
            "region": "region",
            "resource_id": "resourceId",
            "secret_arn": "secretArn",
            "url": "url",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            algorithm: typing.Optional[builtins.str] = None,
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            device_id: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Encryption information.

            :param role_arn: The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).
            :param algorithm: The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256). If you are using SPEKE or SRT-password encryption, this property must be left blank.
            :param constant_initialization_vector: A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
            :param device_id: The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param key_type: The type of key that is used for the encryption. If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` . Default: - "static-key"
            :param region: The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param resource_id: An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param secret_arn: The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
            :param url: The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                encryption_property = mediaconnect.CfnFlow.EncryptionProperty(
                    role_arn="roleArn",
                
                    # the properties below are optional
                    algorithm="algorithm",
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__023b62e8b380bcfa878c2a07568bc0d0f9912919827c329972ee2130250892b3)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument constant_initialization_vector", value=constant_initialization_vector, expected_type=type_hints["constant_initialization_vector"])
                check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
            }
            if algorithm is not None:
                self._values["algorithm"] = algorithm
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if device_id is not None:
                self._values["device_id"] = device_id
            if key_type is not None:
                self._values["key_type"] = key_type
            if region is not None:
                self._values["region"] = region
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def algorithm(self) -> typing.Optional[builtins.str]:
            '''The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256).

            If you are using SPEKE or SRT-password encryption, this property must be left blank.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content.

            This parameter is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_id(self) -> typing.Optional[builtins.str]:
            '''The value of one of the devices that you configured with your digital rights management (DRM) platform key provider.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-deviceid
            '''
            result = self._values.get("device_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''The type of key that is used for the encryption.

            If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` .

            :default: - "static-key"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region that the API Gateway proxy endpoint was created in.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''An identifier for the content.

            The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.

            This parameter is required for static key encryption and is not valid for SPEKE encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL from the API Gateway proxy that you set up to talk to your key server.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.FailoverConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failover_mode": "failoverMode",
            "recovery_window": "recoveryWindow",
            "source_priority": "sourcePriority",
            "state": "state",
        },
    )
    class FailoverConfigProperty:
        def __init__(
            self,
            *,
            failover_mode: typing.Optional[builtins.str] = None,
            recovery_window: typing.Optional[jsii.Number] = None,
            source_priority: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.SourcePriorityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for source failover.

            :param failover_mode: The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams. The string for this property must be entered as MERGE or FAILOVER. No other string entry is valid.
            :param recovery_window: Search window time to look for dash-7 packets.
            :param source_priority: The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.
            :param state: The state of source failover on the flow. If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                failover_config_property = mediaconnect.CfnFlow.FailoverConfigProperty(
                    failover_mode="failoverMode",
                    recovery_window=123,
                    source_priority=mediaconnect.CfnFlow.SourcePriorityProperty(
                        primary_source="primarySource"
                    ),
                    state="state"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__60d936fe41cb44293e591fd7a9b89da19bc9fc2509d0dacf4ad7a22a54e1bae9)
                check_type(argname="argument failover_mode", value=failover_mode, expected_type=type_hints["failover_mode"])
                check_type(argname="argument recovery_window", value=recovery_window, expected_type=type_hints["recovery_window"])
                check_type(argname="argument source_priority", value=source_priority, expected_type=type_hints["source_priority"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if failover_mode is not None:
                self._values["failover_mode"] = failover_mode
            if recovery_window is not None:
                self._values["recovery_window"] = recovery_window
            if source_priority is not None:
                self._values["source_priority"] = source_priority
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def failover_mode(self) -> typing.Optional[builtins.str]:
            '''The type of failover you choose for this flow.

            MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams. The string for this property must be entered as MERGE or FAILOVER. No other string entry is valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-failovermode
            '''
            result = self._values.get("failover_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def recovery_window(self) -> typing.Optional[jsii.Number]:
            '''Search window time to look for dash-7 packets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-recoverywindow
            '''
            result = self._values.get("recovery_window")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def source_priority(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SourcePriorityProperty"]]:
            '''The priority you want to assign to a source.

            You can have a primary stream and a backup stream or two equally prioritized streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-sourcepriority
            '''
            result = self._values.get("source_priority")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SourcePriorityProperty"]], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''The state of source failover on the flow.

            If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailoverConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.FlowTransitEncryptionKeyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"automatic": "automatic", "secrets_manager": "secretsManager"},
    )
    class FlowTransitEncryptionKeyConfigurationProperty:
        def __init__(
            self,
            *,
            automatic: typing.Any = None,
            secrets_manager: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param automatic: Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.
            :param secrets_manager: The configuration settings for transit encryption of a flow source using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-flowtransitencryptionkeyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                flow_transit_encryption_key_configuration_property = mediaconnect.CfnFlow.FlowTransitEncryptionKeyConfigurationProperty(
                    automatic=automatic,
                    secrets_manager=mediaconnect.CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b52880d31b637a0af3233aa7f316659377893fb1e181334df40136a484a6a792)
                check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
                check_type(argname="argument secrets_manager", value=secrets_manager, expected_type=type_hints["secrets_manager"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if automatic is not None:
                self._values["automatic"] = automatic
            if secrets_manager is not None:
                self._values["secrets_manager"] = secrets_manager

        @builtins.property
        def automatic(self) -> typing.Any:
            '''Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-flowtransitencryptionkeyconfiguration.html#cfn-mediaconnect-flow-flowtransitencryptionkeyconfiguration-automatic
            '''
            result = self._values.get("automatic")
            return typing.cast(typing.Any, result)

        @builtins.property
        def secrets_manager(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty"]]:
            '''The configuration settings for transit encryption of a flow source using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-flowtransitencryptionkeyconfiguration.html#cfn-mediaconnect-flow-flowtransitencryptionkeyconfiguration-secretsmanager
            '''
            result = self._values.get("secrets_manager")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowTransitEncryptionKeyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.FlowTransitEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_key_configuration": "encryptionKeyConfiguration",
            "encryption_key_type": "encryptionKeyType",
        },
    )
    class FlowTransitEncryptionProperty:
        def __init__(
            self,
            *,
            encryption_key_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.FlowTransitEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            encryption_key_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.

            :param encryption_key_configuration: Configuration settings for flow transit encryption keys.
            :param encryption_key_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-flowtransitencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                flow_transit_encryption_property = mediaconnect.CfnFlow.FlowTransitEncryptionProperty(
                    encryption_key_configuration=mediaconnect.CfnFlow.FlowTransitEncryptionKeyConfigurationProperty(
                        automatic=automatic,
                        secrets_manager=mediaconnect.CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
                
                    # the properties below are optional
                    encryption_key_type="encryptionKeyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1ed20d2d2ea0c830d5eb7613de0a9e624da82a886e597f4f6c66d0b5c6c3259f)
                check_type(argname="argument encryption_key_configuration", value=encryption_key_configuration, expected_type=type_hints["encryption_key_configuration"])
                check_type(argname="argument encryption_key_type", value=encryption_key_type, expected_type=type_hints["encryption_key_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_key_configuration": encryption_key_configuration,
            }
            if encryption_key_type is not None:
                self._values["encryption_key_type"] = encryption_key_type

        @builtins.property
        def encryption_key_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnFlow.FlowTransitEncryptionKeyConfigurationProperty"]:
            '''Configuration settings for flow transit encryption keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-flowtransitencryption.html#cfn-mediaconnect-flow-flowtransitencryption-encryptionkeyconfiguration
            '''
            result = self._values.get("encryption_key_configuration")
            assert result is not None, "Required property 'encryption_key_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnFlow.FlowTransitEncryptionKeyConfigurationProperty"], result)

        @builtins.property
        def encryption_key_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-flowtransitencryption.html#cfn-mediaconnect-flow-flowtransitencryption-encryptionkeytype
            '''
            result = self._values.get("encryption_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowTransitEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.FmtpProperty",
        jsii_struct_bases=[],
        name_mapping={
            "channel_order": "channelOrder",
            "colorimetry": "colorimetry",
            "exact_framerate": "exactFramerate",
            "par": "par",
            "range": "range",
            "scan_mode": "scanMode",
            "tcs": "tcs",
        },
    )
    class FmtpProperty:
        def __init__(
            self,
            *,
            channel_order: typing.Optional[builtins.str] = None,
            colorimetry: typing.Optional[builtins.str] = None,
            exact_framerate: typing.Optional[builtins.str] = None,
            par: typing.Optional[builtins.str] = None,
            range: typing.Optional[builtins.str] = None,
            scan_mode: typing.Optional[builtins.str] = None,
            tcs: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A set of parameters that define the media stream.

            :param channel_order: The format of the audio channel.
            :param colorimetry: The format used for the representation of color.
            :param exact_framerate: The frame rate for the video stream, in frames/second. For example: 60000/1001.
            :param par: The pixel aspect ratio (PAR) of the video.
            :param range: The encoding range of the video.
            :param scan_mode: The type of compression that was used to smooth the video’s appearance.
            :param tcs: The transfer characteristic system (TCS) that is used in the video.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-fmtp.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                fmtp_property = mediaconnect.CfnFlow.FmtpProperty(
                    channel_order="channelOrder",
                    colorimetry="colorimetry",
                    exact_framerate="exactFramerate",
                    par="par",
                    range="range",
                    scan_mode="scanMode",
                    tcs="tcs"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c34da6d27a4d46f87384739bd6ec7bcc9bf7866bb051703aa63a4b21e8b38dc)
                check_type(argname="argument channel_order", value=channel_order, expected_type=type_hints["channel_order"])
                check_type(argname="argument colorimetry", value=colorimetry, expected_type=type_hints["colorimetry"])
                check_type(argname="argument exact_framerate", value=exact_framerate, expected_type=type_hints["exact_framerate"])
                check_type(argname="argument par", value=par, expected_type=type_hints["par"])
                check_type(argname="argument range", value=range, expected_type=type_hints["range"])
                check_type(argname="argument scan_mode", value=scan_mode, expected_type=type_hints["scan_mode"])
                check_type(argname="argument tcs", value=tcs, expected_type=type_hints["tcs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if channel_order is not None:
                self._values["channel_order"] = channel_order
            if colorimetry is not None:
                self._values["colorimetry"] = colorimetry
            if exact_framerate is not None:
                self._values["exact_framerate"] = exact_framerate
            if par is not None:
                self._values["par"] = par
            if range is not None:
                self._values["range"] = range
            if scan_mode is not None:
                self._values["scan_mode"] = scan_mode
            if tcs is not None:
                self._values["tcs"] = tcs

        @builtins.property
        def channel_order(self) -> typing.Optional[builtins.str]:
            '''The format of the audio channel.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-fmtp.html#cfn-mediaconnect-flow-fmtp-channelorder
            '''
            result = self._values.get("channel_order")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def colorimetry(self) -> typing.Optional[builtins.str]:
            '''The format used for the representation of color.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-fmtp.html#cfn-mediaconnect-flow-fmtp-colorimetry
            '''
            result = self._values.get("colorimetry")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exact_framerate(self) -> typing.Optional[builtins.str]:
            '''The frame rate for the video stream, in frames/second.

            For example: 60000/1001.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-fmtp.html#cfn-mediaconnect-flow-fmtp-exactframerate
            '''
            result = self._values.get("exact_framerate")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def par(self) -> typing.Optional[builtins.str]:
            '''The pixel aspect ratio (PAR) of the video.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-fmtp.html#cfn-mediaconnect-flow-fmtp-par
            '''
            result = self._values.get("par")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def range(self) -> typing.Optional[builtins.str]:
            '''The encoding range of the video.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-fmtp.html#cfn-mediaconnect-flow-fmtp-range
            '''
            result = self._values.get("range")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scan_mode(self) -> typing.Optional[builtins.str]:
            '''The type of compression that was used to smooth the video’s appearance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-fmtp.html#cfn-mediaconnect-flow-fmtp-scanmode
            '''
            result = self._values.get("scan_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tcs(self) -> typing.Optional[builtins.str]:
            '''The transfer characteristic system (TCS) that is used in the video.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-fmtp.html#cfn-mediaconnect-flow-fmtp-tcs
            '''
            result = self._values.get("tcs")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FmtpProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.FrozenFramesProperty",
        jsii_struct_bases=[],
        name_mapping={"state": "state", "threshold_seconds": "thresholdSeconds"},
    )
    class FrozenFramesProperty:
        def __init__(
            self,
            *,
            state: typing.Optional[builtins.str] = None,
            threshold_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configures settings for the ``FrozenFrames`` metric.

            :param state: Indicates whether the ``FrozenFrames`` metric is enabled or disabled.
            :param threshold_seconds: Specifies the number of consecutive seconds of a static image that triggers an event or alert.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-frozenframes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                frozen_frames_property = mediaconnect.CfnFlow.FrozenFramesProperty(
                    state="state",
                    threshold_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__261e148d056da084128b3530c69f370bb4b4b5d73098e06d42eb6c5c4d6025e5)
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
                check_type(argname="argument threshold_seconds", value=threshold_seconds, expected_type=type_hints["threshold_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if state is not None:
                self._values["state"] = state
            if threshold_seconds is not None:
                self._values["threshold_seconds"] = threshold_seconds

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''Indicates whether the ``FrozenFrames`` metric is enabled or disabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-frozenframes.html#cfn-mediaconnect-flow-frozenframes-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def threshold_seconds(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of consecutive seconds of a static image that triggers an event or alert.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-frozenframes.html#cfn-mediaconnect-flow-frozenframes-thresholdseconds
            '''
            result = self._values.get("threshold_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FrozenFramesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.GatewayBridgeSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bridge_arn": "bridgeArn",
            "vpc_interface_attachment": "vpcInterfaceAttachment",
        },
    )
    class GatewayBridgeSourceProperty:
        def __init__(
            self,
            *,
            bridge_arn: builtins.str,
            vpc_interface_attachment: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source configuration for cloud flows receiving a stream from a bridge.

            :param bridge_arn: The ARN of the bridge feeding this flow.
            :param vpc_interface_attachment: The name of the VPC interface attachment to use for this bridge source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-gatewaybridgesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                gateway_bridge_source_property = mediaconnect.CfnFlow.GatewayBridgeSourceProperty(
                    bridge_arn="bridgeArn",
                
                    # the properties below are optional
                    vpc_interface_attachment=mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__00bf15dc37f493c33d6b2109cfa6283d2bb14bdc23b0ae4fd75a67ca60084ea8)
                check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
                check_type(argname="argument vpc_interface_attachment", value=vpc_interface_attachment, expected_type=type_hints["vpc_interface_attachment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bridge_arn": bridge_arn,
            }
            if vpc_interface_attachment is not None:
                self._values["vpc_interface_attachment"] = vpc_interface_attachment

        @builtins.property
        def bridge_arn(self) -> builtins.str:
            '''The ARN of the bridge feeding this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-gatewaybridgesource.html#cfn-mediaconnect-flow-gatewaybridgesource-bridgearn
            '''
            result = self._values.get("bridge_arn")
            assert result is not None, "Required property 'bridge_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_interface_attachment(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.VpcInterfaceAttachmentProperty"]]:
            '''The name of the VPC interface attachment to use for this bridge source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-gatewaybridgesource.html#cfn-mediaconnect-flow-gatewaybridgesource-vpcinterfaceattachment
            '''
            result = self._values.get("vpc_interface_attachment")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.VpcInterfaceAttachmentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayBridgeSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.InputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"input_port": "inputPort", "interface": "interface"},
    )
    class InputConfigurationProperty:
        def __init__(
            self,
            *,
            input_port: jsii.Number,
            interface: typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.InterfaceProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The transport parameters that are associated with an incoming media stream.

            :param input_port: The port that the flow listens on for an incoming media stream.
            :param interface: The VPC interface where the media stream comes in from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-inputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                input_configuration_property = mediaconnect.CfnFlow.InputConfigurationProperty(
                    input_port=123,
                    interface=mediaconnect.CfnFlow.InterfaceProperty(
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fbb4a04e87ed2fedc67d03bbbab23670facee0c55014d0c5d234881ded41ec58)
                check_type(argname="argument input_port", value=input_port, expected_type=type_hints["input_port"])
                check_type(argname="argument interface", value=interface, expected_type=type_hints["interface"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "input_port": input_port,
                "interface": interface,
            }

        @builtins.property
        def input_port(self) -> jsii.Number:
            '''The port that the flow listens on for an incoming media stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-inputconfiguration.html#cfn-mediaconnect-flow-inputconfiguration-inputport
            '''
            result = self._values.get("input_port")
            assert result is not None, "Required property 'input_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def interface(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnFlow.InterfaceProperty"]:
            '''The VPC interface where the media stream comes in from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-inputconfiguration.html#cfn-mediaconnect-flow-inputconfiguration-interface
            '''
            result = self._values.get("interface")
            assert result is not None, "Required property 'interface' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnFlow.InterfaceProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.InterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class InterfaceProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''The VPC interface that is used for the media stream associated with the source or output.

            :param name: The name of the VPC interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-interface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                interface_property = mediaconnect.CfnFlow.InterfaceProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0ca0a6498a5e542f31081d78420cae2b37457c94dbd68dcead2dc4af50843b27)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the VPC interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-interface.html#cfn-mediaconnect-flow-interface-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.MaintenanceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maintenance_day": "maintenanceDay",
            "maintenance_start_hour": "maintenanceStartHour",
        },
    )
    class MaintenanceProperty:
        def __init__(
            self,
            *,
            maintenance_day: builtins.str,
            maintenance_start_hour: builtins.str,
        ) -> None:
            '''The maintenance setting of a flow.

            :param maintenance_day: A day of a week when the maintenance will happen. Use Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday.
            :param maintenance_start_hour: UTC time when the maintenance will happen. Use 24-hour HH:MM format. Minutes must be 00. Example: 13:00. The default value is 02:00.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-maintenance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                maintenance_property = mediaconnect.CfnFlow.MaintenanceProperty(
                    maintenance_day="maintenanceDay",
                    maintenance_start_hour="maintenanceStartHour"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57efc1d88b4fa5a6e6df4c17678237b4420bf63b5cd14e340198e67ed5a1ee60)
                check_type(argname="argument maintenance_day", value=maintenance_day, expected_type=type_hints["maintenance_day"])
                check_type(argname="argument maintenance_start_hour", value=maintenance_start_hour, expected_type=type_hints["maintenance_start_hour"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "maintenance_day": maintenance_day,
                "maintenance_start_hour": maintenance_start_hour,
            }

        @builtins.property
        def maintenance_day(self) -> builtins.str:
            '''A day of a week when the maintenance will happen.

            Use Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-maintenance.html#cfn-mediaconnect-flow-maintenance-maintenanceday
            '''
            result = self._values.get("maintenance_day")
            assert result is not None, "Required property 'maintenance_day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def maintenance_start_hour(self) -> builtins.str:
            '''UTC time when the maintenance will happen.

            Use 24-hour HH:MM format. Minutes must be 00. Example: 13:00. The default value is 02:00.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-maintenance.html#cfn-mediaconnect-flow-maintenance-maintenancestarthour
            '''
            result = self._values.get("maintenance_start_hour")
            assert result is not None, "Required property 'maintenance_start_hour' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.MediaStreamAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"fmtp": "fmtp", "lang": "lang"},
    )
    class MediaStreamAttributesProperty:
        def __init__(
            self,
            *,
            fmtp: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.FmtpProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lang: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Attributes that are related to the media stream.

            :param fmtp: The settings that you want to use to define the media stream.
            :param lang: The audio language, in a format that is recognized by the receiver.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastreamattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                media_stream_attributes_property = mediaconnect.CfnFlow.MediaStreamAttributesProperty(
                    fmtp=mediaconnect.CfnFlow.FmtpProperty(
                        channel_order="channelOrder",
                        colorimetry="colorimetry",
                        exact_framerate="exactFramerate",
                        par="par",
                        range="range",
                        scan_mode="scanMode",
                        tcs="tcs"
                    ),
                    lang="lang"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__98c9c952274e74dd38a0129bccf9e3c8688c812151f95c826ce99e20158cfe87)
                check_type(argname="argument fmtp", value=fmtp, expected_type=type_hints["fmtp"])
                check_type(argname="argument lang", value=lang, expected_type=type_hints["lang"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if fmtp is not None:
                self._values["fmtp"] = fmtp
            if lang is not None:
                self._values["lang"] = lang

        @builtins.property
        def fmtp(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FmtpProperty"]]:
            '''The settings that you want to use to define the media stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastreamattributes.html#cfn-mediaconnect-flow-mediastreamattributes-fmtp
            '''
            result = self._values.get("fmtp")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FmtpProperty"]], result)

        @builtins.property
        def lang(self) -> typing.Optional[builtins.str]:
            '''The audio language, in a format that is recognized by the receiver.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastreamattributes.html#cfn-mediaconnect-flow-mediastreamattributes-lang
            '''
            result = self._values.get("lang")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaStreamAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.MediaStreamProperty",
        jsii_struct_bases=[],
        name_mapping={
            "media_stream_id": "mediaStreamId",
            "media_stream_name": "mediaStreamName",
            "media_stream_type": "mediaStreamType",
            "attributes": "attributes",
            "clock_rate": "clockRate",
            "description": "description",
            "fmt": "fmt",
            "video_format": "videoFormat",
        },
    )
    class MediaStreamProperty:
        def __init__(
            self,
            *,
            media_stream_id: jsii.Number,
            media_stream_name: builtins.str,
            media_stream_type: builtins.str,
            attributes: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.MediaStreamAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            clock_rate: typing.Optional[jsii.Number] = None,
            description: typing.Optional[builtins.str] = None,
            fmt: typing.Optional[jsii.Number] = None,
            video_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A media stream represents one component of your content, such as video, audio, or ancillary data.

            After you add a media stream to your flow, you can associate it with sources and outputs that use the ST 2110 JPEG XS or CDI protocol.

            :param media_stream_id: A unique identifier for the media stream.
            :param media_stream_name: A name that helps you distinguish one media stream from another.
            :param media_stream_type: The type of media stream.
            :param attributes: Attributes that are related to the media stream.
            :param clock_rate: The sample rate for the stream. This value is measured in Hz.
            :param description: A description that can help you quickly identify what your media stream is used for.
            :param fmt: The format type number (sometimes referred to as RTP payload type) of the media stream. MediaConnect assigns this value to the media stream. For ST 2110 JPEG XS outputs, you need to provide this value to the receiver.
            :param video_format: The resolution of the video.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastream.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                media_stream_property = mediaconnect.CfnFlow.MediaStreamProperty(
                    media_stream_id=123,
                    media_stream_name="mediaStreamName",
                    media_stream_type="mediaStreamType",
                
                    # the properties below are optional
                    attributes=mediaconnect.CfnFlow.MediaStreamAttributesProperty(
                        fmtp=mediaconnect.CfnFlow.FmtpProperty(
                            channel_order="channelOrder",
                            colorimetry="colorimetry",
                            exact_framerate="exactFramerate",
                            par="par",
                            range="range",
                            scan_mode="scanMode",
                            tcs="tcs"
                        ),
                        lang="lang"
                    ),
                    clock_rate=123,
                    description="description",
                    fmt=123,
                    video_format="videoFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc935e241ba7a00b3f70633b9ca54a5bca516c17065e6c6d8eeb7ab2523359be)
                check_type(argname="argument media_stream_id", value=media_stream_id, expected_type=type_hints["media_stream_id"])
                check_type(argname="argument media_stream_name", value=media_stream_name, expected_type=type_hints["media_stream_name"])
                check_type(argname="argument media_stream_type", value=media_stream_type, expected_type=type_hints["media_stream_type"])
                check_type(argname="argument attributes", value=attributes, expected_type=type_hints["attributes"])
                check_type(argname="argument clock_rate", value=clock_rate, expected_type=type_hints["clock_rate"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument fmt", value=fmt, expected_type=type_hints["fmt"])
                check_type(argname="argument video_format", value=video_format, expected_type=type_hints["video_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "media_stream_id": media_stream_id,
                "media_stream_name": media_stream_name,
                "media_stream_type": media_stream_type,
            }
            if attributes is not None:
                self._values["attributes"] = attributes
            if clock_rate is not None:
                self._values["clock_rate"] = clock_rate
            if description is not None:
                self._values["description"] = description
            if fmt is not None:
                self._values["fmt"] = fmt
            if video_format is not None:
                self._values["video_format"] = video_format

        @builtins.property
        def media_stream_id(self) -> jsii.Number:
            '''A unique identifier for the media stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastream.html#cfn-mediaconnect-flow-mediastream-mediastreamid
            '''
            result = self._values.get("media_stream_id")
            assert result is not None, "Required property 'media_stream_id' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def media_stream_name(self) -> builtins.str:
            '''A name that helps you distinguish one media stream from another.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastream.html#cfn-mediaconnect-flow-mediastream-mediastreamname
            '''
            result = self._values.get("media_stream_name")
            assert result is not None, "Required property 'media_stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def media_stream_type(self) -> builtins.str:
            '''The type of media stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastream.html#cfn-mediaconnect-flow-mediastream-mediastreamtype
            '''
            result = self._values.get("media_stream_type")
            assert result is not None, "Required property 'media_stream_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def attributes(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.MediaStreamAttributesProperty"]]:
            '''Attributes that are related to the media stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastream.html#cfn-mediaconnect-flow-mediastream-attributes
            '''
            result = self._values.get("attributes")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.MediaStreamAttributesProperty"]], result)

        @builtins.property
        def clock_rate(self) -> typing.Optional[jsii.Number]:
            '''The sample rate for the stream.

            This value is measured in Hz.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastream.html#cfn-mediaconnect-flow-mediastream-clockrate
            '''
            result = self._values.get("clock_rate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description that can help you quickly identify what your media stream is used for.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastream.html#cfn-mediaconnect-flow-mediastream-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fmt(self) -> typing.Optional[jsii.Number]:
            '''The format type number (sometimes referred to as RTP payload type) of the media stream.

            MediaConnect assigns this value to the media stream. For ST 2110 JPEG XS outputs, you need to provide this value to the receiver.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastream.html#cfn-mediaconnect-flow-mediastream-fmt
            '''
            result = self._values.get("fmt")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def video_format(self) -> typing.Optional[builtins.str]:
            '''The resolution of the video.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastream.html#cfn-mediaconnect-flow-mediastream-videoformat
            '''
            result = self._values.get("video_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaStreamProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.MediaStreamSourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encoding_name": "encodingName",
            "media_stream_name": "mediaStreamName",
            "input_configurations": "inputConfigurations",
        },
    )
    class MediaStreamSourceConfigurationProperty:
        def __init__(
            self,
            *,
            encoding_name: builtins.str,
            media_stream_name: builtins.str,
            input_configurations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.InputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The media stream that is associated with the source, and the parameters for that association.

            :param encoding_name: The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.
            :param media_stream_name: A name that helps you distinguish one media stream from another.
            :param input_configurations: The media streams that you want to associate with the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastreamsourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                media_stream_source_configuration_property = mediaconnect.CfnFlow.MediaStreamSourceConfigurationProperty(
                    encoding_name="encodingName",
                    media_stream_name="mediaStreamName",
                
                    # the properties below are optional
                    input_configurations=[mediaconnect.CfnFlow.InputConfigurationProperty(
                        input_port=123,
                        interface=mediaconnect.CfnFlow.InterfaceProperty(
                            name="name"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c288224888dcd985ea78c20d06801a00405d4260bf960e8dbcac65f3e669aa4f)
                check_type(argname="argument encoding_name", value=encoding_name, expected_type=type_hints["encoding_name"])
                check_type(argname="argument media_stream_name", value=media_stream_name, expected_type=type_hints["media_stream_name"])
                check_type(argname="argument input_configurations", value=input_configurations, expected_type=type_hints["input_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encoding_name": encoding_name,
                "media_stream_name": media_stream_name,
            }
            if input_configurations is not None:
                self._values["input_configurations"] = input_configurations

        @builtins.property
        def encoding_name(self) -> builtins.str:
            '''The format that was used to encode the data.

            For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastreamsourceconfiguration.html#cfn-mediaconnect-flow-mediastreamsourceconfiguration-encodingname
            '''
            result = self._values.get("encoding_name")
            assert result is not None, "Required property 'encoding_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def media_stream_name(self) -> builtins.str:
            '''A name that helps you distinguish one media stream from another.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastreamsourceconfiguration.html#cfn-mediaconnect-flow-mediastreamsourceconfiguration-mediastreamname
            '''
            result = self._values.get("media_stream_name")
            assert result is not None, "Required property 'media_stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def input_configurations(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.InputConfigurationProperty"]]]]:
            '''The media streams that you want to associate with the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-mediastreamsourceconfiguration.html#cfn-mediaconnect-flow-mediastreamsourceconfiguration-inputconfigurations
            '''
            result = self._values.get("input_configurations")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.InputConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaStreamSourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.NdiConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "machine_name": "machineName",
            "ndi_discovery_servers": "ndiDiscoveryServers",
            "ndi_state": "ndiState",
        },
    )
    class NdiConfigProperty:
        def __init__(
            self,
            *,
            machine_name: typing.Optional[builtins.str] = None,
            ndi_discovery_servers: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.NdiDiscoveryServerConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ndi_state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration settings for NDI outputs.

            Required when the flow includes NDI outputs.

            :param machine_name: A prefix for the names of the NDI sources that the flow creates. If a custom name isn't specified, MediaConnect generates a unique 12-character ID as the prefix.
            :param ndi_discovery_servers: A list of up to three NDI discovery server configurations. While not required by the API, this configuration is necessary for NDI functionality to work properly.
            :param ndi_state: A setting that controls whether NDI outputs can be used in the flow. Must be ENABLED to add NDI outputs. Default is DISABLED.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-ndiconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                ndi_config_property = mediaconnect.CfnFlow.NdiConfigProperty(
                    machine_name="machineName",
                    ndi_discovery_servers=[mediaconnect.CfnFlow.NdiDiscoveryServerConfigProperty(
                        discovery_server_address="discoveryServerAddress",
                        vpc_interface_adapter="vpcInterfaceAdapter",
                
                        # the properties below are optional
                        discovery_server_port=123
                    )],
                    ndi_state="ndiState"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__69742b949cc5728340bd262c9cb8f8127e5a045369699ab15384d6ad5532a7f7)
                check_type(argname="argument machine_name", value=machine_name, expected_type=type_hints["machine_name"])
                check_type(argname="argument ndi_discovery_servers", value=ndi_discovery_servers, expected_type=type_hints["ndi_discovery_servers"])
                check_type(argname="argument ndi_state", value=ndi_state, expected_type=type_hints["ndi_state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if machine_name is not None:
                self._values["machine_name"] = machine_name
            if ndi_discovery_servers is not None:
                self._values["ndi_discovery_servers"] = ndi_discovery_servers
            if ndi_state is not None:
                self._values["ndi_state"] = ndi_state

        @builtins.property
        def machine_name(self) -> typing.Optional[builtins.str]:
            '''A prefix for the names of the NDI sources that the flow creates.

            If a custom name isn't specified, MediaConnect generates a unique 12-character ID as the prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-ndiconfig.html#cfn-mediaconnect-flow-ndiconfig-machinename
            '''
            result = self._values.get("machine_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ndi_discovery_servers(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.NdiDiscoveryServerConfigProperty"]]]]:
            '''A list of up to three NDI discovery server configurations.

            While not required by the API, this configuration is necessary for NDI functionality to work properly.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-ndiconfig.html#cfn-mediaconnect-flow-ndiconfig-ndidiscoveryservers
            '''
            result = self._values.get("ndi_discovery_servers")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.NdiDiscoveryServerConfigProperty"]]]], result)

        @builtins.property
        def ndi_state(self) -> typing.Optional[builtins.str]:
            '''A setting that controls whether NDI outputs can be used in the flow.

            Must be ENABLED to add NDI outputs. Default is DISABLED.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-ndiconfig.html#cfn-mediaconnect-flow-ndiconfig-ndistate
            '''
            result = self._values.get("ndi_state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NdiConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.NdiDiscoveryServerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "discovery_server_address": "discoveryServerAddress",
            "vpc_interface_adapter": "vpcInterfaceAdapter",
            "discovery_server_port": "discoveryServerPort",
        },
    )
    class NdiDiscoveryServerConfigProperty:
        def __init__(
            self,
            *,
            discovery_server_address: builtins.str,
            vpc_interface_adapter: builtins.str,
            discovery_server_port: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies the configuration settings for individual NDI discovery servers.

            A maximum of 3 servers is allowed.

            :param discovery_server_address: The unique network address of the NDI discovery server.
            :param vpc_interface_adapter: The identifier for the Virtual Private Cloud (VPC) network interface used by the flow.
            :param discovery_server_port: The port for the NDI discovery server. Defaults to 5959 if a custom port isn't specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-ndidiscoveryserverconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                ndi_discovery_server_config_property = mediaconnect.CfnFlow.NdiDiscoveryServerConfigProperty(
                    discovery_server_address="discoveryServerAddress",
                    vpc_interface_adapter="vpcInterfaceAdapter",
                
                    # the properties below are optional
                    discovery_server_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cbd4bce903dd6a95ae93f0b2ca90f98d0d48bb24eebe475acf326160c51d3435)
                check_type(argname="argument discovery_server_address", value=discovery_server_address, expected_type=type_hints["discovery_server_address"])
                check_type(argname="argument vpc_interface_adapter", value=vpc_interface_adapter, expected_type=type_hints["vpc_interface_adapter"])
                check_type(argname="argument discovery_server_port", value=discovery_server_port, expected_type=type_hints["discovery_server_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "discovery_server_address": discovery_server_address,
                "vpc_interface_adapter": vpc_interface_adapter,
            }
            if discovery_server_port is not None:
                self._values["discovery_server_port"] = discovery_server_port

        @builtins.property
        def discovery_server_address(self) -> builtins.str:
            '''The unique network address of the NDI discovery server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-ndidiscoveryserverconfig.html#cfn-mediaconnect-flow-ndidiscoveryserverconfig-discoveryserveraddress
            '''
            result = self._values.get("discovery_server_address")
            assert result is not None, "Required property 'discovery_server_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_interface_adapter(self) -> builtins.str:
            '''The identifier for the Virtual Private Cloud (VPC) network interface used by the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-ndidiscoveryserverconfig.html#cfn-mediaconnect-flow-ndidiscoveryserverconfig-vpcinterfaceadapter
            '''
            result = self._values.get("vpc_interface_adapter")
            assert result is not None, "Required property 'vpc_interface_adapter' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def discovery_server_port(self) -> typing.Optional[jsii.Number]:
            '''The port for the NDI discovery server.

            Defaults to 5959 if a custom port isn't specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-ndidiscoveryserverconfig.html#cfn-mediaconnect-flow-ndidiscoveryserverconfig-discoveryserverport
            '''
            result = self._values.get("discovery_server_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NdiDiscoveryServerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "secret_arn": "secretArn"},
    )
    class SecretsManagerEncryptionKeyConfigurationProperty:
        def __init__(self, *, role_arn: builtins.str, secret_arn: builtins.str) -> None:
            '''The configuration settings for transit encryption of a flow source using AWS Secrets Manager, including the secret ARN and role ARN.

            :param role_arn: The ARN of the IAM role used for transit encryption from the router output using AWS Secrets Manager.
            :param secret_arn: The ARN of the AWS Secrets Manager secret used for transit encryption from the router output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                secrets_manager_encryption_key_configuration_property = mediaconnect.CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6448e00f3099cbc8bc0d9c871cb06fad1c988a5fae8ed52ee99e7b4398735c6e)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "secret_arn": secret_arn,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role used for transit encryption from the router output using AWS Secrets Manager.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration.html#cfn-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The ARN of the AWS Secrets Manager secret used for transit encryption from the router output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration.html#cfn-mediaconnect-flow-secretsmanagerencryptionkeyconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretsManagerEncryptionKeyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.SilentAudioProperty",
        jsii_struct_bases=[],
        name_mapping={"state": "state", "threshold_seconds": "thresholdSeconds"},
    )
    class SilentAudioProperty:
        def __init__(
            self,
            *,
            state: typing.Optional[builtins.str] = None,
            threshold_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configures settings for the ``SilentAudio`` metric.

            :param state: Indicates whether the ``SilentAudio`` metric is enabled or disabled.
            :param threshold_seconds: Specifies the number of consecutive seconds of silence that triggers an event or alert.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-silentaudio.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                silent_audio_property = mediaconnect.CfnFlow.SilentAudioProperty(
                    state="state",
                    threshold_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e28708aca7aa0aae7b96e1c58983b1ac8f27275c71b78ca026802bea4a53ffd6)
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
                check_type(argname="argument threshold_seconds", value=threshold_seconds, expected_type=type_hints["threshold_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if state is not None:
                self._values["state"] = state
            if threshold_seconds is not None:
                self._values["threshold_seconds"] = threshold_seconds

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''Indicates whether the ``SilentAudio`` metric is enabled or disabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-silentaudio.html#cfn-mediaconnect-flow-silentaudio-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def threshold_seconds(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of consecutive seconds of silence that triggers an event or alert.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-silentaudio.html#cfn-mediaconnect-flow-silentaudio-thresholdseconds
            '''
            result = self._values.get("threshold_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SilentAudioProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.SourceMonitoringConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "audio_monitoring_settings": "audioMonitoringSettings",
            "content_quality_analysis_state": "contentQualityAnalysisState",
            "thumbnail_state": "thumbnailState",
            "video_monitoring_settings": "videoMonitoringSettings",
        },
    )
    class SourceMonitoringConfigProperty:
        def __init__(
            self,
            *,
            audio_monitoring_settings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.AudioMonitoringSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            content_quality_analysis_state: typing.Optional[builtins.str] = None,
            thumbnail_state: typing.Optional[builtins.str] = None,
            video_monitoring_settings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.VideoMonitoringSettingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``SourceMonitoringConfig`` property type specifies the source monitoring settings for an ``AWS::MediaConnect::Flow`` .

            :param audio_monitoring_settings: Contains the settings for audio stream metrics monitoring.
            :param content_quality_analysis_state: Indicates whether content quality analysis is enabled or disabled.
            :param thumbnail_state: The current state of the thumbnail monitoring. - If you don't explicitly specify a value when creating a flow, no thumbnail state will be set. - If you update an existing flow and remove a previously set thumbnail state, the value will change to ``DISABLED`` .
            :param video_monitoring_settings: Contains the settings for video stream metrics monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcemonitoringconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                source_monitoring_config_property = mediaconnect.CfnFlow.SourceMonitoringConfigProperty(
                    audio_monitoring_settings=[mediaconnect.CfnFlow.AudioMonitoringSettingProperty(
                        silent_audio=mediaconnect.CfnFlow.SilentAudioProperty(
                            state="state",
                            threshold_seconds=123
                        )
                    )],
                    content_quality_analysis_state="contentQualityAnalysisState",
                    thumbnail_state="thumbnailState",
                    video_monitoring_settings=[mediaconnect.CfnFlow.VideoMonitoringSettingProperty(
                        black_frames=mediaconnect.CfnFlow.BlackFramesProperty(
                            state="state",
                            threshold_seconds=123
                        ),
                        frozen_frames=mediaconnect.CfnFlow.FrozenFramesProperty(
                            state="state",
                            threshold_seconds=123
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__462b2e03950e94b47455b1cc22dd388c278a29615998512d70aa7513e3c8d698)
                check_type(argname="argument audio_monitoring_settings", value=audio_monitoring_settings, expected_type=type_hints["audio_monitoring_settings"])
                check_type(argname="argument content_quality_analysis_state", value=content_quality_analysis_state, expected_type=type_hints["content_quality_analysis_state"])
                check_type(argname="argument thumbnail_state", value=thumbnail_state, expected_type=type_hints["thumbnail_state"])
                check_type(argname="argument video_monitoring_settings", value=video_monitoring_settings, expected_type=type_hints["video_monitoring_settings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if audio_monitoring_settings is not None:
                self._values["audio_monitoring_settings"] = audio_monitoring_settings
            if content_quality_analysis_state is not None:
                self._values["content_quality_analysis_state"] = content_quality_analysis_state
            if thumbnail_state is not None:
                self._values["thumbnail_state"] = thumbnail_state
            if video_monitoring_settings is not None:
                self._values["video_monitoring_settings"] = video_monitoring_settings

        @builtins.property
        def audio_monitoring_settings(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.AudioMonitoringSettingProperty"]]]]:
            '''Contains the settings for audio stream metrics monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcemonitoringconfig.html#cfn-mediaconnect-flow-sourcemonitoringconfig-audiomonitoringsettings
            '''
            result = self._values.get("audio_monitoring_settings")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.AudioMonitoringSettingProperty"]]]], result)

        @builtins.property
        def content_quality_analysis_state(self) -> typing.Optional[builtins.str]:
            '''Indicates whether content quality analysis is enabled or disabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcemonitoringconfig.html#cfn-mediaconnect-flow-sourcemonitoringconfig-contentqualityanalysisstate
            '''
            result = self._values.get("content_quality_analysis_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def thumbnail_state(self) -> typing.Optional[builtins.str]:
            '''The current state of the thumbnail monitoring.

            - If you don't explicitly specify a value when creating a flow, no thumbnail state will be set.
            - If you update an existing flow and remove a previously set thumbnail state, the value will change to ``DISABLED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcemonitoringconfig.html#cfn-mediaconnect-flow-sourcemonitoringconfig-thumbnailstate
            '''
            result = self._values.get("thumbnail_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def video_monitoring_settings(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.VideoMonitoringSettingProperty"]]]]:
            '''Contains the settings for video stream metrics monitoring.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcemonitoringconfig.html#cfn-mediaconnect-flow-sourcemonitoringconfig-videomonitoringsettings
            '''
            result = self._values.get("video_monitoring_settings")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.VideoMonitoringSettingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceMonitoringConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.SourcePriorityProperty",
        jsii_struct_bases=[],
        name_mapping={"primary_source": "primarySource"},
    )
    class SourcePriorityProperty:
        def __init__(self, *, primary_source: builtins.str) -> None:
            '''The priority you want to assign to a source.

            You can have a primary stream and a backup stream or two equally prioritized streams.

            :param primary_source: The name of the source you choose as the primary source for this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcepriority.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                source_priority_property = mediaconnect.CfnFlow.SourcePriorityProperty(
                    primary_source="primarySource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a502d8c706596e3abd881dc963357d969893e22e8d25e78085445e09c58ac78b)
                check_type(argname="argument primary_source", value=primary_source, expected_type=type_hints["primary_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "primary_source": primary_source,
            }

        @builtins.property
        def primary_source(self) -> builtins.str:
            '''The name of the source you choose as the primary source for this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcepriority.html#cfn-mediaconnect-flow-sourcepriority-primarysource
            '''
            result = self._values.get("primary_source")
            assert result is not None, "Required property 'primary_source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourcePriorityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "decryption": "decryption",
            "description": "description",
            "entitlement_arn": "entitlementArn",
            "gateway_bridge_source": "gatewayBridgeSource",
            "ingest_ip": "ingestIp",
            "ingest_port": "ingestPort",
            "max_bitrate": "maxBitrate",
            "max_latency": "maxLatency",
            "max_sync_buffer": "maxSyncBuffer",
            "media_stream_source_configurations": "mediaStreamSourceConfigurations",
            "min_latency": "minLatency",
            "name": "name",
            "protocol": "protocol",
            "router_integration_state": "routerIntegrationState",
            "router_integration_transit_decryption": "routerIntegrationTransitDecryption",
            "sender_control_port": "senderControlPort",
            "sender_ip_address": "senderIpAddress",
            "source_arn": "sourceArn",
            "source_ingest_port": "sourceIngestPort",
            "source_listener_address": "sourceListenerAddress",
            "source_listener_port": "sourceListenerPort",
            "stream_id": "streamId",
            "vpc_interface_name": "vpcInterfaceName",
            "whitelist_cidr": "whitelistCidr",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            decryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            description: typing.Optional[builtins.str] = None,
            entitlement_arn: typing.Optional[builtins.str] = None,
            gateway_bridge_source: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.GatewayBridgeSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ingest_ip: typing.Optional[builtins.str] = None,
            ingest_port: typing.Optional[jsii.Number] = None,
            max_bitrate: typing.Optional[jsii.Number] = None,
            max_latency: typing.Optional[jsii.Number] = None,
            max_sync_buffer: typing.Optional[jsii.Number] = None,
            media_stream_source_configurations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.MediaStreamSourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            min_latency: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
            protocol: typing.Optional[builtins.str] = None,
            router_integration_state: typing.Optional[builtins.str] = None,
            router_integration_transit_decryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.FlowTransitEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sender_control_port: typing.Optional[jsii.Number] = None,
            sender_ip_address: typing.Optional[builtins.str] = None,
            source_arn: typing.Optional[builtins.str] = None,
            source_ingest_port: typing.Optional[builtins.str] = None,
            source_listener_address: typing.Optional[builtins.str] = None,
            source_listener_port: typing.Optional[jsii.Number] = None,
            stream_id: typing.Optional[builtins.str] = None,
            vpc_interface_name: typing.Optional[builtins.str] = None,
            whitelist_cidr: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of the sources of the flow.

            If you are creating a flow with a VPC source, you must first create the flow with a temporary standard source by doing the following:

            - Use CloudFormation to create a flow with a standard source that uses the flow’s public IP address.
            - Use CloudFormation to create the VPC interface to add to this flow. This can also be done as part of the previous step.
            - After CloudFormation has created the flow and the VPC interface, update the source to point to the VPC interface that you created.

            :param decryption: The type of encryption that is used on the content ingested from this source.
            :param description: A description for the source. This value is not used or seen outside of the current MediaConnect account.
            :param entitlement_arn: The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.
            :param gateway_bridge_source: The source configuration for cloud flows receiving a stream from a bridge.
            :param ingest_ip: The IP address that the flow will be listening on for incoming content.
            :param ingest_port: The port that the flow will be listening on for incoming content.
            :param max_bitrate: The maximum bitrate for RIST, RTP, and RTP-FEC streams.
            :param max_latency: The maximum latency in milliseconds for a RIST or Zixi-based source.
            :param max_sync_buffer: The size of the buffer (in milliseconds) to use to sync incoming source data.
            :param media_stream_source_configurations: The media streams that are associated with the source, and the parameters for those associations.
            :param min_latency: The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
            :param name: The name of the source.
            :param protocol: The protocol that is used by the source. AWS CloudFormation does not currently support CDI or ST 2110 JPEG XS source protocols. .. epigraph:: AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
            :param router_integration_state: Indicates if router integration is enabled or disabled on the flow source.
            :param router_integration_transit_decryption: The decryption configuration for the flow source when router integration is enabled.
            :param sender_control_port: The port that the flow uses to send outbound requests to initiate connection with the sender.
            :param sender_ip_address: The IP address that the flow communicates with to initiate connection with the sender.
            :param source_arn: The ARN of the source.
            :param source_ingest_port: The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088.
            :param source_listener_address: Source IP or domain name for SRT-caller protocol.
            :param source_listener_port: Source port for SRT-caller protocol.
            :param stream_id: The stream ID that you want to use for the transport. This parameter applies only to Zixi-based streams.
            :param vpc_interface_name: The name of the VPC interface that is used for this source.
            :param whitelist_cidr: The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                source_property = mediaconnect.CfnFlow.SourceProperty(
                    decryption=mediaconnect.CfnFlow.EncryptionProperty(
                        role_arn="roleArn",
                
                        # the properties below are optional
                        algorithm="algorithm",
                        constant_initialization_vector="constantInitializationVector",
                        device_id="deviceId",
                        key_type="keyType",
                        region="region",
                        resource_id="resourceId",
                        secret_arn="secretArn",
                        url="url"
                    ),
                    description="description",
                    entitlement_arn="entitlementArn",
                    gateway_bridge_source=mediaconnect.CfnFlow.GatewayBridgeSourceProperty(
                        bridge_arn="bridgeArn",
                
                        # the properties below are optional
                        vpc_interface_attachment=mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty(
                            vpc_interface_name="vpcInterfaceName"
                        )
                    ),
                    ingest_ip="ingestIp",
                    ingest_port=123,
                    max_bitrate=123,
                    max_latency=123,
                    max_sync_buffer=123,
                    media_stream_source_configurations=[mediaconnect.CfnFlow.MediaStreamSourceConfigurationProperty(
                        encoding_name="encodingName",
                        media_stream_name="mediaStreamName",
                
                        # the properties below are optional
                        input_configurations=[mediaconnect.CfnFlow.InputConfigurationProperty(
                            input_port=123,
                            interface=mediaconnect.CfnFlow.InterfaceProperty(
                                name="name"
                            )
                        )]
                    )],
                    min_latency=123,
                    name="name",
                    protocol="protocol",
                    router_integration_state="routerIntegrationState",
                    router_integration_transit_decryption=mediaconnect.CfnFlow.FlowTransitEncryptionProperty(
                        encryption_key_configuration=mediaconnect.CfnFlow.FlowTransitEncryptionKeyConfigurationProperty(
                            automatic=automatic,
                            secrets_manager=mediaconnect.CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
                
                        # the properties below are optional
                        encryption_key_type="encryptionKeyType"
                    ),
                    sender_control_port=123,
                    sender_ip_address="senderIpAddress",
                    source_arn="sourceArn",
                    source_ingest_port="sourceIngestPort",
                    source_listener_address="sourceListenerAddress",
                    source_listener_port=123,
                    stream_id="streamId",
                    vpc_interface_name="vpcInterfaceName",
                    whitelist_cidr="whitelistCidr"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c35ebd36bb52715c021bc299f222a377254ec8a3bd90d9c933fbefcac2bdf0c)
                check_type(argname="argument decryption", value=decryption, expected_type=type_hints["decryption"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument entitlement_arn", value=entitlement_arn, expected_type=type_hints["entitlement_arn"])
                check_type(argname="argument gateway_bridge_source", value=gateway_bridge_source, expected_type=type_hints["gateway_bridge_source"])
                check_type(argname="argument ingest_ip", value=ingest_ip, expected_type=type_hints["ingest_ip"])
                check_type(argname="argument ingest_port", value=ingest_port, expected_type=type_hints["ingest_port"])
                check_type(argname="argument max_bitrate", value=max_bitrate, expected_type=type_hints["max_bitrate"])
                check_type(argname="argument max_latency", value=max_latency, expected_type=type_hints["max_latency"])
                check_type(argname="argument max_sync_buffer", value=max_sync_buffer, expected_type=type_hints["max_sync_buffer"])
                check_type(argname="argument media_stream_source_configurations", value=media_stream_source_configurations, expected_type=type_hints["media_stream_source_configurations"])
                check_type(argname="argument min_latency", value=min_latency, expected_type=type_hints["min_latency"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument router_integration_state", value=router_integration_state, expected_type=type_hints["router_integration_state"])
                check_type(argname="argument router_integration_transit_decryption", value=router_integration_transit_decryption, expected_type=type_hints["router_integration_transit_decryption"])
                check_type(argname="argument sender_control_port", value=sender_control_port, expected_type=type_hints["sender_control_port"])
                check_type(argname="argument sender_ip_address", value=sender_ip_address, expected_type=type_hints["sender_ip_address"])
                check_type(argname="argument source_arn", value=source_arn, expected_type=type_hints["source_arn"])
                check_type(argname="argument source_ingest_port", value=source_ingest_port, expected_type=type_hints["source_ingest_port"])
                check_type(argname="argument source_listener_address", value=source_listener_address, expected_type=type_hints["source_listener_address"])
                check_type(argname="argument source_listener_port", value=source_listener_port, expected_type=type_hints["source_listener_port"])
                check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
                check_type(argname="argument whitelist_cidr", value=whitelist_cidr, expected_type=type_hints["whitelist_cidr"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if decryption is not None:
                self._values["decryption"] = decryption
            if description is not None:
                self._values["description"] = description
            if entitlement_arn is not None:
                self._values["entitlement_arn"] = entitlement_arn
            if gateway_bridge_source is not None:
                self._values["gateway_bridge_source"] = gateway_bridge_source
            if ingest_ip is not None:
                self._values["ingest_ip"] = ingest_ip
            if ingest_port is not None:
                self._values["ingest_port"] = ingest_port
            if max_bitrate is not None:
                self._values["max_bitrate"] = max_bitrate
            if max_latency is not None:
                self._values["max_latency"] = max_latency
            if max_sync_buffer is not None:
                self._values["max_sync_buffer"] = max_sync_buffer
            if media_stream_source_configurations is not None:
                self._values["media_stream_source_configurations"] = media_stream_source_configurations
            if min_latency is not None:
                self._values["min_latency"] = min_latency
            if name is not None:
                self._values["name"] = name
            if protocol is not None:
                self._values["protocol"] = protocol
            if router_integration_state is not None:
                self._values["router_integration_state"] = router_integration_state
            if router_integration_transit_decryption is not None:
                self._values["router_integration_transit_decryption"] = router_integration_transit_decryption
            if sender_control_port is not None:
                self._values["sender_control_port"] = sender_control_port
            if sender_ip_address is not None:
                self._values["sender_ip_address"] = sender_ip_address
            if source_arn is not None:
                self._values["source_arn"] = source_arn
            if source_ingest_port is not None:
                self._values["source_ingest_port"] = source_ingest_port
            if source_listener_address is not None:
                self._values["source_listener_address"] = source_listener_address
            if source_listener_port is not None:
                self._values["source_listener_port"] = source_listener_port
            if stream_id is not None:
                self._values["stream_id"] = stream_id
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name
            if whitelist_cidr is not None:
                self._values["whitelist_cidr"] = whitelist_cidr

        @builtins.property
        def decryption(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.EncryptionProperty"]]:
            '''The type of encryption that is used on the content ingested from this source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-decryption
            '''
            result = self._values.get("decryption")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.EncryptionProperty"]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description for the source.

            This value is not used or seen outside of the current MediaConnect account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entitlement_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account.

            The entitlement is set by the content originator and the ARN is generated as part of the originator's flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-entitlementarn
            '''
            result = self._values.get("entitlement_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def gateway_bridge_source(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.GatewayBridgeSourceProperty"]]:
            '''The source configuration for cloud flows receiving a stream from a bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-gatewaybridgesource
            '''
            result = self._values.get("gateway_bridge_source")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.GatewayBridgeSourceProperty"]], result)

        @builtins.property
        def ingest_ip(self) -> typing.Optional[builtins.str]:
            '''The IP address that the flow will be listening on for incoming content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-ingestip
            '''
            result = self._values.get("ingest_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ingest_port(self) -> typing.Optional[jsii.Number]:
            '''The port that the flow will be listening on for incoming content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-ingestport
            '''
            result = self._values.get("ingest_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_bitrate(self) -> typing.Optional[jsii.Number]:
            '''The maximum bitrate for RIST, RTP, and RTP-FEC streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-maxbitrate
            '''
            result = self._values.get("max_bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_latency(self) -> typing.Optional[jsii.Number]:
            '''The maximum latency in milliseconds for a RIST or Zixi-based source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-maxlatency
            '''
            result = self._values.get("max_latency")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_sync_buffer(self) -> typing.Optional[jsii.Number]:
            '''The size of the buffer (in milliseconds) to use to sync incoming source data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-maxsyncbuffer
            '''
            result = self._values.get("max_sync_buffer")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def media_stream_source_configurations(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.MediaStreamSourceConfigurationProperty"]]]]:
            '''The media streams that are associated with the source, and the parameters for those associations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-mediastreamsourceconfigurations
            '''
            result = self._values.get("media_stream_source_configurations")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.MediaStreamSourceConfigurationProperty"]]]], result)

        @builtins.property
        def min_latency(self) -> typing.Optional[jsii.Number]:
            '''The minimum latency in milliseconds for SRT-based streams.

            In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-minlatency
            '''
            result = self._values.get("min_latency")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The protocol that is used by the source.

            AWS CloudFormation does not currently support CDI or ST 2110 JPEG XS source protocols.
            .. epigraph::

               AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def router_integration_state(self) -> typing.Optional[builtins.str]:
            '''Indicates if router integration is enabled or disabled on the flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-routerintegrationstate
            '''
            result = self._values.get("router_integration_state")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def router_integration_transit_decryption(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FlowTransitEncryptionProperty"]]:
            '''The decryption configuration for the flow source when router integration is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-routerintegrationtransitdecryption
            '''
            result = self._values.get("router_integration_transit_decryption")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FlowTransitEncryptionProperty"]], result)

        @builtins.property
        def sender_control_port(self) -> typing.Optional[jsii.Number]:
            '''The port that the flow uses to send outbound requests to initiate connection with the sender.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sendercontrolport
            '''
            result = self._values.get("sender_control_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def sender_ip_address(self) -> typing.Optional[builtins.str]:
            '''The IP address that the flow communicates with to initiate connection with the sender.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-senderipaddress
            '''
            result = self._values.get("sender_ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourcearn
            '''
            result = self._values.get("source_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_ingest_port(self) -> typing.Optional[builtins.str]:
            '''The port that the flow listens on for incoming content.

            If the protocol of the source is Zixi, the port must be set to 2088.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourceingestport
            '''
            result = self._values.get("source_ingest_port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_listener_address(self) -> typing.Optional[builtins.str]:
            '''Source IP or domain name for SRT-caller protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourcelisteneraddress
            '''
            result = self._values.get("source_listener_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_listener_port(self) -> typing.Optional[jsii.Number]:
            '''Source port for SRT-caller protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourcelistenerport
            '''
            result = self._values.get("source_listener_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_id(self) -> typing.Optional[builtins.str]:
            '''The stream ID that you want to use for the transport.

            This parameter applies only to Zixi-based streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-streamid
            '''
            result = self._values.get("stream_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface that is used for this source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def whitelist_cidr(self) -> typing.Optional[builtins.str]:
            '''The range of IP addresses that should be allowed to contribute content to your source.

            These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-whitelistcidr
            '''
            result = self._values.get("whitelist_cidr")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.VideoMonitoringSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"black_frames": "blackFrames", "frozen_frames": "frozenFrames"},
    )
    class VideoMonitoringSettingProperty:
        def __init__(
            self,
            *,
            black_frames: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.BlackFramesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            frozen_frames: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.FrozenFramesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the configuration for video stream metrics monitoring.

            :param black_frames: Detects video frames that are black.
            :param frozen_frames: Detects video frames that have not changed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-videomonitoringsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                video_monitoring_setting_property = mediaconnect.CfnFlow.VideoMonitoringSettingProperty(
                    black_frames=mediaconnect.CfnFlow.BlackFramesProperty(
                        state="state",
                        threshold_seconds=123
                    ),
                    frozen_frames=mediaconnect.CfnFlow.FrozenFramesProperty(
                        state="state",
                        threshold_seconds=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b18d7f5756a7359dc9028ca35bdb8d048195959b43a7f2ac5c0f4b71d0b8761)
                check_type(argname="argument black_frames", value=black_frames, expected_type=type_hints["black_frames"])
                check_type(argname="argument frozen_frames", value=frozen_frames, expected_type=type_hints["frozen_frames"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if black_frames is not None:
                self._values["black_frames"] = black_frames
            if frozen_frames is not None:
                self._values["frozen_frames"] = frozen_frames

        @builtins.property
        def black_frames(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.BlackFramesProperty"]]:
            '''Detects video frames that are black.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-videomonitoringsetting.html#cfn-mediaconnect-flow-videomonitoringsetting-blackframes
            '''
            result = self._values.get("black_frames")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.BlackFramesProperty"]], result)

        @builtins.property
        def frozen_frames(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FrozenFramesProperty"]]:
            '''Detects video frames that have not changed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-videomonitoringsetting.html#cfn-mediaconnect-flow-videomonitoringsetting-frozenframes
            '''
            result = self._values.get("frozen_frames")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FrozenFramesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VideoMonitoringSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for attaching a VPC interface to an resource.

            :param vpc_interface_name: The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterfaceattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_attachment_property = mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__866ca963188936c1dd8965fb722dc7f781261eab36e78ecdb20a9d41b146ef40)
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterfaceattachment.html#cfn-mediaconnect-flow-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.VpcInterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "role_arn": "roleArn",
            "security_group_ids": "securityGroupIds",
            "subnet_id": "subnetId",
            "network_interface_ids": "networkInterfaceIds",
            "network_interface_type": "networkInterfaceType",
        },
    )
    class VpcInterfaceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            role_arn: builtins.str,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_id: builtins.str,
            network_interface_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            network_interface_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of a VPC interface.

            .. epigraph::

               When configuring VPC interfaces for NDI outputs, keep in mind the following:

               - VPC interfaces must be defined as nested attributes within the ``AWS::MediaConnect::Flow`` resource, and not within the top-level ``AWS::MediaConnect::FlowVpcInterface`` resource.
               - There's a maximum limit of three VPC interfaces for each flow. If you've already reached this limit, you can't update the flow to use a different VPC interface without first removing an existing one.

               To update your VPC interfaces in this scenario, you must first remove the VPC interface that’s not being used. Next, add the new VPC interfaces. Lastly, update the ``VpcInterfaceAdapter`` in the ``NDIConfig`` property. These changes must be performed as separate manual operations and cannot be done through a single template update.

            :param name: Immutable and has to be a unique against other VpcInterfaces in this Flow.
            :param role_arn: A role Arn MediaConnect can assume to create ENIs in your account.
            :param security_group_ids: Security Group IDs to be used on ENI.
            :param subnet_id: Subnet must be in the AZ of the Flow.
            :param network_interface_ids: IDs of the network interfaces created in customer's account by MediaConnect .
            :param network_interface_type: The type of network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_property = mediaconnect.CfnFlow.VpcInterfaceProperty(
                    name="name",
                    role_arn="roleArn",
                    security_group_ids=["securityGroupIds"],
                    subnet_id="subnetId",
                
                    # the properties below are optional
                    network_interface_ids=["networkInterfaceIds"],
                    network_interface_type="networkInterfaceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d976d1dab1b395c0026dcc2152c4dd635ae54d817a1f10c4d8f2725ac4862ad4)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
                check_type(argname="argument network_interface_ids", value=network_interface_ids, expected_type=type_hints["network_interface_ids"])
                check_type(argname="argument network_interface_type", value=network_interface_type, expected_type=type_hints["network_interface_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "role_arn": role_arn,
                "security_group_ids": security_group_ids,
                "subnet_id": subnet_id,
            }
            if network_interface_ids is not None:
                self._values["network_interface_ids"] = network_interface_ids
            if network_interface_type is not None:
                self._values["network_interface_type"] = network_interface_type

        @builtins.property
        def name(self) -> builtins.str:
            '''Immutable and has to be a unique against other VpcInterfaces in this Flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterface.html#cfn-mediaconnect-flow-vpcinterface-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''A role Arn MediaConnect can assume to create ENIs in your account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterface.html#cfn-mediaconnect-flow-vpcinterface-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''Security Group IDs to be used on ENI.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterface.html#cfn-mediaconnect-flow-vpcinterface-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_id(self) -> builtins.str:
            '''Subnet must be in the AZ of the Flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterface.html#cfn-mediaconnect-flow-vpcinterface-subnetid
            '''
            result = self._values.get("subnet_id")
            assert result is not None, "Required property 'subnet_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_interface_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''IDs of the network interfaces created in customer's account by MediaConnect .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterface.html#cfn-mediaconnect-flow-vpcinterface-networkinterfaceids
            '''
            result = self._values.get("network_interface_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def network_interface_type(self) -> typing.Optional[builtins.str]:
            '''The type of network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterface.html#cfn-mediaconnect-flow-vpcinterface-networkinterfacetype
            '''
            result = self._values.get("network_interface_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _IFlowEntitlementRef_83db35bc)
class CfnFlowEntitlement(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowEntitlement",
):
    '''The ``AWS::MediaConnect::FlowEntitlement`` resource defines the permission that an AWS account grants to another AWS account to allow access to the content in a specific AWS Elemental MediaConnect flow.

    The content originator grants an entitlement to a specific AWS account (the subscriber). When an entitlement is granted, the subscriber can create a flow using the originator's flow as the source. Each flow can have up to 50 entitlements.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html
    :cloudformationResource: AWS::MediaConnect::FlowEntitlement
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_flow_entitlement = mediaconnect.CfnFlowEntitlement(self, "MyCfnFlowEntitlement",
            description="description",
            flow_arn="flowArn",
            name="name",
            subscribers=["subscribers"],
        
            # the properties below are optional
            data_transfer_subscriber_fee_percent=123,
            encryption=mediaconnect.CfnFlowEntitlement.EncryptionProperty(
                algorithm="algorithm",
                role_arn="roleArn",
        
                # the properties below are optional
                constant_initialization_vector="constantInitializationVector",
                device_id="deviceId",
                key_type="keyType",
                region="region",
                resource_id="resourceId",
                secret_arn="secretArn",
                url="url"
            ),
            entitlement_status="entitlementStatus"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        description: builtins.str,
        flow_arn: builtins.str,
        name: builtins.str,
        subscribers: typing.Sequence[builtins.str],
        data_transfer_subscriber_fee_percent: typing.Optional[jsii.Number] = None,
        encryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowEntitlement.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        entitlement_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::FlowEntitlement``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description of the entitlement. This description appears only on the MediaConnect console and is not visible outside of the current AWS account.
        :param flow_arn: The Amazon Resource Name (ARN) of the flow.
        :param name: The name of the entitlement. This value must be unique within the current flow.
        :param subscribers: The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.
        :param data_transfer_subscriber_fee_percent: The percentage of the entitlement data transfer fee that you want the subscriber to be responsible for. Default: - 0
        :param encryption: Encryption information.
        :param entitlement_status: An indication of whether the new entitlement should be enabled or disabled as soon as it is created. If you don’t specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17ecd85086df3a96cb74577c3e3a831ea91a89b617bcd18f7684fd357569ebd4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowEntitlementProps(
            description=description,
            flow_arn=flow_arn,
            name=name,
            subscribers=subscribers,
            data_transfer_subscriber_fee_percent=data_transfer_subscriber_fee_percent,
            encryption=encryption,
            entitlement_status=entitlement_status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnFlowEntitlement")
    @builtins.classmethod
    def is_cfn_flow_entitlement(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFlowEntitlement.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbbd0b319bddb33c17b2662fae7caf55246f72dd2fa82c3bf38238c549f8a7e4)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFlowEntitlement", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc2981b84449358974725cfa5726c974127f55b1d0ed785957f4a1db25fbaf37)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2fa54f5d69b72c125e54c71a8aa7a22fc52b087370efdb65ece275ef52b680b8)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEntitlementArn")
    def attr_entitlement_arn(self) -> builtins.str:
        '''The entitlement ARN.

        :cloudformationAttribute: EntitlementArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEntitlementArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="flowEntitlementRef")
    def flow_entitlement_ref(self) -> "_FlowEntitlementReference_2242862f":
        '''A reference to a FlowEntitlement resource.'''
        return typing.cast("_FlowEntitlementReference_2242862f", jsii.get(self, "flowEntitlementRef"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description of the entitlement.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5eab3ebe302e351ac5ac0d66029f44599f4749a72395abe65585f0a24955a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow.'''
        return typing.cast(builtins.str, jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e11924d752092913d6e2606c9cde4c9d3a676e93d2cdf59e192e9e6c293bfe35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the entitlement.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__916ef20a18bd718e63e193a4bfe9a47ef0a3fa7c7d6eb6a74a9f583ad5834eb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subscribers")
    def subscribers(self) -> typing.List[builtins.str]:
        '''The AWS account IDs that you want to share your content with.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subscribers"))

    @subscribers.setter
    def subscribers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9ffb421693bf57958756eb013d4d8a721597fcd6b5c4d155ff98a2fc1ee7f4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscribers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dataTransferSubscriberFeePercent")
    def data_transfer_subscriber_fee_percent(self) -> typing.Optional[jsii.Number]:
        '''The percentage of the entitlement data transfer fee that you want the subscriber to be responsible for.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataTransferSubscriberFeePercent"))

    @data_transfer_subscriber_fee_percent.setter
    def data_transfer_subscriber_fee_percent(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__440918e3c472d10f8c3846eeee04790645912cc1f354752fcf74610c24a956dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTransferSubscriberFeePercent", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowEntitlement.EncryptionProperty"]]:
        '''Encryption information.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowEntitlement.EncryptionProperty"]], jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowEntitlement.EncryptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e186a635819e5284e2d58b4d8e7f8c317f8ef3dcaf08d3a66dfe0e4f1b061e89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="entitlementStatus")
    def entitlement_status(self) -> typing.Optional[builtins.str]:
        '''An indication of whether the new entitlement should be enabled or disabled as soon as it is created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entitlementStatus"))

    @entitlement_status.setter
    def entitlement_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdf1b9a179db4ad86ff23860586d83012068ae1abfca84e5defe29f68556a89a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entitlementStatus", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowEntitlement.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm": "algorithm",
            "role_arn": "roleArn",
            "constant_initialization_vector": "constantInitializationVector",
            "device_id": "deviceId",
            "key_type": "keyType",
            "region": "region",
            "resource_id": "resourceId",
            "secret_arn": "secretArn",
            "url": "url",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            algorithm: builtins.str,
            role_arn: builtins.str,
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            device_id: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Encryption information.

            :param algorithm: The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256). If you are using SPEKE or SRT-password encryption, this property must be left blank.
            :param role_arn: The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).
            :param constant_initialization_vector: A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
            :param device_id: The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param key_type: The type of key that is used for the encryption. If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` . Default: - "static-key"
            :param region: The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param resource_id: An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param secret_arn: The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
            :param url: The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                encryption_property = mediaconnect.CfnFlowEntitlement.EncryptionProperty(
                    algorithm="algorithm",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a86c4f896040118c2a4fab234e2a7101cc609c650cf5a8c91892db664909f050)
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument constant_initialization_vector", value=constant_initialization_vector, expected_type=type_hints["constant_initialization_vector"])
                check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "algorithm": algorithm,
                "role_arn": role_arn,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if device_id is not None:
                self._values["device_id"] = device_id
            if key_type is not None:
                self._values["key_type"] = key_type
            if region is not None:
                self._values["region"] = region
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def algorithm(self) -> builtins.str:
            '''The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256).

            If you are using SPEKE or SRT-password encryption, this property must be left blank.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            assert result is not None, "Required property 'algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content.

            This parameter is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_id(self) -> typing.Optional[builtins.str]:
            '''The value of one of the devices that you configured with your digital rights management (DRM) platform key provider.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-deviceid
            '''
            result = self._values.get("device_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''The type of key that is used for the encryption.

            If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` .

            :default: - "static-key"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region that the API Gateway proxy endpoint was created in.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''An identifier for the content.

            The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.

            This parameter is required for static key encryption and is not valid for SPEKE encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL from the API Gateway proxy that you set up to talk to your key server.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowEntitlementProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "flow_arn": "flowArn",
        "name": "name",
        "subscribers": "subscribers",
        "data_transfer_subscriber_fee_percent": "dataTransferSubscriberFeePercent",
        "encryption": "encryption",
        "entitlement_status": "entitlementStatus",
    },
)
class CfnFlowEntitlementProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        flow_arn: builtins.str,
        name: builtins.str,
        subscribers: typing.Sequence[builtins.str],
        data_transfer_subscriber_fee_percent: typing.Optional[jsii.Number] = None,
        encryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowEntitlement.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        entitlement_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlowEntitlement``.

        :param description: A description of the entitlement. This description appears only on the MediaConnect console and is not visible outside of the current AWS account.
        :param flow_arn: The Amazon Resource Name (ARN) of the flow.
        :param name: The name of the entitlement. This value must be unique within the current flow.
        :param subscribers: The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.
        :param data_transfer_subscriber_fee_percent: The percentage of the entitlement data transfer fee that you want the subscriber to be responsible for. Default: - 0
        :param encryption: Encryption information.
        :param entitlement_status: An indication of whether the new entitlement should be enabled or disabled as soon as it is created. If you don’t specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_flow_entitlement_props = mediaconnect.CfnFlowEntitlementProps(
                description="description",
                flow_arn="flowArn",
                name="name",
                subscribers=["subscribers"],
            
                # the properties below are optional
                data_transfer_subscriber_fee_percent=123,
                encryption=mediaconnect.CfnFlowEntitlement.EncryptionProperty(
                    algorithm="algorithm",
                    role_arn="roleArn",
            
                    # the properties below are optional
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                ),
                entitlement_status="entitlementStatus"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7f5911f6dc55c43d6c5bdd5da77a5eb8fb59e8f8418ae5a951a5e0f015b5055)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subscribers", value=subscribers, expected_type=type_hints["subscribers"])
            check_type(argname="argument data_transfer_subscriber_fee_percent", value=data_transfer_subscriber_fee_percent, expected_type=type_hints["data_transfer_subscriber_fee_percent"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument entitlement_status", value=entitlement_status, expected_type=type_hints["entitlement_status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "flow_arn": flow_arn,
            "name": name,
            "subscribers": subscribers,
        }
        if data_transfer_subscriber_fee_percent is not None:
            self._values["data_transfer_subscriber_fee_percent"] = data_transfer_subscriber_fee_percent
        if encryption is not None:
            self._values["encryption"] = encryption
        if entitlement_status is not None:
            self._values["entitlement_status"] = entitlement_status

    @builtins.property
    def description(self) -> builtins.str:
        '''A description of the entitlement.

        This description appears only on the MediaConnect console and is not visible outside of the current AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-flowarn
        '''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the entitlement.

        This value must be unique within the current flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscribers(self) -> typing.List[builtins.str]:
        '''The AWS account IDs that you want to share your content with.

        The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-subscribers
        '''
        result = self._values.get("subscribers")
        assert result is not None, "Required property 'subscribers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def data_transfer_subscriber_fee_percent(self) -> typing.Optional[jsii.Number]:
        '''The percentage of the entitlement data transfer fee that you want the subscriber to be responsible for.

        :default: - 0

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-datatransfersubscriberfeepercent
        '''
        result = self._values.get("data_transfer_subscriber_fee_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowEntitlement.EncryptionProperty"]]:
        '''Encryption information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-encryption
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowEntitlement.EncryptionProperty"]], result)

    @builtins.property
    def entitlement_status(self) -> typing.Optional[builtins.str]:
        '''An indication of whether the new entitlement should be enabled or disabled as soon as it is created.

        If you don’t specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-entitlementstatus
        '''
        result = self._values.get("entitlement_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowEntitlementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IFlowOutputRef_be0a9d75)
class CfnFlowOutput(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput",
):
    '''The ``AWS::MediaConnect::FlowOutput`` resource defines the destination address, protocol, and port that AWS Elemental MediaConnect sends the ingested video to.

    Each flow can have up to 50 outputs. An output can have the same protocol or a different protocol from the source. The following protocols are supported: RIST, RTP, RTP-FEC, SRT-listener, SRT-caller, Zixi pull, and Zixi push. CDI and ST 2110 JPEG XS protocols are not currently supported by AWS CloudFormation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html
    :cloudformationResource: AWS::MediaConnect::FlowOutput
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        # automatic: Any
        
        cfn_flow_output = mediaconnect.CfnFlowOutput(self, "MyCfnFlowOutput",
            flow_arn="flowArn",
        
            # the properties below are optional
            cidr_allow_list=["cidrAllowList"],
            description="description",
            destination="destination",
            encryption=mediaconnect.CfnFlowOutput.EncryptionProperty(
                role_arn="roleArn",
                secret_arn="secretArn",
        
                # the properties below are optional
                algorithm="algorithm",
                key_type="keyType"
            ),
            max_latency=123,
            media_stream_output_configurations=[mediaconnect.CfnFlowOutput.MediaStreamOutputConfigurationProperty(
                encoding_name="encodingName",
                media_stream_name="mediaStreamName",
        
                # the properties below are optional
                destination_configurations=[mediaconnect.CfnFlowOutput.DestinationConfigurationProperty(
                    destination_ip="destinationIp",
                    destination_port=123,
                    interface=mediaconnect.CfnFlowOutput.InterfaceProperty(
                        name="name"
                    )
                )],
                encoding_parameters=mediaconnect.CfnFlowOutput.EncodingParametersProperty(
                    compression_factor=123,
        
                    # the properties below are optional
                    encoder_profile="encoderProfile"
                )
            )],
            min_latency=123,
            name="name",
            ndi_program_name="ndiProgramName",
            ndi_speed_hq_quality=123,
            output_status="outputStatus",
            port=123,
            protocol="protocol",
            remote_id="remoteId",
            router_integration_state="routerIntegrationState",
            router_integration_transit_encryption=mediaconnect.CfnFlowOutput.FlowTransitEncryptionProperty(
                encryption_key_configuration=mediaconnect.CfnFlowOutput.FlowTransitEncryptionKeyConfigurationProperty(
                    automatic=automatic,
                    secrets_manager=mediaconnect.CfnFlowOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                ),
        
                # the properties below are optional
                encryption_key_type="encryptionKeyType"
            ),
            smoothing_latency=123,
            stream_id="streamId",
            vpc_interface_attachment=mediaconnect.CfnFlowOutput.VpcInterfaceAttachmentProperty(
                vpc_interface_name="vpcInterfaceName"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        flow_arn: builtins.str,
        cidr_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        destination: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        media_stream_output_configurations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.MediaStreamOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        min_latency: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        ndi_program_name: typing.Optional[builtins.str] = None,
        ndi_speed_hq_quality: typing.Optional[jsii.Number] = None,
        output_status: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        remote_id: typing.Optional[builtins.str] = None,
        router_integration_state: typing.Optional[builtins.str] = None,
        router_integration_transit_encryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.FlowTransitEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        smoothing_latency: typing.Optional[jsii.Number] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_attachment: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::FlowOutput``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param flow_arn: The Amazon Resource Name (ARN) of the flow this output is attached to.
        :param cidr_allow_list: The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        :param description: A description of the output. This description appears only on the MediaConnect console and will not be seen by the end user.
        :param destination: The IP address where you want to send the output.
        :param encryption: The type of key used for the encryption. If no ``keyType`` is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.
        :param max_latency: The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
        :param media_stream_output_configurations: The media streams that are associated with the output, and the parameters for those associations.
        :param min_latency: The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
        :param name: The name of the bridge's output.
        :param ndi_program_name: A suffix for the names of the NDI sources that the flow creates. If a custom name isn't specified, MediaConnect uses the output name.
        :param ndi_speed_hq_quality: A quality setting for the NDI Speed HQ encoder.
        :param output_status: An indication of whether the output should transmit data or not.
        :param port: The port to use when content is distributed to this output.
        :param protocol: The protocol to use for the output. .. epigraph:: AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
        :param remote_id: The remote ID for the Zixi-pull stream.
        :param router_integration_state: 
        :param router_integration_transit_encryption: Encryption information.
        :param smoothing_latency: The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
        :param stream_id: The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
        :param vpc_interface_attachment: The name of the VPC interface attachment to use for this output.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50a855342b002f2aaf180af2a85e45ce23346b4a5b582c00ee1a8474e9dd9bf1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowOutputProps(
            flow_arn=flow_arn,
            cidr_allow_list=cidr_allow_list,
            description=description,
            destination=destination,
            encryption=encryption,
            max_latency=max_latency,
            media_stream_output_configurations=media_stream_output_configurations,
            min_latency=min_latency,
            name=name,
            ndi_program_name=ndi_program_name,
            ndi_speed_hq_quality=ndi_speed_hq_quality,
            output_status=output_status,
            port=port,
            protocol=protocol,
            remote_id=remote_id,
            router_integration_state=router_integration_state,
            router_integration_transit_encryption=router_integration_transit_encryption,
            smoothing_latency=smoothing_latency,
            stream_id=stream_id,
            vpc_interface_attachment=vpc_interface_attachment,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnFlowOutput")
    @builtins.classmethod
    def is_cfn_flow_output(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFlowOutput.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc12c2292179153951e36b26c5ca33a4865934ab09aaab3ef3247a4db0208245)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFlowOutput", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f7a6ea2f782501225c570fc34c141a4efdd391bd9340c51c8bd1b59b8a807b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fe52bb8ba629a55d8f6926893cc92e58afb2df918e7d368aeddb04aa5bb1855)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrOutputArn")
    def attr_output_arn(self) -> builtins.str:
        '''The ARN of the output.

        :cloudformationAttribute: OutputArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOutputArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="flowOutputRef")
    def flow_output_ref(self) -> "_FlowOutputReference_30ed8edf":
        '''A reference to a FlowOutput resource.'''
        return typing.cast("_FlowOutputReference_30ed8edf", jsii.get(self, "flowOutputRef"))

    @builtins.property
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow this output is attached to.'''
        return typing.cast(builtins.str, jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b58a8b918485e48f2bd2cbf5a806a141e4d5ae34f2cf830391b88420333717)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="cidrAllowList")
    def cidr_allow_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The range of IP addresses that should be allowed to initiate output requests to this flow.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cidrAllowList"))

    @cidr_allow_list.setter
    def cidr_allow_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07f3031245a81d1c4e02553eaeb7fc62e38e625e4d2cfe7b7ff3ecce31ce6ef5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrAllowList", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the output.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04edd4c6554768eef7ffa49af9bf9fdec351390bdef1d2d14056f7b2afa9b477)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> typing.Optional[builtins.str]:
        '''The IP address where you want to send the output.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3f2991cc0ce7b9368aefbf86c1373167ce7a90e3225db313dd6d35540907285)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.EncryptionProperty"]]:
        '''The type of key used for the encryption.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.EncryptionProperty"]], jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.EncryptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a7a7ea75faea54e857e52b24703069f4dd92643ca1173b27422c3504eee69b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxLatency")
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''The maximum latency in milliseconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLatency"))

    @max_latency.setter
    def max_latency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9801fdc6b598fc4f2e913edc8984f374a7594553b0a1ef32ea0fa7be05bb61db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLatency", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mediaStreamOutputConfigurations")
    def media_stream_output_configurations(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.MediaStreamOutputConfigurationProperty"]]]]:
        '''The media streams that are associated with the output, and the parameters for those associations.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.MediaStreamOutputConfigurationProperty"]]]], jsii.get(self, "mediaStreamOutputConfigurations"))

    @media_stream_output_configurations.setter
    def media_stream_output_configurations(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.MediaStreamOutputConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99ca24b6208e72328e18819b003e97cbf14fb0f94304256c59924c6e02ae32d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mediaStreamOutputConfigurations", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="minLatency")
    def min_latency(self) -> typing.Optional[jsii.Number]:
        '''The minimum latency in milliseconds for SRT-based streams.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minLatency"))

    @min_latency.setter
    def min_latency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddb7401a37f3ff6ff7dc25a56db1a28806074c96fc3f42a6bd90cc4feab9b693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLatency", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the bridge's output.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b750df47b88518fdf7bc5d1baec396797cb9cc3a0c8bdc7742108d9c93c231)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ndiProgramName")
    def ndi_program_name(self) -> typing.Optional[builtins.str]:
        '''A suffix for the names of the NDI sources that the flow creates.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ndiProgramName"))

    @ndi_program_name.setter
    def ndi_program_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__726c61d1e734fe3825d1f969a727f62f0da47c2684038a9b2dd3b004d823f5a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ndiProgramName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ndiSpeedHqQuality")
    def ndi_speed_hq_quality(self) -> typing.Optional[jsii.Number]:
        '''A quality setting for the NDI Speed HQ encoder.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ndiSpeedHqQuality"))

    @ndi_speed_hq_quality.setter
    def ndi_speed_hq_quality(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce18d034d798847cffb7feeb7c46dad4031db9cee117a778fb30fb59f6e3cde2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ndiSpeedHqQuality", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="outputStatus")
    def output_status(self) -> typing.Optional[builtins.str]:
        '''An indication of whether the output should transmit data or not.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputStatus"))

    @output_status.setter
    def output_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b4c653e5fd4b3a28c65a69d506d6616ef027aa50bccc2d72a02bc2ff7c57c1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputStatus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port to use when content is distributed to this output.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082204a6d2f259b91fea6a581b0aa8a534b0e447853734806818dfa91f967458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol to use for the output.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a09f7a6d8ae99d18b6e3bb11284fa5b865ca2146c5efb07536e593ee9a05bc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="remoteId")
    def remote_id(self) -> typing.Optional[builtins.str]:
        '''The remote ID for the Zixi-pull stream.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteId"))

    @remote_id.setter
    def remote_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f19d4552e8cf70ccb26264cc49b216d391ddef580a3635679d644bda9f8dabf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="routerIntegrationState")
    def router_integration_state(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routerIntegrationState"))

    @router_integration_state.setter
    def router_integration_state(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a92363a82d416caa03ccab5a501ed2d648ae0c5a5733439e18d20b4fab0532be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routerIntegrationState", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="routerIntegrationTransitEncryption")
    def router_integration_transit_encryption(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.FlowTransitEncryptionProperty"]]:
        '''Encryption information.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.FlowTransitEncryptionProperty"]], jsii.get(self, "routerIntegrationTransitEncryption"))

    @router_integration_transit_encryption.setter
    def router_integration_transit_encryption(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.FlowTransitEncryptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32b31733a523757f4557ebb20483d8cac01327485a4f5ee9746929dd058f123d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routerIntegrationTransitEncryption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="smoothingLatency")
    def smoothing_latency(self) -> typing.Optional[jsii.Number]:
        '''The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "smoothingLatency"))

    @smoothing_latency.setter
    def smoothing_latency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a7c12acde851480773f720ab16362e6f6dd272465bbe84d6b60322c1bfd207d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smoothingLatency", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="streamId")
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''The stream ID that you want to use for this transport.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamId"))

    @stream_id.setter
    def stream_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dadac9d58702681fe997f284efaad53e6d5af9dac998dd803277c6ed1ee2a381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcInterfaceAttachment")
    def vpc_interface_attachment(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.VpcInterfaceAttachmentProperty"]]:
        '''The name of the VPC interface attachment to use for this output.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.VpcInterfaceAttachmentProperty"]], jsii.get(self, "vpcInterfaceAttachment"))

    @vpc_interface_attachment.setter
    def vpc_interface_attachment(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.VpcInterfaceAttachmentProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65a3e058407bcf8bd6fa065c9fd3cd66a1c54e7edb3b48af25c7893fd72db21d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcInterfaceAttachment", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.DestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_ip": "destinationIp",
            "destination_port": "destinationPort",
            "interface": "interface",
        },
    )
    class DestinationConfigurationProperty:
        def __init__(
            self,
            *,
            destination_ip: builtins.str,
            destination_port: jsii.Number,
            interface: typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.InterfaceProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The transport parameters that you want to associate with an outbound media stream.

            :param destination_ip: The IP address where you want MediaConnect to send contents of the media stream.
            :param destination_port: The port that you want MediaConnect to use when it distributes the media stream to the output.
            :param interface: The VPC interface that you want to use for the media stream associated with the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-destinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                destination_configuration_property = mediaconnect.CfnFlowOutput.DestinationConfigurationProperty(
                    destination_ip="destinationIp",
                    destination_port=123,
                    interface=mediaconnect.CfnFlowOutput.InterfaceProperty(
                        name="name"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8b62fc10e1fb76cee67ab63dde918a0006c11ce38e8af823e4d2f2770e4d5765)
                check_type(argname="argument destination_ip", value=destination_ip, expected_type=type_hints["destination_ip"])
                check_type(argname="argument destination_port", value=destination_port, expected_type=type_hints["destination_port"])
                check_type(argname="argument interface", value=interface, expected_type=type_hints["interface"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_ip": destination_ip,
                "destination_port": destination_port,
                "interface": interface,
            }

        @builtins.property
        def destination_ip(self) -> builtins.str:
            '''The IP address where you want MediaConnect to send contents of the media stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-destinationconfiguration.html#cfn-mediaconnect-flowoutput-destinationconfiguration-destinationip
            '''
            result = self._values.get("destination_ip")
            assert result is not None, "Required property 'destination_ip' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_port(self) -> jsii.Number:
            '''The port that you want MediaConnect to use when it distributes the media stream to the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-destinationconfiguration.html#cfn-mediaconnect-flowoutput-destinationconfiguration-destinationport
            '''
            result = self._values.get("destination_port")
            assert result is not None, "Required property 'destination_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def interface(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.InterfaceProperty"]:
            '''The VPC interface that you want to use for the media stream associated with the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-destinationconfiguration.html#cfn-mediaconnect-flowoutput-destinationconfiguration-interface
            '''
            result = self._values.get("interface")
            assert result is not None, "Required property 'interface' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.InterfaceProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.EncodingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "compression_factor": "compressionFactor",
            "encoder_profile": "encoderProfile",
        },
    )
    class EncodingParametersProperty:
        def __init__(
            self,
            *,
            compression_factor: jsii.Number,
            encoder_profile: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A collection of parameters that determine how MediaConnect will convert the content.

            These fields only apply to outputs on flows that have a CDI source.

            :param compression_factor: A value that is used to calculate compression for an output. The bitrate of the output is calculated as follows: Output bitrate = (1 / compressionFactor) * (source bitrate) This property only applies to outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol. Valid values are floating point numbers in the range of 3.0 to 10.0, inclusive.
            :param encoder_profile: A setting on the encoder that drives compression settings. This property only applies to video media streams associated with outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encodingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                encoding_parameters_property = mediaconnect.CfnFlowOutput.EncodingParametersProperty(
                    compression_factor=123,
                
                    # the properties below are optional
                    encoder_profile="encoderProfile"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d7e858c0a050e7b9bf4f84c7f6034ad1cf704a2a9a2b07a5b472d598f1b62d5f)
                check_type(argname="argument compression_factor", value=compression_factor, expected_type=type_hints["compression_factor"])
                check_type(argname="argument encoder_profile", value=encoder_profile, expected_type=type_hints["encoder_profile"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "compression_factor": compression_factor,
            }
            if encoder_profile is not None:
                self._values["encoder_profile"] = encoder_profile

        @builtins.property
        def compression_factor(self) -> jsii.Number:
            '''A value that is used to calculate compression for an output.

            The bitrate of the output is calculated as follows: Output bitrate = (1 / compressionFactor) * (source bitrate) This property only applies to outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol. Valid values are floating point numbers in the range of 3.0 to 10.0, inclusive.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encodingparameters.html#cfn-mediaconnect-flowoutput-encodingparameters-compressionfactor
            '''
            result = self._values.get("compression_factor")
            assert result is not None, "Required property 'compression_factor' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def encoder_profile(self) -> typing.Optional[builtins.str]:
            '''A setting on the encoder that drives compression settings.

            This property only applies to video media streams associated with outputs that use the ST 2110 JPEG XS protocol, with a flow source that uses the CDI protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encodingparameters.html#cfn-mediaconnect-flowoutput-encodingparameters-encoderprofile
            '''
            result = self._values.get("encoder_profile")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncodingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "secret_arn": "secretArn",
            "algorithm": "algorithm",
            "key_type": "keyType",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            secret_arn: builtins.str,
            algorithm: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Encryption information.

            :param role_arn: The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).
            :param secret_arn: The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
            :param algorithm: The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256). If you are using SPEKE or SRT-password encryption, this property must be left blank.
            :param key_type: The type of key that is used for the encryption. If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` . Default: - "static-key"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                encryption_property = mediaconnect.CfnFlowOutput.EncryptionProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn",
                
                    # the properties below are optional
                    algorithm="algorithm",
                    key_type="keyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__12ea6e5693abf5b0e777cf50bd86212ef7db4809c0713169b65c0d055bed2f19)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "secret_arn": secret_arn,
            }
            if algorithm is not None:
                self._values["algorithm"] = algorithm
            if key_type is not None:
                self._values["key_type"] = key_type

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.

            This parameter is required for static key encryption and is not valid for SPEKE encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def algorithm(self) -> typing.Optional[builtins.str]:
            '''The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256).

            If you are using SPEKE or SRT-password encryption, this property must be left blank.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''The type of key that is used for the encryption.

            If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` .

            :default: - "static-key"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.FlowTransitEncryptionKeyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"automatic": "automatic", "secrets_manager": "secretsManager"},
    )
    class FlowTransitEncryptionKeyConfigurationProperty:
        def __init__(
            self,
            *,
            automatic: typing.Any = None,
            secrets_manager: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.SecretsManagerEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param automatic: Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.
            :param secrets_manager: The configuration settings for transit encryption of a flow output using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                flow_transit_encryption_key_configuration_property = mediaconnect.CfnFlowOutput.FlowTransitEncryptionKeyConfigurationProperty(
                    automatic=automatic,
                    secrets_manager=mediaconnect.CfnFlowOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__227e17acb559f1129e2d38ac109471667c1611bee1eedb7dec31ff9273ece0c9)
                check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
                check_type(argname="argument secrets_manager", value=secrets_manager, expected_type=type_hints["secrets_manager"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if automatic is not None:
                self._values["automatic"] = automatic
            if secrets_manager is not None:
                self._values["secrets_manager"] = secrets_manager

        @builtins.property
        def automatic(self) -> typing.Any:
            '''Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration.html#cfn-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-automatic
            '''
            result = self._values.get("automatic")
            return typing.cast(typing.Any, result)

        @builtins.property
        def secrets_manager(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.SecretsManagerEncryptionKeyConfigurationProperty"]]:
            '''The configuration settings for transit encryption of a flow output using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration.html#cfn-mediaconnect-flowoutput-flowtransitencryptionkeyconfiguration-secretsmanager
            '''
            result = self._values.get("secrets_manager")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.SecretsManagerEncryptionKeyConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowTransitEncryptionKeyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.FlowTransitEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_key_configuration": "encryptionKeyConfiguration",
            "encryption_key_type": "encryptionKeyType",
        },
    )
    class FlowTransitEncryptionProperty:
        def __init__(
            self,
            *,
            encryption_key_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.FlowTransitEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            encryption_key_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.

            :param encryption_key_configuration: Configuration settings for flow transit encryption keys.
            :param encryption_key_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-flowtransitencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                flow_transit_encryption_property = mediaconnect.CfnFlowOutput.FlowTransitEncryptionProperty(
                    encryption_key_configuration=mediaconnect.CfnFlowOutput.FlowTransitEncryptionKeyConfigurationProperty(
                        automatic=automatic,
                        secrets_manager=mediaconnect.CfnFlowOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
                
                    # the properties below are optional
                    encryption_key_type="encryptionKeyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__51ad067d64c5f2d51cca478c548fe0d1bac8cb1160599558be1e0c768ec74342)
                check_type(argname="argument encryption_key_configuration", value=encryption_key_configuration, expected_type=type_hints["encryption_key_configuration"])
                check_type(argname="argument encryption_key_type", value=encryption_key_type, expected_type=type_hints["encryption_key_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_key_configuration": encryption_key_configuration,
            }
            if encryption_key_type is not None:
                self._values["encryption_key_type"] = encryption_key_type

        @builtins.property
        def encryption_key_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.FlowTransitEncryptionKeyConfigurationProperty"]:
            '''Configuration settings for flow transit encryption keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-flowtransitencryption.html#cfn-mediaconnect-flowoutput-flowtransitencryption-encryptionkeyconfiguration
            '''
            result = self._values.get("encryption_key_configuration")
            assert result is not None, "Required property 'encryption_key_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.FlowTransitEncryptionKeyConfigurationProperty"], result)

        @builtins.property
        def encryption_key_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-flowtransitencryption.html#cfn-mediaconnect-flowoutput-flowtransitencryption-encryptionkeytype
            '''
            result = self._values.get("encryption_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowTransitEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.InterfaceProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class InterfaceProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''The VPC interface that is used for the media stream associated with the source or output.

            :param name: The name of the VPC interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-interface.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                interface_property = mediaconnect.CfnFlowOutput.InterfaceProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5cc7770548eb391a3e7796f01956da0a9add137c57ab671911bb6c1a675e3dcd)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the VPC interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-interface.html#cfn-mediaconnect-flowoutput-interface-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InterfaceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.MediaStreamOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encoding_name": "encodingName",
            "media_stream_name": "mediaStreamName",
            "destination_configurations": "destinationConfigurations",
            "encoding_parameters": "encodingParameters",
        },
    )
    class MediaStreamOutputConfigurationProperty:
        def __init__(
            self,
            *,
            encoding_name: builtins.str,
            media_stream_name: builtins.str,
            destination_configurations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.DestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            encoding_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.EncodingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The media stream that is associated with the output, and the parameters for that association.

            :param encoding_name: The format that was used to encode the data. For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.
            :param media_stream_name: The name of the media stream.
            :param destination_configurations: The transport parameters that are associated with each outbound media stream.
            :param encoding_parameters: A collection of parameters that determine how MediaConnect will convert the content. These fields only apply to outputs on flows that have a CDI source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                media_stream_output_configuration_property = mediaconnect.CfnFlowOutput.MediaStreamOutputConfigurationProperty(
                    encoding_name="encodingName",
                    media_stream_name="mediaStreamName",
                
                    # the properties below are optional
                    destination_configurations=[mediaconnect.CfnFlowOutput.DestinationConfigurationProperty(
                        destination_ip="destinationIp",
                        destination_port=123,
                        interface=mediaconnect.CfnFlowOutput.InterfaceProperty(
                            name="name"
                        )
                    )],
                    encoding_parameters=mediaconnect.CfnFlowOutput.EncodingParametersProperty(
                        compression_factor=123,
                
                        # the properties below are optional
                        encoder_profile="encoderProfile"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__faa5e437983e66807a96f2eedebbdd774906faf99c35e9c25ec0ff0f66c49af3)
                check_type(argname="argument encoding_name", value=encoding_name, expected_type=type_hints["encoding_name"])
                check_type(argname="argument media_stream_name", value=media_stream_name, expected_type=type_hints["media_stream_name"])
                check_type(argname="argument destination_configurations", value=destination_configurations, expected_type=type_hints["destination_configurations"])
                check_type(argname="argument encoding_parameters", value=encoding_parameters, expected_type=type_hints["encoding_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encoding_name": encoding_name,
                "media_stream_name": media_stream_name,
            }
            if destination_configurations is not None:
                self._values["destination_configurations"] = destination_configurations
            if encoding_parameters is not None:
                self._values["encoding_parameters"] = encoding_parameters

        @builtins.property
        def encoding_name(self) -> builtins.str:
            '''The format that was used to encode the data.

            For ancillary data streams, set the encoding name to smpte291. For audio streams, set the encoding name to pcm. For video, 2110 streams, set the encoding name to raw. For video, JPEG XS streams, set the encoding name to jxsv.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration.html#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-encodingname
            '''
            result = self._values.get("encoding_name")
            assert result is not None, "Required property 'encoding_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def media_stream_name(self) -> builtins.str:
            '''The name of the media stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration.html#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-mediastreamname
            '''
            result = self._values.get("media_stream_name")
            assert result is not None, "Required property 'media_stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_configurations(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.DestinationConfigurationProperty"]]]]:
            '''The transport parameters that are associated with each outbound media stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration.html#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-destinationconfigurations
            '''
            result = self._values.get("destination_configurations")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.DestinationConfigurationProperty"]]]], result)

        @builtins.property
        def encoding_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.EncodingParametersProperty"]]:
            '''A collection of parameters that determine how MediaConnect will convert the content.

            These fields only apply to outputs on flows that have a CDI source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-mediastreamoutputconfiguration.html#cfn-mediaconnect-flowoutput-mediastreamoutputconfiguration-encodingparameters
            '''
            result = self._values.get("encoding_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.EncodingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaStreamOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.SecretsManagerEncryptionKeyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "secret_arn": "secretArn"},
    )
    class SecretsManagerEncryptionKeyConfigurationProperty:
        def __init__(self, *, role_arn: builtins.str, secret_arn: builtins.str) -> None:
            '''The configuration settings for transit encryption of a flow output using AWS Secrets Manager, including the secret ARN and role ARN.

            :param role_arn: The ARN of the IAM role used for transit encryption to the router input using AWS Secrets Manager.
            :param secret_arn: The ARN of the AWS Secrets Manager secret used for transit encryption to the router input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                secrets_manager_encryption_key_configuration_property = mediaconnect.CfnFlowOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__006c867b16e13c1b73b4efbe08794e9b0fe37a42ca38d09660e0ccef770f44f2)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "secret_arn": secret_arn,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role used for transit encryption to the router input using AWS Secrets Manager.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration.html#cfn-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The ARN of the AWS Secrets Manager secret used for transit encryption to the router input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration.html#cfn-mediaconnect-flowoutput-secretsmanagerencryptionkeyconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretsManagerEncryptionKeyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for attaching a VPC interface to an resource.

            :param vpc_interface_name: The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-vpcinterfaceattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_attachment_property = mediaconnect.CfnFlowOutput.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7072f99adeda4341a6581cacf2975b777cc5b063364d5416156250ca7f1e5619)
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-vpcinterfaceattachment.html#cfn-mediaconnect-flowoutput-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutputProps",
    jsii_struct_bases=[],
    name_mapping={
        "flow_arn": "flowArn",
        "cidr_allow_list": "cidrAllowList",
        "description": "description",
        "destination": "destination",
        "encryption": "encryption",
        "max_latency": "maxLatency",
        "media_stream_output_configurations": "mediaStreamOutputConfigurations",
        "min_latency": "minLatency",
        "name": "name",
        "ndi_program_name": "ndiProgramName",
        "ndi_speed_hq_quality": "ndiSpeedHqQuality",
        "output_status": "outputStatus",
        "port": "port",
        "protocol": "protocol",
        "remote_id": "remoteId",
        "router_integration_state": "routerIntegrationState",
        "router_integration_transit_encryption": "routerIntegrationTransitEncryption",
        "smoothing_latency": "smoothingLatency",
        "stream_id": "streamId",
        "vpc_interface_attachment": "vpcInterfaceAttachment",
    },
)
class CfnFlowOutputProps:
    def __init__(
        self,
        *,
        flow_arn: builtins.str,
        cidr_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        destination: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        media_stream_output_configurations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.MediaStreamOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        min_latency: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        ndi_program_name: typing.Optional[builtins.str] = None,
        ndi_speed_hq_quality: typing.Optional[jsii.Number] = None,
        output_status: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        remote_id: typing.Optional[builtins.str] = None,
        router_integration_state: typing.Optional[builtins.str] = None,
        router_integration_transit_encryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.FlowTransitEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        smoothing_latency: typing.Optional[jsii.Number] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_attachment: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowOutput.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlowOutput``.

        :param flow_arn: The Amazon Resource Name (ARN) of the flow this output is attached to.
        :param cidr_allow_list: The range of IP addresses that should be allowed to initiate output requests to this flow. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        :param description: A description of the output. This description appears only on the MediaConnect console and will not be seen by the end user.
        :param destination: The IP address where you want to send the output.
        :param encryption: The type of key used for the encryption. If no ``keyType`` is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.
        :param max_latency: The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
        :param media_stream_output_configurations: The media streams that are associated with the output, and the parameters for those associations.
        :param min_latency: The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
        :param name: The name of the bridge's output.
        :param ndi_program_name: A suffix for the names of the NDI sources that the flow creates. If a custom name isn't specified, MediaConnect uses the output name.
        :param ndi_speed_hq_quality: A quality setting for the NDI Speed HQ encoder.
        :param output_status: An indication of whether the output should transmit data or not.
        :param port: The port to use when content is distributed to this output.
        :param protocol: The protocol to use for the output. .. epigraph:: AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.
        :param remote_id: The remote ID for the Zixi-pull stream.
        :param router_integration_state: 
        :param router_integration_transit_encryption: Encryption information.
        :param smoothing_latency: The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
        :param stream_id: The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
        :param vpc_interface_attachment: The name of the VPC interface attachment to use for this output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            # automatic: Any
            
            cfn_flow_output_props = mediaconnect.CfnFlowOutputProps(
                flow_arn="flowArn",
            
                # the properties below are optional
                cidr_allow_list=["cidrAllowList"],
                description="description",
                destination="destination",
                encryption=mediaconnect.CfnFlowOutput.EncryptionProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn",
            
                    # the properties below are optional
                    algorithm="algorithm",
                    key_type="keyType"
                ),
                max_latency=123,
                media_stream_output_configurations=[mediaconnect.CfnFlowOutput.MediaStreamOutputConfigurationProperty(
                    encoding_name="encodingName",
                    media_stream_name="mediaStreamName",
            
                    # the properties below are optional
                    destination_configurations=[mediaconnect.CfnFlowOutput.DestinationConfigurationProperty(
                        destination_ip="destinationIp",
                        destination_port=123,
                        interface=mediaconnect.CfnFlowOutput.InterfaceProperty(
                            name="name"
                        )
                    )],
                    encoding_parameters=mediaconnect.CfnFlowOutput.EncodingParametersProperty(
                        compression_factor=123,
            
                        # the properties below are optional
                        encoder_profile="encoderProfile"
                    )
                )],
                min_latency=123,
                name="name",
                ndi_program_name="ndiProgramName",
                ndi_speed_hq_quality=123,
                output_status="outputStatus",
                port=123,
                protocol="protocol",
                remote_id="remoteId",
                router_integration_state="routerIntegrationState",
                router_integration_transit_encryption=mediaconnect.CfnFlowOutput.FlowTransitEncryptionProperty(
                    encryption_key_configuration=mediaconnect.CfnFlowOutput.FlowTransitEncryptionKeyConfigurationProperty(
                        automatic=automatic,
                        secrets_manager=mediaconnect.CfnFlowOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
            
                    # the properties below are optional
                    encryption_key_type="encryptionKeyType"
                ),
                smoothing_latency=123,
                stream_id="streamId",
                vpc_interface_attachment=mediaconnect.CfnFlowOutput.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90cee4cbdefa91956af92950bb2bfd2da4fa4f982f439596444cda5251a2c34d)
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument cidr_allow_list", value=cidr_allow_list, expected_type=type_hints["cidr_allow_list"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument max_latency", value=max_latency, expected_type=type_hints["max_latency"])
            check_type(argname="argument media_stream_output_configurations", value=media_stream_output_configurations, expected_type=type_hints["media_stream_output_configurations"])
            check_type(argname="argument min_latency", value=min_latency, expected_type=type_hints["min_latency"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument ndi_program_name", value=ndi_program_name, expected_type=type_hints["ndi_program_name"])
            check_type(argname="argument ndi_speed_hq_quality", value=ndi_speed_hq_quality, expected_type=type_hints["ndi_speed_hq_quality"])
            check_type(argname="argument output_status", value=output_status, expected_type=type_hints["output_status"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument remote_id", value=remote_id, expected_type=type_hints["remote_id"])
            check_type(argname="argument router_integration_state", value=router_integration_state, expected_type=type_hints["router_integration_state"])
            check_type(argname="argument router_integration_transit_encryption", value=router_integration_transit_encryption, expected_type=type_hints["router_integration_transit_encryption"])
            check_type(argname="argument smoothing_latency", value=smoothing_latency, expected_type=type_hints["smoothing_latency"])
            check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
            check_type(argname="argument vpc_interface_attachment", value=vpc_interface_attachment, expected_type=type_hints["vpc_interface_attachment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_arn": flow_arn,
        }
        if cidr_allow_list is not None:
            self._values["cidr_allow_list"] = cidr_allow_list
        if description is not None:
            self._values["description"] = description
        if destination is not None:
            self._values["destination"] = destination
        if encryption is not None:
            self._values["encryption"] = encryption
        if max_latency is not None:
            self._values["max_latency"] = max_latency
        if media_stream_output_configurations is not None:
            self._values["media_stream_output_configurations"] = media_stream_output_configurations
        if min_latency is not None:
            self._values["min_latency"] = min_latency
        if name is not None:
            self._values["name"] = name
        if ndi_program_name is not None:
            self._values["ndi_program_name"] = ndi_program_name
        if ndi_speed_hq_quality is not None:
            self._values["ndi_speed_hq_quality"] = ndi_speed_hq_quality
        if output_status is not None:
            self._values["output_status"] = output_status
        if port is not None:
            self._values["port"] = port
        if protocol is not None:
            self._values["protocol"] = protocol
        if remote_id is not None:
            self._values["remote_id"] = remote_id
        if router_integration_state is not None:
            self._values["router_integration_state"] = router_integration_state
        if router_integration_transit_encryption is not None:
            self._values["router_integration_transit_encryption"] = router_integration_transit_encryption
        if smoothing_latency is not None:
            self._values["smoothing_latency"] = smoothing_latency
        if stream_id is not None:
            self._values["stream_id"] = stream_id
        if vpc_interface_attachment is not None:
            self._values["vpc_interface_attachment"] = vpc_interface_attachment

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow this output is attached to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-flowarn
        '''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidr_allow_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The range of IP addresses that should be allowed to initiate output requests to this flow.

        These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-cidrallowlist
        '''
        result = self._values.get("cidr_allow_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the output.

        This description appears only on the MediaConnect console and will not be seen by the end user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''The IP address where you want to send the output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-destination
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.EncryptionProperty"]]:
        '''The type of key used for the encryption.

        If no ``keyType`` is provided, the service will use the default setting (static-key). Allowable encryption types: static-key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-encryption
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.EncryptionProperty"]], result)

    @builtins.property
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''The maximum latency in milliseconds.

        This parameter applies only to RIST-based and Zixi-based streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-maxlatency
        '''
        result = self._values.get("max_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def media_stream_output_configurations(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.MediaStreamOutputConfigurationProperty"]]]]:
        '''The media streams that are associated with the output, and the parameters for those associations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-mediastreamoutputconfigurations
        '''
        result = self._values.get("media_stream_output_configurations")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.MediaStreamOutputConfigurationProperty"]]]], result)

    @builtins.property
    def min_latency(self) -> typing.Optional[jsii.Number]:
        '''The minimum latency in milliseconds for SRT-based streams.

        In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-minlatency
        '''
        result = self._values.get("min_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the bridge's output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ndi_program_name(self) -> typing.Optional[builtins.str]:
        '''A suffix for the names of the NDI sources that the flow creates.

        If a custom name isn't specified, MediaConnect uses the output name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-ndiprogramname
        '''
        result = self._values.get("ndi_program_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ndi_speed_hq_quality(self) -> typing.Optional[jsii.Number]:
        '''A quality setting for the NDI Speed HQ encoder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-ndispeedhqquality
        '''
        result = self._values.get("ndi_speed_hq_quality")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def output_status(self) -> typing.Optional[builtins.str]:
        '''An indication of whether the output should transmit data or not.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-outputstatus
        '''
        result = self._values.get("output_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port to use when content is distributed to this output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol to use for the output.

        .. epigraph::

           AWS Elemental MediaConnect no longer supports the Fujitsu QoS protocol. This reference is maintained for legacy purposes only.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def remote_id(self) -> typing.Optional[builtins.str]:
        '''The remote ID for the Zixi-pull stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-remoteid
        '''
        result = self._values.get("remote_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def router_integration_state(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-routerintegrationstate
        '''
        result = self._values.get("router_integration_state")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def router_integration_transit_encryption(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.FlowTransitEncryptionProperty"]]:
        '''Encryption information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-routerintegrationtransitencryption
        '''
        result = self._values.get("router_integration_transit_encryption")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.FlowTransitEncryptionProperty"]], result)

    @builtins.property
    def smoothing_latency(self) -> typing.Optional[jsii.Number]:
        '''The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-smoothinglatency
        '''
        result = self._values.get("smoothing_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''The stream ID that you want to use for this transport.

        This parameter applies only to Zixi and SRT caller-based streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-streamid
        '''
        result = self._values.get("stream_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_interface_attachment(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.VpcInterfaceAttachmentProperty"]]:
        '''The name of the VPC interface attachment to use for this output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-vpcinterfaceattachment
        '''
        result = self._values.get("vpc_interface_attachment")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowOutput.VpcInterfaceAttachmentProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowOutputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source": "source",
        "availability_zone": "availabilityZone",
        "flow_size": "flowSize",
        "maintenance": "maintenance",
        "media_streams": "mediaStreams",
        "ndi_config": "ndiConfig",
        "source_failover_config": "sourceFailoverConfig",
        "source_monitoring_config": "sourceMonitoringConfig",
        "vpc_interfaces": "vpcInterfaces",
    },
)
class CfnFlowProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        source: typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.SourceProperty", typing.Dict[builtins.str, typing.Any]]],
        availability_zone: typing.Optional[builtins.str] = None,
        flow_size: typing.Optional[builtins.str] = None,
        maintenance: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.MaintenanceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        media_streams: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.MediaStreamProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ndi_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.NdiConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_failover_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.FailoverConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_monitoring_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.SourceMonitoringConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_interfaces: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlow.VpcInterfaceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlow``.

        :param name: The name of the flow.
        :param source: The settings for the source that you want to use for the new flow.
        :param availability_zone: The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS Region.
        :param flow_size: Determines the processing capacity and feature set of the flow. Set this optional parameter to LARGE if you want to enable NDI outputs on the flow.
        :param maintenance: The maintenance settings you want to use for the flow.
        :param media_streams: The media streams that are associated with the flow. After you associate a media stream with a source, you can also associate it with outputs on the flow.
        :param ndi_config: Specifies the configuration settings for NDI outputs. Required when the flow includes NDI outputs.
        :param source_failover_config: The settings for source failover.
        :param source_monitoring_config: The settings for source monitoring.
        :param vpc_interfaces: The VPC Interfaces for this flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            # automatic: Any
            
            cfn_flow_props = mediaconnect.CfnFlowProps(
                name="name",
                source=mediaconnect.CfnFlow.SourceProperty(
                    decryption=mediaconnect.CfnFlow.EncryptionProperty(
                        role_arn="roleArn",
            
                        # the properties below are optional
                        algorithm="algorithm",
                        constant_initialization_vector="constantInitializationVector",
                        device_id="deviceId",
                        key_type="keyType",
                        region="region",
                        resource_id="resourceId",
                        secret_arn="secretArn",
                        url="url"
                    ),
                    description="description",
                    entitlement_arn="entitlementArn",
                    gateway_bridge_source=mediaconnect.CfnFlow.GatewayBridgeSourceProperty(
                        bridge_arn="bridgeArn",
            
                        # the properties below are optional
                        vpc_interface_attachment=mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty(
                            vpc_interface_name="vpcInterfaceName"
                        )
                    ),
                    ingest_ip="ingestIp",
                    ingest_port=123,
                    max_bitrate=123,
                    max_latency=123,
                    max_sync_buffer=123,
                    media_stream_source_configurations=[mediaconnect.CfnFlow.MediaStreamSourceConfigurationProperty(
                        encoding_name="encodingName",
                        media_stream_name="mediaStreamName",
            
                        # the properties below are optional
                        input_configurations=[mediaconnect.CfnFlow.InputConfigurationProperty(
                            input_port=123,
                            interface=mediaconnect.CfnFlow.InterfaceProperty(
                                name="name"
                            )
                        )]
                    )],
                    min_latency=123,
                    name="name",
                    protocol="protocol",
                    router_integration_state="routerIntegrationState",
                    router_integration_transit_decryption=mediaconnect.CfnFlow.FlowTransitEncryptionProperty(
                        encryption_key_configuration=mediaconnect.CfnFlow.FlowTransitEncryptionKeyConfigurationProperty(
                            automatic=automatic,
                            secrets_manager=mediaconnect.CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
            
                        # the properties below are optional
                        encryption_key_type="encryptionKeyType"
                    ),
                    sender_control_port=123,
                    sender_ip_address="senderIpAddress",
                    source_arn="sourceArn",
                    source_ingest_port="sourceIngestPort",
                    source_listener_address="sourceListenerAddress",
                    source_listener_port=123,
                    stream_id="streamId",
                    vpc_interface_name="vpcInterfaceName",
                    whitelist_cidr="whitelistCidr"
                ),
            
                # the properties below are optional
                availability_zone="availabilityZone",
                flow_size="flowSize",
                maintenance=mediaconnect.CfnFlow.MaintenanceProperty(
                    maintenance_day="maintenanceDay",
                    maintenance_start_hour="maintenanceStartHour"
                ),
                media_streams=[mediaconnect.CfnFlow.MediaStreamProperty(
                    media_stream_id=123,
                    media_stream_name="mediaStreamName",
                    media_stream_type="mediaStreamType",
            
                    # the properties below are optional
                    attributes=mediaconnect.CfnFlow.MediaStreamAttributesProperty(
                        fmtp=mediaconnect.CfnFlow.FmtpProperty(
                            channel_order="channelOrder",
                            colorimetry="colorimetry",
                            exact_framerate="exactFramerate",
                            par="par",
                            range="range",
                            scan_mode="scanMode",
                            tcs="tcs"
                        ),
                        lang="lang"
                    ),
                    clock_rate=123,
                    description="description",
                    fmt=123,
                    video_format="videoFormat"
                )],
                ndi_config=mediaconnect.CfnFlow.NdiConfigProperty(
                    machine_name="machineName",
                    ndi_discovery_servers=[mediaconnect.CfnFlow.NdiDiscoveryServerConfigProperty(
                        discovery_server_address="discoveryServerAddress",
                        vpc_interface_adapter="vpcInterfaceAdapter",
            
                        # the properties below are optional
                        discovery_server_port=123
                    )],
                    ndi_state="ndiState"
                ),
                source_failover_config=mediaconnect.CfnFlow.FailoverConfigProperty(
                    failover_mode="failoverMode",
                    recovery_window=123,
                    source_priority=mediaconnect.CfnFlow.SourcePriorityProperty(
                        primary_source="primarySource"
                    ),
                    state="state"
                ),
                source_monitoring_config=mediaconnect.CfnFlow.SourceMonitoringConfigProperty(
                    audio_monitoring_settings=[mediaconnect.CfnFlow.AudioMonitoringSettingProperty(
                        silent_audio=mediaconnect.CfnFlow.SilentAudioProperty(
                            state="state",
                            threshold_seconds=123
                        )
                    )],
                    content_quality_analysis_state="contentQualityAnalysisState",
                    thumbnail_state="thumbnailState",
                    video_monitoring_settings=[mediaconnect.CfnFlow.VideoMonitoringSettingProperty(
                        black_frames=mediaconnect.CfnFlow.BlackFramesProperty(
                            state="state",
                            threshold_seconds=123
                        ),
                        frozen_frames=mediaconnect.CfnFlow.FrozenFramesProperty(
                            state="state",
                            threshold_seconds=123
                        )
                    )]
                ),
                vpc_interfaces=[mediaconnect.CfnFlow.VpcInterfaceProperty(
                    name="name",
                    role_arn="roleArn",
                    security_group_ids=["securityGroupIds"],
                    subnet_id="subnetId",
            
                    # the properties below are optional
                    network_interface_ids=["networkInterfaceIds"],
                    network_interface_type="networkInterfaceType"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32a16a7697723a7ef816aaa9d297ca08cd44085f922995184f8bfdfde65f0c24)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument flow_size", value=flow_size, expected_type=type_hints["flow_size"])
            check_type(argname="argument maintenance", value=maintenance, expected_type=type_hints["maintenance"])
            check_type(argname="argument media_streams", value=media_streams, expected_type=type_hints["media_streams"])
            check_type(argname="argument ndi_config", value=ndi_config, expected_type=type_hints["ndi_config"])
            check_type(argname="argument source_failover_config", value=source_failover_config, expected_type=type_hints["source_failover_config"])
            check_type(argname="argument source_monitoring_config", value=source_monitoring_config, expected_type=type_hints["source_monitoring_config"])
            check_type(argname="argument vpc_interfaces", value=vpc_interfaces, expected_type=type_hints["vpc_interfaces"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "source": source,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if flow_size is not None:
            self._values["flow_size"] = flow_size
        if maintenance is not None:
            self._values["maintenance"] = maintenance
        if media_streams is not None:
            self._values["media_streams"] = media_streams
        if ndi_config is not None:
            self._values["ndi_config"] = ndi_config
        if source_failover_config is not None:
            self._values["source_failover_config"] = source_failover_config
        if source_monitoring_config is not None:
            self._values["source_monitoring_config"] = source_monitoring_config
        if vpc_interfaces is not None:
            self._values["vpc_interfaces"] = vpc_interfaces

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> typing.Union["_IResolvable_da3f097b", "CfnFlow.SourceProperty"]:
        '''The settings for the source that you want to use for the new flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnFlow.SourceProperty"], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone that you want to create the flow in.

        These options are limited to the Availability Zones within the current AWS Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_size(self) -> typing.Optional[builtins.str]:
        '''Determines the processing capacity and feature set of the flow.

        Set this optional parameter to LARGE if you want to enable NDI outputs on the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-flowsize
        '''
        result = self._values.get("flow_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.MaintenanceProperty"]]:
        '''The maintenance settings you want to use for the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-maintenance
        '''
        result = self._values.get("maintenance")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.MaintenanceProperty"]], result)

    @builtins.property
    def media_streams(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.MediaStreamProperty"]]]]:
        '''The media streams that are associated with the flow.

        After you associate a media stream with a source, you can also associate it with outputs on the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-mediastreams
        '''
        result = self._values.get("media_streams")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.MediaStreamProperty"]]]], result)

    @builtins.property
    def ndi_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.NdiConfigProperty"]]:
        '''Specifies the configuration settings for NDI outputs.

        Required when the flow includes NDI outputs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-ndiconfig
        '''
        result = self._values.get("ndi_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.NdiConfigProperty"]], result)

    @builtins.property
    def source_failover_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FailoverConfigProperty"]]:
        '''The settings for source failover.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-sourcefailoverconfig
        '''
        result = self._values.get("source_failover_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.FailoverConfigProperty"]], result)

    @builtins.property
    def source_monitoring_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SourceMonitoringConfigProperty"]]:
        '''The settings for source monitoring.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-sourcemonitoringconfig
        '''
        result = self._values.get("source_monitoring_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlow.SourceMonitoringConfigProperty"]], result)

    @builtins.property
    def vpc_interfaces(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.VpcInterfaceProperty"]]]]:
        '''The VPC Interfaces for this flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-vpcinterfaces
        '''
        result = self._values.get("vpc_interfaces")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnFlow.VpcInterfaceProperty"]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IFlowSourceRef_b94a8321)
class CfnFlowSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowSource",
):
    '''The ``AWS::MediaConnect::FlowSource`` resource is usedt to add additional sources to an existing flow.

    Adding an additional source requires Failover to be enabled. When you enable Failover, the additional source must use the same protocol as the existing source. A source is the external video content that includes configuration information (encryption and source type) and a network address. Each flow has at least one source. A standard source comes from a source other than another AWS Elemental MediaConnect flow, such as an on-premises encoder.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html
    :cloudformationResource: AWS::MediaConnect::FlowSource
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_flow_source = mediaconnect.CfnFlowSource(self, "MyCfnFlowSource",
            description="description",
            name="name",
        
            # the properties below are optional
            decryption=mediaconnect.CfnFlowSource.EncryptionProperty(
                role_arn="roleArn",
        
                # the properties below are optional
                algorithm="algorithm",
                constant_initialization_vector="constantInitializationVector",
                device_id="deviceId",
                key_type="keyType",
                region="region",
                resource_id="resourceId",
                secret_arn="secretArn",
                url="url"
            ),
            entitlement_arn="entitlementArn",
            flow_arn="flowArn",
            gateway_bridge_source=mediaconnect.CfnFlowSource.GatewayBridgeSourceProperty(
                bridge_arn="bridgeArn",
        
                # the properties below are optional
                vpc_interface_attachment=mediaconnect.CfnFlowSource.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            ),
            ingest_port=123,
            max_bitrate=123,
            max_latency=123,
            min_latency=123,
            protocol="protocol",
            sender_control_port=123,
            sender_ip_address="senderIpAddress",
            source_listener_address="sourceListenerAddress",
            source_listener_port=123,
            stream_id="streamId",
            vpc_interface_name="vpcInterfaceName",
            whitelist_cidr="whitelistCidr"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        description: builtins.str,
        name: builtins.str,
        decryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowSource.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        entitlement_arn: typing.Optional[builtins.str] = None,
        flow_arn: typing.Optional[builtins.str] = None,
        gateway_bridge_source: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowSource.GatewayBridgeSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ingest_port: typing.Optional[jsii.Number] = None,
        max_bitrate: typing.Optional[jsii.Number] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        min_latency: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        sender_control_port: typing.Optional[jsii.Number] = None,
        sender_ip_address: typing.Optional[builtins.str] = None,
        source_listener_address: typing.Optional[builtins.str] = None,
        source_listener_port: typing.Optional[jsii.Number] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_name: typing.Optional[builtins.str] = None,
        whitelist_cidr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::FlowSource``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description for the source. This value is not used or seen outside of the current MediaConnect account.
        :param name: The name of the source.
        :param decryption: The type of encryption that is used on the content ingested from this source. Allowable encryption types: static-key.
        :param entitlement_arn: The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator's flow.
        :param flow_arn: The Amazon Resource Name (ARN) of the flow this source is connected to. The flow must have Failover enabled to add an additional source.
        :param gateway_bridge_source: The bridge's source.
        :param ingest_port: The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088.
        :param max_bitrate: The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams.
        :param max_latency: The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
        :param min_latency: The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
        :param protocol: The protocol that the source uses to deliver the content to MediaConnect. Adding additional sources to an existing flow requires Failover to be enabled. When you enable Failover, the additional source must use the same protocol as the existing source. Only the following protocols support failover: Zixi-push, RTP-FEC, RTP, RIST and SRT protocols. If you use failover with SRT caller or listener, the ``FailoverMode`` property must be set to ``FAILOVER`` . The ``FailoverMode`` property is found in the ``FailoverConfig`` resource of the same flow ARN you used for the source's ``FlowArn`` property. SRT caller/listener does not support merge mode failover.
        :param sender_control_port: The port that the flow uses to send outbound requests to initiate connection with the sender.
        :param sender_ip_address: The IP address that the flow communicates with to initiate connection with the sender.
        :param source_listener_address: Source IP or domain name for SRT-caller protocol.
        :param source_listener_port: Source port for SRT-caller protocol.
        :param stream_id: The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
        :param vpc_interface_name: The name of the VPC interface to use for this source.
        :param whitelist_cidr: The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f14359cee01f3506467d65b7510ab8dfc45bad9d560a39ede9f196eb193c6d3f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowSourceProps(
            description=description,
            name=name,
            decryption=decryption,
            entitlement_arn=entitlement_arn,
            flow_arn=flow_arn,
            gateway_bridge_source=gateway_bridge_source,
            ingest_port=ingest_port,
            max_bitrate=max_bitrate,
            max_latency=max_latency,
            min_latency=min_latency,
            protocol=protocol,
            sender_control_port=sender_control_port,
            sender_ip_address=sender_ip_address,
            source_listener_address=source_listener_address,
            source_listener_port=source_listener_port,
            stream_id=stream_id,
            vpc_interface_name=vpc_interface_name,
            whitelist_cidr=whitelist_cidr,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnFlowSource")
    @builtins.classmethod
    def is_cfn_flow_source(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFlowSource.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__516c9ee96b7a84e3798e10ffbf9f23be95e407b2f0376f64a16b0109b33586e9)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFlowSource", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3fd76f8220dae1a8772091086f599345d67d89097d2f85b9307e60f66eebda)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8852c4ff5ee8f7563716bed6f284156dda285971d2136f38033b85a389bd073b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIngestIp")
    def attr_ingest_ip(self) -> builtins.str:
        '''The IP address that the flow listens on for incoming content.

        :cloudformationAttribute: IngestIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIngestIp"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceArn")
    def attr_source_arn(self) -> builtins.str:
        '''The ARN of the source.

        :cloudformationAttribute: SourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceIngestPort")
    def attr_source_ingest_port(self) -> builtins.str:
        '''The port that the flow listens on for incoming content.

        If the protocol of the source is Zixi, the port must be set to 2088.

        :cloudformationAttribute: SourceIngestPort
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceIngestPort"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="flowSourceRef")
    def flow_source_ref(self) -> "_FlowSourceReference_0d57ee68":
        '''A reference to a FlowSource resource.'''
        return typing.cast("_FlowSourceReference_0d57ee68", jsii.get(self, "flowSourceRef"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description for the source.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__169574c8d258397d0753838843606fa3a6f2792dbfbe9f805a3263cc2ce8bf99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56248647932d6154f5cc0ea3f1df2a2bb25f298ef25872b32e9b4dd6f8e0ff07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="decryption")
    def decryption(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.EncryptionProperty"]]:
        '''The type of encryption that is used on the content ingested from this source.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.EncryptionProperty"]], jsii.get(self, "decryption"))

    @decryption.setter
    def decryption(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.EncryptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__713d2beba8d5285adfd07ee3f7ca737392fb89294806031a6cc288bb72c8f180)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decryption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="entitlementArn")
    def entitlement_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the entitlement that allows you to subscribe to this flow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entitlementArn"))

    @entitlement_arn.setter
    def entitlement_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93ba0fab964dfcf99d0e38ef04172e971ea1753fa1d98e88458675e4386302dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entitlementArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the flow this source is connected to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a393333c9ad7ce002f047c125d9ee3348efa283a66d9def5950529184e3be294)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="gatewayBridgeSource")
    def gateway_bridge_source(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.GatewayBridgeSourceProperty"]]:
        '''The bridge's source.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.GatewayBridgeSourceProperty"]], jsii.get(self, "gatewayBridgeSource"))

    @gateway_bridge_source.setter
    def gateway_bridge_source(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.GatewayBridgeSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5cf895711559ebd9f3d9816442bc2258d4ed6f493bb32badf0ea76f038dd16a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayBridgeSource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ingestPort")
    def ingest_port(self) -> typing.Optional[jsii.Number]:
        '''The port that the flow listens on for incoming content.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ingestPort"))

    @ingest_port.setter
    def ingest_port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8065f994df3b6b1f35a330146835da3506ebb87915688c1139a725cf72b5f618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingestPort", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxBitrate")
    def max_bitrate(self) -> typing.Optional[jsii.Number]:
        '''The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBitrate"))

    @max_bitrate.setter
    def max_bitrate(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e362dd143dad56909dafd2e42bfcb4f36d21b914a7b90872305a01bec7758a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBitrate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxLatency")
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''The maximum latency in milliseconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLatency"))

    @max_latency.setter
    def max_latency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59ebbbae1ffe64a0b2ace0c589cfc271c5cf5155fb97c05e5866f905264c33c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLatency", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="minLatency")
    def min_latency(self) -> typing.Optional[jsii.Number]:
        '''The minimum latency in milliseconds for SRT-based streams.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minLatency"))

    @min_latency.setter
    def min_latency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99ef8a4669e860fa72d8e2f4dc3ad3fe414a8d53d7156d84af37cde5562fb88d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLatency", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol that the source uses to deliver the content to MediaConnect.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb57175f10a9dd5a4e263ec48354d53559458e760a13228af2bc8b2d5a738add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="senderControlPort")
    def sender_control_port(self) -> typing.Optional[jsii.Number]:
        '''The port that the flow uses to send outbound requests to initiate connection with the sender.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "senderControlPort"))

    @sender_control_port.setter
    def sender_control_port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cb25d08779ab67d6811a557f48cd15bde00000d84c5ba57f8165f13a3f72f99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "senderControlPort", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="senderIpAddress")
    def sender_ip_address(self) -> typing.Optional[builtins.str]:
        '''The IP address that the flow communicates with to initiate connection with the sender.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "senderIpAddress"))

    @sender_ip_address.setter
    def sender_ip_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce59a08878045e4b8bc6ff139a2307a1a5d3d8b55ad67c907a140517d9fdee00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "senderIpAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceListenerAddress")
    def source_listener_address(self) -> typing.Optional[builtins.str]:
        '''Source IP or domain name for SRT-caller protocol.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceListenerAddress"))

    @source_listener_address.setter
    def source_listener_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f71f744022b312b3b4bc69179b8e4ce2cdb7fdeb46c179d7c72e3db30ac42e6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceListenerAddress", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sourceListenerPort")
    def source_listener_port(self) -> typing.Optional[jsii.Number]:
        '''Source port for SRT-caller protocol.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sourceListenerPort"))

    @source_listener_port.setter
    def source_listener_port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc08edbf9070870e3f4ff641570a5fbe7bd92875ead1c75b9697e32c94084f4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceListenerPort", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="streamId")
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''The stream ID that you want to use for this transport.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamId"))

    @stream_id.setter
    def stream_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f3b58b86420e937edcb73256eccae2a94f77b56863e967c6b79430f30f5ae00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcInterfaceName")
    def vpc_interface_name(self) -> typing.Optional[builtins.str]:
        '''The name of the VPC interface to use for this source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcInterfaceName"))

    @vpc_interface_name.setter
    def vpc_interface_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaca9be06dd26e302844cbceb849d87c083af662bbe659afe5a1819fd6ac9f7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcInterfaceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="whitelistCidr")
    def whitelist_cidr(self) -> typing.Optional[builtins.str]:
        '''The range of IP addresses that should be allowed to contribute content to your source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whitelistCidr"))

    @whitelist_cidr.setter
    def whitelist_cidr(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45499d5b323bea3d710e7e2165d62c80e1951ab949967a5138abfc7e37f673dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whitelistCidr", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowSource.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "algorithm": "algorithm",
            "constant_initialization_vector": "constantInitializationVector",
            "device_id": "deviceId",
            "key_type": "keyType",
            "region": "region",
            "resource_id": "resourceId",
            "secret_arn": "secretArn",
            "url": "url",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            algorithm: typing.Optional[builtins.str] = None,
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            device_id: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Encryption information.

            :param role_arn: The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).
            :param algorithm: The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256). If you are using SPEKE or SRT-password encryption, this property must be left blank.
            :param constant_initialization_vector: A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
            :param device_id: The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param key_type: The type of key that is used for the encryption. If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` . Default: - "static-key"
            :param region: The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param resource_id: An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param secret_arn: The ARN of the secret that you created in AWS Secrets Manager to store the encryption key. This parameter is required for static key encryption and is not valid for SPEKE encryption.
            :param url: The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                encryption_property = mediaconnect.CfnFlowSource.EncryptionProperty(
                    role_arn="roleArn",
                
                    # the properties below are optional
                    algorithm="algorithm",
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc2e1b7c07a7a0aadaba7f4f2e0a0214eedc45460e5f4d6b8a4e1af4b33ff561)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument constant_initialization_vector", value=constant_initialization_vector, expected_type=type_hints["constant_initialization_vector"])
                check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
            }
            if algorithm is not None:
                self._values["algorithm"] = algorithm
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if device_id is not None:
                self._values["device_id"] = device_id
            if key_type is not None:
                self._values["key_type"] = key_type
            if region is not None:
                self._values["region"] = region
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the role that you created during setup (when you set up MediaConnect as a trusted entity).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def algorithm(self) -> typing.Optional[builtins.str]:
            '''The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256).

            If you are using SPEKE or SRT-password encryption, this property must be left blank.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content.

            This parameter is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_id(self) -> typing.Optional[builtins.str]:
            '''The value of one of the devices that you configured with your digital rights management (DRM) platform key provider.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-deviceid
            '''
            result = self._values.get("device_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''The type of key that is used for the encryption.

            If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` .

            :default: - "static-key"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region that the API Gateway proxy endpoint was created in.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''An identifier for the content.

            The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.

            This parameter is required for static key encryption and is not valid for SPEKE encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL from the API Gateway proxy that you set up to talk to your key server.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowSource.GatewayBridgeSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bridge_arn": "bridgeArn",
            "vpc_interface_attachment": "vpcInterfaceAttachment",
        },
    )
    class GatewayBridgeSourceProperty:
        def __init__(
            self,
            *,
            bridge_arn: builtins.str,
            vpc_interface_attachment: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowSource.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source configuration for cloud flows receiving a stream from a bridge.

            :param bridge_arn: The ARN of the bridge feeding this flow.
            :param vpc_interface_attachment: The name of the VPC interface attachment to use for this bridge source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-gatewaybridgesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                gateway_bridge_source_property = mediaconnect.CfnFlowSource.GatewayBridgeSourceProperty(
                    bridge_arn="bridgeArn",
                
                    # the properties below are optional
                    vpc_interface_attachment=mediaconnect.CfnFlowSource.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30ed56e867002e6d71070cfe3db49514b39a97f4380a7b126282076647a88405)
                check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
                check_type(argname="argument vpc_interface_attachment", value=vpc_interface_attachment, expected_type=type_hints["vpc_interface_attachment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bridge_arn": bridge_arn,
            }
            if vpc_interface_attachment is not None:
                self._values["vpc_interface_attachment"] = vpc_interface_attachment

        @builtins.property
        def bridge_arn(self) -> builtins.str:
            '''The ARN of the bridge feeding this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-gatewaybridgesource.html#cfn-mediaconnect-flowsource-gatewaybridgesource-bridgearn
            '''
            result = self._values.get("bridge_arn")
            assert result is not None, "Required property 'bridge_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_interface_attachment(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.VpcInterfaceAttachmentProperty"]]:
            '''The name of the VPC interface attachment to use for this bridge source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-gatewaybridgesource.html#cfn-mediaconnect-flowsource-gatewaybridgesource-vpcinterfaceattachment
            '''
            result = self._values.get("vpc_interface_attachment")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.VpcInterfaceAttachmentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayBridgeSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowSource.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for attaching a VPC interface to an resource.

            :param vpc_interface_name: The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-vpcinterfaceattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_attachment_property = mediaconnect.CfnFlowSource.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91f29aa73d1270b98bef9297507fc5368a6213455c4fab06ce82317542ccbecb)
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-vpcinterfaceattachment.html#cfn-mediaconnect-flowsource-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "decryption": "decryption",
        "entitlement_arn": "entitlementArn",
        "flow_arn": "flowArn",
        "gateway_bridge_source": "gatewayBridgeSource",
        "ingest_port": "ingestPort",
        "max_bitrate": "maxBitrate",
        "max_latency": "maxLatency",
        "min_latency": "minLatency",
        "protocol": "protocol",
        "sender_control_port": "senderControlPort",
        "sender_ip_address": "senderIpAddress",
        "source_listener_address": "sourceListenerAddress",
        "source_listener_port": "sourceListenerPort",
        "stream_id": "streamId",
        "vpc_interface_name": "vpcInterfaceName",
        "whitelist_cidr": "whitelistCidr",
    },
)
class CfnFlowSourceProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        name: builtins.str,
        decryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowSource.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        entitlement_arn: typing.Optional[builtins.str] = None,
        flow_arn: typing.Optional[builtins.str] = None,
        gateway_bridge_source: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnFlowSource.GatewayBridgeSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ingest_port: typing.Optional[jsii.Number] = None,
        max_bitrate: typing.Optional[jsii.Number] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        min_latency: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        sender_control_port: typing.Optional[jsii.Number] = None,
        sender_ip_address: typing.Optional[builtins.str] = None,
        source_listener_address: typing.Optional[builtins.str] = None,
        source_listener_port: typing.Optional[jsii.Number] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_name: typing.Optional[builtins.str] = None,
        whitelist_cidr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlowSource``.

        :param description: A description for the source. This value is not used or seen outside of the current MediaConnect account.
        :param name: The name of the source.
        :param decryption: The type of encryption that is used on the content ingested from this source. Allowable encryption types: static-key.
        :param entitlement_arn: The ARN of the entitlement that allows you to subscribe to this flow. The entitlement is set by the flow originator, and the ARN is generated as part of the originator's flow.
        :param flow_arn: The Amazon Resource Name (ARN) of the flow this source is connected to. The flow must have Failover enabled to add an additional source.
        :param gateway_bridge_source: The bridge's source.
        :param ingest_port: The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088.
        :param max_bitrate: The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams.
        :param max_latency: The maximum latency in milliseconds. This parameter applies only to RIST-based and Zixi-based streams.
        :param min_latency: The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
        :param protocol: The protocol that the source uses to deliver the content to MediaConnect. Adding additional sources to an existing flow requires Failover to be enabled. When you enable Failover, the additional source must use the same protocol as the existing source. Only the following protocols support failover: Zixi-push, RTP-FEC, RTP, RIST and SRT protocols. If you use failover with SRT caller or listener, the ``FailoverMode`` property must be set to ``FAILOVER`` . The ``FailoverMode`` property is found in the ``FailoverConfig`` resource of the same flow ARN you used for the source's ``FlowArn`` property. SRT caller/listener does not support merge mode failover.
        :param sender_control_port: The port that the flow uses to send outbound requests to initiate connection with the sender.
        :param sender_ip_address: The IP address that the flow communicates with to initiate connection with the sender.
        :param source_listener_address: Source IP or domain name for SRT-caller protocol.
        :param source_listener_port: Source port for SRT-caller protocol.
        :param stream_id: The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
        :param vpc_interface_name: The name of the VPC interface to use for this source.
        :param whitelist_cidr: The range of IP addresses that should be allowed to contribute content to your source. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_flow_source_props = mediaconnect.CfnFlowSourceProps(
                description="description",
                name="name",
            
                # the properties below are optional
                decryption=mediaconnect.CfnFlowSource.EncryptionProperty(
                    role_arn="roleArn",
            
                    # the properties below are optional
                    algorithm="algorithm",
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                ),
                entitlement_arn="entitlementArn",
                flow_arn="flowArn",
                gateway_bridge_source=mediaconnect.CfnFlowSource.GatewayBridgeSourceProperty(
                    bridge_arn="bridgeArn",
            
                    # the properties below are optional
                    vpc_interface_attachment=mediaconnect.CfnFlowSource.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                ),
                ingest_port=123,
                max_bitrate=123,
                max_latency=123,
                min_latency=123,
                protocol="protocol",
                sender_control_port=123,
                sender_ip_address="senderIpAddress",
                source_listener_address="sourceListenerAddress",
                source_listener_port=123,
                stream_id="streamId",
                vpc_interface_name="vpcInterfaceName",
                whitelist_cidr="whitelistCidr"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd2a850713cccb402475afd88e4c523840081ad6429c6abf35e564ea3f27ca1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument decryption", value=decryption, expected_type=type_hints["decryption"])
            check_type(argname="argument entitlement_arn", value=entitlement_arn, expected_type=type_hints["entitlement_arn"])
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument gateway_bridge_source", value=gateway_bridge_source, expected_type=type_hints["gateway_bridge_source"])
            check_type(argname="argument ingest_port", value=ingest_port, expected_type=type_hints["ingest_port"])
            check_type(argname="argument max_bitrate", value=max_bitrate, expected_type=type_hints["max_bitrate"])
            check_type(argname="argument max_latency", value=max_latency, expected_type=type_hints["max_latency"])
            check_type(argname="argument min_latency", value=min_latency, expected_type=type_hints["min_latency"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument sender_control_port", value=sender_control_port, expected_type=type_hints["sender_control_port"])
            check_type(argname="argument sender_ip_address", value=sender_ip_address, expected_type=type_hints["sender_ip_address"])
            check_type(argname="argument source_listener_address", value=source_listener_address, expected_type=type_hints["source_listener_address"])
            check_type(argname="argument source_listener_port", value=source_listener_port, expected_type=type_hints["source_listener_port"])
            check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
            check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            check_type(argname="argument whitelist_cidr", value=whitelist_cidr, expected_type=type_hints["whitelist_cidr"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "name": name,
        }
        if decryption is not None:
            self._values["decryption"] = decryption
        if entitlement_arn is not None:
            self._values["entitlement_arn"] = entitlement_arn
        if flow_arn is not None:
            self._values["flow_arn"] = flow_arn
        if gateway_bridge_source is not None:
            self._values["gateway_bridge_source"] = gateway_bridge_source
        if ingest_port is not None:
            self._values["ingest_port"] = ingest_port
        if max_bitrate is not None:
            self._values["max_bitrate"] = max_bitrate
        if max_latency is not None:
            self._values["max_latency"] = max_latency
        if min_latency is not None:
            self._values["min_latency"] = min_latency
        if protocol is not None:
            self._values["protocol"] = protocol
        if sender_control_port is not None:
            self._values["sender_control_port"] = sender_control_port
        if sender_ip_address is not None:
            self._values["sender_ip_address"] = sender_ip_address
        if source_listener_address is not None:
            self._values["source_listener_address"] = source_listener_address
        if source_listener_port is not None:
            self._values["source_listener_port"] = source_listener_port
        if stream_id is not None:
            self._values["stream_id"] = stream_id
        if vpc_interface_name is not None:
            self._values["vpc_interface_name"] = vpc_interface_name
        if whitelist_cidr is not None:
            self._values["whitelist_cidr"] = whitelist_cidr

    @builtins.property
    def description(self) -> builtins.str:
        '''A description for the source.

        This value is not used or seen outside of the current MediaConnect account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def decryption(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.EncryptionProperty"]]:
        '''The type of encryption that is used on the content ingested from this source.

        Allowable encryption types: static-key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-decryption
        '''
        result = self._values.get("decryption")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.EncryptionProperty"]], result)

    @builtins.property
    def entitlement_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the entitlement that allows you to subscribe to this flow.

        The entitlement is set by the flow originator, and the ARN is generated as part of the originator's flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-entitlementarn
        '''
        result = self._values.get("entitlement_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the flow this source is connected to.

        The flow must have Failover enabled to add an additional source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-flowarn
        '''
        result = self._values.get("flow_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_bridge_source(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.GatewayBridgeSourceProperty"]]:
        '''The bridge's source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-gatewaybridgesource
        '''
        result = self._values.get("gateway_bridge_source")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnFlowSource.GatewayBridgeSourceProperty"]], result)

    @builtins.property
    def ingest_port(self) -> typing.Optional[jsii.Number]:
        '''The port that the flow listens on for incoming content.

        If the protocol of the source is Zixi, the port must be set to 2088.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-ingestport
        '''
        result = self._values.get("ingest_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_bitrate(self) -> typing.Optional[jsii.Number]:
        '''The smoothing max bitrate (in bps) for RIST, RTP, and RTP-FEC streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-maxbitrate
        '''
        result = self._values.get("max_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''The maximum latency in milliseconds.

        This parameter applies only to RIST-based and Zixi-based streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-maxlatency
        '''
        result = self._values.get("max_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_latency(self) -> typing.Optional[jsii.Number]:
        '''The minimum latency in milliseconds for SRT-based streams.

        In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-minlatency
        '''
        result = self._values.get("min_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol that the source uses to deliver the content to MediaConnect.

        Adding additional sources to an existing flow requires Failover to be enabled. When you enable Failover, the additional source must use the same protocol as the existing source. Only the following protocols support failover: Zixi-push, RTP-FEC, RTP, RIST and SRT protocols.

        If you use failover with SRT caller or listener, the ``FailoverMode`` property must be set to ``FAILOVER`` . The ``FailoverMode`` property is found in the ``FailoverConfig`` resource of the same flow ARN you used for the source's ``FlowArn`` property. SRT caller/listener does not support merge mode failover.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sender_control_port(self) -> typing.Optional[jsii.Number]:
        '''The port that the flow uses to send outbound requests to initiate connection with the sender.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-sendercontrolport
        '''
        result = self._values.get("sender_control_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sender_ip_address(self) -> typing.Optional[builtins.str]:
        '''The IP address that the flow communicates with to initiate connection with the sender.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-senderipaddress
        '''
        result = self._values.get("sender_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_listener_address(self) -> typing.Optional[builtins.str]:
        '''Source IP or domain name for SRT-caller protocol.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-sourcelisteneraddress
        '''
        result = self._values.get("source_listener_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_listener_port(self) -> typing.Optional[jsii.Number]:
        '''Source port for SRT-caller protocol.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-sourcelistenerport
        '''
        result = self._values.get("source_listener_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''The stream ID that you want to use for this transport.

        This parameter applies only to Zixi and SRT caller-based streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-streamid
        '''
        result = self._values.get("stream_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_interface_name(self) -> typing.Optional[builtins.str]:
        '''The name of the VPC interface to use for this source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-vpcinterfacename
        '''
        result = self._values.get("vpc_interface_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def whitelist_cidr(self) -> typing.Optional[builtins.str]:
        '''The range of IP addresses that should be allowed to contribute content to your source.

        These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-whitelistcidr
        '''
        result = self._values.get("whitelist_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IFlowVpcInterfaceRef_d5bcec46)
class CfnFlowVpcInterface(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowVpcInterface",
):
    '''The ``AWS::MediaConnect::FlowVpcInterface`` resource is a connection between your AWS Elemental MediaConnect flow and a virtual private cloud (VPC) that you created using the Amazon Virtual Private Cloud service.

    To avoid streaming your content over the public internet, you can add up to two VPC interfaces to your flow and use those connections to transfer content between your VPC and MediaConnect.

    You can update an existing flow to add a VPC interface. If you haven’t created the flow yet, you must create the flow with a temporary standard source by doing the following:

    - Use CloudFormation to create a flow with a standard source that uses to the flow’s public IP address.
    - Use CloudFormation to create a VPC interface to add to this flow. This can also be done as part of the previous step.
    - After CloudFormation has created the flow and the VPC interface, update the source to point to the VPC interface that you created.

    .. epigraph::

       The previous steps must be undone before the CloudFormation stack can be deleted. Because the source is manually updated in step 3, CloudFormation is not aware of this change. The source must be returned to a standard source before CloudFormation stack deletion. > When configuring NDI outputs for your flow, define the VPC interface as a nested attribute within the ``AWS::MediaConnect::Flow`` resource. Do not use the top-level ``AWS::MediaConnect::FlowVpcInterface`` resource type to specify NDI configurations.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html
    :cloudformationResource: AWS::MediaConnect::FlowVpcInterface
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_flow_vpc_interface = mediaconnect.CfnFlowVpcInterface(self, "MyCfnFlowVpcInterface",
            flow_arn="flowArn",
            name="name",
            role_arn="roleArn",
            security_group_ids=["securityGroupIds"],
            subnet_id="subnetId"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        flow_arn: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_id: builtins.str,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::FlowVpcInterface``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param flow_arn: The Amazon Resource Name (ARN) of the flow.
        :param name: The name for the VPC interface. This name must be unique within the flow.
        :param role_arn: The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service.
        :param security_group_ids: A virtual firewall to control inbound and outbound traffic.
        :param subnet_id: The subnet IDs that you want to use for your VPC interface. A range of IP addresses in your VPC. When you create your VPC, you specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. This is the primary CIDR block for your VPC. When you create a subnet for your VPC, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block. The subnets that you use across all VPC interfaces on the flow must be in the same Availability Zone as the flow.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbdfc221c828cffa79a57d6d84dccb050776de58319678209806d7b3bc310582)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowVpcInterfaceProps(
            flow_arn=flow_arn,
            name=name,
            role_arn=role_arn,
            security_group_ids=security_group_ids,
            subnet_id=subnet_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnFlowVpcInterface")
    @builtins.classmethod
    def is_cfn_flow_vpc_interface(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnFlowVpcInterface.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fa6b7ee310467cbf1b90d72ac662a880ec46f0ff1d93db17be2b22f898219cd)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnFlowVpcInterface", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2669da051110c0f17f8e796d79785f21a3eedb15f26aad564f80d786fc0b5008)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb4bbb0359f95aef0014b12311830a206a9476a44d94de97d750a09771a603ae)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrNetworkInterfaceIds")
    def attr_network_interface_ids(self) -> typing.List[builtins.str]:
        '''The IDs of the network interfaces that MediaConnect created in your account.

        :cloudformationAttribute: NetworkInterfaceIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrNetworkInterfaceIds"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="flowVpcInterfaceRef")
    def flow_vpc_interface_ref(self) -> "_FlowVpcInterfaceReference_74070c82":
        '''A reference to a FlowVpcInterface resource.'''
        return typing.cast("_FlowVpcInterfaceReference_74070c82", jsii.get(self, "flowVpcInterfaceRef"))

    @builtins.property
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow.'''
        return typing.cast(builtins.str, jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01b2ebce5fcf204059015d9ab2acd7dd1255fb422e85ba46d8372e7ed14634e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name for the VPC interface.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__315756aca1be9462393133e8a1bd030c6830be9cd62201141209ba92bca00733)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d1a6f274a5840002030ca9431469bb3346277b4320449fb605700060689db4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''A virtual firewall to control inbound and outbound traffic.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22fe25e82013a9b0baddbe815abf51918a6107457c49b594041bb09b37e6db29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        '''The subnet IDs that you want to use for your VPC interface.'''
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21ff66cbd4857ab742f4461a355254e9a8da4cf04f8543fbb07ab7e6bde77b87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowVpcInterfaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "flow_arn": "flowArn",
        "name": "name",
        "role_arn": "roleArn",
        "security_group_ids": "securityGroupIds",
        "subnet_id": "subnetId",
    },
)
class CfnFlowVpcInterfaceProps:
    def __init__(
        self,
        *,
        flow_arn: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnFlowVpcInterface``.

        :param flow_arn: The Amazon Resource Name (ARN) of the flow.
        :param name: The name for the VPC interface. This name must be unique within the flow.
        :param role_arn: The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service.
        :param security_group_ids: A virtual firewall to control inbound and outbound traffic.
        :param subnet_id: The subnet IDs that you want to use for your VPC interface. A range of IP addresses in your VPC. When you create your VPC, you specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. This is the primary CIDR block for your VPC. When you create a subnet for your VPC, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block. The subnets that you use across all VPC interfaces on the flow must be in the same Availability Zone as the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_flow_vpc_interface_props = mediaconnect.CfnFlowVpcInterfaceProps(
                flow_arn="flowArn",
                name="name",
                role_arn="roleArn",
                security_group_ids=["securityGroupIds"],
                subnet_id="subnetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4407e3345806447ad15e49eb19ee87fc76290919c1ac77d7b46df8daf4909410)
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_arn": flow_arn,
            "name": name,
            "role_arn": role_arn,
            "security_group_ids": security_group_ids,
            "subnet_id": subnet_id,
        }

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-flowarn
        '''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the VPC interface.

        This name must be unique within the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''A virtual firewall to control inbound and outbound traffic.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''The subnet IDs that you want to use for your VPC interface.

        A range of IP addresses in your VPC. When you create your VPC, you specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. This is the primary CIDR block for your VPC. When you create a subnet for your VPC, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block. The subnets that you use across all VPC interfaces on the flow must be in the same Availability Zone as the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-subnetid
        '''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowVpcInterfaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IGatewayRef_4783a0c6)
class CfnGateway(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnGateway",
):
    '''The ``AWS::MediaConnect::Gateway`` resource is used to create a new gateway.

    AWS Elemental MediaConnect Gateway is a feature of MediaConnect that allows the deployment of on-premises resources for transporting live video to and from the AWS Cloud. MediaConnect Gateway allows you to contribute live video to the AWS Cloud from on-premises hardware, as well as distribute live video from the AWS Cloud to your local data center.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html
    :cloudformationResource: AWS::MediaConnect::Gateway
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_gateway = mediaconnect.CfnGateway(self, "MyCfnGateway",
            egress_cidr_blocks=["egressCidrBlocks"],
            name="name",
            networks=[mediaconnect.CfnGateway.GatewayNetworkProperty(
                cidr_block="cidrBlock",
                name="name"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        egress_cidr_blocks: typing.Sequence[builtins.str],
        name: builtins.str,
        networks: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.GatewayNetworkProperty", typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Create a new ``AWS::MediaConnect::Gateway``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param egress_cidr_blocks: The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        :param name: The name of the gateway. This name can not be modified after the gateway is created.
        :param networks: The list of networks in the gateway.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a889ede67aac65e3ba7da8735ec09aa46c53edb047800db832cc8f049ee063d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGatewayProps(
            egress_cidr_blocks=egress_cidr_blocks, name=name, networks=networks
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForGateway")
    @builtins.classmethod
    def arn_for_gateway(cls, resource: "_IGatewayRef_4783a0c6") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__846fb03e786e5db212456f5e176807bc8fa26425b8fcdcd3acceeb914a80546a)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForGateway", [resource]))

    @jsii.member(jsii_name="isCfnGateway")
    @builtins.classmethod
    def is_cfn_gateway(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnGateway.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7afaeb3693b7233ba298147075a68f93109f71fb9d4533fc43cf919f16fe45b)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnGateway", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b19201085d642ad5919470c92f83f2874346dacf31c924443c14fa4ce8557e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__309d2649c79792783a657ac296a1e3f1559ca3d115f8d29a00fcf51ab5b9eea1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayArn")
    def attr_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the gateway.

        :cloudformationAttribute: GatewayArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayArn"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayState")
    def attr_gateway_state(self) -> builtins.str:
        '''The current state of the gateway.

        Possible values are: CREATING, ACTIVE, UPDATING, ERROR, DELETING, DELETED.

        :cloudformationAttribute: GatewayState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayState"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="gatewayRef")
    def gateway_ref(self) -> "_GatewayReference_91ca4e85":
        '''A reference to a Gateway resource.'''
        return typing.cast("_GatewayReference_91ca4e85", jsii.get(self, "gatewayRef"))

    @builtins.property
    @jsii.member(jsii_name="egressCidrBlocks")
    def egress_cidr_blocks(self) -> typing.List[builtins.str]:
        '''The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "egressCidrBlocks"))

    @egress_cidr_blocks.setter
    def egress_cidr_blocks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c756c6472ede1cbb1eb656c10e07629e0cf818e434b2e8f9c94de41e295b332e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressCidrBlocks", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f455f9a25731428a340c77bb14b2965a474f55740a64090450ee7dee16709ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networks")
    def networks(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayNetworkProperty"]]]:
        '''The list of networks in the gateway.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayNetworkProperty"]]], jsii.get(self, "networks"))

    @networks.setter
    def networks(
        self,
        value: typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayNetworkProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87886ff9eadfa80377e79911ce74141941af595ecff54249e0b94a2aa4f4fdb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networks", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnGateway.GatewayNetworkProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr_block": "cidrBlock", "name": "name"},
    )
    class GatewayNetworkProperty:
        def __init__(self, *, cidr_block: builtins.str, name: builtins.str) -> None:
            '''The network settings for a gateway.

            :param cidr_block: A unique IP address range to use for this network. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
            :param name: The name of the network. This name is used to reference the network and must be unique among networks in this gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-gateway-gatewaynetwork.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                gateway_network_property = mediaconnect.CfnGateway.GatewayNetworkProperty(
                    cidr_block="cidrBlock",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f67f020f764410bf45106fcabf15d8329d4bbbd3768cac4cd170ba1032378127)
                check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cidr_block": cidr_block,
                "name": name,
            }

        @builtins.property
        def cidr_block(self) -> builtins.str:
            '''A unique IP address range to use for this network.

            These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-gateway-gatewaynetwork.html#cfn-mediaconnect-gateway-gatewaynetwork-cidrblock
            '''
            result = self._values.get("cidr_block")
            assert result is not None, "Required property 'cidr_block' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the network.

            This name is used to reference the network and must be unique among networks in this gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-gateway-gatewaynetwork.html#cfn-mediaconnect-gateway-gatewaynetwork-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayNetworkProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "egress_cidr_blocks": "egressCidrBlocks",
        "name": "name",
        "networks": "networks",
    },
)
class CfnGatewayProps:
    def __init__(
        self,
        *,
        egress_cidr_blocks: typing.Sequence[builtins.str],
        name: builtins.str,
        networks: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnGateway.GatewayNetworkProperty", typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Properties for defining a ``CfnGateway``.

        :param egress_cidr_blocks: The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        :param name: The name of the gateway. This name can not be modified after the gateway is created.
        :param networks: The list of networks in the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_gateway_props = mediaconnect.CfnGatewayProps(
                egress_cidr_blocks=["egressCidrBlocks"],
                name="name",
                networks=[mediaconnect.CfnGateway.GatewayNetworkProperty(
                    cidr_block="cidrBlock",
                    name="name"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c57a9fbadb9701c4e8bd3f97f24fe63b6ebd3d8f830d826fedc59b0e40f450)
            check_type(argname="argument egress_cidr_blocks", value=egress_cidr_blocks, expected_type=type_hints["egress_cidr_blocks"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument networks", value=networks, expected_type=type_hints["networks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "egress_cidr_blocks": egress_cidr_blocks,
            "name": name,
            "networks": networks,
        }

    @builtins.property
    def egress_cidr_blocks(self) -> typing.List[builtins.str]:
        '''The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway.

        These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html#cfn-mediaconnect-gateway-egresscidrblocks
        '''
        result = self._values.get("egress_cidr_blocks")
        assert result is not None, "Required property 'egress_cidr_blocks' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the gateway.

        This name can not be modified after the gateway is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html#cfn-mediaconnect-gateway-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def networks(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayNetworkProperty"]]]:
        '''The list of networks in the gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html#cfn-mediaconnect-gateway-networks
        '''
        result = self._values.get("networks")
        assert result is not None, "Required property 'networks' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnGateway.GatewayNetworkProperty"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IRouterInputRef_6915df50, _ITaggableV2_4e6798f8)
class CfnRouterInput(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput",
):
    '''Represents a router input in AWS Elemental MediaConnect that is used to ingest content to be transmitted to router outputs.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html
    :cloudformationResource: AWS::MediaConnect::RouterInput
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        # automatic: Any
        # default_: Any
        
        cfn_router_input = mediaconnect.CfnRouterInput(self, "MyCfnRouterInput",
            configuration=mediaconnect.CfnRouterInput.RouterInputConfigurationProperty(
                failover=mediaconnect.CfnRouterInput.FailoverRouterInputConfigurationProperty(
                    network_interface_arn="networkInterfaceArn",
                    protocol_configurations=[mediaconnect.CfnRouterInput.FailoverRouterInputProtocolConfigurationProperty(
                        rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                            port=123,
                            recovery_latency_milliseconds=123
                        ),
                        rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                            port=123,
        
                            # the properties below are optional
                            forward_error_correction="forwardErrorCorrection"
                        ),
                        srt_caller=mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                            minimum_latency_milliseconds=123,
                            source_address="sourceAddress",
                            source_port=123,
        
                            # the properties below are optional
                            decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
                            stream_id="streamId"
                        ),
                        srt_listener=mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                            minimum_latency_milliseconds=123,
                            port=123,
        
                            # the properties below are optional
                            decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            )
                        )
                    )],
                    source_priority_mode="sourcePriorityMode",
        
                    # the properties below are optional
                    primary_source_index=123
                ),
                media_connect_flow=mediaconnect.CfnRouterInput.MediaConnectFlowRouterInputConfigurationProperty(
                    source_transit_decryption=mediaconnect.CfnRouterInput.FlowTransitEncryptionProperty(
                        encryption_key_configuration=mediaconnect.CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty(
                            automatic=automatic,
                            secrets_manager=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
        
                        # the properties below are optional
                        encryption_key_type="encryptionKeyType"
                    ),
        
                    # the properties below are optional
                    flow_arn="flowArn",
                    flow_output_arn="flowOutputArn"
                ),
                merge=mediaconnect.CfnRouterInput.MergeRouterInputConfigurationProperty(
                    merge_recovery_window_milliseconds=123,
                    network_interface_arn="networkInterfaceArn",
                    protocol_configurations=[mediaconnect.CfnRouterInput.MergeRouterInputProtocolConfigurationProperty(
                        rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                            port=123,
                            recovery_latency_milliseconds=123
                        ),
                        rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                            port=123,
        
                            # the properties below are optional
                            forward_error_correction="forwardErrorCorrection"
                        )
                    )]
                ),
                standard=mediaconnect.CfnRouterInput.StandardRouterInputConfigurationProperty(
                    network_interface_arn="networkInterfaceArn",
                    protocol_configuration=mediaconnect.CfnRouterInput.RouterInputProtocolConfigurationProperty(
                        rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                            port=123,
                            recovery_latency_milliseconds=123
                        ),
                        rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                            port=123,
        
                            # the properties below are optional
                            forward_error_correction="forwardErrorCorrection"
                        ),
                        srt_caller=mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                            minimum_latency_milliseconds=123,
                            source_address="sourceAddress",
                            source_port=123,
        
                            # the properties below are optional
                            decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
                            stream_id="streamId"
                        ),
                        srt_listener=mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                            minimum_latency_milliseconds=123,
                            port=123,
        
                            # the properties below are optional
                            decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            )
                        )
                    ),
        
                    # the properties below are optional
                    protocol="protocol"
                )
            ),
            maximum_bitrate=123,
            name="name",
            routing_scope="routingScope",
            tier="tier",
        
            # the properties below are optional
            availability_zone="availabilityZone",
            maintenance_configuration=mediaconnect.CfnRouterInput.MaintenanceConfigurationProperty(
                default=default_,
                preferred_day_time=mediaconnect.CfnRouterInput.PreferredDayTimeMaintenanceConfigurationProperty(
                    day="day",
                    time="time"
                )
            ),
            region_name="regionName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            transit_encryption=mediaconnect.CfnRouterInput.RouterInputTransitEncryptionProperty(
                encryption_key_configuration=mediaconnect.CfnRouterInput.RouterInputTransitEncryptionKeyConfigurationProperty(
                    automatic=automatic,
                    secrets_manager=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                ),
        
                # the properties below are optional
                encryption_key_type="encryptionKeyType"
            )
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        maximum_bitrate: jsii.Number,
        name: builtins.str,
        routing_scope: builtins.str,
        tier: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        maintenance_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.MaintenanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        region_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        transit_encryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RouterInputTransitEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::RouterInput``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: The configuration settings for a router input.
        :param maximum_bitrate: The maximum bitrate for the router input.
        :param name: The name of the router input.
        :param routing_scope: Indicates whether the router input is configured for Regional or global routing.
        :param tier: The tier level of the router input.
        :param availability_zone: The Availability Zone of the router input.
        :param maintenance_configuration: The maintenance configuration settings applied to this router input.
        :param region_name: The AWS Region where the router input is located.
        :param tags: Key-value pairs that can be used to tag and organize this router input.
        :param transit_encryption: Encryption information.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fa24b13aaffdcfc1e47f3ced2e884afe1fe974cb91ceb3f0702e3ed196e0855)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRouterInputProps(
            configuration=configuration,
            maximum_bitrate=maximum_bitrate,
            name=name,
            routing_scope=routing_scope,
            tier=tier,
            availability_zone=availability_zone,
            maintenance_configuration=maintenance_configuration,
            region_name=region_name,
            tags=tags,
            transit_encryption=transit_encryption,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForRouterInput")
    @builtins.classmethod
    def arn_for_router_input(
        cls,
        resource: "_IRouterInputRef_6915df50",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b62b590ea740d308b838213af0b2cd196493374e80cd7c3686bd872b19cfdfeb)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForRouterInput", [resource]))

    @jsii.member(jsii_name="isCfnRouterInput")
    @builtins.classmethod
    def is_cfn_router_input(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnRouterInput.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bc6c871ed8b6d73be81a2ae1d1e2c9d9b137109612e38abd34e5848294dbc27)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnRouterInput", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c944fb547e87f295306d8735bbf0eeac4ac8a0b6018a5739d3a31d2e1e718ef6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8e30a6d884b369ff6382f442459ba4c11662a15636af2d199fbc1aa1a790ea21)
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
        '''The Amazon Resource Name (ARN) of the router input.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the router input was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier of the router input.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrInputType")
    def attr_input_type(self) -> builtins.str:
        '''The type of the router input.

        :cloudformationAttribute: InputType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInputType"))

    @builtins.property
    @jsii.member(jsii_name="attrIpAddress")
    def attr_ip_address(self) -> builtins.str:
        '''The IP address of the router input.

        :cloudformationAttribute: IpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrMaintenanceType")
    def attr_maintenance_type(self) -> builtins.str:
        '''The type of maintenance configuration applied to this router input.

        :cloudformationAttribute: MaintenanceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMaintenanceType"))

    @builtins.property
    @jsii.member(jsii_name="attrRoutedOutputs")
    def attr_routed_outputs(self) -> jsii.Number:
        '''The number of router outputs associated with the router input.

        :cloudformationAttribute: RoutedOutputs
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrRoutedOutputs"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The current state of the router input.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the router input was last updated.

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
    @jsii.member(jsii_name="routerInputRef")
    def router_input_ref(self) -> "_RouterInputReference_b71c2141":
        '''A reference to a RouterInput resource.'''
        return typing.cast("_RouterInputReference_b71c2141", jsii.get(self, "routerInputRef"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputConfigurationProperty"]:
        '''The configuration settings for a router input.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc19a3af1b324b171b747b68112c85cb261bd6957bab7764b849ca52d9245142)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maximumBitrate")
    def maximum_bitrate(self) -> jsii.Number:
        '''The maximum bitrate for the router input.'''
        return typing.cast(jsii.Number, jsii.get(self, "maximumBitrate"))

    @maximum_bitrate.setter
    def maximum_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9b9c8e82a356b3f89719f6bbfe30b90040f8129a03f8ce150ad2a8b87ed8246)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBitrate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the router input.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cad73940b17fe84f1f0b506b19a2f76e3972f6d1b1a71c747442330ba7cdd4b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="routingScope")
    def routing_scope(self) -> builtins.str:
        '''Indicates whether the router input is configured for Regional or global routing.'''
        return typing.cast(builtins.str, jsii.get(self, "routingScope"))

    @routing_scope.setter
    def routing_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00684f4fd383ed48bfa0345b412a77ecbdd623ac32a218fb0294e30e4ed401bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingScope", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        '''The tier level of the router input.'''
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84d00c9475e25cd260ddceb328a82f02a2cb361571f2a5fd671818fb15dd8cd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone of the router input.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3dc1a9f3d38364d1ad15584e3cfaccae3ba843735b9a10bd75fa94a9736e60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maintenanceConfiguration")
    def maintenance_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MaintenanceConfigurationProperty"]]:
        '''The maintenance configuration settings applied to this router input.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MaintenanceConfigurationProperty"]], jsii.get(self, "maintenanceConfiguration"))

    @maintenance_configuration.setter
    def maintenance_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MaintenanceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c1170f7ba129480fda3e3b9954bf9b3bab26579ad56ca54217519dd369f2de8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="regionName")
    def region_name(self) -> typing.Optional[builtins.str]:
        '''The AWS Region where the router input is located.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionName"))

    @region_name.setter
    def region_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74fded60926c739a4b66f4bd6fdd901f417bee400d49f669f01a8545de0e3052)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Key-value pairs that can be used to tag and organize this router input.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a824b54cbbdf5489ae89810bc583b0c20d4cfb25aeb8745e7f408d889b008ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="transitEncryption")
    def transit_encryption(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputTransitEncryptionProperty"]]:
        '''Encryption information.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputTransitEncryptionProperty"]], jsii.get(self, "transitEncryption"))

    @transit_encryption.setter
    def transit_encryption(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputTransitEncryptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b52cf5469dfc840d14b0db5fb2454e8064b964427f444c618452b6c06465337)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transitEncryption", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.FailoverRouterInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_interface_arn": "networkInterfaceArn",
            "protocol_configurations": "protocolConfigurations",
            "source_priority_mode": "sourcePriorityMode",
            "primary_source_index": "primarySourceIndex",
        },
    )
    class FailoverRouterInputConfigurationProperty:
        def __init__(
            self,
            *,
            network_interface_arn: builtins.str,
            protocol_configurations: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.FailoverRouterInputProtocolConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
            source_priority_mode: builtins.str,
            primary_source_index: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Configuration settings for a failover router input that allows switching between two input sources.

            :param network_interface_arn: The ARN of the network interface to use for this failover router input.
            :param protocol_configurations: A list of exactly two protocol configurations for the failover input sources. Both must use the same protocol type.
            :param source_priority_mode: 
            :param primary_source_index: The index (0 or 1) that specifies which source in the protocol configurations list is currently active. Used to control which of the two failover sources is currently selected. This field is ignored when sourcePriorityMode is set to NO_PRIORITY

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                failover_router_input_configuration_property = mediaconnect.CfnRouterInput.FailoverRouterInputConfigurationProperty(
                    network_interface_arn="networkInterfaceArn",
                    protocol_configurations=[mediaconnect.CfnRouterInput.FailoverRouterInputProtocolConfigurationProperty(
                        rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                            port=123,
                            recovery_latency_milliseconds=123
                        ),
                        rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                            port=123,
                
                            # the properties below are optional
                            forward_error_correction="forwardErrorCorrection"
                        ),
                        srt_caller=mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                            minimum_latency_milliseconds=123,
                            source_address="sourceAddress",
                            source_port=123,
                
                            # the properties below are optional
                            decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
                            stream_id="streamId"
                        ),
                        srt_listener=mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                            minimum_latency_milliseconds=123,
                            port=123,
                
                            # the properties below are optional
                            decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            )
                        )
                    )],
                    source_priority_mode="sourcePriorityMode",
                
                    # the properties below are optional
                    primary_source_index=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b915443cb98891bf89e968e2338dbbd48e7fc3e6389d7cf5425707945361655)
                check_type(argname="argument network_interface_arn", value=network_interface_arn, expected_type=type_hints["network_interface_arn"])
                check_type(argname="argument protocol_configurations", value=protocol_configurations, expected_type=type_hints["protocol_configurations"])
                check_type(argname="argument source_priority_mode", value=source_priority_mode, expected_type=type_hints["source_priority_mode"])
                check_type(argname="argument primary_source_index", value=primary_source_index, expected_type=type_hints["primary_source_index"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_interface_arn": network_interface_arn,
                "protocol_configurations": protocol_configurations,
                "source_priority_mode": source_priority_mode,
            }
            if primary_source_index is not None:
                self._values["primary_source_index"] = primary_source_index

        @builtins.property
        def network_interface_arn(self) -> builtins.str:
            '''The ARN of the network interface to use for this failover router input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration.html#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-networkinterfacearn
            '''
            result = self._values.get("network_interface_arn")
            assert result is not None, "Required property 'network_interface_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol_configurations(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.FailoverRouterInputProtocolConfigurationProperty"]]]:
            '''A list of exactly two protocol configurations for the failover input sources.

            Both must use the same protocol type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration.html#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-protocolconfigurations
            '''
            result = self._values.get("protocol_configurations")
            assert result is not None, "Required property 'protocol_configurations' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.FailoverRouterInputProtocolConfigurationProperty"]]], result)

        @builtins.property
        def source_priority_mode(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration.html#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-sourceprioritymode
            '''
            result = self._values.get("source_priority_mode")
            assert result is not None, "Required property 'source_priority_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def primary_source_index(self) -> typing.Optional[jsii.Number]:
            '''The index (0 or 1) that specifies which source in the protocol configurations list is currently active.

            Used to control which of the two failover sources is currently selected. This field is ignored when sourcePriorityMode is set to NO_PRIORITY

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-failoverrouterinputconfiguration.html#cfn-mediaconnect-routerinput-failoverrouterinputconfiguration-primarysourceindex
            '''
            result = self._values.get("primary_source_index")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailoverRouterInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.FailoverRouterInputProtocolConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rist": "rist",
            "rtp": "rtp",
            "srt_caller": "srtCaller",
            "srt_listener": "srtListener",
        },
    )
    class FailoverRouterInputProtocolConfigurationProperty:
        def __init__(
            self,
            *,
            rist: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RistRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rtp: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RtpRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            srt_caller: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.SrtCallerRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            srt_listener: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.SrtListenerRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param rist: The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.
            :param rtp: The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.
            :param srt_caller: The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in caller mode, including the source address and port, minimum latency, stream ID, and decryption key configuration.
            :param srt_listener: The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and decryption key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-failoverrouterinputprotocolconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                failover_router_input_protocol_configuration_property = mediaconnect.CfnRouterInput.FailoverRouterInputProtocolConfigurationProperty(
                    rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                        port=123,
                        recovery_latency_milliseconds=123
                    ),
                    rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                        port=123,
                
                        # the properties below are optional
                        forward_error_correction="forwardErrorCorrection"
                    ),
                    srt_caller=mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                        minimum_latency_milliseconds=123,
                        source_address="sourceAddress",
                        source_port=123,
                
                        # the properties below are optional
                        decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                            encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
                        stream_id="streamId"
                    ),
                    srt_listener=mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                        minimum_latency_milliseconds=123,
                        port=123,
                
                        # the properties below are optional
                        decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                            encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d8f038e6a58a77278305824f4d096d5103bdf9497e022340099fbe631d35cdea)
                check_type(argname="argument rist", value=rist, expected_type=type_hints["rist"])
                check_type(argname="argument rtp", value=rtp, expected_type=type_hints["rtp"])
                check_type(argname="argument srt_caller", value=srt_caller, expected_type=type_hints["srt_caller"])
                check_type(argname="argument srt_listener", value=srt_listener, expected_type=type_hints["srt_listener"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if rist is not None:
                self._values["rist"] = rist
            if rtp is not None:
                self._values["rtp"] = rtp
            if srt_caller is not None:
                self._values["srt_caller"] = srt_caller
            if srt_listener is not None:
                self._values["srt_listener"] = srt_listener

        @builtins.property
        def rist(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RistRouterInputConfigurationProperty"]]:
            '''The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-failoverrouterinputprotocolconfiguration.html#cfn-mediaconnect-routerinput-failoverrouterinputprotocolconfiguration-rist
            '''
            result = self._values.get("rist")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RistRouterInputConfigurationProperty"]], result)

        @builtins.property
        def rtp(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RtpRouterInputConfigurationProperty"]]:
            '''The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-failoverrouterinputprotocolconfiguration.html#cfn-mediaconnect-routerinput-failoverrouterinputprotocolconfiguration-rtp
            '''
            result = self._values.get("rtp")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RtpRouterInputConfigurationProperty"]], result)

        @builtins.property
        def srt_caller(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtCallerRouterInputConfigurationProperty"]]:
            '''The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in caller mode, including the source address and port, minimum latency, stream ID, and decryption key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-failoverrouterinputprotocolconfiguration.html#cfn-mediaconnect-routerinput-failoverrouterinputprotocolconfiguration-srtcaller
            '''
            result = self._values.get("srt_caller")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtCallerRouterInputConfigurationProperty"]], result)

        @builtins.property
        def srt_listener(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtListenerRouterInputConfigurationProperty"]]:
            '''The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and decryption key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-failoverrouterinputprotocolconfiguration.html#cfn-mediaconnect-routerinput-failoverrouterinputprotocolconfiguration-srtlistener
            '''
            result = self._values.get("srt_listener")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtListenerRouterInputConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailoverRouterInputProtocolConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"automatic": "automatic", "secrets_manager": "secretsManager"},
    )
    class FlowTransitEncryptionKeyConfigurationProperty:
        def __init__(
            self,
            *,
            automatic: typing.Any = None,
            secrets_manager: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param automatic: Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.
            :param secrets_manager: The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-flowtransitencryptionkeyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                flow_transit_encryption_key_configuration_property = mediaconnect.CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty(
                    automatic=automatic,
                    secrets_manager=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f46fb21f29424f9cdada7e8baeb37950068c69dd5988f39da2d4d57ad111304)
                check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
                check_type(argname="argument secrets_manager", value=secrets_manager, expected_type=type_hints["secrets_manager"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if automatic is not None:
                self._values["automatic"] = automatic
            if secrets_manager is not None:
                self._values["secrets_manager"] = secrets_manager

        @builtins.property
        def automatic(self) -> typing.Any:
            '''Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-flowtransitencryptionkeyconfiguration.html#cfn-mediaconnect-routerinput-flowtransitencryptionkeyconfiguration-automatic
            '''
            result = self._values.get("automatic")
            return typing.cast(typing.Any, result)

        @builtins.property
        def secrets_manager(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty"]]:
            '''The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-flowtransitencryptionkeyconfiguration.html#cfn-mediaconnect-routerinput-flowtransitencryptionkeyconfiguration-secretsmanager
            '''
            result = self._values.get("secrets_manager")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowTransitEncryptionKeyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.FlowTransitEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_key_configuration": "encryptionKeyConfiguration",
            "encryption_key_type": "encryptionKeyType",
        },
    )
    class FlowTransitEncryptionProperty:
        def __init__(
            self,
            *,
            encryption_key_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            encryption_key_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.

            :param encryption_key_configuration: Configuration settings for flow transit encryption keys.
            :param encryption_key_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-flowtransitencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                flow_transit_encryption_property = mediaconnect.CfnRouterInput.FlowTransitEncryptionProperty(
                    encryption_key_configuration=mediaconnect.CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty(
                        automatic=automatic,
                        secrets_manager=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
                
                    # the properties below are optional
                    encryption_key_type="encryptionKeyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ee7cb3dd62027be3aaef58d8e915eab27767b66fa11f87aff2f38eb8e4f62449)
                check_type(argname="argument encryption_key_configuration", value=encryption_key_configuration, expected_type=type_hints["encryption_key_configuration"])
                check_type(argname="argument encryption_key_type", value=encryption_key_type, expected_type=type_hints["encryption_key_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_key_configuration": encryption_key_configuration,
            }
            if encryption_key_type is not None:
                self._values["encryption_key_type"] = encryption_key_type

        @builtins.property
        def encryption_key_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty"]:
            '''Configuration settings for flow transit encryption keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-flowtransitencryption.html#cfn-mediaconnect-routerinput-flowtransitencryption-encryptionkeyconfiguration
            '''
            result = self._values.get("encryption_key_configuration")
            assert result is not None, "Required property 'encryption_key_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty"], result)

        @builtins.property
        def encryption_key_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-flowtransitencryption.html#cfn-mediaconnect-routerinput-flowtransitencryption-encryptionkeytype
            '''
            result = self._values.get("encryption_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowTransitEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.MaintenanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"default": "default", "preferred_day_time": "preferredDayTime"},
    )
    class MaintenanceConfigurationProperty:
        def __init__(
            self,
            *,
            default: typing.Any = None,
            preferred_day_time: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.PreferredDayTimeMaintenanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param default: Configuration settings for default maintenance scheduling.
            :param preferred_day_time: Configuration for preferred day and time maintenance settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-maintenanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # default_: Any
                
                maintenance_configuration_property = mediaconnect.CfnRouterInput.MaintenanceConfigurationProperty(
                    default=default_,
                    preferred_day_time=mediaconnect.CfnRouterInput.PreferredDayTimeMaintenanceConfigurationProperty(
                        day="day",
                        time="time"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a02453ffb5787750cf8b7c68ece86b453aeac195bd6b7a67d442069cdfaf86c1)
                check_type(argname="argument default", value=default, expected_type=type_hints["default"])
                check_type(argname="argument preferred_day_time", value=preferred_day_time, expected_type=type_hints["preferred_day_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if default is not None:
                self._values["default"] = default
            if preferred_day_time is not None:
                self._values["preferred_day_time"] = preferred_day_time

        @builtins.property
        def default(self) -> typing.Any:
            '''Configuration settings for default maintenance scheduling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-maintenanceconfiguration.html#cfn-mediaconnect-routerinput-maintenanceconfiguration-default
            '''
            result = self._values.get("default")
            return typing.cast(typing.Any, result)

        @builtins.property
        def preferred_day_time(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.PreferredDayTimeMaintenanceConfigurationProperty"]]:
            '''Configuration for preferred day and time maintenance settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-maintenanceconfiguration.html#cfn-mediaconnect-routerinput-maintenanceconfiguration-preferreddaytime
            '''
            result = self._values.get("preferred_day_time")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.PreferredDayTimeMaintenanceConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.MediaConnectFlowRouterInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_transit_decryption": "sourceTransitDecryption",
            "flow_arn": "flowArn",
            "flow_output_arn": "flowOutputArn",
        },
    )
    class MediaConnectFlowRouterInputConfigurationProperty:
        def __init__(
            self,
            *,
            source_transit_decryption: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.FlowTransitEncryptionProperty", typing.Dict[builtins.str, typing.Any]]],
            flow_arn: typing.Optional[builtins.str] = None,
            flow_output_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration settings for connecting a router input to a flow output.

            :param source_transit_decryption: The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.
            :param flow_arn: The ARN of the flow to connect to.
            :param flow_output_arn: The ARN of the flow output to connect to this router input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                media_connect_flow_router_input_configuration_property = mediaconnect.CfnRouterInput.MediaConnectFlowRouterInputConfigurationProperty(
                    source_transit_decryption=mediaconnect.CfnRouterInput.FlowTransitEncryptionProperty(
                        encryption_key_configuration=mediaconnect.CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty(
                            automatic=automatic,
                            secrets_manager=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
                
                        # the properties below are optional
                        encryption_key_type="encryptionKeyType"
                    ),
                
                    # the properties below are optional
                    flow_arn="flowArn",
                    flow_output_arn="flowOutputArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__07cd74860f626ccccd2d7b9722c16c895a7f51382af41cc9a3aa3da275bb3b5f)
                check_type(argname="argument source_transit_decryption", value=source_transit_decryption, expected_type=type_hints["source_transit_decryption"])
                check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
                check_type(argname="argument flow_output_arn", value=flow_output_arn, expected_type=type_hints["flow_output_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_transit_decryption": source_transit_decryption,
            }
            if flow_arn is not None:
                self._values["flow_arn"] = flow_arn
            if flow_output_arn is not None:
                self._values["flow_output_arn"] = flow_output_arn

        @builtins.property
        def source_transit_decryption(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterInput.FlowTransitEncryptionProperty"]:
            '''The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration.html#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-sourcetransitdecryption
            '''
            result = self._values.get("source_transit_decryption")
            assert result is not None, "Required property 'source_transit_decryption' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterInput.FlowTransitEncryptionProperty"], result)

        @builtins.property
        def flow_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the flow to connect to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration.html#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-flowarn
            '''
            result = self._values.get("flow_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def flow_output_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the flow output to connect to this router input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration.html#cfn-mediaconnect-routerinput-mediaconnectflowrouterinputconfiguration-flowoutputarn
            '''
            result = self._values.get("flow_output_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaConnectFlowRouterInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.MergeRouterInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "merge_recovery_window_milliseconds": "mergeRecoveryWindowMilliseconds",
            "network_interface_arn": "networkInterfaceArn",
            "protocol_configurations": "protocolConfigurations",
        },
    )
    class MergeRouterInputConfigurationProperty:
        def __init__(
            self,
            *,
            merge_recovery_window_milliseconds: jsii.Number,
            network_interface_arn: builtins.str,
            protocol_configurations: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.MergeRouterInputProtocolConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Configuration settings for a merge router input that combines two input sources.

            :param merge_recovery_window_milliseconds: The time window in milliseconds for merging the two input sources.
            :param network_interface_arn: The ARN of the network interface to use for this merge router input.
            :param protocol_configurations: A list of exactly two protocol configurations for the merge input sources. Both must use the same protocol type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                merge_router_input_configuration_property = mediaconnect.CfnRouterInput.MergeRouterInputConfigurationProperty(
                    merge_recovery_window_milliseconds=123,
                    network_interface_arn="networkInterfaceArn",
                    protocol_configurations=[mediaconnect.CfnRouterInput.MergeRouterInputProtocolConfigurationProperty(
                        rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                            port=123,
                            recovery_latency_milliseconds=123
                        ),
                        rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                            port=123,
                
                            # the properties below are optional
                            forward_error_correction="forwardErrorCorrection"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c207577b6eab68f0d1c3f7593cc0b00c18a7e10d165eed0314d6bcb41a434578)
                check_type(argname="argument merge_recovery_window_milliseconds", value=merge_recovery_window_milliseconds, expected_type=type_hints["merge_recovery_window_milliseconds"])
                check_type(argname="argument network_interface_arn", value=network_interface_arn, expected_type=type_hints["network_interface_arn"])
                check_type(argname="argument protocol_configurations", value=protocol_configurations, expected_type=type_hints["protocol_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "merge_recovery_window_milliseconds": merge_recovery_window_milliseconds,
                "network_interface_arn": network_interface_arn,
                "protocol_configurations": protocol_configurations,
            }

        @builtins.property
        def merge_recovery_window_milliseconds(self) -> jsii.Number:
            '''The time window in milliseconds for merging the two input sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration.html#cfn-mediaconnect-routerinput-mergerouterinputconfiguration-mergerecoverywindowmilliseconds
            '''
            result = self._values.get("merge_recovery_window_milliseconds")
            assert result is not None, "Required property 'merge_recovery_window_milliseconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def network_interface_arn(self) -> builtins.str:
            '''The ARN of the network interface to use for this merge router input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration.html#cfn-mediaconnect-routerinput-mergerouterinputconfiguration-networkinterfacearn
            '''
            result = self._values.get("network_interface_arn")
            assert result is not None, "Required property 'network_interface_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol_configurations(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MergeRouterInputProtocolConfigurationProperty"]]]:
            '''A list of exactly two protocol configurations for the merge input sources.

            Both must use the same protocol type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mergerouterinputconfiguration.html#cfn-mediaconnect-routerinput-mergerouterinputconfiguration-protocolconfigurations
            '''
            result = self._values.get("protocol_configurations")
            assert result is not None, "Required property 'protocol_configurations' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MergeRouterInputProtocolConfigurationProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MergeRouterInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.MergeRouterInputProtocolConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"rist": "rist", "rtp": "rtp"},
    )
    class MergeRouterInputProtocolConfigurationProperty:
        def __init__(
            self,
            *,
            rist: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RistRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rtp: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RtpRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param rist: The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.
            :param rtp: The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mergerouterinputprotocolconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                merge_router_input_protocol_configuration_property = mediaconnect.CfnRouterInput.MergeRouterInputProtocolConfigurationProperty(
                    rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                        port=123,
                        recovery_latency_milliseconds=123
                    ),
                    rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                        port=123,
                
                        # the properties below are optional
                        forward_error_correction="forwardErrorCorrection"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d4bff0ea4788435a62555083659b5a3393ff9c2dc3b37396f56d5473c1b65763)
                check_type(argname="argument rist", value=rist, expected_type=type_hints["rist"])
                check_type(argname="argument rtp", value=rtp, expected_type=type_hints["rtp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if rist is not None:
                self._values["rist"] = rist
            if rtp is not None:
                self._values["rtp"] = rtp

        @builtins.property
        def rist(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RistRouterInputConfigurationProperty"]]:
            '''The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mergerouterinputprotocolconfiguration.html#cfn-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-rist
            '''
            result = self._values.get("rist")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RistRouterInputConfigurationProperty"]], result)

        @builtins.property
        def rtp(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RtpRouterInputConfigurationProperty"]]:
            '''The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-mergerouterinputprotocolconfiguration.html#cfn-mediaconnect-routerinput-mergerouterinputprotocolconfiguration-rtp
            '''
            result = self._values.get("rtp")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RtpRouterInputConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MergeRouterInputProtocolConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.PreferredDayTimeMaintenanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"day": "day", "time": "time"},
    )
    class PreferredDayTimeMaintenanceConfigurationProperty:
        def __init__(self, *, day: builtins.str, time: builtins.str) -> None:
            '''Configuration for preferred day and time maintenance settings.

            :param day: 
            :param time: The preferred time for maintenance operations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                preferred_day_time_maintenance_configuration_property = mediaconnect.CfnRouterInput.PreferredDayTimeMaintenanceConfigurationProperty(
                    day="day",
                    time="time"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc21d5c65ee1f7e8a6d879dc6bdeea6e77c637daf5b2e9885e67ec9a9279f8d5)
                check_type(argname="argument day", value=day, expected_type=type_hints["day"])
                check_type(argname="argument time", value=time, expected_type=type_hints["time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "day": day,
                "time": time,
            }

        @builtins.property
        def day(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration.html#cfn-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-day
            '''
            result = self._values.get("day")
            assert result is not None, "Required property 'day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time(self) -> builtins.str:
            '''The preferred time for maintenance operations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration.html#cfn-mediaconnect-routerinput-preferreddaytimemaintenanceconfiguration-time
            '''
            result = self._values.get("time")
            assert result is not None, "Required property 'time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PreferredDayTimeMaintenanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "port": "port",
            "recovery_latency_milliseconds": "recoveryLatencyMilliseconds",
        },
    )
    class RistRouterInputConfigurationProperty:
        def __init__(
            self,
            *,
            port: jsii.Number,
            recovery_latency_milliseconds: jsii.Number,
        ) -> None:
            '''The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.

            :param port: The port number used for the RIST protocol in the router input configuration.
            :param recovery_latency_milliseconds: The recovery latency in milliseconds for the RIST protocol in the router input configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                rist_router_input_configuration_property = mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                    port=123,
                    recovery_latency_milliseconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__53b65288b7279c56646f36579c820e91edb724a5c19852f9a2b528f0d5893abd)
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument recovery_latency_milliseconds", value=recovery_latency_milliseconds, expected_type=type_hints["recovery_latency_milliseconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "port": port,
                "recovery_latency_milliseconds": recovery_latency_milliseconds,
            }

        @builtins.property
        def port(self) -> jsii.Number:
            '''The port number used for the RIST protocol in the router input configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration.html#cfn-mediaconnect-routerinput-ristrouterinputconfiguration-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def recovery_latency_milliseconds(self) -> jsii.Number:
            '''The recovery latency in milliseconds for the RIST protocol in the router input configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-ristrouterinputconfiguration.html#cfn-mediaconnect-routerinput-ristrouterinputconfiguration-recoverylatencymilliseconds
            '''
            result = self._values.get("recovery_latency_milliseconds")
            assert result is not None, "Required property 'recovery_latency_milliseconds' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RistRouterInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.RouterInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failover": "failover",
            "media_connect_flow": "mediaConnectFlow",
            "merge": "merge",
            "standard": "standard",
        },
    )
    class RouterInputConfigurationProperty:
        def __init__(
            self,
            *,
            failover: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.FailoverRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            media_connect_flow: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.MediaConnectFlowRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            merge: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.MergeRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            standard: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.StandardRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param failover: Configuration settings for a failover router input that allows switching between two input sources.
            :param media_connect_flow: Configuration settings for connecting a router input to a flow output.
            :param merge: Configuration settings for a merge router input that combines two input sources.
            :param standard: The configuration settings for a standard router input, including the protocol, protocol-specific configuration, network interface, and availability zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                router_input_configuration_property = mediaconnect.CfnRouterInput.RouterInputConfigurationProperty(
                    failover=mediaconnect.CfnRouterInput.FailoverRouterInputConfigurationProperty(
                        network_interface_arn="networkInterfaceArn",
                        protocol_configurations=[mediaconnect.CfnRouterInput.FailoverRouterInputProtocolConfigurationProperty(
                            rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                                port=123,
                                recovery_latency_milliseconds=123
                            ),
                            rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                                port=123,
                
                                # the properties below are optional
                                forward_error_correction="forwardErrorCorrection"
                            ),
                            srt_caller=mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                                minimum_latency_milliseconds=123,
                                source_address="sourceAddress",
                                source_port=123,
                
                                # the properties below are optional
                                decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                ),
                                stream_id="streamId"
                            ),
                            srt_listener=mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                                minimum_latency_milliseconds=123,
                                port=123,
                
                                # the properties below are optional
                                decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                )
                            )
                        )],
                        source_priority_mode="sourcePriorityMode",
                
                        # the properties below are optional
                        primary_source_index=123
                    ),
                    media_connect_flow=mediaconnect.CfnRouterInput.MediaConnectFlowRouterInputConfigurationProperty(
                        source_transit_decryption=mediaconnect.CfnRouterInput.FlowTransitEncryptionProperty(
                            encryption_key_configuration=mediaconnect.CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty(
                                automatic=automatic,
                                secrets_manager=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
                
                            # the properties below are optional
                            encryption_key_type="encryptionKeyType"
                        ),
                
                        # the properties below are optional
                        flow_arn="flowArn",
                        flow_output_arn="flowOutputArn"
                    ),
                    merge=mediaconnect.CfnRouterInput.MergeRouterInputConfigurationProperty(
                        merge_recovery_window_milliseconds=123,
                        network_interface_arn="networkInterfaceArn",
                        protocol_configurations=[mediaconnect.CfnRouterInput.MergeRouterInputProtocolConfigurationProperty(
                            rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                                port=123,
                                recovery_latency_milliseconds=123
                            ),
                            rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                                port=123,
                
                                # the properties below are optional
                                forward_error_correction="forwardErrorCorrection"
                            )
                        )]
                    ),
                    standard=mediaconnect.CfnRouterInput.StandardRouterInputConfigurationProperty(
                        network_interface_arn="networkInterfaceArn",
                        protocol_configuration=mediaconnect.CfnRouterInput.RouterInputProtocolConfigurationProperty(
                            rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                                port=123,
                                recovery_latency_milliseconds=123
                            ),
                            rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                                port=123,
                
                                # the properties below are optional
                                forward_error_correction="forwardErrorCorrection"
                            ),
                            srt_caller=mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                                minimum_latency_milliseconds=123,
                                source_address="sourceAddress",
                                source_port=123,
                
                                # the properties below are optional
                                decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                ),
                                stream_id="streamId"
                            ),
                            srt_listener=mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                                minimum_latency_milliseconds=123,
                                port=123,
                
                                # the properties below are optional
                                decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                )
                            )
                        ),
                
                        # the properties below are optional
                        protocol="protocol"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__367935140f8b2e56d02ff3e2c05252a68073eace6c0eeda3b7abeeeac1209e1b)
                check_type(argname="argument failover", value=failover, expected_type=type_hints["failover"])
                check_type(argname="argument media_connect_flow", value=media_connect_flow, expected_type=type_hints["media_connect_flow"])
                check_type(argname="argument merge", value=merge, expected_type=type_hints["merge"])
                check_type(argname="argument standard", value=standard, expected_type=type_hints["standard"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if failover is not None:
                self._values["failover"] = failover
            if media_connect_flow is not None:
                self._values["media_connect_flow"] = media_connect_flow
            if merge is not None:
                self._values["merge"] = merge
            if standard is not None:
                self._values["standard"] = standard

        @builtins.property
        def failover(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.FailoverRouterInputConfigurationProperty"]]:
            '''Configuration settings for a failover router input that allows switching between two input sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputconfiguration.html#cfn-mediaconnect-routerinput-routerinputconfiguration-failover
            '''
            result = self._values.get("failover")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.FailoverRouterInputConfigurationProperty"]], result)

        @builtins.property
        def media_connect_flow(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MediaConnectFlowRouterInputConfigurationProperty"]]:
            '''Configuration settings for connecting a router input to a flow output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputconfiguration.html#cfn-mediaconnect-routerinput-routerinputconfiguration-mediaconnectflow
            '''
            result = self._values.get("media_connect_flow")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MediaConnectFlowRouterInputConfigurationProperty"]], result)

        @builtins.property
        def merge(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MergeRouterInputConfigurationProperty"]]:
            '''Configuration settings for a merge router input that combines two input sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputconfiguration.html#cfn-mediaconnect-routerinput-routerinputconfiguration-merge
            '''
            result = self._values.get("merge")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MergeRouterInputConfigurationProperty"]], result)

        @builtins.property
        def standard(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.StandardRouterInputConfigurationProperty"]]:
            '''The configuration settings for a standard router input, including the protocol, protocol-specific configuration, network interface, and availability zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputconfiguration.html#cfn-mediaconnect-routerinput-routerinputconfiguration-standard
            '''
            result = self._values.get("standard")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.StandardRouterInputConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouterInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.RouterInputProtocolConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rist": "rist",
            "rtp": "rtp",
            "srt_caller": "srtCaller",
            "srt_listener": "srtListener",
        },
    )
    class RouterInputProtocolConfigurationProperty:
        def __init__(
            self,
            *,
            rist: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RistRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rtp: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RtpRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            srt_caller: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.SrtCallerRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            srt_listener: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.SrtListenerRouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param rist: The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.
            :param rtp: The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.
            :param srt_caller: The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in caller mode, including the source address and port, minimum latency, stream ID, and decryption key configuration.
            :param srt_listener: The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and decryption key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                router_input_protocol_configuration_property = mediaconnect.CfnRouterInput.RouterInputProtocolConfigurationProperty(
                    rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                        port=123,
                        recovery_latency_milliseconds=123
                    ),
                    rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                        port=123,
                
                        # the properties below are optional
                        forward_error_correction="forwardErrorCorrection"
                    ),
                    srt_caller=mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                        minimum_latency_milliseconds=123,
                        source_address="sourceAddress",
                        source_port=123,
                
                        # the properties below are optional
                        decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                            encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
                        stream_id="streamId"
                    ),
                    srt_listener=mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                        minimum_latency_milliseconds=123,
                        port=123,
                
                        # the properties below are optional
                        decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                            encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6bee2f8b18c83277f36b402b57e84bb58ee2a5352632583caaeb637773d1069c)
                check_type(argname="argument rist", value=rist, expected_type=type_hints["rist"])
                check_type(argname="argument rtp", value=rtp, expected_type=type_hints["rtp"])
                check_type(argname="argument srt_caller", value=srt_caller, expected_type=type_hints["srt_caller"])
                check_type(argname="argument srt_listener", value=srt_listener, expected_type=type_hints["srt_listener"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if rist is not None:
                self._values["rist"] = rist
            if rtp is not None:
                self._values["rtp"] = rtp
            if srt_caller is not None:
                self._values["srt_caller"] = srt_caller
            if srt_listener is not None:
                self._values["srt_listener"] = srt_listener

        @builtins.property
        def rist(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RistRouterInputConfigurationProperty"]]:
            '''The configuration settings for a router input using the RIST (Reliable Internet Stream Transport) protocol, including the port and recovery latency.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration.html#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-rist
            '''
            result = self._values.get("rist")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RistRouterInputConfigurationProperty"]], result)

        @builtins.property
        def rtp(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RtpRouterInputConfigurationProperty"]]:
            '''The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration.html#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-rtp
            '''
            result = self._values.get("rtp")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RtpRouterInputConfigurationProperty"]], result)

        @builtins.property
        def srt_caller(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtCallerRouterInputConfigurationProperty"]]:
            '''The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in caller mode, including the source address and port, minimum latency, stream ID, and decryption key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration.html#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-srtcaller
            '''
            result = self._values.get("srt_caller")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtCallerRouterInputConfigurationProperty"]], result)

        @builtins.property
        def srt_listener(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtListenerRouterInputConfigurationProperty"]]:
            '''The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and decryption key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputprotocolconfiguration.html#cfn-mediaconnect-routerinput-routerinputprotocolconfiguration-srtlistener
            '''
            result = self._values.get("srt_listener")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtListenerRouterInputConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouterInputProtocolConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.RouterInputTransitEncryptionKeyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"automatic": "automatic", "secrets_manager": "secretsManager"},
    )
    class RouterInputTransitEncryptionKeyConfigurationProperty:
        def __init__(
            self,
            *,
            automatic: typing.Any = None,
            secrets_manager: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param automatic: Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.
            :param secrets_manager: The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputtransitencryptionkeyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                router_input_transit_encryption_key_configuration_property = mediaconnect.CfnRouterInput.RouterInputTransitEncryptionKeyConfigurationProperty(
                    automatic=automatic,
                    secrets_manager=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fcc66546aaf31b61e1efa68ba13e70820ab56b959d9cce333b0e5b3482a1bc09)
                check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
                check_type(argname="argument secrets_manager", value=secrets_manager, expected_type=type_hints["secrets_manager"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if automatic is not None:
                self._values["automatic"] = automatic
            if secrets_manager is not None:
                self._values["secrets_manager"] = secrets_manager

        @builtins.property
        def automatic(self) -> typing.Any:
            '''Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputtransitencryptionkeyconfiguration.html#cfn-mediaconnect-routerinput-routerinputtransitencryptionkeyconfiguration-automatic
            '''
            result = self._values.get("automatic")
            return typing.cast(typing.Any, result)

        @builtins.property
        def secrets_manager(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty"]]:
            '''The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputtransitencryptionkeyconfiguration.html#cfn-mediaconnect-routerinput-routerinputtransitencryptionkeyconfiguration-secretsmanager
            '''
            result = self._values.get("secrets_manager")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouterInputTransitEncryptionKeyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.RouterInputTransitEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_key_configuration": "encryptionKeyConfiguration",
            "encryption_key_type": "encryptionKeyType",
        },
    )
    class RouterInputTransitEncryptionProperty:
        def __init__(
            self,
            *,
            encryption_key_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RouterInputTransitEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            encryption_key_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The transit encryption settings for a router input.

            :param encryption_key_configuration: Defines the configuration settings for transit encryption keys.
            :param encryption_key_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputtransitencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                router_input_transit_encryption_property = mediaconnect.CfnRouterInput.RouterInputTransitEncryptionProperty(
                    encryption_key_configuration=mediaconnect.CfnRouterInput.RouterInputTransitEncryptionKeyConfigurationProperty(
                        automatic=automatic,
                        secrets_manager=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
                
                    # the properties below are optional
                    encryption_key_type="encryptionKeyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__85f5061e2ce8c42b22b7dc305382ea9bfa145cf532ef8f62591b3684205d6713)
                check_type(argname="argument encryption_key_configuration", value=encryption_key_configuration, expected_type=type_hints["encryption_key_configuration"])
                check_type(argname="argument encryption_key_type", value=encryption_key_type, expected_type=type_hints["encryption_key_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_key_configuration": encryption_key_configuration,
            }
            if encryption_key_type is not None:
                self._values["encryption_key_type"] = encryption_key_type

        @builtins.property
        def encryption_key_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputTransitEncryptionKeyConfigurationProperty"]:
            '''Defines the configuration settings for transit encryption keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputtransitencryption.html#cfn-mediaconnect-routerinput-routerinputtransitencryption-encryptionkeyconfiguration
            '''
            result = self._values.get("encryption_key_configuration")
            assert result is not None, "Required property 'encryption_key_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputTransitEncryptionKeyConfigurationProperty"], result)

        @builtins.property
        def encryption_key_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-routerinputtransitencryption.html#cfn-mediaconnect-routerinput-routerinputtransitencryption-encryptionkeytype
            '''
            result = self._values.get("encryption_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouterInputTransitEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "port": "port",
            "forward_error_correction": "forwardErrorCorrection",
        },
    )
    class RtpRouterInputConfigurationProperty:
        def __init__(
            self,
            *,
            port: jsii.Number,
            forward_error_correction: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration settings for a Router Input using the RTP (Real-Time Transport Protocol) protocol, including the port and forward error correction state.

            :param port: The port number used for the RTP protocol in the router input configuration.
            :param forward_error_correction: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                rtp_router_input_configuration_property = mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                    port=123,
                
                    # the properties below are optional
                    forward_error_correction="forwardErrorCorrection"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3cb7da58ee58865b37c64051cce4480a789d51b84a87b3f8c0bb5c8c54eaed49)
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument forward_error_correction", value=forward_error_correction, expected_type=type_hints["forward_error_correction"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "port": port,
            }
            if forward_error_correction is not None:
                self._values["forward_error_correction"] = forward_error_correction

        @builtins.property
        def port(self) -> jsii.Number:
            '''The port number used for the RTP protocol in the router input configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration.html#cfn-mediaconnect-routerinput-rtprouterinputconfiguration-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def forward_error_correction(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-rtprouterinputconfiguration.html#cfn-mediaconnect-routerinput-rtprouterinputconfiguration-forwarderrorcorrection
            '''
            result = self._values.get("forward_error_correction")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RtpRouterInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "secret_arn": "secretArn"},
    )
    class SecretsManagerEncryptionKeyConfigurationProperty:
        def __init__(self, *, role_arn: builtins.str, secret_arn: builtins.str) -> None:
            '''The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :param role_arn: The ARN of the IAM role assumed by MediaConnect to access the AWS Secrets Manager secret.
            :param secret_arn: The ARN of the AWS Secrets Manager secret used for transit encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-secretsmanagerencryptionkeyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                secrets_manager_encryption_key_configuration_property = mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__656ecf17b2aa0c4612970c8eb2678158214e80be3a6040146c524608d6fe0ffc)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "secret_arn": secret_arn,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role assumed by MediaConnect to access the AWS Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-secretsmanagerencryptionkeyconfiguration.html#cfn-mediaconnect-routerinput-secretsmanagerencryptionkeyconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The ARN of the AWS Secrets Manager secret used for transit encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-secretsmanagerencryptionkeyconfiguration.html#cfn-mediaconnect-routerinput-secretsmanagerencryptionkeyconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretsManagerEncryptionKeyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "minimum_latency_milliseconds": "minimumLatencyMilliseconds",
            "source_address": "sourceAddress",
            "source_port": "sourcePort",
            "decryption_configuration": "decryptionConfiguration",
            "stream_id": "streamId",
        },
    )
    class SrtCallerRouterInputConfigurationProperty:
        def __init__(
            self,
            *,
            minimum_latency_milliseconds: jsii.Number,
            source_address: builtins.str,
            source_port: jsii.Number,
            decryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.SrtDecryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            stream_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in caller mode, including the source address and port, minimum latency, stream ID, and decryption key configuration.

            :param minimum_latency_milliseconds: The minimum latency in milliseconds for the SRT protocol in caller mode.
            :param source_address: The source IP address for the SRT protocol in caller mode.
            :param source_port: The source port number for the SRT protocol in caller mode.
            :param decryption_configuration: Contains the configuration settings for decrypting SRT streams, including the encryption key details and decryption parameters.
            :param stream_id: The stream ID for the SRT protocol in caller mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                srt_caller_router_input_configuration_property = mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                    minimum_latency_milliseconds=123,
                    source_address="sourceAddress",
                    source_port=123,
                
                    # the properties below are optional
                    decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                        encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
                    stream_id="streamId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__beeb94f30bd48ba57793ec4ae9b1de79893c6af67077601ee991d8325f1c1155)
                check_type(argname="argument minimum_latency_milliseconds", value=minimum_latency_milliseconds, expected_type=type_hints["minimum_latency_milliseconds"])
                check_type(argname="argument source_address", value=source_address, expected_type=type_hints["source_address"])
                check_type(argname="argument source_port", value=source_port, expected_type=type_hints["source_port"])
                check_type(argname="argument decryption_configuration", value=decryption_configuration, expected_type=type_hints["decryption_configuration"])
                check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "minimum_latency_milliseconds": minimum_latency_milliseconds,
                "source_address": source_address,
                "source_port": source_port,
            }
            if decryption_configuration is not None:
                self._values["decryption_configuration"] = decryption_configuration
            if stream_id is not None:
                self._values["stream_id"] = stream_id

        @builtins.property
        def minimum_latency_milliseconds(self) -> jsii.Number:
            '''The minimum latency in milliseconds for the SRT protocol in caller mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration.html#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-minimumlatencymilliseconds
            '''
            result = self._values.get("minimum_latency_milliseconds")
            assert result is not None, "Required property 'minimum_latency_milliseconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def source_address(self) -> builtins.str:
            '''The source IP address for the SRT protocol in caller mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration.html#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-sourceaddress
            '''
            result = self._values.get("source_address")
            assert result is not None, "Required property 'source_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_port(self) -> jsii.Number:
            '''The source port number for the SRT protocol in caller mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration.html#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-sourceport
            '''
            result = self._values.get("source_port")
            assert result is not None, "Required property 'source_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def decryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtDecryptionConfigurationProperty"]]:
            '''Contains the configuration settings for decrypting SRT streams, including the encryption key details and decryption parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration.html#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-decryptionconfiguration
            '''
            result = self._values.get("decryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtDecryptionConfigurationProperty"]], result)

        @builtins.property
        def stream_id(self) -> typing.Optional[builtins.str]:
            '''The stream ID for the SRT protocol in caller mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtcallerrouterinputconfiguration.html#cfn-mediaconnect-routerinput-srtcallerrouterinputconfiguration-streamid
            '''
            result = self._values.get("stream_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SrtCallerRouterInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_key": "encryptionKey"},
    )
    class SrtDecryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_key: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains the configuration settings for decrypting SRT streams, including the encryption key details and decryption parameters.

            :param encryption_key: The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                srt_decryption_configuration_property = mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                    encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b8e55bc2cc629dfc624dfe6751b96283b3f6c08591aba80e4005288f47ee98a)
                check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_key": encryption_key,
            }

        @builtins.property
        def encryption_key(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty"]:
            '''The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtdecryptionconfiguration.html#cfn-mediaconnect-routerinput-srtdecryptionconfiguration-encryptionkey
            '''
            result = self._values.get("encryption_key")
            assert result is not None, "Required property 'encryption_key' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SrtDecryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "minimum_latency_milliseconds": "minimumLatencyMilliseconds",
            "port": "port",
            "decryption_configuration": "decryptionConfiguration",
        },
    )
    class SrtListenerRouterInputConfigurationProperty:
        def __init__(
            self,
            *,
            minimum_latency_milliseconds: jsii.Number,
            port: jsii.Number,
            decryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.SrtDecryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration settings for a router input using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and decryption key configuration.

            :param minimum_latency_milliseconds: The minimum latency in milliseconds for the SRT protocol in listener mode.
            :param port: The port number for the SRT protocol in listener mode.
            :param decryption_configuration: Contains the configuration settings for decrypting SRT streams, including the encryption key details and decryption parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                srt_listener_router_input_configuration_property = mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                    minimum_latency_milliseconds=123,
                    port=123,
                
                    # the properties below are optional
                    decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                        encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2020f903810fd45bfaa02594fdb1a23bdb3bcc4a9ac870d479f9756284d1f45d)
                check_type(argname="argument minimum_latency_milliseconds", value=minimum_latency_milliseconds, expected_type=type_hints["minimum_latency_milliseconds"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument decryption_configuration", value=decryption_configuration, expected_type=type_hints["decryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "minimum_latency_milliseconds": minimum_latency_milliseconds,
                "port": port,
            }
            if decryption_configuration is not None:
                self._values["decryption_configuration"] = decryption_configuration

        @builtins.property
        def minimum_latency_milliseconds(self) -> jsii.Number:
            '''The minimum latency in milliseconds for the SRT protocol in listener mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration.html#cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-minimumlatencymilliseconds
            '''
            result = self._values.get("minimum_latency_milliseconds")
            assert result is not None, "Required property 'minimum_latency_milliseconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The port number for the SRT protocol in listener mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration.html#cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def decryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtDecryptionConfigurationProperty"]]:
            '''Contains the configuration settings for decrypting SRT streams, including the encryption key details and decryption parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-srtlistenerrouterinputconfiguration.html#cfn-mediaconnect-routerinput-srtlistenerrouterinputconfiguration-decryptionconfiguration
            '''
            result = self._values.get("decryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.SrtDecryptionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SrtListenerRouterInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInput.StandardRouterInputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_interface_arn": "networkInterfaceArn",
            "protocol_configuration": "protocolConfiguration",
            "protocol": "protocol",
        },
    )
    class StandardRouterInputConfigurationProperty:
        def __init__(
            self,
            *,
            network_interface_arn: builtins.str,
            protocol_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RouterInputProtocolConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            protocol: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration settings for a standard router input, including the protocol, protocol-specific configuration, network interface, and availability zone.

            :param network_interface_arn: The Amazon Resource Name (ARN) of the network interface associated with the standard router input.
            :param protocol_configuration: The protocol configuration settings for a router input.
            :param protocol: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                standard_router_input_configuration_property = mediaconnect.CfnRouterInput.StandardRouterInputConfigurationProperty(
                    network_interface_arn="networkInterfaceArn",
                    protocol_configuration=mediaconnect.CfnRouterInput.RouterInputProtocolConfigurationProperty(
                        rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                            port=123,
                            recovery_latency_milliseconds=123
                        ),
                        rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                            port=123,
                
                            # the properties below are optional
                            forward_error_correction="forwardErrorCorrection"
                        ),
                        srt_caller=mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                            minimum_latency_milliseconds=123,
                            source_address="sourceAddress",
                            source_port=123,
                
                            # the properties below are optional
                            decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
                            stream_id="streamId"
                        ),
                        srt_listener=mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                            minimum_latency_milliseconds=123,
                            port=123,
                
                            # the properties below are optional
                            decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            )
                        )
                    ),
                
                    # the properties below are optional
                    protocol="protocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__95ce52cf6881e0f95e336a6920de1725ead5c20a78c3b050791def2f0629d492)
                check_type(argname="argument network_interface_arn", value=network_interface_arn, expected_type=type_hints["network_interface_arn"])
                check_type(argname="argument protocol_configuration", value=protocol_configuration, expected_type=type_hints["protocol_configuration"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_interface_arn": network_interface_arn,
                "protocol_configuration": protocol_configuration,
            }
            if protocol is not None:
                self._values["protocol"] = protocol

        @builtins.property
        def network_interface_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the network interface associated with the standard router input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration.html#cfn-mediaconnect-routerinput-standardrouterinputconfiguration-networkinterfacearn
            '''
            result = self._values.get("network_interface_arn")
            assert result is not None, "Required property 'network_interface_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputProtocolConfigurationProperty"]:
            '''The protocol configuration settings for a router input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration.html#cfn-mediaconnect-routerinput-standardrouterinputconfiguration-protocolconfiguration
            '''
            result = self._values.get("protocol_configuration")
            assert result is not None, "Required property 'protocol_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputProtocolConfigurationProperty"], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routerinput-standardrouterinputconfiguration.html#cfn-mediaconnect-routerinput-standardrouterinputconfiguration-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StandardRouterInputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterInputProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "maximum_bitrate": "maximumBitrate",
        "name": "name",
        "routing_scope": "routingScope",
        "tier": "tier",
        "availability_zone": "availabilityZone",
        "maintenance_configuration": "maintenanceConfiguration",
        "region_name": "regionName",
        "tags": "tags",
        "transit_encryption": "transitEncryption",
    },
)
class CfnRouterInputProps:
    def __init__(
        self,
        *,
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RouterInputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        maximum_bitrate: jsii.Number,
        name: builtins.str,
        routing_scope: builtins.str,
        tier: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        maintenance_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.MaintenanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        region_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        transit_encryption: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterInput.RouterInputTransitEncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRouterInput``.

        :param configuration: The configuration settings for a router input.
        :param maximum_bitrate: The maximum bitrate for the router input.
        :param name: The name of the router input.
        :param routing_scope: Indicates whether the router input is configured for Regional or global routing.
        :param tier: The tier level of the router input.
        :param availability_zone: The Availability Zone of the router input.
        :param maintenance_configuration: The maintenance configuration settings applied to this router input.
        :param region_name: The AWS Region where the router input is located.
        :param tags: Key-value pairs that can be used to tag and organize this router input.
        :param transit_encryption: Encryption information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            # automatic: Any
            # default_: Any
            
            cfn_router_input_props = mediaconnect.CfnRouterInputProps(
                configuration=mediaconnect.CfnRouterInput.RouterInputConfigurationProperty(
                    failover=mediaconnect.CfnRouterInput.FailoverRouterInputConfigurationProperty(
                        network_interface_arn="networkInterfaceArn",
                        protocol_configurations=[mediaconnect.CfnRouterInput.FailoverRouterInputProtocolConfigurationProperty(
                            rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                                port=123,
                                recovery_latency_milliseconds=123
                            ),
                            rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                                port=123,
            
                                # the properties below are optional
                                forward_error_correction="forwardErrorCorrection"
                            ),
                            srt_caller=mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                                minimum_latency_milliseconds=123,
                                source_address="sourceAddress",
                                source_port=123,
            
                                # the properties below are optional
                                decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                ),
                                stream_id="streamId"
                            ),
                            srt_listener=mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                                minimum_latency_milliseconds=123,
                                port=123,
            
                                # the properties below are optional
                                decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                )
                            )
                        )],
                        source_priority_mode="sourcePriorityMode",
            
                        # the properties below are optional
                        primary_source_index=123
                    ),
                    media_connect_flow=mediaconnect.CfnRouterInput.MediaConnectFlowRouterInputConfigurationProperty(
                        source_transit_decryption=mediaconnect.CfnRouterInput.FlowTransitEncryptionProperty(
                            encryption_key_configuration=mediaconnect.CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty(
                                automatic=automatic,
                                secrets_manager=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
            
                            # the properties below are optional
                            encryption_key_type="encryptionKeyType"
                        ),
            
                        # the properties below are optional
                        flow_arn="flowArn",
                        flow_output_arn="flowOutputArn"
                    ),
                    merge=mediaconnect.CfnRouterInput.MergeRouterInputConfigurationProperty(
                        merge_recovery_window_milliseconds=123,
                        network_interface_arn="networkInterfaceArn",
                        protocol_configurations=[mediaconnect.CfnRouterInput.MergeRouterInputProtocolConfigurationProperty(
                            rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                                port=123,
                                recovery_latency_milliseconds=123
                            ),
                            rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                                port=123,
            
                                # the properties below are optional
                                forward_error_correction="forwardErrorCorrection"
                            )
                        )]
                    ),
                    standard=mediaconnect.CfnRouterInput.StandardRouterInputConfigurationProperty(
                        network_interface_arn="networkInterfaceArn",
                        protocol_configuration=mediaconnect.CfnRouterInput.RouterInputProtocolConfigurationProperty(
                            rist=mediaconnect.CfnRouterInput.RistRouterInputConfigurationProperty(
                                port=123,
                                recovery_latency_milliseconds=123
                            ),
                            rtp=mediaconnect.CfnRouterInput.RtpRouterInputConfigurationProperty(
                                port=123,
            
                                # the properties below are optional
                                forward_error_correction="forwardErrorCorrection"
                            ),
                            srt_caller=mediaconnect.CfnRouterInput.SrtCallerRouterInputConfigurationProperty(
                                minimum_latency_milliseconds=123,
                                source_address="sourceAddress",
                                source_port=123,
            
                                # the properties below are optional
                                decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                ),
                                stream_id="streamId"
                            ),
                            srt_listener=mediaconnect.CfnRouterInput.SrtListenerRouterInputConfigurationProperty(
                                minimum_latency_milliseconds=123,
                                port=123,
            
                                # the properties below are optional
                                decryption_configuration=mediaconnect.CfnRouterInput.SrtDecryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                )
                            )
                        ),
            
                        # the properties below are optional
                        protocol="protocol"
                    )
                ),
                maximum_bitrate=123,
                name="name",
                routing_scope="routingScope",
                tier="tier",
            
                # the properties below are optional
                availability_zone="availabilityZone",
                maintenance_configuration=mediaconnect.CfnRouterInput.MaintenanceConfigurationProperty(
                    default=default_,
                    preferred_day_time=mediaconnect.CfnRouterInput.PreferredDayTimeMaintenanceConfigurationProperty(
                        day="day",
                        time="time"
                    )
                ),
                region_name="regionName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                transit_encryption=mediaconnect.CfnRouterInput.RouterInputTransitEncryptionProperty(
                    encryption_key_configuration=mediaconnect.CfnRouterInput.RouterInputTransitEncryptionKeyConfigurationProperty(
                        automatic=automatic,
                        secrets_manager=mediaconnect.CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
            
                    # the properties below are optional
                    encryption_key_type="encryptionKeyType"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__629abd36e1d3f5d9a60304da2c55389ba519de279616eb9eae24baa19310f5f4)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument maximum_bitrate", value=maximum_bitrate, expected_type=type_hints["maximum_bitrate"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument routing_scope", value=routing_scope, expected_type=type_hints["routing_scope"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument maintenance_configuration", value=maintenance_configuration, expected_type=type_hints["maintenance_configuration"])
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument transit_encryption", value=transit_encryption, expected_type=type_hints["transit_encryption"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
            "maximum_bitrate": maximum_bitrate,
            "name": name,
            "routing_scope": routing_scope,
            "tier": tier,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if maintenance_configuration is not None:
            self._values["maintenance_configuration"] = maintenance_configuration
        if region_name is not None:
            self._values["region_name"] = region_name
        if tags is not None:
            self._values["tags"] = tags
        if transit_encryption is not None:
            self._values["transit_encryption"] = transit_encryption

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputConfigurationProperty"]:
        '''The configuration settings for a router input.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html#cfn-mediaconnect-routerinput-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputConfigurationProperty"], result)

    @builtins.property
    def maximum_bitrate(self) -> jsii.Number:
        '''The maximum bitrate for the router input.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html#cfn-mediaconnect-routerinput-maximumbitrate
        '''
        result = self._values.get("maximum_bitrate")
        assert result is not None, "Required property 'maximum_bitrate' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the router input.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html#cfn-mediaconnect-routerinput-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def routing_scope(self) -> builtins.str:
        '''Indicates whether the router input is configured for Regional or global routing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html#cfn-mediaconnect-routerinput-routingscope
        '''
        result = self._values.get("routing_scope")
        assert result is not None, "Required property 'routing_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tier(self) -> builtins.str:
        '''The tier level of the router input.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html#cfn-mediaconnect-routerinput-tier
        '''
        result = self._values.get("tier")
        assert result is not None, "Required property 'tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone of the router input.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html#cfn-mediaconnect-routerinput-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MaintenanceConfigurationProperty"]]:
        '''The maintenance configuration settings applied to this router input.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html#cfn-mediaconnect-routerinput-maintenanceconfiguration
        '''
        result = self._values.get("maintenance_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.MaintenanceConfigurationProperty"]], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''The AWS Region where the router input is located.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html#cfn-mediaconnect-routerinput-regionname
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Key-value pairs that can be used to tag and organize this router input.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html#cfn-mediaconnect-routerinput-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def transit_encryption(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputTransitEncryptionProperty"]]:
        '''Encryption information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routerinput.html#cfn-mediaconnect-routerinput-transitencryption
        '''
        result = self._values.get("transit_encryption")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterInput.RouterInputTransitEncryptionProperty"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRouterInputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IRouterNetworkInterfaceRef_05bd061c, _ITaggableV2_4e6798f8)
class CfnRouterNetworkInterface(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterNetworkInterface",
):
    '''Represents a router network interface in AWS Elemental MediaConnect that is used to define a network boundary for router resources.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routernetworkinterface.html
    :cloudformationResource: AWS::MediaConnect::RouterNetworkInterface
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_router_network_interface = mediaconnect.CfnRouterNetworkInterface(self, "MyCfnRouterNetworkInterface",
            configuration=mediaconnect.CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty(
                public=mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceConfigurationProperty(
                    allow_rules=[mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceRuleProperty(
                        cidr="cidr"
                    )]
                ),
                vpc=mediaconnect.CfnRouterNetworkInterface.VpcRouterNetworkInterfaceConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_id="subnetId"
                )
            ),
            name="name",
        
            # the properties below are optional
            region_name="regionName",
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
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        region_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::RouterNetworkInterface``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: The configuration settings for a router network interface.
        :param name: The name of the router network interface.
        :param region_name: The AWS Region where the router network interface is located.
        :param tags: Key-value pairs that can be used to tag and organize this router network interface.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24310ca09a20908bd3bbf12dedeae64057a241ad260d0173c063494e94a5e372)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRouterNetworkInterfaceProps(
            configuration=configuration, name=name, region_name=region_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForRouterNetworkInterface")
    @builtins.classmethod
    def arn_for_router_network_interface(
        cls,
        resource: "_IRouterNetworkInterfaceRef_05bd061c",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31cc864547a94937d2c7f541798d2155fb714db7022c9ef5c73db0655c89a985)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForRouterNetworkInterface", [resource]))

    @jsii.member(jsii_name="isCfnRouterNetworkInterface")
    @builtins.classmethod
    def is_cfn_router_network_interface(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnRouterNetworkInterface.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58580bda8f3f828588ff2afcfe7bb604e0dda1e286e8115e82a78cd696a8501c)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnRouterNetworkInterface", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99813ca43090ccca654d469e7c1278029c90800fa145e079a4c1a327ab3e09c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e4249152775ddcb28eec7583b5299fb11c67a758dbbd05886d4cb11ac3c3cf26)
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
        '''The Amazon Resource Name (ARN) of the router network interface.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociatedInputCount")
    def attr_associated_input_count(self) -> jsii.Number:
        '''The number of router inputs associated with the network interface.

        :cloudformationAttribute: AssociatedInputCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAssociatedInputCount"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociatedOutputCount")
    def attr_associated_output_count(self) -> jsii.Number:
        '''The number of router outputs associated with the network interface.

        :cloudformationAttribute: AssociatedOutputCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAssociatedOutputCount"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the router network interface was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier of the router network interface.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrNetworkInterfaceType")
    def attr_network_interface_type(self) -> builtins.str:
        '''The type of the router network interface.

        :cloudformationAttribute: NetworkInterfaceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNetworkInterfaceType"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The current state of the router network interface.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the router network interface was last updated.

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
    @jsii.member(jsii_name="routerNetworkInterfaceRef")
    def router_network_interface_ref(
        self,
    ) -> "_RouterNetworkInterfaceReference_fdc8b08c":
        '''A reference to a RouterNetworkInterface resource.'''
        return typing.cast("_RouterNetworkInterfaceReference_fdc8b08c", jsii.get(self, "routerNetworkInterfaceRef"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty"]:
        '''The configuration settings for a router network interface.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ada01cdf0843f372e2358efd8825753add57ec0a85c656d8730df8fe11d675f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the router network interface.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43e368d1cada7b7c423f1301292b045fe35c167df6909c271c310814e384d2f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="regionName")
    def region_name(self) -> typing.Optional[builtins.str]:
        '''The AWS Region where the router network interface is located.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionName"))

    @region_name.setter
    def region_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__640023b56bd3332877d359f440c6fc815950e5fd32985dc6f11c1892bd7cfaaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Key-value pairs that can be used to tag and organize this router network interface.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70255a3ae365875252abf102dc0c10255d13f5d5552ee11bd61363fcd195a6d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"allow_rules": "allowRules"},
    )
    class PublicRouterNetworkInterfaceConfigurationProperty:
        def __init__(
            self,
            *,
            allow_rules: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterNetworkInterface.PublicRouterNetworkInterfaceRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''The configuration settings for a public router network interface, including the list of allowed CIDR blocks.

            :param allow_rules: The list of allowed CIDR blocks for the public router network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                public_router_network_interface_configuration_property = mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceConfigurationProperty(
                    allow_rules=[mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceRuleProperty(
                        cidr="cidr"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86b2b80a7d574588364b855dababd894760b38396c485dd9b78bbd7b36199e16)
                check_type(argname="argument allow_rules", value=allow_rules, expected_type=type_hints["allow_rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allow_rules": allow_rules,
            }

        @builtins.property
        def allow_rules(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.PublicRouterNetworkInterfaceRuleProperty"]]]:
            '''The list of allowed CIDR blocks for the public router network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration.html#cfn-mediaconnect-routernetworkinterface-publicrouternetworkinterfaceconfiguration-allowrules
            '''
            result = self._values.get("allow_rules")
            assert result is not None, "Required property 'allow_rules' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.PublicRouterNetworkInterfaceRuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublicRouterNetworkInterfaceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr": "cidr"},
    )
    class PublicRouterNetworkInterfaceRuleProperty:
        def __init__(self, *, cidr: builtins.str) -> None:
            '''A rule that allows a specific CIDR block to access the public router network interface.

            :param cidr: The CIDR block that is allowed to access the public router network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                public_router_network_interface_rule_property = mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceRuleProperty(
                    cidr="cidr"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b16b6a0a6e17ced0af99bf04d82b87f0ed226b2b3a5459757c42969b81e58901)
                check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cidr": cidr,
            }

        @builtins.property
        def cidr(self) -> builtins.str:
            '''The CIDR block that is allowed to access the public router network interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule.html#cfn-mediaconnect-routernetworkinterface-publicrouternetworkinterfacerule-cidr
            '''
            result = self._values.get("cidr")
            assert result is not None, "Required property 'cidr' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PublicRouterNetworkInterfaceRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"public": "public", "vpc": "vpc"},
    )
    class RouterNetworkInterfaceConfigurationProperty:
        def __init__(
            self,
            *,
            public: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterNetworkInterface.PublicRouterNetworkInterfaceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            vpc: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterNetworkInterface.VpcRouterNetworkInterfaceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param public: The configuration settings for a public router network interface, including the list of allowed CIDR blocks.
            :param vpc: The configuration settings for a router network interface within a VPC, including the security group IDs and subnet ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                router_network_interface_configuration_property = mediaconnect.CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty(
                    public=mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceConfigurationProperty(
                        allow_rules=[mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceRuleProperty(
                            cidr="cidr"
                        )]
                    ),
                    vpc=mediaconnect.CfnRouterNetworkInterface.VpcRouterNetworkInterfaceConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_id="subnetId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed1657ecdbbe74a0573f76b57267bb3e8bae064809e9330b8325b2050859af13)
                check_type(argname="argument public", value=public, expected_type=type_hints["public"])
                check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if public is not None:
                self._values["public"] = public
            if vpc is not None:
                self._values["vpc"] = vpc

        @builtins.property
        def public(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.PublicRouterNetworkInterfaceConfigurationProperty"]]:
            '''The configuration settings for a public router network interface, including the list of allowed CIDR blocks.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration.html#cfn-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-public
            '''
            result = self._values.get("public")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.PublicRouterNetworkInterfaceConfigurationProperty"]], result)

        @builtins.property
        def vpc(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.VpcRouterNetworkInterfaceConfigurationProperty"]]:
            '''The configuration settings for a router network interface within a VPC, including the security group IDs and subnet ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration.html#cfn-mediaconnect-routernetworkinterface-routernetworkinterfaceconfiguration-vpc
            '''
            result = self._values.get("vpc")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.VpcRouterNetworkInterfaceConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouterNetworkInterfaceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterNetworkInterface.VpcRouterNetworkInterfaceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_id": "subnetId",
        },
    )
    class VpcRouterNetworkInterfaceConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_id: builtins.str,
        ) -> None:
            '''The configuration settings for a router network interface within a VPC, including the security group IDs and subnet ID.

            :param security_group_ids: The IDs of the security groups to associate with the router network interface within the VPC.
            :param subnet_id: The ID of the subnet within the VPC to associate the router network interface with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_router_network_interface_configuration_property = mediaconnect.CfnRouterNetworkInterface.VpcRouterNetworkInterfaceConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_id="subnetId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e100934f67ad4ab390b48cc7ed268e9b09228c57ff83fdda79b86e4a8e736125)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_id": subnet_id,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''The IDs of the security groups to associate with the router network interface within the VPC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration.html#cfn-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_id(self) -> builtins.str:
            '''The ID of the subnet within the VPC to associate the router network interface with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration.html#cfn-mediaconnect-routernetworkinterface-vpcrouternetworkinterfaceconfiguration-subnetid
            '''
            result = self._values.get("subnet_id")
            assert result is not None, "Required property 'subnet_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcRouterNetworkInterfaceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterNetworkInterfaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "name": "name",
        "region_name": "regionName",
        "tags": "tags",
    },
)
class CfnRouterNetworkInterfaceProps:
    def __init__(
        self,
        *,
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        region_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRouterNetworkInterface``.

        :param configuration: The configuration settings for a router network interface.
        :param name: The name of the router network interface.
        :param region_name: The AWS Region where the router network interface is located.
        :param tags: Key-value pairs that can be used to tag and organize this router network interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routernetworkinterface.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_router_network_interface_props = mediaconnect.CfnRouterNetworkInterfaceProps(
                configuration=mediaconnect.CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty(
                    public=mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceConfigurationProperty(
                        allow_rules=[mediaconnect.CfnRouterNetworkInterface.PublicRouterNetworkInterfaceRuleProperty(
                            cidr="cidr"
                        )]
                    ),
                    vpc=mediaconnect.CfnRouterNetworkInterface.VpcRouterNetworkInterfaceConfigurationProperty(
                        security_group_ids=["securityGroupIds"],
                        subnet_id="subnetId"
                    )
                ),
                name="name",
            
                # the properties below are optional
                region_name="regionName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c96298441d1fa6afb4e99a0f43137a8859e8ca44045c1e46e91194e38b1ef1c)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
            "name": name,
        }
        if region_name is not None:
            self._values["region_name"] = region_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty"]:
        '''The configuration settings for a router network interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routernetworkinterface.html#cfn-mediaconnect-routernetworkinterface-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty"], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the router network interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routernetworkinterface.html#cfn-mediaconnect-routernetworkinterface-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''The AWS Region where the router network interface is located.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routernetworkinterface.html#cfn-mediaconnect-routernetworkinterface-regionname
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Key-value pairs that can be used to tag and organize this router network interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routernetworkinterface.html#cfn-mediaconnect-routernetworkinterface-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRouterNetworkInterfaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IRouterOutputRef_afa317cd, _ITaggableV2_4e6798f8)
class CfnRouterOutput(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput",
):
    '''Represents a router input in AWS Elemental MediaConnect that can be used to egress content transmitted from router inputs.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html
    :cloudformationResource: AWS::MediaConnect::RouterOutput
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        # automatic: Any
        # default_: Any
        
        cfn_router_output = mediaconnect.CfnRouterOutput(self, "MyCfnRouterOutput",
            configuration=mediaconnect.CfnRouterOutput.RouterOutputConfigurationProperty(
                media_connect_flow=mediaconnect.CfnRouterOutput.MediaConnectFlowRouterOutputConfigurationProperty(
                    destination_transit_encryption=mediaconnect.CfnRouterOutput.FlowTransitEncryptionProperty(
                        encryption_key_configuration=mediaconnect.CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty(
                            automatic=automatic,
                            secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
        
                        # the properties below are optional
                        encryption_key_type="encryptionKeyType"
                    ),
        
                    # the properties below are optional
                    flow_arn="flowArn",
                    flow_source_arn="flowSourceArn"
                ),
                media_live_input=mediaconnect.CfnRouterOutput.MediaLiveInputRouterOutputConfigurationProperty(
                    destination_transit_encryption=mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionProperty(
                        encryption_key_configuration=mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty(
                            automatic=automatic,
                            secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
        
                        # the properties below are optional
                        encryption_key_type="encryptionKeyType"
                    ),
        
                    # the properties below are optional
                    media_live_input_arn="mediaLiveInputArn",
                    media_live_pipeline_id="mediaLivePipelineId"
                ),
                standard=mediaconnect.CfnRouterOutput.StandardRouterOutputConfigurationProperty(
                    network_interface_arn="networkInterfaceArn",
                    protocol_configuration=mediaconnect.CfnRouterOutput.RouterOutputProtocolConfigurationProperty(
                        rist=mediaconnect.CfnRouterOutput.RistRouterOutputConfigurationProperty(
                            destination_address="destinationAddress",
                            destination_port=123
                        ),
                        rtp=mediaconnect.CfnRouterOutput.RtpRouterOutputConfigurationProperty(
                            destination_address="destinationAddress",
                            destination_port=123,
        
                            # the properties below are optional
                            forward_error_correction="forwardErrorCorrection"
                        ),
                        srt_caller=mediaconnect.CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty(
                            destination_address="destinationAddress",
                            destination_port=123,
                            minimum_latency_milliseconds=123,
        
                            # the properties below are optional
                            encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
                            stream_id="streamId"
                        ),
                        srt_listener=mediaconnect.CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty(
                            minimum_latency_milliseconds=123,
                            port=123,
        
                            # the properties below are optional
                            encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            )
                        )
                    ),
        
                    # the properties below are optional
                    protocol="protocol"
                )
            ),
            maximum_bitrate=123,
            name="name",
            routing_scope="routingScope",
            tier="tier",
        
            # the properties below are optional
            availability_zone="availabilityZone",
            maintenance_configuration=mediaconnect.CfnRouterOutput.MaintenanceConfigurationProperty(
                default=default_,
                preferred_day_time=mediaconnect.CfnRouterOutput.PreferredDayTimeMaintenanceConfigurationProperty(
                    day="day",
                    time="time"
                )
            ),
            region_name="regionName",
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
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.RouterOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        maximum_bitrate: jsii.Number,
        name: builtins.str,
        routing_scope: builtins.str,
        tier: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        maintenance_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.MaintenanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        region_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::MediaConnect::RouterOutput``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: The configuration settings for a router output.
        :param maximum_bitrate: The maximum bitrate for the router output.
        :param name: The name of the router output.
        :param routing_scope: Indicates whether the router output is configured for Regional or global routing.
        :param tier: The tier level of the router output.
        :param availability_zone: The Availability Zone of the router output.
        :param maintenance_configuration: The maintenance configuration settings applied to this router output.
        :param region_name: The AWS Region where the router output is located.
        :param tags: Key-value pairs that can be used to tag and organize this router output.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0723832b1d0cb17f5bcd9018d140834abd5e94bc96fb3fb67d22f77fb5439c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRouterOutputProps(
            configuration=configuration,
            maximum_bitrate=maximum_bitrate,
            name=name,
            routing_scope=routing_scope,
            tier=tier,
            availability_zone=availability_zone,
            maintenance_configuration=maintenance_configuration,
            region_name=region_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForRouterOutput")
    @builtins.classmethod
    def arn_for_router_output(
        cls,
        resource: "_IRouterOutputRef_afa317cd",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24a2fbac160b0fd704ba7504535f3e38f1a17f7911da11e6a5c0eb4336436bbc)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForRouterOutput", [resource]))

    @jsii.member(jsii_name="isCfnRouterOutput")
    @builtins.classmethod
    def is_cfn_router_output(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnRouterOutput.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76381601efd880f1b3fc396253c86e23a095f42a58d2fdaf834228f3d26a1240)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnRouterOutput", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46c254968a788990028c9b84207c991e7dbd51c1a2e4cd0ceb7a94af8e32e549)
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
            type_hints = typing.get_type_hints(_typecheckingstub__96ef8ccb0c5e0eb94acef4319249f97dfa0ce9d3c9e57dbf2db800211064be5d)
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
        '''The Amazon Resource Name (ARN) of the router output.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The timestamp when the router output was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier of the router output.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrIpAddress")
    def attr_ip_address(self) -> builtins.str:
        '''The IP address of the router output.

        :cloudformationAttribute: IpAddress
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpAddress"))

    @builtins.property
    @jsii.member(jsii_name="attrMaintenanceType")
    def attr_maintenance_type(self) -> builtins.str:
        '''The type of maintenance configuration applied to this router output.

        :cloudformationAttribute: MaintenanceType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMaintenanceType"))

    @builtins.property
    @jsii.member(jsii_name="attrOutputType")
    def attr_output_type(self) -> builtins.str:
        '''The type of the router output.

        :cloudformationAttribute: OutputType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOutputType"))

    @builtins.property
    @jsii.member(jsii_name="attrRoutedState")
    def attr_routed_state(self) -> builtins.str:
        '''The current state of the association between the router output and its input.

        :cloudformationAttribute: RoutedState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRoutedState"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The overall state of the router output.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdatedAt")
    def attr_updated_at(self) -> builtins.str:
        '''The timestamp when the router output was last updated.

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
    @jsii.member(jsii_name="routerOutputRef")
    def router_output_ref(self) -> "_RouterOutputReference_12c4ea61":
        '''A reference to a RouterOutput resource.'''
        return typing.cast("_RouterOutputReference_12c4ea61", jsii.get(self, "routerOutputRef"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RouterOutputConfigurationProperty"]:
        '''The configuration settings for a router output.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RouterOutputConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RouterOutputConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f147da00aaf1cdc7014a62b08d8cdc0f9cfce3df5d377973424d2f11377219c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maximumBitrate")
    def maximum_bitrate(self) -> jsii.Number:
        '''The maximum bitrate for the router output.'''
        return typing.cast(jsii.Number, jsii.get(self, "maximumBitrate"))

    @maximum_bitrate.setter
    def maximum_bitrate(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6343c02a4b0b9d5d865add8c4d996a26f8389b83b214b7350ac7818a31991557)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBitrate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the router output.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4216c7d780d8fb5794084f06923c5c5b6e06951c7c74d95e570b19c17f16c07d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="routingScope")
    def routing_scope(self) -> builtins.str:
        '''Indicates whether the router output is configured for Regional or global routing.'''
        return typing.cast(builtins.str, jsii.get(self, "routingScope"))

    @routing_scope.setter
    def routing_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31256d5031051647600a9f3e6d4c7348c96db2131b170cbb3b84d03cb08508d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingScope", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        '''The tier level of the router output.'''
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1241eacdcaad6a0aadee10ac0ca9c13dd7f59cf1e7f5d785c7c1fc63190e220)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone of the router output.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b8371a3dd1aa326607abab281477f883dfadb45d27717b05bafb937c2ca7c31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maintenanceConfiguration")
    def maintenance_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MaintenanceConfigurationProperty"]]:
        '''The maintenance configuration settings applied to this router output.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MaintenanceConfigurationProperty"]], jsii.get(self, "maintenanceConfiguration"))

    @maintenance_configuration.setter
    def maintenance_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MaintenanceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2d9d66ea8cc6f7fb9f2d963cee39b38487405038346bed562a4282d170af87a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maintenanceConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="regionName")
    def region_name(self) -> typing.Optional[builtins.str]:
        '''The AWS Region where the router output is located.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionName"))

    @region_name.setter
    def region_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f23a2bac43b9e1bd96cf5c900f5ae7d229b5b15428c990a76f5392b3623edc92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regionName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Key-value pairs that can be used to tag and organize this router output.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb6937ae740be264a96755b4785a6121ef85f3be99b91fb48ef0d32ab567b808)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"automatic": "automatic", "secrets_manager": "secretsManager"},
    )
    class FlowTransitEncryptionKeyConfigurationProperty:
        def __init__(
            self,
            *,
            automatic: typing.Any = None,
            secrets_manager: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param automatic: Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.
            :param secrets_manager: The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-flowtransitencryptionkeyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                flow_transit_encryption_key_configuration_property = mediaconnect.CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty(
                    automatic=automatic,
                    secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d2919cc0452cea1b6c29eff661620544fa1903342e65d8def16c87e34ebac3af)
                check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
                check_type(argname="argument secrets_manager", value=secrets_manager, expected_type=type_hints["secrets_manager"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if automatic is not None:
                self._values["automatic"] = automatic
            if secrets_manager is not None:
                self._values["secrets_manager"] = secrets_manager

        @builtins.property
        def automatic(self) -> typing.Any:
            '''Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-flowtransitencryptionkeyconfiguration.html#cfn-mediaconnect-routeroutput-flowtransitencryptionkeyconfiguration-automatic
            '''
            result = self._values.get("automatic")
            return typing.cast(typing.Any, result)

        @builtins.property
        def secrets_manager(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty"]]:
            '''The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-flowtransitencryptionkeyconfiguration.html#cfn-mediaconnect-routeroutput-flowtransitencryptionkeyconfiguration-secretsmanager
            '''
            result = self._values.get("secrets_manager")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowTransitEncryptionKeyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.FlowTransitEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_key_configuration": "encryptionKeyConfiguration",
            "encryption_key_type": "encryptionKeyType",
        },
    )
    class FlowTransitEncryptionProperty:
        def __init__(
            self,
            *,
            encryption_key_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            encryption_key_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.

            :param encryption_key_configuration: Configuration settings for flow transit encryption keys.
            :param encryption_key_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-flowtransitencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                flow_transit_encryption_property = mediaconnect.CfnRouterOutput.FlowTransitEncryptionProperty(
                    encryption_key_configuration=mediaconnect.CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty(
                        automatic=automatic,
                        secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
                
                    # the properties below are optional
                    encryption_key_type="encryptionKeyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__eb7cec781c17f5df2ca2950847ce1a86c7e216d13b67c9830306688dd24f423c)
                check_type(argname="argument encryption_key_configuration", value=encryption_key_configuration, expected_type=type_hints["encryption_key_configuration"])
                check_type(argname="argument encryption_key_type", value=encryption_key_type, expected_type=type_hints["encryption_key_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_key_configuration": encryption_key_configuration,
            }
            if encryption_key_type is not None:
                self._values["encryption_key_type"] = encryption_key_type

        @builtins.property
        def encryption_key_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty"]:
            '''Configuration settings for flow transit encryption keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-flowtransitencryption.html#cfn-mediaconnect-routeroutput-flowtransitencryption-encryptionkeyconfiguration
            '''
            result = self._values.get("encryption_key_configuration")
            assert result is not None, "Required property 'encryption_key_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty"], result)

        @builtins.property
        def encryption_key_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-flowtransitencryption.html#cfn-mediaconnect-routeroutput-flowtransitencryption-encryptionkeytype
            '''
            result = self._values.get("encryption_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FlowTransitEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.MaintenanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"default": "default", "preferred_day_time": "preferredDayTime"},
    )
    class MaintenanceConfigurationProperty:
        def __init__(
            self,
            *,
            default: typing.Any = None,
            preferred_day_time: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.PreferredDayTimeMaintenanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param default: Configuration settings for default maintenance scheduling.
            :param preferred_day_time: Configuration for preferred day and time maintenance settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-maintenanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # default_: Any
                
                maintenance_configuration_property = mediaconnect.CfnRouterOutput.MaintenanceConfigurationProperty(
                    default=default_,
                    preferred_day_time=mediaconnect.CfnRouterOutput.PreferredDayTimeMaintenanceConfigurationProperty(
                        day="day",
                        time="time"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3168eb6355c5a713c93dcf1c47b10105621a55ece693c6e8524178049155072b)
                check_type(argname="argument default", value=default, expected_type=type_hints["default"])
                check_type(argname="argument preferred_day_time", value=preferred_day_time, expected_type=type_hints["preferred_day_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if default is not None:
                self._values["default"] = default
            if preferred_day_time is not None:
                self._values["preferred_day_time"] = preferred_day_time

        @builtins.property
        def default(self) -> typing.Any:
            '''Configuration settings for default maintenance scheduling.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-maintenanceconfiguration.html#cfn-mediaconnect-routeroutput-maintenanceconfiguration-default
            '''
            result = self._values.get("default")
            return typing.cast(typing.Any, result)

        @builtins.property
        def preferred_day_time(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.PreferredDayTimeMaintenanceConfigurationProperty"]]:
            '''Configuration for preferred day and time maintenance settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-maintenanceconfiguration.html#cfn-mediaconnect-routeroutput-maintenanceconfiguration-preferreddaytime
            '''
            result = self._values.get("preferred_day_time")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.PreferredDayTimeMaintenanceConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MaintenanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.MediaConnectFlowRouterOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_transit_encryption": "destinationTransitEncryption",
            "flow_arn": "flowArn",
            "flow_source_arn": "flowSourceArn",
        },
    )
    class MediaConnectFlowRouterOutputConfigurationProperty:
        def __init__(
            self,
            *,
            destination_transit_encryption: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.FlowTransitEncryptionProperty", typing.Dict[builtins.str, typing.Any]]],
            flow_arn: typing.Optional[builtins.str] = None,
            flow_source_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration settings for connecting a router output to a MediaConnect flow source.

            :param destination_transit_encryption: The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.
            :param flow_arn: The ARN of the flow to connect to this router output.
            :param flow_source_arn: The ARN of the flow source to connect to this router output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                media_connect_flow_router_output_configuration_property = mediaconnect.CfnRouterOutput.MediaConnectFlowRouterOutputConfigurationProperty(
                    destination_transit_encryption=mediaconnect.CfnRouterOutput.FlowTransitEncryptionProperty(
                        encryption_key_configuration=mediaconnect.CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty(
                            automatic=automatic,
                            secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
                
                        # the properties below are optional
                        encryption_key_type="encryptionKeyType"
                    ),
                
                    # the properties below are optional
                    flow_arn="flowArn",
                    flow_source_arn="flowSourceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c91e97d97b93eb546e4ca89c6248ae26ae42ceadf35a6181ea7b383b55804b49)
                check_type(argname="argument destination_transit_encryption", value=destination_transit_encryption, expected_type=type_hints["destination_transit_encryption"])
                check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
                check_type(argname="argument flow_source_arn", value=flow_source_arn, expected_type=type_hints["flow_source_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_transit_encryption": destination_transit_encryption,
            }
            if flow_arn is not None:
                self._values["flow_arn"] = flow_arn
            if flow_source_arn is not None:
                self._values["flow_source_arn"] = flow_source_arn

        @builtins.property
        def destination_transit_encryption(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.FlowTransitEncryptionProperty"]:
            '''The configuration that defines how content is encrypted during transit between the MediaConnect router and a MediaConnect flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-destinationtransitencryption
            '''
            result = self._values.get("destination_transit_encryption")
            assert result is not None, "Required property 'destination_transit_encryption' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.FlowTransitEncryptionProperty"], result)

        @builtins.property
        def flow_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the flow to connect to this router output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-flowarn
            '''
            result = self._values.get("flow_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def flow_source_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the flow source to connect to this router output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-mediaconnectflowrouteroutputconfiguration-flowsourcearn
            '''
            result = self._values.get("flow_source_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaConnectFlowRouterOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.MediaLiveInputRouterOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_transit_encryption": "destinationTransitEncryption",
            "media_live_input_arn": "mediaLiveInputArn",
            "media_live_pipeline_id": "mediaLivePipelineId",
        },
    )
    class MediaLiveInputRouterOutputConfigurationProperty:
        def __init__(
            self,
            *,
            destination_transit_encryption: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.MediaLiveTransitEncryptionProperty", typing.Dict[builtins.str, typing.Any]]],
            media_live_input_arn: typing.Optional[builtins.str] = None,
            media_live_pipeline_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration settings for connecting a router output to a MediaLive input.

            :param destination_transit_encryption: The encryption configuration that defines how content is encrypted during transit between MediaConnect Router and MediaLive. This configuration determines whether encryption keys are automatically managed by the service or manually managed through AWS Secrets Manager.
            :param media_live_input_arn: The ARN of the MediaLive input to connect to this router output.
            :param media_live_pipeline_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                media_live_input_router_output_configuration_property = mediaconnect.CfnRouterOutput.MediaLiveInputRouterOutputConfigurationProperty(
                    destination_transit_encryption=mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionProperty(
                        encryption_key_configuration=mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty(
                            automatic=automatic,
                            secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
                
                        # the properties below are optional
                        encryption_key_type="encryptionKeyType"
                    ),
                
                    # the properties below are optional
                    media_live_input_arn="mediaLiveInputArn",
                    media_live_pipeline_id="mediaLivePipelineId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__296fe8c5575c6daa0aee10695b4fa916e9cc5d0a13736ad1ed6b81b458d5454e)
                check_type(argname="argument destination_transit_encryption", value=destination_transit_encryption, expected_type=type_hints["destination_transit_encryption"])
                check_type(argname="argument media_live_input_arn", value=media_live_input_arn, expected_type=type_hints["media_live_input_arn"])
                check_type(argname="argument media_live_pipeline_id", value=media_live_pipeline_id, expected_type=type_hints["media_live_pipeline_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_transit_encryption": destination_transit_encryption,
            }
            if media_live_input_arn is not None:
                self._values["media_live_input_arn"] = media_live_input_arn
            if media_live_pipeline_id is not None:
                self._values["media_live_pipeline_id"] = media_live_pipeline_id

        @builtins.property
        def destination_transit_encryption(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MediaLiveTransitEncryptionProperty"]:
            '''The encryption configuration that defines how content is encrypted during transit between MediaConnect Router and MediaLive.

            This configuration determines whether encryption keys are automatically managed by the service or manually managed through AWS Secrets Manager.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-destinationtransitencryption
            '''
            result = self._values.get("destination_transit_encryption")
            assert result is not None, "Required property 'destination_transit_encryption' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MediaLiveTransitEncryptionProperty"], result)

        @builtins.property
        def media_live_input_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the MediaLive input to connect to this router output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-medialiveinputarn
            '''
            result = self._values.get("media_live_input_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def media_live_pipeline_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-medialiveinputrouteroutputconfiguration-medialivepipelineid
            '''
            result = self._values.get("media_live_pipeline_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaLiveInputRouterOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"automatic": "automatic", "secrets_manager": "secretsManager"},
    )
    class MediaLiveTransitEncryptionKeyConfigurationProperty:
        def __init__(
            self,
            *,
            automatic: typing.Any = None,
            secrets_manager: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param automatic: Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.
            :param secrets_manager: The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-medialivetransitencryptionkeyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                media_live_transit_encryption_key_configuration_property = mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty(
                    automatic=automatic,
                    secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__15fd9e770cad7633d1755bc0f3ee7c7619085574f4779ab136bccba68f8b110e)
                check_type(argname="argument automatic", value=automatic, expected_type=type_hints["automatic"])
                check_type(argname="argument secrets_manager", value=secrets_manager, expected_type=type_hints["secrets_manager"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if automatic is not None:
                self._values["automatic"] = automatic
            if secrets_manager is not None:
                self._values["secrets_manager"] = secrets_manager

        @builtins.property
        def automatic(self) -> typing.Any:
            '''Configuration settings for automatic encryption key management, where MediaConnect handles key creation and rotation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-medialivetransitencryptionkeyconfiguration.html#cfn-mediaconnect-routeroutput-medialivetransitencryptionkeyconfiguration-automatic
            '''
            result = self._values.get("automatic")
            return typing.cast(typing.Any, result)

        @builtins.property
        def secrets_manager(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty"]]:
            '''The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-medialivetransitencryptionkeyconfiguration.html#cfn-mediaconnect-routeroutput-medialivetransitencryptionkeyconfiguration-secretsmanager
            '''
            result = self._values.get("secrets_manager")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaLiveTransitEncryptionKeyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_key_configuration": "encryptionKeyConfiguration",
            "encryption_key_type": "encryptionKeyType",
        },
    )
    class MediaLiveTransitEncryptionProperty:
        def __init__(
            self,
            *,
            encryption_key_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            encryption_key_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The encryption configuration that defines how content is encrypted during transit between MediaConnect Router and MediaLive.

            This configuration determines whether encryption keys are automatically managed by the service or manually managed through AWS Secrets Manager.

            :param encryption_key_configuration: Configuration settings for the MediaLive transit encryption key.
            :param encryption_key_type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-medialivetransitencryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                media_live_transit_encryption_property = mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionProperty(
                    encryption_key_configuration=mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty(
                        automatic=automatic,
                        secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
                
                    # the properties below are optional
                    encryption_key_type="encryptionKeyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bca59142eba771d1b11d62bea50d63c8ea9c3e3f701bc82dec8d3053a8e335a9)
                check_type(argname="argument encryption_key_configuration", value=encryption_key_configuration, expected_type=type_hints["encryption_key_configuration"])
                check_type(argname="argument encryption_key_type", value=encryption_key_type, expected_type=type_hints["encryption_key_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_key_configuration": encryption_key_configuration,
            }
            if encryption_key_type is not None:
                self._values["encryption_key_type"] = encryption_key_type

        @builtins.property
        def encryption_key_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty"]:
            '''Configuration settings for the MediaLive transit encryption key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-medialivetransitencryption.html#cfn-mediaconnect-routeroutput-medialivetransitencryption-encryptionkeyconfiguration
            '''
            result = self._values.get("encryption_key_configuration")
            assert result is not None, "Required property 'encryption_key_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty"], result)

        @builtins.property
        def encryption_key_type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-medialivetransitencryption.html#cfn-mediaconnect-routeroutput-medialivetransitencryption-encryptionkeytype
            '''
            result = self._values.get("encryption_key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MediaLiveTransitEncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.PreferredDayTimeMaintenanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"day": "day", "time": "time"},
    )
    class PreferredDayTimeMaintenanceConfigurationProperty:
        def __init__(self, *, day: builtins.str, time: builtins.str) -> None:
            '''Configuration for preferred day and time maintenance settings.

            :param day: 
            :param time: The preferred time for maintenance operations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-preferreddaytimemaintenanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                preferred_day_time_maintenance_configuration_property = mediaconnect.CfnRouterOutput.PreferredDayTimeMaintenanceConfigurationProperty(
                    day="day",
                    time="time"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__06a3dadf828214b14502e7163f28e97ca8eaba7fe6816f85989f565bc4e469d7)
                check_type(argname="argument day", value=day, expected_type=type_hints["day"])
                check_type(argname="argument time", value=time, expected_type=type_hints["time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "day": day,
                "time": time,
            }

        @builtins.property
        def day(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-preferreddaytimemaintenanceconfiguration.html#cfn-mediaconnect-routeroutput-preferreddaytimemaintenanceconfiguration-day
            '''
            result = self._values.get("day")
            assert result is not None, "Required property 'day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time(self) -> builtins.str:
            '''The preferred time for maintenance operations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-preferreddaytimemaintenanceconfiguration.html#cfn-mediaconnect-routeroutput-preferreddaytimemaintenanceconfiguration-time
            '''
            result = self._values.get("time")
            assert result is not None, "Required property 'time' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PreferredDayTimeMaintenanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.RistRouterOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_address": "destinationAddress",
            "destination_port": "destinationPort",
        },
    )
    class RistRouterOutputConfigurationProperty:
        def __init__(
            self,
            *,
            destination_address: builtins.str,
            destination_port: jsii.Number,
        ) -> None:
            '''The configuration settings for a router output using the RIST (Reliable Internet Stream Transport) protocol, including the destination address and port.

            :param destination_address: The destination IP address for the RIST protocol in the router output configuration.
            :param destination_port: The destination port number for the RIST protocol in the router output configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-ristrouteroutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                rist_router_output_configuration_property = mediaconnect.CfnRouterOutput.RistRouterOutputConfigurationProperty(
                    destination_address="destinationAddress",
                    destination_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ae36a4a425b1a376a579bc881963342c2907067c5765e9a309cac9c1792dec7c)
                check_type(argname="argument destination_address", value=destination_address, expected_type=type_hints["destination_address"])
                check_type(argname="argument destination_port", value=destination_port, expected_type=type_hints["destination_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_address": destination_address,
                "destination_port": destination_port,
            }

        @builtins.property
        def destination_address(self) -> builtins.str:
            '''The destination IP address for the RIST protocol in the router output configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-ristrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-ristrouteroutputconfiguration-destinationaddress
            '''
            result = self._values.get("destination_address")
            assert result is not None, "Required property 'destination_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_port(self) -> jsii.Number:
            '''The destination port number for the RIST protocol in the router output configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-ristrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-ristrouteroutputconfiguration-destinationport
            '''
            result = self._values.get("destination_port")
            assert result is not None, "Required property 'destination_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RistRouterOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.RouterOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "media_connect_flow": "mediaConnectFlow",
            "media_live_input": "mediaLiveInput",
            "standard": "standard",
        },
    )
    class RouterOutputConfigurationProperty:
        def __init__(
            self,
            *,
            media_connect_flow: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.MediaConnectFlowRouterOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            media_live_input: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.MediaLiveInputRouterOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            standard: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.StandardRouterOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param media_connect_flow: Configuration settings for connecting a router output to a MediaConnect flow source.
            :param media_live_input: Configuration settings for connecting a router output to a MediaLive input.
            :param standard: The configuration settings for a standard router output, including the protocol, protocol-specific configuration, network interface, and availability zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-routeroutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                # automatic: Any
                
                router_output_configuration_property = mediaconnect.CfnRouterOutput.RouterOutputConfigurationProperty(
                    media_connect_flow=mediaconnect.CfnRouterOutput.MediaConnectFlowRouterOutputConfigurationProperty(
                        destination_transit_encryption=mediaconnect.CfnRouterOutput.FlowTransitEncryptionProperty(
                            encryption_key_configuration=mediaconnect.CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty(
                                automatic=automatic,
                                secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
                
                            # the properties below are optional
                            encryption_key_type="encryptionKeyType"
                        ),
                
                        # the properties below are optional
                        flow_arn="flowArn",
                        flow_source_arn="flowSourceArn"
                    ),
                    media_live_input=mediaconnect.CfnRouterOutput.MediaLiveInputRouterOutputConfigurationProperty(
                        destination_transit_encryption=mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionProperty(
                            encryption_key_configuration=mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty(
                                automatic=automatic,
                                secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
                
                            # the properties below are optional
                            encryption_key_type="encryptionKeyType"
                        ),
                
                        # the properties below are optional
                        media_live_input_arn="mediaLiveInputArn",
                        media_live_pipeline_id="mediaLivePipelineId"
                    ),
                    standard=mediaconnect.CfnRouterOutput.StandardRouterOutputConfigurationProperty(
                        network_interface_arn="networkInterfaceArn",
                        protocol_configuration=mediaconnect.CfnRouterOutput.RouterOutputProtocolConfigurationProperty(
                            rist=mediaconnect.CfnRouterOutput.RistRouterOutputConfigurationProperty(
                                destination_address="destinationAddress",
                                destination_port=123
                            ),
                            rtp=mediaconnect.CfnRouterOutput.RtpRouterOutputConfigurationProperty(
                                destination_address="destinationAddress",
                                destination_port=123,
                
                                # the properties below are optional
                                forward_error_correction="forwardErrorCorrection"
                            ),
                            srt_caller=mediaconnect.CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty(
                                destination_address="destinationAddress",
                                destination_port=123,
                                minimum_latency_milliseconds=123,
                
                                # the properties below are optional
                                encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                ),
                                stream_id="streamId"
                            ),
                            srt_listener=mediaconnect.CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty(
                                minimum_latency_milliseconds=123,
                                port=123,
                
                                # the properties below are optional
                                encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                )
                            )
                        ),
                
                        # the properties below are optional
                        protocol="protocol"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__195e2aba5e342493ec27f8f63f43810db21ee1b303be1cfa962c7f9a490a7d3d)
                check_type(argname="argument media_connect_flow", value=media_connect_flow, expected_type=type_hints["media_connect_flow"])
                check_type(argname="argument media_live_input", value=media_live_input, expected_type=type_hints["media_live_input"])
                check_type(argname="argument standard", value=standard, expected_type=type_hints["standard"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if media_connect_flow is not None:
                self._values["media_connect_flow"] = media_connect_flow
            if media_live_input is not None:
                self._values["media_live_input"] = media_live_input
            if standard is not None:
                self._values["standard"] = standard

        @builtins.property
        def media_connect_flow(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MediaConnectFlowRouterOutputConfigurationProperty"]]:
            '''Configuration settings for connecting a router output to a MediaConnect flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-routeroutputconfiguration.html#cfn-mediaconnect-routeroutput-routeroutputconfiguration-mediaconnectflow
            '''
            result = self._values.get("media_connect_flow")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MediaConnectFlowRouterOutputConfigurationProperty"]], result)

        @builtins.property
        def media_live_input(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MediaLiveInputRouterOutputConfigurationProperty"]]:
            '''Configuration settings for connecting a router output to a MediaLive input.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-routeroutputconfiguration.html#cfn-mediaconnect-routeroutput-routeroutputconfiguration-medialiveinput
            '''
            result = self._values.get("media_live_input")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MediaLiveInputRouterOutputConfigurationProperty"]], result)

        @builtins.property
        def standard(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.StandardRouterOutputConfigurationProperty"]]:
            '''The configuration settings for a standard router output, including the protocol, protocol-specific configuration, network interface, and availability zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-routeroutputconfiguration.html#cfn-mediaconnect-routeroutput-routeroutputconfiguration-standard
            '''
            result = self._values.get("standard")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.StandardRouterOutputConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouterOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.RouterOutputProtocolConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "rist": "rist",
            "rtp": "rtp",
            "srt_caller": "srtCaller",
            "srt_listener": "srtListener",
        },
    )
    class RouterOutputProtocolConfigurationProperty:
        def __init__(
            self,
            *,
            rist: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.RistRouterOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rtp: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.RtpRouterOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            srt_caller: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            srt_listener: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param rist: The configuration settings for a router output using the RIST (Reliable Internet Stream Transport) protocol, including the destination address and port.
            :param rtp: The configuration settings for a router output using the RTP (Real-Time Transport Protocol) protocol, including the destination address and port, and forward error correction state.
            :param srt_caller: The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in caller mode, including the destination address and port, minimum latency, stream ID, and encryption key configuration.
            :param srt_listener: The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and encryption key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                router_output_protocol_configuration_property = mediaconnect.CfnRouterOutput.RouterOutputProtocolConfigurationProperty(
                    rist=mediaconnect.CfnRouterOutput.RistRouterOutputConfigurationProperty(
                        destination_address="destinationAddress",
                        destination_port=123
                    ),
                    rtp=mediaconnect.CfnRouterOutput.RtpRouterOutputConfigurationProperty(
                        destination_address="destinationAddress",
                        destination_port=123,
                
                        # the properties below are optional
                        forward_error_correction="forwardErrorCorrection"
                    ),
                    srt_caller=mediaconnect.CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty(
                        destination_address="destinationAddress",
                        destination_port=123,
                        minimum_latency_milliseconds=123,
                
                        # the properties below are optional
                        encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                            encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        ),
                        stream_id="streamId"
                    ),
                    srt_listener=mediaconnect.CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty(
                        minimum_latency_milliseconds=123,
                        port=123,
                
                        # the properties below are optional
                        encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                            encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                role_arn="roleArn",
                                secret_arn="secretArn"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__562d01ca7d13c69f8bd962654080b4d33fa8642743ff71dd15962ebd61569f3d)
                check_type(argname="argument rist", value=rist, expected_type=type_hints["rist"])
                check_type(argname="argument rtp", value=rtp, expected_type=type_hints["rtp"])
                check_type(argname="argument srt_caller", value=srt_caller, expected_type=type_hints["srt_caller"])
                check_type(argname="argument srt_listener", value=srt_listener, expected_type=type_hints["srt_listener"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if rist is not None:
                self._values["rist"] = rist
            if rtp is not None:
                self._values["rtp"] = rtp
            if srt_caller is not None:
                self._values["srt_caller"] = srt_caller
            if srt_listener is not None:
                self._values["srt_listener"] = srt_listener

        @builtins.property
        def rist(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RistRouterOutputConfigurationProperty"]]:
            '''The configuration settings for a router output using the RIST (Reliable Internet Stream Transport) protocol, including the destination address and port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration.html#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-rist
            '''
            result = self._values.get("rist")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RistRouterOutputConfigurationProperty"]], result)

        @builtins.property
        def rtp(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RtpRouterOutputConfigurationProperty"]]:
            '''The configuration settings for a router output using the RTP (Real-Time Transport Protocol) protocol, including the destination address and port, and forward error correction state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration.html#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-rtp
            '''
            result = self._values.get("rtp")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RtpRouterOutputConfigurationProperty"]], result)

        @builtins.property
        def srt_caller(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty"]]:
            '''The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in caller mode, including the destination address and port, minimum latency, stream ID, and encryption key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration.html#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-srtcaller
            '''
            result = self._values.get("srt_caller")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty"]], result)

        @builtins.property
        def srt_listener(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty"]]:
            '''The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and encryption key configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-routeroutputprotocolconfiguration.html#cfn-mediaconnect-routeroutput-routeroutputprotocolconfiguration-srtlistener
            '''
            result = self._values.get("srt_listener")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouterOutputProtocolConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.RtpRouterOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_address": "destinationAddress",
            "destination_port": "destinationPort",
            "forward_error_correction": "forwardErrorCorrection",
        },
    )
    class RtpRouterOutputConfigurationProperty:
        def __init__(
            self,
            *,
            destination_address: builtins.str,
            destination_port: jsii.Number,
            forward_error_correction: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration settings for a router output using the RTP (Real-Time Transport Protocol) protocol, including the destination address and port, and forward error correction state.

            :param destination_address: The destination IP address for the RTP protocol in the router output configuration.
            :param destination_port: The destination port number for the RTP protocol in the router output configuration.
            :param forward_error_correction: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                rtp_router_output_configuration_property = mediaconnect.CfnRouterOutput.RtpRouterOutputConfigurationProperty(
                    destination_address="destinationAddress",
                    destination_port=123,
                
                    # the properties below are optional
                    forward_error_correction="forwardErrorCorrection"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__979ac0b18bf0bc76a507f9f24868b0ff8e68ab9d4bf73ca30f060372ccbea196)
                check_type(argname="argument destination_address", value=destination_address, expected_type=type_hints["destination_address"])
                check_type(argname="argument destination_port", value=destination_port, expected_type=type_hints["destination_port"])
                check_type(argname="argument forward_error_correction", value=forward_error_correction, expected_type=type_hints["forward_error_correction"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_address": destination_address,
                "destination_port": destination_port,
            }
            if forward_error_correction is not None:
                self._values["forward_error_correction"] = forward_error_correction

        @builtins.property
        def destination_address(self) -> builtins.str:
            '''The destination IP address for the RTP protocol in the router output configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-destinationaddress
            '''
            result = self._values.get("destination_address")
            assert result is not None, "Required property 'destination_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_port(self) -> jsii.Number:
            '''The destination port number for the RTP protocol in the router output configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-destinationport
            '''
            result = self._values.get("destination_port")
            assert result is not None, "Required property 'destination_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def forward_error_correction(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-rtprouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-rtprouteroutputconfiguration-forwarderrorcorrection
            '''
            result = self._values.get("forward_error_correction")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RtpRouterOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"role_arn": "roleArn", "secret_arn": "secretArn"},
    )
    class SecretsManagerEncryptionKeyConfigurationProperty:
        def __init__(self, *, role_arn: builtins.str, secret_arn: builtins.str) -> None:
            '''The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :param role_arn: The ARN of the IAM role assumed by MediaConnect to access the AWS Secrets Manager secret.
            :param secret_arn: The ARN of the AWS Secrets Manager secret used for transit encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-secretsmanagerencryptionkeyconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                secrets_manager_encryption_key_configuration_property = mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__066db337f47042a13b7d50a298df594df0a3bcbe095ae9b4f093e6805b55e954)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "secret_arn": secret_arn,
            }

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARN of the IAM role assumed by MediaConnect to access the AWS Secrets Manager secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-secretsmanagerencryptionkeyconfiguration.html#cfn-mediaconnect-routeroutput-secretsmanagerencryptionkeyconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The ARN of the AWS Secrets Manager secret used for transit encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-secretsmanagerencryptionkeyconfiguration.html#cfn-mediaconnect-routeroutput-secretsmanagerencryptionkeyconfiguration-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretsManagerEncryptionKeyConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_address": "destinationAddress",
            "destination_port": "destinationPort",
            "minimum_latency_milliseconds": "minimumLatencyMilliseconds",
            "encryption_configuration": "encryptionConfiguration",
            "stream_id": "streamId",
        },
    )
    class SrtCallerRouterOutputConfigurationProperty:
        def __init__(
            self,
            *,
            destination_address: builtins.str,
            destination_port: jsii.Number,
            minimum_latency_milliseconds: jsii.Number,
            encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.SrtEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            stream_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in caller mode, including the destination address and port, minimum latency, stream ID, and encryption key configuration.

            :param destination_address: The destination IP address for the SRT protocol in caller mode.
            :param destination_port: The destination port number for the SRT protocol in caller mode.
            :param minimum_latency_milliseconds: The minimum latency in milliseconds for the SRT protocol in caller mode.
            :param encryption_configuration: Contains the configuration settings for encrypting SRT streams, including the encryption key details and encryption parameters.
            :param stream_id: The stream ID for the SRT protocol in caller mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                srt_caller_router_output_configuration_property = mediaconnect.CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty(
                    destination_address="destinationAddress",
                    destination_port=123,
                    minimum_latency_milliseconds=123,
                
                    # the properties below are optional
                    encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                        encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    ),
                    stream_id="streamId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7c3254adaa7e8d0f5267957a6b36ec0a736bd46e05edb0d526175da04f002a94)
                check_type(argname="argument destination_address", value=destination_address, expected_type=type_hints["destination_address"])
                check_type(argname="argument destination_port", value=destination_port, expected_type=type_hints["destination_port"])
                check_type(argname="argument minimum_latency_milliseconds", value=minimum_latency_milliseconds, expected_type=type_hints["minimum_latency_milliseconds"])
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
                check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_address": destination_address,
                "destination_port": destination_port,
                "minimum_latency_milliseconds": minimum_latency_milliseconds,
            }
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration
            if stream_id is not None:
                self._values["stream_id"] = stream_id

        @builtins.property
        def destination_address(self) -> builtins.str:
            '''The destination IP address for the SRT protocol in caller mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-destinationaddress
            '''
            result = self._values.get("destination_address")
            assert result is not None, "Required property 'destination_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_port(self) -> jsii.Number:
            '''The destination port number for the SRT protocol in caller mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-destinationport
            '''
            result = self._values.get("destination_port")
            assert result is not None, "Required property 'destination_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def minimum_latency_milliseconds(self) -> jsii.Number:
            '''The minimum latency in milliseconds for the SRT protocol in caller mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-minimumlatencymilliseconds
            '''
            result = self._values.get("minimum_latency_milliseconds")
            assert result is not None, "Required property 'minimum_latency_milliseconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SrtEncryptionConfigurationProperty"]]:
            '''Contains the configuration settings for encrypting SRT streams, including the encryption key details and encryption parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SrtEncryptionConfigurationProperty"]], result)

        @builtins.property
        def stream_id(self) -> typing.Optional[builtins.str]:
            '''The stream ID for the SRT protocol in caller mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-srtcallerrouteroutputconfiguration-streamid
            '''
            result = self._values.get("stream_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SrtCallerRouterOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"encryption_key": "encryptionKey"},
    )
    class SrtEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_key: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Contains the configuration settings for encrypting SRT streams, including the encryption key details and encryption parameters.

            :param encryption_key: The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                srt_encryption_configuration_property = mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                    encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                        role_arn="roleArn",
                        secret_arn="secretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bd76c0aac777140ccfdcd9b8dde075deccd8b20e8fb2f4ae5c88addc5b54ccef)
                check_type(argname="argument encryption_key", value=encryption_key, expected_type=type_hints["encryption_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_key": encryption_key,
            }

        @builtins.property
        def encryption_key(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty"]:
            '''The configuration settings for transit encryption using AWS Secrets Manager, including the secret ARN and role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtencryptionconfiguration.html#cfn-mediaconnect-routeroutput-srtencryptionconfiguration-encryptionkey
            '''
            result = self._values.get("encryption_key")
            assert result is not None, "Required property 'encryption_key' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SrtEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "minimum_latency_milliseconds": "minimumLatencyMilliseconds",
            "port": "port",
            "encryption_configuration": "encryptionConfiguration",
        },
    )
    class SrtListenerRouterOutputConfigurationProperty:
        def __init__(
            self,
            *,
            minimum_latency_milliseconds: jsii.Number,
            port: jsii.Number,
            encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.SrtEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration settings for a router output using the SRT (Secure Reliable Transport) protocol in listener mode, including the port, minimum latency, and encryption key configuration.

            :param minimum_latency_milliseconds: The minimum latency in milliseconds for the SRT protocol in listener mode.
            :param port: The port number for the SRT protocol in listener mode.
            :param encryption_configuration: Contains the configuration settings for encrypting SRT streams, including the encryption key details and encryption parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                srt_listener_router_output_configuration_property = mediaconnect.CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty(
                    minimum_latency_milliseconds=123,
                    port=123,
                
                    # the properties below are optional
                    encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                        encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                            role_arn="roleArn",
                            secret_arn="secretArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46a504c749dcd4fafe4de2e4d8b321ec6c39bf1a1cb6ef1c43a2b6dbee93549e)
                check_type(argname="argument minimum_latency_milliseconds", value=minimum_latency_milliseconds, expected_type=type_hints["minimum_latency_milliseconds"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "minimum_latency_milliseconds": minimum_latency_milliseconds,
                "port": port,
            }
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration

        @builtins.property
        def minimum_latency_milliseconds(self) -> jsii.Number:
            '''The minimum latency in milliseconds for the SRT protocol in listener mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-minimumlatencymilliseconds
            '''
            result = self._values.get("minimum_latency_milliseconds")
            assert result is not None, "Required property 'minimum_latency_milliseconds' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The port number for the SRT protocol in listener mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SrtEncryptionConfigurationProperty"]]:
            '''Contains the configuration settings for encrypting SRT streams, including the encryption key details and encryption parameters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-srtlistenerrouteroutputconfiguration-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.SrtEncryptionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SrtListenerRouterOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutput.StandardRouterOutputConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "network_interface_arn": "networkInterfaceArn",
            "protocol_configuration": "protocolConfiguration",
            "protocol": "protocol",
        },
    )
    class StandardRouterOutputConfigurationProperty:
        def __init__(
            self,
            *,
            network_interface_arn: builtins.str,
            protocol_configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.RouterOutputProtocolConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            protocol: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration settings for a standard router output, including the protocol, protocol-specific configuration, network interface, and availability zone.

            :param network_interface_arn: The Amazon Resource Name (ARN) of the network interface associated with the standard router output.
            :param protocol_configuration: The protocol configuration settings for a router output.
            :param protocol: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                standard_router_output_configuration_property = mediaconnect.CfnRouterOutput.StandardRouterOutputConfigurationProperty(
                    network_interface_arn="networkInterfaceArn",
                    protocol_configuration=mediaconnect.CfnRouterOutput.RouterOutputProtocolConfigurationProperty(
                        rist=mediaconnect.CfnRouterOutput.RistRouterOutputConfigurationProperty(
                            destination_address="destinationAddress",
                            destination_port=123
                        ),
                        rtp=mediaconnect.CfnRouterOutput.RtpRouterOutputConfigurationProperty(
                            destination_address="destinationAddress",
                            destination_port=123,
                
                            # the properties below are optional
                            forward_error_correction="forwardErrorCorrection"
                        ),
                        srt_caller=mediaconnect.CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty(
                            destination_address="destinationAddress",
                            destination_port=123,
                            minimum_latency_milliseconds=123,
                
                            # the properties below are optional
                            encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
                            stream_id="streamId"
                        ),
                        srt_listener=mediaconnect.CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty(
                            minimum_latency_milliseconds=123,
                            port=123,
                
                            # the properties below are optional
                            encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                                encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            )
                        )
                    ),
                
                    # the properties below are optional
                    protocol="protocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__010befd5e2660537f2f9db5cecf3b56ab325c13eace710cabb8f4ab0cb7d831b)
                check_type(argname="argument network_interface_arn", value=network_interface_arn, expected_type=type_hints["network_interface_arn"])
                check_type(argname="argument protocol_configuration", value=protocol_configuration, expected_type=type_hints["protocol_configuration"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "network_interface_arn": network_interface_arn,
                "protocol_configuration": protocol_configuration,
            }
            if protocol is not None:
                self._values["protocol"] = protocol

        @builtins.property
        def network_interface_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the network interface associated with the standard router output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-networkinterfacearn
            '''
            result = self._values.get("network_interface_arn")
            assert result is not None, "Required property 'network_interface_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol_configuration(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RouterOutputProtocolConfigurationProperty"]:
            '''The protocol configuration settings for a router output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-protocolconfiguration
            '''
            result = self._values.get("protocol_configuration")
            assert result is not None, "Required property 'protocol_configuration' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RouterOutputProtocolConfigurationProperty"], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-routeroutput-standardrouteroutputconfiguration.html#cfn-mediaconnect-routeroutput-standardrouteroutputconfiguration-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StandardRouterOutputConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnRouterOutputProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "maximum_bitrate": "maximumBitrate",
        "name": "name",
        "routing_scope": "routingScope",
        "tier": "tier",
        "availability_zone": "availabilityZone",
        "maintenance_configuration": "maintenanceConfiguration",
        "region_name": "regionName",
        "tags": "tags",
    },
)
class CfnRouterOutputProps:
    def __init__(
        self,
        *,
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.RouterOutputConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        maximum_bitrate: jsii.Number,
        name: builtins.str,
        routing_scope: builtins.str,
        tier: builtins.str,
        availability_zone: typing.Optional[builtins.str] = None,
        maintenance_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnRouterOutput.MaintenanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        region_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRouterOutput``.

        :param configuration: The configuration settings for a router output.
        :param maximum_bitrate: The maximum bitrate for the router output.
        :param name: The name of the router output.
        :param routing_scope: Indicates whether the router output is configured for Regional or global routing.
        :param tier: The tier level of the router output.
        :param availability_zone: The Availability Zone of the router output.
        :param maintenance_configuration: The maintenance configuration settings applied to this router output.
        :param region_name: The AWS Region where the router output is located.
        :param tags: Key-value pairs that can be used to tag and organize this router output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            # automatic: Any
            # default_: Any
            
            cfn_router_output_props = mediaconnect.CfnRouterOutputProps(
                configuration=mediaconnect.CfnRouterOutput.RouterOutputConfigurationProperty(
                    media_connect_flow=mediaconnect.CfnRouterOutput.MediaConnectFlowRouterOutputConfigurationProperty(
                        destination_transit_encryption=mediaconnect.CfnRouterOutput.FlowTransitEncryptionProperty(
                            encryption_key_configuration=mediaconnect.CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty(
                                automatic=automatic,
                                secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
            
                            # the properties below are optional
                            encryption_key_type="encryptionKeyType"
                        ),
            
                        # the properties below are optional
                        flow_arn="flowArn",
                        flow_source_arn="flowSourceArn"
                    ),
                    media_live_input=mediaconnect.CfnRouterOutput.MediaLiveInputRouterOutputConfigurationProperty(
                        destination_transit_encryption=mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionProperty(
                            encryption_key_configuration=mediaconnect.CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty(
                                automatic=automatic,
                                secrets_manager=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                    role_arn="roleArn",
                                    secret_arn="secretArn"
                                )
                            ),
            
                            # the properties below are optional
                            encryption_key_type="encryptionKeyType"
                        ),
            
                        # the properties below are optional
                        media_live_input_arn="mediaLiveInputArn",
                        media_live_pipeline_id="mediaLivePipelineId"
                    ),
                    standard=mediaconnect.CfnRouterOutput.StandardRouterOutputConfigurationProperty(
                        network_interface_arn="networkInterfaceArn",
                        protocol_configuration=mediaconnect.CfnRouterOutput.RouterOutputProtocolConfigurationProperty(
                            rist=mediaconnect.CfnRouterOutput.RistRouterOutputConfigurationProperty(
                                destination_address="destinationAddress",
                                destination_port=123
                            ),
                            rtp=mediaconnect.CfnRouterOutput.RtpRouterOutputConfigurationProperty(
                                destination_address="destinationAddress",
                                destination_port=123,
            
                                # the properties below are optional
                                forward_error_correction="forwardErrorCorrection"
                            ),
                            srt_caller=mediaconnect.CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty(
                                destination_address="destinationAddress",
                                destination_port=123,
                                minimum_latency_milliseconds=123,
            
                                # the properties below are optional
                                encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                ),
                                stream_id="streamId"
                            ),
                            srt_listener=mediaconnect.CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty(
                                minimum_latency_milliseconds=123,
                                port=123,
            
                                # the properties below are optional
                                encryption_configuration=mediaconnect.CfnRouterOutput.SrtEncryptionConfigurationProperty(
                                    encryption_key=mediaconnect.CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty(
                                        role_arn="roleArn",
                                        secret_arn="secretArn"
                                    )
                                )
                            )
                        ),
            
                        # the properties below are optional
                        protocol="protocol"
                    )
                ),
                maximum_bitrate=123,
                name="name",
                routing_scope="routingScope",
                tier="tier",
            
                # the properties below are optional
                availability_zone="availabilityZone",
                maintenance_configuration=mediaconnect.CfnRouterOutput.MaintenanceConfigurationProperty(
                    default=default_,
                    preferred_day_time=mediaconnect.CfnRouterOutput.PreferredDayTimeMaintenanceConfigurationProperty(
                        day="day",
                        time="time"
                    )
                ),
                region_name="regionName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47e40b68b394725a4935bfc1b6ffcf51630ed2e6a0f1075f0c828959594668c7)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument maximum_bitrate", value=maximum_bitrate, expected_type=type_hints["maximum_bitrate"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument routing_scope", value=routing_scope, expected_type=type_hints["routing_scope"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument maintenance_configuration", value=maintenance_configuration, expected_type=type_hints["maintenance_configuration"])
            check_type(argname="argument region_name", value=region_name, expected_type=type_hints["region_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
            "maximum_bitrate": maximum_bitrate,
            "name": name,
            "routing_scope": routing_scope,
            "tier": tier,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if maintenance_configuration is not None:
            self._values["maintenance_configuration"] = maintenance_configuration
        if region_name is not None:
            self._values["region_name"] = region_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RouterOutputConfigurationProperty"]:
        '''The configuration settings for a router output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html#cfn-mediaconnect-routeroutput-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.RouterOutputConfigurationProperty"], result)

    @builtins.property
    def maximum_bitrate(self) -> jsii.Number:
        '''The maximum bitrate for the router output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html#cfn-mediaconnect-routeroutput-maximumbitrate
        '''
        result = self._values.get("maximum_bitrate")
        assert result is not None, "Required property 'maximum_bitrate' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the router output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html#cfn-mediaconnect-routeroutput-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def routing_scope(self) -> builtins.str:
        '''Indicates whether the router output is configured for Regional or global routing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html#cfn-mediaconnect-routeroutput-routingscope
        '''
        result = self._values.get("routing_scope")
        assert result is not None, "Required property 'routing_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tier(self) -> builtins.str:
        '''The tier level of the router output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html#cfn-mediaconnect-routeroutput-tier
        '''
        result = self._values.get("tier")
        assert result is not None, "Required property 'tier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone of the router output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html#cfn-mediaconnect-routeroutput-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MaintenanceConfigurationProperty"]]:
        '''The maintenance configuration settings applied to this router output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html#cfn-mediaconnect-routeroutput-maintenanceconfiguration
        '''
        result = self._values.get("maintenance_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnRouterOutput.MaintenanceConfigurationProperty"]], result)

    @builtins.property
    def region_name(self) -> typing.Optional[builtins.str]:
        '''The AWS Region where the router output is located.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html#cfn-mediaconnect-routeroutput-regionname
        '''
        result = self._values.get("region_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Key-value pairs that can be used to tag and organize this router output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-routeroutput.html#cfn-mediaconnect-routeroutput-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRouterOutputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBridge",
    "CfnBridgeOutput",
    "CfnBridgeOutputProps",
    "CfnBridgeProps",
    "CfnBridgeSource",
    "CfnBridgeSourceProps",
    "CfnFlow",
    "CfnFlowEntitlement",
    "CfnFlowEntitlementProps",
    "CfnFlowOutput",
    "CfnFlowOutputProps",
    "CfnFlowProps",
    "CfnFlowSource",
    "CfnFlowSourceProps",
    "CfnFlowVpcInterface",
    "CfnFlowVpcInterfaceProps",
    "CfnGateway",
    "CfnGatewayProps",
    "CfnRouterInput",
    "CfnRouterInputProps",
    "CfnRouterNetworkInterface",
    "CfnRouterNetworkInterfaceProps",
    "CfnRouterOutput",
    "CfnRouterOutputProps",
]

publication.publish()

def _typecheckingstub__21d1f093ae6c3ef104fbfbb93b13b3338230662ddb218fed6d74e5040acf931c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    placement_arn: builtins.str,
    sources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    egress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.EgressGatewayBridgeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.IngressGatewayBridgeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeOutputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.FailoverConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61c94f5a708599ab90700dbc916f984911d2356933cecac7cb8883e4716ef8e3(
    resource: _IBridgeRef_2f2ab872,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efc0ae85c0d5def613a48526ecb28ec24a692b3f96ffc4f3733d1a84d3727827(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e83409273af3b66857452f9f32805fa3650ea56dd8bccf1a4cae459f1669317(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34788268cca3ef6b9f17b00e64981600b0697ff2af1a873da5b2521e55e8f627(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__897e5b31abf5fb8064d23feda8e8dab6abc8fc04b479fede8ec2f5a8f11283ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c0d91a8143e25d3431f038cc493b72ff78caeb2aae6a8de25ef906162ed203(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c151228d22c29de1b22fb11c72513278ae8b19faf50c26128a49b5bb5cd8231e(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBridge.BridgeSourceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8744f4915b3da8a1fb0b28e71cdd2260912dbea385353bb4a2378a0dcf2e1a19(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.EgressGatewayBridgeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2370206c3aaeddbbe4f170d30b717ce583cd273a4a651e68abaf2042096869bf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.IngressGatewayBridgeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f0f04e00fdc529449b6434bd02be499c861ae34a03215caf6afedaf59974ca0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBridge.BridgeOutputProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a1d3ccb8b1bf31380b43926b18329ad07b95b13cfd50c81dfdcb52ed4700194(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.FailoverConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9a85716cc44ad0d338a783771f76c5420792553cd40338bc48069294fac934(
    *,
    flow_arn: builtins.str,
    name: builtins.str,
    flow_vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__621a738d7654729dd7b3374ce4f5872ae1b369d023ed93a125315923bc53acb5(
    *,
    ip_address: builtins.str,
    name: builtins.str,
    network_name: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    ttl: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1642b43f3173ebc33fe250c935a5af5006fe555caff2d5246139c99d6cfb0d9b(
    *,
    multicast_ip: builtins.str,
    name: builtins.str,
    network_name: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    multicast_source_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.MulticastSourceSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dff659c89b605c1b1a727af90c48784adba90b01104dfd2da4ea33b042b8e12f(
    *,
    network_output: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeNetworkOutputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__048c12dd6c2d1c5e61292ef13f12e16c2c87cce382b5d57ada270cfd08a1b24d(
    *,
    flow_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeFlowSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeNetworkSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b88384d6e7eaf984035fe7a0fba90d12833212086c785ad13a9117af87f05ec0(
    *,
    max_bitrate: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2344e6b90e667c45e503f080b931cc817ed70f01054abb50495f2670d204d2b3(
    *,
    failover_mode: builtins.str,
    source_priority: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.SourcePriorityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__167e9f3b8055cd05eb90612891a377cb4cde612ba7f0ec6b9e69f7d2df6ce8e6(
    *,
    max_bitrate: jsii.Number,
    max_outputs: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e23d21827eb73665886579f4c9de765df4e5ab5b7f9a9d2336b912b8e357707(
    *,
    multicast_source_ip: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ccd453e30991d345c7d1533308b0d3e5827af4b03a42b43534f313026666a0(
    *,
    primary_source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7119bd5cac44e94824a018e0819faa64fdc04125060ad413d57b0a00d0a8066(
    *,
    vpc_interface_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37400ec0d6ede2ac41f09e81db31275470bfb18f7999012a07d588a5abfc45e7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bridge_arn: builtins.str,
    name: builtins.str,
    network_output: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeOutput.BridgeNetworkOutputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc406bff1020285bbe72922bef2d2aefa766c79f162aca8ee2e4a24ff7ff76ef(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb205f08441d39d8e1889501076cfae52006c266e0dcc55675d37bdd36eecce7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dfc4c93ee2ec8174192f41cba8f3d6deeacc3ee4b3eeb41940e9f61c1b8c0a5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__238bd53ec2ae6381eaaf2c652a080561d1722805471e9d898d9d8e2b66530295(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4567364d21ca9ebe1a2f33abcf1e7bc00c0f6b671c2062fd3c6766537faf1fa0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78fe544a540a0346bab7b296adf77b0088521ed5104d3678ee517ee4d8b43eb1(
    value: typing.Union[_IResolvable_da3f097b, CfnBridgeOutput.BridgeNetworkOutputProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c8d614c4eaf3e7a9715a54c7d8f6d68001dfdd34bed46af49b236cf97208c5b(
    *,
    ip_address: builtins.str,
    network_name: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    ttl: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c246f60ce4e5ad45fa8b46aaba3a5dc86b8fbceb04cd700ed6ecc964f18f2a(
    *,
    bridge_arn: builtins.str,
    name: builtins.str,
    network_output: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeOutput.BridgeNetworkOutputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73e5019972892e93be93b465cdd4743483355d6d745af2863fcbd2ab360c88ef(
    *,
    name: builtins.str,
    placement_arn: builtins.str,
    sources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    egress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.EgressGatewayBridgeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.IngressGatewayBridgeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeOutputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.FailoverConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e36e10c04a0f01de7ebc0521a5800daea1daa62e3bd343704ff6e84525f6f408(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bridge_arn: builtins.str,
    name: builtins.str,
    flow_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.BridgeFlowSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.BridgeNetworkSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9c15695da88b46044324b66fa4fc2c80ce78a1c90ef0b5016473957483a3e8(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ee6617fa681b5aaf625fc2493bb4ea5b5e578a01029bdd7ba2b8647be429130(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64ce37bd7d5055cf2fb388e369c965f5e01fd162753e68839b53dd0443911c4b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28bb545b11a59b0c10f19770b49da21586071508bfbed47b6b137ab43e2aaa5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ff480997cae96d755e2b7e83019229c27702f843cafce3fc5647020ec7d7a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9a2d6952ebe510d69e3877d36b01cb4f6aa83e11dfcf61576bdfaffa0dea74(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridgeSource.BridgeFlowSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb1ff783738c431282bcaa0dec602d425b3f5a39195a1f65e4e683ba344caea(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridgeSource.BridgeNetworkSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bb9109e42561a117540865cd31be3adb19651461f90f2af2ac7c6ce75a0c13e(
    *,
    flow_arn: builtins.str,
    flow_vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93b2199f774afbb32a622ba44ca26954c8e46e149f1bc0836b1dda198de28020(
    *,
    multicast_ip: builtins.str,
    network_name: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    multicast_source_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.MulticastSourceSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43fa91d86269952c92522f3e880b2f507aa1cc51cd5dbe28fb9249f61e4324cd(
    *,
    multicast_source_ip: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6d9b48314e46735258c941180d8e92fa25af944c2b991fb6827ccc97fa800b4(
    *,
    vpc_interface_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f2a15e5c2c97898000fd91706ed5ee02d0a7d5d31640d04f545d4db3c27ec23(
    *,
    bridge_arn: builtins.str,
    name: builtins.str,
    flow_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.BridgeFlowSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.BridgeNetworkSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3568a95be2a886825b3db731f10e2fdea8be142c554d1e2055d7e22f5e6a3991(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    availability_zone: typing.Optional[builtins.str] = None,
    flow_size: typing.Optional[builtins.str] = None,
    maintenance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MaintenanceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    media_streams: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MediaStreamProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ndi_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.NdiConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.FailoverConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_monitoring_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceMonitoringConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.VpcInterfaceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c54b3021fd089afdcef76ee7ca3c18274773c4b4384f46a6700f34b567e51aa4(
    resource: _IFlowRef_c5e8f48d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b34fb3378a823873473e36770156bfc974eb22a36bab11daaf47bd382948fda7(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3bf65a3dfd8c719cb8ba7cde45e0dc8693f2306db4dba4cd6da5e4727579cc7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8244ccdcee08a7984c185f2ee476300520ed80658ec1efcbcb9634a230a0687a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b9dd07005f4a1ea040eea97dccca156a16f5e9f3f6686139fbd52108ac4c3b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__869299c75adeb5a7d478686f55b98acba18c279372a76486ab2c6231b1e54e54(
    value: typing.Union[_IResolvable_da3f097b, CfnFlow.SourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843065332a6d7586586605a6ec8a2bd932a36dd6774052d60e5f9fd8e52c280c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18797920a62f69ac5303a95d3356fc95d49473634b7f27d9e7ef811a4ad6cb34(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd188e9c2d5f8f194cf0b4c16e8b355b0ebcec43d953e6b0c8b77128e640aab(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlow.MaintenanceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c580931c160d15b8c0f43f0fe96dc390b640ae81cbc1900b00f369aaa3c3f6e4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFlow.MediaStreamProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f78a65c7535e71bd81a721df5718188077330f02b6d7cdd75ebb5693c7db1cf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlow.NdiConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7deae7edf526ef9a6af2e16b592ef198ecb0cc777d1c7d97f392933ad97ef6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlow.FailoverConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03a0a0b12b76b8e0b7700d38b27d7f2ca928ad701fe5600b9bad475822621b98(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlow.SourceMonitoringConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e75424871a1b67422fa8fe727bf0720abe8ea217c131244844ca71d14e25f4d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFlow.VpcInterfaceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ac15d313eb79141f926e0599cfa8d16a302729713ebc92bf0a1af7adbf56f21(
    *,
    silent_audio: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SilentAudioProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8eed2a01102ad4205f67e0e6efdd3aaeca33633021098b7b3d1d73054d386f3(
    *,
    state: typing.Optional[builtins.str] = None,
    threshold_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__023b62e8b380bcfa878c2a07568bc0d0f9912919827c329972ee2130250892b3(
    *,
    role_arn: builtins.str,
    algorithm: typing.Optional[builtins.str] = None,
    constant_initialization_vector: typing.Optional[builtins.str] = None,
    device_id: typing.Optional[builtins.str] = None,
    key_type: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
    secret_arn: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d936fe41cb44293e591fd7a9b89da19bc9fc2509d0dacf4ad7a22a54e1bae9(
    *,
    failover_mode: typing.Optional[builtins.str] = None,
    recovery_window: typing.Optional[jsii.Number] = None,
    source_priority: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourcePriorityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b52880d31b637a0af3233aa7f316659377893fb1e181334df40136a484a6a792(
    *,
    automatic: typing.Any = None,
    secrets_manager: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SecretsManagerEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ed20d2d2ea0c830d5eb7613de0a9e624da82a886e597f4f6c66d0b5c6c3259f(
    *,
    encryption_key_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.FlowTransitEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    encryption_key_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c34da6d27a4d46f87384739bd6ec7bcc9bf7866bb051703aa63a4b21e8b38dc(
    *,
    channel_order: typing.Optional[builtins.str] = None,
    colorimetry: typing.Optional[builtins.str] = None,
    exact_framerate: typing.Optional[builtins.str] = None,
    par: typing.Optional[builtins.str] = None,
    range: typing.Optional[builtins.str] = None,
    scan_mode: typing.Optional[builtins.str] = None,
    tcs: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__261e148d056da084128b3530c69f370bb4b4b5d73098e06d42eb6c5c4d6025e5(
    *,
    state: typing.Optional[builtins.str] = None,
    threshold_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00bf15dc37f493c33d6b2109cfa6283d2bb14bdc23b0ae4fd75a67ca60084ea8(
    *,
    bridge_arn: builtins.str,
    vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbb4a04e87ed2fedc67d03bbbab23670facee0c55014d0c5d234881ded41ec58(
    *,
    input_port: jsii.Number,
    interface: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.InterfaceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ca0a6498a5e542f31081d78420cae2b37457c94dbd68dcead2dc4af50843b27(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57efc1d88b4fa5a6e6df4c17678237b4420bf63b5cd14e340198e67ed5a1ee60(
    *,
    maintenance_day: builtins.str,
    maintenance_start_hour: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c9c952274e74dd38a0129bccf9e3c8688c812151f95c826ce99e20158cfe87(
    *,
    fmtp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.FmtpProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lang: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc935e241ba7a00b3f70633b9ca54a5bca516c17065e6c6d8eeb7ab2523359be(
    *,
    media_stream_id: jsii.Number,
    media_stream_name: builtins.str,
    media_stream_type: builtins.str,
    attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MediaStreamAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    clock_rate: typing.Optional[jsii.Number] = None,
    description: typing.Optional[builtins.str] = None,
    fmt: typing.Optional[jsii.Number] = None,
    video_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c288224888dcd985ea78c20d06801a00405d4260bf960e8dbcac65f3e669aa4f(
    *,
    encoding_name: builtins.str,
    media_stream_name: builtins.str,
    input_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.InputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69742b949cc5728340bd262c9cb8f8127e5a045369699ab15384d6ad5532a7f7(
    *,
    machine_name: typing.Optional[builtins.str] = None,
    ndi_discovery_servers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.NdiDiscoveryServerConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ndi_state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbd4bce903dd6a95ae93f0b2ca90f98d0d48bb24eebe475acf326160c51d3435(
    *,
    discovery_server_address: builtins.str,
    vpc_interface_adapter: builtins.str,
    discovery_server_port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6448e00f3099cbc8bc0d9c871cb06fad1c988a5fae8ed52ee99e7b4398735c6e(
    *,
    role_arn: builtins.str,
    secret_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e28708aca7aa0aae7b96e1c58983b1ac8f27275c71b78ca026802bea4a53ffd6(
    *,
    state: typing.Optional[builtins.str] = None,
    threshold_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__462b2e03950e94b47455b1cc22dd388c278a29615998512d70aa7513e3c8d698(
    *,
    audio_monitoring_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.AudioMonitoringSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    content_quality_analysis_state: typing.Optional[builtins.str] = None,
    thumbnail_state: typing.Optional[builtins.str] = None,
    video_monitoring_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.VideoMonitoringSettingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a502d8c706596e3abd881dc963357d969893e22e8d25e78085445e09c58ac78b(
    *,
    primary_source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c35ebd36bb52715c021bc299f222a377254ec8a3bd90d9c933fbefcac2bdf0c(
    *,
    decryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    entitlement_arn: typing.Optional[builtins.str] = None,
    gateway_bridge_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.GatewayBridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingest_ip: typing.Optional[builtins.str] = None,
    ingest_port: typing.Optional[jsii.Number] = None,
    max_bitrate: typing.Optional[jsii.Number] = None,
    max_latency: typing.Optional[jsii.Number] = None,
    max_sync_buffer: typing.Optional[jsii.Number] = None,
    media_stream_source_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MediaStreamSourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    min_latency: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    router_integration_state: typing.Optional[builtins.str] = None,
    router_integration_transit_decryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.FlowTransitEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sender_control_port: typing.Optional[jsii.Number] = None,
    sender_ip_address: typing.Optional[builtins.str] = None,
    source_arn: typing.Optional[builtins.str] = None,
    source_ingest_port: typing.Optional[builtins.str] = None,
    source_listener_address: typing.Optional[builtins.str] = None,
    source_listener_port: typing.Optional[jsii.Number] = None,
    stream_id: typing.Optional[builtins.str] = None,
    vpc_interface_name: typing.Optional[builtins.str] = None,
    whitelist_cidr: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b18d7f5756a7359dc9028ca35bdb8d048195959b43a7f2ac5c0f4b71d0b8761(
    *,
    black_frames: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.BlackFramesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    frozen_frames: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.FrozenFramesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__866ca963188936c1dd8965fb722dc7f781261eab36e78ecdb20a9d41b146ef40(
    *,
    vpc_interface_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d976d1dab1b395c0026dcc2152c4dd635ae54d817a1f10c4d8f2725ac4862ad4(
    *,
    name: builtins.str,
    role_arn: builtins.str,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_id: builtins.str,
    network_interface_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    network_interface_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17ecd85086df3a96cb74577c3e3a831ea91a89b617bcd18f7684fd357569ebd4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    flow_arn: builtins.str,
    name: builtins.str,
    subscribers: typing.Sequence[builtins.str],
    data_transfer_subscriber_fee_percent: typing.Optional[jsii.Number] = None,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowEntitlement.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    entitlement_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbbd0b319bddb33c17b2662fae7caf55246f72dd2fa82c3bf38238c549f8a7e4(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc2981b84449358974725cfa5726c974127f55b1d0ed785957f4a1db25fbaf37(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fa54f5d69b72c125e54c71a8aa7a22fc52b087370efdb65ece275ef52b680b8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba5eab3ebe302e351ac5ac0d66029f44599f4749a72395abe65585f0a24955a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e11924d752092913d6e2606c9cde4c9d3a676e93d2cdf59e192e9e6c293bfe35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916ef20a18bd718e63e193a4bfe9a47ef0a3fa7c7d6eb6a74a9f583ad5834eb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ffb421693bf57958756eb013d4d8a721597fcd6b5c4d155ff98a2fc1ee7f4e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__440918e3c472d10f8c3846eeee04790645912cc1f354752fcf74610c24a956dc(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e186a635819e5284e2d58b4d8e7f8c317f8ef3dcaf08d3a66dfe0e4f1b061e89(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowEntitlement.EncryptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdf1b9a179db4ad86ff23860586d83012068ae1abfca84e5defe29f68556a89a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86c4f896040118c2a4fab234e2a7101cc609c650cf5a8c91892db664909f050(
    *,
    algorithm: builtins.str,
    role_arn: builtins.str,
    constant_initialization_vector: typing.Optional[builtins.str] = None,
    device_id: typing.Optional[builtins.str] = None,
    key_type: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
    secret_arn: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7f5911f6dc55c43d6c5bdd5da77a5eb8fb59e8f8418ae5a951a5e0f015b5055(
    *,
    description: builtins.str,
    flow_arn: builtins.str,
    name: builtins.str,
    subscribers: typing.Sequence[builtins.str],
    data_transfer_subscriber_fee_percent: typing.Optional[jsii.Number] = None,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowEntitlement.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    entitlement_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50a855342b002f2aaf180af2a85e45ce23346b4a5b582c00ee1a8474e9dd9bf1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    flow_arn: builtins.str,
    cidr_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    destination: typing.Optional[builtins.str] = None,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_latency: typing.Optional[jsii.Number] = None,
    media_stream_output_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.MediaStreamOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    min_latency: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    ndi_program_name: typing.Optional[builtins.str] = None,
    ndi_speed_hq_quality: typing.Optional[jsii.Number] = None,
    output_status: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[builtins.str] = None,
    remote_id: typing.Optional[builtins.str] = None,
    router_integration_state: typing.Optional[builtins.str] = None,
    router_integration_transit_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.FlowTransitEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    smoothing_latency: typing.Optional[jsii.Number] = None,
    stream_id: typing.Optional[builtins.str] = None,
    vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc12c2292179153951e36b26c5ca33a4865934ab09aaab3ef3247a4db0208245(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f7a6ea2f782501225c570fc34c141a4efdd391bd9340c51c8bd1b59b8a807b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fe52bb8ba629a55d8f6926893cc92e58afb2df918e7d368aeddb04aa5bb1855(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b58a8b918485e48f2bd2cbf5a806a141e4d5ae34f2cf830391b88420333717(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07f3031245a81d1c4e02553eaeb7fc62e38e625e4d2cfe7b7ff3ecce31ce6ef5(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04edd4c6554768eef7ffa49af9bf9fdec351390bdef1d2d14056f7b2afa9b477(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3f2991cc0ce7b9368aefbf86c1373167ce7a90e3225db313dd6d35540907285(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a7a7ea75faea54e857e52b24703069f4dd92643ca1173b27422c3504eee69b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowOutput.EncryptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9801fdc6b598fc4f2e913edc8984f374a7594553b0a1ef32ea0fa7be05bb61db(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99ca24b6208e72328e18819b003e97cbf14fb0f94304256c59924c6e02ae32d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFlowOutput.MediaStreamOutputConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb7401a37f3ff6ff7dc25a56db1a28806074c96fc3f42a6bd90cc4feab9b693(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b750df47b88518fdf7bc5d1baec396797cb9cc3a0c8bdc7742108d9c93c231(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__726c61d1e734fe3825d1f969a727f62f0da47c2684038a9b2dd3b004d823f5a0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce18d034d798847cffb7feeb7c46dad4031db9cee117a778fb30fb59f6e3cde2(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b4c653e5fd4b3a28c65a69d506d6616ef027aa50bccc2d72a02bc2ff7c57c1b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082204a6d2f259b91fea6a581b0aa8a534b0e447853734806818dfa91f967458(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a09f7a6d8ae99d18b6e3bb11284fa5b865ca2146c5efb07536e593ee9a05bc7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f19d4552e8cf70ccb26264cc49b216d391ddef580a3635679d644bda9f8dabf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a92363a82d416caa03ccab5a501ed2d648ae0c5a5733439e18d20b4fab0532be(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32b31733a523757f4557ebb20483d8cac01327485a4f5ee9746929dd058f123d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowOutput.FlowTransitEncryptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a7c12acde851480773f720ab16362e6f6dd272465bbe84d6b60322c1bfd207d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dadac9d58702681fe997f284efaad53e6d5af9dac998dd803277c6ed1ee2a381(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65a3e058407bcf8bd6fa065c9fd3cd66a1c54e7edb3b48af25c7893fd72db21d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowOutput.VpcInterfaceAttachmentProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b62fc10e1fb76cee67ab63dde918a0006c11ce38e8af823e4d2f2770e4d5765(
    *,
    destination_ip: builtins.str,
    destination_port: jsii.Number,
    interface: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.InterfaceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e858c0a050e7b9bf4f84c7f6034ad1cf704a2a9a2b07a5b472d598f1b62d5f(
    *,
    compression_factor: jsii.Number,
    encoder_profile: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12ea6e5693abf5b0e777cf50bd86212ef7db4809c0713169b65c0d055bed2f19(
    *,
    role_arn: builtins.str,
    secret_arn: builtins.str,
    algorithm: typing.Optional[builtins.str] = None,
    key_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__227e17acb559f1129e2d38ac109471667c1611bee1eedb7dec31ff9273ece0c9(
    *,
    automatic: typing.Any = None,
    secrets_manager: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.SecretsManagerEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51ad067d64c5f2d51cca478c548fe0d1bac8cb1160599558be1e0c768ec74342(
    *,
    encryption_key_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.FlowTransitEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    encryption_key_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cc7770548eb391a3e7796f01956da0a9add137c57ab671911bb6c1a675e3dcd(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa5e437983e66807a96f2eedebbdd774906faf99c35e9c25ec0ff0f66c49af3(
    *,
    encoding_name: builtins.str,
    media_stream_name: builtins.str,
    destination_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.DestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    encoding_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.EncodingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__006c867b16e13c1b73b4efbe08794e9b0fe37a42ca38d09660e0ccef770f44f2(
    *,
    role_arn: builtins.str,
    secret_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7072f99adeda4341a6581cacf2975b777cc5b063364d5416156250ca7f1e5619(
    *,
    vpc_interface_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90cee4cbdefa91956af92950bb2bfd2da4fa4f982f439596444cda5251a2c34d(
    *,
    flow_arn: builtins.str,
    cidr_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    destination: typing.Optional[builtins.str] = None,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_latency: typing.Optional[jsii.Number] = None,
    media_stream_output_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.MediaStreamOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    min_latency: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    ndi_program_name: typing.Optional[builtins.str] = None,
    ndi_speed_hq_quality: typing.Optional[jsii.Number] = None,
    output_status: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[builtins.str] = None,
    remote_id: typing.Optional[builtins.str] = None,
    router_integration_state: typing.Optional[builtins.str] = None,
    router_integration_transit_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.FlowTransitEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    smoothing_latency: typing.Optional[jsii.Number] = None,
    stream_id: typing.Optional[builtins.str] = None,
    vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a16a7697723a7ef816aaa9d297ca08cd44085f922995184f8bfdfde65f0c24(
    *,
    name: builtins.str,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    availability_zone: typing.Optional[builtins.str] = None,
    flow_size: typing.Optional[builtins.str] = None,
    maintenance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MaintenanceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    media_streams: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MediaStreamProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ndi_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.NdiConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.FailoverConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_monitoring_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceMonitoringConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_interfaces: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.VpcInterfaceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14359cee01f3506467d65b7510ab8dfc45bad9d560a39ede9f196eb193c6d3f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    name: builtins.str,
    decryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    entitlement_arn: typing.Optional[builtins.str] = None,
    flow_arn: typing.Optional[builtins.str] = None,
    gateway_bridge_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.GatewayBridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingest_port: typing.Optional[jsii.Number] = None,
    max_bitrate: typing.Optional[jsii.Number] = None,
    max_latency: typing.Optional[jsii.Number] = None,
    min_latency: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[builtins.str] = None,
    sender_control_port: typing.Optional[jsii.Number] = None,
    sender_ip_address: typing.Optional[builtins.str] = None,
    source_listener_address: typing.Optional[builtins.str] = None,
    source_listener_port: typing.Optional[jsii.Number] = None,
    stream_id: typing.Optional[builtins.str] = None,
    vpc_interface_name: typing.Optional[builtins.str] = None,
    whitelist_cidr: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__516c9ee96b7a84e3798e10ffbf9f23be95e407b2f0376f64a16b0109b33586e9(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3fd76f8220dae1a8772091086f599345d67d89097d2f85b9307e60f66eebda(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8852c4ff5ee8f7563716bed6f284156dda285971d2136f38033b85a389bd073b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__169574c8d258397d0753838843606fa3a6f2792dbfbe9f805a3263cc2ce8bf99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56248647932d6154f5cc0ea3f1df2a2bb25f298ef25872b32e9b4dd6f8e0ff07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__713d2beba8d5285adfd07ee3f7ca737392fb89294806031a6cc288bb72c8f180(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowSource.EncryptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93ba0fab964dfcf99d0e38ef04172e971ea1753fa1d98e88458675e4386302dc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a393333c9ad7ce002f047c125d9ee3348efa283a66d9def5950529184e3be294(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5cf895711559ebd9f3d9816442bc2258d4ed6f493bb32badf0ea76f038dd16a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowSource.GatewayBridgeSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8065f994df3b6b1f35a330146835da3506ebb87915688c1139a725cf72b5f618(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e362dd143dad56909dafd2e42bfcb4f36d21b914a7b90872305a01bec7758a1f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59ebbbae1ffe64a0b2ace0c589cfc271c5cf5155fb97c05e5866f905264c33c3(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ef8a4669e860fa72d8e2f4dc3ad3fe414a8d53d7156d84af37cde5562fb88d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb57175f10a9dd5a4e263ec48354d53559458e760a13228af2bc8b2d5a738add(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb25d08779ab67d6811a557f48cd15bde00000d84c5ba57f8165f13a3f72f99(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce59a08878045e4b8bc6ff139a2307a1a5d3d8b55ad67c907a140517d9fdee00(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f71f744022b312b3b4bc69179b8e4ce2cdb7fdeb46c179d7c72e3db30ac42e6c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc08edbf9070870e3f4ff641570a5fbe7bd92875ead1c75b9697e32c94084f4f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3b58b86420e937edcb73256eccae2a94f77b56863e967c6b79430f30f5ae00(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaca9be06dd26e302844cbceb849d87c083af662bbe659afe5a1819fd6ac9f7b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45499d5b323bea3d710e7e2165d62c80e1951ab949967a5138abfc7e37f673dc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc2e1b7c07a7a0aadaba7f4f2e0a0214eedc45460e5f4d6b8a4e1af4b33ff561(
    *,
    role_arn: builtins.str,
    algorithm: typing.Optional[builtins.str] = None,
    constant_initialization_vector: typing.Optional[builtins.str] = None,
    device_id: typing.Optional[builtins.str] = None,
    key_type: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
    secret_arn: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30ed56e867002e6d71070cfe3db49514b39a97f4380a7b126282076647a88405(
    *,
    bridge_arn: builtins.str,
    vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f29aa73d1270b98bef9297507fc5368a6213455c4fab06ce82317542ccbecb(
    *,
    vpc_interface_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dd2a850713cccb402475afd88e4c523840081ad6429c6abf35e564ea3f27ca1(
    *,
    description: builtins.str,
    name: builtins.str,
    decryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    entitlement_arn: typing.Optional[builtins.str] = None,
    flow_arn: typing.Optional[builtins.str] = None,
    gateway_bridge_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.GatewayBridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingest_port: typing.Optional[jsii.Number] = None,
    max_bitrate: typing.Optional[jsii.Number] = None,
    max_latency: typing.Optional[jsii.Number] = None,
    min_latency: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[builtins.str] = None,
    sender_control_port: typing.Optional[jsii.Number] = None,
    sender_ip_address: typing.Optional[builtins.str] = None,
    source_listener_address: typing.Optional[builtins.str] = None,
    source_listener_port: typing.Optional[jsii.Number] = None,
    stream_id: typing.Optional[builtins.str] = None,
    vpc_interface_name: typing.Optional[builtins.str] = None,
    whitelist_cidr: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbdfc221c828cffa79a57d6d84dccb050776de58319678209806d7b3bc310582(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    flow_arn: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fa6b7ee310467cbf1b90d72ac662a880ec46f0ff1d93db17be2b22f898219cd(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2669da051110c0f17f8e796d79785f21a3eedb15f26aad564f80d786fc0b5008(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb4bbb0359f95aef0014b12311830a206a9476a44d94de97d750a09771a603ae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01b2ebce5fcf204059015d9ab2acd7dd1255fb422e85ba46d8372e7ed14634e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__315756aca1be9462393133e8a1bd030c6830be9cd62201141209ba92bca00733(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d1a6f274a5840002030ca9431469bb3346277b4320449fb605700060689db4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22fe25e82013a9b0baddbe815abf51918a6107457c49b594041bb09b37e6db29(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ff66cbd4857ab742f4461a355254e9a8da4cf04f8543fbb07ab7e6bde77b87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4407e3345806447ad15e49eb19ee87fc76290919c1ac77d7b46df8daf4909410(
    *,
    flow_arn: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a889ede67aac65e3ba7da8735ec09aa46c53edb047800db832cc8f049ee063d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    egress_cidr_blocks: typing.Sequence[builtins.str],
    name: builtins.str,
    networks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayNetworkProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846fb03e786e5db212456f5e176807bc8fa26425b8fcdcd3acceeb914a80546a(
    resource: _IGatewayRef_4783a0c6,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7afaeb3693b7233ba298147075a68f93109f71fb9d4533fc43cf919f16fe45b(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b19201085d642ad5919470c92f83f2874346dacf31c924443c14fa4ce8557e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__309d2649c79792783a657ac296a1e3f1559ca3d115f8d29a00fcf51ab5b9eea1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c756c6472ede1cbb1eb656c10e07629e0cf818e434b2e8f9c94de41e295b332e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f455f9a25731428a340c77bb14b2965a474f55740a64090450ee7dee16709ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87886ff9eadfa80377e79911ce74141941af595ecff54249e0b94a2aa4f4fdb6(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayNetworkProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f67f020f764410bf45106fcabf15d8329d4bbbd3768cac4cd170ba1032378127(
    *,
    cidr_block: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c57a9fbadb9701c4e8bd3f97f24fe63b6ebd3d8f830d826fedc59b0e40f450(
    *,
    egress_cidr_blocks: typing.Sequence[builtins.str],
    name: builtins.str,
    networks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayNetworkProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fa24b13aaffdcfc1e47f3ced2e884afe1fe974cb91ceb3f0702e3ed196e0855(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    maximum_bitrate: jsii.Number,
    name: builtins.str,
    routing_scope: builtins.str,
    tier: builtins.str,
    availability_zone: typing.Optional[builtins.str] = None,
    maintenance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.MaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    region_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    transit_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RouterInputTransitEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b62b590ea740d308b838213af0b2cd196493374e80cd7c3686bd872b19cfdfeb(
    resource: _IRouterInputRef_6915df50,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bc6c871ed8b6d73be81a2ae1d1e2c9d9b137109612e38abd34e5848294dbc27(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c944fb547e87f295306d8735bbf0eeac4ac8a0b6018a5739d3a31d2e1e718ef6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e30a6d884b369ff6382f442459ba4c11662a15636af2d199fbc1aa1a790ea21(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc19a3af1b324b171b747b68112c85cb261bd6957bab7764b849ca52d9245142(
    value: typing.Union[_IResolvable_da3f097b, CfnRouterInput.RouterInputConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9b9c8e82a356b3f89719f6bbfe30b90040f8129a03f8ce150ad2a8b87ed8246(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cad73940b17fe84f1f0b506b19a2f76e3972f6d1b1a71c747442330ba7cdd4b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00684f4fd383ed48bfa0345b412a77ecbdd623ac32a218fb0294e30e4ed401bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84d00c9475e25cd260ddceb328a82f02a2cb361571f2a5fd671818fb15dd8cd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3dc1a9f3d38364d1ad15584e3cfaccae3ba843735b9a10bd75fa94a9736e60(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c1170f7ba129480fda3e3b9954bf9b3bab26579ad56ca54217519dd369f2de8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRouterInput.MaintenanceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74fded60926c739a4b66f4bd6fdd901f417bee400d49f669f01a8545de0e3052(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a824b54cbbdf5489ae89810bc583b0c20d4cfb25aeb8745e7f408d889b008ac(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b52cf5469dfc840d14b0db5fb2454e8064b964427f444c618452b6c06465337(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRouterInput.RouterInputTransitEncryptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b915443cb98891bf89e968e2338dbbd48e7fc3e6389d7cf5425707945361655(
    *,
    network_interface_arn: builtins.str,
    protocol_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.FailoverRouterInputProtocolConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    source_priority_mode: builtins.str,
    primary_source_index: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f038e6a58a77278305824f4d096d5103bdf9497e022340099fbe631d35cdea(
    *,
    rist: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RistRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rtp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RtpRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    srt_caller: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.SrtCallerRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    srt_listener: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.SrtListenerRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f46fb21f29424f9cdada7e8baeb37950068c69dd5988f39da2d4d57ad111304(
    *,
    automatic: typing.Any = None,
    secrets_manager: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee7cb3dd62027be3aaef58d8e915eab27767b66fa11f87aff2f38eb8e4f62449(
    *,
    encryption_key_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.FlowTransitEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    encryption_key_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a02453ffb5787750cf8b7c68ece86b453aeac195bd6b7a67d442069cdfaf86c1(
    *,
    default: typing.Any = None,
    preferred_day_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.PreferredDayTimeMaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07cd74860f626ccccd2d7b9722c16c895a7f51382af41cc9a3aa3da275bb3b5f(
    *,
    source_transit_decryption: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.FlowTransitEncryptionProperty, typing.Dict[builtins.str, typing.Any]]],
    flow_arn: typing.Optional[builtins.str] = None,
    flow_output_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c207577b6eab68f0d1c3f7593cc0b00c18a7e10d165eed0314d6bcb41a434578(
    *,
    merge_recovery_window_milliseconds: jsii.Number,
    network_interface_arn: builtins.str,
    protocol_configurations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.MergeRouterInputProtocolConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4bff0ea4788435a62555083659b5a3393ff9c2dc3b37396f56d5473c1b65763(
    *,
    rist: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RistRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rtp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RtpRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc21d5c65ee1f7e8a6d879dc6bdeea6e77c637daf5b2e9885e67ec9a9279f8d5(
    *,
    day: builtins.str,
    time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53b65288b7279c56646f36579c820e91edb724a5c19852f9a2b528f0d5893abd(
    *,
    port: jsii.Number,
    recovery_latency_milliseconds: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__367935140f8b2e56d02ff3e2c05252a68073eace6c0eeda3b7abeeeac1209e1b(
    *,
    failover: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.FailoverRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    media_connect_flow: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.MediaConnectFlowRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    merge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.MergeRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    standard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.StandardRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bee2f8b18c83277f36b402b57e84bb58ee2a5352632583caaeb637773d1069c(
    *,
    rist: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RistRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rtp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RtpRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    srt_caller: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.SrtCallerRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    srt_listener: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.SrtListenerRouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcc66546aaf31b61e1efa68ba13e70820ab56b959d9cce333b0e5b3482a1bc09(
    *,
    automatic: typing.Any = None,
    secrets_manager: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85f5061e2ce8c42b22b7dc305382ea9bfa145cf532ef8f62591b3684205d6713(
    *,
    encryption_key_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RouterInputTransitEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    encryption_key_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cb7da58ee58865b37c64051cce4480a789d51b84a87b3f8c0bb5c8c54eaed49(
    *,
    port: jsii.Number,
    forward_error_correction: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__656ecf17b2aa0c4612970c8eb2678158214e80be3a6040146c524608d6fe0ffc(
    *,
    role_arn: builtins.str,
    secret_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beeb94f30bd48ba57793ec4ae9b1de79893c6af67077601ee991d8325f1c1155(
    *,
    minimum_latency_milliseconds: jsii.Number,
    source_address: builtins.str,
    source_port: jsii.Number,
    decryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.SrtDecryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stream_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8e55bc2cc629dfc624dfe6751b96283b3f6c08591aba80e4005288f47ee98a(
    *,
    encryption_key: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.SecretsManagerEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2020f903810fd45bfaa02594fdb1a23bdb3bcc4a9ac870d479f9756284d1f45d(
    *,
    minimum_latency_milliseconds: jsii.Number,
    port: jsii.Number,
    decryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.SrtDecryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95ce52cf6881e0f95e336a6920de1725ead5c20a78c3b050791def2f0629d492(
    *,
    network_interface_arn: builtins.str,
    protocol_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RouterInputProtocolConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__629abd36e1d3f5d9a60304da2c55389ba519de279616eb9eae24baa19310f5f4(
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RouterInputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    maximum_bitrate: jsii.Number,
    name: builtins.str,
    routing_scope: builtins.str,
    tier: builtins.str,
    availability_zone: typing.Optional[builtins.str] = None,
    maintenance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.MaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    region_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    transit_encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterInput.RouterInputTransitEncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24310ca09a20908bd3bbf12dedeae64057a241ad260d0173c063494e94a5e372(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    region_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31cc864547a94937d2c7f541798d2155fb714db7022c9ef5c73db0655c89a985(
    resource: _IRouterNetworkInterfaceRef_05bd061c,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58580bda8f3f828588ff2afcfe7bb604e0dda1e286e8115e82a78cd696a8501c(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99813ca43090ccca654d469e7c1278029c90800fa145e079a4c1a327ab3e09c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4249152775ddcb28eec7583b5299fb11c67a758dbbd05886d4cb11ac3c3cf26(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ada01cdf0843f372e2358efd8825753add57ec0a85c656d8730df8fe11d675f8(
    value: typing.Union[_IResolvable_da3f097b, CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43e368d1cada7b7c423f1301292b045fe35c167df6909c271c310814e384d2f2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__640023b56bd3332877d359f440c6fc815950e5fd32985dc6f11c1892bd7cfaaf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70255a3ae365875252abf102dc0c10255d13f5d5552ee11bd61363fcd195a6d8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86b2b80a7d574588364b855dababd894760b38396c485dd9b78bbd7b36199e16(
    *,
    allow_rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterNetworkInterface.PublicRouterNetworkInterfaceRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b16b6a0a6e17ced0af99bf04d82b87f0ed226b2b3a5459757c42969b81e58901(
    *,
    cidr: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed1657ecdbbe74a0573f76b57267bb3e8bae064809e9330b8325b2050859af13(
    *,
    public: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterNetworkInterface.PublicRouterNetworkInterfaceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterNetworkInterface.VpcRouterNetworkInterfaceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e100934f67ad4ab390b48cc7ed268e9b09228c57ff83fdda79b86e4a8e736125(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c96298441d1fa6afb4e99a0f43137a8859e8ca44045c1e46e91194e38b1ef1c(
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterNetworkInterface.RouterNetworkInterfaceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    region_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0723832b1d0cb17f5bcd9018d140834abd5e94bc96fb3fb67d22f77fb5439c3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.RouterOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    maximum_bitrate: jsii.Number,
    name: builtins.str,
    routing_scope: builtins.str,
    tier: builtins.str,
    availability_zone: typing.Optional[builtins.str] = None,
    maintenance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.MaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    region_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24a2fbac160b0fd704ba7504535f3e38f1a17f7911da11e6a5c0eb4336436bbc(
    resource: _IRouterOutputRef_afa317cd,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76381601efd880f1b3fc396253c86e23a095f42a58d2fdaf834228f3d26a1240(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46c254968a788990028c9b84207c991e7dbd51c1a2e4cd0ceb7a94af8e32e549(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96ef8ccb0c5e0eb94acef4319249f97dfa0ce9d3c9e57dbf2db800211064be5d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f147da00aaf1cdc7014a62b08d8cdc0f9cfce3df5d377973424d2f11377219c(
    value: typing.Union[_IResolvable_da3f097b, CfnRouterOutput.RouterOutputConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6343c02a4b0b9d5d865add8c4d996a26f8389b83b214b7350ac7818a31991557(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4216c7d780d8fb5794084f06923c5c5b6e06951c7c74d95e570b19c17f16c07d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31256d5031051647600a9f3e6d4c7348c96db2131b170cbb3b84d03cb08508d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1241eacdcaad6a0aadee10ac0ca9c13dd7f59cf1e7f5d785c7c1fc63190e220(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b8371a3dd1aa326607abab281477f883dfadb45d27717b05bafb937c2ca7c31(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2d9d66ea8cc6f7fb9f2d963cee39b38487405038346bed562a4282d170af87a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRouterOutput.MaintenanceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f23a2bac43b9e1bd96cf5c900f5ae7d229b5b15428c990a76f5392b3623edc92(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb6937ae740be264a96755b4785a6121ef85f3be99b91fb48ef0d32ab567b808(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2919cc0452cea1b6c29eff661620544fa1903342e65d8def16c87e34ebac3af(
    *,
    automatic: typing.Any = None,
    secrets_manager: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb7cec781c17f5df2ca2950847ce1a86c7e216d13b67c9830306688dd24f423c(
    *,
    encryption_key_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.FlowTransitEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    encryption_key_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3168eb6355c5a713c93dcf1c47b10105621a55ece693c6e8524178049155072b(
    *,
    default: typing.Any = None,
    preferred_day_time: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.PreferredDayTimeMaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c91e97d97b93eb546e4ca89c6248ae26ae42ceadf35a6181ea7b383b55804b49(
    *,
    destination_transit_encryption: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.FlowTransitEncryptionProperty, typing.Dict[builtins.str, typing.Any]]],
    flow_arn: typing.Optional[builtins.str] = None,
    flow_source_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__296fe8c5575c6daa0aee10695b4fa916e9cc5d0a13736ad1ed6b81b458d5454e(
    *,
    destination_transit_encryption: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.MediaLiveTransitEncryptionProperty, typing.Dict[builtins.str, typing.Any]]],
    media_live_input_arn: typing.Optional[builtins.str] = None,
    media_live_pipeline_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15fd9e770cad7633d1755bc0f3ee7c7619085574f4779ab136bccba68f8b110e(
    *,
    automatic: typing.Any = None,
    secrets_manager: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bca59142eba771d1b11d62bea50d63c8ea9c3e3f701bc82dec8d3053a8e335a9(
    *,
    encryption_key_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.MediaLiveTransitEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    encryption_key_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06a3dadf828214b14502e7163f28e97ca8eaba7fe6816f85989f565bc4e469d7(
    *,
    day: builtins.str,
    time: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae36a4a425b1a376a579bc881963342c2907067c5765e9a309cac9c1792dec7c(
    *,
    destination_address: builtins.str,
    destination_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__195e2aba5e342493ec27f8f63f43810db21ee1b303be1cfa962c7f9a490a7d3d(
    *,
    media_connect_flow: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.MediaConnectFlowRouterOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    media_live_input: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.MediaLiveInputRouterOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    standard: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.StandardRouterOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__562d01ca7d13c69f8bd962654080b4d33fa8642743ff71dd15962ebd61569f3d(
    *,
    rist: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.RistRouterOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rtp: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.RtpRouterOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    srt_caller: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.SrtCallerRouterOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    srt_listener: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.SrtListenerRouterOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979ac0b18bf0bc76a507f9f24868b0ff8e68ab9d4bf73ca30f060372ccbea196(
    *,
    destination_address: builtins.str,
    destination_port: jsii.Number,
    forward_error_correction: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__066db337f47042a13b7d50a298df594df0a3bcbe095ae9b4f093e6805b55e954(
    *,
    role_arn: builtins.str,
    secret_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c3254adaa7e8d0f5267957a6b36ec0a736bd46e05edb0d526175da04f002a94(
    *,
    destination_address: builtins.str,
    destination_port: jsii.Number,
    minimum_latency_milliseconds: jsii.Number,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.SrtEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stream_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd76c0aac777140ccfdcd9b8dde075deccd8b20e8fb2f4ae5c88addc5b54ccef(
    *,
    encryption_key: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.SecretsManagerEncryptionKeyConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46a504c749dcd4fafe4de2e4d8b321ec6c39bf1a1cb6ef1c43a2b6dbee93549e(
    *,
    minimum_latency_milliseconds: jsii.Number,
    port: jsii.Number,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.SrtEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__010befd5e2660537f2f9db5cecf3b56ab325c13eace710cabb8f4ab0cb7d831b(
    *,
    network_interface_arn: builtins.str,
    protocol_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.RouterOutputProtocolConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47e40b68b394725a4935bfc1b6ffcf51630ed2e6a0f1075f0c828959594668c7(
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.RouterOutputConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    maximum_bitrate: jsii.Number,
    name: builtins.str,
    routing_scope: builtins.str,
    tier: builtins.str,
    availability_zone: typing.Optional[builtins.str] = None,
    maintenance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouterOutput.MaintenanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    region_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
