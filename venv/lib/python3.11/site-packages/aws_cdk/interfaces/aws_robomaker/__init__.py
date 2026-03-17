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
    jsii_type="aws-cdk-lib.interfaces.aws_robomaker.FleetReference",
    jsii_struct_bases=[],
    name_mapping={"fleet_arn": "fleetArn"},
)
class FleetReference:
    def __init__(self, *, fleet_arn: builtins.str) -> None:
        '''A reference to a Fleet resource.

        :param fleet_arn: The ARN of the Fleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_robomaker as interfaces_robomaker
            
            fleet_reference = interfaces_robomaker.FleetReference(
                fleet_arn="fleetArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c10993338f88da3005ff431bd1293ac217565719cf7233001fba0d736c42349)
            check_type(argname="argument fleet_arn", value=fleet_arn, expected_type=type_hints["fleet_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fleet_arn": fleet_arn,
        }

    @builtins.property
    def fleet_arn(self) -> builtins.str:
        '''The ARN of the Fleet resource.'''
        result = self._values.get("fleet_arn")
        assert result is not None, "Required property 'fleet_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_robomaker.IFleetRef")
class IFleetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Fleet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        ...


class _IFleetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Fleet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_robomaker.IFleetRef"

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        return typing.cast("FleetReference", jsii.get(self, "fleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFleetRef).__jsii_proxy_class__ = lambda : _IFleetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_robomaker.IRobotApplicationRef")
class IRobotApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RobotApplication.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="robotApplicationRef")
    def robot_application_ref(self) -> "RobotApplicationReference":
        '''(experimental) A reference to a RobotApplication resource.

        :stability: experimental
        '''
        ...


class _IRobotApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RobotApplication.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_robomaker.IRobotApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="robotApplicationRef")
    def robot_application_ref(self) -> "RobotApplicationReference":
        '''(experimental) A reference to a RobotApplication resource.

        :stability: experimental
        '''
        return typing.cast("RobotApplicationReference", jsii.get(self, "robotApplicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRobotApplicationRef).__jsii_proxy_class__ = lambda : _IRobotApplicationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_robomaker.IRobotApplicationVersionRef"
)
class IRobotApplicationVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RobotApplicationVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="robotApplicationVersionRef")
    def robot_application_version_ref(self) -> "RobotApplicationVersionReference":
        '''(experimental) A reference to a RobotApplicationVersion resource.

        :stability: experimental
        '''
        ...


class _IRobotApplicationVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RobotApplicationVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_robomaker.IRobotApplicationVersionRef"

    @builtins.property
    @jsii.member(jsii_name="robotApplicationVersionRef")
    def robot_application_version_ref(self) -> "RobotApplicationVersionReference":
        '''(experimental) A reference to a RobotApplicationVersion resource.

        :stability: experimental
        '''
        return typing.cast("RobotApplicationVersionReference", jsii.get(self, "robotApplicationVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRobotApplicationVersionRef).__jsii_proxy_class__ = lambda : _IRobotApplicationVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_robomaker.IRobotRef")
class IRobotRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Robot.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="robotRef")
    def robot_ref(self) -> "RobotReference":
        '''(experimental) A reference to a Robot resource.

        :stability: experimental
        '''
        ...


class _IRobotRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Robot.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_robomaker.IRobotRef"

    @builtins.property
    @jsii.member(jsii_name="robotRef")
    def robot_ref(self) -> "RobotReference":
        '''(experimental) A reference to a Robot resource.

        :stability: experimental
        '''
        return typing.cast("RobotReference", jsii.get(self, "robotRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRobotRef).__jsii_proxy_class__ = lambda : _IRobotRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_robomaker.ISimulationApplicationRef"
)
class ISimulationApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SimulationApplication.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="simulationApplicationRef")
    def simulation_application_ref(self) -> "SimulationApplicationReference":
        '''(experimental) A reference to a SimulationApplication resource.

        :stability: experimental
        '''
        ...


class _ISimulationApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SimulationApplication.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_robomaker.ISimulationApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="simulationApplicationRef")
    def simulation_application_ref(self) -> "SimulationApplicationReference":
        '''(experimental) A reference to a SimulationApplication resource.

        :stability: experimental
        '''
        return typing.cast("SimulationApplicationReference", jsii.get(self, "simulationApplicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISimulationApplicationRef).__jsii_proxy_class__ = lambda : _ISimulationApplicationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_robomaker.ISimulationApplicationVersionRef"
)
class ISimulationApplicationVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SimulationApplicationVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="simulationApplicationVersionRef")
    def simulation_application_version_ref(
        self,
    ) -> "SimulationApplicationVersionReference":
        '''(experimental) A reference to a SimulationApplicationVersion resource.

        :stability: experimental
        '''
        ...


class _ISimulationApplicationVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SimulationApplicationVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_robomaker.ISimulationApplicationVersionRef"

    @builtins.property
    @jsii.member(jsii_name="simulationApplicationVersionRef")
    def simulation_application_version_ref(
        self,
    ) -> "SimulationApplicationVersionReference":
        '''(experimental) A reference to a SimulationApplicationVersion resource.

        :stability: experimental
        '''
        return typing.cast("SimulationApplicationVersionReference", jsii.get(self, "simulationApplicationVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISimulationApplicationVersionRef).__jsii_proxy_class__ = lambda : _ISimulationApplicationVersionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_robomaker.RobotApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"robot_application_arn": "robotApplicationArn"},
)
class RobotApplicationReference:
    def __init__(self, *, robot_application_arn: builtins.str) -> None:
        '''A reference to a RobotApplication resource.

        :param robot_application_arn: The ARN of the RobotApplication resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_robomaker as interfaces_robomaker
            
            robot_application_reference = interfaces_robomaker.RobotApplicationReference(
                robot_application_arn="robotApplicationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d23a14f4bd33e81173681bcb6adceba86d56d1d45110a8a9a779ce4f79f197d1)
            check_type(argname="argument robot_application_arn", value=robot_application_arn, expected_type=type_hints["robot_application_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "robot_application_arn": robot_application_arn,
        }

    @builtins.property
    def robot_application_arn(self) -> builtins.str:
        '''The ARN of the RobotApplication resource.'''
        result = self._values.get("robot_application_arn")
        assert result is not None, "Required property 'robot_application_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RobotApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_robomaker.RobotApplicationVersionReference",
    jsii_struct_bases=[],
    name_mapping={"robot_application_version_arn": "robotApplicationVersionArn"},
)
class RobotApplicationVersionReference:
    def __init__(self, *, robot_application_version_arn: builtins.str) -> None:
        '''A reference to a RobotApplicationVersion resource.

        :param robot_application_version_arn: The ARN of the RobotApplicationVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_robomaker as interfaces_robomaker
            
            robot_application_version_reference = interfaces_robomaker.RobotApplicationVersionReference(
                robot_application_version_arn="robotApplicationVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b85f04a390b22ad72339608e4c5c5e994d9e507b908b4d4144275932c1c63c4)
            check_type(argname="argument robot_application_version_arn", value=robot_application_version_arn, expected_type=type_hints["robot_application_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "robot_application_version_arn": robot_application_version_arn,
        }

    @builtins.property
    def robot_application_version_arn(self) -> builtins.str:
        '''The ARN of the RobotApplicationVersion resource.'''
        result = self._values.get("robot_application_version_arn")
        assert result is not None, "Required property 'robot_application_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RobotApplicationVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_robomaker.RobotReference",
    jsii_struct_bases=[],
    name_mapping={"robot_arn": "robotArn"},
)
class RobotReference:
    def __init__(self, *, robot_arn: builtins.str) -> None:
        '''A reference to a Robot resource.

        :param robot_arn: The ARN of the Robot resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_robomaker as interfaces_robomaker
            
            robot_reference = interfaces_robomaker.RobotReference(
                robot_arn="robotArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d56761450f42bbcda4d23cda262f89cd6605562342aa078b57ae7f3eef01dc8d)
            check_type(argname="argument robot_arn", value=robot_arn, expected_type=type_hints["robot_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "robot_arn": robot_arn,
        }

    @builtins.property
    def robot_arn(self) -> builtins.str:
        '''The ARN of the Robot resource.'''
        result = self._values.get("robot_arn")
        assert result is not None, "Required property 'robot_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RobotReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_robomaker.SimulationApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"simulation_application_arn": "simulationApplicationArn"},
)
class SimulationApplicationReference:
    def __init__(self, *, simulation_application_arn: builtins.str) -> None:
        '''A reference to a SimulationApplication resource.

        :param simulation_application_arn: The ARN of the SimulationApplication resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_robomaker as interfaces_robomaker
            
            simulation_application_reference = interfaces_robomaker.SimulationApplicationReference(
                simulation_application_arn="simulationApplicationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c65622433df6db7b8e0e69e679efa8445482ea622b0fc2de89670155cc597724)
            check_type(argname="argument simulation_application_arn", value=simulation_application_arn, expected_type=type_hints["simulation_application_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "simulation_application_arn": simulation_application_arn,
        }

    @builtins.property
    def simulation_application_arn(self) -> builtins.str:
        '''The ARN of the SimulationApplication resource.'''
        result = self._values.get("simulation_application_arn")
        assert result is not None, "Required property 'simulation_application_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SimulationApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_robomaker.SimulationApplicationVersionReference",
    jsii_struct_bases=[],
    name_mapping={
        "simulation_application_version_arn": "simulationApplicationVersionArn",
    },
)
class SimulationApplicationVersionReference:
    def __init__(self, *, simulation_application_version_arn: builtins.str) -> None:
        '''A reference to a SimulationApplicationVersion resource.

        :param simulation_application_version_arn: The ARN of the SimulationApplicationVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_robomaker as interfaces_robomaker
            
            simulation_application_version_reference = interfaces_robomaker.SimulationApplicationVersionReference(
                simulation_application_version_arn="simulationApplicationVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__320cab997c649735c78587849b0c8b0fff36beca8328ce313fc35609cc8e5ef1)
            check_type(argname="argument simulation_application_version_arn", value=simulation_application_version_arn, expected_type=type_hints["simulation_application_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "simulation_application_version_arn": simulation_application_version_arn,
        }

    @builtins.property
    def simulation_application_version_arn(self) -> builtins.str:
        '''The ARN of the SimulationApplicationVersion resource.'''
        result = self._values.get("simulation_application_version_arn")
        assert result is not None, "Required property 'simulation_application_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SimulationApplicationVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "FleetReference",
    "IFleetRef",
    "IRobotApplicationRef",
    "IRobotApplicationVersionRef",
    "IRobotRef",
    "ISimulationApplicationRef",
    "ISimulationApplicationVersionRef",
    "RobotApplicationReference",
    "RobotApplicationVersionReference",
    "RobotReference",
    "SimulationApplicationReference",
    "SimulationApplicationVersionReference",
]

publication.publish()

def _typecheckingstub__7c10993338f88da3005ff431bd1293ac217565719cf7233001fba0d736c42349(
    *,
    fleet_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d23a14f4bd33e81173681bcb6adceba86d56d1d45110a8a9a779ce4f79f197d1(
    *,
    robot_application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b85f04a390b22ad72339608e4c5c5e994d9e507b908b4d4144275932c1c63c4(
    *,
    robot_application_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d56761450f42bbcda4d23cda262f89cd6605562342aa078b57ae7f3eef01dc8d(
    *,
    robot_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c65622433df6db7b8e0e69e679efa8445482ea622b0fc2de89670155cc597724(
    *,
    simulation_application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320cab997c649735c78587849b0c8b0fff36beca8328ce313fc35609cc8e5ef1(
    *,
    simulation_application_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IFleetRef, IRobotApplicationRef, IRobotApplicationVersionRef, IRobotRef, ISimulationApplicationRef, ISimulationApplicationVersionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
