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
    jsii_type="aws-cdk-lib.interfaces.aws_msk.BatchScramSecretReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn"},
)
class BatchScramSecretReference:
    def __init__(self, *, cluster_arn: builtins.str) -> None:
        '''A reference to a BatchScramSecret resource.

        :param cluster_arn: The ClusterArn of the BatchScramSecret resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_msk as interfaces_msk
            
            batch_scram_secret_reference = interfaces_msk.BatchScramSecretReference(
                cluster_arn="clusterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ae6fd3d6b9a92551a7fe3361254f3ecb9afe5a6d80aba771970693b48cccc54)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
        }

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The ClusterArn of the BatchScramSecret resource.'''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchScramSecretReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_msk.ClusterPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"cluster_arn": "clusterArn"},
)
class ClusterPolicyReference:
    def __init__(self, *, cluster_arn: builtins.str) -> None:
        '''A reference to a ClusterPolicy resource.

        :param cluster_arn: The ClusterArn of the ClusterPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_msk as interfaces_msk
            
            cluster_policy_reference = interfaces_msk.ClusterPolicyReference(
                cluster_arn="clusterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7437407d73b1f96febd4fbf267a7df0376e00317b287110a369a63b2103e33ea)
            check_type(argname="argument cluster_arn", value=cluster_arn, expected_type=type_hints["cluster_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster_arn": cluster_arn,
        }

    @builtins.property
    def cluster_arn(self) -> builtins.str:
        '''The ClusterArn of the ClusterPolicy resource.'''
        result = self._values.get("cluster_arn")
        assert result is not None, "Required property 'cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_msk.ClusterReference",
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
            from aws_cdk.interfaces import aws_msk as interfaces_msk
            
            cluster_reference = interfaces_msk.ClusterReference(
                cluster_arn="clusterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8818272280762cb9d13032c7d2b464bd15beeb018f33fd68fcd2cef71918be4a)
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
    jsii_type="aws-cdk-lib.interfaces.aws_msk.ConfigurationReference",
    jsii_struct_bases=[],
    name_mapping={"configuration_arn": "configurationArn"},
)
class ConfigurationReference:
    def __init__(self, *, configuration_arn: builtins.str) -> None:
        '''A reference to a Configuration resource.

        :param configuration_arn: The Arn of the Configuration resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_msk as interfaces_msk
            
            configuration_reference = interfaces_msk.ConfigurationReference(
                configuration_arn="configurationArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac4483325f29ec090543f797d00d9496c22aa71cc0eb3e899712d8e19bbfcf94)
            check_type(argname="argument configuration_arn", value=configuration_arn, expected_type=type_hints["configuration_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_arn": configuration_arn,
        }

    @builtins.property
    def configuration_arn(self) -> builtins.str:
        '''The Arn of the Configuration resource.'''
        result = self._values.get("configuration_arn")
        assert result is not None, "Required property 'configuration_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_msk.IBatchScramSecretRef")
class IBatchScramSecretRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a BatchScramSecret.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="batchScramSecretRef")
    def batch_scram_secret_ref(self) -> "BatchScramSecretReference":
        '''(experimental) A reference to a BatchScramSecret resource.

        :stability: experimental
        '''
        ...


class _IBatchScramSecretRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a BatchScramSecret.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_msk.IBatchScramSecretRef"

    @builtins.property
    @jsii.member(jsii_name="batchScramSecretRef")
    def batch_scram_secret_ref(self) -> "BatchScramSecretReference":
        '''(experimental) A reference to a BatchScramSecret resource.

        :stability: experimental
        '''
        return typing.cast("BatchScramSecretReference", jsii.get(self, "batchScramSecretRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBatchScramSecretRef).__jsii_proxy_class__ = lambda : _IBatchScramSecretRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_msk.IClusterPolicyRef")
class IClusterPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterPolicyRef")
    def cluster_policy_ref(self) -> "ClusterPolicyReference":
        '''(experimental) A reference to a ClusterPolicy resource.

        :stability: experimental
        '''
        ...


class _IClusterPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_msk.IClusterPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="clusterPolicyRef")
    def cluster_policy_ref(self) -> "ClusterPolicyReference":
        '''(experimental) A reference to a ClusterPolicy resource.

        :stability: experimental
        '''
        return typing.cast("ClusterPolicyReference", jsii.get(self, "clusterPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterPolicyRef).__jsii_proxy_class__ = lambda : _IClusterPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_msk.IClusterRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_msk.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_msk.IConfigurationRef")
class IConfigurationRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Configuration.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="configurationRef")
    def configuration_ref(self) -> "ConfigurationReference":
        '''(experimental) A reference to a Configuration resource.

        :stability: experimental
        '''
        ...


