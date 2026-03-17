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


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_codeguruprofiler.IProfilingGroupRef"
)
class IProfilingGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ProfilingGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="profilingGroupRef")
    def profiling_group_ref(self) -> "ProfilingGroupReference":
        '''(experimental) A reference to a ProfilingGroup resource.

        :stability: experimental
        '''
        ...


class _IProfilingGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ProfilingGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_codeguruprofiler.IProfilingGroupRef"

    @builtins.property
    @jsii.member(jsii_name="profilingGroupRef")
    def profiling_group_ref(self) -> "ProfilingGroupReference":
        '''(experimental) A reference to a ProfilingGroup resource.

        :stability: experimental
        '''
        return typing.cast("ProfilingGroupReference", jsii.get(self, "profilingGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IProfilingGroupRef).__jsii_proxy_class__ = lambda : _IProfilingGroupRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_codeguruprofiler.ProfilingGroupReference",
    jsii_struct_bases=[],
    name_mapping={
        "profiling_group_arn": "profilingGroupArn",
        "profiling_group_name": "profilingGroupName",
    },
)
class ProfilingGroupReference:
    def __init__(
        self,
        *,
        profiling_group_arn: builtins.str,
        profiling_group_name: builtins.str,
    ) -> None:
        '''A reference to a ProfilingGroup resource.

        :param profiling_group_arn: The ARN of the ProfilingGroup resource.
        :param profiling_group_name: The ProfilingGroupName of the ProfilingGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_codeguruprofiler as interfaces_codeguruprofiler
            
            profiling_group_reference = interfaces_codeguruprofiler.ProfilingGroupReference(
                profiling_group_arn="profilingGroupArn",
                profiling_group_name="profilingGroupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__379dcecb1cab1b83dcc39a39fdc8cb9acc996393d71a020512e32bd43716cc53)
            check_type(argname="argument profiling_group_arn", value=profiling_group_arn, expected_type=type_hints["profiling_group_arn"])
            check_type(argname="argument profiling_group_name", value=profiling_group_name, expected_type=type_hints["profiling_group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "profiling_group_arn": profiling_group_arn,
            "profiling_group_name": profiling_group_name,
        }

    @builtins.property
    def profiling_group_arn(self) -> builtins.str:
        '''The ARN of the ProfilingGroup resource.'''
        result = self._values.get("profiling_group_arn")
        assert result is not None, "Required property 'profiling_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profiling_group_name(self) -> builtins.str:
        '''The ProfilingGroupName of the ProfilingGroup resource.'''
        result = self._values.get("profiling_group_name")
        assert result is not None, "Required property 'profiling_group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ProfilingGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IProfilingGroupRef",
    "ProfilingGroupReference",
]

publication.publish()

def _typecheckingstub__379dcecb1cab1b83dcc39a39fdc8cb9acc996393d71a020512e32bd43716cc53(
    *,
    profiling_group_arn: builtins.str,
    profiling_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IProfilingGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
