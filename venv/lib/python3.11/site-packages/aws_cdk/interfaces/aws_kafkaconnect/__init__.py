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
    jsii_type="aws-cdk-lib.interfaces.aws_kafkaconnect.ConnectorReference",
    jsii_struct_bases=[],
    name_mapping={"connector_arn": "connectorArn"},
)
class ConnectorReference:
    def __init__(self, *, connector_arn: builtins.str) -> None:
        '''A reference to a Connector resource.

        :param connector_arn: The ConnectorArn of the Connector resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kafkaconnect as interfaces_kafkaconnect
            
            connector_reference = interfaces_kafkaconnect.ConnectorReference(
                connector_arn="connectorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__62ca535c7b68a85cfb613cc0df34a54de7f31244f168630b4dfddaedc01b3033)
            check_type(argname="argument connector_arn", value=connector_arn, expected_type=type_hints["connector_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_arn": connector_arn,
        }

    @builtins.property
    def connector_arn(self) -> builtins.str:
        '''The ConnectorArn of the Connector resource.'''
        result = self._values.get("connector_arn")
        assert result is not None, "Required property 'connector_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kafkaconnect.CustomPluginReference",
    jsii_struct_bases=[],
    name_mapping={"custom_plugin_arn": "customPluginArn"},
)
class CustomPluginReference:
    def __init__(self, *, custom_plugin_arn: builtins.str) -> None:
        '''A reference to a CustomPlugin resource.

        :param custom_plugin_arn: The CustomPluginArn of the CustomPlugin resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kafkaconnect as interfaces_kafkaconnect
            
            custom_plugin_reference = interfaces_kafkaconnect.CustomPluginReference(
                custom_plugin_arn="customPluginArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d9cbfbfa9de008ffc5c1ac1a21fc52f30a3cf75e8f9199867e36522b2371b88)
            check_type(argname="argument custom_plugin_arn", value=custom_plugin_arn, expected_type=type_hints["custom_plugin_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_plugin_arn": custom_plugin_arn,
        }

    @builtins.property
    def custom_plugin_arn(self) -> builtins.str:
        '''The CustomPluginArn of the CustomPlugin resource.'''
        result = self._values.get("custom_plugin_arn")
        assert result is not None, "Required property 'custom_plugin_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomPluginReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kafkaconnect.IConnectorRef")
class IConnectorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        ...


class _IConnectorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connector.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kafkaconnect.IConnectorRef"

    @builtins.property
    @jsii.member(jsii_name="connectorRef")
    def connector_ref(self) -> "ConnectorReference":
        '''(experimental) A reference to a Connector resource.

        :stability: experimental
        '''
        return typing.cast("ConnectorReference", jsii.get(self, "connectorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectorRef).__jsii_proxy_class__ = lambda : _IConnectorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_kafkaconnect.ICustomPluginRef")
class ICustomPluginRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomPlugin.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customPluginRef")
    def custom_plugin_ref(self) -> "CustomPluginReference":
        '''(experimental) A reference to a CustomPlugin resource.

        :stability: experimental
        '''
        ...


class _ICustomPluginRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomPlugin.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kafkaconnect.ICustomPluginRef"

    @builtins.property
    @jsii.member(jsii_name="customPluginRef")
    def custom_plugin_ref(self) -> "CustomPluginReference":
        '''(experimental) A reference to a CustomPlugin resource.

        :stability: experimental
        '''
        return typing.cast("CustomPluginReference", jsii.get(self, "customPluginRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomPluginRef).__jsii_proxy_class__ = lambda : _ICustomPluginRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_kafkaconnect.IWorkerConfigurationRef"
)
class IWorkerConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WorkerConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workerConfigurationRef")
    def worker_configuration_ref(self) -> "WorkerConfigurationReference":
        '''(experimental) A reference to a WorkerConfiguration resource.

        :stability: experimental
        '''
        ...


class _IWorkerConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WorkerConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kafkaconnect.IWorkerConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="workerConfigurationRef")
    def worker_configuration_ref(self) -> "WorkerConfigurationReference":
        '''(experimental) A reference to a WorkerConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("WorkerConfigurationReference", jsii.get(self, "workerConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkerConfigurationRef).__jsii_proxy_class__ = lambda : _IWorkerConfigurationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kafkaconnect.WorkerConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"worker_configuration_arn": "workerConfigurationArn"},
)
class WorkerConfigurationReference:
    def __init__(self, *, worker_configuration_arn: builtins.str) -> None:
        '''A reference to a WorkerConfiguration resource.

        :param worker_configuration_arn: The WorkerConfigurationArn of the WorkerConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kafkaconnect as interfaces_kafkaconnect
            
            worker_configuration_reference = interfaces_kafkaconnect.WorkerConfigurationReference(
                worker_configuration_arn="workerConfigurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78ace45728fbb4be69948c030d6e0b04a230109b3a5385ecf42d9539bfc61a70)
            check_type(argname="argument worker_configuration_arn", value=worker_configuration_arn, expected_type=type_hints["worker_configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "worker_configuration_arn": worker_configuration_arn,
        }

    @builtins.property
    def worker_configuration_arn(self) -> builtins.str:
        '''The WorkerConfigurationArn of the WorkerConfiguration resource.'''
        result = self._values.get("worker_configuration_arn")
        assert result is not None, "Required property 'worker_configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkerConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConnectorReference",
    "CustomPluginReference",
    "IConnectorRef",
    "ICustomPluginRef",
    "IWorkerConfigurationRef",
    "WorkerConfigurationReference",
]

publication.publish()

def _typecheckingstub__62ca535c7b68a85cfb613cc0df34a54de7f31244f168630b4dfddaedc01b3033(
    *,
    connector_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d9cbfbfa9de008ffc5c1ac1a21fc52f30a3cf75e8f9199867e36522b2371b88(
    *,
    custom_plugin_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ace45728fbb4be69948c030d6e0b04a230109b3a5385ecf42d9539bfc61a70(
    *,
    worker_configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectorRef, ICustomPluginRef, IWorkerConfigurationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
