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
    jsii_type="aws-cdk-lib.interfaces.aws_appintegrations.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_arn": "applicationArn"},
)
class ApplicationReference:
    def __init__(self, *, application_arn: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_arn: The ApplicationArn of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appintegrations as interfaces_appintegrations
            
            application_reference = interfaces_appintegrations.ApplicationReference(
                application_arn="applicationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__930faccfa5d23173be51a6ba0efbc5aea4717a3732fc1180e7b0b8cceefa375f)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ApplicationArn of the Application resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_appintegrations.DataIntegrationReference",
    jsii_struct_bases=[],
    name_mapping={
        "data_integration_arn": "dataIntegrationArn",
        "data_integration_id": "dataIntegrationId",
    },
)
class DataIntegrationReference:
    def __init__(
        self,
        *,
        data_integration_arn: builtins.str,
        data_integration_id: builtins.str,
    ) -> None:
        '''A reference to a DataIntegration resource.

        :param data_integration_arn: The ARN of the DataIntegration resource.
        :param data_integration_id: The Id of the DataIntegration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appintegrations as interfaces_appintegrations
            
            data_integration_reference = interfaces_appintegrations.DataIntegrationReference(
                data_integration_arn="dataIntegrationArn",
                data_integration_id="dataIntegrationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80f4cd0f27bbfb91de742779697a9290c43788351f371e534aa41a652e3b7e84)
            check_type(argname="argument data_integration_arn", value=data_integration_arn, expected_type=type_hints["data_integration_arn"])
            check_type(argname="argument data_integration_id", value=data_integration_id, expected_type=type_hints["data_integration_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_integration_arn": data_integration_arn,
            "data_integration_id": data_integration_id,
        }

    @builtins.property
    def data_integration_arn(self) -> builtins.str:
        '''The ARN of the DataIntegration resource.'''
        result = self._values.get("data_integration_arn")
        assert result is not None, "Required property 'data_integration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_integration_id(self) -> builtins.str:
        '''The Id of the DataIntegration resource.'''
        result = self._values.get("data_integration_id")
        assert result is not None, "Required property 'data_integration_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataIntegrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_appintegrations.EventIntegrationReference",
    jsii_struct_bases=[],
    name_mapping={
        "event_integration_arn": "eventIntegrationArn",
        "event_integration_name": "eventIntegrationName",
    },
)
class EventIntegrationReference:
    def __init__(
        self,
        *,
        event_integration_arn: builtins.str,
        event_integration_name: builtins.str,
    ) -> None:
        '''A reference to a EventIntegration resource.

        :param event_integration_arn: The ARN of the EventIntegration resource.
        :param event_integration_name: The Name of the EventIntegration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_appintegrations as interfaces_appintegrations
            
            event_integration_reference = interfaces_appintegrations.EventIntegrationReference(
                event_integration_arn="eventIntegrationArn",
                event_integration_name="eventIntegrationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7607f7cbad87b5f7201deb380119731f021ae4b9505810b9bbf606184e1dfb7)
            check_type(argname="argument event_integration_arn", value=event_integration_arn, expected_type=type_hints["event_integration_arn"])
            check_type(argname="argument event_integration_name", value=event_integration_name, expected_type=type_hints["event_integration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "event_integration_arn": event_integration_arn,
            "event_integration_name": event_integration_name,
        }

    @builtins.property
    def event_integration_arn(self) -> builtins.str:
        '''The ARN of the EventIntegration resource.'''
        result = self._values.get("event_integration_arn")
        assert result is not None, "Required property 'event_integration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_integration_name(self) -> builtins.str:
        '''The Name of the EventIntegration resource.'''
        result = self._values.get("event_integration_name")
        assert result is not None, "Required property 'event_integration_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EventIntegrationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_appintegrations.IApplicationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appintegrations.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appintegrations.IDataIntegrationRef"
)
class IDataIntegrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataIntegration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataIntegrationRef")
    def data_integration_ref(self) -> "DataIntegrationReference":
        '''(experimental) A reference to a DataIntegration resource.

        :stability: experimental
        '''
        ...


class _IDataIntegrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataIntegration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appintegrations.IDataIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="dataIntegrationRef")
    def data_integration_ref(self) -> "DataIntegrationReference":
        '''(experimental) A reference to a DataIntegration resource.

        :stability: experimental
        '''
        return typing.cast("DataIntegrationReference", jsii.get(self, "dataIntegrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataIntegrationRef).__jsii_proxy_class__ = lambda : _IDataIntegrationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_appintegrations.IEventIntegrationRef"
)
class IEventIntegrationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a EventIntegration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="eventIntegrationRef")
    def event_integration_ref(self) -> "EventIntegrationReference":
        '''(experimental) A reference to a EventIntegration resource.

        :stability: experimental
        '''
        ...


class _IEventIntegrationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a EventIntegration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_appintegrations.IEventIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="eventIntegrationRef")
    def event_integration_ref(self) -> "EventIntegrationReference":
        '''(experimental) A reference to a EventIntegration resource.

        :stability: experimental
        '''
        return typing.cast("EventIntegrationReference", jsii.get(self, "eventIntegrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEventIntegrationRef).__jsii_proxy_class__ = lambda : _IEventIntegrationRefProxy


__all__ = [
    "ApplicationReference",
    "DataIntegrationReference",
    "EventIntegrationReference",
    "IApplicationRef",
    "IDataIntegrationRef",
    "IEventIntegrationRef",
]

publication.publish()

def _typecheckingstub__930faccfa5d23173be51a6ba0efbc5aea4717a3732fc1180e7b0b8cceefa375f(
    *,
    application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80f4cd0f27bbfb91de742779697a9290c43788351f371e534aa41a652e3b7e84(
    *,
    data_integration_arn: builtins.str,
    data_integration_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7607f7cbad87b5f7201deb380119731f021ae4b9505810b9bbf606184e1dfb7(
    *,
    event_integration_arn: builtins.str,
    event_integration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef, IDataIntegrationRef, IEventIntegrationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
