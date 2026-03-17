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
    jsii_type="aws-cdk-lib.interfaces.aws_memorydb.ACLReference",
    jsii_struct_bases=[],
    name_mapping={"acl_arn": "aclArn", "acl_name": "aclName"},
)
class ACLReference:
    def __init__(self, *, acl_arn: builtins.str, acl_name: builtins.str) -> None:
        '''A reference to a ACL resource.

        :param acl_arn: The ARN of the ACL resource.
        :param acl_name: The ACLName of the ACL resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_memorydb as interfaces_memorydb
            
            a_cLReference = interfaces_memorydb.ACLReference(
                acl_arn="aclArn",
                acl_name="aclName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__982f28c3a9b42816be0816db50a9f6523de8c69c56f49ca86ab1dee0afc8dbcc)
            check_type(argname="argument acl_arn", value=acl_arn, expected_type=type_hints["acl_arn"])
            check_type(argname="argument acl_name", value=acl_name, expected_type=type_hints["acl_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acl_arn": acl_arn,
            "acl_name": acl_name,
        }

    @builtins.property
    def acl_arn(self) -> builtins.str:
        '''The ARN of the ACL resource.'''
        result = self._values.get("acl_arn")
        assert result is not None, "Required property 'acl_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def acl_name(self) -> builtins.str:
        '''The ACLName of the ACL resource.'''
        result = self._values.get("acl_name")
        assert result is not None, "Required property 'acl_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ACLReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_memorydb.ClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn", "cluster_name": "clusterName"},
)
class ClusterReference:
    def __init__(
        self,
        *,
        cluster_arn: builtins.str,
        cluster_name: builtins.str,
    ) -> None:
        '''A reference to a Cluster resource.

        :param cluster_arn: The ARN of the Cluster resource.
        :param cluster_name: The ClusterName of the Cluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_memorydb as interfaces_memorydb
            
            cluster_reference = interfaces_memorydb.ClusterReference(
                cluster_arn="clusterArn",
                cluster_name="clusterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3deef1425782efff9b4d98e66cec56c0c0150df563370d932f95306adc751eb9)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
            "cluster_name": cluster_name,
        }

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The ARN of the Cluster resource.'''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The ClusterName of the Cluster resource.'''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_memorydb.IACLRef")
class IACLRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ACL.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="aclRef")
    def acl_ref(self) -> "ACLReference":
        '''(experimental) A reference to a ACL resource.

        :stability: experimental
        '''
        ...


class _IACLRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ACL.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_memorydb.IACLRef"

    @builtins.property
    @jsii.member(jsii_name="aclRef")
    def acl_ref(self) -> "ACLReference":
        '''(experimental) A reference to a ACL resource.

        :stability: experimental
        '''
        return typing.cast("ACLReference", jsii.get(self, "aclRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IACLRef).__jsii_proxy_class__ = lambda : _IACLRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_memorydb.IClusterRef")
class IClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Cluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        ...


class _IClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Cluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_memorydb.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_memorydb.IMultiRegionClusterRef")
class IMultiRegionClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a MultiRegionCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="multiRegionClusterRef")
    def multi_region_cluster_ref(self) -> "MultiRegionClusterReference":
        '''(experimental) A reference to a MultiRegionCluster resource.

        :stability: experimental
        '''
        ...


