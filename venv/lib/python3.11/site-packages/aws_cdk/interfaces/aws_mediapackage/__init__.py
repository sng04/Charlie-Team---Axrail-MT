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
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackage.AssetReference",
    jsii_struct_bases=[],
    name_mapping={"asset_arn": "assetArn", "asset_id": "assetId"},
)
class AssetReference:
    def __init__(self, *, asset_arn: builtins.str, asset_id: builtins.str) -> None:
        '''A reference to a Asset resource.

        :param asset_arn: The ARN of the Asset resource.
        :param asset_id: The Id of the Asset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediapackage as interfaces_mediapackage
            
            asset_reference = interfaces_mediapackage.AssetReference(
                asset_arn="assetArn",
                asset_id="assetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d16e590cda98c290cd0546b98002ac00b9f570b972f31368b1e34cdf51fd9489)
            check_type(argname="argument asset_arn", value=asset_arn, expected_type=type_hints["asset_arn"])
            check_type(argname="argument asset_id", value=asset_id, expected_type=type_hints["asset_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "asset_arn": asset_arn,
            "asset_id": asset_id,
        }

    @builtins.property
    def asset_arn(self) -> builtins.str:
        '''The ARN of the Asset resource.'''
        result = self._values.get("asset_arn")
        assert result is not None, "Required property 'asset_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def asset_id(self) -> builtins.str:
        '''The Id of the Asset resource.'''
        result = self._values.get("asset_id")
        assert result is not None, "Required property 'asset_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AssetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackage.ChannelReference",
    jsii_struct_bases=[],
    name_mapping={"channel_arn": "channelArn", "channel_id": "channelId"},
)
class ChannelReference:
    def __init__(self, *, channel_arn: builtins.str, channel_id: builtins.str) -> None:
        '''A reference to a Channel resource.

        :param channel_arn: The ARN of the Channel resource.
        :param channel_id: The Id of the Channel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediapackage as interfaces_mediapackage
            
            channel_reference = interfaces_mediapackage.ChannelReference(
                channel_arn="channelArn",
                channel_id="channelId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4efb0079b37a3c8b5a216527c02be37850310ee32dcdaab1eea8bd805bfd63bb)
            check_type(argname="argument channel_arn", value=channel_arn, expected_type=type_hints["channel_arn"])
            check_type(argname="argument channel_id", value=channel_id, expected_type=type_hints["channel_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "channel_arn": channel_arn,
            "channel_id": channel_id,
        }

    @builtins.property
    def channel_arn(self) -> builtins.str:
        '''The ARN of the Channel resource.'''
        result = self._values.get("channel_arn")
        assert result is not None, "Required property 'channel_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def channel_id(self) -> builtins.str:
        '''The Id of the Channel resource.'''
        result = self._values.get("channel_id")
        assert result is not None, "Required property 'channel_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ChannelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediapackage.IAssetRef")
class IAssetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Asset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="assetRef")
    def asset_ref(self) -> "AssetReference":
        '''(experimental) A reference to a Asset resource.

        :stability: experimental
        '''
        ...


