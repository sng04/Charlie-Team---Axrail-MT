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
    jsii_type="aws-cdk-lib.interfaces.aws_odb.CloudAutonomousVmClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cloud_autonomous_vm_cluster_arn": "cloudAutonomousVmClusterArn"},
)
class CloudAutonomousVmClusterReference:
    def __init__(self, *, cloud_autonomous_vm_cluster_arn: builtins.str) -> None:
        '''A reference to a CloudAutonomousVmCluster resource.

        :param cloud_autonomous_vm_cluster_arn: The CloudAutonomousVmClusterArn of the CloudAutonomousVmCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_odb as interfaces_odb
            
            cloud_autonomous_vm_cluster_reference = interfaces_odb.CloudAutonomousVmClusterReference(
                cloud_autonomous_vm_cluster_arn="cloudAutonomousVmClusterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24f47f559e097d1f99e8b694a5a38dbdc87eddb68da4937ccedaf72af612ea50)
            check_type(argname="argument cloud_autonomous_vm_cluster_arn", value=cloud_autonomous_vm_cluster_arn, expected_type=type_hints["cloud_autonomous_vm_cluster_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_autonomous_vm_cluster_arn": cloud_autonomous_vm_cluster_arn,
        }

    @builtins.property
    def cloud_autonomous_vm_cluster_arn(self) -> builtins.str:
        '''The CloudAutonomousVmClusterArn of the CloudAutonomousVmCluster resource.'''
        result = self._values.get("cloud_autonomous_vm_cluster_arn")
        assert result is not None, "Required property 'cloud_autonomous_vm_cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAutonomousVmClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_odb.CloudExadataInfrastructureReference",
    jsii_struct_bases=[],
    name_mapping={"cloud_exadata_infrastructure_arn": "cloudExadataInfrastructureArn"},
)
class CloudExadataInfrastructureReference:
    def __init__(self, *, cloud_exadata_infrastructure_arn: builtins.str) -> None:
        '''A reference to a CloudExadataInfrastructure resource.

        :param cloud_exadata_infrastructure_arn: The CloudExadataInfrastructureArn of the CloudExadataInfrastructure resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_odb as interfaces_odb
            
            cloud_exadata_infrastructure_reference = interfaces_odb.CloudExadataInfrastructureReference(
                cloud_exadata_infrastructure_arn="cloudExadataInfrastructureArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42c18f800ef88ea913172e37ac6192f7948d1899683a6b17f70c472ee560f9a6)
            check_type(argname="argument cloud_exadata_infrastructure_arn", value=cloud_exadata_infrastructure_arn, expected_type=type_hints["cloud_exadata_infrastructure_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_exadata_infrastructure_arn": cloud_exadata_infrastructure_arn,
        }

    @builtins.property
    def cloud_exadata_infrastructure_arn(self) -> builtins.str:
        '''The CloudExadataInfrastructureArn of the CloudExadataInfrastructure resource.'''
        result = self._values.get("cloud_exadata_infrastructure_arn")
        assert result is not None, "Required property 'cloud_exadata_infrastructure_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudExadataInfrastructureReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_odb.CloudVmClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cloud_vm_cluster_arn": "cloudVmClusterArn"},
)
class CloudVmClusterReference:
    def __init__(self, *, cloud_vm_cluster_arn: builtins.str) -> None:
        '''A reference to a CloudVmCluster resource.

        :param cloud_vm_cluster_arn: The CloudVmClusterArn of the CloudVmCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_odb as interfaces_odb
            
            cloud_vm_cluster_reference = interfaces_odb.CloudVmClusterReference(
                cloud_vm_cluster_arn="cloudVmClusterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6787835ee51e3576a47e957c925da1d5f69df18d0710d2ad1d4db086a7ce0c81)
            check_type(argname="argument cloud_vm_cluster_arn", value=cloud_vm_cluster_arn, expected_type=type_hints["cloud_vm_cluster_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cloud_vm_cluster_arn": cloud_vm_cluster_arn,
        }

    @builtins.property
    def cloud_vm_cluster_arn(self) -> builtins.str:
        '''The CloudVmClusterArn of the CloudVmCluster resource.'''
        result = self._values.get("cloud_vm_cluster_arn")
        assert result is not None, "Required property 'cloud_vm_cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudVmClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_odb.ICloudAutonomousVmClusterRef"
)
class ICloudAutonomousVmClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CloudAutonomousVmCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cloudAutonomousVmClusterRef")
    def cloud_autonomous_vm_cluster_ref(self) -> "CloudAutonomousVmClusterReference":
        '''(experimental) A reference to a CloudAutonomousVmCluster resource.

        :stability: experimental
        '''
        ...


class _ICloudAutonomousVmClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CloudAutonomousVmCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_odb.ICloudAutonomousVmClusterRef"

    @builtins.property
    @jsii.member(jsii_name="cloudAutonomousVmClusterRef")
    def cloud_autonomous_vm_cluster_ref(self) -> "CloudAutonomousVmClusterReference":
        '''(experimental) A reference to a CloudAutonomousVmCluster resource.

        :stability: experimental
        '''
        return typing.cast("CloudAutonomousVmClusterReference", jsii.get(self, "cloudAutonomousVmClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICloudAutonomousVmClusterRef).__jsii_proxy_class__ = lambda : _ICloudAutonomousVmClusterRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_odb.ICloudExadataInfrastructureRef"
)
class ICloudExadataInfrastructureRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CloudExadataInfrastructure.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cloudExadataInfrastructureRef")
    def cloud_exadata_infrastructure_ref(self) -> "CloudExadataInfrastructureReference":
        '''(experimental) A reference to a CloudExadataInfrastructure resource.

        :stability: experimental
        '''
        ...


class _ICloudExadataInfrastructureRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CloudExadataInfrastructure.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_odb.ICloudExadataInfrastructureRef"

    @builtins.property
    @jsii.member(jsii_name="cloudExadataInfrastructureRef")
    def cloud_exadata_infrastructure_ref(self) -> "CloudExadataInfrastructureReference":
        '''(experimental) A reference to a CloudExadataInfrastructure resource.

        :stability: experimental
        '''
        return typing.cast("CloudExadataInfrastructureReference", jsii.get(self, "cloudExadataInfrastructureRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICloudExadataInfrastructureRef).__jsii_proxy_class__ = lambda : _ICloudExadataInfrastructureRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_odb.ICloudVmClusterRef")
class ICloudVmClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CloudVmCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cloudVmClusterRef")
    def cloud_vm_cluster_ref(self) -> "CloudVmClusterReference":
        '''(experimental) A reference to a CloudVmCluster resource.

        :stability: experimental
        '''
        ...


class _ICloudVmClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CloudVmCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_odb.ICloudVmClusterRef"

    @builtins.property
    @jsii.member(jsii_name="cloudVmClusterRef")
    def cloud_vm_cluster_ref(self) -> "CloudVmClusterReference":
        '''(experimental) A reference to a CloudVmCluster resource.

        :stability: experimental
        '''
        return typing.cast("CloudVmClusterReference", jsii.get(self, "cloudVmClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICloudVmClusterRef).__jsii_proxy_class__ = lambda : _ICloudVmClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_odb.IOdbNetworkRef")
class IOdbNetworkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OdbNetwork.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="odbNetworkRef")
    def odb_network_ref(self) -> "OdbNetworkReference":
        '''(experimental) A reference to a OdbNetwork resource.

        :stability: experimental
        '''
        ...


class _IOdbNetworkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OdbNetwork.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_odb.IOdbNetworkRef"

    @builtins.property
    @jsii.member(jsii_name="odbNetworkRef")
    def odb_network_ref(self) -> "OdbNetworkReference":
        '''(experimental) A reference to a OdbNetwork resource.

        :stability: experimental
        '''
        return typing.cast("OdbNetworkReference", jsii.get(self, "odbNetworkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOdbNetworkRef).__jsii_proxy_class__ = lambda : _IOdbNetworkRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_odb.IOdbPeeringConnectionRef")
class IOdbPeeringConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a OdbPeeringConnection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="odbPeeringConnectionRef")
    def odb_peering_connection_ref(self) -> "OdbPeeringConnectionReference":
        '''(experimental) A reference to a OdbPeeringConnection resource.

        :stability: experimental
        '''
        ...


class _IOdbPeeringConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a OdbPeeringConnection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_odb.IOdbPeeringConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="odbPeeringConnectionRef")
    def odb_peering_connection_ref(self) -> "OdbPeeringConnectionReference":
        '''(experimental) A reference to a OdbPeeringConnection resource.

        :stability: experimental
        '''
        return typing.cast("OdbPeeringConnectionReference", jsii.get(self, "odbPeeringConnectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IOdbPeeringConnectionRef).__jsii_proxy_class__ = lambda : _IOdbPeeringConnectionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_odb.OdbNetworkReference",
    jsii_struct_bases=[],
    name_mapping={"odb_network_arn": "odbNetworkArn"},
)
class OdbNetworkReference:
    def __init__(self, *, odb_network_arn: builtins.str) -> None:
        '''A reference to a OdbNetwork resource.

        :param odb_network_arn: The OdbNetworkArn of the OdbNetwork resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_odb as interfaces_odb
            
            odb_network_reference = interfaces_odb.OdbNetworkReference(
                odb_network_arn="odbNetworkArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcd10c7758ee3a6ea3380811028675124f296c973d2ee34053ad8b5c6732f9c7)
            check_type(argname="argument odb_network_arn", value=odb_network_arn, expected_type=type_hints["odb_network_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "odb_network_arn": odb_network_arn,
        }

    @builtins.property
    def odb_network_arn(self) -> builtins.str:
        '''The OdbNetworkArn of the OdbNetwork resource.'''
        result = self._values.get("odb_network_arn")
        assert result is not None, "Required property 'odb_network_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OdbNetworkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_odb.OdbPeeringConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"odb_peering_connection_arn": "odbPeeringConnectionArn"},
)
class OdbPeeringConnectionReference:
    def __init__(self, *, odb_peering_connection_arn: builtins.str) -> None:
        '''A reference to a OdbPeeringConnection resource.

        :param odb_peering_connection_arn: The OdbPeeringConnectionArn of the OdbPeeringConnection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_odb as interfaces_odb
            
            odb_peering_connection_reference = interfaces_odb.OdbPeeringConnectionReference(
                odb_peering_connection_arn="odbPeeringConnectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__618c5752938ece684b449b51809742fa009be29d013b2b4dee097d8cb9aac13a)
            check_type(argname="argument odb_peering_connection_arn", value=odb_peering_connection_arn, expected_type=type_hints["odb_peering_connection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "odb_peering_connection_arn": odb_peering_connection_arn,
        }

    @builtins.property
    def odb_peering_connection_arn(self) -> builtins.str:
        '''The OdbPeeringConnectionArn of the OdbPeeringConnection resource.'''
        result = self._values.get("odb_peering_connection_arn")
        assert result is not None, "Required property 'odb_peering_connection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OdbPeeringConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CloudAutonomousVmClusterReference",
    "CloudExadataInfrastructureReference",
    "CloudVmClusterReference",
    "ICloudAutonomousVmClusterRef",
    "ICloudExadataInfrastructureRef",
    "ICloudVmClusterRef",
    "IOdbNetworkRef",
    "IOdbPeeringConnectionRef",
    "OdbNetworkReference",
    "OdbPeeringConnectionReference",
]

publication.publish()

def _typecheckingstub__24f47f559e097d1f99e8b694a5a38dbdc87eddb68da4937ccedaf72af612ea50(
    *,
    cloud_autonomous_vm_cluster_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42c18f800ef88ea913172e37ac6192f7948d1899683a6b17f70c472ee560f9a6(
    *,
    cloud_exadata_infrastructure_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6787835ee51e3576a47e957c925da1d5f69df18d0710d2ad1d4db086a7ce0c81(
    *,
    cloud_vm_cluster_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcd10c7758ee3a6ea3380811028675124f296c973d2ee34053ad8b5c6732f9c7(
    *,
    odb_network_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618c5752938ece684b449b51809742fa009be29d013b2b4dee097d8cb9aac13a(
    *,
    odb_peering_connection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICloudAutonomousVmClusterRef, ICloudExadataInfrastructureRef, ICloudVmClusterRef, IOdbNetworkRef, IOdbPeeringConnectionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
