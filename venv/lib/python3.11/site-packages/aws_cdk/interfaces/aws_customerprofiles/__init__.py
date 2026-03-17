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
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.CalculatedAttributeDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "calculated_attribute_name": "calculatedAttributeName",
        "domain_name": "domainName",
    },
)
class CalculatedAttributeDefinitionReference:
    def __init__(
        self,
        *,
        calculated_attribute_name: builtins.str,
        domain_name: builtins.str,
    ) -> None:
        '''A reference to a CalculatedAttributeDefinition resource.

        :param calculated_attribute_name: The CalculatedAttributeName of the CalculatedAttributeDefinition resource.
        :param domain_name: The DomainName of the CalculatedAttributeDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_customerprofiles as interfaces_customerprofiles
            
            calculated_attribute_definition_reference = interfaces_customerprofiles.CalculatedAttributeDefinitionReference(
                calculated_attribute_name="calculatedAttributeName",
                domain_name="domainName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69c9f928479930b4b44080f25dd85b476623eec3824c328993708294648462b1)
            check_type(argname="argument calculated_attribute_name", value=calculated_attribute_name, expected_type=type_hints["calculated_attribute_name"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "calculated_attribute_name": calculated_attribute_name,
            "domain_name": domain_name,
        }

    @builtins.property
    def calculated_attribute_name(self) -> builtins.str:
        '''The CalculatedAttributeName of the CalculatedAttributeDefinition resource.'''
        result = self._values.get("calculated_attribute_name")
        assert result is not None, "Required property 'calculated_attribute_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the CalculatedAttributeDefinition resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CalculatedAttributeDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.DomainReference",
    jsii_struct_bases=[],
    name_mapping={"domain_name": "domainName"},
)
class DomainReference:
    def __init__(self, *, domain_name: builtins.str) -> None:
        '''A reference to a Domain resource.

        :param domain_name: The DomainName of the Domain resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_customerprofiles as interfaces_customerprofiles
            
            domain_reference = interfaces_customerprofiles.DomainReference(
                domain_name="domainName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__085431f7ef067509a28b7dcfd8d0009bde06b147b2e50777fc5636a355898a85)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the Domain resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DomainReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.EventStreamReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "event_stream_arn": "eventStreamArn",
        "event_stream_name": "eventStreamName",
    },
)
class EventStreamReference:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        event_stream_arn: builtins.str,
        event_stream_name: builtins.str,
    ) -> None:
        '''A reference to a EventStream resource.

        :param domain_name: The DomainName of the EventStream resource.
        :param event_stream_arn: The ARN of the EventStream resource.
        :param event_stream_name: The EventStreamName of the EventStream resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_customerprofiles as interfaces_customerprofiles
            
            event_stream_reference = interfaces_customerprofiles.EventStreamReference(
                domain_name="domainName",
                event_stream_arn="eventStreamArn",
                event_stream_name="eventStreamName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f85d0947924869d1226fd3a731b5037d6538589e1a7a8c514366dc5156e00a23)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument event_stream_arn", value=event_stream_arn, expected_type=type_hints["event_stream_arn"])
            check_type(argname="argument event_stream_name", value=event_stream_name, expected_type=type_hints["event_stream_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "event_stream_arn": event_stream_arn,
            "event_stream_name": event_stream_name,
        }

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the EventStream resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_stream_arn(self) -> builtins.str:
        '''The ARN of the EventStream resource.'''
        result = self._values.get("event_stream_arn")
        assert result is not None, "Required property 'event_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_stream_name(self) -> builtins.str:
        '''The EventStreamName of the EventStream resource.'''
        result = self._values.get("event_stream_name")
        assert result is not None, "Required property 'event_stream_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventStreamReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.EventTriggerReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "event_trigger_name": "eventTriggerName",
    },
)
class EventTriggerReference:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        event_trigger_name: builtins.str,
    ) -> None:
        '''A reference to a EventTrigger resource.

        :param domain_name: The DomainName of the EventTrigger resource.
        :param event_trigger_name: The EventTriggerName of the EventTrigger resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_customerprofiles as interfaces_customerprofiles
            
            event_trigger_reference = interfaces_customerprofiles.EventTriggerReference(
                domain_name="domainName",
                event_trigger_name="eventTriggerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84611b6f2bbd585ebcc9429b7fcf0cc74a8710c38b133dc685a584140c6db520)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument event_trigger_name", value=event_trigger_name, expected_type=type_hints["event_trigger_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "event_trigger_name": event_trigger_name,
        }

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the EventTrigger resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_trigger_name(self) -> builtins.str:
        '''The EventTriggerName of the EventTrigger resource.'''
        result = self._values.get("event_trigger_name")
        assert result is not None, "Required property 'event_trigger_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventTriggerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.ICalculatedAttributeDefinitionRef"
)
class ICalculatedAttributeDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CalculatedAttributeDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="calculatedAttributeDefinitionRef")
    def calculated_attribute_definition_ref(
        self,
    ) -> "CalculatedAttributeDefinitionReference":
        '''(experimental) A reference to a CalculatedAttributeDefinition resource.

        :stability: experimental
        '''
        ...


