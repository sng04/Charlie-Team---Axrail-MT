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
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.ConnectorDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "connector_definition_arn": "connectorDefinitionArn",
        "connector_definition_id": "connectorDefinitionId",
    },
)
class ConnectorDefinitionReference:
    def __init__(
        self,
        *,
        connector_definition_arn: builtins.str,
        connector_definition_id: builtins.str,
    ) -> None:
        '''A reference to a ConnectorDefinition resource.

        :param connector_definition_arn: The ARN of the ConnectorDefinition resource.
        :param connector_definition_id: The Id of the ConnectorDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            connector_definition_reference = interfaces_greengrass.ConnectorDefinitionReference(
                connector_definition_arn="connectorDefinitionArn",
                connector_definition_id="connectorDefinitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__feb9810004ef139e502c8c7585fc5a9a71826a3a6accf002663d062bf230968a)
            check_type(argname="argument connector_definition_arn", value=connector_definition_arn, expected_type=type_hints["connector_definition_arn"])
            check_type(argname="argument connector_definition_id", value=connector_definition_id, expected_type=type_hints["connector_definition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_definition_arn": connector_definition_arn,
            "connector_definition_id": connector_definition_id,
        }

    @builtins.property
    def connector_definition_arn(self) -> builtins.str:
        '''The ARN of the ConnectorDefinition resource.'''
        result = self._values.get("connector_definition_arn")
        assert result is not None, "Required property 'connector_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_definition_id(self) -> builtins.str:
        '''The Id of the ConnectorDefinition resource.'''
        result = self._values.get("connector_definition_id")
        assert result is not None, "Required property 'connector_definition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.ConnectorDefinitionVersionReference",
    jsii_struct_bases=[],
    name_mapping={"connector_definition_version_id": "connectorDefinitionVersionId"},
)
class ConnectorDefinitionVersionReference:
    def __init__(self, *, connector_definition_version_id: builtins.str) -> None:
        '''A reference to a ConnectorDefinitionVersion resource.

        :param connector_definition_version_id: The Id of the ConnectorDefinitionVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            connector_definition_version_reference = interfaces_greengrass.ConnectorDefinitionVersionReference(
                connector_definition_version_id="connectorDefinitionVersionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f74039bd2f530231f7a7ae93595569080ed17728d1fc6d45adce7975096633ad)
            check_type(argname="argument connector_definition_version_id", value=connector_definition_version_id, expected_type=type_hints["connector_definition_version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_definition_version_id": connector_definition_version_id,
        }

    @builtins.property
    def connector_definition_version_id(self) -> builtins.str:
        '''The Id of the ConnectorDefinitionVersion resource.'''
        result = self._values.get("connector_definition_version_id")
        assert result is not None, "Required property 'connector_definition_version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorDefinitionVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.CoreDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "core_definition_arn": "coreDefinitionArn",
        "core_definition_id": "coreDefinitionId",
    },
)
class CoreDefinitionReference:
    def __init__(
        self,
        *,
        core_definition_arn: builtins.str,
        core_definition_id: builtins.str,
    ) -> None:
        '''A reference to a CoreDefinition resource.

        :param core_definition_arn: The ARN of the CoreDefinition resource.
        :param core_definition_id: The Id of the CoreDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            core_definition_reference = interfaces_greengrass.CoreDefinitionReference(
                core_definition_arn="coreDefinitionArn",
                core_definition_id="coreDefinitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86f703c2321804962693391e080e2978cccb8e1757b5e4a7ac4832b2aae04afc)
            check_type(argname="argument core_definition_arn", value=core_definition_arn, expected_type=type_hints["core_definition_arn"])
            check_type(argname="argument core_definition_id", value=core_definition_id, expected_type=type_hints["core_definition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "core_definition_arn": core_definition_arn,
            "core_definition_id": core_definition_id,
        }

    @builtins.property
    def core_definition_arn(self) -> builtins.str:
        '''The ARN of the CoreDefinition resource.'''
        result = self._values.get("core_definition_arn")
        assert result is not None, "Required property 'core_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def core_definition_id(self) -> builtins.str:
        '''The Id of the CoreDefinition resource.'''
        result = self._values.get("core_definition_id")
        assert result is not None, "Required property 'core_definition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CoreDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.CoreDefinitionVersionReference",
    jsii_struct_bases=[],
    name_mapping={"core_definition_version_id": "coreDefinitionVersionId"},
)
class CoreDefinitionVersionReference:
    def __init__(self, *, core_definition_version_id: builtins.str) -> None:
        '''A reference to a CoreDefinitionVersion resource.

        :param core_definition_version_id: The Id of the CoreDefinitionVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            core_definition_version_reference = interfaces_greengrass.CoreDefinitionVersionReference(
                core_definition_version_id="coreDefinitionVersionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__938bf6eb990871c55f16debdd2682f40477380d9195265ea7dc7c9c30094d493)
            check_type(argname="argument core_definition_version_id", value=core_definition_version_id, expected_type=type_hints["core_definition_version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "core_definition_version_id": core_definition_version_id,
        }

    @builtins.property
    def core_definition_version_id(self) -> builtins.str:
        '''The Id of the CoreDefinitionVersion resource.'''
        result = self._values.get("core_definition_version_id")
        assert result is not None, "Required property 'core_definition_version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CoreDefinitionVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.DeviceDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "device_definition_arn": "deviceDefinitionArn",
        "device_definition_id": "deviceDefinitionId",
    },
)
class DeviceDefinitionReference:
    def __init__(
        self,
        *,
        device_definition_arn: builtins.str,
        device_definition_id: builtins.str,
    ) -> None:
        '''A reference to a DeviceDefinition resource.

        :param device_definition_arn: The ARN of the DeviceDefinition resource.
        :param device_definition_id: The Id of the DeviceDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            device_definition_reference = interfaces_greengrass.DeviceDefinitionReference(
                device_definition_arn="deviceDefinitionArn",
                device_definition_id="deviceDefinitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8cc0e0a2939088dbe7c387a73930acca8f35728c09b8788203bbd136f05e272)
            check_type(argname="argument device_definition_arn", value=device_definition_arn, expected_type=type_hints["device_definition_arn"])
            check_type(argname="argument device_definition_id", value=device_definition_id, expected_type=type_hints["device_definition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_definition_arn": device_definition_arn,
            "device_definition_id": device_definition_id,
        }

    @builtins.property
    def device_definition_arn(self) -> builtins.str:
        '''The ARN of the DeviceDefinition resource.'''
        result = self._values.get("device_definition_arn")
        assert result is not None, "Required property 'device_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def device_definition_id(self) -> builtins.str:
        '''The Id of the DeviceDefinition resource.'''
        result = self._values.get("device_definition_id")
        assert result is not None, "Required property 'device_definition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeviceDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.DeviceDefinitionVersionReference",
    jsii_struct_bases=[],
    name_mapping={"device_definition_version_id": "deviceDefinitionVersionId"},
)
class DeviceDefinitionVersionReference:
    def __init__(self, *, device_definition_version_id: builtins.str) -> None:
        '''A reference to a DeviceDefinitionVersion resource.

        :param device_definition_version_id: The Id of the DeviceDefinitionVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            device_definition_version_reference = interfaces_greengrass.DeviceDefinitionVersionReference(
                device_definition_version_id="deviceDefinitionVersionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__643844e9ccd4b63fbf6f2f3b4431d096e30496ff653396912844a7380037e89c)
            check_type(argname="argument device_definition_version_id", value=device_definition_version_id, expected_type=type_hints["device_definition_version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "device_definition_version_id": device_definition_version_id,
        }

    @builtins.property
    def device_definition_version_id(self) -> builtins.str:
        '''The Id of the DeviceDefinitionVersion resource.'''
        result = self._values.get("device_definition_version_id")
        assert result is not None, "Required property 'device_definition_version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DeviceDefinitionVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.FunctionDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "function_definition_arn": "functionDefinitionArn",
        "function_definition_id": "functionDefinitionId",
    },
)
class FunctionDefinitionReference:
    def __init__(
        self,
        *,
        function_definition_arn: builtins.str,
        function_definition_id: builtins.str,
    ) -> None:
        '''A reference to a FunctionDefinition resource.

        :param function_definition_arn: The ARN of the FunctionDefinition resource.
        :param function_definition_id: The Id of the FunctionDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            function_definition_reference = interfaces_greengrass.FunctionDefinitionReference(
                function_definition_arn="functionDefinitionArn",
                function_definition_id="functionDefinitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e09a59a60ec473f7bb0f6db9138716f5d5dacf733ad8c43df3865687ff692d5)
            check_type(argname="argument function_definition_arn", value=function_definition_arn, expected_type=type_hints["function_definition_arn"])
            check_type(argname="argument function_definition_id", value=function_definition_id, expected_type=type_hints["function_definition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_definition_arn": function_definition_arn,
            "function_definition_id": function_definition_id,
        }

    @builtins.property
    def function_definition_arn(self) -> builtins.str:
        '''The ARN of the FunctionDefinition resource.'''
        result = self._values.get("function_definition_arn")
        assert result is not None, "Required property 'function_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def function_definition_id(self) -> builtins.str:
        '''The Id of the FunctionDefinition resource.'''
        result = self._values.get("function_definition_id")
        assert result is not None, "Required property 'function_definition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.FunctionDefinitionVersionReference",
    jsii_struct_bases=[],
    name_mapping={"function_definition_version_id": "functionDefinitionVersionId"},
)
class FunctionDefinitionVersionReference:
    def __init__(self, *, function_definition_version_id: builtins.str) -> None:
        '''A reference to a FunctionDefinitionVersion resource.

        :param function_definition_version_id: The Id of the FunctionDefinitionVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            function_definition_version_reference = interfaces_greengrass.FunctionDefinitionVersionReference(
                function_definition_version_id="functionDefinitionVersionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ab37888b9562f928140377091b63ce70c367d4d017e04d2d6b9593c49ab63d)
            check_type(argname="argument function_definition_version_id", value=function_definition_version_id, expected_type=type_hints["function_definition_version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_definition_version_id": function_definition_version_id,
        }

    @builtins.property
    def function_definition_version_id(self) -> builtins.str:
        '''The Id of the FunctionDefinitionVersion resource.'''
        result = self._values.get("function_definition_version_id")
        assert result is not None, "Required property 'function_definition_version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionDefinitionVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.GroupReference",
    jsii_struct_bases=[],
    name_mapping={"group_arn": "groupArn", "group_id": "groupId"},
)
class GroupReference:
    def __init__(self, *, group_arn: builtins.str, group_id: builtins.str) -> None:
        '''A reference to a Group resource.

        :param group_arn: The ARN of the Group resource.
        :param group_id: The Id of the Group resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            group_reference = interfaces_greengrass.GroupReference(
                group_arn="groupArn",
                group_id="groupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81d3637e624e6270d769ba20892614a7bdab10b9fff0a8d202f4b9335d6629f8)
            check_type(argname="argument group_arn", value=group_arn, expected_type=type_hints["group_arn"])
            check_type(argname="argument group_id", value=group_id, expected_type=type_hints["group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_arn": group_arn,
            "group_id": group_id,
        }

    @builtins.property
    def group_arn(self) -> builtins.str:
        '''The ARN of the Group resource.'''
        result = self._values.get("group_arn")
        assert result is not None, "Required property 'group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group_id(self) -> builtins.str:
        '''The Id of the Group resource.'''
        result = self._values.get("group_id")
        assert result is not None, "Required property 'group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.GroupVersionReference",
    jsii_struct_bases=[],
    name_mapping={"group_version_id": "groupVersionId"},
)
class GroupVersionReference:
    def __init__(self, *, group_version_id: builtins.str) -> None:
        '''A reference to a GroupVersion resource.

        :param group_version_id: The Id of the GroupVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            group_version_reference = interfaces_greengrass.GroupVersionReference(
                group_version_id="groupVersionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a277c2f9ad12beb76a85e8c6302f931893206339e834fb5d12a2a0fced88730)
            check_type(argname="argument group_version_id", value=group_version_id, expected_type=type_hints["group_version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_version_id": group_version_id,
        }

    @builtins.property
    def group_version_id(self) -> builtins.str:
        '''The Id of the GroupVersion resource.'''
        result = self._values.get("group_version_id")
        assert result is not None, "Required property 'group_version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.IConnectorDefinitionRef"
)
class IConnectorDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectorDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectorDefinitionRef")
    def connector_definition_ref(self) -> "ConnectorDefinitionReference":
        '''(experimental) A reference to a ConnectorDefinition resource.

        :stability: experimental
        '''
        ...


class _IConnectorDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectorDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.IConnectorDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="connectorDefinitionRef")
    def connector_definition_ref(self) -> "ConnectorDefinitionReference":
        '''(experimental) A reference to a ConnectorDefinition resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorDefinitionReference", jsii.get(self, "connectorDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorDefinitionRef).__jsii_proxy_class__ = lambda : _IConnectorDefinitionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.IConnectorDefinitionVersionRef"
)
class IConnectorDefinitionVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectorDefinitionVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectorDefinitionVersionRef")
    def connector_definition_version_ref(self) -> "ConnectorDefinitionVersionReference":
        '''(experimental) A reference to a ConnectorDefinitionVersion resource.

        :stability: experimental
        '''
        ...


class _IConnectorDefinitionVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConnectorDefinitionVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.IConnectorDefinitionVersionRef"

    @builtins.property
    @jsii.member(jsii_name="connectorDefinitionVersionRef")
    def connector_definition_version_ref(self) -> "ConnectorDefinitionVersionReference":
        '''(experimental) A reference to a ConnectorDefinitionVersion resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorDefinitionVersionReference", jsii.get(self, "connectorDefinitionVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorDefinitionVersionRef).__jsii_proxy_class__ = lambda : _IConnectorDefinitionVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_greengrass.ICoreDefinitionRef")
class ICoreDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CoreDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="coreDefinitionRef")
    def core_definition_ref(self) -> "CoreDefinitionReference":
        '''(experimental) A reference to a CoreDefinition resource.

        :stability: experimental
        '''
        ...


class _ICoreDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CoreDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.ICoreDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="coreDefinitionRef")
    def core_definition_ref(self) -> "CoreDefinitionReference":
        '''(experimental) A reference to a CoreDefinition resource.

        :stability: experimental
        '''
        return typing.cast("CoreDefinitionReference", jsii.get(self, "coreDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICoreDefinitionRef).__jsii_proxy_class__ = lambda : _ICoreDefinitionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.ICoreDefinitionVersionRef"
)
class ICoreDefinitionVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CoreDefinitionVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="coreDefinitionVersionRef")
    def core_definition_version_ref(self) -> "CoreDefinitionVersionReference":
        '''(experimental) A reference to a CoreDefinitionVersion resource.

        :stability: experimental
        '''
        ...


class _ICoreDefinitionVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CoreDefinitionVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.ICoreDefinitionVersionRef"

    @builtins.property
    @jsii.member(jsii_name="coreDefinitionVersionRef")
    def core_definition_version_ref(self) -> "CoreDefinitionVersionReference":
        '''(experimental) A reference to a CoreDefinitionVersion resource.

        :stability: experimental
        '''
        return typing.cast("CoreDefinitionVersionReference", jsii.get(self, "coreDefinitionVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICoreDefinitionVersionRef).__jsii_proxy_class__ = lambda : _ICoreDefinitionVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_greengrass.IDeviceDefinitionRef")
class IDeviceDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeviceDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deviceDefinitionRef")
    def device_definition_ref(self) -> "DeviceDefinitionReference":
        '''(experimental) A reference to a DeviceDefinition resource.

        :stability: experimental
        '''
        ...


class _IDeviceDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeviceDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.IDeviceDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="deviceDefinitionRef")
    def device_definition_ref(self) -> "DeviceDefinitionReference":
        '''(experimental) A reference to a DeviceDefinition resource.

        :stability: experimental
        '''
        return typing.cast("DeviceDefinitionReference", jsii.get(self, "deviceDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeviceDefinitionRef).__jsii_proxy_class__ = lambda : _IDeviceDefinitionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.IDeviceDefinitionVersionRef"
)
class IDeviceDefinitionVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DeviceDefinitionVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="deviceDefinitionVersionRef")
    def device_definition_version_ref(self) -> "DeviceDefinitionVersionReference":
        '''(experimental) A reference to a DeviceDefinitionVersion resource.

        :stability: experimental
        '''
        ...


