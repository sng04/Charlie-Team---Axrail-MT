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
    jsii_type="aws-cdk-lib.interfaces.aws_batch.ComputeEnvironmentReference",
    jsii_struct_bases=[],
    name_mapping={"compute_environment_arn": "computeEnvironmentArn"},
)
class ComputeEnvironmentReference:
    def __init__(self, *, compute_environment_arn: builtins.str) -> None:
        '''A reference to a ComputeEnvironment resource.

        :param compute_environment_arn: The ComputeEnvironmentArn of the ComputeEnvironment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_batch as interfaces_batch
            
            compute_environment_reference = interfaces_batch.ComputeEnvironmentReference(
                compute_environment_arn="computeEnvironmentArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9892f46319fee3a567a6dd9e3467be2ed38db4f5f461dd27c0fc11f2560566ac)
            check_type(argname="argument compute_environment_arn", value=compute_environment_arn, expected_type=type_hints["compute_environment_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "compute_environment_arn": compute_environment_arn,
        }

    @builtins.property
    def compute_environment_arn(self) -> builtins.str:
        '''The ComputeEnvironmentArn of the ComputeEnvironment resource.'''
        result = self._values.get("compute_environment_arn")
        assert result is not None, "Required property 'compute_environment_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeEnvironmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_batch.ConsumableResourceReference",
    jsii_struct_bases=[],
    name_mapping={"consumable_resource_arn": "consumableResourceArn"},
)
class ConsumableResourceReference:
    def __init__(self, *, consumable_resource_arn: builtins.str) -> None:
        '''A reference to a ConsumableResource resource.

        :param consumable_resource_arn: The ConsumableResourceArn of the ConsumableResource resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_batch as interfaces_batch
            
            consumable_resource_reference = interfaces_batch.ConsumableResourceReference(
                consumable_resource_arn="consumableResourceArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efae255fc2224f92988a48a3e484cd67fe6c4ec91ce5e9c6fed9a015b90b5c26)
            check_type(argname="argument consumable_resource_arn", value=consumable_resource_arn, expected_type=type_hints["consumable_resource_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "consumable_resource_arn": consumable_resource_arn,
        }

    @builtins.property
    def consumable_resource_arn(self) -> builtins.str:
        '''The ConsumableResourceArn of the ConsumableResource resource.'''
        result = self._values.get("consumable_resource_arn")
        assert result is not None, "Required property 'consumable_resource_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConsumableResourceReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_batch.IComputeEnvironmentRef")
class IComputeEnvironmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ComputeEnvironment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="computeEnvironmentRef")
    def compute_environment_ref(self) -> "ComputeEnvironmentReference":
        '''(experimental) A reference to a ComputeEnvironment resource.

        :stability: experimental
        '''
        ...


class _IComputeEnvironmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ComputeEnvironment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_batch.IComputeEnvironmentRef"

    @builtins.property
    @jsii.member(jsii_name="computeEnvironmentRef")
    def compute_environment_ref(self) -> "ComputeEnvironmentReference":
        '''(experimental) A reference to a ComputeEnvironment resource.

        :stability: experimental
        '''
        return typing.cast("ComputeEnvironmentReference", jsii.get(self, "computeEnvironmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IComputeEnvironmentRef).__jsii_proxy_class__ = lambda : _IComputeEnvironmentRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_batch.IConsumableResourceRef")
class IConsumableResourceRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ConsumableResource.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="consumableResourceRef")
    def consumable_resource_ref(self) -> "ConsumableResourceReference":
        '''(experimental) A reference to a ConsumableResource resource.

        :stability: experimental
        '''
        ...


class _IConsumableResourceRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ConsumableResource.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_batch.IConsumableResourceRef"

    @builtins.property
    @jsii.member(jsii_name="consumableResourceRef")
    def consumable_resource_ref(self) -> "ConsumableResourceReference":
        '''(experimental) A reference to a ConsumableResource resource.

        :stability: experimental
        '''
        return typing.cast("ConsumableResourceReference", jsii.get(self, "consumableResourceRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConsumableResourceRef).__jsii_proxy_class__ = lambda : _IConsumableResourceRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_batch.IJobDefinitionRef")
class IJobDefinitionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a JobDefinition.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="jobDefinitionRef")
    def job_definition_ref(self) -> "JobDefinitionReference":
        '''(experimental) A reference to a JobDefinition resource.

        :stability: experimental
        '''
        ...


