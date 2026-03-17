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
    jsii_type="aws-cdk-lib.interfaces.aws_neptunegraph.GraphReference",
    jsii_struct_bases=[],
    name_mapping={"graph_arn": "graphArn", "graph_id": "graphId"},
)
class GraphReference:
    def __init__(self, *, graph_arn: builtins.str, graph_id: builtins.str) -> None:
        '''A reference to a Graph resource.

        :param graph_arn: The ARN of the Graph resource.
        :param graph_id: The GraphId of the Graph resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_neptunegraph as interfaces_neptunegraph
            
            graph_reference = interfaces_neptunegraph.GraphReference(
                graph_arn="graphArn",
                graph_id="graphId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__401f4219a143f0d18ff519d94a91d225890cda8d15e3db0ed99855f20240c907)
            check_type(argname="argument graph_arn", value=graph_arn, expected_type=type_hints["graph_arn"])
            check_type(argname="argument graph_id", value=graph_id, expected_type=type_hints["graph_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "graph_arn": graph_arn,
            "graph_id": graph_id,
        }

    @builtins.property
    def graph_arn(self) -> builtins.str:
        '''The ARN of the Graph resource.'''
        result = self._values.get("graph_arn")
        assert result is not None, "Required property 'graph_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def graph_id(self) -> builtins.str:
        '''The GraphId of the Graph resource.'''
        result = self._values.get("graph_id")
        assert result is not None, "Required property 'graph_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GraphReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_neptunegraph.IGraphRef")
class IGraphRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Graph.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="graphRef")
    def graph_ref(self) -> "GraphReference":
        '''(experimental) A reference to a Graph resource.

        :stability: experimental
        '''
        ...


class _IGraphRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Graph.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_neptunegraph.IGraphRef"

    @builtins.property
    @jsii.member(jsii_name="graphRef")
    def graph_ref(self) -> "GraphReference":
        '''(experimental) A reference to a Graph resource.

        :stability: experimental
        '''
        return typing.cast("GraphReference", jsii.get(self, "graphRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGraphRef).__jsii_proxy_class__ = lambda : _IGraphRefProxy


@jsii.interface(
    jsii_type="aws-cdk-lib.interfaces.aws_neptunegraph.IPrivateGraphEndpointRef"
)
class IPrivateGraphEndpointRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a PrivateGraphEndpoint.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="privateGraphEndpointRef")
    def private_graph_endpoint_ref(self) -> "PrivateGraphEndpointReference":
        '''(experimental) A reference to a PrivateGraphEndpoint resource.

        :stability: experimental
        '''
        ...


class _IPrivateGraphEndpointRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a PrivateGraphEndpoint.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_neptunegraph.IPrivateGraphEndpointRef"

    @builtins.property
    @jsii.member(jsii_name="privateGraphEndpointRef")
    def private_graph_endpoint_ref(self) -> "PrivateGraphEndpointReference":
        '''(experimental) A reference to a PrivateGraphEndpoint resource.

        :stability: experimental
        '''
        return typing.cast("PrivateGraphEndpointReference", jsii.get(self, "privateGraphEndpointRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrivateGraphEndpointRef).__jsii_proxy_class__ = lambda : _IPrivateGraphEndpointRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_neptunegraph.PrivateGraphEndpointReference",
    jsii_struct_bases=[],
    name_mapping={
        "private_graph_endpoint_identifier": "privateGraphEndpointIdentifier",
    },
)
class PrivateGraphEndpointReference:
    def __init__(self, *, private_graph_endpoint_identifier: builtins.str) -> None:
        '''A reference to a PrivateGraphEndpoint resource.

        :param private_graph_endpoint_identifier: The PrivateGraphEndpointIdentifier of the PrivateGraphEndpoint resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_neptunegraph as interfaces_neptunegraph
            
            private_graph_endpoint_reference = interfaces_neptunegraph.PrivateGraphEndpointReference(
                private_graph_endpoint_identifier="privateGraphEndpointIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__165df245cdebb6d7603090b9a3b7a84c382733456814a2820d93b1ac9b005307)
            check_type(argname="argument private_graph_endpoint_identifier", value=private_graph_endpoint_identifier, expected_type=type_hints["private_graph_endpoint_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "private_graph_endpoint_identifier": private_graph_endpoint_identifier,
        }

    @builtins.property
    def private_graph_endpoint_identifier(self) -> builtins.str:
        '''The PrivateGraphEndpointIdentifier of the PrivateGraphEndpoint resource.'''
        result = self._values.get("private_graph_endpoint_identifier")
        assert result is not None, "Required property 'private_graph_endpoint_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateGraphEndpointReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GraphReference",
    "IGraphRef",
    "IPrivateGraphEndpointRef",
    "PrivateGraphEndpointReference",
]

publication.publish()

def _typecheckingstub__401f4219a143f0d18ff519d94a91d225890cda8d15e3db0ed99855f20240c907(
    *,
    graph_arn: builtins.str,
    graph_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__165df245cdebb6d7603090b9a3b7a84c382733456814a2820d93b1ac9b005307(
    *,
    private_graph_endpoint_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IGraphRef, IPrivateGraphEndpointRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
