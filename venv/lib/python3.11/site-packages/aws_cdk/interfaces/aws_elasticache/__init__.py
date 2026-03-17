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
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.CacheClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_name": "clusterName"},
)
class CacheClusterReference:
    def __init__(self, *, cluster_name: builtins.str) -> None:
        '''A reference to a CacheCluster resource.

        :param cluster_name: The ClusterName of the CacheCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticache as interfaces_elasticache
            
            cache_cluster_reference = interfaces_elasticache.CacheClusterReference(
                cluster_name="clusterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7fa7e3375e8ad9ab2e170d818c5ec8f7d2bde03d305b4be5f21f114bf0b3e9b)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_name": cluster_name,
        }

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The ClusterName of the CacheCluster resource.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CacheClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.GlobalReplicationGroupReference",
    jsii_struct_bases=[],
    name_mapping={"global_replication_group_id": "globalReplicationGroupId"},
)
class GlobalReplicationGroupReference:
    def __init__(self, *, global_replication_group_id: builtins.str) -> None:
        '''A reference to a GlobalReplicationGroup resource.

        :param global_replication_group_id: The GlobalReplicationGroupId of the GlobalReplicationGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticache as interfaces_elasticache
            
            global_replication_group_reference = interfaces_elasticache.GlobalReplicationGroupReference(
                global_replication_group_id="globalReplicationGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1110cc555afddf2d94b13f3aa1ac1afa10f65e8907104e13f6b902a4643d6894)
            check_type(argname="argument global_replication_group_id", value=global_replication_group_id, expected_type=type_hints["global_replication_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "global_replication_group_id": global_replication_group_id,
        }

    @builtins.property
    def global_replication_group_id(self) -> builtins.str:
        '''The GlobalReplicationGroupId of the GlobalReplicationGroup resource.'''
        result = self._values.get("global_replication_group_id")
        assert result is not None, "Required property 'global_replication_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GlobalReplicationGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_elasticache.ICacheClusterRef")
class ICacheClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CacheCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="cacheClusterRef")
    def cache_cluster_ref(self) -> "CacheClusterReference":
        '''(experimental) A reference to a CacheCluster resource.

        :stability: experimental
        '''
        ...


