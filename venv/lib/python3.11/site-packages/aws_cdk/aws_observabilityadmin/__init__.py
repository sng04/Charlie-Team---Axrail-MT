r'''
# AWS::ObservabilityAdmin Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_observabilityadmin as observabilityadmin
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ObservabilityAdmin construct libraries](https://constructs.dev/search?q=observabilityadmin)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ObservabilityAdmin resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ObservabilityAdmin.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ObservabilityAdmin](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ObservabilityAdmin.html).

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
from ..interfaces.aws_observabilityadmin import (
    IOrganizationCentralizationRuleRef as _IOrganizationCentralizationRuleRef_c0e786ce,
    IOrganizationTelemetryRuleRef as _IOrganizationTelemetryRuleRef_c536ab68,
    IS3TableIntegrationRef as _IS3TableIntegrationRef_0d27be71,
    ITelemetryPipelinesRef as _ITelemetryPipelinesRef_a5d8576e,
    ITelemetryRuleRef as _ITelemetryRuleRef_9918195f,
    OrganizationCentralizationRuleReference as _OrganizationCentralizationRuleReference_e0f14dd2,
    OrganizationTelemetryRuleReference as _OrganizationTelemetryRuleReference_447c11d2,
    S3TableIntegrationReference as _S3TableIntegrationReference_5391966c,
    TelemetryPipelinesReference as _TelemetryPipelinesReference_c5feae72,
    TelemetryRuleReference as _TelemetryRuleReference_35b2b664,
)


@jsii.implements(_IInspectable_c2943556, _IOrganizationCentralizationRuleRef_c0e786ce, _ITaggableV2_4e6798f8)
class CfnOrganizationCentralizationRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule",
):
    '''Defines how telemetry data should be centralized across an AWS Organization, including source and destination configurations.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationcentralizationrule.html
    :cloudformationResource: AWS::ObservabilityAdmin::OrganizationCentralizationRule
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_observabilityadmin as observabilityadmin
        
        cfn_organization_centralization_rule = observabilityadmin.CfnOrganizationCentralizationRule(self, "MyCfnOrganizationCentralizationRule",
            rule=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleProperty(
                destination=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty(
                    region="region",
        
                    # the properties below are optional
                    account="account",
                    destination_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty(
                        backup_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                            region="region",
        
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn"
                        ),
                        log_group_name_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty(
                            log_group_name_pattern="logGroupNamePattern"
                        ),
                        logs_encryption_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                            encryption_strategy="encryptionStrategy",
        
                            # the properties below are optional
                            encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                            kms_key_arn="kmsKeyArn"
                        )
                    )
                ),
                source=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty(
                    regions=["regions"],
        
                    # the properties below are optional
                    scope="scope",
                    source_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty(
                        encrypted_log_group_strategy="encryptedLogGroupStrategy",
                        log_group_selection_criteria="logGroupSelectionCriteria"
                    )
                )
            ),
            rule_name="ruleName",
        
            # the properties below are optional
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
        rule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationCentralizationRule.CentralizationRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ObservabilityAdmin::OrganizationCentralizationRule``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule: 
        :param rule_name: The name of the organization centralization rule.
        :param tags: A key-value pair to filter resources based on tags associated with the resource. For more information about tags, see `What are tags? <https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html>`_
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18acbc8917f3c4cbc8bb06f5fae76010e41ab5f0e9b157f4c324c214a180ef2e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationCentralizationRuleProps(
            rule=rule, rule_name=rule_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnOrganizationCentralizationRule")
    @builtins.classmethod
    def is_cfn_organization_centralization_rule(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnOrganizationCentralizationRule.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecabb5646d522a7c00aa40f3e19c4d2e5dccb6109cb58329723f9f47be7267d6)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnOrganizationCentralizationRule", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02b2ea8ec552fc96b3662b368fa64eea5f82839c3bd0f1aa52bd64bc495f5341)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f130448a4f76aff49b8e31a382ea5ab14eacdf34a74afe86be23352ded6622e1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the organization centralization rule.

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

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
    @jsii.member(jsii_name="organizationCentralizationRuleRef")
    def organization_centralization_rule_ref(
        self,
    ) -> "_OrganizationCentralizationRuleReference_e0f14dd2":
        '''A reference to a OrganizationCentralizationRule resource.'''
        return typing.cast("_OrganizationCentralizationRuleReference_e0f14dd2", jsii.get(self, "organizationCentralizationRuleRef"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.CentralizationRuleProperty"]:
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.CentralizationRuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.CentralizationRuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fbb5a84b6997cee28db4665d22fee83629861a1e51fe754b85b3858441e7c2d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        '''The name of the organization centralization rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f42b1edd10be1da3c565db5f9585850487a7c51b5ad7ab0a72c1d4345b4ac7f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A key-value pair to filter resources based on tags associated with the resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a58679a9a3a800195cc0ecf82553695580c2dd2061901e27320b9025cb6ed262)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "region": "region",
            "account": "account",
            "destination_logs_configuration": "destinationLogsConfiguration",
        },
    )
    class CentralizationRuleDestinationProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            account: typing.Optional[builtins.str] = None,
            destination_logs_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration specifying the primary destination for centralized telemetry data.

            :param region: The primary destination region to which telemetry data should be centralized.
            :param account: The destination account (within the organization) to which the telemetry data should be centralized.
            :param destination_logs_configuration: Log specific configuration for centralization destination log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                centralization_rule_destination_property = observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty(
                    region="region",
                
                    # the properties below are optional
                    account="account",
                    destination_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty(
                        backup_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                            region="region",
                
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn"
                        ),
                        log_group_name_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty(
                            log_group_name_pattern="logGroupNamePattern"
                        ),
                        logs_encryption_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                            encryption_strategy="encryptionStrategy",
                
                            # the properties below are optional
                            encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                            kms_key_arn="kmsKeyArn"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48736d0ec2563919af9b82675cbe965d2288bd15210b9c8b34911e7a89ae0f47)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument account", value=account, expected_type=type_hints["account"])
                check_type(argname="argument destination_logs_configuration", value=destination_logs_configuration, expected_type=type_hints["destination_logs_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region": region,
            }
            if account is not None:
                self._values["account"] = account
            if destination_logs_configuration is not None:
                self._values["destination_logs_configuration"] = destination_logs_configuration

        @builtins.property
        def region(self) -> builtins.str:
            '''The primary destination region to which telemetry data should be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account(self) -> typing.Optional[builtins.str]:
            '''The destination account (within the organization) to which the telemetry data should be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-account
            '''
            result = self._values.get("account")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_logs_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty"]]:
            '''Log specific configuration for centralization destination log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationruledestination.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationruledestination-destinationlogsconfiguration
            '''
            result = self._values.get("destination_logs_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CentralizationRuleDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "source": "source"},
    )
    class CentralizationRuleProperty:
        def __init__(
            self,
            *,
            destination: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            source: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''Defines how telemetry data should be centralized across an AWS Organization, including source and destination configurations.

            :param destination: Configuration determining where the telemetry data should be centralized, backed up, as well as encryption configuration for the primary and backup destinations.
            :param source: Configuration determining the source of the telemetry data to be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                centralization_rule_property = observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleProperty(
                    destination=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty(
                        region="region",
                
                        # the properties below are optional
                        account="account",
                        destination_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty(
                            backup_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                                region="region",
                
                                # the properties below are optional
                                kms_key_arn="kmsKeyArn"
                            ),
                            log_group_name_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty(
                                log_group_name_pattern="logGroupNamePattern"
                            ),
                            logs_encryption_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                                encryption_strategy="encryptionStrategy",
                
                                # the properties below are optional
                                encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                                kms_key_arn="kmsKeyArn"
                            )
                        )
                    ),
                    source=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty(
                        regions=["regions"],
                
                        # the properties below are optional
                        scope="scope",
                        source_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty(
                            encrypted_log_group_strategy="encryptedLogGroupStrategy",
                            log_group_selection_criteria="logGroupSelectionCriteria"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb475427ce4a2316b8478f1c58d17ddd5783412b26cdfb98819c47313aa718dc)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
                "source": source,
            }

        @builtins.property
        def destination(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty"]:
            '''Configuration determining where the telemetry data should be centralized, backed up, as well as encryption configuration for the primary and backup destinations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationrule-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty"], result)

        @builtins.property
        def source(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty"]:
            '''Configuration determining the source of the telemetry data to be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrule.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationrule-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CentralizationRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "regions": "regions",
            "scope": "scope",
            "source_logs_configuration": "sourceLogsConfiguration",
        },
    )
    class CentralizationRuleSourceProperty:
        def __init__(
            self,
            *,
            regions: typing.Sequence[builtins.str],
            scope: typing.Optional[builtins.str] = None,
            source_logs_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration specifying the source of telemetry data to be centralized.

            :param regions: The list of source regions from which telemetry data should be centralized.
            :param scope: The organizational scope from which telemetry data should be centralized, specified using organization id, accounts or organizational unit ids.
            :param source_logs_configuration: Log specific configuration for centralization source log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                centralization_rule_source_property = observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty(
                    regions=["regions"],
                
                    # the properties below are optional
                    scope="scope",
                    source_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty(
                        encrypted_log_group_strategy="encryptedLogGroupStrategy",
                        log_group_selection_criteria="logGroupSelectionCriteria"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8c4d1dff0252b97263e138c77bea2f698277762eeffd4fcf3911e496ac5762e4)
                check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
                check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
                check_type(argname="argument source_logs_configuration", value=source_logs_configuration, expected_type=type_hints["source_logs_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "regions": regions,
            }
            if scope is not None:
                self._values["scope"] = scope
            if source_logs_configuration is not None:
                self._values["source_logs_configuration"] = source_logs_configuration

        @builtins.property
        def regions(self) -> typing.List[builtins.str]:
            '''The list of source regions from which telemetry data should be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-regions
            '''
            result = self._values.get("regions")
            assert result is not None, "Required property 'regions' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def scope(self) -> typing.Optional[builtins.str]:
            '''The organizational scope from which telemetry data should be centralized, specified using organization id, accounts or organizational unit ids.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-scope
            '''
            result = self._values.get("scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_logs_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty"]]:
            '''Log specific configuration for centralization source log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-centralizationrulesource.html#cfn-observabilityadmin-organizationcentralizationrule-centralizationrulesource-sourcelogsconfiguration
            '''
            result = self._values.get("source_logs_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CentralizationRuleSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "backup_configuration": "backupConfiguration",
            "log_group_name_configuration": "logGroupNameConfiguration",
            "logs_encryption_configuration": "logsEncryptionConfiguration",
        },
    )
    class DestinationLogsConfigurationProperty:
        def __init__(
            self,
            *,
            backup_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            log_group_name_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            logs_encryption_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration for centralization destination log groups, including encryption and backup settings.

            :param backup_configuration: Configuration defining the backup region and an optional KMS key for the backup destination.
            :param log_group_name_configuration: 
            :param logs_encryption_configuration: The encryption configuration for centralization destination log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                destination_logs_configuration_property = observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty(
                    backup_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                        region="region",
                
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn"
                    ),
                    log_group_name_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty(
                        log_group_name_pattern="logGroupNamePattern"
                    ),
                    logs_encryption_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                        encryption_strategy="encryptionStrategy",
                
                        # the properties below are optional
                        encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                        kms_key_arn="kmsKeyArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5dd7a39f2c94fa5f25cdcfc83cd888a8c3b22c09afa009f3ed5de76fd5befe41)
                check_type(argname="argument backup_configuration", value=backup_configuration, expected_type=type_hints["backup_configuration"])
                check_type(argname="argument log_group_name_configuration", value=log_group_name_configuration, expected_type=type_hints["log_group_name_configuration"])
                check_type(argname="argument logs_encryption_configuration", value=logs_encryption_configuration, expected_type=type_hints["logs_encryption_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if backup_configuration is not None:
                self._values["backup_configuration"] = backup_configuration
            if log_group_name_configuration is not None:
                self._values["log_group_name_configuration"] = log_group_name_configuration
            if logs_encryption_configuration is not None:
                self._values["logs_encryption_configuration"] = logs_encryption_configuration

        @builtins.property
        def backup_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty"]]:
            '''Configuration defining the backup region and an optional KMS key for the backup destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-backupconfiguration
            '''
            result = self._values.get("backup_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty"]], result)

        @builtins.property
        def log_group_name_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-loggroupnameconfiguration
            '''
            result = self._values.get("log_group_name_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty"]], result)

        @builtins.property
        def logs_encryption_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty"]]:
            '''The encryption configuration for centralization destination log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-destinationlogsconfiguration-logsencryptionconfiguration
            '''
            result = self._values.get("logs_encryption_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationLogsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name_pattern": "logGroupNamePattern"},
    )
    class LogGroupNameConfigurationProperty:
        def __init__(self, *, log_group_name_pattern: builtins.str) -> None:
            '''
            :param log_group_name_pattern: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                log_group_name_configuration_property = observabilityadmin.CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty(
                    log_group_name_pattern="logGroupNamePattern"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc628f661292ed8b216472c835d47a09fd581394061ab648aa685a81bcef75c8)
                check_type(argname="argument log_group_name_pattern", value=log_group_name_pattern, expected_type=type_hints["log_group_name_pattern"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_name_pattern": log_group_name_pattern,
            }

        @builtins.property
        def log_group_name_pattern(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration-loggroupnamepattern
            '''
            result = self._values.get("log_group_name_pattern")
            assert result is not None, "Required property 'log_group_name_pattern' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogGroupNameConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"region": "region", "kms_key_arn": "kmsKeyArn"},
    )
    class LogsBackupConfigurationProperty:
        def __init__(
            self,
            *,
            region: builtins.str,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for backing up centralized log data to a secondary region.

            :param region: Logs specific backup destination region within the primary destination account to which log data should be centralized.
            :param kms_key_arn: KMS Key ARN belonging to the primary destination account and backup region, to encrypt newly created central log groups in the backup destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                logs_backup_configuration_property = observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                    region="region",
                
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__35d26acca25f06381fb096b21a6f3791d0ef735549ac7bae5795f4e646184d86)
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "region": region,
            }
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def region(self) -> builtins.str:
            '''Logs specific backup destination region within the primary destination account to which log data should be centralized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''KMS Key ARN belonging to the primary destination account and backup region, to encrypt newly created central log groups in the backup destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-logsbackupconfiguration-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogsBackupConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encryption_strategy": "encryptionStrategy",
            "encryption_conflict_resolution_strategy": "encryptionConflictResolutionStrategy",
            "kms_key_arn": "kmsKeyArn",
        },
    )
    class LogsEncryptionConfigurationProperty:
        def __init__(
            self,
            *,
            encryption_strategy: builtins.str,
            encryption_conflict_resolution_strategy: typing.Optional[builtins.str] = None,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration for encrypting centralized log groups.

            This configuration is only applied to destination log groups for which the corresponding source log groups are encrypted using Customer Managed KMS Keys.

            :param encryption_strategy: Configuration that determines the encryption strategy of the destination log groups. CUSTOMER_MANAGED uses the configured KmsKeyArn to encrypt newly created destination log groups.
            :param encryption_conflict_resolution_strategy: Conflict resolution strategy for centralization if the encryption strategy is set to CUSTOMER_MANAGED and the destination log group is encrypted with an AWS_OWNED KMS Key. ALLOW lets centralization go through while SKIP prevents centralization into the destination log group.
            :param kms_key_arn: KMS Key ARN belonging to the primary destination account and region, to encrypt newly created central log groups in the primary destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                logs_encryption_configuration_property = observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                    encryption_strategy="encryptionStrategy",
                
                    # the properties below are optional
                    encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d66f88a29d04606b9d6748d2a92fb0d7bf4a500a64fceff8556e1ac2275828e)
                check_type(argname="argument encryption_strategy", value=encryption_strategy, expected_type=type_hints["encryption_strategy"])
                check_type(argname="argument encryption_conflict_resolution_strategy", value=encryption_conflict_resolution_strategy, expected_type=type_hints["encryption_conflict_resolution_strategy"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encryption_strategy": encryption_strategy,
            }
            if encryption_conflict_resolution_strategy is not None:
                self._values["encryption_conflict_resolution_strategy"] = encryption_conflict_resolution_strategy
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def encryption_strategy(self) -> builtins.str:
            '''Configuration that determines the encryption strategy of the destination log groups.

            CUSTOMER_MANAGED uses the configured KmsKeyArn to encrypt newly created destination log groups.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionstrategy
            '''
            result = self._values.get("encryption_strategy")
            assert result is not None, "Required property 'encryption_strategy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def encryption_conflict_resolution_strategy(
            self,
        ) -> typing.Optional[builtins.str]:
            '''Conflict resolution strategy for centralization if the encryption strategy is set to CUSTOMER_MANAGED and the destination log group is encrypted with an AWS_OWNED KMS Key.

            ALLOW lets centralization go through while SKIP prevents centralization into the destination log group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-encryptionconflictresolutionstrategy
            '''
            result = self._values.get("encryption_conflict_resolution_strategy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''KMS Key ARN belonging to the primary destination account and region, to encrypt newly created central log groups in the primary destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-logsencryptionconfiguration-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogsEncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "encrypted_log_group_strategy": "encryptedLogGroupStrategy",
            "log_group_selection_criteria": "logGroupSelectionCriteria",
        },
    )
    class SourceLogsConfigurationProperty:
        def __init__(
            self,
            *,
            encrypted_log_group_strategy: builtins.str,
            log_group_selection_criteria: builtins.str,
        ) -> None:
            '''Configuration for selecting and handling source log groups for centralization.

            :param encrypted_log_group_strategy: A strategy determining whether to centralize source log groups that are encrypted with customer managed KMS keys (CMK). ALLOW will consider CMK encrypted source log groups for centralization while SKIP will skip CMK encrypted source log groups from centralization.
            :param log_group_selection_criteria: The selection criteria that specifies which source log groups to centralize. The selection criteria uses the same format as OAM link filters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                source_logs_configuration_property = observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty(
                    encrypted_log_group_strategy="encryptedLogGroupStrategy",
                    log_group_selection_criteria="logGroupSelectionCriteria"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__20a12247cb1287e19ec3a764cc738d756d26c889450a5b771811f8378a2b5d6c)
                check_type(argname="argument encrypted_log_group_strategy", value=encrypted_log_group_strategy, expected_type=type_hints["encrypted_log_group_strategy"])
                check_type(argname="argument log_group_selection_criteria", value=log_group_selection_criteria, expected_type=type_hints["log_group_selection_criteria"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "encrypted_log_group_strategy": encrypted_log_group_strategy,
                "log_group_selection_criteria": log_group_selection_criteria,
            }

        @builtins.property
        def encrypted_log_group_strategy(self) -> builtins.str:
            '''A strategy determining whether to centralize source log groups that are encrypted with customer managed KMS keys (CMK).

            ALLOW will consider CMK encrypted source log groups for centralization while SKIP will skip CMK encrypted source log groups from centralization.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-encryptedloggroupstrategy
            '''
            result = self._values.get("encrypted_log_group_strategy")
            assert result is not None, "Required property 'encrypted_log_group_strategy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_group_selection_criteria(self) -> builtins.str:
            '''The selection criteria that specifies which source log groups to centralize.

            The selection criteria uses the same format as OAM link filters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration.html#cfn-observabilityadmin-organizationcentralizationrule-sourcelogsconfiguration-loggroupselectioncriteria
            '''
            result = self._values.get("log_group_selection_criteria")
            assert result is not None, "Required property 'log_group_selection_criteria' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceLogsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationCentralizationRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_name": "ruleName", "tags": "tags"},
)
class CfnOrganizationCentralizationRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationCentralizationRule.CentralizationRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOrganizationCentralizationRule``.

        :param rule: 
        :param rule_name: The name of the organization centralization rule.
        :param tags: A key-value pair to filter resources based on tags associated with the resource. For more information about tags, see `What are tags? <https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationcentralizationrule.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            cfn_organization_centralization_rule_props = observabilityadmin.CfnOrganizationCentralizationRuleProps(
                rule=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleProperty(
                    destination=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty(
                        region="region",
            
                        # the properties below are optional
                        account="account",
                        destination_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty(
                            backup_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty(
                                region="region",
            
                                # the properties below are optional
                                kms_key_arn="kmsKeyArn"
                            ),
                            log_group_name_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty(
                                log_group_name_pattern="logGroupNamePattern"
                            ),
                            logs_encryption_configuration=observabilityadmin.CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty(
                                encryption_strategy="encryptionStrategy",
            
                                # the properties below are optional
                                encryption_conflict_resolution_strategy="encryptionConflictResolutionStrategy",
                                kms_key_arn="kmsKeyArn"
                            )
                        )
                    ),
                    source=observabilityadmin.CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty(
                        regions=["regions"],
            
                        # the properties below are optional
                        scope="scope",
                        source_logs_configuration=observabilityadmin.CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty(
                            encrypted_log_group_strategy="encryptedLogGroupStrategy",
                            log_group_selection_criteria="logGroupSelectionCriteria"
                        )
                    )
                ),
                rule_name="ruleName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00d0ecee2cd9ac728ca3e321203ce2e611e56b0b2d415ba2673a50599e4512cd)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
            "rule_name": rule_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.CentralizationRuleProperty"]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationcentralizationrule.html#cfn-observabilityadmin-organizationcentralizationrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOrganizationCentralizationRule.CentralizationRuleProperty"], result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the organization centralization rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationcentralizationrule.html#cfn-observabilityadmin-organizationcentralizationrule-rulename
        '''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''A key-value pair to filter resources based on tags associated with the resource.

        For more information about tags, see `What are tags? <https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationcentralizationrule.html#cfn-observabilityadmin-organizationcentralizationrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationCentralizationRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IOrganizationTelemetryRuleRef_c536ab68, _ITaggableV2_4e6798f8)
class CfnOrganizationTelemetryRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule",
):
    '''Retrieves the details of a specific organization centralization rule.

    This operation can only be called by the organization's management account or a delegated administrator account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html
    :cloudformationResource: AWS::ObservabilityAdmin::OrganizationTelemetryRule
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_observabilityadmin as observabilityadmin
        
        cfn_organization_telemetry_rule = observabilityadmin.CfnOrganizationTelemetryRule(self, "MyCfnOrganizationTelemetryRule",
            rule=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty(
                resource_type="resourceType",
                telemetry_type="telemetryType",
        
                # the properties below are optional
                destination_configuration=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                    cloudtrail_parameters=observabilityadmin.CfnOrganizationTelemetryRule.CloudtrailParametersProperty(
                        advanced_event_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty(
                            field_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty(
                                ends_with=["endsWith"],
                                equal_to=["equalTo"],
                                field="field",
                                not_ends_with=["notEndsWith"],
                                not_equals=["notEquals"],
                                not_starts_with=["notStartsWith"],
                                starts_with=["startsWith"]
                            )],
        
                            # the properties below are optional
                            name="name"
                        )]
                    ),
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    elb_load_balancer_logging_parameters=observabilityadmin.CfnOrganizationTelemetryRule.ELBLoadBalancerLoggingParametersProperty(
                        field_delimiter="fieldDelimiter",
                        output_format="outputFormat"
                    ),
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    ),
                    waf_logging_parameters=observabilityadmin.CfnOrganizationTelemetryRule.WAFLoggingParametersProperty(
                        logging_filter=observabilityadmin.CfnOrganizationTelemetryRule.LoggingFilterProperty(
                            default_behavior="defaultBehavior",
                            filters=[observabilityadmin.CfnOrganizationTelemetryRule.FilterProperty(
                                behavior="behavior",
                                conditions=[observabilityadmin.CfnOrganizationTelemetryRule.ConditionProperty(
                                    action_condition=observabilityadmin.CfnOrganizationTelemetryRule.ActionConditionProperty(
                                        action="action"
                                    ),
                                    label_name_condition=observabilityadmin.CfnOrganizationTelemetryRule.LabelNameConditionProperty(
                                        label_name="labelName"
                                    )
                                )],
                                requirement="requirement"
                            )]
                        ),
                        log_type="logType",
                        redacted_fields=[observabilityadmin.CfnOrganizationTelemetryRule.FieldToMatchProperty(
                            method="method",
                            query_string="queryString",
                            single_header=observabilityadmin.CfnOrganizationTelemetryRule.SingleHeaderProperty(
                                name="name"
                            ),
                            uri_path="uriPath"
                        )]
                    )
                ),
                scope="scope",
                selection_criteria="selectionCriteria",
                telemetry_source_types=["telemetrySourceTypes"]
            ),
            rule_name="ruleName",
        
            # the properties below are optional
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
        rule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.TelemetryRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ObservabilityAdmin::OrganizationTelemetryRule``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule: The name of the organization telemetry rule.
        :param rule_name: The name of the organization centralization rule.
        :param tags: Lists all tags attached to the specified resource. Supports telemetry rule resources and telemetry pipeline resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a67d6a9dd82924a413b7d3435faeb8efa735048df0244b926e672def8c2d5f75)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationTelemetryRuleProps(
            rule=rule, rule_name=rule_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnOrganizationTelemetryRule")
    @builtins.classmethod
    def is_cfn_organization_telemetry_rule(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnOrganizationTelemetryRule.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7ca13b7cccda36c5b43cead9ffee16b45fa649b63750b67cfc542107deb6702)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnOrganizationTelemetryRule", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cb893813673a29ee1f384593916d34bdcc440b816dfc54ad27097692c5a64e9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c809c768027da00df4018694393faf5d77af9754b12923bf684ada119faecfc7)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The arn of the organization telemetry rule.

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

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
    @jsii.member(jsii_name="organizationTelemetryRuleRef")
    def organization_telemetry_rule_ref(
        self,
    ) -> "_OrganizationTelemetryRuleReference_447c11d2":
        '''A reference to a OrganizationTelemetryRule resource.'''
        return typing.cast("_OrganizationTelemetryRuleReference_447c11d2", jsii.get(self, "organizationTelemetryRuleRef"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.TelemetryRuleProperty"]:
        '''The name of the organization telemetry rule.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.TelemetryRuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.TelemetryRuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97cf84910a3c46b94c3e90ddf73c07b304a029e413bebd1b7c5e7b2bbe5cd411)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        '''The name of the organization centralization rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84099afcf940dd46614099ecc03e181396a6d202813d1517bd79414c5aa2f5ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Lists all tags attached to the specified resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d494e45ec3f03fbc2168c2e374f689615e98524c832aa6247ad243fabe01ffe7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.ActionConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action"},
    )
    class ActionConditionProperty:
        def __init__(self, *, action: typing.Optional[builtins.str] = None) -> None:
            '''Condition that matches based on the specific WAF action taken on the request.

            :param action: The WAF action to match against (ALLOW, BLOCK, COUNT, CAPTCHA, CHALLENGE, EXCLUDED_AS_COUNT).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-actioncondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                action_condition_property = observabilityadmin.CfnOrganizationTelemetryRule.ActionConditionProperty(
                    action="action"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b6b5585476ea575f5f355362e763f68412449ff22910a34eb3e7d80ceec7283)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''The WAF action to match against (ALLOW, BLOCK, COUNT, CAPTCHA, CHALLENGE, EXCLUDED_AS_COUNT).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-actioncondition.html#cfn-observabilityadmin-organizationtelemetryrule-actioncondition-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"field_selectors": "fieldSelectors", "name": "name"},
    )
    class AdvancedEventSelectorProperty:
        def __init__(
            self,
            *,
            field_selectors: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]],
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Advanced event selectors let you create fine-grained selectors for management, data, and network activity events.

            :param field_selectors: Contains all selector statements in an advanced event selector.
            :param name: An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                advanced_event_selector_property = observabilityadmin.CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty(
                    field_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty(
                        ends_with=["endsWith"],
                        equal_to=["equalTo"],
                        field="field",
                        not_ends_with=["notEndsWith"],
                        not_equals=["notEquals"],
                        not_starts_with=["notStartsWith"],
                        starts_with=["startsWith"]
                    )],
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a8d791206424757183daedc38dee2af439aaf16a9fafc6af1201043adf7c3de)
                check_type(argname="argument field_selectors", value=field_selectors, expected_type=type_hints["field_selectors"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_selectors": field_selectors,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def field_selectors(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty"]]]:
            '''Contains all selector statements in an advanced event selector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector.html#cfn-observabilityadmin-organizationtelemetryrule-advancedeventselector-fieldselectors
            '''
            result = self._values.get("field_selectors")
            assert result is not None, "Required property 'field_selectors' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty"]]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedeventselector.html#cfn-observabilityadmin-organizationtelemetryrule-advancedeventselector-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedEventSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ends_with": "endsWith",
            "equal_to": "equalTo",
            "field": "field",
            "not_ends_with": "notEndsWith",
            "not_equals": "notEquals",
            "not_starts_with": "notStartsWith",
            "starts_with": "startsWith",
        },
    )
    class AdvancedFieldSelectorProperty:
        def __init__(
            self,
            *,
            ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
            field: typing.Optional[builtins.str] = None,
            not_ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Defines criteria for selecting resources based on field values.

            :param ends_with: Matches if the field value ends with the specified value.
            :param equal_to: Matches if the field value equals the specified value.
            :param field: The name of the field to use for selection.
            :param not_ends_with: Matches if the field value does not end with the specified value.
            :param not_equals: Matches if the field value does not equal the specified value.
            :param not_starts_with: Matches if the field value does not start with the specified value.
            :param starts_with: Matches if the field value starts with the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedfieldselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                advanced_field_selector_property = observabilityadmin.CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty(
                    ends_with=["endsWith"],
                    equal_to=["equalTo"],
                    field="field",
                    not_ends_with=["notEndsWith"],
                    not_equals=["notEquals"],
                    not_starts_with=["notStartsWith"],
                    starts_with=["startsWith"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3a750f509bbf975a3106e6633766b065ca671d998289bcba4ef16d2b9c83abab)
                check_type(argname="argument ends_with", value=ends_with, expected_type=type_hints["ends_with"])
                check_type(argname="argument equal_to", value=equal_to, expected_type=type_hints["equal_to"])
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
                check_type(argname="argument not_ends_with", value=not_ends_with, expected_type=type_hints["not_ends_with"])
                check_type(argname="argument not_equals", value=not_equals, expected_type=type_hints["not_equals"])
                check_type(argname="argument not_starts_with", value=not_starts_with, expected_type=type_hints["not_starts_with"])
                check_type(argname="argument starts_with", value=starts_with, expected_type=type_hints["starts_with"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ends_with is not None:
                self._values["ends_with"] = ends_with
            if equal_to is not None:
                self._values["equal_to"] = equal_to
            if field is not None:
                self._values["field"] = field
            if not_ends_with is not None:
                self._values["not_ends_with"] = not_ends_with
            if not_equals is not None:
                self._values["not_equals"] = not_equals
            if not_starts_with is not None:
                self._values["not_starts_with"] = not_starts_with
            if starts_with is not None:
                self._values["starts_with"] = starts_with

        @builtins.property
        def ends_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value ends with the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedfieldselector.html#cfn-observabilityadmin-organizationtelemetryrule-advancedfieldselector-endswith
            '''
            result = self._values.get("ends_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def equal_to(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value equals the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedfieldselector.html#cfn-observabilityadmin-organizationtelemetryrule-advancedfieldselector-equals
            '''
            result = self._values.get("equal_to")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field(self) -> typing.Optional[builtins.str]:
            '''The name of the field to use for selection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedfieldselector.html#cfn-observabilityadmin-organizationtelemetryrule-advancedfieldselector-field
            '''
            result = self._values.get("field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def not_ends_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value does not end with the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedfieldselector.html#cfn-observabilityadmin-organizationtelemetryrule-advancedfieldselector-notendswith
            '''
            result = self._values.get("not_ends_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_equals(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value does not equal the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedfieldselector.html#cfn-observabilityadmin-organizationtelemetryrule-advancedfieldselector-notequals
            '''
            result = self._values.get("not_equals")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_starts_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value does not start with the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedfieldselector.html#cfn-observabilityadmin-organizationtelemetryrule-advancedfieldselector-notstartswith
            '''
            result = self._values.get("not_starts_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def starts_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value starts with the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-advancedfieldselector.html#cfn-observabilityadmin-organizationtelemetryrule-advancedfieldselector-startswith
            '''
            result = self._values.get("starts_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedFieldSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.CloudtrailParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"advanced_event_selectors": "advancedEventSelectors"},
    )
    class CloudtrailParametersProperty:
        def __init__(
            self,
            *,
            advanced_event_selectors: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Parameters specific to AWS CloudTrail telemetry configuration.

            :param advanced_event_selectors: The advanced event selectors to use for filtering AWS CloudTrail events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                cloudtrail_parameters_property = observabilityadmin.CfnOrganizationTelemetryRule.CloudtrailParametersProperty(
                    advanced_event_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty(
                        field_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty(
                            ends_with=["endsWith"],
                            equal_to=["equalTo"],
                            field="field",
                            not_ends_with=["notEndsWith"],
                            not_equals=["notEquals"],
                            not_starts_with=["notStartsWith"],
                            starts_with=["startsWith"]
                        )],
                
                        # the properties below are optional
                        name="name"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6841a259b98239da9d79c07870bb6bcff9cbcac2a6f70f508616cce4cc82daa9)
                check_type(argname="argument advanced_event_selectors", value=advanced_event_selectors, expected_type=type_hints["advanced_event_selectors"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "advanced_event_selectors": advanced_event_selectors,
            }

        @builtins.property
        def advanced_event_selectors(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty"]]]:
            '''The advanced event selectors to use for filtering AWS CloudTrail events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-cloudtrailparameters.html#cfn-observabilityadmin-organizationtelemetryrule-cloudtrailparameters-advancedeventselectors
            '''
            result = self._values.get("advanced_event_selectors")
            assert result is not None, "Required property 'advanced_event_selectors' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudtrailParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.ConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_condition": "actionCondition",
            "label_name_condition": "labelNameCondition",
        },
    )
    class ConditionProperty:
        def __init__(
            self,
            *,
            action_condition: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.ActionConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            label_name_condition: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.LabelNameConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A single condition that can match based on WAF rule action or label name.

            :param action_condition: Matches log records based on the WAF rule action taken (ALLOW, BLOCK, COUNT, etc.).
            :param label_name_condition: Matches log records based on WAF rule labels applied to the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-condition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                condition_property = observabilityadmin.CfnOrganizationTelemetryRule.ConditionProperty(
                    action_condition=observabilityadmin.CfnOrganizationTelemetryRule.ActionConditionProperty(
                        action="action"
                    ),
                    label_name_condition=observabilityadmin.CfnOrganizationTelemetryRule.LabelNameConditionProperty(
                        label_name="labelName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__420adeb7464d458e2857bc92abac2bedbf48d00e02f72464d36b05d3d8e2eb70)
                check_type(argname="argument action_condition", value=action_condition, expected_type=type_hints["action_condition"])
                check_type(argname="argument label_name_condition", value=label_name_condition, expected_type=type_hints["label_name_condition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action_condition is not None:
                self._values["action_condition"] = action_condition
            if label_name_condition is not None:
                self._values["label_name_condition"] = label_name_condition

        @builtins.property
        def action_condition(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.ActionConditionProperty"]]:
            '''Matches log records based on the WAF rule action taken (ALLOW, BLOCK, COUNT, etc.).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-condition.html#cfn-observabilityadmin-organizationtelemetryrule-condition-actioncondition
            '''
            result = self._values.get("action_condition")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.ActionConditionProperty"]], result)

        @builtins.property
        def label_name_condition(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.LabelNameConditionProperty"]]:
            '''Matches log records based on WAF rule labels applied to the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-condition.html#cfn-observabilityadmin-organizationtelemetryrule-condition-labelnamecondition
            '''
            result = self._values.get("label_name_condition")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.LabelNameConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.ELBLoadBalancerLoggingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_delimiter": "fieldDelimiter",
            "output_format": "outputFormat",
        },
    )
    class ELBLoadBalancerLoggingParametersProperty:
        def __init__(
            self,
            *,
            field_delimiter: typing.Optional[builtins.str] = None,
            output_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration parameters for ELB load balancer logging, including output format and field delimiter settings.

            :param field_delimiter: The delimiter character used to separate fields in ELB access log entries when using plain text format.
            :param output_format: The format for ELB access log entries (plain text or JSON format).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                e_lBLoad_balancer_logging_parameters_property = observabilityadmin.CfnOrganizationTelemetryRule.ELBLoadBalancerLoggingParametersProperty(
                    field_delimiter="fieldDelimiter",
                    output_format="outputFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b56ef10916fda37562f5a73d7cca6d1cfc6daec018d9ce8b63aaaff139c12895)
                check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
                check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if field_delimiter is not None:
                self._values["field_delimiter"] = field_delimiter
            if output_format is not None:
                self._values["output_format"] = output_format

        @builtins.property
        def field_delimiter(self) -> typing.Optional[builtins.str]:
            '''The delimiter character used to separate fields in ELB access log entries when using plain text format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters.html#cfn-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-fielddelimiter
            '''
            result = self._values.get("field_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_format(self) -> typing.Optional[builtins.str]:
            '''The format for ELB access log entries (plain text or JSON format).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters.html#cfn-observabilityadmin-organizationtelemetryrule-elbloadbalancerloggingparameters-outputformat
            '''
            result = self._values.get("output_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ELBLoadBalancerLoggingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "method": "method",
            "query_string": "queryString",
            "single_header": "singleHeader",
            "uri_path": "uriPath",
        },
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            method: typing.Optional[builtins.str] = None,
            query_string: typing.Optional[builtins.str] = None,
            single_header: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.SingleHeaderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            uri_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies a field in the request to redact from WAF logs, such as headers, query parameters, or body content.

            :param method: Redacts the HTTP method from WAF logs.
            :param query_string: Redacts the entire query string from WAF logs.
            :param single_header: Redacts a specific header field by name from WAF logs.
            :param uri_path: Redacts the URI path from WAF logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                field_to_match_property = observabilityadmin.CfnOrganizationTelemetryRule.FieldToMatchProperty(
                    method="method",
                    query_string="queryString",
                    single_header=observabilityadmin.CfnOrganizationTelemetryRule.SingleHeaderProperty(
                        name="name"
                    ),
                    uri_path="uriPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__131a6841535b3ea1a525c04136403368fbb8448ee443a93a42242015401ac5dc)
                check_type(argname="argument method", value=method, expected_type=type_hints["method"])
                check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
                check_type(argname="argument single_header", value=single_header, expected_type=type_hints["single_header"])
                check_type(argname="argument uri_path", value=uri_path, expected_type=type_hints["uri_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if method is not None:
                self._values["method"] = method
            if query_string is not None:
                self._values["query_string"] = query_string
            if single_header is not None:
                self._values["single_header"] = single_header
            if uri_path is not None:
                self._values["uri_path"] = uri_path

        @builtins.property
        def method(self) -> typing.Optional[builtins.str]:
            '''Redacts the HTTP method from WAF logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch.html#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_string(self) -> typing.Optional[builtins.str]:
            '''Redacts the entire query string from WAF logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch.html#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-querystring
            '''
            result = self._values.get("query_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def single_header(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.SingleHeaderProperty"]]:
            '''Redacts a specific header field by name from WAF logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch.html#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-singleheader
            '''
            result = self._values.get("single_header")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.SingleHeaderProperty"]], result)

        @builtins.property
        def uri_path(self) -> typing.Optional[builtins.str]:
            '''Redacts the URI path from WAF logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-fieldtomatch.html#cfn-observabilityadmin-organizationtelemetryrule-fieldtomatch-uripath
            '''
            result = self._values.get("uri_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "behavior": "behavior",
            "conditions": "conditions",
            "requirement": "requirement",
        },
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            behavior: typing.Optional[builtins.str] = None,
            conditions: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.ConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            requirement: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A single filter condition that specifies behavior, requirement, and matching conditions for WAF log records.

            :param behavior: The action to take for log records matching this filter (KEEP or DROP).
            :param conditions: The list of conditions that determine if a log record matches this filter.
            :param requirement: Whether the log record must meet all conditions (MEETS_ALL) or any condition (MEETS_ANY) to match this filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                filter_property = observabilityadmin.CfnOrganizationTelemetryRule.FilterProperty(
                    behavior="behavior",
                    conditions=[observabilityadmin.CfnOrganizationTelemetryRule.ConditionProperty(
                        action_condition=observabilityadmin.CfnOrganizationTelemetryRule.ActionConditionProperty(
                            action="action"
                        ),
                        label_name_condition=observabilityadmin.CfnOrganizationTelemetryRule.LabelNameConditionProperty(
                            label_name="labelName"
                        )
                    )],
                    requirement="requirement"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__74122cf2cd3a4de6fe59f3acfea6ea55d497184459a9d73d02526969478c6d70)
                check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
                check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
                check_type(argname="argument requirement", value=requirement, expected_type=type_hints["requirement"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if behavior is not None:
                self._values["behavior"] = behavior
            if conditions is not None:
                self._values["conditions"] = conditions
            if requirement is not None:
                self._values["requirement"] = requirement

        @builtins.property
        def behavior(self) -> typing.Optional[builtins.str]:
            '''The action to take for log records matching this filter (KEEP or DROP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-filter.html#cfn-observabilityadmin-organizationtelemetryrule-filter-behavior
            '''
            result = self._values.get("behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def conditions(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.ConditionProperty"]]]]:
            '''The list of conditions that determine if a log record matches this filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-filter.html#cfn-observabilityadmin-organizationtelemetryrule-filter-conditions
            '''
            result = self._values.get("conditions")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.ConditionProperty"]]]], result)

        @builtins.property
        def requirement(self) -> typing.Optional[builtins.str]:
            '''Whether the log record must meet all conditions (MEETS_ALL) or any condition (MEETS_ANY) to match this filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-filter.html#cfn-observabilityadmin-organizationtelemetryrule-filter-requirement
            '''
            result = self._values.get("requirement")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.LabelNameConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"label_name": "labelName"},
    )
    class LabelNameConditionProperty:
        def __init__(self, *, label_name: typing.Optional[builtins.str] = None) -> None:
            '''Condition that matches based on WAF rule labels, with label names limited to 1024 characters.

            :param label_name: The label name to match, supporting alphanumeric characters, underscores, hyphens, and colons.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-labelnamecondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                label_name_condition_property = observabilityadmin.CfnOrganizationTelemetryRule.LabelNameConditionProperty(
                    label_name="labelName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1e1cb85478af2a0db2ff4e2c1201fbe45401829631a994c0a6593451b59b5c80)
                check_type(argname="argument label_name", value=label_name, expected_type=type_hints["label_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if label_name is not None:
                self._values["label_name"] = label_name

        @builtins.property
        def label_name(self) -> typing.Optional[builtins.str]:
            '''The label name to match, supporting alphanumeric characters, underscores, hyphens, and colons.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-labelnamecondition.html#cfn-observabilityadmin-organizationtelemetryrule-labelnamecondition-labelname
            '''
            result = self._values.get("label_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelNameConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.LoggingFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"default_behavior": "defaultBehavior", "filters": "filters"},
    )
    class LoggingFilterProperty:
        def __init__(
            self,
            *,
            default_behavior: typing.Optional[builtins.str] = None,
            filters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.FilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration that determines which WAF log records to keep or drop based on specified conditions.

            :param default_behavior: The default action (KEEP or DROP) for log records that don't match any filter conditions.
            :param filters: A list of filter conditions that determine log record handling behavior.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-loggingfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                logging_filter_property = observabilityadmin.CfnOrganizationTelemetryRule.LoggingFilterProperty(
                    default_behavior="defaultBehavior",
                    filters=[observabilityadmin.CfnOrganizationTelemetryRule.FilterProperty(
                        behavior="behavior",
                        conditions=[observabilityadmin.CfnOrganizationTelemetryRule.ConditionProperty(
                            action_condition=observabilityadmin.CfnOrganizationTelemetryRule.ActionConditionProperty(
                                action="action"
                            ),
                            label_name_condition=observabilityadmin.CfnOrganizationTelemetryRule.LabelNameConditionProperty(
                                label_name="labelName"
                            )
                        )],
                        requirement="requirement"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0a6ecd2133b0bae7130114f115e61eb5e98343b8c136ecade19918d01b854904)
                check_type(argname="argument default_behavior", value=default_behavior, expected_type=type_hints["default_behavior"])
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if default_behavior is not None:
                self._values["default_behavior"] = default_behavior
            if filters is not None:
                self._values["filters"] = filters

        @builtins.property
        def default_behavior(self) -> typing.Optional[builtins.str]:
            '''The default action (KEEP or DROP) for log records that don't match any filter conditions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-loggingfilter.html#cfn-observabilityadmin-organizationtelemetryrule-loggingfilter-defaultbehavior
            '''
            result = self._values.get("default_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def filters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.FilterProperty"]]]]:
            '''A list of filter conditions that determine log record handling behavior.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-loggingfilter.html#cfn-observabilityadmin-organizationtelemetryrule-loggingfilter-filters
            '''
            result = self._values.get("filters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.FilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.SingleHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class SingleHeaderProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''Structure containing a name field limited to 64 characters for header or query parameter identification.

            :param name: The name value, limited to 64 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-singleheader.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                single_header_property = observabilityadmin.CfnOrganizationTelemetryRule.SingleHeaderProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__32eaac1f45f8f639979d1f81a515778d4b95e9e651411f27f6a838b958d2ac3d)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name value, limited to 64 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-singleheader.html#cfn-observabilityadmin-organizationtelemetryrule-singleheader-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SingleHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloudtrail_parameters": "cloudtrailParameters",
            "destination_pattern": "destinationPattern",
            "destination_type": "destinationType",
            "elb_load_balancer_logging_parameters": "elbLoadBalancerLoggingParameters",
            "retention_in_days": "retentionInDays",
            "vpc_flow_log_parameters": "vpcFlowLogParameters",
            "waf_logging_parameters": "wafLoggingParameters",
        },
    )
    class TelemetryDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            cloudtrail_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.CloudtrailParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            destination_pattern: typing.Optional[builtins.str] = None,
            destination_type: typing.Optional[builtins.str] = None,
            elb_load_balancer_logging_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.ELBLoadBalancerLoggingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retention_in_days: typing.Optional[jsii.Number] = None,
            vpc_flow_log_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            waf_logging_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.WAFLoggingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration specifying where and how telemetry data should be delivered for AWS resources.

            :param cloudtrail_parameters: Configuration parameters specific to AWS CloudTrail when CloudTrail is the source type.
            :param destination_pattern: The pattern used to generate the destination path or name, supporting macros like and .
            :param destination_type: The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3").
            :param elb_load_balancer_logging_parameters: Configuration parameters specific to ELB load balancer logging when ELB is the resource type.
            :param retention_in_days: The number of days to retain the telemetry data in the destination.
            :param vpc_flow_log_parameters: Configuration parameters specific to VPC Flow Logs when VPC is the resource type.
            :param waf_logging_parameters: Configuration parameters specific to WAF logging when WAF is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_destination_configuration_property = observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                    cloudtrail_parameters=observabilityadmin.CfnOrganizationTelemetryRule.CloudtrailParametersProperty(
                        advanced_event_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty(
                            field_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty(
                                ends_with=["endsWith"],
                                equal_to=["equalTo"],
                                field="field",
                                not_ends_with=["notEndsWith"],
                                not_equals=["notEquals"],
                                not_starts_with=["notStartsWith"],
                                starts_with=["startsWith"]
                            )],
                
                            # the properties below are optional
                            name="name"
                        )]
                    ),
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    elb_load_balancer_logging_parameters=observabilityadmin.CfnOrganizationTelemetryRule.ELBLoadBalancerLoggingParametersProperty(
                        field_delimiter="fieldDelimiter",
                        output_format="outputFormat"
                    ),
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    ),
                    waf_logging_parameters=observabilityadmin.CfnOrganizationTelemetryRule.WAFLoggingParametersProperty(
                        logging_filter=observabilityadmin.CfnOrganizationTelemetryRule.LoggingFilterProperty(
                            default_behavior="defaultBehavior",
                            filters=[observabilityadmin.CfnOrganizationTelemetryRule.FilterProperty(
                                behavior="behavior",
                                conditions=[observabilityadmin.CfnOrganizationTelemetryRule.ConditionProperty(
                                    action_condition=observabilityadmin.CfnOrganizationTelemetryRule.ActionConditionProperty(
                                        action="action"
                                    ),
                                    label_name_condition=observabilityadmin.CfnOrganizationTelemetryRule.LabelNameConditionProperty(
                                        label_name="labelName"
                                    )
                                )],
                                requirement="requirement"
                            )]
                        ),
                        log_type="logType",
                        redacted_fields=[observabilityadmin.CfnOrganizationTelemetryRule.FieldToMatchProperty(
                            method="method",
                            query_string="queryString",
                            single_header=observabilityadmin.CfnOrganizationTelemetryRule.SingleHeaderProperty(
                                name="name"
                            ),
                            uri_path="uriPath"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36b4168c57b4555036ca598e8299a36985c9aab7a1eb6b84357df4454b340171)
                check_type(argname="argument cloudtrail_parameters", value=cloudtrail_parameters, expected_type=type_hints["cloudtrail_parameters"])
                check_type(argname="argument destination_pattern", value=destination_pattern, expected_type=type_hints["destination_pattern"])
                check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
                check_type(argname="argument elb_load_balancer_logging_parameters", value=elb_load_balancer_logging_parameters, expected_type=type_hints["elb_load_balancer_logging_parameters"])
                check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
                check_type(argname="argument vpc_flow_log_parameters", value=vpc_flow_log_parameters, expected_type=type_hints["vpc_flow_log_parameters"])
                check_type(argname="argument waf_logging_parameters", value=waf_logging_parameters, expected_type=type_hints["waf_logging_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloudtrail_parameters is not None:
                self._values["cloudtrail_parameters"] = cloudtrail_parameters
            if destination_pattern is not None:
                self._values["destination_pattern"] = destination_pattern
            if destination_type is not None:
                self._values["destination_type"] = destination_type
            if elb_load_balancer_logging_parameters is not None:
                self._values["elb_load_balancer_logging_parameters"] = elb_load_balancer_logging_parameters
            if retention_in_days is not None:
                self._values["retention_in_days"] = retention_in_days
            if vpc_flow_log_parameters is not None:
                self._values["vpc_flow_log_parameters"] = vpc_flow_log_parameters
            if waf_logging_parameters is not None:
                self._values["waf_logging_parameters"] = waf_logging_parameters

        @builtins.property
        def cloudtrail_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.CloudtrailParametersProperty"]]:
            '''Configuration parameters specific to AWS CloudTrail when CloudTrail is the source type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-cloudtrailparameters
            '''
            result = self._values.get("cloudtrail_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.CloudtrailParametersProperty"]], result)

        @builtins.property
        def destination_pattern(self) -> typing.Optional[builtins.str]:
            '''The pattern used to generate the destination path or name, supporting macros like  and .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-destinationpattern
            '''
            result = self._values.get("destination_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_type(self) -> typing.Optional[builtins.str]:
            '''The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3").

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-destinationtype
            '''
            result = self._values.get("destination_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def elb_load_balancer_logging_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.ELBLoadBalancerLoggingParametersProperty"]]:
            '''Configuration parameters specific to ELB load balancer logging when ELB is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-elbloadbalancerloggingparameters
            '''
            result = self._values.get("elb_load_balancer_logging_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.ELBLoadBalancerLoggingParametersProperty"]], result)

        @builtins.property
        def retention_in_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days to retain the telemetry data in the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-retentionindays
            '''
            result = self._values.get("retention_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def vpc_flow_log_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty"]]:
            '''Configuration parameters specific to VPC Flow Logs when VPC is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-vpcflowlogparameters
            '''
            result = self._values.get("vpc_flow_log_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty"]], result)

        @builtins.property
        def waf_logging_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.WAFLoggingParametersProperty"]]:
            '''Configuration parameters specific to WAF logging when WAF is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-organizationtelemetryrule-telemetrydestinationconfiguration-wafloggingparameters
            '''
            result = self._values.get("waf_logging_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.WAFLoggingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_type": "resourceType",
            "telemetry_type": "telemetryType",
            "destination_configuration": "destinationConfiguration",
            "scope": "scope",
            "selection_criteria": "selectionCriteria",
            "telemetry_source_types": "telemetrySourceTypes",
        },
    )
    class TelemetryRuleProperty:
        def __init__(
            self,
            *,
            resource_type: builtins.str,
            telemetry_type: builtins.str,
            destination_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scope: typing.Optional[builtins.str] = None,
            selection_criteria: typing.Optional[builtins.str] = None,
            telemetry_source_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Defines how telemetry should be configured for specific AWS resources.

            :param resource_type: The type of AWS resource to configure telemetry for (e.g., "AWS::EC2::VPC", "AWS::EKS::Cluster", "AWS::WAFv2::WebACL").
            :param telemetry_type: The type of telemetry to collect (Logs, Metrics, or Traces).
            :param destination_configuration: Configuration specifying where and how the telemetry data should be delivered.
            :param scope: The organizational scope to which the rule applies, specified using accounts or organizational units.
            :param selection_criteria: Criteria for selecting which resources the rule applies to, such as resource tags.
            :param telemetry_source_types: The specific telemetry source types to configure for the resource, such as VPC_FLOW_LOGS or EKS_AUDIT_LOGS. TelemetrySourceTypes must be correlated with the specific resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_rule_property = observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
                
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                        cloudtrail_parameters=observabilityadmin.CfnOrganizationTelemetryRule.CloudtrailParametersProperty(
                            advanced_event_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty(
                                field_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty(
                                    ends_with=["endsWith"],
                                    equal_to=["equalTo"],
                                    field="field",
                                    not_ends_with=["notEndsWith"],
                                    not_equals=["notEquals"],
                                    not_starts_with=["notStartsWith"],
                                    starts_with=["startsWith"]
                                )],
                
                                # the properties below are optional
                                name="name"
                            )]
                        ),
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        elb_load_balancer_logging_parameters=observabilityadmin.CfnOrganizationTelemetryRule.ELBLoadBalancerLoggingParametersProperty(
                            field_delimiter="fieldDelimiter",
                            output_format="outputFormat"
                        ),
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        ),
                        waf_logging_parameters=observabilityadmin.CfnOrganizationTelemetryRule.WAFLoggingParametersProperty(
                            logging_filter=observabilityadmin.CfnOrganizationTelemetryRule.LoggingFilterProperty(
                                default_behavior="defaultBehavior",
                                filters=[observabilityadmin.CfnOrganizationTelemetryRule.FilterProperty(
                                    behavior="behavior",
                                    conditions=[observabilityadmin.CfnOrganizationTelemetryRule.ConditionProperty(
                                        action_condition=observabilityadmin.CfnOrganizationTelemetryRule.ActionConditionProperty(
                                            action="action"
                                        ),
                                        label_name_condition=observabilityadmin.CfnOrganizationTelemetryRule.LabelNameConditionProperty(
                                            label_name="labelName"
                                        )
                                    )],
                                    requirement="requirement"
                                )]
                            ),
                            log_type="logType",
                            redacted_fields=[observabilityadmin.CfnOrganizationTelemetryRule.FieldToMatchProperty(
                                method="method",
                                query_string="queryString",
                                single_header=observabilityadmin.CfnOrganizationTelemetryRule.SingleHeaderProperty(
                                    name="name"
                                ),
                                uri_path="uriPath"
                            )]
                        )
                    ),
                    scope="scope",
                    selection_criteria="selectionCriteria",
                    telemetry_source_types=["telemetrySourceTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8febf24ebcbc00029972152d874df5e847a9f5cd45e05abb26e69f7a2cabc5bf)
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument telemetry_type", value=telemetry_type, expected_type=type_hints["telemetry_type"])
                check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
                check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
                check_type(argname="argument selection_criteria", value=selection_criteria, expected_type=type_hints["selection_criteria"])
                check_type(argname="argument telemetry_source_types", value=telemetry_source_types, expected_type=type_hints["telemetry_source_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_type": resource_type,
                "telemetry_type": telemetry_type,
            }
            if destination_configuration is not None:
                self._values["destination_configuration"] = destination_configuration
            if scope is not None:
                self._values["scope"] = scope
            if selection_criteria is not None:
                self._values["selection_criteria"] = selection_criteria
            if telemetry_source_types is not None:
                self._values["telemetry_source_types"] = telemetry_source_types

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''The type of AWS resource to configure telemetry for (e.g., "AWS::EC2::VPC", "AWS::EKS::Cluster", "AWS::WAFv2::WebACL").

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def telemetry_type(self) -> builtins.str:
            '''The type of telemetry to collect (Logs, Metrics, or Traces).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-telemetrytype
            '''
            result = self._values.get("telemetry_type")
            assert result is not None, "Required property 'telemetry_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty"]]:
            '''Configuration specifying where and how the telemetry data should be delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-destinationconfiguration
            '''
            result = self._values.get("destination_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty"]], result)

        @builtins.property
        def scope(self) -> typing.Optional[builtins.str]:
            '''The organizational scope to which the rule applies, specified using accounts or organizational units.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-scope
            '''
            result = self._values.get("scope")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def selection_criteria(self) -> typing.Optional[builtins.str]:
            '''Criteria for selecting which resources the rule applies to, such as resource tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-selectioncriteria
            '''
            result = self._values.get("selection_criteria")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def telemetry_source_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The specific telemetry source types to configure for the resource, such as VPC_FLOW_LOGS or EKS_AUDIT_LOGS.

            TelemetrySourceTypes must be correlated with the specific resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-telemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-telemetryrule-telemetrysourcetypes
            '''
            result = self._values.get("telemetry_source_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_format": "logFormat",
            "max_aggregation_interval": "maxAggregationInterval",
            "traffic_type": "trafficType",
        },
    )
    class VPCFlowLogParametersProperty:
        def __init__(
            self,
            *,
            log_format: typing.Optional[builtins.str] = None,
            max_aggregation_interval: typing.Optional[jsii.Number] = None,
            traffic_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration parameters specific to VPC Flow Logs.

            :param log_format: The format in which VPC Flow Log entries should be logged.
            :param max_aggregation_interval: The maximum interval in seconds between the capture of flow log records.
            :param traffic_type: The type of traffic to log (ACCEPT, REJECT, or ALL).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                v_pCFlow_log_parameters_property = observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                    log_format="logFormat",
                    max_aggregation_interval=123,
                    traffic_type="trafficType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__945b01222f6573dfd9bd365335b34de4d056db844b2fe9ffa6c9d40371eaff6e)
                check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
                check_type(argname="argument max_aggregation_interval", value=max_aggregation_interval, expected_type=type_hints["max_aggregation_interval"])
                check_type(argname="argument traffic_type", value=traffic_type, expected_type=type_hints["traffic_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_format is not None:
                self._values["log_format"] = log_format
            if max_aggregation_interval is not None:
                self._values["max_aggregation_interval"] = max_aggregation_interval
            if traffic_type is not None:
                self._values["traffic_type"] = traffic_type

        @builtins.property
        def log_format(self) -> typing.Optional[builtins.str]:
            '''The format in which VPC Flow Log entries should be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-logformat
            '''
            result = self._values.get("log_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_aggregation_interval(self) -> typing.Optional[jsii.Number]:
            '''The maximum interval in seconds between the capture of flow log records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-maxaggregationinterval
            '''
            result = self._values.get("max_aggregation_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def traffic_type(self) -> typing.Optional[builtins.str]:
            '''The type of traffic to log (ACCEPT, REJECT, or ALL).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-organizationtelemetryrule-vpcflowlogparameters-traffictype
            '''
            result = self._values.get("traffic_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCFlowLogParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRule.WAFLoggingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "logging_filter": "loggingFilter",
            "log_type": "logType",
            "redacted_fields": "redactedFields",
        },
    )
    class WAFLoggingParametersProperty:
        def __init__(
            self,
            *,
            logging_filter: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.LoggingFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            log_type: typing.Optional[builtins.str] = None,
            redacted_fields: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.FieldToMatchProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration parameters for WAF logging, including redacted fields and logging filters.

            :param logging_filter: A filter configuration that determines which WAF log records to include or exclude.
            :param log_type: The type of WAF logs to collect (currently supports WAF_LOGS).
            :param redacted_fields: The fields to redact from WAF logs to protect sensitive information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-wafloggingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                w_aFLogging_parameters_property = observabilityadmin.CfnOrganizationTelemetryRule.WAFLoggingParametersProperty(
                    logging_filter=observabilityadmin.CfnOrganizationTelemetryRule.LoggingFilterProperty(
                        default_behavior="defaultBehavior",
                        filters=[observabilityadmin.CfnOrganizationTelemetryRule.FilterProperty(
                            behavior="behavior",
                            conditions=[observabilityadmin.CfnOrganizationTelemetryRule.ConditionProperty(
                                action_condition=observabilityadmin.CfnOrganizationTelemetryRule.ActionConditionProperty(
                                    action="action"
                                ),
                                label_name_condition=observabilityadmin.CfnOrganizationTelemetryRule.LabelNameConditionProperty(
                                    label_name="labelName"
                                )
                            )],
                            requirement="requirement"
                        )]
                    ),
                    log_type="logType",
                    redacted_fields=[observabilityadmin.CfnOrganizationTelemetryRule.FieldToMatchProperty(
                        method="method",
                        query_string="queryString",
                        single_header=observabilityadmin.CfnOrganizationTelemetryRule.SingleHeaderProperty(
                            name="name"
                        ),
                        uri_path="uriPath"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__170d7139909f3f9728055df526e99eee9f0d1bbb7e2ffd7d9636e18c28848f0b)
                check_type(argname="argument logging_filter", value=logging_filter, expected_type=type_hints["logging_filter"])
                check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
                check_type(argname="argument redacted_fields", value=redacted_fields, expected_type=type_hints["redacted_fields"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if logging_filter is not None:
                self._values["logging_filter"] = logging_filter
            if log_type is not None:
                self._values["log_type"] = log_type
            if redacted_fields is not None:
                self._values["redacted_fields"] = redacted_fields

        @builtins.property
        def logging_filter(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.LoggingFilterProperty"]]:
            '''A filter configuration that determines which WAF log records to include or exclude.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-wafloggingparameters.html#cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-loggingfilter
            '''
            result = self._values.get("logging_filter")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.LoggingFilterProperty"]], result)

        @builtins.property
        def log_type(self) -> typing.Optional[builtins.str]:
            '''The type of WAF logs to collect (currently supports WAF_LOGS).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-wafloggingparameters.html#cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-logtype
            '''
            result = self._values.get("log_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def redacted_fields(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.FieldToMatchProperty"]]]]:
            '''The fields to redact from WAF logs to protect sensitive information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-organizationtelemetryrule-wafloggingparameters.html#cfn-observabilityadmin-organizationtelemetryrule-wafloggingparameters-redactedfields
            '''
            result = self._values.get("redacted_fields")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.FieldToMatchProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WAFLoggingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnOrganizationTelemetryRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_name": "ruleName", "tags": "tags"},
)
class CfnOrganizationTelemetryRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnOrganizationTelemetryRule.TelemetryRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOrganizationTelemetryRule``.

        :param rule: The name of the organization telemetry rule.
        :param rule_name: The name of the organization centralization rule.
        :param tags: Lists all tags attached to the specified resource. Supports telemetry rule resources and telemetry pipeline resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            cfn_organization_telemetry_rule_props = observabilityadmin.CfnOrganizationTelemetryRuleProps(
                rule=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
            
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty(
                        cloudtrail_parameters=observabilityadmin.CfnOrganizationTelemetryRule.CloudtrailParametersProperty(
                            advanced_event_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty(
                                field_selectors=[observabilityadmin.CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty(
                                    ends_with=["endsWith"],
                                    equal_to=["equalTo"],
                                    field="field",
                                    not_ends_with=["notEndsWith"],
                                    not_equals=["notEquals"],
                                    not_starts_with=["notStartsWith"],
                                    starts_with=["startsWith"]
                                )],
            
                                # the properties below are optional
                                name="name"
                            )]
                        ),
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        elb_load_balancer_logging_parameters=observabilityadmin.CfnOrganizationTelemetryRule.ELBLoadBalancerLoggingParametersProperty(
                            field_delimiter="fieldDelimiter",
                            output_format="outputFormat"
                        ),
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        ),
                        waf_logging_parameters=observabilityadmin.CfnOrganizationTelemetryRule.WAFLoggingParametersProperty(
                            logging_filter=observabilityadmin.CfnOrganizationTelemetryRule.LoggingFilterProperty(
                                default_behavior="defaultBehavior",
                                filters=[observabilityadmin.CfnOrganizationTelemetryRule.FilterProperty(
                                    behavior="behavior",
                                    conditions=[observabilityadmin.CfnOrganizationTelemetryRule.ConditionProperty(
                                        action_condition=observabilityadmin.CfnOrganizationTelemetryRule.ActionConditionProperty(
                                            action="action"
                                        ),
                                        label_name_condition=observabilityadmin.CfnOrganizationTelemetryRule.LabelNameConditionProperty(
                                            label_name="labelName"
                                        )
                                    )],
                                    requirement="requirement"
                                )]
                            ),
                            log_type="logType",
                            redacted_fields=[observabilityadmin.CfnOrganizationTelemetryRule.FieldToMatchProperty(
                                method="method",
                                query_string="queryString",
                                single_header=observabilityadmin.CfnOrganizationTelemetryRule.SingleHeaderProperty(
                                    name="name"
                                ),
                                uri_path="uriPath"
                            )]
                        )
                    ),
                    scope="scope",
                    selection_criteria="selectionCriteria",
                    telemetry_source_types=["telemetrySourceTypes"]
                ),
                rule_name="ruleName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45c94381428dd096d5bd5b31c1a78b0ec6c66b125c46a889f389e957dbf9f76b)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
            "rule_name": rule_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.TelemetryRuleProperty"]:
        '''The name of the organization telemetry rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnOrganizationTelemetryRule.TelemetryRuleProperty"], result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the organization centralization rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-rulename
        '''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Lists all tags attached to the specified resource.

        Supports telemetry rule resources and telemetry pipeline resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-organizationtelemetryrule.html#cfn-observabilityadmin-organizationtelemetryrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationTelemetryRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _IS3TableIntegrationRef_0d27be71, _ITaggableV2_4e6798f8)
class CfnS3TableIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnS3TableIntegration",
):
    '''Creates an integration between CloudWatch and S3 Tables for analytics.

    This integration enables querying CloudWatch telemetry data using analytics engines like Amazon Athena, Amazon Redshift, and Apache Spark.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-s3tableintegration.html
    :cloudformationResource: AWS::ObservabilityAdmin::S3TableIntegration
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_observabilityadmin as observabilityadmin
        
        cfn_s3_table_integration = observabilityadmin.CfnS3TableIntegration(self, "MyCfnS3TableIntegration",
            encryption=observabilityadmin.CfnS3TableIntegration.EncryptionConfigProperty(
                sse_algorithm="sseAlgorithm",
        
                # the properties below are optional
                kms_key_arn="kmsKeyArn"
            ),
            role_arn="roleArn",
        
            # the properties below are optional
            log_sources=[observabilityadmin.CfnS3TableIntegration.LogSourceProperty(
                name="name",
                type="type",
        
                # the properties below are optional
                identifier="identifier"
            )],
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
        encryption: typing.Union["_IResolvable_da3f097b", typing.Union["CfnS3TableIntegration.EncryptionConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        log_sources: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnS3TableIntegration.LogSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ObservabilityAdmin::S3TableIntegration``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param encryption: Defines the encryption configuration for S3 Table integrations, including the encryption algorithm and KMS key settings.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role that grants permissions for the S3 Table integration to access necessary resources.
        :param log_sources: A data source with an S3 Table integration for query access in the ``logs`` namespace.
        :param tags: The key-value pairs to associate with the S3 Table integration resource for categorization and management purposes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e613f2b4c0bd0fe05183ae10e1072f669e68ecf8da1370aa25246cc8572b5e2f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnS3TableIntegrationProps(
            encryption=encryption,
            role_arn=role_arn,
            log_sources=log_sources,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForS3TableIntegration")
    @builtins.classmethod
    def arn_for_s3_table_integration(
        cls,
        resource: "_IS3TableIntegrationRef_0d27be71",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de0e786e830272a9cd43196ab4d988d850d39e09ac6deece3f6f3fc217267fc9)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForS3TableIntegration", [resource]))

    @jsii.member(jsii_name="isCfnS3TableIntegration")
    @builtins.classmethod
    def is_cfn_s3_table_integration(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnS3TableIntegration.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f060eb6521743a2fee36ac86bf0a3ec88f3659183452e5bc1ed20405e82d070)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnS3TableIntegration", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db8d8b6fa8e1af24ec5902bc335bccad34c4c808d7ce93702198c675306c9490)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b1915c865e4c74d8cf78a70268ef686e156945564d8c734eae1c805be7b1dcca)
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
        '''The Amazon Resource Name (ARN) of the S3 Table integration.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="s3TableIntegrationRef")
    def s3_table_integration_ref(self) -> "_S3TableIntegrationReference_5391966c":
        '''A reference to a S3TableIntegration resource.'''
        return typing.cast("_S3TableIntegrationReference_5391966c", jsii.get(self, "s3TableIntegrationRef"))

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnS3TableIntegration.EncryptionConfigProperty"]:
        '''Defines the encryption configuration for S3 Table integrations, including the encryption algorithm and KMS key settings.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnS3TableIntegration.EncryptionConfigProperty"], jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnS3TableIntegration.EncryptionConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf60cf475e52ec2455d6bb2610fe113c13df025036010f81e85a0d6a8a9568df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants permissions for the S3 Table integration to access necessary resources.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9563b76b32841a10a2062025b5dc3f2c3e65ffaf4e26519dd2e2939d724590b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="logSources")
    def log_sources(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnS3TableIntegration.LogSourceProperty"]]]]:
        '''A data source with an S3 Table integration for query access in the ``logs`` namespace.'''
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnS3TableIntegration.LogSourceProperty"]]]], jsii.get(self, "logSources"))

    @log_sources.setter
    def log_sources(
        self,
        value: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnS3TableIntegration.LogSourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca350dbe6386e8726b94ecfb8ecdcec3eadaea66fddf8e9ace5f7364958e217a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logSources", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The key-value pairs to associate with the S3 Table integration resource for categorization and management purposes.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8d9af1b518d9d7c5df43afc2d1661b0c7f8c2f6e31ea999f0f18044da32c60a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnS3TableIntegration.EncryptionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"sse_algorithm": "sseAlgorithm", "kms_key_arn": "kmsKeyArn"},
    )
    class EncryptionConfigProperty:
        def __init__(
            self,
            *,
            sse_algorithm: builtins.str,
            kms_key_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Defines the encryption configuration for S3 Table integrations, including the encryption algorithm and KMS key settings.

            :param sse_algorithm: The server-side encryption algorithm used for encrypting data in the S3 Table integration.
            :param kms_key_arn: The Amazon Resource Name (ARN) of the KMS key used for encryption when using customer-managed keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-s3tableintegration-encryptionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                encryption_config_property = observabilityadmin.CfnS3TableIntegration.EncryptionConfigProperty(
                    sse_algorithm="sseAlgorithm",
                
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__08cffef92f415425c011859c528aa6887003c25fca6427c36632c3e7f6effd76)
                check_type(argname="argument sse_algorithm", value=sse_algorithm, expected_type=type_hints["sse_algorithm"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sse_algorithm": sse_algorithm,
            }
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn

        @builtins.property
        def sse_algorithm(self) -> builtins.str:
            '''The server-side encryption algorithm used for encrypting data in the S3 Table integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-s3tableintegration-encryptionconfig.html#cfn-observabilityadmin-s3tableintegration-encryptionconfig-ssealgorithm
            '''
            result = self._values.get("sse_algorithm")
            assert result is not None, "Required property 'sse_algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the KMS key used for encryption when using customer-managed keys.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-s3tableintegration-encryptionconfig.html#cfn-observabilityadmin-s3tableintegration-encryptionconfig-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnS3TableIntegration.LogSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "type": "type", "identifier": "identifier"},
    )
    class LogSourceProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            type: builtins.str,
            identifier: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A data source with an S3 Table integration for query access in the ``logs`` namespace.

            :param name: The name of the data source.
            :param type: The type of the data source.
            :param identifier: The unique identifier for the association between the data source and S3 Table integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-s3tableintegration-logsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                log_source_property = observabilityadmin.CfnS3TableIntegration.LogSourceProperty(
                    name="name",
                    type="type",
                
                    # the properties below are optional
                    identifier="identifier"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b66342dc0f7b0ba6d95ddc850e30226765bf042a0bf8a8471a04ad534920ea96)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "type": type,
            }
            if identifier is not None:
                self._values["identifier"] = identifier

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-s3tableintegration-logsource.html#cfn-observabilityadmin-s3tableintegration-logsource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the data source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-s3tableintegration-logsource.html#cfn-observabilityadmin-s3tableintegration-logsource-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def identifier(self) -> typing.Optional[builtins.str]:
            '''The unique identifier for the association between the data source and S3 Table integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-s3tableintegration-logsource.html#cfn-observabilityadmin-s3tableintegration-logsource-identifier
            '''
            result = self._values.get("identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnS3TableIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "encryption": "encryption",
        "role_arn": "roleArn",
        "log_sources": "logSources",
        "tags": "tags",
    },
)
class CfnS3TableIntegrationProps:
    def __init__(
        self,
        *,
        encryption: typing.Union["_IResolvable_da3f097b", typing.Union["CfnS3TableIntegration.EncryptionConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        role_arn: builtins.str,
        log_sources: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnS3TableIntegration.LogSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnS3TableIntegration``.

        :param encryption: Defines the encryption configuration for S3 Table integrations, including the encryption algorithm and KMS key settings.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role that grants permissions for the S3 Table integration to access necessary resources.
        :param log_sources: A data source with an S3 Table integration for query access in the ``logs`` namespace.
        :param tags: The key-value pairs to associate with the S3 Table integration resource for categorization and management purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-s3tableintegration.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            cfn_s3_table_integration_props = observabilityadmin.CfnS3TableIntegrationProps(
                encryption=observabilityadmin.CfnS3TableIntegration.EncryptionConfigProperty(
                    sse_algorithm="sseAlgorithm",
            
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn"
                ),
                role_arn="roleArn",
            
                # the properties below are optional
                log_sources=[observabilityadmin.CfnS3TableIntegration.LogSourceProperty(
                    name="name",
                    type="type",
            
                    # the properties below are optional
                    identifier="identifier"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__595e24a51b54bcce8c75e459e7e3581741d212973d102f13a7b1f8c21e64c7c6)
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument log_sources", value=log_sources, expected_type=type_hints["log_sources"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "encryption": encryption,
            "role_arn": role_arn,
        }
        if log_sources is not None:
            self._values["log_sources"] = log_sources
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def encryption(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnS3TableIntegration.EncryptionConfigProperty"]:
        '''Defines the encryption configuration for S3 Table integrations, including the encryption algorithm and KMS key settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-s3tableintegration.html#cfn-observabilityadmin-s3tableintegration-encryption
        '''
        result = self._values.get("encryption")
        assert result is not None, "Required property 'encryption' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnS3TableIntegration.EncryptionConfigProperty"], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role that grants permissions for the S3 Table integration to access necessary resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-s3tableintegration.html#cfn-observabilityadmin-s3tableintegration-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_sources(
        self,
    ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnS3TableIntegration.LogSourceProperty"]]]]:
        '''A data source with an S3 Table integration for query access in the ``logs`` namespace.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-s3tableintegration.html#cfn-observabilityadmin-s3tableintegration-logsources
        '''
        result = self._values.get("log_sources")
        return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnS3TableIntegration.LogSourceProperty"]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The key-value pairs to associate with the S3 Table integration resource for categorization and management purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-s3tableintegration.html#cfn-observabilityadmin-s3tableintegration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnS3TableIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITelemetryPipelinesRef_a5d8576e, _ITaggableV2_4e6798f8)
class CfnTelemetryPipelines(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryPipelines",
):
    '''Creates a telemetry pipeline for processing and transforming telemetry data.

    The pipeline defines how data flows from sources through processors to destinations, enabling data transformation and delivering capabilities.

    **Using CloudWatch as a pipeline source** The following is an example of a ``Body`` property value for the ``Configuration`` object. { "Type": "AWS::ObservabilityAdmin::TelemetryPipelines", "Properties": { "Configuration": { "Body": "pipeline:\\n source:\\n cloudwatch_logs:\\n log_event_metadata:\\n data_source_name: "my_data_source"\\n data_source_type: "default"\\n aws:\\n sts_role_arn: "arn:aws:iam::123456789012:role/MyPipelineAccessRole"\\n processor:\\n - parse_json: {}\\n sink:\\n - cloudwatch_logs:\\n log_group: "@original"" } }
    } Type: AWS::ObservabilityAdmin::TelemetryPipelines
    Properties: Configuration: Body: | pipeline: source: cloudwatch_logs: log_event_metadata: data_source_name: "my_data_source" data_source_type: "default" aws: sts_role_arn: "arn:aws:iam::123456789012:role/MyPipelineAccessRole" processor: - parse_json: {} sink: - cloudwatch_logs: log_group: "@original" **Using Amazon S3 as a pipeline source** The following is an example of a ``Body`` property value for the ``Configuration`` object. { "Type": "AWS::ObservabilityAdmin::TelemetryPipelines", "Properties": { "Configuration": { "Body": "pipeline:\\n source:\\n s3:\\n sqs:\\n visibility_timeout: "PT60S"\\n visibility_duplication_protection: true\\n maximum_messages: 10\\n queue_url: "https://sqs.us-east-1.amazonaws.com/123456789012/my-sqs-queue"\\n notification_type: "sqs"\\n codec:\\n ndjson: {}\\n aws:\\n region: "us-east-1"\\n sts_role_arn: "arn:aws:iam::123456789012:role/MyAccessRole"\\n data_source_name: "crowdstrike_falcon"\\n processor:\\n - ocsf:\\n version: "1.5"\\n mapping_version: "1.5.0"\\n schema:\\n crowdstrike_falcon:\\n sink:\\n - cloudwatch_logs:\\n log_group: "my-log-group"" } }
    } Type: AWS::ObservabilityAdmin::TelemetryPipelines
    Properties: Configuration: Body: | pipeline: source: s3: sqs: visibility_timeout: "PT60S" visibility_duplication_protection: true maximum_messages: 10 queue_url: "https://sqs.us-east-1.amazonaws.com/123456789012/my-sqs-queue" notification_type: "sqs" codec: ndjson: {} aws: region: "us-east-1" sts_role_arn: "arn:aws:iam::123456789012:role/MyAccessRole" data_source_name: "crowdstrike_falcon" processor: - ocsf: version: "1.5" mapping_version: "1.5.0" schema: crowdstrike_falcon: sink: - cloudwatch_logs: log_group: "my-log-group"

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetrypipelines.html
    :cloudformationResource: AWS::ObservabilityAdmin::TelemetryPipelines
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_observabilityadmin as observabilityadmin
        
        cfn_telemetry_pipelines = observabilityadmin.CfnTelemetryPipelines(self, "MyCfnTelemetryPipelines",
            configuration=observabilityadmin.CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty(
                body="body"
            ),
        
            # the properties below are optional
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
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ObservabilityAdmin::TelemetryPipelines``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: The configuration that defines how the telemetry pipeline processes data, including sources, processors, and destinations. For more information, see the `Amazon CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Creating-pipelines.html>`_ .
        :param name: The name of the telemetry pipeline to create. The name must be unique within your account.
        :param tags: The key-value pairs to associate with the telemetry pipeline resource for categorization and management purposes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f612352088aa915560d9c73b4fc630a10a3f3706939f1998202a1ad9dcaa9b2e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTelemetryPipelinesProps(
            configuration=configuration, name=name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="arnForTelemetryPipelines")
    @builtins.classmethod
    def arn_for_telemetry_pipelines(
        cls,
        resource: "_ITelemetryPipelinesRef_a5d8576e",
    ) -> builtins.str:
        '''
        :param resource: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2734bd526aa4a19a2468ecd3f94c2f174bcdef0f646010e77d960f2aee980e1c)
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "arnForTelemetryPipelines", [resource]))

    @jsii.member(jsii_name="isCfnTelemetryPipelines")
    @builtins.classmethod
    def is_cfn_telemetry_pipelines(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnTelemetryPipelines.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13e724affcae9c67447d564bf1f406f85952620e01688ec9374c2e240d21ce00)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnTelemetryPipelines", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b7b0d3ae71540f27e1eef685497e34fb8fa229fd184e2f79e2601bd982007f4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ef1a0ed45cdf50ec0b96e10e26fffd4fa055a06795675917f6bf670790ac26d)
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
        '''The Amazon Resource Name (ARN) of the created telemetry pipeline.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPipeline")
    def attr_pipeline(self) -> "_IResolvable_da3f097b":
        '''
        :cloudformationAttribute: Pipeline
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrPipeline"))

    @builtins.property
    @jsii.member(jsii_name="attrPipelineIdentifier")
    def attr_pipeline_identifier(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the telemetry pipeline.

        :cloudformationAttribute: PipelineIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPipelineIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the telemetry pipeline.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> "_IResolvable_da3f097b":
        '''
        :cloudformationAttribute: StatusReason
        '''
        return typing.cast("_IResolvable_da3f097b", jsii.get(self, "attrStatusReason"))

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
    @jsii.member(jsii_name="telemetryPipelinesRef")
    def telemetry_pipelines_ref(self) -> "_TelemetryPipelinesReference_c5feae72":
        '''A reference to a TelemetryPipelines resource.'''
        return typing.cast("_TelemetryPipelinesReference_c5feae72", jsii.get(self, "telemetryPipelinesRef"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty"]:
        '''The configuration that defines how the telemetry pipeline processes data, including sources, processors, and destinations.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0ea345d0670a42e8cd1fa5ccce024ab9a78b08ece4b335f587f586aa3446f66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the telemetry pipeline to create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05b27d7721bf16162cc6c8d3ddffb2e5ab5b3582d0e2acfae8e22f54d86e7f56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The key-value pairs to associate with the telemetry pipeline resource for categorization and management purposes.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__481c302f9e6ff7c9111f4e3c3983ac44f104411494a50dcd0e8fbb96b18d733d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"body": "body"},
    )
    class TelemetryPipelineConfigurationProperty:
        def __init__(self, *, body: builtins.str) -> None:
            '''Defines the configuration for a pipeline, including how data flows from sources through processors to destinations.

            The configuration is specified in YAML format and must include a valid pipeline definition with required source and sink components. This pipeline enables end-to-end telemetry data collection, transformation, and delivery while supporting optional processing steps and extensions for enhanced functionality.

            The primary pipeline configuration section are:

            - *Source:* Defines where log data originates from (S3 buckets, CloudWatch Logs, third-party APIs). Each pipeline must have exactly one source.
            - *Processors (optional):* Transform, parse, and enrich log data as it flows through the pipeline. Processors are applied sequentially in the order they are defined.
            - *Sink:* Defines the destination where processed log data is sent. Each pipeline must have exactly one sink.
            - *Extensions (optional):* Provide additional functionality such as AWS Secrets Manager integration for credential management.

            For more details on each configuration section see `CloudWatch pipelines User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-pipelines.html>`_ . Additional comprehensive configuration examples can be found in the `CreateTelemetryPipeline API docs <https://docs.aws.amazon.com/cloudwatch/latest/observabilityadmin/API_CreateTelemetryPipeline.html#API_CreateTelemetryPipeline_Examples>`_ .

            :param body: The pipeline configuration body that defines the data processing rules and transformations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_pipeline_configuration_property = observabilityadmin.CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty(
                    body="body"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9bb4b947dbc757a669388b15cdcb2ebb178c00d3708260a46724a325f1525920)
                check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "body": body,
            }

        @builtins.property
        def body(self) -> builtins.str:
            '''The pipeline configuration body that defines the data processing rules and transformations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration.html#cfn-observabilityadmin-telemetrypipelines-telemetrypipelineconfiguration-body
            '''
            result = self._values.get("body")
            assert result is not None, "Required property 'body' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryPipelineConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryPipelines.TelemetryPipelineProperty",
        jsii_struct_bases=[],
        name_mapping={
            "arn": "arn",
            "configuration": "configuration",
            "created_time_stamp": "createdTimeStamp",
            "last_update_time_stamp": "lastUpdateTimeStamp",
            "name": "name",
            "status": "status",
            "status_reason": "statusReason",
            "tags": "tags",
        },
    )
    class TelemetryPipelineProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            created_time_stamp: typing.Optional[jsii.Number] = None,
            last_update_time_stamp: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
            status_reason: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryPipelines.TelemetryPipelineStatusReasonProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Represents a complete telemetry pipeline resource with configuration, status, and metadata for data processing and transformation.

            :param arn: The Amazon Resource Name (ARN) of the telemetry pipeline.
            :param configuration: The configuration that defines how the telemetry pipeline processes data. For more information, see the `Amazon CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Creating-pipelines.html>`_ .
            :param created_time_stamp: The timestamp when the telemetry pipeline was created.
            :param last_update_time_stamp: The timestamp when the telemetry pipeline was last updated.
            :param name: The name of the telemetry pipeline.
            :param status: The current status of the telemetry pipeline.
            :param status_reason: Additional information about the pipeline status, including reasons for failure states.
            :param tags: The key-value pairs associated with the telemetry pipeline resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline.html
            :exampleMetadata: fixture=_generated

            Example::

                from aws_cdk import CfnTag
                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_pipeline_property = observabilityadmin.CfnTelemetryPipelines.TelemetryPipelineProperty(
                    arn="arn",
                    configuration=observabilityadmin.CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty(
                        body="body"
                    ),
                    created_time_stamp=123,
                    last_update_time_stamp=123,
                    name="name",
                    status="status",
                    status_reason=observabilityadmin.CfnTelemetryPipelines.TelemetryPipelineStatusReasonProperty(
                        description="description"
                    ),
                    tags=[CfnTag(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__521e5519bd3500dba951faf81c8c8ad63ae7bedb065325d66cf2300ff66789f8)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
                check_type(argname="argument created_time_stamp", value=created_time_stamp, expected_type=type_hints["created_time_stamp"])
                check_type(argname="argument last_update_time_stamp", value=last_update_time_stamp, expected_type=type_hints["last_update_time_stamp"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument status_reason", value=status_reason, expected_type=type_hints["status_reason"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if configuration is not None:
                self._values["configuration"] = configuration
            if created_time_stamp is not None:
                self._values["created_time_stamp"] = created_time_stamp
            if last_update_time_stamp is not None:
                self._values["last_update_time_stamp"] = last_update_time_stamp
            if name is not None:
                self._values["name"] = name
            if status is not None:
                self._values["status"] = status
            if status_reason is not None:
                self._values["status_reason"] = status_reason
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the telemetry pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline.html#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty"]]:
            '''The configuration that defines how the telemetry pipeline processes data.

            For more information, see the `Amazon CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Creating-pipelines.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline.html#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-configuration
            '''
            result = self._values.get("configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty"]], result)

        @builtins.property
        def created_time_stamp(self) -> typing.Optional[jsii.Number]:
            '''The timestamp when the telemetry pipeline was created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline.html#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-createdtimestamp
            '''
            result = self._values.get("created_time_stamp")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def last_update_time_stamp(self) -> typing.Optional[jsii.Number]:
            '''The timestamp when the telemetry pipeline was last updated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline.html#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-lastupdatetimestamp
            '''
            result = self._values.get("last_update_time_stamp")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the telemetry pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline.html#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''The current status of the telemetry pipeline.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline.html#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status_reason(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryPipelines.TelemetryPipelineStatusReasonProperty"]]:
            '''Additional information about the pipeline status, including reasons for failure states.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline.html#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-statusreason
            '''
            result = self._values.get("status_reason")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryPipelines.TelemetryPipelineStatusReasonProperty"]], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
            '''The key-value pairs associated with the telemetry pipeline resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipeline.html#cfn-observabilityadmin-telemetrypipelines-telemetrypipeline-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryPipelineProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryPipelines.TelemetryPipelineStatusReasonProperty",
        jsii_struct_bases=[],
        name_mapping={"description": "description"},
    )
    class TelemetryPipelineStatusReasonProperty:
        def __init__(
            self,
            *,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides detailed information about the status of a telemetry pipeline, including reasons for specific states.

            :param description: A description of the pipeline status reason, providing additional context about the current state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_pipeline_status_reason_property = observabilityadmin.CfnTelemetryPipelines.TelemetryPipelineStatusReasonProperty(
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8ac245ad25f1a31f025f3074cc38689cbc6eb0da13fbd131c2413958c035568e)
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the pipeline status reason, providing additional context about the current state.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason.html#cfn-observabilityadmin-telemetrypipelines-telemetrypipelinestatusreason-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryPipelineStatusReasonProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryPipelinesProps",
    jsii_struct_bases=[],
    name_mapping={"configuration": "configuration", "name": "name", "tags": "tags"},
)
class CfnTelemetryPipelinesProps:
    def __init__(
        self,
        *,
        configuration: typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTelemetryPipelines``.

        :param configuration: The configuration that defines how the telemetry pipeline processes data, including sources, processors, and destinations. For more information, see the `Amazon CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Creating-pipelines.html>`_ .
        :param name: The name of the telemetry pipeline to create. The name must be unique within your account.
        :param tags: The key-value pairs to associate with the telemetry pipeline resource for categorization and management purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetrypipelines.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            cfn_telemetry_pipelines_props = observabilityadmin.CfnTelemetryPipelinesProps(
                configuration=observabilityadmin.CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty(
                    body="body"
                ),
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5369e75735c42fa71fba44fea4843e2a7be2cb41f104bf1b5e5c9c21b640b915)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty"]:
        '''The configuration that defines how the telemetry pipeline processes data, including sources, processors, and destinations.

        For more information, see the `Amazon CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Creating-pipelines.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetrypipelines.html#cfn-observabilityadmin-telemetrypipelines-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the telemetry pipeline to create.

        The name must be unique within your account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetrypipelines.html#cfn-observabilityadmin-telemetrypipelines-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''The key-value pairs to associate with the telemetry pipeline resource for categorization and management purposes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetrypipelines.html#cfn-observabilityadmin-telemetrypipelines-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTelemetryPipelinesProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITelemetryRuleRef_9918195f, _ITaggableV2_4e6798f8)
class CfnTelemetryRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule",
):
    '''Creates a telemetry rule that defines how telemetry should be configured for AWS resources in your account.

    The rule specifies which resources should have telemetry enabled and how that telemetry data should be collected based on resource type, telemetry type, and selection criteria.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html
    :cloudformationResource: AWS::ObservabilityAdmin::TelemetryRule
    :exampleMetadata: fixture=_generated

    Example::

        from aws_cdk import CfnTag
        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_observabilityadmin as observabilityadmin
        
        cfn_telemetry_rule = observabilityadmin.CfnTelemetryRule(self, "MyCfnTelemetryRule",
            rule=observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty(
                resource_type="resourceType",
                telemetry_type="telemetryType",
        
                # the properties below are optional
                destination_configuration=observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                    cloudtrail_parameters=observabilityadmin.CfnTelemetryRule.CloudtrailParametersProperty(
                        advanced_event_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedEventSelectorProperty(
                            field_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedFieldSelectorProperty(
                                ends_with=["endsWith"],
                                equal_to=["equalTo"],
                                field="field",
                                not_ends_with=["notEndsWith"],
                                not_equals=["notEquals"],
                                not_starts_with=["notStartsWith"],
                                starts_with=["startsWith"]
                            )],
        
                            # the properties below are optional
                            name="name"
                        )]
                    ),
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    elb_load_balancer_logging_parameters=observabilityadmin.CfnTelemetryRule.ELBLoadBalancerLoggingParametersProperty(
                        field_delimiter="fieldDelimiter",
                        output_format="outputFormat"
                    ),
                    log_delivery_parameters=observabilityadmin.CfnTelemetryRule.LogDeliveryParametersProperty(
                        log_types=["logTypes"]
                    ),
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    ),
                    waf_logging_parameters=observabilityadmin.CfnTelemetryRule.WAFLoggingParametersProperty(
                        logging_filter=observabilityadmin.CfnTelemetryRule.LoggingFilterProperty(
                            default_behavior="defaultBehavior",
                            filters=[observabilityadmin.CfnTelemetryRule.FilterProperty(
                                behavior="behavior",
                                conditions=[observabilityadmin.CfnTelemetryRule.ConditionProperty(
                                    action_condition=observabilityadmin.CfnTelemetryRule.ActionConditionProperty(
                                        action="action"
                                    ),
                                    label_name_condition=observabilityadmin.CfnTelemetryRule.LabelNameConditionProperty(
                                        label_name="labelName"
                                    )
                                )],
                                requirement="requirement"
                            )]
                        ),
                        log_type="logType",
                        redacted_fields=[observabilityadmin.CfnTelemetryRule.FieldToMatchProperty(
                            method="method",
                            query_string="queryString",
                            single_header=observabilityadmin.CfnTelemetryRule.SingleHeaderProperty(
                                name="name"
                            ),
                            uri_path="uriPath"
                        )]
                    )
                ),
                selection_criteria="selectionCriteria",
                telemetry_source_types=["telemetrySourceTypes"]
            ),
            rule_name="ruleName",
        
            # the properties below are optional
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
        rule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.TelemetryRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Create a new ``AWS::ObservabilityAdmin::TelemetryRule``.

        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule: Retrieves the details of a specific telemetry rule in your account.
        :param rule_name: The name of the telemetry rule.
        :param tags: Lists all tags attached to the specified resource. Supports telemetry rule resources and telemetry pipeline resources.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cb28d06ef60815f8488b771b64aca8e3671a315a3f6676ad80a414dcd296224)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTelemetryRuleProps(rule=rule, rule_name=rule_name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="isCfnTelemetryRule")
    @builtins.classmethod
    def is_cfn_telemetry_rule(cls, x: typing.Any) -> builtins.bool:
        '''Checks whether the given object is a CfnTelemetryRule.

        :param x: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15d46db6be93b2acc11cf6216144d83efa879d1fceb7052f192fd6a434af63b9)
            check_type(argname="argument x", value=x, expected_type=type_hints["x"])
        return typing.cast(builtins.bool, jsii.sinvoke(cls, "isCfnTelemetryRule", [x]))

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: "_TreeInspector_488e0dd5") -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c971c1c4e8e03d4140674a22f18490c0a14f143dab5c9b15a801d0e69e908b92)
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
            type_hints = typing.get_type_hints(_typecheckingstub__adf48e055c256d6f5cb987ba3921807e211a303c3d38be6a02b6932f52a739fe)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRuleArn")
    def attr_rule_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the telemetry rule.

        :cloudformationAttribute: RuleArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRuleArn"))

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
    @jsii.member(jsii_name="telemetryRuleRef")
    def telemetry_rule_ref(self) -> "_TelemetryRuleReference_35b2b664":
        '''A reference to a TelemetryRule resource.'''
        return typing.cast("_TelemetryRuleReference_35b2b664", jsii.get(self, "telemetryRuleRef"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.TelemetryRuleProperty"]:
        '''Retrieves the details of a specific telemetry rule in your account.'''
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.TelemetryRuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.TelemetryRuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__253115d76ca17e48e13df2aa679666bb12581680b457a45a7743f6a80d6dbfa1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ruleName")
    def rule_name(self) -> builtins.str:
        '''The name of the telemetry rule.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleName"))

    @rule_name.setter
    def rule_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c59aae5f9c690d805a52b4e5949569db025239eb21172f781673428651a87d80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Lists all tags attached to the specified resource.'''
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List["_CfnTag_f6864754"]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec4f4991901119d1b8ec2bf2b1d23daff9627e5f20b555f27ec8fd5bc58890b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.ActionConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action"},
    )
    class ActionConditionProperty:
        def __init__(self, *, action: typing.Optional[builtins.str] = None) -> None:
            '''Condition that matches based on the specific WAF action taken on the request.

            :param action: The WAF action to match against (ALLOW, BLOCK, COUNT, CAPTCHA, CHALLENGE, EXCLUDED_AS_COUNT).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-actioncondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                action_condition_property = observabilityadmin.CfnTelemetryRule.ActionConditionProperty(
                    action="action"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__50557e914800706360d6a6d0fd3fa96ca54609369f32f1412635fd95de5c04fd)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''The WAF action to match against (ALLOW, BLOCK, COUNT, CAPTCHA, CHALLENGE, EXCLUDED_AS_COUNT).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-actioncondition.html#cfn-observabilityadmin-telemetryrule-actioncondition-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.AdvancedEventSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={"field_selectors": "fieldSelectors", "name": "name"},
    )
    class AdvancedEventSelectorProperty:
        def __init__(
            self,
            *,
            field_selectors: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.AdvancedFieldSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]],
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Advanced event selectors let you create fine-grained selectors for management, data, and network activity events.

            :param field_selectors: Contains all selector statements in an advanced event selector.
            :param name: An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedeventselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                advanced_event_selector_property = observabilityadmin.CfnTelemetryRule.AdvancedEventSelectorProperty(
                    field_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedFieldSelectorProperty(
                        ends_with=["endsWith"],
                        equal_to=["equalTo"],
                        field="field",
                        not_ends_with=["notEndsWith"],
                        not_equals=["notEquals"],
                        not_starts_with=["notStartsWith"],
                        starts_with=["startsWith"]
                    )],
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__34e91e8b7bfb8885a361b9a019e847677797f97575e5c9e1c82c3ee8cb4fe68d)
                check_type(argname="argument field_selectors", value=field_selectors, expected_type=type_hints["field_selectors"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "field_selectors": field_selectors,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def field_selectors(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.AdvancedFieldSelectorProperty"]]]:
            '''Contains all selector statements in an advanced event selector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedeventselector.html#cfn-observabilityadmin-telemetryrule-advancedeventselector-fieldselectors
            '''
            result = self._values.get("field_selectors")
            assert result is not None, "Required property 'field_selectors' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.AdvancedFieldSelectorProperty"]]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''An optional, descriptive name for an advanced event selector, such as "Log data events for only two S3 buckets".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedeventselector.html#cfn-observabilityadmin-telemetryrule-advancedeventselector-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedEventSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.AdvancedFieldSelectorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ends_with": "endsWith",
            "equal_to": "equalTo",
            "field": "field",
            "not_ends_with": "notEndsWith",
            "not_equals": "notEquals",
            "not_starts_with": "notStartsWith",
            "starts_with": "startsWith",
        },
    )
    class AdvancedFieldSelectorProperty:
        def __init__(
            self,
            *,
            ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
            field: typing.Optional[builtins.str] = None,
            not_ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
            not_starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
            starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Defines criteria for selecting resources based on field values.

            :param ends_with: Matches if the field value ends with the specified value.
            :param equal_to: Matches if the field value equals the specified value.
            :param field: The name of the field to use for selection.
            :param not_ends_with: Matches if the field value does not end with the specified value.
            :param not_equals: Matches if the field value does not equal the specified value.
            :param not_starts_with: Matches if the field value does not start with the specified value.
            :param starts_with: Matches if the field value starts with the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedfieldselector.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                advanced_field_selector_property = observabilityadmin.CfnTelemetryRule.AdvancedFieldSelectorProperty(
                    ends_with=["endsWith"],
                    equal_to=["equalTo"],
                    field="field",
                    not_ends_with=["notEndsWith"],
                    not_equals=["notEquals"],
                    not_starts_with=["notStartsWith"],
                    starts_with=["startsWith"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5faffd9294bd925fc19af734c530e3ea1568e156d6666558fb1e9a63ed9e319b)
                check_type(argname="argument ends_with", value=ends_with, expected_type=type_hints["ends_with"])
                check_type(argname="argument equal_to", value=equal_to, expected_type=type_hints["equal_to"])
                check_type(argname="argument field", value=field, expected_type=type_hints["field"])
                check_type(argname="argument not_ends_with", value=not_ends_with, expected_type=type_hints["not_ends_with"])
                check_type(argname="argument not_equals", value=not_equals, expected_type=type_hints["not_equals"])
                check_type(argname="argument not_starts_with", value=not_starts_with, expected_type=type_hints["not_starts_with"])
                check_type(argname="argument starts_with", value=starts_with, expected_type=type_hints["starts_with"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ends_with is not None:
                self._values["ends_with"] = ends_with
            if equal_to is not None:
                self._values["equal_to"] = equal_to
            if field is not None:
                self._values["field"] = field
            if not_ends_with is not None:
                self._values["not_ends_with"] = not_ends_with
            if not_equals is not None:
                self._values["not_equals"] = not_equals
            if not_starts_with is not None:
                self._values["not_starts_with"] = not_starts_with
            if starts_with is not None:
                self._values["starts_with"] = starts_with

        @builtins.property
        def ends_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value ends with the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedfieldselector.html#cfn-observabilityadmin-telemetryrule-advancedfieldselector-endswith
            '''
            result = self._values.get("ends_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def equal_to(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value equals the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedfieldselector.html#cfn-observabilityadmin-telemetryrule-advancedfieldselector-equals
            '''
            result = self._values.get("equal_to")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def field(self) -> typing.Optional[builtins.str]:
            '''The name of the field to use for selection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedfieldselector.html#cfn-observabilityadmin-telemetryrule-advancedfieldselector-field
            '''
            result = self._values.get("field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def not_ends_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value does not end with the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedfieldselector.html#cfn-observabilityadmin-telemetryrule-advancedfieldselector-notendswith
            '''
            result = self._values.get("not_ends_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_equals(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value does not equal the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedfieldselector.html#cfn-observabilityadmin-telemetryrule-advancedfieldselector-notequals
            '''
            result = self._values.get("not_equals")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def not_starts_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value does not start with the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedfieldselector.html#cfn-observabilityadmin-telemetryrule-advancedfieldselector-notstartswith
            '''
            result = self._values.get("not_starts_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def starts_with(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Matches if the field value starts with the specified value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-advancedfieldselector.html#cfn-observabilityadmin-telemetryrule-advancedfieldselector-startswith
            '''
            result = self._values.get("starts_with")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AdvancedFieldSelectorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.CloudtrailParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"advanced_event_selectors": "advancedEventSelectors"},
    )
    class CloudtrailParametersProperty:
        def __init__(
            self,
            *,
            advanced_event_selectors: typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.AdvancedEventSelectorProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Parameters specific to AWS CloudTrail telemetry configuration.

            :param advanced_event_selectors: The advanced event selectors to use for filtering AWS CloudTrail events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-cloudtrailparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                cloudtrail_parameters_property = observabilityadmin.CfnTelemetryRule.CloudtrailParametersProperty(
                    advanced_event_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedEventSelectorProperty(
                        field_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedFieldSelectorProperty(
                            ends_with=["endsWith"],
                            equal_to=["equalTo"],
                            field="field",
                            not_ends_with=["notEndsWith"],
                            not_equals=["notEquals"],
                            not_starts_with=["notStartsWith"],
                            starts_with=["startsWith"]
                        )],
                
                        # the properties below are optional
                        name="name"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__62ff49994749a104a46f12763305b7e1872bf64c00794dcd8ff06fff28ff5016)
                check_type(argname="argument advanced_event_selectors", value=advanced_event_selectors, expected_type=type_hints["advanced_event_selectors"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "advanced_event_selectors": advanced_event_selectors,
            }

        @builtins.property
        def advanced_event_selectors(
            self,
        ) -> typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.AdvancedEventSelectorProperty"]]]:
            '''The advanced event selectors to use for filtering AWS CloudTrail events.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-cloudtrailparameters.html#cfn-observabilityadmin-telemetryrule-cloudtrailparameters-advancedeventselectors
            '''
            result = self._values.get("advanced_event_selectors")
            assert result is not None, "Required property 'advanced_event_selectors' is missing"
            return typing.cast(typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.AdvancedEventSelectorProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudtrailParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.ConditionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_condition": "actionCondition",
            "label_name_condition": "labelNameCondition",
        },
    )
    class ConditionProperty:
        def __init__(
            self,
            *,
            action_condition: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.ActionConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            label_name_condition: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.LabelNameConditionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A single condition that can match based on WAF rule action or label name.

            :param action_condition: Matches log records based on the WAF rule action taken (ALLOW, BLOCK, COUNT, etc.).
            :param label_name_condition: Matches log records based on WAF rule labels applied to the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-condition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                condition_property = observabilityadmin.CfnTelemetryRule.ConditionProperty(
                    action_condition=observabilityadmin.CfnTelemetryRule.ActionConditionProperty(
                        action="action"
                    ),
                    label_name_condition=observabilityadmin.CfnTelemetryRule.LabelNameConditionProperty(
                        label_name="labelName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c897e4ce5b2e29b5a786649170e489dde012e76b9528806d6868b20b58fbe044)
                check_type(argname="argument action_condition", value=action_condition, expected_type=type_hints["action_condition"])
                check_type(argname="argument label_name_condition", value=label_name_condition, expected_type=type_hints["label_name_condition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action_condition is not None:
                self._values["action_condition"] = action_condition
            if label_name_condition is not None:
                self._values["label_name_condition"] = label_name_condition

        @builtins.property
        def action_condition(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.ActionConditionProperty"]]:
            '''Matches log records based on the WAF rule action taken (ALLOW, BLOCK, COUNT, etc.).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-condition.html#cfn-observabilityadmin-telemetryrule-condition-actioncondition
            '''
            result = self._values.get("action_condition")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.ActionConditionProperty"]], result)

        @builtins.property
        def label_name_condition(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.LabelNameConditionProperty"]]:
            '''Matches log records based on WAF rule labels applied to the request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-condition.html#cfn-observabilityadmin-telemetryrule-condition-labelnamecondition
            '''
            result = self._values.get("label_name_condition")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.LabelNameConditionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.ELBLoadBalancerLoggingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "field_delimiter": "fieldDelimiter",
            "output_format": "outputFormat",
        },
    )
    class ELBLoadBalancerLoggingParametersProperty:
        def __init__(
            self,
            *,
            field_delimiter: typing.Optional[builtins.str] = None,
            output_format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration parameters for ELB load balancer logging, including output format and field delimiter settings.

            :param field_delimiter: The delimiter character used to separate fields in ELB access log entries when using plain text format.
            :param output_format: The format for ELB access log entries (plain text or JSON format).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-elbloadbalancerloggingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                e_lBLoad_balancer_logging_parameters_property = observabilityadmin.CfnTelemetryRule.ELBLoadBalancerLoggingParametersProperty(
                    field_delimiter="fieldDelimiter",
                    output_format="outputFormat"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__03a18a983d83cbe92b3f9982fcddc595f10337f8733ae0d29f3010716bab954c)
                check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
                check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if field_delimiter is not None:
                self._values["field_delimiter"] = field_delimiter
            if output_format is not None:
                self._values["output_format"] = output_format

        @builtins.property
        def field_delimiter(self) -> typing.Optional[builtins.str]:
            '''The delimiter character used to separate fields in ELB access log entries when using plain text format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-elbloadbalancerloggingparameters.html#cfn-observabilityadmin-telemetryrule-elbloadbalancerloggingparameters-fielddelimiter
            '''
            result = self._values.get("field_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def output_format(self) -> typing.Optional[builtins.str]:
            '''The format for ELB access log entries (plain text or JSON format).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-elbloadbalancerloggingparameters.html#cfn-observabilityadmin-telemetryrule-elbloadbalancerloggingparameters-outputformat
            '''
            result = self._values.get("output_format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ELBLoadBalancerLoggingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.FieldToMatchProperty",
        jsii_struct_bases=[],
        name_mapping={
            "method": "method",
            "query_string": "queryString",
            "single_header": "singleHeader",
            "uri_path": "uriPath",
        },
    )
    class FieldToMatchProperty:
        def __init__(
            self,
            *,
            method: typing.Optional[builtins.str] = None,
            query_string: typing.Optional[builtins.str] = None,
            single_header: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.SingleHeaderProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            uri_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies a field in the request to redact from WAF logs, such as headers, query parameters, or body content.

            :param method: Redacts the HTTP method from WAF logs.
            :param query_string: Redacts the entire query string from WAF logs.
            :param single_header: Redacts a specific header field by name from WAF logs.
            :param uri_path: Redacts the URI path from WAF logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-fieldtomatch.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                field_to_match_property = observabilityadmin.CfnTelemetryRule.FieldToMatchProperty(
                    method="method",
                    query_string="queryString",
                    single_header=observabilityadmin.CfnTelemetryRule.SingleHeaderProperty(
                        name="name"
                    ),
                    uri_path="uriPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3976476c0a0e097f45e5560dcbf47e3f22424da7ff8b7eeb81ddaa36b8424717)
                check_type(argname="argument method", value=method, expected_type=type_hints["method"])
                check_type(argname="argument query_string", value=query_string, expected_type=type_hints["query_string"])
                check_type(argname="argument single_header", value=single_header, expected_type=type_hints["single_header"])
                check_type(argname="argument uri_path", value=uri_path, expected_type=type_hints["uri_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if method is not None:
                self._values["method"] = method
            if query_string is not None:
                self._values["query_string"] = query_string
            if single_header is not None:
                self._values["single_header"] = single_header
            if uri_path is not None:
                self._values["uri_path"] = uri_path

        @builtins.property
        def method(self) -> typing.Optional[builtins.str]:
            '''Redacts the HTTP method from WAF logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-fieldtomatch.html#cfn-observabilityadmin-telemetryrule-fieldtomatch-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def query_string(self) -> typing.Optional[builtins.str]:
            '''Redacts the entire query string from WAF logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-fieldtomatch.html#cfn-observabilityadmin-telemetryrule-fieldtomatch-querystring
            '''
            result = self._values.get("query_string")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def single_header(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.SingleHeaderProperty"]]:
            '''Redacts a specific header field by name from WAF logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-fieldtomatch.html#cfn-observabilityadmin-telemetryrule-fieldtomatch-singleheader
            '''
            result = self._values.get("single_header")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.SingleHeaderProperty"]], result)

        @builtins.property
        def uri_path(self) -> typing.Optional[builtins.str]:
            '''Redacts the URI path from WAF logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-fieldtomatch.html#cfn-observabilityadmin-telemetryrule-fieldtomatch-uripath
            '''
            result = self._values.get("uri_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FieldToMatchProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "behavior": "behavior",
            "conditions": "conditions",
            "requirement": "requirement",
        },
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            behavior: typing.Optional[builtins.str] = None,
            conditions: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.ConditionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            requirement: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A single filter condition that specifies behavior, requirement, and matching conditions for WAF log records.

            :param behavior: The action to take for log records matching this filter (KEEP or DROP).
            :param conditions: The list of conditions that determine if a log record matches this filter.
            :param requirement: Whether the log record must meet all conditions (MEETS_ALL) or any condition (MEETS_ANY) to match this filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                filter_property = observabilityadmin.CfnTelemetryRule.FilterProperty(
                    behavior="behavior",
                    conditions=[observabilityadmin.CfnTelemetryRule.ConditionProperty(
                        action_condition=observabilityadmin.CfnTelemetryRule.ActionConditionProperty(
                            action="action"
                        ),
                        label_name_condition=observabilityadmin.CfnTelemetryRule.LabelNameConditionProperty(
                            label_name="labelName"
                        )
                    )],
                    requirement="requirement"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__49a49dafe52d9710a05d5e9354c3584d91d95a89fb01156df326d91c12f8e7aa)
                check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
                check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
                check_type(argname="argument requirement", value=requirement, expected_type=type_hints["requirement"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if behavior is not None:
                self._values["behavior"] = behavior
            if conditions is not None:
                self._values["conditions"] = conditions
            if requirement is not None:
                self._values["requirement"] = requirement

        @builtins.property
        def behavior(self) -> typing.Optional[builtins.str]:
            '''The action to take for log records matching this filter (KEEP or DROP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-filter.html#cfn-observabilityadmin-telemetryrule-filter-behavior
            '''
            result = self._values.get("behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def conditions(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.ConditionProperty"]]]]:
            '''The list of conditions that determine if a log record matches this filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-filter.html#cfn-observabilityadmin-telemetryrule-filter-conditions
            '''
            result = self._values.get("conditions")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.ConditionProperty"]]]], result)

        @builtins.property
        def requirement(self) -> typing.Optional[builtins.str]:
            '''Whether the log record must meet all conditions (MEETS_ALL) or any condition (MEETS_ANY) to match this filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-filter.html#cfn-observabilityadmin-telemetryrule-filter-requirement
            '''
            result = self._values.get("requirement")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.LabelNameConditionProperty",
        jsii_struct_bases=[],
        name_mapping={"label_name": "labelName"},
    )
    class LabelNameConditionProperty:
        def __init__(self, *, label_name: typing.Optional[builtins.str] = None) -> None:
            '''Condition that matches based on WAF rule labels, with label names limited to 1024 characters.

            :param label_name: The label name to match, supporting alphanumeric characters, underscores, hyphens, and colons.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-labelnamecondition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                label_name_condition_property = observabilityadmin.CfnTelemetryRule.LabelNameConditionProperty(
                    label_name="labelName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff01fa602d174a91ced1cb282fb0eb60b7d5109e9b2f83417d27bea0261462a3)
                check_type(argname="argument label_name", value=label_name, expected_type=type_hints["label_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if label_name is not None:
                self._values["label_name"] = label_name

        @builtins.property
        def label_name(self) -> typing.Optional[builtins.str]:
            '''The label name to match, supporting alphanumeric characters, underscores, hyphens, and colons.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-labelnamecondition.html#cfn-observabilityadmin-telemetryrule-labelnamecondition-labelname
            '''
            result = self._values.get("label_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LabelNameConditionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.LogDeliveryParametersProperty",
        jsii_struct_bases=[],
        name_mapping={"log_types": "logTypes"},
    )
    class LogDeliveryParametersProperty:
        def __init__(
            self,
            *,
            log_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration parameters for Amazon Bedrock AgentCore logging, including ``logType`` settings.

            :param log_types: The type of log that the source is sending.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-logdeliveryparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                log_delivery_parameters_property = observabilityadmin.CfnTelemetryRule.LogDeliveryParametersProperty(
                    log_types=["logTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7324b57f326b27aa49521b6ab51d6cfe3f1c8e68c78bb51ad7e061edc92c0a8d)
                check_type(argname="argument log_types", value=log_types, expected_type=type_hints["log_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_types is not None:
                self._values["log_types"] = log_types

        @builtins.property
        def log_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The type of log that the source is sending.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-logdeliveryparameters.html#cfn-observabilityadmin-telemetryrule-logdeliveryparameters-logtypes
            '''
            result = self._values.get("log_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDeliveryParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.LoggingFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"default_behavior": "defaultBehavior", "filters": "filters"},
    )
    class LoggingFilterProperty:
        def __init__(
            self,
            *,
            default_behavior: typing.Optional[builtins.str] = None,
            filters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.FilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration that determines which WAF log records to keep or drop based on specified conditions.

            :param default_behavior: The default action (KEEP or DROP) for log records that don't match any filter conditions.
            :param filters: A list of filter conditions that determine log record handling behavior.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-loggingfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                logging_filter_property = observabilityadmin.CfnTelemetryRule.LoggingFilterProperty(
                    default_behavior="defaultBehavior",
                    filters=[observabilityadmin.CfnTelemetryRule.FilterProperty(
                        behavior="behavior",
                        conditions=[observabilityadmin.CfnTelemetryRule.ConditionProperty(
                            action_condition=observabilityadmin.CfnTelemetryRule.ActionConditionProperty(
                                action="action"
                            ),
                            label_name_condition=observabilityadmin.CfnTelemetryRule.LabelNameConditionProperty(
                                label_name="labelName"
                            )
                        )],
                        requirement="requirement"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ec5b265219a09ae971954fc5efb55eeca562e31b03200d5a454f07b91730c0c0)
                check_type(argname="argument default_behavior", value=default_behavior, expected_type=type_hints["default_behavior"])
                check_type(argname="argument filters", value=filters, expected_type=type_hints["filters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if default_behavior is not None:
                self._values["default_behavior"] = default_behavior
            if filters is not None:
                self._values["filters"] = filters

        @builtins.property
        def default_behavior(self) -> typing.Optional[builtins.str]:
            '''The default action (KEEP or DROP) for log records that don't match any filter conditions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-loggingfilter.html#cfn-observabilityadmin-telemetryrule-loggingfilter-defaultbehavior
            '''
            result = self._values.get("default_behavior")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def filters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.FilterProperty"]]]]:
            '''A list of filter conditions that determine log record handling behavior.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-loggingfilter.html#cfn-observabilityadmin-telemetryrule-loggingfilter-filters
            '''
            result = self._values.get("filters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.FilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.SingleHeaderProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class SingleHeaderProperty:
        def __init__(self, *, name: builtins.str) -> None:
            '''Structure containing a name field limited to 64 characters for header or query parameter identification.

            :param name: The name value, limited to 64 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-singleheader.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                single_header_property = observabilityadmin.CfnTelemetryRule.SingleHeaderProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__52016d9c5461305a90cf833adbbbe8dfceb9080f12605147dcc5869d62c25ad4)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name value, limited to 64 characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-singleheader.html#cfn-observabilityadmin-telemetryrule-singleheader-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SingleHeaderProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cloudtrail_parameters": "cloudtrailParameters",
            "destination_pattern": "destinationPattern",
            "destination_type": "destinationType",
            "elb_load_balancer_logging_parameters": "elbLoadBalancerLoggingParameters",
            "log_delivery_parameters": "logDeliveryParameters",
            "retention_in_days": "retentionInDays",
            "vpc_flow_log_parameters": "vpcFlowLogParameters",
            "waf_logging_parameters": "wafLoggingParameters",
        },
    )
    class TelemetryDestinationConfigurationProperty:
        def __init__(
            self,
            *,
            cloudtrail_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.CloudtrailParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            destination_pattern: typing.Optional[builtins.str] = None,
            destination_type: typing.Optional[builtins.str] = None,
            elb_load_balancer_logging_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.ELBLoadBalancerLoggingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            log_delivery_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.LogDeliveryParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            retention_in_days: typing.Optional[jsii.Number] = None,
            vpc_flow_log_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.VPCFlowLogParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            waf_logging_parameters: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.WAFLoggingParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Configuration specifying where and how telemetry data should be delivered for AWS resources.

            :param cloudtrail_parameters: Configuration parameters specific to AWS CloudTrail when CloudTrail is the source type.
            :param destination_pattern: The pattern used to generate the destination path or name, supporting macros like and .
            :param destination_type: The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3").
            :param elb_load_balancer_logging_parameters: Configuration parameters specific to ELB load balancer logging when ELB is the resource type.
            :param log_delivery_parameters: Configuration parameters specific to Amazon Bedrock AgentCore logging when Amazon Bedrock AgentCore is the resource type.
            :param retention_in_days: The number of days to retain the telemetry data in the destination.
            :param vpc_flow_log_parameters: Configuration parameters specific to VPC Flow Logs when VPC is the resource type.
            :param waf_logging_parameters: Configuration parameters specific to WAF logging when WAF is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_destination_configuration_property = observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                    cloudtrail_parameters=observabilityadmin.CfnTelemetryRule.CloudtrailParametersProperty(
                        advanced_event_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedEventSelectorProperty(
                            field_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedFieldSelectorProperty(
                                ends_with=["endsWith"],
                                equal_to=["equalTo"],
                                field="field",
                                not_ends_with=["notEndsWith"],
                                not_equals=["notEquals"],
                                not_starts_with=["notStartsWith"],
                                starts_with=["startsWith"]
                            )],
                
                            # the properties below are optional
                            name="name"
                        )]
                    ),
                    destination_pattern="destinationPattern",
                    destination_type="destinationType",
                    elb_load_balancer_logging_parameters=observabilityadmin.CfnTelemetryRule.ELBLoadBalancerLoggingParametersProperty(
                        field_delimiter="fieldDelimiter",
                        output_format="outputFormat"
                    ),
                    log_delivery_parameters=observabilityadmin.CfnTelemetryRule.LogDeliveryParametersProperty(
                        log_types=["logTypes"]
                    ),
                    retention_in_days=123,
                    vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                        log_format="logFormat",
                        max_aggregation_interval=123,
                        traffic_type="trafficType"
                    ),
                    waf_logging_parameters=observabilityadmin.CfnTelemetryRule.WAFLoggingParametersProperty(
                        logging_filter=observabilityadmin.CfnTelemetryRule.LoggingFilterProperty(
                            default_behavior="defaultBehavior",
                            filters=[observabilityadmin.CfnTelemetryRule.FilterProperty(
                                behavior="behavior",
                                conditions=[observabilityadmin.CfnTelemetryRule.ConditionProperty(
                                    action_condition=observabilityadmin.CfnTelemetryRule.ActionConditionProperty(
                                        action="action"
                                    ),
                                    label_name_condition=observabilityadmin.CfnTelemetryRule.LabelNameConditionProperty(
                                        label_name="labelName"
                                    )
                                )],
                                requirement="requirement"
                            )]
                        ),
                        log_type="logType",
                        redacted_fields=[observabilityadmin.CfnTelemetryRule.FieldToMatchProperty(
                            method="method",
                            query_string="queryString",
                            single_header=observabilityadmin.CfnTelemetryRule.SingleHeaderProperty(
                                name="name"
                            ),
                            uri_path="uriPath"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__01ec7a824466c4f6343ec939656046b6c12a168edd9bbf6ebca41e4b5d1554d5)
                check_type(argname="argument cloudtrail_parameters", value=cloudtrail_parameters, expected_type=type_hints["cloudtrail_parameters"])
                check_type(argname="argument destination_pattern", value=destination_pattern, expected_type=type_hints["destination_pattern"])
                check_type(argname="argument destination_type", value=destination_type, expected_type=type_hints["destination_type"])
                check_type(argname="argument elb_load_balancer_logging_parameters", value=elb_load_balancer_logging_parameters, expected_type=type_hints["elb_load_balancer_logging_parameters"])
                check_type(argname="argument log_delivery_parameters", value=log_delivery_parameters, expected_type=type_hints["log_delivery_parameters"])
                check_type(argname="argument retention_in_days", value=retention_in_days, expected_type=type_hints["retention_in_days"])
                check_type(argname="argument vpc_flow_log_parameters", value=vpc_flow_log_parameters, expected_type=type_hints["vpc_flow_log_parameters"])
                check_type(argname="argument waf_logging_parameters", value=waf_logging_parameters, expected_type=type_hints["waf_logging_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cloudtrail_parameters is not None:
                self._values["cloudtrail_parameters"] = cloudtrail_parameters
            if destination_pattern is not None:
                self._values["destination_pattern"] = destination_pattern
            if destination_type is not None:
                self._values["destination_type"] = destination_type
            if elb_load_balancer_logging_parameters is not None:
                self._values["elb_load_balancer_logging_parameters"] = elb_load_balancer_logging_parameters
            if log_delivery_parameters is not None:
                self._values["log_delivery_parameters"] = log_delivery_parameters
            if retention_in_days is not None:
                self._values["retention_in_days"] = retention_in_days
            if vpc_flow_log_parameters is not None:
                self._values["vpc_flow_log_parameters"] = vpc_flow_log_parameters
            if waf_logging_parameters is not None:
                self._values["waf_logging_parameters"] = waf_logging_parameters

        @builtins.property
        def cloudtrail_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.CloudtrailParametersProperty"]]:
            '''Configuration parameters specific to AWS CloudTrail when CloudTrail is the source type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-cloudtrailparameters
            '''
            result = self._values.get("cloudtrail_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.CloudtrailParametersProperty"]], result)

        @builtins.property
        def destination_pattern(self) -> typing.Optional[builtins.str]:
            '''The pattern used to generate the destination path or name, supporting macros like  and .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationpattern
            '''
            result = self._values.get("destination_pattern")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def destination_type(self) -> typing.Optional[builtins.str]:
            '''The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3").

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-destinationtype
            '''
            result = self._values.get("destination_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def elb_load_balancer_logging_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.ELBLoadBalancerLoggingParametersProperty"]]:
            '''Configuration parameters specific to ELB load balancer logging when ELB is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-elbloadbalancerloggingparameters
            '''
            result = self._values.get("elb_load_balancer_logging_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.ELBLoadBalancerLoggingParametersProperty"]], result)

        @builtins.property
        def log_delivery_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.LogDeliveryParametersProperty"]]:
            '''Configuration parameters specific to Amazon Bedrock AgentCore logging when Amazon Bedrock AgentCore is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-logdeliveryparameters
            '''
            result = self._values.get("log_delivery_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.LogDeliveryParametersProperty"]], result)

        @builtins.property
        def retention_in_days(self) -> typing.Optional[jsii.Number]:
            '''The number of days to retain the telemetry data in the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-retentionindays
            '''
            result = self._values.get("retention_in_days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def vpc_flow_log_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.VPCFlowLogParametersProperty"]]:
            '''Configuration parameters specific to VPC Flow Logs when VPC is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-vpcflowlogparameters
            '''
            result = self._values.get("vpc_flow_log_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.VPCFlowLogParametersProperty"]], result)

        @builtins.property
        def waf_logging_parameters(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.WAFLoggingParametersProperty"]]:
            '''Configuration parameters specific to WAF logging when WAF is the resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetrydestinationconfiguration.html#cfn-observabilityadmin-telemetryrule-telemetrydestinationconfiguration-wafloggingparameters
            '''
            result = self._values.get("waf_logging_parameters")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.WAFLoggingParametersProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryDestinationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "resource_type": "resourceType",
            "telemetry_type": "telemetryType",
            "destination_configuration": "destinationConfiguration",
            "selection_criteria": "selectionCriteria",
            "telemetry_source_types": "telemetrySourceTypes",
        },
    )
    class TelemetryRuleProperty:
        def __init__(
            self,
            *,
            resource_type: builtins.str,
            telemetry_type: builtins.str,
            destination_configuration: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.TelemetryDestinationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            selection_criteria: typing.Optional[builtins.str] = None,
            telemetry_source_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Defines how telemetry should be configured for specific AWS resources.

            :param resource_type: The type of AWS resource to configure telemetry for (e.g., "AWS::EC2::VPC", "AWS::EKS::Cluster", "AWS::WAFv2::WebACL").
            :param telemetry_type: The type of telemetry to collect (Logs, Metrics, or Traces).
            :param destination_configuration: Configuration specifying where and how the telemetry data should be delivered.
            :param selection_criteria: Criteria for selecting which resources the rule applies to, such as resource tags.
            :param telemetry_source_types: The specific telemetry source types to configure for the resource, such as VPC_FLOW_LOGS or EKS_AUDIT_LOGS. TelemetrySourceTypes must be correlated with the specific resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                telemetry_rule_property = observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
                
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                        cloudtrail_parameters=observabilityadmin.CfnTelemetryRule.CloudtrailParametersProperty(
                            advanced_event_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedEventSelectorProperty(
                                field_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedFieldSelectorProperty(
                                    ends_with=["endsWith"],
                                    equal_to=["equalTo"],
                                    field="field",
                                    not_ends_with=["notEndsWith"],
                                    not_equals=["notEquals"],
                                    not_starts_with=["notStartsWith"],
                                    starts_with=["startsWith"]
                                )],
                
                                # the properties below are optional
                                name="name"
                            )]
                        ),
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        elb_load_balancer_logging_parameters=observabilityadmin.CfnTelemetryRule.ELBLoadBalancerLoggingParametersProperty(
                            field_delimiter="fieldDelimiter",
                            output_format="outputFormat"
                        ),
                        log_delivery_parameters=observabilityadmin.CfnTelemetryRule.LogDeliveryParametersProperty(
                            log_types=["logTypes"]
                        ),
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        ),
                        waf_logging_parameters=observabilityadmin.CfnTelemetryRule.WAFLoggingParametersProperty(
                            logging_filter=observabilityadmin.CfnTelemetryRule.LoggingFilterProperty(
                                default_behavior="defaultBehavior",
                                filters=[observabilityadmin.CfnTelemetryRule.FilterProperty(
                                    behavior="behavior",
                                    conditions=[observabilityadmin.CfnTelemetryRule.ConditionProperty(
                                        action_condition=observabilityadmin.CfnTelemetryRule.ActionConditionProperty(
                                            action="action"
                                        ),
                                        label_name_condition=observabilityadmin.CfnTelemetryRule.LabelNameConditionProperty(
                                            label_name="labelName"
                                        )
                                    )],
                                    requirement="requirement"
                                )]
                            ),
                            log_type="logType",
                            redacted_fields=[observabilityadmin.CfnTelemetryRule.FieldToMatchProperty(
                                method="method",
                                query_string="queryString",
                                single_header=observabilityadmin.CfnTelemetryRule.SingleHeaderProperty(
                                    name="name"
                                ),
                                uri_path="uriPath"
                            )]
                        )
                    ),
                    selection_criteria="selectionCriteria",
                    telemetry_source_types=["telemetrySourceTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25d1c19a045d927560ccf78552c0595fbd7db1322a4e66f60e4d9cb5393b81c3)
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument telemetry_type", value=telemetry_type, expected_type=type_hints["telemetry_type"])
                check_type(argname="argument destination_configuration", value=destination_configuration, expected_type=type_hints["destination_configuration"])
                check_type(argname="argument selection_criteria", value=selection_criteria, expected_type=type_hints["selection_criteria"])
                check_type(argname="argument telemetry_source_types", value=telemetry_source_types, expected_type=type_hints["telemetry_source_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "resource_type": resource_type,
                "telemetry_type": telemetry_type,
            }
            if destination_configuration is not None:
                self._values["destination_configuration"] = destination_configuration
            if selection_criteria is not None:
                self._values["selection_criteria"] = selection_criteria
            if telemetry_source_types is not None:
                self._values["telemetry_source_types"] = telemetry_source_types

        @builtins.property
        def resource_type(self) -> builtins.str:
            '''The type of AWS resource to configure telemetry for (e.g., "AWS::EC2::VPC", "AWS::EKS::Cluster", "AWS::WAFv2::WebACL").

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-resourcetype
            '''
            result = self._values.get("resource_type")
            assert result is not None, "Required property 'resource_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def telemetry_type(self) -> builtins.str:
            '''The type of telemetry to collect (Logs, Metrics, or Traces).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-telemetrytype
            '''
            result = self._values.get("telemetry_type")
            assert result is not None, "Required property 'telemetry_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_configuration(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.TelemetryDestinationConfigurationProperty"]]:
            '''Configuration specifying where and how the telemetry data should be delivered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-destinationconfiguration
            '''
            result = self._values.get("destination_configuration")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.TelemetryDestinationConfigurationProperty"]], result)

        @builtins.property
        def selection_criteria(self) -> typing.Optional[builtins.str]:
            '''Criteria for selecting which resources the rule applies to, such as resource tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-selectioncriteria
            '''
            result = self._values.get("selection_criteria")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def telemetry_source_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The specific telemetry source types to configure for the resource, such as VPC_FLOW_LOGS or EKS_AUDIT_LOGS.

            TelemetrySourceTypes must be correlated with the specific resource type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-telemetryrule.html#cfn-observabilityadmin-telemetryrule-telemetryrule-telemetrysourcetypes
            '''
            result = self._values.get("telemetry_source_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TelemetryRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "log_format": "logFormat",
            "max_aggregation_interval": "maxAggregationInterval",
            "traffic_type": "trafficType",
        },
    )
    class VPCFlowLogParametersProperty:
        def __init__(
            self,
            *,
            log_format: typing.Optional[builtins.str] = None,
            max_aggregation_interval: typing.Optional[jsii.Number] = None,
            traffic_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration parameters specific to VPC Flow Logs.

            :param log_format: The format in which VPC Flow Log entries should be logged.
            :param max_aggregation_interval: The maximum interval in seconds between the capture of flow log records.
            :param traffic_type: The type of traffic to log (ACCEPT, REJECT, or ALL).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                v_pCFlow_log_parameters_property = observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                    log_format="logFormat",
                    max_aggregation_interval=123,
                    traffic_type="trafficType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb426e63d8ddff6bc9e58865c89c023dbf7b61ef2e21b2f9ff902df9db830681)
                check_type(argname="argument log_format", value=log_format, expected_type=type_hints["log_format"])
                check_type(argname="argument max_aggregation_interval", value=max_aggregation_interval, expected_type=type_hints["max_aggregation_interval"])
                check_type(argname="argument traffic_type", value=traffic_type, expected_type=type_hints["traffic_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if log_format is not None:
                self._values["log_format"] = log_format
            if max_aggregation_interval is not None:
                self._values["max_aggregation_interval"] = max_aggregation_interval
            if traffic_type is not None:
                self._values["traffic_type"] = traffic_type

        @builtins.property
        def log_format(self) -> typing.Optional[builtins.str]:
            '''The format in which VPC Flow Log entries should be logged.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-logformat
            '''
            result = self._values.get("log_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_aggregation_interval(self) -> typing.Optional[jsii.Number]:
            '''The maximum interval in seconds between the capture of flow log records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-maxaggregationinterval
            '''
            result = self._values.get("max_aggregation_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def traffic_type(self) -> typing.Optional[builtins.str]:
            '''The type of traffic to log (ACCEPT, REJECT, or ALL).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-vpcflowlogparameters.html#cfn-observabilityadmin-telemetryrule-vpcflowlogparameters-traffictype
            '''
            result = self._values.get("traffic_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCFlowLogParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRule.WAFLoggingParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "logging_filter": "loggingFilter",
            "log_type": "logType",
            "redacted_fields": "redactedFields",
        },
    )
    class WAFLoggingParametersProperty:
        def __init__(
            self,
            *,
            logging_filter: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.LoggingFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            log_type: typing.Optional[builtins.str] = None,
            redacted_fields: typing.Optional[typing.Union["_IResolvable_da3f097b", typing.Sequence[typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.FieldToMatchProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Configuration parameters for WAF logging, including redacted fields and logging filters.

            :param logging_filter: A filter configuration that determines which WAF log records to include or exclude.
            :param log_type: The type of WAF logs to collect (currently supports WAF_LOGS).
            :param redacted_fields: The fields to redact from WAF logs to protect sensitive information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-wafloggingparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_observabilityadmin as observabilityadmin
                
                w_aFLogging_parameters_property = observabilityadmin.CfnTelemetryRule.WAFLoggingParametersProperty(
                    logging_filter=observabilityadmin.CfnTelemetryRule.LoggingFilterProperty(
                        default_behavior="defaultBehavior",
                        filters=[observabilityadmin.CfnTelemetryRule.FilterProperty(
                            behavior="behavior",
                            conditions=[observabilityadmin.CfnTelemetryRule.ConditionProperty(
                                action_condition=observabilityadmin.CfnTelemetryRule.ActionConditionProperty(
                                    action="action"
                                ),
                                label_name_condition=observabilityadmin.CfnTelemetryRule.LabelNameConditionProperty(
                                    label_name="labelName"
                                )
                            )],
                            requirement="requirement"
                        )]
                    ),
                    log_type="logType",
                    redacted_fields=[observabilityadmin.CfnTelemetryRule.FieldToMatchProperty(
                        method="method",
                        query_string="queryString",
                        single_header=observabilityadmin.CfnTelemetryRule.SingleHeaderProperty(
                            name="name"
                        ),
                        uri_path="uriPath"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe797c9dc099285e31e1c64db2dde79d74254b16b68898be88f378c3f0acc959)
                check_type(argname="argument logging_filter", value=logging_filter, expected_type=type_hints["logging_filter"])
                check_type(argname="argument log_type", value=log_type, expected_type=type_hints["log_type"])
                check_type(argname="argument redacted_fields", value=redacted_fields, expected_type=type_hints["redacted_fields"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if logging_filter is not None:
                self._values["logging_filter"] = logging_filter
            if log_type is not None:
                self._values["log_type"] = log_type
            if redacted_fields is not None:
                self._values["redacted_fields"] = redacted_fields

        @builtins.property
        def logging_filter(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.LoggingFilterProperty"]]:
            '''A filter configuration that determines which WAF log records to include or exclude.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-wafloggingparameters.html#cfn-observabilityadmin-telemetryrule-wafloggingparameters-loggingfilter
            '''
            result = self._values.get("logging_filter")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.LoggingFilterProperty"]], result)

        @builtins.property
        def log_type(self) -> typing.Optional[builtins.str]:
            '''The type of WAF logs to collect (currently supports WAF_LOGS).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-wafloggingparameters.html#cfn-observabilityadmin-telemetryrule-wafloggingparameters-logtype
            '''
            result = self._values.get("log_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def redacted_fields(
            self,
        ) -> typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.FieldToMatchProperty"]]]]:
            '''The fields to redact from WAF logs to protect sensitive information.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-observabilityadmin-telemetryrule-wafloggingparameters.html#cfn-observabilityadmin-telemetryrule-wafloggingparameters-redactedfields
            '''
            result = self._values.get("redacted_fields")
            return typing.cast(typing.Optional[typing.Union["_IResolvable_da3f097b", typing.List[typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.FieldToMatchProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WAFLoggingParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_observabilityadmin.CfnTelemetryRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_name": "ruleName", "tags": "tags"},
)
class CfnTelemetryRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union["_IResolvable_da3f097b", typing.Union["CfnTelemetryRule.TelemetryRuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union["_CfnTag_f6864754", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTelemetryRule``.

        :param rule: Retrieves the details of a specific telemetry rule in your account.
        :param rule_name: The name of the telemetry rule.
        :param tags: Lists all tags attached to the specified resource. Supports telemetry rule resources and telemetry pipeline resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html
        :exampleMetadata: fixture=_generated

        Example::

            from aws_cdk import CfnTag
            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_observabilityadmin as observabilityadmin
            
            cfn_telemetry_rule_props = observabilityadmin.CfnTelemetryRuleProps(
                rule=observabilityadmin.CfnTelemetryRule.TelemetryRuleProperty(
                    resource_type="resourceType",
                    telemetry_type="telemetryType",
            
                    # the properties below are optional
                    destination_configuration=observabilityadmin.CfnTelemetryRule.TelemetryDestinationConfigurationProperty(
                        cloudtrail_parameters=observabilityadmin.CfnTelemetryRule.CloudtrailParametersProperty(
                            advanced_event_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedEventSelectorProperty(
                                field_selectors=[observabilityadmin.CfnTelemetryRule.AdvancedFieldSelectorProperty(
                                    ends_with=["endsWith"],
                                    equal_to=["equalTo"],
                                    field="field",
                                    not_ends_with=["notEndsWith"],
                                    not_equals=["notEquals"],
                                    not_starts_with=["notStartsWith"],
                                    starts_with=["startsWith"]
                                )],
            
                                # the properties below are optional
                                name="name"
                            )]
                        ),
                        destination_pattern="destinationPattern",
                        destination_type="destinationType",
                        elb_load_balancer_logging_parameters=observabilityadmin.CfnTelemetryRule.ELBLoadBalancerLoggingParametersProperty(
                            field_delimiter="fieldDelimiter",
                            output_format="outputFormat"
                        ),
                        log_delivery_parameters=observabilityadmin.CfnTelemetryRule.LogDeliveryParametersProperty(
                            log_types=["logTypes"]
                        ),
                        retention_in_days=123,
                        vpc_flow_log_parameters=observabilityadmin.CfnTelemetryRule.VPCFlowLogParametersProperty(
                            log_format="logFormat",
                            max_aggregation_interval=123,
                            traffic_type="trafficType"
                        ),
                        waf_logging_parameters=observabilityadmin.CfnTelemetryRule.WAFLoggingParametersProperty(
                            logging_filter=observabilityadmin.CfnTelemetryRule.LoggingFilterProperty(
                                default_behavior="defaultBehavior",
                                filters=[observabilityadmin.CfnTelemetryRule.FilterProperty(
                                    behavior="behavior",
                                    conditions=[observabilityadmin.CfnTelemetryRule.ConditionProperty(
                                        action_condition=observabilityadmin.CfnTelemetryRule.ActionConditionProperty(
                                            action="action"
                                        ),
                                        label_name_condition=observabilityadmin.CfnTelemetryRule.LabelNameConditionProperty(
                                            label_name="labelName"
                                        )
                                    )],
                                    requirement="requirement"
                                )]
                            ),
                            log_type="logType",
                            redacted_fields=[observabilityadmin.CfnTelemetryRule.FieldToMatchProperty(
                                method="method",
                                query_string="queryString",
                                single_header=observabilityadmin.CfnTelemetryRule.SingleHeaderProperty(
                                    name="name"
                                ),
                                uri_path="uriPath"
                            )]
                        )
                    ),
                    selection_criteria="selectionCriteria",
                    telemetry_source_types=["telemetrySourceTypes"]
                ),
                rule_name="ruleName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7455cb845b044ed569a8ec8407abf811920062f00d1e54ad191e90dc9b7e2811)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_name", value=rule_name, expected_type=type_hints["rule_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
            "rule_name": rule_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def rule(
        self,
    ) -> typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.TelemetryRuleProperty"]:
        '''Retrieves the details of a specific telemetry rule in your account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html#cfn-observabilityadmin-telemetryrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union["_IResolvable_da3f097b", "CfnTelemetryRule.TelemetryRuleProperty"], result)

    @builtins.property
    def rule_name(self) -> builtins.str:
        '''The name of the telemetry rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html#cfn-observabilityadmin-telemetryrule-rulename
        '''
        result = self._values.get("rule_name")
        assert result is not None, "Required property 'rule_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List["_CfnTag_f6864754"]]:
        '''Lists all tags attached to the specified resource.

        Supports telemetry rule resources and telemetry pipeline resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-observabilityadmin-telemetryrule.html#cfn-observabilityadmin-telemetryrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List["_CfnTag_f6864754"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTelemetryRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnOrganizationCentralizationRule",
    "CfnOrganizationCentralizationRuleProps",
    "CfnOrganizationTelemetryRule",
    "CfnOrganizationTelemetryRuleProps",
    "CfnS3TableIntegration",
    "CfnS3TableIntegrationProps",
    "CfnTelemetryPipelines",
    "CfnTelemetryPipelinesProps",
    "CfnTelemetryRule",
    "CfnTelemetryRuleProps",
]

publication.publish()

def _typecheckingstub__18acbc8917f3c4cbc8bb06f5fae76010e41ab5f0e9b157f4c324c214a180ef2e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.CentralizationRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecabb5646d522a7c00aa40f3e19c4d2e5dccb6109cb58329723f9f47be7267d6(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02b2ea8ec552fc96b3662b368fa64eea5f82839c3bd0f1aa52bd64bc495f5341(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f130448a4f76aff49b8e31a382ea5ab14eacdf34a74afe86be23352ded6622e1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fbb5a84b6997cee28db4665d22fee83629861a1e51fe754b85b3858441e7c2d(
    value: typing.Union[_IResolvable_da3f097b, CfnOrganizationCentralizationRule.CentralizationRuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f42b1edd10be1da3c565db5f9585850487a7c51b5ad7ab0a72c1d4345b4ac7f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a58679a9a3a800195cc0ecf82553695580c2dd2061901e27320b9025cb6ed262(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48736d0ec2563919af9b82675cbe965d2288bd15210b9c8b34911e7a89ae0f47(
    *,
    region: builtins.str,
    account: typing.Optional[builtins.str] = None,
    destination_logs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.DestinationLogsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb475427ce4a2316b8478f1c58d17ddd5783412b26cdfb98819c47313aa718dc(
    *,
    destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.CentralizationRuleDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.CentralizationRuleSourceProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c4d1dff0252b97263e138c77bea2f698277762eeffd4fcf3911e496ac5762e4(
    *,
    regions: typing.Sequence[builtins.str],
    scope: typing.Optional[builtins.str] = None,
    source_logs_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.SourceLogsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dd7a39f2c94fa5f25cdcfc83cd888a8c3b22c09afa009f3ed5de76fd5befe41(
    *,
    backup_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.LogsBackupConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_group_name_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.LogGroupNameConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    logs_encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.LogsEncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc628f661292ed8b216472c835d47a09fd581394061ab648aa685a81bcef75c8(
    *,
    log_group_name_pattern: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d26acca25f06381fb096b21a6f3791d0ef735549ac7bae5795f4e646184d86(
    *,
    region: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d66f88a29d04606b9d6748d2a92fb0d7bf4a500a64fceff8556e1ac2275828e(
    *,
    encryption_strategy: builtins.str,
    encryption_conflict_resolution_strategy: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a12247cb1287e19ec3a764cc738d756d26c889450a5b771811f8378a2b5d6c(
    *,
    encrypted_log_group_strategy: builtins.str,
    log_group_selection_criteria: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00d0ecee2cd9ac728ca3e321203ce2e611e56b0b2d415ba2673a50599e4512cd(
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationCentralizationRule.CentralizationRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a67d6a9dd82924a413b7d3435faeb8efa735048df0244b926e672def8c2d5f75(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7ca13b7cccda36c5b43cead9ffee16b45fa649b63750b67cfc542107deb6702(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb893813673a29ee1f384593916d34bdcc440b816dfc54ad27097692c5a64e9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c809c768027da00df4018694393faf5d77af9754b12923bf684ada119faecfc7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97cf84910a3c46b94c3e90ddf73c07b304a029e413bebd1b7c5e7b2bbe5cd411(
    value: typing.Union[_IResolvable_da3f097b, CfnOrganizationTelemetryRule.TelemetryRuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84099afcf940dd46614099ecc03e181396a6d202813d1517bd79414c5aa2f5ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d494e45ec3f03fbc2168c2e374f689615e98524c832aa6247ad243fabe01ffe7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b6b5585476ea575f5f355362e763f68412449ff22910a34eb3e7d80ceec7283(
    *,
    action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a8d791206424757183daedc38dee2af439aaf16a9fafc6af1201043adf7c3de(
    *,
    field_selectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.AdvancedFieldSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a750f509bbf975a3106e6633766b065ca671d998289bcba4ef16d2b9c83abab(
    *,
    ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
    field: typing.Optional[builtins.str] = None,
    not_ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6841a259b98239da9d79c07870bb6bcff9cbcac2a6f70f508616cce4cc82daa9(
    *,
    advanced_event_selectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.AdvancedEventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__420adeb7464d458e2857bc92abac2bedbf48d00e02f72464d36b05d3d8e2eb70(
    *,
    action_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.ActionConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    label_name_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.LabelNameConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b56ef10916fda37562f5a73d7cca6d1cfc6daec018d9ce8b63aaaff139c12895(
    *,
    field_delimiter: typing.Optional[builtins.str] = None,
    output_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__131a6841535b3ea1a525c04136403368fbb8448ee443a93a42242015401ac5dc(
    *,
    method: typing.Optional[builtins.str] = None,
    query_string: typing.Optional[builtins.str] = None,
    single_header: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.SingleHeaderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    uri_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74122cf2cd3a4de6fe59f3acfea6ea55d497184459a9d73d02526969478c6d70(
    *,
    behavior: typing.Optional[builtins.str] = None,
    conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.ConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    requirement: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e1cb85478af2a0db2ff4e2c1201fbe45401829631a994c0a6593451b59b5c80(
    *,
    label_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a6ecd2133b0bae7130114f115e61eb5e98343b8c136ecade19918d01b854904(
    *,
    default_behavior: typing.Optional[builtins.str] = None,
    filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.FilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32eaac1f45f8f639979d1f81a515778d4b95e9e651411f27f6a838b958d2ac3d(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36b4168c57b4555036ca598e8299a36985c9aab7a1eb6b84357df4454b340171(
    *,
    cloudtrail_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.CloudtrailParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    destination_pattern: typing.Optional[builtins.str] = None,
    destination_type: typing.Optional[builtins.str] = None,
    elb_load_balancer_logging_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.ELBLoadBalancerLoggingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    vpc_flow_log_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.VPCFlowLogParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    waf_logging_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.WAFLoggingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8febf24ebcbc00029972152d874df5e847a9f5cd45e05abb26e69f7a2cabc5bf(
    *,
    resource_type: builtins.str,
    telemetry_type: builtins.str,
    destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.TelemetryDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scope: typing.Optional[builtins.str] = None,
    selection_criteria: typing.Optional[builtins.str] = None,
    telemetry_source_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945b01222f6573dfd9bd365335b34de4d056db844b2fe9ffa6c9d40371eaff6e(
    *,
    log_format: typing.Optional[builtins.str] = None,
    max_aggregation_interval: typing.Optional[jsii.Number] = None,
    traffic_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__170d7139909f3f9728055df526e99eee9f0d1bbb7e2ffd7d9636e18c28848f0b(
    *,
    logging_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.LoggingFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_type: typing.Optional[builtins.str] = None,
    redacted_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.FieldToMatchProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45c94381428dd096d5bd5b31c1a78b0ec6c66b125c46a889f389e957dbf9f76b(
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnOrganizationTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e613f2b4c0bd0fe05183ae10e1072f669e68ecf8da1370aa25246cc8572b5e2f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    encryption: typing.Union[_IResolvable_da3f097b, typing.Union[CfnS3TableIntegration.EncryptionConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    log_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnS3TableIntegration.LogSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de0e786e830272a9cd43196ab4d988d850d39e09ac6deece3f6f3fc217267fc9(
    resource: _IS3TableIntegrationRef_0d27be71,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f060eb6521743a2fee36ac86bf0a3ec88f3659183452e5bc1ed20405e82d070(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db8d8b6fa8e1af24ec5902bc335bccad34c4c808d7ce93702198c675306c9490(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1915c865e4c74d8cf78a70268ef686e156945564d8c734eae1c805be7b1dcca(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf60cf475e52ec2455d6bb2610fe113c13df025036010f81e85a0d6a8a9568df(
    value: typing.Union[_IResolvable_da3f097b, CfnS3TableIntegration.EncryptionConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9563b76b32841a10a2062025b5dc3f2c3e65ffaf4e26519dd2e2939d724590b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca350dbe6386e8726b94ecfb8ecdcec3eadaea66fddf8e9ace5f7364958e217a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnS3TableIntegration.LogSourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8d9af1b518d9d7c5df43afc2d1661b0c7f8c2f6e31ea999f0f18044da32c60a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08cffef92f415425c011859c528aa6887003c25fca6427c36632c3e7f6effd76(
    *,
    sse_algorithm: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b66342dc0f7b0ba6d95ddc850e30226765bf042a0bf8a8471a04ad534920ea96(
    *,
    name: builtins.str,
    type: builtins.str,
    identifier: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__595e24a51b54bcce8c75e459e7e3581741d212973d102f13a7b1f8c21e64c7c6(
    *,
    encryption: typing.Union[_IResolvable_da3f097b, typing.Union[CfnS3TableIntegration.EncryptionConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    role_arn: builtins.str,
    log_sources: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnS3TableIntegration.LogSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f612352088aa915560d9c73b4fc630a10a3f3706939f1998202a1ad9dcaa9b2e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2734bd526aa4a19a2468ecd3f94c2f174bcdef0f646010e77d960f2aee980e1c(
    resource: _ITelemetryPipelinesRef_a5d8576e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13e724affcae9c67447d564bf1f406f85952620e01688ec9374c2e240d21ce00(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b7b0d3ae71540f27e1eef685497e34fb8fa229fd184e2f79e2601bd982007f4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ef1a0ed45cdf50ec0b96e10e26fffd4fa055a06795675917f6bf670790ac26d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0ea345d0670a42e8cd1fa5ccce024ab9a78b08ece4b335f587f586aa3446f66(
    value: typing.Union[_IResolvable_da3f097b, CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05b27d7721bf16162cc6c8d3ddffb2e5ab5b3582d0e2acfae8e22f54d86e7f56(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__481c302f9e6ff7c9111f4e3c3983ac44f104411494a50dcd0e8fbb96b18d733d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bb4b947dbc757a669388b15cdcb2ebb178c00d3708260a46724a325f1525920(
    *,
    body: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__521e5519bd3500dba951faf81c8c8ad63ae7bedb065325d66cf2300ff66789f8(
    *,
    arn: typing.Optional[builtins.str] = None,
    configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    created_time_stamp: typing.Optional[jsii.Number] = None,
    last_update_time_stamp: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    status_reason: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryPipelines.TelemetryPipelineStatusReasonProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ac245ad25f1a31f025f3074cc38689cbc6eb0da13fbd131c2413958c035568e(
    *,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5369e75735c42fa71fba44fea4843e2a7be2cb41f104bf1b5e5c9c21b640b915(
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryPipelines.TelemetryPipelineConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cb28d06ef60815f8488b771b64aca8e3671a315a3f6676ad80a414dcd296224(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15d46db6be93b2acc11cf6216144d83efa879d1fceb7052f192fd6a434af63b9(
    x: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c971c1c4e8e03d4140674a22f18490c0a14f143dab5c9b15a801d0e69e908b92(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adf48e055c256d6f5cb987ba3921807e211a303c3d38be6a02b6932f52a739fe(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__253115d76ca17e48e13df2aa679666bb12581680b457a45a7743f6a80d6dbfa1(
    value: typing.Union[_IResolvable_da3f097b, CfnTelemetryRule.TelemetryRuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c59aae5f9c690d805a52b4e5949569db025239eb21172f781673428651a87d80(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec4f4991901119d1b8ec2bf2b1d23daff9627e5f20b555f27ec8fd5bc58890b7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50557e914800706360d6a6d0fd3fa96ca54609369f32f1412635fd95de5c04fd(
    *,
    action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34e91e8b7bfb8885a361b9a019e847677797f97575e5c9e1c82c3ee8cb4fe68d(
    *,
    field_selectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.AdvancedFieldSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5faffd9294bd925fc19af734c530e3ea1568e156d6666558fb1e9a63ed9e319b(
    *,
    ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    equal_to: typing.Optional[typing.Sequence[builtins.str]] = None,
    field: typing.Optional[builtins.str] = None,
    not_ends_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_equals: typing.Optional[typing.Sequence[builtins.str]] = None,
    not_starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
    starts_with: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__62ff49994749a104a46f12763305b7e1872bf64c00794dcd8ff06fff28ff5016(
    *,
    advanced_event_selectors: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.AdvancedEventSelectorProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c897e4ce5b2e29b5a786649170e489dde012e76b9528806d6868b20b58fbe044(
    *,
    action_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.ActionConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    label_name_condition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.LabelNameConditionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03a18a983d83cbe92b3f9982fcddc595f10337f8733ae0d29f3010716bab954c(
    *,
    field_delimiter: typing.Optional[builtins.str] = None,
    output_format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3976476c0a0e097f45e5560dcbf47e3f22424da7ff8b7eeb81ddaa36b8424717(
    *,
    method: typing.Optional[builtins.str] = None,
    query_string: typing.Optional[builtins.str] = None,
    single_header: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.SingleHeaderProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    uri_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a49dafe52d9710a05d5e9354c3584d91d95a89fb01156df326d91c12f8e7aa(
    *,
    behavior: typing.Optional[builtins.str] = None,
    conditions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.ConditionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    requirement: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff01fa602d174a91ced1cb282fb0eb60b7d5109e9b2f83417d27bea0261462a3(
    *,
    label_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7324b57f326b27aa49521b6ab51d6cfe3f1c8e68c78bb51ad7e061edc92c0a8d(
    *,
    log_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec5b265219a09ae971954fc5efb55eeca562e31b03200d5a454f07b91730c0c0(
    *,
    default_behavior: typing.Optional[builtins.str] = None,
    filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.FilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52016d9c5461305a90cf833adbbbe8dfceb9080f12605147dcc5869d62c25ad4(
    *,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01ec7a824466c4f6343ec939656046b6c12a168edd9bbf6ebca41e4b5d1554d5(
    *,
    cloudtrail_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.CloudtrailParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    destination_pattern: typing.Optional[builtins.str] = None,
    destination_type: typing.Optional[builtins.str] = None,
    elb_load_balancer_logging_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.ELBLoadBalancerLoggingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_delivery_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.LogDeliveryParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    retention_in_days: typing.Optional[jsii.Number] = None,
    vpc_flow_log_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.VPCFlowLogParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    waf_logging_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.WAFLoggingParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d1c19a045d927560ccf78552c0595fbd7db1322a4e66f60e4d9cb5393b81c3(
    *,
    resource_type: builtins.str,
    telemetry_type: builtins.str,
    destination_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.TelemetryDestinationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    selection_criteria: typing.Optional[builtins.str] = None,
    telemetry_source_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb426e63d8ddff6bc9e58865c89c023dbf7b61ef2e21b2f9ff902df9db830681(
    *,
    log_format: typing.Optional[builtins.str] = None,
    max_aggregation_interval: typing.Optional[jsii.Number] = None,
    traffic_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe797c9dc099285e31e1c64db2dde79d74254b16b68898be88f378c3f0acc959(
    *,
    logging_filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.LoggingFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    log_type: typing.Optional[builtins.str] = None,
    redacted_fields: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.FieldToMatchProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7455cb845b044ed569a8ec8407abf811920062f00d1e54ad191e90dc9b7e2811(
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTelemetryRule.TelemetryRuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
