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
    jsii_type="aws-cdk-lib.interfaces.aws_synthetics.CanaryReference",
    jsii_struct_bases=[],
    name_mapping={"canary_name": "canaryName"},
)
class CanaryReference:
    def __init__(self, *, canary_name: builtins.str) -> None:
        '''A reference to a Canary resource.

        :param canary_name: The Name of the Canary resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_synthetics as interfaces_synthetics
            
            canary_reference = interfaces_synthetics.CanaryReference(
                canary_name="canaryName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfd065f0c9658eada75bb354bd0cabf0d37665555e9a8a1b313f029fc8182f67)
            check_type(argname="argument canary_name", value=canary_name, expected_type=type_hints["canary_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "canary_name": canary_name,
        }

    @builtins.property
    def canary_name(self) -> builtins.str:
        '''The Name of the Canary resource.'''
        result = self._values.get("canary_name")
        assert result is not None, "Required property 'canary_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CanaryReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_synthetics.GroupReference",
    jsii_struct_bases=[],
    name_mapping={"group_name": "groupName"},
)
class GroupReference:
    def __init__(self, *, group_name: builtins.str) -> None:
        '''A reference to a Group resource.

        :param group_name: The Name of the Group resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_synthetics as interfaces_synthetics
            
            group_reference = interfaces_synthetics.GroupReference(
                group_name="groupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cb562236ae8f3ba69e52d59927534399c59f90c1a1d58dd69cf8e1087782697)
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_name": group_name,
        }

    @builtins.property
    def group_name(self) -> builtins.str:
        '''The Name of the Group resource.'''
        result = self._values.get("group_name")
        assert result is not None, "Required property 'group_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_synthetics.ICanaryRef")
class ICanaryRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Canary.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="canaryRef")
    def canary_ref(self) -> "CanaryReference":
        '''(experimental) A reference to a Canary resource.

        :stability: experimental
        '''
        ...


class _ICanaryRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Canary.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_synthetics.ICanaryRef"

    @builtins.property
    @jsii.member(jsii_name="canaryRef")
    def canary_ref(self) -> "CanaryReference":
        '''(experimental) A reference to a Canary resource.

        :stability: experimental
        '''
        return typing.cast("CanaryReference", jsii.get(self, "canaryRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICanaryRef).__jsii_proxy_class__ = lambda : _ICanaryRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_synthetics.IGroupRef")
class IGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Group.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="groupRef")
    def group_ref(self) -> "GroupReference":
        '''(experimental) A reference to a Group resource.

        :stability: experimental
        '''
        ...


class _IGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Group.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_synthetics.IGroupRef"

    @builtins.property
    @jsii.member(jsii_name="groupRef")
    def group_ref(self) -> "GroupReference":
        '''(experimental) A reference to a Group resource.

        :stability: experimental
        '''
        return typing.cast("GroupReference", jsii.get(self, "groupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupRef).__jsii_proxy_class__ = lambda : _IGroupRefProxy


__all__ = [
    "CanaryReference",
    "GroupReference",
    "ICanaryRef",
    "IGroupRef",
]

publication.publish()

def _typecheckingstub__cfd065f0c9658eada75bb354bd0cabf0d37665555e9a8a1b313f029fc8182f67(
    *,
    canary_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb562236ae8f3ba69e52d59927534399c59f90c1a1d58dd69cf8e1087782697(
    *,
    group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ICanaryRef, IGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
