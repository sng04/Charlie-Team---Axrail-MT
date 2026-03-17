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
    jsii_type="aws-cdk-lib.interfaces.aws_amplifyuibuilder.ComponentReference",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "component_id": "componentId",
        "environment_name": "environmentName",
    },
)
class ComponentReference:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        component_id: builtins.str,
        environment_name: builtins.str,
    ) -> None:
        '''A reference to a Component resource.

        :param app_id: The AppId of the Component resource.
        :param component_id: The Id of the Component resource.
        :param environment_name: The EnvironmentName of the Component resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_amplifyuibuilder as interfaces_amplifyuibuilder
            
            component_reference = interfaces_amplifyuibuilder.ComponentReference(
                app_id="appId",
                component_id="componentId",
                environment_name="environmentName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3db2cf173de1ecd1b81095e2f9e746f608829598ca99e775cb93df9c8e0769b)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
            check_type(argname="argument component_id", value=component_id, expected_type=type_hints["component_id"])
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
            "component_id": component_id,
            "environment_name": environment_name,
        }

    @builtins.property
    def app_id(self) -> builtins.str:
        '''The AppId of the Component resource.'''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def component_id(self) -> builtins.str:
        '''The Id of the Component resource.'''
        result = self._values.get("component_id")
        assert result is not None, "Required property 'component_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_name(self) -> builtins.str:
        '''The EnvironmentName of the Component resource.'''
        result = self._values.get("environment_name")
        assert result is not None, "Required property 'environment_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComponentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_amplifyuibuilder.FormReference",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "environment_name": "environmentName",
        "form_id": "formId",
    },
)
class FormReference:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        environment_name: builtins.str,
        form_id: builtins.str,
    ) -> None:
        '''A reference to a Form resource.

        :param app_id: The AppId of the Form resource.
        :param environment_name: The EnvironmentName of the Form resource.
        :param form_id: The Id of the Form resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_amplifyuibuilder as interfaces_amplifyuibuilder
            
            form_reference = interfaces_amplifyuibuilder.FormReference(
                app_id="appId",
                environment_name="environmentName",
                form_id="formId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eea402a898cb91c9699c35d33ddc6857343d860854d4a480e50dbe9b5addc026)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
            check_type(argname="argument form_id", value=form_id, expected_type=type_hints["form_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
            "environment_name": environment_name,
            "form_id": form_id,
        }

    @builtins.property
    def app_id(self) -> builtins.str:
        '''The AppId of the Form resource.'''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_name(self) -> builtins.str:
        '''The EnvironmentName of the Form resource.'''
        result = self._values.get("environment_name")
        assert result is not None, "Required property 'environment_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def form_id(self) -> builtins.str:
        '''The Id of the Form resource.'''
        result = self._values.get("form_id")
        assert result is not None, "Required property 'form_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FormReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_amplifyuibuilder.IComponentRef")
class IComponentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Component.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="componentRef")
    def component_ref(self) -> "ComponentReference":
        '''(experimental) A reference to a Component resource.

        :stability: experimental
        '''
        ...


class _IComponentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Component.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_amplifyuibuilder.IComponentRef"

    @builtins.property
    @jsii.member(jsii_name="componentRef")
    def component_ref(self) -> "ComponentReference":
        '''(experimental) A reference to a Component resource.

        :stability: experimental
        '''
        return typing.cast("ComponentReference", jsii.get(self, "componentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IComponentRef).__jsii_proxy_class__ = lambda : _IComponentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_amplifyuibuilder.IFormRef")
class IFormRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Form.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="formRef")
    def form_ref(self) -> "FormReference":
        '''(experimental) A reference to a Form resource.

        :stability: experimental
        '''
        ...


class _IFormRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Form.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_amplifyuibuilder.IFormRef"

    @builtins.property
    @jsii.member(jsii_name="formRef")
    def form_ref(self) -> "FormReference":
        '''(experimental) A reference to a Form resource.

        :stability: experimental
        '''
        return typing.cast("FormReference", jsii.get(self, "formRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFormRef).__jsii_proxy_class__ = lambda : _IFormRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_amplifyuibuilder.IThemeRef")
class IThemeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Theme.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="themeRef")
    def theme_ref(self) -> "ThemeReference":
        '''(experimental) A reference to a Theme resource.

        :stability: experimental
        '''
        ...


class _IThemeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Theme.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_amplifyuibuilder.IThemeRef"

    @builtins.property
    @jsii.member(jsii_name="themeRef")
    def theme_ref(self) -> "ThemeReference":
        '''(experimental) A reference to a Theme resource.

        :stability: experimental
        '''
        return typing.cast("ThemeReference", jsii.get(self, "themeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IThemeRef).__jsii_proxy_class__ = lambda : _IThemeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_amplifyuibuilder.ThemeReference",
    jsii_struct_bases=[],
    name_mapping={
        "app_id": "appId",
        "environment_name": "environmentName",
        "theme_id": "themeId",
    },
)
class ThemeReference:
    def __init__(
        self,
        *,
        app_id: builtins.str,
        environment_name: builtins.str,
        theme_id: builtins.str,
    ) -> None:
        '''A reference to a Theme resource.

        :param app_id: The AppId of the Theme resource.
        :param environment_name: The EnvironmentName of the Theme resource.
        :param theme_id: The Id of the Theme resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_amplifyuibuilder as interfaces_amplifyuibuilder
            
            theme_reference = interfaces_amplifyuibuilder.ThemeReference(
                app_id="appId",
                environment_name="environmentName",
                theme_id="themeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__586ab3e86d97387a47bc7f44c2e6233cbe06e304bb8afa0beab77965fc5131cd)
            check_type(argname="argument app_id", value=app_id, expected_type=type_hints["app_id"])
            check_type(argname="argument environment_name", value=environment_name, expected_type=type_hints["environment_name"])
            check_type(argname="argument theme_id", value=theme_id, expected_type=type_hints["theme_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_id": app_id,
            "environment_name": environment_name,
            "theme_id": theme_id,
        }

    @builtins.property
    def app_id(self) -> builtins.str:
        '''The AppId of the Theme resource.'''
        result = self._values.get("app_id")
        assert result is not None, "Required property 'app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_name(self) -> builtins.str:
        '''The EnvironmentName of the Theme resource.'''
        result = self._values.get("environment_name")
        assert result is not None, "Required property 'environment_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def theme_id(self) -> builtins.str:
        '''The Id of the Theme resource.'''
        result = self._values.get("theme_id")
        assert result is not None, "Required property 'theme_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThemeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ComponentReference",
    "FormReference",
    "IComponentRef",
    "IFormRef",
    "IThemeRef",
    "ThemeReference",
]

publication.publish()

def _typecheckingstub__c3db2cf173de1ecd1b81095e2f9e746f608829598ca99e775cb93df9c8e0769b(
    *,
    app_id: builtins.str,
    component_id: builtins.str,
    environment_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eea402a898cb91c9699c35d33ddc6857343d860854d4a480e50dbe9b5addc026(
    *,
    app_id: builtins.str,
    environment_name: builtins.str,
    form_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__586ab3e86d97387a47bc7f44c2e6233cbe06e304bb8afa0beab77965fc5131cd(
    *,
    app_id: builtins.str,
    environment_name: builtins.str,
    theme_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IComponentRef, IFormRef, IThemeRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