class _ICacheClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CacheCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticache.ICacheClusterRef"

    @builtins.property
    @jsii.member(jsii_name="cacheClusterRef")
    def cache_cluster_ref(self) -> "CacheClusterReference":
        '''(experimental) A reference to a CacheCluster resource.

        :stability: experimental
        '''
        return typing.cast("CacheClusterReference", jsii.get(self, "cacheClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICacheClusterRef).__jsii_proxy_class__ = lambda : _ICacheClusterRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.IGlobalReplicationGroupRef"
)
class IGlobalReplicationGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalReplicationGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupRef")
    def global_replication_group_ref(self) -> "GlobalReplicationGroupReference":
        '''(experimental) A reference to a GlobalReplicationGroup resource.

        :stability: experimental
        '''
        ...


class _IGlobalReplicationGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a GlobalReplicationGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticache.IGlobalReplicationGroupRef"

    @builtins.property
    @jsii.member(jsii_name="globalReplicationGroupRef")
    def global_replication_group_ref(self) -> "GlobalReplicationGroupReference":
        '''(experimental) A reference to a GlobalReplicationGroup resource.

        :stability: experimental
        '''
        return typing.cast("GlobalReplicationGroupReference", jsii.get(self, "globalReplicationGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGlobalReplicationGroupRef).__jsii_proxy_class__ = lambda : _IGlobalReplicationGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_elasticache.IParameterGroupRef")
class IParameterGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ParameterGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="parameterGroupRef")
    def parameter_group_ref(self) -> "ParameterGroupReference":
        '''(experimental) A reference to a ParameterGroup resource.

        :stability: experimental
        '''
        ...


class _IParameterGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ParameterGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticache.IParameterGroupRef"

    @builtins.property
    @jsii.member(jsii_name="parameterGroupRef")
    def parameter_group_ref(self) -> "ParameterGroupReference":
        '''(experimental) A reference to a ParameterGroup resource.

        :stability: experimental
        '''
        return typing.cast("ParameterGroupReference", jsii.get(self, "parameterGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParameterGroupRef).__jsii_proxy_class__ = lambda : _IParameterGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.IReplicationGroupRef"
)
class IReplicationGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="replicationGroupRef")
    def replication_group_ref(self) -> "ReplicationGroupReference":
        '''(experimental) A reference to a ReplicationGroup resource.

        :stability: experimental
        '''
        ...


class _IReplicationGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReplicationGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticache.IReplicationGroupRef"

    @builtins.property
    @jsii.member(jsii_name="replicationGroupRef")
    def replication_group_ref(self) -> "ReplicationGroupReference":
        '''(experimental) A reference to a ReplicationGroup resource.

        :stability: experimental
        '''
        return typing.cast("ReplicationGroupReference", jsii.get(self, "replicationGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReplicationGroupRef).__jsii_proxy_class__ = lambda : _IReplicationGroupRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.ISecurityGroupIngressRef"
)
class ISecurityGroupIngressRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroupIngress.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityGroupIngressRef")
    def security_group_ingress_ref(self) -> "SecurityGroupIngressReference":
        '''(experimental) A reference to a SecurityGroupIngress resource.

        :stability: experimental
        '''
        ...


class _ISecurityGroupIngressRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroupIngress.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticache.ISecurityGroupIngressRef"

    @builtins.property
    @jsii.member(jsii_name="securityGroupIngressRef")
    def security_group_ingress_ref(self) -> "SecurityGroupIngressReference":
        '''(experimental) A reference to a SecurityGroupIngress resource.

        :stability: experimental
        '''
        return typing.cast("SecurityGroupIngressReference", jsii.get(self, "securityGroupIngressRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityGroupIngressRef).__jsii_proxy_class__ = lambda : _ISecurityGroupIngressRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_elasticache.ISecurityGroupRef")
class ISecurityGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="securityGroupRef")
    def security_group_ref(self) -> "SecurityGroupReference":
        '''(experimental) A reference to a SecurityGroup resource.

        :stability: experimental
        '''
        ...


class _ISecurityGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SecurityGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticache.ISecurityGroupRef"

    @builtins.property
    @jsii.member(jsii_name="securityGroupRef")
    def security_group_ref(self) -> "SecurityGroupReference":
        '''(experimental) A reference to a SecurityGroup resource.

        :stability: experimental
        '''
        return typing.cast("SecurityGroupReference", jsii.get(self, "securityGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISecurityGroupRef).__jsii_proxy_class__ = lambda : _ISecurityGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_elasticache.IServerlessCacheRef")
class IServerlessCacheRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServerlessCache.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serverlessCacheRef")
    def serverless_cache_ref(self) -> "ServerlessCacheReference":
        '''(experimental) A reference to a ServerlessCache resource.

        :stability: experimental
        '''
        ...


class _IServerlessCacheRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServerlessCache.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticache.IServerlessCacheRef"

    @builtins.property
    @jsii.member(jsii_name="serverlessCacheRef")
    def serverless_cache_ref(self) -> "ServerlessCacheReference":
        '''(experimental) A reference to a ServerlessCache resource.

        :stability: experimental
        '''
        return typing.cast("ServerlessCacheReference", jsii.get(self, "serverlessCacheRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServerlessCacheRef).__jsii_proxy_class__ = lambda : _IServerlessCacheRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_elasticache.ISubnetGroupRef")
class ISubnetGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SubnetGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="subnetGroupRef")
    def subnet_group_ref(self) -> "SubnetGroupReference":
        '''(experimental) A reference to a SubnetGroup resource.

        :stability: experimental
        '''
        ...


class _ISubnetGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SubnetGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticache.ISubnetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="subnetGroupRef")
    def subnet_group_ref(self) -> "SubnetGroupReference":
        '''(experimental) A reference to a SubnetGroup resource.

        :stability: experimental
        '''
        return typing.cast("SubnetGroupReference", jsii.get(self, "subnetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubnetGroupRef).__jsii_proxy_class__ = lambda : _ISubnetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_elasticache.IUserGroupRef")
class IUserGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a UserGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userGroupRef")
    def user_group_ref(self) -> "UserGroupReference":
        '''(experimental) A reference to a UserGroup resource.

        :stability: experimental
        '''
        ...


class _IUserGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a UserGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticache.IUserGroupRef"

    @builtins.property
    @jsii.member(jsii_name="userGroupRef")
    def user_group_ref(self) -> "UserGroupReference":
        '''(experimental) A reference to a UserGroup resource.

        :stability: experimental
        '''
        return typing.cast("UserGroupReference", jsii.get(self, "userGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserGroupRef).__jsii_proxy_class__ = lambda : _IUserGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_elasticache.IUserRef")
class IUserRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a User.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="userRef")
    def user_ref(self) -> "UserReference":
        '''(experimental) A reference to a User resource.

        :stability: experimental
        '''
        ...


class _IUserRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a User.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticache.IUserRef"

    @builtins.property
    @jsii.member(jsii_name="userRef")
    def user_ref(self) -> "UserReference":
        '''(experimental) A reference to a User resource.

        :stability: experimental
        '''
        return typing.cast("UserReference", jsii.get(self, "userRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IUserRef).__jsii_proxy_class__ = lambda : _IUserRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.ParameterGroupReference",
    jsii_struct_bases=[],
    name_mapping={"cache_parameter_group_name": "cacheParameterGroupName"},
)
class ParameterGroupReference:
    def __init__(self, *, cache_parameter_group_name: builtins.str) -> None:
        '''A reference to a ParameterGroup resource.

        :param cache_parameter_group_name: The CacheParameterGroupName of the ParameterGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticache as interfaces_elasticache
            
            parameter_group_reference = interfaces_elasticache.ParameterGroupReference(
                cache_parameter_group_name="cacheParameterGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eca65ea880b260aad6464c837598920044ffd8da7d0d1fef38a23c3e50049b3)
            check_type(argname="argument cache_parameter_group_name", value=cache_parameter_group_name, expected_type=type_hints["cache_parameter_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cache_parameter_group_name": cache_parameter_group_name,
        }

    @builtins.property
    def cache_parameter_group_name(self) -> builtins.str:
        '''The CacheParameterGroupName of the ParameterGroup resource.'''
        result = self._values.get("cache_parameter_group_name")
        assert result is not None, "Required property 'cache_parameter_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ParameterGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.ReplicationGroupReference",
    jsii_struct_bases=[],
    name_mapping={"replication_group_id": "replicationGroupId"},
)
class ReplicationGroupReference:
    def __init__(self, *, replication_group_id: builtins.str) -> None:
        '''A reference to a ReplicationGroup resource.

        :param replication_group_id: The ReplicationGroupId of the ReplicationGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticache as interfaces_elasticache
            
            replication_group_reference = interfaces_elasticache.ReplicationGroupReference(
                replication_group_id="replicationGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac21f93e3244bf3b28faf92f749d98bf4a6f689a52cbf892b72ae014468205da)
            check_type(argname="argument replication_group_id", value=replication_group_id, expected_type=type_hints["replication_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_group_id": replication_group_id,
        }

    @builtins.property
    def replication_group_id(self) -> builtins.str:
        '''The ReplicationGroupId of the ReplicationGroup resource.'''
        result = self._values.get("replication_group_id")
        assert result is not None, "Required property 'replication_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicationGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.SecurityGroupIngressReference",
    jsii_struct_bases=[],
    name_mapping={"security_group_ingress_id": "securityGroupIngressId"},
)
class SecurityGroupIngressReference:
    def __init__(self, *, security_group_ingress_id: builtins.str) -> None:
        '''A reference to a SecurityGroupIngress resource.

        :param security_group_ingress_id: The Id of the SecurityGroupIngress resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticache as interfaces_elasticache
            
            security_group_ingress_reference = interfaces_elasticache.SecurityGroupIngressReference(
                security_group_ingress_id="securityGroupIngressId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5cc2f20d59a04dd2db34bd06fad2d883d90a43eab7cc70a91b2bc99343bd3ba)
            check_type(argname="argument security_group_ingress_id", value=security_group_ingress_id, expected_type=type_hints["security_group_ingress_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_ingress_id": security_group_ingress_id,
        }

    @builtins.property
    def security_group_ingress_id(self) -> builtins.str:
        '''The Id of the SecurityGroupIngress resource.'''
        result = self._values.get("security_group_ingress_id")
        assert result is not None, "Required property 'security_group_ingress_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupIngressReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.SecurityGroupReference",
    jsii_struct_bases=[],
    name_mapping={"security_group_id": "securityGroupId"},
)
class SecurityGroupReference:
    def __init__(self, *, security_group_id: builtins.str) -> None:
        '''A reference to a SecurityGroup resource.

        :param security_group_id: The Id of the SecurityGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticache as interfaces_elasticache
            
            security_group_reference = interfaces_elasticache.SecurityGroupReference(
                security_group_id="securityGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edbac7e81bc0d56bfe5455ec2ba3a35ffb9f7106e31e26eeeb3cc5e36f1dfc73)
            check_type(argname="argument security_group_id", value=security_group_id, expected_type=type_hints["security_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_id": security_group_id,
        }

    @builtins.property
    def security_group_id(self) -> builtins.str:
        '''The Id of the SecurityGroup resource.'''
        result = self._values.get("security_group_id")
        assert result is not None, "Required property 'security_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SecurityGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.ServerlessCacheReference",
    jsii_struct_bases=[],
    name_mapping={
        "serverless_cache_arn": "serverlessCacheArn",
        "serverless_cache_name": "serverlessCacheName",
    },
)
class ServerlessCacheReference:
    def __init__(
        self,
        *,
        serverless_cache_arn: builtins.str,
        serverless_cache_name: builtins.str,
    ) -> None:
        '''A reference to a ServerlessCache resource.

        :param serverless_cache_arn: The ARN of the ServerlessCache resource.
        :param serverless_cache_name: The ServerlessCacheName of the ServerlessCache resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticache as interfaces_elasticache
            
            serverless_cache_reference = interfaces_elasticache.ServerlessCacheReference(
                serverless_cache_arn="serverlessCacheArn",
                serverless_cache_name="serverlessCacheName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c94aa82c079bf8158b72805daa60250c874d40f90102e5ebc270b618e66f0c26)
            check_type(argname="argument serverless_cache_arn", value=serverless_cache_arn, expected_type=type_hints["serverless_cache_arn"])
            check_type(argname="argument serverless_cache_name", value=serverless_cache_name, expected_type=type_hints["serverless_cache_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "serverless_cache_arn": serverless_cache_arn,
            "serverless_cache_name": serverless_cache_name,
        }

    @builtins.property
    def serverless_cache_arn(self) -> builtins.str:
        '''The ARN of the ServerlessCache resource.'''
        result = self._values.get("serverless_cache_arn")
        assert result is not None, "Required property 'serverless_cache_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def serverless_cache_name(self) -> builtins.str:
        '''The ServerlessCacheName of the ServerlessCache resource.'''
        result = self._values.get("serverless_cache_name")
        assert result is not None, "Required property 'serverless_cache_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerlessCacheReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.SubnetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"cache_subnet_group_name": "cacheSubnetGroupName"},
)
class SubnetGroupReference:
    def __init__(self, *, cache_subnet_group_name: builtins.str) -> None:
        '''A reference to a SubnetGroup resource.

        :param cache_subnet_group_name: The CacheSubnetGroupName of the SubnetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticache as interfaces_elasticache
            
            subnet_group_reference = interfaces_elasticache.SubnetGroupReference(
                cache_subnet_group_name="cacheSubnetGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd0edc5fe5c2fffc1f963bab957d3a470ad443c9f82256665eb5f6070e6ef81a)
            check_type(argname="argument cache_subnet_group_name", value=cache_subnet_group_name, expected_type=type_hints["cache_subnet_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cache_subnet_group_name": cache_subnet_group_name,
        }

    @builtins.property
    def cache_subnet_group_name(self) -> builtins.str:
        '''The CacheSubnetGroupName of the SubnetGroup resource.'''
        result = self._values.get("cache_subnet_group_name")
        assert result is not None, "Required property 'cache_subnet_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SubnetGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.UserGroupReference",
    jsii_struct_bases=[],
    name_mapping={"user_group_arn": "userGroupArn", "user_group_id": "userGroupId"},
)
class UserGroupReference:
    def __init__(
        self,
        *,
        user_group_arn: builtins.str,
        user_group_id: builtins.str,
    ) -> None:
        '''A reference to a UserGroup resource.

        :param user_group_arn: The ARN of the UserGroup resource.
        :param user_group_id: The UserGroupId of the UserGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticache as interfaces_elasticache
            
            user_group_reference = interfaces_elasticache.UserGroupReference(
                user_group_arn="userGroupArn",
                user_group_id="userGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c897b5f47bb454c979ac0b259e1b55b875a6cdd1ff3ff0bbd060c62ffaa03fb8)
            check_type(argname="argument user_group_arn", value=user_group_arn, expected_type=type_hints["user_group_arn"])
            check_type(argname="argument user_group_id", value=user_group_id, expected_type=type_hints["user_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_group_arn": user_group_arn,
            "user_group_id": user_group_id,
        }

    @builtins.property
    def user_group_arn(self) -> builtins.str:
        '''The ARN of the UserGroup resource.'''
        result = self._values.get("user_group_arn")
        assert result is not None, "Required property 'user_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_group_id(self) -> builtins.str:
        '''The UserGroupId of the UserGroup resource.'''
        result = self._values.get("user_group_id")
        assert result is not None, "Required property 'user_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticache.UserReference",
    jsii_struct_bases=[],
    name_mapping={"user_arn": "userArn", "user_name": "userName"},
)
class UserReference:
    def __init__(self, *, user_arn: builtins.str, user_name: builtins.str) -> None:
        '''A reference to a User resource.

        :param user_arn: The ARN of the User resource.
        :param user_name: The UserName of the User resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticache as interfaces_elasticache
            
            user_reference = interfaces_elasticache.UserReference(
                user_arn="userArn",
                user_name="userName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f5266f1a03ff8c36e332d77e256f7bd512f4776df1f9ef4e242fbab2df66185)
            check_type(argname="argument user_arn", value=user_arn, expected_type=type_hints["user_arn"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "user_arn": user_arn,
            "user_name": user_name,
        }

    @builtins.property
    def user_arn(self) -> builtins.str:
        '''The ARN of the User resource.'''
        result = self._values.get("user_arn")
        assert result is not None, "Required property 'user_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''The UserName of the User resource.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "UserReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CacheClusterReference",
    "GlobalReplicationGroupReference",
    "ICacheClusterRef",
    "IGlobalReplicationGroupRef",
    "IParameterGroupRef",
    "IReplicationGroupRef",
    "ISecurityGroupIngressRef",
    "ISecurityGroupRef",
    "IServerlessCacheRef",
    "ISubnetGroupRef",
    "IUserGroupRef",
    "IUserRef",
    "ParameterGroupReference",
    "ReplicationGroupReference",
    "SecurityGroupIngressReference",
    "SecurityGroupReference",
    "ServerlessCacheReference",
    "SubnetGroupReference",
    "UserGroupReference",
    "UserReference",
]

publication.publish()

def _typecheckingstub__e7fa7e3375e8ad9ab2e170d818c5ec8f7d2bde03d305b4be5f21f114bf0b3e9b(
    *,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1110cc555afddf2d94b13f3aa1ac1afa10f65e8907104e13f6b902a4643d6894(
    *,
    global_replication_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eca65ea880b260aad6464c837598920044ffd8da7d0d1fef38a23c3e50049b3(
    *,
    cache_parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac21f93e3244bf3b28faf92f749d98bf4a6f689a52cbf892b72ae014468205da(
    *,
    replication_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5cc2f20d59a04dd2db34bd06fad2d883d90a43eab7cc70a91b2bc99343bd3ba(
    *,
    security_group_ingress_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edbac7e81bc0d56bfe5455ec2ba3a35ffb9f7106e31e26eeeb3cc5e36f1dfc73(
    *,
    security_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c94aa82c079bf8158b72805daa60250c874d40f90102e5ebc270b618e66f0c26(
    *,
    serverless_cache_arn: builtins.str,
    serverless_cache_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd0edc5fe5c2fffc1f963bab957d3a470ad443c9f82256665eb5f6070e6ef81a(
    *,
    cache_subnet_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c897b5f47bb454c979ac0b259e1b55b875a6cdd1ff3ff0bbd060c62ffaa03fb8(
    *,
    user_group_arn: builtins.str,
    user_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f5266f1a03ff8c36e332d77e256f7bd512f4776df1f9ef4e242fbab2df66185(
    *,
    user_arn: builtins.str,
    user_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICacheClusterRef, IGlobalReplicationGroupRef, IParameterGroupRef, IReplicationGroupRef, ISecurityGroupIngressRef, ISecurityGroupRef, IServerlessCacheRef, ISubnetGroupRef, IUserGroupRef, IUserRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
