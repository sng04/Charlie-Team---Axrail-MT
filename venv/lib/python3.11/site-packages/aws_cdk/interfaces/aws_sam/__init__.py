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
    jsii_type="aws-cdk-lib.interfaces.aws_sam.ApiReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApiReference:
    def __init__(self) -> None:
        '''A reference to a Api resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sam as interfaces_sam
            
            api_reference = interfaces_sam.ApiReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sam.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class ApplicationReference:
    def __init__(self) -> None:
        '''A reference to a Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sam as interfaces_sam
            
            application_reference = interfaces_sam.ApplicationReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sam.FunctionReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class FunctionReference:
    def __init__(self) -> None:
        '''A reference to a Function resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sam as interfaces_sam
            
            function_reference = interfaces_sam.FunctionReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sam.HttpApiReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class HttpApiReference:
    def __init__(self) -> None:
        '''A reference to a HttpApi resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sam as interfaces_sam
            
            http_api_reference = interfaces_sam.HttpApiReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpApiReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sam.IApiRef")
class IApiRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Api.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apiRef")
    def api_ref(self) -> "ApiReference":
        '''(experimental) A reference to a Api resource.

        :stability: experimental
        '''
        ...


class _IApiRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Api.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sam.IApiRef"

    @builtins.property
    @jsii.member(jsii_name="apiRef")
    def api_ref(self) -> "ApiReference":
        '''(experimental) A reference to a Api resource.

        :stability: experimental
        '''
        return typing.cast("ApiReference", jsii.get(self, "apiRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiRef).__jsii_proxy_class__ = lambda : _IApiRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sam.IApplicationRef")
class IApplicationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        ...


class _IApplicationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Application.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sam.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sam.IFunctionRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sam.IFunctionRef"

    @builtins.property
    @jsii.member(jsii_name="functionRef")
    def function_ref(self) -> "FunctionReference":
        '''(experimental) A reference to a Function resource.

        :stability: experimental
        '''
        return typing.cast("FunctionReference", jsii.get(self, "functionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFunctionRef).__jsii_proxy_class__ = lambda : _IFunctionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sam.IHttpApiRef")
class IHttpApiRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a HttpApi.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="httpApiRef")
    def http_api_ref(self) -> "HttpApiReference":
        '''(experimental) A reference to a HttpApi resource.

        :stability: experimental
        '''
        ...


class _IHttpApiRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a HttpApi.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sam.IHttpApiRef"

    @builtins.property
    @jsii.member(jsii_name="httpApiRef")
    def http_api_ref(self) -> "HttpApiReference":
        '''(experimental) A reference to a HttpApi resource.

        :stability: experimental
        '''
        return typing.cast("HttpApiReference", jsii.get(self, "httpApiRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHttpApiRef).__jsii_proxy_class__ = lambda : _IHttpApiRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sam.ILayerVersionRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sam.ILayerVersionRef"

    @builtins.property
    @jsii.member(jsii_name="layerVersionRef")
    def layer_version_ref(self) -> "LayerVersionReference":
        '''(experimental) A reference to a LayerVersion resource.

        :stability: experimental
        '''
        return typing.cast("LayerVersionReference", jsii.get(self, "layerVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILayerVersionRef).__jsii_proxy_class__ = lambda : _ILayerVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sam.ISimpleTableRef")
class ISimpleTableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SimpleTable.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="simpleTableRef")
    def simple_table_ref(self) -> "SimpleTableReference":
        '''(experimental) A reference to a SimpleTable resource.

        :stability: experimental
        '''
        ...


class _ISimpleTableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SimpleTable.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sam.ISimpleTableRef"

    @builtins.property
    @jsii.member(jsii_name="simpleTableRef")
    def simple_table_ref(self) -> "SimpleTableReference":
        '''(experimental) A reference to a SimpleTable resource.

        :stability: experimental
        '''
        return typing.cast("SimpleTableReference", jsii.get(self, "simpleTableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISimpleTableRef).__jsii_proxy_class__ = lambda : _ISimpleTableRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_sam.IStateMachineRef")
class IStateMachineRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a StateMachine.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="stateMachineRef")
    def state_machine_ref(self) -> "StateMachineReference":
        '''(experimental) A reference to a StateMachine resource.

        :stability: experimental
        '''
        ...


class _IStateMachineRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a StateMachine.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_sam.IStateMachineRef"

    @builtins.property
    @jsii.member(jsii_name="stateMachineRef")
    def state_machine_ref(self) -> "StateMachineReference":
        '''(experimental) A reference to a StateMachine resource.

        :stability: experimental
        '''
        return typing.cast("StateMachineReference", jsii.get(self, "stateMachineRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IStateMachineRef).__jsii_proxy_class__ = lambda : _IStateMachineRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sam.LayerVersionReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class LayerVersionReference:
    def __init__(self) -> None:
        '''A reference to a LayerVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sam as interfaces_sam
            
            layer_version_reference = interfaces_sam.LayerVersionReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LayerVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sam.SimpleTableReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class SimpleTableReference:
    def __init__(self) -> None:
        '''A reference to a SimpleTable resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sam as interfaces_sam
            
            simple_table_reference = interfaces_sam.SimpleTableReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SimpleTableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_sam.StateMachineReference",
    jsii_struct_bases=[],
    name_mapping={},
)
class StateMachineReference:
    def __init__(self) -> None:
        '''A reference to a StateMachine resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_sam as interfaces_sam
            
            state_machine_reference = interfaces_sam.StateMachineReference()
        '''
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StateMachineReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiReference",
    "ApplicationReference",
    "FunctionReference",
    "HttpApiReference",
    "IApiRef",
    "IApplicationRef",
    "IFunctionRef",
    "IHttpApiRef",
    "ILayerVersionRef",
    "ISimpleTableRef",
    "IStateMachineRef",
    "LayerVersionReference",
    "SimpleTableReference",
    "StateMachineReference",
]

publication.publish()

for cls in [IApiRef, IApplicationRef, IFunctionRef, IHttpApiRef, ILayerVersionRef, ISimpleTableRef, IStateMachineRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
