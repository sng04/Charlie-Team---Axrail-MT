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
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.CustomResourceReference",
    jsii_struct_bases=[],
    name_mapping={"custom_resource_id": "customResourceId"},
)
class CustomResourceReference:
    def __init__(self, *, custom_resource_id: builtins.str) -> None:
        '''A reference to a CustomResource resource.

        :param custom_resource_id: The Id of the CustomResource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            custom_resource_reference = interfaces_cloudformation.CustomResourceReference(
                custom_resource_id="customResourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b7c6fc64f1a76292b3e9c451ff5d2ef2906f21f9ee7be7f2213d5cbc5e2d8d0)
            check_type(argname="argument custom_resource_id", value=custom_resource_id, expected_type=type_hints["custom_resource_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_resource_id": custom_resource_id,
        }

    @builtins.property
    def custom_resource_id(self) -> builtins.str:
        '''The Id of the CustomResource resource.'''
        result = self._values.get("custom_resource_id")
        assert result is not None, "Required property 'custom_resource_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomResourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.GuardHookReference",
    jsii_struct_bases=[],
    name_mapping={"hook_arn": "hookArn"},
)
class GuardHookReference:
    def __init__(self, *, hook_arn: builtins.str) -> None:
        '''A reference to a GuardHook resource.

        :param hook_arn: The HookArn of the GuardHook resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            guard_hook_reference = interfaces_cloudformation.GuardHookReference(
                hook_arn="hookArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__775ac6fdd8641de5fd9822abf6f886825b2f6e4892f6bdf2d249a6c799b83b70)
            check_type(argname="argument hook_arn", value=hook_arn, expected_type=type_hints["hook_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hook_arn": hook_arn,
        }

    @builtins.property
    def hook_arn(self) -> builtins.str:
        '''The HookArn of the GuardHook resource.'''
        result = self._values.get("hook_arn")
        assert result is not None, "Required property 'hook_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GuardHookReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.HookDefaultVersionReference",
    jsii_struct_bases=[],
    name_mapping={"hook_default_version_arn": "hookDefaultVersionArn"},
)
class HookDefaultVersionReference:
    def __init__(self, *, hook_default_version_arn: builtins.str) -> None:
        '''A reference to a HookDefaultVersion resource.

        :param hook_default_version_arn: The Arn of the HookDefaultVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            hook_default_version_reference = interfaces_cloudformation.HookDefaultVersionReference(
                hook_default_version_arn="hookDefaultVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6d0b56d2950ab15ec15c230e341be18d0f0974ea5d59e387f7232dad93053cb)
            check_type(argname="argument hook_default_version_arn", value=hook_default_version_arn, expected_type=type_hints["hook_default_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hook_default_version_arn": hook_default_version_arn,
        }

    @builtins.property
    def hook_default_version_arn(self) -> builtins.str:
        '''The Arn of the HookDefaultVersion resource.'''
        result = self._values.get("hook_default_version_arn")
        assert result is not None, "Required property 'hook_default_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HookDefaultVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.HookTypeConfigReference",
    jsii_struct_bases=[],
    name_mapping={"configuration_arn": "configurationArn"},
)
class HookTypeConfigReference:
    def __init__(self, *, configuration_arn: builtins.str) -> None:
        '''A reference to a HookTypeConfig resource.

        :param configuration_arn: The ConfigurationArn of the HookTypeConfig resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            hook_type_config_reference = interfaces_cloudformation.HookTypeConfigReference(
                configuration_arn="configurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3b50301833de36cb0604dcfcaa3be80edace6d3e1a0e6006db4da13bc85b78e)
            check_type(argname="argument configuration_arn", value=configuration_arn, expected_type=type_hints["configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_arn": configuration_arn,
        }

    @builtins.property
    def configuration_arn(self) -> builtins.str:
        '''The ConfigurationArn of the HookTypeConfig resource.'''
        result = self._values.get("configuration_arn")
        assert result is not None, "Required property 'configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HookTypeConfigReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.HookVersionReference",
    jsii_struct_bases=[],
    name_mapping={"hook_version_arn": "hookVersionArn"},
)
class HookVersionReference:
    def __init__(self, *, hook_version_arn: builtins.str) -> None:
        '''A reference to a HookVersion resource.

        :param hook_version_arn: The Arn of the HookVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            hook_version_reference = interfaces_cloudformation.HookVersionReference(
                hook_version_arn="hookVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__266211dcc23f86069691e9aa5c7355e16923c23e8b1e58b1c126f6521314dd38)
            check_type(argname="argument hook_version_arn", value=hook_version_arn, expected_type=type_hints["hook_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hook_version_arn": hook_version_arn,
        }

    @builtins.property
    def hook_version_arn(self) -> builtins.str:
        '''The Arn of the HookVersion resource.'''
        result = self._values.get("hook_version_arn")
        assert result is not None, "Required property 'hook_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HookVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.ICustomResourceRef"
)
class ICustomResourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomResource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customResourceRef")
    def custom_resource_ref(self) -> "CustomResourceReference":
        '''(experimental) A reference to a CustomResource resource.

        :stability: experimental
        '''
        ...


class _ICustomResourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomResource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.ICustomResourceRef"

    @builtins.property
    @jsii.member(jsii_name="customResourceRef")
    def custom_resource_ref(self) -> "CustomResourceReference":
        '''(experimental) A reference to a CustomResource resource.

        :stability: experimental
        '''
        return typing.cast("CustomResourceReference", jsii.get(self, "customResourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomResourceRef).__jsii_proxy_class__ = lambda : _ICustomResourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IGuardHookRef")
class IGuardHookRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GuardHook.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="guardHookRef")
    def guard_hook_ref(self) -> "GuardHookReference":
        '''(experimental) A reference to a GuardHook resource.

        :stability: experimental
        '''
        ...


class _IGuardHookRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GuardHook.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IGuardHookRef"

    @builtins.property
    @jsii.member(jsii_name="guardHookRef")
    def guard_hook_ref(self) -> "GuardHookReference":
        '''(experimental) A reference to a GuardHook resource.

        :stability: experimental
        '''
        return typing.cast("GuardHookReference", jsii.get(self, "guardHookRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGuardHookRef).__jsii_proxy_class__ = lambda : _IGuardHookRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IHookDefaultVersionRef"
)
class IHookDefaultVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HookDefaultVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hookDefaultVersionRef")
    def hook_default_version_ref(self) -> "HookDefaultVersionReference":
        '''(experimental) A reference to a HookDefaultVersion resource.

        :stability: experimental
        '''
        ...


class _IHookDefaultVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HookDefaultVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IHookDefaultVersionRef"

    @builtins.property
    @jsii.member(jsii_name="hookDefaultVersionRef")
    def hook_default_version_ref(self) -> "HookDefaultVersionReference":
        '''(experimental) A reference to a HookDefaultVersion resource.

        :stability: experimental
        '''
        return typing.cast("HookDefaultVersionReference", jsii.get(self, "hookDefaultVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHookDefaultVersionRef).__jsii_proxy_class__ = lambda : _IHookDefaultVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IHookTypeConfigRef"
)
class IHookTypeConfigRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HookTypeConfig.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hookTypeConfigRef")
    def hook_type_config_ref(self) -> "HookTypeConfigReference":
        '''(experimental) A reference to a HookTypeConfig resource.

        :stability: experimental
        '''
        ...


class _IHookTypeConfigRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HookTypeConfig.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IHookTypeConfigRef"

    @builtins.property
    @jsii.member(jsii_name="hookTypeConfigRef")
    def hook_type_config_ref(self) -> "HookTypeConfigReference":
        '''(experimental) A reference to a HookTypeConfig resource.

        :stability: experimental
        '''
        return typing.cast("HookTypeConfigReference", jsii.get(self, "hookTypeConfigRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHookTypeConfigRef).__jsii_proxy_class__ = lambda : _IHookTypeConfigRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IHookVersionRef")
class IHookVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HookVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="hookVersionRef")
    def hook_version_ref(self) -> "HookVersionReference":
        '''(experimental) A reference to a HookVersion resource.

        :stability: experimental
        '''
        ...


class _IHookVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HookVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IHookVersionRef"

    @builtins.property
    @jsii.member(jsii_name="hookVersionRef")
    def hook_version_ref(self) -> "HookVersionReference":
        '''(experimental) A reference to a HookVersion resource.

        :stability: experimental
        '''
        return typing.cast("HookVersionReference", jsii.get(self, "hookVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHookVersionRef).__jsii_proxy_class__ = lambda : _IHookVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.ILambdaHookRef")
class ILambdaHookRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LambdaHook.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="lambdaHookRef")
    def lambda_hook_ref(self) -> "LambdaHookReference":
        '''(experimental) A reference to a LambdaHook resource.

        :stability: experimental
        '''
        ...


class _ILambdaHookRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LambdaHook.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.ILambdaHookRef"

    @builtins.property
    @jsii.member(jsii_name="lambdaHookRef")
    def lambda_hook_ref(self) -> "LambdaHookReference":
        '''(experimental) A reference to a LambdaHook resource.

        :stability: experimental
        '''
        return typing.cast("LambdaHookReference", jsii.get(self, "lambdaHookRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILambdaHookRef).__jsii_proxy_class__ = lambda : _ILambdaHookRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IMacroRef")
class IMacroRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Macro.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="macroRef")
    def macro_ref(self) -> "MacroReference":
        '''(experimental) A reference to a Macro resource.

        :stability: experimental
        '''
        ...


class _IMacroRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Macro.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IMacroRef"

    @builtins.property
    @jsii.member(jsii_name="macroRef")
    def macro_ref(self) -> "MacroReference":
        '''(experimental) A reference to a Macro resource.

        :stability: experimental
        '''
        return typing.cast("MacroReference", jsii.get(self, "macroRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMacroRef).__jsii_proxy_class__ = lambda : _IMacroRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IModuleDefaultVersionRef"
)
class IModuleDefaultVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ModuleDefaultVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="moduleDefaultVersionRef")
    def module_default_version_ref(self) -> "ModuleDefaultVersionReference":
        '''(experimental) A reference to a ModuleDefaultVersion resource.

        :stability: experimental
        '''
        ...


class _IModuleDefaultVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ModuleDefaultVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IModuleDefaultVersionRef"

    @builtins.property
    @jsii.member(jsii_name="moduleDefaultVersionRef")
    def module_default_version_ref(self) -> "ModuleDefaultVersionReference":
        '''(experimental) A reference to a ModuleDefaultVersion resource.

        :stability: experimental
        '''
        return typing.cast("ModuleDefaultVersionReference", jsii.get(self, "moduleDefaultVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModuleDefaultVersionRef).__jsii_proxy_class__ = lambda : _IModuleDefaultVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IModuleVersionRef"
)
class IModuleVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ModuleVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="moduleVersionRef")
    def module_version_ref(self) -> "ModuleVersionReference":
        '''(experimental) A reference to a ModuleVersion resource.

        :stability: experimental
        '''
        ...


class _IModuleVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ModuleVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IModuleVersionRef"

    @builtins.property
    @jsii.member(jsii_name="moduleVersionRef")
    def module_version_ref(self) -> "ModuleVersionReference":
        '''(experimental) A reference to a ModuleVersion resource.

        :stability: experimental
        '''
        return typing.cast("ModuleVersionReference", jsii.get(self, "moduleVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IModuleVersionRef).__jsii_proxy_class__ = lambda : _IModuleVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IPublicTypeVersionRef"
)
class IPublicTypeVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PublicTypeVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="publicTypeVersionRef")
    def public_type_version_ref(self) -> "PublicTypeVersionReference":
        '''(experimental) A reference to a PublicTypeVersion resource.

        :stability: experimental
        '''
        ...


class _IPublicTypeVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PublicTypeVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IPublicTypeVersionRef"

    @builtins.property
    @jsii.member(jsii_name="publicTypeVersionRef")
    def public_type_version_ref(self) -> "PublicTypeVersionReference":
        '''(experimental) A reference to a PublicTypeVersion resource.

        :stability: experimental
        '''
        return typing.cast("PublicTypeVersionReference", jsii.get(self, "publicTypeVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublicTypeVersionRef).__jsii_proxy_class__ = lambda : _IPublicTypeVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IPublisherRef")
class IPublisherRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Publisher.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="publisherRef")
    def publisher_ref(self) -> "PublisherReference":
        '''(experimental) A reference to a Publisher resource.

        :stability: experimental
        '''
        ...


class _IPublisherRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Publisher.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IPublisherRef"

    @builtins.property
    @jsii.member(jsii_name="publisherRef")
    def publisher_ref(self) -> "PublisherReference":
        '''(experimental) A reference to a Publisher resource.

        :stability: experimental
        '''
        return typing.cast("PublisherReference", jsii.get(self, "publisherRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublisherRef).__jsii_proxy_class__ = lambda : _IPublisherRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IResourceDefaultVersionRef"
)
class IResourceDefaultVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceDefaultVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceDefaultVersionRef")
    def resource_default_version_ref(self) -> "ResourceDefaultVersionReference":
        '''(experimental) A reference to a ResourceDefaultVersion resource.

        :stability: experimental
        '''
        ...


class _IResourceDefaultVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceDefaultVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IResourceDefaultVersionRef"

    @builtins.property
    @jsii.member(jsii_name="resourceDefaultVersionRef")
    def resource_default_version_ref(self) -> "ResourceDefaultVersionReference":
        '''(experimental) A reference to a ResourceDefaultVersion resource.

        :stability: experimental
        '''
        return typing.cast("ResourceDefaultVersionReference", jsii.get(self, "resourceDefaultVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceDefaultVersionRef).__jsii_proxy_class__ = lambda : _IResourceDefaultVersionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IResourceVersionRef"
)
class IResourceVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceVersionRef")
    def resource_version_ref(self) -> "ResourceVersionReference":
        '''(experimental) A reference to a ResourceVersion resource.

        :stability: experimental
        '''
        ...


class _IResourceVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ResourceVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IResourceVersionRef"

    @builtins.property
    @jsii.member(jsii_name="resourceVersionRef")
    def resource_version_ref(self) -> "ResourceVersionReference":
        '''(experimental) A reference to a ResourceVersion resource.

        :stability: experimental
        '''
        return typing.cast("ResourceVersionReference", jsii.get(self, "resourceVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceVersionRef).__jsii_proxy_class__ = lambda : _IResourceVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IStackRef")
class IStackRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Stack.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stackRef")
    def stack_ref(self) -> "StackReference":
        '''(experimental) A reference to a Stack resource.

        :stability: experimental
        '''
        ...


class _IStackRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Stack.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IStackRef"

    @builtins.property
    @jsii.member(jsii_name="stackRef")
    def stack_ref(self) -> "StackReference":
        '''(experimental) A reference to a Stack resource.

        :stability: experimental
        '''
        return typing.cast("StackReference", jsii.get(self, "stackRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackRef).__jsii_proxy_class__ = lambda : _IStackRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IStackSetRef")
class IStackSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StackSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stackSetRef")
    def stack_set_ref(self) -> "StackSetReference":
        '''(experimental) A reference to a StackSet resource.

        :stability: experimental
        '''
        ...


class _IStackSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StackSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IStackSetRef"

    @builtins.property
    @jsii.member(jsii_name="stackSetRef")
    def stack_set_ref(self) -> "StackSetReference":
        '''(experimental) A reference to a StackSet resource.

        :stability: experimental
        '''
        return typing.cast("StackSetReference", jsii.get(self, "stackSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStackSetRef).__jsii_proxy_class__ = lambda : _IStackSetRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.ITypeActivationRef"
)
class ITypeActivationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TypeActivation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="typeActivationRef")
    def type_activation_ref(self) -> "TypeActivationReference":
        '''(experimental) A reference to a TypeActivation resource.

        :stability: experimental
        '''
        ...


class _ITypeActivationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TypeActivation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.ITypeActivationRef"

    @builtins.property
    @jsii.member(jsii_name="typeActivationRef")
    def type_activation_ref(self) -> "TypeActivationReference":
        '''(experimental) A reference to a TypeActivation resource.

        :stability: experimental
        '''
        return typing.cast("TypeActivationReference", jsii.get(self, "typeActivationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITypeActivationRef).__jsii_proxy_class__ = lambda : _ITypeActivationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IWaitConditionHandleRef"
)
class IWaitConditionHandleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WaitConditionHandle.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="waitConditionHandleRef")
    def wait_condition_handle_ref(self) -> "WaitConditionHandleReference":
        '''(experimental) A reference to a WaitConditionHandle resource.

        :stability: experimental
        '''
        ...


class _IWaitConditionHandleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WaitConditionHandle.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IWaitConditionHandleRef"

    @builtins.property
    @jsii.member(jsii_name="waitConditionHandleRef")
    def wait_condition_handle_ref(self) -> "WaitConditionHandleReference":
        '''(experimental) A reference to a WaitConditionHandle resource.

        :stability: experimental
        '''
        return typing.cast("WaitConditionHandleReference", jsii.get(self, "waitConditionHandleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWaitConditionHandleRef).__jsii_proxy_class__ = lambda : _IWaitConditionHandleRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.IWaitConditionRef"
)
class IWaitConditionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WaitCondition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="waitConditionRef")
    def wait_condition_ref(self) -> "WaitConditionReference":
        '''(experimental) A reference to a WaitCondition resource.

        :stability: experimental
        '''
        ...


class _IWaitConditionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WaitCondition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_cloudformation.IWaitConditionRef"

    @builtins.property
    @jsii.member(jsii_name="waitConditionRef")
    def wait_condition_ref(self) -> "WaitConditionReference":
        '''(experimental) A reference to a WaitCondition resource.

        :stability: experimental
        '''
        return typing.cast("WaitConditionReference", jsii.get(self, "waitConditionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWaitConditionRef).__jsii_proxy_class__ = lambda : _IWaitConditionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.LambdaHookReference",
    jsii_struct_bases=[],
    name_mapping={"hook_arn": "hookArn"},
)
class LambdaHookReference:
    def __init__(self, *, hook_arn: builtins.str) -> None:
        '''A reference to a LambdaHook resource.

        :param hook_arn: The HookArn of the LambdaHook resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            lambda_hook_reference = interfaces_cloudformation.LambdaHookReference(
                hook_arn="hookArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e3e149c2cd60a1f4cbf516eb637ccb933da9baf121c066add455af8325df39a)
            check_type(argname="argument hook_arn", value=hook_arn, expected_type=type_hints["hook_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hook_arn": hook_arn,
        }

    @builtins.property
    def hook_arn(self) -> builtins.str:
        '''The HookArn of the LambdaHook resource.'''
        result = self._values.get("hook_arn")
        assert result is not None, "Required property 'hook_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaHookReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.MacroReference",
    jsii_struct_bases=[],
    name_mapping={"macro_id": "macroId"},
)
class MacroReference:
    def __init__(self, *, macro_id: builtins.str) -> None:
        '''A reference to a Macro resource.

        :param macro_id: The Id of the Macro resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            macro_reference = interfaces_cloudformation.MacroReference(
                macro_id="macroId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__366a7715c180b8366595d728f6b7187f9dff8b33626b1e127c98125ef79544af)
            check_type(argname="argument macro_id", value=macro_id, expected_type=type_hints["macro_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "macro_id": macro_id,
        }

    @builtins.property
    def macro_id(self) -> builtins.str:
        '''The Id of the Macro resource.'''
        result = self._values.get("macro_id")
        assert result is not None, "Required property 'macro_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MacroReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.ModuleDefaultVersionReference",
    jsii_struct_bases=[],
    name_mapping={"module_default_version_arn": "moduleDefaultVersionArn"},
)
class ModuleDefaultVersionReference:
    def __init__(self, *, module_default_version_arn: builtins.str) -> None:
        '''A reference to a ModuleDefaultVersion resource.

        :param module_default_version_arn: The Arn of the ModuleDefaultVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            module_default_version_reference = interfaces_cloudformation.ModuleDefaultVersionReference(
                module_default_version_arn="moduleDefaultVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1473fbf7e79219893e9298fa36b5f862fdef7e8b1af71e233a42d6186c98295c)
            check_type(argname="argument module_default_version_arn", value=module_default_version_arn, expected_type=type_hints["module_default_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "module_default_version_arn": module_default_version_arn,
        }

    @builtins.property
    def module_default_version_arn(self) -> builtins.str:
        '''The Arn of the ModuleDefaultVersion resource.'''
        result = self._values.get("module_default_version_arn")
        assert result is not None, "Required property 'module_default_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModuleDefaultVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.ModuleVersionReference",
    jsii_struct_bases=[],
    name_mapping={"module_version_arn": "moduleVersionArn"},
)
class ModuleVersionReference:
    def __init__(self, *, module_version_arn: builtins.str) -> None:
        '''A reference to a ModuleVersion resource.

        :param module_version_arn: The Arn of the ModuleVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            module_version_reference = interfaces_cloudformation.ModuleVersionReference(
                module_version_arn="moduleVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a65c00ebebea4a4b826cdbacf2a78f91c0c8969030eb148a097375b93ee26475)
            check_type(argname="argument module_version_arn", value=module_version_arn, expected_type=type_hints["module_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "module_version_arn": module_version_arn,
        }

    @builtins.property
    def module_version_arn(self) -> builtins.str:
        '''The Arn of the ModuleVersion resource.'''
        result = self._values.get("module_version_arn")
        assert result is not None, "Required property 'module_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ModuleVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.PublicTypeVersionReference",
    jsii_struct_bases=[],
    name_mapping={"public_type_arn": "publicTypeArn"},
)
class PublicTypeVersionReference:
    def __init__(self, *, public_type_arn: builtins.str) -> None:
        '''A reference to a PublicTypeVersion resource.

        :param public_type_arn: The PublicTypeArn of the PublicTypeVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            public_type_version_reference = interfaces_cloudformation.PublicTypeVersionReference(
                public_type_arn="publicTypeArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6908473a67abdf74221854b71a6b8fa8e43350247630952cb02ef56a16a3a88)
            check_type(argname="argument public_type_arn", value=public_type_arn, expected_type=type_hints["public_type_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "public_type_arn": public_type_arn,
        }

    @builtins.property
    def public_type_arn(self) -> builtins.str:
        '''The PublicTypeArn of the PublicTypeVersion resource.'''
        result = self._values.get("public_type_arn")
        assert result is not None, "Required property 'public_type_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicTypeVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.PublisherReference",
    jsii_struct_bases=[],
    name_mapping={"publisher_id": "publisherId"},
)
class PublisherReference:
    def __init__(self, *, publisher_id: builtins.str) -> None:
        '''A reference to a Publisher resource.

        :param publisher_id: The PublisherId of the Publisher resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            publisher_reference = interfaces_cloudformation.PublisherReference(
                publisher_id="publisherId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e30b58013075f9a66218400828f24e5a7fc49ae648010f729db35325b0e53e6e)
            check_type(argname="argument publisher_id", value=publisher_id, expected_type=type_hints["publisher_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "publisher_id": publisher_id,
        }

    @builtins.property
    def publisher_id(self) -> builtins.str:
        '''The PublisherId of the Publisher resource.'''
        result = self._values.get("publisher_id")
        assert result is not None, "Required property 'publisher_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublisherReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.ResourceDefaultVersionReference",
    jsii_struct_bases=[],
    name_mapping={"resource_default_version_arn": "resourceDefaultVersionArn"},
)
class ResourceDefaultVersionReference:
    def __init__(self, *, resource_default_version_arn: builtins.str) -> None:
        '''A reference to a ResourceDefaultVersion resource.

        :param resource_default_version_arn: The Arn of the ResourceDefaultVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            resource_default_version_reference = interfaces_cloudformation.ResourceDefaultVersionReference(
                resource_default_version_arn="resourceDefaultVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd89a00f795ff43273f16fd4e8d86052b8de8d8cdc1cf2ef6bafe998f17b0027)
            check_type(argname="argument resource_default_version_arn", value=resource_default_version_arn, expected_type=type_hints["resource_default_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_default_version_arn": resource_default_version_arn,
        }

    @builtins.property
    def resource_default_version_arn(self) -> builtins.str:
        '''The Arn of the ResourceDefaultVersion resource.'''
        result = self._values.get("resource_default_version_arn")
        assert result is not None, "Required property 'resource_default_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceDefaultVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.ResourceVersionReference",
    jsii_struct_bases=[],
    name_mapping={"resource_version_arn": "resourceVersionArn"},
)
class ResourceVersionReference:
    def __init__(self, *, resource_version_arn: builtins.str) -> None:
        '''A reference to a ResourceVersion resource.

        :param resource_version_arn: The Arn of the ResourceVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            resource_version_reference = interfaces_cloudformation.ResourceVersionReference(
                resource_version_arn="resourceVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7afe7f88b7b3fcd57c7d29a6b5b149948932e7b0307ab06381241d082b4405c)
            check_type(argname="argument resource_version_arn", value=resource_version_arn, expected_type=type_hints["resource_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_version_arn": resource_version_arn,
        }

    @builtins.property
    def resource_version_arn(self) -> builtins.str:
        '''The Arn of the ResourceVersion resource.'''
        result = self._values.get("resource_version_arn")
        assert result is not None, "Required property 'resource_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.StackReference",
    jsii_struct_bases=[],
    name_mapping={"stack_id": "stackId"},
)
class StackReference:
    def __init__(self, *, stack_id: builtins.str) -> None:
        '''A reference to a Stack resource.

        :param stack_id: The StackId of the Stack resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            stack_reference = interfaces_cloudformation.StackReference(
                stack_id="stackId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6be9545bf5a86ea5129685abb086ec5c7023f1f26f6fafbebda4620a6d57b7c)
            check_type(argname="argument stack_id", value=stack_id, expected_type=type_hints["stack_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stack_id": stack_id,
        }

    @builtins.property
    def stack_id(self) -> builtins.str:
        '''The StackId of the Stack resource.'''
        result = self._values.get("stack_id")
        assert result is not None, "Required property 'stack_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.StackSetReference",
    jsii_struct_bases=[],
    name_mapping={"stack_set_id": "stackSetId"},
)
class StackSetReference:
    def __init__(self, *, stack_set_id: builtins.str) -> None:
        '''A reference to a StackSet resource.

        :param stack_set_id: The StackSetId of the StackSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            stack_set_reference = interfaces_cloudformation.StackSetReference(
                stack_set_id="stackSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c9319f9e4b031c1fcadb66d55b5d5ecc5b80323ab4ec3ff28175eaf9653ffbc)
            check_type(argname="argument stack_set_id", value=stack_set_id, expected_type=type_hints["stack_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stack_set_id": stack_set_id,
        }

    @builtins.property
    def stack_set_id(self) -> builtins.str:
        '''The StackSetId of the StackSet resource.'''
        result = self._values.get("stack_set_id")
        assert result is not None, "Required property 'stack_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StackSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.TypeActivationReference",
    jsii_struct_bases=[],
    name_mapping={"type_activation_arn": "typeActivationArn"},
)
class TypeActivationReference:
    def __init__(self, *, type_activation_arn: builtins.str) -> None:
        '''A reference to a TypeActivation resource.

        :param type_activation_arn: The Arn of the TypeActivation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            type_activation_reference = interfaces_cloudformation.TypeActivationReference(
                type_activation_arn="typeActivationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26329ee952aa28a16422cf96de9a99c6c0c8ac8e65f8a956838d06fd71caeac7)
            check_type(argname="argument type_activation_arn", value=type_activation_arn, expected_type=type_hints["type_activation_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type_activation_arn": type_activation_arn,
        }

    @builtins.property
    def type_activation_arn(self) -> builtins.str:
        '''The Arn of the TypeActivation resource.'''
        result = self._values.get("type_activation_arn")
        assert result is not None, "Required property 'type_activation_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TypeActivationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.WaitConditionHandleReference",
    jsii_struct_bases=[],
    name_mapping={"wait_condition_handle_id": "waitConditionHandleId"},
)
class WaitConditionHandleReference:
    def __init__(self, *, wait_condition_handle_id: builtins.str) -> None:
        '''A reference to a WaitConditionHandle resource.

        :param wait_condition_handle_id: The Id of the WaitConditionHandle resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            wait_condition_handle_reference = interfaces_cloudformation.WaitConditionHandleReference(
                wait_condition_handle_id="waitConditionHandleId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddc6bfcf32d0990155c44ccab804f3e6c6dddb9cb279ee3bb4506b6f0b08875c)
            check_type(argname="argument wait_condition_handle_id", value=wait_condition_handle_id, expected_type=type_hints["wait_condition_handle_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "wait_condition_handle_id": wait_condition_handle_id,
        }

    @builtins.property
    def wait_condition_handle_id(self) -> builtins.str:
        '''The Id of the WaitConditionHandle resource.'''
        result = self._values.get("wait_condition_handle_id")
        assert result is not None, "Required property 'wait_condition_handle_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WaitConditionHandleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_cloudformation.WaitConditionReference",
    jsii_struct_bases=[],
    name_mapping={"wait_condition_id": "waitConditionId"},
)
class WaitConditionReference:
    def __init__(self, *, wait_condition_id: builtins.str) -> None:
        '''A reference to a WaitCondition resource.

        :param wait_condition_id: The Id of the WaitCondition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_cloudformation as interfaces_cloudformation
            
            wait_condition_reference = interfaces_cloudformation.WaitConditionReference(
                wait_condition_id="waitConditionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d396cb2698def31eae15c415fd26053d72bd38dd3d779cb62542b599b36f389b)
            check_type(argname="argument wait_condition_id", value=wait_condition_id, expected_type=type_hints["wait_condition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "wait_condition_id": wait_condition_id,
        }

    @builtins.property
    def wait_condition_id(self) -> builtins.str:
        '''The Id of the WaitCondition resource.'''
        result = self._values.get("wait_condition_id")
        assert result is not None, "Required property 'wait_condition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WaitConditionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CustomResourceReference",
    "GuardHookReference",
    "HookDefaultVersionReference",
    "HookTypeConfigReference",
    "HookVersionReference",
    "ICustomResourceRef",
    "IGuardHookRef",
    "IHookDefaultVersionRef",
    "IHookTypeConfigRef",
    "IHookVersionRef",
    "ILambdaHookRef",
    "IMacroRef",
    "IModuleDefaultVersionRef",
    "IModuleVersionRef",
    "IPublicTypeVersionRef",
    "IPublisherRef",
    "IResourceDefaultVersionRef",
    "IResourceVersionRef",
    "IStackRef",
    "IStackSetRef",
    "ITypeActivationRef",
    "IWaitConditionHandleRef",
    "IWaitConditionRef",
    "LambdaHookReference",
    "MacroReference",
    "ModuleDefaultVersionReference",
    "ModuleVersionReference",
    "PublicTypeVersionReference",
    "PublisherReference",
    "ResourceDefaultVersionReference",
    "ResourceVersionReference",
    "StackReference",
    "StackSetReference",
    "TypeActivationReference",
    "WaitConditionHandleReference",
    "WaitConditionReference",
]

publication.publish()

def _typecheckingstub__5b7c6fc64f1a76292b3e9c451ff5d2ef2906f21f9ee7be7f2213d5cbc5e2d8d0(
    *,
    custom_resource_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__775ac6fdd8641de5fd9822abf6f886825b2f6e4892f6bdf2d249a6c799b83b70(
    *,
    hook_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6d0b56d2950ab15ec15c230e341be18d0f0974ea5d59e387f7232dad93053cb(
    *,
    hook_default_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3b50301833de36cb0604dcfcaa3be80edace6d3e1a0e6006db4da13bc85b78e(
    *,
    configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__266211dcc23f86069691e9aa5c7355e16923c23e8b1e58b1c126f6521314dd38(
    *,
    hook_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e3e149c2cd60a1f4cbf516eb637ccb933da9baf121c066add455af8325df39a(
    *,
    hook_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__366a7715c180b8366595d728f6b7187f9dff8b33626b1e127c98125ef79544af(
    *,
    macro_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1473fbf7e79219893e9298fa36b5f862fdef7e8b1af71e233a42d6186c98295c(
    *,
    module_default_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a65c00ebebea4a4b826cdbacf2a78f91c0c8969030eb148a097375b93ee26475(
    *,
    module_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6908473a67abdf74221854b71a6b8fa8e43350247630952cb02ef56a16a3a88(
    *,
    public_type_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e30b58013075f9a66218400828f24e5a7fc49ae648010f729db35325b0e53e6e(
    *,
    publisher_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd89a00f795ff43273f16fd4e8d86052b8de8d8cdc1cf2ef6bafe998f17b0027(
    *,
    resource_default_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7afe7f88b7b3fcd57c7d29a6b5b149948932e7b0307ab06381241d082b4405c(
    *,
    resource_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6be9545bf5a86ea5129685abb086ec5c7023f1f26f6fafbebda4620a6d57b7c(
    *,
    stack_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9319f9e4b031c1fcadb66d55b5d5ecc5b80323ab4ec3ff28175eaf9653ffbc(
    *,
    stack_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26329ee952aa28a16422cf96de9a99c6c0c8ac8e65f8a956838d06fd71caeac7(
    *,
    type_activation_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddc6bfcf32d0990155c44ccab804f3e6c6dddb9cb279ee3bb4506b6f0b08875c(
    *,
    wait_condition_handle_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d396cb2698def31eae15c415fd26053d72bd38dd3d779cb62542b599b36f389b(
    *,
    wait_condition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICustomResourceRef, IGuardHookRef, IHookDefaultVersionRef, IHookTypeConfigRef, IHookVersionRef, ILambdaHookRef, IMacroRef, IModuleDefaultVersionRef, IModuleVersionRef, IPublicTypeVersionRef, IPublisherRef, IResourceDefaultVersionRef, IResourceVersionRef, IStackRef, IStackSetRef, ITypeActivationRef, IWaitConditionHandleRef, IWaitConditionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
