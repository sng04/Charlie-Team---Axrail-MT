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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.ApplicationCloudWatchLoggingOptionReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_cloud_watch_logging_option_id": "applicationCloudWatchLoggingOptionId",
    },
)
class ApplicationCloudWatchLoggingOptionReference:
    def __init__(
        self,
        *,
        application_cloud_watch_logging_option_id: builtins.str,
    ) -> None:
        '''A reference to a ApplicationCloudWatchLoggingOption resource.

        :param application_cloud_watch_logging_option_id: The Id of the ApplicationCloudWatchLoggingOption resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kinesisanalyticsv2 as interfaces_kinesisanalyticsv2
            
            application_cloud_watch_logging_option_reference = interfaces_kinesisanalyticsv2.ApplicationCloudWatchLoggingOptionReference(
                application_cloud_watch_logging_option_id="applicationCloudWatchLoggingOptionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f8a246b267dcf66927f7d28716d327ef1bcdb2934e5fc953d206a2e899b8630)
            check_type(argname="argument application_cloud_watch_logging_option_id", value=application_cloud_watch_logging_option_id, expected_type=type_hints["application_cloud_watch_logging_option_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_cloud_watch_logging_option_id": application_cloud_watch_logging_option_id,
        }

    @builtins.property
    def application_cloud_watch_logging_option_id(self) -> builtins.str:
        '''The Id of the ApplicationCloudWatchLoggingOption resource.'''
        result = self._values.get("application_cloud_watch_logging_option_id")
        assert result is not None, "Required property 'application_cloud_watch_logging_option_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationCloudWatchLoggingOptionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.ApplicationOutputReference",
    jsii_struct_bases=[],
    name_mapping={"application_output_id": "applicationOutputId"},
)
class ApplicationOutputReference:
    def __init__(self, *, application_output_id: builtins.str) -> None:
        '''A reference to a ApplicationOutput resource.

        :param application_output_id: The Id of the ApplicationOutput resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kinesisanalyticsv2 as interfaces_kinesisanalyticsv2
            
            application_output_reference = interfaces_kinesisanalyticsv2.ApplicationOutputReference(
                application_output_id="applicationOutputId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afa3fb6015fc0c5ec88161bcc061bd360450dd475c18e6d3cf70cc24841b13b6)
            check_type(argname="argument application_output_id", value=application_output_id, expected_type=type_hints["application_output_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_output_id": application_output_id,
        }

    @builtins.property
    def application_output_id(self) -> builtins.str:
        '''The Id of the ApplicationOutput resource.'''
        result = self._values.get("application_output_id")
        assert result is not None, "Required property 'application_output_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationOutputReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_name": "applicationName"},
)
class ApplicationReference:
    def __init__(self, *, application_name: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_name: The ApplicationName of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kinesisanalyticsv2 as interfaces_kinesisanalyticsv2
            
            application_reference = interfaces_kinesisanalyticsv2.ApplicationReference(
                application_name="applicationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08bf72e70c6818b577a9f599411c03a33aced8681df05639b0b6cb4d32506f63)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
        }

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The ApplicationName of the Application resource.'''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.ApplicationReferenceDataSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_reference_data_source_id": "applicationReferenceDataSourceId",
    },
)
class ApplicationReferenceDataSourceReference:
    def __init__(self, *, application_reference_data_source_id: builtins.str) -> None:
        '''A reference to a ApplicationReferenceDataSource resource.

        :param application_reference_data_source_id: The Id of the ApplicationReferenceDataSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kinesisanalyticsv2 as interfaces_kinesisanalyticsv2
            
            application_reference_data_source_reference = interfaces_kinesisanalyticsv2.ApplicationReferenceDataSourceReference(
                application_reference_data_source_id="applicationReferenceDataSourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cca7193af9dd0db26b3420ccc8595e5ecfa0e043f75a4357ece05bd4a135a78c)
            check_type(argname="argument application_reference_data_source_id", value=application_reference_data_source_id, expected_type=type_hints["application_reference_data_source_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_reference_data_source_id": application_reference_data_source_id,
        }

    @builtins.property
    def application_reference_data_source_id(self) -> builtins.str:
        '''The Id of the ApplicationReferenceDataSource resource.'''
        result = self._values.get("application_reference_data_source_id")
        assert result is not None, "Required property 'application_reference_data_source_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationReferenceDataSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.IApplicationCloudWatchLoggingOptionRef"
)
class IApplicationCloudWatchLoggingOptionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationCloudWatchLoggingOption.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationCloudWatchLoggingOptionRef")
    def application_cloud_watch_logging_option_ref(
        self,
    ) -> "ApplicationCloudWatchLoggingOptionReference":
        '''(experimental) A reference to a ApplicationCloudWatchLoggingOption resource.

        :stability: experimental
        '''
        ...


class _IApplicationCloudWatchLoggingOptionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationCloudWatchLoggingOption.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.IApplicationCloudWatchLoggingOptionRef"

    @builtins.property
    @jsii.member(jsii_name="applicationCloudWatchLoggingOptionRef")
    def application_cloud_watch_logging_option_ref(
        self,
    ) -> "ApplicationCloudWatchLoggingOptionReference":
        '''(experimental) A reference to a ApplicationCloudWatchLoggingOption resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationCloudWatchLoggingOptionReference", jsii.get(self, "applicationCloudWatchLoggingOptionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationCloudWatchLoggingOptionRef).__jsii_proxy_class__ = lambda : _IApplicationCloudWatchLoggingOptionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.IApplicationOutputRef"
)
class IApplicationOutputRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationOutput.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationOutputRef")
    def application_output_ref(self) -> "ApplicationOutputReference":
        '''(experimental) A reference to a ApplicationOutput resource.

        :stability: experimental
        '''
        ...


class _IApplicationOutputRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationOutput.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.IApplicationOutputRef"

    @builtins.property
    @jsii.member(jsii_name="applicationOutputRef")
    def application_output_ref(self) -> "ApplicationOutputReference":
        '''(experimental) A reference to a ApplicationOutput resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationOutputReference", jsii.get(self, "applicationOutputRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationOutputRef).__jsii_proxy_class__ = lambda : _IApplicationOutputRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.IApplicationRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.IApplicationRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.IApplicationReferenceDataSourceRef"
)
class IApplicationReferenceDataSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationReferenceDataSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationReferenceDataSourceRef")
    def application_reference_data_source_ref(
        self,
    ) -> "ApplicationReferenceDataSourceReference":
        '''(experimental) A reference to a ApplicationReferenceDataSource resource.

        :stability: experimental
        '''
        ...


