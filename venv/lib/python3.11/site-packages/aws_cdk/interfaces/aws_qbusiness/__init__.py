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
    jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.ApplicationReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_arn": "applicationArn",
        "application_id": "applicationId",
    },
)
class ApplicationReference:
    def __init__(
        self,
        *,
        application_arn: builtins.str,
        application_id: builtins.str,
    ) -> None:
        '''A reference to a Application resource.

        :param application_arn: The ARN of the Application resource.
        :param application_id: The ApplicationId of the Application resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_qbusiness as interfaces_qbusiness
            
            application_reference = interfaces_qbusiness.ApplicationReference(
                application_arn="applicationArn",
                application_id="applicationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02780d7e62f54269cdd696dfde5f4e7da716acfbebae0e1f7ce853be6d52bd3d)
            check_type(argname="argument application_arn", value=application_arn, expected_type=type_hints["application_arn"])
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_arn": application_arn,
            "application_id": application_id,
        }

    @builtins.property
    def application_arn(self) -> builtins.str:
        '''The ARN of the Application resource.'''
        result = self._values.get("application_arn")
        assert result is not None, "Required property 'application_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Application resource.'''
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
    jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.DataAccessorReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "data_accessor_arn": "dataAccessorArn",
        "data_accessor_id": "dataAccessorId",
    },
)
class DataAccessorReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        data_accessor_arn: builtins.str,
        data_accessor_id: builtins.str,
    ) -> None:
        '''A reference to a DataAccessor resource.

        :param application_id: The ApplicationId of the DataAccessor resource.
        :param data_accessor_arn: The ARN of the DataAccessor resource.
        :param data_accessor_id: The DataAccessorId of the DataAccessor resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_qbusiness as interfaces_qbusiness
            
            data_accessor_reference = interfaces_qbusiness.DataAccessorReference(
                application_id="applicationId",
                data_accessor_arn="dataAccessorArn",
                data_accessor_id="dataAccessorId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__848e0be0e45da9b5e17d7c25a4df995453dab35fb28d46250adb03ae80146e37)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument data_accessor_arn", value=data_accessor_arn, expected_type=type_hints["data_accessor_arn"])
            check_type(argname="argument data_accessor_id", value=data_accessor_id, expected_type=type_hints["data_accessor_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "data_accessor_arn": data_accessor_arn,
            "data_accessor_id": data_accessor_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the DataAccessor resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_accessor_arn(self) -> builtins.str:
        '''The ARN of the DataAccessor resource.'''
        result = self._values.get("data_accessor_arn")
        assert result is not None, "Required property 'data_accessor_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_accessor_id(self) -> builtins.str:
        '''The DataAccessorId of the DataAccessor resource.'''
        result = self._values.get("data_accessor_id")
        assert result is not None, "Required property 'data_accessor_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAccessorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.DataSourceReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "data_source_arn": "dataSourceArn",
        "data_source_id": "dataSourceId",
        "index_id": "indexId",
    },
)
class DataSourceReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        data_source_arn: builtins.str,
        data_source_id: builtins.str,
        index_id: builtins.str,
    ) -> None:
        '''A reference to a DataSource resource.

        :param application_id: The ApplicationId of the DataSource resource.
        :param data_source_arn: The ARN of the DataSource resource.
        :param data_source_id: The DataSourceId of the DataSource resource.
        :param index_id: The IndexId of the DataSource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_qbusiness as interfaces_qbusiness
            
            data_source_reference = interfaces_qbusiness.DataSourceReference(
                application_id="applicationId",
                data_source_arn="dataSourceArn",
                data_source_id="dataSourceId",
                index_id="indexId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__997c866f81aa301cc81240b33c2d94d2cb4d92cd26ec5f6773cd85bfaff0f159)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument data_source_arn", value=data_source_arn, expected_type=type_hints["data_source_arn"])
            check_type(argname="argument data_source_id", value=data_source_id, expected_type=type_hints["data_source_id"])
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "data_source_arn": data_source_arn,
            "data_source_id": data_source_id,
            "index_id": index_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the DataSource resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_arn(self) -> builtins.str:
        '''The ARN of the DataSource resource.'''
        result = self._values.get("data_source_arn")
        assert result is not None, "Required property 'data_source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_id(self) -> builtins.str:
        '''The DataSourceId of the DataSource resource.'''
        result = self._values.get("data_source_id")
        assert result is not None, "Required property 'data_source_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The IndexId of the DataSource resource.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataSourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.IApplicationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_qbusiness.IApplicationRef"

    @builtins.property
    @jsii.member(jsii_name="applicationRef")
    def application_ref(self) -> "ApplicationReference":
        '''(experimental) A reference to a Application resource.

        :stability: experimental
        '''
        return typing.cast("ApplicationReference", jsii.get(self, "applicationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IApplicationRef).__jsii_proxy_class__ = lambda : _IApplicationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.IDataAccessorRef")
class IDataAccessorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataAccessor.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataAccessorRef")
    def data_accessor_ref(self) -> "DataAccessorReference":
        '''(experimental) A reference to a DataAccessor resource.

        :stability: experimental
        '''
        ...


class _IDataAccessorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataAccessor.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_qbusiness.IDataAccessorRef"

    @builtins.property
    @jsii.member(jsii_name="dataAccessorRef")
    def data_accessor_ref(self) -> "DataAccessorReference":
        '''(experimental) A reference to a DataAccessor resource.

        :stability: experimental
        '''
        return typing.cast("DataAccessorReference", jsii.get(self, "dataAccessorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataAccessorRef).__jsii_proxy_class__ = lambda : _IDataAccessorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.IDataSourceRef")
class IDataSourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        ...


class _IDataSourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataSource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_qbusiness.IDataSourceRef"

    @builtins.property
    @jsii.member(jsii_name="dataSourceRef")
    def data_source_ref(self) -> "DataSourceReference":
        '''(experimental) A reference to a DataSource resource.

        :stability: experimental
        '''
        return typing.cast("DataSourceReference", jsii.get(self, "dataSourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataSourceRef).__jsii_proxy_class__ = lambda : _IDataSourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.IIndexRef")
class IIndexRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Index.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "IndexReference":
        '''(experimental) A reference to a Index resource.

        :stability: experimental
        '''
        ...


class _IIndexRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Index.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_qbusiness.IIndexRef"

    @builtins.property
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "IndexReference":
        '''(experimental) A reference to a Index resource.

        :stability: experimental
        '''
        return typing.cast("IndexReference", jsii.get(self, "indexRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIndexRef).__jsii_proxy_class__ = lambda : _IIndexRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.IPermissionRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_qbusiness.IPermissionRef"

    @builtins.property
    @jsii.member(jsii_name="permissionRef")
    def permission_ref(self) -> "PermissionReference":
        '''(experimental) A reference to a Permission resource.

        :stability: experimental
        '''
        return typing.cast("PermissionReference", jsii.get(self, "permissionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPermissionRef).__jsii_proxy_class__ = lambda : _IPermissionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.IPluginRef")
class IPluginRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Plugin.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="pluginRef")
    def plugin_ref(self) -> "PluginReference":
        '''(experimental) A reference to a Plugin resource.

        :stability: experimental
        '''
        ...


class _IPluginRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Plugin.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_qbusiness.IPluginRef"

    @builtins.property
    @jsii.member(jsii_name="pluginRef")
    def plugin_ref(self) -> "PluginReference":
        '''(experimental) A reference to a Plugin resource.

        :stability: experimental
        '''
        return typing.cast("PluginReference", jsii.get(self, "pluginRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPluginRef).__jsii_proxy_class__ = lambda : _IPluginRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.IRetrieverRef")
class IRetrieverRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Retriever.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="retrieverRef")
    def retriever_ref(self) -> "RetrieverReference":
        '''(experimental) A reference to a Retriever resource.

        :stability: experimental
        '''
        ...


class _IRetrieverRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Retriever.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_qbusiness.IRetrieverRef"

    @builtins.property
    @jsii.member(jsii_name="retrieverRef")
    def retriever_ref(self) -> "RetrieverReference":
        '''(experimental) A reference to a Retriever resource.

        :stability: experimental
        '''
        return typing.cast("RetrieverReference", jsii.get(self, "retrieverRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRetrieverRef).__jsii_proxy_class__ = lambda : _IRetrieverRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.IWebExperienceRef")
class IWebExperienceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WebExperience.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="webExperienceRef")
    def web_experience_ref(self) -> "WebExperienceReference":
        '''(experimental) A reference to a WebExperience resource.

        :stability: experimental
        '''
        ...


class _IWebExperienceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WebExperience.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_qbusiness.IWebExperienceRef"

    @builtins.property
    @jsii.member(jsii_name="webExperienceRef")
    def web_experience_ref(self) -> "WebExperienceReference":
        '''(experimental) A reference to a WebExperience resource.

        :stability: experimental
        '''
        return typing.cast("WebExperienceReference", jsii.get(self, "webExperienceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWebExperienceRef).__jsii_proxy_class__ = lambda : _IWebExperienceRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.IndexReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "index_arn": "indexArn",
        "index_id": "indexId",
    },
)
class IndexReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        index_arn: builtins.str,
        index_id: builtins.str,
    ) -> None:
        '''A reference to a Index resource.

        :param application_id: The ApplicationId of the Index resource.
        :param index_arn: The ARN of the Index resource.
        :param index_id: The IndexId of the Index resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_qbusiness as interfaces_qbusiness
            
            index_reference = interfaces_qbusiness.IndexReference(
                application_id="applicationId",
                index_arn="indexArn",
                index_id="indexId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afa511e74f77e7f53931e5e988c7e1a3a9aeb0e0da2419f98c71a19b093e00f8)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument index_arn", value=index_arn, expected_type=type_hints["index_arn"])
            check_type(argname="argument index_id", value=index_id, expected_type=type_hints["index_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "index_arn": index_arn,
            "index_id": index_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Index resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_arn(self) -> builtins.str:
        '''The ARN of the Index resource.'''
        result = self._values.get("index_arn")
        assert result is not None, "Required property 'index_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def index_id(self) -> builtins.str:
        '''The IndexId of the Index resource.'''
        result = self._values.get("index_id")
        assert result is not None, "Required property 'index_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IndexReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.PermissionReference",
    jsii_struct_bases=[],
    name_mapping={"application_id": "applicationId", "statement_id": "statementId"},
)
class PermissionReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        statement_id: builtins.str,
    ) -> None:
        '''A reference to a Permission resource.

        :param application_id: The ApplicationId of the Permission resource.
        :param statement_id: The StatementId of the Permission resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_qbusiness as interfaces_qbusiness
            
            permission_reference = interfaces_qbusiness.PermissionReference(
                application_id="applicationId",
                statement_id="statementId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b22983f84762f2d6144f8b698b11a708facb4dd0758b51f1d4c216cfc1834bcf)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument statement_id", value=statement_id, expected_type=type_hints["statement_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "statement_id": statement_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Permission resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statement_id(self) -> builtins.str:
        '''The StatementId of the Permission resource.'''
        result = self._values.get("statement_id")
        assert result is not None, "Required property 'statement_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.PluginReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "plugin_arn": "pluginArn",
        "plugin_id": "pluginId",
    },
)
class PluginReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        plugin_arn: builtins.str,
        plugin_id: builtins.str,
    ) -> None:
        '''A reference to a Plugin resource.

        :param application_id: The ApplicationId of the Plugin resource.
        :param plugin_arn: The ARN of the Plugin resource.
        :param plugin_id: The PluginId of the Plugin resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_qbusiness as interfaces_qbusiness
            
            plugin_reference = interfaces_qbusiness.PluginReference(
                application_id="applicationId",
                plugin_arn="pluginArn",
                plugin_id="pluginId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b69bfd1245ecb05ca568637f2d293f301a4ddf0d129f764db8d644cc20ac21d)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument plugin_arn", value=plugin_arn, expected_type=type_hints["plugin_arn"])
            check_type(argname="argument plugin_id", value=plugin_id, expected_type=type_hints["plugin_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "plugin_arn": plugin_arn,
            "plugin_id": plugin_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Plugin resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plugin_arn(self) -> builtins.str:
        '''The ARN of the Plugin resource.'''
        result = self._values.get("plugin_arn")
        assert result is not None, "Required property 'plugin_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def plugin_id(self) -> builtins.str:
        '''The PluginId of the Plugin resource.'''
        result = self._values.get("plugin_id")
        assert result is not None, "Required property 'plugin_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PluginReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.RetrieverReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "retriever_arn": "retrieverArn",
        "retriever_id": "retrieverId",
    },
)
class RetrieverReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        retriever_arn: builtins.str,
        retriever_id: builtins.str,
    ) -> None:
        '''A reference to a Retriever resource.

        :param application_id: The ApplicationId of the Retriever resource.
        :param retriever_arn: The ARN of the Retriever resource.
        :param retriever_id: The RetrieverId of the Retriever resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_qbusiness as interfaces_qbusiness
            
            retriever_reference = interfaces_qbusiness.RetrieverReference(
                application_id="applicationId",
                retriever_arn="retrieverArn",
                retriever_id="retrieverId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c0bdf172a0ce1e83224dc6653ba7dfc9fa653e3ffbe3185aebc60b20eef800f)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument retriever_arn", value=retriever_arn, expected_type=type_hints["retriever_arn"])
            check_type(argname="argument retriever_id", value=retriever_id, expected_type=type_hints["retriever_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "retriever_arn": retriever_arn,
            "retriever_id": retriever_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the Retriever resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retriever_arn(self) -> builtins.str:
        '''The ARN of the Retriever resource.'''
        result = self._values.get("retriever_arn")
        assert result is not None, "Required property 'retriever_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retriever_id(self) -> builtins.str:
        '''The RetrieverId of the Retriever resource.'''
        result = self._values.get("retriever_id")
        assert result is not None, "Required property 'retriever_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RetrieverReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_qbusiness.WebExperienceReference",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "web_experience_arn": "webExperienceArn",
        "web_experience_id": "webExperienceId",
    },
)
class WebExperienceReference:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        web_experience_arn: builtins.str,
        web_experience_id: builtins.str,
    ) -> None:
        '''A reference to a WebExperience resource.

        :param application_id: The ApplicationId of the WebExperience resource.
        :param web_experience_arn: The ARN of the WebExperience resource.
        :param web_experience_id: The WebExperienceId of the WebExperience resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_qbusiness as interfaces_qbusiness
            
            web_experience_reference = interfaces_qbusiness.WebExperienceReference(
                application_id="applicationId",
                web_experience_arn="webExperienceArn",
                web_experience_id="webExperienceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbb4cb5bcd25420cc779bd0e2ea30049db3a0b746b212c1e164e4184edaf9598)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument web_experience_arn", value=web_experience_arn, expected_type=type_hints["web_experience_arn"])
            check_type(argname="argument web_experience_id", value=web_experience_id, expected_type=type_hints["web_experience_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_id": application_id,
            "web_experience_arn": web_experience_arn,
            "web_experience_id": web_experience_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''The ApplicationId of the WebExperience resource.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def web_experience_arn(self) -> builtins.str:
        '''The ARN of the WebExperience resource.'''
        result = self._values.get("web_experience_arn")
        assert result is not None, "Required property 'web_experience_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def web_experience_id(self) -> builtins.str:
        '''The WebExperienceId of the WebExperience resource.'''
        result = self._values.get("web_experience_id")
        assert result is not None, "Required property 'web_experience_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebExperienceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApplicationReference",
    "DataAccessorReference",
    "DataSourceReference",
    "IApplicationRef",
    "IDataAccessorRef",
    "IDataSourceRef",
    "IIndexRef",
    "IPermissionRef",
    "IPluginRef",
    "IRetrieverRef",
    "IWebExperienceRef",
    "IndexReference",
    "PermissionReference",
    "PluginReference",
    "RetrieverReference",
    "WebExperienceReference",
]

publication.publish()

def _typecheckingstub__02780d7e62f54269cdd696dfde5f4e7da716acfbebae0e1f7ce853be6d52bd3d(
    *,
    application_arn: builtins.str,
    application_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__848e0be0e45da9b5e17d7c25a4df995453dab35fb28d46250adb03ae80146e37(
    *,
    application_id: builtins.str,
    data_accessor_arn: builtins.str,
    data_accessor_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__997c866f81aa301cc81240b33c2d94d2cb4d92cd26ec5f6773cd85bfaff0f159(
    *,
    application_id: builtins.str,
    data_source_arn: builtins.str,
    data_source_id: builtins.str,
    index_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa511e74f77e7f53931e5e988c7e1a3a9aeb0e0da2419f98c71a19b093e00f8(
    *,
    application_id: builtins.str,
    index_arn: builtins.str,
    index_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b22983f84762f2d6144f8b698b11a708facb4dd0758b51f1d4c216cfc1834bcf(
    *,
    application_id: builtins.str,
    statement_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b69bfd1245ecb05ca568637f2d293f301a4ddf0d129f764db8d644cc20ac21d(
    *,
    application_id: builtins.str,
    plugin_arn: builtins.str,
    plugin_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c0bdf172a0ce1e83224dc6653ba7dfc9fa653e3ffbe3185aebc60b20eef800f(
    *,
    application_id: builtins.str,
    retriever_arn: builtins.str,
    retriever_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbb4cb5bcd25420cc779bd0e2ea30049db3a0b746b212c1e164e4184edaf9598(
    *,
    application_id: builtins.str,
    web_experience_arn: builtins.str,
    web_experience_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IApplicationRef, IDataAccessorRef, IDataSourceRef, IIndexRef, IPermissionRef, IPluginRef, IRetrieverRef, IWebExperienceRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