class _IDeviceDefinitionVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DeviceDefinitionVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.IDeviceDefinitionVersionRef"

    @builtins.property
    @jsii.member(jsii_name="deviceDefinitionVersionRef")
    def device_definition_version_ref(self) -> "DeviceDefinitionVersionReference":
        '''(experimental) A reference to a DeviceDefinitionVersion resource.

        :stability: experimental
        '''
        return typing.cast("DeviceDefinitionVersionReference", jsii.get(self, "deviceDefinitionVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDeviceDefinitionVersionRef).__jsii_proxy_class__ = lambda : _IDeviceDefinitionVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.IFunctionDefinitionRef"
)
class IFunctionDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FunctionDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="functionDefinitionRef")
    def function_definition_ref(self) -> "FunctionDefinitionReference":
        '''(experimental) A reference to a FunctionDefinition resource.

        :stability: experimental
        '''
        ...


class _IFunctionDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FunctionDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.IFunctionDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="functionDefinitionRef")
    def function_definition_ref(self) -> "FunctionDefinitionReference":
        '''(experimental) A reference to a FunctionDefinition resource.

        :stability: experimental
        '''
        return typing.cast("FunctionDefinitionReference", jsii.get(self, "functionDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFunctionDefinitionRef).__jsii_proxy_class__ = lambda : _IFunctionDefinitionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.IFunctionDefinitionVersionRef"
)
class IFunctionDefinitionVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FunctionDefinitionVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="functionDefinitionVersionRef")
    def function_definition_version_ref(self) -> "FunctionDefinitionVersionReference":
        '''(experimental) A reference to a FunctionDefinitionVersion resource.

        :stability: experimental
        '''
        ...