class _IApplicationReferenceDataSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ApplicationReferenceDataSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesisanalyticsv2.IApplicationReferenceDataSourceRef"

    @builtins.property
    @jsii.member(jsii_name="applicationReferenceDataSourceRef")
    def application_reference_data_source_ref(
        self,
    ) -> "ApplicationReferenceDataSourceReference":
        '''(experimental) A reference to a ApplicationReferenceDataSource resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReferenceDataSourceReference", jsii.get(self, "applicationReferenceDataSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationReferenceDataSourceRef).__jsii_proxy_class__ = lambda : _IApplicationReferenceDataSourceRefProxy


__all__ = [
    "ApplicationCloudWatchLoggingOptionReference",
    "ApplicationOutputReference",
    "ApplicationReference",
    "ApplicationReferenceDataSourceReference",
    "IApplicationCloudWatchLoggingOptionRef",
    "IApplicationOutputRef",
    "IApplicationRef",
    "IApplicationReferenceDataSourceRef",
]

publication.publish()

def _typecheckingstub__2f8a246b267dcf66927f7d28716d327ef1bcdb2934e5fc953d206a2e899b8630(
    *,
    application_cloud_watch_logging_option_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa3fb6015fc0c5ec88161bcc061bd360450dd475c18e6d3cf70cc24841b13b6(
    *,
    application_output_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08bf72e70c6818b577a9f599411c03a33aced8681df05639b0b6cb4d32506f63(
    *,
    application_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cca7193af9dd0db26b3420ccc8595e5ecfa0e043f75a4357ece05bd4a135a78c(
    *,
    application_reference_data_source_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationCloudWatchLoggingOptionRef, IApplicationOutputRef, IApplicationRef, IApplicationReferenceDataSourceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
