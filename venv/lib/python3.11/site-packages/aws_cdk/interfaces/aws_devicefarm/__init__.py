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
    jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.DevicePoolReference",
    jsii_struct_bases=[],
    name_mapping={"device_pool_arn": "devicePoolArn"},
)
class DevicePoolReference:
    def __init__(self, *, device_pool_arn: builtins.str) -> None:
        '''A reference to a DevicePool resource.

        :param device_pool_arn: The Arn of the DevicePool resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devicefarm as interfaces_devicefarm
            
            device_pool_reference = interfaces_devicefarm.DevicePoolReference(
                device_pool_arn="devicePoolArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6fa41dfe195486b945fa7a362f59ce6d48484656b7ea950b33cecf53168f918)
            check_type(argname="argument device_pool_arn", value=device_pool_arn, expected_type=type_hints["device_pool_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_pool_arn": device_pool_arn,
        }

    @builtins.property
    def device_pool_arn(self) -> builtins.str:
        '''The Arn of the DevicePool resource.'''
        result = self._values.get("device_pool_arn")
        assert result is not None, "Required property 'device_pool_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevicePoolReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.IDevicePoolRef")
class IDevicePoolRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DevicePool.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="devicePoolRef")
    def device_pool_ref(self) -> "DevicePoolReference":
        '''(experimental) A reference to a DevicePool resource.

        :stability: experimental
        '''
        ...


class _IDevicePoolRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DevicePool.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devicefarm.IDevicePoolRef"

    @builtins.property
    @jsii.member(jsii_name="devicePoolRef")
    def device_pool_ref(self) -> "DevicePoolReference":
        '''(experimental) A reference to a DevicePool resource.

        :stability: experimental
        '''
        return typing.cast("DevicePoolReference", jsii.get(self, "devicePoolRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDevicePoolRef).__jsii_proxy_class__ = lambda : _IDevicePoolRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.IInstanceProfileRef")
class IInstanceProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="instanceProfileRef")
    def instance_profile_ref(self) -> "InstanceProfileReference":
        '''(experimental) A reference to a InstanceProfile resource.

        :stability: experimental
        '''
        ...


class _IInstanceProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InstanceProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devicefarm.IInstanceProfileRef"

    @builtins.property
    @jsii.member(jsii_name="instanceProfileRef")
    def instance_profile_ref(self) -> "InstanceProfileReference":
        '''(experimental) A reference to a InstanceProfile resource.

        :stability: experimental
        '''
        return typing.cast("InstanceProfileReference", jsii.get(self, "instanceProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInstanceProfileRef).__jsii_proxy_class__ = lambda : _IInstanceProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.INetworkProfileRef")
class INetworkProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="networkProfileRef")
    def network_profile_ref(self) -> "NetworkProfileReference":
        '''(experimental) A reference to a NetworkProfile resource.

        :stability: experimental
        '''
        ...


class _INetworkProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a NetworkProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devicefarm.INetworkProfileRef"

    @builtins.property
    @jsii.member(jsii_name="networkProfileRef")
    def network_profile_ref(self) -> "NetworkProfileReference":
        '''(experimental) A reference to a NetworkProfile resource.

        :stability: experimental
        '''
        return typing.cast("NetworkProfileReference", jsii.get(self, "networkProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INetworkProfileRef).__jsii_proxy_class__ = lambda : _INetworkProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.IProjectRef")
class IProjectRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Project.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        ...


class _IProjectRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Project.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devicefarm.IProjectRef"

    @builtins.property
    @jsii.member(jsii_name="projectRef")
    def project_ref(self) -> "ProjectReference":
        '''(experimental) A reference to a Project resource.

        :stability: experimental
        '''
        return typing.cast("ProjectReference", jsii.get(self, "projectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProjectRef).__jsii_proxy_class__ = lambda : _IProjectRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.ITestGridProjectRef")
class ITestGridProjectRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TestGridProject.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="testGridProjectRef")
    def test_grid_project_ref(self) -> "TestGridProjectReference":
        '''(experimental) A reference to a TestGridProject resource.

        :stability: experimental
        '''
        ...


class _ITestGridProjectRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TestGridProject.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devicefarm.ITestGridProjectRef"

    @builtins.property
    @jsii.member(jsii_name="testGridProjectRef")
    def test_grid_project_ref(self) -> "TestGridProjectReference":
        '''(experimental) A reference to a TestGridProject resource.

        :stability: experimental
        '''
        return typing.cast("TestGridProjectReference", jsii.get(self, "testGridProjectRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITestGridProjectRef).__jsii_proxy_class__ = lambda : _ITestGridProjectRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.IVPCEConfigurationRef"
)
class IVPCEConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpceConfigurationRef")
    def vpce_configuration_ref(self) -> "VPCEConfigurationReference":
        '''(experimental) A reference to a VPCEConfiguration resource.

        :stability: experimental
        '''
        ...


class _IVPCEConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VPCEConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_devicefarm.IVPCEConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="vpceConfigurationRef")
    def vpce_configuration_ref(self) -> "VPCEConfigurationReference":
        '''(experimental) A reference to a VPCEConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("VPCEConfigurationReference", jsii.get(self, "vpceConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVPCEConfigurationRef).__jsii_proxy_class__ = lambda : _IVPCEConfigurationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.InstanceProfileReference",
    jsii_struct_bases=[],
    name_mapping={"instance_profile_arn": "instanceProfileArn"},
)
class InstanceProfileReference:
    def __init__(self, *, instance_profile_arn: builtins.str) -> None:
        '''A reference to a InstanceProfile resource.

        :param instance_profile_arn: The Arn of the InstanceProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devicefarm as interfaces_devicefarm
            
            instance_profile_reference = interfaces_devicefarm.InstanceProfileReference(
                instance_profile_arn="instanceProfileArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e5bdc64cdfcfefb69deec82565d63ddc57d0eef98491e9f42f3a3be4252e09c)
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "instance_profile_arn": instance_profile_arn,
        }

    @builtins.property
    def instance_profile_arn(self) -> builtins.str:
        '''The Arn of the InstanceProfile resource.'''
        result = self._values.get("instance_profile_arn")
        assert result is not None, "Required property 'instance_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.NetworkProfileReference",
    jsii_struct_bases=[],
    name_mapping={"network_profile_arn": "networkProfileArn"},
)
class NetworkProfileReference:
    def __init__(self, *, network_profile_arn: builtins.str) -> None:
        '''A reference to a NetworkProfile resource.

        :param network_profile_arn: The Arn of the NetworkProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devicefarm as interfaces_devicefarm
            
            network_profile_reference = interfaces_devicefarm.NetworkProfileReference(
                network_profile_arn="networkProfileArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fe8c9dec47d8909868d79f6cd61a01136f8a4902c5053129d0189adf634b2f4)
            check_type(argname="argument network_profile_arn", value=network_profile_arn, expected_type=type_hints["network_profile_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "network_profile_arn": network_profile_arn,
        }

    @builtins.property
    def network_profile_arn(self) -> builtins.str:
        '''The Arn of the NetworkProfile resource.'''
        result = self._values.get("network_profile_arn")
        assert result is not None, "Required property 'network_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.ProjectReference",
    jsii_struct_bases=[],
    name_mapping={"project_arn": "projectArn"},
)
class ProjectReference:
    def __init__(self, *, project_arn: builtins.str) -> None:
        '''A reference to a Project resource.

        :param project_arn: The Arn of the Project resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devicefarm as interfaces_devicefarm
            
            project_reference = interfaces_devicefarm.ProjectReference(
                project_arn="projectArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4c3a7aa56ebf3a2c641245d95442df6ade72d2a729e37dc6edd020bb607c111)
            check_type(argname="argument project_arn", value=project_arn, expected_type=type_hints["project_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "project_arn": project_arn,
        }

    @builtins.property
    def project_arn(self) -> builtins.str:
        '''The Arn of the Project resource.'''
        result = self._values.get("project_arn")
        assert result is not None, "Required property 'project_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProjectReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.TestGridProjectReference",
    jsii_struct_bases=[],
    name_mapping={"test_grid_project_arn": "testGridProjectArn"},
)
class TestGridProjectReference:
    def __init__(self, *, test_grid_project_arn: builtins.str) -> None:
        '''A reference to a TestGridProject resource.

        :param test_grid_project_arn: The Arn of the TestGridProject resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devicefarm as interfaces_devicefarm
            
            test_grid_project_reference = interfaces_devicefarm.TestGridProjectReference(
                test_grid_project_arn="testGridProjectArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87f265414f05bd136bba63546376bc2e436efa434aab240574ffa93dae93acc8)
            check_type(argname="argument test_grid_project_arn", value=test_grid_project_arn, expected_type=type_hints["test_grid_project_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "test_grid_project_arn": test_grid_project_arn,
        }

    @builtins.property
    def test_grid_project_arn(self) -> builtins.str:
        '''The Arn of the TestGridProject resource.'''
        result = self._values.get("test_grid_project_arn")
        assert result is not None, "Required property 'test_grid_project_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TestGridProjectReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_devicefarm.VPCEConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"vpce_configuration_arn": "vpceConfigurationArn"},
)
class VPCEConfigurationReference:
    def __init__(self, *, vpce_configuration_arn: builtins.str) -> None:
        '''A reference to a VPCEConfiguration resource.

        :param vpce_configuration_arn: The Arn of the VPCEConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_devicefarm as interfaces_devicefarm
            
            v_pCEConfiguration_reference = interfaces_devicefarm.VPCEConfigurationReference(
                vpce_configuration_arn="vpceConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b288bcd87f2c0fa8d760d6c34b871baa157a88f4015e77c240ef6abf4db384a5)
            check_type(argname="argument vpce_configuration_arn", value=vpce_configuration_arn, expected_type=type_hints["vpce_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpce_configuration_arn": vpce_configuration_arn,
        }

    @builtins.property
    def vpce_configuration_arn(self) -> builtins.str:
        '''The Arn of the VPCEConfiguration resource.'''
        result = self._values.get("vpce_configuration_arn")
        assert result is not None, "Required property 'vpce_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VPCEConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DevicePoolReference",
    "IDevicePoolRef",
    "IInstanceProfileRef",
    "INetworkProfileRef",
    "IProjectRef",
    "ITestGridProjectRef",
    "IVPCEConfigurationRef",
    "InstanceProfileReference",
    "NetworkProfileReference",
    "ProjectReference",
    "TestGridProjectReference",
    "VPCEConfigurationReference",
]

publication.publish()

def _typecheckingstub__d6fa41dfe195486b945fa7a362f59ce6d48484656b7ea950b33cecf53168f918(
    *,
    device_pool_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e5bdc64cdfcfefb69deec82565d63ddc57d0eef98491e9f42f3a3be4252e09c(
    *,
    instance_profile_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fe8c9dec47d8909868d79f6cd61a01136f8a4902c5053129d0189adf634b2f4(
    *,
    network_profile_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4c3a7aa56ebf3a2c641245d95442df6ade72d2a729e37dc6edd020bb607c111(
    *,
    project_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87f265414f05bd136bba63546376bc2e436efa434aab240574ffa93dae93acc8(
    *,
    test_grid_project_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b288bcd87f2c0fa8d760d6c34b871baa157a88f4015e77c240ef6abf4db384a5(
    *,
    vpce_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDevicePoolRef, IInstanceProfileRef, INetworkProfileRef, IProjectRef, ITestGridProjectRef, IVPCEConfigurationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