class _IFunctionDefinitionVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FunctionDefinitionVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.IFunctionDefinitionVersionRef"

    @builtins.property
    @jsii.member(jsii_name="functionDefinitionVersionRef")
    def function_definition_version_ref(self) -> "FunctionDefinitionVersionReference":
        '''(experimental) A reference to a FunctionDefinitionVersion resource.

        :stability: experimental
        '''
        return typing.cast("FunctionDefinitionVersionReference", jsii.get(self, "functionDefinitionVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFunctionDefinitionVersionRef).__jsii_proxy_class__ = lambda : _IFunctionDefinitionVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_greengrass.IGroupRef")
class IGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Group.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="groupRef")
    def group_ref(self) -> "GroupReference":
        '''(experimental) A reference to a Group resource.

        :stability: experimental
        '''
        ...


class _IGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Group.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.IGroupRef"

    @builtins.property
    @jsii.member(jsii_name="groupRef")
    def group_ref(self) -> "GroupReference":
        '''(experimental) A reference to a Group resource.

        :stability: experimental
        '''
        return typing.cast("GroupReference", jsii.get(self, "groupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupRef).__jsii_proxy_class__ = lambda : _IGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_greengrass.IGroupVersionRef")
class IGroupVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GroupVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="groupVersionRef")
    def group_version_ref(self) -> "GroupVersionReference":
        '''(experimental) A reference to a GroupVersion resource.

        :stability: experimental
        '''
        ...


