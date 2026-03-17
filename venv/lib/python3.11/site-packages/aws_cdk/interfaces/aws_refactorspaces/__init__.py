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
    jsii_type="aws-cdk-lib.interfaces.aws_refactorspaces.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_arn": "applicationArn",
        "application_identifier": "applicationIdentifier",
        "environment_identifier": "environmentIdentifier",
    },
)
class ApplicationReference:
    def __init__(
        self,
        *,
        application_arn: builtins.str,
        application_identifier: builtins.str,
        environment_identifier: builtins.str,
    ) -> None:
        '''A reference to a Application resource.

        :param application_arn: The ARN of the Application resource.
        :param application_identifier: The ApplicationIdentifier of the Application resource.
        :param environment_identifier: The EnvironmentIdentifier of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_refactorspaces as interfaces_refactorspaces
            
            application_reference = interfaces_refactorspaces.ApplicationReference(
                application_arn="applicationArn",
                application_identifier="applicationIdentifier",
                environment_identifier="environmentIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__799af1f3a3bf1d71326ad9248fa7ad5a1fb6ba6306710c0c1ff544d217788207)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument application_identifier", value=application_identifier, expected_type=type_hints["application_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
            "application_identifier": application_identifier,
            "environment_identifier": environment_identifier,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ARN of the Application resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_identifier(self) -> builtins.str:
        '''The ApplicationIdentifier of the Application resource.'''
        result = self._values.get("application_identifier")
        assert result is not None, "Required property 'application_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The EnvironmentIdentifier of the Application resource.'''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_refactorspaces.EnvironmentReference",
    jsii_struct_bases=[],
    name_mapping={
        "environment_arn": "environmentArn",
        "environment_identifier": "environmentIdentifier",
    },
)
class EnvironmentReference:
    def __init__(
        self,
        *,
        environment_arn: builtins.str,
        environment_identifier: builtins.str,
    ) -> None:
        '''A reference to a Environment resource.

        :param environment_arn: The ARN of the Environment resource.
        :param environment_identifier: The EnvironmentIdentifier of the Environment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_refactorspaces as interfaces_refactorspaces
            
            environment_reference = interfaces_refactorspaces.EnvironmentReference(
                environment_arn="environmentArn",
                environment_identifier="environmentIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5d4ad8dcbd232c03cf9017a97966b00a30a021e86bb1d5f88fe983b1b03776a)
            check_type(argname="argument environment_arn", value=environment_arn, expected_type=type_hints["environment_arn"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment_arn": environment_arn,
            "environment_identifier": environment_identifier,
        }

    @builtins.property
    def environment_arn(self) -> builtins.str:
        '''The ARN of the Environment resource.'''
        result = self._values.get("environment_arn")
        assert result is not None, "Required property 'environment_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The EnvironmentIdentifier of the Environment resource.'''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_refactorspaces.IApplicationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_refactorspaces.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_refactorspaces.IEnvironmentRef")
class IEnvironmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Environment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Environment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_refactorspaces.IEnvironmentRef"

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentReference", jsii.get(self, "environmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentRef).__jsii_proxy_class__ = lambda : _IEnvironmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_refactorspaces.IRouteRef")
class IRouteRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Route.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="routeRef")
    def route_ref(self) -> "RouteReference":
        '''(experimental) A reference to a Route resource.

        :stability: experimental
        '''
        ...


