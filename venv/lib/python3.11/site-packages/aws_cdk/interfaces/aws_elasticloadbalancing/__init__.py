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
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancing.ILoadBalancerRef"
)
class ILoadBalancerRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LoadBalancer.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="loadBalancerRef")
    def load_balancer_ref(self) -> "LoadBalancerReference":
        '''(experimental) A reference to a LoadBalancer resource.

        :stability: experimental
        '''
        ...


class _ILoadBalancerRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LoadBalancer.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_elasticloadbalancing.ILoadBalancerRef"

    @builtins.property
    @jsii.member(jsii_name="loadBalancerRef")
    def load_balancer_ref(self) -> "LoadBalancerReference":
        '''(experimental) A reference to a LoadBalancer resource.

        :stability: experimental
        '''
        return typing.cast("LoadBalancerReference", jsii.get(self, "loadBalancerRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILoadBalancerRef).__jsii_proxy_class__ = lambda : _ILoadBalancerRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_elasticloadbalancing.LoadBalancerReference",
    jsii_struct_bases=[],
    name_mapping={"load_balancer_name": "loadBalancerName"},
)
class LoadBalancerReference:
    def __init__(self, *, load_balancer_name: builtins.str) -> None:
        '''A reference to a LoadBalancer resource.

        :param load_balancer_name: The LoadBalancerName of the LoadBalancer resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_elasticloadbalancing as interfaces_elasticloadbalancing
            
            load_balancer_reference = interfaces_elasticloadbalancing.LoadBalancerReference(
                load_balancer_name="loadBalancerName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcf014b61d9cbc6234dfacc907c27ebff410e96cc0547c87fa9dd0b7c43f629e)
            check_type(argname="argument load_balancer_name", value=load_balancer_name, expected_type=type_hints["load_balancer_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "load_balancer_name": load_balancer_name,
        }

    @builtins.property
    def load_balancer_name(self) -> builtins.str:
        '''The LoadBalancerName of the LoadBalancer resource.'''
        result = self._values.get("load_balancer_name")
        assert result is not None, "Required property 'load_balancer_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ILoadBalancerRef",
    "LoadBalancerReference",
]

publication.publish()

def _typecheckingstub__fcf014b61d9cbc6234dfacc907c27ebff410e96cc0547c87fa9dd0b7c43f629e(
    *,
    load_balancer_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ILoadBalancerRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
