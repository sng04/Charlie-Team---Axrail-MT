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
    jsii_type="aws-cdk-lib.interfaces.aws_codestarconnections.ConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"connection_arn": "connectionArn"},
)
class ConnectionReference:
    def __init__(self, *, connection_arn: builtins.str) -> None:
        '''A reference to a Connection resource.

        :param connection_arn: The ConnectionArn of the Connection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codestarconnections as interfaces_codestarconnections
            
            connection_reference = interfaces_codestarconnections.ConnectionReference(
                connection_arn="connectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa7c03d4047d1de6fb7d7dfd6a3d42a3deb3e714298c85a7ec3518a8a8848abe)
            check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_arn": connection_arn,
        }

    @builtins.property
    def connection_arn(self) -> builtins.str:
        '''The ConnectionArn of the Connection resource.'''
        result = self._values.get("connection_arn")
        assert result is not None, "Required property 'connection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_codestarconnections.IConnectionRef"
)
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codestarconnections.IConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="connectionRef")
    def connection_ref(self) -> "ConnectionReference":
        '''(experimental) A reference to a Connection resource.

        :stability: experimental
        '''
        return typing.cast("ConnectionReference", jsii.get(self, "connectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConnectionRef).__jsii_proxy_class__ = lambda : _IConnectionRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_codestarconnections.IRepositoryLinkRef"
)
class IRepositoryLinkRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RepositoryLink.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="repositoryLinkRef")
    def repository_link_ref(self) -> "RepositoryLinkReference":
        '''(experimental) A reference to a RepositoryLink resource.

        :stability: experimental
        '''
        ...


class _IRepositoryLinkRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RepositoryLink.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codestarconnections.IRepositoryLinkRef"

    @builtins.property
    @jsii.member(jsii_name="repositoryLinkRef")
    def repository_link_ref(self) -> "RepositoryLinkReference":
        '''(experimental) A reference to a RepositoryLink resource.

        :stability: experimental
        '''
        return typing.cast("RepositoryLinkReference", jsii.get(self, "repositoryLinkRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRepositoryLinkRef).__jsii_proxy_class__ = lambda : _IRepositoryLinkRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_codestarconnections.ISyncConfigurationRef"
)
class ISyncConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SyncConfiguration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="syncConfigurationRef")
    def sync_configuration_ref(self) -> "SyncConfigurationReference":
        '''(experimental) A reference to a SyncConfiguration resource.

        :stability: experimental
        '''
        ...


class _ISyncConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SyncConfiguration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codestarconnections.ISyncConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="syncConfigurationRef")
    def sync_configuration_ref(self) -> "SyncConfigurationReference":
        '''(experimental) A reference to a SyncConfiguration resource.

        :stability: experimental
        '''
        return typing.cast("SyncConfigurationReference", jsii.get(self, "syncConfigurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISyncConfigurationRef).__jsii_proxy_class__ = lambda : _ISyncConfigurationRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codestarconnections.RepositoryLinkReference",
    jsii_struct_bases=[],
    name_mapping={"repository_link_arn": "repositoryLinkArn"},
)
class RepositoryLinkReference:
    def __init__(self, *, repository_link_arn: builtins.str) -> None:
        '''A reference to a RepositoryLink resource.

        :param repository_link_arn: The RepositoryLinkArn of the RepositoryLink resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codestarconnections as interfaces_codestarconnections
            
            repository_link_reference = interfaces_codestarconnections.RepositoryLinkReference(
                repository_link_arn="repositoryLinkArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89e98e5aec86f800ef04bb639614932d787a843e687f0e7981d1344061d39296)
            check_type(argname="argument repository_link_arn", value=repository_link_arn, expected_type=type_hints["repository_link_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_link_arn": repository_link_arn,
        }

    @builtins.property
    def repository_link_arn(self) -> builtins.str:
        '''The RepositoryLinkArn of the RepositoryLink resource.'''
        result = self._values.get("repository_link_arn")
        assert result is not None, "Required property 'repository_link_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RepositoryLinkReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codestarconnections.SyncConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"resource_name": "resourceName", "sync_type": "syncType"},
)
class SyncConfigurationReference:
    def __init__(self, *, resource_name: builtins.str, sync_type: builtins.str) -> None:
        '''A reference to a SyncConfiguration resource.

        :param resource_name: The ResourceName of the SyncConfiguration resource.
        :param sync_type: The SyncType of the SyncConfiguration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codestarconnections as interfaces_codestarconnections
            
            sync_configuration_reference = interfaces_codestarconnections.SyncConfigurationReference(
                resource_name="resourceName",
                sync_type="syncType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91ec744db8b409d3c8a8f342ffefea82b15b9987bbcbcc3219e875872693a9af)
            check_type(argname="argument resource_name", value=resource_name, expected_type=type_hints["resource_name"])
            check_type(argname="argument sync_type", value=sync_type, expected_type=type_hints["sync_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "resource_name": resource_name,
            "sync_type": sync_type,
        }

    @builtins.property
    def resource_name(self) -> builtins.str:
        '''The ResourceName of the SyncConfiguration resource.'''
        result = self._values.get("resource_name")
        assert result is not None, "Required property 'resource_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sync_type(self) -> builtins.str:
        '''The SyncType of the SyncConfiguration resource.'''
        result = self._values.get("sync_type")
        assert result is not None, "Required property 'sync_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyncConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ConnectionReference",
    "IConnectionRef",
    "IRepositoryLinkRef",
    "ISyncConfigurationRef",
    "RepositoryLinkReference",
    "SyncConfigurationReference",
]

publication.publish()

def _typecheckingstub__aa7c03d4047d1de6fb7d7dfd6a3d42a3deb3e714298c85a7ec3518a8a8848abe(
    *,
    connection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89e98e5aec86f800ef04bb639614932d787a843e687f0e7981d1344061d39296(
    *,
    repository_link_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91ec744db8b409d3c8a8f342ffefea82b15b9987bbcbcc3219e875872693a9af(
    *,
    resource_name: builtins.str,
    sync_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IConnectionRef, IRepositoryLinkRef, ISyncConfigurationRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