class _IJobDefinitionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a JobDefinition.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_batch.IJobDefinitionRef"

    @builtins.property
    @jsii.member(jsii_name="jobDefinitionRef")
    def job_definition_ref(self) -> "JobDefinitionReference":
        '''(experimental) A reference to a JobDefinition resource.

        :stability: experimental
        '''
        return typing.cast("JobDefinitionReference", jsii.get(self, "jobDefinitionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJobDefinitionRef).__jsii_proxy_class__ = lambda : _IJobDefinitionRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_batch.IJobQueueRef")
class IJobQueueRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a JobQueue.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="jobQueueRef")
    def job_queue_ref(self) -> "JobQueueReference":
        '''(experimental) A reference to a JobQueue resource.

        :stability: experimental
        '''
        ...


class _IJobQueueRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a JobQueue.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_batch.IJobQueueRef"

    @builtins.property
    @jsii.member(jsii_name="jobQueueRef")
    def job_queue_ref(self) -> "JobQueueReference":
        '''(experimental) A reference to a JobQueue resource.

        :stability: experimental
        '''
        return typing.cast("JobQueueReference", jsii.get(self, "jobQueueRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IJobQueueRef).__jsii_proxy_class__ = lambda : _IJobQueueRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_batch.ISchedulingPolicyRef")
class ISchedulingPolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SchedulingPolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="schedulingPolicyRef")
    def scheduling_policy_ref(self) -> "SchedulingPolicyReference":
        '''(experimental) A reference to a SchedulingPolicy resource.

        :stability: experimental
        '''
        ...


class _ISchedulingPolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SchedulingPolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_batch.ISchedulingPolicyRef"

    @builtins.property
    @jsii.member(jsii_name="schedulingPolicyRef")
    def scheduling_policy_ref(self) -> "SchedulingPolicyReference":
        '''(experimental) A reference to a SchedulingPolicy resource.

        :stability: experimental
        '''
        return typing.cast("SchedulingPolicyReference", jsii.get(self, "schedulingPolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISchedulingPolicyRef).__jsii_proxy_class__ = lambda : _ISchedulingPolicyRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_batch.IServiceEnvironmentRef")
class IServiceEnvironmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceEnvironment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="serviceEnvironmentRef")
    def service_environment_ref(self) -> "ServiceEnvironmentReference":
        '''(experimental) A reference to a ServiceEnvironment resource.

        :stability: experimental
        '''
        ...


