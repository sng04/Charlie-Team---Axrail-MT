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
    jsii_type="aws-cdk-lib.interfaces.aws_ecs.CapacityProviderReference",
    jsii_struct_bases=[],
    name_mapping={"capacity_provider_name": "capacityProviderName"},
)
class CapacityProviderReference:
    def __init__(self, *, capacity_provider_name: builtins.str) -> None:
        '''A reference to a CapacityProvider resource.

        :param capacity_provider_name: The Name of the CapacityProvider resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecs as interfaces_ecs
            
            capacity_provider_reference = interfaces_ecs.CapacityProviderReference(
                capacity_provider_name="capacityProviderName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ba991623f78206f7be97200346e58e378992549d035637dc090551a69f20ec3)
            check_type(argname="argument capacity_provider_name", value=capacity_provider_name, expected_type=type_hints["capacity_provider_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "capacity_provider_name": capacity_provider_name,
        }

    @builtins.property
    def capacity_provider_name(self) -> builtins.str:
        '''The Name of the CapacityProvider resource.'''
        result = self._values.get("capacity_provider_name")
        assert result is not None, "Required property 'capacity_provider_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CapacityProviderReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecs.ClusterCapacityProviderAssociationsReference",
    jsii_struct_bases=[],
    name_mapping={"cluster": "cluster"},
)
class ClusterCapacityProviderAssociationsReference:
    def __init__(self, *, cluster: builtins.str) -> None:
        '''A reference to a ClusterCapacityProviderAssociations resource.

        :param cluster: The Cluster of the ClusterCapacityProviderAssociations resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecs as interfaces_ecs
            
            cluster_capacity_provider_associations_reference = interfaces_ecs.ClusterCapacityProviderAssociationsReference(
                cluster="cluster"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2b8d5b33ca63c32c0d1158dd708eba06510c3cdb10a0dedf8a251abeae5d016)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
        }

    @builtins.property
    def cluster(self) -> builtins.str:
        '''The Cluster of the ClusterCapacityProviderAssociations resource.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ClusterCapacityProviderAssociationsReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecs.ClusterReference",
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
            from aws_cdk.interfaces import aws_ecs as interfaces_ecs
            
            cluster_reference = interfaces_ecs.ClusterReference(
                cluster_arn="clusterArn",
                cluster_name="clusterName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9e5dd6081100ec0e14557c42f52e5c06875846f7f419b115ab533eaa1227a4e)
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


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecs.ExpressGatewayServiceReference",
    jsii_struct_bases=[],
    name_mapping={"service_arn": "serviceArn"},
)
class ExpressGatewayServiceReference:
    def __init__(self, *, service_arn: builtins.str) -> None:
        '''A reference to a ExpressGatewayService resource.

        :param service_arn: The ServiceArn of the ExpressGatewayService resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecs as interfaces_ecs
            
            express_gateway_service_reference = interfaces_ecs.ExpressGatewayServiceReference(
                service_arn="serviceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ea0eff1c207b387e3ce1c36391f0df7e092a4238b4d23d239261228685a988d)
            check_type(argname="argument service_arn", value=service_arn, expected_type=type_hints["service_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_arn": service_arn,
        }

    @builtins.property
    def service_arn(self) -> builtins.str:
        '''The ServiceArn of the ExpressGatewayService resource.'''
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ExpressGatewayServiceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecs.ICapacityProviderRef")
class ICapacityProviderRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityProvider.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="capacityProviderRef")
    def capacity_provider_ref(self) -> "CapacityProviderReference":
        '''(experimental) A reference to a CapacityProvider resource.

        :stability: experimental
        '''
        ...


class _ICapacityProviderRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a CapacityProvider.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecs.ICapacityProviderRef"

    @builtins.property
    @jsii.member(jsii_name="capacityProviderRef")
    def capacity_provider_ref(self) -> "CapacityProviderReference":
        '''(experimental) A reference to a CapacityProvider resource.

        :stability: experimental
        '''
        return typing.cast("CapacityProviderReference", jsii.get(self, "capacityProviderRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICapacityProviderRef).__jsii_proxy_class__ = lambda : _ICapacityProviderRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_ecs.IClusterCapacityProviderAssociationsRef"
)
class IClusterCapacityProviderAssociationsRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterCapacityProviderAssociations.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="clusterCapacityProviderAssociationsRef")
    def cluster_capacity_provider_associations_ref(
        self,
    ) -> "ClusterCapacityProviderAssociationsReference":
        '''(experimental) A reference to a ClusterCapacityProviderAssociations resource.

        :stability: experimental
        '''
        ...


class _IClusterCapacityProviderAssociationsRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ClusterCapacityProviderAssociations.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecs.IClusterCapacityProviderAssociationsRef"

    @builtins.property
    @jsii.member(jsii_name="clusterCapacityProviderAssociationsRef")
    def cluster_capacity_provider_associations_ref(
        self,
    ) -> "ClusterCapacityProviderAssociationsReference":
        '''(experimental) A reference to a ClusterCapacityProviderAssociations resource.

        :stability: experimental
        '''
        return typing.cast("ClusterCapacityProviderAssociationsReference", jsii.get(self, "clusterCapacityProviderAssociationsRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterCapacityProviderAssociationsRef).__jsii_proxy_class__ = lambda : _IClusterCapacityProviderAssociationsRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecs.IClusterRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecs.IClusterRef"

    @builtins.property
    @jsii.member(jsii_name="clusterRef")
    def cluster_ref(self) -> "ClusterReference":
        '''(experimental) A reference to a Cluster resource.

        :stability: experimental
        '''
        return typing.cast("ClusterReference", jsii.get(self, "clusterRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IClusterRef).__jsii_proxy_class__ = lambda : _IClusterRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecs.IExpressGatewayServiceRef")
class IExpressGatewayServiceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ExpressGatewayService.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="expressGatewayServiceRef")
    def express_gateway_service_ref(self) -> "ExpressGatewayServiceReference":
        '''(experimental) A reference to a ExpressGatewayService resource.

        :stability: experimental
        '''
        ...


class _IExpressGatewayServiceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ExpressGatewayService.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecs.IExpressGatewayServiceRef"

    @builtins.property
    @jsii.member(jsii_name="expressGatewayServiceRef")
    def express_gateway_service_ref(self) -> "ExpressGatewayServiceReference":
        '''(experimental) A reference to a ExpressGatewayService resource.

        :stability: experimental
        '''
        return typing.cast("ExpressGatewayServiceReference", jsii.get(self, "expressGatewayServiceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IExpressGatewayServiceRef).__jsii_proxy_class__ = lambda : _IExpressGatewayServiceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecs.IPrimaryTaskSetRef")
class IPrimaryTaskSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PrimaryTaskSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="primaryTaskSetRef")
    def primary_task_set_ref(self) -> "PrimaryTaskSetReference":
        '''(experimental) A reference to a PrimaryTaskSet resource.

        :stability: experimental
        '''
        ...


class _IPrimaryTaskSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PrimaryTaskSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecs.IPrimaryTaskSetRef"

    @builtins.property
    @jsii.member(jsii_name="primaryTaskSetRef")
    def primary_task_set_ref(self) -> "PrimaryTaskSetReference":
        '''(experimental) A reference to a PrimaryTaskSet resource.

        :stability: experimental
        '''
        return typing.cast("PrimaryTaskSetReference", jsii.get(self, "primaryTaskSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrimaryTaskSetRef).__jsii_proxy_class__ = lambda : _IPrimaryTaskSetRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecs.IServiceRef")
class IServiceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        ...


class _IServiceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Service.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecs.IServiceRef"

    @builtins.property
    @jsii.member(jsii_name="serviceRef")
    def service_ref(self) -> "ServiceReference":
        '''(experimental) A reference to a Service resource.

        :stability: experimental
        '''
        return typing.cast("ServiceReference", jsii.get(self, "serviceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceRef).__jsii_proxy_class__ = lambda : _IServiceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecs.ITaskDefinitionRef")
class ITaskDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TaskDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionRef")
    def task_definition_ref(self) -> "TaskDefinitionReference":
        '''(experimental) A reference to a TaskDefinition resource.

        :stability: experimental
        '''
        ...


class _ITaskDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TaskDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecs.ITaskDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="taskDefinitionRef")
    def task_definition_ref(self) -> "TaskDefinitionReference":
        '''(experimental) A reference to a TaskDefinition resource.

        :stability: experimental
        '''
        return typing.cast("TaskDefinitionReference", jsii.get(self, "taskDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITaskDefinitionRef).__jsii_proxy_class__ = lambda : _ITaskDefinitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_ecs.ITaskSetRef")
class ITaskSetRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TaskSet.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="taskSetRef")
    def task_set_ref(self) -> "TaskSetReference":
        '''(experimental) A reference to a TaskSet resource.

        :stability: experimental
        '''
        ...


class _ITaskSetRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TaskSet.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_ecs.ITaskSetRef"

    @builtins.property
    @jsii.member(jsii_name="taskSetRef")
    def task_set_ref(self) -> "TaskSetReference":
        '''(experimental) A reference to a TaskSet resource.

        :stability: experimental
        '''
        return typing.cast("TaskSetReference", jsii.get(self, "taskSetRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITaskSetRef).__jsii_proxy_class__ = lambda : _ITaskSetRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecs.PrimaryTaskSetReference",
    jsii_struct_bases=[],
    name_mapping={"cluster": "cluster", "service": "service"},
)
class PrimaryTaskSetReference:
    def __init__(self, *, cluster: builtins.str, service: builtins.str) -> None:
        '''A reference to a PrimaryTaskSet resource.

        :param cluster: The Cluster of the PrimaryTaskSet resource.
        :param service: The Service of the PrimaryTaskSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecs as interfaces_ecs
            
            primary_task_set_reference = interfaces_ecs.PrimaryTaskSetReference(
                cluster="cluster",
                service="service"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a1b939f002ad0ae1231600a088f90e5a07ee32dc47266ea7d20bc40291c4085)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
            "service": service,
        }

    @builtins.property
    def cluster(self) -> builtins.str:
        '''The Cluster of the PrimaryTaskSet resource.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The Service of the PrimaryTaskSet resource.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrimaryTaskSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecs.ServiceReference",
    jsii_struct_bases=[],
    name_mapping={"service_arn": "serviceArn"},
)
class ServiceReference:
    def __init__(self, *, service_arn: builtins.str) -> None:
        '''A reference to a Service resource.

        :param service_arn: The ServiceArn of the Service resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecs as interfaces_ecs
            
            service_reference = interfaces_ecs.ServiceReference(
                service_arn="serviceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__222e58c3bfd0aefe61c64da263b2f2f7ee538bff76050254c35072818cb84d58)
            check_type(argname="argument service_arn", value=service_arn, expected_type=type_hints["service_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_arn": service_arn,
        }

    @builtins.property
    def service_arn(self) -> builtins.str:
        '''The ServiceArn of the Service resource.'''
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecs.TaskDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={"task_definition_arn": "taskDefinitionArn"},
)
class TaskDefinitionReference:
    def __init__(self, *, task_definition_arn: builtins.str) -> None:
        '''A reference to a TaskDefinition resource.

        :param task_definition_arn: The TaskDefinitionArn of the TaskDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecs as interfaces_ecs
            
            task_definition_reference = interfaces_ecs.TaskDefinitionReference(
                task_definition_arn="taskDefinitionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d3399131a06519592dee06a25b10deee54dd67b0605a0fbbe5d52f243cb02fc)
            check_type(argname="argument task_definition_arn", value=task_definition_arn, expected_type=type_hints["task_definition_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "task_definition_arn": task_definition_arn,
        }

    @builtins.property
    def task_definition_arn(self) -> builtins.str:
        '''The TaskDefinitionArn of the TaskDefinition resource.'''
        result = self._values.get("task_definition_arn")
        assert result is not None, "Required property 'task_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_ecs.TaskSetReference",
    jsii_struct_bases=[],
    name_mapping={
        "cluster": "cluster",
        "service": "service",
        "task_set_id": "taskSetId",
    },
)
class TaskSetReference:
    def __init__(
        self,
        *,
        cluster: builtins.str,
        service: builtins.str,
        task_set_id: builtins.str,
    ) -> None:
        '''A reference to a TaskSet resource.

        :param cluster: The Cluster of the TaskSet resource.
        :param service: The Service of the TaskSet resource.
        :param task_set_id: The Id of the TaskSet resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_ecs as interfaces_ecs
            
            task_set_reference = interfaces_ecs.TaskSetReference(
                cluster="cluster",
                service="service",
                task_set_id="taskSetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74cd9665edddb0a5616888159b532fdbf6e5e802106c342a4e8d6846d23d1674)
            check_type(argname="argument cluster", value=cluster, expected_type=type_hints["cluster"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument task_set_id", value=task_set_id, expected_type=type_hints["task_set_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "cluster": cluster,
            "service": service,
            "task_set_id": task_set_id,
        }

    @builtins.property
    def cluster(self) -> builtins.str:
        '''The Cluster of the TaskSet resource.'''
        result = self._values.get("cluster")
        assert result is not None, "Required property 'cluster' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The Service of the TaskSet resource.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def task_set_id(self) -> builtins.str:
        '''The Id of the TaskSet resource.'''
        result = self._values.get("task_set_id")
        assert result is not None, "Required property 'task_set_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TaskSetReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CapacityProviderReference",
    "ClusterCapacityProviderAssociationsReference",
    "ClusterReference",
    "ExpressGatewayServiceReference",
    "ICapacityProviderRef",
    "IClusterCapacityProviderAssociationsRef",
    "IClusterRef",
    "IExpressGatewayServiceRef",
    "IPrimaryTaskSetRef",
    "IServiceRef",
    "ITaskDefinitionRef",
    "ITaskSetRef",
    "PrimaryTaskSetReference",
    "ServiceReference",
    "TaskDefinitionReference",
    "TaskSetReference",
]

publication.publish()

def _typecheckingstub__6ba991623f78206f7be97200346e58e378992549d035637dc090551a69f20ec3(
    *,
    capacity_provider_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2b8d5b33ca63c32c0d1158dd708eba06510c3cdb10a0dedf8a251abeae5d016(
    *,
    cluster: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9e5dd6081100ec0e14557c42f52e5c06875846f7f419b115ab533eaa1227a4e(
    *,
    cluster_arn: builtins.str,
    cluster_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea0eff1c207b387e3ce1c36391f0df7e092a4238b4d23d239261228685a988d(
    *,
    service_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a1b939f002ad0ae1231600a088f90e5a07ee32dc47266ea7d20bc40291c4085(
    *,
    cluster: builtins.str,
    service: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__222e58c3bfd0aefe61c64da263b2f2f7ee538bff76050254c35072818cb84d58(
    *,
    service_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3399131a06519592dee06a25b10deee54dd67b0605a0fbbe5d52f243cb02fc(
    *,
    task_definition_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74cd9665edddb0a5616888159b532fdbf6e5e802106c342a4e8d6846d23d1674(
    *,
    cluster: builtins.str,
    service: builtins.str,
    task_set_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICapacityProviderRef, IClusterCapacityProviderAssociationsRef, IClusterRef, IExpressGatewayServiceRef, IPrimaryTaskSetRef, IServiceRef, ITaskDefinitionRef, ITaskSetRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