class _IAssetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Asset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediapackage.IAssetRef"

    @builtins.property
    @jsii.member(jsii_name="assetRef")
    def asset_ref(self) -> "AssetReference":
        '''(experimental) A reference to a Asset resource.

        :stability: experimental
        '''
        return typing.cast("AssetReference", jsii.get(self, "assetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAssetRef).__jsii_proxy_class__ = lambda : _IAssetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediapackage.IChannelRef")
class IChannelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Channel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        ...


class _IChannelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Channel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediapackage.IChannelRef"

    @builtins.property
    @jsii.member(jsii_name="channelRef")
    def channel_ref(self) -> "ChannelReference":
        '''(experimental) A reference to a Channel resource.

        :stability: experimental
        '''
        return typing.cast("ChannelReference", jsii.get(self, "channelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IChannelRef).__jsii_proxy_class__ = lambda : _IChannelRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediapackage.IOriginEndpointRef")
class IOriginEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OriginEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="originEndpointRef")
    def origin_endpoint_ref(self) -> "OriginEndpointReference":
        '''(experimental) A reference to a OriginEndpoint resource.

        :stability: experimental
        '''
        ...


class _IOriginEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OriginEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediapackage.IOriginEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="originEndpointRef")
    def origin_endpoint_ref(self) -> "OriginEndpointReference":
        '''(experimental) A reference to a OriginEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("OriginEndpointReference", jsii.get(self, "originEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOriginEndpointRef).__jsii_proxy_class__ = lambda : _IOriginEndpointRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackage.IPackagingConfigurationRef"
)
class IPackagingConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PackagingConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="packagingConfigurationRef")
    def packaging_configuration_ref(self) -> "PackagingConfigurationReference":
        '''(experimental) A reference to a PackagingConfiguration resource.

        :stability: experimental
        '''
        ...


class _IPackagingConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PackagingConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediapackage.IPackagingConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="packagingConfigurationRef")
    def packaging_configuration_ref(self) -> "PackagingConfigurationReference":
        '''(experimental) A reference to a PackagingConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("PackagingConfigurationReference", jsii.get(self, "packagingConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPackagingConfigurationRef).__jsii_proxy_class__ = lambda : _IPackagingConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mediapackage.IPackagingGroupRef")
class IPackagingGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PackagingGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="packagingGroupRef")
    def packaging_group_ref(self) -> "PackagingGroupReference":
        '''(experimental) A reference to a PackagingGroup resource.

        :stability: experimental
        '''
        ...