class _IServiceEnvironmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ServiceEnvironment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_batch.IServiceEnvironmentRef"

    @builtins.property
    @jsii.member(jsii_name="serviceEnvironmentRef")
    def service_environment_ref(self) -> "ServiceEnvironmentReference":
        '''(experimental) A reference to a ServiceEnvironment resource.

        :stability: experimental
        '''
        return typing.cast("ServiceEnvironmentReference", jsii.get(self, "serviceEnvironmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServiceEnvironmentRef).__jsii_proxy_class__ = lambda : _IServiceEnvironmentRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_batch.JobDefinitionReference",
    jsii_struct_bases=[],
    name_mapping={"job_definition_arn": "jobDefinitionArn"},
)
class JobDefinitionReference:
    def __init__(self, *, job_definition_arn: builtins.str) -> None:
        '''A reference to a JobDefinition resource.

        :param job_definition_arn: The JobDefinitionArn of the JobDefinition resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_batch as interfaces_batch
            
            job_definition_reference = interfaces_batch.JobDefinitionReference(
                job_definition_arn="jobDefinitionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03d6fd2ef98b3bbd19b585886fbfc0882ccef6244aa7d36aaded401eb007a47f)
            check_type(argname="argument job_definition_arn", value=job_definition_arn, expected_type=type_hints["job_definition_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_definition_arn": job_definition_arn,
        }

    @builtins.property
    def job_definition_arn(self) -> builtins.str:
        '''The JobDefinitionArn of the JobDefinition resource.'''
        result = self._values.get("job_definition_arn")
        assert result is not None, "Required property 'job_definition_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobDefinitionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_batch.JobQueueReference",
    jsii_struct_bases=[],
    name_mapping={"job_queue_arn": "jobQueueArn"},
)
class JobQueueReference:
    def __init__(self, *, job_queue_arn: builtins.str) -> None:
        '''A reference to a JobQueue resource.

        :param job_queue_arn: The JobQueueArn of the JobQueue resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_batch as interfaces_batch
            
            job_queue_reference = interfaces_batch.JobQueueReference(
                job_queue_arn="jobQueueArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f741a3233b35e5b1fc106c1afb13f1a1cd2fdd8c9475679574235a13d2be1525)
            check_type(argname="argument job_queue_arn", value=job_queue_arn, expected_type=type_hints["job_queue_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "job_queue_arn": job_queue_arn,
        }

    @builtins.property
    def job_queue_arn(self) -> builtins.str:
        '''The JobQueueArn of the JobQueue resource.'''
        result = self._values.get("job_queue_arn")
        assert result is not None, "Required property 'job_queue_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "JobQueueReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_batch.SchedulingPolicyReference",
    jsii_struct_bases=[],
    name_mapping={"scheduling_policy_arn": "schedulingPolicyArn"},
)
class SchedulingPolicyReference:
    def __init__(self, *, scheduling_policy_arn: builtins.str) -> None:
        '''A reference to a SchedulingPolicy resource.

        :param scheduling_policy_arn: The Arn of the SchedulingPolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_batch as interfaces_batch
            
            scheduling_policy_reference = interfaces_batch.SchedulingPolicyReference(
                scheduling_policy_arn="schedulingPolicyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55dd4b778d4201026db0389e824b4eb31db89ab05e34ef6d6631ca81ce59f232)
            check_type(argname="argument scheduling_policy_arn", value=scheduling_policy_arn, expected_type=type_hints["scheduling_policy_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scheduling_policy_arn": scheduling_policy_arn,
        }

    @builtins.property
    def scheduling_policy_arn(self) -> builtins.str:
        '''The Arn of the SchedulingPolicy resource.'''
        result = self._values.get("scheduling_policy_arn")
        assert result is not None, "Required property 'scheduling_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SchedulingPolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_batch.ServiceEnvironmentReference",
    jsii_struct_bases=[],
    name_mapping={"service_environment_arn": "serviceEnvironmentArn"},
)
class ServiceEnvironmentReference:
    def __init__(self, *, service_environment_arn: builtins.str) -> None:
        '''A reference to a ServiceEnvironment resource.

        :param service_environment_arn: The ServiceEnvironmentArn of the ServiceEnvironment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_batch as interfaces_batch
            
            service_environment_reference = interfaces_batch.ServiceEnvironmentReference(
                service_environment_arn="serviceEnvironmentArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a7595da09bf52fb20ecdcaaf1d2bf46051a9c20cb746bfb3a793d6c4b143f7e)
            check_type(argname="argument service_environment_arn", value=service_environment_arn, expected_type=type_hints["service_environment_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "service_environment_arn": service_environment_arn,
        }

    @builtins.property
    def service_environment_arn(self) -> builtins.str:
        '''The ServiceEnvironmentArn of the ServiceEnvironment resource.'''
        result = self._values.get("service_environment_arn")
        assert result is not None, "Required property 'service_environment_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceEnvironmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ComputeEnvironmentReference",
    "ConsumableResourceReference",
    "IComputeEnvironmentRef",
    "IConsumableResourceRef",
    "IJobDefinitionRef",
    "IJobQueueRef",
    "ISchedulingPolicyRef",
    "IServiceEnvironmentRef",
    "JobDefinitionReference",
    "JobQueueReference",
    "SchedulingPolicyReference",
    "ServiceEnvironmentReference",
]

publication.publish()

def _typecheckingstub__9892f46319fee3a567a6dd9e3467be2ed38db4f5f461dd27c0fc11f2560566ac(
    *,
    compute_environment_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efae255fc2224f92988a48a3e484cd67fe6c4ec91ce5e9c6fed9a015b90b5c26(
    *,
    consumable_resource_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03d6fd2ef98b3bbd19b585886fbfc0882ccef6244aa7d36aaded401eb007a47f(
    *,
    job_definition_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f741a3233b35e5b1fc106c1afb13f1a1cd2fdd8c9475679574235a13d2be1525(
    *,
    job_queue_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55dd4b778d4201026db0389e824b4eb31db89ab05e34ef6d6631ca81ce59f232(
    *,
    scheduling_policy_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a7595da09bf52fb20ecdcaaf1d2bf46051a9c20cb746bfb3a793d6c4b143f7e(
    *,
    service_environment_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IComputeEnvironmentRef, IConsumableResourceRef, IJobDefinitionRef, IJobQueueRef, ISchedulingPolicyRef, IServiceEnvironmentRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
