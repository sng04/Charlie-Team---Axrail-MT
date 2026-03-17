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
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoverycontrol.ClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn"},
)
class ClusterReference:
    def __init__(self, *, cluster_arn: builtins.str) -> None:
        '''A reference to a Cluster resource.

        :param cluster_arn: The ClusterArn of the Cluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53recoverycontrol as interfaces_route53recoverycontrol
            
            cluster_reference = interfaces_route53recoverycontrol.ClusterReference(
                cluster_arn="clusterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46872316b94e76798e953517db575f1b0ffa8b517272545ee2c95a5770e2e786)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
        }

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The ClusterArn of the Cluster resource.'''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoverycontrol.ControlPanelReference",
    jsii_struct_bases=[],
    name_mapping={"control_panel_arn": "controlPanelArn"},
)
class ControlPanelReference:
    def __init__(self, *, control_panel_arn: builtins.str) -> None:
        '''A reference to a ControlPanel resource.

        :param control_panel_arn: The ControlPanelArn of the ControlPanel resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53recoverycontrol as interfaces_route53recoverycontrol
            
            control_panel_reference = interfaces_route53recoverycontrol.ControlPanelReference(
                control_panel_arn="controlPanelArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e13533961e7f00349c3f489aa2ccb43d3bea34fc8803c5b5d5c0d6b30d7249)
            check_type(argname="argument control_panel_arn", value=control_panel_arn, expected_type=type_hints["control_panel_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "control_panel_arn": control_panel_arn,
        }

    @builtins.property
    def control_panel_arn(self) -> builtins.str:
        '''The ControlPanelArn of the ControlPanel resource.'''
        result = self._values.get("control_panel_arn")
        assert result is not None, "Required property 'control_panel_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ControlPanelReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoverycontrol.IClusterRef"
)
class IClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Cluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        ...


class _IClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Cluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53recoverycontrol.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoverycontrol.IControlPanelRef"
)
class IControlPanelRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ControlPanel.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="controlPanelRef")
    def control_panel_ref(self) -> "ControlPanelReference":
        '''(experimental) A reference to a ControlPanel resource.

        :stability: experimental
        '''
        ...


class _IControlPanelRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ControlPanel.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53recoverycontrol.IControlPanelRef"

    @builtins.property
    @jsii.member(jsii_name="controlPanelRef")
    def control_panel_ref(self) -> "ControlPanelReference":
        '''(experimental) A reference to a ControlPanel resource.

        :stability: experimental
        '''
        return typing.cast("ControlPanelReference", jsii.get(self, "controlPanelRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IControlPanelRef).__jsii_proxy_class__ = lambda : _IControlPanelRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoverycontrol.IRoutingControlRef"
)
class IRoutingControlRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RoutingControl.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routingControlRef")
    def routing_control_ref(self) -> "RoutingControlReference":
        '''(experimental) A reference to a RoutingControl resource.

        :stability: experimental
        '''
        ...


class _IRoutingControlRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RoutingControl.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53recoverycontrol.IRoutingControlRef"

    @builtins.property
    @jsii.member(jsii_name="routingControlRef")
    def routing_control_ref(self) -> "RoutingControlReference":
        '''(experimental) A reference to a RoutingControl resource.

        :stability: experimental
        '''
        return typing.cast("RoutingControlReference", jsii.get(self, "routingControlRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRoutingControlRef).__jsii_proxy_class__ = lambda : _IRoutingControlRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoverycontrol.ISafetyRuleRef"
)
class ISafetyRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SafetyRule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="safetyRuleRef")
    def safety_rule_ref(self) -> "SafetyRuleReference":
        '''(experimental) A reference to a SafetyRule resource.

        :stability: experimental
        '''
        ...


class _ISafetyRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SafetyRule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_route53recoverycontrol.ISafetyRuleRef"

    @builtins.property
    @jsii.member(jsii_name="safetyRuleRef")
    def safety_rule_ref(self) -> "SafetyRuleReference":
        '''(experimental) A reference to a SafetyRule resource.

        :stability: experimental
        '''
        return typing.cast("SafetyRuleReference", jsii.get(self, "safetyRuleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISafetyRuleRef).__jsii_proxy_class__ = lambda : _ISafetyRuleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoverycontrol.RoutingControlReference",
    jsii_struct_bases=[],
    name_mapping={"routing_control_arn": "routingControlArn"},
)
class RoutingControlReference:
    def __init__(self, *, routing_control_arn: builtins.str) -> None:
        '''A reference to a RoutingControl resource.

        :param routing_control_arn: The RoutingControlArn of the RoutingControl resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53recoverycontrol as interfaces_route53recoverycontrol
            
            routing_control_reference = interfaces_route53recoverycontrol.RoutingControlReference(
                routing_control_arn="routingControlArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f897bde02ed612039eb8e1bb3180a4a89f2eb0bfde83e34cc1d52103eea37a4d)
            check_type(argname="argument routing_control_arn", value=routing_control_arn, expected_type=type_hints["routing_control_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "routing_control_arn": routing_control_arn,
        }

    @builtins.property
    def routing_control_arn(self) -> builtins.str:
        '''The RoutingControlArn of the RoutingControl resource.'''
        result = self._values.get("routing_control_arn")
        assert result is not None, "Required property 'routing_control_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoutingControlReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_route53recoverycontrol.SafetyRuleReference",
    jsii_struct_bases=[],
    name_mapping={"safety_rule_arn": "safetyRuleArn"},
)
class SafetyRuleReference:
    def __init__(self, *, safety_rule_arn: builtins.str) -> None:
        '''A reference to a SafetyRule resource.

        :param safety_rule_arn: The SafetyRuleArn of the SafetyRule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_route53recoverycontrol as interfaces_route53recoverycontrol
            
            safety_rule_reference = interfaces_route53recoverycontrol.SafetyRuleReference(
                safety_rule_arn="safetyRuleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c9b8a5d4251f49522e156e6840f8d173913e327325acbe2014a2c3de571da04)
            check_type(argname="argument safety_rule_arn", value=safety_rule_arn, expected_type=type_hints["safety_rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "safety_rule_arn": safety_rule_arn,
        }

    @builtins.property
    def safety_rule_arn(self) -> builtins.str:
        '''The SafetyRuleArn of the SafetyRule resource.'''
        result = self._values.get("safety_rule_arn")
        assert result is not None, "Required property 'safety_rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SafetyRuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ClusterReference",
    "ControlPanelReference",
    "IClusterRef",
    "IControlPanelRef",
    "IRoutingControlRef",
    "ISafetyRuleRef",
    "RoutingControlReference",
    "SafetyRuleReference",
]

publication.publish()

def _typecheckingstub__46872316b94e76798e953517db575f1b0ffa8b517272545ee2c95a5770e2e786(
    *,
    cluster_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e13533961e7f00349c3f489aa2ccb43d3bea34fc8803c5b5d5c0d6b30d7249(
    *,
    control_panel_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f897bde02ed612039eb8e1bb3180a4a89f2eb0bfde83e34cc1d52103eea37a4d(
    *,
    routing_control_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c9b8a5d4251f49522e156e6840f8d173913e327325acbe2014a2c3de571da04(
    *,
    safety_rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IClusterRef, IControlPanelRef, IRoutingControlRef, ISafetyRuleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
