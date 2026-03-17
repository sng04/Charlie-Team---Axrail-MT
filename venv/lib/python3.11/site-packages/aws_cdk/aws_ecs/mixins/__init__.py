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
from .. import CfnCluster as _CfnCluster_8e709f8b
from ... import Mixin as _Mixin_d3d231df


class ClusterSettings(
    _Mixin_d3d231df,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ecs.mixins.ClusterSettings",
):
    '''Applies one or more cluster settings to an ECS cluster.

    If a setting with the same name already exists, its value is replaced.

    :exampleMetadata: infused

    Example::

        ecs.CfnCluster(self, "Cluster").with(ecs.mixins.ClusterSettings([name="containerInsights", value="enhanced"]))
    '''

    def __init__(
        self,
        settings: typing.Sequence[typing.Union["_CfnCluster_8e709f8b.ClusterSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param settings: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__330f6d3486223a52f5a9301c591ff3cfe4883f1d51f8ce905443a08bb36647d5)
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
        jsii.create(self.__class__, self, [settings])

    @jsii.member(jsii_name="applyTo")
    def apply_to(self, cluster: "_constructs_77d1e7e8.IConstruct") -> None:
        '''Applies the mixin functionality to the target construct.

        :param cluster: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb87ac656b0fc6c6c1f39c76c38e76a9578388765834a1eb500892a5ea99995d)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        return typing.cast(None, jsii.invoke(self, "applyTo", [cluster]))

    @jsii.member(jsii_name="supports")
    def supports(self, construct: "_constructs_77d1e7e8.IConstruct") -> builtins.bool:
        '''Determines whether this mixin can be applied to the given construct.

        :param construct: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__248294cdc37e84b78b4b04f9c8084680fbe83e1bb5e8432efc1cc19b1d8e9d29)
            check_type(argname="argument construct", value=construct, expected_type=type_hints["construct"])
        return typing.cast(builtins.bool, jsii.invoke(self, "supports", [construct]))


__all__ = [
    "ClusterSettings",
]

publication.publish()

def _typecheckingstub__330f6d3486223a52f5a9301c591ff3cfe4883f1d51f8ce905443a08bb36647d5(
    settings: typing.Sequence[typing.Union[_CfnCluster_8e709f8b.ClusterSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb87ac656b0fc6c6c1f39c76c38e76a9578388765834a1eb500892a5ea99995d(
    cluster: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__248294cdc37e84b78b4b04f9c8084680fbe83e1bb5e8432efc1cc19b1d8e9d29(
    construct: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass
