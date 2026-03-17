r'''
# AWS::MWAAServerless Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mwaaserverless as mwaaserverless
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MWAAServerless construct libraries](https://constructs.dev/search?q=mwaaserverless)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MWAAServerless resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MWAAServerless.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MWAAServerless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MWAAServerless.html).

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_mwaaserverless import (
    IWorkflowRef as _IWorkflowRef_a598eb41,
    WorkflowReference as _WorkflowReference_c262e190,
)


@jsii.implements(_IInspectable_c2943556, _IWorkflowRef_a598eb41, _ITaggableV2_4e6798f8)
class CfnWorkflow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mwaaserverless.CfnWorkflow",
):
    '''Resource Type definition for AWS::MWAAServerless::Workflow resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html
    :cloudformationResource: AWS::MWAAServerless::Workflow
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mwaaserverless as mwaaserverless
        
        cfn_workflow = mwaaserverless.CfnWorkflow(self, "MyCfnWorkflow",
            definition_s3_location=mwaaserverless.CfnWorkflow.S3LocationProperty(
                bucket="bucket",
                object_key="objectKey",
        
                # the properties below are optional
                version_id="versionId"
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            description="description",
            encryption_configuration=mwaaserverless.CfnWorkflow.EncryptionConfigurationProperty(
                type="type",
        
                # the properties below are optional
                kms_key_id="kmsKeyId"
            ),
            logging_configuration=mwaaserverless.CfnWorkflow.LoggingConfigurationProperty(
                log_group_name="logGroupName"
            ),
            name="name",
            network_configuration=mwaaserverless.CfnWorkflow.NetworkConfigurationProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            ),
            tags={
                "tags_key": "tags"
            },
            trigger_mode="triggerMode"
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        definition_s3_location: typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        logging_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        trigger_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``AWS::MWAAServerless::Workflow``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param definition_s3_location: 
        :param role_arn: 
        :param description: 
        :param encryption_configuration: 
        :param logging_configuration: 
        :param name: 
        :param network_configuration: 
        :param tags: A map of key-value pairs to be applied as tags.
        :param trigger_mode: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e2bce4e70d0388a15f4045d87762a0a9bbddefe5c4cc8c92886c1b7845258e0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkflowProps(
            definition_s3_location=definition_s3_location,
            role_arn=role_arn,
            description=description,
            encryption_configuration=encryption_configuration,
            logging_configuration=logging_configuration,
            name=name,
            network_configuration=network_configuration,
            tags=tags,
            trigger_mode=trigger_mode,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForWorkflow")
    @builtins.classmethod
    def arn_for_workflow(cls, resource: "_IWorkflowRef_a598eb41") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efc54da51356e725bfba680e59b62e7e55f48ab6956daffaa508b6cab05c5e86)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForWorkflow", [resource]))

    @jsii.member(jsii_name="isCfnWorkflow")
    @builtins.classmethod
    def is_cfn_workflow(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnWorkflow.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5697aec59969556cfbcaceefca05dbf4c705565c3ec1073054085e4a20769875)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnWorkflow", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f57466d2bdf054afc7e3d49308403099c41f9ad23a2a007aa91db68f1d828655)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8d08c346e322e0ff67f18f1d4fda12317dc15cef6543ce133d019da52b2c66aa)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrModifiedAt")
    def attr_modified_at(self) -> builtins.str:
        '''
        :cloudformationAttribute: ModifiedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModifiedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrScheduleConfiguration")
    def attr_schedule_configuration(self) -> "_IResolvable_da3f097b":
        '''
        :cloudformationAttribute: ScheduleConfiguration
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrScheduleConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkflowArn")
    def attr_workflow_arn(self) -> builtins.str:
        '''
        :cloudformationAttribute: WorkflowArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkflowArn"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkflowStatus")
    def attr_workflow_status(self) -> builtins.str:
        '''
        :cloudformationAttribute: WorkflowStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkflowStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkflowVersion")
    def attr_workflow_version(self) -> builtins.str:
        '''
        :cloudformationAttribute: WorkflowVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkflowVersion"))

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
    @jsii.member(jsii_name="workflowRef")
    def workflow_ref(self) -> "_WorkflowReference_c262e190":
        '''A reference to a Workflow resource.'''
        return typing.cast("_WorkflowReference_c262e190", jsii.get(self, "workflowRef"))

    @builtins.property
    @jsii.member(jsii_name="definitionS3Location")
    def definition_s3_location(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnWorkflow.S3LocationProperty"]:
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnWorkflow.S3LocationProperty"], jsii.get(self, "definitionS3Location"))

    @definition_s3_location.setter
    def definition_s3_location(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnWorkflow.S3LocationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9833b67c113a89f2316d0e981ed4884c44210bb5afe3d98b3f48c3dbd4c6636)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionS3Location", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f38d2888a3ed8ca88fab9cf362f64be8b28ae698d973d6eb717ffc7d26ea95d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c0e967a0d20001fac7826a1236cef88937fe92efa3aea43c4aee0668b77ace4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.EncryptionConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9714e5f8cd597317652144f2aeeb3923ed676c079ccbe101f8b1965d814594e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="loggingConfiguration")
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.LoggingConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.LoggingConfigurationProperty"]], jsii.get(self, "loggingConfiguration"))

    @logging_configuration.setter
    def logging_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.LoggingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c616011f97b5b305e924c2f2daf971e2cd5a3d599eaa2a5175e319dd0350d98e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31f3fefe9f76e831f4847bf707c5a491dada758aeb33ba982ee044c4ceb516af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.NetworkConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.NetworkConfigurationProperty"]], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.NetworkConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e84aedb46d5aeced351a3acc6109aa72f2931744f9ad449eb7c33a1f3e2a6537)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of key-value pairs to be applied as tags.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba570a00bba6210a762247c25ee50e6fe4f1c5b260184321978c4e85227da8ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="triggerMode")
    def trigger_mode(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "triggerMode"))

    @trigger_mode.setter
    def trigger_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__557aba21ad8506797a84212d0251edcf4b4a6f696028d7d683d648a27326f66c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerMode", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mwaaserverless.CfnWorkflow.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "kms_key_id": "kmsKeyId"},
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param type: 
            :param kms_key_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mwaaserverless as mwaaserverless
                
                encryption_configuration_property = mwaaserverless.CfnWorkflow.EncryptionConfigurationProperty(
                    type="type",
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__efe2f8cb733b4f3d7876c831146f412fca47453cee38a647e87fa75297eb0496)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-encryptionconfiguration.html#cfn-mwaaserverless-workflow-encryptionconfiguration-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-encryptionconfiguration.html#cfn-mwaaserverless-workflow-encryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
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
        jsii_type="aws-cdk-lib.aws_mwaaserverless.CfnWorkflow.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName"},
    )
    class LoggingConfigurationProperty:
        def __init__(self, *, log_group_name: builtins.str) -> None:
            '''
            :param log_group_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-loggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mwaaserverless as mwaaserverless
                
                logging_configuration_property = mwaaserverless.CfnWorkflow.LoggingConfigurationProperty(
                    log_group_name="logGroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8fd38e2fbacdb3636b041bc0c31da853f2a1440112ae620aee7dcbcb464ed0d2)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_name": log_group_name,
            }

        @builtins.property
        def log_group_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-loggingconfiguration.html#cfn-mwaaserverless-workflow-loggingconfiguration-loggroupname
            '''
            result = self._values.get("log_group_name")
            assert result is not None, "Required property 'log_group_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mwaaserverless.CfnWorkflow.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param security_group_ids: 
            :param subnet_ids: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mwaaserverless as mwaaserverless
                
                network_configuration_property = mwaaserverless.CfnWorkflow.NetworkConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc665a96ee907dadbb61655a0cb8e254c68ed2f7ce1a7cd2fb137b2a62b24b74)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-networkconfiguration.html#cfn-mwaaserverless-workflow-networkconfiguration-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-networkconfiguration.html#cfn-mwaaserverless-workflow-networkconfiguration-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mwaaserverless.CfnWorkflow.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "object_key": "objectKey",
            "version_id": "versionId",
        },
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            object_key: builtins.str,
            version_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param bucket: 
            :param object_key: 
            :param version_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mwaaserverless as mwaaserverless
                
                s3_location_property = mwaaserverless.CfnWorkflow.S3LocationProperty(
                    bucket="bucket",
                    object_key="objectKey",
                
                    # the properties below are optional
                    version_id="versionId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c0b299a68cbcd9cd5ffcaabf1024d30bf5364601588183689d527cf511904c20)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument object_key", value=object_key, expected_type=type_hints["object_key"])
                check_type(argname="argument version_id", value=version_id, expected_type=type_hints["version_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "object_key": object_key,
            }
            if version_id is not None:
                self._values["version_id"] = version_id

        @builtins.property
        def bucket(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-s3location.html#cfn-mwaaserverless-workflow-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-s3location.html#cfn-mwaaserverless-workflow-s3location-objectkey
            '''
            result = self._values.get("object_key")
            assert result is not None, "Required property 'object_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-s3location.html#cfn-mwaaserverless-workflow-s3location-versionid
            '''
            result = self._values.get("version_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mwaaserverless.CfnWorkflow.ScheduleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"cron_expression": "cronExpression"},
    )
    class ScheduleConfigurationProperty:
        def __init__(
            self,
            *,
            cron_expression: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param cron_expression: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-scheduleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mwaaserverless as mwaaserverless
                
                schedule_configuration_property = mwaaserverless.CfnWorkflow.ScheduleConfigurationProperty(
                    cron_expression="cronExpression"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d814c110ae85b71696876c2542c53feea69d634875096fa14e3d8603f231b37)
                check_type(argname="argument cron_expression", value=cron_expression, expected_type=type_hints["cron_expression"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cron_expression is not None:
                self._values["cron_expression"] = cron_expression

        @builtins.property
        def cron_expression(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaaserverless-workflow-scheduleconfiguration.html#cfn-mwaaserverless-workflow-scheduleconfiguration-cronexpression
            '''
            result = self._values.get("cron_expression")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mwaaserverless.CfnWorkflowProps",
    jsii_struct_bases=[],
    name_mapping={
        "definition_s3_location": "definitionS3Location",
        "role_arn": "roleArn",
        "description": "description",
        "encryption_configuration": "encryptionConfiguration",
        "logging_configuration": "loggingConfiguration",
        "name": "name",
        "network_configuration": "networkConfiguration",
        "tags": "tags",
        "trigger_mode": "triggerMode",
    },
)
class CfnWorkflowProps:
    def __init__(
        self,
        *,
        definition_s3_location: typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        logging_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        network_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnWorkflow.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        trigger_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkflow``.

        :param definition_s3_location: 
        :param role_arn: 
        :param description: 
        :param encryption_configuration: 
        :param logging_configuration: 
        :param name: 
        :param network_configuration: 
        :param tags: A map of key-value pairs to be applied as tags.
        :param trigger_mode: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mwaaserverless as mwaaserverless
            
            cfn_workflow_props = mwaaserverless.CfnWorkflowProps(
                definition_s3_location=mwaaserverless.CfnWorkflow.S3LocationProperty(
                    bucket="bucket",
                    object_key="objectKey",
            
                    # the properties below are optional
                    version_id="versionId"
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                description="description",
                encryption_configuration=mwaaserverless.CfnWorkflow.EncryptionConfigurationProperty(
                    type="type",
            
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                ),
                logging_configuration=mwaaserverless.CfnWorkflow.LoggingConfigurationProperty(
                    log_group_name="logGroupName"
                ),
                name="name",
                network_configuration=mwaaserverless.CfnWorkflow.NetworkConfigurationProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                ),
                tags={
                    "tags_key": "tags"
                },
                trigger_mode="triggerMode"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36755512823c440877f151e4568051c22a8df773ab4409c547b6f6b7d91f5cdb)
            check_type(argname="argument definition_s3_location", value=definition_s3_location, expected_type=type_hints["definition_s3_location"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument logging_configuration", value=logging_configuration, expected_type=type_hints["logging_configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trigger_mode", value=trigger_mode, expected_type=type_hints["trigger_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "definition_s3_location": definition_s3_location,
            "role_arn": role_arn,
        }
        if description is not None:
            self._values["description"] = description
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if logging_configuration is not None:
            self._values["logging_configuration"] = logging_configuration
        if name is not None:
            self._values["name"] = name
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if tags is not None:
            self._values["tags"] = tags
        if trigger_mode is not None:
            self._values["trigger_mode"] = trigger_mode

    @builtins.property
    def definition_s3_location(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnWorkflow.S3LocationProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html#cfn-mwaaserverless-workflow-definitions3location
        '''
        result = self._values.get("definition_s3_location")
        assert result is not None, "Required property 'definition_s3_location' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnWorkflow.S3LocationProperty"], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html#cfn-mwaaserverless-workflow-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html#cfn-mwaaserverless-workflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.EncryptionConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html#cfn-mwaaserverless-workflow-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.EncryptionConfigurationProperty"]], result)

    @builtins.property
    def logging_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.LoggingConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html#cfn-mwaaserverless-workflow-loggingconfiguration
        '''
        result = self._values.get("logging_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.LoggingConfigurationProperty"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html#cfn-mwaaserverless-workflow-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.NetworkConfigurationProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html#cfn-mwaaserverless-workflow-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnWorkflow.NetworkConfigurationProperty"]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of key-value pairs to be applied as tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html#cfn-mwaaserverless-workflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def trigger_mode(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mwaaserverless-workflow.html#cfn-mwaaserverless-workflow-triggermode
        '''
        result = self._values.get("trigger_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkflowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnWorkflow",
    "CfnWorkflowProps",
]

publication.publish()

def _typecheckingstub__7e2bce4e70d0388a15f4045d87762a0a9bbddefe5c4cc8c92886c1b7845258e0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    definition_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    trigger_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efc54da51356e725bfba680e59b62e7e55f48ab6956daffaa508b6cab05c5e86(
    resource: _IWorkflowRef_a598eb41,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5697aec59969556cfbcaceefca05dbf4c705565c3ec1073054085e4a20769875(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f57466d2bdf054afc7e3d49308403099c41f9ad23a2a007aa91db68f1d828655(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d08c346e322e0ff67f18f1d4fda12317dc15cef6543ce133d019da52b2c66aa(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9833b67c113a89f2316d0e981ed4884c44210bb5afe3d98b3f48c3dbd4c6636(
    value: typing.Union[_IResolvable_da3f097b, CfnWorkflow.S3LocationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f38d2888a3ed8ca88fab9cf362f64be8b28ae698d973d6eb717ffc7d26ea95d1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c0e967a0d20001fac7826a1236cef88937fe92efa3aea43c4aee0668b77ace4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9714e5f8cd597317652144f2aeeb3923ed676c079ccbe101f8b1965d814594e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkflow.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c616011f97b5b305e924c2f2daf971e2cd5a3d599eaa2a5175e319dd0350d98e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkflow.LoggingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31f3fefe9f76e831f4847bf707c5a491dada758aeb33ba982ee044c4ceb516af(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e84aedb46d5aeced351a3acc6109aa72f2931744f9ad449eb7c33a1f3e2a6537(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnWorkflow.NetworkConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba570a00bba6210a762247c25ee50e6fe4f1c5b260184321978c4e85227da8ab(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__557aba21ad8506797a84212d0251edcf4b4a6f696028d7d683d648a27326f66c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efe2f8cb733b4f3d7876c831146f412fca47453cee38a647e87fa75297eb0496(
    *,
    type: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd38e2fbacdb3636b041bc0c31da853f2a1440112ae620aee7dcbcb464ed0d2(
    *,
    log_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc665a96ee907dadbb61655a0cb8e254c68ed2f7ce1a7cd2fb137b2a62b24b74(
    *,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0b299a68cbcd9cd5ffcaabf1024d30bf5364601588183689d527cf511904c20(
    *,
    bucket: builtins.str,
    object_key: builtins.str,
    version_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d814c110ae85b71696876c2542c53feea69d634875096fa14e3d8603f231b37(
    *,
    cron_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36755512823c440877f151e4568051c22a8df773ab4409c547b6f6b7d91f5cdb(
    *,
    definition_s3_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    description: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    logging_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    trigger_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
