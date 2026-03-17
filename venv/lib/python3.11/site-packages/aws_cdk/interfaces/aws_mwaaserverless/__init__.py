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


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_mwaaserverless.IWorkflowRef")
class IWorkflowRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a Workflow.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        ...


class _IWorkflowRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a Workflow.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_mwaaserverless.IWorkflowRef"

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        return typing.cast("WorkflowReference", jsii.get(self, "workflowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkflowRef).__jsii_proxy_class__ = lambda : _IWorkflowRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_mwaaserverless.WorkflowReference",
    jsii_struct_bases=[],
    name_mapping={"workflow_arn": "workflowArn"},
)
class WorkflowReference:
    def __init__(self, *, workflow_arn: builtins.str) -> None:
        '''A reference to a Workflow resource.

        :param workflow_arn: The WorkflowArn of the Workflow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_mwaaserverless as interfaces_mwaaserverless
            
            workflow_reference = interfaces_mwaaserverless.WorkflowReference(
                workflow_arn="workflowArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65acb1560dbb330b20abcd36181f2e001973c8230c1f53e44464a26b50152850)
            check_type(argname="argument workflow_arn", value=workflow_arn, expected_type=type_hints["workflow_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workflow_arn": workflow_arn,
        }

    @builtins.property
    def workflow_arn(self) -> builtins.str:
        '''The WorkflowArn of the Workflow resource.'''
        result = self._values.get("workflow_arn")
        assert result is not None, "Required property 'workflow_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "IWorkflowRef",
    "WorkflowReference",
]

publication.publish()

def _typecheckingstub__65acb1560dbb330b20abcd36181f2e001973c8230c1f53e44464a26b50152850(
    *,
    workflow_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IWorkflowRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
