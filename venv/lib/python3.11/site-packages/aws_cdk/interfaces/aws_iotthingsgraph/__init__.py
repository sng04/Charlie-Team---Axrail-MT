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
    jsii_type="aws-cdk-lib.interfaces.aws_iotthingsgraph.FlowTemplateReference",
    jsii_struct_bases=[],
    name_mapping={"flow_template_id": "flowTemplateId"},
)
class FlowTemplateReference:
    def __init__(self, *, flow_template_id: builtins.str) -> None:
        '''A reference to a FlowTemplate resource.

        :param flow_template_id: The Id of the FlowTemplate resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_iotthingsgraph as interfaces_iotthingsgraph
            
            flow_template_reference = interfaces_iotthingsgraph.FlowTemplateReference(
                flow_template_id="flowTemplateId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f57f7c5c4b24a0e5a79f7abd90385889b8a94c65e33b0ae1974313c7fba6824)
            check_type(argname="argument flow_template_id", value=flow_template_id, expected_type=type_hints["flow_template_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_template_id": flow_template_id,
        }

    @builtins.property
    def flow_template_id(self) -> builtins.str:
        '''The Id of the FlowTemplate resource.'''
        result = self._values.get("flow_template_id")
        assert result is not None, "Required property 'flow_template_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FlowTemplateReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_iotthingsgraph.IFlowTemplateRef")
class IFlowTemplateRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a FlowTemplate.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="flowTemplateRef")
    def flow_template_ref(self) -> "FlowTemplateReference":
        '''(experimental) A reference to a FlowTemplate resource.

        :stability: experimental
        '''
        ...


class _IFlowTemplateRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a FlowTemplate.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_iotthingsgraph.IFlowTemplateRef"

    @builtins.property
    @jsii.member(jsii_name="flowTemplateRef")
    def flow_template_ref(self) -> "FlowTemplateReference":
        '''(experimental) A reference to a FlowTemplate resource.

        :stability: experimental
        '''
        return typing.cast("FlowTemplateReference", jsii.get(self, "flowTemplateRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IFlowTemplateRef).__jsii_proxy_class__ = lambda : _IFlowTemplateRefProxy


__all__ = [
    "FlowTemplateReference",
    "IFlowTemplateRef",
]

publication.publish()

def _typecheckingstub__4f57f7c5c4b24a0e5a79f7abd90385889b8a94c65e33b0ae1974313c7fba6824(
    *,
    flow_template_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IFlowTemplateRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
