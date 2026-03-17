r'''
# AWS::Omics Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_omics as omics
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Omics construct libraries](https://constructs.dev/search?q=omics)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Omics resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Omics.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Omics](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Omics.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
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

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_omics import (
    AnnotationStoreReference as _AnnotationStoreReference_bb5ff456,
    IAnnotationStoreRef as _IAnnotationStoreRef_c33c98b4,
    IReferenceStoreRef as _IReferenceStoreRef_e44b493e,
    IRunGroupRef as _IRunGroupRef_937b5363,
    ISequenceStoreRef as _ISequenceStoreRef_d8ce7b6b,
    IVariantStoreRef as _IVariantStoreRef_49e3cae7,
    IWorkflowRef as _IWorkflowRef_c34b3fa1,
    IWorkflowVersionRef as _IWorkflowVersionRef_8e877e7d,
    ReferenceStoreReference as _ReferenceStoreReference_0fa98700,
    RunGroupReference as _RunGroupReference_d14ed290,
    SequenceStoreReference as _SequenceStoreReference_12ae1dcf,
    VariantStoreReference as _VariantStoreReference_494e1db9,
    WorkflowReference as _WorkflowReference_d2d5c008,
    WorkflowVersionReference as _WorkflowVersionReference_1d5421a4,
)


@jsii.implements(_IInspectable_c2943556, _IAnnotationStoreRef_c33c98b4, _ITaggable_36806126)
class CfnAnnotationStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStore",
):
    '''.. epigraph::

   AWS HealthOmics variant stores and annotation stores are no longer open to new customers.

    Existing customers can continue to use the service as normal. For more information, see `AWS HealthOmics variant store and annotation store availability change <https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html>`_ .

    Creates an annotation store.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html
    :cloudformationResource: AWS::Omics::AnnotationStore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        # schema: Any
        
        cfn_annotation_store = omics.CfnAnnotationStore(self, "MyCfnAnnotationStore",
            name="name",
            store_format="storeFormat",
        
            # the properties below are optional
            description="description",
            reference=omics.CfnAnnotationStore.ReferenceItemProperty(
                reference_arn="referenceArn"
            ),
            sse_config=omics.CfnAnnotationStore.SseConfigProperty(
                type="type",
        
                # the properties below are optional
                key_arn="keyArn"
            ),
            store_options=omics.CfnAnnotationStore.StoreOptionsProperty(
                tsv_store_options=omics.CfnAnnotationStore.TsvStoreOptionsProperty(
                    annotation_type="annotationType",
                    format_to_header={
                        "format_to_header_key": "formatToHeader"
                    },
                    schema=schema
                )
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        store_format: builtins.str,
        description: typing.Optional[builtins.str] = None,
        reference: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnnotationStore.ReferenceItemProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sse_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnnotationStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        store_options: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnnotationStore.StoreOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Omics::AnnotationStore``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the Annotation Store.
        :param store_format: The annotation file format of the store.
        :param description: A description for the store.
        :param reference: The genome reference for the store's annotations.
        :param sse_config: The store's server-side encryption (SSE) settings.
        :param store_options: File parsing options for the annotation store.
        :param tags: Tags for the store.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5dcb906702f10b4a247a16c504ec605912264b052a73f0ae664d93bee73764)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAnnotationStoreProps(
            name=name,
            store_format=store_format,
            description=description,
            reference=reference,
            sse_config=sse_config,
            store_options=store_options,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForAnnotationStore")
    @builtins.classmethod
    def arn_for_annotation_store(
        cls,
        resource: "_IAnnotationStoreRef_c33c98b4",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d081c3f84956f6e383e1daee886fd75ec67836196a107b0828cceab885d95c55)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForAnnotationStore", [resource]))

    @jsii.member(jsii_name="fromAnnotationStoreName")
    @builtins.classmethod
    def from_annotation_store_name(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        annotation_store_name: builtins.str,
    ) -> "_IAnnotationStoreRef_c33c98b4":
        '''Creates a new IAnnotationStoreRef from a annotationStoreName.

        :param scope: -
        :param id: -
        :param annotation_store_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea8d23b9f77f5d9216bba34b2f07ff06220a6053227128a855b380a90746d1fe)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument annotation_store_name", value=annotation_store_name, expected_type=type_hints["annotation_store_name"])
        return typing.cast("_IAnnotationStoreRef_c33c98b4", jsii.sinvoke(cls, "fromAnnotationStoreName", [scope, id, annotation_store_name]))

    @jsii.member(jsii_name="isCfnAnnotationStore")
    @builtins.classmethod
    def is_cfn_annotation_store(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnAnnotationStore.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e5f634e0e551a9001147ebab16825824c6f25bedd18bb12f684ba868eccebf2)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnAnnotationStore", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d66bbde88d332dceb0812bb6bbf08c2418490d8b0e9774a97971a3b895f48b8)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa50ba289bb96ea508cb6a4202ffc1689e383887b754b989d8350c1e79bdf41c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="annotationStoreRef")
    def annotation_store_ref(self) -> "_AnnotationStoreReference_bb5ff456":
        '''A reference to a AnnotationStore resource.'''
        return typing.cast("_AnnotationStoreReference_bb5ff456", jsii.get(self, "annotationStoreRef"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the store was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The store's ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The store's status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''The store's status message.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property
    @jsii.member(jsii_name="attrStoreArn")
    def attr_store_arn(self) -> builtins.str:
        '''The store's ARN.

        :cloudformationAttribute: StoreArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStoreArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStoreSizeBytes")
    def attr_store_size_bytes(self) -> "_IResolvable_da3f097b":
        '''The store's size in bytes.

        :cloudformationAttribute: StoreSizeBytes
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrStoreSizeBytes"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''When the store was updated.

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the Annotation Store.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d9b73e29df1d36e34609deddf6492296be4ec0e0c99ae60a05f9cab95febd6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storeFormat")
    def store_format(self) -> builtins.str:
        '''The annotation file format of the store.'''
        return typing.cast(builtins.str, jsii.get(self, "storeFormat"))

    @store_format.setter
    def store_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39db05833c4ce77a84e366d7b58478b995b315232f05d9f9932602373f9c2c7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storeFormat", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bf53e865a22afeab85ecdb04fcf364678cf903b5624472147bf80f81f04730f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="reference")
    def reference(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.ReferenceItemProperty"]]:
        '''The genome reference for the store's annotations.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.ReferenceItemProperty"]], jsii.get(self, "reference"))

    @reference.setter
    def reference(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.ReferenceItemProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59c0d69a72a95b731117630b98efd8729539c64fef15303dab4addb9eae6ffa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reference", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sseConfig")
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.SseConfigProperty"]]:
        '''The store's server-side encryption (SSE) settings.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.SseConfigProperty"]], jsii.get(self, "sseConfig"))

    @sse_config.setter
    def sse_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.SseConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5edec3d71b0ff38cdce6ec8a872457ab8f95894314688d3b059e6b2fd20a3c07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storeOptions")
    def store_options(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.StoreOptionsProperty"]]:
        '''File parsing options for the annotation store.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.StoreOptionsProperty"]], jsii.get(self, "storeOptions"))

    @store_options.setter
    def store_options(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.StoreOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e84dfea35f835d11c086ac495c8e1952da55b4069d246ca2b527bb2a7655e94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storeOptions", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bd3f81b2e8f342de3db84fde3693c24cb6514a2f2b2e76534d5136fdc26945b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStore.ReferenceItemProperty",
        jsii_struct_bases=[],
        name_mapping={"reference_arn": "referenceArn"},
    )
    class ReferenceItemProperty:
        def __init__(self, *, reference_arn: builtins.str) -> None:
            '''A genome reference.

            :param reference_arn: The reference's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-referenceitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                reference_item_property = omics.CfnAnnotationStore.ReferenceItemProperty(
                    reference_arn="referenceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f161bf0df41584a24622d738207d338081faec41cddac7f0cda31f0cbf50b695)
                check_type(argname="argument reference_arn", value=reference_arn, expected_type=type_hints["reference_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "reference_arn": reference_arn,
            }

        @builtins.property
        def reference_arn(self) -> builtins.str:
            '''The reference's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-referenceitem.html#cfn-omics-annotationstore-referenceitem-referencearn
            '''
            result = self._values.get("reference_arn")
            assert result is not None, "Required property 'reference_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStore.SseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "key_arn": "keyArn"},
    )
    class SseConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Server-side encryption (SSE) settings for a store.

            :param type: The encryption type.
            :param key_arn: An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-sseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                sse_config_property = omics.CfnAnnotationStore.SseConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30b0283b46d5b34e1109c108b303d6ab3e549e041b5482192ec0ef37b83e6920)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def type(self) -> builtins.str:
            '''The encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-sseconfig.html#cfn-omics-annotationstore-sseconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-sseconfig.html#cfn-omics-annotationstore-sseconfig-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStore.StoreOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"tsv_store_options": "tsvStoreOptions"},
    )
    class StoreOptionsProperty:
        def __init__(
            self,
            *,
            tsv_store_options: typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnnotationStore.TsvStoreOptionsProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The store's file parsing options.

            :param tsv_store_options: Formatting options for a TSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-storeoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                # schema: Any
                
                store_options_property = omics.CfnAnnotationStore.StoreOptionsProperty(
                    tsv_store_options=omics.CfnAnnotationStore.TsvStoreOptionsProperty(
                        annotation_type="annotationType",
                        format_to_header={
                            "format_to_header_key": "formatToHeader"
                        },
                        schema=schema
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__68b9968e466757cfc2e4ee7eb053201b466a44d185aa6082edce78e859f4f489)
                check_type(argname="argument tsv_store_options", value=tsv_store_options, expected_type=type_hints["tsv_store_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "tsv_store_options": tsv_store_options,
            }

        @builtins.property
        def tsv_store_options(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.TsvStoreOptionsProperty"]:
            '''Formatting options for a TSV file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-storeoptions.html#cfn-omics-annotationstore-storeoptions-tsvstoreoptions
            '''
            result = self._values.get("tsv_store_options")
            assert result is not None, "Required property 'tsv_store_options' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.TsvStoreOptionsProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StoreOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStore.TsvStoreOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "annotation_type": "annotationType",
            "format_to_header": "formatToHeader",
            "schema": "schema",
        },
    )
    class TsvStoreOptionsProperty:
        def __init__(
            self,
            *,
            annotation_type: typing.Optional[builtins.str] = None,
            format_to_header: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]] = None,
            schema: typing.Any = None,
        ) -> None:
            '''The store's parsing options.

            :param annotation_type: The store's annotation type.
            :param format_to_header: The store's header key to column name mapping.
            :param schema: The schema of an annotation store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                # schema: Any
                
                tsv_store_options_property = omics.CfnAnnotationStore.TsvStoreOptionsProperty(
                    annotation_type="annotationType",
                    format_to_header={
                        "format_to_header_key": "formatToHeader"
                    },
                    schema=schema
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__14b0c73be5d34083c239713770a8134020bc8cab75d4b0a1a82a28463074bb3d)
                check_type(argname="argument annotation_type", value=annotation_type, expected_type=type_hints["annotation_type"])
                check_type(argname="argument format_to_header", value=format_to_header, expected_type=type_hints["format_to_header"])
                check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if annotation_type is not None:
                self._values["annotation_type"] = annotation_type
            if format_to_header is not None:
                self._values["format_to_header"] = format_to_header
            if schema is not None:
                self._values["schema"] = schema

        @builtins.property
        def annotation_type(self) -> typing.Optional[builtins.str]:
            '''The store's annotation type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html#cfn-omics-annotationstore-tsvstoreoptions-annotationtype
            '''
            result = self._values.get("annotation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def format_to_header(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]]:
            '''The store's header key to column name mapping.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html#cfn-omics-annotationstore-tsvstoreoptions-formattoheader
            '''
            result = self._values.get("format_to_header")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]], result)

        @builtins.property
        def schema(self) -> typing.Any:
            '''The schema of an annotation store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-annotationstore-tsvstoreoptions.html#cfn-omics-annotationstore-tsvstoreoptions-schema
            '''
            result = self._values.get("schema")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TsvStoreOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnAnnotationStoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "store_format": "storeFormat",
        "description": "description",
        "reference": "reference",
        "sse_config": "sseConfig",
        "store_options": "storeOptions",
        "tags": "tags",
    },
)
class CfnAnnotationStoreProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        store_format: builtins.str,
        description: typing.Optional[builtins.str] = None,
        reference: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnnotationStore.ReferenceItemProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sse_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnnotationStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        store_options: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnAnnotationStore.StoreOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAnnotationStore``.

        :param name: The name of the Annotation Store.
        :param store_format: The annotation file format of the store.
        :param description: A description for the store.
        :param reference: The genome reference for the store's annotations.
        :param sse_config: The store's server-side encryption (SSE) settings.
        :param store_options: File parsing options for the annotation store.
        :param tags: Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            # schema: Any
            
            cfn_annotation_store_props = omics.CfnAnnotationStoreProps(
                name="name",
                store_format="storeFormat",
            
                # the properties below are optional
                description="description",
                reference=omics.CfnAnnotationStore.ReferenceItemProperty(
                    reference_arn="referenceArn"
                ),
                sse_config=omics.CfnAnnotationStore.SseConfigProperty(
                    type="type",
            
                    # the properties below are optional
                    key_arn="keyArn"
                ),
                store_options=omics.CfnAnnotationStore.StoreOptionsProperty(
                    tsv_store_options=omics.CfnAnnotationStore.TsvStoreOptionsProperty(
                        annotation_type="annotationType",
                        format_to_header={
                            "format_to_header_key": "formatToHeader"
                        },
                        schema=schema
                    )
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db27a54e4b1e96ecf8263cf950eaa96b8620641082ddea726be734d30e205831)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument store_format", value=store_format, expected_type=type_hints["store_format"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument reference", value=reference, expected_type=type_hints["reference"])
            check_type(argname="argument sse_config", value=sse_config, expected_type=type_hints["sse_config"])
            check_type(argname="argument store_options", value=store_options, expected_type=type_hints["store_options"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "store_format": store_format,
        }
        if description is not None:
            self._values["description"] = description
        if reference is not None:
            self._values["reference"] = reference
        if sse_config is not None:
            self._values["sse_config"] = sse_config
        if store_options is not None:
            self._values["store_options"] = store_options
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the Annotation Store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def store_format(self) -> builtins.str:
        '''The annotation file format of the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-storeformat
        '''
        result = self._values.get("store_format")
        assert result is not None, "Required property 'store_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reference(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.ReferenceItemProperty"]]:
        '''The genome reference for the store's annotations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-reference
        '''
        result = self._values.get("reference")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.ReferenceItemProperty"]], result)

    @builtins.property
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.SseConfigProperty"]]:
        '''The store's server-side encryption (SSE) settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-sseconfig
        '''
        result = self._values.get("sse_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.SseConfigProperty"]], result)

    @builtins.property
    def store_options(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.StoreOptionsProperty"]]:
        '''File parsing options for the annotation store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-storeoptions
        '''
        result = self._values.get("store_options")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnAnnotationStore.StoreOptionsProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-annotationstore.html#cfn-omics-annotationstore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAnnotationStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IReferenceStoreRef_e44b493e, _ITaggable_36806126)
class CfnReferenceStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnReferenceStore",
):
    '''Creates a reference store.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html
    :cloudformationResource: AWS::Omics::ReferenceStore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        cfn_reference_store = omics.CfnReferenceStore(self, "MyCfnReferenceStore",
            name="name",
        
            # the properties below are optional
            description="description",
            sse_config=omics.CfnReferenceStore.SseConfigProperty(
                type="type",
        
                # the properties below are optional
                key_arn="keyArn"
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        sse_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnReferenceStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Omics::ReferenceStore``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the store.
        :param description: A description for the store.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e38c503967033ff76d3e45880727cc62a1df749cb0aac8298f6d06d14d6e3320)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReferenceStoreProps(
            name=name, description=description, sse_config=sse_config, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForReferenceStore")
    @builtins.classmethod
    def arn_for_reference_store(
        cls,
        resource: "_IReferenceStoreRef_e44b493e",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__183bf8595aa4fa216452da5239ca1639a58401e756cb23717c36ec75daa0a396)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForReferenceStore", [resource]))

    @jsii.member(jsii_name="fromReferenceStoreArn")
    @builtins.classmethod
    def from_reference_store_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IReferenceStoreRef_e44b493e":
        '''Creates a new IReferenceStoreRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03eab96b33743423157434263c495ecf4bb597bb49fcadef0690e503e3540689)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IReferenceStoreRef_e44b493e", jsii.sinvoke(cls, "fromReferenceStoreArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromReferenceStoreId")
    @builtins.classmethod
    def from_reference_store_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        reference_store_id: builtins.str,
    ) -> "_IReferenceStoreRef_e44b493e":
        '''Creates a new IReferenceStoreRef from a referenceStoreId.

        :param scope: -
        :param id: -
        :param reference_store_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d3a144262ad49c5d6ecb97bcdeda753c5514368bac2ab437b403dd5ecbff176)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument reference_store_id", value=reference_store_id, expected_type=type_hints["reference_store_id"])
        return typing.cast("_IReferenceStoreRef_e44b493e", jsii.sinvoke(cls, "fromReferenceStoreId", [scope, id, reference_store_id]))

    @jsii.member(jsii_name="isCfnReferenceStore")
    @builtins.classmethod
    def is_cfn_reference_store(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnReferenceStore.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37cb4b310cd2f37468be221e1f8c07466a5f9c1031fbf8c2b24f0722a58417c4)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnReferenceStore", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d75805be97b46dc8c38477db9eef63661d2478cb95cd31687daa2a21a351dfd)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a01b78cf451516a0eb2572826af339a051c95495f454b03b62693537679d6e9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The store's ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the store was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrReferenceStoreId")
    def attr_reference_store_id(self) -> builtins.str:
        '''The store's ID.

        :cloudformationAttribute: ReferenceStoreId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReferenceStoreId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="referenceStoreRef")
    def reference_store_ref(self) -> "_ReferenceStoreReference_0fa98700":
        '''A reference to a ReferenceStore resource.'''
        return typing.cast("_ReferenceStoreReference_0fa98700", jsii.get(self, "referenceStoreRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the store.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a1e17328f2c1518d508a235b2c42ef44e871bafb1772ad49e45f0b8d5583ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c89d0da98832090d35c5574aec7e23cd54990b36f1507999a687aed1e0a56bbb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sseConfig")
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnReferenceStore.SseConfigProperty"]]:
        '''Server-side encryption (SSE) settings for the store.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnReferenceStore.SseConfigProperty"]], jsii.get(self, "sseConfig"))

    @sse_config.setter
    def sse_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnReferenceStore.SseConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63bf4a022de72dc8d560891710d6dee497173e638e81419fd5d8b3c20d9a650b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5978dd78915de34b6caff418b41982c856f0f6071f77fc0f1306963a5cfe845e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnReferenceStore.SseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "key_arn": "keyArn"},
    )
    class SseConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Server-side encryption (SSE) settings for a store.

            :param type: The encryption type.
            :param key_arn: An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-referencestore-sseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                sse_config_property = omics.CfnReferenceStore.SseConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a277036a5a95a03f8b276d47ec8bcb3f25bf4f304bc5ee7452d8472c7e1ada3a)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def type(self) -> builtins.str:
            '''The encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-referencestore-sseconfig.html#cfn-omics-referencestore-sseconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-referencestore-sseconfig.html#cfn-omics-referencestore-sseconfig-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnReferenceStoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "sse_config": "sseConfig",
        "tags": "tags",
    },
)
class CfnReferenceStoreProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        sse_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnReferenceStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReferenceStore``.

        :param name: A name for the store.
        :param description: A description for the store.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            cfn_reference_store_props = omics.CfnReferenceStoreProps(
                name="name",
            
                # the properties below are optional
                description="description",
                sse_config=omics.CfnReferenceStore.SseConfigProperty(
                    type="type",
            
                    # the properties below are optional
                    key_arn="keyArn"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fa5ddefbb60b1902a7a8a0da56893c57cde7f27eb458a6b71907aad7ac2b4ca)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument sse_config", value=sse_config, expected_type=type_hints["sse_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if sse_config is not None:
            self._values["sse_config"] = sse_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnReferenceStore.SseConfigProperty"]]:
        '''Server-side encryption (SSE) settings for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-sseconfig
        '''
        result = self._values.get("sse_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnReferenceStore.SseConfigProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-referencestore.html#cfn-omics-referencestore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReferenceStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IRunGroupRef_937b5363, _ITaggable_36806126)
class CfnRunGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnRunGroup",
):
    '''Creates a run group to limit the compute resources for the runs that are added to the group.

    Returns an ARN, ID, and tags for the run group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html
    :cloudformationResource: AWS::Omics::RunGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        cfn_run_group = omics.CfnRunGroup(self, "MyCfnRunGroup",
            max_cpus=123,
            max_duration=123,
            max_gpus=123,
            max_runs=123,
            name="name",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        max_cpus: typing.Optional[jsii.Number] = None,
        max_duration: typing.Optional[jsii.Number] = None,
        max_gpus: typing.Optional[jsii.Number] = None,
        max_runs: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Omics::RunGroup``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param max_cpus: The group's maximum CPU count setting.
        :param max_duration: The group's maximum duration setting in minutes.
        :param max_gpus: The maximum GPUs that can be used by a run group.
        :param max_runs: The group's maximum concurrent run setting.
        :param name: The group's name.
        :param tags: Tags for the group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d92bdf2175b79063decd2ff3bbf2745e423b61fa98f3bf6b832b7632771b7e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRunGroupProps(
            max_cpus=max_cpus,
            max_duration=max_duration,
            max_gpus=max_gpus,
            max_runs=max_runs,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForRunGroup")
    @builtins.classmethod
    def arn_for_run_group(cls, resource: "_IRunGroupRef_937b5363") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db1a82ee01daefb6257f7e73e38ab5b5e98e001181ab9869f5d6dd18e3cc3993)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForRunGroup", [resource]))

    @jsii.member(jsii_name="isCfnRunGroup")
    @builtins.classmethod
    def is_cfn_run_group(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnRunGroup.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a98b2a8d393a5018138cf8c7c78a10435f63b2eea12b677df4c77fca4365013d)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnRunGroup", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34a9f76d09fa73ea3c0c86debaea039d1ecfeb5a751151276cc0002d8d2737c1)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61e5e671b78fea2bdc872b82befc94adc6014522a707589b79b6dc63795f14c0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The run group's ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the run group was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The run group's ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="runGroupRef")
    def run_group_ref(self) -> "_RunGroupReference_d14ed290":
        '''A reference to a RunGroup resource.'''
        return typing.cast("_RunGroupReference_d14ed290", jsii.get(self, "runGroupRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="maxCpus")
    def max_cpus(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum CPU count setting.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxCpus"))

    @max_cpus.setter
    def max_cpus(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2024f9c040e790d1988694b9f616763247d6b00f2fdcd97552dbe2c3cae45b40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxCpus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxDuration")
    def max_duration(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum duration setting in minutes.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxDuration"))

    @max_duration.setter
    def max_duration(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6aa9c45084b47d1e497a843bdc464ca31516a118303fa388c0f5db7b5bbd3630)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxDuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxGpus")
    def max_gpus(self) -> typing.Optional[jsii.Number]:
        '''The maximum GPUs that can be used by a run group.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxGpus"))

    @max_gpus.setter
    def max_gpus(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1884be9d7a33f4597167d89c5fb81946a94d32f6879e4877ffa669c1ef0f4f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxGpus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxRuns")
    def max_runs(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum concurrent run setting.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxRuns"))

    @max_runs.setter
    def max_runs(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__235fda5a64dcc62cd14ad311c90dce78abbc930ce336e74e69a63f027c84b0c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxRuns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The group's name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14846c448c724a5e0421b3370cbf6d8071cc9d1d1f7f635d8b528b854c1db3a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the group.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f64a1ae8ed7c7141ee2c0e9f12df462d424e227637fb190daac9751a95f18d1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnRunGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "max_cpus": "maxCpus",
        "max_duration": "maxDuration",
        "max_gpus": "maxGpus",
        "max_runs": "maxRuns",
        "name": "name",
        "tags": "tags",
    },
)
class CfnRunGroupProps:
    def __init__(
        self,
        *,
        max_cpus: typing.Optional[jsii.Number] = None,
        max_duration: typing.Optional[jsii.Number] = None,
        max_gpus: typing.Optional[jsii.Number] = None,
        max_runs: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRunGroup``.

        :param max_cpus: The group's maximum CPU count setting.
        :param max_duration: The group's maximum duration setting in minutes.
        :param max_gpus: The maximum GPUs that can be used by a run group.
        :param max_runs: The group's maximum concurrent run setting.
        :param name: The group's name.
        :param tags: Tags for the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            cfn_run_group_props = omics.CfnRunGroupProps(
                max_cpus=123,
                max_duration=123,
                max_gpus=123,
                max_runs=123,
                name="name",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0687d84f98238d006185c8fc00317ac96c5244d8d1b550e56fda04cb4eca97f9)
            check_type(argname="argument max_cpus", value=max_cpus, expected_type=type_hints["max_cpus"])
            check_type(argname="argument max_duration", value=max_duration, expected_type=type_hints["max_duration"])
            check_type(argname="argument max_gpus", value=max_gpus, expected_type=type_hints["max_gpus"])
            check_type(argname="argument max_runs", value=max_runs, expected_type=type_hints["max_runs"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if max_cpus is not None:
            self._values["max_cpus"] = max_cpus
        if max_duration is not None:
            self._values["max_duration"] = max_duration
        if max_gpus is not None:
            self._values["max_gpus"] = max_gpus
        if max_runs is not None:
            self._values["max_runs"] = max_runs
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def max_cpus(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum CPU count setting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxcpus
        '''
        result = self._values.get("max_cpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_duration(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum duration setting in minutes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxduration
        '''
        result = self._values.get("max_duration")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_gpus(self) -> typing.Optional[jsii.Number]:
        '''The maximum GPUs that can be used by a run group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxgpus
        '''
        result = self._values.get("max_gpus")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_runs(self) -> typing.Optional[jsii.Number]:
        '''The group's maximum concurrent run setting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-maxruns
        '''
        result = self._values.get("max_runs")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The group's name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-rungroup.html#cfn-omics-rungroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRunGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ISequenceStoreRef_d8ce7b6b, _ITaggable_36806126)
class CfnSequenceStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnSequenceStore",
):
    '''Creates a sequence store.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html
    :cloudformationResource: AWS::Omics::SequenceStore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        # s3_access_policy: Any
        
        cfn_sequence_store = omics.CfnSequenceStore(self, "MyCfnSequenceStore",
            name="name",
        
            # the properties below are optional
            access_log_location="accessLogLocation",
            description="description",
            e_tag_algorithm_family="eTagAlgorithmFamily",
            fallback_location="fallbackLocation",
            propagated_set_level_tags=["propagatedSetLevelTags"],
            s3_access_policy=s3_access_policy,
            sse_config=omics.CfnSequenceStore.SseConfigProperty(
                type="type",
        
                # the properties below are optional
                key_arn="keyArn"
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        access_log_location: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        e_tag_algorithm_family: typing.Optional[builtins.str] = None,
        fallback_location: typing.Optional[builtins.str] = None,
        propagated_set_level_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        s3_access_policy: typing.Any = None,
        sse_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSequenceStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Omics::SequenceStore``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the store.
        :param access_log_location: Location of the access logs.
        :param description: A description for the store.
        :param e_tag_algorithm_family: The algorithm family of the ETag.
        :param fallback_location: An S3 location that is used to store files that have failed a direct upload.
        :param propagated_set_level_tags: The tags keys to propagate to the S3 objects associated with read sets in the sequence store.
        :param s3_access_policy: The resource policy that controls S3 access on the store.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a589aadb7c598845d5e4c6ef138fe8cbeb7253209ba9eb0e5e590611eec980dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSequenceStoreProps(
            name=name,
            access_log_location=access_log_location,
            description=description,
            e_tag_algorithm_family=e_tag_algorithm_family,
            fallback_location=fallback_location,
            propagated_set_level_tags=propagated_set_level_tags,
            s3_access_policy=s3_access_policy,
            sse_config=sse_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSequenceStore")
    @builtins.classmethod
    def arn_for_sequence_store(
        cls,
        resource: "_ISequenceStoreRef_d8ce7b6b",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9a735aaa47b911b08cfd5af5019bd48d4f4d14bcdffa2fef80322b11f850d47)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSequenceStore", [resource]))

    @jsii.member(jsii_name="fromSequenceStoreArn")
    @builtins.classmethod
    def from_sequence_store_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_ISequenceStoreRef_d8ce7b6b":
        '''Creates a new ISequenceStoreRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0401ce1b5169b8a6f265ee186bf5ea3e78a0a8a2b71e6256e2a1effe74e148d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_ISequenceStoreRef_d8ce7b6b", jsii.sinvoke(cls, "fromSequenceStoreArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromSequenceStoreId")
    @builtins.classmethod
    def from_sequence_store_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        sequence_store_id: builtins.str,
    ) -> "_ISequenceStoreRef_d8ce7b6b":
        '''Creates a new ISequenceStoreRef from a sequenceStoreId.

        :param scope: -
        :param id: -
        :param sequence_store_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__939e1e0c5383ed843656a8c66c9eeac470cdb45344d2aa8c6353ab2273bb3618)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument sequence_store_id", value=sequence_store_id, expected_type=type_hints["sequence_store_id"])
        return typing.cast("_ISequenceStoreRef_d8ce7b6b", jsii.sinvoke(cls, "fromSequenceStoreId", [scope, id, sequence_store_id]))

    @jsii.member(jsii_name="isCfnSequenceStore")
    @builtins.classmethod
    def is_cfn_sequence_store(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSequenceStore.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d2570829ea1706cde1490e1a50299861f8a0479fe93d29fc4d8c19b41689f96)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSequenceStore", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea9a45fe9e84d5319386c1a777f6361e3fed5c916c543c8964323b54759ee470)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7932486ef43d64891becc28acf4d1c7abdf6063eb9aa69d9bffa95c24d2d9d9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The store's ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the store was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrS3AccessPointArn")
    def attr_s3_access_point_arn(self) -> builtins.str:
        '''This is ARN of the access point associated with the S3 bucket storing read sets.

        :cloudformationAttribute: S3AccessPointArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrS3AccessPointArn"))

    @builtins.property
    @jsii.member(jsii_name="attrS3Uri")
    def attr_s3_uri(self) -> builtins.str:
        '''The S3 URI of the sequence store.

        :cloudformationAttribute: S3Uri
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrS3Uri"))

    @builtins.property
    @jsii.member(jsii_name="attrSequenceStoreId")
    def attr_sequence_store_id(self) -> builtins.str:
        '''The store's ID.

        :cloudformationAttribute: SequenceStoreId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSequenceStoreId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Status of the sequence store.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''The status message of the sequence store.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''The last-updated time of the Sequence Store.

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="sequenceStoreRef")
    def sequence_store_ref(self) -> "_SequenceStoreReference_12ae1dcf":
        '''A reference to a SequenceStore resource.'''
        return typing.cast("_SequenceStoreReference_12ae1dcf", jsii.get(self, "sequenceStoreRef"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the store.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8e53b0b20084e7e23dc393ceafe95167d7bce2ef95f48e5bca0556a29d78fa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="accessLogLocation")
    def access_log_location(self) -> typing.Optional[builtins.str]:
        '''Location of the access logs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessLogLocation"))

    @access_log_location.setter
    def access_log_location(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7549c525ad472ac7db5f5282211a0aac7a47906e8ed893e7de2371f8677691f0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLogLocation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__128fafb1df9e961d7c5982e50a60c29fbada98403f437d20e8bab3669320ca5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="eTagAlgorithmFamily")
    def e_tag_algorithm_family(self) -> typing.Optional[builtins.str]:
        '''The algorithm family of the ETag.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "eTagAlgorithmFamily"))

    @e_tag_algorithm_family.setter
    def e_tag_algorithm_family(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0fd26684f557f3150b6eaf7b8b6f5ea741a5a2ba9e37d4a05ec66dea9e5c724)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eTagAlgorithmFamily", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fallbackLocation")
    def fallback_location(self) -> typing.Optional[builtins.str]:
        '''An S3 location that is used to store files that have failed a direct upload.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fallbackLocation"))

    @fallback_location.setter
    def fallback_location(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f87faaa51a41810707e9283275d0283e54c3ebebf2803e01abef2984151aca1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fallbackLocation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="propagatedSetLevelTags")
    def propagated_set_level_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The tags keys to propagate to the S3 objects associated with read sets in the sequence store.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "propagatedSetLevelTags"))

    @propagated_set_level_tags.setter
    def propagated_set_level_tags(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94d2835859304a00ff97481068a5f88aa75e5f963a8554869a9bb60a55200b93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "propagatedSetLevelTags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="s3AccessPolicy")
    def s3_access_policy(self) -> typing.Any:
        '''The resource policy that controls S3 access on the store.'''
        return typing.cast(typing.Any, jsii.get(self, "s3AccessPolicy"))

    @s3_access_policy.setter
    def s3_access_policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d38bc4fc98e65bd66719d736641dbe0eef30ad1a6a932a71665c6fd3c7a01c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3AccessPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sseConfig")
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSequenceStore.SseConfigProperty"]]:
        '''Server-side encryption (SSE) settings for the store.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSequenceStore.SseConfigProperty"]], jsii.get(self, "sseConfig"))

    @sse_config.setter
    def sse_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSequenceStore.SseConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92eed2332efa6d161a72ca8ae646e24cacee45f7acbbbb2e0aacb4b034c468be)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ce2c9ded7857e7f4d2115b4b17528bedb51685351fbcf322f7727f4fcf76354)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnSequenceStore.SseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "key_arn": "keyArn"},
    )
    class SseConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Server-side encryption (SSE) settings for a store.

            :param type: The encryption type.
            :param key_arn: An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-sequencestore-sseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                sse_config_property = omics.CfnSequenceStore.SseConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__16d14d56ac16dd0c8b7ee5046e40e324719a67cf46d9a70bdf176e614b6904fc)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def type(self) -> builtins.str:
            '''The encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-sequencestore-sseconfig.html#cfn-omics-sequencestore-sseconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-sequencestore-sseconfig.html#cfn-omics-sequencestore-sseconfig-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnSequenceStoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "access_log_location": "accessLogLocation",
        "description": "description",
        "e_tag_algorithm_family": "eTagAlgorithmFamily",
        "fallback_location": "fallbackLocation",
        "propagated_set_level_tags": "propagatedSetLevelTags",
        "s3_access_policy": "s3AccessPolicy",
        "sse_config": "sseConfig",
        "tags": "tags",
    },
)
class CfnSequenceStoreProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        access_log_location: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        e_tag_algorithm_family: typing.Optional[builtins.str] = None,
        fallback_location: typing.Optional[builtins.str] = None,
        propagated_set_level_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        s3_access_policy: typing.Any = None,
        sse_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSequenceStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSequenceStore``.

        :param name: A name for the store.
        :param access_log_location: Location of the access logs.
        :param description: A description for the store.
        :param e_tag_algorithm_family: The algorithm family of the ETag.
        :param fallback_location: An S3 location that is used to store files that have failed a direct upload.
        :param propagated_set_level_tags: The tags keys to propagate to the S3 objects associated with read sets in the sequence store.
        :param s3_access_policy: The resource policy that controls S3 access on the store.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            # s3_access_policy: Any
            
            cfn_sequence_store_props = omics.CfnSequenceStoreProps(
                name="name",
            
                # the properties below are optional
                access_log_location="accessLogLocation",
                description="description",
                e_tag_algorithm_family="eTagAlgorithmFamily",
                fallback_location="fallbackLocation",
                propagated_set_level_tags=["propagatedSetLevelTags"],
                s3_access_policy=s3_access_policy,
                sse_config=omics.CfnSequenceStore.SseConfigProperty(
                    type="type",
            
                    # the properties below are optional
                    key_arn="keyArn"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c912afa5be2bea750b085186b08f53bd688bc0a1dd08b1f1c6951a21015380fc)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument access_log_location", value=access_log_location, expected_type=type_hints["access_log_location"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument e_tag_algorithm_family", value=e_tag_algorithm_family, expected_type=type_hints["e_tag_algorithm_family"])
            check_type(argname="argument fallback_location", value=fallback_location, expected_type=type_hints["fallback_location"])
            check_type(argname="argument propagated_set_level_tags", value=propagated_set_level_tags, expected_type=type_hints["propagated_set_level_tags"])
            check_type(argname="argument s3_access_policy", value=s3_access_policy, expected_type=type_hints["s3_access_policy"])
            check_type(argname="argument sse_config", value=sse_config, expected_type=type_hints["sse_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if access_log_location is not None:
            self._values["access_log_location"] = access_log_location
        if description is not None:
            self._values["description"] = description
        if e_tag_algorithm_family is not None:
            self._values["e_tag_algorithm_family"] = e_tag_algorithm_family
        if fallback_location is not None:
            self._values["fallback_location"] = fallback_location
        if propagated_set_level_tags is not None:
            self._values["propagated_set_level_tags"] = propagated_set_level_tags
        if s3_access_policy is not None:
            self._values["s3_access_policy"] = s3_access_policy
        if sse_config is not None:
            self._values["sse_config"] = sse_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_log_location(self) -> typing.Optional[builtins.str]:
        '''Location of the access logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-accessloglocation
        '''
        result = self._values.get("access_log_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def e_tag_algorithm_family(self) -> typing.Optional[builtins.str]:
        '''The algorithm family of the ETag.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-etagalgorithmfamily
        '''
        result = self._values.get("e_tag_algorithm_family")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fallback_location(self) -> typing.Optional[builtins.str]:
        '''An S3 location that is used to store files that have failed a direct upload.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-fallbacklocation
        '''
        result = self._values.get("fallback_location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def propagated_set_level_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The tags keys to propagate to the S3 objects associated with read sets in the sequence store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-propagatedsetleveltags
        '''
        result = self._values.get("propagated_set_level_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def s3_access_policy(self) -> typing.Any:
        '''The resource policy that controls S3 access on the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-s3accesspolicy
        '''
        result = self._values.get("s3_access_policy")
        return typing.cast(typing.Any, result)

    @builtins.property
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSequenceStore.SseConfigProperty"]]:
        '''Server-side encryption (SSE) settings for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-sseconfig
        '''
        result = self._values.get("sse_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSequenceStore.SseConfigProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-sequencestore.html#cfn-omics-sequencestore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSequenceStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IVariantStoreRef_49e3cae7, _ITaggable_36806126)
class CfnVariantStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnVariantStore",
):
    '''Create a store for variant data.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html
    :cloudformationResource: AWS::Omics::VariantStore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        cfn_variant_store = omics.CfnVariantStore(self, "MyCfnVariantStore",
            name="name",
            reference=omics.CfnVariantStore.ReferenceItemProperty(
                reference_arn="referenceArn"
            ),
        
            # the properties below are optional
            description="description",
            sse_config=omics.CfnVariantStore.SseConfigProperty(
                type="type",
        
                # the properties below are optional
                key_arn="keyArn"
            ),
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        name: builtins.str,
        reference: typing.Union["_IResolvable_da3f097b", typing.Union["CfnVariantStore.ReferenceItemProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        sse_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnVariantStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Create a new ``AWS::Omics::VariantStore``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A name for the store.
        :param reference: The genome reference for the store's variants.
        :param description: A description for the store.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d38872c12590b13122bc23c110efd40d1aa8369a37e1015fcc0ee2529e01904)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVariantStoreProps(
            name=name,
            reference=reference,
            description=description,
            sse_config=sse_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForVariantStore")
    @builtins.classmethod
    def arn_for_variant_store(
        cls,
        resource: "_IVariantStoreRef_49e3cae7",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b7a9767f78947b0511605022e00727fbf04af579b424576a2d6c01b31b28ba8)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForVariantStore", [resource]))

    @jsii.member(jsii_name="fromVariantStoreName")
    @builtins.classmethod
    def from_variant_store_name(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        variant_store_name: builtins.str,
    ) -> "_IVariantStoreRef_49e3cae7":
        '''Creates a new IVariantStoreRef from a variantStoreName.

        :param scope: -
        :param id: -
        :param variant_store_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f419b3d012ad3960d3cb7ca202c16de7716902d7708b8a5f93c80ecc69b0794)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument variant_store_name", value=variant_store_name, expected_type=type_hints["variant_store_name"])
        return typing.cast("_IVariantStoreRef_49e3cae7", jsii.sinvoke(cls, "fromVariantStoreName", [scope, id, variant_store_name]))

    @jsii.member(jsii_name="isCfnVariantStore")
    @builtins.classmethod
    def is_cfn_variant_store(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnVariantStore.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__491360ac38318f0cc89b8ce7f0ac1b68853729c931ed3c5f800ae95f95f7dc86)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnVariantStore", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ca6bc97e153eee8b1d732a90be1690a35fffe864b7b05aaaac9e52711640fed)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__570cd7098cbc0f8a1520e467e899d1d2ec7d6bc45da494a51344b868369142a6)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the store was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The store's ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The store's status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusMessage")
    def attr_status_message(self) -> builtins.str:
        '''The store's status message.

        :cloudformationAttribute: StatusMessage
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusMessage"))

    @builtins.property
    @jsii.member(jsii_name="attrStoreArn")
    def attr_store_arn(self) -> builtins.str:
        '''The store's ARN.

        :cloudformationAttribute: StoreArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStoreArn"))

    @builtins.property
    @jsii.member(jsii_name="attrStoreSizeBytes")
    def attr_store_size_bytes(self) -> "_IResolvable_da3f097b":
        '''The store's size in bytes.

        :cloudformationAttribute: StoreSizeBytes
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrStoreSizeBytes"))

    @builtins.property
    @jsii.member(jsii_name="attrUpdateTime")
    def attr_update_time(self) -> builtins.str:
        '''When the store was updated.

        :cloudformationAttribute: UpdateTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUpdateTime"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="variantStoreRef")
    def variant_store_ref(self) -> "_VariantStoreReference_494e1db9":
        '''A reference to a VariantStore resource.'''
        return typing.cast("_VariantStoreReference_494e1db9", jsii.get(self, "variantStoreRef"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A name for the store.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a7151068f14ce10b8b0f9147b1e5b5afd6f6b7308067934acd8af16a512c243)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="reference")
    def reference(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnVariantStore.ReferenceItemProperty"]:
        '''The genome reference for the store's variants.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnVariantStore.ReferenceItemProperty"], jsii.get(self, "reference"))

    @reference.setter
    def reference(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnVariantStore.ReferenceItemProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__088cb3f651ad7a064e751c97def87bcf2e6e4149c7bcf54b57474d4b8b7d1b6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reference", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b58e2ea0e9ae60ac9a3dd7935556c2d0e2dfe3ff2de0f2ef79c50a0f2cdc07d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sseConfig")
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnVariantStore.SseConfigProperty"]]:
        '''Server-side encryption (SSE) settings for the store.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnVariantStore.SseConfigProperty"]], jsii.get(self, "sseConfig"))

    @sse_config.setter
    def sse_config(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnVariantStore.SseConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14ca86abdbf91bcd47e50c693a441fd60292ffbe1b4f732e112498a42712d29e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58acd4facff447c8ba521704b60e2e575ce07cca5086f7089300382b0d72deb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnVariantStore.ReferenceItemProperty",
        jsii_struct_bases=[],
        name_mapping={"reference_arn": "referenceArn"},
    )
    class ReferenceItemProperty:
        def __init__(self, *, reference_arn: builtins.str) -> None:
            '''The read set's genome reference ARN.

            :param reference_arn: The reference's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-referenceitem.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                reference_item_property = omics.CfnVariantStore.ReferenceItemProperty(
                    reference_arn="referenceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d03f1b71084719c634c1eec42eaa49cce433fd4e222652c52e9ca9afca86c44)
                check_type(argname="argument reference_arn", value=reference_arn, expected_type=type_hints["reference_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "reference_arn": reference_arn,
            }

        @builtins.property
        def reference_arn(self) -> builtins.str:
            '''The reference's ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-referenceitem.html#cfn-omics-variantstore-referenceitem-referencearn
            '''
            result = self._values.get("reference_arn")
            assert result is not None, "Required property 'reference_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReferenceItemProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnVariantStore.SseConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "key_arn": "keyArn"},
    )
    class SseConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Server-side encryption (SSE) settings for a store.

            :param type: The encryption type.
            :param key_arn: An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-sseconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                sse_config_property = omics.CfnVariantStore.SseConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    key_arn="keyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__151f006e709dbecd4ae7c2469b6d65397d70b22812c239977c3f339440eefaf8)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if key_arn is not None:
                self._values["key_arn"] = key_arn

        @builtins.property
        def type(self) -> builtins.str:
            '''The encryption type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-sseconfig.html#cfn-omics-variantstore-sseconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_arn(self) -> typing.Optional[builtins.str]:
            '''An encryption key ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-variantstore-sseconfig.html#cfn-omics-variantstore-sseconfig-keyarn
            '''
            result = self._values.get("key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnVariantStoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "reference": "reference",
        "description": "description",
        "sse_config": "sseConfig",
        "tags": "tags",
    },
)
class CfnVariantStoreProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        reference: typing.Union["_IResolvable_da3f097b", typing.Union["CfnVariantStore.ReferenceItemProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        sse_config: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnVariantStore.SseConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVariantStore``.

        :param name: A name for the store.
        :param reference: The genome reference for the store's variants.
        :param description: A description for the store.
        :param sse_config: Server-side encryption (SSE) settings for the store.
        :param tags: Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            cfn_variant_store_props = omics.CfnVariantStoreProps(
                name="name",
                reference=omics.CfnVariantStore.ReferenceItemProperty(
                    reference_arn="referenceArn"
                ),
            
                # the properties below are optional
                description="description",
                sse_config=omics.CfnVariantStore.SseConfigProperty(
                    type="type",
            
                    # the properties below are optional
                    key_arn="keyArn"
                ),
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9cee3839b5919ab156aab54490277c559d790311fd9ea2b761f99373fdb7eaec)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument reference", value=reference, expected_type=type_hints["reference"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument sse_config", value=sse_config, expected_type=type_hints["sse_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "reference": reference,
        }
        if description is not None:
            self._values["description"] = description
        if sse_config is not None:
            self._values["sse_config"] = sse_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A name for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def reference(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnVariantStore.ReferenceItemProperty"]:
        '''The genome reference for the store's variants.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-reference
        '''
        result = self._values.get("reference")
        assert result is not None, "Required property 'reference' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnVariantStore.ReferenceItemProperty"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sse_config(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnVariantStore.SseConfigProperty"]]:
        '''Server-side encryption (SSE) settings for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-sseconfig
        '''
        result = self._values.get("sse_config")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnVariantStore.SseConfigProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-variantstore.html#cfn-omics-variantstore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVariantStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IWorkflowRef_c34b3fa1, _ITaggable_36806126)
class CfnWorkflow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnWorkflow",
):
    '''Creates a private workflow. Before you create a private workflow, you must create and configure these required resources:.

    - *Workflow definition file:* A workflow definition file written in WDL, Nextflow, or CWL. The workflow definition specifies the inputs and outputs for runs that use the workflow. It also includes specifications for the runs and run tasks for your workflow, including compute and memory requirements. The workflow definition file must be in ``.zip`` format. For more information, see `Workflow definition files <https://docs.aws.amazon.com/omics/latest/dev/workflow-definition-files.html>`_ in AWS HealthOmics.
    - You can use Amazon Q CLI to build and validate your workflow definition files in WDL, Nextflow, and CWL. For more information, see `Example prompts for Amazon Q CLI <https://docs.aws.amazon.com/omics/latest/dev/getting-started.html#omics-q-prompts>`_ and the `AWS HealthOmics Agentic generative AI tutorial <https://docs.aws.amazon.com/https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai>`_ on GitHub.
    - *(Optional) Parameter template file:* A parameter template file written in JSON. Create the file to define the run parameters, or AWS HealthOmics generates the parameter template for you. For more information, see `Parameter template files for HealthOmics workflows <https://docs.aws.amazon.com/omics/latest/dev/parameter-templates.html>`_ .
    - *ECR container images:* Create container images for the workflow in a private ECR repository, or synchronize images from a supported upstream registry with your Amazon ECR private repository.
    - *(Optional) Sentieon licenses:* Request a Sentieon license to use the Sentieon software in private workflows.

    For more information, see `Creating or updating a private workflow in AWS HealthOmics <https://docs.aws.amazon.com/omics/latest/dev/creating-private-workflows.html>`_ in the *AWS HealthOmics User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html
    :cloudformationResource: AWS::Omics::Workflow
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        cfn_workflow = omics.CfnWorkflow(self, "MyCfnWorkflow",
            accelerators="accelerators",
            container_registry_map=omics.CfnWorkflow.ContainerRegistryMapProperty(
                image_mappings=[omics.CfnWorkflow.ImageMappingProperty(
                    destination_image="destinationImage",
                    source_image="sourceImage"
                )],
                registry_mappings=[omics.CfnWorkflow.RegistryMappingProperty(
                    ecr_account_id="ecrAccountId",
                    ecr_repository_prefix="ecrRepositoryPrefix",
                    upstream_registry_url="upstreamRegistryUrl",
                    upstream_repository_prefix="upstreamRepositoryPrefix"
                )]
            ),
            container_registry_map_uri="containerRegistryMapUri",
            definition_repository=omics.CfnWorkflow.DefinitionRepositoryProperty(
                connection_arn="connectionArn",
                exclude_file_patterns=["excludeFilePatterns"],
                full_repository_id="fullRepositoryId",
                source_reference=omics.CfnWorkflow.SourceReferenceProperty(
                    type="type",
                    value="value"
                )
            ),
            definition_uri="definitionUri",
            description="description",
            engine="engine",
            main="main",
            name="name",
            parameter_template={
                "parameter_template_key": omics.CfnWorkflow.WorkflowParameterProperty(
                    description="description",
                    optional=False
                )
            },
            parameter_template_path="parameterTemplatePath",
            readme_markdown="readmeMarkdown",
            readme_path="readmePath",
            readme_uri="readmeUri",
            storage_capacity=123,
            storage_type="storageType",
            tags={
                "tags_key": "tags"
            },
            workflow_bucket_owner_id="workflowBucketOwnerId"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        accelerators: typing.Optional[builtins.str] = None,
        container_registry_map: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.ContainerRegistryMapProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        container_registry_map_uri: typing.Optional[builtins.str] = None,
        definition_repository: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.DefinitionRepositoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        definition_uri: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        main: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        parameter_template: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.WorkflowParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        parameter_template_path: typing.Optional[builtins.str] = None,
        readme_markdown: typing.Optional[builtins.str] = None,
        readme_path: typing.Optional[builtins.str] = None,
        readme_uri: typing.Optional[builtins.str] = None,
        storage_capacity: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workflow_bucket_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Omics::Workflow``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param accelerators: 
        :param container_registry_map: Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see `Container images <https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html>`_ in the *AWS HealthOmics User Guide* .
        :param container_registry_map_uri: 
        :param definition_repository: Contains information about a source code repository that hosts the workflow definition files.
        :param definition_uri: The URI of a definition for the workflow.
        :param description: The parameter's description.
        :param engine: An engine for the workflow.
        :param main: The path of the main definition file for the workflow.
        :param name: The workflow's name.
        :param parameter_template: The workflow's parameter template.
        :param parameter_template_path: Path to the primary workflow parameter template JSON file inside the repository.
        :param readme_markdown: The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.
        :param readme_path: The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the README.md file from the root directory of the repository will be used.
        :param readme_uri: The S3 URI of the README file for the workflow. This file provides documentation and usage information for the workflow. The S3 URI must begin with s3://USER-OWNED-BUCKET/. The requester must have access to the S3 bucket and object. The max README content length is 500 KiB.
        :param storage_capacity: The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. The ``storageCapacity`` can be overwritten at run time. The storage capacity is not required for runs with a ``DYNAMIC`` storage type.
        :param storage_type: 
        :param tags: Tags for the workflow.
        :param workflow_bucket_owner_id: Optional workflow bucket owner ID to verify the workflow bucket.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2d05cb293836959a925b22dbe1861bc4457d2d510bd3a480ae858ea9f00850d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkflowProps(
            accelerators=accelerators,
            container_registry_map=container_registry_map,
            container_registry_map_uri=container_registry_map_uri,
            definition_repository=definition_repository,
            definition_uri=definition_uri,
            description=description,
            engine=engine,
            main=main,
            name=name,
            parameter_template=parameter_template,
            parameter_template_path=parameter_template_path,
            readme_markdown=readme_markdown,
            readme_path=readme_path,
            readme_uri=readme_uri,
            storage_capacity=storage_capacity,
            storage_type=storage_type,
            tags=tags,
            workflow_bucket_owner_id=workflow_bucket_owner_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForWorkflow")
    @builtins.classmethod
    def arn_for_workflow(cls, resource: "_IWorkflowRef_c34b3fa1") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67df20aaeaafc046258133711462983b03f7d276f5db7702f3acf0f303341182)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForWorkflow", [resource]))

    @jsii.member(jsii_name="isCfnWorkflow")
    @builtins.classmethod
    def is_cfn_workflow(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnWorkflow.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85eaacf4591f2168dc63862126dd9dd0579c6fdfc3c94bffdd6d2a411210f03e)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnWorkflow", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98655701238267dcfc2598ca58d2fdf3b94be0fdd6d36c6407b8c9216e530168)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3d18757469eec460375791b428b2b2a8ebd5be703fbc705cb706233f42a0050)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The ARN for the workflow.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''When the workflow was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The workflow's ID.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The workflow's status.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The workflow's type.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="attrUuid")
    def attr_uuid(self) -> builtins.str:
        '''
        :cloudformationAttribute: Uuid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUuid"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "_WorkflowReference_d2d5c008":
        '''A reference to a Workflow resource.'''
        return typing.cast("_WorkflowReference_d2d5c008", jsii.get(self, "workflowRef"))

    @builtins.property
    @jsii.member(jsii_name="accelerators")
    def accelerators(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accelerators"))

    @accelerators.setter
    def accelerators(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__286f71b00d1993ebc792c6e260606dac95cf17ec599b45b4cb2111b4ca57a0fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accelerators", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerRegistryMap")
    def container_registry_map(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.ContainerRegistryMapProperty"]]:
        '''Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.ContainerRegistryMapProperty"]], jsii.get(self, "containerRegistryMap"))

    @container_registry_map.setter
    def container_registry_map(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.ContainerRegistryMapProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d61321fc4a694dded60b8fceeeafd83e9ae3f79a0329bdba98cd03787f3daa3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryMap", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerRegistryMapUri")
    def container_registry_map_uri(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRegistryMapUri"))

    @container_registry_map_uri.setter
    def container_registry_map_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1466a9fdbdff03b1c7b3fd5e72f7386ca160db487d501609519ca1c35a987aca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryMapUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="definitionRepository")
    def definition_repository(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.DefinitionRepositoryProperty"]]:
        '''Contains information about a source code repository that hosts the workflow definition files.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.DefinitionRepositoryProperty"]], jsii.get(self, "definitionRepository"))

    @definition_repository.setter
    def definition_repository(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.DefinitionRepositoryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b6e4242f1457a50b9f5b17595e8985df9311b3b5ec98f525f390f9387770415)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionRepository", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="definitionUri")
    def definition_uri(self) -> typing.Optional[builtins.str]:
        '''The URI of a definition for the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "definitionUri"))

    @definition_uri.setter
    def definition_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc102140c3b77bda25eda4edac3ddf245628b20791c9053f2a901ded02c9b780)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The parameter's description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73c565083430765eb26563b0a57061f931b2ec1240d0b6c03b6bdad1003055c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> typing.Optional[builtins.str]:
        '''An engine for the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2edee5dfbe37830cd0e2e70344c7e33e9cf08c5c243438272da4a5634eae529f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="main")
    def main(self) -> typing.Optional[builtins.str]:
        '''The path of the main definition file for the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "main"))

    @main.setter
    def main(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f791067dcd2f7a992bf37cf0c6c81e381b2e0344e60cf85051d19bb08c69bf13)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "main", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The workflow's name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6845f053d191fb8caa10b651afe2128f50703f821981813813ed0bb9862dad7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parameterTemplate")
    def parameter_template(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnWorkflow.WorkflowParameterProperty"]]]]:
        '''The workflow's parameter template.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnWorkflow.WorkflowParameterProperty"]]]], jsii.get(self, "parameterTemplate"))

    @parameter_template.setter
    def parameter_template(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnWorkflow.WorkflowParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd71f853b8475a5b472d76bce0cd20afc1269357412bdaa83e29ea355af8f64b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterTemplate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parameterTemplatePath")
    def parameter_template_path(self) -> typing.Optional[builtins.str]:
        '''Path to the primary workflow parameter template JSON file inside the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterTemplatePath"))

    @parameter_template_path.setter
    def parameter_template_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d41351b64d942ee30b08547c1780197e0df1eca59541df6f21ad720a36cb6716)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterTemplatePath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readmeMarkdown")
    def readme_markdown(self) -> typing.Optional[builtins.str]:
        '''The markdown content for the workflow's README file.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readmeMarkdown"))

    @readme_markdown.setter
    def readme_markdown(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecc1997459356ed8d8ca95f01eab7bd4215d815bf69cff594388b6f7222e0c8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readmeMarkdown", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readmePath")
    def readme_path(self) -> typing.Optional[builtins.str]:
        '''The path to the workflow README markdown file within the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readmePath"))

    @readme_path.setter
    def readme_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16e36c31f82073225a89cc2a0da972aba7908d4ad2dd686757120c7089f99861)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readmePath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readmeUri")
    def readme_uri(self) -> typing.Optional[builtins.str]:
        '''The S3 URI of the README file for the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readmeUri"))

    @readme_uri.setter
    def readme_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28c67e6013e7a108b99f462f48461025e53196240b5182ef0ee813188829ec6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readmeUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageCapacity")
    def storage_capacity(self) -> typing.Optional[jsii.Number]:
        '''The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacity"))

    @storage_capacity.setter
    def storage_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37c3d929054386cb4ebdbc60c2c3558d7cd34bed65861db5661f96d5d75ce7df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacity", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82b78c9fdaf5e3e15a75209f5d891cf1513f47077977c45c2d020ffe13e990ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the workflow.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__651d8f1caf8b2c987665acfeae50e19a5626bb723832dae7067c423aab3ac2b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workflowBucketOwnerId")
    def workflow_bucket_owner_id(self) -> typing.Optional[builtins.str]:
        '''Optional workflow bucket owner ID to verify the workflow bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workflowBucketOwnerId"))

    @workflow_bucket_owner_id.setter
    def workflow_bucket_owner_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fec2ca5e32cee87eaac65d878c60669f18bb90724ac13ab05f21221ebd80766e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflowBucketOwnerId", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflow.ContainerRegistryMapProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_mappings": "imageMappings",
            "registry_mappings": "registryMappings",
        },
    )
    class ContainerRegistryMapProperty:
        def __init__(
            self,
            *,
            image_mappings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.ImageMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            registry_mappings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.RegistryMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries.

            For more information, see `Container images <https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html>`_ in the *AWS HealthOmics User Guide* .

            :param image_mappings: Image mappings specify path mappings between the ECR private repository and their corresponding external repositories.
            :param registry_mappings: Mapping that provides the ECR repository path where upstream container images are pulled and synchronized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-containerregistrymap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                container_registry_map_property = omics.CfnWorkflow.ContainerRegistryMapProperty(
                    image_mappings=[omics.CfnWorkflow.ImageMappingProperty(
                        destination_image="destinationImage",
                        source_image="sourceImage"
                    )],
                    registry_mappings=[omics.CfnWorkflow.RegistryMappingProperty(
                        ecr_account_id="ecrAccountId",
                        ecr_repository_prefix="ecrRepositoryPrefix",
                        upstream_registry_url="upstreamRegistryUrl",
                        upstream_repository_prefix="upstreamRepositoryPrefix"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b93208b886c42793f6b22971c79ed50b456a125a28fedf2949548b0a03f82c3e)
                check_type(argname="argument image_mappings", value=image_mappings, expected_type=type_hints["image_mappings"])
                check_type(argname="argument registry_mappings", value=registry_mappings, expected_type=type_hints["registry_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if image_mappings is not None:
                self._values["image_mappings"] = image_mappings
            if registry_mappings is not None:
                self._values["registry_mappings"] = registry_mappings

        @builtins.property
        def image_mappings(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.ImageMappingProperty"]]]]:
            '''Image mappings specify path mappings between the ECR private repository and their corresponding external repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-containerregistrymap.html#cfn-omics-workflow-containerregistrymap-imagemappings
            '''
            result = self._values.get("image_mappings")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.ImageMappingProperty"]]]], result)

        @builtins.property
        def registry_mappings(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.RegistryMappingProperty"]]]]:
            '''Mapping that provides the ECR repository path where upstream container images are pulled and synchronized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-containerregistrymap.html#cfn-omics-workflow-containerregistrymap-registrymappings
            '''
            result = self._values.get("registry_mappings")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.RegistryMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerRegistryMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflow.DefinitionRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_arn": "connectionArn",
            "exclude_file_patterns": "excludeFilePatterns",
            "full_repository_id": "fullRepositoryId",
            "source_reference": "sourceReference",
        },
    )
    class DefinitionRepositoryProperty:
        def __init__(
            self,
            *,
            connection_arn: typing.Optional[builtins.str] = None,
            exclude_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            full_repository_id: typing.Optional[builtins.str] = None,
            source_reference: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.SourceReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about a source code repository that hosts the workflow definition files.

            :param connection_arn: The Amazon Resource Name (ARN) of the connection to the source code repository.
            :param exclude_file_patterns: A list of file patterns to exclude when retrieving the workflow definition from the repository.
            :param full_repository_id: The full repository identifier, including the repository owner and name. For example, 'repository-owner/repository-name'.
            :param source_reference: The source reference for the repository, such as a branch name, tag, or commit ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-definitionrepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                definition_repository_property = omics.CfnWorkflow.DefinitionRepositoryProperty(
                    connection_arn="connectionArn",
                    exclude_file_patterns=["excludeFilePatterns"],
                    full_repository_id="fullRepositoryId",
                    source_reference=omics.CfnWorkflow.SourceReferenceProperty(
                        type="type",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3c23b09e8f18584c69d282b6816697f2992e22dbf81773246b66875fbb0c0c8)
                check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
                check_type(argname="argument exclude_file_patterns", value=exclude_file_patterns, expected_type=type_hints["exclude_file_patterns"])
                check_type(argname="argument full_repository_id", value=full_repository_id, expected_type=type_hints["full_repository_id"])
                check_type(argname="argument source_reference", value=source_reference, expected_type=type_hints["source_reference"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection_arn is not None:
                self._values["connection_arn"] = connection_arn
            if exclude_file_patterns is not None:
                self._values["exclude_file_patterns"] = exclude_file_patterns
            if full_repository_id is not None:
                self._values["full_repository_id"] = full_repository_id
            if source_reference is not None:
                self._values["source_reference"] = source_reference

        @builtins.property
        def connection_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the connection to the source code repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-definitionrepository.html#cfn-omics-workflow-definitionrepository-connectionarn
            '''
            result = self._values.get("connection_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclude_file_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of file patterns to exclude when retrieving the workflow definition from the repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-definitionrepository.html#cfn-omics-workflow-definitionrepository-excludefilepatterns
            '''
            result = self._values.get("exclude_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def full_repository_id(self) -> typing.Optional[builtins.str]:
            '''The full repository identifier, including the repository owner and name.

            For example, 'repository-owner/repository-name'.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-definitionrepository.html#cfn-omics-workflow-definitionrepository-fullrepositoryid
            '''
            result = self._values.get("full_repository_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_reference(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.SourceReferenceProperty"]]:
            '''The source reference for the repository, such as a branch name, tag, or commit ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-definitionrepository.html#cfn-omics-workflow-definitionrepository-sourcereference
            '''
            result = self._values.get("source_reference")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.SourceReferenceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefinitionRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflow.ImageMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_image": "destinationImage",
            "source_image": "sourceImage",
        },
    )
    class ImageMappingProperty:
        def __init__(
            self,
            *,
            destination_image: typing.Optional[builtins.str] = None,
            source_image: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies image mappings that workflow tasks can use.

            For example, you can replace all the task references of a public image to use an equivalent image in your private ECR repository. You can use image mappings with upstream registries that don't support pull through cache. You need to manually synchronize the upstream registry with your private repository.

            :param destination_image: Specifies the URI of the corresponding image in the private ECR registry.
            :param source_image: Specifies the URI of the source image in the upstream registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-imagemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                image_mapping_property = omics.CfnWorkflow.ImageMappingProperty(
                    destination_image="destinationImage",
                    source_image="sourceImage"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__98f85817eb366199f668581daf61aabd43de777e1bd4110572941bbd0bb03687)
                check_type(argname="argument destination_image", value=destination_image, expected_type=type_hints["destination_image"])
                check_type(argname="argument source_image", value=source_image, expected_type=type_hints["source_image"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_image is not None:
                self._values["destination_image"] = destination_image
            if source_image is not None:
                self._values["source_image"] = source_image

        @builtins.property
        def destination_image(self) -> typing.Optional[builtins.str]:
            '''Specifies the URI of the corresponding image in the private ECR registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-imagemapping.html#cfn-omics-workflow-imagemapping-destinationimage
            '''
            result = self._values.get("destination_image")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_image(self) -> typing.Optional[builtins.str]:
            '''Specifies the URI of the source image in the upstream registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-imagemapping.html#cfn-omics-workflow-imagemapping-sourceimage
            '''
            result = self._values.get("source_image")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflow.RegistryMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ecr_account_id": "ecrAccountId",
            "ecr_repository_prefix": "ecrRepositoryPrefix",
            "upstream_registry_url": "upstreamRegistryUrl",
            "upstream_repository_prefix": "upstreamRepositoryPrefix",
        },
    )
    class RegistryMappingProperty:
        def __init__(
            self,
            *,
            ecr_account_id: typing.Optional[builtins.str] = None,
            ecr_repository_prefix: typing.Optional[builtins.str] = None,
            upstream_registry_url: typing.Optional[builtins.str] = None,
            upstream_repository_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''If you are using the ECR pull through cache feature, the registry mapping maps between the ECR repository and the upstream registry where container images are pulled and synchronized.

            :param ecr_account_id: Account ID of the account that owns the upstream container image.
            :param ecr_repository_prefix: The repository prefix to use in the ECR private repository.
            :param upstream_registry_url: The URI of the upstream registry.
            :param upstream_repository_prefix: The repository prefix of the corresponding repository in the upstream registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-registrymapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                registry_mapping_property = omics.CfnWorkflow.RegistryMappingProperty(
                    ecr_account_id="ecrAccountId",
                    ecr_repository_prefix="ecrRepositoryPrefix",
                    upstream_registry_url="upstreamRegistryUrl",
                    upstream_repository_prefix="upstreamRepositoryPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf8725b8e4b50a33568267e8b0666f0c8b9e8a47c56098879cb0cdba27310fbf)
                check_type(argname="argument ecr_account_id", value=ecr_account_id, expected_type=type_hints["ecr_account_id"])
                check_type(argname="argument ecr_repository_prefix", value=ecr_repository_prefix, expected_type=type_hints["ecr_repository_prefix"])
                check_type(argname="argument upstream_registry_url", value=upstream_registry_url, expected_type=type_hints["upstream_registry_url"])
                check_type(argname="argument upstream_repository_prefix", value=upstream_repository_prefix, expected_type=type_hints["upstream_repository_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ecr_account_id is not None:
                self._values["ecr_account_id"] = ecr_account_id
            if ecr_repository_prefix is not None:
                self._values["ecr_repository_prefix"] = ecr_repository_prefix
            if upstream_registry_url is not None:
                self._values["upstream_registry_url"] = upstream_registry_url
            if upstream_repository_prefix is not None:
                self._values["upstream_repository_prefix"] = upstream_repository_prefix

        @builtins.property
        def ecr_account_id(self) -> typing.Optional[builtins.str]:
            '''Account ID of the account that owns the upstream container image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-registrymapping.html#cfn-omics-workflow-registrymapping-ecraccountid
            '''
            result = self._values.get("ecr_account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ecr_repository_prefix(self) -> typing.Optional[builtins.str]:
            '''The repository prefix to use in the ECR private repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-registrymapping.html#cfn-omics-workflow-registrymapping-ecrrepositoryprefix
            '''
            result = self._values.get("ecr_repository_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def upstream_registry_url(self) -> typing.Optional[builtins.str]:
            '''The URI of the upstream registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-registrymapping.html#cfn-omics-workflow-registrymapping-upstreamregistryurl
            '''
            result = self._values.get("upstream_registry_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def upstream_repository_prefix(self) -> typing.Optional[builtins.str]:
            '''The repository prefix of the corresponding repository in the upstream registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-registrymapping.html#cfn-omics-workflow-registrymapping-upstreamrepositoryprefix
            '''
            result = self._values.get("upstream_repository_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegistryMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflow.SourceReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class SourceReferenceProperty:
        def __init__(
            self,
            *,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the source reference in a code repository, such as a branch, tag, or commit.

            :param type: The type of source reference, such as branch, tag, or commit.
            :param value: The value of the source reference, such as the branch name, tag name, or commit ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-sourcereference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                source_reference_property = omics.CfnWorkflow.SourceReferenceProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f4e57d9f64919c2d451cd965846e1f5ee2aa3404611459632e4dd2699b4654d1)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of source reference, such as branch, tag, or commit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-sourcereference.html#cfn-omics-workflow-sourcereference-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the source reference, such as the branch name, tag name, or commit ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-sourcereference.html#cfn-omics-workflow-sourcereference-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflow.WorkflowParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"description": "description", "optional": "optional"},
    )
    class WorkflowParameterProperty:
        def __init__(
            self,
            *,
            description: typing.Optional[builtins.str] = None,
            optional: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''A workflow parameter.

            :param description: The parameter's description.
            :param optional: Whether the parameter is optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-workflowparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                workflow_parameter_property = omics.CfnWorkflow.WorkflowParameterProperty(
                    description="description",
                    optional=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__beb0e924d2102ff644fd2da920cdd60f013b66e8285db8ffc0ce774a694580a5)
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if description is not None:
                self._values["description"] = description
            if optional is not None:
                self._values["optional"] = optional

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The parameter's description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-workflowparameter.html#cfn-omics-workflow-workflowparameter-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def optional(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''Whether the parameter is optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflow-workflowparameter.html#cfn-omics-workflow-workflowparameter-optional
            '''
            result = self._values.get("optional")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnWorkflowProps",
    jsii_struct_bases=[],
    name_mapping={
        "accelerators": "accelerators",
        "container_registry_map": "containerRegistryMap",
        "container_registry_map_uri": "containerRegistryMapUri",
        "definition_repository": "definitionRepository",
        "definition_uri": "definitionUri",
        "description": "description",
        "engine": "engine",
        "main": "main",
        "name": "name",
        "parameter_template": "parameterTemplate",
        "parameter_template_path": "parameterTemplatePath",
        "readme_markdown": "readmeMarkdown",
        "readme_path": "readmePath",
        "readme_uri": "readmeUri",
        "storage_capacity": "storageCapacity",
        "storage_type": "storageType",
        "tags": "tags",
        "workflow_bucket_owner_id": "workflowBucketOwnerId",
    },
)
class CfnWorkflowProps:
    def __init__(
        self,
        *,
        accelerators: typing.Optional[builtins.str] = None,
        container_registry_map: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.ContainerRegistryMapProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        container_registry_map_uri: typing.Optional[builtins.str] = None,
        definition_repository: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.DefinitionRepositoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        definition_uri: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        main: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        parameter_template: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.WorkflowParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        parameter_template_path: typing.Optional[builtins.str] = None,
        readme_markdown: typing.Optional[builtins.str] = None,
        readme_path: typing.Optional[builtins.str] = None,
        readme_uri: typing.Optional[builtins.str] = None,
        storage_capacity: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workflow_bucket_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkflow``.

        :param accelerators: 
        :param container_registry_map: Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see `Container images <https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html>`_ in the *AWS HealthOmics User Guide* .
        :param container_registry_map_uri: 
        :param definition_repository: Contains information about a source code repository that hosts the workflow definition files.
        :param definition_uri: The URI of a definition for the workflow.
        :param description: The parameter's description.
        :param engine: An engine for the workflow.
        :param main: The path of the main definition file for the workflow.
        :param name: The workflow's name.
        :param parameter_template: The workflow's parameter template.
        :param parameter_template_path: Path to the primary workflow parameter template JSON file inside the repository.
        :param readme_markdown: The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.
        :param readme_path: The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the README.md file from the root directory of the repository will be used.
        :param readme_uri: The S3 URI of the README file for the workflow. This file provides documentation and usage information for the workflow. The S3 URI must begin with s3://USER-OWNED-BUCKET/. The requester must have access to the S3 bucket and object. The max README content length is 500 KiB.
        :param storage_capacity: The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version. The ``storageCapacity`` can be overwritten at run time. The storage capacity is not required for runs with a ``DYNAMIC`` storage type.
        :param storage_type: 
        :param tags: Tags for the workflow.
        :param workflow_bucket_owner_id: Optional workflow bucket owner ID to verify the workflow bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            cfn_workflow_props = omics.CfnWorkflowProps(
                accelerators="accelerators",
                container_registry_map=omics.CfnWorkflow.ContainerRegistryMapProperty(
                    image_mappings=[omics.CfnWorkflow.ImageMappingProperty(
                        destination_image="destinationImage",
                        source_image="sourceImage"
                    )],
                    registry_mappings=[omics.CfnWorkflow.RegistryMappingProperty(
                        ecr_account_id="ecrAccountId",
                        ecr_repository_prefix="ecrRepositoryPrefix",
                        upstream_registry_url="upstreamRegistryUrl",
                        upstream_repository_prefix="upstreamRepositoryPrefix"
                    )]
                ),
                container_registry_map_uri="containerRegistryMapUri",
                definition_repository=omics.CfnWorkflow.DefinitionRepositoryProperty(
                    connection_arn="connectionArn",
                    exclude_file_patterns=["excludeFilePatterns"],
                    full_repository_id="fullRepositoryId",
                    source_reference=omics.CfnWorkflow.SourceReferenceProperty(
                        type="type",
                        value="value"
                    )
                ),
                definition_uri="definitionUri",
                description="description",
                engine="engine",
                main="main",
                name="name",
                parameter_template={
                    "parameter_template_key": omics.CfnWorkflow.WorkflowParameterProperty(
                        description="description",
                        optional=False
                    )
                },
                parameter_template_path="parameterTemplatePath",
                readme_markdown="readmeMarkdown",
                readme_path="readmePath",
                readme_uri="readmeUri",
                storage_capacity=123,
                storage_type="storageType",
                tags={
                    "tags_key": "tags"
                },
                workflow_bucket_owner_id="workflowBucketOwnerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09bedca50200dd06a4bbe4bb6135e76dacff76287249f3d28b8f285f8205f173)
            check_type(argname="argument accelerators", value=accelerators, expected_type=type_hints["accelerators"])
            check_type(argname="argument container_registry_map", value=container_registry_map, expected_type=type_hints["container_registry_map"])
            check_type(argname="argument container_registry_map_uri", value=container_registry_map_uri, expected_type=type_hints["container_registry_map_uri"])
            check_type(argname="argument definition_repository", value=definition_repository, expected_type=type_hints["definition_repository"])
            check_type(argname="argument definition_uri", value=definition_uri, expected_type=type_hints["definition_uri"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument main", value=main, expected_type=type_hints["main"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parameter_template", value=parameter_template, expected_type=type_hints["parameter_template"])
            check_type(argname="argument parameter_template_path", value=parameter_template_path, expected_type=type_hints["parameter_template_path"])
            check_type(argname="argument readme_markdown", value=readme_markdown, expected_type=type_hints["readme_markdown"])
            check_type(argname="argument readme_path", value=readme_path, expected_type=type_hints["readme_path"])
            check_type(argname="argument readme_uri", value=readme_uri, expected_type=type_hints["readme_uri"])
            check_type(argname="argument storage_capacity", value=storage_capacity, expected_type=type_hints["storage_capacity"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument workflow_bucket_owner_id", value=workflow_bucket_owner_id, expected_type=type_hints["workflow_bucket_owner_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if accelerators is not None:
            self._values["accelerators"] = accelerators
        if container_registry_map is not None:
            self._values["container_registry_map"] = container_registry_map
        if container_registry_map_uri is not None:
            self._values["container_registry_map_uri"] = container_registry_map_uri
        if definition_repository is not None:
            self._values["definition_repository"] = definition_repository
        if definition_uri is not None:
            self._values["definition_uri"] = definition_uri
        if description is not None:
            self._values["description"] = description
        if engine is not None:
            self._values["engine"] = engine
        if main is not None:
            self._values["main"] = main
        if name is not None:
            self._values["name"] = name
        if parameter_template is not None:
            self._values["parameter_template"] = parameter_template
        if parameter_template_path is not None:
            self._values["parameter_template_path"] = parameter_template_path
        if readme_markdown is not None:
            self._values["readme_markdown"] = readme_markdown
        if readme_path is not None:
            self._values["readme_path"] = readme_path
        if readme_uri is not None:
            self._values["readme_uri"] = readme_uri
        if storage_capacity is not None:
            self._values["storage_capacity"] = storage_capacity
        if storage_type is not None:
            self._values["storage_type"] = storage_type
        if tags is not None:
            self._values["tags"] = tags
        if workflow_bucket_owner_id is not None:
            self._values["workflow_bucket_owner_id"] = workflow_bucket_owner_id

    @builtins.property
    def accelerators(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-accelerators
        '''
        result = self._values.get("accelerators")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_registry_map(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.ContainerRegistryMapProperty"]]:
        '''Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries.

        For more information, see `Container images <https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html>`_ in the *AWS HealthOmics User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-containerregistrymap
        '''
        result = self._values.get("container_registry_map")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.ContainerRegistryMapProperty"]], result)

    @builtins.property
    def container_registry_map_uri(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-containerregistrymapuri
        '''
        result = self._values.get("container_registry_map_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def definition_repository(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.DefinitionRepositoryProperty"]]:
        '''Contains information about a source code repository that hosts the workflow definition files.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-definitionrepository
        '''
        result = self._values.get("definition_repository")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.DefinitionRepositoryProperty"]], result)

    @builtins.property
    def definition_uri(self) -> typing.Optional[builtins.str]:
        '''The URI of a definition for the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-definitionuri
        '''
        result = self._values.get("definition_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The parameter's description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''An engine for the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-engine
        '''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def main(self) -> typing.Optional[builtins.str]:
        '''The path of the main definition file for the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-main
        '''
        result = self._values.get("main")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The workflow's name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_template(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnWorkflow.WorkflowParameterProperty"]]]]:
        '''The workflow's parameter template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-parametertemplate
        '''
        result = self._values.get("parameter_template")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnWorkflow.WorkflowParameterProperty"]]]], result)

    @builtins.property
    def parameter_template_path(self) -> typing.Optional[builtins.str]:
        '''Path to the primary workflow parameter template JSON file inside the repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-parametertemplatepath
        '''
        result = self._values.get("parameter_template_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readme_markdown(self) -> typing.Optional[builtins.str]:
        '''The markdown content for the workflow's README file.

        This provides documentation and usage information for users of the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-readmemarkdown
        '''
        result = self._values.get("readme_markdown")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readme_path(self) -> typing.Optional[builtins.str]:
        '''The path to the workflow README markdown file within the repository.

        This file provides documentation and usage information for the workflow. If not specified, the README.md file from the root directory of the repository will be used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-readmepath
        '''
        result = self._values.get("readme_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readme_uri(self) -> typing.Optional[builtins.str]:
        '''The S3 URI of the README file for the workflow.

        This file provides documentation and usage information for the workflow. The S3 URI must begin with s3://USER-OWNED-BUCKET/. The requester must have access to the S3 bucket and object. The max README content length is 500 KiB.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-readmeuri
        '''
        result = self._values.get("readme_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_capacity(self) -> typing.Optional[jsii.Number]:
        '''The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version.

        The ``storageCapacity`` can be overwritten at run time. The storage capacity is not required for runs with a ``DYNAMIC`` storage type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-storagecapacity
        '''
        result = self._values.get("storage_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-storagetype
        '''
        result = self._values.get("storage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Tags for the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def workflow_bucket_owner_id(self) -> typing.Optional[builtins.str]:
        '''Optional workflow bucket owner ID to verify the workflow bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflow.html#cfn-omics-workflow-workflowbucketownerid
        '''
        result = self._values.get("workflow_bucket_owner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkflowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IWorkflowVersionRef_8e877e7d, _ITaggableV2_4e6798f8)
class CfnWorkflowVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_omics.CfnWorkflowVersion",
):
    '''Creates a new workflow version for the workflow that you specify with the ``workflowId`` parameter.

    When you create a new version of a workflow, you need to specify the configuration for the new version. It doesn't inherit any configuration values from the workflow.

    Provide a version name that is unique for this workflow. You cannot change the name after HealthOmics creates the version.
    .. epigraph::

       Don't include any personally identifiable information (PII) in the version name. Version names appear in the workflow version ARN.

    For more information, see `Workflow versioning in AWS HealthOmics <https://docs.aws.amazon.com/omics/latest/dev/workflow-versions.html>`_ in the *AWS HealthOmics User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html
    :cloudformationResource: AWS::Omics::WorkflowVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_omics as omics
        
        cfn_workflow_version = omics.CfnWorkflowVersion(self, "MyCfnWorkflowVersion",
            version_name="versionName",
            workflow_id="workflowId",
        
            # the properties below are optional
            accelerators="accelerators",
            container_registry_map=omics.CfnWorkflowVersion.ContainerRegistryMapProperty(
                image_mappings=[omics.CfnWorkflowVersion.ImageMappingProperty(
                    destination_image="destinationImage",
                    source_image="sourceImage"
                )],
                registry_mappings=[omics.CfnWorkflowVersion.RegistryMappingProperty(
                    ecr_account_id="ecrAccountId",
                    ecr_repository_prefix="ecrRepositoryPrefix",
                    upstream_registry_url="upstreamRegistryUrl",
                    upstream_repository_prefix="upstreamRepositoryPrefix"
                )]
            ),
            container_registry_map_uri="containerRegistryMapUri",
            definition_repository=omics.CfnWorkflowVersion.DefinitionRepositoryProperty(
                connection_arn="connectionArn",
                exclude_file_patterns=["excludeFilePatterns"],
                full_repository_id="fullRepositoryId",
                source_reference=omics.CfnWorkflowVersion.SourceReferenceProperty(
                    type="type",
                    value="value"
                )
            ),
            definition_uri="definitionUri",
            description="description",
            engine="engine",
            main="main",
            parameter_template={
                "parameter_template_key": omics.CfnWorkflowVersion.WorkflowParameterProperty(
                    description="description",
                    optional=False
                )
            },
            parameter_template_path="parameterTemplatePath",
            readme_markdown="readmeMarkdown",
            readme_path="readmePath",
            readme_uri="readmeUri",
            storage_capacity=123,
            storage_type="storageType",
            tags={
                "tags_key": "tags"
            },
            workflow_bucket_owner_id="workflowBucketOwnerId"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        version_name: builtins.str,
        workflow_id: builtins.str,
        accelerators: typing.Optional[builtins.str] = None,
        container_registry_map: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowVersion.ContainerRegistryMapProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        container_registry_map_uri: typing.Optional[builtins.str] = None,
        definition_repository: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowVersion.DefinitionRepositoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        definition_uri: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        main: typing.Optional[builtins.str] = None,
        parameter_template: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowVersion.WorkflowParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        parameter_template_path: typing.Optional[builtins.str] = None,
        readme_markdown: typing.Optional[builtins.str] = None,
        readme_path: typing.Optional[builtins.str] = None,
        readme_uri: typing.Optional[builtins.str] = None,
        storage_capacity: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workflow_bucket_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::Omics::WorkflowVersion``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param version_name: The name of the workflow version.
        :param workflow_id: The workflow's ID.
        :param accelerators: 
        :param container_registry_map: Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see `Container images <https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html>`_ in the *AWS HealthOmics User Guide* .
        :param container_registry_map_uri: 
        :param definition_repository: Contains information about a source code repository that hosts the workflow definition files.
        :param definition_uri: 
        :param description: The description of the workflow version.
        :param engine: 
        :param main: 
        :param parameter_template: 
        :param parameter_template_path: Path to the primary workflow parameter template JSON file inside the repository.
        :param readme_markdown: The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.
        :param readme_path: The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the README.md file from the root directory of the repository will be used.
        :param readme_uri: The S3 URI of the README file for the workflow. This file provides documentation and usage information for the workflow. The S3 URI must begin with s3://USER-OWNED-BUCKET/. The requester must have access to the S3 bucket and object. The max README content length is 500 KiB.
        :param storage_capacity: 
        :param storage_type: 
        :param tags: A map of resource tags.
        :param workflow_bucket_owner_id: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9bbd83c3821b6d01e1b0445c2a66c0e7c312d81583ae6cf8dbe78c8d6a4bf99)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkflowVersionProps(
            version_name=version_name,
            workflow_id=workflow_id,
            accelerators=accelerators,
            container_registry_map=container_registry_map,
            container_registry_map_uri=container_registry_map_uri,
            definition_repository=definition_repository,
            definition_uri=definition_uri,
            description=description,
            engine=engine,
            main=main,
            parameter_template=parameter_template,
            parameter_template_path=parameter_template_path,
            readme_markdown=readme_markdown,
            readme_path=readme_path,
            readme_uri=readme_uri,
            storage_capacity=storage_capacity,
            storage_type=storage_type,
            tags=tags,
            workflow_bucket_owner_id=workflow_bucket_owner_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForWorkflowVersion")
    @builtins.classmethod
    def arn_for_workflow_version(
        cls,
        resource: "_IWorkflowVersionRef_8e877e7d",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba9428a8b7901e336eeab6247d137358ee9bc60145cd3f57cd9d69410752a02c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForWorkflowVersion", [resource]))

    @jsii.member(jsii_name="isCfnWorkflowVersion")
    @builtins.classmethod
    def is_cfn_workflow_version(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnWorkflowVersion.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c7054b8c2aebdab065713b2bf74644dd2b89b4b92f0f3161c76b3b26d5273ab)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnWorkflowVersion", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a7de38e00c231b3afd92bbb59cad40657b334333096dde12413f391ade16867)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1461fce0dec6c9339e6bbc0df050886fb1f30852661c80911b28268bdee03c9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''ARN of the workflow version.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''The creation time of the workflow version.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The status of the workflow version.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''The type of the workflow version.

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

    @builtins.property
    @jsii.member(jsii_name="attrUuid")
    def attr_uuid(self) -> builtins.str:
        '''
        :cloudformationAttribute: Uuid
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUuid"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> "_TagManager_0a598cb3":
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast("_TagManager_0a598cb3", jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="workflowVersionRef")
    def workflow_version_ref(self) -> "_WorkflowVersionReference_1d5421a4":
        '''A reference to a WorkflowVersion resource.'''
        return typing.cast("_WorkflowVersionReference_1d5421a4", jsii.get(self, "workflowVersionRef"))

    @builtins.property
    @jsii.member(jsii_name="versionName")
    def version_name(self) -> builtins.str:
        '''The name of the workflow version.'''
        return typing.cast(builtins.str, jsii.get(self, "versionName"))

    @version_name.setter
    def version_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9f5bdcc4a225102f171d30f4738ab832792497c08ecb206114ad57125adf01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workflowId")
    def workflow_id(self) -> builtins.str:
        '''The workflow's ID.'''
        return typing.cast(builtins.str, jsii.get(self, "workflowId"))

    @workflow_id.setter
    def workflow_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5def0afb0cd8ab9471e48b541cd9dceaeb6826bfe7a8a24d0c36614c73b1a6d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflowId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="accelerators")
    def accelerators(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accelerators"))

    @accelerators.setter
    def accelerators(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b69952a53a68976751566fbcf17774d0dfa2d7ede106cb440b751f76c7eb99ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accelerators", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerRegistryMap")
    def container_registry_map(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.ContainerRegistryMapProperty"]]:
        '''Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.ContainerRegistryMapProperty"]], jsii.get(self, "containerRegistryMap"))

    @container_registry_map.setter
    def container_registry_map(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.ContainerRegistryMapProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46a9bb90d987260f113e2b2c7bfe0d00e76229ce25afbfccf1a386b82f85e224)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryMap", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerRegistryMapUri")
    def container_registry_map_uri(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerRegistryMapUri"))

    @container_registry_map_uri.setter
    def container_registry_map_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65acb20ad98b8b631169a3db99c88bd3662a7e2bd947577b5265d087e4b8362d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerRegistryMapUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="definitionRepository")
    def definition_repository(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.DefinitionRepositoryProperty"]]:
        '''Contains information about a source code repository that hosts the workflow definition files.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.DefinitionRepositoryProperty"]], jsii.get(self, "definitionRepository"))

    @definition_repository.setter
    def definition_repository(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.DefinitionRepositoryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76f88fb7dbfba72f92fec4a64878a9e7fdd595353c2e76e5f675a9f318a5b5e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionRepository", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="definitionUri")
    def definition_uri(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "definitionUri"))

    @definition_uri.setter
    def definition_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a8ff1e5a2ba3fcf1c5fb306e96445a76ec1ac6872615b206206a2a173f64978)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the workflow version.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d26e61de900859028fd4b5aff7eb7fefa87386da043d620b3407bc69ef3f950b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ade62566da0dd0e16cdb86d20bb176d8778e02a5223101deea2467f1ee7cadc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="main")
    def main(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "main"))

    @main.setter
    def main(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb201e46965fe4b385e0e52f84a505023c34c0c16c33aea7e75a09209c34d1af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "main", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parameterTemplate")
    def parameter_template(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.WorkflowParameterProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.WorkflowParameterProperty"]]]], jsii.get(self, "parameterTemplate"))

    @parameter_template.setter
    def parameter_template(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.WorkflowParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__909f80095cd6043c196e37a387a0f1f32bfcddcd8f9a81c5e8f5ac8b4874faa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterTemplate", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="parameterTemplatePath")
    def parameter_template_path(self) -> typing.Optional[builtins.str]:
        '''Path to the primary workflow parameter template JSON file inside the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterTemplatePath"))

    @parameter_template_path.setter
    def parameter_template_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1012e58717a3baf054312a40aba36847bbd98b702310ea8aff265f26caeab471)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterTemplatePath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readmeMarkdown")
    def readme_markdown(self) -> typing.Optional[builtins.str]:
        '''The markdown content for the workflow's README file.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readmeMarkdown"))

    @readme_markdown.setter
    def readme_markdown(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cea66896cfd0dfa12a8b3d0b44794207352c9c78eb70c50e46466b4eea34898)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readmeMarkdown", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readmePath")
    def readme_path(self) -> typing.Optional[builtins.str]:
        '''The path to the workflow README markdown file within the repository.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readmePath"))

    @readme_path.setter
    def readme_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40cad564b15c28b2c112ad54de257f81d4d31fdfe311871657ae5bd714eb9ee6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readmePath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="readmeUri")
    def readme_uri(self) -> typing.Optional[builtins.str]:
        '''The S3 URI of the README file for the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readmeUri"))

    @readme_uri.setter
    def readme_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abe09bb1e32d84773aaf309a744224900a63bf483fa24970e875c0b0a2f1b1cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readmeUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageCapacity")
    def storage_capacity(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "storageCapacity"))

    @storage_capacity.setter
    def storage_capacity(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba60096260fa288ca386a5b2841efb8fa9833ea893400efeba006766f392a7b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageCapacity", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="storageType")
    def storage_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageType"))

    @storage_type.setter
    def storage_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50ce9715f4efa14e458d6207fae79f6b0ebc36a3bf74435e024116d9f8060ca2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of resource tags.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfbcbf729952f991d2243244c21c373b5bf1a3947ed2973ab1664037cdf636f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="workflowBucketOwnerId")
    def workflow_bucket_owner_id(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workflowBucketOwnerId"))

    @workflow_bucket_owner_id.setter
    def workflow_bucket_owner_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc6b06c168132bf54bf849b9d49774230af45a049e67f52bc48dd0220c18775d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflowBucketOwnerId", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflowVersion.ContainerRegistryMapProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_mappings": "imageMappings",
            "registry_mappings": "registryMappings",
        },
    )
    class ContainerRegistryMapProperty:
        def __init__(
            self,
            *,
            image_mappings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowVersion.ImageMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            registry_mappings: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowVersion.RegistryMappingProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries.

            For more information, see `Container images <https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html>`_ in the *AWS HealthOmics User Guide* .

            :param image_mappings: Image mappings specify path mappings between the ECR private repository and their corresponding external repositories.
            :param registry_mappings: Mapping that provides the ECR repository path where upstream container images are pulled and synchronized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-containerregistrymap.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                container_registry_map_property = omics.CfnWorkflowVersion.ContainerRegistryMapProperty(
                    image_mappings=[omics.CfnWorkflowVersion.ImageMappingProperty(
                        destination_image="destinationImage",
                        source_image="sourceImage"
                    )],
                    registry_mappings=[omics.CfnWorkflowVersion.RegistryMappingProperty(
                        ecr_account_id="ecrAccountId",
                        ecr_repository_prefix="ecrRepositoryPrefix",
                        upstream_registry_url="upstreamRegistryUrl",
                        upstream_repository_prefix="upstreamRepositoryPrefix"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__32eb3bf30b3d01f44e56bdf643f62609b8cbc84d473cb19e3564543b645033d4)
                check_type(argname="argument image_mappings", value=image_mappings, expected_type=type_hints["image_mappings"])
                check_type(argname="argument registry_mappings", value=registry_mappings, expected_type=type_hints["registry_mappings"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if image_mappings is not None:
                self._values["image_mappings"] = image_mappings
            if registry_mappings is not None:
                self._values["registry_mappings"] = registry_mappings

        @builtins.property
        def image_mappings(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.ImageMappingProperty"]]]]:
            '''Image mappings specify path mappings between the ECR private repository and their corresponding external repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-containerregistrymap.html#cfn-omics-workflowversion-containerregistrymap-imagemappings
            '''
            result = self._values.get("image_mappings")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.ImageMappingProperty"]]]], result)

        @builtins.property
        def registry_mappings(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.RegistryMappingProperty"]]]]:
            '''Mapping that provides the ECR repository path where upstream container images are pulled and synchronized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-containerregistrymap.html#cfn-omics-workflowversion-containerregistrymap-registrymappings
            '''
            result = self._values.get("registry_mappings")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.RegistryMappingProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerRegistryMapProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflowVersion.DefinitionRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_arn": "connectionArn",
            "exclude_file_patterns": "excludeFilePatterns",
            "full_repository_id": "fullRepositoryId",
            "source_reference": "sourceReference",
        },
    )
    class DefinitionRepositoryProperty:
        def __init__(
            self,
            *,
            connection_arn: typing.Optional[builtins.str] = None,
            exclude_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
            full_repository_id: typing.Optional[builtins.str] = None,
            source_reference: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowVersion.SourceReferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about a source code repository that hosts the workflow definition files.

            :param connection_arn: The Amazon Resource Name (ARN) of the connection to the source code repository.
            :param exclude_file_patterns: A list of file patterns to exclude when retrieving the workflow definition from the repository.
            :param full_repository_id: The full repository identifier, including the repository owner and name. For example, 'repository-owner/repository-name'.
            :param source_reference: The source reference for the repository, such as a branch name, tag, or commit ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-definitionrepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                definition_repository_property = omics.CfnWorkflowVersion.DefinitionRepositoryProperty(
                    connection_arn="connectionArn",
                    exclude_file_patterns=["excludeFilePatterns"],
                    full_repository_id="fullRepositoryId",
                    source_reference=omics.CfnWorkflowVersion.SourceReferenceProperty(
                        type="type",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e0748aa0fb5a9a9d624696b0fc54ab2faf0941992918eb234ba6c3bb4a47aef5)
                check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
                check_type(argname="argument exclude_file_patterns", value=exclude_file_patterns, expected_type=type_hints["exclude_file_patterns"])
                check_type(argname="argument full_repository_id", value=full_repository_id, expected_type=type_hints["full_repository_id"])
                check_type(argname="argument source_reference", value=source_reference, expected_type=type_hints["source_reference"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connection_arn is not None:
                self._values["connection_arn"] = connection_arn
            if exclude_file_patterns is not None:
                self._values["exclude_file_patterns"] = exclude_file_patterns
            if full_repository_id is not None:
                self._values["full_repository_id"] = full_repository_id
            if source_reference is not None:
                self._values["source_reference"] = source_reference

        @builtins.property
        def connection_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the connection to the source code repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-definitionrepository.html#cfn-omics-workflowversion-definitionrepository-connectionarn
            '''
            result = self._values.get("connection_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def exclude_file_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of file patterns to exclude when retrieving the workflow definition from the repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-definitionrepository.html#cfn-omics-workflowversion-definitionrepository-excludefilepatterns
            '''
            result = self._values.get("exclude_file_patterns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def full_repository_id(self) -> typing.Optional[builtins.str]:
            '''The full repository identifier, including the repository owner and name.

            For example, 'repository-owner/repository-name'.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-definitionrepository.html#cfn-omics-workflowversion-definitionrepository-fullrepositoryid
            '''
            result = self._values.get("full_repository_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_reference(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.SourceReferenceProperty"]]:
            '''The source reference for the repository, such as a branch name, tag, or commit ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-definitionrepository.html#cfn-omics-workflowversion-definitionrepository-sourcereference
            '''
            result = self._values.get("source_reference")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.SourceReferenceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefinitionRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflowVersion.ImageMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_image": "destinationImage",
            "source_image": "sourceImage",
        },
    )
    class ImageMappingProperty:
        def __init__(
            self,
            *,
            destination_image: typing.Optional[builtins.str] = None,
            source_image: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies image mappings that workflow tasks can use.

            For example, you can replace all the task references of a public image to use an equivalent image in your private ECR repository. You can use image mappings with upstream registries that don't support pull through cache. You need to manually synchronize the upstream registry with your private repository.

            :param destination_image: Specifies the URI of the corresponding image in the private ECR registry.
            :param source_image: Specifies the URI of the source image in the upstream registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-imagemapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                image_mapping_property = omics.CfnWorkflowVersion.ImageMappingProperty(
                    destination_image="destinationImage",
                    source_image="sourceImage"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__421f9ca400f5d5d6c3aa9a53dbe35757f3408b2b30be15794288deb51c48b293)
                check_type(argname="argument destination_image", value=destination_image, expected_type=type_hints["destination_image"])
                check_type(argname="argument source_image", value=source_image, expected_type=type_hints["source_image"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_image is not None:
                self._values["destination_image"] = destination_image
            if source_image is not None:
                self._values["source_image"] = source_image

        @builtins.property
        def destination_image(self) -> typing.Optional[builtins.str]:
            '''Specifies the URI of the corresponding image in the private ECR registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-imagemapping.html#cfn-omics-workflowversion-imagemapping-destinationimage
            '''
            result = self._values.get("destination_image")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_image(self) -> typing.Optional[builtins.str]:
            '''Specifies the URI of the source image in the upstream registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-imagemapping.html#cfn-omics-workflowversion-imagemapping-sourceimage
            '''
            result = self._values.get("source_image")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflowVersion.RegistryMappingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ecr_account_id": "ecrAccountId",
            "ecr_repository_prefix": "ecrRepositoryPrefix",
            "upstream_registry_url": "upstreamRegistryUrl",
            "upstream_repository_prefix": "upstreamRepositoryPrefix",
        },
    )
    class RegistryMappingProperty:
        def __init__(
            self,
            *,
            ecr_account_id: typing.Optional[builtins.str] = None,
            ecr_repository_prefix: typing.Optional[builtins.str] = None,
            upstream_registry_url: typing.Optional[builtins.str] = None,
            upstream_repository_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''If you are using the ECR pull through cache feature, the registry mapping maps between the ECR repository and the upstream registry where container images are pulled and synchronized.

            :param ecr_account_id: Account ID of the account that owns the upstream container image.
            :param ecr_repository_prefix: The repository prefix to use in the ECR private repository.
            :param upstream_registry_url: The URI of the upstream registry.
            :param upstream_repository_prefix: The repository prefix of the corresponding repository in the upstream registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-registrymapping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                registry_mapping_property = omics.CfnWorkflowVersion.RegistryMappingProperty(
                    ecr_account_id="ecrAccountId",
                    ecr_repository_prefix="ecrRepositoryPrefix",
                    upstream_registry_url="upstreamRegistryUrl",
                    upstream_repository_prefix="upstreamRepositoryPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9eab95380e8258bf7a10a1ed8080d039134ac7daf1f5f0c979d28cb4f5c4f426)
                check_type(argname="argument ecr_account_id", value=ecr_account_id, expected_type=type_hints["ecr_account_id"])
                check_type(argname="argument ecr_repository_prefix", value=ecr_repository_prefix, expected_type=type_hints["ecr_repository_prefix"])
                check_type(argname="argument upstream_registry_url", value=upstream_registry_url, expected_type=type_hints["upstream_registry_url"])
                check_type(argname="argument upstream_repository_prefix", value=upstream_repository_prefix, expected_type=type_hints["upstream_repository_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ecr_account_id is not None:
                self._values["ecr_account_id"] = ecr_account_id
            if ecr_repository_prefix is not None:
                self._values["ecr_repository_prefix"] = ecr_repository_prefix
            if upstream_registry_url is not None:
                self._values["upstream_registry_url"] = upstream_registry_url
            if upstream_repository_prefix is not None:
                self._values["upstream_repository_prefix"] = upstream_repository_prefix

        @builtins.property
        def ecr_account_id(self) -> typing.Optional[builtins.str]:
            '''Account ID of the account that owns the upstream container image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-registrymapping.html#cfn-omics-workflowversion-registrymapping-ecraccountid
            '''
            result = self._values.get("ecr_account_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ecr_repository_prefix(self) -> typing.Optional[builtins.str]:
            '''The repository prefix to use in the ECR private repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-registrymapping.html#cfn-omics-workflowversion-registrymapping-ecrrepositoryprefix
            '''
            result = self._values.get("ecr_repository_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def upstream_registry_url(self) -> typing.Optional[builtins.str]:
            '''The URI of the upstream registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-registrymapping.html#cfn-omics-workflowversion-registrymapping-upstreamregistryurl
            '''
            result = self._values.get("upstream_registry_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def upstream_repository_prefix(self) -> typing.Optional[builtins.str]:
            '''The repository prefix of the corresponding repository in the upstream registry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-registrymapping.html#cfn-omics-workflowversion-registrymapping-upstreamrepositoryprefix
            '''
            result = self._values.get("upstream_repository_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RegistryMappingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflowVersion.SourceReferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class SourceReferenceProperty:
        def __init__(
            self,
            *,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the source reference in a code repository, such as a branch, tag, or commit.

            :param type: The type of source reference, such as branch, tag, or commit.
            :param value: The value of the source reference, such as the branch name, tag name, or commit ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-sourcereference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                source_reference_property = omics.CfnWorkflowVersion.SourceReferenceProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bd0032779911f1051b3896f001118256f2cbf0d060b22c10b5fdeb3b3e488c73)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The type of source reference, such as branch, tag, or commit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-sourcereference.html#cfn-omics-workflowversion-sourcereference-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value of the source reference, such as the branch name, tag name, or commit ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-sourcereference.html#cfn-omics-workflowversion-sourcereference-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceReferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_omics.CfnWorkflowVersion.WorkflowParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"description": "description", "optional": "optional"},
    )
    class WorkflowParameterProperty:
        def __init__(
            self,
            *,
            description: typing.Optional[builtins.str] = None,
            optional: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''A workflow parameter.

            :param description: The parameter's description.
            :param optional: Whether the parameter is optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-workflowparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_omics as omics
                
                workflow_parameter_property = omics.CfnWorkflowVersion.WorkflowParameterProperty(
                    description="description",
                    optional=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d434101b6df92e22ac3acf923cd7bb4105c1a82dad119b383839a4f14189485)
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument optional", value=optional, expected_type=type_hints["optional"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if description is not None:
                self._values["description"] = description
            if optional is not None:
                self._values["optional"] = optional

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The parameter's description.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-workflowparameter.html#cfn-omics-workflowversion-workflowparameter-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def optional(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''Whether the parameter is optional.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-omics-workflowversion-workflowparameter.html#cfn-omics-workflowversion-workflowparameter-optional
            '''
            result = self._values.get("optional")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_omics.CfnWorkflowVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "version_name": "versionName",
        "workflow_id": "workflowId",
        "accelerators": "accelerators",
        "container_registry_map": "containerRegistryMap",
        "container_registry_map_uri": "containerRegistryMapUri",
        "definition_repository": "definitionRepository",
        "definition_uri": "definitionUri",
        "description": "description",
        "engine": "engine",
        "main": "main",
        "parameter_template": "parameterTemplate",
        "parameter_template_path": "parameterTemplatePath",
        "readme_markdown": "readmeMarkdown",
        "readme_path": "readmePath",
        "readme_uri": "readmeUri",
        "storage_capacity": "storageCapacity",
        "storage_type": "storageType",
        "tags": "tags",
        "workflow_bucket_owner_id": "workflowBucketOwnerId",
    },
)
class CfnWorkflowVersionProps:
    def __init__(
        self,
        *,
        version_name: builtins.str,
        workflow_id: builtins.str,
        accelerators: typing.Optional[builtins.str] = None,
        container_registry_map: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowVersion.ContainerRegistryMapProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        container_registry_map_uri: typing.Optional[builtins.str] = None,
        definition_repository: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowVersion.DefinitionRepositoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        definition_uri: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        main: typing.Optional[builtins.str] = None,
        parameter_template: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflowVersion.WorkflowParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        parameter_template_path: typing.Optional[builtins.str] = None,
        readme_markdown: typing.Optional[builtins.str] = None,
        readme_path: typing.Optional[builtins.str] = None,
        readme_uri: typing.Optional[builtins.str] = None,
        storage_capacity: typing.Optional[jsii.Number] = None,
        storage_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        workflow_bucket_owner_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkflowVersion``.

        :param version_name: The name of the workflow version.
        :param workflow_id: The workflow's ID.
        :param accelerators: 
        :param container_registry_map: Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries. For more information, see `Container images <https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html>`_ in the *AWS HealthOmics User Guide* .
        :param container_registry_map_uri: 
        :param definition_repository: Contains information about a source code repository that hosts the workflow definition files.
        :param definition_uri: 
        :param description: The description of the workflow version.
        :param engine: 
        :param main: 
        :param parameter_template: 
        :param parameter_template_path: Path to the primary workflow parameter template JSON file inside the repository.
        :param readme_markdown: The markdown content for the workflow's README file. This provides documentation and usage information for users of the workflow.
        :param readme_path: The path to the workflow README markdown file within the repository. This file provides documentation and usage information for the workflow. If not specified, the README.md file from the root directory of the repository will be used.
        :param readme_uri: The S3 URI of the README file for the workflow. This file provides documentation and usage information for the workflow. The S3 URI must begin with s3://USER-OWNED-BUCKET/. The requester must have access to the S3 bucket and object. The max README content length is 500 KiB.
        :param storage_capacity: 
        :param storage_type: 
        :param tags: A map of resource tags.
        :param workflow_bucket_owner_id: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_omics as omics
            
            cfn_workflow_version_props = omics.CfnWorkflowVersionProps(
                version_name="versionName",
                workflow_id="workflowId",
            
                # the properties below are optional
                accelerators="accelerators",
                container_registry_map=omics.CfnWorkflowVersion.ContainerRegistryMapProperty(
                    image_mappings=[omics.CfnWorkflowVersion.ImageMappingProperty(
                        destination_image="destinationImage",
                        source_image="sourceImage"
                    )],
                    registry_mappings=[omics.CfnWorkflowVersion.RegistryMappingProperty(
                        ecr_account_id="ecrAccountId",
                        ecr_repository_prefix="ecrRepositoryPrefix",
                        upstream_registry_url="upstreamRegistryUrl",
                        upstream_repository_prefix="upstreamRepositoryPrefix"
                    )]
                ),
                container_registry_map_uri="containerRegistryMapUri",
                definition_repository=omics.CfnWorkflowVersion.DefinitionRepositoryProperty(
                    connection_arn="connectionArn",
                    exclude_file_patterns=["excludeFilePatterns"],
                    full_repository_id="fullRepositoryId",
                    source_reference=omics.CfnWorkflowVersion.SourceReferenceProperty(
                        type="type",
                        value="value"
                    )
                ),
                definition_uri="definitionUri",
                description="description",
                engine="engine",
                main="main",
                parameter_template={
                    "parameter_template_key": omics.CfnWorkflowVersion.WorkflowParameterProperty(
                        description="description",
                        optional=False
                    )
                },
                parameter_template_path="parameterTemplatePath",
                readme_markdown="readmeMarkdown",
                readme_path="readmePath",
                readme_uri="readmeUri",
                storage_capacity=123,
                storage_type="storageType",
                tags={
                    "tags_key": "tags"
                },
                workflow_bucket_owner_id="workflowBucketOwnerId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32259ddc7b7d888918efaf09deb63ba780f3721ec1da9ea606ed8100a4b9fb3e)
            check_type(argname="argument version_name", value=version_name, expected_type=type_hints["version_name"])
            check_type(argname="argument workflow_id", value=workflow_id, expected_type=type_hints["workflow_id"])
            check_type(argname="argument accelerators", value=accelerators, expected_type=type_hints["accelerators"])
            check_type(argname="argument container_registry_map", value=container_registry_map, expected_type=type_hints["container_registry_map"])
            check_type(argname="argument container_registry_map_uri", value=container_registry_map_uri, expected_type=type_hints["container_registry_map_uri"])
            check_type(argname="argument definition_repository", value=definition_repository, expected_type=type_hints["definition_repository"])
            check_type(argname="argument definition_uri", value=definition_uri, expected_type=type_hints["definition_uri"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument main", value=main, expected_type=type_hints["main"])
            check_type(argname="argument parameter_template", value=parameter_template, expected_type=type_hints["parameter_template"])
            check_type(argname="argument parameter_template_path", value=parameter_template_path, expected_type=type_hints["parameter_template_path"])
            check_type(argname="argument readme_markdown", value=readme_markdown, expected_type=type_hints["readme_markdown"])
            check_type(argname="argument readme_path", value=readme_path, expected_type=type_hints["readme_path"])
            check_type(argname="argument readme_uri", value=readme_uri, expected_type=type_hints["readme_uri"])
            check_type(argname="argument storage_capacity", value=storage_capacity, expected_type=type_hints["storage_capacity"])
            check_type(argname="argument storage_type", value=storage_type, expected_type=type_hints["storage_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument workflow_bucket_owner_id", value=workflow_bucket_owner_id, expected_type=type_hints["workflow_bucket_owner_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "version_name": version_name,
            "workflow_id": workflow_id,
        }
        if accelerators is not None:
            self._values["accelerators"] = accelerators
        if container_registry_map is not None:
            self._values["container_registry_map"] = container_registry_map
        if container_registry_map_uri is not None:
            self._values["container_registry_map_uri"] = container_registry_map_uri
        if definition_repository is not None:
            self._values["definition_repository"] = definition_repository
        if definition_uri is not None:
            self._values["definition_uri"] = definition_uri
        if description is not None:
            self._values["description"] = description
        if engine is not None:
            self._values["engine"] = engine
        if main is not None:
            self._values["main"] = main
        if parameter_template is not None:
            self._values["parameter_template"] = parameter_template
        if parameter_template_path is not None:
            self._values["parameter_template_path"] = parameter_template_path
        if readme_markdown is not None:
            self._values["readme_markdown"] = readme_markdown
        if readme_path is not None:
            self._values["readme_path"] = readme_path
        if readme_uri is not None:
            self._values["readme_uri"] = readme_uri
        if storage_capacity is not None:
            self._values["storage_capacity"] = storage_capacity
        if storage_type is not None:
            self._values["storage_type"] = storage_type
        if tags is not None:
            self._values["tags"] = tags
        if workflow_bucket_owner_id is not None:
            self._values["workflow_bucket_owner_id"] = workflow_bucket_owner_id

    @builtins.property
    def version_name(self) -> builtins.str:
        '''The name of the workflow version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-versionname
        '''
        result = self._values.get("version_name")
        assert result is not None, "Required property 'version_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def workflow_id(self) -> builtins.str:
        '''The workflow's ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-workflowid
        '''
        result = self._values.get("workflow_id")
        assert result is not None, "Required property 'workflow_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def accelerators(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-accelerators
        '''
        result = self._values.get("accelerators")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_registry_map(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.ContainerRegistryMapProperty"]]:
        '''Use a container registry map to specify mappings between the ECR private repository and one or more upstream registries.

        For more information, see `Container images <https://docs.aws.amazon.com/omics/latest/dev/workflows-ecr.html>`_ in the *AWS HealthOmics User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-containerregistrymap
        '''
        result = self._values.get("container_registry_map")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.ContainerRegistryMapProperty"]], result)

    @builtins.property
    def container_registry_map_uri(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-containerregistrymapuri
        '''
        result = self._values.get("container_registry_map_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def definition_repository(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.DefinitionRepositoryProperty"]]:
        '''Contains information about a source code repository that hosts the workflow definition files.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-definitionrepository
        '''
        result = self._values.get("definition_repository")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.DefinitionRepositoryProperty"]], result)

    @builtins.property
    def definition_uri(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-definitionuri
        '''
        result = self._values.get("definition_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the workflow version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-engine
        '''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def main(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-main
        '''
        result = self._values.get("main")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_template(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.WorkflowParameterProperty"]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-parametertemplate
        '''
        result = self._values.get("parameter_template")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Mapping[builtins.str, typing.Union["_IResolvable_da3f097b", "CfnWorkflowVersion.WorkflowParameterProperty"]]]], result)

    @builtins.property
    def parameter_template_path(self) -> typing.Optional[builtins.str]:
        '''Path to the primary workflow parameter template JSON file inside the repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-parametertemplatepath
        '''
        result = self._values.get("parameter_template_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readme_markdown(self) -> typing.Optional[builtins.str]:
        '''The markdown content for the workflow's README file.

        This provides documentation and usage information for users of the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-readmemarkdown
        '''
        result = self._values.get("readme_markdown")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readme_path(self) -> typing.Optional[builtins.str]:
        '''The path to the workflow README markdown file within the repository.

        This file provides documentation and usage information for the workflow. If not specified, the README.md file from the root directory of the repository will be used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-readmepath
        '''
        result = self._values.get("readme_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def readme_uri(self) -> typing.Optional[builtins.str]:
        '''The S3 URI of the README file for the workflow.

        This file provides documentation and usage information for the workflow. The S3 URI must begin with s3://USER-OWNED-BUCKET/. The requester must have access to the S3 bucket and object. The max README content length is 500 KiB.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-readmeuri
        '''
        result = self._values.get("readme_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_capacity(self) -> typing.Optional[jsii.Number]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-storagecapacity
        '''
        result = self._values.get("storage_capacity")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def storage_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-storagetype
        '''
        result = self._values.get("storage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of resource tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def workflow_bucket_owner_id(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-omics-workflowversion.html#cfn-omics-workflowversion-workflowbucketownerid
        '''
        result = self._values.get("workflow_bucket_owner_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkflowVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAnnotationStore",
    "CfnAnnotationStoreProps",
    "CfnReferenceStore",
    "CfnReferenceStoreProps",
    "CfnRunGroup",
    "CfnRunGroupProps",
    "CfnSequenceStore",
    "CfnSequenceStoreProps",
    "CfnVariantStore",
    "CfnVariantStoreProps",
    "CfnWorkflow",
    "CfnWorkflowProps",
    "CfnWorkflowVersion",
    "CfnWorkflowVersionProps",
]

publication.publish()

def _typecheckingstub__ba5dcb906702f10b4a247a16c504ec605912264b052a73f0ae664d93bee73764(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    store_format: builtins.str,
    description: typing.Optional[builtins.str] = None,
    reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.ReferenceItemProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    store_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.StoreOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d081c3f84956f6e383e1daee886fd75ec67836196a107b0828cceab885d95c55(
    resource: _IAnnotationStoreRef_c33c98b4,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea8d23b9f77f5d9216bba34b2f07ff06220a6053227128a855b380a90746d1fe(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    annotation_store_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e5f634e0e551a9001147ebab16825824c6f25bedd18bb12f684ba868eccebf2(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d66bbde88d332dceb0812bb6bbf08c2418490d8b0e9774a97971a3b895f48b8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa50ba289bb96ea508cb6a4202ffc1689e383887b754b989d8350c1e79bdf41c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d9b73e29df1d36e34609deddf6492296be4ec0e0c99ae60a05f9cab95febd6e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39db05833c4ce77a84e366d7b58478b995b315232f05d9f9932602373f9c2c7f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bf53e865a22afeab85ecdb04fcf364678cf903b5624472147bf80f81f04730f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59c0d69a72a95b731117630b98efd8729539c64fef15303dab4addb9eae6ffa4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.ReferenceItemProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5edec3d71b0ff38cdce6ec8a872457ab8f95894314688d3b059e6b2fd20a3c07(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.SseConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e84dfea35f835d11c086ac495c8e1952da55b4069d246ca2b527bb2a7655e94(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAnnotationStore.StoreOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bd3f81b2e8f342de3db84fde3693c24cb6514a2f2b2e76534d5136fdc26945b(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f161bf0df41584a24622d738207d338081faec41cddac7f0cda31f0cbf50b695(
    *,
    reference_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b0283b46d5b34e1109c108b303d6ab3e549e041b5482192ec0ef37b83e6920(
    *,
    type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68b9968e466757cfc2e4ee7eb053201b466a44d185aa6082edce78e859f4f489(
    *,
    tsv_store_options: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.TsvStoreOptionsProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14b0c73be5d34083c239713770a8134020bc8cab75d4b0a1a82a28463074bb3d(
    *,
    annotation_type: typing.Optional[builtins.str] = None,
    format_to_header: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
    schema: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db27a54e4b1e96ecf8263cf950eaa96b8620641082ddea726be734d30e205831(
    *,
    name: builtins.str,
    store_format: builtins.str,
    description: typing.Optional[builtins.str] = None,
    reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.ReferenceItemProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    store_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAnnotationStore.StoreOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e38c503967033ff76d3e45880727cc62a1df749cb0aac8298f6d06d14d6e3320(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReferenceStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__183bf8595aa4fa216452da5239ca1639a58401e756cb23717c36ec75daa0a396(
    resource: _IReferenceStoreRef_e44b493e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03eab96b33743423157434263c495ecf4bb597bb49fcadef0690e503e3540689(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d3a144262ad49c5d6ecb97bcdeda753c5514368bac2ab437b403dd5ecbff176(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    reference_store_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37cb4b310cd2f37468be221e1f8c07466a5f9c1031fbf8c2b24f0722a58417c4(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d75805be97b46dc8c38477db9eef63661d2478cb95cd31687daa2a21a351dfd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a01b78cf451516a0eb2572826af339a051c95495f454b03b62693537679d6e9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a1e17328f2c1518d508a235b2c42ef44e871bafb1772ad49e45f0b8d5583ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c89d0da98832090d35c5574aec7e23cd54990b36f1507999a687aed1e0a56bbb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63bf4a022de72dc8d560891710d6dee497173e638e81419fd5d8b3c20d9a650b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnReferenceStore.SseConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5978dd78915de34b6caff418b41982c856f0f6071f77fc0f1306963a5cfe845e(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a277036a5a95a03f8b276d47ec8bcb3f25bf4f304bc5ee7452d8472c7e1ada3a(
    *,
    type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa5ddefbb60b1902a7a8a0da56893c57cde7f27eb458a6b71907aad7ac2b4ca(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReferenceStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d92bdf2175b79063decd2ff3bbf2745e423b61fa98f3bf6b832b7632771b7e8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    max_cpus: typing.Optional[jsii.Number] = None,
    max_duration: typing.Optional[jsii.Number] = None,
    max_gpus: typing.Optional[jsii.Number] = None,
    max_runs: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db1a82ee01daefb6257f7e73e38ab5b5e98e001181ab9869f5d6dd18e3cc3993(
    resource: _IRunGroupRef_937b5363,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a98b2a8d393a5018138cf8c7c78a10435f63b2eea12b677df4c77fca4365013d(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34a9f76d09fa73ea3c0c86debaea039d1ecfeb5a751151276cc0002d8d2737c1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61e5e671b78fea2bdc872b82befc94adc6014522a707589b79b6dc63795f14c0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2024f9c040e790d1988694b9f616763247d6b00f2fdcd97552dbe2c3cae45b40(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6aa9c45084b47d1e497a843bdc464ca31516a118303fa388c0f5db7b5bbd3630(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1884be9d7a33f4597167d89c5fb81946a94d32f6879e4877ffa669c1ef0f4f7(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__235fda5a64dcc62cd14ad311c90dce78abbc930ce336e74e69a63f027c84b0c0(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14846c448c724a5e0421b3370cbf6d8071cc9d1d1f7f635d8b528b854c1db3a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f64a1ae8ed7c7141ee2c0e9f12df462d424e227637fb190daac9751a95f18d1a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0687d84f98238d006185c8fc00317ac96c5244d8d1b550e56fda04cb4eca97f9(
    *,
    max_cpus: typing.Optional[jsii.Number] = None,
    max_duration: typing.Optional[jsii.Number] = None,
    max_gpus: typing.Optional[jsii.Number] = None,
    max_runs: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a589aadb7c598845d5e4c6ef138fe8cbeb7253209ba9eb0e5e590611eec980dc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    access_log_location: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    e_tag_algorithm_family: typing.Optional[builtins.str] = None,
    fallback_location: typing.Optional[builtins.str] = None,
    propagated_set_level_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    s3_access_policy: typing.Any = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSequenceStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9a735aaa47b911b08cfd5af5019bd48d4f4d14bcdffa2fef80322b11f850d47(
    resource: _ISequenceStoreRef_d8ce7b6b,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0401ce1b5169b8a6f265ee186bf5ea3e78a0a8a2b71e6256e2a1effe74e148d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__939e1e0c5383ed843656a8c66c9eeac470cdb45344d2aa8c6353ab2273bb3618(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    sequence_store_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d2570829ea1706cde1490e1a50299861f8a0479fe93d29fc4d8c19b41689f96(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea9a45fe9e84d5319386c1a777f6361e3fed5c916c543c8964323b54759ee470(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7932486ef43d64891becc28acf4d1c7abdf6063eb9aa69d9bffa95c24d2d9d9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8e53b0b20084e7e23dc393ceafe95167d7bce2ef95f48e5bca0556a29d78fa9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7549c525ad472ac7db5f5282211a0aac7a47906e8ed893e7de2371f8677691f0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__128fafb1df9e961d7c5982e50a60c29fbada98403f437d20e8bab3669320ca5c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0fd26684f557f3150b6eaf7b8b6f5ea741a5a2ba9e37d4a05ec66dea9e5c724(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f87faaa51a41810707e9283275d0283e54c3ebebf2803e01abef2984151aca1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94d2835859304a00ff97481068a5f88aa75e5f963a8554869a9bb60a55200b93(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d38bc4fc98e65bd66719d736641dbe0eef30ad1a6a932a71665c6fd3c7a01c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92eed2332efa6d161a72ca8ae646e24cacee45f7acbbbb2e0aacb4b034c468be(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSequenceStore.SseConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ce2c9ded7857e7f4d2115b4b17528bedb51685351fbcf322f7727f4fcf76354(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16d14d56ac16dd0c8b7ee5046e40e324719a67cf46d9a70bdf176e614b6904fc(
    *,
    type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c912afa5be2bea750b085186b08f53bd688bc0a1dd08b1f1c6951a21015380fc(
    *,
    name: builtins.str,
    access_log_location: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    e_tag_algorithm_family: typing.Optional[builtins.str] = None,
    fallback_location: typing.Optional[builtins.str] = None,
    propagated_set_level_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    s3_access_policy: typing.Any = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSequenceStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d38872c12590b13122bc23c110efd40d1aa8369a37e1015fcc0ee2529e01904(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVariantStore.ReferenceItemProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVariantStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b7a9767f78947b0511605022e00727fbf04af579b424576a2d6c01b31b28ba8(
    resource: _IVariantStoreRef_49e3cae7,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f419b3d012ad3960d3cb7ca202c16de7716902d7708b8a5f93c80ecc69b0794(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    variant_store_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491360ac38318f0cc89b8ce7f0ac1b68853729c931ed3c5f800ae95f95f7dc86(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ca6bc97e153eee8b1d732a90be1690a35fffe864b7b05aaaac9e52711640fed(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__570cd7098cbc0f8a1520e467e899d1d2ec7d6bc45da494a51344b868369142a6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a7151068f14ce10b8b0f9147b1e5b5afd6f6b7308067934acd8af16a512c243(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088cb3f651ad7a064e751c97def87bcf2e6e4149c7bcf54b57474d4b8b7d1b6d(
    value: typing.Union[_IResolvable_da3f097b, CfnVariantStore.ReferenceItemProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b58e2ea0e9ae60ac9a3dd7935556c2d0e2dfe3ff2de0f2ef79c50a0f2cdc07d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14ca86abdbf91bcd47e50c693a441fd60292ffbe1b4f732e112498a42712d29e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVariantStore.SseConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58acd4facff447c8ba521704b60e2e575ce07cca5086f7089300382b0d72deb1(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d03f1b71084719c634c1eec42eaa49cce433fd4e222652c52e9ca9afca86c44(
    *,
    reference_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__151f006e709dbecd4ae7c2469b6d65397d70b22812c239977c3f339440eefaf8(
    *,
    type: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cee3839b5919ab156aab54490277c559d790311fd9ea2b761f99373fdb7eaec(
    *,
    name: builtins.str,
    reference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVariantStore.ReferenceItemProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    sse_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVariantStore.SseConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2d05cb293836959a925b22dbe1861bc4457d2d510bd3a480ae858ea9f00850d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    accelerators: typing.Optional[builtins.str] = None,
    container_registry_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.ContainerRegistryMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    container_registry_map_uri: typing.Optional[builtins.str] = None,
    definition_repository: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.DefinitionRepositoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    definition_uri: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    engine: typing.Optional[builtins.str] = None,
    main: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    parameter_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    parameter_template_path: typing.Optional[builtins.str] = None,
    readme_markdown: typing.Optional[builtins.str] = None,
    readme_path: typing.Optional[builtins.str] = None,
    readme_uri: typing.Optional[builtins.str] = None,
    storage_capacity: typing.Optional[jsii.Number] = None,
    storage_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    workflow_bucket_owner_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67df20aaeaafc046258133711462983b03f7d276f5db7702f3acf0f303341182(
    resource: _IWorkflowRef_c34b3fa1,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85eaacf4591f2168dc63862126dd9dd0579c6fdfc3c94bffdd6d2a411210f03e(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98655701238267dcfc2598ca58d2fdf3b94be0fdd6d36c6407b8c9216e530168(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3d18757469eec460375791b428b2b2a8ebd5be703fbc705cb706233f42a0050(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__286f71b00d1993ebc792c6e260606dac95cf17ec599b45b4cb2111b4ca57a0fe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d61321fc4a694dded60b8fceeeafd83e9ae3f79a0329bdba98cd03787f3daa3c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkflow.ContainerRegistryMapProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1466a9fdbdff03b1c7b3fd5e72f7386ca160db487d501609519ca1c35a987aca(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b6e4242f1457a50b9f5b17595e8985df9311b3b5ec98f525f390f9387770415(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkflow.DefinitionRepositoryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc102140c3b77bda25eda4edac3ddf245628b20791c9053f2a901ded02c9b780(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73c565083430765eb26563b0a57061f931b2ec1240d0b6c03b6bdad1003055c2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2edee5dfbe37830cd0e2e70344c7e33e9cf08c5c243438272da4a5634eae529f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f791067dcd2f7a992bf37cf0c6c81e381b2e0344e60cf85051d19bb08c69bf13(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6845f053d191fb8caa10b651afe2128f50703f821981813813ed0bb9862dad7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd71f853b8475a5b472d76bce0cd20afc1269357412bdaa83e29ea355af8f64b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnWorkflow.WorkflowParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d41351b64d942ee30b08547c1780197e0df1eca59541df6f21ad720a36cb6716(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecc1997459356ed8d8ca95f01eab7bd4215d815bf69cff594388b6f7222e0c8a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e36c31f82073225a89cc2a0da972aba7908d4ad2dd686757120c7089f99861(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28c67e6013e7a108b99f462f48461025e53196240b5182ef0ee813188829ec6a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37c3d929054386cb4ebdbc60c2c3558d7cd34bed65861db5661f96d5d75ce7df(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82b78c9fdaf5e3e15a75209f5d891cf1513f47077977c45c2d020ffe13e990ac(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__651d8f1caf8b2c987665acfeae50e19a5626bb723832dae7067c423aab3ac2b5(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fec2ca5e32cee87eaac65d878c60669f18bb90724ac13ab05f21221ebd80766e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b93208b886c42793f6b22971c79ed50b456a125a28fedf2949548b0a03f82c3e(
    *,
    image_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.ImageMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    registry_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.RegistryMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c23b09e8f18584c69d282b6816697f2992e22dbf81773246b66875fbb0c0c8(
    *,
    connection_arn: typing.Optional[builtins.str] = None,
    exclude_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    full_repository_id: typing.Optional[builtins.str] = None,
    source_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.SourceReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98f85817eb366199f668581daf61aabd43de777e1bd4110572941bbd0bb03687(
    *,
    destination_image: typing.Optional[builtins.str] = None,
    source_image: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf8725b8e4b50a33568267e8b0666f0c8b9e8a47c56098879cb0cdba27310fbf(
    *,
    ecr_account_id: typing.Optional[builtins.str] = None,
    ecr_repository_prefix: typing.Optional[builtins.str] = None,
    upstream_registry_url: typing.Optional[builtins.str] = None,
    upstream_repository_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4e57d9f64919c2d451cd965846e1f5ee2aa3404611459632e4dd2699b4654d1(
    *,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beb0e924d2102ff644fd2da920cdd60f013b66e8285db8ffc0ce774a694580a5(
    *,
    description: typing.Optional[builtins.str] = None,
    optional: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09bedca50200dd06a4bbe4bb6135e76dacff76287249f3d28b8f285f8205f173(
    *,
    accelerators: typing.Optional[builtins.str] = None,
    container_registry_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.ContainerRegistryMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    container_registry_map_uri: typing.Optional[builtins.str] = None,
    definition_repository: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.DefinitionRepositoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    definition_uri: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    engine: typing.Optional[builtins.str] = None,
    main: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    parameter_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    parameter_template_path: typing.Optional[builtins.str] = None,
    readme_markdown: typing.Optional[builtins.str] = None,
    readme_path: typing.Optional[builtins.str] = None,
    readme_uri: typing.Optional[builtins.str] = None,
    storage_capacity: typing.Optional[jsii.Number] = None,
    storage_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    workflow_bucket_owner_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9bbd83c3821b6d01e1b0445c2a66c0e7c312d81583ae6cf8dbe78c8d6a4bf99(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    version_name: builtins.str,
    workflow_id: builtins.str,
    accelerators: typing.Optional[builtins.str] = None,
    container_registry_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowVersion.ContainerRegistryMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    container_registry_map_uri: typing.Optional[builtins.str] = None,
    definition_repository: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowVersion.DefinitionRepositoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    definition_uri: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    engine: typing.Optional[builtins.str] = None,
    main: typing.Optional[builtins.str] = None,
    parameter_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowVersion.WorkflowParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    parameter_template_path: typing.Optional[builtins.str] = None,
    readme_markdown: typing.Optional[builtins.str] = None,
    readme_path: typing.Optional[builtins.str] = None,
    readme_uri: typing.Optional[builtins.str] = None,
    storage_capacity: typing.Optional[jsii.Number] = None,
    storage_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    workflow_bucket_owner_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba9428a8b7901e336eeab6247d137358ee9bc60145cd3f57cd9d69410752a02c(
    resource: _IWorkflowVersionRef_8e877e7d,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c7054b8c2aebdab065713b2bf74644dd2b89b4b92f0f3161c76b3b26d5273ab(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a7de38e00c231b3afd92bbb59cad40657b334333096dde12413f391ade16867(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1461fce0dec6c9339e6bbc0df050886fb1f30852661c80911b28268bdee03c9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9f5bdcc4a225102f171d30f4738ab832792497c08ecb206114ad57125adf01(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5def0afb0cd8ab9471e48b541cd9dceaeb6826bfe7a8a24d0c36614c73b1a6d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b69952a53a68976751566fbcf17774d0dfa2d7ede106cb440b751f76c7eb99ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46a9bb90d987260f113e2b2c7bfe0d00e76229ce25afbfccf1a386b82f85e224(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkflowVersion.ContainerRegistryMapProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65acb20ad98b8b631169a3db99c88bd3662a7e2bd947577b5265d087e4b8362d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76f88fb7dbfba72f92fec4a64878a9e7fdd595353c2e76e5f675a9f318a5b5e6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkflowVersion.DefinitionRepositoryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a8ff1e5a2ba3fcf1c5fb306e96445a76ec1ac6872615b206206a2a173f64978(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d26e61de900859028fd4b5aff7eb7fefa87386da043d620b3407bc69ef3f950b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ade62566da0dd0e16cdb86d20bb176d8778e02a5223101deea2467f1ee7cadc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb201e46965fe4b385e0e52f84a505023c34c0c16c33aea7e75a09209c34d1af(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__909f80095cd6043c196e37a387a0f1f32bfcddcd8f9a81c5e8f5ac8b4874faa9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnWorkflowVersion.WorkflowParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1012e58717a3baf054312a40aba36847bbd98b702310ea8aff265f26caeab471(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cea66896cfd0dfa12a8b3d0b44794207352c9c78eb70c50e46466b4eea34898(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40cad564b15c28b2c112ad54de257f81d4d31fdfe311871657ae5bd714eb9ee6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abe09bb1e32d84773aaf309a744224900a63bf483fa24970e875c0b0a2f1b1cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba60096260fa288ca386a5b2841efb8fa9833ea893400efeba006766f392a7b7(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50ce9715f4efa14e458d6207fae79f6b0ebc36a3bf74435e024116d9f8060ca2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfbcbf729952f991d2243244c21c373b5bf1a3947ed2973ab1664037cdf636f8(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc6b06c168132bf54bf849b9d49774230af45a049e67f52bc48dd0220c18775d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32eb3bf30b3d01f44e56bdf643f62609b8cbc84d473cb19e3564543b645033d4(
    *,
    image_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowVersion.ImageMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    registry_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowVersion.RegistryMappingProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0748aa0fb5a9a9d624696b0fc54ab2faf0941992918eb234ba6c3bb4a47aef5(
    *,
    connection_arn: typing.Optional[builtins.str] = None,
    exclude_file_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
    full_repository_id: typing.Optional[builtins.str] = None,
    source_reference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowVersion.SourceReferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__421f9ca400f5d5d6c3aa9a53dbe35757f3408b2b30be15794288deb51c48b293(
    *,
    destination_image: typing.Optional[builtins.str] = None,
    source_image: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9eab95380e8258bf7a10a1ed8080d039134ac7daf1f5f0c979d28cb4f5c4f426(
    *,
    ecr_account_id: typing.Optional[builtins.str] = None,
    ecr_repository_prefix: typing.Optional[builtins.str] = None,
    upstream_registry_url: typing.Optional[builtins.str] = None,
    upstream_repository_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd0032779911f1051b3896f001118256f2cbf0d060b22c10b5fdeb3b3e488c73(
    *,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d434101b6df92e22ac3acf923cd7bb4105c1a82dad119b383839a4f14189485(
    *,
    description: typing.Optional[builtins.str] = None,
    optional: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32259ddc7b7d888918efaf09deb63ba780f3721ec1da9ea606ed8100a4b9fb3e(
    *,
    version_name: builtins.str,
    workflow_id: builtins.str,
    accelerators: typing.Optional[builtins.str] = None,
    container_registry_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowVersion.ContainerRegistryMapProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    container_registry_map_uri: typing.Optional[builtins.str] = None,
    definition_repository: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowVersion.DefinitionRepositoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    definition_uri: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    engine: typing.Optional[builtins.str] = None,
    main: typing.Optional[builtins.str] = None,
    parameter_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflowVersion.WorkflowParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    parameter_template_path: typing.Optional[builtins.str] = None,
    readme_markdown: typing.Optional[builtins.str] = None,
    readme_path: typing.Optional[builtins.str] = None,
    readme_uri: typing.Optional[builtins.str] = None,
    storage_capacity: typing.Optional[jsii.Number] = None,
    storage_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    workflow_bucket_owner_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
