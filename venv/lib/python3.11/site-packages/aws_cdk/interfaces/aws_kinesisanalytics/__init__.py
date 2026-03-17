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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalytics.ApplicationOutputReference",
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
            from aws_cdk.interfaces import aws_kinesisanalytics as interfaces_kinesisanalytics
            
            application_output_reference = interfaces_kinesisanalytics.ApplicationOutputReference(
                application_output_id="applicationOutputId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a664c4dd1f9ddde17b27380c5fb66dda30900134285e96f427e90d7bbd3d63d)
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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalytics.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={"application_id": "applicationId"},
)
class ApplicationReference:
    def __init__(self, *, application_id: builtins.str) -> None:
        '''A reference to a Application resource.

        :param application_id: The Id of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_kinesisanalytics as interfaces_kinesisanalytics
            
            application_reference = interfaces_kinesisanalytics.ApplicationReference(
                application_id="applicationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c4aada0ae4a6c13476a706a7151e195d2ca2780cdb28a7dc17eb6b7e066655)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The Id of the Application resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalytics.ApplicationReferenceDataSourceReference",
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
            from aws_cdk.interfaces import aws_kinesisanalytics as interfaces_kinesisanalytics
            
            application_reference_data_source_reference = interfaces_kinesisanalytics.ApplicationReferenceDataSourceReference(
                application_reference_data_source_id="applicationReferenceDataSourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__930d7611d413e07f4c68a96fbb8ede654a69a67c50a29b4a83b8f8d3098a85a9)
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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalytics.IApplicationOutputRef"
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesisanalytics.IApplicationOutputRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalytics.IApplicationRef"
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesisanalytics.IApplicationRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_kinesisanalytics.IApplicationReferenceDataSourceRef"
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_kinesisanalytics.IApplicationReferenceDataSourceRef"

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
    "ApplicationOutputReference",
    "ApplicationReference",
    "ApplicationReferenceDataSourceReference",
    "IApplicationOutputRef",
    "IApplicationRef",
    "IApplicationReferenceDataSourceRef",
]

publication.publish()

def _typecheckingstub__8a664c4dd1f9ddde17b27380c5fb66dda30900134285e96f427e90d7bbd3d63d(
    *,
    application_output_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c4aada0ae4a6c13476a706a7151e195d2ca2780cdb28a7dc17eb6b7e066655(
    *,
    application_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__930d7611d413e07f4c68a96fbb8ede654a69a67c50a29b4a83b8f8d3098a85a9(
    *,
    application_reference_data_source_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationOutputRef, IApplicationRef, IApplicationReferenceDataSourceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
