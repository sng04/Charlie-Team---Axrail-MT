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
    jsii_type="aws-cdk-lib.interfaces.aws_managedblockchain.AccessorReference",
    jsii_struct_bases=[],
    name_mapping={"accessor_arn": "accessorArn", "accessor_id": "accessorId"},
)
class AccessorReference:
    def __init__(
        self,
        *,
        accessor_arn: builtins.str,
        accessor_id: builtins.str,
    ) -> None:
        '''A reference to a Accessor resource.

        :param accessor_arn: The ARN of the Accessor resource.
        :param accessor_id: The Id of the Accessor resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_managedblockchain as interfaces_managedblockchain
            
            accessor_reference = interfaces_managedblockchain.AccessorReference(
                accessor_arn="accessorArn",
                accessor_id="accessorId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__470e9c36096d8537a9bb6a205b998d45b83f117a8ad8fdd497e847df9798931a)
            check_type(argname="argument accessor_arn", value=accessor_arn, expected_type=type_hints["accessor_arn"])
            check_type(argname="argument accessor_id", value=accessor_id, expected_type=type_hints["accessor_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "accessor_arn": accessor_arn,
            "accessor_id": accessor_id,
        }

    @builtins.property
    def accessor_arn(self) -> builtins.str:
        '''The ARN of the Accessor resource.'''
        result = self._values.get("accessor_arn")
        assert result is not None, "Required property 'accessor_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accessor_id(self) -> builtins.str:
        '''The Id of the Accessor resource.'''
        result = self._values.get("accessor_id")
        assert result is not None, "Required property 'accessor_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AccessorReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_managedblockchain.IAccessorRef")
class IAccessorRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Accessor.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="accessorRef")
    def accessor_ref(self) -> "AccessorReference":
        '''(experimental) A reference to a Accessor resource.

        :stability: experimental
        '''
        ...


class _IAccessorRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Accessor.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_managedblockchain.IAccessorRef"

    @builtins.property
    @jsii.member(jsii_name="accessorRef")
    def accessor_ref(self) -> "AccessorReference":
        '''(experimental) A reference to a Accessor resource.

        :stability: experimental
        '''
        return typing.cast("AccessorReference", jsii.get(self, "accessorRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAccessorRef).__jsii_proxy_class__ = lambda : _IAccessorRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_managedblockchain.IMemberRef")
class IMemberRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Member.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="memberRef")
    def member_ref(self) -> "MemberReference":
        '''(experimental) A reference to a Member resource.

        :stability: experimental
        '''
        ...


class _IMemberRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Member.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_managedblockchain.IMemberRef"

    @builtins.property
    @jsii.member(jsii_name="memberRef")
    def member_ref(self) -> "MemberReference":
        '''(experimental) A reference to a Member resource.

        :stability: experimental
        '''
        return typing.cast("MemberReference", jsii.get(self, "memberRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IMemberRef).__jsii_proxy_class__ = lambda : _IMemberRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_managedblockchain.INodeRef")
class INodeRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Node.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="nodeRef")
    def node_ref(self) -> "NodeReference":
        '''(experimental) A reference to a Node resource.

        :stability: experimental
        '''
        ...


class _INodeRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Node.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_managedblockchain.INodeRef"

    @builtins.property
    @jsii.member(jsii_name="nodeRef")
    def node_ref(self) -> "NodeReference":
        '''(experimental) A reference to a Node resource.

        :stability: experimental
        '''
        return typing.cast("NodeReference", jsii.get(self, "nodeRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, INodeRef).__jsii_proxy_class__ = lambda : _INodeRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_managedblockchain.MemberReference",
    jsii_struct_bases=[],
    name_mapping={"member_id": "memberId"},
)
class MemberReference:
    def __init__(self, *, member_id: builtins.str) -> None:
        '''A reference to a Member resource.

        :param member_id: The MemberId of the Member resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_managedblockchain as interfaces_managedblockchain
            
            member_reference = interfaces_managedblockchain.MemberReference(
                member_id="memberId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53756b8941eb9962b342ccd85c785fd9597bbceea551caf229a648604856c320)
            check_type(argname="argument member_id", value=member_id, expected_type=type_hints["member_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "member_id": member_id,
        }

    @builtins.property
    def member_id(self) -> builtins.str:
        '''The MemberId of the Member resource.'''
        result = self._values.get("member_id")
        assert result is not None, "Required property 'member_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MemberReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_managedblockchain.NodeReference",
    jsii_struct_bases=[],
    name_mapping={"node_arn": "nodeArn", "node_id": "nodeId"},
)
class NodeReference:
    def __init__(self, *, node_arn: builtins.str, node_id: builtins.str) -> None:
        '''A reference to a Node resource.

        :param node_arn: The ARN of the Node resource.
        :param node_id: The NodeId of the Node resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_managedblockchain as interfaces_managedblockchain
            
            node_reference = interfaces_managedblockchain.NodeReference(
                node_arn="nodeArn",
                node_id="nodeId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10ea42cfcf642197710289601db4289fcb781e6ee46ac2c60d215f584a3121f2)
            check_type(argname="argument node_arn", value=node_arn, expected_type=type_hints["node_arn"])
            check_type(argname="argument node_id", value=node_id, expected_type=type_hints["node_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "node_arn": node_arn,
            "node_id": node_id,
        }

    @builtins.property
    def node_arn(self) -> builtins.str:
        '''The ARN of the Node resource.'''
        result = self._values.get("node_arn")
        assert result is not None, "Required property 'node_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_id(self) -> builtins.str:
        '''The NodeId of the Node resource.'''
        result = self._values.get("node_id")
        assert result is not None, "Required property 'node_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NodeReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AccessorReference",
    "IAccessorRef",
    "IMemberRef",
    "INodeRef",
    "MemberReference",
    "NodeReference",
]

publication.publish()

def _typecheckingstub__470e9c36096d8537a9bb6a205b998d45b83f117a8ad8fdd497e847df9798931a(
    *,
    accessor_arn: builtins.str,
    accessor_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53756b8941eb9962b342ccd85c785fd9597bbceea551caf229a648604856c320(
    *,
    member_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10ea42cfcf642197710289601db4289fcb781e6ee46ac2c60d215f584a3121f2(
    *,
    node_arn: builtins.str,
    node_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAccessorRef, IMemberRef, INodeRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