class _IRouteRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Route.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_refactorspaces.IRouteRef"

    @builtins.property
    @jsii.member(jsii_name="routeRef")
    def route_ref(self) -> "RouteReference":
        '''(experimental) A reference to a Route resource.

        :stability: experimental
        '''
        return typing.cast("RouteReference", jsii.get(self, "routeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRouteRef).__jsii_proxy_class__ = lambda : _IRouteRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_refactorspaces.IServiceRef")
class IServiceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        ...


class _IServiceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_refactorspaces.IServiceRef"

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        return typing.cast("ServiceReference", jsii.get(self, "serviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceRef).__jsii_proxy_class__ = lambda : _IServiceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_refactorspaces.RouteReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_identifier": "applicationIdentifier",
        "environment_identifier": "environmentIdentifier",
        "route_arn": "routeArn",
        "route_identifier": "routeIdentifier",
    },
)
class RouteReference:
    def __init__(
        self,
        *,
        application_identifier: builtins.str,
        environment_identifier: builtins.str,
        route_arn: builtins.str,
        route_identifier: builtins.str,
    ) -> None:
        '''A reference to a Route resource.

        :param application_identifier: The ApplicationIdentifier of the Route resource.
        :param environment_identifier: The EnvironmentIdentifier of the Route resource.
        :param route_arn: The ARN of the Route resource.
        :param route_identifier: The RouteIdentifier of the Route resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_refactorspaces as interfaces_refactorspaces
            
            route_reference = interfaces_refactorspaces.RouteReference(
                application_identifier="applicationIdentifier",
                environment_identifier="environmentIdentifier",
                route_arn="routeArn",
                route_identifier="routeIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5621a13f20aae1287d52b4b4d36bdab9f962b15dd6201e7007834938af03ab29)
            check_type(argname="argument application_identifier", value=application_identifier, expected_type=type_hints["application_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument route_arn", value=route_arn, expected_type=type_hints["route_arn"])
            check_type(argname="argument route_identifier", value=route_identifier, expected_type=type_hints["route_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_identifier": application_identifier,
            "environment_identifier": environment_identifier,
            "route_arn": route_arn,
            "route_identifier": route_identifier,
        }

    @builtins.property
    def application_identifier(self) -> builtins.str:
        '''The ApplicationIdentifier of the Route resource.'''
        result = self._values.get("application_identifier")
        assert result is not None, "Required property 'application_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The EnvironmentIdentifier of the Route resource.'''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_arn(self) -> builtins.str:
        '''The ARN of the Route resource.'''
        result = self._values.get("route_arn")
        assert result is not None, "Required property 'route_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_identifier(self) -> builtins.str:
        '''The RouteIdentifier of the Route resource.'''
        result = self._values.get("route_identifier")
        assert result is not None, "Required property 'route_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RouteReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_refactorspaces.ServiceReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_identifier": "applicationIdentifier",
        "environment_identifier": "environmentIdentifier",
        "service_arn": "serviceArn",
        "service_identifier": "serviceIdentifier",
    },
)
class ServiceReference:
    def __init__(
        self,
        *,
        application_identifier: builtins.str,
        environment_identifier: builtins.str,
        service_arn: builtins.str,
        service_identifier: builtins.str,
    ) -> None:
        '''A reference to a Service resource.

        :param application_identifier: The ApplicationIdentifier of the Service resource.
        :param environment_identifier: The EnvironmentIdentifier of the Service resource.
        :param service_arn: The ARN of the Service resource.
        :param service_identifier: The ServiceIdentifier of the Service resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_refactorspaces as interfaces_refactorspaces
            
            service_reference = interfaces_refactorspaces.ServiceReference(
                application_identifier="applicationIdentifier",
                environment_identifier="environmentIdentifier",
                service_arn="serviceArn",
                service_identifier="serviceIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f912079330eb23bba0021407c4236ba330fc1f76d77c6935ac96d17442a5383a)
            check_type(argname="argument application_identifier", value=application_identifier, expected_type=type_hints["application_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument service_arn", value=service_arn, expected_type=type_hints["service_arn"])
            check_type(argname="argument service_identifier", value=service_identifier, expected_type=type_hints["service_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_identifier": application_identifier,
            "environment_identifier": environment_identifier,
            "service_arn": service_arn,
            "service_identifier": service_identifier,
        }

    @builtins.property
    def application_identifier(self) -> builtins.str:
        '''The ApplicationIdentifier of the Service resource.'''
        result = self._values.get("application_identifier")
        assert result is not None, "Required property 'application_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The EnvironmentIdentifier of the Service resource.'''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_arn(self) -> builtins.str:
        '''The ARN of the Service resource.'''
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_identifier(self) -> builtins.str:
        '''The ServiceIdentifier of the Service resource.'''
        result = self._values.get("service_identifier")
        assert result is not None, "Required property 'service_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApplicationReference",
    "EnvironmentReference",
    "IApplicationRef",
    "IEnvironmentRef",
    "IRouteRef",
    "IServiceRef",
    "RouteReference",
    "ServiceReference",
]

publication.publish()

def _typecheckingstub__799af1f3a3bf1d71326ad9248fa7ad5a1fb6ba6306710c0c1ff544d217788207(
    *,
    application_arn: builtins.str,
    application_identifier: builtins.str,
    environment_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d4ad8dcbd232c03cf9017a97966b00a30a021e86bb1d5f88fe983b1b03776a(
    *,
    environment_arn: builtins.str,
    environment_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5621a13f20aae1287d52b4b4d36bdab9f962b15dd6201e7007834938af03ab29(
    *,
    application_identifier: builtins.str,
    environment_identifier: builtins.str,
    route_arn: builtins.str,
    route_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f912079330eb23bba0021407c4236ba330fc1f76d77c6935ac96d17442a5383a(
    *,
    application_identifier: builtins.str,
    environment_identifier: builtins.str,
    service_arn: builtins.str,
    service_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef, IEnvironmentRef, IRouteRef, IServiceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
