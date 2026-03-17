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
    jsii_type="aws-cdk-lib.interfaces.aws_dax.ClusterReference",
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
            from aws_cdk.interfaces import aws_dax as interfaces_dax
            
            cluster_reference = interfaces_dax.ClusterReference(
                cluster_arn="clusterArn",
                cluster_name="clusterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05406601d1a4f85ebaa2850ac9c6ac421d1ad692fb7d01bf8a326a3953f7e38b)
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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dax.IClusterRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dax.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dax.IParameterGroupRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dax.IParameterGroupRef"

    @builtins.property
    @jsii.member(jsii_name="parameterGroupRef")
    def parameter_group_ref(self) -> "ParameterGroupReference":
        '''(experimental) A reference to a ParameterGroup resource.

        :stability: experimental
        '''
        return typing.cast("ParameterGroupReference", jsii.get(self, "parameterGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IParameterGroupRef).__jsii_proxy_class__ = lambda : _IParameterGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dax.ISubnetGroupRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dax.ISubnetGroupRef"

    @builtins.property
    @jsii.member(jsii_name="subnetGroupRef")
    def subnet_group_ref(self) -> "SubnetGroupReference":
        '''(experimental) A reference to a SubnetGroup resource.

        :stability: experimental
        '''
        return typing.cast("SubnetGroupReference", jsii.get(self, "subnetGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISubnetGroupRef).__jsii_proxy_class__ = lambda : _ISubnetGroupRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dax.ParameterGroupReference",
    jsii_struct_bases=[],
    name_mapping={"parameter_group_name": "parameterGroupName"},
)
class ParameterGroupReference:
    def __init__(self, *, parameter_group_name: builtins.str) -> None:
        '''A reference to a ParameterGroup resource.

        :param parameter_group_name: The ParameterGroupName of the ParameterGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dax as interfaces_dax
            
            parameter_group_reference = interfaces_dax.ParameterGroupReference(
                parameter_group_name="parameterGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7df59dc4674887428e9aabb0ae3c8f44947489e82e8fc231fc079e8886664f1)
            check_type(argname="argument parameter_group_name", value=parameter_group_name, expected_type=type_hints["parameter_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "parameter_group_name": parameter_group_name,
        }

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
    jsii_type="aws-cdk-lib.interfaces.aws_dax.SubnetGroupReference",
    jsii_struct_bases=[],
    name_mapping={"subnet_group_name": "subnetGroupName"},
)
class SubnetGroupReference:
    def __init__(self, *, subnet_group_name: builtins.str) -> None:
        '''A reference to a SubnetGroup resource.

        :param subnet_group_name: The SubnetGroupName of the SubnetGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dax as interfaces_dax
            
            subnet_group_reference = interfaces_dax.SubnetGroupReference(
                subnet_group_name="subnetGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9a0c3f06e1935cdf153ef5db387147d3c9ee2f0e536009e9e281f2ae65366ed)
            check_type(argname="argument subnet_group_name", value=subnet_group_name, expected_type=type_hints["subnet_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnet_group_name": subnet_group_name,
        }

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


__all__ = [
    "ClusterReference",
    "IClusterRef",
    "IParameterGroupRef",
    "ISubnetGroupRef",
    "ParameterGroupReference",
    "SubnetGroupReference",
]

publication.publish()

def _typecheckingstub__05406601d1a4f85ebaa2850ac9c6ac421d1ad692fb7d01bf8a326a3953f7e38b(
    *,
    cluster_arn: builtins.str,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7df59dc4674887428e9aabb0ae3c8f44947489e82e8fc231fc079e8886664f1(
    *,
    parameter_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a0c3f06e1935cdf153ef5db387147d3c9ee2f0e536009e9e281f2ae65366ed(
    *,
    subnet_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IClusterRef, IParameterGroupRef, ISubnetGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