class _IGroupVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GroupVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.IGroupVersionRef"

    @builtins.property
    @jsii.member(jsii_name="groupVersionRef")
    def group_version_ref(self) -> "GroupVersionReference":
        '''(experimental) A reference to a GroupVersion resource.

        :stability: experimental
        '''
        return typing.cast("GroupVersionReference", jsii.get(self, "groupVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupVersionRef).__jsii_proxy_class__ = lambda : _IGroupVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_greengrass.ILoggerDefinitionRef")
class ILoggerDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LoggerDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="loggerDefinitionRef")
    def logger_definition_ref(self) -> "LoggerDefinitionReference":
        '''(experimental) A reference to a LoggerDefinition resource.

        :stability: experimental
        '''
        ...


class _ILoggerDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LoggerDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.ILoggerDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="loggerDefinitionRef")
    def logger_definition_ref(self) -> "LoggerDefinitionReference":
        '''(experimental) A reference to a LoggerDefinition resource.

        :stability: experimental
        '''
        return typing.cast("LoggerDefinitionReference", jsii.get(self, "loggerDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILoggerDefinitionRef).__jsii_proxy_class__ = lambda : _ILoggerDefinitionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.ILoggerDefinitionVersionRef"
)
class ILoggerDefinitionVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LoggerDefinitionVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="loggerDefinitionVersionRef")
    def logger_definition_version_ref(self) -> "LoggerDefinitionVersionReference":
        '''(experimental) A reference to a LoggerDefinitionVersion resource.

        :stability: experimental
        '''
        ...


