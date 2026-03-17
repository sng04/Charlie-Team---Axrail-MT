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
    jsii_type="aws-cdk-lib.interfaces.aws_omics.AnnotationStoreReference",
    jsii_struct_bases=[],
    name_mapping={"annotation_store_name": "annotationStoreName"},
)
class AnnotationStoreReference:
    def __init__(self, *, annotation_store_name: builtins.str) -> None:
        '''A reference to a AnnotationStore resource.

        :param annotation_store_name: The Name of the AnnotationStore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_omics as interfaces_omics
            
            annotation_store_reference = interfaces_omics.AnnotationStoreReference(
                annotation_store_name="annotationStoreName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__430e4feb750862574ea45c9c05b0ad5b146c26a568b63a51016e4499db2e690d)
            check_type(argname="argument annotation_store_name", value=annotation_store_name, expected_type=type_hints["annotation_store_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "annotation_store_name": annotation_store_name,
        }

    @builtins.property
    def annotation_store_name(self) -> builtins.str:
        '''The Name of the AnnotationStore resource.'''
        result = self._values.get("annotation_store_name")
        assert result is not None, "Required property 'annotation_store_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AnnotationStoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_omics.IAnnotationStoreRef")
class IAnnotationStoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a AnnotationStore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="annotationStoreRef")
    def annotation_store_ref(self) -> "AnnotationStoreReference":
        '''(experimental) A reference to a AnnotationStore resource.

        :stability: experimental
        '''
        ...


class _IAnnotationStoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a AnnotationStore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_omics.IAnnotationStoreRef"

    @builtins.property
    @jsii.member(jsii_name="annotationStoreRef")
    def annotation_store_ref(self) -> "AnnotationStoreReference":
        '''(experimental) A reference to a AnnotationStore resource.

        :stability: experimental
        '''
        return typing.cast("AnnotationStoreReference", jsii.get(self, "annotationStoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAnnotationStoreRef).__jsii_proxy_class__ = lambda : _IAnnotationStoreRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_omics.IReferenceStoreRef")
class IReferenceStoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a ReferenceStore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="referenceStoreRef")
    def reference_store_ref(self) -> "ReferenceStoreReference":
        '''(experimental) A reference to a ReferenceStore resource.

        :stability: experimental
        '''
        ...


class _IReferenceStoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a ReferenceStore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_omics.IReferenceStoreRef"

    @builtins.property
    @jsii.member(jsii_name="referenceStoreRef")
    def reference_store_ref(self) -> "ReferenceStoreReference":
        '''(experimental) A reference to a ReferenceStore resource.

        :stability: experimental
        '''
        return typing.cast("ReferenceStoreReference", jsii.get(self, "referenceStoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReferenceStoreRef).__jsii_proxy_class__ = lambda : _IReferenceStoreRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_omics.IRunGroupRef")
class IRunGroupRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a RunGroup.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="runGroupRef")
    def run_group_ref(self) -> "RunGroupReference":
        '''(experimental) A reference to a RunGroup resource.

        :stability: experimental
        '''
        ...


class _IRunGroupRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a RunGroup.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_omics.IRunGroupRef"

    @builtins.property
    @jsii.member(jsii_name="runGroupRef")
    def run_group_ref(self) -> "RunGroupReference":
        '''(experimental) A reference to a RunGroup resource.

        :stability: experimental
        '''
        return typing.cast("RunGroupReference", jsii.get(self, "runGroupRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRunGroupRef).__jsii_proxy_class__ = lambda : _IRunGroupRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_omics.ISequenceStoreRef")
class ISequenceStoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a SequenceStore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="sequenceStoreRef")
    def sequence_store_ref(self) -> "SequenceStoreReference":
        '''(experimental) A reference to a SequenceStore resource.

        :stability: experimental
        '''
        ...


class _ISequenceStoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a SequenceStore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_omics.ISequenceStoreRef"

    @builtins.property
    @jsii.member(jsii_name="sequenceStoreRef")
    def sequence_store_ref(self) -> "SequenceStoreReference":
        '''(experimental) A reference to a SequenceStore resource.

        :stability: experimental
        '''
        return typing.cast("SequenceStoreReference", jsii.get(self, "sequenceStoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISequenceStoreRef).__jsii_proxy_class__ = lambda : _ISequenceStoreRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_omics.IVariantStoreRef")
class IVariantStoreRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a VariantStore.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="variantStoreRef")
    def variant_store_ref(self) -> "VariantStoreReference":
        '''(experimental) A reference to a VariantStore resource.

        :stability: experimental
        '''
        ...


class _IVariantStoreRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a VariantStore.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_omics.IVariantStoreRef"

    @builtins.property
    @jsii.member(jsii_name="variantStoreRef")
    def variant_store_ref(self) -> "VariantStoreReference":
        '''(experimental) A reference to a VariantStore resource.

        :stability: experimental
        '''
        return typing.cast("VariantStoreReference", jsii.get(self, "variantStoreRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVariantStoreRef).__jsii_proxy_class__ = lambda : _IVariantStoreRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_omics.IWorkflowRef")
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

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_omics.IWorkflowRef"

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "WorkflowReference":
        '''(experimental) A reference to a Workflow resource.

        :stability: experimental
        '''
        return typing.cast("WorkflowReference", jsii.get(self, "workflowRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkflowRef).__jsii_proxy_class__ = lambda : _IWorkflowRefProxy


@jsii.interface(jsii_type="aws-cdk-lib.interfaces.aws_omics.IWorkflowVersionRef")
class IWorkflowVersionRef(
    _constructs_77d1e7e8.IConstruct,
    _IEnvironmentAware_f39049ee,
    typing_extensions.Protocol,
):
    '''(experimental) Indicates that this resource can be referenced as a WorkflowVersion.

    :stability: experimental
    '''

    @builtins.property
    @jsii.member(jsii_name="workflowVersionRef")
    def workflow_version_ref(self) -> "WorkflowVersionReference":
        '''(experimental) A reference to a WorkflowVersion resource.

        :stability: experimental
        '''
        ...


class _IWorkflowVersionRefProxy(
    jsii.proxy_for(_constructs_77d1e7e8.IConstruct), # type: ignore[misc]
    jsii.proxy_for(_IEnvironmentAware_f39049ee), # type: ignore[misc]
):
    '''(experimental) Indicates that this resource can be referenced as a WorkflowVersion.

    :stability: experimental
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.interfaces.aws_omics.IWorkflowVersionRef"

    @builtins.property
    @jsii.member(jsii_name="workflowVersionRef")
    def workflow_version_ref(self) -> "WorkflowVersionReference":
        '''(experimental) A reference to a WorkflowVersion resource.

        :stability: experimental
        '''
        return typing.cast("WorkflowVersionReference", jsii.get(self, "workflowVersionRef"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IWorkflowVersionRef).__jsii_proxy_class__ = lambda : _IWorkflowVersionRefProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_omics.ReferenceStoreReference",
    jsii_struct_bases=[],
    name_mapping={
        "reference_store_arn": "referenceStoreArn",
        "reference_store_id": "referenceStoreId",
    },
)
class ReferenceStoreReference:
    def __init__(
        self,
        *,
        reference_store_arn: builtins.str,
        reference_store_id: builtins.str,
    ) -> None:
        '''A reference to a ReferenceStore resource.

        :param reference_store_arn: The ARN of the ReferenceStore resource.
        :param reference_store_id: The ReferenceStoreId of the ReferenceStore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_omics as interfaces_omics
            
            reference_store_reference = interfaces_omics.ReferenceStoreReference(
                reference_store_arn="referenceStoreArn",
                reference_store_id="referenceStoreId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d5e6b3446d103ff66f8fb19cc638248e5c8ef4e0c53327e381eb65a8d2d7074)
            check_type(argname="argument reference_store_arn", value=reference_store_arn, expected_type=type_hints["reference_store_arn"])
            check_type(argname="argument reference_store_id", value=reference_store_id, expected_type=type_hints["reference_store_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "reference_store_arn": reference_store_arn,
            "reference_store_id": reference_store_id,
        }

    @builtins.property
    def reference_store_arn(self) -> builtins.str:
        '''The ARN of the ReferenceStore resource.'''
        result = self._values.get("reference_store_arn")
        assert result is not None, "Required property 'reference_store_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reference_store_id(self) -> builtins.str:
        '''The ReferenceStoreId of the ReferenceStore resource.'''
        result = self._values.get("reference_store_id")
        assert result is not None, "Required property 'reference_store_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReferenceStoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_omics.RunGroupReference",
    jsii_struct_bases=[],
    name_mapping={"run_group_arn": "runGroupArn", "run_group_id": "runGroupId"},
)
class RunGroupReference:
    def __init__(
        self,
        *,
        run_group_arn: builtins.str,
        run_group_id: builtins.str,
    ) -> None:
        '''A reference to a RunGroup resource.

        :param run_group_arn: The ARN of the RunGroup resource.
        :param run_group_id: The Id of the RunGroup resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_omics as interfaces_omics
            
            run_group_reference = interfaces_omics.RunGroupReference(
                run_group_arn="runGroupArn",
                run_group_id="runGroupId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59b5c9f7bd7475042c1b8681f3ca9e34da03e6def192139ee2def162d86ea178)
            check_type(argname="argument run_group_arn", value=run_group_arn, expected_type=type_hints["run_group_arn"])
            check_type(argname="argument run_group_id", value=run_group_id, expected_type=type_hints["run_group_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "run_group_arn": run_group_arn,
            "run_group_id": run_group_id,
        }

    @builtins.property
    def run_group_arn(self) -> builtins.str:
        '''The ARN of the RunGroup resource.'''
        result = self._values.get("run_group_arn")
        assert result is not None, "Required property 'run_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def run_group_id(self) -> builtins.str:
        '''The Id of the RunGroup resource.'''
        result = self._values.get("run_group_id")
        assert result is not None, "Required property 'run_group_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RunGroupReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_omics.SequenceStoreReference",
    jsii_struct_bases=[],
    name_mapping={
        "sequence_store_arn": "sequenceStoreArn",
        "sequence_store_id": "sequenceStoreId",
    },
)
class SequenceStoreReference:
    def __init__(
        self,
        *,
        sequence_store_arn: builtins.str,
        sequence_store_id: builtins.str,
    ) -> None:
        '''A reference to a SequenceStore resource.

        :param sequence_store_arn: The ARN of the SequenceStore resource.
        :param sequence_store_id: The SequenceStoreId of the SequenceStore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_omics as interfaces_omics
            
            sequence_store_reference = interfaces_omics.SequenceStoreReference(
                sequence_store_arn="sequenceStoreArn",
                sequence_store_id="sequenceStoreId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c363a4fdb78d86ba909b958577450f0c5eff9576d66c114df711fd23a0c2565)
            check_type(argname="argument sequence_store_arn", value=sequence_store_arn, expected_type=type_hints["sequence_store_arn"])
            check_type(argname="argument sequence_store_id", value=sequence_store_id, expected_type=type_hints["sequence_store_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sequence_store_arn": sequence_store_arn,
            "sequence_store_id": sequence_store_id,
        }

    @builtins.property
    def sequence_store_arn(self) -> builtins.str:
        '''The ARN of the SequenceStore resource.'''
        result = self._values.get("sequence_store_arn")
        assert result is not None, "Required property 'sequence_store_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sequence_store_id(self) -> builtins.str:
        '''The SequenceStoreId of the SequenceStore resource.'''
        result = self._values.get("sequence_store_id")
        assert result is not None, "Required property 'sequence_store_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SequenceStoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_omics.VariantStoreReference",
    jsii_struct_bases=[],
    name_mapping={"variant_store_name": "variantStoreName"},
)
class VariantStoreReference:
    def __init__(self, *, variant_store_name: builtins.str) -> None:
        '''A reference to a VariantStore resource.

        :param variant_store_name: The Name of the VariantStore resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_omics as interfaces_omics
            
            variant_store_reference = interfaces_omics.VariantStoreReference(
                variant_store_name="variantStoreName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cc5f944c024a1a7de0edcaaf4f42adefaa1e14f7f6b71e0c6e0ffd6b15f48d7)
            check_type(argname="argument variant_store_name", value=variant_store_name, expected_type=type_hints["variant_store_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "variant_store_name": variant_store_name,
        }

    @builtins.property
    def variant_store_name(self) -> builtins.str:
        '''The Name of the VariantStore resource.'''
        result = self._values.get("variant_store_name")
        assert result is not None, "Required property 'variant_store_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VariantStoreReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_omics.WorkflowReference",
    jsii_struct_bases=[],
    name_mapping={"workflow_arn": "workflowArn", "workflow_id": "workflowId"},
)
class WorkflowReference:
    def __init__(
        self,
        *,
        workflow_arn: builtins.str,
        workflow_id: builtins.str,
    ) -> None:
        '''A reference to a Workflow resource.

        :param workflow_arn: The ARN of the Workflow resource.
        :param workflow_id: The Id of the Workflow resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_omics as interfaces_omics
            
            workflow_reference = interfaces_omics.WorkflowReference(
                workflow_arn="workflowArn",
                workflow_id="workflowId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a8363eb67a98b72d0a27e742b5fd66c62e434c673f2ea860480756e98b48ea5)
            check_type(argname="argument workflow_arn", value=workflow_arn, expected_type=type_hints["workflow_arn"])
            check_type(argname="argument workflow_id", value=workflow_id, expected_type=type_hints["workflow_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workflow_arn": workflow_arn,
            "workflow_id": workflow_id,
        }

    @builtins.property
    def workflow_arn(self) -> builtins.str:
        '''The ARN of the Workflow resource.'''
        result = self._values.get("workflow_arn")
        assert result is not None, "Required property 'workflow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workflow_id(self) -> builtins.str:
        '''The Id of the Workflow resource.'''
        result = self._values.get("workflow_id")
        assert result is not None, "Required property 'workflow_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.interfaces.aws_omics.WorkflowVersionReference",
    jsii_struct_bases=[],
    name_mapping={"workflow_version_arn": "workflowVersionArn"},
)
class WorkflowVersionReference:
    def __init__(self, *, workflow_version_arn: builtins.str) -> None:
        '''A reference to a WorkflowVersion resource.

        :param workflow_version_arn: The Arn of the WorkflowVersion resource.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk.interfaces import aws_omics as interfaces_omics
            
            workflow_version_reference = interfaces_omics.WorkflowVersionReference(
                workflow_version_arn="workflowVersionArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4351d465b39f1db743cbdd04337465acfe258d84589dd69fb981206603c3add0)
            check_type(argname="argument workflow_version_arn", value=workflow_version_arn, expected_type=type_hints["workflow_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "workflow_version_arn": workflow_version_arn,
        }

    @builtins.property
    def workflow_version_arn(self) -> builtins.str:
        '''The Arn of the WorkflowVersion resource.'''
        result = self._values.get("workflow_version_arn")
        assert result is not None, "Required property 'workflow_version_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkflowVersionReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AnnotationStoreReference",
    "IAnnotationStoreRef",
    "IReferenceStoreRef",
    "IRunGroupRef",
    "ISequenceStoreRef",
    "IVariantStoreRef",
    "IWorkflowRef",
    "IWorkflowVersionRef",
    "ReferenceStoreReference",
    "RunGroupReference",
    "SequenceStoreReference",
    "VariantStoreReference",
    "WorkflowReference",
    "WorkflowVersionReference",
]

publication.publish()

def _typecheckingstub__430e4feb750862574ea45c9c05b0ad5b146c26a568b63a51016e4499db2e690d(
    *,
    annotation_store_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d5e6b3446d103ff66f8fb19cc638248e5c8ef4e0c53327e381eb65a8d2d7074(
    *,
    reference_store_arn: builtins.str,
    reference_store_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59b5c9f7bd7475042c1b8681f3ca9e34da03e6def192139ee2def162d86ea178(
    *,
    run_group_arn: builtins.str,
    run_group_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c363a4fdb78d86ba909b958577450f0c5eff9576d66c114df711fd23a0c2565(
    *,
    sequence_store_arn: builtins.str,
    sequence_store_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cc5f944c024a1a7de0edcaaf4f42adefaa1e14f7f6b71e0c6e0ffd6b15f48d7(
    *,
    variant_store_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a8363eb67a98b72d0a27e742b5fd66c62e434c673f2ea860480756e98b48ea5(
    *,
    workflow_arn: builtins.str,
    workflow_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4351d465b39f1db743cbdd04337465acfe258d84589dd69fb981206603c3add0(
    *,
    workflow_version_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

for cls in [IAnnotationStoreRef, IReferenceStoreRef, IRunGroupRef, ISequenceStoreRef, IVariantStoreRef, IWorkflowRef, IWorkflowVersionRef]:
    typing.cast(typing.Any, cls).__protocol_attrs__ = typing.cast(typing.Any, cls).__protocol_attrs__ - set(['__jsii_proxy_class__', '__jsii_type__'])
