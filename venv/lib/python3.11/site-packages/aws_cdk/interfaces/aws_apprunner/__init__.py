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
    jsii_type="aws-cdk-lib.interfaces.aws_apprunner.AutoScalingConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"auto_scaling_configuration_arn": "autoScalingConfigurationArn"},
)
class AutoScalingConfigurationReference:
    def __init__(self, *, auto_scaling_configuration_arn: builtins.str) -> None:
        '''A reference to a AutoScalingConfiguration resource.

        :param auto_scaling_configuration_arn: The AutoScalingConfigurationArn of the AutoScalingConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apprunner as interfaces_apprunner
            
            auto_scaling_configuration_reference = interfaces_apprunner.AutoScalingConfigurationReference(
                auto_scaling_configuration_arn="autoScalingConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b23311553dbebbf746f39eeee73f382a361dfb4ec7ca9ba4d02d9c1ed64f8a41)
            check_type(argname="argument auto_scaling_configuration_arn", value=auto_scaling_configuration_arn, expected_type=type_hints["auto_scaling_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auto_scaling_configuration_arn": auto_scaling_configuration_arn,
        }

    @builtins.property
    def auto_scaling_configuration_arn(self) -> builtins.str:
        '''The AutoScalingConfigurationArn of the AutoScalingConfiguration resource.'''
        result = self._values.get("auto_scaling_configuration_arn")
        assert result is not None, "Required property 'auto_scaling_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoScalingConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_apprunner.IAutoScalingConfigurationRef"
)
class IAutoScalingConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AutoScalingConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="autoScalingConfigurationRef")
    def auto_scaling_configuration_ref(self) -> "AutoScalingConfigurationReference":
        '''(experimental) A reference to a AutoScalingConfiguration resource.

        :stability: experimental
        '''
        ...


class _IAutoScalingConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AutoScalingConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apprunner.IAutoScalingConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="autoScalingConfigurationRef")
    def auto_scaling_configuration_ref(self) -> "AutoScalingConfigurationReference":
        '''(experimental) A reference to a AutoScalingConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("AutoScalingConfigurationReference", jsii.get(self, "autoScalingConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAutoScalingConfigurationRef).__jsii_proxy_class__ = lambda : _IAutoScalingConfigurationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_apprunner.IObservabilityConfigurationRef"
)
class IObservabilityConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ObservabilityConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="observabilityConfigurationRef")
    def observability_configuration_ref(self) -> "ObservabilityConfigurationReference":
        '''(experimental) A reference to a ObservabilityConfiguration resource.

        :stability: experimental
        '''
        ...