class _IMultiRegionClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a MultiRegionCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_memorydb.IMultiRegionClusterRef"

    @builtins.property
    @jsii.member(jsii_name="multiRegionClusterRef")
    def multi_region_cluster_ref(self) -> "MultiRegionClusterReference":
        '''(experimental) A reference to a MultiRegionCluster resource.

        :stability: experimental
        '''
        return typing.cast("MultiRegionClusterReference", jsii.get(self, "multiRegionClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMultiRegionClusterRef).__jsii_proxy_class__ = lambda : _IMultiRegionClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_memorydb.IParameterGroupRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_memorydb.IParameterGroupRef"

    @builtins.property
    @jsii.member(jsii_name="parameterGroupRef")
    def parameter_group_ref(self) -> "ParameterGroupReference":
        '''(experimental) A reference to a ParameterGroup resource.

        :stability: experimental
        '''
        return typing.cast("ParameterGroupReference", jsii.get(self, "parameterGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParameterGroupRef).__jsii_proxy_class__ = lambda : _IParameterGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_memorydb.ISubnetGroupRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_memorydb.ISubnetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="subnetGroupRef")
    def subnet_group_ref(self) -> "SubnetGroupReference":
        '''(experimental) A reference to a SubnetGroup resource.

        :stability: experimental
        '''
        return typing.cast("SubnetGroupReference", jsii.get(self, "subnetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubnetGroupRef).__jsii_proxy_class__ = lambda : _ISubnetGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_memorydb.IUserRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_memorydb.IUserRef"

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
    jsii_type="aws-cdk-lib.interfaces.aws_memorydb.MultiRegionClusterReference",
    jsii_struct_bases=[],
    name_mapping={
        "multi_region_cluster_arn": "multiRegionClusterArn",
        "multi_region_cluster_name": "multiRegionClusterName",
    },
)
class MultiRegionClusterReference:
    def __init__(
        self,
        *,
        multi_region_cluster_arn: builtins.str,
        multi_region_cluster_name: builtins.str,
    ) -> None:
        '''A reference to a MultiRegionCluster resource.

        :param multi_region_cluster_arn: The ARN of the MultiRegionCluster resource.
        :param multi_region_cluster_name: The MultiRegionClusterName of the MultiRegionCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_memorydb as interfaces_memorydb
            
            multi_region_cluster_reference = interfaces_memorydb.MultiRegionClusterReference(
                multi_region_cluster_arn="multiRegionClusterArn",
                multi_region_cluster_name="multiRegionClusterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75089b41f224535ca8b53af8adb788da8ab8d10bb872bc9a10a092a1a9c3b547)
            check_type(argname="argument multi_region_cluster_arn", value=multi_region_cluster_arn, expected_type=type_hints["multi_region_cluster_arn"])
            check_type(argname="argument multi_region_cluster_name", value=multi_region_cluster_name, expected_type=type_hints["multi_region_cluster_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "multi_region_cluster_arn": multi_region_cluster_arn,
            "multi_region_cluster_name": multi_region_cluster_name,
        }

    @builtins.property
    def multi_region_cluster_arn(self) -> builtins.str:
        '''The ARN of the MultiRegionCluster resource.'''
        result = self._values.get("multi_region_cluster_arn")
        assert result is not None, "Required property 'multi_region_cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def multi_region_cluster_name(self) -> builtins.str:
        '''The MultiRegionClusterName of the MultiRegionCluster resource.'''
        result = self._values.get("multi_region_cluster_name")
        assert result is not None, "Required property 'multi_region_cluster_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MultiRegionClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_memorydb.ParameterGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_group_arn": "parameterGroupArn",
        "parameter_group_name": "parameterGroupName",
    },
)
class ParameterGroupReference:
    def __init__(
        self,
        *,
        parameter_group_arn: builtins.str,
        parameter_group_name: builtins.str,
    ) -> None:
        '''A reference to a ParameterGroup resource.

        :param parameter_group_arn: The ARN of the ParameterGroup resource.
        :param parameter_group_name: The ParameterGroupName of the ParameterGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_memorydb as interfaces_memorydb
            
            parameter_group_reference = interfaces_memorydb.ParameterGroupReference(
                parameter_group_arn="parameterGroupArn",
                parameter_group_name="parameterGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4ce9a12bead66527ba95eaf76ca4ea36b47fd939e732e4960545097be001fdb)
            check_type(argname="argument parameter_group_arn", value=parameter_group_arn, expected_type=type_hints["parameter_group_arn"])
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_group_arn": parameter_group_arn,
            "parameter_group_name": parameter_group_name,
        }

    @builtins.property
    def parameter_group_arn(self) -> builtins.str:
        '''The ARN of the ParameterGroup resource.'''
        result = self._values.get("parameter_group_arn")
        assert result is not None, "Required property 'parameter_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameter_group_name(self) -> builtins.str:
        '''The ParameterGroupName of the ParameterGroup resource.'''
        result = self._values.get("parameter_group_name")
        assert result is not None, "Required property 'parameter_group_name' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_memorydb.SubnetGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "subnet_group_arn": "subnetGroupArn",
        "subnet_group_name": "subnetGroupName",
    },
)
class SubnetGroupReference:
    def __init__(
        self,
        *,
        subnet_group_arn: builtins.str,
        subnet_group_name: builtins.str,
    ) -> None:
        '''A reference to a SubnetGroup resource.

        :param subnet_group_arn: The ARN of the SubnetGroup resource.
        :param subnet_group_name: The SubnetGroupName of the SubnetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_memorydb as interfaces_memorydb
            
            subnet_group_reference = interfaces_memorydb.SubnetGroupReference(
                subnet_group_arn="subnetGroupArn",
                subnet_group_name="subnetGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__883529d4f6ed163d080574cce70282fa264bc95b899e5b38e34449540c227601)
            check_type(argname="argument subnet_group_arn", value=subnet_group_arn, expected_type=type_hints["subnet_group_arn"])
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnet_group_arn": subnet_group_arn,
            "subnet_group_name": subnet_group_name,
        }

    @builtins.property
    def subnet_group_arn(self) -> builtins.str:
        '''The ARN of the SubnetGroup resource.'''
        result = self._values.get("subnet_group_arn")
        assert result is not None, "Required property 'subnet_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_group_name(self) -> builtins.str:
        '''The SubnetGroupName of the SubnetGroup resource.'''
        result = self._values.get("subnet_group_name")
        assert result is not None, "Required property 'subnet_group_name' is missing"
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
    jsii_type="aws-cdk-lib.interfaces.aws_memorydb.UserReference",
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
            from aws_cdk.interfaces import aws_memorydb as interfaces_memorydb
            
            user_reference = interfaces_memorydb.UserReference(
                user_arn="userArn",
                user_name="userName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__203a6447b73a85638b9a88eb98c6073ff4f32f7b65519ff5e6d5f08d2da656ce)
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
    "ACLReference",
    "ClusterReference",
    "IACLRef",
    "IClusterRef",
    "IMultiRegionClusterRef",
    "IParameterGroupRef",
    "ISubnetGroupRef",
    "IUserRef",
    "MultiRegionClusterReference",
    "ParameterGroupReference",
    "SubnetGroupReference",
    "UserReference",
]

publication.publish()

def _typecheckingstub__982f28c3a9b42816be0816db50a9f6523de8c69c56f49ca86ab1dee0afc8dbcc(
    *,
    acl_arn: builtins.str,
    acl_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3deef1425782efff9b4d98e66cec56c0c0150df563370d932f95306adc751eb9(
    *,
    cluster_arn: builtins.str,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75089b41f224535ca8b53af8adb788da8ab8d10bb872bc9a10a092a1a9c3b547(
    *,
    multi_region_cluster_arn: builtins.str,
    multi_region_cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ce9a12bead66527ba95eaf76ca4ea36b47fd939e732e4960545097be001fdb(
    *,
    parameter_group_arn: builtins.str,
    parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883529d4f6ed163d080574cce70282fa264bc95b899e5b38e34449540c227601(
    *,
    subnet_group_arn: builtins.str,
    subnet_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__203a6447b73a85638b9a88eb98c6073ff4f32f7b65519ff5e6d5f08d2da656ce(
    *,
    user_arn: builtins.str,
    user_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IACLRef, IClusterRef, IMultiRegionClusterRef, IParameterGroupRef, ISubnetGroupRef, IUserRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
