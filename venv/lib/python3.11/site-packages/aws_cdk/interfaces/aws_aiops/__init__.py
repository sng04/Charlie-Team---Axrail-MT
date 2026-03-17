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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_aiops.IInvestigationGroupRef")
class IInvestigationGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a InvestigationGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="investigationGroupRef")
    def investigation_group_ref(self) -> "InvestigationGroupReference":
        '''(experimental) A reference to a InvestigationGroup resource.

        :stability: experimental
        '''
        ...


class _IInvestigationGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a InvestigationGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_aiops.IInvestigationGroupRef"

    @builtins.property
    @jsii.member(jsii_name="investigationGroupRef")
    def investigation_group_ref(self) -> "InvestigationGroupReference":
        '''(experimental) A reference to a InvestigationGroup resource.

        :stability: experimental
        '''
        return typing.cast("InvestigationGroupReference", jsii.get(self, "investigationGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IInvestigationGroupRef).__jsii_proxy_class__ = lambda : _IInvestigationGroupRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_aiops.InvestigationGroupReference",
    jsii_struct_bases=[],
    name_mapping={"investigation_group_arn": "investigationGroupArn"},
)
class InvestigationGroupReference:
    def __init__(self, *, investigation_group_arn: builtins.str) -> None:
        '''A reference to a InvestigationGroup resource.

        :param investigation_group_arn: The Arn of the InvestigationGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_aiops as interfaces_aiops
            
            investigation_group_reference = interfaces_aiops.InvestigationGroupReference(
                investigation_group_arn="investigationGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__237101d010f7a2115df544b351aa0bf8a64f5668ba830bd1aabcad02af066bde)
            check_type(argname="argument investigation_group_arn", value=investigation_group_arn, expected_type=type_hints["investigation_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "investigation_group_arn": investigation_group_arn,
        }

    @builtins.property
    def investigation_group_arn(self) -> builtins.str:
        '''The Arn of the InvestigationGroup resource.'''
        result = self._values.get("investigation_group_arn")
        assert result is not None, "Required property 'investigation_group_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InvestigationGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IInvestigationGroupRef",
    "InvestigationGroupReference",
]

publication.publish()

def _typecheckingstub__237101d010f7a2115df544b351aa0bf8a64f5668ba830bd1aabcad02af066bde(
    *,
    investigation_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IInvestigationGroupRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
