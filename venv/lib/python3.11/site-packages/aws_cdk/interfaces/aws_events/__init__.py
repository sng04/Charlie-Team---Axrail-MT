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
    jsii_type="aws-cdk-lib.interfaces.aws_events.ApiDestinationReference",
    jsii_struct_bases=[],
    name_mapping={
        "api_destination_arn": "apiDestinationArn",
        "api_destination_name": "apiDestinationName",
    },
)
class ApiDestinationReference:
    def __init__(
        self,
        *,
        api_destination_arn: builtins.str,
        api_destination_name: builtins.str,
    ) -> None:
        '''A reference to a ApiDestination resource.

        :param api_destination_arn: The ARN of the ApiDestination resource.
        :param api_destination_name: The Name of the ApiDestination resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_events as interfaces_events
            
            api_destination_reference = interfaces_events.ApiDestinationReference(
                api_destination_arn="apiDestinationArn",
                api_destination_name="apiDestinationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f26c7cdb281c7a4d8f2e2edcba95c8017e1c1368708cc0ebb78edda3fb6b4cb)
            check_type(argname="argument api_destination_arn", value=api_destination_arn, expected_type=type_hints["api_destination_arn"])
            check_type(argname="argument api_destination_name", value=api_destination_name, expected_type=type_hints["api_destination_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_destination_arn": api_destination_arn,
            "api_destination_name": api_destination_name,
        }

    @builtins.property
    def api_destination_arn(self) -> builtins.str:
        '''The ARN of the ApiDestination resource.'''
        result = self._values.get("api_destination_arn")
        assert result is not None, "Required property 'api_destination_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_destination_name(self) -> builtins.str:
        '''The Name of the ApiDestination resource.'''
        result = self._values.get("api_destination_name")
        assert result is not None, "Required property 'api_destination_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiDestinationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_events.ArchiveReference",
    jsii_struct_bases=[],
    name_mapping={"archive_arn": "archiveArn", "archive_name": "archiveName"},
)
class ArchiveReference:
    def __init__(
        self,
        *,
        archive_arn: builtins.str,
        archive_name: builtins.str,
    ) -> None:
        '''A reference to a Archive resource.

        :param archive_arn: The ARN of the Archive resource.
        :param archive_name: The ArchiveName of the Archive resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_events as interfaces_events
            
            archive_reference = interfaces_events.ArchiveReference(
                archive_arn="archiveArn",
                archive_name="archiveName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41aa45e37c07a2d77eebba7d90fa917289b2431e09a1a0661efa073986b05a68)
            check_type(argname="argument archive_arn", value=archive_arn, expected_type=type_hints["archive_arn"])
            check_type(argname="argument archive_name", value=archive_name, expected_type=type_hints["archive_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "archive_arn": archive_arn,
            "archive_name": archive_name,
        }

    @builtins.property
    def archive_arn(self) -> builtins.str:
        '''The ARN of the Archive resource.'''
        result = self._values.get("archive_arn")
        assert result is not None, "Required property 'archive_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def archive_name(self) -> builtins.str:
        '''The ArchiveName of the Archive resource.'''
        result = self._values.get("archive_name")
        assert result is not None, "Required property 'archive_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArchiveReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_events.ConnectionReference",
    jsii_struct_bases=[],
    name_mapping={
        "connection_arn": "connectionArn",
        "connection_name": "connectionName",
    },
)
class ConnectionReference:
    def __init__(
        self,
        *,
        connection_arn: builtins.str,
        connection_name: builtins.str,
    ) -> None:
        '''A reference to a Connection resource.

        :param connection_arn: The ARN of the Connection resource.
        :param connection_name: The Name of the Connection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_events as interfaces_events
            
            connection_reference = interfaces_events.ConnectionReference(
                connection_arn="connectionArn",
                connection_name="connectionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d912a3e12771f4cdf7baef158002185ac2864d352507287ad7a587729a2a0a94)
            check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_arn": connection_arn,
            "connection_name": connection_name,
        }

    @builtins.property
    def connection_arn(self) -> builtins.str:
        '''The ARN of the Connection resource.'''
        result = self._values.get("connection_arn")
        assert result is not None, "Required property 'connection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''The Name of the Connection resource.'''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_events.EndpointReference",
    jsii_struct_bases=[],
    name_mapping={"endpoint_arn": "endpointArn", "endpoint_name": "endpointName"},
)
class EndpointReference:
    def __init__(
        self,
        *,
        endpoint_arn: builtins.str,
        endpoint_name: builtins.str,
    ) -> None:
        '''A reference to a Endpoint resource.

        :param endpoint_arn: The ARN of the Endpoint resource.
        :param endpoint_name: The Name of the Endpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_events as interfaces_events
            
            endpoint_reference = interfaces_events.EndpointReference(
                endpoint_arn="endpointArn",
                endpoint_name="endpointName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bcf7d22d800cd806c4c35f066953b153bf55e1c241ad56890916edefde3a9093)
            check_type(argname="argument endpoint_arn", value=endpoint_arn, expected_type=type_hints["endpoint_arn"])
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_arn": endpoint_arn,
            "endpoint_name": endpoint_name,
        }

    @builtins.property
    def endpoint_arn(self) -> builtins.str:
        '''The ARN of the Endpoint resource.'''
        result = self._values.get("endpoint_arn")
        assert result is not None, "Required property 'endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_name(self) -> builtins.str:
        '''The Name of the Endpoint resource.'''
        result = self._values.get("endpoint_name")
        assert result is not None, "Required property 'endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_events.EventBusPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"event_bus_name": "eventBusName", "statement_id": "statementId"},
)
class EventBusPolicyReference:
    def __init__(
        self,
        *,
        event_bus_name: builtins.str,
        statement_id: builtins.str,
    ) -> None:
        '''A reference to a EventBusPolicy resource.

        :param event_bus_name: The EventBusName of the EventBusPolicy resource.
        :param statement_id: The StatementId of the EventBusPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_events as interfaces_events
            
            event_bus_policy_reference = interfaces_events.EventBusPolicyReference(
                event_bus_name="eventBusName",
                statement_id="statementId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5409376ea1ad25a99a1d62154cb54f8b13568799e34febf3939de66c4ab0a845)
            check_type(argname="argument event_bus_name", value=event_bus_name, expected_type=type_hints["event_bus_name"])
            check_type(argname="argument statement_id", value=statement_id, expected_type=type_hints["statement_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_bus_name": event_bus_name,
            "statement_id": statement_id,
        }

    @builtins.property
    def event_bus_name(self) -> builtins.str:
        '''The EventBusName of the EventBusPolicy resource.'''
        result = self._values.get("event_bus_name")
        assert result is not None, "Required property 'event_bus_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statement_id(self) -> builtins.str:
        '''The StatementId of the EventBusPolicy resource.'''
        result = self._values.get("statement_id")
        assert result is not None, "Required property 'statement_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventBusPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_events.EventBusReference",
    jsii_struct_bases=[],
    name_mapping={"event_bus_arn": "eventBusArn", "event_bus_name": "eventBusName"},
)
class EventBusReference:
    def __init__(
        self,
        *,
        event_bus_arn: builtins.str,
        event_bus_name: builtins.str,
    ) -> None:
        '''A reference to a EventBus resource.

        :param event_bus_arn: The ARN of the EventBus resource.
        :param event_bus_name: The Name of the EventBus resource.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_events as events
            from aws_cdk.aws_apigatewayv2_integrations import HttpEventBridgeIntegration
            
            # bus: events.IEventBus
            # http_api: apigwv2.HttpApi
            
            
            # default integration (PutEvents)
            http_api.add_routes(
                path="/default",
                methods=[apigwv2.HttpMethod.POST],
                integration=HttpEventBridgeIntegration("DefaultEventBridgeIntegration",
                    event_bus_ref=bus.event_bus_ref
                )
            )
            
            # explicit subtype
            http_api.add_routes(
                path="/put-events",
                methods=[apigwv2.HttpMethod.POST],
                integration=HttpEventBridgeIntegration("ExplicitSubtypeIntegration",
                    event_bus_ref=bus.event_bus_ref,
                    subtype=apigwv2.HttpIntegrationSubtype.EVENTBRIDGE_PUT_EVENTS
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd8cecdb7b30bd92322708fc33fdc2ad7fb6dea8f6e926855954f0f1a79d6537)
            check_type(argname="argument event_bus_arn", value=event_bus_arn, expected_type=type_hints["event_bus_arn"])
            check_type(argname="argument event_bus_name", value=event_bus_name, expected_type=type_hints["event_bus_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_bus_arn": event_bus_arn,
            "event_bus_name": event_bus_name,
        }

    @builtins.property
    def event_bus_arn(self) -> builtins.str:
        '''The ARN of the EventBus resource.'''
        result = self._values.get("event_bus_arn")
        assert result is not None, "Required property 'event_bus_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_bus_name(self) -> builtins.str:
        '''The Name of the EventBus resource.'''
        result = self._values.get("event_bus_name")
        assert result is not None, "Required property 'event_bus_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventBusReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_events.IApiDestinationRef")
class IApiDestinationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApiDestination.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="apiDestinationRef")
    def api_destination_ref(self) -> "ApiDestinationReference":
        '''(experimental) A reference to a ApiDestination resource.

        :stability: experimental
        '''
        ...


class _IApiDestinationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApiDestination.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_events.IApiDestinationRef"

    @builtins.property
    @jsii.member(jsii_name="apiDestinationRef")
    def api_destination_ref(self) -> "ApiDestinationReference":
        '''(experimental) A reference to a ApiDestination resource.

        :stability: experimental
        '''
        return typing.cast("ApiDestinationReference", jsii.get(self, "apiDestinationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApiDestinationRef).__jsii_proxy_class__ = lambda : _IApiDestinationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_events.IArchiveRef")
class IArchiveRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Archive.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="archiveRef")
    def archive_ref(self) -> "ArchiveReference":
        '''(experimental) A reference to a Archive resource.

        :stability: experimental
        '''
        ...


class _IArchiveRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Archive.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_events.IArchiveRef"

    @builtins.property
    @jsii.member(jsii_name="archiveRef")
    def archive_ref(self) -> "ArchiveReference":
        '''(experimental) A reference to a Archive resource.

        :stability: experimental
        '''
        return typing.cast("ArchiveReference", jsii.get(self, "archiveRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IArchiveRef).__jsii_proxy_class__ = lambda : _IArchiveRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_events.IConnectionRef")
class IConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        ...


class _IConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Connection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_events.IConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionReference", jsii.get(self, "connectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionRef).__jsii_proxy_class__ = lambda : _IConnectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_events.IEndpointRef")
class IEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Endpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "EndpointReference":
        '''(experimental) A reference to a Endpoint resource.

        :stability: experimental
        '''
        ...


class _IEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Endpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_events.IEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "EndpointReference":
        '''(experimental) A reference to a Endpoint resource.

        :stability: experimental
        '''
        return typing.cast("EndpointReference", jsii.get(self, "endpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEndpointRef).__jsii_proxy_class__ = lambda : _IEndpointRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_events.IEventBusPolicyRef")
class IEventBusPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventBusPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventBusPolicyRef")
    def event_bus_policy_ref(self) -> "EventBusPolicyReference":
        '''(experimental) A reference to a EventBusPolicy resource.

        :stability: experimental
        '''
        ...


class _IEventBusPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventBusPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_events.IEventBusPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="eventBusPolicyRef")
    def event_bus_policy_ref(self) -> "EventBusPolicyReference":
        '''(experimental) A reference to a EventBusPolicy resource.

        :stability: experimental
        '''
        return typing.cast("EventBusPolicyReference", jsii.get(self, "eventBusPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventBusPolicyRef).__jsii_proxy_class__ = lambda : _IEventBusPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_events.IEventBusRef")
class IEventBusRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventBus.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventBusRef")
    def event_bus_ref(self) -> "EventBusReference":
        '''(experimental) A reference to a EventBus resource.

        :stability: experimental
        '''
        ...


class _IEventBusRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventBus.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_events.IEventBusRef"

    @builtins.property
    @jsii.member(jsii_name="eventBusRef")
    def event_bus_ref(self) -> "EventBusReference":
        '''(experimental) A reference to a EventBus resource.

        :stability: experimental
        '''
        return typing.cast("EventBusReference", jsii.get(self, "eventBusRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventBusRef).__jsii_proxy_class__ = lambda : _IEventBusRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_events.IRuleRef")
class IRuleRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Rule.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="ruleRef")
    def rule_ref(self) -> "RuleReference":
        '''(experimental) A reference to a Rule resource.

        :stability: experimental
        '''
        ...


class _IRuleRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Rule.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_events.IRuleRef"

    @builtins.property
    @jsii.member(jsii_name="ruleRef")
    def rule_ref(self) -> "RuleReference":
        '''(experimental) A reference to a Rule resource.

        :stability: experimental
        '''
        return typing.cast("RuleReference", jsii.get(self, "ruleRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRuleRef).__jsii_proxy_class__ = lambda : _IRuleRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_events.RuleReference",
    jsii_struct_bases=[],
    name_mapping={"rule_arn": "ruleArn"},
)
class RuleReference:
    def __init__(self, *, rule_arn: builtins.str) -> None:
        '''A reference to a Rule resource.

        :param rule_arn: The Arn of the Rule resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_events as interfaces_events
            
            rule_reference = interfaces_events.RuleReference(
                rule_arn="ruleArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1386bff26a0e1756dfc8c5d9caea262c08aaf98d9b423f3afa7d30103b554c2b)
            check_type(argname="argument rule_arn", value=rule_arn, expected_type=type_hints["rule_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_arn": rule_arn,
        }

    @builtins.property
    def rule_arn(self) -> builtins.str:
        '''The Arn of the Rule resource.'''
        result = self._values.get("rule_arn")
        assert result is not None, "Required property 'rule_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RuleReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApiDestinationReference",
    "ArchiveReference",
    "ConnectionReference",
    "EndpointReference",
    "EventBusPolicyReference",
    "EventBusReference",
    "IApiDestinationRef",
    "IArchiveRef",
    "IConnectionRef",
    "IEndpointRef",
    "IEventBusPolicyRef",
    "IEventBusRef",
    "IRuleRef",
    "RuleReference",
]

publication.publish()

def _typecheckingstub__8f26c7cdb281c7a4d8f2e2edcba95c8017e1c1368708cc0ebb78edda3fb6b4cb(
    *,
    api_destination_arn: builtins.str,
    api_destination_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41aa45e37c07a2d77eebba7d90fa917289b2431e09a1a0661efa073986b05a68(
    *,
    archive_arn: builtins.str,
    archive_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d912a3e12771f4cdf7baef158002185ac2864d352507287ad7a587729a2a0a94(
    *,
    connection_arn: builtins.str,
    connection_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcf7d22d800cd806c4c35f066953b153bf55e1c241ad56890916edefde3a9093(
    *,
    endpoint_arn: builtins.str,
    endpoint_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5409376ea1ad25a99a1d62154cb54f8b13568799e34febf3939de66c4ab0a845(
    *,
    event_bus_name: builtins.str,
    statement_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8cecdb7b30bd92322708fc33fdc2ad7fb6dea8f6e926855954f0f1a79d6537(
    *,
    event_bus_arn: builtins.str,
    event_bus_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1386bff26a0e1756dfc8c5d9caea262c08aaf98d9b423f3afa7d30103b554c2b(
    *,
    rule_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApiDestinationRef, IArchiveRef, IConnectionRef, IEndpointRef, IEventBusPolicyRef, IEventBusRef, IRuleRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