class _IObservabilityConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ObservabilityConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apprunner.IObservabilityConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="observabilityConfigurationRef")
    def observability_configuration_ref(self) -> "ObservabilityConfigurationReference":
        '''(experimental) A reference to a ObservabilityConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("ObservabilityConfigurationReference", jsii.get(self, "observabilityConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IObservabilityConfigurationRef).__jsii_proxy_class__ = lambda : _IObservabilityConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apprunner.IServiceRef")
class IServiceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        ...


class _IServiceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apprunner.IServiceRef"

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        return typing.cast("ServiceReference", jsii.get(self, "serviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceRef).__jsii_proxy_class__ = lambda : _IServiceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_apprunner.IVpcConnectorRef")
class IVpcConnectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VpcConnector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcConnectorRef")
    def vpc_connector_ref(self) -> "VpcConnectorReference":
        '''(experimental) A reference to a VpcConnector resource.

        :stability: experimental
        '''
        ...


class _IVpcConnectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VpcConnector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apprunner.IVpcConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="vpcConnectorRef")
    def vpc_connector_ref(self) -> "VpcConnectorReference":
        '''(experimental) A reference to a VpcConnector resource.

        :stability: experimental
        '''
        return typing.cast("VpcConnectorReference", jsii.get(self, "vpcConnectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVpcConnectorRef).__jsii_proxy_class__ = lambda : _IVpcConnectorRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_apprunner.IVpcIngressConnectionRef"
)
class IVpcIngressConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VpcIngressConnection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcIngressConnectionRef")
    def vpc_ingress_connection_ref(self) -> "VpcIngressConnectionReference":
        '''(experimental) A reference to a VpcIngressConnection resource.

        :stability: experimental
        '''
        ...


class _IVpcIngressConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VpcIngressConnection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_apprunner.IVpcIngressConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="vpcIngressConnectionRef")
    def vpc_ingress_connection_ref(self) -> "VpcIngressConnectionReference":
        '''(experimental) A reference to a VpcIngressConnection resource.

        :stability: experimental
        '''
        return typing.cast("VpcIngressConnectionReference", jsii.get(self, "vpcIngressConnectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVpcIngressConnectionRef).__jsii_proxy_class__ = lambda : _IVpcIngressConnectionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apprunner.ObservabilityConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"observability_configuration_arn": "observabilityConfigurationArn"},
)
class ObservabilityConfigurationReference:
    def __init__(self, *, observability_configuration_arn: builtins.str) -> None:
        '''A reference to a ObservabilityConfiguration resource.

        :param observability_configuration_arn: The ObservabilityConfigurationArn of the ObservabilityConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apprunner as interfaces_apprunner
            
            observability_configuration_reference = interfaces_apprunner.ObservabilityConfigurationReference(
                observability_configuration_arn="observabilityConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10ecefea892e5ef185bf208418555683f7e742ba9406e739995117075f499eab)
            check_type(argname="argument observability_configuration_arn", value=observability_configuration_arn, expected_type=type_hints["observability_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "observability_configuration_arn": observability_configuration_arn,
        }

    @builtins.property
    def observability_configuration_arn(self) -> builtins.str:
        '''The ObservabilityConfigurationArn of the ObservabilityConfiguration resource.'''
        result = self._values.get("observability_configuration_arn")
        assert result is not None, "Required property 'observability_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ObservabilityConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apprunner.ServiceReference",
    jsii_struct_bases=[],
    name_mapping={"service_arn": "serviceArn"},
)
class ServiceReference:
    def __init__(self, *, service_arn: builtins.str) -> None:
        '''A reference to a Service resource.

        :param service_arn: The ServiceArn of the Service resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apprunner as interfaces_apprunner
            
            service_reference = interfaces_apprunner.ServiceReference(
                service_arn="serviceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bbb56cbe5c4f3b4a1f82fee24b81285757c9e31ac24f28c2174c61b78764d16)
            check_type(argname="argument service_arn", value=service_arn, expected_type=type_hints["service_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_arn": service_arn,
        }

    @builtins.property
    def service_arn(self) -> builtins.str:
        '''The ServiceArn of the Service resource.'''
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apprunner.VpcConnectorReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_connector_arn": "vpcConnectorArn"},
)
class VpcConnectorReference:
    def __init__(self, *, vpc_connector_arn: builtins.str) -> None:
        '''A reference to a VpcConnector resource.

        :param vpc_connector_arn: The VpcConnectorArn of the VpcConnector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apprunner as interfaces_apprunner
            
            vpc_connector_reference = interfaces_apprunner.VpcConnectorReference(
                vpc_connector_arn="vpcConnectorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a5736d3b7a952404839f327bd5a27112dbd098bf3b1cb8032c1181e0fad204c)
            check_type(argname="argument vpc_connector_arn", value=vpc_connector_arn, expected_type=type_hints["vpc_connector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_connector_arn": vpc_connector_arn,
        }

    @builtins.property
    def vpc_connector_arn(self) -> builtins.str:
        '''The VpcConnectorArn of the VpcConnector resource.'''
        result = self._values.get("vpc_connector_arn")
        assert result is not None, "Required property 'vpc_connector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_apprunner.VpcIngressConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_ingress_connection_arn": "vpcIngressConnectionArn"},
)
class VpcIngressConnectionReference:
    def __init__(self, *, vpc_ingress_connection_arn: builtins.str) -> None:
        '''A reference to a VpcIngressConnection resource.

        :param vpc_ingress_connection_arn: The VpcIngressConnectionArn of the VpcIngressConnection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_apprunner as interfaces_apprunner
            
            vpc_ingress_connection_reference = interfaces_apprunner.VpcIngressConnectionReference(
                vpc_ingress_connection_arn="vpcIngressConnectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__089bc7f9cb92ee68b27c295c044cbe69aee00d63ad614c03f1fb09081ec0c831)
            check_type(argname="argument vpc_ingress_connection_arn", value=vpc_ingress_connection_arn, expected_type=type_hints["vpc_ingress_connection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_ingress_connection_arn": vpc_ingress_connection_arn,
        }

    @builtins.property
    def vpc_ingress_connection_arn(self) -> builtins.str:
        '''The VpcIngressConnectionArn of the VpcIngressConnection resource.'''
        result = self._values.get("vpc_ingress_connection_arn")
        assert result is not None, "Required property 'vpc_ingress_connection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcIngressConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AutoScalingConfigurationReference",
    "IAutoScalingConfigurationRef",
    "IObservabilityConfigurationRef",
    "IServiceRef",
    "IVpcConnectorRef",
    "IVpcIngressConnectionRef",
    "ObservabilityConfigurationReference",
    "ServiceReference",
    "VpcConnectorReference",
    "VpcIngressConnectionReference",
]

publication.publish()

def _typecheckingstub__b23311553dbebbf746f39eeee73f382a361dfb4ec7ca9ba4d02d9c1ed64f8a41(
    *,
    auto_scaling_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10ecefea892e5ef185bf208418555683f7e742ba9406e739995117075f499eab(
    *,
    observability_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bbb56cbe5c4f3b4a1f82fee24b81285757c9e31ac24f28c2174c61b78764d16(
    *,
    service_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a5736d3b7a952404839f327bd5a27112dbd098bf3b1cb8032c1181e0fad204c(
    *,
    vpc_connector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__089bc7f9cb92ee68b27c295c044cbe69aee00d63ad614c03f1fb09081ec0c831(
    *,
    vpc_ingress_connection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAutoScalingConfigurationRef, IObservabilityConfigurationRef, IServiceRef, IVpcConnectorRef, IVpcIngressConnectionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
