r'''
# AWS::S3Vectors Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_s3vectors as s3vectors
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for S3Vectors construct libraries](https://constructs.dev/search?q=s3vectors)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::S3Vectors resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Vectors.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::S3Vectors](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_S3Vectors.html).

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
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_s3vectors import (
    IIndexRef as _IIndexRef_4272045e,
    IVectorBucketPolicyRef as _IVectorBucketPolicyRef_9ad4e2a8,
    IVectorBucketRef as _IVectorBucketRef_238bcb24,
    IndexReference as _IndexReference_f8041417,
    VectorBucketPolicyReference as _VectorBucketPolicyReference_3f2d6cbc,
    VectorBucketReference as _VectorBucketReference_62393c93,
)


@jsii.implements(_IInspectable_c2943556, _IIndexRef_4272045e, _ITaggableV2_4e6798f8)
class CfnIndex(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3vectors.CfnIndex",
):
    '''The ``AWS::S3Vectors::Index`` resource defines a vector index within an Amazon S3 vector bucket.

    For more information, see `Creating a vector index in a vector bucket <https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-create-index.html>`_ in the *Amazon Simple Storage Service User Guide* .

    You must specify either ``VectorBucketName`` or ``VectorBucketArn`` to identify the bucket that contains the index.

    To control how AWS CloudFormation handles the vector index when the stack is deleted, you can set a deletion policy for your index. You can choose to *retain* the index or to *delete* the index. For more information, see `DeletionPolicy attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html>`_ .

    - **Permissions** - The required permissions for CloudFormation to use are based on the operations that are performed on the stack.
    - Create
    - s3vectors:CreateIndex
    - s3vectors:GetIndex
    - Read
    - s3vectors:GetIndex
    - Delete
    - s3vectors:DeleteIndex
    - s3vectors:GetIndex
    - List
    - s3vectors:ListIndexes

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html
    :cloudformationResource: AWS::S3Vectors::Index
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3vectors as s3vectors
        
        cfn_index = s3vectors.CfnIndex(self, "MyCfnIndex",
            data_type="dataType",
            dimension=123,
            distance_metric="distanceMetric",
        
            # the properties below are optional
            encryption_configuration=s3vectors.CfnIndex.EncryptionConfigurationProperty(
                kms_key_arn="kmsKeyArn",
                sse_type="sseType"
            ),
            index_name="indexName",
            metadata_configuration=s3vectors.CfnIndex.MetadataConfigurationProperty(
                non_filterable_metadata_keys=["nonFilterableMetadataKeys"]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vector_bucket_arn="vectorBucketArn",
            vector_bucket_name="vectorBucketName"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        data_type: builtins.str,
        dimension: jsii.Number,
        distance_metric: builtins.str,
        encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnIndex.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        index_name: typing.Optional[builtins.str] = None,
        metadata_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnIndex.MetadataConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        vector_bucket_arn: typing.Optional[builtins.str] = None,
        vector_bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::S3Vectors::Index``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param data_type: The data type of the vectors to be inserted into the vector index. Currently, only ``float32`` is supported, which represents 32-bit floating-point numbers.
        :param dimension: The dimensions of the vectors to be inserted into the vector index. This value must be between 1 and 4096, inclusive. All vectors stored in the index must have the same number of dimensions. The dimension value affects the storage requirements and search performance. Higher dimensions require more storage space and may impact search latency.
        :param distance_metric: The distance metric to be used for similarity search. Valid values are:. - ``cosine`` - Measures the cosine of the angle between two vectors. - ``euclidean`` - Measures the straight-line distance between two points in multi-dimensional space. Lower values indicate greater similarity.
        :param encryption_configuration: The encryption configuration for a vector index. By default, if you don't specify, all new vectors in the vector index will use the encryption configuration of the vector bucket.
        :param index_name: The name of the vector index to create. The index name must be between 3 and 63 characters long and can contain only lowercase letters, numbers, hyphens (-), and dots (.). The index name must be unique within the vector bucket. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the index name. .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
        :param metadata_configuration: The metadata configuration for the vector index.
        :param tags: User tags (key-value pairs) to associate with the index.
        :param vector_bucket_arn: The Amazon Resource Name (ARN) of the vector bucket that contains the vector index.
        :param vector_bucket_name: The name of the vector bucket that contains the vector index.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87bd43a194666dd054aecee5dc42b978d33dae31b98b1bacec49341d4916205e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIndexProps(
            data_type=data_type,
            dimension=dimension,
            distance_metric=distance_metric,
            encryption_configuration=encryption_configuration,
            index_name=index_name,
            metadata_configuration=metadata_configuration,
            tags=tags,
            vector_bucket_arn=vector_bucket_arn,
            vector_bucket_name=vector_bucket_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForIndex")
    @builtins.classmethod
    def arn_for_index(cls, resource: "_IIndexRef_4272045e") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32e62c574691f1e6a9b9acb81be5224bf6aefeb13ff8a3279c085732027b3ece)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForIndex", [resource]))

    @jsii.member(jsii_name="isCfnIndex")
    @builtins.classmethod
    def is_cfn_index(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnIndex.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcff37fdf03ad5adbbed6ad76ecd89562dab8f009aea7435b74d00f4dbfe01a4)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnIndex", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abf75f37384ae6010cf34366284fd709b9bf09472bc476d814cde62f1244e1f5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__731726592378e5451eb8d8956c8a160ef274b5bd0d04312393ac06dda83e154f)
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
        '''Returns the date and time when the vector index was created.

        Example: ``2024-12-21T10:30:00Z``

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrIndexArn")
    def attr_index_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the specified index.

        Example: ``arn:aws:s3vectors:us-east-1:123456789012:bucket/amzn-s3-demo-vector-bucket/index/my-index``

        :cloudformationAttribute: IndexArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIndexArn"))

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
    @jsii.member(jsii_name="indexRef")
    def index_ref(self) -> "_IndexReference_f8041417":
        '''A reference to a Index resource.'''
        return typing.cast("_IndexReference_f8041417", jsii.get(self, "indexRef"))

    @builtins.property
    @jsii.member(jsii_name="dataType")
    def data_type(self) -> builtins.str:
        '''The data type of the vectors to be inserted into the vector index.'''
        return typing.cast(builtins.str, jsii.get(self, "dataType"))

    @data_type.setter
    def data_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c823d66dd49125b2784b64987a69c1442232d36162528420c812cdaf0483bb62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="dimension")
    def dimension(self) -> jsii.Number:
        '''The dimensions of the vectors to be inserted into the vector index.'''
        return typing.cast(jsii.Number, jsii.get(self, "dimension"))

    @dimension.setter
    def dimension(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__709ca3449db711fe8736cb15c71a260517a124f93ed8f0f8ea0fd07224b34491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dimension", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="distanceMetric")
    def distance_metric(self) -> builtins.str:
        '''The distance metric to be used for similarity search.

        Valid values are:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "distanceMetric"))

    @distance_metric.setter
    def distance_metric(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd2e189f3b0010c6a77fa4f43ad73f492b5e1099536bd12a0ebe077c09648a0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "distanceMetric", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnIndex.EncryptionConfigurationProperty"]]:
        '''The encryption configuration for a vector index.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnIndex.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnIndex.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3562181b475724860644b029c5aa0b0da6ef36ffc910f5b75f4a2ca99b0ad526)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="indexName")
    def index_name(self) -> typing.Optional[builtins.str]:
        '''The name of the vector index to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexName"))

    @index_name.setter
    def index_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aff851423be8566880565e79db1928638490e19822427a39ecb4692fac23aba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="metadataConfiguration")
    def metadata_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnIndex.MetadataConfigurationProperty"]]:
        '''The metadata configuration for the vector index.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnIndex.MetadataConfigurationProperty"]], jsii.get(self, "metadataConfiguration"))

    @metadata_configuration.setter
    def metadata_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnIndex.MetadataConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adf0789238c3ff54ec752516d17506a5dc3025daf5543ed37b3703a9638c6ce3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''User tags (key-value pairs) to associate with the index.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be4bbbd8df829f30f21de18dbcd012115700ffb27edd6ce3da3b491d6d136392)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vectorBucketArn")
    def vector_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the vector bucket that contains the vector index.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vectorBucketArn"))

    @vector_bucket_arn.setter
    def vector_bucket_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dac369cc81e6a72eae40497750fec7e4bb88a8f4e2eb0a59dcbce3ecef2449ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vectorBucketArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vectorBucketName")
    def vector_bucket_name(self) -> typing.Optional[builtins.str]:
        '''The name of the vector bucket that contains the vector index.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vectorBucketName"))

    @vector_bucket_name.setter
    def vector_bucket_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__626d4bf5143365f338c97aea670a95f8c1fbfa0ad3a9cc00928821e5edb04014)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vectorBucketName", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3vectors.CfnIndex.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_arn": "kmsKeyArn", "sse_type": "sseType"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            kms_key_arn: typing.Optional[builtins.str] = None,
            sse_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The encryption configuration for a vector bucket or index.

            By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically ``AES256`` . You can optionally override bucket level encryption settings, and set a specific encryption configuration for a vector index at the time of index creation.

            :param kms_key_arn: AWS Key Management Service (KMS) customer managed key ID to use for the encryption configuration. This parameter is allowed if and only if ``sseType`` is set to ``aws:kms`` . To specify the KMS key, you must use the format of the KMS key Amazon Resource Name (ARN). For example, specify Key ARN in the following format: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``
            :param sse_type: The server-side encryption type to use for the encryption configuration of the vector bucket. By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically ``AES256`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3vectors-index-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3vectors as s3vectors
                
                encryption_configuration_property = s3vectors.CfnIndex.EncryptionConfigurationProperty(
                    kms_key_arn="kmsKeyArn",
                    sse_type="sseType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f9165e9fb93aff2add01bdd93a7038addf5ef28b5c63327f886cde432f32daca)
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
                check_type(argname="argument sse_type", value=sse_type, expected_type=type_hints["sse_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn
            if sse_type is not None:
                self._values["sse_type"] = sse_type

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''AWS Key Management Service (KMS) customer managed key ID to use for the encryption configuration.

            This parameter is allowed if and only if ``sseType`` is set to ``aws:kms`` .

            To specify the KMS key, you must use the format of the KMS key Amazon Resource Name (ARN).

            For example, specify Key ARN in the following format: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3vectors-index-encryptionconfiguration.html#cfn-s3vectors-index-encryptionconfiguration-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sse_type(self) -> typing.Optional[builtins.str]:
            '''The server-side encryption type to use for the encryption configuration of the vector bucket.

            By default, if you don't specify, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically ``AES256`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3vectors-index-encryptionconfiguration.html#cfn-s3vectors-index-encryptionconfiguration-ssetype
            '''
            result = self._values.get("sse_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3vectors.CfnIndex.MetadataConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"non_filterable_metadata_keys": "nonFilterableMetadataKeys"},
    )
    class MetadataConfigurationProperty:
        def __init__(
            self,
            *,
            non_filterable_metadata_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The metadata configuration for the vector index.

            This configuration allows you to specify which metadata keys should be treated as non-filterable.

            :param non_filterable_metadata_keys: Non-filterable metadata keys allow you to enrich vectors with additional context during storage and retrieval. Unlike default metadata keys, these keys can't be used as query filters. Non-filterable metadata keys can be retrieved but can't be searched, queried, or filtered. You can access non-filterable metadata keys of your vectors after finding the vectors. You can specify 1 to 10 non-filterable metadata keys. Each key must be 1 to 63 characters long.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3vectors-index-metadataconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3vectors as s3vectors
                
                metadata_configuration_property = s3vectors.CfnIndex.MetadataConfigurationProperty(
                    non_filterable_metadata_keys=["nonFilterableMetadataKeys"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__02647dc0f92f11b90c5132d15f87d8d903be3aad20d526f7d8a526c8d3fc1268)
                check_type(argname="argument non_filterable_metadata_keys", value=non_filterable_metadata_keys, expected_type=type_hints["non_filterable_metadata_keys"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if non_filterable_metadata_keys is not None:
                self._values["non_filterable_metadata_keys"] = non_filterable_metadata_keys

        @builtins.property
        def non_filterable_metadata_keys(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''Non-filterable metadata keys allow you to enrich vectors with additional context during storage and retrieval.

            Unlike default metadata keys, these keys can't be used as query filters. Non-filterable metadata keys can be retrieved but can't be searched, queried, or filtered. You can access non-filterable metadata keys of your vectors after finding the vectors.

            You can specify 1 to 10 non-filterable metadata keys. Each key must be 1 to 63 characters long.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3vectors-index-metadataconfiguration.html#cfn-s3vectors-index-metadataconfiguration-nonfilterablemetadatakeys
            '''
            result = self._values.get("non_filterable_metadata_keys")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetadataConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3vectors.CfnIndexProps",
    jsii_struct_bases=[],
    name_mapping={
        "data_type": "dataType",
        "dimension": "dimension",
        "distance_metric": "distanceMetric",
        "encryption_configuration": "encryptionConfiguration",
        "index_name": "indexName",
        "metadata_configuration": "metadataConfiguration",
        "tags": "tags",
        "vector_bucket_arn": "vectorBucketArn",
        "vector_bucket_name": "vectorBucketName",
    },
)
class CfnIndexProps:
    def __init__(
        self,
        *,
        data_type: builtins.str,
        dimension: jsii.Number,
        distance_metric: builtins.str,
        encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnIndex.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        index_name: typing.Optional[builtins.str] = None,
        metadata_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnIndex.MetadataConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        vector_bucket_arn: typing.Optional[builtins.str] = None,
        vector_bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnIndex``.

        :param data_type: The data type of the vectors to be inserted into the vector index. Currently, only ``float32`` is supported, which represents 32-bit floating-point numbers.
        :param dimension: The dimensions of the vectors to be inserted into the vector index. This value must be between 1 and 4096, inclusive. All vectors stored in the index must have the same number of dimensions. The dimension value affects the storage requirements and search performance. Higher dimensions require more storage space and may impact search latency.
        :param distance_metric: The distance metric to be used for similarity search. Valid values are:. - ``cosine`` - Measures the cosine of the angle between two vectors. - ``euclidean`` - Measures the straight-line distance between two points in multi-dimensional space. Lower values indicate greater similarity.
        :param encryption_configuration: The encryption configuration for a vector index. By default, if you don't specify, all new vectors in the vector index will use the encryption configuration of the vector bucket.
        :param index_name: The name of the vector index to create. The index name must be between 3 and 63 characters long and can contain only lowercase letters, numbers, hyphens (-), and dots (.). The index name must be unique within the vector bucket. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the index name. .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
        :param metadata_configuration: The metadata configuration for the vector index.
        :param tags: User tags (key-value pairs) to associate with the index.
        :param vector_bucket_arn: The Amazon Resource Name (ARN) of the vector bucket that contains the vector index.
        :param vector_bucket_name: The name of the vector bucket that contains the vector index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3vectors as s3vectors
            
            cfn_index_props = s3vectors.CfnIndexProps(
                data_type="dataType",
                dimension=123,
                distance_metric="distanceMetric",
            
                # the properties below are optional
                encryption_configuration=s3vectors.CfnIndex.EncryptionConfigurationProperty(
                    kms_key_arn="kmsKeyArn",
                    sse_type="sseType"
                ),
                index_name="indexName",
                metadata_configuration=s3vectors.CfnIndex.MetadataConfigurationProperty(
                    non_filterable_metadata_keys=["nonFilterableMetadataKeys"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vector_bucket_arn="vectorBucketArn",
                vector_bucket_name="vectorBucketName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ea84a5df8ebf668282b156128f8a09e7618a68ade5fffdf6ff86d39157f5a5d)
            check_type(argname="argument data_type", value=data_type, expected_type=type_hints["data_type"])
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument distance_metric", value=distance_metric, expected_type=type_hints["distance_metric"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument index_name", value=index_name, expected_type=type_hints["index_name"])
            check_type(argname="argument metadata_configuration", value=metadata_configuration, expected_type=type_hints["metadata_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vector_bucket_arn", value=vector_bucket_arn, expected_type=type_hints["vector_bucket_arn"])
            check_type(argname="argument vector_bucket_name", value=vector_bucket_name, expected_type=type_hints["vector_bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "data_type": data_type,
            "dimension": dimension,
            "distance_metric": distance_metric,
        }
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if index_name is not None:
            self._values["index_name"] = index_name
        if metadata_configuration is not None:
            self._values["metadata_configuration"] = metadata_configuration
        if tags is not None:
            self._values["tags"] = tags
        if vector_bucket_arn is not None:
            self._values["vector_bucket_arn"] = vector_bucket_arn
        if vector_bucket_name is not None:
            self._values["vector_bucket_name"] = vector_bucket_name

    @builtins.property
    def data_type(self) -> builtins.str:
        '''The data type of the vectors to be inserted into the vector index.

        Currently, only ``float32`` is supported, which represents 32-bit floating-point numbers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html#cfn-s3vectors-index-datatype
        '''
        result = self._values.get("data_type")
        assert result is not None, "Required property 'data_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dimension(self) -> jsii.Number:
        '''The dimensions of the vectors to be inserted into the vector index.

        This value must be between 1 and 4096, inclusive. All vectors stored in the index must have the same number of dimensions.

        The dimension value affects the storage requirements and search performance. Higher dimensions require more storage space and may impact search latency.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html#cfn-s3vectors-index-dimension
        '''
        result = self._values.get("dimension")
        assert result is not None, "Required property 'dimension' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def distance_metric(self) -> builtins.str:
        '''The distance metric to be used for similarity search. Valid values are:.

        - ``cosine`` - Measures the cosine of the angle between two vectors.
        - ``euclidean`` - Measures the straight-line distance between two points in multi-dimensional space. Lower values indicate greater similarity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html#cfn-s3vectors-index-distancemetric
        '''
        result = self._values.get("distance_metric")
        assert result is not None, "Required property 'distance_metric' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnIndex.EncryptionConfigurationProperty"]]:
        '''The encryption configuration for a vector index.

        By default, if you don't specify, all new vectors in the vector index will use the encryption configuration of the vector bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html#cfn-s3vectors-index-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnIndex.EncryptionConfigurationProperty"]], result)

    @builtins.property
    def index_name(self) -> typing.Optional[builtins.str]:
        '''The name of the vector index to create.

        The index name must be between 3 and 63 characters long and can contain only lowercase letters, numbers, hyphens (-), and dots (.). The index name must be unique within the vector bucket.

        If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the index name.
        .. epigraph::

           If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html#cfn-s3vectors-index-indexname
        '''
        result = self._values.get("index_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnIndex.MetadataConfigurationProperty"]]:
        '''The metadata configuration for the vector index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html#cfn-s3vectors-index-metadataconfiguration
        '''
        result = self._values.get("metadata_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnIndex.MetadataConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''User tags (key-value pairs) to associate with the index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html#cfn-s3vectors-index-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def vector_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the vector bucket that contains the vector index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html#cfn-s3vectors-index-vectorbucketarn
        '''
        result = self._values.get("vector_bucket_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vector_bucket_name(self) -> typing.Optional[builtins.str]:
        '''The name of the vector bucket that contains the vector index.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-index.html#cfn-s3vectors-index-vectorbucketname
        '''
        result = self._values.get("vector_bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIndexProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IVectorBucketRef_238bcb24, _ITaggableV2_4e6798f8)
class CfnVectorBucket(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3vectors.CfnVectorBucket",
):
    '''Defines an Amazon S3 vector bucket in the same AWS Region where you create the AWS CloudFormation stack.

    Vector buckets are specialized storage containers designed for storing and managing vector data used in machine learning and AI applications. They provide optimized storage and retrieval capabilities for high-dimensional vector data.

    To control how AWS CloudFormation handles the bucket when the stack is deleted, you can set a deletion policy for your bucket. You can choose to *retain* the bucket or to *delete* the bucket. For more information, see `DeletionPolicy attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html>`_ .
    .. epigraph::

       You can only delete empty vector buckets. Deletion fails for buckets that have contents.

    - **Permissions** - The required permissions for CloudFormation to use are based on the operations that are performed on the stack.
    - Create
    - s3vectors:CreateVectorBucket
    - s3vectors:GetVectorBucket
    - kms:GenerateDataKey (if using KMS encryption)
    - Read
    - s3vectors:GetVectorBucket
    - kms:GenerateDataKey (if using KMS encryption)
    - Delete
    - s3vectors:DeleteVectorBucket
    - s3vectors:GetVectorBucket
    - kms:GenerateDataKey (if using KMS encryption)
    - List
    - s3vectors:ListVectorBuckets
    - kms:GenerateDataKey (if using KMS encryption)

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-vectorbucket.html
    :cloudformationResource: AWS::S3Vectors::VectorBucket
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3vectors as s3vectors
        
        cfn_vector_bucket = s3vectors.CfnVectorBucket(self, "MyCfnVectorBucket",
            encryption_configuration=s3vectors.CfnVectorBucket.EncryptionConfigurationProperty(
                kms_key_arn="kmsKeyArn",
                sse_type="sseType"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vector_bucket_name="vectorBucketName"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnVectorBucket.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        vector_bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::S3Vectors::VectorBucket``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param encryption_configuration: The encryption configuration for the vector bucket.
        :param tags: User tags (key-value pairs) to associate with the vector bucket.
        :param vector_bucket_name: A name for the vector bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). The bucket name must be unique in the same AWS account for each AWS Region. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must be between 3 and 63 characters long and must not contain uppercase characters or underscores. .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a52d66a4aae762d071703714133bff3215199691ee6f06fec05144ec742e090e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVectorBucketProps(
            encryption_configuration=encryption_configuration,
            tags=tags,
            vector_bucket_name=vector_bucket_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForVectorBucket")
    @builtins.classmethod
    def arn_for_vector_bucket(
        cls,
        resource: "_IVectorBucketRef_238bcb24",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89411d490809081b29a45d8c02fcb4cc145b0df3aed499145104f0657ba929f4)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForVectorBucket", [resource]))

    @jsii.member(jsii_name="isCfnVectorBucket")
    @builtins.classmethod
    def is_cfn_vector_bucket(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnVectorBucket.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9895d4c963c7fd96f4be56b99de4dab5b35aa0baafc908ffa5866a1330fe3a18)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnVectorBucket", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__640db6894c3240a3b378c5237337953d313c22d856cd2fb21a91ac21e141613c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ac846d2ab15e1003f215128393cef109784fe6985ec04a5d2e373121e5ee1cf)
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
        '''Returns the date and time when the vector bucket was created.

        Example: ``2024-12-21T10:30:00Z``

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrVectorBucketArn")
    def attr_vector_bucket_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the specified vector bucket.

        Example: ``arn:aws:s3vectors:us-east-1:123456789012:bucket/amzn-s3-demo-vector-bucket``

        :cloudformationAttribute: VectorBucketArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVectorBucketArn"))

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
    @jsii.member(jsii_name="vectorBucketRef")
    def vector_bucket_ref(self) -> "_VectorBucketReference_62393c93":
        '''A reference to a VectorBucket resource.'''
        return typing.cast("_VectorBucketReference_62393c93", jsii.get(self, "vectorBucketRef"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnVectorBucket.EncryptionConfigurationProperty"]]:
        '''The encryption configuration for the vector bucket.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnVectorBucket.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnVectorBucket.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__476996e4c3089c3364c3345d4c51c4d606b950b97248fc4afa1b8517c670f8f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''User tags (key-value pairs) to associate with the vector bucket.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b052022df884995ff323390b18015ff823b8b7d5553482a7666cc8e2bfda4e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vectorBucketName")
    def vector_bucket_name(self) -> typing.Optional[builtins.str]:
        '''A name for the vector bucket.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vectorBucketName"))

    @vector_bucket_name.setter
    def vector_bucket_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1879d6c9fc256da4dcb55ff2cd68263944a788d8c99c5f1e425ad9e64192a268)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vectorBucketName", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_s3vectors.CfnVectorBucket.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_arn": "kmsKeyArn", "sse_type": "sseType"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            kms_key_arn: typing.Optional[builtins.str] = None,
            sse_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the encryption configuration for the vector bucket.

            By default, all new vectors in Amazon S3 vector buckets use server-side encryption with Amazon S3 managed keys (SSE-S3), specifically AES256.

            :param kms_key_arn: AWS Key Management Service (KMS) customer managed key ARN to use for the encryption configuration. This parameter is required if and only if ``SseType`` is set to ``aws:kms`` . You must specify the full ARN of the KMS key. Key IDs or key aliases aren't supported. .. epigraph:: Amazon S3 Vectors only supports symmetric encryption KMS keys. For more information, see `Asymmetric keys in AWS KMS <https://docs.aws.amazon.com//kms/latest/developerguide/symmetric-asymmetric.html>`_ in the *AWS Key Management Service Developer Guide* .
            :param sse_type: The server-side encryption type to use for the encryption configuration of the vector bucket. Valid values are ``AES256`` for Amazon S3 managed keys and ``aws:kms`` for AWS KMS keys. Default: - "AES256"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3vectors-vectorbucket-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_s3vectors as s3vectors
                
                encryption_configuration_property = s3vectors.CfnVectorBucket.EncryptionConfigurationProperty(
                    kms_key_arn="kmsKeyArn",
                    sse_type="sseType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d4ba5067d69ad54e4dc886b50fef43813033e236d5cfc14a644bb2168b2cee94)
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
                check_type(argname="argument sse_type", value=sse_type, expected_type=type_hints["sse_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn
            if sse_type is not None:
                self._values["sse_type"] = sse_type

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''AWS Key Management Service (KMS) customer managed key ARN to use for the encryption configuration.

            This parameter is required if and only if ``SseType`` is set to ``aws:kms`` .

            You must specify the full ARN of the KMS key. Key IDs or key aliases aren't supported.
            .. epigraph::

               Amazon S3 Vectors only supports symmetric encryption KMS keys. For more information, see `Asymmetric keys in AWS KMS <https://docs.aws.amazon.com//kms/latest/developerguide/symmetric-asymmetric.html>`_ in the *AWS Key Management Service Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3vectors-vectorbucket-encryptionconfiguration.html#cfn-s3vectors-vectorbucket-encryptionconfiguration-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sse_type(self) -> typing.Optional[builtins.str]:
            '''The server-side encryption type to use for the encryption configuration of the vector bucket.

            Valid values are ``AES256`` for Amazon S3 managed keys and ``aws:kms`` for AWS KMS keys.

            :default: - "AES256"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3vectors-vectorbucket-encryptionconfiguration.html#cfn-s3vectors-vectorbucket-encryptionconfiguration-ssetype
            '''
            result = self._values.get("sse_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556, _IVectorBucketPolicyRef_9ad4e2a8)
class CfnVectorBucketPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_s3vectors.CfnVectorBucketPolicy",
):
    '''The ``AWS::S3Vectors::VectorBucketPolicy`` resource defines an Amazon S3 vector bucket policy to control access to an Amazon S3 vector bucket.

    Vector bucket policies are written in JSON and allow you to grant or deny permissions across all (or a subset of) objects within a vector bucket.

    You must specify either ``VectorBucketName`` or ``VectorBucketArn`` to identify the target bucket.

    To control how AWS CloudFormation handles the vector bucket policy when the stack is deleted, you can set a deletion policy for your policy. You can choose to *retain* the policy or to *delete* the policy. For more information, see `DeletionPolicy attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html>`_ .

    - **Permissions** - The required permissions for CloudFormation to use are based on the operations that are performed on the stack.
    - Create
    - s3vectors:GetVectorBucketPolicy
    - s3vectors:PutVectorBucketPolicy
    - Read
    - s3vectors:GetVectorBucketPolicy
    - Update
    - s3vectors:GetVectorBucketPolicy
    - s3vectors:PutVectorBucketPolicy
    - Delete
    - s3vectors:GetVectorBucketPolicy
    - s3vectors:DeleteVectorBucketPolicy
    - List
    - s3vectors:GetVectorBucketPolicy
    - s3vectors:ListVectorBuckets

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-vectorbucketpolicy.html
    :cloudformationResource: AWS::S3Vectors::VectorBucketPolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_s3vectors as s3vectors
        
        # policy: Any
        
        cfn_vector_bucket_policy = s3vectors.CfnVectorBucketPolicy(self, "MyCfnVectorBucketPolicy",
            policy=policy,
        
            # the properties below are optional
            vector_bucket_arn="vectorBucketArn",
            vector_bucket_name="vectorBucketName"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        policy: typing.Any,
        vector_bucket_arn: typing.Optional[builtins.str] = None,
        vector_bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::S3Vectors::VectorBucketPolicy``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy: A policy document containing permissions to add to the specified vector bucket. In IAM , you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM .
        :param vector_bucket_arn: The Amazon Resource Name (ARN) of the S3 vector bucket to which the policy applies.
        :param vector_bucket_name: The name of the S3 vector bucket to which the policy applies.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aee2d22aedfbf922cb325dc74e1f86dfd5fddeabc946e682b7e7daff49602847)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVectorBucketPolicyProps(
            policy=policy,
            vector_bucket_arn=vector_bucket_arn,
            vector_bucket_name=vector_bucket_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnVectorBucketPolicy")
    @builtins.classmethod
    def is_cfn_vector_bucket_policy(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnVectorBucketPolicy.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3726d6c463352d1ebd48e9e765a1a947a0c681b16f3cd62fcca774644436b8bb)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnVectorBucketPolicy", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b009bbcea5fa7fa263cab9d9522e5e301535b1ade8033c93631254bc35724d59)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d8f0d2d4e7a9dec45d4052937acaf1348456e0cc4ebdf7d82856c9846182f043)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="vectorBucketPolicyRef")
    def vector_bucket_policy_ref(self) -> "_VectorBucketPolicyReference_3f2d6cbc":
        '''A reference to a VectorBucketPolicy resource.'''
        return typing.cast("_VectorBucketPolicyReference_3f2d6cbc", jsii.get(self, "vectorBucketPolicyRef"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''A policy document containing permissions to add to the specified vector bucket.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13f1a283deb175d320cdff8d43b010c30ccafabd7821351f0b5c86ca7a48b31b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vectorBucketArn")
    def vector_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the S3 vector bucket to which the policy applies.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vectorBucketArn"))

    @vector_bucket_arn.setter
    def vector_bucket_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ba261025c54aa0fb18a9b5b2e3fab72be4ad30d1d852fc5f1492aa6911a8aad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vectorBucketArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vectorBucketName")
    def vector_bucket_name(self) -> typing.Optional[builtins.str]:
        '''The name of the S3 vector bucket to which the policy applies.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vectorBucketName"))

    @vector_bucket_name.setter
    def vector_bucket_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cca6053ffe0f77fd07d26cceada81f3e3e9e5b832049344b1f7d88c006f06d45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vectorBucketName", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3vectors.CfnVectorBucketPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy": "policy",
        "vector_bucket_arn": "vectorBucketArn",
        "vector_bucket_name": "vectorBucketName",
    },
)
class CfnVectorBucketPolicyProps:
    def __init__(
        self,
        *,
        policy: typing.Any,
        vector_bucket_arn: typing.Optional[builtins.str] = None,
        vector_bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVectorBucketPolicy``.

        :param policy: A policy document containing permissions to add to the specified vector bucket. In IAM , you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM .
        :param vector_bucket_arn: The Amazon Resource Name (ARN) of the S3 vector bucket to which the policy applies.
        :param vector_bucket_name: The name of the S3 vector bucket to which the policy applies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-vectorbucketpolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3vectors as s3vectors
            
            # policy: Any
            
            cfn_vector_bucket_policy_props = s3vectors.CfnVectorBucketPolicyProps(
                policy=policy,
            
                # the properties below are optional
                vector_bucket_arn="vectorBucketArn",
                vector_bucket_name="vectorBucketName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f526fb025093579ae7085ed34610b038bedad50bc4dda479dea96c217e4198e)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument vector_bucket_arn", value=vector_bucket_arn, expected_type=type_hints["vector_bucket_arn"])
            check_type(argname="argument vector_bucket_name", value=vector_bucket_name, expected_type=type_hints["vector_bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy": policy,
        }
        if vector_bucket_arn is not None:
            self._values["vector_bucket_arn"] = vector_bucket_arn
        if vector_bucket_name is not None:
            self._values["vector_bucket_name"] = vector_bucket_name

    @builtins.property
    def policy(self) -> typing.Any:
        '''A policy document containing permissions to add to the specified vector bucket.

        In IAM , you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-vectorbucketpolicy.html#cfn-s3vectors-vectorbucketpolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def vector_bucket_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the S3 vector bucket to which the policy applies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-vectorbucketpolicy.html#cfn-s3vectors-vectorbucketpolicy-vectorbucketarn
        '''
        result = self._values.get("vector_bucket_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vector_bucket_name(self) -> typing.Optional[builtins.str]:
        '''The name of the S3 vector bucket to which the policy applies.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-vectorbucketpolicy.html#cfn-s3vectors-vectorbucketpolicy-vectorbucketname
        '''
        result = self._values.get("vector_bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVectorBucketPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_s3vectors.CfnVectorBucketProps",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_configuration": "encryptionConfiguration",
        "tags": "tags",
        "vector_bucket_name": "vectorBucketName",
    },
)
class CfnVectorBucketProps:
    def __init__(
        self,
        *,
        encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnVectorBucket.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        vector_bucket_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVectorBucket``.

        :param encryption_configuration: The encryption configuration for the vector bucket.
        :param tags: User tags (key-value pairs) to associate with the vector bucket.
        :param vector_bucket_name: A name for the vector bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). The bucket name must be unique in the same AWS account for each AWS Region. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name. The bucket name must be between 3 and 63 characters long and must not contain uppercase characters or underscores. .. epigraph:: If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-vectorbucket.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_s3vectors as s3vectors
            
            cfn_vector_bucket_props = s3vectors.CfnVectorBucketProps(
                encryption_configuration=s3vectors.CfnVectorBucket.EncryptionConfigurationProperty(
                    kms_key_arn="kmsKeyArn",
                    sse_type="sseType"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vector_bucket_name="vectorBucketName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__557f3461f0c9f94a1c325dd824a3303ad88eff46565842be7f5c9f62ac2ce7dc)
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vector_bucket_name", value=vector_bucket_name, expected_type=type_hints["vector_bucket_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if tags is not None:
            self._values["tags"] = tags
        if vector_bucket_name is not None:
            self._values["vector_bucket_name"] = vector_bucket_name

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnVectorBucket.EncryptionConfigurationProperty"]]:
        '''The encryption configuration for the vector bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-vectorbucket.html#cfn-s3vectors-vectorbucket-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnVectorBucket.EncryptionConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''User tags (key-value pairs) to associate with the vector bucket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-vectorbucket.html#cfn-s3vectors-vectorbucket-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    @builtins.property
    def vector_bucket_name(self) -> typing.Optional[builtins.str]:
        '''A name for the vector bucket.

        The bucket name must contain only lowercase letters, numbers, and hyphens (-). The bucket name must be unique in the same AWS account for each AWS Region. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the bucket name.

        The bucket name must be between 3 and 63 characters long and must not contain uppercase characters or underscores.
        .. epigraph::

           If you specify a name, you can't perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you need to replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3vectors-vectorbucket.html#cfn-s3vectors-vectorbucket-vectorbucketname
        '''
        result = self._values.get("vector_bucket_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVectorBucketProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnIndex",
    "CfnIndexProps",
    "CfnVectorBucket",
    "CfnVectorBucketPolicy",
    "CfnVectorBucketPolicyProps",
    "CfnVectorBucketProps",
]

publication.publish()

def _typecheckingstub__87bd43a194666dd054aecee5dc42b978d33dae31b98b1bacec49341d4916205e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    data_type: builtins.str,
    dimension: jsii.Number,
    distance_metric: builtins.str,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    index_name: typing.Optional[builtins.str] = None,
    metadata_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.MetadataConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vector_bucket_arn: typing.Optional[builtins.str] = None,
    vector_bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32e62c574691f1e6a9b9acb81be5224bf6aefeb13ff8a3279c085732027b3ece(
    resource: _IIndexRef_4272045e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcff37fdf03ad5adbbed6ad76ecd89562dab8f009aea7435b74d00f4dbfe01a4(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abf75f37384ae6010cf34366284fd709b9bf09472bc476d814cde62f1244e1f5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__731726592378e5451eb8d8956c8a160ef274b5bd0d04312393ac06dda83e154f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c823d66dd49125b2784b64987a69c1442232d36162528420c812cdaf0483bb62(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__709ca3449db711fe8736cb15c71a260517a124f93ed8f0f8ea0fd07224b34491(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd2e189f3b0010c6a77fa4f43ad73f492b5e1099536bd12a0ebe077c09648a0b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3562181b475724860644b029c5aa0b0da6ef36ffc910f5b75f4a2ca99b0ad526(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aff851423be8566880565e79db1928638490e19822427a39ecb4692fac23aba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adf0789238c3ff54ec752516d17506a5dc3025daf5543ed37b3703a9638c6ce3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIndex.MetadataConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be4bbbd8df829f30f21de18dbcd012115700ffb27edd6ce3da3b491d6d136392(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dac369cc81e6a72eae40497750fec7e4bb88a8f4e2eb0a59dcbce3ecef2449ec(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__626d4bf5143365f338c97aea670a95f8c1fbfa0ad3a9cc00928821e5edb04014(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9165e9fb93aff2add01bdd93a7038addf5ef28b5c63327f886cde432f32daca(
    *,
    kms_key_arn: typing.Optional[builtins.str] = None,
    sse_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02647dc0f92f11b90c5132d15f87d8d903be3aad20d526f7d8a526c8d3fc1268(
    *,
    non_filterable_metadata_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ea84a5df8ebf668282b156128f8a09e7618a68ade5fffdf6ff86d39157f5a5d(
    *,
    data_type: builtins.str,
    dimension: jsii.Number,
    distance_metric: builtins.str,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    index_name: typing.Optional[builtins.str] = None,
    metadata_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIndex.MetadataConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vector_bucket_arn: typing.Optional[builtins.str] = None,
    vector_bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a52d66a4aae762d071703714133bff3215199691ee6f06fec05144ec742e090e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVectorBucket.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vector_bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89411d490809081b29a45d8c02fcb4cc145b0df3aed499145104f0657ba929f4(
    resource: _IVectorBucketRef_238bcb24,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9895d4c963c7fd96f4be56b99de4dab5b35aa0baafc908ffa5866a1330fe3a18(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__640db6894c3240a3b378c5237337953d313c22d856cd2fb21a91ac21e141613c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ac846d2ab15e1003f215128393cef109784fe6985ec04a5d2e373121e5ee1cf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__476996e4c3089c3364c3345d4c51c4d606b950b97248fc4afa1b8517c670f8f6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVectorBucket.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b052022df884995ff323390b18015ff823b8b7d5553482a7666cc8e2bfda4e2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1879d6c9fc256da4dcb55ff2cd68263944a788d8c99c5f1e425ad9e64192a268(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ba5067d69ad54e4dc886b50fef43813033e236d5cfc14a644bb2168b2cee94(
    *,
    kms_key_arn: typing.Optional[builtins.str] = None,
    sse_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aee2d22aedfbf922cb325dc74e1f86dfd5fddeabc946e682b7e7daff49602847(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy: typing.Any,
    vector_bucket_arn: typing.Optional[builtins.str] = None,
    vector_bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3726d6c463352d1ebd48e9e765a1a947a0c681b16f3cd62fcca774644436b8bb(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b009bbcea5fa7fa263cab9d9522e5e301535b1ade8033c93631254bc35724d59(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8f0d2d4e7a9dec45d4052937acaf1348456e0cc4ebdf7d82856c9846182f043(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13f1a283deb175d320cdff8d43b010c30ccafabd7821351f0b5c86ca7a48b31b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba261025c54aa0fb18a9b5b2e3fab72be4ad30d1d852fc5f1492aa6911a8aad(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cca6053ffe0f77fd07d26cceada81f3e3e9e5b832049344b1f7d88c006f06d45(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f526fb025093579ae7085ed34610b038bedad50bc4dda479dea96c217e4198e(
    *,
    policy: typing.Any,
    vector_bucket_arn: typing.Optional[builtins.str] = None,
    vector_bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__557f3461f0c9f94a1c325dd824a3303ad88eff46565842be7f5c9f62ac2ce7dc(
    *,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVectorBucket.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vector_bucket_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
