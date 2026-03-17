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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_dlm.ILifecyclePolicyRef")
class ILifecyclePolicyRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a LifecyclePolicy.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicyRef")
    def lifecycle_policy_ref(self) -> "LifecyclePolicyReference":
        '''(experimental) A reference to a LifecyclePolicy resource.

        :stability: experimental
        '''
        ...


class _ILifecyclePolicyRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a LifecyclePolicy.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_dlm.ILifecyclePolicyRef"

    @builtins.property
    @jsii.member(jsii_name="lifecyclePolicyRef")
    def lifecycle_policy_ref(self) -> "LifecyclePolicyReference":
        '''(experimental) A reference to a LifecyclePolicy resource.

        :stability: experimental
        '''
        return typing.cast("LifecyclePolicyReference", jsii.get(self, "lifecyclePolicyRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILifecyclePolicyRef).__jsii_proxy_class__ = lambda : _ILifecyclePolicyRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_dlm.LifecyclePolicyReference",
    jsii_struct_bases=[],
    name_mapping={
        "lifecycle_policy_arn": "lifecyclePolicyArn",
        "lifecycle_policy_id": "lifecyclePolicyId",
    },
)
class LifecyclePolicyReference:
    def __init__(
        self,
        *,
        lifecycle_policy_arn: builtins.str,
        lifecycle_policy_id: builtins.str,
    ) -> None:
        '''A reference to a LifecyclePolicy resource.

        :param lifecycle_policy_arn: The ARN of the LifecyclePolicy resource.
        :param lifecycle_policy_id: The Id of the LifecyclePolicy resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_dlm as interfaces_dlm
            
            lifecycle_policy_reference = interfaces_dlm.LifecyclePolicyReference(
                lifecycle_policy_arn="lifecyclePolicyArn",
                lifecycle_policy_id="lifecyclePolicyId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcade0729cb210d4dec4658db34a681ecb1e3a2a066b4109217f0eabc3a16722)
            check_type(argname="argument lifecycle_policy_arn", value=lifecycle_policy_arn, expected_type=type_hints["lifecycle_policy_arn"])
            check_type(argname="argument lifecycle_policy_id", value=lifecycle_policy_id, expected_type=type_hints["lifecycle_policy_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lifecycle_policy_arn": lifecycle_policy_arn,
            "lifecycle_policy_id": lifecycle_policy_id,
        }

    @builtins.property
    def lifecycle_policy_arn(self) -> builtins.str:
        '''The ARN of the LifecyclePolicy resource.'''
        result = self._values.get("lifecycle_policy_arn")
        assert result is not None, "Required property 'lifecycle_policy_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def lifecycle_policy_id(self) -> builtins.str:
        '''The Id of the LifecyclePolicy resource.'''
        result = self._values.get("lifecycle_policy_id")
        assert result is not None, "Required property 'lifecycle_policy_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LifecyclePolicyReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ILifecyclePolicyRef",
    "LifecyclePolicyReference",
]

publication.publish()

def _typecheckingstub__fcade0729cb210d4dec4658db34a681ecb1e3a2a066b4109217f0eabc3a16722(
    *,
    lifecycle_policy_arn: builtins.str,
    lifecycle_policy_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [ILifecyclePolicyRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