class _IPackagingGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PackagingGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mediapackage.IPackagingGroupRef"

    @builtins.property
    @jsii.member(jsii_name="packagingGroupRef")
    def packaging_group_ref(self) -> "PackagingGroupReference":
        '''(experimental) A reference to a PackagingGroup resource.

        :stability: experimental
        '''
        return typing.cast("PackagingGroupReference", jsii.get(self, "packagingGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPackagingGroupRef).__jsii_proxy_class__ = lambda : _IPackagingGroupRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackage.OriginEndpointReference",
    jsii_struct_bases=[],
    name_mapping={
        "origin_endpoint_arn": "originEndpointArn",
        "origin_endpoint_id": "originEndpointId",
    },
)
class OriginEndpointReference:
    def __init__(
        self,
        *,
        origin_endpoint_arn: builtins.str,
        origin_endpoint_id: builtins.str,
    ) -> None:
        '''A reference to a OriginEndpoint resource.

        :param origin_endpoint_arn: The ARN of the OriginEndpoint resource.
        :param origin_endpoint_id: The Id of the OriginEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediapackage as interfaces_mediapackage
            
            origin_endpoint_reference = interfaces_mediapackage.OriginEndpointReference(
                origin_endpoint_arn="originEndpointArn",
                origin_endpoint_id="originEndpointId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05596b0d26f4975f16a02840836b7495eb684cdb2459f99fc07731a186e740f0)
            check_type(argname="argument origin_endpoint_arn", value=origin_endpoint_arn, expected_type=type_hints["origin_endpoint_arn"])
            check_type(argname="argument origin_endpoint_id", value=origin_endpoint_id, expected_type=type_hints["origin_endpoint_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "origin_endpoint_arn": origin_endpoint_arn,
            "origin_endpoint_id": origin_endpoint_id,
        }

    @builtins.property
    def origin_endpoint_arn(self) -> builtins.str:
        '''The ARN of the OriginEndpoint resource.'''
        result = self._values.get("origin_endpoint_arn")
        assert result is not None, "Required property 'origin_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def origin_endpoint_id(self) -> builtins.str:
        '''The Id of the OriginEndpoint resource.'''
        result = self._values.get("origin_endpoint_id")
        assert result is not None, "Required property 'origin_endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackage.PackagingConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "packaging_configuration_arn": "packagingConfigurationArn",
        "packaging_configuration_id": "packagingConfigurationId",
    },
)
class PackagingConfigurationReference:
    def __init__(
        self,
        *,
        packaging_configuration_arn: builtins.str,
        packaging_configuration_id: builtins.str,
    ) -> None:
        '''A reference to a PackagingConfiguration resource.

        :param packaging_configuration_arn: The ARN of the PackagingConfiguration resource.
        :param packaging_configuration_id: The Id of the PackagingConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediapackage as interfaces_mediapackage
            
            packaging_configuration_reference = interfaces_mediapackage.PackagingConfigurationReference(
                packaging_configuration_arn="packagingConfigurationArn",
                packaging_configuration_id="packagingConfigurationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b63d44ab2cace3a16defbd479b253699c1c6df5d1a5173bdccafc9f0bcedce0)
            check_type(argname="argument packaging_configuration_arn", value=packaging_configuration_arn, expected_type=type_hints["packaging_configuration_arn"])
            check_type(argname="argument packaging_configuration_id", value=packaging_configuration_id, expected_type=type_hints["packaging_configuration_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "packaging_configuration_arn": packaging_configuration_arn,
            "packaging_configuration_id": packaging_configuration_id,
        }

    @builtins.property
    def packaging_configuration_arn(self) -> builtins.str:
        '''The ARN of the PackagingConfiguration resource.'''
        result = self._values.get("packaging_configuration_arn")
        assert result is not None, "Required property 'packaging_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def packaging_configuration_id(self) -> builtins.str:
        '''The Id of the PackagingConfiguration resource.'''
        result = self._values.get("packaging_configuration_id")
        assert result is not None, "Required property 'packaging_configuration_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PackagingConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mediapackage.PackagingGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "packaging_group_arn": "packagingGroupArn",
        "packaging_group_id": "packagingGroupId",
    },
)
class PackagingGroupReference:
    def __init__(
        self,
        *,
        packaging_group_arn: builtins.str,
        packaging_group_id: builtins.str,
    ) -> None:
        '''A reference to a PackagingGroup resource.

        :param packaging_group_arn: The ARN of the PackagingGroup resource.
        :param packaging_group_id: The Id of the PackagingGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mediapackage as interfaces_mediapackage
            
            packaging_group_reference = interfaces_mediapackage.PackagingGroupReference(
                packaging_group_arn="packagingGroupArn",
                packaging_group_id="packagingGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db65eb06f9e062a8f448e531b07b218e2f86d3fb83c3032a17aad865fdb1b076)
            check_type(argname="argument packaging_group_arn", value=packaging_group_arn, expected_type=type_hints["packaging_group_arn"])
            check_type(argname="argument packaging_group_id", value=packaging_group_id, expected_type=type_hints["packaging_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "packaging_group_arn": packaging_group_arn,
            "packaging_group_id": packaging_group_id,
        }

    @builtins.property
    def packaging_group_arn(self) -> builtins.str:
        '''The ARN of the PackagingGroup resource.'''
        result = self._values.get("packaging_group_arn")
        assert result is not None, "Required property 'packaging_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def packaging_group_id(self) -> builtins.str:
        '''The Id of the PackagingGroup resource.'''
        result = self._values.get("packaging_group_id")
        assert result is not None, "Required property 'packaging_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PackagingGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AssetReference",
    "ChannelReference",
    "IAssetRef",
    "IChannelRef",
    "IOriginEndpointRef",
    "IPackagingConfigurationRef",
    "IPackagingGroupRef",
    "OriginEndpointReference",
    "PackagingConfigurationReference",
    "PackagingGroupReference",
]

publication.publish()

def _typecheckingstub__d16e590cda98c290cd0546b98002ac00b9f570b972f31368b1e34cdf51fd9489(
    *,
    asset_arn: builtins.str,
    asset_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4efb0079b37a3c8b5a216527c02be37850310ee32dcdaab1eea8bd805bfd63bb(
    *,
    channel_arn: builtins.str,
    channel_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05596b0d26f4975f16a02840836b7495eb684cdb2459f99fc07731a186e740f0(
    *,
    origin_endpoint_arn: builtins.str,
    origin_endpoint_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b63d44ab2cace3a16defbd479b253699c1c6df5d1a5173bdccafc9f0bcedce0(
    *,
    packaging_configuration_arn: builtins.str,
    packaging_configuration_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db65eb06f9e062a8f448e531b07b218e2f86d3fb83c3032a17aad865fdb1b076(
    *,
    packaging_group_arn: builtins.str,
    packaging_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAssetRef, IChannelRef, IOriginEndpointRef, IPackagingConfigurationRef, IPackagingGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
