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
    jsii_type="aws-cdk-lib.interfaces.aws_groundstation.ConfigReference",
    jsii_struct_bases=[],
    name_mapping={"config_arn": "configArn"},
)
class ConfigReference:
    def __init__(self, *, config_arn: builtins.str) -> None:
        '''A reference to a Config resource.

        :param config_arn: The Arn of the Config resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_groundstation as interfaces_groundstation
            
            config_reference = interfaces_groundstation.ConfigReference(
                config_arn="configArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a6eaca3ff4ada34d80c539d2864b116d6fe5e953320140c2bdab6f056955efd)
            check_type(argname="argument config_arn", value=config_arn, expected_type=type_hints["config_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "config_arn": config_arn,
        }

    @builtins.property
    def config_arn(self) -> builtins.str:
        '''The Arn of the Config resource.'''
        result = self._values.get("config_arn")
        assert result is not None, "Required property 'config_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_groundstation.DataflowEndpointGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "dataflow_endpoint_group_arn": "dataflowEndpointGroupArn",
        "dataflow_endpoint_group_id": "dataflowEndpointGroupId",
    },
)
class DataflowEndpointGroupReference:
    def __init__(
        self,
        *,
        dataflow_endpoint_group_arn: builtins.str,
        dataflow_endpoint_group_id: builtins.str,
    ) -> None:
        '''A reference to a DataflowEndpointGroup resource.

        :param dataflow_endpoint_group_arn: The ARN of the DataflowEndpointGroup resource.
        :param dataflow_endpoint_group_id: The Id of the DataflowEndpointGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_groundstation as interfaces_groundstation
            
            dataflow_endpoint_group_reference = interfaces_groundstation.DataflowEndpointGroupReference(
                dataflow_endpoint_group_arn="dataflowEndpointGroupArn",
                dataflow_endpoint_group_id="dataflowEndpointGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72d1ff0dffa16a3c8c6709aada5fd4e7954b2daf59284c5dc613b0d17e2fecc5)
            check_type(argname="argument dataflow_endpoint_group_arn", value=dataflow_endpoint_group_arn, expected_type=type_hints["dataflow_endpoint_group_arn"])
            check_type(argname="argument dataflow_endpoint_group_id", value=dataflow_endpoint_group_id, expected_type=type_hints["dataflow_endpoint_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataflow_endpoint_group_arn": dataflow_endpoint_group_arn,
            "dataflow_endpoint_group_id": dataflow_endpoint_group_id,
        }

    @builtins.property
    def dataflow_endpoint_group_arn(self) -> builtins.str:
        '''The ARN of the DataflowEndpointGroup resource.'''
        result = self._values.get("dataflow_endpoint_group_arn")
        assert result is not None, "Required property 'dataflow_endpoint_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataflow_endpoint_group_id(self) -> builtins.str:
        '''The Id of the DataflowEndpointGroup resource.'''
        result = self._values.get("dataflow_endpoint_group_id")
        assert result is not None, "Required property 'dataflow_endpoint_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataflowEndpointGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_groundstation.DataflowEndpointGroupV2Reference",
    jsii_struct_bases=[],
    name_mapping={
        "dataflow_endpoint_group_v2_arn": "dataflowEndpointGroupV2Arn",
        "dataflow_endpoint_group_v2_id": "dataflowEndpointGroupV2Id",
    },
)
class DataflowEndpointGroupV2Reference:
    def __init__(
        self,
        *,
        dataflow_endpoint_group_v2_arn: builtins.str,
        dataflow_endpoint_group_v2_id: builtins.str,
    ) -> None:
        '''A reference to a DataflowEndpointGroupV2 resource.

        :param dataflow_endpoint_group_v2_arn: The ARN of the DataflowEndpointGroupV2 resource.
        :param dataflow_endpoint_group_v2_id: The Id of the DataflowEndpointGroupV2 resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_groundstation as interfaces_groundstation
            
            dataflow_endpoint_group_v2_reference = interfaces_groundstation.DataflowEndpointGroupV2Reference(
                dataflow_endpoint_group_v2_arn="dataflowEndpointGroupV2Arn",
                dataflow_endpoint_group_v2_id="dataflowEndpointGroupV2Id"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19502ad27588b6241a233e7abd2ad6c1e78c07030a2333abd2715d742b74d080)
            check_type(argname="argument dataflow_endpoint_group_v2_arn", value=dataflow_endpoint_group_v2_arn, expected_type=type_hints["dataflow_endpoint_group_v2_arn"])
            check_type(argname="argument dataflow_endpoint_group_v2_id", value=dataflow_endpoint_group_v2_id, expected_type=type_hints["dataflow_endpoint_group_v2_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dataflow_endpoint_group_v2_arn": dataflow_endpoint_group_v2_arn,
            "dataflow_endpoint_group_v2_id": dataflow_endpoint_group_v2_id,
        }

    @builtins.property
    def dataflow_endpoint_group_v2_arn(self) -> builtins.str:
        '''The ARN of the DataflowEndpointGroupV2 resource.'''
        result = self._values.get("dataflow_endpoint_group_v2_arn")
        assert result is not None, "Required property 'dataflow_endpoint_group_v2_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataflow_endpoint_group_v2_id(self) -> builtins.str:
        '''The Id of the DataflowEndpointGroupV2 resource.'''
        result = self._values.get("dataflow_endpoint_group_v2_id")
        assert result is not None, "Required property 'dataflow_endpoint_group_v2_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataflowEndpointGroupV2Reference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_groundstation.IConfigRef")
class IConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Config.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configRef")
    def config_ref(self) -> "ConfigReference":
        '''(experimental) A reference to a Config resource.

        :stability: experimental
        '''
        ...


class _IConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Config.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_groundstation.IConfigRef"

    @builtins.property
    @jsii.member(jsii_name="configRef")
    def config_ref(self) -> "ConfigReference":
        '''(experimental) A reference to a Config resource.

        :stability: experimental
        '''
        return typing.cast("ConfigReference", jsii.get(self, "configRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigRef).__jsii_proxy_class__ = lambda : _IConfigRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_groundstation.IDataflowEndpointGroupRef"
)
class IDataflowEndpointGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataflowEndpointGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataflowEndpointGroupRef")
    def dataflow_endpoint_group_ref(self) -> "DataflowEndpointGroupReference":
        '''(experimental) A reference to a DataflowEndpointGroup resource.

        :stability: experimental
        '''
        ...


class _IDataflowEndpointGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataflowEndpointGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_groundstation.IDataflowEndpointGroupRef"

    @builtins.property
    @jsii.member(jsii_name="dataflowEndpointGroupRef")
    def dataflow_endpoint_group_ref(self) -> "DataflowEndpointGroupReference":
        '''(experimental) A reference to a DataflowEndpointGroup resource.

        :stability: experimental
        '''
        return typing.cast("DataflowEndpointGroupReference", jsii.get(self, "dataflowEndpointGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataflowEndpointGroupRef).__jsii_proxy_class__ = lambda : _IDataflowEndpointGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_groundstation.IDataflowEndpointGroupV2Ref"
)
class IDataflowEndpointGroupV2Ref(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataflowEndpointGroupV2.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataflowEndpointGroupV2Ref")
    def dataflow_endpoint_group_v2_ref(self) -> "DataflowEndpointGroupV2Reference":
        '''(experimental) A reference to a DataflowEndpointGroupV2 resource.

        :stability: experimental
        '''
        ...


class _IDataflowEndpointGroupV2RefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataflowEndpointGroupV2.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_groundstation.IDataflowEndpointGroupV2Ref"

    @builtins.property
    @jsii.member(jsii_name="dataflowEndpointGroupV2Ref")
    def dataflow_endpoint_group_v2_ref(self) -> "DataflowEndpointGroupV2Reference":
        '''(experimental) A reference to a DataflowEndpointGroupV2 resource.

        :stability: experimental
        '''
        return typing.cast("DataflowEndpointGroupV2Reference", jsii.get(self, "dataflowEndpointGroupV2Ref"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataflowEndpointGroupV2Ref).__jsii_proxy_class__ = lambda : _IDataflowEndpointGroupV2RefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_groundstation.IMissionProfileRef"
)
class IMissionProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MissionProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="missionProfileRef")
    def mission_profile_ref(self) -> "MissionProfileReference":
        '''(experimental) A reference to a MissionProfile resource.

        :stability: experimental
        '''
        ...


class _IMissionProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MissionProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_groundstation.IMissionProfileRef"

    @builtins.property
    @jsii.member(jsii_name="missionProfileRef")
    def mission_profile_ref(self) -> "MissionProfileReference":
        '''(experimental) A reference to a MissionProfile resource.

        :stability: experimental
        '''
        return typing.cast("MissionProfileReference", jsii.get(self, "missionProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMissionProfileRef).__jsii_proxy_class__ = lambda : _IMissionProfileRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_groundstation.MissionProfileReference",
    jsii_struct_bases=[],
    name_mapping={
        "mission_profile_arn": "missionProfileArn",
        "mission_profile_id": "missionProfileId",
    },
)
class MissionProfileReference:
    def __init__(
        self,
        *,
        mission_profile_arn: builtins.str,
        mission_profile_id: builtins.str,
    ) -> None:
        '''A reference to a MissionProfile resource.

        :param mission_profile_arn: The Arn of the MissionProfile resource.
        :param mission_profile_id: The Id of the MissionProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_groundstation as interfaces_groundstation
            
            mission_profile_reference = interfaces_groundstation.MissionProfileReference(
                mission_profile_arn="missionProfileArn",
                mission_profile_id="missionProfileId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4505c7556cd6ef4e255a1db4087f115cab71d95522e90f85fa418f40952ce36)
            check_type(argname="argument mission_profile_arn", value=mission_profile_arn, expected_type=type_hints["mission_profile_arn"])
            check_type(argname="argument mission_profile_id", value=mission_profile_id, expected_type=type_hints["mission_profile_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "mission_profile_arn": mission_profile_arn,
            "mission_profile_id": mission_profile_id,
        }

    @builtins.property
    def mission_profile_arn(self) -> builtins.str:
        '''The Arn of the MissionProfile resource.'''
        result = self._values.get("mission_profile_arn")
        assert result is not None, "Required property 'mission_profile_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mission_profile_id(self) -> builtins.str:
        '''The Id of the MissionProfile resource.'''
        result = self._values.get("mission_profile_id")
        assert result is not None, "Required property 'mission_profile_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MissionProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConfigReference",
    "DataflowEndpointGroupReference",
    "DataflowEndpointGroupV2Reference",
    "IConfigRef",
    "IDataflowEndpointGroupRef",
    "IDataflowEndpointGroupV2Ref",
    "IMissionProfileRef",
    "MissionProfileReference",
]

publication.publish()

def _typecheckingstub__1a6eaca3ff4ada34d80c539d2864b116d6fe5e953320140c2bdab6f056955efd(
    *,
    config_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72d1ff0dffa16a3c8c6709aada5fd4e7954b2daf59284c5dc613b0d17e2fecc5(
    *,
    dataflow_endpoint_group_arn: builtins.str,
    dataflow_endpoint_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19502ad27588b6241a233e7abd2ad6c1e78c07030a2333abd2715d742b74d080(
    *,
    dataflow_endpoint_group_v2_arn: builtins.str,
    dataflow_endpoint_group_v2_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4505c7556cd6ef4e255a1db4087f115cab71d95522e90f85fa418f40952ce36(
    *,
    mission_profile_arn: builtins.str,
    mission_profile_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConfigRef, IDataflowEndpointGroupRef, IDataflowEndpointGroupV2Ref, IMissionProfileRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
