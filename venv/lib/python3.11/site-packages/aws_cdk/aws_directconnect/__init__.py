r'''
# AWS::DirectConnect Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_directconnect as directconnect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DirectConnect construct libraries](https://constructs.dev/search?q=directconnect)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DirectConnect resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DirectConnect.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DirectConnect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DirectConnect.html).

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
from ..interfaces.aws_directconnect import (
    ConnectionReference as _ConnectionReference_8d8aa955,
    DirectConnectGatewayAssociationReference as _DirectConnectGatewayAssociationReference_97734978,
    DirectConnectGatewayReference as _DirectConnectGatewayReference_7dc2de35,
    IConnectionRef as _IConnectionRef_63fe92b7,
    IDirectConnectGatewayAssociationRef as _IDirectConnectGatewayAssociationRef_93a3b5e1,
    IDirectConnectGatewayRef as _IDirectConnectGatewayRef_e4e09968,
    ILagRef as _ILagRef_ad81be41,
    IPrivateVirtualInterfaceRef as _IPrivateVirtualInterfaceRef_a98e61e0,
    IPublicVirtualInterfaceRef as _IPublicVirtualInterfaceRef_0fd1f317,
    ITransitVirtualInterfaceRef as _ITransitVirtualInterfaceRef_9c818912,
    LagReference as _LagReference_ed9e2cd2,
    PrivateVirtualInterfaceReference as _PrivateVirtualInterfaceReference_47831550,
    PublicVirtualInterfaceReference as _PublicVirtualInterfaceReference_2cea0598,
    TransitVirtualInterfaceReference as _TransitVirtualInterfaceReference_efcb62ac,
)
from ..interfaces.aws_ec2 import (
    ITransitGatewayRef as _ITransitGatewayRef_1edffe36,
    IVPNGatewayRef as _IVPNGatewayRef_54a7e8d1,
)


@jsii.implements(_IInspectable_c2943556, _IConnectionRef_63fe92b7, _ITaggableV2_4e6798f8)
class CfnConnection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directconnect.CfnConnection",
):
    '''Resource Type definition for AWS::DirectConnect::Connection.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-connection.html
    :cloudformationResource: AWS::DirectConnect::Connection
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directconnect as directconnect
        
        cfn_connection = directconnect.CfnConnection(self, "MyCfnConnection",
            bandwidth="bandwidth",
            connection_name="connectionName",
            location="location",
        
            # the properties below are optional
            lag_id="lagId",
            provider_name="providerName",
            request_mac_sec=False,
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
        bandwidth: builtins.str,
        connection_name: builtins.str,
        location: builtins.str,
        lag_id: typing.Optional[typing.Union[builtins.str, "_ILagRef_ad81be41"]] = None,
        provider_name: typing.Optional[builtins.str] = None,
        request_mac_sec: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DirectConnect::Connection``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bandwidth: The bandwidth of the connection.
        :param connection_name: The name of the connection.
        :param location: The location of the connection.
        :param lag_id: 
        :param provider_name: The name of the service provider associated with the requested connection.
        :param request_mac_sec: Indicates whether you want the connection to support MAC Security (MACsec).
        :param tags: The tags associated with the connection.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abd3e826047cb4f3add3b32f81e0f0d51a366c3420ae204b61e1322264552878)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectionProps(
            bandwidth=bandwidth,
            connection_name=connection_name,
            location=location,
            lag_id=lag_id,
            provider_name=provider_name,
            request_mac_sec=request_mac_sec,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForConnection")
    @builtins.classmethod
    def arn_for_connection(cls, resource: "_IConnectionRef_63fe92b7") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc811b42835421ce0b775a0ef448945f7612f6d663ec68f45052ffe146f739af)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForConnection", [resource]))

    @jsii.member(jsii_name="isCfnConnection")
    @builtins.classmethod
    def is_cfn_connection(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnConnection.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7bc74ef019927b96fcf4a1e828df49db6d129e277ce74ef8cd1337c04d2f59c)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnConnection", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95e48f0564de8b818083771b3c0c5ac940302a8db9319c86e67ac3c1f6570673)
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb36ef03a603aeaadd087cc23147c9f72eac9aeb1d035e9db5bd9580f12bfa66)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionArn")
    def attr_connection_arn(self) -> builtins.str:
        '''The ARN of the connection.

        :cloudformationAttribute: ConnectionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionId")
    def attr_connection_id(self) -> builtins.str:
        '''The ID of the connection.

        :cloudformationAttribute: ConnectionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionId"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionState")
    def attr_connection_state(self) -> builtins.str:
        '''The state of the connection.

        :cloudformationAttribute: ConnectionState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionState"))

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
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "_ConnectionReference_8d8aa955":
        '''A reference to a Connection resource.'''
        return typing.cast("_ConnectionReference_8d8aa955", jsii.get(self, "connectionRef"))

    @builtins.property
    @jsii.member(jsii_name="bandwidth")
    def bandwidth(self) -> builtins.str:
        '''The bandwidth of the connection.'''
        return typing.cast(builtins.str, jsii.get(self, "bandwidth"))

    @bandwidth.setter
    def bandwidth(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2e7f49b3a509e9eab2180d0340be2e045e35ecc946afee8ed2737c59d7453b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bandwidth", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        '''The name of the connection.'''
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @connection_name.setter
    def connection_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e216f63044a3047449997488350c6e2142da6557eb519bb3c3d2834d37b24f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        '''The location of the connection.'''
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfa87ce37b008a9d122d42e4d16dc3838265d4d9a856e01ad831b3f920cda236)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lagId")
    def lag_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lagId"))

    @lag_id.setter
    def lag_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e57a138f92a6b26b88dbc27dcdec303c809669b1720f93a79992da39993d5ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lagId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''The name of the service provider associated with the requested connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerName"))

    @provider_name.setter
    def provider_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89d9beed62c085a97aa40d6e0b1fe180bdffacdf695e658ae6d1d1f75ff104e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="requestMacSec")
    def request_mac_sec(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Indicates whether you want the connection to support MAC Security (MACsec).'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "requestMacSec"))

    @request_mac_sec.setter
    def request_mac_sec(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de3c51aad61f0509ee73f481eb3557b9d725aa29947a78539706e92a04e8a64d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMacSec", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the connection.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f4754aee1d5c0403ec5b4b9c9456d81b46e0922c6cdca103190a7717871d0e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directconnect.CfnConnectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "bandwidth": "bandwidth",
        "connection_name": "connectionName",
        "location": "location",
        "lag_id": "lagId",
        "provider_name": "providerName",
        "request_mac_sec": "requestMacSec",
        "tags": "tags",
    },
)
class CfnConnectionProps:
    def __init__(
        self,
        *,
        bandwidth: builtins.str,
        connection_name: builtins.str,
        location: builtins.str,
        lag_id: typing.Optional[typing.Union[builtins.str, "_ILagRef_ad81be41"]] = None,
        provider_name: typing.Optional[builtins.str] = None,
        request_mac_sec: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnection``.

        :param bandwidth: The bandwidth of the connection.
        :param connection_name: The name of the connection.
        :param location: The location of the connection.
        :param lag_id: 
        :param provider_name: The name of the service provider associated with the requested connection.
        :param request_mac_sec: Indicates whether you want the connection to support MAC Security (MACsec).
        :param tags: The tags associated with the connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-connection.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directconnect as directconnect
            
            cfn_connection_props = directconnect.CfnConnectionProps(
                bandwidth="bandwidth",
                connection_name="connectionName",
                location="location",
            
                # the properties below are optional
                lag_id="lagId",
                provider_name="providerName",
                request_mac_sec=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cef94b4040c7599de15de3fed0380cef62c508ee4f4bfb62a0e9bf146744d326)
            check_type(argname="argument bandwidth", value=bandwidth, expected_type=type_hints["bandwidth"])
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument lag_id", value=lag_id, expected_type=type_hints["lag_id"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument request_mac_sec", value=request_mac_sec, expected_type=type_hints["request_mac_sec"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bandwidth": bandwidth,
            "connection_name": connection_name,
            "location": location,
        }
        if lag_id is not None:
            self._values["lag_id"] = lag_id
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if request_mac_sec is not None:
            self._values["request_mac_sec"] = request_mac_sec
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def bandwidth(self) -> builtins.str:
        '''The bandwidth of the connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-connection.html#cfn-directconnect-connection-bandwidth
        '''
        result = self._values.get("bandwidth")
        assert result is not None, "Required property 'bandwidth' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''The name of the connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-connection.html#cfn-directconnect-connection-connectionname
        '''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The location of the connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-connection.html#cfn-directconnect-connection-location
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lag_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, "_ILagRef_ad81be41"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-connection.html#cfn-directconnect-connection-lagid
        '''
        result = self._values.get("lag_id")
        return typing.cast(typing.Optional[typing.Union[builtins.str, "_ILagRef_ad81be41"]], result)

    @builtins.property
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''The name of the service provider associated with the requested connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-connection.html#cfn-directconnect-connection-providername
        '''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_mac_sec(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Indicates whether you want the connection to support MAC Security (MACsec).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-connection.html#cfn-directconnect-connection-requestmacsec
        '''
        result = self._values.get("request_mac_sec")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-connection.html#cfn-directconnect-connection-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IDirectConnectGatewayRef_e4e09968, _ITaggableV2_4e6798f8)
class CfnDirectConnectGateway(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directconnect.CfnDirectConnectGateway",
):
    '''Resource Type definition for AWS::DirectConnect::DirectConnectGateway.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgateway.html
    :cloudformationResource: AWS::DirectConnect::DirectConnectGateway
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directconnect as directconnect
        
        cfn_direct_connect_gateway = directconnect.CfnDirectConnectGateway(self, "MyCfnDirectConnectGateway",
            direct_connect_gateway_name="directConnectGatewayName",
        
            # the properties below are optional
            amazon_side_asn="amazonSideAsn",
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
        direct_connect_gateway_name: builtins.str,
        amazon_side_asn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DirectConnect::DirectConnectGateway``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param direct_connect_gateway_name: The name of the Direct Connect gateway.
        :param amazon_side_asn: The autonomous system number (ASN) for the Amazon side of the connection.
        :param tags: The tags associated with the Direct Connect gateway.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1615be6a70d3256b8e774756f54d3b4cf912ec766378fb3e8ee821d12e361d8e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDirectConnectGatewayProps(
            direct_connect_gateway_name=direct_connect_gateway_name,
            amazon_side_asn=amazon_side_asn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForDirectConnectGateway")
    @builtins.classmethod
    def arn_for_direct_connect_gateway(
        cls,
        resource: "_IDirectConnectGatewayRef_e4e09968",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeac989b64b6c9e654802d2150c0e71cc5703a83fce5dd0348ab697181c4885e)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForDirectConnectGateway", [resource]))

    @jsii.member(jsii_name="isCfnDirectConnectGateway")
    @builtins.classmethod
    def is_cfn_direct_connect_gateway(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDirectConnectGateway.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88bf54ee18195dc7a8967a7c425f0ba2d37c2a9bf16222bde5b4aef4c0c77585)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDirectConnectGateway", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6f4599f1ad70aac102c5ff274184d302d9a7af0a7037dc65d9493a7250a50ea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cd4fe56d4dca103dacd6de6ee8157cc37d4830b5dea3b62dab0efdc2c8cfa8b8)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDirectConnectGatewayArn")
    def attr_direct_connect_gateway_arn(self) -> builtins.str:
        '''The ARN of the Direct Connect gateway.

        :cloudformationAttribute: DirectConnectGatewayArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDirectConnectGatewayArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDirectConnectGatewayId")
    def attr_direct_connect_gateway_id(self) -> builtins.str:
        '''The ID of the Direct Connect gateway.

        :cloudformationAttribute: DirectConnectGatewayId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDirectConnectGatewayId"))

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
    @jsii.member(jsii_name="directConnectGatewayRef")
    def direct_connect_gateway_ref(self) -> "_DirectConnectGatewayReference_7dc2de35":
        '''A reference to a DirectConnectGateway resource.'''
        return typing.cast("_DirectConnectGatewayReference_7dc2de35", jsii.get(self, "directConnectGatewayRef"))

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayName")
    def direct_connect_gateway_name(self) -> builtins.str:
        '''The name of the Direct Connect gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "directConnectGatewayName"))

    @direct_connect_gateway_name.setter
    def direct_connect_gateway_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__119a3a401444a4f739c5d7eb958461baf9823a5be3f705cb331b7bd20f47a375)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directConnectGatewayName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="amazonSideAsn")
    def amazon_side_asn(self) -> typing.Optional[builtins.str]:
        '''The autonomous system number (ASN) for the Amazon side of the connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amazonSideAsn"))

    @amazon_side_asn.setter
    def amazon_side_asn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa42fe7f405b6fa870f5aa740a26933b9d10caad6a489a5e6e143d06def0f4f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amazonSideAsn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the Direct Connect gateway.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7218e90e3f0ec285cf01b746fdec827917118cd2f14ae196b858db1654c866c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.implements(_IInspectable_c2943556, _IDirectConnectGatewayAssociationRef_93a3b5e1)
class CfnDirectConnectGatewayAssociation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directconnect.CfnDirectConnectGatewayAssociation",
):
    '''Resource Type definition for AWS::DirectConnect::DirectConnectGatewayAssociation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgatewayassociation.html
    :cloudformationResource: AWS::DirectConnect::DirectConnectGatewayAssociation
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directconnect as directconnect
        
        cfn_direct_connect_gateway_association = directconnect.CfnDirectConnectGatewayAssociation(self, "MyCfnDirectConnectGatewayAssociation",
            associated_gateway_id="associatedGatewayId",
            direct_connect_gateway_id="directConnectGatewayId",
        
            # the properties below are optional
            accept_direct_connect_gateway_association_proposal_role_arn="acceptDirectConnectGatewayAssociationProposalRoleArn",
            allowed_prefixes_to_direct_connect_gateway=["allowedPrefixesToDirectConnectGateway"]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        associated_gateway_id: typing.Union[builtins.str, "_ITransitGatewayRef_1edffe36", "_IVPNGatewayRef_54a7e8d1"],
        direct_connect_gateway_id: typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"],
        accept_direct_connect_gateway_association_proposal_role_arn: typing.Optional[builtins.str] = None,
        allowed_prefixes_to_direct_connect_gateway: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::DirectConnect::DirectConnectGatewayAssociation``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param associated_gateway_id: 
        :param direct_connect_gateway_id: 
        :param accept_direct_connect_gateway_association_proposal_role_arn: The Amazon Resource Name (ARN) of the role to accept the Direct Connect Gateway association proposal. Needs directconnect:AcceptDirectConnectGatewayAssociationProposal permissions.
        :param allowed_prefixes_to_direct_connect_gateway: The Amazon VPC prefixes to advertise to the Direct Connect gateway. This parameter is required when you create an association to a transit gateway.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9610c3b37235aa2ee47e7088939e594786d6f4d5693f025059bad085a12dacf6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDirectConnectGatewayAssociationProps(
            associated_gateway_id=associated_gateway_id,
            direct_connect_gateway_id=direct_connect_gateway_id,
            accept_direct_connect_gateway_association_proposal_role_arn=accept_direct_connect_gateway_association_proposal_role_arn,
            allowed_prefixes_to_direct_connect_gateway=allowed_prefixes_to_direct_connect_gateway,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnDirectConnectGatewayAssociation")
    @builtins.classmethod
    def is_cfn_direct_connect_gateway_association(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnDirectConnectGatewayAssociation.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d8e0743a98d958886293e96e4e1e2655dd0ec24bcf2d73ddb4d1ca9d0ee4bb0)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnDirectConnectGatewayAssociation", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f42fd8eed9bf77e08c4a0333fe356f95fb63414699ab51892384bd4c7cd8ff45)
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
            type_hints = typing.get_type_hints(_typecheckingstub__545ac3d037192afa3e02747ab9d0f6b2516376105efeb0ee9599129bb7fc1bed)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociationId")
    def attr_association_id(self) -> builtins.str:
        '''The ID of the Direct Connect gateway association.

        :cloudformationAttribute: AssociationId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAssociationId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayAssociationRef")
    def direct_connect_gateway_association_ref(
        self,
    ) -> "_DirectConnectGatewayAssociationReference_97734978":
        '''A reference to a DirectConnectGatewayAssociation resource.'''
        return typing.cast("_DirectConnectGatewayAssociationReference_97734978", jsii.get(self, "directConnectGatewayAssociationRef"))

    @builtins.property
    @jsii.member(jsii_name="associatedGatewayId")
    def associated_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associatedGatewayId"))

    @associated_gateway_id.setter
    def associated_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad0ad4da945c7888b1cdc557eaad43a19712e50c70eb2a0a0b45721d129656ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associatedGatewayId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayId")
    def direct_connect_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directConnectGatewayId"))

    @direct_connect_gateway_id.setter
    def direct_connect_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b8ceca005e12409044ebdd46c4661d076dc807df321d7c42c9d057bd105450f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directConnectGatewayId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="acceptDirectConnectGatewayAssociationProposalRoleArn")
    def accept_direct_connect_gateway_association_proposal_role_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the role to accept the Direct Connect Gateway association proposal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "acceptDirectConnectGatewayAssociationProposalRoleArn"))

    @accept_direct_connect_gateway_association_proposal_role_arn.setter
    def accept_direct_connect_gateway_association_proposal_role_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c17d25b54f1640987f5c7809c477911de8d79fda8aaa710471ce731c32844bc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptDirectConnectGatewayAssociationProposalRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="allowedPrefixesToDirectConnectGateway")
    def allowed_prefixes_to_direct_connect_gateway(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon VPC prefixes to advertise to the Direct Connect gateway.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedPrefixesToDirectConnectGateway"))

    @allowed_prefixes_to_direct_connect_gateway.setter
    def allowed_prefixes_to_direct_connect_gateway(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd1b070f48f63dd27940fbeb93f973d4627754096548f1aff97cef55c04d544e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedPrefixesToDirectConnectGateway", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directconnect.CfnDirectConnectGatewayAssociationProps",
    jsii_struct_bases=[],
    name_mapping={
        "associated_gateway_id": "associatedGatewayId",
        "direct_connect_gateway_id": "directConnectGatewayId",
        "accept_direct_connect_gateway_association_proposal_role_arn": "acceptDirectConnectGatewayAssociationProposalRoleArn",
        "allowed_prefixes_to_direct_connect_gateway": "allowedPrefixesToDirectConnectGateway",
    },
)
class CfnDirectConnectGatewayAssociationProps:
    def __init__(
        self,
        *,
        associated_gateway_id: typing.Union[builtins.str, "_ITransitGatewayRef_1edffe36", "_IVPNGatewayRef_54a7e8d1"],
        direct_connect_gateway_id: typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"],
        accept_direct_connect_gateway_association_proposal_role_arn: typing.Optional[builtins.str] = None,
        allowed_prefixes_to_direct_connect_gateway: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDirectConnectGatewayAssociation``.

        :param associated_gateway_id: 
        :param direct_connect_gateway_id: 
        :param accept_direct_connect_gateway_association_proposal_role_arn: The Amazon Resource Name (ARN) of the role to accept the Direct Connect Gateway association proposal. Needs directconnect:AcceptDirectConnectGatewayAssociationProposal permissions.
        :param allowed_prefixes_to_direct_connect_gateway: The Amazon VPC prefixes to advertise to the Direct Connect gateway. This parameter is required when you create an association to a transit gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgatewayassociation.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directconnect as directconnect
            
            cfn_direct_connect_gateway_association_props = directconnect.CfnDirectConnectGatewayAssociationProps(
                associated_gateway_id="associatedGatewayId",
                direct_connect_gateway_id="directConnectGatewayId",
            
                # the properties below are optional
                accept_direct_connect_gateway_association_proposal_role_arn="acceptDirectConnectGatewayAssociationProposalRoleArn",
                allowed_prefixes_to_direct_connect_gateway=["allowedPrefixesToDirectConnectGateway"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aba4d505c450c0c0634988995815ecbce3886430a251d53e2e1cea03d00e3dc)
            check_type(argname="argument associated_gateway_id", value=associated_gateway_id, expected_type=type_hints["associated_gateway_id"])
            check_type(argname="argument direct_connect_gateway_id", value=direct_connect_gateway_id, expected_type=type_hints["direct_connect_gateway_id"])
            check_type(argname="argument accept_direct_connect_gateway_association_proposal_role_arn", value=accept_direct_connect_gateway_association_proposal_role_arn, expected_type=type_hints["accept_direct_connect_gateway_association_proposal_role_arn"])
            check_type(argname="argument allowed_prefixes_to_direct_connect_gateway", value=allowed_prefixes_to_direct_connect_gateway, expected_type=type_hints["allowed_prefixes_to_direct_connect_gateway"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "associated_gateway_id": associated_gateway_id,
            "direct_connect_gateway_id": direct_connect_gateway_id,
        }
        if accept_direct_connect_gateway_association_proposal_role_arn is not None:
            self._values["accept_direct_connect_gateway_association_proposal_role_arn"] = accept_direct_connect_gateway_association_proposal_role_arn
        if allowed_prefixes_to_direct_connect_gateway is not None:
            self._values["allowed_prefixes_to_direct_connect_gateway"] = allowed_prefixes_to_direct_connect_gateway

    @builtins.property
    def associated_gateway_id(
        self,
    ) -> typing.Union[builtins.str, "_ITransitGatewayRef_1edffe36", "_IVPNGatewayRef_54a7e8d1"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgatewayassociation.html#cfn-directconnect-directconnectgatewayassociation-associatedgatewayid
        '''
        result = self._values.get("associated_gateway_id")
        assert result is not None, "Required property 'associated_gateway_id' is missing"
        return typing.cast(typing.Union[builtins.str, "_ITransitGatewayRef_1edffe36", "_IVPNGatewayRef_54a7e8d1"], result)

    @builtins.property
    def direct_connect_gateway_id(
        self,
    ) -> typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgatewayassociation.html#cfn-directconnect-directconnectgatewayassociation-directconnectgatewayid
        '''
        result = self._values.get("direct_connect_gateway_id")
        assert result is not None, "Required property 'direct_connect_gateway_id' is missing"
        return typing.cast(typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"], result)

    @builtins.property
    def accept_direct_connect_gateway_association_proposal_role_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the role to accept the Direct Connect Gateway association proposal.

        Needs directconnect:AcceptDirectConnectGatewayAssociationProposal permissions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgatewayassociation.html#cfn-directconnect-directconnectgatewayassociation-acceptdirectconnectgatewayassociationproposalrolearn
        '''
        result = self._values.get("accept_direct_connect_gateway_association_proposal_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def allowed_prefixes_to_direct_connect_gateway(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon VPC prefixes to advertise to the Direct Connect gateway.

        This parameter is required when you create an association to a transit gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgatewayassociation.html#cfn-directconnect-directconnectgatewayassociation-allowedprefixestodirectconnectgateway
        '''
        result = self._values.get("allowed_prefixes_to_direct_connect_gateway")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDirectConnectGatewayAssociationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directconnect.CfnDirectConnectGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "direct_connect_gateway_name": "directConnectGatewayName",
        "amazon_side_asn": "amazonSideAsn",
        "tags": "tags",
    },
)
class CfnDirectConnectGatewayProps:
    def __init__(
        self,
        *,
        direct_connect_gateway_name: builtins.str,
        amazon_side_asn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDirectConnectGateway``.

        :param direct_connect_gateway_name: The name of the Direct Connect gateway.
        :param amazon_side_asn: The autonomous system number (ASN) for the Amazon side of the connection.
        :param tags: The tags associated with the Direct Connect gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgateway.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directconnect as directconnect
            
            cfn_direct_connect_gateway_props = directconnect.CfnDirectConnectGatewayProps(
                direct_connect_gateway_name="directConnectGatewayName",
            
                # the properties below are optional
                amazon_side_asn="amazonSideAsn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d12d0ef664e1585e49496cef753d3714e192674e47da7867d1068f7d108500ca)
            check_type(argname="argument direct_connect_gateway_name", value=direct_connect_gateway_name, expected_type=type_hints["direct_connect_gateway_name"])
            check_type(argname="argument amazon_side_asn", value=amazon_side_asn, expected_type=type_hints["amazon_side_asn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "direct_connect_gateway_name": direct_connect_gateway_name,
        }
        if amazon_side_asn is not None:
            self._values["amazon_side_asn"] = amazon_side_asn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def direct_connect_gateway_name(self) -> builtins.str:
        '''The name of the Direct Connect gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgateway.html#cfn-directconnect-directconnectgateway-directconnectgatewayname
        '''
        result = self._values.get("direct_connect_gateway_name")
        assert result is not None, "Required property 'direct_connect_gateway_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def amazon_side_asn(self) -> typing.Optional[builtins.str]:
        '''The autonomous system number (ASN) for the Amazon side of the connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgateway.html#cfn-directconnect-directconnectgateway-amazonsideasn
        '''
        result = self._values.get("amazon_side_asn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the Direct Connect gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-directconnectgateway.html#cfn-directconnect-directconnectgateway-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDirectConnectGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ILagRef_ad81be41, _ITaggableV2_4e6798f8)
class CfnLag(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directconnect.CfnLag",
):
    '''Resource Type definition for AWS::DirectConnect::Lag.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-lag.html
    :cloudformationResource: AWS::DirectConnect::Lag
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directconnect as directconnect
        
        cfn_lag = directconnect.CfnLag(self, "MyCfnLag",
            connections_bandwidth="connectionsBandwidth",
            lag_name="lagName",
            location="location",
        
            # the properties below are optional
            minimum_links=123,
            provider_name="providerName",
            request_mac_sec=False,
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
        connections_bandwidth: builtins.str,
        lag_name: builtins.str,
        location: builtins.str,
        minimum_links: typing.Optional[jsii.Number] = None,
        provider_name: typing.Optional[builtins.str] = None,
        request_mac_sec: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DirectConnect::Lag``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connections_bandwidth: The bandwidth of the individual physical dedicated connections bundled by the LAG.
        :param lag_name: The name of the LAG.
        :param location: The location for the LAG.
        :param minimum_links: The minimum number of physical dedicated connections that must be operational for the LAG itself to be operational.
        :param provider_name: The name of the service provider associated with the requested LAG.
        :param request_mac_sec: Indicates whether you want the LAG to support MAC Security (MACsec).
        :param tags: The tags associated with the LAG.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71e07e1e973634e160c150954ce8d83214cd17c3957c56543bbea6f5fba0271d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLagProps(
            connections_bandwidth=connections_bandwidth,
            lag_name=lag_name,
            location=location,
            minimum_links=minimum_links,
            provider_name=provider_name,
            request_mac_sec=request_mac_sec,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForLag")
    @builtins.classmethod
    def arn_for_lag(cls, resource: "_ILagRef_ad81be41") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__242c81ea3f73ce5a36d840b7ee19805959188daeef9bd9b0f21a7bbfa1503479)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForLag", [resource]))

    @jsii.member(jsii_name="isCfnLag")
    @builtins.classmethod
    def is_cfn_lag(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnLag.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e303f0ea6e2eacc1eb30b7cd80a76514600efd466e569e9689059172d3ae1a67)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnLag", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb555e87f0f441ba3fe669a7ab2dcc5af52aae255e46489e3ec68b236604d6fa)
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
            type_hints = typing.get_type_hints(_typecheckingstub__84cba34045079c5172b3e91cd8aabdce8e2c0e0fce48380ba3f8cf9546b0708b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLagArn")
    def attr_lag_arn(self) -> builtins.str:
        '''The ARN of the LAG.

        :cloudformationAttribute: LagArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLagArn"))

    @builtins.property
    @jsii.member(jsii_name="attrLagId")
    def attr_lag_id(self) -> builtins.str:
        '''The ID of the LAG.

        :cloudformationAttribute: LagId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLagId"))

    @builtins.property
    @jsii.member(jsii_name="attrLagState")
    def attr_lag_state(self) -> builtins.str:
        '''The state of the LAG.

        :cloudformationAttribute: LagState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLagState"))

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
    @jsii.member(jsii_name="lagRef")
    def lag_ref(self) -> "_LagReference_ed9e2cd2":
        '''A reference to a Lag resource.'''
        return typing.cast("_LagReference_ed9e2cd2", jsii.get(self, "lagRef"))

    @builtins.property
    @jsii.member(jsii_name="connectionsBandwidth")
    def connections_bandwidth(self) -> builtins.str:
        '''The bandwidth of the individual physical dedicated connections bundled by the LAG.'''
        return typing.cast(builtins.str, jsii.get(self, "connectionsBandwidth"))

    @connections_bandwidth.setter
    def connections_bandwidth(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85cc7ef201d327e225d81d2d9169b5d4ad43aba6d15ef11cf93a48722a6bef4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionsBandwidth", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lagName")
    def lag_name(self) -> builtins.str:
        '''The name of the LAG.'''
        return typing.cast(builtins.str, jsii.get(self, "lagName"))

    @lag_name.setter
    def lag_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e83119cc99194ef86f3183056b8345e95c8b2098dd6f9aa00c07f76cde76759b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lagName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        '''The location for the LAG.'''
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96fa230eaf764b1c8371fc8a545f8f8ef8cd02faf385e3185ab98b0deb6d55b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="minimumLinks")
    def minimum_links(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of physical dedicated connections that must be operational for the LAG itself to be operational.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumLinks"))

    @minimum_links.setter
    def minimum_links(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4effe40bac9119e70c74b0ac4bff66dab2ee3fb0c76251442b20e20d2fe1ef0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumLinks", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="providerName")
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''The name of the service provider associated with the requested LAG.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerName"))

    @provider_name.setter
    def provider_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__376203ab16c44d6b6ecb9e3e4280481f8d0549cae91fc05930abcc70c5559687)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="requestMacSec")
    def request_mac_sec(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Indicates whether you want the LAG to support MAC Security (MACsec).'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "requestMacSec"))

    @request_mac_sec.setter
    def request_mac_sec(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7a1a9dd628dda178fd7245c01d6d820f8da7ca508dde21a923653f06fea892c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestMacSec", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the LAG.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7643963ed557c0e7d5eecd7f6d06e89df6563dbbd74e8ea1599569cb94029c99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directconnect.CfnLagProps",
    jsii_struct_bases=[],
    name_mapping={
        "connections_bandwidth": "connectionsBandwidth",
        "lag_name": "lagName",
        "location": "location",
        "minimum_links": "minimumLinks",
        "provider_name": "providerName",
        "request_mac_sec": "requestMacSec",
        "tags": "tags",
    },
)
class CfnLagProps:
    def __init__(
        self,
        *,
        connections_bandwidth: builtins.str,
        lag_name: builtins.str,
        location: builtins.str,
        minimum_links: typing.Optional[jsii.Number] = None,
        provider_name: typing.Optional[builtins.str] = None,
        request_mac_sec: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLag``.

        :param connections_bandwidth: The bandwidth of the individual physical dedicated connections bundled by the LAG.
        :param lag_name: The name of the LAG.
        :param location: The location for the LAG.
        :param minimum_links: The minimum number of physical dedicated connections that must be operational for the LAG itself to be operational.
        :param provider_name: The name of the service provider associated with the requested LAG.
        :param request_mac_sec: Indicates whether you want the LAG to support MAC Security (MACsec).
        :param tags: The tags associated with the LAG.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-lag.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directconnect as directconnect
            
            cfn_lag_props = directconnect.CfnLagProps(
                connections_bandwidth="connectionsBandwidth",
                lag_name="lagName",
                location="location",
            
                # the properties below are optional
                minimum_links=123,
                provider_name="providerName",
                request_mac_sec=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76f90241fc45565e7dbde4fbc117ddc4d00c34343f0ae967573f7940b73137c8)
            check_type(argname="argument connections_bandwidth", value=connections_bandwidth, expected_type=type_hints["connections_bandwidth"])
            check_type(argname="argument lag_name", value=lag_name, expected_type=type_hints["lag_name"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument minimum_links", value=minimum_links, expected_type=type_hints["minimum_links"])
            check_type(argname="argument provider_name", value=provider_name, expected_type=type_hints["provider_name"])
            check_type(argname="argument request_mac_sec", value=request_mac_sec, expected_type=type_hints["request_mac_sec"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connections_bandwidth": connections_bandwidth,
            "lag_name": lag_name,
            "location": location,
        }
        if minimum_links is not None:
            self._values["minimum_links"] = minimum_links
        if provider_name is not None:
            self._values["provider_name"] = provider_name
        if request_mac_sec is not None:
            self._values["request_mac_sec"] = request_mac_sec
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connections_bandwidth(self) -> builtins.str:
        '''The bandwidth of the individual physical dedicated connections bundled by the LAG.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-lag.html#cfn-directconnect-lag-connectionsbandwidth
        '''
        result = self._values.get("connections_bandwidth")
        assert result is not None, "Required property 'connections_bandwidth' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lag_name(self) -> builtins.str:
        '''The name of the LAG.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-lag.html#cfn-directconnect-lag-lagname
        '''
        result = self._values.get("lag_name")
        assert result is not None, "Required property 'lag_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The location for the LAG.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-lag.html#cfn-directconnect-lag-location
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def minimum_links(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of physical dedicated connections that must be operational for the LAG itself to be operational.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-lag.html#cfn-directconnect-lag-minimumlinks
        '''
        result = self._values.get("minimum_links")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def provider_name(self) -> typing.Optional[builtins.str]:
        '''The name of the service provider associated with the requested LAG.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-lag.html#cfn-directconnect-lag-providername
        '''
        result = self._values.get("provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_mac_sec(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Indicates whether you want the LAG to support MAC Security (MACsec).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-lag.html#cfn-directconnect-lag-requestmacsec
        '''
        result = self._values.get("request_mac_sec")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the LAG.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-lag.html#cfn-directconnect-lag-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLagProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IPrivateVirtualInterfaceRef_a98e61e0, _ITaggableV2_4e6798f8)
class CfnPrivateVirtualInterface(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directconnect.CfnPrivateVirtualInterface",
):
    '''Resource Type definition for AWS::DirectConnect::PrivateVirtualInterface.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html
    :cloudformationResource: AWS::DirectConnect::PrivateVirtualInterface
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directconnect as directconnect
        
        cfn_private_virtual_interface = directconnect.CfnPrivateVirtualInterface(self, "MyCfnPrivateVirtualInterface",
            bgp_peers=[directconnect.CfnPrivateVirtualInterface.BgpPeerProperty(
                address_family="addressFamily",
                asn="asn",
        
                # the properties below are optional
                amazon_address="amazonAddress",
                auth_key="authKey",
                bgp_peer_id="bgpPeerId",
                customer_address="customerAddress"
            )],
            connection_id="connectionId",
            virtual_interface_name="virtualInterfaceName",
            vlan=123,
        
            # the properties below are optional
            allocate_private_virtual_interface_role_arn="allocatePrivateVirtualInterfaceRoleArn",
            direct_connect_gateway_id="directConnectGatewayId",
            enable_site_link=False,
            mtu=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            virtual_gateway_id="virtualGatewayId"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        bgp_peers: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPrivateVirtualInterface.BgpPeerProperty", typing.Dict[builtins.str, typing.Any]]]]],
        connection_id: typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"],
        virtual_interface_name: builtins.str,
        vlan: jsii.Number,
        allocate_private_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
        direct_connect_gateway_id: typing.Optional[typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"]] = None,
        enable_site_link: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        mtu: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        virtual_gateway_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::DirectConnect::PrivateVirtualInterface``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bgp_peers: The BGP peers configured on this virtual interface.
        :param connection_id: 
        :param virtual_interface_name: The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
        :param vlan: The ID of the VLAN.
        :param allocate_private_virtual_interface_role_arn: The Amazon Resource Name (ARN) of the role to allocate the private virtual interface. Needs directconnect:AllocatePrivateVirtualInterface permissions and tag permissions if applicable.
        :param direct_connect_gateway_id: 
        :param enable_site_link: Indicates whether to enable or disable SiteLink.
        :param mtu: The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.
        :param tags: The tags associated with the private virtual interface.
        :param virtual_gateway_id: The ID or ARN of the virtual private gateway.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b999bfd5ff244ca66e7bc7c8536b0b41cd03026156da31d75f5336483c8409d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPrivateVirtualInterfaceProps(
            bgp_peers=bgp_peers,
            connection_id=connection_id,
            virtual_interface_name=virtual_interface_name,
            vlan=vlan,
            allocate_private_virtual_interface_role_arn=allocate_private_virtual_interface_role_arn,
            direct_connect_gateway_id=direct_connect_gateway_id,
            enable_site_link=enable_site_link,
            mtu=mtu,
            tags=tags,
            virtual_gateway_id=virtual_gateway_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnPrivateVirtualInterface")
    @builtins.classmethod
    def is_cfn_private_virtual_interface(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnPrivateVirtualInterface.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00bf21163c98fc514b0d82eb2e086c4cb097a375ed76cadebcc4d31d674bee26)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnPrivateVirtualInterface", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__38bfe59b40e5f2cc9fdded02a1abb9dc78bc269081f47ff7a63e690542bab683)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6bd885e0ed5ef6e152ac48182fbc4fad5271712f4ab65bd18fefa214e4b3985f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrVirtualInterfaceArn")
    def attr_virtual_interface_arn(self) -> builtins.str:
        '''The ID of the virtual interface.

        :cloudformationAttribute: VirtualInterfaceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualInterfaceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVirtualInterfaceId")
    def attr_virtual_interface_id(self) -> builtins.str:
        '''The ID of the virtual interface.

        :cloudformationAttribute: VirtualInterfaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualInterfaceId"))

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
    @jsii.member(jsii_name="privateVirtualInterfaceRef")
    def private_virtual_interface_ref(
        self,
    ) -> "_PrivateVirtualInterfaceReference_47831550":
        '''A reference to a PrivateVirtualInterface resource.'''
        return typing.cast("_PrivateVirtualInterfaceReference_47831550", jsii.get(self, "privateVirtualInterfaceRef"))

    @builtins.property
    @jsii.member(jsii_name="bgpPeers")
    def bgp_peers(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPrivateVirtualInterface.BgpPeerProperty"]]]:
        '''The BGP peers configured on this virtual interface.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPrivateVirtualInterface.BgpPeerProperty"]]], jsii.get(self, "bgpPeers"))

    @bgp_peers.setter
    def bgp_peers(
        self,
        value: typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPrivateVirtualInterface.BgpPeerProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a377f3dc38cfdfcfbb888a8194c187841a1ffdf0187a8b1a9fb7944019ca7650)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgpPeers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41eecff3bb92985ba75103960b7f55da43a9af0be5f254c382fda4106f0f0550)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="virtualInterfaceName")
    def virtual_interface_name(self) -> builtins.str:
        '''The name of the virtual interface assigned by the customer network.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualInterfaceName"))

    @virtual_interface_name.setter
    def virtual_interface_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af2652fdc0950ee77258f3161aacdeadf450794286361020dc461d4ee6a849b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualInterfaceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vlan")
    def vlan(self) -> jsii.Number:
        '''The ID of the VLAN.'''
        return typing.cast(jsii.Number, jsii.get(self, "vlan"))

    @vlan.setter
    def vlan(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7be0f3eb45e2d56a69509393435a0c9c889408be16f96dbb8151c115cdaaf32)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vlan", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="allocatePrivateVirtualInterfaceRoleArn")
    def allocate_private_virtual_interface_role_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the role to allocate the private virtual interface.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocatePrivateVirtualInterfaceRoleArn"))

    @allocate_private_virtual_interface_role_arn.setter
    def allocate_private_virtual_interface_role_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc2ac054c23a5452fce570bc81a80994c8e147459879c7de51393c0f63a16879)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocatePrivateVirtualInterfaceRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayId")
    def direct_connect_gateway_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directConnectGatewayId"))

    @direct_connect_gateway_id.setter
    def direct_connect_gateway_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d78b40e3a07653fbdb507c846d981a976cbff848d1febdc2cc43309729bd4348)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directConnectGatewayId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableSiteLink")
    def enable_site_link(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Indicates whether to enable or disable SiteLink.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "enableSiteLink"))

    @enable_site_link.setter
    def enable_site_link(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__901ddf3550f52d20f3db06493d53d33da7d865d1a2fa5e207ae907cb1cae6d8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSiteLink", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mtu")
    def mtu(self) -> typing.Optional[jsii.Number]:
        '''The maximum transmission unit (MTU), in bytes.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mtu"))

    @mtu.setter
    def mtu(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ed96ea2147f833a590e8cb859e1264fdc9a4fd816c38bdb7de360223dd7e2ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mtu", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the private virtual interface.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb6b73505c5342ad306f9886d5bff4e132c15676d4f2e45fcbe415b72ed035bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="virtualGatewayId")
    def virtual_gateway_id(self) -> typing.Optional[builtins.str]:
        '''The ID or ARN of the virtual private gateway.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "virtualGatewayId"))

    @virtual_gateway_id.setter
    def virtual_gateway_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23f80a4087ac6f3310be4fb0275b69ad615c5d64db1d6f947c5a22a628b95a3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualGatewayId", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_directconnect.CfnPrivateVirtualInterface.BgpPeerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address_family": "addressFamily",
            "asn": "asn",
            "amazon_address": "amazonAddress",
            "auth_key": "authKey",
            "bgp_peer_id": "bgpPeerId",
            "customer_address": "customerAddress",
        },
    )
    class BgpPeerProperty:
        def __init__(
            self,
            *,
            address_family: builtins.str,
            asn: builtins.str,
            amazon_address: typing.Optional[builtins.str] = None,
            auth_key: typing.Optional[builtins.str] = None,
            bgp_peer_id: typing.Optional[builtins.str] = None,
            customer_address: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a BGP peer.

            :param address_family: The address family for the BGP peer.
            :param asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            :param amazon_address: The IP address assigned to the Amazon interface.
            :param auth_key: The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximum length of 80 characters.
            :param bgp_peer_id: 
            :param customer_address: The IP address assigned to the customer interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-privatevirtualinterface-bgppeer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_directconnect as directconnect
                
                bgp_peer_property = directconnect.CfnPrivateVirtualInterface.BgpPeerProperty(
                    address_family="addressFamily",
                    asn="asn",
                
                    # the properties below are optional
                    amazon_address="amazonAddress",
                    auth_key="authKey",
                    bgp_peer_id="bgpPeerId",
                    customer_address="customerAddress"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__497e11bdb89ebeb1deee774b538b67dcf4e0efe42bdbf5015631df088a809dac)
                check_type(argname="argument address_family", value=address_family, expected_type=type_hints["address_family"])
                check_type(argname="argument asn", value=asn, expected_type=type_hints["asn"])
                check_type(argname="argument amazon_address", value=amazon_address, expected_type=type_hints["amazon_address"])
                check_type(argname="argument auth_key", value=auth_key, expected_type=type_hints["auth_key"])
                check_type(argname="argument bgp_peer_id", value=bgp_peer_id, expected_type=type_hints["bgp_peer_id"])
                check_type(argname="argument customer_address", value=customer_address, expected_type=type_hints["customer_address"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "address_family": address_family,
                "asn": asn,
            }
            if amazon_address is not None:
                self._values["amazon_address"] = amazon_address
            if auth_key is not None:
                self._values["auth_key"] = auth_key
            if bgp_peer_id is not None:
                self._values["bgp_peer_id"] = bgp_peer_id
            if customer_address is not None:
                self._values["customer_address"] = customer_address

        @builtins.property
        def address_family(self) -> builtins.str:
            '''The address family for the BGP peer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-privatevirtualinterface-bgppeer.html#cfn-directconnect-privatevirtualinterface-bgppeer-addressfamily
            '''
            result = self._values.get("address_family")
            assert result is not None, "Required property 'address_family' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def asn(self) -> builtins.str:
            '''The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-privatevirtualinterface-bgppeer.html#cfn-directconnect-privatevirtualinterface-bgppeer-asn
            '''
            result = self._values.get("asn")
            assert result is not None, "Required property 'asn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def amazon_address(self) -> typing.Optional[builtins.str]:
            '''The IP address assigned to the Amazon interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-privatevirtualinterface-bgppeer.html#cfn-directconnect-privatevirtualinterface-bgppeer-amazonaddress
            '''
            result = self._values.get("amazon_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_key(self) -> typing.Optional[builtins.str]:
            '''The authentication key for BGP configuration.

            This string has a minimum length of 6 characters and and a maximum length of 80 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-privatevirtualinterface-bgppeer.html#cfn-directconnect-privatevirtualinterface-bgppeer-authkey
            '''
            result = self._values.get("auth_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bgp_peer_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-privatevirtualinterface-bgppeer.html#cfn-directconnect-privatevirtualinterface-bgppeer-bgppeerid
            '''
            result = self._values.get("bgp_peer_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def customer_address(self) -> typing.Optional[builtins.str]:
            '''The IP address assigned to the customer interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-privatevirtualinterface-bgppeer.html#cfn-directconnect-privatevirtualinterface-bgppeer-customeraddress
            '''
            result = self._values.get("customer_address")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BgpPeerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directconnect.CfnPrivateVirtualInterfaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "bgp_peers": "bgpPeers",
        "connection_id": "connectionId",
        "virtual_interface_name": "virtualInterfaceName",
        "vlan": "vlan",
        "allocate_private_virtual_interface_role_arn": "allocatePrivateVirtualInterfaceRoleArn",
        "direct_connect_gateway_id": "directConnectGatewayId",
        "enable_site_link": "enableSiteLink",
        "mtu": "mtu",
        "tags": "tags",
        "virtual_gateway_id": "virtualGatewayId",
    },
)
class CfnPrivateVirtualInterfaceProps:
    def __init__(
        self,
        *,
        bgp_peers: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPrivateVirtualInterface.BgpPeerProperty", typing.Dict[builtins.str, typing.Any]]]]],
        connection_id: typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"],
        virtual_interface_name: builtins.str,
        vlan: jsii.Number,
        allocate_private_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
        direct_connect_gateway_id: typing.Optional[typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"]] = None,
        enable_site_link: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        mtu: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        virtual_gateway_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPrivateVirtualInterface``.

        :param bgp_peers: The BGP peers configured on this virtual interface.
        :param connection_id: 
        :param virtual_interface_name: The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
        :param vlan: The ID of the VLAN.
        :param allocate_private_virtual_interface_role_arn: The Amazon Resource Name (ARN) of the role to allocate the private virtual interface. Needs directconnect:AllocatePrivateVirtualInterface permissions and tag permissions if applicable.
        :param direct_connect_gateway_id: 
        :param enable_site_link: Indicates whether to enable or disable SiteLink.
        :param mtu: The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.
        :param tags: The tags associated with the private virtual interface.
        :param virtual_gateway_id: The ID or ARN of the virtual private gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directconnect as directconnect
            
            cfn_private_virtual_interface_props = directconnect.CfnPrivateVirtualInterfaceProps(
                bgp_peers=[directconnect.CfnPrivateVirtualInterface.BgpPeerProperty(
                    address_family="addressFamily",
                    asn="asn",
            
                    # the properties below are optional
                    amazon_address="amazonAddress",
                    auth_key="authKey",
                    bgp_peer_id="bgpPeerId",
                    customer_address="customerAddress"
                )],
                connection_id="connectionId",
                virtual_interface_name="virtualInterfaceName",
                vlan=123,
            
                # the properties below are optional
                allocate_private_virtual_interface_role_arn="allocatePrivateVirtualInterfaceRoleArn",
                direct_connect_gateway_id="directConnectGatewayId",
                enable_site_link=False,
                mtu=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                virtual_gateway_id="virtualGatewayId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4235226dc710b191f689dc9cfba93959927dfea6356ec9f8e5e5a4a4924acec4)
            check_type(argname="argument bgp_peers", value=bgp_peers, expected_type=type_hints["bgp_peers"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument virtual_interface_name", value=virtual_interface_name, expected_type=type_hints["virtual_interface_name"])
            check_type(argname="argument vlan", value=vlan, expected_type=type_hints["vlan"])
            check_type(argname="argument allocate_private_virtual_interface_role_arn", value=allocate_private_virtual_interface_role_arn, expected_type=type_hints["allocate_private_virtual_interface_role_arn"])
            check_type(argname="argument direct_connect_gateway_id", value=direct_connect_gateway_id, expected_type=type_hints["direct_connect_gateway_id"])
            check_type(argname="argument enable_site_link", value=enable_site_link, expected_type=type_hints["enable_site_link"])
            check_type(argname="argument mtu", value=mtu, expected_type=type_hints["mtu"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument virtual_gateway_id", value=virtual_gateway_id, expected_type=type_hints["virtual_gateway_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bgp_peers": bgp_peers,
            "connection_id": connection_id,
            "virtual_interface_name": virtual_interface_name,
            "vlan": vlan,
        }
        if allocate_private_virtual_interface_role_arn is not None:
            self._values["allocate_private_virtual_interface_role_arn"] = allocate_private_virtual_interface_role_arn
        if direct_connect_gateway_id is not None:
            self._values["direct_connect_gateway_id"] = direct_connect_gateway_id
        if enable_site_link is not None:
            self._values["enable_site_link"] = enable_site_link
        if mtu is not None:
            self._values["mtu"] = mtu
        if tags is not None:
            self._values["tags"] = tags
        if virtual_gateway_id is not None:
            self._values["virtual_gateway_id"] = virtual_gateway_id

    @builtins.property
    def bgp_peers(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPrivateVirtualInterface.BgpPeerProperty"]]]:
        '''The BGP peers configured on this virtual interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html#cfn-directconnect-privatevirtualinterface-bgppeers
        '''
        result = self._values.get("bgp_peers")
        assert result is not None, "Required property 'bgp_peers' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPrivateVirtualInterface.BgpPeerProperty"]]], result)

    @builtins.property
    def connection_id(
        self,
    ) -> typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html#cfn-directconnect-privatevirtualinterface-connectionid
        '''
        result = self._values.get("connection_id")
        assert result is not None, "Required property 'connection_id' is missing"
        return typing.cast(typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"], result)

    @builtins.property
    def virtual_interface_name(self) -> builtins.str:
        '''The name of the virtual interface assigned by the customer network.

        The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html#cfn-directconnect-privatevirtualinterface-virtualinterfacename
        '''
        result = self._values.get("virtual_interface_name")
        assert result is not None, "Required property 'virtual_interface_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vlan(self) -> jsii.Number:
        '''The ID of the VLAN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html#cfn-directconnect-privatevirtualinterface-vlan
        '''
        result = self._values.get("vlan")
        assert result is not None, "Required property 'vlan' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def allocate_private_virtual_interface_role_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the role to allocate the private virtual interface.

        Needs directconnect:AllocatePrivateVirtualInterface permissions and tag permissions if applicable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html#cfn-directconnect-privatevirtualinterface-allocateprivatevirtualinterfacerolearn
        '''
        result = self._values.get("allocate_private_virtual_interface_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def direct_connect_gateway_id(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html#cfn-directconnect-privatevirtualinterface-directconnectgatewayid
        '''
        result = self._values.get("direct_connect_gateway_id")
        return typing.cast(typing.Optional[typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"]], result)

    @builtins.property
    def enable_site_link(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Indicates whether to enable or disable SiteLink.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html#cfn-directconnect-privatevirtualinterface-enablesitelink
        '''
        result = self._values.get("enable_site_link")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def mtu(self) -> typing.Optional[jsii.Number]:
        '''The maximum transmission unit (MTU), in bytes.

        The supported values are 1500 and 9001. The default value is 1500.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html#cfn-directconnect-privatevirtualinterface-mtu
        '''
        result = self._values.get("mtu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the private virtual interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html#cfn-directconnect-privatevirtualinterface-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def virtual_gateway_id(self) -> typing.Optional[builtins.str]:
        '''The ID or ARN of the virtual private gateway.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-privatevirtualinterface.html#cfn-directconnect-privatevirtualinterface-virtualgatewayid
        '''
        result = self._values.get("virtual_gateway_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPrivateVirtualInterfaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IPublicVirtualInterfaceRef_0fd1f317, _ITaggableV2_4e6798f8)
class CfnPublicVirtualInterface(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directconnect.CfnPublicVirtualInterface",
):
    '''Resource Type definition for AWS::DirectConnect::PublicVirtualInterface.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-publicvirtualinterface.html
    :cloudformationResource: AWS::DirectConnect::PublicVirtualInterface
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directconnect as directconnect
        
        cfn_public_virtual_interface = directconnect.CfnPublicVirtualInterface(self, "MyCfnPublicVirtualInterface",
            bgp_peers=[directconnect.CfnPublicVirtualInterface.BgpPeerProperty(
                address_family="addressFamily",
                asn="asn",
        
                # the properties below are optional
                amazon_address="amazonAddress",
                auth_key="authKey",
                bgp_peer_id="bgpPeerId",
                customer_address="customerAddress"
            )],
            connection_id="connectionId",
            virtual_interface_name="virtualInterfaceName",
            vlan=123,
        
            # the properties below are optional
            allocate_public_virtual_interface_role_arn="allocatePublicVirtualInterfaceRoleArn",
            route_filter_prefixes=["routeFilterPrefixes"],
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
        bgp_peers: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPublicVirtualInterface.BgpPeerProperty", typing.Dict[builtins.str, typing.Any]]]]],
        connection_id: typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"],
        virtual_interface_name: builtins.str,
        vlan: jsii.Number,
        allocate_public_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
        route_filter_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DirectConnect::PublicVirtualInterface``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bgp_peers: The BGP peers configured on this virtual interface.
        :param connection_id: 
        :param virtual_interface_name: The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
        :param vlan: The ID of the VLAN.
        :param allocate_public_virtual_interface_role_arn: The Amazon Resource Name (ARN) of the role to allocate the public virtual interface. Needs directconnect:AllocatePublicVirtualInterface permissions and tag permissions if applicable.
        :param route_filter_prefixes: The routes to be advertised to the AWS network in this region.
        :param tags: The tags associated with the public virtual interface.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb624942469eb4c46619a6a53b66f8eefaefb7869b75206e9cc0f6ecfe9c4686)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPublicVirtualInterfaceProps(
            bgp_peers=bgp_peers,
            connection_id=connection_id,
            virtual_interface_name=virtual_interface_name,
            vlan=vlan,
            allocate_public_virtual_interface_role_arn=allocate_public_virtual_interface_role_arn,
            route_filter_prefixes=route_filter_prefixes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnPublicVirtualInterface")
    @builtins.classmethod
    def is_cfn_public_virtual_interface(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnPublicVirtualInterface.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39a0d3a556867f13de687ec0219611d8afed4ca5a46dde9755d8595545c79cda)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnPublicVirtualInterface", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f532504cdf995bfc683e973211df2172c108b3d15efe62bed7c5470f79849fb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f1fee6b61972a50e0775b498e7174cbbbdca7dfdd9e3caa58b90de29b3bd661f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrVirtualInterfaceArn")
    def attr_virtual_interface_arn(self) -> builtins.str:
        '''The ARN of the virtual interface.

        :cloudformationAttribute: VirtualInterfaceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualInterfaceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVirtualInterfaceId")
    def attr_virtual_interface_id(self) -> builtins.str:
        '''The ID of the virtual interface.

        :cloudformationAttribute: VirtualInterfaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualInterfaceId"))

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
    @jsii.member(jsii_name="publicVirtualInterfaceRef")
    def public_virtual_interface_ref(
        self,
    ) -> "_PublicVirtualInterfaceReference_2cea0598":
        '''A reference to a PublicVirtualInterface resource.'''
        return typing.cast("_PublicVirtualInterfaceReference_2cea0598", jsii.get(self, "publicVirtualInterfaceRef"))

    @builtins.property
    @jsii.member(jsii_name="bgpPeers")
    def bgp_peers(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPublicVirtualInterface.BgpPeerProperty"]]]:
        '''The BGP peers configured on this virtual interface.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPublicVirtualInterface.BgpPeerProperty"]]], jsii.get(self, "bgpPeers"))

    @bgp_peers.setter
    def bgp_peers(
        self,
        value: typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPublicVirtualInterface.BgpPeerProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f44cde981a81e7ffa5693c513087f99e0bb137b4e6cb13c5ad826be9dbdf109)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgpPeers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d39b2e691dc81f2913cc829d97b4f3df45cd3685edd8e3cd9deddc45abdb4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="virtualInterfaceName")
    def virtual_interface_name(self) -> builtins.str:
        '''The name of the virtual interface assigned by the customer network.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualInterfaceName"))

    @virtual_interface_name.setter
    def virtual_interface_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f2a73cc5dc053ed58e9ac6baf4f2f62c72804fcf71ff3673a1c3a521109fb93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualInterfaceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vlan")
    def vlan(self) -> jsii.Number:
        '''The ID of the VLAN.'''
        return typing.cast(jsii.Number, jsii.get(self, "vlan"))

    @vlan.setter
    def vlan(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2b555240297573629e6980f8443995cc7ef32715fdc6a5278208d552fa7560a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vlan", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="allocatePublicVirtualInterfaceRoleArn")
    def allocate_public_virtual_interface_role_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the role to allocate the public virtual interface.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocatePublicVirtualInterfaceRoleArn"))

    @allocate_public_virtual_interface_role_arn.setter
    def allocate_public_virtual_interface_role_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57043a41fced754517b9e33f9547d38de18424e15989706839ddcab948060ded)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocatePublicVirtualInterfaceRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="routeFilterPrefixes")
    def route_filter_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The routes to be advertised to the AWS network in this region.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "routeFilterPrefixes"))

    @route_filter_prefixes.setter
    def route_filter_prefixes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a470793a5aed4e3f78d1bba8a0be22800607924bdad3e6ea09f9a68136db3f8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeFilterPrefixes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the public virtual interface.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c53c8d59a5a9e38b1ef03554805949bdd64f4c7567b7742dfbaa892c79ea5880)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_directconnect.CfnPublicVirtualInterface.BgpPeerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address_family": "addressFamily",
            "asn": "asn",
            "amazon_address": "amazonAddress",
            "auth_key": "authKey",
            "bgp_peer_id": "bgpPeerId",
            "customer_address": "customerAddress",
        },
    )
    class BgpPeerProperty:
        def __init__(
            self,
            *,
            address_family: builtins.str,
            asn: builtins.str,
            amazon_address: typing.Optional[builtins.str] = None,
            auth_key: typing.Optional[builtins.str] = None,
            bgp_peer_id: typing.Optional[builtins.str] = None,
            customer_address: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a BGP peer.

            :param address_family: The address family for the BGP peer.
            :param asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            :param amazon_address: The IP address assigned to the Amazon interface.
            :param auth_key: The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximum length of 80 characters.
            :param bgp_peer_id: 
            :param customer_address: The IP address assigned to the customer interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-publicvirtualinterface-bgppeer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_directconnect as directconnect
                
                bgp_peer_property = directconnect.CfnPublicVirtualInterface.BgpPeerProperty(
                    address_family="addressFamily",
                    asn="asn",
                
                    # the properties below are optional
                    amazon_address="amazonAddress",
                    auth_key="authKey",
                    bgp_peer_id="bgpPeerId",
                    customer_address="customerAddress"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76cbced85c2e693501bdf352afdf52f270e01694a49b284d6059a89d4d38f72a)
                check_type(argname="argument address_family", value=address_family, expected_type=type_hints["address_family"])
                check_type(argname="argument asn", value=asn, expected_type=type_hints["asn"])
                check_type(argname="argument amazon_address", value=amazon_address, expected_type=type_hints["amazon_address"])
                check_type(argname="argument auth_key", value=auth_key, expected_type=type_hints["auth_key"])
                check_type(argname="argument bgp_peer_id", value=bgp_peer_id, expected_type=type_hints["bgp_peer_id"])
                check_type(argname="argument customer_address", value=customer_address, expected_type=type_hints["customer_address"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "address_family": address_family,
                "asn": asn,
            }
            if amazon_address is not None:
                self._values["amazon_address"] = amazon_address
            if auth_key is not None:
                self._values["auth_key"] = auth_key
            if bgp_peer_id is not None:
                self._values["bgp_peer_id"] = bgp_peer_id
            if customer_address is not None:
                self._values["customer_address"] = customer_address

        @builtins.property
        def address_family(self) -> builtins.str:
            '''The address family for the BGP peer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-publicvirtualinterface-bgppeer.html#cfn-directconnect-publicvirtualinterface-bgppeer-addressfamily
            '''
            result = self._values.get("address_family")
            assert result is not None, "Required property 'address_family' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def asn(self) -> builtins.str:
            '''The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-publicvirtualinterface-bgppeer.html#cfn-directconnect-publicvirtualinterface-bgppeer-asn
            '''
            result = self._values.get("asn")
            assert result is not None, "Required property 'asn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def amazon_address(self) -> typing.Optional[builtins.str]:
            '''The IP address assigned to the Amazon interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-publicvirtualinterface-bgppeer.html#cfn-directconnect-publicvirtualinterface-bgppeer-amazonaddress
            '''
            result = self._values.get("amazon_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_key(self) -> typing.Optional[builtins.str]:
            '''The authentication key for BGP configuration.

            This string has a minimum length of 6 characters and and a maximum length of 80 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-publicvirtualinterface-bgppeer.html#cfn-directconnect-publicvirtualinterface-bgppeer-authkey
            '''
            result = self._values.get("auth_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bgp_peer_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-publicvirtualinterface-bgppeer.html#cfn-directconnect-publicvirtualinterface-bgppeer-bgppeerid
            '''
            result = self._values.get("bgp_peer_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def customer_address(self) -> typing.Optional[builtins.str]:
            '''The IP address assigned to the customer interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-publicvirtualinterface-bgppeer.html#cfn-directconnect-publicvirtualinterface-bgppeer-customeraddress
            '''
            result = self._values.get("customer_address")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BgpPeerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directconnect.CfnPublicVirtualInterfaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "bgp_peers": "bgpPeers",
        "connection_id": "connectionId",
        "virtual_interface_name": "virtualInterfaceName",
        "vlan": "vlan",
        "allocate_public_virtual_interface_role_arn": "allocatePublicVirtualInterfaceRoleArn",
        "route_filter_prefixes": "routeFilterPrefixes",
        "tags": "tags",
    },
)
class CfnPublicVirtualInterfaceProps:
    def __init__(
        self,
        *,
        bgp_peers: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnPublicVirtualInterface.BgpPeerProperty", typing.Dict[builtins.str, typing.Any]]]]],
        connection_id: typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"],
        virtual_interface_name: builtins.str,
        vlan: jsii.Number,
        allocate_public_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
        route_filter_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPublicVirtualInterface``.

        :param bgp_peers: The BGP peers configured on this virtual interface.
        :param connection_id: 
        :param virtual_interface_name: The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
        :param vlan: The ID of the VLAN.
        :param allocate_public_virtual_interface_role_arn: The Amazon Resource Name (ARN) of the role to allocate the public virtual interface. Needs directconnect:AllocatePublicVirtualInterface permissions and tag permissions if applicable.
        :param route_filter_prefixes: The routes to be advertised to the AWS network in this region.
        :param tags: The tags associated with the public virtual interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-publicvirtualinterface.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directconnect as directconnect
            
            cfn_public_virtual_interface_props = directconnect.CfnPublicVirtualInterfaceProps(
                bgp_peers=[directconnect.CfnPublicVirtualInterface.BgpPeerProperty(
                    address_family="addressFamily",
                    asn="asn",
            
                    # the properties below are optional
                    amazon_address="amazonAddress",
                    auth_key="authKey",
                    bgp_peer_id="bgpPeerId",
                    customer_address="customerAddress"
                )],
                connection_id="connectionId",
                virtual_interface_name="virtualInterfaceName",
                vlan=123,
            
                # the properties below are optional
                allocate_public_virtual_interface_role_arn="allocatePublicVirtualInterfaceRoleArn",
                route_filter_prefixes=["routeFilterPrefixes"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90c6271856e4af9b71018ea29afa7c5c6b15f873ee9d157717f75a62759db624)
            check_type(argname="argument bgp_peers", value=bgp_peers, expected_type=type_hints["bgp_peers"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument virtual_interface_name", value=virtual_interface_name, expected_type=type_hints["virtual_interface_name"])
            check_type(argname="argument vlan", value=vlan, expected_type=type_hints["vlan"])
            check_type(argname="argument allocate_public_virtual_interface_role_arn", value=allocate_public_virtual_interface_role_arn, expected_type=type_hints["allocate_public_virtual_interface_role_arn"])
            check_type(argname="argument route_filter_prefixes", value=route_filter_prefixes, expected_type=type_hints["route_filter_prefixes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bgp_peers": bgp_peers,
            "connection_id": connection_id,
            "virtual_interface_name": virtual_interface_name,
            "vlan": vlan,
        }
        if allocate_public_virtual_interface_role_arn is not None:
            self._values["allocate_public_virtual_interface_role_arn"] = allocate_public_virtual_interface_role_arn
        if route_filter_prefixes is not None:
            self._values["route_filter_prefixes"] = route_filter_prefixes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def bgp_peers(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPublicVirtualInterface.BgpPeerProperty"]]]:
        '''The BGP peers configured on this virtual interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-publicvirtualinterface.html#cfn-directconnect-publicvirtualinterface-bgppeers
        '''
        result = self._values.get("bgp_peers")
        assert result is not None, "Required property 'bgp_peers' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnPublicVirtualInterface.BgpPeerProperty"]]], result)

    @builtins.property
    def connection_id(
        self,
    ) -> typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-publicvirtualinterface.html#cfn-directconnect-publicvirtualinterface-connectionid
        '''
        result = self._values.get("connection_id")
        assert result is not None, "Required property 'connection_id' is missing"
        return typing.cast(typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"], result)

    @builtins.property
    def virtual_interface_name(self) -> builtins.str:
        '''The name of the virtual interface assigned by the customer network.

        The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-publicvirtualinterface.html#cfn-directconnect-publicvirtualinterface-virtualinterfacename
        '''
        result = self._values.get("virtual_interface_name")
        assert result is not None, "Required property 'virtual_interface_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vlan(self) -> jsii.Number:
        '''The ID of the VLAN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-publicvirtualinterface.html#cfn-directconnect-publicvirtualinterface-vlan
        '''
        result = self._values.get("vlan")
        assert result is not None, "Required property 'vlan' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def allocate_public_virtual_interface_role_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the role to allocate the public virtual interface.

        Needs directconnect:AllocatePublicVirtualInterface permissions and tag permissions if applicable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-publicvirtualinterface.html#cfn-directconnect-publicvirtualinterface-allocatepublicvirtualinterfacerolearn
        '''
        result = self._values.get("allocate_public_virtual_interface_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_filter_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The routes to be advertised to the AWS network in this region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-publicvirtualinterface.html#cfn-directconnect-publicvirtualinterface-routefilterprefixes
        '''
        result = self._values.get("route_filter_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the public virtual interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-publicvirtualinterface.html#cfn-directconnect-publicvirtualinterface-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPublicVirtualInterfaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITransitVirtualInterfaceRef_9c818912, _ITaggableV2_4e6798f8)
class CfnTransitVirtualInterface(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_directconnect.CfnTransitVirtualInterface",
):
    '''Resource Type definition for AWS::DirectConnect::TransitVirtualInterface.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html
    :cloudformationResource: AWS::DirectConnect::TransitVirtualInterface
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_directconnect as directconnect
        
        cfn_transit_virtual_interface = directconnect.CfnTransitVirtualInterface(self, "MyCfnTransitVirtualInterface",
            bgp_peers=[directconnect.CfnTransitVirtualInterface.BgpPeerProperty(
                address_family="addressFamily",
                asn="asn",
        
                # the properties below are optional
                amazon_address="amazonAddress",
                auth_key="authKey",
                bgp_peer_id="bgpPeerId",
                customer_address="customerAddress"
            )],
            connection_id="connectionId",
            direct_connect_gateway_id="directConnectGatewayId",
            virtual_interface_name="virtualInterfaceName",
            vlan=123,
        
            # the properties below are optional
            allocate_transit_virtual_interface_role_arn="allocateTransitVirtualInterfaceRoleArn",
            enable_site_link=False,
            mtu=123,
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
        bgp_peers: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTransitVirtualInterface.BgpPeerProperty", typing.Dict[builtins.str, typing.Any]]]]],
        connection_id: typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"],
        direct_connect_gateway_id: typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"],
        virtual_interface_name: builtins.str,
        vlan: jsii.Number,
        allocate_transit_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
        enable_site_link: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        mtu: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::DirectConnect::TransitVirtualInterface``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bgp_peers: The BGP peers configured on this virtual interface..
        :param connection_id: 
        :param direct_connect_gateway_id: 
        :param virtual_interface_name: The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
        :param vlan: The ID of the VLAN.
        :param allocate_transit_virtual_interface_role_arn: The Amazon Resource Name (ARN) of the role to allocate the TransitVifAllocation. Needs directconnect:AllocateTransitVirtualInterface permissions and tag permissions if applicable.
        :param enable_site_link: Indicates whether to enable or disable SiteLink.
        :param mtu: The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.
        :param tags: The tags associated with the private virtual interface.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8457181aefda9690d8c418796e9a515a2e66c5ac47ef49f5bc5009c032225092)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTransitVirtualInterfaceProps(
            bgp_peers=bgp_peers,
            connection_id=connection_id,
            direct_connect_gateway_id=direct_connect_gateway_id,
            virtual_interface_name=virtual_interface_name,
            vlan=vlan,
            allocate_transit_virtual_interface_role_arn=allocate_transit_virtual_interface_role_arn,
            enable_site_link=enable_site_link,
            mtu=mtu,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnTransitVirtualInterface")
    @builtins.classmethod
    def is_cfn_transit_virtual_interface(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnTransitVirtualInterface.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7a6aa3d436db57a05a0f9c69a735b36148e8fe79e5a1924ba21377a694a1e1e)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnTransitVirtualInterface", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f20090e74737b5107ec03ba9190842e3f80d15942d16324fd95ed298b7759185)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a922b83142d09b492418483facac0563f872463a354b375553098b5e1092a64c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrVirtualInterfaceArn")
    def attr_virtual_interface_arn(self) -> builtins.str:
        '''The ARN of the virtual interface.

        :cloudformationAttribute: VirtualInterfaceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualInterfaceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVirtualInterfaceId")
    def attr_virtual_interface_id(self) -> builtins.str:
        '''The ID of the virtual interface.

        :cloudformationAttribute: VirtualInterfaceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVirtualInterfaceId"))

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
    @jsii.member(jsii_name="transitVirtualInterfaceRef")
    def transit_virtual_interface_ref(
        self,
    ) -> "_TransitVirtualInterfaceReference_efcb62ac":
        '''A reference to a TransitVirtualInterface resource.'''
        return typing.cast("_TransitVirtualInterfaceReference_efcb62ac", jsii.get(self, "transitVirtualInterfaceRef"))

    @builtins.property
    @jsii.member(jsii_name="bgpPeers")
    def bgp_peers(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTransitVirtualInterface.BgpPeerProperty"]]]:
        '''The BGP peers configured on this virtual interface..'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTransitVirtualInterface.BgpPeerProperty"]]], jsii.get(self, "bgpPeers"))

    @bgp_peers.setter
    def bgp_peers(
        self,
        value: typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTransitVirtualInterface.BgpPeerProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3b9b304e783af9090d2ec707f39cd5d1a2b81e550a8b21bebe0eb5a21ecac36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bgpPeers", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4ccfc04a3c912c34568a6a5720e015f1825b8219ba97f86a5ebb55a652bcf15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="directConnectGatewayId")
    def direct_connect_gateway_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directConnectGatewayId"))

    @direct_connect_gateway_id.setter
    def direct_connect_gateway_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3617cad06aea221ec06776b7dce786c2f2df66985f8406d81f7d4ac3d9b9a99a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directConnectGatewayId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="virtualInterfaceName")
    def virtual_interface_name(self) -> builtins.str:
        '''The name of the virtual interface assigned by the customer network.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualInterfaceName"))

    @virtual_interface_name.setter
    def virtual_interface_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bed18506fa2829afe14ed93e9974de1505dcc9a3b2b6ddae81716856407c5747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualInterfaceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vlan")
    def vlan(self) -> jsii.Number:
        '''The ID of the VLAN.'''
        return typing.cast(jsii.Number, jsii.get(self, "vlan"))

    @vlan.setter
    def vlan(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c3d955f7f3495d5127ff7429ea26623c64b18712014f01657aeed28c33c81fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vlan", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="allocateTransitVirtualInterfaceRoleArn")
    def allocate_transit_virtual_interface_role_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the role to allocate the TransitVifAllocation.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "allocateTransitVirtualInterfaceRoleArn"))

    @allocate_transit_virtual_interface_role_arn.setter
    def allocate_transit_virtual_interface_role_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a124137823eef4be92b8af8eb63b635385f95a2985d7a63c460405f25ed0bc3f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocateTransitVirtualInterfaceRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="enableSiteLink")
    def enable_site_link(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Indicates whether to enable or disable SiteLink.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], jsii.get(self, "enableSiteLink"))

    @enable_site_link.setter
    def enable_site_link(
        self,
        value: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e03280b75ba0f770370d14184a3abe6d0ba0f8b6df43840d4d9976c87d5f034d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSiteLink", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="mtu")
    def mtu(self) -> typing.Optional[jsii.Number]:
        '''The maximum transmission unit (MTU), in bytes.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "mtu"))

    @mtu.setter
    def mtu(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d19784da4e32c6ec4fe08fbf8f5821561fcb9deaa0adf75925b256d14d9076d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mtu", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the private virtual interface.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84a469d82380a2c77aa1e6129aec6e66170b2e4285400f743b393d509e744c2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_directconnect.CfnTransitVirtualInterface.BgpPeerProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address_family": "addressFamily",
            "asn": "asn",
            "amazon_address": "amazonAddress",
            "auth_key": "authKey",
            "bgp_peer_id": "bgpPeerId",
            "customer_address": "customerAddress",
        },
    )
    class BgpPeerProperty:
        def __init__(
            self,
            *,
            address_family: builtins.str,
            asn: builtins.str,
            amazon_address: typing.Optional[builtins.str] = None,
            auth_key: typing.Optional[builtins.str] = None,
            bgp_peer_id: typing.Optional[builtins.str] = None,
            customer_address: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A key-value pair to associate with a resource.

            :param address_family: The address family for the BGP peer.
            :param asn: The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.
            :param amazon_address: The IP address assigned to the Amazon interface.
            :param auth_key: The authentication key for BGP configuration. This string has a minimum length of 6 characters and and a maximum length of 80 characters.
            :param bgp_peer_id: 
            :param customer_address: The IP address assigned to the customer interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-transitvirtualinterface-bgppeer.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_directconnect as directconnect
                
                bgp_peer_property = directconnect.CfnTransitVirtualInterface.BgpPeerProperty(
                    address_family="addressFamily",
                    asn="asn",
                
                    # the properties below are optional
                    amazon_address="amazonAddress",
                    auth_key="authKey",
                    bgp_peer_id="bgpPeerId",
                    customer_address="customerAddress"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__86175311c426d11df4ae41f4f060bb07d2e554ddb0e944f5628a45df53003c50)
                check_type(argname="argument address_family", value=address_family, expected_type=type_hints["address_family"])
                check_type(argname="argument asn", value=asn, expected_type=type_hints["asn"])
                check_type(argname="argument amazon_address", value=amazon_address, expected_type=type_hints["amazon_address"])
                check_type(argname="argument auth_key", value=auth_key, expected_type=type_hints["auth_key"])
                check_type(argname="argument bgp_peer_id", value=bgp_peer_id, expected_type=type_hints["bgp_peer_id"])
                check_type(argname="argument customer_address", value=customer_address, expected_type=type_hints["customer_address"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "address_family": address_family,
                "asn": asn,
            }
            if amazon_address is not None:
                self._values["amazon_address"] = amazon_address
            if auth_key is not None:
                self._values["auth_key"] = auth_key
            if bgp_peer_id is not None:
                self._values["bgp_peer_id"] = bgp_peer_id
            if customer_address is not None:
                self._values["customer_address"] = customer_address

        @builtins.property
        def address_family(self) -> builtins.str:
            '''The address family for the BGP peer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-transitvirtualinterface-bgppeer.html#cfn-directconnect-transitvirtualinterface-bgppeer-addressfamily
            '''
            result = self._values.get("address_family")
            assert result is not None, "Required property 'address_family' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def asn(self) -> builtins.str:
            '''The autonomous system (AS) number for Border Gateway Protocol (BGP) configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-transitvirtualinterface-bgppeer.html#cfn-directconnect-transitvirtualinterface-bgppeer-asn
            '''
            result = self._values.get("asn")
            assert result is not None, "Required property 'asn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def amazon_address(self) -> typing.Optional[builtins.str]:
            '''The IP address assigned to the Amazon interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-transitvirtualinterface-bgppeer.html#cfn-directconnect-transitvirtualinterface-bgppeer-amazonaddress
            '''
            result = self._values.get("amazon_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_key(self) -> typing.Optional[builtins.str]:
            '''The authentication key for BGP configuration.

            This string has a minimum length of 6 characters and and a maximum length of 80 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-transitvirtualinterface-bgppeer.html#cfn-directconnect-transitvirtualinterface-bgppeer-authkey
            '''
            result = self._values.get("auth_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bgp_peer_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-transitvirtualinterface-bgppeer.html#cfn-directconnect-transitvirtualinterface-bgppeer-bgppeerid
            '''
            result = self._values.get("bgp_peer_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def customer_address(self) -> typing.Optional[builtins.str]:
            '''The IP address assigned to the customer interface.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directconnect-transitvirtualinterface-bgppeer.html#cfn-directconnect-transitvirtualinterface-bgppeer-customeraddress
            '''
            result = self._values.get("customer_address")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BgpPeerProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_directconnect.CfnTransitVirtualInterfaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "bgp_peers": "bgpPeers",
        "connection_id": "connectionId",
        "direct_connect_gateway_id": "directConnectGatewayId",
        "virtual_interface_name": "virtualInterfaceName",
        "vlan": "vlan",
        "allocate_transit_virtual_interface_role_arn": "allocateTransitVirtualInterfaceRoleArn",
        "enable_site_link": "enableSiteLink",
        "mtu": "mtu",
        "tags": "tags",
    },
)
class CfnTransitVirtualInterfaceProps:
    def __init__(
        self,
        *,
        bgp_peers: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTransitVirtualInterface.BgpPeerProperty", typing.Dict[builtins.str, typing.Any]]]]],
        connection_id: typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"],
        direct_connect_gateway_id: typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"],
        virtual_interface_name: builtins.str,
        vlan: jsii.Number,
        allocate_transit_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
        enable_site_link: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        mtu: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTransitVirtualInterface``.

        :param bgp_peers: The BGP peers configured on this virtual interface..
        :param connection_id: 
        :param direct_connect_gateway_id: 
        :param virtual_interface_name: The name of the virtual interface assigned by the customer network. The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).
        :param vlan: The ID of the VLAN.
        :param allocate_transit_virtual_interface_role_arn: The Amazon Resource Name (ARN) of the role to allocate the TransitVifAllocation. Needs directconnect:AllocateTransitVirtualInterface permissions and tag permissions if applicable.
        :param enable_site_link: Indicates whether to enable or disable SiteLink.
        :param mtu: The maximum transmission unit (MTU), in bytes. The supported values are 1500 and 9001. The default value is 1500.
        :param tags: The tags associated with the private virtual interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_directconnect as directconnect
            
            cfn_transit_virtual_interface_props = directconnect.CfnTransitVirtualInterfaceProps(
                bgp_peers=[directconnect.CfnTransitVirtualInterface.BgpPeerProperty(
                    address_family="addressFamily",
                    asn="asn",
            
                    # the properties below are optional
                    amazon_address="amazonAddress",
                    auth_key="authKey",
                    bgp_peer_id="bgpPeerId",
                    customer_address="customerAddress"
                )],
                connection_id="connectionId",
                direct_connect_gateway_id="directConnectGatewayId",
                virtual_interface_name="virtualInterfaceName",
                vlan=123,
            
                # the properties below are optional
                allocate_transit_virtual_interface_role_arn="allocateTransitVirtualInterfaceRoleArn",
                enable_site_link=False,
                mtu=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa8466c27cdbb4001c029d13613d4fafd6773cca7380c863874c112e9e606107)
            check_type(argname="argument bgp_peers", value=bgp_peers, expected_type=type_hints["bgp_peers"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument direct_connect_gateway_id", value=direct_connect_gateway_id, expected_type=type_hints["direct_connect_gateway_id"])
            check_type(argname="argument virtual_interface_name", value=virtual_interface_name, expected_type=type_hints["virtual_interface_name"])
            check_type(argname="argument vlan", value=vlan, expected_type=type_hints["vlan"])
            check_type(argname="argument allocate_transit_virtual_interface_role_arn", value=allocate_transit_virtual_interface_role_arn, expected_type=type_hints["allocate_transit_virtual_interface_role_arn"])
            check_type(argname="argument enable_site_link", value=enable_site_link, expected_type=type_hints["enable_site_link"])
            check_type(argname="argument mtu", value=mtu, expected_type=type_hints["mtu"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bgp_peers": bgp_peers,
            "connection_id": connection_id,
            "direct_connect_gateway_id": direct_connect_gateway_id,
            "virtual_interface_name": virtual_interface_name,
            "vlan": vlan,
        }
        if allocate_transit_virtual_interface_role_arn is not None:
            self._values["allocate_transit_virtual_interface_role_arn"] = allocate_transit_virtual_interface_role_arn
        if enable_site_link is not None:
            self._values["enable_site_link"] = enable_site_link
        if mtu is not None:
            self._values["mtu"] = mtu
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def bgp_peers(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTransitVirtualInterface.BgpPeerProperty"]]]:
        '''The BGP peers configured on this virtual interface..

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html#cfn-directconnect-transitvirtualinterface-bgppeers
        '''
        result = self._values.get("bgp_peers")
        assert result is not None, "Required property 'bgp_peers' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTransitVirtualInterface.BgpPeerProperty"]]], result)

    @builtins.property
    def connection_id(
        self,
    ) -> typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html#cfn-directconnect-transitvirtualinterface-connectionid
        '''
        result = self._values.get("connection_id")
        assert result is not None, "Required property 'connection_id' is missing"
        return typing.cast(typing.Union[builtins.str, "_IConnectionRef_63fe92b7", "_ILagRef_ad81be41"], result)

    @builtins.property
    def direct_connect_gateway_id(
        self,
    ) -> typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html#cfn-directconnect-transitvirtualinterface-directconnectgatewayid
        '''
        result = self._values.get("direct_connect_gateway_id")
        assert result is not None, "Required property 'direct_connect_gateway_id' is missing"
        return typing.cast(typing.Union[builtins.str, "_IDirectConnectGatewayRef_e4e09968"], result)

    @builtins.property
    def virtual_interface_name(self) -> builtins.str:
        '''The name of the virtual interface assigned by the customer network.

        The name has a maximum of 100 characters. The following are valid characters: a-z, 0-9 and a hyphen (-).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html#cfn-directconnect-transitvirtualinterface-virtualinterfacename
        '''
        result = self._values.get("virtual_interface_name")
        assert result is not None, "Required property 'virtual_interface_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vlan(self) -> jsii.Number:
        '''The ID of the VLAN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html#cfn-directconnect-transitvirtualinterface-vlan
        '''
        result = self._values.get("vlan")
        assert result is not None, "Required property 'vlan' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def allocate_transit_virtual_interface_role_arn(
        self,
    ) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the role to allocate the TransitVifAllocation.

        Needs directconnect:AllocateTransitVirtualInterface permissions and tag permissions if applicable.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html#cfn-directconnect-transitvirtualinterface-allocatetransitvirtualinterfacerolearn
        '''
        result = self._values.get("allocate_transit_virtual_interface_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_site_link(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
        '''Indicates whether to enable or disable SiteLink.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html#cfn-directconnect-transitvirtualinterface-enablesitelink
        '''
        result = self._values.get("enable_site_link")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

    @builtins.property
    def mtu(self) -> typing.Optional[jsii.Number]:
        '''The maximum transmission unit (MTU), in bytes.

        The supported values are 1500 and 9001. The default value is 1500.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html#cfn-directconnect-transitvirtualinterface-mtu
        '''
        result = self._values.get("mtu")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The tags associated with the private virtual interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directconnect-transitvirtualinterface.html#cfn-directconnect-transitvirtualinterface-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTransitVirtualInterfaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnection",
    "CfnConnectionProps",
    "CfnDirectConnectGateway",
    "CfnDirectConnectGatewayAssociation",
    "CfnDirectConnectGatewayAssociationProps",
    "CfnDirectConnectGatewayProps",
    "CfnLag",
    "CfnLagProps",
    "CfnPrivateVirtualInterface",
    "CfnPrivateVirtualInterfaceProps",
    "CfnPublicVirtualInterface",
    "CfnPublicVirtualInterfaceProps",
    "CfnTransitVirtualInterface",
    "CfnTransitVirtualInterfaceProps",
]

publication.publish()

def _typecheckingstub__abd3e826047cb4f3add3b32f81e0f0d51a366c3420ae204b61e1322264552878(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bandwidth: builtins.str,
    connection_name: builtins.str,
    location: builtins.str,
    lag_id: typing.Optional[typing.Union[builtins.str, _ILagRef_ad81be41]] = None,
    provider_name: typing.Optional[builtins.str] = None,
    request_mac_sec: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc811b42835421ce0b775a0ef448945f7612f6d663ec68f45052ffe146f739af(
    resource: _IConnectionRef_63fe92b7,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7bc74ef019927b96fcf4a1e828df49db6d129e277ce74ef8cd1337c04d2f59c(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95e48f0564de8b818083771b3c0c5ac940302a8db9319c86e67ac3c1f6570673(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb36ef03a603aeaadd087cc23147c9f72eac9aeb1d035e9db5bd9580f12bfa66(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2e7f49b3a509e9eab2180d0340be2e045e35ecc946afee8ed2737c59d7453b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e216f63044a3047449997488350c6e2142da6557eb519bb3c3d2834d37b24f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfa87ce37b008a9d122d42e4d16dc3838265d4d9a856e01ad831b3f920cda236(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e57a138f92a6b26b88dbc27dcdec303c809669b1720f93a79992da39993d5ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d9beed62c085a97aa40d6e0b1fe180bdffacdf695e658ae6d1d1f75ff104e2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de3c51aad61f0509ee73f481eb3557b9d725aa29947a78539706e92a04e8a64d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f4754aee1d5c0403ec5b4b9c9456d81b46e0922c6cdca103190a7717871d0e3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cef94b4040c7599de15de3fed0380cef62c508ee4f4bfb62a0e9bf146744d326(
    *,
    bandwidth: builtins.str,
    connection_name: builtins.str,
    location: builtins.str,
    lag_id: typing.Optional[typing.Union[builtins.str, _ILagRef_ad81be41]] = None,
    provider_name: typing.Optional[builtins.str] = None,
    request_mac_sec: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1615be6a70d3256b8e774756f54d3b4cf912ec766378fb3e8ee821d12e361d8e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    direct_connect_gateway_name: builtins.str,
    amazon_side_asn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeac989b64b6c9e654802d2150c0e71cc5703a83fce5dd0348ab697181c4885e(
    resource: _IDirectConnectGatewayRef_e4e09968,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88bf54ee18195dc7a8967a7c425f0ba2d37c2a9bf16222bde5b4aef4c0c77585(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6f4599f1ad70aac102c5ff274184d302d9a7af0a7037dc65d9493a7250a50ea(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd4fe56d4dca103dacd6de6ee8157cc37d4830b5dea3b62dab0efdc2c8cfa8b8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__119a3a401444a4f739c5d7eb958461baf9823a5be3f705cb331b7bd20f47a375(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa42fe7f405b6fa870f5aa740a26933b9d10caad6a489a5e6e143d06def0f4f5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7218e90e3f0ec285cf01b746fdec827917118cd2f14ae196b858db1654c866c5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9610c3b37235aa2ee47e7088939e594786d6f4d5693f025059bad085a12dacf6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    associated_gateway_id: typing.Union[builtins.str, _ITransitGatewayRef_1edffe36, _IVPNGatewayRef_54a7e8d1],
    direct_connect_gateway_id: typing.Union[builtins.str, _IDirectConnectGatewayRef_e4e09968],
    accept_direct_connect_gateway_association_proposal_role_arn: typing.Optional[builtins.str] = None,
    allowed_prefixes_to_direct_connect_gateway: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d8e0743a98d958886293e96e4e1e2655dd0ec24bcf2d73ddb4d1ca9d0ee4bb0(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f42fd8eed9bf77e08c4a0333fe356f95fb63414699ab51892384bd4c7cd8ff45(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__545ac3d037192afa3e02747ab9d0f6b2516376105efeb0ee9599129bb7fc1bed(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad0ad4da945c7888b1cdc557eaad43a19712e50c70eb2a0a0b45721d129656ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b8ceca005e12409044ebdd46c4661d076dc807df321d7c42c9d057bd105450f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c17d25b54f1640987f5c7809c477911de8d79fda8aaa710471ce731c32844bc6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd1b070f48f63dd27940fbeb93f973d4627754096548f1aff97cef55c04d544e(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aba4d505c450c0c0634988995815ecbce3886430a251d53e2e1cea03d00e3dc(
    *,
    associated_gateway_id: typing.Union[builtins.str, _ITransitGatewayRef_1edffe36, _IVPNGatewayRef_54a7e8d1],
    direct_connect_gateway_id: typing.Union[builtins.str, _IDirectConnectGatewayRef_e4e09968],
    accept_direct_connect_gateway_association_proposal_role_arn: typing.Optional[builtins.str] = None,
    allowed_prefixes_to_direct_connect_gateway: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d12d0ef664e1585e49496cef753d3714e192674e47da7867d1068f7d108500ca(
    *,
    direct_connect_gateway_name: builtins.str,
    amazon_side_asn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71e07e1e973634e160c150954ce8d83214cd17c3957c56543bbea6f5fba0271d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connections_bandwidth: builtins.str,
    lag_name: builtins.str,
    location: builtins.str,
    minimum_links: typing.Optional[jsii.Number] = None,
    provider_name: typing.Optional[builtins.str] = None,
    request_mac_sec: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__242c81ea3f73ce5a36d840b7ee19805959188daeef9bd9b0f21a7bbfa1503479(
    resource: _ILagRef_ad81be41,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e303f0ea6e2eacc1eb30b7cd80a76514600efd466e569e9689059172d3ae1a67(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb555e87f0f441ba3fe669a7ab2dcc5af52aae255e46489e3ec68b236604d6fa(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84cba34045079c5172b3e91cd8aabdce8e2c0e0fce48380ba3f8cf9546b0708b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85cc7ef201d327e225d81d2d9169b5d4ad43aba6d15ef11cf93a48722a6bef4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e83119cc99194ef86f3183056b8345e95c8b2098dd6f9aa00c07f76cde76759b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96fa230eaf764b1c8371fc8a545f8f8ef8cd02faf385e3185ab98b0deb6d55b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4effe40bac9119e70c74b0ac4bff66dab2ee3fb0c76251442b20e20d2fe1ef0(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__376203ab16c44d6b6ecb9e3e4280481f8d0549cae91fc05930abcc70c5559687(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7a1a9dd628dda178fd7245c01d6d820f8da7ca508dde21a923653f06fea892c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7643963ed557c0e7d5eecd7f6d06e89df6563dbbd74e8ea1599569cb94029c99(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76f90241fc45565e7dbde4fbc117ddc4d00c34343f0ae967573f7940b73137c8(
    *,
    connections_bandwidth: builtins.str,
    lag_name: builtins.str,
    location: builtins.str,
    minimum_links: typing.Optional[jsii.Number] = None,
    provider_name: typing.Optional[builtins.str] = None,
    request_mac_sec: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b999bfd5ff244ca66e7bc7c8536b0b41cd03026156da31d75f5336483c8409d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bgp_peers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrivateVirtualInterface.BgpPeerProperty, typing.Dict[builtins.str, typing.Any]]]]],
    connection_id: typing.Union[builtins.str, _IConnectionRef_63fe92b7, _ILagRef_ad81be41],
    virtual_interface_name: builtins.str,
    vlan: jsii.Number,
    allocate_private_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
    direct_connect_gateway_id: typing.Optional[typing.Union[builtins.str, _IDirectConnectGatewayRef_e4e09968]] = None,
    enable_site_link: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    mtu: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    virtual_gateway_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00bf21163c98fc514b0d82eb2e086c4cb097a375ed76cadebcc4d31d674bee26(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38bfe59b40e5f2cc9fdded02a1abb9dc78bc269081f47ff7a63e690542bab683(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6bd885e0ed5ef6e152ac48182fbc4fad5271712f4ab65bd18fefa214e4b3985f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a377f3dc38cfdfcfbb888a8194c187841a1ffdf0187a8b1a9fb7944019ca7650(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPrivateVirtualInterface.BgpPeerProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41eecff3bb92985ba75103960b7f55da43a9af0be5f254c382fda4106f0f0550(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2652fdc0950ee77258f3161aacdeadf450794286361020dc461d4ee6a849b1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7be0f3eb45e2d56a69509393435a0c9c889408be16f96dbb8151c115cdaaf32(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc2ac054c23a5452fce570bc81a80994c8e147459879c7de51393c0f63a16879(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78b40e3a07653fbdb507c846d981a976cbff848d1febdc2cc43309729bd4348(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__901ddf3550f52d20f3db06493d53d33da7d865d1a2fa5e207ae907cb1cae6d8a(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ed96ea2147f833a590e8cb859e1264fdc9a4fd816c38bdb7de360223dd7e2ad(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb6b73505c5342ad306f9886d5bff4e132c15676d4f2e45fcbe415b72ed035bb(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23f80a4087ac6f3310be4fb0275b69ad615c5d64db1d6f947c5a22a628b95a3a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__497e11bdb89ebeb1deee774b538b67dcf4e0efe42bdbf5015631df088a809dac(
    *,
    address_family: builtins.str,
    asn: builtins.str,
    amazon_address: typing.Optional[builtins.str] = None,
    auth_key: typing.Optional[builtins.str] = None,
    bgp_peer_id: typing.Optional[builtins.str] = None,
    customer_address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4235226dc710b191f689dc9cfba93959927dfea6356ec9f8e5e5a4a4924acec4(
    *,
    bgp_peers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPrivateVirtualInterface.BgpPeerProperty, typing.Dict[builtins.str, typing.Any]]]]],
    connection_id: typing.Union[builtins.str, _IConnectionRef_63fe92b7, _ILagRef_ad81be41],
    virtual_interface_name: builtins.str,
    vlan: jsii.Number,
    allocate_private_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
    direct_connect_gateway_id: typing.Optional[typing.Union[builtins.str, _IDirectConnectGatewayRef_e4e09968]] = None,
    enable_site_link: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    mtu: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    virtual_gateway_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb624942469eb4c46619a6a53b66f8eefaefb7869b75206e9cc0f6ecfe9c4686(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bgp_peers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPublicVirtualInterface.BgpPeerProperty, typing.Dict[builtins.str, typing.Any]]]]],
    connection_id: typing.Union[builtins.str, _IConnectionRef_63fe92b7, _ILagRef_ad81be41],
    virtual_interface_name: builtins.str,
    vlan: jsii.Number,
    allocate_public_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
    route_filter_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a0d3a556867f13de687ec0219611d8afed4ca5a46dde9755d8595545c79cda(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f532504cdf995bfc683e973211df2172c108b3d15efe62bed7c5470f79849fb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1fee6b61972a50e0775b498e7174cbbbdca7dfdd9e3caa58b90de29b3bd661f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f44cde981a81e7ffa5693c513087f99e0bb137b4e6cb13c5ad826be9dbdf109(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnPublicVirtualInterface.BgpPeerProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d39b2e691dc81f2913cc829d97b4f3df45cd3685edd8e3cd9deddc45abdb4d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2a73cc5dc053ed58e9ac6baf4f2f62c72804fcf71ff3673a1c3a521109fb93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2b555240297573629e6980f8443995cc7ef32715fdc6a5278208d552fa7560a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57043a41fced754517b9e33f9547d38de18424e15989706839ddcab948060ded(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a470793a5aed4e3f78d1bba8a0be22800607924bdad3e6ea09f9a68136db3f8e(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c53c8d59a5a9e38b1ef03554805949bdd64f4c7567b7742dfbaa892c79ea5880(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76cbced85c2e693501bdf352afdf52f270e01694a49b284d6059a89d4d38f72a(
    *,
    address_family: builtins.str,
    asn: builtins.str,
    amazon_address: typing.Optional[builtins.str] = None,
    auth_key: typing.Optional[builtins.str] = None,
    bgp_peer_id: typing.Optional[builtins.str] = None,
    customer_address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90c6271856e4af9b71018ea29afa7c5c6b15f873ee9d157717f75a62759db624(
    *,
    bgp_peers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPublicVirtualInterface.BgpPeerProperty, typing.Dict[builtins.str, typing.Any]]]]],
    connection_id: typing.Union[builtins.str, _IConnectionRef_63fe92b7, _ILagRef_ad81be41],
    virtual_interface_name: builtins.str,
    vlan: jsii.Number,
    allocate_public_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
    route_filter_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8457181aefda9690d8c418796e9a515a2e66c5ac47ef49f5bc5009c032225092(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bgp_peers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransitVirtualInterface.BgpPeerProperty, typing.Dict[builtins.str, typing.Any]]]]],
    connection_id: typing.Union[builtins.str, _IConnectionRef_63fe92b7, _ILagRef_ad81be41],
    direct_connect_gateway_id: typing.Union[builtins.str, _IDirectConnectGatewayRef_e4e09968],
    virtual_interface_name: builtins.str,
    vlan: jsii.Number,
    allocate_transit_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
    enable_site_link: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    mtu: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7a6aa3d436db57a05a0f9c69a735b36148e8fe79e5a1924ba21377a694a1e1e(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f20090e74737b5107ec03ba9190842e3f80d15942d16324fd95ed298b7759185(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a922b83142d09b492418483facac0563f872463a354b375553098b5e1092a64c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3b9b304e783af9090d2ec707f39cd5d1a2b81e550a8b21bebe0eb5a21ecac36(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnTransitVirtualInterface.BgpPeerProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4ccfc04a3c912c34568a6a5720e015f1825b8219ba97f86a5ebb55a652bcf15(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3617cad06aea221ec06776b7dce786c2f2df66985f8406d81f7d4ac3d9b9a99a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bed18506fa2829afe14ed93e9974de1505dcc9a3b2b6ddae81716856407c5747(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3d955f7f3495d5127ff7429ea26623c64b18712014f01657aeed28c33c81fc(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a124137823eef4be92b8af8eb63b635385f95a2985d7a63c460405f25ed0bc3f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e03280b75ba0f770370d14184a3abe6d0ba0f8b6df43840d4d9976c87d5f034d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d19784da4e32c6ec4fe08fbf8f5821561fcb9deaa0adf75925b256d14d9076d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a469d82380a2c77aa1e6129aec6e66170b2e4285400f743b393d509e744c2f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86175311c426d11df4ae41f4f060bb07d2e554ddb0e944f5628a45df53003c50(
    *,
    address_family: builtins.str,
    asn: builtins.str,
    amazon_address: typing.Optional[builtins.str] = None,
    auth_key: typing.Optional[builtins.str] = None,
    bgp_peer_id: typing.Optional[builtins.str] = None,
    customer_address: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa8466c27cdbb4001c029d13613d4fafd6773cca7380c863874c112e9e606107(
    *,
    bgp_peers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTransitVirtualInterface.BgpPeerProperty, typing.Dict[builtins.str, typing.Any]]]]],
    connection_id: typing.Union[builtins.str, _IConnectionRef_63fe92b7, _ILagRef_ad81be41],
    direct_connect_gateway_id: typing.Union[builtins.str, _IDirectConnectGatewayRef_e4e09968],
    virtual_interface_name: builtins.str,
    vlan: jsii.Number,
    allocate_transit_virtual_interface_role_arn: typing.Optional[builtins.str] = None,
    enable_site_link: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    mtu: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
