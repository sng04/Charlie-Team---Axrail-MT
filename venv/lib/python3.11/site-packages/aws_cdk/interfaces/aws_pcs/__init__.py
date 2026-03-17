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
    jsii_type="aws-cdk-lib.interfaces.aws_pcs.ClusterReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn"},
)
class ClusterReference:
    def __init__(self, *, cluster_arn: builtins.str) -> None:
        '''A reference to a Cluster resource.

        :param cluster_arn: The Arn of the Cluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pcs as interfaces_pcs
            
            cluster_reference = interfaces_pcs.ClusterReference(
                cluster_arn="clusterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f19eef432c5188a0ea3df59cb28218513cb898ba2b6490710346045af4d929e)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
        }

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The Arn of the Cluster resource.'''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pcs.ComputeNodeGroupReference",
    jsii_struct_bases=[],
    name_mapping={"compute_node_group_arn": "computeNodeGroupArn"},
)
class ComputeNodeGroupReference:
    def __init__(self, *, compute_node_group_arn: builtins.str) -> None:
        '''A reference to a ComputeNodeGroup resource.

        :param compute_node_group_arn: The Arn of the ComputeNodeGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pcs as interfaces_pcs
            
            compute_node_group_reference = interfaces_pcs.ComputeNodeGroupReference(
                compute_node_group_arn="computeNodeGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__524904a7f4260417adac262fff3ddc56e72d2b5ccf1e9d50a2d872ef61450f4e)
            check_type(argname="argument compute_node_group_arn", value=compute_node_group_arn, expected_type=type_hints["compute_node_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "compute_node_group_arn": compute_node_group_arn,
        }

    @builtins.property
    def compute_node_group_arn(self) -> builtins.str:
        '''The Arn of the ComputeNodeGroup resource.'''
        result = self._values.get("compute_node_group_arn")
        assert result is not None, "Required property 'compute_node_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeNodeGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pcs.IClusterRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pcs.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pcs.IComputeNodeGroupRef")
class IComputeNodeGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ComputeNodeGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="computeNodeGroupRef")
    def compute_node_group_ref(self) -> "ComputeNodeGroupReference":
        '''(experimental) A reference to a ComputeNodeGroup resource.

        :stability: experimental
        '''
        ...


class _IComputeNodeGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ComputeNodeGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pcs.IComputeNodeGroupRef"

    @builtins.property
    @jsii.member(jsii_name="computeNodeGroupRef")
    def compute_node_group_ref(self) -> "ComputeNodeGroupReference":
        '''(experimental) A reference to a ComputeNodeGroup resource.

        :stability: experimental
        '''
        return typing.cast("ComputeNodeGroupReference", jsii.get(self, "computeNodeGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IComputeNodeGroupRef).__jsii_proxy_class__ = lambda : _IComputeNodeGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_pcs.IQueueRef")
class IQueueRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Queue.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="queueRef")
    def queue_ref(self) -> "QueueReference":
        '''(experimental) A reference to a Queue resource.

        :stability: experimental
        '''
        ...


class _IQueueRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Queue.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_pcs.IQueueRef"

    @builtins.property
    @jsii.member(jsii_name="queueRef")
    def queue_ref(self) -> "QueueReference":
        '''(experimental) A reference to a Queue resource.

        :stability: experimental
        '''
        return typing.cast("QueueReference", jsii.get(self, "queueRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IQueueRef).__jsii_proxy_class__ = lambda : _IQueueRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_pcs.QueueReference",
    jsii_struct_bases=[],
    name_mapping={"queue_arn": "queueArn"},
)
class QueueReference:
    def __init__(self, *, queue_arn: builtins.str) -> None:
        '''A reference to a Queue resource.

        :param queue_arn: The Arn of the Queue resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_pcs as interfaces_pcs
            
            queue_reference = interfaces_pcs.QueueReference(
                queue_arn="queueArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61ebaa5a540a0a8bf4fa8c5c304d69a5f0a697386cf6ce2fed4e88faa7fea6d8)
            check_type(argname="argument queue_arn", value=queue_arn, expected_type=type_hints["queue_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "queue_arn": queue_arn,
        }

    @builtins.property
    def queue_arn(self) -> builtins.str:
        '''The Arn of the Queue resource.'''
        result = self._values.get("queue_arn")
        assert result is not None, "Required property 'queue_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "QueueReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ClusterReference",
    "ComputeNodeGroupReference",
    "IClusterRef",
    "IComputeNodeGroupRef",
    "IQueueRef",
    "QueueReference",
]

publication.publish()

def _typecheckingstub__4f19eef432c5188a0ea3df59cb28218513cb898ba2b6490710346045af4d929e(
    *,
    cluster_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__524904a7f4260417adac262fff3ddc56e72d2b5ccf1e9d50a2d872ef61450f4e(
    *,
    compute_node_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61ebaa5a540a0a8bf4fa8c5c304d69a5f0a697386cf6ce2fed4e88faa7fea6d8(
    *,
    queue_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IClusterRef, IComputeNodeGroupRef, IQueueRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