class _IConfigurationRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Configuration.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_msk.IConfigurationRef"

    @builtins.property
    @jsii.member(jsii_name="configurationRef")
    def configuration_ref(self) -> "ConfigurationReference":
        '''(experimental) A reference to a Configuration resource.

        :stability: experimental
        '''
        return typing.cast("ConfigurationReference", jsii.get(self, "configurationRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationRef).__jsii_proxy_class__ = lambda : _IConfigurationRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_msk.IReplicatorRef")
class IReplicatorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Replicator.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="replicatorRef")
    def replicator_ref(self) -> "ReplicatorReference":
        '''(experimental) A reference to a Replicator resource.

        :stability: experimental
        '''
        ...


class _IReplicatorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Replicator.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_msk.IReplicatorRef"

    @builtins.property
    @jsii.member(jsii_name="replicatorRef")
    def replicator_ref(self) -> "ReplicatorReference":
        '''(experimental) A reference to a Replicator resource.

        :stability: experimental
        '''
        return typing.cast("ReplicatorReference", jsii.get(self, "replicatorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReplicatorRef).__jsii_proxy_class__ = lambda : _IReplicatorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_msk.IServerlessClusterRef")
class IServerlessClusterRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServerlessCluster.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serverlessClusterRef")
    def serverless_cluster_ref(self) -> "ServerlessClusterReference":
        '''(experimental) A reference to a ServerlessCluster resource.

        :stability: experimental
        '''
        ...


class _IServerlessClusterRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServerlessCluster.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_msk.IServerlessClusterRef"

    @builtins.property
    @jsii.member(jsii_name="serverlessClusterRef")
    def serverless_cluster_ref(self) -> "ServerlessClusterReference":
        '''(experimental) A reference to a ServerlessCluster resource.

        :stability: experimental
        '''
        return typing.cast("ServerlessClusterReference", jsii.get(self, "serverlessClusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServerlessClusterRef).__jsii_proxy_class__ = lambda : _IServerlessClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_msk.ITopicRef")
class ITopicRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Topic.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="topicRef")
    def topic_ref(self) -> "TopicReference":
        '''(experimental) A reference to a Topic resource.

        :stability: experimental
        '''
        ...


class _ITopicRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Topic.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_msk.ITopicRef"

    @builtins.property
    @jsii.member(jsii_name="topicRef")
    def topic_ref(self) -> "TopicReference":
        '''(experimental) A reference to a Topic resource.

        :stability: experimental
        '''
        return typing.cast("TopicReference", jsii.get(self, "topicRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITopicRef).__jsii_proxy_class__ = lambda : _ITopicRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_msk.IVpcConnectionRef")
class IVpcConnectionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VpcConnection.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="vpcConnectionRef")
    def vpc_connection_ref(self) -> "VpcConnectionReference":
        '''(experimental) A reference to a VpcConnection resource.

        :stability: experimental
        '''
        ...


class _IVpcConnectionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VpcConnection.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_msk.IVpcConnectionRef"

    @builtins.property
    @jsii.member(jsii_name="vpcConnectionRef")
    def vpc_connection_ref(self) -> "VpcConnectionReference":
        '''(experimental) A reference to a VpcConnection resource.

        :stability: experimental
        '''
        return typing.cast("VpcConnectionReference", jsii.get(self, "vpcConnectionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVpcConnectionRef).__jsii_proxy_class__ = lambda : _IVpcConnectionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_msk.ReplicatorReference",
    jsii_struct_bases=[],
    name_mapping={"replicator_arn": "replicatorArn"},
)
class ReplicatorReference:
    def __init__(self, *, replicator_arn: builtins.str) -> None:
        '''A reference to a Replicator resource.

        :param replicator_arn: The ReplicatorArn of the Replicator resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_msk as interfaces_msk
            
            replicator_reference = interfaces_msk.ReplicatorReference(
                replicator_arn="replicatorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5263d5fd3d72353960dd34ae5c95e89382a09b37faaf247a895a78a673082937)
            check_type(argname="argument replicator_arn", value=replicator_arn, expected_type=type_hints["replicator_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replicator_arn": replicator_arn,
        }

    @builtins.property
    def replicator_arn(self) -> builtins.str:
        '''The ReplicatorArn of the Replicator resource.'''
        result = self._values.get("replicator_arn")
        assert result is not None, "Required property 'replicator_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReplicatorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_msk.ServerlessClusterReference",
    jsii_struct_bases=[],
    name_mapping={"serverless_cluster_arn": "serverlessClusterArn"},
)
class ServerlessClusterReference:
    def __init__(self, *, serverless_cluster_arn: builtins.str) -> None:
        '''A reference to a ServerlessCluster resource.

        :param serverless_cluster_arn: The Arn of the ServerlessCluster resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_msk as interfaces_msk
            
            serverless_cluster_reference = interfaces_msk.ServerlessClusterReference(
                serverless_cluster_arn="serverlessClusterArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3321e6aad062bb2681b8b3ca453afdbe7ce171d7e0f9708f642675a5e92f259b)
            check_type(argname="argument serverless_cluster_arn", value=serverless_cluster_arn, expected_type=type_hints["serverless_cluster_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "serverless_cluster_arn": serverless_cluster_arn,
        }

    @builtins.property
    def serverless_cluster_arn(self) -> builtins.str:
        '''The Arn of the ServerlessCluster resource.'''
        result = self._values.get("serverless_cluster_arn")
        assert result is not None, "Required property 'serverless_cluster_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerlessClusterReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_msk.TopicReference",
    jsii_struct_bases=[],
    name_mapping={"topic_arn": "topicArn"},
)
class TopicReference:
    def __init__(self, *, topic_arn: builtins.str) -> None:
        '''A reference to a Topic resource.

        :param topic_arn: The TopicArn of the Topic resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_msk as interfaces_msk
            
            topic_reference = interfaces_msk.TopicReference(
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2099850b9885f27ffe5c85b2a40f22d4b54b7f7c42e467c067cb92ef2e2a1713)
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "topic_arn": topic_arn,
        }

    @builtins.property
    def topic_arn(self) -> builtins.str:
        '''The TopicArn of the Topic resource.'''
        result = self._values.get("topic_arn")
        assert result is not None, "Required property 'topic_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TopicReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_msk.VpcConnectionReference",
    jsii_struct_bases=[],
    name_mapping={"vpc_connection_arn": "vpcConnectionArn"},
)
class VpcConnectionReference:
    def __init__(self, *, vpc_connection_arn: builtins.str) -> None:
        '''A reference to a VpcConnection resource.

        :param vpc_connection_arn: The Arn of the VpcConnection resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_msk as interfaces_msk
            
            vpc_connection_reference = interfaces_msk.VpcConnectionReference(
                vpc_connection_arn="vpcConnectionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__558a2bbe85670dfe0fc92872489481ed10c7f008336d8079d1585447114a3ca8)
            check_type(argname="argument vpc_connection_arn", value=vpc_connection_arn, expected_type=type_hints["vpc_connection_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "vpc_connection_arn": vpc_connection_arn,
        }

    @builtins.property
    def vpc_connection_arn(self) -> builtins.str:
        '''The Arn of the VpcConnection resource.'''
        result = self._values.get("vpc_connection_arn")
        assert result is not None, "Required property 'vpc_connection_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcConnectionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "BatchScramSecretReference",
    "ClusterPolicyReference",
    "ClusterReference",
    "ConfigurationReference",
    "IBatchScramSecretRef",
    "IClusterPolicyRef",
    "IClusterRef",
    "IConfigurationRef",
    "IReplicatorRef",
    "IServerlessClusterRef",
    "ITopicRef",
    "IVpcConnectionRef",
    "ReplicatorReference",
    "ServerlessClusterReference",
    "TopicReference",
    "VpcConnectionReference",
]

publication.publish()

def _typecheckingstub__9ae6fd3d6b9a92551a7fe3361254f3ecb9afe5a6d80aba771970693b48cccc54(
    *,
    cluster_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7437407d73b1f96febd4fbf267a7df0376e00317b287110a369a63b2103e33ea(
    *,
    cluster_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8818272280762cb9d13032c7d2b464bd15beeb018f33fd68fcd2cef71918be4a(
    *,
    cluster_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac4483325f29ec090543f797d00d9496c22aa71cc0eb3e899712d8e19bbfcf94(
    *,
    configuration_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5263d5fd3d72353960dd34ae5c95e89382a09b37faaf247a895a78a673082937(
    *,
    replicator_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3321e6aad062bb2681b8b3ca453afdbe7ce171d7e0f9708f642675a5e92f259b(
    *,
    serverless_cluster_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2099850b9885f27ffe5c85b2a40f22d4b54b7f7c42e467c067cb92ef2e2a1713(
    *,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__558a2bbe85670dfe0fc92872489481ed10c7f008336d8079d1585447114a3ca8(
    *,
    vpc_connection_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IBatchScramSecretRef, IClusterPolicyRef, IClusterRef, IConfigurationRef, IReplicatorRef, IServerlessClusterRef, ITopicRef, IVpcConnectionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
