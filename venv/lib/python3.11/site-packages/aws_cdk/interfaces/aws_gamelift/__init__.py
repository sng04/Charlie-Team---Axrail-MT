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
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.AliasReference",
    jsii_struct_bases=[],
    name_mapping={"alias_arn": "aliasArn", "alias_id": "aliasId"},
)
class AliasReference:
    def __init__(self, *, alias_arn: builtins.str, alias_id: builtins.str) -> None:
        '''A reference to a Alias resource.

        :param alias_arn: The ARN of the Alias resource.
        :param alias_id: The AliasId of the Alias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            alias_reference = interfaces_gamelift.AliasReference(
                alias_arn="aliasArn",
                alias_id="aliasId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81545cc04bebd1b6f40300f3243d262a46f42800620f495f5a38d3781e273702)
            check_type(argname="argument alias_arn", value=alias_arn, expected_type=type_hints["alias_arn"])
            check_type(argname="argument alias_id", value=alias_id, expected_type=type_hints["alias_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias_arn": alias_arn,
            "alias_id": alias_id,
        }

    @builtins.property
    def alias_arn(self) -> builtins.str:
        '''The ARN of the Alias resource.'''
        result = self._values.get("alias_arn")
        assert result is not None, "Required property 'alias_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias_id(self) -> builtins.str:
        '''The AliasId of the Alias resource.'''
        result = self._values.get("alias_id")
        assert result is not None, "Required property 'alias_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.BuildReference",
    jsii_struct_bases=[],
    name_mapping={"build_arn": "buildArn", "build_id": "buildId"},
)
class BuildReference:
    def __init__(self, *, build_arn: builtins.str, build_id: builtins.str) -> None:
        '''A reference to a Build resource.

        :param build_arn: The ARN of the Build resource.
        :param build_id: The BuildId of the Build resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            build_reference = interfaces_gamelift.BuildReference(
                build_arn="buildArn",
                build_id="buildId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e39afd357979864cdb0a0e965025e9600edb7d1d723c5d80bd567e33674e4ad4)
            check_type(argname="argument build_arn", value=build_arn, expected_type=type_hints["build_arn"])
            check_type(argname="argument build_id", value=build_id, expected_type=type_hints["build_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "build_arn": build_arn,
            "build_id": build_id,
        }

    @builtins.property
    def build_arn(self) -> builtins.str:
        '''The ARN of the Build resource.'''
        result = self._values.get("build_arn")
        assert result is not None, "Required property 'build_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def build_id(self) -> builtins.str:
        '''The BuildId of the Build resource.'''
        result = self._values.get("build_id")
        assert result is not None, "Required property 'build_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BuildReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.ContainerFleetReference",
    jsii_struct_bases=[],
    name_mapping={"fleet_arn": "fleetArn", "fleet_id": "fleetId"},
)
class ContainerFleetReference:
    def __init__(self, *, fleet_arn: builtins.str, fleet_id: builtins.str) -> None:
        '''A reference to a ContainerFleet resource.

        :param fleet_arn: The ARN of the ContainerFleet resource.
        :param fleet_id: The FleetId of the ContainerFleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            container_fleet_reference = interfaces_gamelift.ContainerFleetReference(
                fleet_arn="fleetArn",
                fleet_id="fleetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16c358839d20499f02bc5631233f96eaee22a25eb9ec5256f6a4d30651735d82)
            check_type(argname="argument fleet_arn", value=fleet_arn, expected_type=type_hints["fleet_arn"])
            check_type(argname="argument fleet_id", value=fleet_id, expected_type=type_hints["fleet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fleet_arn": fleet_arn,
            "fleet_id": fleet_id,
        }

    @builtins.property
    def fleet_arn(self) -> builtins.str:
        '''The ARN of the ContainerFleet resource.'''
        result = self._values.get("fleet_arn")
        assert result is not None, "Required property 'fleet_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fleet_id(self) -> builtins.str:
        '''The FleetId of the ContainerFleet resource.'''
        result = self._values.get("fleet_id")
        assert result is not None, "Required property 'fleet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerFleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.ContainerGroupDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "container_group_definition_arn": "containerGroupDefinitionArn",
        "container_group_definition_name": "containerGroupDefinitionName",
    },
)
class ContainerGroupDefinitionReference:
    def __init__(
        self,
        *,
        container_group_definition_arn: builtins.str,
        container_group_definition_name: builtins.str,
    ) -> None:
        '''A reference to a ContainerGroupDefinition resource.

        :param container_group_definition_arn: The ARN of the ContainerGroupDefinition resource.
        :param container_group_definition_name: The Name of the ContainerGroupDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            container_group_definition_reference = interfaces_gamelift.ContainerGroupDefinitionReference(
                container_group_definition_arn="containerGroupDefinitionArn",
                container_group_definition_name="containerGroupDefinitionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c4025f74a8de88eb68bdfa436229cb4bd5b891982aea5a4f8f68d5c1b15ba09)
            check_type(argname="argument container_group_definition_arn", value=container_group_definition_arn, expected_type=type_hints["container_group_definition_arn"])
            check_type(argname="argument container_group_definition_name", value=container_group_definition_name, expected_type=type_hints["container_group_definition_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_group_definition_arn": container_group_definition_arn,
            "container_group_definition_name": container_group_definition_name,
        }

    @builtins.property
    def container_group_definition_arn(self) -> builtins.str:
        '''The ARN of the ContainerGroupDefinition resource.'''
        result = self._values.get("container_group_definition_arn")
        assert result is not None, "Required property 'container_group_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_group_definition_name(self) -> builtins.str:
        '''The Name of the ContainerGroupDefinition resource.'''
        result = self._values.get("container_group_definition_name")
        assert result is not None, "Required property 'container_group_definition_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContainerGroupDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.FleetReference",
    jsii_struct_bases=[],
    name_mapping={"fleet_arn": "fleetArn", "fleet_id": "fleetId"},
)
class FleetReference:
    def __init__(self, *, fleet_arn: builtins.str, fleet_id: builtins.str) -> None:
        '''A reference to a Fleet resource.

        :param fleet_arn: The ARN of the Fleet resource.
        :param fleet_id: The FleetId of the Fleet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            fleet_reference = interfaces_gamelift.FleetReference(
                fleet_arn="fleetArn",
                fleet_id="fleetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14a0761deedfe27c2952d83b765671e1f2d64083fd6d00eeb8fa9cdcc6666860)
            check_type(argname="argument fleet_arn", value=fleet_arn, expected_type=type_hints["fleet_arn"])
            check_type(argname="argument fleet_id", value=fleet_id, expected_type=type_hints["fleet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fleet_arn": fleet_arn,
            "fleet_id": fleet_id,
        }

    @builtins.property
    def fleet_arn(self) -> builtins.str:
        '''The ARN of the Fleet resource.'''
        result = self._values.get("fleet_arn")
        assert result is not None, "Required property 'fleet_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fleet_id(self) -> builtins.str:
        '''The FleetId of the Fleet resource.'''
        result = self._values.get("fleet_id")
        assert result is not None, "Required property 'fleet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FleetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.GameServerGroupReference",
    jsii_struct_bases=[],
    name_mapping={"game_server_group_arn": "gameServerGroupArn"},
)
class GameServerGroupReference:
    def __init__(self, *, game_server_group_arn: builtins.str) -> None:
        '''A reference to a GameServerGroup resource.

        :param game_server_group_arn: The GameServerGroupArn of the GameServerGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            game_server_group_reference = interfaces_gamelift.GameServerGroupReference(
                game_server_group_arn="gameServerGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eed49d51771b830d643a4e4ffadaabeece46b2073ce63973239c01c9ae06f8b9)
            check_type(argname="argument game_server_group_arn", value=game_server_group_arn, expected_type=type_hints["game_server_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "game_server_group_arn": game_server_group_arn,
        }

    @builtins.property
    def game_server_group_arn(self) -> builtins.str:
        '''The GameServerGroupArn of the GameServerGroup resource.'''
        result = self._values.get("game_server_group_arn")
        assert result is not None, "Required property 'game_server_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GameServerGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.GameSessionQueueReference",
    jsii_struct_bases=[],
    name_mapping={
        "game_session_queue_arn": "gameSessionQueueArn",
        "game_session_queue_name": "gameSessionQueueName",
    },
)
class GameSessionQueueReference:
    def __init__(
        self,
        *,
        game_session_queue_arn: builtins.str,
        game_session_queue_name: builtins.str,
    ) -> None:
        '''A reference to a GameSessionQueue resource.

        :param game_session_queue_arn: The ARN of the GameSessionQueue resource.
        :param game_session_queue_name: The Name of the GameSessionQueue resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            game_session_queue_reference = interfaces_gamelift.GameSessionQueueReference(
                game_session_queue_arn="gameSessionQueueArn",
                game_session_queue_name="gameSessionQueueName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaba6b78f225d34505e094f1ef37186fa6df83a00d620b1928d86b244926c808)
            check_type(argname="argument game_session_queue_arn", value=game_session_queue_arn, expected_type=type_hints["game_session_queue_arn"])
            check_type(argname="argument game_session_queue_name", value=game_session_queue_name, expected_type=type_hints["game_session_queue_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "game_session_queue_arn": game_session_queue_arn,
            "game_session_queue_name": game_session_queue_name,
        }

    @builtins.property
    def game_session_queue_arn(self) -> builtins.str:
        '''The ARN of the GameSessionQueue resource.'''
        result = self._values.get("game_session_queue_arn")
        assert result is not None, "Required property 'game_session_queue_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def game_session_queue_name(self) -> builtins.str:
        '''The Name of the GameSessionQueue resource.'''
        result = self._values.get("game_session_queue_name")
        assert result is not None, "Required property 'game_session_queue_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GameSessionQueueReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gamelift.IAliasRef")
class IAliasRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Alias.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aliasRef")
    def alias_ref(self) -> "AliasReference":
        '''(experimental) A reference to a Alias resource.

        :stability: experimental
        '''
        ...


class _IAliasRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Alias.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.IAliasRef"

    @builtins.property
    @jsii.member(jsii_name="aliasRef")
    def alias_ref(self) -> "AliasReference":
        '''(experimental) A reference to a Alias resource.

        :stability: experimental
        '''
        return typing.cast("AliasReference", jsii.get(self, "aliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAliasRef).__jsii_proxy_class__ = lambda : _IAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gamelift.IBuildRef")
class IBuildRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Build.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="buildRef")
    def build_ref(self) -> "BuildReference":
        '''(experimental) A reference to a Build resource.

        :stability: experimental
        '''
        ...


class _IBuildRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Build.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.IBuildRef"

    @builtins.property
    @jsii.member(jsii_name="buildRef")
    def build_ref(self) -> "BuildReference":
        '''(experimental) A reference to a Build resource.

        :stability: experimental
        '''
        return typing.cast("BuildReference", jsii.get(self, "buildRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBuildRef).__jsii_proxy_class__ = lambda : _IBuildRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gamelift.IContainerFleetRef")
class IContainerFleetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContainerFleet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="containerFleetRef")
    def container_fleet_ref(self) -> "ContainerFleetReference":
        '''(experimental) A reference to a ContainerFleet resource.

        :stability: experimental
        '''
        ...


class _IContainerFleetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContainerFleet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.IContainerFleetRef"

    @builtins.property
    @jsii.member(jsii_name="containerFleetRef")
    def container_fleet_ref(self) -> "ContainerFleetReference":
        '''(experimental) A reference to a ContainerFleet resource.

        :stability: experimental
        '''
        return typing.cast("ContainerFleetReference", jsii.get(self, "containerFleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContainerFleetRef).__jsii_proxy_class__ = lambda : _IContainerFleetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.IContainerGroupDefinitionRef"
)
class IContainerGroupDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ContainerGroupDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="containerGroupDefinitionRef")
    def container_group_definition_ref(self) -> "ContainerGroupDefinitionReference":
        '''(experimental) A reference to a ContainerGroupDefinition resource.

        :stability: experimental
        '''
        ...


class _IContainerGroupDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ContainerGroupDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.IContainerGroupDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="containerGroupDefinitionRef")
    def container_group_definition_ref(self) -> "ContainerGroupDefinitionReference":
        '''(experimental) A reference to a ContainerGroupDefinition resource.

        :stability: experimental
        '''
        return typing.cast("ContainerGroupDefinitionReference", jsii.get(self, "containerGroupDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IContainerGroupDefinitionRef).__jsii_proxy_class__ = lambda : _IContainerGroupDefinitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gamelift.IFleetRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.IFleetRef"

    @builtins.property
    @jsii.member(jsii_name="fleetRef")
    def fleet_ref(self) -> "FleetReference":
        '''(experimental) A reference to a Fleet resource.

        :stability: experimental
        '''
        return typing.cast("FleetReference", jsii.get(self, "fleetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFleetRef).__jsii_proxy_class__ = lambda : _IFleetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gamelift.IGameServerGroupRef")
class IGameServerGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GameServerGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gameServerGroupRef")
    def game_server_group_ref(self) -> "GameServerGroupReference":
        '''(experimental) A reference to a GameServerGroup resource.

        :stability: experimental
        '''
        ...


class _IGameServerGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GameServerGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.IGameServerGroupRef"

    @builtins.property
    @jsii.member(jsii_name="gameServerGroupRef")
    def game_server_group_ref(self) -> "GameServerGroupReference":
        '''(experimental) A reference to a GameServerGroup resource.

        :stability: experimental
        '''
        return typing.cast("GameServerGroupReference", jsii.get(self, "gameServerGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGameServerGroupRef).__jsii_proxy_class__ = lambda : _IGameServerGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gamelift.IGameSessionQueueRef")
class IGameSessionQueueRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GameSessionQueue.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="gameSessionQueueRef")
    def game_session_queue_ref(self) -> "GameSessionQueueReference":
        '''(experimental) A reference to a GameSessionQueue resource.

        :stability: experimental
        '''
        ...


class _IGameSessionQueueRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GameSessionQueue.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.IGameSessionQueueRef"

    @builtins.property
    @jsii.member(jsii_name="gameSessionQueueRef")
    def game_session_queue_ref(self) -> "GameSessionQueueReference":
        '''(experimental) A reference to a GameSessionQueue resource.

        :stability: experimental
        '''
        return typing.cast("GameSessionQueueReference", jsii.get(self, "gameSessionQueueRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGameSessionQueueRef).__jsii_proxy_class__ = lambda : _IGameSessionQueueRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gamelift.ILocationRef")
class ILocationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Location.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="locationRef")
    def location_ref(self) -> "LocationReference":
        '''(experimental) A reference to a Location resource.

        :stability: experimental
        '''
        ...


class _ILocationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Location.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.ILocationRef"

    @builtins.property
    @jsii.member(jsii_name="locationRef")
    def location_ref(self) -> "LocationReference":
        '''(experimental) A reference to a Location resource.

        :stability: experimental
        '''
        return typing.cast("LocationReference", jsii.get(self, "locationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILocationRef).__jsii_proxy_class__ = lambda : _ILocationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.IMatchmakingConfigurationRef"
)
class IMatchmakingConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MatchmakingConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="matchmakingConfigurationRef")
    def matchmaking_configuration_ref(self) -> "MatchmakingConfigurationReference":
        '''(experimental) A reference to a MatchmakingConfiguration resource.

        :stability: experimental
        '''
        ...


class _IMatchmakingConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MatchmakingConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.IMatchmakingConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="matchmakingConfigurationRef")
    def matchmaking_configuration_ref(self) -> "MatchmakingConfigurationReference":
        '''(experimental) A reference to a MatchmakingConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("MatchmakingConfigurationReference", jsii.get(self, "matchmakingConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMatchmakingConfigurationRef).__jsii_proxy_class__ = lambda : _IMatchmakingConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gamelift.IMatchmakingRuleSetRef")
class IMatchmakingRuleSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MatchmakingRuleSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="matchmakingRuleSetRef")
    def matchmaking_rule_set_ref(self) -> "MatchmakingRuleSetReference":
        '''(experimental) A reference to a MatchmakingRuleSet resource.

        :stability: experimental
        '''
        ...


class _IMatchmakingRuleSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MatchmakingRuleSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.IMatchmakingRuleSetRef"

    @builtins.property
    @jsii.member(jsii_name="matchmakingRuleSetRef")
    def matchmaking_rule_set_ref(self) -> "MatchmakingRuleSetReference":
        '''(experimental) A reference to a MatchmakingRuleSet resource.

        :stability: experimental
        '''
        return typing.cast("MatchmakingRuleSetReference", jsii.get(self, "matchmakingRuleSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMatchmakingRuleSetRef).__jsii_proxy_class__ = lambda : _IMatchmakingRuleSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_gamelift.IScriptRef")
class IScriptRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Script.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="scriptRef")
    def script_ref(self) -> "ScriptReference":
        '''(experimental) A reference to a Script resource.

        :stability: experimental
        '''
        ...


class _IScriptRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Script.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_gamelift.IScriptRef"

    @builtins.property
    @jsii.member(jsii_name="scriptRef")
    def script_ref(self) -> "ScriptReference":
        '''(experimental) A reference to a Script resource.

        :stability: experimental
        '''
        return typing.cast("ScriptReference", jsii.get(self, "scriptRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IScriptRef).__jsii_proxy_class__ = lambda : _IScriptRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.LocationReference",
    jsii_struct_bases=[],
    name_mapping={"location_arn": "locationArn", "location_name": "locationName"},
)
class LocationReference:
    def __init__(
        self,
        *,
        location_arn: builtins.str,
        location_name: builtins.str,
    ) -> None:
        '''A reference to a Location resource.

        :param location_arn: The ARN of the Location resource.
        :param location_name: The LocationName of the Location resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            location_reference = interfaces_gamelift.LocationReference(
                location_arn="locationArn",
                location_name="locationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d38962f536753d3d7e3ec8c20ecce982e21a10ac85e69ccfd9291df9452cdb2b)
            check_type(argname="argument location_arn", value=location_arn, expected_type=type_hints["location_arn"])
            check_type(argname="argument location_name", value=location_name, expected_type=type_hints["location_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_arn": location_arn,
            "location_name": location_name,
        }

    @builtins.property
    def location_arn(self) -> builtins.str:
        '''The ARN of the Location resource.'''
        result = self._values.get("location_arn")
        assert result is not None, "Required property 'location_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_name(self) -> builtins.str:
        '''The LocationName of the Location resource.'''
        result = self._values.get("location_name")
        assert result is not None, "Required property 'location_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LocationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.MatchmakingConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={
        "matchmaking_configuration_arn": "matchmakingConfigurationArn",
        "matchmaking_configuration_name": "matchmakingConfigurationName",
    },
)
class MatchmakingConfigurationReference:
    def __init__(
        self,
        *,
        matchmaking_configuration_arn: builtins.str,
        matchmaking_configuration_name: builtins.str,
    ) -> None:
        '''A reference to a MatchmakingConfiguration resource.

        :param matchmaking_configuration_arn: The ARN of the MatchmakingConfiguration resource.
        :param matchmaking_configuration_name: The Name of the MatchmakingConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            matchmaking_configuration_reference = interfaces_gamelift.MatchmakingConfigurationReference(
                matchmaking_configuration_arn="matchmakingConfigurationArn",
                matchmaking_configuration_name="matchmakingConfigurationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__652b9e6286ea4f923689b277ca538ac65edf1d5dec9f15e4e817dd492c877e95)
            check_type(argname="argument matchmaking_configuration_arn", value=matchmaking_configuration_arn, expected_type=type_hints["matchmaking_configuration_arn"])
            check_type(argname="argument matchmaking_configuration_name", value=matchmaking_configuration_name, expected_type=type_hints["matchmaking_configuration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "matchmaking_configuration_arn": matchmaking_configuration_arn,
            "matchmaking_configuration_name": matchmaking_configuration_name,
        }

    @builtins.property
    def matchmaking_configuration_arn(self) -> builtins.str:
        '''The ARN of the MatchmakingConfiguration resource.'''
        result = self._values.get("matchmaking_configuration_arn")
        assert result is not None, "Required property 'matchmaking_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def matchmaking_configuration_name(self) -> builtins.str:
        '''The Name of the MatchmakingConfiguration resource.'''
        result = self._values.get("matchmaking_configuration_name")
        assert result is not None, "Required property 'matchmaking_configuration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MatchmakingConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.MatchmakingRuleSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "matchmaking_rule_set_arn": "matchmakingRuleSetArn",
        "matchmaking_rule_set_name": "matchmakingRuleSetName",
    },
)
class MatchmakingRuleSetReference:
    def __init__(
        self,
        *,
        matchmaking_rule_set_arn: builtins.str,
        matchmaking_rule_set_name: builtins.str,
    ) -> None:
        '''A reference to a MatchmakingRuleSet resource.

        :param matchmaking_rule_set_arn: The ARN of the MatchmakingRuleSet resource.
        :param matchmaking_rule_set_name: The Name of the MatchmakingRuleSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            matchmaking_rule_set_reference = interfaces_gamelift.MatchmakingRuleSetReference(
                matchmaking_rule_set_arn="matchmakingRuleSetArn",
                matchmaking_rule_set_name="matchmakingRuleSetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ea758ab9c6c55fd32771d207aec1adbbafc4918621fb9f0331df1ff8d72b36e)
            check_type(argname="argument matchmaking_rule_set_arn", value=matchmaking_rule_set_arn, expected_type=type_hints["matchmaking_rule_set_arn"])
            check_type(argname="argument matchmaking_rule_set_name", value=matchmaking_rule_set_name, expected_type=type_hints["matchmaking_rule_set_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "matchmaking_rule_set_arn": matchmaking_rule_set_arn,
            "matchmaking_rule_set_name": matchmaking_rule_set_name,
        }

    @builtins.property
    def matchmaking_rule_set_arn(self) -> builtins.str:
        '''The ARN of the MatchmakingRuleSet resource.'''
        result = self._values.get("matchmaking_rule_set_arn")
        assert result is not None, "Required property 'matchmaking_rule_set_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def matchmaking_rule_set_name(self) -> builtins.str:
        '''The Name of the MatchmakingRuleSet resource.'''
        result = self._values.get("matchmaking_rule_set_name")
        assert result is not None, "Required property 'matchmaking_rule_set_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MatchmakingRuleSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_gamelift.ScriptReference",
    jsii_struct_bases=[],
    name_mapping={"script_arn": "scriptArn", "script_id": "scriptId"},
)
class ScriptReference:
    def __init__(self, *, script_arn: builtins.str, script_id: builtins.str) -> None:
        '''A reference to a Script resource.

        :param script_arn: The ARN of the Script resource.
        :param script_id: The Id of the Script resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_gamelift as interfaces_gamelift
            
            script_reference = interfaces_gamelift.ScriptReference(
                script_arn="scriptArn",
                script_id="scriptId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e937f7ba8775875c3e775c0fe702df7d7e020dc7e88969fe496060f62e3c6094)
            check_type(argname="argument script_arn", value=script_arn, expected_type=type_hints["script_arn"])
            check_type(argname="argument script_id", value=script_id, expected_type=type_hints["script_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "script_arn": script_arn,
            "script_id": script_id,
        }

    @builtins.property
    def script_arn(self) -> builtins.str:
        '''The ARN of the Script resource.'''
        result = self._values.get("script_arn")
        assert result is not None, "Required property 'script_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def script_id(self) -> builtins.str:
        '''The Id of the Script resource.'''
        result = self._values.get("script_id")
        assert result is not None, "Required property 'script_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScriptReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AliasReference",
    "BuildReference",
    "ContainerFleetReference",
    "ContainerGroupDefinitionReference",
    "FleetReference",
    "GameServerGroupReference",
    "GameSessionQueueReference",
    "IAliasRef",
    "IBuildRef",
    "IContainerFleetRef",
    "IContainerGroupDefinitionRef",
    "IFleetRef",
    "IGameServerGroupRef",
    "IGameSessionQueueRef",
    "ILocationRef",
    "IMatchmakingConfigurationRef",
    "IMatchmakingRuleSetRef",
    "IScriptRef",
    "LocationReference",
    "MatchmakingConfigurationReference",
    "MatchmakingRuleSetReference",
    "ScriptReference",
]

publication.publish()

def _typecheckingstub__81545cc04bebd1b6f40300f3243d262a46f42800620f495f5a38d3781e273702(
    *,
    alias_arn: builtins.str,
    alias_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e39afd357979864cdb0a0e965025e9600edb7d1d723c5d80bd567e33674e4ad4(
    *,
    build_arn: builtins.str,
    build_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16c358839d20499f02bc5631233f96eaee22a25eb9ec5256f6a4d30651735d82(
    *,
    fleet_arn: builtins.str,
    fleet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c4025f74a8de88eb68bdfa436229cb4bd5b891982aea5a4f8f68d5c1b15ba09(
    *,
    container_group_definition_arn: builtins.str,
    container_group_definition_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a0761deedfe27c2952d83b765671e1f2d64083fd6d00eeb8fa9cdcc6666860(
    *,
    fleet_arn: builtins.str,
    fleet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eed49d51771b830d643a4e4ffadaabeece46b2073ce63973239c01c9ae06f8b9(
    *,
    game_server_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaba6b78f225d34505e094f1ef37186fa6df83a00d620b1928d86b244926c808(
    *,
    game_session_queue_arn: builtins.str,
    game_session_queue_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d38962f536753d3d7e3ec8c20ecce982e21a10ac85e69ccfd9291df9452cdb2b(
    *,
    location_arn: builtins.str,
    location_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__652b9e6286ea4f923689b277ca538ac65edf1d5dec9f15e4e817dd492c877e95(
    *,
    matchmaking_configuration_arn: builtins.str,
    matchmaking_configuration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea758ab9c6c55fd32771d207aec1adbbafc4918621fb9f0331df1ff8d72b36e(
    *,
    matchmaking_rule_set_arn: builtins.str,
    matchmaking_rule_set_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e937f7ba8775875c3e775c0fe702df7d7e020dc7e88969fe496060f62e3c6094(
    *,
    script_arn: builtins.str,
    script_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAliasRef, IBuildRef, IContainerFleetRef, IContainerGroupDefinitionRef, IFleetRef, IGameServerGroupRef, IGameSessionQueueRef, ILocationRef, IMatchmakingConfigurationRef, IMatchmakingRuleSetRef, IScriptRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
