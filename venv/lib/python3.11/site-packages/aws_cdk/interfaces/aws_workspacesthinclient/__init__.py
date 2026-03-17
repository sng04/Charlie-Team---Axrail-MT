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
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesthinclient.EnvironmentReference",
    jsii_struct_bases=[],
    name_mapping={
        "environment_arn": "environmentArn",
        "environment_id": "environmentId",
    },
)
class EnvironmentReference:
    def __init__(
        self,
        *,
        environment_arn: builtins.str,
        environment_id: builtins.str,
    ) -> None:
        '''A reference to a Environment resource.

        :param environment_arn: The ARN of the Environment resource.
        :param environment_id: The Id of the Environment resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_workspacesthinclient as interfaces_workspacesthinclient
            
            environment_reference = interfaces_workspacesthinclient.EnvironmentReference(
                environment_arn="environmentArn",
                environment_id="environmentId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45398128220e7ec8e8c8a28404c1ac9b5b549fdeccd62befc487317fa012f07d)
            check_type(argname="argument environment_arn", value=environment_arn, expected_type=type_hints["environment_arn"])
            check_type(argname="argument environment_id", value=environment_id, expected_type=type_hints["environment_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment_arn": environment_arn,
            "environment_id": environment_id,
        }

    @builtins.property
    def environment_arn(self) -> builtins.str:
        '''The ARN of the Environment resource.'''
        result = self._values.get("environment_arn")
        assert result is not None, "Required property 'environment_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_id(self) -> builtins.str:
        '''The Id of the Environment resource.'''
        result = self._values.get("environment_id")
        assert result is not None, "Required property 'environment_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EnvironmentReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_workspacesthinclient.IEnvironmentRef"
)
class IEnvironmentRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Environment.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        ...


class _IEnvironmentRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Environment.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_workspacesthinclient.IEnvironmentRef"

    @builtins.property
    @jsii.member(jsii_name="environmentRef")
    def environment_ref(self) -> "EnvironmentReference":
        '''(experimental) A reference to a Environment resource.

        :stability: experimental
        '''
        return typing.cast("EnvironmentReference", jsii.get(self, "environmentRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEnvironmentRef).__jsii_proxy_class__ = lambda : _IEnvironmentRefProxy


__all__ = [
    "EnvironmentReference",
    "IEnvironmentRef",
]

publication.publish()

def _typecheckingstub__45398128220e7ec8e8c8a28404c1ac9b5b549fdeccd62befc487317fa012f07d(
    *,
    environment_arn: builtins.str,
    environment_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IEnvironmentRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
