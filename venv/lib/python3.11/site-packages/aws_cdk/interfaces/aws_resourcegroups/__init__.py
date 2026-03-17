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
    jsii_type="aws-cdk-lib.interfaces.aws_resourcegroups.GroupReference",
    jsii_struct_bases=[],
    name_mapping={"group_arn": "groupArn", "group_name": "groupName"},
)
class GroupReference:
    def __init__(self, *, group_arn: builtins.str, group_name: builtins.str) -> None:
        '''A reference to a Group resource.

        :param group_arn: The ARN of the Group resource.
        :param group_name: The Name of the Group resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_resourcegroups as interfaces_resourcegroups
            
            group_reference = interfaces_resourcegroups.GroupReference(
                group_arn="groupArn",
                group_name="groupName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de96f869c9839fec47adcfb2b629bd6ec6748bdb184fe9309c855ff3375594ed)
            check_type(argname="argument group_arn", value=group_arn, expected_type=type_hints["group_arn"])
            check_type(argname="argument group_name", value=group_name, expected_type=type_hints["group_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "group_arn": group_arn,
            "group_name": group_name,
        }

    @builtins.property
    def group_arn(self) -> builtins.str:
        '''The ARN of the Group resource.'''
        result = self._values.get("group_arn")
        assert result is not None, "Required property 'group_arn' is missing"
        return typing.cast(builtins.str, result)

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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_resourcegroups.IGroupRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_resourcegroups.IGroupRef"

    @builtins.property
    @jsii.member(jsii_name="groupRef")
    def group_ref(self) -> "GroupReference":
        '''(experimental) A reference to a Group resource.

        :stability: experimental
        '''
        return typing.cast("GroupReference", jsii.get(self, "groupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IGroupRef).__jsii_proxy_class__ = lambda : _IGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_resourcegroups.ITagSyncTaskRef")
class ITagSyncTaskRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a TagSyncTask.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="tagSyncTaskRef")
    def tag_sync_task_ref(self) -> "TagSyncTaskReference":
        '''(experimental) A reference to a TagSyncTask resource.

        :stability: experimental
        '''
        ...


class _ITagSyncTaskRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a TagSyncTask.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_resourcegroups.ITagSyncTaskRef"

    @builtins.property
    @jsii.member(jsii_name="tagSyncTaskRef")
    def tag_sync_task_ref(self) -> "TagSyncTaskReference":
        '''(experimental) A reference to a TagSyncTask resource.

        :stability: experimental
        '''
        return typing.cast("TagSyncTaskReference", jsii.get(self, "tagSyncTaskRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ITagSyncTaskRef).__jsii_proxy_class__ = lambda : _ITagSyncTaskRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_resourcegroups.TagSyncTaskReference",
    jsii_struct_bases=[],
    name_mapping={"task_arn": "taskArn"},
)
class TagSyncTaskReference:
    def __init__(self, *, task_arn: builtins.str) -> None:
        '''A reference to a TagSyncTask resource.

        :param task_arn: The TaskArn of the TagSyncTask resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_resourcegroups as interfaces_resourcegroups
            
            tag_sync_task_reference = interfaces_resourcegroups.TagSyncTaskReference(
                task_arn="taskArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7be762e0fa2ae57c29d2b33464ecdd38a60f5cd0ab37eaf86f0b039c8306af1)
            check_type(argname="argument task_arn", value=task_arn, expected_type=type_hints["task_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "task_arn": task_arn,
        }

    @builtins.property
    def task_arn(self) -> builtins.str:
        '''The TaskArn of the TagSyncTask resource.'''
        result = self._values.get("task_arn")
        assert result is not None, "Required property 'task_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TagSyncTaskReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GroupReference",
    "IGroupRef",
    "ITagSyncTaskRef",
    "TagSyncTaskReference",
]

publication.publish()

def _typecheckingstub__de96f869c9839fec47adcfb2b629bd6ec6748bdb184fe9309c855ff3375594ed(
    *,
    group_arn: builtins.str,
    group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7be762e0fa2ae57c29d2b33464ecdd38a60f5cd0ab37eaf86f0b039c8306af1(
    *,
    task_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IGroupRef, ITagSyncTaskRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
