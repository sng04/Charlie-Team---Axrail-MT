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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_simspaceweaver.ISimulationRef")
class ISimulationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Simulation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="simulationRef")
    def simulation_ref(self) -> "SimulationReference":
        '''(experimental) A reference to a Simulation resource.

        :stability: experimental
        '''
        ...


class _ISimulationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Simulation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_simspaceweaver.ISimulationRef"

    @builtins.property
    @jsii.member(jsii_name="simulationRef")
    def simulation_ref(self) -> "SimulationReference":
        '''(experimental) A reference to a Simulation resource.

        :stability: experimental
        '''
        return typing.cast("SimulationReference", jsii.get(self, "simulationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISimulationRef).__jsii_proxy_class__ = lambda : _ISimulationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_simspaceweaver.SimulationReference",
    jsii_struct_bases=[],
    name_mapping={"simulation_name": "simulationName"},
)
class SimulationReference:
    def __init__(self, *, simulation_name: builtins.str) -> None:
        '''A reference to a Simulation resource.

        :param simulation_name: The Name of the Simulation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_simspaceweaver as interfaces_simspaceweaver
            
            simulation_reference = interfaces_simspaceweaver.SimulationReference(
                simulation_name="simulationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3756cce6ce9c0f5ec8a6806766cff2d154f6366b86789398e96f9d66c9b8bbb2)
            check_type(argname="argument simulation_name", value=simulation_name, expected_type=type_hints["simulation_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "simulation_name": simulation_name,
        }

    @builtins.property
    def simulation_name(self) -> builtins.str:
        '''The Name of the Simulation resource.'''
        result = self._values.get("simulation_name")
        assert result is not None, "Required property 'simulation_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SimulationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ISimulationRef",
    "SimulationReference",
]

publication.publish()

def _typecheckingstub__3756cce6ce9c0f5ec8a6806766cff2d154f6366b86789398e96f9d66c9b8bbb2(
    *,
    simulation_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ISimulationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