class _ICalculatedAttributeDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CalculatedAttributeDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_customerprofiles.ICalculatedAttributeDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="calculatedAttributeDefinitionRef")
    def calculated_attribute_definition_ref(
        self,
    ) -> "CalculatedAttributeDefinitionReference":
        '''(experimental) A reference to a CalculatedAttributeDefinition resource.

        :stability: experimental
        '''
        return typing.cast("CalculatedAttributeDefinitionReference", jsii.get(self, "calculatedAttributeDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICalculatedAttributeDefinitionRef).__jsii_proxy_class__ = lambda : _ICalculatedAttributeDefinitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.IDomainRef")
class IDomainRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Domain.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        ...


class _IDomainRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Domain.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_customerprofiles.IDomainRef"

    @builtins.property
    @jsii.member(jsii_name="domainRef")
    def domain_ref(self) -> "DomainReference":
        '''(experimental) A reference to a Domain resource.

        :stability: experimental
        '''
        return typing.cast("DomainReference", jsii.get(self, "domainRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDomainRef).__jsii_proxy_class__ = lambda : _IDomainRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.IEventStreamRef"
)
class IEventStreamRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventStream.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventStreamRef")
    def event_stream_ref(self) -> "EventStreamReference":
        '''(experimental) A reference to a EventStream resource.

        :stability: experimental
        '''
        ...


class _IEventStreamRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventStream.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_customerprofiles.IEventStreamRef"

    @builtins.property
    @jsii.member(jsii_name="eventStreamRef")
    def event_stream_ref(self) -> "EventStreamReference":
        '''(experimental) A reference to a EventStream resource.

        :stability: experimental
        '''
        return typing.cast("EventStreamReference", jsii.get(self, "eventStreamRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventStreamRef).__jsii_proxy_class__ = lambda : _IEventStreamRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.IEventTriggerRef"
)
class IEventTriggerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventTrigger.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventTriggerRef")
    def event_trigger_ref(self) -> "EventTriggerReference":
        '''(experimental) A reference to a EventTrigger resource.

        :stability: experimental
        '''
        ...


class _IEventTriggerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventTrigger.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_customerprofiles.IEventTriggerRef"

    @builtins.property
    @jsii.member(jsii_name="eventTriggerRef")
    def event_trigger_ref(self) -> "EventTriggerReference":
        '''(experimental) A reference to a EventTrigger resource.

        :stability: experimental
        '''
        return typing.cast("EventTriggerReference", jsii.get(self, "eventTriggerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventTriggerRef).__jsii_proxy_class__ = lambda : _IEventTriggerRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.IIntegrationRef"
)
class IIntegrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Integration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        ...


class _IIntegrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Integration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_customerprofiles.IIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationReference", jsii.get(self, "integrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationRef).__jsii_proxy_class__ = lambda : _IIntegrationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.IObjectTypeRef")
class IObjectTypeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ObjectType.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="objectTypeRef")
    def object_type_ref(self) -> "ObjectTypeReference":
        '''(experimental) A reference to a ObjectType resource.

        :stability: experimental
        '''
        ...


class _IObjectTypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ObjectType.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_customerprofiles.IObjectTypeRef"

    @builtins.property
    @jsii.member(jsii_name="objectTypeRef")
    def object_type_ref(self) -> "ObjectTypeReference":
        '''(experimental) A reference to a ObjectType resource.

        :stability: experimental
        '''
        return typing.cast("ObjectTypeReference", jsii.get(self, "objectTypeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IObjectTypeRef).__jsii_proxy_class__ = lambda : _IObjectTypeRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.ISegmentDefinitionRef"
)
class ISegmentDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SegmentDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="segmentDefinitionRef")
    def segment_definition_ref(self) -> "SegmentDefinitionReference":
        '''(experimental) A reference to a SegmentDefinition resource.

        :stability: experimental
        '''
        ...


class _ISegmentDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SegmentDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_customerprofiles.ISegmentDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="segmentDefinitionRef")
    def segment_definition_ref(self) -> "SegmentDefinitionReference":
        '''(experimental) A reference to a SegmentDefinition resource.

        :stability: experimental
        '''
        return typing.cast("SegmentDefinitionReference", jsii.get(self, "segmentDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISegmentDefinitionRef).__jsii_proxy_class__ = lambda : _ISegmentDefinitionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.IntegrationReference",
    jsii_struct_bases=[],
    name_mapping={"domain_name": "domainName", "uri": "uri"},
)
class IntegrationReference:
    def __init__(self, *, domain_name: builtins.str, uri: builtins.str) -> None:
        '''A reference to a Integration resource.

        :param domain_name: The DomainName of the Integration resource.
        :param uri: The Uri of the Integration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_customerprofiles as interfaces_customerprofiles
            
            integration_reference = interfaces_customerprofiles.IntegrationReference(
                domain_name="domainName",
                uri="uri"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94eec83ed0b43d1237d9672aa6820fc456e2f4bf8d1743901aaa16e7d122586d)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "uri": uri,
        }

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the Integration resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def uri(self) -> builtins.str:
        '''The Uri of the Integration resource.'''
        result = self._values.get("uri")
        assert result is not None, "Required property 'uri' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.ObjectTypeReference",
    jsii_struct_bases=[],
    name_mapping={"domain_name": "domainName", "object_type_name": "objectTypeName"},
)
class ObjectTypeReference:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        object_type_name: builtins.str,
    ) -> None:
        '''A reference to a ObjectType resource.

        :param domain_name: The DomainName of the ObjectType resource.
        :param object_type_name: The ObjectTypeName of the ObjectType resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_customerprofiles as interfaces_customerprofiles
            
            object_type_reference = interfaces_customerprofiles.ObjectTypeReference(
                domain_name="domainName",
                object_type_name="objectTypeName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcdfa1e22cd22dc7400da7632968be09334b8baeadcbbfcdcedf890b2e396cf1)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument object_type_name", value=object_type_name, expected_type=type_hints["object_type_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "object_type_name": object_type_name,
        }

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the ObjectType resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def object_type_name(self) -> builtins.str:
        '''The ObjectTypeName of the ObjectType resource.'''
        result = self._values.get("object_type_name")
        assert result is not None, "Required property 'object_type_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ObjectTypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_customerprofiles.SegmentDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "segment_definition_arn": "segmentDefinitionArn",
        "segment_definition_name": "segmentDefinitionName",
    },
)
class SegmentDefinitionReference:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        segment_definition_arn: builtins.str,
        segment_definition_name: builtins.str,
    ) -> None:
        '''A reference to a SegmentDefinition resource.

        :param domain_name: The DomainName of the SegmentDefinition resource.
        :param segment_definition_arn: The ARN of the SegmentDefinition resource.
        :param segment_definition_name: The SegmentDefinitionName of the SegmentDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_customerprofiles as interfaces_customerprofiles
            
            segment_definition_reference = interfaces_customerprofiles.SegmentDefinitionReference(
                domain_name="domainName",
                segment_definition_arn="segmentDefinitionArn",
                segment_definition_name="segmentDefinitionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e30c09a37c8a79e5b1574fa33f089f6b93ba58323998bc89f415eb9d8f457d6)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument segment_definition_arn", value=segment_definition_arn, expected_type=type_hints["segment_definition_arn"])
            check_type(argname="argument segment_definition_name", value=segment_definition_name, expected_type=type_hints["segment_definition_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "segment_definition_arn": segment_definition_arn,
            "segment_definition_name": segment_definition_name,
        }

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The DomainName of the SegmentDefinition resource.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def segment_definition_arn(self) -> builtins.str:
        '''The ARN of the SegmentDefinition resource.'''
        result = self._values.get("segment_definition_arn")
        assert result is not None, "Required property 'segment_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def segment_definition_name(self) -> builtins.str:
        '''The SegmentDefinitionName of the SegmentDefinition resource.'''
        result = self._values.get("segment_definition_name")
        assert result is not None, "Required property 'segment_definition_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SegmentDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CalculatedAttributeDefinitionReference",
    "DomainReference",
    "EventStreamReference",
    "EventTriggerReference",
    "ICalculatedAttributeDefinitionRef",
    "IDomainRef",
    "IEventStreamRef",
    "IEventTriggerRef",
    "IIntegrationRef",
    "IObjectTypeRef",
    "ISegmentDefinitionRef",
    "IntegrationReference",
    "ObjectTypeReference",
    "SegmentDefinitionReference",
]

publication.publish()

def _typecheckingstub__69c9f928479930b4b44080f25dd85b476623eec3824c328993708294648462b1(
    *,
    calculated_attribute_name: builtins.str,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__085431f7ef067509a28b7dcfd8d0009bde06b147b2e50777fc5636a355898a85(
    *,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f85d0947924869d1226fd3a731b5037d6538589e1a7a8c514366dc5156e00a23(
    *,
    domain_name: builtins.str,
    event_stream_arn: builtins.str,
    event_stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84611b6f2bbd585ebcc9429b7fcf0cc74a8710c38b133dc685a584140c6db520(
    *,
    domain_name: builtins.str,
    event_trigger_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94eec83ed0b43d1237d9672aa6820fc456e2f4bf8d1743901aaa16e7d122586d(
    *,
    domain_name: builtins.str,
    uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcdfa1e22cd22dc7400da7632968be09334b8baeadcbbfcdcedf890b2e396cf1(
    *,
    domain_name: builtins.str,
    object_type_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e30c09a37c8a79e5b1574fa33f089f6b93ba58323998bc89f415eb9d8f457d6(
    *,
    domain_name: builtins.str,
    segment_definition_arn: builtins.str,
    segment_definition_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICalculatedAttributeDefinitionRef, IDomainRef, IEventStreamRef, IEventTriggerRef, IIntegrationRef, IObjectTypeRef, ISegmentDefinitionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
