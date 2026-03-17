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
    jsii_type="aws-cdk-lib.interfaces.aws_glue.ClassifierReference",
    jsii_struct_bases=[],
    name_mapping={"classifier_id": "classifierId"},
)
class ClassifierReference:
    def __init__(self, *, classifier_id: builtins.str) -> None:
        '''A reference to a Classifier resource.

        :param classifier_id: The Id of the Classifier resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            classifier_reference = interfaces_glue.ClassifierReference(
                classifier_id="classifierId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__153075acc355fb8c67c2595f86bb736959d7a3490470e1496c4634652a073e55)
            check_type(argname="argument classifier_id", value=classifier_id, expected_type=type_hints["classifier_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "classifier_id": classifier_id,
        }

    @builtins.property
    def classifier_id(self) -> builtins.str:
        '''The Id of the Classifier resource.'''
        result = self._values.get("classifier_id")
        assert result is not None, "Required property 'classifier_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClassifierReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.ConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"connection_id": "connectionId"},
)
class ConnectionReference:
    def __init__(self, *, connection_id: builtins.str) -> None:
        '''A reference to a Connection resource.

        :param connection_id: The Id of the Connection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            connection_reference = interfaces_glue.ConnectionReference(
                connection_id="connectionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0c23f5314f51a17152319ab80f389d2f1b18975384c84d1d2931ac1a3121d9f)
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_id": connection_id,
        }

    @builtins.property
    def connection_id(self) -> builtins.str:
        '''The Id of the Connection resource.'''
        result = self._values.get("connection_id")
        assert result is not None, "Required property 'connection_id' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_glue.CrawlerReference",
    jsii_struct_bases=[],
    name_mapping={"crawler_name": "crawlerName"},
)
class CrawlerReference:
    def __init__(self, *, crawler_name: builtins.str) -> None:
        '''A reference to a Crawler resource.

        :param crawler_name: The Name of the Crawler resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            crawler_reference = interfaces_glue.CrawlerReference(
                crawler_name="crawlerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad53740eb8897f033af56fd03963af3e4f644f727baf57ca71c35961fceb97b6)
            check_type(argname="argument crawler_name", value=crawler_name, expected_type=type_hints["crawler_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "crawler_name": crawler_name,
        }

    @builtins.property
    def crawler_name(self) -> builtins.str:
        '''The Name of the Crawler resource.'''
        result = self._values.get("crawler_name")
        assert result is not None, "Required property 'crawler_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CrawlerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.CustomEntityTypeReference",
    jsii_struct_bases=[],
    name_mapping={"custom_entity_type_id": "customEntityTypeId"},
)
class CustomEntityTypeReference:
    def __init__(self, *, custom_entity_type_id: builtins.str) -> None:
        '''A reference to a CustomEntityType resource.

        :param custom_entity_type_id: The Id of the CustomEntityType resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            custom_entity_type_reference = interfaces_glue.CustomEntityTypeReference(
                custom_entity_type_id="customEntityTypeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2752daff245d03b65a99c918eff72a3eb4c7c58fc56a5bf622d9117515921d7f)
            check_type(argname="argument custom_entity_type_id", value=custom_entity_type_id, expected_type=type_hints["custom_entity_type_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "custom_entity_type_id": custom_entity_type_id,
        }

    @builtins.property
    def custom_entity_type_id(self) -> builtins.str:
        '''The Id of the CustomEntityType resource.'''
        result = self._values.get("custom_entity_type_id")
        assert result is not None, "Required property 'custom_entity_type_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomEntityTypeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.DataCatalogEncryptionSettingsReference",
    jsii_struct_bases=[],
    name_mapping={
        "data_catalog_encryption_settings_id": "dataCatalogEncryptionSettingsId",
    },
)
class DataCatalogEncryptionSettingsReference:
    def __init__(self, *, data_catalog_encryption_settings_id: builtins.str) -> None:
        '''A reference to a DataCatalogEncryptionSettings resource.

        :param data_catalog_encryption_settings_id: The Id of the DataCatalogEncryptionSettings resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            data_catalog_encryption_settings_reference = interfaces_glue.DataCatalogEncryptionSettingsReference(
                data_catalog_encryption_settings_id="dataCatalogEncryptionSettingsId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__824f5a564c0864f04cf9c7b44937b6e5dbe2d9acb8bd8b048f28e3b1f667a924)
            check_type(argname="argument data_catalog_encryption_settings_id", value=data_catalog_encryption_settings_id, expected_type=type_hints["data_catalog_encryption_settings_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_catalog_encryption_settings_id": data_catalog_encryption_settings_id,
        }

    @builtins.property
    def data_catalog_encryption_settings_id(self) -> builtins.str:
        '''The Id of the DataCatalogEncryptionSettings resource.'''
        result = self._values.get("data_catalog_encryption_settings_id")
        assert result is not None, "Required property 'data_catalog_encryption_settings_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataCatalogEncryptionSettingsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.DataQualityRulesetReference",
    jsii_struct_bases=[],
    name_mapping={"data_quality_ruleset_id": "dataQualityRulesetId"},
)
class DataQualityRulesetReference:
    def __init__(self, *, data_quality_ruleset_id: builtins.str) -> None:
        '''A reference to a DataQualityRuleset resource.

        :param data_quality_ruleset_id: The Id of the DataQualityRuleset resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            data_quality_ruleset_reference = interfaces_glue.DataQualityRulesetReference(
                data_quality_ruleset_id="dataQualityRulesetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__637b7e752aad4e64a85b4673d0fd9fbde33283ca6452dac108809ad38887f3cd)
            check_type(argname="argument data_quality_ruleset_id", value=data_quality_ruleset_id, expected_type=type_hints["data_quality_ruleset_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_quality_ruleset_id": data_quality_ruleset_id,
        }

    @builtins.property
    def data_quality_ruleset_id(self) -> builtins.str:
        '''The Id of the DataQualityRuleset resource.'''
        result = self._values.get("data_quality_ruleset_id")
        assert result is not None, "Required property 'data_quality_ruleset_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataQualityRulesetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.DatabaseReference",
    jsii_struct_bases=[],
    name_mapping={"database_name": "databaseName"},
)
class DatabaseReference:
    def __init__(self, *, database_name: builtins.str) -> None:
        '''A reference to a Database resource.

        :param database_name: The DatabaseName of the Database resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            database_reference = interfaces_glue.DatabaseReference(
                database_name="databaseName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b006942e6851e8e5b67ab80d761f762e021506f9975b704097cc0df559962e7e)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
        }

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The DatabaseName of the Database resource.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DatabaseReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.DevEndpointReference",
    jsii_struct_bases=[],
    name_mapping={"endpoint_name": "endpointName"},
)
class DevEndpointReference:
    def __init__(self, *, endpoint_name: builtins.str) -> None:
        '''A reference to a DevEndpoint resource.

        :param endpoint_name: The EndpointName of the DevEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            dev_endpoint_reference = interfaces_glue.DevEndpointReference(
                endpoint_name="endpointName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__050454acd533b9c974358b1bfdec6277e66592a87a752610c62dc6b896b95d0f)
            check_type(argname="argument endpoint_name", value=endpoint_name, expected_type=type_hints["endpoint_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_name": endpoint_name,
        }

    @builtins.property
    def endpoint_name(self) -> builtins.str:
        '''The EndpointName of the DevEndpoint resource.'''
        result = self._values.get("endpoint_name")
        assert result is not None, "Required property 'endpoint_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IClassifierRef")
class IClassifierRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Classifier.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="classifierRef")
    def classifier_ref(self) -> "ClassifierReference":
        '''(experimental) A reference to a Classifier resource.

        :stability: experimental
        '''
        ...


class _IClassifierRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Classifier.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IClassifierRef"

    @builtins.property
    @jsii.member(jsii_name="classifierRef")
    def classifier_ref(self) -> "ClassifierReference":
        '''(experimental) A reference to a Classifier resource.

        :stability: experimental
        '''
        return typing.cast("ClassifierReference", jsii.get(self, "classifierRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClassifierRef).__jsii_proxy_class__ = lambda : _IClassifierRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IConnectionRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionReference", jsii.get(self, "connectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionRef).__jsii_proxy_class__ = lambda : _IConnectionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ICrawlerRef")
class ICrawlerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Crawler.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="crawlerRef")
    def crawler_ref(self) -> "CrawlerReference":
        '''(experimental) A reference to a Crawler resource.

        :stability: experimental
        '''
        ...


class _ICrawlerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Crawler.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ICrawlerRef"

    @builtins.property
    @jsii.member(jsii_name="crawlerRef")
    def crawler_ref(self) -> "CrawlerReference":
        '''(experimental) A reference to a Crawler resource.

        :stability: experimental
        '''
        return typing.cast("CrawlerReference", jsii.get(self, "crawlerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICrawlerRef).__jsii_proxy_class__ = lambda : _ICrawlerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ICustomEntityTypeRef")
class ICustomEntityTypeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CustomEntityType.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="customEntityTypeRef")
    def custom_entity_type_ref(self) -> "CustomEntityTypeReference":
        '''(experimental) A reference to a CustomEntityType resource.

        :stability: experimental
        '''
        ...


class _ICustomEntityTypeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CustomEntityType.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ICustomEntityTypeRef"

    @builtins.property
    @jsii.member(jsii_name="customEntityTypeRef")
    def custom_entity_type_ref(self) -> "CustomEntityTypeReference":
        '''(experimental) A reference to a CustomEntityType resource.

        :stability: experimental
        '''
        return typing.cast("CustomEntityTypeReference", jsii.get(self, "customEntityTypeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICustomEntityTypeRef).__jsii_proxy_class__ = lambda : _ICustomEntityTypeRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IDataCatalogEncryptionSettingsRef"
)
class IDataCatalogEncryptionSettingsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataCatalogEncryptionSettings.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataCatalogEncryptionSettingsRef")
    def data_catalog_encryption_settings_ref(
        self,
    ) -> "DataCatalogEncryptionSettingsReference":
        '''(experimental) A reference to a DataCatalogEncryptionSettings resource.

        :stability: experimental
        '''
        ...


class _IDataCatalogEncryptionSettingsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataCatalogEncryptionSettings.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IDataCatalogEncryptionSettingsRef"

    @builtins.property
    @jsii.member(jsii_name="dataCatalogEncryptionSettingsRef")
    def data_catalog_encryption_settings_ref(
        self,
    ) -> "DataCatalogEncryptionSettingsReference":
        '''(experimental) A reference to a DataCatalogEncryptionSettings resource.

        :stability: experimental
        '''
        return typing.cast("DataCatalogEncryptionSettingsReference", jsii.get(self, "dataCatalogEncryptionSettingsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataCatalogEncryptionSettingsRef).__jsii_proxy_class__ = lambda : _IDataCatalogEncryptionSettingsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IDataQualityRulesetRef")
class IDataQualityRulesetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataQualityRuleset.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataQualityRulesetRef")
    def data_quality_ruleset_ref(self) -> "DataQualityRulesetReference":
        '''(experimental) A reference to a DataQualityRuleset resource.

        :stability: experimental
        '''
        ...


class _IDataQualityRulesetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataQualityRuleset.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IDataQualityRulesetRef"

    @builtins.property
    @jsii.member(jsii_name="dataQualityRulesetRef")
    def data_quality_ruleset_ref(self) -> "DataQualityRulesetReference":
        '''(experimental) A reference to a DataQualityRuleset resource.

        :stability: experimental
        '''
        return typing.cast("DataQualityRulesetReference", jsii.get(self, "dataQualityRulesetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataQualityRulesetRef).__jsii_proxy_class__ = lambda : _IDataQualityRulesetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IDatabaseRef")
class IDatabaseRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Database.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="databaseRef")
    def database_ref(self) -> "DatabaseReference":
        '''(experimental) A reference to a Database resource.

        :stability: experimental
        '''
        ...


class _IDatabaseRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Database.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IDatabaseRef"

    @builtins.property
    @jsii.member(jsii_name="databaseRef")
    def database_ref(self) -> "DatabaseReference":
        '''(experimental) A reference to a Database resource.

        :stability: experimental
        '''
        return typing.cast("DatabaseReference", jsii.get(self, "databaseRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDatabaseRef).__jsii_proxy_class__ = lambda : _IDatabaseRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IDevEndpointRef")
class IDevEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DevEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="devEndpointRef")
    def dev_endpoint_ref(self) -> "DevEndpointReference":
        '''(experimental) A reference to a DevEndpoint resource.

        :stability: experimental
        '''
        ...


class _IDevEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DevEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IDevEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="devEndpointRef")
    def dev_endpoint_ref(self) -> "DevEndpointReference":
        '''(experimental) A reference to a DevEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("DevEndpointReference", jsii.get(self, "devEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDevEndpointRef).__jsii_proxy_class__ = lambda : _IDevEndpointRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IIdentityCenterConfigurationRef"
)
class IIdentityCenterConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityCenterConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="identityCenterConfigurationRef")
    def identity_center_configuration_ref(
        self,
    ) -> "IdentityCenterConfigurationReference":
        '''(experimental) A reference to a IdentityCenterConfiguration resource.

        :stability: experimental
        '''
        ...


class _IIdentityCenterConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IdentityCenterConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IIdentityCenterConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="identityCenterConfigurationRef")
    def identity_center_configuration_ref(
        self,
    ) -> "IdentityCenterConfigurationReference":
        '''(experimental) A reference to a IdentityCenterConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("IdentityCenterConfigurationReference", jsii.get(self, "identityCenterConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIdentityCenterConfigurationRef).__jsii_proxy_class__ = lambda : _IIdentityCenterConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IIntegrationRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IIntegrationRef"

    @builtins.property
    @jsii.member(jsii_name="integrationRef")
    def integration_ref(self) -> "IntegrationReference":
        '''(experimental) A reference to a Integration resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationReference", jsii.get(self, "integrationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationRef).__jsii_proxy_class__ = lambda : _IIntegrationRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IIntegrationResourcePropertyRef"
)
class IIntegrationResourcePropertyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a IntegrationResourceProperty.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="integrationResourcePropertyRef")
    def integration_resource_property_ref(
        self,
    ) -> "IntegrationResourcePropertyReference":
        '''(experimental) A reference to a IntegrationResourceProperty resource.

        :stability: experimental
        '''
        ...


class _IIntegrationResourcePropertyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a IntegrationResourceProperty.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IIntegrationResourcePropertyRef"

    @builtins.property
    @jsii.member(jsii_name="integrationResourcePropertyRef")
    def integration_resource_property_ref(
        self,
    ) -> "IntegrationResourcePropertyReference":
        '''(experimental) A reference to a IntegrationResourceProperty resource.

        :stability: experimental
        '''
        return typing.cast("IntegrationResourcePropertyReference", jsii.get(self, "integrationResourcePropertyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IIntegrationResourcePropertyRef).__jsii_proxy_class__ = lambda : _IIntegrationResourcePropertyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IJobRef")
class IJobRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Job.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="jobRef")
    def job_ref(self) -> "JobReference":
        '''(experimental) A reference to a Job resource.

        :stability: experimental
        '''
        ...


class _IJobRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Job.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IJobRef"

    @builtins.property
    @jsii.member(jsii_name="jobRef")
    def job_ref(self) -> "JobReference":
        '''(experimental) A reference to a Job resource.

        :stability: experimental
        '''
        return typing.cast("JobReference", jsii.get(self, "jobRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJobRef).__jsii_proxy_class__ = lambda : _IJobRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IMLTransformRef")
class IMLTransformRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MLTransform.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="mlTransformRef")
    def ml_transform_ref(self) -> "MLTransformReference":
        '''(experimental) A reference to a MLTransform resource.

        :stability: experimental
        '''
        ...


class _IMLTransformRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MLTransform.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IMLTransformRef"

    @builtins.property
    @jsii.member(jsii_name="mlTransformRef")
    def ml_transform_ref(self) -> "MLTransformReference":
        '''(experimental) A reference to a MLTransform resource.

        :stability: experimental
        '''
        return typing.cast("MLTransformReference", jsii.get(self, "mlTransformRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMLTransformRef).__jsii_proxy_class__ = lambda : _IMLTransformRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IPartitionRef")
class IPartitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Partition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="partitionRef")
    def partition_ref(self) -> "PartitionReference":
        '''(experimental) A reference to a Partition resource.

        :stability: experimental
        '''
        ...


class _IPartitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Partition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IPartitionRef"

    @builtins.property
    @jsii.member(jsii_name="partitionRef")
    def partition_ref(self) -> "PartitionReference":
        '''(experimental) A reference to a Partition resource.

        :stability: experimental
        '''
        return typing.cast("PartitionReference", jsii.get(self, "partitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPartitionRef).__jsii_proxy_class__ = lambda : _IPartitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IRegistryRef")
class IRegistryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Registry.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="registryRef")
    def registry_ref(self) -> "RegistryReference":
        '''(experimental) A reference to a Registry resource.

        :stability: experimental
        '''
        ...


class _IRegistryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Registry.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IRegistryRef"

    @builtins.property
    @jsii.member(jsii_name="registryRef")
    def registry_ref(self) -> "RegistryReference":
        '''(experimental) A reference to a Registry resource.

        :stability: experimental
        '''
        return typing.cast("RegistryReference", jsii.get(self, "registryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRegistryRef).__jsii_proxy_class__ = lambda : _IRegistryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ISchemaRef")
class ISchemaRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Schema.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schemaRef")
    def schema_ref(self) -> "SchemaReference":
        '''(experimental) A reference to a Schema resource.

        :stability: experimental
        '''
        ...


class _ISchemaRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Schema.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ISchemaRef"

    @builtins.property
    @jsii.member(jsii_name="schemaRef")
    def schema_ref(self) -> "SchemaReference":
        '''(experimental) A reference to a Schema resource.

        :stability: experimental
        '''
        return typing.cast("SchemaReference", jsii.get(self, "schemaRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaRef).__jsii_proxy_class__ = lambda : _ISchemaRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ISchemaVersionMetadataRef")
class ISchemaVersionMetadataRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SchemaVersionMetadata.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schemaVersionMetadataRef")
    def schema_version_metadata_ref(self) -> "SchemaVersionMetadataReference":
        '''(experimental) A reference to a SchemaVersionMetadata resource.

        :stability: experimental
        '''
        ...


class _ISchemaVersionMetadataRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SchemaVersionMetadata.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ISchemaVersionMetadataRef"

    @builtins.property
    @jsii.member(jsii_name="schemaVersionMetadataRef")
    def schema_version_metadata_ref(self) -> "SchemaVersionMetadataReference":
        '''(experimental) A reference to a SchemaVersionMetadata resource.

        :stability: experimental
        '''
        return typing.cast("SchemaVersionMetadataReference", jsii.get(self, "schemaVersionMetadataRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaVersionMetadataRef).__jsii_proxy_class__ = lambda : _ISchemaVersionMetadataRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ISchemaVersionRef")
class ISchemaVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SchemaVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schemaVersionRef")
    def schema_version_ref(self) -> "SchemaVersionReference":
        '''(experimental) A reference to a SchemaVersion resource.

        :stability: experimental
        '''
        ...


class _ISchemaVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SchemaVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ISchemaVersionRef"

    @builtins.property
    @jsii.member(jsii_name="schemaVersionRef")
    def schema_version_ref(self) -> "SchemaVersionReference":
        '''(experimental) A reference to a SchemaVersion resource.

        :stability: experimental
        '''
        return typing.cast("SchemaVersionReference", jsii.get(self, "schemaVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchemaVersionRef).__jsii_proxy_class__ = lambda : _ISchemaVersionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ISecurityConfigurationRef")
class ISecurityConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationRef")
    def security_configuration_ref(self) -> "SecurityConfigurationReference":
        '''(experimental) A reference to a SecurityConfiguration resource.

        :stability: experimental
        '''
        ...


class _ISecurityConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ISecurityConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationRef")
    def security_configuration_ref(self) -> "SecurityConfigurationReference":
        '''(experimental) A reference to a SecurityConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("SecurityConfigurationReference", jsii.get(self, "securityConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityConfigurationRef).__jsii_proxy_class__ = lambda : _ISecurityConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ITableOptimizerRef")
class ITableOptimizerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TableOptimizer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tableOptimizerRef")
    def table_optimizer_ref(self) -> "TableOptimizerReference":
        '''(experimental) A reference to a TableOptimizer resource.

        :stability: experimental
        '''
        ...


class _ITableOptimizerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TableOptimizer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ITableOptimizerRef"

    @builtins.property
    @jsii.member(jsii_name="tableOptimizerRef")
    def table_optimizer_ref(self) -> "TableOptimizerReference":
        '''(experimental) A reference to a TableOptimizer resource.

        :stability: experimental
        '''
        return typing.cast("TableOptimizerReference", jsii.get(self, "tableOptimizerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITableOptimizerRef).__jsii_proxy_class__ = lambda : _ITableOptimizerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ITableRef")
class ITableRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Table.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tableRef")
    def table_ref(self) -> "TableReference":
        '''(experimental) A reference to a Table resource.

        :stability: experimental
        '''
        ...


class _ITableRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Table.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ITableRef"

    @builtins.property
    @jsii.member(jsii_name="tableRef")
    def table_ref(self) -> "TableReference":
        '''(experimental) A reference to a Table resource.

        :stability: experimental
        '''
        return typing.cast("TableReference", jsii.get(self, "tableRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITableRef).__jsii_proxy_class__ = lambda : _ITableRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.ITriggerRef")
class ITriggerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Trigger.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="triggerRef")
    def trigger_ref(self) -> "TriggerReference":
        '''(experimental) A reference to a Trigger resource.

        :stability: experimental
        '''
        ...


class _ITriggerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Trigger.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.ITriggerRef"

    @builtins.property
    @jsii.member(jsii_name="triggerRef")
    def trigger_ref(self) -> "TriggerReference":
        '''(experimental) A reference to a Trigger resource.

        :stability: experimental
        '''
        return typing.cast("TriggerReference", jsii.get(self, "triggerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITriggerRef).__jsii_proxy_class__ = lambda : _ITriggerRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IUsageProfileRef")
class IUsageProfileRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UsageProfile.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="usageProfileRef")
    def usage_profile_ref(self) -> "UsageProfileReference":
        '''(experimental) A reference to a UsageProfile resource.

        :stability: experimental
        '''
        ...


class _IUsageProfileRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UsageProfile.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IUsageProfileRef"

    @builtins.property
    @jsii.member(jsii_name="usageProfileRef")
    def usage_profile_ref(self) -> "UsageProfileReference":
        '''(experimental) A reference to a UsageProfile resource.

        :stability: experimental
        '''
        return typing.cast("UsageProfileReference", jsii.get(self, "usageProfileRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUsageProfileRef).__jsii_proxy_class__ = lambda : _IUsageProfileRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_glue.IWorkflowRef")
class IWorkflowRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workflow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        ...


class _IWorkflowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workflow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_glue.IWorkflowRef"

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        return typing.cast("WorkflowReference", jsii.get(self, "workflowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkflowRef).__jsii_proxy_class__ = lambda : _IWorkflowRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IdentityCenterConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"account_id": "accountId"},
)
class IdentityCenterConfigurationReference:
    def __init__(self, *, account_id: builtins.str) -> None:
        '''A reference to a IdentityCenterConfiguration resource.

        :param account_id: The AccountId of the IdentityCenterConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            identity_center_configuration_reference = interfaces_glue.IdentityCenterConfigurationReference(
                account_id="accountId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dce890d13c4e501fd50bfd966cbe5558eac1e8b2415bc6f873c45a675fef0455)
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_id": account_id,
        }

    @builtins.property
    def account_id(self) -> builtins.str:
        '''The AccountId of the IdentityCenterConfiguration resource.'''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IdentityCenterConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IntegrationReference",
    jsii_struct_bases=[],
    name_mapping={
        "integration_arn": "integrationArn",
        "integration_name": "integrationName",
    },
)
class IntegrationReference:
    def __init__(
        self,
        *,
        integration_arn: builtins.str,
        integration_name: builtins.str,
    ) -> None:
        '''A reference to a Integration resource.

        :param integration_arn: The IntegrationArn of the Integration resource.
        :param integration_name: The IntegrationName of the Integration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            integration_reference = interfaces_glue.IntegrationReference(
                integration_arn="integrationArn",
                integration_name="integrationName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__487ef973bf980b9533ab5e35911c785df93801badcd04a6ad9191c32ce95e300)
            check_type(argname="argument integration_arn", value=integration_arn, expected_type=type_hints["integration_arn"])
            check_type(argname="argument integration_name", value=integration_name, expected_type=type_hints["integration_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "integration_arn": integration_arn,
            "integration_name": integration_name,
        }

    @builtins.property
    def integration_arn(self) -> builtins.str:
        '''The IntegrationArn of the Integration resource.'''
        result = self._values.get("integration_arn")
        assert result is not None, "Required property 'integration_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_name(self) -> builtins.str:
        '''The IntegrationName of the Integration resource.'''
        result = self._values.get("integration_name")
        assert result is not None, "Required property 'integration_name' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_glue.IntegrationResourcePropertyReference",
    jsii_struct_bases=[],
    name_mapping={
        "resource_arn": "resourceArn",
        "resource_property_arn": "resourcePropertyArn",
    },
)
class IntegrationResourcePropertyReference:
    def __init__(
        self,
        *,
        resource_arn: builtins.str,
        resource_property_arn: builtins.str,
    ) -> None:
        '''A reference to a IntegrationResourceProperty resource.

        :param resource_arn: The ResourceArn of the IntegrationResourceProperty resource.
        :param resource_property_arn: The ResourcePropertyArn of the IntegrationResourceProperty resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            integration_resource_property_reference = interfaces_glue.IntegrationResourcePropertyReference(
                resource_arn="resourceArn",
                resource_property_arn="resourcePropertyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d78e927b289090d3ea11c2e52f58b5cdc45b50ebf0cb9ac19af7a86759d45975)
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument resource_property_arn", value=resource_property_arn, expected_type=type_hints["resource_property_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_arn": resource_arn,
            "resource_property_arn": resource_property_arn,
        }

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ResourceArn of the IntegrationResourceProperty resource.'''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_property_arn(self) -> builtins.str:
        '''The ResourcePropertyArn of the IntegrationResourceProperty resource.'''
        result = self._values.get("resource_property_arn")
        assert result is not None, "Required property 'resource_property_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "IntegrationResourcePropertyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.JobReference",
    jsii_struct_bases=[],
    name_mapping={"job_name": "jobName"},
)
class JobReference:
    def __init__(self, *, job_name: builtins.str) -> None:
        '''A reference to a Job resource.

        :param job_name: The Name of the Job resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            job_reference = interfaces_glue.JobReference(
                job_name="jobName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8c47c403cca6462755fa024cf63a9b8531d52ca6834543a739c13e8ee51c9e9)
            check_type(argname="argument job_name", value=job_name, expected_type=type_hints["job_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_name": job_name,
        }

    @builtins.property
    def job_name(self) -> builtins.str:
        '''The Name of the Job resource.'''
        result = self._values.get("job_name")
        assert result is not None, "Required property 'job_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.MLTransformReference",
    jsii_struct_bases=[],
    name_mapping={"ml_transform_id": "mlTransformId"},
)
class MLTransformReference:
    def __init__(self, *, ml_transform_id: builtins.str) -> None:
        '''A reference to a MLTransform resource.

        :param ml_transform_id: The Id of the MLTransform resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            m_lTransform_reference = interfaces_glue.MLTransformReference(
                ml_transform_id="mlTransformId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3f1a2f7b4f39bcc3b7be922b88fffd5ccf9f63df878ae375f85fa00250d7cff)
            check_type(argname="argument ml_transform_id", value=ml_transform_id, expected_type=type_hints["ml_transform_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ml_transform_id": ml_transform_id,
        }

    @builtins.property
    def ml_transform_id(self) -> builtins.str:
        '''The Id of the MLTransform resource.'''
        result = self._values.get("ml_transform_id")
        assert result is not None, "Required property 'ml_transform_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MLTransformReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.PartitionReference",
    jsii_struct_bases=[],
    name_mapping={"partition_id": "partitionId"},
)
class PartitionReference:
    def __init__(self, *, partition_id: builtins.str) -> None:
        '''A reference to a Partition resource.

        :param partition_id: The Id of the Partition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            partition_reference = interfaces_glue.PartitionReference(
                partition_id="partitionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a9698059eb8899c746fb237350793d2faff1bdfa61b71f202add91131734519)
            check_type(argname="argument partition_id", value=partition_id, expected_type=type_hints["partition_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "partition_id": partition_id,
        }

    @builtins.property
    def partition_id(self) -> builtins.str:
        '''The Id of the Partition resource.'''
        result = self._values.get("partition_id")
        assert result is not None, "Required property 'partition_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PartitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.RegistryReference",
    jsii_struct_bases=[],
    name_mapping={"registry_arn": "registryArn"},
)
class RegistryReference:
    def __init__(self, *, registry_arn: builtins.str) -> None:
        '''A reference to a Registry resource.

        :param registry_arn: The Arn of the Registry resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            registry_reference = interfaces_glue.RegistryReference(
                registry_arn="registryArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f46875075b9b44d3958fe5be64778d351238ba406d2bfaf624a127c572ecfdd)
            check_type(argname="argument registry_arn", value=registry_arn, expected_type=type_hints["registry_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "registry_arn": registry_arn,
        }

    @builtins.property
    def registry_arn(self) -> builtins.str:
        '''The Arn of the Registry resource.'''
        result = self._values.get("registry_arn")
        assert result is not None, "Required property 'registry_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.SchemaReference",
    jsii_struct_bases=[],
    name_mapping={"schema_arn": "schemaArn"},
)
class SchemaReference:
    def __init__(self, *, schema_arn: builtins.str) -> None:
        '''A reference to a Schema resource.

        :param schema_arn: The Arn of the Schema resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            schema_reference = interfaces_glue.SchemaReference(
                schema_arn="schemaArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b578c469d6ed870abb6802e9d10670c2f571c62a79988a4ded4d3dccbcf0754e)
            check_type(argname="argument schema_arn", value=schema_arn, expected_type=type_hints["schema_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "schema_arn": schema_arn,
        }

    @builtins.property
    def schema_arn(self) -> builtins.str:
        '''The Arn of the Schema resource.'''
        result = self._values.get("schema_arn")
        assert result is not None, "Required property 'schema_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.SchemaVersionMetadataReference",
    jsii_struct_bases=[],
    name_mapping={
        "key": "key",
        "schema_version_id": "schemaVersionId",
        "value": "value",
    },
)
class SchemaVersionMetadataReference:
    def __init__(
        self,
        *,
        key: builtins.str,
        schema_version_id: builtins.str,
        value: builtins.str,
    ) -> None:
        '''A reference to a SchemaVersionMetadata resource.

        :param key: The Key of the SchemaVersionMetadata resource.
        :param schema_version_id: The SchemaVersionId of the SchemaVersionMetadata resource.
        :param value: The Value of the SchemaVersionMetadata resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            schema_version_metadata_reference = interfaces_glue.SchemaVersionMetadataReference(
                key="key",
                schema_version_id="schemaVersionId",
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4b127790a6c1e064bc511d8914a963c65c84be0739a54f9274fdb48b4f2105d)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument schema_version_id", value=schema_version_id, expected_type=type_hints["schema_version_id"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "key": key,
            "schema_version_id": schema_version_id,
            "value": value,
        }

    @builtins.property
    def key(self) -> builtins.str:
        '''The Key of the SchemaVersionMetadata resource.'''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema_version_id(self) -> builtins.str:
        '''The SchemaVersionId of the SchemaVersionMetadata resource.'''
        result = self._values.get("schema_version_id")
        assert result is not None, "Required property 'schema_version_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The Value of the SchemaVersionMetadata resource.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaVersionMetadataReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.SchemaVersionReference",
    jsii_struct_bases=[],
    name_mapping={"version_id": "versionId"},
)
class SchemaVersionReference:
    def __init__(self, *, version_id: builtins.str) -> None:
        '''A reference to a SchemaVersion resource.

        :param version_id: The VersionId of the SchemaVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            schema_version_reference = interfaces_glue.SchemaVersionReference(
                version_id="versionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8183bbaf7cbe72ac30393afbba3db6508105f9305b6e69bf1acef9abffd833d2)
            check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version_id": version_id,
        }

    @builtins.property
    def version_id(self) -> builtins.str:
        '''The VersionId of the SchemaVersion resource.'''
        result = self._values.get("version_id")
        assert result is not None, "Required property 'version_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchemaVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.SecurityConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"security_configuration_id": "securityConfigurationId"},
)
class SecurityConfigurationReference:
    def __init__(self, *, security_configuration_id: builtins.str) -> None:
        '''A reference to a SecurityConfiguration resource.

        :param security_configuration_id: The Id of the SecurityConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            security_configuration_reference = interfaces_glue.SecurityConfigurationReference(
                security_configuration_id="securityConfigurationId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f762055d8744dcdcadf6d3ee48e027edbbedb409f2aee69d69051529ab7d003)
            check_type(argname="argument security_configuration_id", value=security_configuration_id, expected_type=type_hints["security_configuration_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_configuration_id": security_configuration_id,
        }

    @builtins.property
    def security_configuration_id(self) -> builtins.str:
        '''The Id of the SecurityConfiguration resource.'''
        result = self._values.get("security_configuration_id")
        assert result is not None, "Required property 'security_configuration_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.TableOptimizerReference",
    jsii_struct_bases=[],
    name_mapping={"table_optimizer_id": "tableOptimizerId"},
)
class TableOptimizerReference:
    def __init__(self, *, table_optimizer_id: builtins.str) -> None:
        '''A reference to a TableOptimizer resource.

        :param table_optimizer_id: The Id of the TableOptimizer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            table_optimizer_reference = interfaces_glue.TableOptimizerReference(
                table_optimizer_id="tableOptimizerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36d18932d532cd2df3f2355353c78a3d21a028fa0d2181f51b94ae7c9101726b)
            check_type(argname="argument table_optimizer_id", value=table_optimizer_id, expected_type=type_hints["table_optimizer_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_optimizer_id": table_optimizer_id,
        }

    @builtins.property
    def table_optimizer_id(self) -> builtins.str:
        '''The Id of the TableOptimizer resource.'''
        result = self._values.get("table_optimizer_id")
        assert result is not None, "Required property 'table_optimizer_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableOptimizerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.TableReference",
    jsii_struct_bases=[],
    name_mapping={"table_id": "tableId"},
)
class TableReference:
    def __init__(self, *, table_id: builtins.str) -> None:
        '''A reference to a Table resource.

        :param table_id: The Id of the Table resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            table_reference = interfaces_glue.TableReference(
                table_id="tableId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d91e1bc0dff8ee618900793d998bcf5ed91fd48153fcbcc02d63186fa2219535)
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "table_id": table_id,
        }

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The Id of the Table resource.'''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TableReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.TriggerReference",
    jsii_struct_bases=[],
    name_mapping={"trigger_name": "triggerName"},
)
class TriggerReference:
    def __init__(self, *, trigger_name: builtins.str) -> None:
        '''A reference to a Trigger resource.

        :param trigger_name: The Name of the Trigger resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            trigger_reference = interfaces_glue.TriggerReference(
                trigger_name="triggerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85c96b93a2c298c01219667b5012a8e417cd40c14e36afd3fd093081bbfc5a3e)
            check_type(argname="argument trigger_name", value=trigger_name, expected_type=type_hints["trigger_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "trigger_name": trigger_name,
        }

    @builtins.property
    def trigger_name(self) -> builtins.str:
        '''The Name of the Trigger resource.'''
        result = self._values.get("trigger_name")
        assert result is not None, "Required property 'trigger_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TriggerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.UsageProfileReference",
    jsii_struct_bases=[],
    name_mapping={"usage_profile_name": "usageProfileName"},
)
class UsageProfileReference:
    def __init__(self, *, usage_profile_name: builtins.str) -> None:
        '''A reference to a UsageProfile resource.

        :param usage_profile_name: The Name of the UsageProfile resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            usage_profile_reference = interfaces_glue.UsageProfileReference(
                usage_profile_name="usageProfileName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31cd7baf9c81bae2e0d29221ca6cf6bf1b06b730a8c9d8fedf8630e653710373)
            check_type(argname="argument usage_profile_name", value=usage_profile_name, expected_type=type_hints["usage_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "usage_profile_name": usage_profile_name,
        }

    @builtins.property
    def usage_profile_name(self) -> builtins.str:
        '''The Name of the UsageProfile resource.'''
        result = self._values.get("usage_profile_name")
        assert result is not None, "Required property 'usage_profile_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UsageProfileReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_glue.WorkflowReference",
    jsii_struct_bases=[],
    name_mapping={"workflow_name": "workflowName"},
)
class WorkflowReference:
    def __init__(self, *, workflow_name: builtins.str) -> None:
        '''A reference to a Workflow resource.

        :param workflow_name: The Name of the Workflow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_glue as interfaces_glue
            
            workflow_reference = interfaces_glue.WorkflowReference(
                workflow_name="workflowName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05490662a534e7ac737a01a3e54258abf2c5d6dd3a563391b841bd656b5b6220)
            check_type(argname="argument workflow_name", value=workflow_name, expected_type=type_hints["workflow_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workflow_name": workflow_name,
        }

    @builtins.property
    def workflow_name(self) -> builtins.str:
        '''The Name of the Workflow resource.'''
        result = self._values.get("workflow_name")
        assert result is not None, "Required property 'workflow_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ClassifierReference",
    "ConnectionReference",
    "CrawlerReference",
    "CustomEntityTypeReference",
    "DataCatalogEncryptionSettingsReference",
    "DataQualityRulesetReference",
    "DatabaseReference",
    "DevEndpointReference",
    "IClassifierRef",
    "IConnectionRef",
    "ICrawlerRef",
    "ICustomEntityTypeRef",
    "IDataCatalogEncryptionSettingsRef",
    "IDataQualityRulesetRef",
    "IDatabaseRef",
    "IDevEndpointRef",
    "IIdentityCenterConfigurationRef",
    "IIntegrationRef",
    "IIntegrationResourcePropertyRef",
    "IJobRef",
    "IMLTransformRef",
    "IPartitionRef",
    "IRegistryRef",
    "ISchemaRef",
    "ISchemaVersionMetadataRef",
    "ISchemaVersionRef",
    "ISecurityConfigurationRef",
    "ITableOptimizerRef",
    "ITableRef",
    "ITriggerRef",
    "IUsageProfileRef",
    "IWorkflowRef",
    "IdentityCenterConfigurationReference",
    "IntegrationReference",
    "IntegrationResourcePropertyReference",
    "JobReference",
    "MLTransformReference",
    "PartitionReference",
    "RegistryReference",
    "SchemaReference",
    "SchemaVersionMetadataReference",
    "SchemaVersionReference",
    "SecurityConfigurationReference",
    "TableOptimizerReference",
    "TableReference",
    "TriggerReference",
    "UsageProfileReference",
    "WorkflowReference",
]

publication.publish()

def _typecheckingstub__153075acc355fb8c67c2595f86bb736959d7a3490470e1496c4634652a073e55(
    *,
    classifier_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0c23f5314f51a17152319ab80f389d2f1b18975384c84d1d2931ac1a3121d9f(
    *,
    connection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad53740eb8897f033af56fd03963af3e4f644f727baf57ca71c35961fceb97b6(
    *,
    crawler_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2752daff245d03b65a99c918eff72a3eb4c7c58fc56a5bf622d9117515921d7f(
    *,
    custom_entity_type_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824f5a564c0864f04cf9c7b44937b6e5dbe2d9acb8bd8b048f28e3b1f667a924(
    *,
    data_catalog_encryption_settings_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__637b7e752aad4e64a85b4673d0fd9fbde33283ca6452dac108809ad38887f3cd(
    *,
    data_quality_ruleset_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b006942e6851e8e5b67ab80d761f762e021506f9975b704097cc0df559962e7e(
    *,
    database_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__050454acd533b9c974358b1bfdec6277e66592a87a752610c62dc6b896b95d0f(
    *,
    endpoint_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dce890d13c4e501fd50bfd966cbe5558eac1e8b2415bc6f873c45a675fef0455(
    *,
    account_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__487ef973bf980b9533ab5e35911c785df93801badcd04a6ad9191c32ce95e300(
    *,
    integration_arn: builtins.str,
    integration_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d78e927b289090d3ea11c2e52f58b5cdc45b50ebf0cb9ac19af7a86759d45975(
    *,
    resource_arn: builtins.str,
    resource_property_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8c47c403cca6462755fa024cf63a9b8531d52ca6834543a739c13e8ee51c9e9(
    *,
    job_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3f1a2f7b4f39bcc3b7be922b88fffd5ccf9f63df878ae375f85fa00250d7cff(
    *,
    ml_transform_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a9698059eb8899c746fb237350793d2faff1bdfa61b71f202add91131734519(
    *,
    partition_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f46875075b9b44d3958fe5be64778d351238ba406d2bfaf624a127c572ecfdd(
    *,
    registry_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b578c469d6ed870abb6802e9d10670c2f571c62a79988a4ded4d3dccbcf0754e(
    *,
    schema_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4b127790a6c1e064bc511d8914a963c65c84be0739a54f9274fdb48b4f2105d(
    *,
    key: builtins.str,
    schema_version_id: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8183bbaf7cbe72ac30393afbba3db6508105f9305b6e69bf1acef9abffd833d2(
    *,
    version_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f762055d8744dcdcadf6d3ee48e027edbbedb409f2aee69d69051529ab7d003(
    *,
    security_configuration_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36d18932d532cd2df3f2355353c78a3d21a028fa0d2181f51b94ae7c9101726b(
    *,
    table_optimizer_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d91e1bc0dff8ee618900793d998bcf5ed91fd48153fcbcc02d63186fa2219535(
    *,
    table_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85c96b93a2c298c01219667b5012a8e417cd40c14e36afd3fd093081bbfc5a3e(
    *,
    trigger_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31cd7baf9c81bae2e0d29221ca6cf6bf1b06b730a8c9d8fedf8630e653710373(
    *,
    usage_profile_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05490662a534e7ac737a01a3e54258abf2c5d6dd3a563391b841bd656b5b6220(
    *,
    workflow_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IClassifierRef, IConnectionRef, ICrawlerRef, ICustomEntityTypeRef, IDataCatalogEncryptionSettingsRef, IDataQualityRulesetRef, IDatabaseRef, IDevEndpointRef, IIdentityCenterConfigurationRef, IIntegrationRef, IIntegrationResourcePropertyRef, IJobRef, IMLTransformRef, IPartitionRef, IRegistryRef, ISchemaRef, ISchemaVersionMetadataRef, ISchemaVersionRef, ISecurityConfigurationRef, ITableOptimizerRef, ITableRef, ITriggerRef, IUsageProfileRef, IWorkflowRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
