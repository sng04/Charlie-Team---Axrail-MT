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
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.DataCellsFilterReference",
    jsii_struct_bases=[],
    name_mapping={
        "database_name": "databaseName",
        "data_cells_filter_name": "dataCellsFilterName",
        "table_catalog_id": "tableCatalogId",
        "table_name": "tableName",
    },
)
class DataCellsFilterReference:
    def __init__(
        self,
        *,
        database_name: builtins.str,
        data_cells_filter_name: builtins.str,
        table_catalog_id: builtins.str,
        table_name: builtins.str,
    ) -> None:
        '''A reference to a DataCellsFilter resource.

        :param database_name: The DatabaseName of the DataCellsFilter resource.
        :param data_cells_filter_name: The Name of the DataCellsFilter resource.
        :param table_catalog_id: The TableCatalogId of the DataCellsFilter resource.
        :param table_name: The TableName of the DataCellsFilter resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lakeformation as interfaces_lakeformation
            
            data_cells_filter_reference = interfaces_lakeformation.DataCellsFilterReference(
                database_name="databaseName",
                data_cells_filter_name="dataCellsFilterName",
                table_catalog_id="tableCatalogId",
                table_name="tableName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4481235e03c692964bec4e715dcfcea0a2dec7424d50d8336843422e15d0a299)
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument data_cells_filter_name", value=data_cells_filter_name, expected_type=type_hints["data_cells_filter_name"])
            check_type(argname="argument table_catalog_id", value=table_catalog_id, expected_type=type_hints["table_catalog_id"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_name": database_name,
            "data_cells_filter_name": data_cells_filter_name,
            "table_catalog_id": table_catalog_id,
            "table_name": table_name,
        }

    @builtins.property
    def database_name(self) -> builtins.str:
        '''The DatabaseName of the DataCellsFilter resource.'''
        result = self._values.get("database_name")
        assert result is not None, "Required property 'database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_cells_filter_name(self) -> builtins.str:
        '''The Name of the DataCellsFilter resource.'''
        result = self._values.get("data_cells_filter_name")
        assert result is not None, "Required property 'data_cells_filter_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_catalog_id(self) -> builtins.str:
        '''The TableCatalogId of the DataCellsFilter resource.'''
        result = self._values.get("table_catalog_id")
        assert result is not None, "Required property 'table_catalog_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_name(self) -> builtins.str:
        '''The TableName of the DataCellsFilter resource.'''
        result = self._values.get("table_name")
        assert result is not None, "Required property 'table_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataCellsFilterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.DataLakeSettingsReference",
    jsii_struct_bases=[],
    name_mapping={"data_lake_settings_id": "dataLakeSettingsId"},
)
class DataLakeSettingsReference:
    def __init__(self, *, data_lake_settings_id: builtins.str) -> None:
        '''A reference to a DataLakeSettings resource.

        :param data_lake_settings_id: The Id of the DataLakeSettings resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lakeformation as interfaces_lakeformation
            
            data_lake_settings_reference = interfaces_lakeformation.DataLakeSettingsReference(
                data_lake_settings_id="dataLakeSettingsId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbf7837c830af141c706ded9c4ec48a8571b2af65cdb877c8c2cc4bd128c065c)
            check_type(argname="argument data_lake_settings_id", value=data_lake_settings_id, expected_type=type_hints["data_lake_settings_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_lake_settings_id": data_lake_settings_id,
        }

    @builtins.property
    def data_lake_settings_id(self) -> builtins.str:
        '''The Id of the DataLakeSettings resource.'''
        result = self._values.get("data_lake_settings_id")
        assert result is not None, "Required property 'data_lake_settings_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataLakeSettingsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.IDataCellsFilterRef"
)
class IDataCellsFilterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataCellsFilter.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataCellsFilterRef")
    def data_cells_filter_ref(self) -> "DataCellsFilterReference":
        '''(experimental) A reference to a DataCellsFilter resource.

        :stability: experimental
        '''
        ...


class _IDataCellsFilterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataCellsFilter.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lakeformation.IDataCellsFilterRef"

    @builtins.property
    @jsii.member(jsii_name="dataCellsFilterRef")
    def data_cells_filter_ref(self) -> "DataCellsFilterReference":
        '''(experimental) A reference to a DataCellsFilter resource.

        :stability: experimental
        '''
        return typing.cast("DataCellsFilterReference", jsii.get(self, "dataCellsFilterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataCellsFilterRef).__jsii_proxy_class__ = lambda : _IDataCellsFilterRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.IDataLakeSettingsRef"
)
class IDataLakeSettingsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a DataLakeSettings.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="dataLakeSettingsRef")
    def data_lake_settings_ref(self) -> "DataLakeSettingsReference":
        '''(experimental) A reference to a DataLakeSettings resource.

        :stability: experimental
        '''
        ...


class _IDataLakeSettingsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a DataLakeSettings.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lakeformation.IDataLakeSettingsRef"

    @builtins.property
    @jsii.member(jsii_name="dataLakeSettingsRef")
    def data_lake_settings_ref(self) -> "DataLakeSettingsReference":
        '''(experimental) A reference to a DataLakeSettings resource.

        :stability: experimental
        '''
        return typing.cast("DataLakeSettingsReference", jsii.get(self, "dataLakeSettingsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDataLakeSettingsRef).__jsii_proxy_class__ = lambda : _IDataLakeSettingsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.IPermissionsRef")
class IPermissionsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Permissions.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="permissionsRef")
    def permissions_ref(self) -> "PermissionsReference":
        '''(experimental) A reference to a Permissions resource.

        :stability: experimental
        '''
        ...


class _IPermissionsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Permissions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lakeformation.IPermissionsRef"

    @builtins.property
    @jsii.member(jsii_name="permissionsRef")
    def permissions_ref(self) -> "PermissionsReference":
        '''(experimental) A reference to a Permissions resource.

        :stability: experimental
        '''
        return typing.cast("PermissionsReference", jsii.get(self, "permissionsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPermissionsRef).__jsii_proxy_class__ = lambda : _IPermissionsRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.IPrincipalPermissionsRef"
)
class IPrincipalPermissionsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PrincipalPermissions.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="principalPermissionsRef")
    def principal_permissions_ref(self) -> "PrincipalPermissionsReference":
        '''(experimental) A reference to a PrincipalPermissions resource.

        :stability: experimental
        '''
        ...


class _IPrincipalPermissionsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PrincipalPermissions.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lakeformation.IPrincipalPermissionsRef"

    @builtins.property
    @jsii.member(jsii_name="principalPermissionsRef")
    def principal_permissions_ref(self) -> "PrincipalPermissionsReference":
        '''(experimental) A reference to a PrincipalPermissions resource.

        :stability: experimental
        '''
        return typing.cast("PrincipalPermissionsReference", jsii.get(self, "principalPermissionsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrincipalPermissionsRef).__jsii_proxy_class__ = lambda : _IPrincipalPermissionsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.IResourceRef")
class IResourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Resource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="resourceRef")
    def resource_ref(self) -> "ResourceReference":
        '''(experimental) A reference to a Resource resource.

        :stability: experimental
        '''
        ...


class _IResourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Resource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lakeformation.IResourceRef"

    @builtins.property
    @jsii.member(jsii_name="resourceRef")
    def resource_ref(self) -> "ResourceReference":
        '''(experimental) A reference to a Resource resource.

        :stability: experimental
        '''
        return typing.cast("ResourceReference", jsii.get(self, "resourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IResourceRef).__jsii_proxy_class__ = lambda : _IResourceRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.ITagAssociationRef"
)
class ITagAssociationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TagAssociation.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tagAssociationRef")
    def tag_association_ref(self) -> "TagAssociationReference":
        '''(experimental) A reference to a TagAssociation resource.

        :stability: experimental
        '''
        ...


class _ITagAssociationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TagAssociation.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lakeformation.ITagAssociationRef"

    @builtins.property
    @jsii.member(jsii_name="tagAssociationRef")
    def tag_association_ref(self) -> "TagAssociationReference":
        '''(experimental) A reference to a TagAssociation resource.

        :stability: experimental
        '''
        return typing.cast("TagAssociationReference", jsii.get(self, "tagAssociationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITagAssociationRef).__jsii_proxy_class__ = lambda : _ITagAssociationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.ITagRef")
class ITagRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Tag.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tagRef")
    def tag_ref(self) -> "TagReference":
        '''(experimental) A reference to a Tag resource.

        :stability: experimental
        '''
        ...


class _ITagRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Tag.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_lakeformation.ITagRef"

    @builtins.property
    @jsii.member(jsii_name="tagRef")
    def tag_ref(self) -> "TagReference":
        '''(experimental) A reference to a Tag resource.

        :stability: experimental
        '''
        return typing.cast("TagReference", jsii.get(self, "tagRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITagRef).__jsii_proxy_class__ = lambda : _ITagRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.PermissionsReference",
    jsii_struct_bases=[],
    name_mapping={"permissions_id": "permissionsId"},
)
class PermissionsReference:
    def __init__(self, *, permissions_id: builtins.str) -> None:
        '''A reference to a Permissions resource.

        :param permissions_id: The Id of the Permissions resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lakeformation as interfaces_lakeformation
            
            permissions_reference = interfaces_lakeformation.PermissionsReference(
                permissions_id="permissionsId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be8547b28182f3cda5ad6898330f8f395c9f75ad41a66d0a0b957cb2ddbd8e50)
            check_type(argname="argument permissions_id", value=permissions_id, expected_type=type_hints["permissions_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "permissions_id": permissions_id,
        }

    @builtins.property
    def permissions_id(self) -> builtins.str:
        '''The Id of the Permissions resource.'''
        result = self._values.get("permissions_id")
        assert result is not None, "Required property 'permissions_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PermissionsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.PrincipalPermissionsReference",
    jsii_struct_bases=[],
    name_mapping={
        "principal_identifier": "principalIdentifier",
        "resource_identifier": "resourceIdentifier",
    },
)
class PrincipalPermissionsReference:
    def __init__(
        self,
        *,
        principal_identifier: builtins.str,
        resource_identifier: builtins.str,
    ) -> None:
        '''A reference to a PrincipalPermissions resource.

        :param principal_identifier: The PrincipalIdentifier of the PrincipalPermissions resource.
        :param resource_identifier: The ResourceIdentifier of the PrincipalPermissions resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lakeformation as interfaces_lakeformation
            
            principal_permissions_reference = interfaces_lakeformation.PrincipalPermissionsReference(
                principal_identifier="principalIdentifier",
                resource_identifier="resourceIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6387bb91585adb01e0b1beffddec28918e8b362da3c33efa10aeb17d81b5a3a0)
            check_type(argname="argument principal_identifier", value=principal_identifier, expected_type=type_hints["principal_identifier"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "principal_identifier": principal_identifier,
            "resource_identifier": resource_identifier,
        }

    @builtins.property
    def principal_identifier(self) -> builtins.str:
        '''The PrincipalIdentifier of the PrincipalPermissions resource.'''
        result = self._values.get("principal_identifier")
        assert result is not None, "Required property 'principal_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_identifier(self) -> builtins.str:
        '''The ResourceIdentifier of the PrincipalPermissions resource.'''
        result = self._values.get("resource_identifier")
        assert result is not None, "Required property 'resource_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrincipalPermissionsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.ResourceReference",
    jsii_struct_bases=[],
    name_mapping={"resource_id": "resourceId"},
)
class ResourceReference:
    def __init__(self, *, resource_id: builtins.str) -> None:
        '''A reference to a Resource resource.

        :param resource_id: The Id of the Resource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lakeformation as interfaces_lakeformation
            
            resource_reference = interfaces_lakeformation.ResourceReference(
                resource_id="resourceId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a5cb670439a52924afee3c01504dd09fd4c58dbb3b8620f1f1eb2e44398b999)
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_id": resource_id,
        }

    @builtins.property
    def resource_id(self) -> builtins.str:
        '''The Id of the Resource resource.'''
        result = self._values.get("resource_id")
        assert result is not None, "Required property 'resource_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ResourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.TagAssociationReference",
    jsii_struct_bases=[],
    name_mapping={
        "resource_identifier": "resourceIdentifier",
        "tags_identifier": "tagsIdentifier",
    },
)
class TagAssociationReference:
    def __init__(
        self,
        *,
        resource_identifier: builtins.str,
        tags_identifier: builtins.str,
    ) -> None:
        '''A reference to a TagAssociation resource.

        :param resource_identifier: The ResourceIdentifier of the TagAssociation resource.
        :param tags_identifier: The TagsIdentifier of the TagAssociation resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lakeformation as interfaces_lakeformation
            
            tag_association_reference = interfaces_lakeformation.TagAssociationReference(
                resource_identifier="resourceIdentifier",
                tags_identifier="tagsIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e6e8c7f7355dd1eb98120b013e1964350550b4511df94ae37b2b7fcf09a4ae8)
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument tags_identifier", value=tags_identifier, expected_type=type_hints["tags_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_identifier": resource_identifier,
            "tags_identifier": tags_identifier,
        }

    @builtins.property
    def resource_identifier(self) -> builtins.str:
        '''The ResourceIdentifier of the TagAssociation resource.'''
        result = self._values.get("resource_identifier")
        assert result is not None, "Required property 'resource_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags_identifier(self) -> builtins.str:
        '''The TagsIdentifier of the TagAssociation resource.'''
        result = self._values.get("tags_identifier")
        assert result is not None, "Required property 'tags_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagAssociationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_lakeformation.TagReference",
    jsii_struct_bases=[],
    name_mapping={"tag_key": "tagKey"},
)
class TagReference:
    def __init__(self, *, tag_key: builtins.str) -> None:
        '''A reference to a Tag resource.

        :param tag_key: The TagKey of the Tag resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_lakeformation as interfaces_lakeformation
            
            tag_reference = interfaces_lakeformation.TagReference(
                tag_key="tagKey"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9f042d5200978030ff397c34b5f15a045eb40ddd0893b7322f1f28655d48010)
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "tag_key": tag_key,
        }

    @builtins.property
    def tag_key(self) -> builtins.str:
        '''The TagKey of the Tag resource.'''
        result = self._values.get("tag_key")
        assert result is not None, "Required property 'tag_key' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "DataCellsFilterReference",
    "DataLakeSettingsReference",
    "IDataCellsFilterRef",
    "IDataLakeSettingsRef",
    "IPermissionsRef",
    "IPrincipalPermissionsRef",
    "IResourceRef",
    "ITagAssociationRef",
    "ITagRef",
    "PermissionsReference",
    "PrincipalPermissionsReference",
    "ResourceReference",
    "TagAssociationReference",
    "TagReference",
]

publication.publish()

def _typecheckingstub__4481235e03c692964bec4e715dcfcea0a2dec7424d50d8336843422e15d0a299(
    *,
    database_name: builtins.str,
    data_cells_filter_name: builtins.str,
    table_catalog_id: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbf7837c830af141c706ded9c4ec48a8571b2af65cdb877c8c2cc4bd128c065c(
    *,
    data_lake_settings_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be8547b28182f3cda5ad6898330f8f395c9f75ad41a66d0a0b957cb2ddbd8e50(
    *,
    permissions_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6387bb91585adb01e0b1beffddec28918e8b362da3c33efa10aeb17d81b5a3a0(
    *,
    principal_identifier: builtins.str,
    resource_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a5cb670439a52924afee3c01504dd09fd4c58dbb3b8620f1f1eb2e44398b999(
    *,
    resource_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e6e8c7f7355dd1eb98120b013e1964350550b4511df94ae37b2b7fcf09a4ae8(
    *,
    resource_identifier: builtins.str,
    tags_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9f042d5200978030ff397c34b5f15a045eb40ddd0893b7322f1f28655d48010(
    *,
    tag_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IDataCellsFilterRef, IDataLakeSettingsRef, IPermissionsRef, IPrincipalPermissionsRef, IResourceRef, ITagAssociationRef, ITagRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
