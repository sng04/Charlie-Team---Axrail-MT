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
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.AliasReference",
    jsii_struct_bases=[],
    name_mapping={"alias_arn": "aliasArn"},
)
class AliasReference:
    def __init__(self, *, alias_arn: builtins.str) -> None:
        '''A reference to a Alias resource.

        :param alias_arn: The AliasArn of the Alias resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            alias_reference = interfaces_lambda.AliasReference(
                alias_arn="aliasArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b5bdc37a9ac06d42b682902b37a528e61143ca57e7d401996ee0bf55267110d)
            check_type(argname="argument alias_arn", value=alias_arn, expected_type=type_hints["alias_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias_arn": alias_arn,
        }

    @builtins.property
    def alias_arn(self) -> builtins.str:
        '''The AliasArn of the Alias resource.'''
        result = self._values.get("alias_arn")
        assert result is not None, "Required property 'alias_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.CapacityProviderReference",
    jsii_struct_bases=[],
    name_mapping={
        "capacity_provider_arn": "capacityProviderArn",
        "capacity_provider_name": "capacityProviderName",
    },
)
class CapacityProviderReference:
    def __init__(
        self,
        *,
        capacity_provider_arn: builtins.str,
        capacity_provider_name: builtins.str,
    ) -> None:
        '''A reference to a CapacityProvider resource.

        :param capacity_provider_arn: The ARN of the CapacityProvider resource.
        :param capacity_provider_name: The CapacityProviderName of the CapacityProvider resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            capacity_provider_reference = interfaces_lambda.CapacityProviderReference(
                capacity_provider_arn="capacityProviderArn",
                capacity_provider_name="capacityProviderName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00dca94efa22346b052a6470fe46fd4bd396570533c2cf79a9e8680d82ea3171)
            check_type(argname="argument capacity_provider_arn", value=capacity_provider_arn, expected_type=type_hints["capacity_provider_arn"])
            check_type(argname="argument capacity_provider_name", value=capacity_provider_name, expected_type=type_hints["capacity_provider_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity_provider_arn": capacity_provider_arn,
            "capacity_provider_name": capacity_provider_name,
        }

    @builtins.property
    def capacity_provider_arn(self) -> builtins.str:
        '''The ARN of the CapacityProvider resource.'''
        result = self._values.get("capacity_provider_arn")
        assert result is not None, "Required property 'capacity_provider_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def capacity_provider_name(self) -> builtins.str:
        '''The CapacityProviderName of the CapacityProvider resource.'''
        result = self._values.get("capacity_provider_name")
        assert result is not None, "Required property 'capacity_provider_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CapacityProviderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.CodeSigningConfigReference",
    jsii_struct_bases=[],
    name_mapping={"code_signing_config_arn": "codeSigningConfigArn"},
)
class CodeSigningConfigReference:
    def __init__(self, *, code_signing_config_arn: builtins.str) -> None:
        '''A reference to a CodeSigningConfig resource.

        :param code_signing_config_arn: The CodeSigningConfigArn of the CodeSigningConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            code_signing_config_reference = interfaces_lambda.CodeSigningConfigReference(
                code_signing_config_arn="codeSigningConfigArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a65cb8c0b429ec22cf1d0fcf55d6e640e2f1752d66573677dfa9b12e9b1ad46)
            check_type(argname="argument code_signing_config_arn", value=code_signing_config_arn, expected_type=type_hints["code_signing_config_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code_signing_config_arn": code_signing_config_arn,
        }

    @builtins.property
    def code_signing_config_arn(self) -> builtins.str:
        '''The CodeSigningConfigArn of the CodeSigningConfig resource.'''
        result = self._values.get("code_signing_config_arn")
        assert result is not None, "Required property 'code_signing_config_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeSigningConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.EventInvokeConfigReference",
    jsii_struct_bases=[],
    name_mapping={"function_name": "functionName", "qualifier": "qualifier"},
)
class EventInvokeConfigReference:
    def __init__(self, *, function_name: builtins.str, qualifier: builtins.str) -> None:
        '''A reference to a EventInvokeConfig resource.

        :param function_name: The FunctionName of the EventInvokeConfig resource.
        :param qualifier: The Qualifier of the EventInvokeConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            event_invoke_config_reference = interfaces_lambda.EventInvokeConfigReference(
                function_name="functionName",
                qualifier="qualifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8869408494c20506fc78a425087fa4248d28fe6ce88a0a8defcb34070253257c)
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument qualifier", value=qualifier, expected_type=type_hints["qualifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_name": function_name,
            "qualifier": qualifier,
        }

    @builtins.property
    def function_name(self) -> builtins.str:
        '''The FunctionName of the EventInvokeConfig resource.'''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def qualifier(self) -> builtins.str:
        '''The Qualifier of the EventInvokeConfig resource.'''
        result = self._values.get("qualifier")
        assert result is not None, "Required property 'qualifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventInvokeConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.EventSourceMappingReference",
    jsii_struct_bases=[],
    name_mapping={
        "event_source_mapping_arn": "eventSourceMappingArn",
        "event_source_mapping_id": "eventSourceMappingId",
    },
)
class EventSourceMappingReference:
    def __init__(
        self,
        *,
        event_source_mapping_arn: builtins.str,
        event_source_mapping_id: builtins.str,
    ) -> None:
        '''A reference to a EventSourceMapping resource.

        :param event_source_mapping_arn: The ARN of the EventSourceMapping resource.
        :param event_source_mapping_id: The Id of the EventSourceMapping resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            event_source_mapping_reference = interfaces_lambda.EventSourceMappingReference(
                event_source_mapping_arn="eventSourceMappingArn",
                event_source_mapping_id="eventSourceMappingId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__914c7bca34a11dc37f498de7d99986f5ca17a68862b75858d85f142f5eca98ff)
            check_type(argname="argument event_source_mapping_arn", value=event_source_mapping_arn, expected_type=type_hints["event_source_mapping_arn"])
            check_type(argname="argument event_source_mapping_id", value=event_source_mapping_id, expected_type=type_hints["event_source_mapping_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_source_mapping_arn": event_source_mapping_arn,
            "event_source_mapping_id": event_source_mapping_id,
        }

    @builtins.property
    def event_source_mapping_arn(self) -> builtins.str:
        '''The ARN of the EventSourceMapping resource.'''
        result = self._values.get("event_source_mapping_arn")
        assert result is not None, "Required property 'event_source_mapping_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_source_mapping_id(self) -> builtins.str:
        '''The Id of the EventSourceMapping resource.'''
        result = self._values.get("event_source_mapping_id")
        assert result is not None, "Required property 'event_source_mapping_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventSourceMappingReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.FunctionReference",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn", "function_name": "functionName"},
)
class FunctionReference:
    def __init__(
        self,
        *,
        function_arn: builtins.str,
        function_name: builtins.str,
    ) -> None:
        '''A reference to a Function resource.

        :param function_arn: The ARN of the Function resource.
        :param function_name: The FunctionName of the Function resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            function_reference = interfaces_lambda.FunctionReference(
                function_arn="functionArn",
                function_name="functionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2622d2568fff85e244bc224e1e86796ca1a12d869401ce912f5ed6c1b88ec8eb)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
            "function_name": function_name,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''The ARN of the Function resource.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def function_name(self) -> builtins.str:
        '''The FunctionName of the Function resource.'''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lambda.IAliasRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.IAliasRef"

    @builtins.property
    @jsii.member(jsii_name="aliasRef")
    def alias_ref(self) -> "AliasReference":
        '''(experimental) A reference to a Alias resource.

        :stability: experimental
        '''
        return typing.cast("AliasReference", jsii.get(self, "aliasRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAliasRef).__jsii_proxy_class__ = lambda : _IAliasRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lambda.ICapacityProviderRef")
class ICapacityProviderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityProvider.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="capacityProviderRef")
    def capacity_provider_ref(self) -> "CapacityProviderReference":
        '''(experimental) A reference to a CapacityProvider resource.

        :stability: experimental
        '''
        ...


class _ICapacityProviderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityProvider.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.ICapacityProviderRef"

    @builtins.property
    @jsii.member(jsii_name="capacityProviderRef")
    def capacity_provider_ref(self) -> "CapacityProviderReference":
        '''(experimental) A reference to a CapacityProvider resource.

        :stability: experimental
        '''
        return typing.cast("CapacityProviderReference", jsii.get(self, "capacityProviderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICapacityProviderRef).__jsii_proxy_class__ = lambda : _ICapacityProviderRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lambda.ICodeSigningConfigRef")
class ICodeSigningConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CodeSigningConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="codeSigningConfigRef")
    def code_signing_config_ref(self) -> "CodeSigningConfigReference":
        '''(experimental) A reference to a CodeSigningConfig resource.

        :stability: experimental
        '''
        ...


class _ICodeSigningConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CodeSigningConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.ICodeSigningConfigRef"

    @builtins.property
    @jsii.member(jsii_name="codeSigningConfigRef")
    def code_signing_config_ref(self) -> "CodeSigningConfigReference":
        '''(experimental) A reference to a CodeSigningConfig resource.

        :stability: experimental
        '''
        return typing.cast("CodeSigningConfigReference", jsii.get(self, "codeSigningConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICodeSigningConfigRef).__jsii_proxy_class__ = lambda : _ICodeSigningConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lambda.IEventInvokeConfigRef")
class IEventInvokeConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventInvokeConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventInvokeConfigRef")
    def event_invoke_config_ref(self) -> "EventInvokeConfigReference":
        '''(experimental) A reference to a EventInvokeConfig resource.

        :stability: experimental
        '''
        ...


class _IEventInvokeConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventInvokeConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.IEventInvokeConfigRef"

    @builtins.property
    @jsii.member(jsii_name="eventInvokeConfigRef")
    def event_invoke_config_ref(self) -> "EventInvokeConfigReference":
        '''(experimental) A reference to a EventInvokeConfig resource.

        :stability: experimental
        '''
        return typing.cast("EventInvokeConfigReference", jsii.get(self, "eventInvokeConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventInvokeConfigRef).__jsii_proxy_class__ = lambda : _IEventInvokeConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lambda.IEventSourceMappingRef")
class IEventSourceMappingRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventSourceMapping.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventSourceMappingRef")
    def event_source_mapping_ref(self) -> "EventSourceMappingReference":
        '''(experimental) A reference to a EventSourceMapping resource.

        :stability: experimental
        '''
        ...


class _IEventSourceMappingRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventSourceMapping.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.IEventSourceMappingRef"

    @builtins.property
    @jsii.member(jsii_name="eventSourceMappingRef")
    def event_source_mapping_ref(self) -> "EventSourceMappingReference":
        '''(experimental) A reference to a EventSourceMapping resource.

        :stability: experimental
        '''
        return typing.cast("EventSourceMappingReference", jsii.get(self, "eventSourceMappingRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventSourceMappingRef).__jsii_proxy_class__ = lambda : _IEventSourceMappingRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lambda.IFunctionRef")
class IFunctionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Function.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="functionRef")
    def function_ref(self) -> "FunctionReference":
        '''(experimental) A reference to a Function resource.

        :stability: experimental
        '''
        ...


class _IFunctionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Function.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.IFunctionRef"

    @builtins.property
    @jsii.member(jsii_name="functionRef")
    def function_ref(self) -> "FunctionReference":
        '''(experimental) A reference to a Function resource.

        :stability: experimental
        '''
        return typing.cast("FunctionReference", jsii.get(self, "functionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFunctionRef).__jsii_proxy_class__ = lambda : _IFunctionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.ILayerVersionPermissionRef"
)
class ILayerVersionPermissionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LayerVersionPermission.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="layerVersionPermissionRef")
    def layer_version_permission_ref(self) -> "LayerVersionPermissionReference":
        '''(experimental) A reference to a LayerVersionPermission resource.

        :stability: experimental
        '''
        ...


class _ILayerVersionPermissionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LayerVersionPermission.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.ILayerVersionPermissionRef"

    @builtins.property
    @jsii.member(jsii_name="layerVersionPermissionRef")
    def layer_version_permission_ref(self) -> "LayerVersionPermissionReference":
        '''(experimental) A reference to a LayerVersionPermission resource.

        :stability: experimental
        '''
        return typing.cast("LayerVersionPermissionReference", jsii.get(self, "layerVersionPermissionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILayerVersionPermissionRef).__jsii_proxy_class__ = lambda : _ILayerVersionPermissionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lambda.ILayerVersionRef")
class ILayerVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LayerVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="layerVersionRef")
    def layer_version_ref(self) -> "LayerVersionReference":
        '''(experimental) A reference to a LayerVersion resource.

        :stability: experimental
        '''
        ...


class _ILayerVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LayerVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.ILayerVersionRef"

    @builtins.property
    @jsii.member(jsii_name="layerVersionRef")
    def layer_version_ref(self) -> "LayerVersionReference":
        '''(experimental) A reference to a LayerVersion resource.

        :stability: experimental
        '''
        return typing.cast("LayerVersionReference", jsii.get(self, "layerVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILayerVersionRef).__jsii_proxy_class__ = lambda : _ILayerVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lambda.IPermissionRef")
class IPermissionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Permission.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="permissionRef")
    def permission_ref(self) -> "PermissionReference":
        '''(experimental) A reference to a Permission resource.

        :stability: experimental
        '''
        ...


class _IPermissionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Permission.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.IPermissionRef"

    @builtins.property
    @jsii.member(jsii_name="permissionRef")
    def permission_ref(self) -> "PermissionReference":
        '''(experimental) A reference to a Permission resource.

        :stability: experimental
        '''
        return typing.cast("PermissionReference", jsii.get(self, "permissionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPermissionRef).__jsii_proxy_class__ = lambda : _IPermissionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lambda.IUrlRef")
class IUrlRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Url.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="urlRef")
    def url_ref(self) -> "UrlReference":
        '''(experimental) A reference to a Url resource.

        :stability: experimental
        '''
        ...


class _IUrlRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Url.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.IUrlRef"

    @builtins.property
    @jsii.member(jsii_name="urlRef")
    def url_ref(self) -> "UrlReference":
        '''(experimental) A reference to a Url resource.

        :stability: experimental
        '''
        return typing.cast("UrlReference", jsii.get(self, "urlRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUrlRef).__jsii_proxy_class__ = lambda : _IUrlRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lambda.IVersionRef")
class IVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Version.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="versionRef")
    def version_ref(self) -> "VersionReference":
        '''(experimental) A reference to a Version resource.

        :stability: experimental
        '''
        ...


class _IVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Version.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lambda.IVersionRef"

    @builtins.property
    @jsii.member(jsii_name="versionRef")
    def version_ref(self) -> "VersionReference":
        '''(experimental) A reference to a Version resource.

        :stability: experimental
        '''
        return typing.cast("VersionReference", jsii.get(self, "versionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVersionRef).__jsii_proxy_class__ = lambda : _IVersionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.LayerVersionPermissionReference",
    jsii_struct_bases=[],
    name_mapping={"layer_version_permission_id": "layerVersionPermissionId"},
)
class LayerVersionPermissionReference:
    def __init__(self, *, layer_version_permission_id: builtins.str) -> None:
        '''A reference to a LayerVersionPermission resource.

        :param layer_version_permission_id: The Id of the LayerVersionPermission resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            layer_version_permission_reference = interfaces_lambda.LayerVersionPermissionReference(
                layer_version_permission_id="layerVersionPermissionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fce6482a550bee55dfb2043ffc5f2c335c77c3f0024e8ba1a17120766954f0d)
            check_type(argname="argument layer_version_permission_id", value=layer_version_permission_id, expected_type=type_hints["layer_version_permission_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "layer_version_permission_id": layer_version_permission_id,
        }

    @builtins.property
    def layer_version_permission_id(self) -> builtins.str:
        '''The Id of the LayerVersionPermission resource.'''
        result = self._values.get("layer_version_permission_id")
        assert result is not None, "Required property 'layer_version_permission_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LayerVersionPermissionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.LayerVersionReference",
    jsii_struct_bases=[],
    name_mapping={"layer_version_arn": "layerVersionArn"},
)
class LayerVersionReference:
    def __init__(self, *, layer_version_arn: builtins.str) -> None:
        '''A reference to a LayerVersion resource.

        :param layer_version_arn: The LayerVersionArn of the LayerVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            layer_version_reference = interfaces_lambda.LayerVersionReference(
                layer_version_arn="layerVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7abcb136f4f2b538a6636e1bb18d321c62bd48d1cecd42d19f1ba521ddcb7ef)
            check_type(argname="argument layer_version_arn", value=layer_version_arn, expected_type=type_hints["layer_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "layer_version_arn": layer_version_arn,
        }

    @builtins.property
    def layer_version_arn(self) -> builtins.str:
        '''The LayerVersionArn of the LayerVersion resource.'''
        result = self._values.get("layer_version_arn")
        assert result is not None, "Required property 'layer_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LayerVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.PermissionReference",
    jsii_struct_bases=[],
    name_mapping={"function_name": "functionName", "permission_id": "permissionId"},
)
class PermissionReference:
    def __init__(
        self,
        *,
        function_name: builtins.str,
        permission_id: builtins.str,
    ) -> None:
        '''A reference to a Permission resource.

        :param function_name: The FunctionName of the Permission resource.
        :param permission_id: The Id of the Permission resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            permission_reference = interfaces_lambda.PermissionReference(
                function_name="functionName",
                permission_id="permissionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ae650600646cc849a26dcaf279873a6f95a9ec8ad73f8dc4af5d9055c6d7ba8)
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument permission_id", value=permission_id, expected_type=type_hints["permission_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_name": function_name,
            "permission_id": permission_id,
        }

    @builtins.property
    def function_name(self) -> builtins.str:
        '''The FunctionName of the Permission resource.'''
        result = self._values.get("function_name")
        assert result is not None, "Required property 'function_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def permission_id(self) -> builtins.str:
        '''The Id of the Permission resource.'''
        result = self._values.get("permission_id")
        assert result is not None, "Required property 'permission_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PermissionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.UrlReference",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class UrlReference:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''A reference to a Url resource.

        :param function_arn: The FunctionArn of the Url resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            url_reference = interfaces_lambda.UrlReference(
                function_arn="functionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7993d40300b6226e3801bcd00ef035491568259a4dee9da3e5a1980adb1133eb)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''The FunctionArn of the Url resource.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UrlReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lambda.VersionReference",
    jsii_struct_bases=[],
    name_mapping={"function_arn": "functionArn"},
)
class VersionReference:
    def __init__(self, *, function_arn: builtins.str) -> None:
        '''A reference to a Version resource.

        :param function_arn: The FunctionArn of the Version resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lambda as interfaces_lambda
            
            version_reference = interfaces_lambda.VersionReference(
                function_arn="functionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4eef012bdf282178fc15f29261bb73aca6423bb74d9618d940489c8c85502423)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''The FunctionArn of the Version resource.'''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AliasReference",
    "CapacityProviderReference",
    "CodeSigningConfigReference",
    "EventInvokeConfigReference",
    "EventSourceMappingReference",
    "FunctionReference",
    "IAliasRef",
    "ICapacityProviderRef",
    "ICodeSigningConfigRef",
    "IEventInvokeConfigRef",
    "IEventSourceMappingRef",
    "IFunctionRef",
    "ILayerVersionPermissionRef",
    "ILayerVersionRef",
    "IPermissionRef",
    "IUrlRef",
    "IVersionRef",
    "LayerVersionPermissionReference",
    "LayerVersionReference",
    "PermissionReference",
    "UrlReference",
    "VersionReference",
]

publication.publish()

def _typecheckingstub__0b5bdc37a9ac06d42b682902b37a528e61143ca57e7d401996ee0bf55267110d(
    *,
    alias_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00dca94efa22346b052a6470fe46fd4bd396570533c2cf79a9e8680d82ea3171(
    *,
    capacity_provider_arn: builtins.str,
    capacity_provider_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a65cb8c0b429ec22cf1d0fcf55d6e640e2f1752d66573677dfa9b12e9b1ad46(
    *,
    code_signing_config_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8869408494c20506fc78a425087fa4248d28fe6ce88a0a8defcb34070253257c(
    *,
    function_name: builtins.str,
    qualifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__914c7bca34a11dc37f498de7d99986f5ca17a68862b75858d85f142f5eca98ff(
    *,
    event_source_mapping_arn: builtins.str,
    event_source_mapping_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2622d2568fff85e244bc224e1e86796ca1a12d869401ce912f5ed6c1b88ec8eb(
    *,
    function_arn: builtins.str,
    function_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fce6482a550bee55dfb2043ffc5f2c335c77c3f0024e8ba1a17120766954f0d(
    *,
    layer_version_permission_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7abcb136f4f2b538a6636e1bb18d321c62bd48d1cecd42d19f1ba521ddcb7ef(
    *,
    layer_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ae650600646cc849a26dcaf279873a6f95a9ec8ad73f8dc4af5d9055c6d7ba8(
    *,
    function_name: builtins.str,
    permission_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7993d40300b6226e3801bcd00ef035491568259a4dee9da3e5a1980adb1133eb(
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4eef012bdf282178fc15f29261bb73aca6423bb74d9618d940489c8c85502423(
    *,
    function_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAliasRef, ICapacityProviderRef, ICodeSigningConfigRef, IEventInvokeConfigRef, IEventSourceMappingRef, IFunctionRef, ILayerVersionPermissionRef, ILayerVersionRef, IPermissionRef, IUrlRef, IVersionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
