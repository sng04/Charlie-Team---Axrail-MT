r'''
# AWS::EMRContainers Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_emrcontainers as emrcontainers
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EMRContainers construct libraries](https://constructs.dev/search?q=emrcontainers)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EMRContainers resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRContainers.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EMRContainers](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EMRContainers.html).

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
    ITaggable as _ITaggable_36806126,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..interfaces.aws_emrcontainers import (
    EndpointReference as _EndpointReference_178108f2,
    IEndpointRef as _IEndpointRef_7ea728ed,
    ISecurityConfigurationRef as _ISecurityConfigurationRef_1a326316,
    IVirtualClusterRef as _IVirtualClusterRef_14fb6023,
    SecurityConfigurationReference as _SecurityConfigurationReference_bdef2ea6,
    VirtualClusterReference as _VirtualClusterReference_ded7b2ce,
)


@jsii.implements(_IInspectable_c2943556, _IEndpointRef_7ea728ed, _ITaggableV2_4e6798f8)
class CfnEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint",
):
    '''Resource Schema of AWS::EMRContainers::Endpoint Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html
    :cloudformationResource: AWS::EMRContainers::Endpoint
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emrcontainers as emrcontainers
        
        # e_mREKSConfiguration_property_: emrcontainers.CfnEndpoint.EMREKSConfigurationProperty
        
        cfn_endpoint = emrcontainers.CfnEndpoint(self, "MyCfnEndpoint",
            execution_role_arn="executionRoleArn",
            release_label="releaseLabel",
            type="type",
            virtual_cluster_id="virtualClusterId",
        
            # the properties below are optional
            configuration_overrides=emrcontainers.CfnEndpoint.ConfigurationOverridesProperty(
                application_configuration=[emrcontainers.CfnEndpoint.EMREKSConfigurationProperty(
                    classification="classification",
        
                    # the properties below are optional
                    configurations=[e_mREKSConfiguration_property_],
                    properties={
                        "properties_key": "properties"
                    }
                )],
                monitoring_configuration=emrcontainers.CfnEndpoint.MonitoringConfigurationProperty(
                    cloud_watch_monitoring_configuration=emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty(
                        log_group_name="logGroupName",
        
                        # the properties below are optional
                        log_stream_name_prefix="logStreamNamePrefix"
                    ),
                    container_log_rotation_configuration=emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty(
                        max_files_to_keep=123,
                        rotation_size="rotationSize"
                    ),
                    persistent_app_ui="persistentAppUi",
                    s3_monitoring_configuration=emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty(
                        log_uri="logUri"
                    )
                )
            ),
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        execution_role_arn: builtins.str,
        release_label: builtins.str,
        type: builtins.str,
        virtual_cluster_id: builtins.str,
        configuration_overrides: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEndpoint.ConfigurationOverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EMRContainers::Endpoint``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param execution_role_arn: The execution role ARN for the managed endpoint.
        :param release_label: The Amazon EMR release label.
        :param type: The type of the managed endpoint.
        :param virtual_cluster_id: The ID of the virtual cluster for which the managed endpoint is created.
        :param configuration_overrides: 
        :param name: The name of the managed endpoint.
        :param tags: An array of key-value pairs to apply to this managed endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23b89c74ef5fd6a5347927e915b67a755f92f55810673773d86745b94ec9ce0c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEndpointProps(
            execution_role_arn=execution_role_arn,
            release_label=release_label,
            type=type,
            virtual_cluster_id=virtual_cluster_id,
            configuration_overrides=configuration_overrides,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForEndpoint")
    @builtins.classmethod
    def arn_for_endpoint(cls, resource: "_IEndpointRef_7ea728ed") -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d0893eaff59c12b7e6dd4dfd799d44a31fa49362dec8ba203c7f8e79029bff9)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForEndpoint", [resource]))

    @jsii.member(jsii_name="isCfnEndpoint")
    @builtins.classmethod
    def is_cfn_endpoint(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnEndpoint.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__635096970c8f6988b319790d01d10b7af1624a2bd87a8fd19d2f526067565d38)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnEndpoint", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f81524f5f031b60202ef5750c9c53a9e8e5e0357685aef97a068e09c19a1d5d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__22395c6c2f1b0a694a9e0faf2c896173a496cbdf51ca26ecd7214a44487b981e)
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
        '''The ARN of the managed endpoint.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCertificateAuthority")
    def attr_certificate_authority(self) -> "_IResolvable_da3f097b":
        '''
        :cloudformationAttribute: CertificateAuthority
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrCertificateAuthority"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> builtins.str:
        '''The date and time when the managed endpoint was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrFailureReason")
    def attr_failure_reason(self) -> builtins.str:
        '''The reason for a failed managed endpoint.

        :cloudformationAttribute: FailureReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFailureReason"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the managed endpoint.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrSecurityGroup")
    def attr_security_group(self) -> builtins.str:
        '''The security group associated with the managed endpoint.

        :cloudformationAttribute: SecurityGroup
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSecurityGroup"))

    @builtins.property
    @jsii.member(jsii_name="attrServerUrl")
    def attr_server_url(self) -> builtins.str:
        '''The server URL of the managed endpoint.

        :cloudformationAttribute: ServerUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServerUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrState")
    def attr_state(self) -> builtins.str:
        '''The state of the managed endpoint.

        :cloudformationAttribute: State
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrState"))

    @builtins.property
    @jsii.member(jsii_name="attrStateDetails")
    def attr_state_details(self) -> builtins.str:
        '''Additional details about the state of the managed endpoint.

        :cloudformationAttribute: StateDetails
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStateDetails"))

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
    @jsii.member(jsii_name="endpointRef")
    def endpoint_ref(self) -> "_EndpointReference_178108f2":
        '''A reference to a Endpoint resource.'''
        return typing.cast("_EndpointReference_178108f2", jsii.get(self, "endpointRef"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        '''The execution role ARN for the managed endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82adad35327e5af1f867ea3ce6b09d9cf8bf066d4f3f0c3a297e3425583291ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="releaseLabel")
    def release_label(self) -> builtins.str:
        '''The Amazon EMR release label.'''
        return typing.cast(builtins.str, jsii.get(self, "releaseLabel"))

    @release_label.setter
    def release_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fdfe64e097ccd04046eb25d75f28e5f90eca1ce0eda856ca0f77cf38cdb414e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "releaseLabel", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of the managed endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e3365f1d0529739a9e96ac4af19a8abe17480deaa11498dbba4db6c1eb52a61)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="virtualClusterId")
    def virtual_cluster_id(self) -> builtins.str:
        '''The ID of the virtual cluster for which the managed endpoint is created.'''
        return typing.cast(builtins.str, jsii.get(self, "virtualClusterId"))

    @virtual_cluster_id.setter
    def virtual_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b0a84d01612790328a1ecc8558a579f74f52fa1a781ed7197676c50fce5a6e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "virtualClusterId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="configurationOverrides")
    def configuration_overrides(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.ConfigurationOverridesProperty"]]:
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.ConfigurationOverridesProperty"]], jsii.get(self, "configurationOverrides"))

    @configuration_overrides.setter
    def configuration_overrides(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.ConfigurationOverridesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e0c8197e58a0f1f00521e2589c5fe3688295bc923b51b75d41f29f6aec64d3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationOverrides", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the managed endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ff6a672ee7bf784cfbde2614d2f6cae307ce23728014e1a8bb6736b2020c7c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this managed endpoint.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea06eef637e8c0a25b829a6c624ac3e00fd1f47e5a0dc21e18b827b60481aa0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.CertificateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_arn": "certificateArn",
            "certificate_data": "certificateData",
        },
    )
    class CertificateProperty:
        def __init__(
            self,
            *,
            certificate_arn: typing.Optional[builtins.str] = None,
            certificate_data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param certificate_arn: 
            :param certificate_data: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-certificate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                certificate_property = emrcontainers.CfnEndpoint.CertificateProperty(
                    certificate_arn="certificateArn",
                    certificate_data="certificateData"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0753442657548325e3bd0a9ec7c567fdf41626466b3e89bfed14dee1c6cec778)
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument certificate_data", value=certificate_data, expected_type=type_hints["certificate_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_arn is not None:
                self._values["certificate_arn"] = certificate_arn
            if certificate_data is not None:
                self._values["certificate_data"] = certificate_data

        @builtins.property
        def certificate_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-certificate.html#cfn-emrcontainers-endpoint-certificate-certificatearn
            '''
            result = self._values.get("certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def certificate_data(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-certificate.html#cfn-emrcontainers-endpoint-certificate-certificatedata
            '''
            result = self._values.get("certificate_data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CertificateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_group_name": "logGroupName",
            "log_stream_name_prefix": "logStreamNamePrefix",
        },
    )
    class CloudWatchMonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            log_group_name: builtins.str,
            log_stream_name_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param log_group_name: 
            :param log_stream_name_prefix: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                cloud_watch_monitoring_configuration_property = emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty(
                    log_group_name="logGroupName",
                
                    # the properties below are optional
                    log_stream_name_prefix="logStreamNamePrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8ecb22ba4d8b0faedcb5f445667dd4c14b1bb238ebfc25811866bc27bb2f9f29)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
                check_type(argname="argument log_stream_name_prefix", value=log_stream_name_prefix, expected_type=type_hints["log_stream_name_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_name": log_group_name,
            }
            if log_stream_name_prefix is not None:
                self._values["log_stream_name_prefix"] = log_stream_name_prefix

        @builtins.property
        def log_group_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration.html#cfn-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-loggroupname
            '''
            result = self._values.get("log_group_name")
            assert result is not None, "Required property 'log_group_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_stream_name_prefix(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-cloudwatchmonitoringconfiguration.html#cfn-emrcontainers-endpoint-cloudwatchmonitoringconfiguration-logstreamnameprefix
            '''
            result = self._values.get("log_stream_name_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchMonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.ConfigurationOverridesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_configuration": "applicationConfiguration",
            "monitoring_configuration": "monitoringConfiguration",
        },
    )
    class ConfigurationOverridesProperty:
        def __init__(
            self,
            *,
            application_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEndpoint.EMREKSConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            monitoring_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEndpoint.MonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param application_configuration: 
            :param monitoring_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-configurationoverrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                # e_mREKSConfiguration_property_: emrcontainers.CfnEndpoint.EMREKSConfigurationProperty
                
                configuration_overrides_property = emrcontainers.CfnEndpoint.ConfigurationOverridesProperty(
                    application_configuration=[emrcontainers.CfnEndpoint.EMREKSConfigurationProperty(
                        classification="classification",
                
                        # the properties below are optional
                        configurations=[e_mREKSConfiguration_property_],
                        properties={
                            "properties_key": "properties"
                        }
                    )],
                    monitoring_configuration=emrcontainers.CfnEndpoint.MonitoringConfigurationProperty(
                        cloud_watch_monitoring_configuration=emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty(
                            log_group_name="logGroupName",
                
                            # the properties below are optional
                            log_stream_name_prefix="logStreamNamePrefix"
                        ),
                        container_log_rotation_configuration=emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty(
                            max_files_to_keep=123,
                            rotation_size="rotationSize"
                        ),
                        persistent_app_ui="persistentAppUi",
                        s3_monitoring_configuration=emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty(
                            log_uri="logUri"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46f984090360c20eea47211457bc59ba0064e851b8407461cf578437814aeb01)
                check_type(argname="argument application_configuration", value=application_configuration, expected_type=type_hints["application_configuration"])
                check_type(argname="argument monitoring_configuration", value=monitoring_configuration, expected_type=type_hints["monitoring_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_configuration is not None:
                self._values["application_configuration"] = application_configuration
            if monitoring_configuration is not None:
                self._values["monitoring_configuration"] = monitoring_configuration

        @builtins.property
        def application_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.EMREKSConfigurationProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-configurationoverrides.html#cfn-emrcontainers-endpoint-configurationoverrides-applicationconfiguration
            '''
            result = self._values.get("application_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.EMREKSConfigurationProperty"]]]], result)

        @builtins.property
        def monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.MonitoringConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-configurationoverrides.html#cfn-emrcontainers-endpoint-configurationoverrides-monitoringconfiguration
            '''
            result = self._values.get("monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.MonitoringConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationOverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_files_to_keep": "maxFilesToKeep",
            "rotation_size": "rotationSize",
        },
    )
    class ContainerLogRotationConfigurationProperty:
        def __init__(
            self,
            *,
            max_files_to_keep: jsii.Number,
            rotation_size: builtins.str,
        ) -> None:
            '''
            :param max_files_to_keep: 
            :param rotation_size: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-containerlogrotationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_log_rotation_configuration_property = emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty(
                    max_files_to_keep=123,
                    rotation_size="rotationSize"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__817b097d9818e8dbd56314bb022a526176ef9e0a159ab0fbb93fd2ba36f723a2)
                check_type(argname="argument max_files_to_keep", value=max_files_to_keep, expected_type=type_hints["max_files_to_keep"])
                check_type(argname="argument rotation_size", value=rotation_size, expected_type=type_hints["rotation_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_files_to_keep": max_files_to_keep,
                "rotation_size": rotation_size,
            }

        @builtins.property
        def max_files_to_keep(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-containerlogrotationconfiguration.html#cfn-emrcontainers-endpoint-containerlogrotationconfiguration-maxfilestokeep
            '''
            result = self._values.get("max_files_to_keep")
            assert result is not None, "Required property 'max_files_to_keep' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def rotation_size(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-containerlogrotationconfiguration.html#cfn-emrcontainers-endpoint-containerlogrotationconfiguration-rotationsize
            '''
            result = self._values.get("rotation_size")
            assert result is not None, "Required property 'rotation_size' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerLogRotationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.EMREKSConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "classification": "classification",
            "configurations": "configurations",
            "properties": "properties",
        },
    )
    class EMREKSConfigurationProperty:
        def __init__(
            self,
            *,
            classification: builtins.str,
            configurations: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEndpoint.EMREKSConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            properties: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]] = None,
        ) -> None:
            '''
            :param classification: 
            :param configurations: 
            :param properties: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-emreksconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                # e_mREKSConfiguration_property_: emrcontainers.CfnEndpoint.EMREKSConfigurationProperty
                
                e_mREKSConfiguration_property = emrcontainers.CfnEndpoint.EMREKSConfigurationProperty(
                    classification="classification",
                
                    # the properties below are optional
                    configurations=[e_mREKSConfiguration_property_],
                    properties={
                        "properties_key": "properties"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5e05064bc37ba71915107a21d96057346160606aa8cdc19d7293f9c9037b47a)
                check_type(argname="argument classification", value=classification, expected_type=type_hints["classification"])
                check_type(argname="argument configurations", value=configurations, expected_type=type_hints["configurations"])
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "classification": classification,
            }
            if configurations is not None:
                self._values["configurations"] = configurations
            if properties is not None:
                self._values["properties"] = properties

        @builtins.property
        def classification(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-emreksconfiguration.html#cfn-emrcontainers-endpoint-emreksconfiguration-classification
            '''
            result = self._values.get("classification")
            assert result is not None, "Required property 'classification' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def configurations(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.EMREKSConfigurationProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-emreksconfiguration.html#cfn-emrcontainers-endpoint-emreksconfiguration-configurations
            '''
            result = self._values.get("configurations")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.EMREKSConfigurationProperty"]]]], result)

        @builtins.property
        def properties(
            self,
        ) -> typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-emreksconfiguration.html#cfn-emrcontainers-endpoint-emreksconfiguration-properties
            '''
            result = self._values.get("properties")
            return typing.cast(typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], "_IResolvable_da3f097b"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EMREKSConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.MonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloud_watch_monitoring_configuration": "cloudWatchMonitoringConfiguration",
            "container_log_rotation_configuration": "containerLogRotationConfiguration",
            "persistent_app_ui": "persistentAppUi",
            "s3_monitoring_configuration": "s3MonitoringConfiguration",
        },
    )
    class MonitoringConfigurationProperty:
        def __init__(
            self,
            *,
            cloud_watch_monitoring_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEndpoint.CloudWatchMonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            container_log_rotation_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEndpoint.ContainerLogRotationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            persistent_app_ui: typing.Optional[builtins.str] = None,
            s3_monitoring_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEndpoint.S3MonitoringConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param cloud_watch_monitoring_configuration: 
            :param container_log_rotation_configuration: 
            :param persistent_app_ui: 
            :param s3_monitoring_configuration: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                monitoring_configuration_property = emrcontainers.CfnEndpoint.MonitoringConfigurationProperty(
                    cloud_watch_monitoring_configuration=emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty(
                        log_group_name="logGroupName",
                
                        # the properties below are optional
                        log_stream_name_prefix="logStreamNamePrefix"
                    ),
                    container_log_rotation_configuration=emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty(
                        max_files_to_keep=123,
                        rotation_size="rotationSize"
                    ),
                    persistent_app_ui="persistentAppUi",
                    s3_monitoring_configuration=emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty(
                        log_uri="logUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8a0503e26d3c8fcf0703183603081e1b7a18027a03a980ed33b0bb37c14dff86)
                check_type(argname="argument cloud_watch_monitoring_configuration", value=cloud_watch_monitoring_configuration, expected_type=type_hints["cloud_watch_monitoring_configuration"])
                check_type(argname="argument container_log_rotation_configuration", value=container_log_rotation_configuration, expected_type=type_hints["container_log_rotation_configuration"])
                check_type(argname="argument persistent_app_ui", value=persistent_app_ui, expected_type=type_hints["persistent_app_ui"])
                check_type(argname="argument s3_monitoring_configuration", value=s3_monitoring_configuration, expected_type=type_hints["s3_monitoring_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloud_watch_monitoring_configuration is not None:
                self._values["cloud_watch_monitoring_configuration"] = cloud_watch_monitoring_configuration
            if container_log_rotation_configuration is not None:
                self._values["container_log_rotation_configuration"] = container_log_rotation_configuration
            if persistent_app_ui is not None:
                self._values["persistent_app_ui"] = persistent_app_ui
            if s3_monitoring_configuration is not None:
                self._values["s3_monitoring_configuration"] = s3_monitoring_configuration

        @builtins.property
        def cloud_watch_monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.CloudWatchMonitoringConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html#cfn-emrcontainers-endpoint-monitoringconfiguration-cloudwatchmonitoringconfiguration
            '''
            result = self._values.get("cloud_watch_monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.CloudWatchMonitoringConfigurationProperty"]], result)

        @builtins.property
        def container_log_rotation_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.ContainerLogRotationConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html#cfn-emrcontainers-endpoint-monitoringconfiguration-containerlogrotationconfiguration
            '''
            result = self._values.get("container_log_rotation_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.ContainerLogRotationConfigurationProperty"]], result)

        @builtins.property
        def persistent_app_ui(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html#cfn-emrcontainers-endpoint-monitoringconfiguration-persistentappui
            '''
            result = self._values.get("persistent_app_ui")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_monitoring_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.S3MonitoringConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-monitoringconfiguration.html#cfn-emrcontainers-endpoint-monitoringconfiguration-s3monitoringconfiguration
            '''
            result = self._values.get("s3_monitoring_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.S3MonitoringConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_uri": "logUri"},
    )
    class S3MonitoringConfigurationProperty:
        def __init__(self, *, log_uri: builtins.str) -> None:
            '''
            :param log_uri: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-s3monitoringconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                s3_monitoring_configuration_property = emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty(
                    log_uri="logUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d2e089a4b5c6bf3faf983bfe03d5042364c4f68c554cd62834b53e7101c615e6)
                check_type(argname="argument log_uri", value=log_uri, expected_type=type_hints["log_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_uri": log_uri,
            }

        @builtins.property
        def log_uri(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-endpoint-s3monitoringconfiguration.html#cfn-emrcontainers-endpoint-s3monitoringconfiguration-loguri
            '''
            result = self._values.get("log_uri")
            assert result is not None, "Required property 'log_uri' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3MonitoringConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role_arn": "executionRoleArn",
        "release_label": "releaseLabel",
        "type": "type",
        "virtual_cluster_id": "virtualClusterId",
        "configuration_overrides": "configurationOverrides",
        "name": "name",
        "tags": "tags",
    },
)
class CfnEndpointProps:
    def __init__(
        self,
        *,
        execution_role_arn: builtins.str,
        release_label: builtins.str,
        type: builtins.str,
        virtual_cluster_id: builtins.str,
        configuration_overrides: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnEndpoint.ConfigurationOverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEndpoint``.

        :param execution_role_arn: The execution role ARN for the managed endpoint.
        :param release_label: The Amazon EMR release label.
        :param type: The type of the managed endpoint.
        :param virtual_cluster_id: The ID of the virtual cluster for which the managed endpoint is created.
        :param configuration_overrides: 
        :param name: The name of the managed endpoint.
        :param tags: An array of key-value pairs to apply to this managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emrcontainers as emrcontainers
            
            # e_mREKSConfiguration_property_: emrcontainers.CfnEndpoint.EMREKSConfigurationProperty
            
            cfn_endpoint_props = emrcontainers.CfnEndpointProps(
                execution_role_arn="executionRoleArn",
                release_label="releaseLabel",
                type="type",
                virtual_cluster_id="virtualClusterId",
            
                # the properties below are optional
                configuration_overrides=emrcontainers.CfnEndpoint.ConfigurationOverridesProperty(
                    application_configuration=[emrcontainers.CfnEndpoint.EMREKSConfigurationProperty(
                        classification="classification",
            
                        # the properties below are optional
                        configurations=[e_mREKSConfiguration_property_],
                        properties={
                            "properties_key": "properties"
                        }
                    )],
                    monitoring_configuration=emrcontainers.CfnEndpoint.MonitoringConfigurationProperty(
                        cloud_watch_monitoring_configuration=emrcontainers.CfnEndpoint.CloudWatchMonitoringConfigurationProperty(
                            log_group_name="logGroupName",
            
                            # the properties below are optional
                            log_stream_name_prefix="logStreamNamePrefix"
                        ),
                        container_log_rotation_configuration=emrcontainers.CfnEndpoint.ContainerLogRotationConfigurationProperty(
                            max_files_to_keep=123,
                            rotation_size="rotationSize"
                        ),
                        persistent_app_ui="persistentAppUi",
                        s3_monitoring_configuration=emrcontainers.CfnEndpoint.S3MonitoringConfigurationProperty(
                            log_uri="logUri"
                        )
                    )
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf3149ecf1698607ceb24e9bbca6c307d3e7ef064cb79d95651abb2c6d47065)
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument release_label", value=release_label, expected_type=type_hints["release_label"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument virtual_cluster_id", value=virtual_cluster_id, expected_type=type_hints["virtual_cluster_id"])
            check_type(argname="argument configuration_overrides", value=configuration_overrides, expected_type=type_hints["configuration_overrides"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "execution_role_arn": execution_role_arn,
            "release_label": release_label,
            "type": type,
            "virtual_cluster_id": virtual_cluster_id,
        }
        if configuration_overrides is not None:
            self._values["configuration_overrides"] = configuration_overrides
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''The execution role ARN for the managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def release_label(self) -> builtins.str:
        '''The Amazon EMR release label.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-releaselabel
        '''
        result = self._values.get("release_label")
        assert result is not None, "Required property 'release_label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def virtual_cluster_id(self) -> builtins.str:
        '''The ID of the virtual cluster for which the managed endpoint is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-virtualclusterid
        '''
        result = self._values.get("virtual_cluster_id")
        assert result is not None, "Required property 'virtual_cluster_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_overrides(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.ConfigurationOverridesProperty"]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-configurationoverrides
        '''
        result = self._values.get("configuration_overrides")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnEndpoint.ConfigurationOverridesProperty"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this managed endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-endpoint.html#cfn-emrcontainers-endpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ISecurityConfigurationRef_1a326316, _ITaggableV2_4e6798f8)
class CfnSecurityConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration",
):
    '''Resource Schema of AWS::EMRContainers::SecurityConfiguration Type.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html
    :cloudformationResource: AWS::EMRContainers::SecurityConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emrcontainers as emrcontainers
        
        cfn_security_configuration = emrcontainers.CfnSecurityConfiguration(self, "MyCfnSecurityConfiguration",
            security_configuration_data=emrcontainers.CfnSecurityConfiguration.SecurityConfigurationDataProperty(
                authentication_configuration=emrcontainers.CfnSecurityConfiguration.AuthenticationConfigurationProperty(
                    iam_configuration={
                        "system_role": "systemRole"
                    },
                    identity_center_configuration=emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty(
                        enable_identity_center=False,
                        identity_center_application_assignment_required=False,
                        identity_center_instance_arn="identityCenterInstanceArn"
                    )
                ),
                authorization_configuration=emrcontainers.CfnSecurityConfiguration.AuthorizationConfigurationProperty(
                    lake_formation_configuration=emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty(
                        authorized_session_tag_value="authorizedSessionTagValue",
                        query_access_control_enabled=False,
                        query_engine_role_arn="queryEngineRoleArn",
                        secure_namespace_info=emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                            cluster_id="clusterId",
                            namespace="namespace"
                        )
                    )
                ),
                encryption_configuration=emrcontainers.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                    at_rest_encryption_configuration=emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty(
                        local_disk_encryption_configuration=emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                            aws_kms_key_id="awsKmsKeyId",
                            encryption_key_provider_type="encryptionKeyProviderType"
                        ),
                        s3_encryption_configuration=emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                            encryption_option="encryptionOption",
                            kms_key_id="kmsKeyId"
                        )
                    ),
                    in_transit_encryption_configuration=emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty(
                        tls_certificate_configuration=emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                            certificate_provider_type="certificateProviderType",
                            private_key_secret_arn="privateKeySecretArn",
                            public_key_secret_arn="publicKeySecretArn"
                        )
                    )
                )
            ),
        
            # the properties below are optional
            container_provider=emrcontainers.CfnSecurityConfiguration.ContainerProviderProperty(
                id="id",
                type="type",
        
                # the properties below are optional
                info=emrcontainers.CfnSecurityConfiguration.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnSecurityConfiguration.EksInfoProperty(
                        namespace="namespace"
                    )
                )
            ),
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        security_configuration_data: typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.SecurityConfigurationDataProperty", typing.Dict[builtins.str, typing.Any]]],
        container_provider: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.ContainerProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EMRContainers::SecurityConfiguration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param security_configuration_data: Security configuration data containing encryption and authorization settings.
        :param container_provider: Container provider information.
        :param name: The name of the security configuration.
        :param tags: An array of key-value pairs to apply to this security configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6854e9fbbee664e2db7e06fdaa2e3ba6c9701b0e2bce486f38e57890c884e5af)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSecurityConfigurationProps(
            security_configuration_data=security_configuration_data,
            container_provider=container_provider,
            name=name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForSecurityConfiguration")
    @builtins.classmethod
    def arn_for_security_configuration(
        cls,
        resource: "_ISecurityConfigurationRef_1a326316",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd681409fc29491c4c7e38d95888109a4646290c7d21b905a648c8e49a16cc2f)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForSecurityConfiguration", [resource]))

    @jsii.member(jsii_name="isCfnSecurityConfiguration")
    @builtins.classmethod
    def is_cfn_security_configuration(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnSecurityConfiguration.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__660efc2daaa24d4382b34d964b39452ea882396bad4388acc85c9310c23989b7)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnSecurityConfiguration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adb0191ab4815b507e015b9e53d9a0db9a4b2cee4d58e694160b44a0afe9de56)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1af0cddd893391660a5e37e50121ea37e58f057538ee52904d314b61aa41e9f8)
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
        '''The ARN of the security configuration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the security configuration.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="securityConfigurationRef")
    def security_configuration_ref(self) -> "_SecurityConfigurationReference_bdef2ea6":
        '''A reference to a SecurityConfiguration resource.'''
        return typing.cast("_SecurityConfigurationReference_bdef2ea6", jsii.get(self, "securityConfigurationRef"))

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationData")
    def security_configuration_data(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.SecurityConfigurationDataProperty"]:
        '''Security configuration data containing encryption and authorization settings.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.SecurityConfigurationDataProperty"], jsii.get(self, "securityConfigurationData"))

    @security_configuration_data.setter
    def security_configuration_data(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.SecurityConfigurationDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f26dc902c9625031a3359860f64fc2c50df8f76bad05bb460ecddf60a8aef53f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfigurationData", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="containerProvider")
    def container_provider(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.ContainerProviderProperty"]]:
        '''Container provider information.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.ContainerProviderProperty"]], jsii.get(self, "containerProvider"))

    @container_provider.setter
    def container_provider(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.ContainerProviderProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e042738064d96ccff993bc56cc79c7f46ec050b950127cf902598481c68cc9ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerProvider", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the security configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53a52be55c2ce7be9e3a6ef926bc4d573b86d29f190210e5a9df93e655aaa102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this security configuration.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c1399f0742e46b06a814da734363ceffaf363d4e01a9b76b7506306a813a9c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "local_disk_encryption_configuration": "localDiskEncryptionConfiguration",
            "s3_encryption_configuration": "s3EncryptionConfiguration",
        },
    )
    class AtRestEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            local_disk_encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.S3EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''At-rest encryption configuration.

            :param local_disk_encryption_configuration: Local disk encryption configuration.
            :param s3_encryption_configuration: S3 encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                at_rest_encryption_configuration_property = emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty(
                    local_disk_encryption_configuration=emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                        aws_kms_key_id="awsKmsKeyId",
                        encryption_key_provider_type="encryptionKeyProviderType"
                    ),
                    s3_encryption_configuration=emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                        encryption_option="encryptionOption",
                        kms_key_id="kmsKeyId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d89332cbba1127be6b8fe5491bceeed96e052518779c07ad4e4adacc05f75a31)
                check_type(argname="argument local_disk_encryption_configuration", value=local_disk_encryption_configuration, expected_type=type_hints["local_disk_encryption_configuration"])
                check_type(argname="argument s3_encryption_configuration", value=s3_encryption_configuration, expected_type=type_hints["s3_encryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if local_disk_encryption_configuration is not None:
                self._values["local_disk_encryption_configuration"] = local_disk_encryption_configuration
            if s3_encryption_configuration is not None:
                self._values["s3_encryption_configuration"] = s3_encryption_configuration

        @builtins.property
        def local_disk_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty"]]:
            '''Local disk encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-atrestencryptionconfiguration-localdiskencryptionconfiguration
            '''
            result = self._values.get("local_disk_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty"]], result)

        @builtins.property
        def s3_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.S3EncryptionConfigurationProperty"]]:
            '''S3 encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-atrestencryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-atrestencryptionconfiguration-s3encryptionconfiguration
            '''
            result = self._values.get("s3_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.S3EncryptionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AtRestEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iam_configuration": "iamConfiguration",
            "identity_center_configuration": "identityCenterConfiguration",
        },
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            iam_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.IAMConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            identity_center_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.IdentityCenterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Authentication configuration for the security configuration.

            :param iam_configuration: IAM configuration.
            :param identity_center_configuration: Identity Center configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                authentication_configuration_property = emrcontainers.CfnSecurityConfiguration.AuthenticationConfigurationProperty(
                    iam_configuration={
                        "system_role": "systemRole"
                    },
                    identity_center_configuration=emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty(
                        enable_identity_center=False,
                        identity_center_application_assignment_required=False,
                        identity_center_instance_arn="identityCenterInstanceArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b3caee46c3c428a38039046963627b08574e1358dac5ece585461aababf8e4ef)
                check_type(argname="argument iam_configuration", value=iam_configuration, expected_type=type_hints["iam_configuration"])
                check_type(argname="argument identity_center_configuration", value=identity_center_configuration, expected_type=type_hints["identity_center_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam_configuration is not None:
                self._values["iam_configuration"] = iam_configuration
            if identity_center_configuration is not None:
                self._values["identity_center_configuration"] = identity_center_configuration

        @builtins.property
        def iam_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.IAMConfigurationProperty"]]:
            '''IAM configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration.html#cfn-emrcontainers-securityconfiguration-authenticationconfiguration-iamconfiguration
            '''
            result = self._values.get("iam_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.IAMConfigurationProperty"]], result)

        @builtins.property
        def identity_center_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.IdentityCenterConfigurationProperty"]]:
            '''Identity Center configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-authenticationconfiguration.html#cfn-emrcontainers-securityconfiguration-authenticationconfiguration-identitycenterconfiguration
            '''
            result = self._values.get("identity_center_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.IdentityCenterConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.AuthorizationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"lake_formation_configuration": "lakeFormationConfiguration"},
    )
    class AuthorizationConfigurationProperty:
        def __init__(
            self,
            *,
            lake_formation_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.LakeFormationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Authorization configuration for the security configuration.

            :param lake_formation_configuration: Lake Formation configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                authorization_configuration_property = emrcontainers.CfnSecurityConfiguration.AuthorizationConfigurationProperty(
                    lake_formation_configuration=emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty(
                        authorized_session_tag_value="authorizedSessionTagValue",
                        query_access_control_enabled=False,
                        query_engine_role_arn="queryEngineRoleArn",
                        secure_namespace_info=emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                            cluster_id="clusterId",
                            namespace="namespace"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76bfe5c6bd23193313bfe6dec8fbee6bf437673f2b46dac54b11ef0689913eab)
                check_type(argname="argument lake_formation_configuration", value=lake_formation_configuration, expected_type=type_hints["lake_formation_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lake_formation_configuration is not None:
                self._values["lake_formation_configuration"] = lake_formation_configuration

        @builtins.property
        def lake_formation_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.LakeFormationConfigurationProperty"]]:
            '''Lake Formation configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-authorizationconfiguration.html#cfn-emrcontainers-securityconfiguration-authorizationconfiguration-lakeformationconfiguration
            '''
            result = self._values.get("lake_formation_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.LakeFormationConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthorizationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.ContainerInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"eks_info": "eksInfo"},
    )
    class ContainerInfoProperty:
        def __init__(
            self,
            *,
            eks_info: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.EksInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Container information.

            :param eks_info: EKS information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_info_property = emrcontainers.CfnSecurityConfiguration.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnSecurityConfiguration.EksInfoProperty(
                        namespace="namespace"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e0c51a22b843b82d3a2f70b24e8095308dd8fdfb79690f5b0cd87fd63c28654d)
                check_type(argname="argument eks_info", value=eks_info, expected_type=type_hints["eks_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if eks_info is not None:
                self._values["eks_info"] = eks_info

        @builtins.property
        def eks_info(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.EksInfoProperty"]]:
            '''EKS information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerinfo.html#cfn-emrcontainers-securityconfiguration-containerinfo-eksinfo
            '''
            result = self._values.get("eks_info")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.EksInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.ContainerProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "type": "type", "info": "info"},
    )
    class ContainerProviderProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            type: builtins.str,
            info: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.ContainerInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Container provider information.

            :param id: The container provider ID.
            :param type: The container provider type.
            :param info: Container information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_provider_property = emrcontainers.CfnSecurityConfiguration.ContainerProviderProperty(
                    id="id",
                    type="type",
                
                    # the properties below are optional
                    info=emrcontainers.CfnSecurityConfiguration.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnSecurityConfiguration.EksInfoProperty(
                            namespace="namespace"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7defba1afab8843e36776150f6c12baad1d8fceaa1fd92112cabce82147e94e2)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument info", value=info, expected_type=type_hints["info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "type": type,
            }
            if info is not None:
                self._values["info"] = info

        @builtins.property
        def id(self) -> builtins.str:
            '''The container provider ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerprovider.html#cfn-emrcontainers-securityconfiguration-containerprovider-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The container provider type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerprovider.html#cfn-emrcontainers-securityconfiguration-containerprovider-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def info(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.ContainerInfoProperty"]]:
            '''Container information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-containerprovider.html#cfn-emrcontainers-securityconfiguration-containerprovider-info
            '''
            result = self._values.get("info")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.ContainerInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.EksInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"namespace": "namespace"},
    )
    class EksInfoProperty:
        def __init__(self, *, namespace: typing.Optional[builtins.str] = None) -> None:
            '''EKS information.

            :param namespace: The EKS namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-eksinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                eks_info_property = emrcontainers.CfnSecurityConfiguration.EksInfoProperty(
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5e7712fd7b4a2a053327b1eea8a52f21d3d1f1d9e7efa9b2397fcd486b8eaeb2)
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if namespace is not None:
                self._values["namespace"] = namespace

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The EKS namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-eksinfo.html#cfn-emrcontainers-securityconfiguration-eksinfo-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "at_rest_encryption_configuration": "atRestEncryptionConfiguration",
            "in_transit_encryption_configuration": "inTransitEncryptionConfiguration",
        },
    )
    class EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            at_rest_encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            in_transit_encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Encryption configuration for the security configuration.

            :param at_rest_encryption_configuration: At-rest encryption configuration.
            :param in_transit_encryption_configuration: In-transit encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                encryption_configuration_property = emrcontainers.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                    at_rest_encryption_configuration=emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty(
                        local_disk_encryption_configuration=emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                            aws_kms_key_id="awsKmsKeyId",
                            encryption_key_provider_type="encryptionKeyProviderType"
                        ),
                        s3_encryption_configuration=emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                            encryption_option="encryptionOption",
                            kms_key_id="kmsKeyId"
                        )
                    ),
                    in_transit_encryption_configuration=emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty(
                        tls_certificate_configuration=emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                            certificate_provider_type="certificateProviderType",
                            private_key_secret_arn="privateKeySecretArn",
                            public_key_secret_arn="publicKeySecretArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f41c637d9cbed4eeb23e20c4bd7928d0c1cf31163ac17153b7e304db762c1128)
                check_type(argname="argument at_rest_encryption_configuration", value=at_rest_encryption_configuration, expected_type=type_hints["at_rest_encryption_configuration"])
                check_type(argname="argument in_transit_encryption_configuration", value=in_transit_encryption_configuration, expected_type=type_hints["in_transit_encryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if at_rest_encryption_configuration is not None:
                self._values["at_rest_encryption_configuration"] = at_rest_encryption_configuration
            if in_transit_encryption_configuration is not None:
                self._values["in_transit_encryption_configuration"] = in_transit_encryption_configuration

        @builtins.property
        def at_rest_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty"]]:
            '''At-rest encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-encryptionconfiguration-atrestencryptionconfiguration
            '''
            result = self._values.get("at_rest_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty"]], result)

        @builtins.property
        def in_transit_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty"]]:
            '''In-transit encryption configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-encryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-encryptionconfiguration-intransitencryptionconfiguration
            '''
            result = self._values.get("in_transit_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.IAMConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"system_role": "systemRole"},
    )
    class IAMConfigurationProperty:
        def __init__(
            self,
            *,
            system_role: typing.Optional[builtins.str] = None,
        ) -> None:
            '''IAM configuration.

            :param system_role: The system role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-iamconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                i_aMConfiguration_property = {
                    "system_role": "systemRole"
                }
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__496b9118a2747d1a2075cedbe8d8eb5f5ac83784984ccc18bef308ce389d64e5)
                check_type(argname="argument system_role", value=system_role, expected_type=type_hints["system_role"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if system_role is not None:
                self._values["system_role"] = system_role

        @builtins.property
        def system_role(self) -> typing.Optional[builtins.str]:
            '''The system role ARN.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-iamconfiguration.html#cfn-emrcontainers-securityconfiguration-iamconfiguration-systemrole
            '''
            result = self._values.get("system_role")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IAMConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "enable_identity_center": "enableIdentityCenter",
            "identity_center_application_assignment_required": "identityCenterApplicationAssignmentRequired",
            "identity_center_instance_arn": "identityCenterInstanceArn",
        },
    )
    class IdentityCenterConfigurationProperty:
        def __init__(
            self,
            *,
            enable_identity_center: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
            identity_center_application_assignment_required: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
            identity_center_instance_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Identity Center configuration.

            :param enable_identity_center: Whether to enable Identity Center integration.
            :param identity_center_application_assignment_required: Whether Identity Center application assignment is required.
            :param identity_center_instance_arn: The ARN of the Identity Center instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                identity_center_configuration_property = emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty(
                    enable_identity_center=False,
                    identity_center_application_assignment_required=False,
                    identity_center_instance_arn="identityCenterInstanceArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f599ccca334d667e8c2151ff1efb55fe1a5722a9cef6e6b8e3ad7fc64f6fcb70)
                check_type(argname="argument enable_identity_center", value=enable_identity_center, expected_type=type_hints["enable_identity_center"])
                check_type(argname="argument identity_center_application_assignment_required", value=identity_center_application_assignment_required, expected_type=type_hints["identity_center_application_assignment_required"])
                check_type(argname="argument identity_center_instance_arn", value=identity_center_instance_arn, expected_type=type_hints["identity_center_instance_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enable_identity_center is not None:
                self._values["enable_identity_center"] = enable_identity_center
            if identity_center_application_assignment_required is not None:
                self._values["identity_center_application_assignment_required"] = identity_center_application_assignment_required
            if identity_center_instance_arn is not None:
                self._values["identity_center_instance_arn"] = identity_center_instance_arn

        @builtins.property
        def enable_identity_center(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''Whether to enable Identity Center integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.html#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-enableidentitycenter
            '''
            result = self._values.get("enable_identity_center")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        @builtins.property
        def identity_center_application_assignment_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''Whether Identity Center application assignment is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.html#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterapplicationassignmentrequired
            '''
            result = self._values.get("identity_center_application_assignment_required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        @builtins.property
        def identity_center_instance_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Identity Center instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-identitycenterconfiguration.html#cfn-emrcontainers-securityconfiguration-identitycenterconfiguration-identitycenterinstancearn
            '''
            result = self._values.get("identity_center_instance_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityCenterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"tls_certificate_configuration": "tlsCertificateConfiguration"},
    )
    class InTransitEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            tls_certificate_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.TLSCertificateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''In-transit encryption configuration.

            :param tls_certificate_configuration: TLS certificate configuration for in-transit encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                in_transit_encryption_configuration_property = emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty(
                    tls_certificate_configuration=emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                        certificate_provider_type="certificateProviderType",
                        private_key_secret_arn="privateKeySecretArn",
                        public_key_secret_arn="publicKeySecretArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8a9664211c1bd9e53f5b1ef1ea8cf192b0fc36da061879adc5e0f50d83df33bb)
                check_type(argname="argument tls_certificate_configuration", value=tls_certificate_configuration, expected_type=type_hints["tls_certificate_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if tls_certificate_configuration is not None:
                self._values["tls_certificate_configuration"] = tls_certificate_configuration

        @builtins.property
        def tls_certificate_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.TLSCertificateConfigurationProperty"]]:
            '''TLS certificate configuration for in-transit encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-intransitencryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-intransitencryptionconfiguration-tlscertificateconfiguration
            '''
            result = self._values.get("tls_certificate_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.TLSCertificateConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InTransitEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorized_session_tag_value": "authorizedSessionTagValue",
            "query_access_control_enabled": "queryAccessControlEnabled",
            "query_engine_role_arn": "queryEngineRoleArn",
            "secure_namespace_info": "secureNamespaceInfo",
        },
    )
    class LakeFormationConfigurationProperty:
        def __init__(
            self,
            *,
            authorized_session_tag_value: typing.Optional[builtins.str] = None,
            query_access_control_enabled: typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]] = None,
            query_engine_role_arn: typing.Optional[builtins.str] = None,
            secure_namespace_info: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.SecureNamespaceInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Lake Formation configuration.

            :param authorized_session_tag_value: The session tag to authorize Lake Formation access.
            :param query_access_control_enabled: Whether query access control is enabled.
            :param query_engine_role_arn: The ARN of the query engine role.
            :param secure_namespace_info: Secure namespace information for Lake Formation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                lake_formation_configuration_property = emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty(
                    authorized_session_tag_value="authorizedSessionTagValue",
                    query_access_control_enabled=False,
                    query_engine_role_arn="queryEngineRoleArn",
                    secure_namespace_info=emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                        cluster_id="clusterId",
                        namespace="namespace"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__28a87784f85f0e663cd90e1e0ab8f0457d68b1df23a29ec1815efffb1fd76efd)
                check_type(argname="argument authorized_session_tag_value", value=authorized_session_tag_value, expected_type=type_hints["authorized_session_tag_value"])
                check_type(argname="argument query_access_control_enabled", value=query_access_control_enabled, expected_type=type_hints["query_access_control_enabled"])
                check_type(argname="argument query_engine_role_arn", value=query_engine_role_arn, expected_type=type_hints["query_engine_role_arn"])
                check_type(argname="argument secure_namespace_info", value=secure_namespace_info, expected_type=type_hints["secure_namespace_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authorized_session_tag_value is not None:
                self._values["authorized_session_tag_value"] = authorized_session_tag_value
            if query_access_control_enabled is not None:
                self._values["query_access_control_enabled"] = query_access_control_enabled
            if query_engine_role_arn is not None:
                self._values["query_engine_role_arn"] = query_engine_role_arn
            if secure_namespace_info is not None:
                self._values["secure_namespace_info"] = secure_namespace_info

        @builtins.property
        def authorized_session_tag_value(self) -> typing.Optional[builtins.str]:
            '''The session tag to authorize Lake Formation access.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-authorizedsessiontagvalue
            '''
            result = self._values.get("authorized_session_tag_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_access_control_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]]:
            '''Whether query access control is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-queryaccesscontrolenabled
            '''
            result = self._values.get("query_access_control_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, "_IResolvable_da3f097b"]], result)

        @builtins.property
        def query_engine_role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the query engine role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-queryenginerolearn
            '''
            result = self._values.get("query_engine_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secure_namespace_info(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.SecureNamespaceInfoProperty"]]:
            '''Secure namespace information for Lake Formation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-lakeformationconfiguration.html#cfn-emrcontainers-securityconfiguration-lakeformationconfiguration-securenamespaceinfo
            '''
            result = self._values.get("secure_namespace_info")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.SecureNamespaceInfoProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LakeFormationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_kms_key_id": "awsKmsKeyId",
            "encryption_key_provider_type": "encryptionKeyProviderType",
        },
    )
    class LocalDiskEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            aws_kms_key_id: typing.Optional[builtins.str] = None,
            encryption_key_provider_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Local disk encryption configuration.

            :param aws_kms_key_id: The AWS KMS key ID.
            :param encryption_key_provider_type: The encryption key provider type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                local_disk_encryption_configuration_property = emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                    aws_kms_key_id="awsKmsKeyId",
                    encryption_key_provider_type="encryptionKeyProviderType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4511400021d1afa893531440e558c9b57d99a8e63fbbae50c1a5f5360e1eff2d)
                check_type(argname="argument aws_kms_key_id", value=aws_kms_key_id, expected_type=type_hints["aws_kms_key_id"])
                check_type(argname="argument encryption_key_provider_type", value=encryption_key_provider_type, expected_type=type_hints["encryption_key_provider_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_kms_key_id is not None:
                self._values["aws_kms_key_id"] = aws_kms_key_id
            if encryption_key_provider_type is not None:
                self._values["encryption_key_provider_type"] = encryption_key_provider_type

        @builtins.property
        def aws_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The AWS KMS key ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-awskmskeyid
            '''
            result = self._values.get("aws_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_key_provider_type(self) -> typing.Optional[builtins.str]:
            '''The encryption key provider type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-localdiskencryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-localdiskencryptionconfiguration-encryptionkeyprovidertype
            '''
            result = self._values.get("encryption_key_provider_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocalDiskEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_option": "encryptionOption",
            "kms_key_id": "kmsKeyId",
        },
    )
    class S3EncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_option: typing.Optional[builtins.str] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''S3 encryption configuration.

            :param encryption_option: The S3 encryption option.
            :param kms_key_id: The KMS key ID for encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                s3_encryption_configuration_property = emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                    encryption_option="encryptionOption",
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd8412be690034fa6d1270d9b5c028c8a5a0b2b83defe7f3c1a7d21b32790a48)
                check_type(argname="argument encryption_option", value=encryption_option, expected_type=type_hints["encryption_option"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encryption_option is not None:
                self._values["encryption_option"] = encryption_option
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def encryption_option(self) -> typing.Optional[builtins.str]:
            '''The S3 encryption option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-s3encryptionconfiguration-encryptionoption
            '''
            result = self._values.get("encryption_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The KMS key ID for encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-s3encryptionconfiguration.html#cfn-emrcontainers-securityconfiguration-s3encryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_id": "clusterId", "namespace": "namespace"},
    )
    class SecureNamespaceInfoProperty:
        def __init__(
            self,
            *,
            cluster_id: typing.Optional[builtins.str] = None,
            namespace: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Secure namespace information for Lake Formation.

            :param cluster_id: The ID of the cluster.
            :param namespace: The namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                secure_namespace_info_property = emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                    cluster_id="clusterId",
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3759e01f350e1d397915bd4d597987fa0422a4123e65b626ce60a9961e8df11c)
                check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cluster_id is not None:
                self._values["cluster_id"] = cluster_id
            if namespace is not None:
                self._values["namespace"] = namespace

        @builtins.property
        def cluster_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo.html#cfn-emrcontainers-securityconfiguration-securenamespaceinfo-clusterid
            '''
            result = self._values.get("cluster_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def namespace(self) -> typing.Optional[builtins.str]:
            '''The namespace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securenamespaceinfo.html#cfn-emrcontainers-securityconfiguration-securenamespaceinfo-namespace
            '''
            result = self._values.get("namespace")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecureNamespaceInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.SecurityConfigurationDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_configuration": "authenticationConfiguration",
            "authorization_configuration": "authorizationConfiguration",
            "encryption_configuration": "encryptionConfiguration",
        },
    )
    class SecurityConfigurationDataProperty:
        def __init__(
            self,
            *,
            authentication_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.AuthenticationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            authorization_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.AuthorizationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Security configuration data containing encryption and authorization settings.

            :param authentication_configuration: Authentication configuration for the security configuration.
            :param authorization_configuration: Authorization configuration for the security configuration.
            :param encryption_configuration: Encryption configuration for the security configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                security_configuration_data_property = emrcontainers.CfnSecurityConfiguration.SecurityConfigurationDataProperty(
                    authentication_configuration=emrcontainers.CfnSecurityConfiguration.AuthenticationConfigurationProperty(
                        iam_configuration={
                            "system_role": "systemRole"
                        },
                        identity_center_configuration=emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty(
                            enable_identity_center=False,
                            identity_center_application_assignment_required=False,
                            identity_center_instance_arn="identityCenterInstanceArn"
                        )
                    ),
                    authorization_configuration=emrcontainers.CfnSecurityConfiguration.AuthorizationConfigurationProperty(
                        lake_formation_configuration=emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty(
                            authorized_session_tag_value="authorizedSessionTagValue",
                            query_access_control_enabled=False,
                            query_engine_role_arn="queryEngineRoleArn",
                            secure_namespace_info=emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                                cluster_id="clusterId",
                                namespace="namespace"
                            )
                        )
                    ),
                    encryption_configuration=emrcontainers.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                        at_rest_encryption_configuration=emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty(
                            local_disk_encryption_configuration=emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                                aws_kms_key_id="awsKmsKeyId",
                                encryption_key_provider_type="encryptionKeyProviderType"
                            ),
                            s3_encryption_configuration=emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                                encryption_option="encryptionOption",
                                kms_key_id="kmsKeyId"
                            )
                        ),
                        in_transit_encryption_configuration=emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty(
                            tls_certificate_configuration=emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                                certificate_provider_type="certificateProviderType",
                                private_key_secret_arn="privateKeySecretArn",
                                public_key_secret_arn="publicKeySecretArn"
                            )
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f493d86970b0aa105efd09d9ecac31f88dcd70be4b4008d89647b65c9b717653)
                check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
                check_type(argname="argument authorization_configuration", value=authorization_configuration, expected_type=type_hints["authorization_configuration"])
                check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authentication_configuration is not None:
                self._values["authentication_configuration"] = authentication_configuration
            if authorization_configuration is not None:
                self._values["authorization_configuration"] = authorization_configuration
            if encryption_configuration is not None:
                self._values["encryption_configuration"] = encryption_configuration

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.AuthenticationConfigurationProperty"]]:
            '''Authentication configuration for the security configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata.html#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.AuthenticationConfigurationProperty"]], result)

        @builtins.property
        def authorization_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.AuthorizationConfigurationProperty"]]:
            '''Authorization configuration for the security configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata.html#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-authorizationconfiguration
            '''
            result = self._values.get("authorization_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.AuthorizationConfigurationProperty"]], result)

        @builtins.property
        def encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.EncryptionConfigurationProperty"]]:
            '''Encryption configuration for the security configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-securityconfigurationdata.html#cfn-emrcontainers-securityconfiguration-securityconfigurationdata-encryptionconfiguration
            '''
            result = self._values.get("encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.EncryptionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecurityConfigurationDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_provider_type": "certificateProviderType",
            "private_key_secret_arn": "privateKeySecretArn",
            "public_key_secret_arn": "publicKeySecretArn",
        },
    )
    class TLSCertificateConfigurationProperty:
        def __init__(
            self,
            *,
            certificate_provider_type: typing.Optional[builtins.str] = None,
            private_key_secret_arn: typing.Optional[builtins.str] = None,
            public_key_secret_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''TLS certificate configuration for in-transit encryption.

            :param certificate_provider_type: The certificate provider type.
            :param private_key_secret_arn: The ARN of the secret containing the private key.
            :param public_key_secret_arn: The ARN of the secret containing the public key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                t_lSCertificate_configuration_property = emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                    certificate_provider_type="certificateProviderType",
                    private_key_secret_arn="privateKeySecretArn",
                    public_key_secret_arn="publicKeySecretArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f48594c857b1e3ec68169c0a14e6791998c57deb66a4337a04f55c5cd650e7e)
                check_type(argname="argument certificate_provider_type", value=certificate_provider_type, expected_type=type_hints["certificate_provider_type"])
                check_type(argname="argument private_key_secret_arn", value=private_key_secret_arn, expected_type=type_hints["private_key_secret_arn"])
                check_type(argname="argument public_key_secret_arn", value=public_key_secret_arn, expected_type=type_hints["public_key_secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_provider_type is not None:
                self._values["certificate_provider_type"] = certificate_provider_type
            if private_key_secret_arn is not None:
                self._values["private_key_secret_arn"] = private_key_secret_arn
            if public_key_secret_arn is not None:
                self._values["public_key_secret_arn"] = public_key_secret_arn

        @builtins.property
        def certificate_provider_type(self) -> typing.Optional[builtins.str]:
            '''The certificate provider type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration.html#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-certificateprovidertype
            '''
            result = self._values.get("certificate_provider_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def private_key_secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret containing the private key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration.html#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-privatekeysecretarn
            '''
            result = self._values.get("private_key_secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def public_key_secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret containing the public key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-securityconfiguration-tlscertificateconfiguration.html#cfn-emrcontainers-securityconfiguration-tlscertificateconfiguration-publickeysecretarn
            '''
            result = self._values.get("public_key_secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TLSCertificateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnSecurityConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "security_configuration_data": "securityConfigurationData",
        "container_provider": "containerProvider",
        "name": "name",
        "tags": "tags",
    },
)
class CfnSecurityConfigurationProps:
    def __init__(
        self,
        *,
        security_configuration_data: typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.SecurityConfigurationDataProperty", typing.Dict[builtins.str, typing.Any]]],
        container_provider: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnSecurityConfiguration.ContainerProviderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSecurityConfiguration``.

        :param security_configuration_data: Security configuration data containing encryption and authorization settings.
        :param container_provider: Container provider information.
        :param name: The name of the security configuration.
        :param tags: An array of key-value pairs to apply to this security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emrcontainers as emrcontainers
            
            cfn_security_configuration_props = emrcontainers.CfnSecurityConfigurationProps(
                security_configuration_data=emrcontainers.CfnSecurityConfiguration.SecurityConfigurationDataProperty(
                    authentication_configuration=emrcontainers.CfnSecurityConfiguration.AuthenticationConfigurationProperty(
                        iam_configuration={
                            "system_role": "systemRole"
                        },
                        identity_center_configuration=emrcontainers.CfnSecurityConfiguration.IdentityCenterConfigurationProperty(
                            enable_identity_center=False,
                            identity_center_application_assignment_required=False,
                            identity_center_instance_arn="identityCenterInstanceArn"
                        )
                    ),
                    authorization_configuration=emrcontainers.CfnSecurityConfiguration.AuthorizationConfigurationProperty(
                        lake_formation_configuration=emrcontainers.CfnSecurityConfiguration.LakeFormationConfigurationProperty(
                            authorized_session_tag_value="authorizedSessionTagValue",
                            query_access_control_enabled=False,
                            query_engine_role_arn="queryEngineRoleArn",
                            secure_namespace_info=emrcontainers.CfnSecurityConfiguration.SecureNamespaceInfoProperty(
                                cluster_id="clusterId",
                                namespace="namespace"
                            )
                        )
                    ),
                    encryption_configuration=emrcontainers.CfnSecurityConfiguration.EncryptionConfigurationProperty(
                        at_rest_encryption_configuration=emrcontainers.CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty(
                            local_disk_encryption_configuration=emrcontainers.CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty(
                                aws_kms_key_id="awsKmsKeyId",
                                encryption_key_provider_type="encryptionKeyProviderType"
                            ),
                            s3_encryption_configuration=emrcontainers.CfnSecurityConfiguration.S3EncryptionConfigurationProperty(
                                encryption_option="encryptionOption",
                                kms_key_id="kmsKeyId"
                            )
                        ),
                        in_transit_encryption_configuration=emrcontainers.CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty(
                            tls_certificate_configuration=emrcontainers.CfnSecurityConfiguration.TLSCertificateConfigurationProperty(
                                certificate_provider_type="certificateProviderType",
                                private_key_secret_arn="privateKeySecretArn",
                                public_key_secret_arn="publicKeySecretArn"
                            )
                        )
                    )
                ),
            
                # the properties below are optional
                container_provider=emrcontainers.CfnSecurityConfiguration.ContainerProviderProperty(
                    id="id",
                    type="type",
            
                    # the properties below are optional
                    info=emrcontainers.CfnSecurityConfiguration.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnSecurityConfiguration.EksInfoProperty(
                            namespace="namespace"
                        )
                    )
                ),
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aac200d052b6d8b5d83eb4ae9a2c63aeb84f4e4ce7bc48d47327fc9874cfba98)
            check_type(argname="argument security_configuration_data", value=security_configuration_data, expected_type=type_hints["security_configuration_data"])
            check_type(argname="argument container_provider", value=container_provider, expected_type=type_hints["container_provider"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_configuration_data": security_configuration_data,
        }
        if container_provider is not None:
            self._values["container_provider"] = container_provider
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def security_configuration_data(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.SecurityConfigurationDataProperty"]:
        '''Security configuration data containing encryption and authorization settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html#cfn-emrcontainers-securityconfiguration-securityconfigurationdata
        '''
        result = self._values.get("security_configuration_data")
        assert result is not None, "Required property 'security_configuration_data' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.SecurityConfigurationDataProperty"], result)

    @builtins.property
    def container_provider(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.ContainerProviderProperty"]]:
        '''Container provider information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html#cfn-emrcontainers-securityconfiguration-containerprovider
        '''
        result = self._values.get("container_provider")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnSecurityConfiguration.ContainerProviderProperty"]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html#cfn-emrcontainers-securityconfiguration-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-securityconfiguration.html#cfn-emrcontainers-securityconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSecurityConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IVirtualClusterRef_14fb6023, _ITaggable_36806126)
class CfnVirtualCluster(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster",
):
    '''The ``AWS::EMRContainers::VirtualCluster`` resource specifies a virtual cluster.

    A virtual cluster is a managed entity on Amazon EMR on EKS. You can create, describe, list, and delete virtual clusters. They do not consume any additional resources in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html
    :cloudformationResource: AWS::EMRContainers::VirtualCluster
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_emrcontainers as emrcontainers
        
        cfn_virtual_cluster = emrcontainers.CfnVirtualCluster(self, "MyCfnVirtualCluster",
            container_provider=emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                id="id",
                info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                        namespace="namespace"
                    )
                ),
                type="type"
            ),
            name="name",
        
            # the properties below are optional
            security_configuration_id="securityConfigurationId",
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        *,
        container_provider: typing.Union["_IResolvable_da3f097b", typing.Union["CfnVirtualCluster.ContainerProviderProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        security_configuration_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::EMRContainers::VirtualCluster``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param container_provider: The container provider of the virtual cluster.
        :param name: The name of the virtual cluster.
        :param security_configuration_id: The ID of the security configuration.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a06dc2760ceb0de7a449a23941f15987094157d1a540c30fa67c9e49a3e06101)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVirtualClusterProps(
            container_provider=container_provider,
            name=name,
            security_configuration_id=security_configuration_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForVirtualCluster")
    @builtins.classmethod
    def arn_for_virtual_cluster(
        cls,
        resource: "_IVirtualClusterRef_14fb6023",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__516f2f16964e7ef220cab41225b3b7c3e3c0a9ee6b852252c3f1a1871264629c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForVirtualCluster", [resource]))

    @jsii.member(jsii_name="fromVirtualClusterArn")
    @builtins.classmethod
    def from_virtual_cluster_arn(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        arn: builtins.str,
    ) -> "_IVirtualClusterRef_14fb6023":
        '''Creates a new IVirtualClusterRef from an ARN.

        :param scope: -
        :param id: -
        :param arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d7111433bac0bf3eef5f3ffc73c4e649ef41bf63a44cfbc891a7f06a1b9be4b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
        return typing.cast("_IVirtualClusterRef_14fb6023", jsii.sinvoke(cls, "fromVirtualClusterArn", [scope, id, arn]))

    @jsii.member(jsii_name="fromVirtualClusterId")
    @builtins.classmethod
    def from_virtual_cluster_id(
        cls,
        scope: "_constructs_77d1e7e8.Construct",
        id: builtins.str,
        virtual_cluster_id: builtins.str,
    ) -> "_IVirtualClusterRef_14fb6023":
        '''Creates a new IVirtualClusterRef from a virtualClusterId.

        :param scope: -
        :param id: -
        :param virtual_cluster_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcaea2c30abe44238307f21b3c8a59222637a0fd52fab165c6272df6fa333e6a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument virtual_cluster_id", value=virtual_cluster_id, expected_type=type_hints["virtual_cluster_id"])
        return typing.cast("_IVirtualClusterRef_14fb6023", jsii.sinvoke(cls, "fromVirtualClusterId", [scope, id, virtual_cluster_id]))

    @jsii.member(jsii_name="isCfnVirtualCluster")
    @builtins.classmethod
    def is_cfn_virtual_cluster(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnVirtualCluster.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c9228b7a5165151302a3840836f9259f95d9a03c7684570914df3c5f40c23a7)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnVirtualCluster", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__802f118bbdec329d651201f6f69836e8e9523c47d32a262a55c4813747ccf78c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3035614e8641a59d4a7600ad906f142054401a42e6c1ca14df8b5d57d08f0823)
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
        '''The Amazon Resource Name (ARN) of the project, such as ``arn:aws:emr-containers:us-east-1:123456789012:/virtualclusters/ab4rp1abcs8xz47n3x0example`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The ID of the virtual cluster, such as ``ab4rp1abcs8xz47n3x0example`` .

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="virtualClusterRef")
    def virtual_cluster_ref(self) -> "_VirtualClusterReference_ded7b2ce":
        '''A reference to a VirtualCluster resource.'''
        return typing.cast("_VirtualClusterReference_ded7b2ce", jsii.get(self, "virtualClusterRef"))

    @builtins.property
    @jsii.member(jsii_name="containerProvider")
    def container_provider(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnVirtualCluster.ContainerProviderProperty"]:
        '''The container provider of the virtual cluster.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnVirtualCluster.ContainerProviderProperty"], jsii.get(self, "containerProvider"))

    @container_provider.setter
    def container_provider(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnVirtualCluster.ContainerProviderProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__617f2c6bc289034f068a4b514139fc0bee8f6455f589c3e2de7ee7fb7a3a92e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerProvider", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the virtual cluster.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aea4d0052a5a6cb82d57b5655349988466e02d75bbcc22aec370e6810b4c382d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityConfigurationId")
    def security_configuration_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the security configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityConfigurationId"))

    @security_configuration_id.setter
    def security_configuration_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d05d102efa2c9eb1d454519ceade8e11615a54a4a6a9f26f4883e2051aa27414)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityConfigurationId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3436f23ae2ca4313aacb96519980906e71e5bc37e7a466a53353480f948e674)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster.ContainerInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"eks_info": "eksInfo"},
    )
    class ContainerInfoProperty:
        def __init__(
            self,
            *,
            eks_info: typing.Union["_IResolvable_da3f097b", typing.Union["CfnVirtualCluster.EksInfoProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The information about the container used for a job run or a managed endpoint.

            :param eks_info: The information about the Amazon EKS cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_info_property = emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                    eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                        namespace="namespace"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e5baf7a38335e2eb8733f2aa2d96a9593d774d095fb8a05dcf1d8bd22323050)
                check_type(argname="argument eks_info", value=eks_info, expected_type=type_hints["eks_info"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "eks_info": eks_info,
            }

        @builtins.property
        def eks_info(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnVirtualCluster.EksInfoProperty"]:
            '''The information about the Amazon EKS cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerinfo.html#cfn-emrcontainers-virtualcluster-containerinfo-eksinfo
            '''
            result = self._values.get("eks_info")
            assert result is not None, "Required property 'eks_info' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnVirtualCluster.EksInfoProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster.ContainerProviderProperty",
        jsii_struct_bases=[],
        name_mapping={"id": "id", "info": "info", "type": "type"},
    )
    class ContainerProviderProperty:
        def __init__(
            self,
            *,
            id: builtins.str,
            info: typing.Union["_IResolvable_da3f097b", typing.Union["CfnVirtualCluster.ContainerInfoProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''The information about the container provider.

            :param id: The ID of the container cluster. *Minimum* : 1 *Maximum* : 100 *Pattern* : ``^[0-9A-Za-z][A-Za-z0-9\\-_]*``
            :param info: The information about the container cluster.
            :param type: The type of the container provider. Amazon EKS is the only supported type as of now.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                container_provider_property = emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                    id="id",
                    info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                            namespace="namespace"
                        )
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__19801d68aea5b7c69bfd60c7d9c690e62c4643fe80fcda956e884f367b8b1dcf)
                check_type(argname="argument id", value=id, expected_type=type_hints["id"])
                check_type(argname="argument info", value=info, expected_type=type_hints["info"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "id": id,
                "info": info,
                "type": type,
            }

        @builtins.property
        def id(self) -> builtins.str:
            '''The ID of the container cluster.

            *Minimum* : 1

            *Maximum* : 100

            *Pattern* : ``^[0-9A-Za-z][A-Za-z0-9\\-_]*``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-id
            '''
            result = self._values.get("id")
            assert result is not None, "Required property 'id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def info(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnVirtualCluster.ContainerInfoProperty"]:
            '''The information about the container cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-info
            '''
            result = self._values.get("info")
            assert result is not None, "Required property 'info' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnVirtualCluster.ContainerInfoProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the container provider.

            Amazon EKS is the only supported type as of now.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-containerprovider.html#cfn-emrcontainers-virtualcluster-containerprovider-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerProviderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualCluster.EksInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"namespace": "namespace"},
    )
    class EksInfoProperty:
        def __init__(self, *, namespace: builtins.str) -> None:
            '''The information about the Amazon EKS cluster.

            :param namespace: The namespaces of the EKS cluster. *Minimum* : 1 *Maximum* : 63 *Pattern* : ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_emrcontainers as emrcontainers
                
                eks_info_property = emrcontainers.CfnVirtualCluster.EksInfoProperty(
                    namespace="namespace"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__26be72236c14a8878e3d92d7b17397aa49c8a844f85e9e98c958600dd7a08c8f)
                check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "namespace": namespace,
            }

        @builtins.property
        def namespace(self) -> builtins.str:
            '''The namespaces of the EKS cluster.

            *Minimum* : 1

            *Maximum* : 63

            *Pattern* : ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-emrcontainers-virtualcluster-eksinfo.html#cfn-emrcontainers-virtualcluster-eksinfo-namespace
            '''
            result = self._values.get("namespace")
            assert result is not None, "Required property 'namespace' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EksInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_emrcontainers.CfnVirtualClusterProps",
    jsii_struct_bases=[],
    name_mapping={
        "container_provider": "containerProvider",
        "name": "name",
        "security_configuration_id": "securityConfigurationId",
        "tags": "tags",
    },
)
class CfnVirtualClusterProps:
    def __init__(
        self,
        *,
        container_provider: typing.Union["_IResolvable_da3f097b", typing.Union["CfnVirtualCluster.ContainerProviderProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        security_configuration_id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVirtualCluster``.

        :param container_provider: The container provider of the virtual cluster.
        :param name: The name of the virtual cluster.
        :param security_configuration_id: The ID of the security configuration.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_emrcontainers as emrcontainers
            
            cfn_virtual_cluster_props = emrcontainers.CfnVirtualClusterProps(
                container_provider=emrcontainers.CfnVirtualCluster.ContainerProviderProperty(
                    id="id",
                    info=emrcontainers.CfnVirtualCluster.ContainerInfoProperty(
                        eks_info=emrcontainers.CfnVirtualCluster.EksInfoProperty(
                            namespace="namespace"
                        )
                    ),
                    type="type"
                ),
                name="name",
            
                # the properties below are optional
                security_configuration_id="securityConfigurationId",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79f93ead2a436b8c5a2fc364fff5d9da849a851543aa1433cd7ab649d79d55f9)
            check_type(argname="argument container_provider", value=container_provider, expected_type=type_hints["container_provider"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument security_configuration_id", value=security_configuration_id, expected_type=type_hints["security_configuration_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_provider": container_provider,
            "name": name,
        }
        if security_configuration_id is not None:
            self._values["security_configuration_id"] = security_configuration_id
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def container_provider(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnVirtualCluster.ContainerProviderProperty"]:
        '''The container provider of the virtual cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-containerprovider
        '''
        result = self._values.get("container_provider")
        assert result is not None, "Required property 'container_provider' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnVirtualCluster.ContainerProviderProperty"], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the virtual cluster.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_configuration_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the security configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-securityconfigurationid
        '''
        result = self._values.get("security_configuration_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-emrcontainers-virtualcluster.html#cfn-emrcontainers-virtualcluster-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVirtualClusterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEndpoint",
    "CfnEndpointProps",
    "CfnSecurityConfiguration",
    "CfnSecurityConfigurationProps",
    "CfnVirtualCluster",
    "CfnVirtualClusterProps",
]

publication.publish()

def _typecheckingstub__23b89c74ef5fd6a5347927e915b67a755f92f55810673773d86745b94ec9ce0c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    execution_role_arn: builtins.str,
    release_label: builtins.str,
    type: builtins.str,
    virtual_cluster_id: builtins.str,
    configuration_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.ConfigurationOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d0893eaff59c12b7e6dd4dfd799d44a31fa49362dec8ba203c7f8e79029bff9(
    resource: _IEndpointRef_7ea728ed,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__635096970c8f6988b319790d01d10b7af1624a2bd87a8fd19d2f526067565d38(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f81524f5f031b60202ef5750c9c53a9e8e5e0357685aef97a068e09c19a1d5d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22395c6c2f1b0a694a9e0faf2c896173a496cbdf51ca26ecd7214a44487b981e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82adad35327e5af1f867ea3ce6b09d9cf8bf066d4f3f0c3a297e3425583291ed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fdfe64e097ccd04046eb25d75f28e5f90eca1ce0eda856ca0f77cf38cdb414e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e3365f1d0529739a9e96ac4af19a8abe17480deaa11498dbba4db6c1eb52a61(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b0a84d01612790328a1ecc8558a579f74f52fa1a781ed7197676c50fce5a6e2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e0c8197e58a0f1f00521e2589c5fe3688295bc923b51b75d41f29f6aec64d3e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.ConfigurationOverridesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ff6a672ee7bf784cfbde2614d2f6cae307ce23728014e1a8bb6736b2020c7c0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea06eef637e8c0a25b829a6c624ac3e00fd1f47e5a0dc21e18b827b60481aa0c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0753442657548325e3bd0a9ec7c567fdf41626466b3e89bfed14dee1c6cec778(
    *,
    certificate_arn: typing.Optional[builtins.str] = None,
    certificate_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ecb22ba4d8b0faedcb5f445667dd4c14b1bb238ebfc25811866bc27bb2f9f29(
    *,
    log_group_name: builtins.str,
    log_stream_name_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46f984090360c20eea47211457bc59ba0064e851b8407461cf578437814aeb01(
    *,
    application_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.EMREKSConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__817b097d9818e8dbd56314bb022a526176ef9e0a159ab0fbb93fd2ba36f723a2(
    *,
    max_files_to_keep: jsii.Number,
    rotation_size: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5e05064bc37ba71915107a21d96057346160606aa8cdc19d7293f9c9037b47a(
    *,
    classification: builtins.str,
    configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.EMREKSConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    properties: typing.Optional[typing.Union[typing.Mapping[builtins.str, builtins.str], _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a0503e26d3c8fcf0703183603081e1b7a18027a03a980ed33b0bb37c14dff86(
    *,
    cloud_watch_monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.CloudWatchMonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    container_log_rotation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.ContainerLogRotationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    persistent_app_ui: typing.Optional[builtins.str] = None,
    s3_monitoring_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.S3MonitoringConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2e089a4b5c6bf3faf983bfe03d5042364c4f68c554cd62834b53e7101c615e6(
    *,
    log_uri: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf3149ecf1698607ceb24e9bbca6c307d3e7ef064cb79d95651abb2c6d47065(
    *,
    execution_role_arn: builtins.str,
    release_label: builtins.str,
    type: builtins.str,
    virtual_cluster_id: builtins.str,
    configuration_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.ConfigurationOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6854e9fbbee664e2db7e06fdaa2e3ba6c9701b0e2bce486f38e57890c884e5af(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_configuration_data: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.SecurityConfigurationDataProperty, typing.Dict[builtins.str, typing.Any]]],
    container_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd681409fc29491c4c7e38d95888109a4646290c7d21b905a648c8e49a16cc2f(
    resource: _ISecurityConfigurationRef_1a326316,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__660efc2daaa24d4382b34d964b39452ea882396bad4388acc85c9310c23989b7(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adb0191ab4815b507e015b9e53d9a0db9a4b2cee4d58e694160b44a0afe9de56(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1af0cddd893391660a5e37e50121ea37e58f057538ee52904d314b61aa41e9f8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f26dc902c9625031a3359860f64fc2c50df8f76bad05bb460ecddf60a8aef53f(
    value: typing.Union[_IResolvable_da3f097b, CfnSecurityConfiguration.SecurityConfigurationDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e042738064d96ccff993bc56cc79c7f46ec050b950127cf902598481c68cc9ca(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSecurityConfiguration.ContainerProviderProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53a52be55c2ce7be9e3a6ef926bc4d573b86d29f190210e5a9df93e655aaa102(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c1399f0742e46b06a814da734363ceffaf363d4e01a9b76b7506306a813a9c7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d89332cbba1127be6b8fe5491bceeed96e052518779c07ad4e4adacc05f75a31(
    *,
    local_disk_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.LocalDiskEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.S3EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3caee46c3c428a38039046963627b08574e1358dac5ece585461aababf8e4ef(
    *,
    iam_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.IAMConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    identity_center_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.IdentityCenterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76bfe5c6bd23193313bfe6dec8fbee6bf437673f2b46dac54b11ef0689913eab(
    *,
    lake_formation_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.LakeFormationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0c51a22b843b82d3a2f70b24e8095308dd8fdfb79690f5b0cd87fd63c28654d(
    *,
    eks_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.EksInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7defba1afab8843e36776150f6c12baad1d8fceaa1fd92112cabce82147e94e2(
    *,
    id: builtins.str,
    type: builtins.str,
    info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.ContainerInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e7712fd7b4a2a053327b1eea8a52f21d3d1f1d9e7efa9b2397fcd486b8eaeb2(
    *,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f41c637d9cbed4eeb23e20c4bd7928d0c1cf31163ac17153b7e304db762c1128(
    *,
    at_rest_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.AtRestEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    in_transit_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.InTransitEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__496b9118a2747d1a2075cedbe8d8eb5f5ac83784984ccc18bef308ce389d64e5(
    *,
    system_role: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f599ccca334d667e8c2151ff1efb55fe1a5722a9cef6e6b8e3ad7fc64f6fcb70(
    *,
    enable_identity_center: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    identity_center_application_assignment_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    identity_center_instance_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a9664211c1bd9e53f5b1ef1ea8cf192b0fc36da061879adc5e0f50d83df33bb(
    *,
    tls_certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.TLSCertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28a87784f85f0e663cd90e1e0ab8f0457d68b1df23a29ec1815efffb1fd76efd(
    *,
    authorized_session_tag_value: typing.Optional[builtins.str] = None,
    query_access_control_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    query_engine_role_arn: typing.Optional[builtins.str] = None,
    secure_namespace_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.SecureNamespaceInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4511400021d1afa893531440e558c9b57d99a8e63fbbae50c1a5f5360e1eff2d(
    *,
    aws_kms_key_id: typing.Optional[builtins.str] = None,
    encryption_key_provider_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd8412be690034fa6d1270d9b5c028c8a5a0b2b83defe7f3c1a7d21b32790a48(
    *,
    encryption_option: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3759e01f350e1d397915bd4d597987fa0422a4123e65b626ce60a9961e8df11c(
    *,
    cluster_id: typing.Optional[builtins.str] = None,
    namespace: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f493d86970b0aa105efd09d9ecac31f88dcd70be4b4008d89647b65c9b717653(
    *,
    authentication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    authorization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.AuthorizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f48594c857b1e3ec68169c0a14e6791998c57deb66a4337a04f55c5cd650e7e(
    *,
    certificate_provider_type: typing.Optional[builtins.str] = None,
    private_key_secret_arn: typing.Optional[builtins.str] = None,
    public_key_secret_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aac200d052b6d8b5d83eb4ae9a2c63aeb84f4e4ce7bc48d47327fc9874cfba98(
    *,
    security_configuration_data: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.SecurityConfigurationDataProperty, typing.Dict[builtins.str, typing.Any]]],
    container_provider: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSecurityConfiguration.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a06dc2760ceb0de7a449a23941f15987094157d1a540c30fa67c9e49a3e06101(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    container_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVirtualCluster.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    security_configuration_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__516f2f16964e7ef220cab41225b3b7c3e3c0a9ee6b852252c3f1a1871264629c(
    resource: _IVirtualClusterRef_14fb6023,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d7111433bac0bf3eef5f3ffc73c4e649ef41bf63a44cfbc891a7f06a1b9be4b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcaea2c30abe44238307f21b3c8a59222637a0fd52fab165c6272df6fa333e6a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    virtual_cluster_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c9228b7a5165151302a3840836f9259f95d9a03c7684570914df3c5f40c23a7(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__802f118bbdec329d651201f6f69836e8e9523c47d32a262a55c4813747ccf78c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3035614e8641a59d4a7600ad906f142054401a42e6c1ca14df8b5d57d08f0823(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__617f2c6bc289034f068a4b514139fc0bee8f6455f589c3e2de7ee7fb7a3a92e3(
    value: typing.Union[_IResolvable_da3f097b, CfnVirtualCluster.ContainerProviderProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aea4d0052a5a6cb82d57b5655349988466e02d75bbcc22aec370e6810b4c382d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d05d102efa2c9eb1d454519ceade8e11615a54a4a6a9f26f4883e2051aa27414(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3436f23ae2ca4313aacb96519980906e71e5bc37e7a466a53353480f948e674(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e5baf7a38335e2eb8733f2aa2d96a9593d774d095fb8a05dcf1d8bd22323050(
    *,
    eks_info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVirtualCluster.EksInfoProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19801d68aea5b7c69bfd60c7d9c690e62c4643fe80fcda956e884f367b8b1dcf(
    *,
    id: builtins.str,
    info: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVirtualCluster.ContainerInfoProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26be72236c14a8878e3d92d7b17397aa49c8a844f85e9e98c958600dd7a08c8f(
    *,
    namespace: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79f93ead2a436b8c5a2fc364fff5d9da849a851543aa1433cd7ab649d79d55f9(
    *,
    container_provider: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVirtualCluster.ContainerProviderProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    security_configuration_id: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