class _ILoggerDefinitionVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LoggerDefinitionVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.ILoggerDefinitionVersionRef"

    @builtins.property
    @jsii.member(jsii_name="loggerDefinitionVersionRef")
    def logger_definition_version_ref(self) -> "LoggerDefinitionVersionReference":
        '''(experimental) A reference to a LoggerDefinitionVersion resource.

        :stability: experimental
        '''
        return typing.cast("LoggerDefinitionVersionReference", jsii.get(self, "loggerDefinitionVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILoggerDefinitionVersionRef).__jsii_proxy_class__ = lambda : _ILoggerDefinitionVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.IResourceDefinitionRef"
)
class IResourceDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceDefinitionRef")
    def resource_definition_ref(self) -> "ResourceDefinitionReference":
        '''(experimental) A reference to a ResourceDefinition resource.

        :stability: experimental
        '''
        ...


class _IResourceDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.IResourceDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="resourceDefinitionRef")
    def resource_definition_ref(self) -> "ResourceDefinitionReference":
        '''(experimental) A reference to a ResourceDefinition resource.

        :stability: experimental
        '''
        return typing.cast("ResourceDefinitionReference", jsii.get(self, "resourceDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceDefinitionRef).__jsii_proxy_class__ = lambda : _IResourceDefinitionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.IResourceDefinitionVersionRef"
)
class IResourceDefinitionVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceDefinitionVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceDefinitionVersionRef")
    def resource_definition_version_ref(self) -> "ResourceDefinitionVersionReference":
        '''(experimental) A reference to a ResourceDefinitionVersion resource.

        :stability: experimental
        '''
        ...


class _IResourceDefinitionVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceDefinitionVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.IResourceDefinitionVersionRef"

    @builtins.property
    @jsii.member(jsii_name="resourceDefinitionVersionRef")
    def resource_definition_version_ref(self) -> "ResourceDefinitionVersionReference":
        '''(experimental) A reference to a ResourceDefinitionVersion resource.

        :stability: experimental
        '''
        return typing.cast("ResourceDefinitionVersionReference", jsii.get(self, "resourceDefinitionVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceDefinitionVersionRef).__jsii_proxy_class__ = lambda : _IResourceDefinitionVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.ISubscriptionDefinitionRef"
)
class ISubscriptionDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SubscriptionDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subscriptionDefinitionRef")
    def subscription_definition_ref(self) -> "SubscriptionDefinitionReference":
        '''(experimental) A reference to a SubscriptionDefinition resource.

        :stability: experimental
        '''
        ...


class _ISubscriptionDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SubscriptionDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.ISubscriptionDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="subscriptionDefinitionRef")
    def subscription_definition_ref(self) -> "SubscriptionDefinitionReference":
        '''(experimental) A reference to a SubscriptionDefinition resource.

        :stability: experimental
        '''
        return typing.cast("SubscriptionDefinitionReference", jsii.get(self, "subscriptionDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubscriptionDefinitionRef).__jsii_proxy_class__ = lambda : _ISubscriptionDefinitionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.ISubscriptionDefinitionVersionRef"
)
class ISubscriptionDefinitionVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SubscriptionDefinitionVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subscriptionDefinitionVersionRef")
    def subscription_definition_version_ref(
        self,
    ) -> "SubscriptionDefinitionVersionReference":
        '''(experimental) A reference to a SubscriptionDefinitionVersion resource.

        :stability: experimental
        '''
        ...


class _ISubscriptionDefinitionVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SubscriptionDefinitionVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_greengrass.ISubscriptionDefinitionVersionRef"

    @builtins.property
    @jsii.member(jsii_name="subscriptionDefinitionVersionRef")
    def subscription_definition_version_ref(
        self,
    ) -> "SubscriptionDefinitionVersionReference":
        '''(experimental) A reference to a SubscriptionDefinitionVersion resource.

        :stability: experimental
        '''
        return typing.cast("SubscriptionDefinitionVersionReference", jsii.get(self, "subscriptionDefinitionVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubscriptionDefinitionVersionRef).__jsii_proxy_class__ = lambda : _ISubscriptionDefinitionVersionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.LoggerDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "logger_definition_arn": "loggerDefinitionArn",
        "logger_definition_id": "loggerDefinitionId",
    },
)
class LoggerDefinitionReference:
    def __init__(
        self,
        *,
        logger_definition_arn: builtins.str,
        logger_definition_id: builtins.str,
    ) -> None:
        '''A reference to a LoggerDefinition resource.

        :param logger_definition_arn: The ARN of the LoggerDefinition resource.
        :param logger_definition_id: The Id of the LoggerDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            logger_definition_reference = interfaces_greengrass.LoggerDefinitionReference(
                logger_definition_arn="loggerDefinitionArn",
                logger_definition_id="loggerDefinitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6811b44d8327c7a7c12ae2a598aeb4a37fcdadf5b235433d292e858d5d55ade0)
            check_type(argname="argument logger_definition_arn", value=logger_definition_arn, expected_type=type_hints["logger_definition_arn"])
            check_type(argname="argument logger_definition_id", value=logger_definition_id, expected_type=type_hints["logger_definition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "logger_definition_arn": logger_definition_arn,
            "logger_definition_id": logger_definition_id,
        }

    @builtins.property
    def logger_definition_arn(self) -> builtins.str:
        '''The ARN of the LoggerDefinition resource.'''
        result = self._values.get("logger_definition_arn")
        assert result is not None, "Required property 'logger_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def logger_definition_id(self) -> builtins.str:
        '''The Id of the LoggerDefinition resource.'''
        result = self._values.get("logger_definition_id")
        assert result is not None, "Required property 'logger_definition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggerDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.LoggerDefinitionVersionReference",
    jsii_struct_bases=[],
    name_mapping={"logger_definition_version_id": "loggerDefinitionVersionId"},
)
class LoggerDefinitionVersionReference:
    def __init__(self, *, logger_definition_version_id: builtins.str) -> None:
        '''A reference to a LoggerDefinitionVersion resource.

        :param logger_definition_version_id: The Id of the LoggerDefinitionVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            logger_definition_version_reference = interfaces_greengrass.LoggerDefinitionVersionReference(
                logger_definition_version_id="loggerDefinitionVersionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2df9b1c3f8f75951a3e8db5d5828fdefc2ea77bc0c2fdea644a34d2c0aecb916)
            check_type(argname="argument logger_definition_version_id", value=logger_definition_version_id, expected_type=type_hints["logger_definition_version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "logger_definition_version_id": logger_definition_version_id,
        }

    @builtins.property
    def logger_definition_version_id(self) -> builtins.str:
        '''The Id of the LoggerDefinitionVersion resource.'''
        result = self._values.get("logger_definition_version_id")
        assert result is not None, "Required property 'logger_definition_version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoggerDefinitionVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.ResourceDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "resource_definition_arn": "resourceDefinitionArn",
        "resource_definition_id": "resourceDefinitionId",
    },
)
class ResourceDefinitionReference:
    def __init__(
        self,
        *,
        resource_definition_arn: builtins.str,
        resource_definition_id: builtins.str,
    ) -> None:
        '''A reference to a ResourceDefinition resource.

        :param resource_definition_arn: The ARN of the ResourceDefinition resource.
        :param resource_definition_id: The Id of the ResourceDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            resource_definition_reference = interfaces_greengrass.ResourceDefinitionReference(
                resource_definition_arn="resourceDefinitionArn",
                resource_definition_id="resourceDefinitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15421579579b23b2ee6fde536cb3484a2f69b5e9f47c32bc1079dd3564f90342)
            check_type(argname="argument resource_definition_arn", value=resource_definition_arn, expected_type=type_hints["resource_definition_arn"])
            check_type(argname="argument resource_definition_id", value=resource_definition_id, expected_type=type_hints["resource_definition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_definition_arn": resource_definition_arn,
            "resource_definition_id": resource_definition_id,
        }

    @builtins.property
    def resource_definition_arn(self) -> builtins.str:
        '''The ARN of the ResourceDefinition resource.'''
        result = self._values.get("resource_definition_arn")
        assert result is not None, "Required property 'resource_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_definition_id(self) -> builtins.str:
        '''The Id of the ResourceDefinition resource.'''
        result = self._values.get("resource_definition_id")
        assert result is not None, "Required property 'resource_definition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.ResourceDefinitionVersionReference",
    jsii_struct_bases=[],
    name_mapping={"resource_definition_version_id": "resourceDefinitionVersionId"},
)
class ResourceDefinitionVersionReference:
    def __init__(self, *, resource_definition_version_id: builtins.str) -> None:
        '''A reference to a ResourceDefinitionVersion resource.

        :param resource_definition_version_id: The Id of the ResourceDefinitionVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            resource_definition_version_reference = interfaces_greengrass.ResourceDefinitionVersionReference(
                resource_definition_version_id="resourceDefinitionVersionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f40c0364a1f82a6ba84b221ba716f60bf66d385cfd833e44e30e41e523ed1370)
            check_type(argname="argument resource_definition_version_id", value=resource_definition_version_id, expected_type=type_hints["resource_definition_version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_definition_version_id": resource_definition_version_id,
        }

    @builtins.property
    def resource_definition_version_id(self) -> builtins.str:
        '''The Id of the ResourceDefinitionVersion resource.'''
        result = self._values.get("resource_definition_version_id")
        assert result is not None, "Required property 'resource_definition_version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceDefinitionVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.SubscriptionDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "subscription_definition_arn": "subscriptionDefinitionArn",
        "subscription_definition_id": "subscriptionDefinitionId",
    },
)
class SubscriptionDefinitionReference:
    def __init__(
        self,
        *,
        subscription_definition_arn: builtins.str,
        subscription_definition_id: builtins.str,
    ) -> None:
        '''A reference to a SubscriptionDefinition resource.

        :param subscription_definition_arn: The ARN of the SubscriptionDefinition resource.
        :param subscription_definition_id: The Id of the SubscriptionDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            subscription_definition_reference = interfaces_greengrass.SubscriptionDefinitionReference(
                subscription_definition_arn="subscriptionDefinitionArn",
                subscription_definition_id="subscriptionDefinitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5efc59acdfcec0fc8652b8011f4b750cfd2b275ff5958378b6092b3cfaa7801d)
            check_type(argname="argument subscription_definition_arn", value=subscription_definition_arn, expected_type=type_hints["subscription_definition_arn"])
            check_type(argname="argument subscription_definition_id", value=subscription_definition_id, expected_type=type_hints["subscription_definition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscription_definition_arn": subscription_definition_arn,
            "subscription_definition_id": subscription_definition_id,
        }

    @builtins.property
    def subscription_definition_arn(self) -> builtins.str:
        '''The ARN of the SubscriptionDefinition resource.'''
        result = self._values.get("subscription_definition_arn")
        assert result is not None, "Required property 'subscription_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscription_definition_id(self) -> builtins.str:
        '''The Id of the SubscriptionDefinition resource.'''
        result = self._values.get("subscription_definition_id")
        assert result is not None, "Required property 'subscription_definition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_greengrass.SubscriptionDefinitionVersionReference",
    jsii_struct_bases=[],
    name_mapping={
        "subscription_definition_version_id": "subscriptionDefinitionVersionId",
    },
)
class SubscriptionDefinitionVersionReference:
    def __init__(self, *, subscription_definition_version_id: builtins.str) -> None:
        '''A reference to a SubscriptionDefinitionVersion resource.

        :param subscription_definition_version_id: The Id of the SubscriptionDefinitionVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_greengrass as interfaces_greengrass
            
            subscription_definition_version_reference = interfaces_greengrass.SubscriptionDefinitionVersionReference(
                subscription_definition_version_id="subscriptionDefinitionVersionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__467fab44fe227f2955017bb8546314831f4a65f9fdc6edc4a3f6aa2cd96eb67e)
            check_type(argname="argument subscription_definition_version_id", value=subscription_definition_version_id, expected_type=type_hints["subscription_definition_version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subscription_definition_version_id": subscription_definition_version_id,
        }

    @builtins.property
    def subscription_definition_version_id(self) -> builtins.str:
        '''The Id of the SubscriptionDefinitionVersion resource.'''
        result = self._values.get("subscription_definition_version_id")
        assert result is not None, "Required property 'subscription_definition_version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubscriptionDefinitionVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConnectorDefinitionReference",
    "ConnectorDefinitionVersionReference",
    "CoreDefinitionReference",
    "CoreDefinitionVersionReference",
    "DeviceDefinitionReference",
    "DeviceDefinitionVersionReference",
    "FunctionDefinitionReference",
    "FunctionDefinitionVersionReference",
    "GroupReference",
    "GroupVersionReference",
    "IConnectorDefinitionRef",
    "IConnectorDefinitionVersionRef",
    "ICoreDefinitionRef",
    "ICoreDefinitionVersionRef",
    "IDeviceDefinitionRef",
    "IDeviceDefinitionVersionRef",
    "IFunctionDefinitionRef",
    "IFunctionDefinitionVersionRef",
    "IGroupRef",
    "IGroupVersionRef",
    "ILoggerDefinitionRef",
    "ILoggerDefinitionVersionRef",
    "IResourceDefinitionRef",
    "IResourceDefinitionVersionRef",
    "ISubscriptionDefinitionRef",
    "ISubscriptionDefinitionVersionRef",
    "LoggerDefinitionReference",
    "LoggerDefinitionVersionReference",
    "ResourceDefinitionReference",
    "ResourceDefinitionVersionReference",
    "SubscriptionDefinitionReference",
    "SubscriptionDefinitionVersionReference",
]

publication.publish()

def _typecheckingstub__feb9810004ef139e502c8c7585fc5a9a71826a3a6accf002663d062bf230968a(
    *,
    connector_definition_arn: builtins.str,
    connector_definition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f74039bd2f530231f7a7ae93595569080ed17728d1fc6d45adce7975096633ad(
    *,
    connector_definition_version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86f703c2321804962693391e080e2978cccb8e1757b5e4a7ac4832b2aae04afc(
    *,
    core_definition_arn: builtins.str,
    core_definition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__938bf6eb990871c55f16debdd2682f40477380d9195265ea7dc7c9c30094d493(
    *,
    core_definition_version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8cc0e0a2939088dbe7c387a73930acca8f35728c09b8788203bbd136f05e272(
    *,
    device_definition_arn: builtins.str,
    device_definition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__643844e9ccd4b63fbf6f2f3b4431d096e30496ff653396912844a7380037e89c(
    *,
    device_definition_version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e09a59a60ec473f7bb0f6db9138716f5d5dacf733ad8c43df3865687ff692d5(
    *,
    function_definition_arn: builtins.str,
    function_definition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ab37888b9562f928140377091b63ce70c367d4d017e04d2d6b9593c49ab63d(
    *,
    function_definition_version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81d3637e624e6270d769ba20892614a7bdab10b9fff0a8d202f4b9335d6629f8(
    *,
    group_arn: builtins.str,
    group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a277c2f9ad12beb76a85e8c6302f931893206339e834fb5d12a2a0fced88730(
    *,
    group_version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6811b44d8327c7a7c12ae2a598aeb4a37fcdadf5b235433d292e858d5d55ade0(
    *,
    logger_definition_arn: builtins.str,
    logger_definition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2df9b1c3f8f75951a3e8db5d5828fdefc2ea77bc0c2fdea644a34d2c0aecb916(
    *,
    logger_definition_version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15421579579b23b2ee6fde536cb3484a2f69b5e9f47c32bc1079dd3564f90342(
    *,
    resource_definition_arn: builtins.str,
    resource_definition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f40c0364a1f82a6ba84b221ba716f60bf66d385cfd833e44e30e41e523ed1370(
    *,
    resource_definition_version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5efc59acdfcec0fc8652b8011f4b750cfd2b275ff5958378b6092b3cfaa7801d(
    *,
    subscription_definition_arn: builtins.str,
    subscription_definition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__467fab44fe227f2955017bb8546314831f4a65f9fdc6edc4a3f6aa2cd96eb67e(
    *,
    subscription_definition_version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectorDefinitionRef, IConnectorDefinitionVersionRef, ICoreDefinitionRef, ICoreDefinitionVersionRef, IDeviceDefinitionRef, IDeviceDefinitionVersionRef, IFunctionDefinitionRef, IFunctionDefinitionVersionRef, IGroupRef, IGroupVersionRef, ILoggerDefinitionRef, ILoggerDefinitionVersionRef, IResourceDefinitionRef, IResourceDefinitionVersionRef, ISubscriptionDefinitionRef, ISubscriptionDefinitionVersionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
